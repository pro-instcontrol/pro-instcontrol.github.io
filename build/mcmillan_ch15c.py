# -*- coding: utf-8 -*-
"""Chapter 15, module C - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 468-473 (PDF pp. 489-494).

Covers the tail of 15.5.3, headings 15.5.4, 15.5.5, 15.6 and
15.6.1-15.6.3, and the unnumbered bold protection-concept subheadings
(oil-immersed, pressurized, powder-filled, flameproof, increased
safety, intrinsic safety, encapsulation and type 'N'), ending with the
last paragraph before the printed 'References' heading. The chapter
shell owns the chapter h2, the ten printed references, the glossary,
the source-quirk note and the copyright; this module emits no figures,
tables, displayed equations or reference list.

Printed quirks are kept in the English text and bilingual notes are
added for every divergence flagged in survey C, including the five
cross-page continuations. The Vietnamese follows the intended meaning.
This is an unofficial study translation. The source PDF is not
republished.
"""
from mcmillan_common import h3, h4, p, note, ul, ol


def body_vi():
    b = []

    # C1 - tail of a paragraph begun on printed p.467 (raw 20072-20077).
    b.append(p("Thuật ngữ 'vận hành từ xa' được dùng để chỉ thiết bị đóng "
               "cắt, vì thiết bị đóng cắt vận hành tại chỗ luôn được giả "
               "định là có khóa liên động cơ khí để ngăn việc mở vỏ bọc, "
               "trừ khi thiết bị đóng cắt ở vị trí đã cô lập. Trong trường "
               "hợp hiếm hoi là không như vậy, thì các yêu cầu về khóa "
               "liên động hoặc cảnh báo cũng áp dụng cho thiết bị đóng cắt "
               "vận hành tại chỗ."))
    b.append(note("<b>Lưu ý về ranh giới trang giữa các trang in 467 và "
                  "468.</b> Đoạn kết thúc trang in 467 bằng 'The term "
                  "‘remotely' và tiếp tục đầu trang in 468 bằng "
                  "'operated’ is used in relation to switchgear ...'. Hai "
                  "nửa được gộp thành một đoạn liên tục; bản tiếng Anh "
                  "giữ nguyên chỗ bắt đầu giữa câu của bản in."))

    # C2 (printed p.468 / PDF p.489, raw 20078-20081).
    b.append(p("Dao cắt (cầu dao cách ly) là một vấn đề đặc biệt vì chúng "
               "là thiết bị 'ngắt không tải' và không được thiết kế để "
               "vận hành khi có tải. Vì vậy, cần lắp khóa liên động ngăn "
               "không cho chúng vận hành khi có tải, hoặc phải đưa ra "
               "cảnh báo cụ thể chống lại hành động như vậy."))
    b.append(note("<b>Lưu ý về dấu ngoặc kép trong '’off load’'.</b> Cả dấu "
                  "mở lẫn dấu đóng trong bản in và lớp OCR đều là dấu "
                  "ngoặc đơn cong bên phải; bản tiếng Anh giữ nguyên "
                  "cách viết này."))

    # C3 (printed p.468 / PDF p.489, raw 20082-20086).
    b.append(p("Thiết bị khóa liên động được dùng trong bất kỳ trường hợp "
               "nào phải sao cho không thể dễ dàng bị phá vỡ bằng các dụng "
               "cụ như tuốc-nơ-vít hoặc kìm mà nhân viên thường mang theo. "
               "Mục tiêu của việc này là giảm thiểu rủi ro do sai sót và "
               "đây là yêu cầu tương tự như yêu cầu áp dụng cho khóa liên "
               "động của thiết bị dùng trong môi trường có nguy cơ do khí "
               "và hơi."))

    # C4 - heading 15.5.4 (printed p.468 / PDF p.489).
    b.append(h3("15.5.4 Phích cắm và ổ cắm", "15.5.4 Plugs and sockets"))

    # C5 (printed p.468 / PDF p.489, raw 20088-20094).
    b.append(p("Cũng như đối với thiết bị dùng trong môi trường có nguy cơ "
               "do khí và hơi, phích cắm và ổ cắm cần được khóa liên động "
               "để ngăn việc tách rời khi đang có điện, hoặc nếu không có "
               "khóa liên động, phải được nhận diện bằng cảnh báo là "
               "những bộ phận không được tách rời như vậy. Phần cố định "
               "của phích cắm và ổ cắm (phần tạo thành một bộ phận của "
               "thiết bị) cũng được yêu cầu duy trì xếp hạng IP của vỏ "
               "bọc khi phần di động không có mặt. Một lần nữa, các thiết "
               "bị khóa liên động, nếu được lắp, phải vận hành được khi "
               "có tải và không thể bị phá vỡ bằng các dụng cụ thường "
               "được mang theo."))

    # C6 - heading 15.5.5 (printed p.468 / PDF p.489).
    b.append(h3("15.5.5 Đèn và thiết bị tương tự",
                "15.5.5 Luminaires and similar apparatus"))

    # C7 (printed p.468 / PDF p.489, raw 20096-20101).
    b.append(p("Thiết bị như đèn, mà vỏ bọc được mở dễ dàng hơn so với "
               "các thiết bị khác vì nhu cầu thay bóng đèn, v.v., cũng "
               "nên có nhãn cảnh báo không được mở khi đang có điện, trừ "
               "khi chúng cũng được khóa liên động tương tự. Điều này là "
               "cần thiết vì trong điều kiện công nghiệp tiêu chuẩn, việc "
               "thực hiện các thao tác như thay bóng đèn khi đang có điện "
               "là bình thường, và điều đó không được phép xảy ra ở các "
               "khu vực nguy hiểm."))

    # C8 - heading 15.6 (printed p.468 / PDF p.489, raw 20102-20103).
    b.append(h3("15.6 Thiết bị phù hợp với các khái niệm bảo vệ thích hợp "
                "cho nguy cơ do khí, hơi và sương mù",
                "15.6 Apparatus conforming to the protection concepts "
                "appropriate to gas, vapour and mist risks"))

    # C9 + C10 (printed pp.468-469 / PDF pp.489-490, raw 20104-20120;
    # one continuous paragraph split by the page break).
    b.append(p("Có rất nhiều thiết bị được thiết kế và thường được chứng "
               "nhận/phê duyệt để vận hành trong khí quyển nổ của khí, hơi "
               "hoặc sương mù, và không khí. Chúng phải tuân theo các yêu "
               "cầu kết cấu chi tiết không khác biệt hay kém hơn so với "
               "các yêu cầu đối với thiết bị dùng trong khí quyển nổ của "
               "bụi và không khí. Việc chứng nhận kết cấu của thiết bị cho "
               "nguy cơ do khí/hơi/sương mù và không khí được thực hiện "
               "bởi bên thứ ba, mang lại mức độ tin cậy cao về kết cấu của "
               "thiết bị. Thêm vào đó, nhiều khu vực nguy hiểm được tạo ra "
               "bởi cả nguy cơ bụi/không khí lẫn nguy cơ "
               "khí/hơi/sương mù/không khí, đòi hỏi thiết bị phải phù hợp "
               "với các tình huống vận hành, vì ngay cả khi thiết bị có thể "
               "không gây cháy hỗn hợp bụi/không khí, nó vẫn có thể gây "
               "cháy hỗn hợp khí/không khí, và bản thân hỗn hợp này lại có "
               "thể trở thành nguồn gây cháy của hỗn hợp bụi/không khí. Vì "
               "các lý do trên (và cũng vì tính kinh tế trong thiết kế và "
               "chế tạo), có lợi khi dùng một loại thiết bị cho cả hai nguy "
               "cơ, dù chúng xuất hiện cùng nhau hay riêng biệt. Vì lý do "
               "này, người ta đã xem xét sự phù hợp của thiết bị được chế "
               "tạo theo dải Tiêu chuẩn BS/EN 500 liên quan đến BS 6941¹⁰ "
               "để dùng trong nguy cơ do bụi, với các kết quả sau."))
    b.append(note("<b>Lưu ý về các chỗ gộp từ khi xuống dòng.</b> Lớp OCR "
                  "tách 'certified/approved' thành 'certi-fied/approved' và "
                  "'consideration' thành 'considera-tion'; trang in cho "
                  "thấy các từ bình thường. Các từ được gộp lại ở đây."))
    b.append(note("<b>Lưu ý về ranh giới trang giữa các trang in 468 và "
                  "469.</b> Đoạn kết thúc trang in 468 bằng '...both "
                  "dust/air and gas/vapour/mist/air' và tiếp tục đầu trang "
                  "in 469 bằng 'risks requiring apparatus to be suitable "
                  "for operational situations ...'. Hai nửa được gộp "
                  "thành một đoạn liên tục."))
    b.append(note("<b>Lưu ý về chỉ số ghi chú 'BS 6941¹⁰'.</b> Trang in cho "
                  "thấy chỉ số ¹⁰ ở dạng mũ sau 'BS 6941'; lớp OCR làm "
                  "phẳng chỉ số này thành một dấu ngoặc kép thẳng. Chỉ số "
                  "mũ được giữ nguyên."))

    # C11 - heading 15.6.1 (printed p.469 / PDF p.490).
    b.append(h3("15.6.1 Đánh lửa do tia lửa", "15.6.1 Spark ignition"))

    # C12 (printed p.469 / PDF p.490, raw 20122-20130).
    b.append(p("Thiết bị được dùng trong khí quyển nổ của khí, hơi hoặc "
               "sương mù, và không khí, và trong đó phát sinh tia lửa trong "
               "điều kiện vận hành bình thường hoặc điều kiện sự cố được "
               "công nhận, được yêu cầu phải bảo vệ chống lại tia lửa bằng "
               "các kỹ thuật như an toàn nội tại (Chương 13), vỏ bọc chống "
               "cháy nổ (Chương 10) hoặc dùng các kỹ thuật không gây cháy "
               "(Chương 14). Điều này là vì nói chung không thể loại trừ "
               "hỗn hợp khí/hơi/sương mù và không khí ra khỏi vỏ bọc. Tuy "
               "nhiên, trong trường hợp hỗn hợp bụi/không khí thì có thể "
               "làm được điều đó, và do đó, miễn là vỏ bọc của thiết bị "
               "đáp ứng đủ yêu cầu, tia lửa trở thành vấn đề ít nghiêm "
               "trọng hơn nói chung đối với bụi."))

    # C13 - heading 15.6.2 (printed p.469 / PDF p.490).
    b.append(h3("15.6.2 Đánh lửa do bề mặt nóng",
                "15.6.2 Hot surface ignition"))

    # C14 (printed p.469 / PDF p.490, raw 20132-20138).
    b.append(p("Việc phân loại nhiệt độ bề mặt được thực hiện cho nguy cơ "
               "do khí/hơi/sương mù và không khí không phù hợp ngay với "
               "các tình huống có bụi, vì nó thường bao gồm nhiệt độ bên "
               "trong thiết bị mà hỗn hợp khí/hơi/sương mù và không khí "
               "tiếp cận được, nhưng bụi thì không tiếp cận được khi áp "
               "dụng các tiêu chí vỏ bọc để loại trừ bụi. Thêm vào đó, các "
               "hệ số dùng trong phân loại nhiệt độ bề mặt khác với các "
               "hệ số áp dụng cho nguy cơ do bụi đã được giải thích trong "
               "chương này."))

    # C15 (printed p.469 / PDF p.490, raw 20139-20146).
    b.append(p("Phương pháp đơn giản nhất để chọn thiết bị dùng cho nguy "
               "cơ do khí hoặc hơi nhằm sử dụng trong nguy cơ do bụi trên "
               "cơ sở Phân loại nhiệt độ bề mặt là dùng Bảng 15.1, nhưng "
               "cần nhận ra rằng cách này thường đưa ra giải pháp rất "
               "nặng nề vì nó xét đến nhiệt độ bên trong. Ngoài ra, thiết "
               "bị có thể được thử nghiệm để xác định nhiệt độ bề mặt "
               "bên ngoài cực đại và dùng giá trị thu được cho mục đích "
               "lựa chọn. Tuy nhiên, trong trường hợp sau, cần dùng hệ số "
               "an toàn 10 °C đã được giải thích trước đó trong chương "
               "này."))
    b.append(note("<b>Lưu ý về dấu cách trong '10 °C'.</b> Trang in cho "
                  "thấy một khe hở nhỏ giữa '10' và '°C'; lớp OCR viết "
                  "'10°C'. Cách đọc theo trang in được dùng."))

    # C16 - heading 15.6.3 (printed p.469 / PDF p.490, raw 20147-20148).
    b.append(h3("15.6.3 Cơ sở lựa chọn thiết bị có khái niệm bảo vệ phù "
                "hợp với nguy cơ do khí/hơi/sương mù và không khí",
                "15.6.3 Basis of selection of apparatus with protection "
                "concepts appropriate to gas/vapour/mist and air risks"))

    # C17 + C18 (printed pp.469-470 / PDF pp.490-491, raw 20149-20155).
    b.append(p("Như đã chỉ ra, yêu cầu cơ bản đối với thiết bị dùng trong "
               "nguy cơ do bụi trong nhiều trường hợp gần như giống với "
               "yêu cầu đối với thiết bị dùng cho nguy cơ do khí và hơi. "
               "Điều này có nghĩa là, với rất ít hoặc không cần sửa đổi, "
               "có thể chứng minh rằng thiết bị như vậy phù hợp với nguy "
               "cơ do bụi, miễn là đã thực hiện lựa chọn theo phân loại "
               "nhiệt độ như đã mô tả ở trên."))
    b.append(note("<b>Lưu ý về ranh giới trang giữa các trang in 469 và "
                  "470.</b> Đoạn kết thúc trang in 469 bằng '...those "
                  "required for apparatus for' và tiếp tục đầu trang in "
                  "470 bằng 'gas and vapour risks. This means that ...'. "
                  "Hai nửa được gộp thành một đoạn liên tục."))

    # C19 - unnumbered subheading (printed p.470 / PDF p.491, raw 20156).
    b.append(h4("Thiết bị ngâm dầu ‘o’ (Chương 9)",
                "Oil-immersed apparatus ‘0’ (Chapter 9)"))
    b.append(note("<b>Lưu ý về ký hiệu ‘0’ trong tiêu đề này.</b> Bản in "
                  "dùng chữ số không giữa hai dấu ngoặc kép trong 'Oil-"
                  "immersed apparatus ‘0’ (Chapter 9)'; ký hiệu bảo vệ "
                  "ngâm dầu đúng là chữ ‘o’. Bản tiếng Anh giữ chữ số như "
                  "bản in; bản tiếng Việt theo nghĩa đúng."))

    # C20 (printed p.470 / PDF p.491, raw 20157).
    b.append(p("Loại thiết bị này phù hợp trong các trường hợp sau."))

    # C21 (printed p.470 / PDF p.491, raw 20158-20162).
    b.append(p("Thứ nhất, vỏ bọc của thiết bị phải là IP5X hoặc IP6X, tùy "
               "theo Vùng sử dụng dự kiến (IP5X cho Vùng Y hoặc Vùng 22, "
               "và IP 6X cho Vùng Z hoặc Vùng 21). Dù sự thay đổi mức độ "
               "kín của vỏ bọc đối với bụi dẫn điện không phù hợp ở đây, "
               "vẫn có nguy cơ một số loại bụi làm suy giảm chất lượng "
               "dầu, và trong những trường hợp đó luôn yêu cầu IP6X."))
    b.append(note("<b>Lưu ý về dấu cách trong 'IP 6X'.</b> Trang in có dấu "
                  "cách giữa 'IP' và '6X' trong 'IP 6X for Zone Z or Zone "
                  "21' (ở những chỗ khác là 'IP6X'). Cách viết này được "
                  "giữ nguyên trong bản tiếng Anh; bản tiếng Việt dùng "
                  "nghĩa đúng."))

    # C22 (printed p.470 / PDF p.491, raw 20163-20168).
    b.append(p("Thứ hai, đối với khái niệm bảo vệ này, phân loại nhiệt độ "
               "bề mặt được thực hiện cho bề mặt của dầu, về thực tế "
               "tương đương với nhiệt độ của vỏ bọc, và không có lợi gì "
               "khi bổ sung thêm thử nghiệm nhiệt độ bề mặt. Do đó, nhiệt "
               "độ bề mặt cực đại đạt được phải là nhiệt độ cực đại được "
               "phép của cấp nhiệt độ bề mặt đã cho."))

    # C23 - unnumbered subheading (printed p.470 / PDF p.491, raw 20169).
    b.append(h4("Thiết bị áp lực ‘p’ (Chương 11)",
                "Pressurized apparatus ‘p’ (Chapter 11)"))

    # C24 (printed p.470 / PDF p.491, raw 20170).
    b.append(p("Loại thiết bị này được chấp nhận trong các trường hợp "
               "sau."))

    # C25 (printed p.470 / PDF p.491, raw 20171-20178).
    b.append(p("Thứ nhất, yêu cầu chung đối với vỏ bọc là phải đáp ứng "
               "IP6X (cho Vùng Z hoặc 21) hoặc IP5X (cho Vùng Y hoặc 22) "
               "trong trường hợp không có áp lực. Trong trường hợp này, "
               "yêu cầu IP6X trong mọi trường hợp đối với bụi dẫn điện là "
               "phù hợp vì sự xem xét được thực hiện khi không có áp lực. "
               "Ngoài ra, cần xem xét ảnh hưởng của các cửa thoát khí thải "
               "trong khu vực nguy hiểm. Những cửa này cần được tính đến "
               "trong xếp hạng IP, khác với các cửa vào khí thì không, vì "
               "chúng sẽ không tiếp xúc với môi trường có bụi."))
    b.append(note("<b>Lưu ý về cách viết 'pressurization'.</b> Bản in dùng "
                  "cách viết kiểu Mỹ 'pressurization' thay vì "
                  "'pressurisation'. Cách viết này được giữ nguyên trong "
                  "bản tiếng Anh."))

    # C26 (printed p.470 / PDF p.491, raw 20179-20183).
    b.append(p("Thứ hai, phân loại nhiệt độ bề mặt đã được thực hiện trên "
               "bề mặt ngoài của vỏ bọc, và không có lợi gì khi cố xác "
               "định nhiệt độ bề mặt bên ngoài. Do đó, nhiệt độ bề mặt "
               "được giả định là nhiệt độ cực đại được phép cho cấp nhiệt "
               "độ bề mặt đã được cấp."))

    # C27 - unnumbered subheading (printed p.470 / PDF p.491, raw 20184).
    b.append(h4("Thiết bị nhồi bột ‘q’ (Chương 9)",
                "Powder-filled apparatus ‘q’ (Chapter 9)"))

    # C28 (printed p.470 / PDF p.491, raw 20185).
    b.append(p("Loại thiết bị này được chấp nhận trong các trường hợp "
               "sau."))

    # C29 + C30 (printed pp.470-471 / PDF pp.491-492, raw 20186-20193).
    b.append(p("Thứ nhất, loại thiết bị này nên được lựa chọn trên cơ sở "
               "các tiêu chí lựa chọn IP (IP6X cho Vùng Z và 21, IP5X cho "
               "Vùng Y và 22). Tuy nhiên, một lần nữa, cần có IP6X trong "
               "mọi trường hợp mà bụi dẫn điện, vì nếu bụi lọt vào vỏ bọc "
               "và trộn với bột, nó có thể ảnh hưởng bất lợi đến hoạt "
               "động của thiết bị. Khả năng bụi phản ứng với bột là rất "
               "nhỏ vì chất sau thường là thạch anh hoặc thủy tinh."))
    b.append(note("<b>Lưu ý về ranh giới trang giữa các trang in 470 và "
                  "471.</b> Đoạn kết thúc trang in 470 bằng '...There is "
                  "little' và tiếp tục đầu trang in 471 bằng 'likelihood "
                  "of the dust reacting with the powder ...'. Hai nửa "
                  "được gộp thành một đoạn liên tục."))

    # C31 (printed p.471 / PDF p.492, raw 20194-20198).
    b.append(p("Thứ hai, phân loại nhiệt độ bề mặt đã được thực hiện trên "
               "bề mặt của bột, về thực tế chính là nhiệt độ của vỏ bọc, "
               "do đó không có lợi gì khi đo nhiệt độ vỏ bọc. Nhiệt độ bề "
               "mặt sẽ là nhiệt độ cực đại được phép theo phân loại nhiệt "
               "độ bề mặt đã được cấp."))
    b.append(note("<b>Lưu ý về dấu phẩy trong 'will, be'.</b> Bản in có "
                  "dấu phẩy sau 'will' trong câu 'The surface temperature "
                  "will, be the maximum temperature permitted ...'. Dấu "
                  "phẩy này được giữ nguyên trong bản tiếng Anh; bản "
                  "tiếng Việt theo nghĩa đúng."))

    # C32 - unnumbered subheading (printed p.471 / PDF p.492, raw 20199).
    b.append(h4("Vỏ bọc chống cháy nổ ‘d’ (Chương 10)",
                "Flameproof enclosure ‘d’ (Chapter 10)"))

    # C33 (printed p.471 / PDF p.492, raw 20200).
    b.append(p("Loại thiết bị này được chấp nhận trong các trường hợp "
               "sau."))

    # C34 (printed p.471 / PDF p.492, raw 20201-20205).
    b.append(p("Thứ nhất, việc lựa chọn thiết bị chống cháy nổ để dùng "
               "trong nguy cơ do bụi dựa trên mức độ kín của vỏ bọc. IP6X "
               "được yêu cầu cho Vùng Z và 21, IP5X cho Vùng Y và 22. Đối "
               "với bụi dẫn điện, luôn yêu cầu IP6X vì sự xâm nhập của "
               "bụi vào vỏ bọc có thể gây nổ bụi bên trong, và hiệu năng "
               "của vỏ bọc trong những trường hợp như vậy thì chưa được "
               "biết."))

    # C35 (printed p.471 / PDF p.492, raw 20206-20209).
    b.append(p("Thứ hai, phân loại nhiệt độ của vỏ bọc chống cháy nổ được "
               "thực hiện trên bề mặt ngoài của vỏ bọc và việc đo nhiệt "
               "độ vỏ bọc không mang lại lợi ích gì. Nhiệt độ bề mặt được "
               "giả định là nhiệt độ cực đại được phép theo phân loại "
               "nhiệt độ bề mặt đã được cấp."))

    # C36 - unnumbered subheading (printed p.471 / PDF p.492, raw 20210).
    b.append(h4("Thiết bị an toàn tăng cường ‘e’ (Chương 12)",
                "Increased safety apparatus ‘e’ (Chapter 12)"))

    # C37 (printed p.471 / PDF p.492, raw 20211).
    b.append(p("Loại thiết bị này được chấp nhận trong các trường hợp "
               "sau."))

    # C38 (printed p.471 / PDF p.492, raw 20212-20218).
    b.append(p("Thứ nhất, an toàn tăng cường là kỹ thuật dựa một phần vào "
               "mức độ kín của vỏ bọc và yêu cầu vỏ bọc IP54, nhờ đó thông "
               "thường có thể dùng được ở Vùng Y và 22. Việc nâng mức độ "
               "kín của vỏ bọc lên tối thiểu IP64 sẽ làm cho thiết bị phù "
               "hợp với Vùng Z và 21. Một điểm cần nhấn mạnh là an toàn "
               "tăng cường phụ thuộc đáng kể vào thiết bị bảo vệ trong "
               "nguồn cấp của nó, đặc biệt trong trường hợp máy quay. "
               "Điều này cũng đúng như vậy đối với nguy cơ do bụi và đặc "
               "biệt phải tuân thủ thời gian đó."))
    b.append(note("<b>Lưu ý về 'Zone Z an 21'.</b> Bản in ghi 'will make it "
                  "suitable for Zone Z an 21.' với 'an' (thiếu chữ 'd'). "
                  "Cách viết này được giữ nguyên trong bản tiếng Anh; bản "
                  "tiếng Việt dùng 'và'."))
    b.append(note("<b>Lưu ý về cụm 'te time'.</b> Bản in ghi 'and te time "
                  "particularly must be adhered to.' với 'te' thay vì "
                  "'the'. Cách viết này được giữ nguyên trong bản tiếng "
                  "Anh; bản tiếng Việt theo nghĩa đúng."))

    # C39 (printed p.471 / PDF p.492, raw 20219-20225).
    b.append(p("Một điểm quan trọng là phân loại nhiệt độ dựa trên bộ phận "
               "nóng nhất của thiết bị, dù bên trong hay bên ngoài vỏ bọc. "
               "Nếu phân loại nhiệt độ của thiết bị thấy quá chặt chẽ khi "
               "dùng Bảng 15.1, thì việc đo nhiệt độ bên ngoài vỏ bọc có "
               "thể mang lại lợi ích đáng kể. Điều này thậm chí đúng đối "
               "với máy quay khi máy nhạy với rô-to (tức là nhiệt độ "
               "rô-to quyết định phân loại nhiệt độ bề mặt)."))
    b.append(note("<b>Lưu ý về '(i.e.,'.</b> Trang in cho thấy '(i.e., the "
                  "rotor temperature decides ...)' trong khi lớp OCR đọc "
                  "nhầm thành 'Le.'. Cách đọc theo trang in được dùng."))

    # C40 - unnumbered subheading (printed p.471 / PDF p.492, raw 20226).
    b.append(h4("An toàn nội tại ‘i’ (Chương 13)",
                "Intrinsic safety ‘i’ (Chapter 13)"))
    b.append(note("<b>Lưu ý về ký hiệu '‘i’' trong tiêu đề.</b> Trang in "
                  "cho thấy 'Intrinsic safety ‘i’ (Chapter 13)'; lớp OCR "
                  "làm sai ký hiệu thành '7’'. Cách đọc theo trang in được "
                  "dùng."))

    # C41 + C42 (printed pp.471-472 / PDF pp.492-493, raw 20227-20236).
    b.append(p("Thiết bị loại này được chấp nhận trong các trường hợp sau, "
               "nhưng vì an toàn nội tại không dựa vào vỏ bọc để đảm bảo "
               "an toàn nên có thể áp dụng cách tiếp cận linh hoạt hơn. "
               "Nếu thiết bị an toàn nội tại có vỏ bọc IP6X, nó phù hợp " 
               "để dùng ở Vùng Z hoặc 21, và nếu có vỏ bọc IP5X thì phù "
               "hợp cho Vùng Y hoặc 22 mà không cần xem xét thêm. Như "
               "trước đây, với cách tiếp cận này, vỏ bọc cần là IP6X ngay "
               "cả đối với Vùng Y hoặc 22 nếu bụi dẫn điện."))
    b.append(note("<b>Lưu ý về ranh giới trang giữa các trang in 471 và "
                  "472.</b> Đoạn kết thúc trang in 471 bằng '...a more "
                  "flexible approach is possible.' và tiếp tục đầu trang "
                  "in 472 bằng 'If the intrinsically safe apparatus has an "
                  "enclosure of IP6X ...'. Hai nửa được gộp thành một "
                  "đoạn liên tục."))

    # C43 (printed p.472 / PDF p.493, raw 20237-20247).
    b.append(p("Cách tiếp cận trên không tính đến sự an toàn bổ sung của "
               "an toàn nội tại, theo đó cần có sự cố thì một lắp đặt mới "
               "có khả năng gây cháy. Điều này đúng dù lắp đặt là ‘ia’ hay "
               "‘ib’. Tuy nhiên, trong trường hợp này, có nhiều lợi ích "
               "khi xem xét các mạch bên trong. Nếu vỏ bọc không đủ kín "
               "thì bụi có thể lọt vào. Ví dụ, khi bụi không dẫn điện, nó "
               "chỉ có tác dụng tạo một lớp phủ lên các linh kiện trong "
               "vỏ bọc. Điều này khó có thể làm thay đổi đáng kể phân loại "
               "nhiệt độ của thiết bị, và vì 'không có sự cố', 'có một sự "
               "cố' trong trường hợp ‘ib’ và có hai sự cố trong trường hợp "
               "‘ia’, bất kỳ tia lửa bên trong nào cũng không gây cháy, do "
               "đó thiết bị phải phù hợp cho Vùng Z."))
    b.append(note("<b>Lưu ý về dấu ngoặc kép trong '‘ia’' và '‘ib’'.</b> "
                  "Trang in dùng dấu ngoặc kép cong ở 'whether the "
                  "installation is ‘ia’ or ‘ib’' và ở '‘without fault’, "
                  "'‘with one fault’ ...'; lớp OCR dùng dấu thẳng. Cách "
                  "đọc theo trang in được dùng."))
    b.append(note("<b>Lưu ý về các lỗi OCR trong đoạn an toàn nội tại.</b> "
                  "Lớp OCR đọc nhầm 'non-conducting' thành 'non-conduding' "
                  "và 'significantly alter' thành 'sigruficantly alter'; "
                  "trang in cho thấy các từ đúng như trên. Cách đọc theo "
                  "trang in được dùng."))

    # C44 (printed p.472 / PDF p.493, raw 20248-20255).
    b.append(p("Nếu bụi dẫn điện, thì mọi bộ phận dẫn điện bên trong thiết "
               "bị có thể được giả định là nối liên kết với nhau, trừ khi "
               "chúng được phủ (sơn vecni), đóng gói hoặc cách điện. Trong "
               "những trường hợp này, thiết bị nên được đánh giá trên cơ "
               "sở đó, và nếu vẫn có thể chứng minh rằng tia lửa và bề mặt "
               "nóng không gây cháy trong điều kiện hai sự cố đối với "
               "‘ia’ với các kết nối bên trong bổ sung này, thì thiết bị "
               "vẫn phù hợp cho Vùng Z hoặc 21. Tương tự, nếu thực hiện "
               "đánh giá tương tự cho thiết bị ‘ib’, nó sẽ phù hợp cho "
               "Vùng 22 hoặc Vùng Y. Trong điều kiện ẩm độ hoặc các tình "
               "huống khác mà bụi có thể được coi là ẩm, thì bụi phải được "
               "xem là bụi dẫn điện, ngay cả khi ở trạng thái khô nó không "
               "dẫn điện."))
    b.append(note("<b>Lưu ý về dấu cách trong 'Zone Z or 21'.</b> Trang in "
                  "có dấu cách trong 'the equipment remains suitable for "
                  "Zone Z or 21'; lớp OCR viết 'ZoneZ'. Cách đọc theo "
                  "trang in được dùng."))

    # C45 (printed p.472 / PDF p.493, raw 20256-20262).
    b.append(p("Mở rộng cách tiếp cận này, một thiết bị ‘ia’ đáp ứng các "
               "yêu cầu nêu trên cho bụi không dẫn điện hoặc bụi dẫn điện "
               "(hoặc bụi ẩm), và cũng được đặt trong vỏ bọc IP6X, có mức "
               "độ bảo vệ cao hơn nhiều so với bất kỳ thiết bị nào kể "
               "trên. Thiết bị này phải có thể sử dụng an toàn trong Vùng "
               "20 mới cho loại bụi tương ứng mà hiện không có thiết bị "
               "được bảo vệ nào khác."))
    b.append(note("<b>Lưu ý về 'nonconducting' không có dấu gạch nối.</b> "
                  "Bản in ghi 'for either nonconducting or conducting (or "
                  "moist) dusts' với 'nonconducting' không có dấu gạch "
                  "nối, trong khi ở đoạn trước trên cùng trang là "
                  "'non-conducting'. Cách viết này được giữ nguyên trong "
                  "bản tiếng Anh; bản tiếng Việt dùng nghĩa đúng."))

    # C46 - unnumbered subheading (printed p.472 / PDF p.493, raw 20263).
    b.append(h4("Đóng gói ‘m’ (Chương 9)",
                "Encapsulation ‘m’ (Chapter 9)"))

    # C47 (printed p.472 / PDF p.493, raw 20264-20268).
    b.append(p("Theo định nghĩa, thiết bị đóng gói loại trừ bụi ở mức ít "
               "nhất IP6X và loại thiết bị này phù hợp cho Vùng Z và 21 "
               "(do đó cũng phù hợp cho Vùng Y và 22) mà không cần xem "
               "xét thêm. Cấp nhiệt độ bề mặt dựa trên nhiệt độ bên ngoài "
               "của vật liệu đóng gói, và nhiệt độ cực đại thường nên "
               "lấy là nhiệt độ cực đại được phép theo phân loại nhiệt độ "
               "bề mặt."))

    # C48 (printed p.472 / PDF p.493, raw 20269-20271).
    b.append(p("Tuy nhiên, cần lưu ý rằng các phương tiện kết nối của loại "
               "thiết bị này thường sử dụng các khái niệm bảo vệ thay "
               "thế, và yêu cầu của chúng cũng cần được xem xét."))

    # C49 - unnumbered subheading (printed p.473 / PDF p.494, raw 20274).
    b.append(h4("Thiết bị có loại bảo vệ ‘N’ (n) (Chương 14)",
                "Apparatus with type of protection ‘N’ (n) (Chapter 14)"))
    b.append(note("<b>Lưu ý về chữ '(n)' viết thường trong tiêu đề cuối.</b> "
                  "Bản in ghi 'Apparatus with type of protection ‘N’ (n) "
                  "(Chapter 14)': ‘N’ viết hoa trong dấu ngoặc kép nhưng "
                  "(n) viết thường trong dấu ngoặc tròn. Cách viết này "
                  "được giữ nguyên trong bản tiếng Anh."))

    # C50 - last paragraph before 'References' (printed p.473 / PDF p.494,
    # raw 20275-20280).
    b.append(p("Loại thiết bị này thường chỉ được chấp nhận ở Vùng Y hoặc "
               "22, và chỉ khi có mức độ kín vỏ bọc IP5X đối với bụi không "
               "dẫn điện và IP6X đối với bụi dẫn điện. Vì nhiệt độ bề mặt "
               "của nó có thể được xác định dựa trên các linh kiện bên "
               "trong, việc đo nhiệt độ vỏ bọc có thể hữu ích khi nhiệt "
               "độ cực đại được phép theo phân loại nhiệt độ bề mặt không "
               "được chấp nhận."))

    # Source quirks of the printed reference list, which belongs to the
    # chapter shell; recorded here rather than reproducing the list.
    b.append(note("<b>Lưu ý về 'Part 1, (1985).' trong tài liệu tham "
                  "khảo 1.</b> Dấu phẩy sau 'Part 1' có trong bản in và "
                  "được giữ nguyên trong danh sách tài liệu tham khảo do "
                  "phần chung của chương trình bày."))
    b.append(note("<b>Lưu ý về cách in '1000V ac and 1200V dc' trong tài "
                  "liệu tham khảo 6.</b> Trang in cho thấy các chữ số "
                  "trong '1000V ac and 1200V dc'; lớp OCR đọc giá trị đầu "
                  "là '1OOOV' với chữ O. Cách đọc theo trang in được giữ "
                  "nguyên."))
    b.append(note("<b>Lưu ý về chữ 'Electrical machines' viết thường "
                  "trong tài liệu tham khảo 8.</b> Tài liệu tham khảo 8 in "
                  "'General Requirements for Rotating Electrical "
                  "machines.' với 'machines' viết thường, trong khi tài "
                  "liệu tham khảo 7 lại viết 'Machines.'. Cách viết theo "
                  "bản in được giữ nguyên."))
    b.append(note("<b>Lưu ý về thứ tự hai cột của danh sách tài liệu "
                  "tham khảo trong lớp OCR.</b> Lớp OCR đặt mô tả của các "
                  "tài liệu tham khảo 3, 7, 8, 9 và 10 trước nhãn cột trái "
                  "của chúng; trang in xác lập các cặp đúng là 3 "
                  "RoSPA/ICI, 7 EN 60034, 8 BS 4999, 9 BS/EN 50014 (1993) "
                  "và 10 BS 6941 (1988). Các cặp theo trang in được dùng."))

    return "".join(b)


def body_en():
    b = []

    # C1 - tail of a paragraph begun on printed p.467 (raw 20072-20077).
    b.append(p("operated’ is used in relation to switchgear as locally "
               "operated switchgear is always assumed to have mechanical "
               "interlocking to prevent enclosure opening unless the "
               "switchgear is in the isolated position. In the unlikely "
               "event that this is not so, then the interlocking or "
               "warning requirements apply to locally operated switchgear "
               "also."))
    b.append(note("<b>Note on the page boundary between printed pp.467 and "
                  "468.</b> The paragraph ends printed p.467 with 'The "
                  "term ‘remotely' and continues at the top of printed "
                  "p.468 with 'operated’ is used in relation to switchgear "
                  "...'. The two halves are joined as one continuous "
                  "paragraph; the English text keeps the mid-sentence "
                  "opening exactly as printed."))

    # C2 (printed p.468 / PDF p.489, raw 20078-20081).
    b.append(p("Disconnectors (isolators) are a particular problem as they "
               "are ’off load’ devices and are not intended to be operated "
               "on-load. These therefore require that an interlock "
               "preventing their on-load operation is fitted, or a "
               "specific warning against such action is provided."))
    b.append(note("<b>Note on the quotation marks in '’off load’'.</b> "
                  "Both the opening and closing marks are right single "
                  "quotation marks in the print and in the OCR layer; the "
                  "English text reproduces them as printed."))

    # C3 (printed p.468 / PDF p.489, raw 20082-20086).
    b.append(p("The interlocking devices used in any circumstance must be "
               "such that they cannot be readily defeated by use of such "
               "tools as screwdrivers or pliers which are generally "
               "carried by personnel. The objective of this is to minimize "
               "the risk of mistakes and is a similar requirement to that "
               "used in the case of interlocks for apparatus for gas and "
               "vapour risks."))

    # C4 - heading 15.5.4 (printed p.468 / PDF p.489).
    b.append(h3("15.5.4 Plugs and sockets", "15.5.4 Plugs and sockets"))

    # C5 (printed p.468 / PDF p.489, raw 20088-20094).
    b.append(p("As with apparatus for gas and vapour risks, plugs and "
               "sockets need to be interlocked to prevent energized "
               "separation or, if not interlocked, to be identified by "
               "warning as items which must not be so separated. The fixed "
               "part of the plug and socket (that forming part of the "
               "apparatus) is also required to maintain the IP-rating of "
               "the enclosure when the moving part is not present. Again, "
               "the interlocking devices, if fitted, must be on-load "
               "operable and not defeatable by normally carried tools."))

    # C6 - heading 15.5.5 (printed p.468 / PDF p.489).
    b.append(h3("15.5.5 Luminaires and similar apparatus",
                "15.5.5 Luminaires and similar apparatus"))

    # C7 (printed p.468 / PDF p.489, raw 20096-20101).
    b.append(p("Apparatus, such as luminaires, where enclosures are more "
               "readily opened than is the case for other apparatus, "
               "because of the needs of relamping, etc., should also carry "
               "a label warning against opening while energized unless "
               "they are similarly interlocked. This is necessary as it is "
               "normal in standard industrial circumstances to carry out "
               "such practices as relamping live and this must not be the "
               "case in hazardous areas."))

    # C8 - heading 15.6 (printed p.468 / PDF p.489, raw 20102-20103).
    b.append(h3("15.6 Apparatus conforming to the protection concepts "
                "appropriate to gas, vapour and mist risks",
                "15.6 Apparatus conforming to the protection concepts "
                "appropriate to gas, vapour and mist risks"))

    # C9 + C10 (printed pp.468-469 / PDF pp.489-490, raw 20104-20120).
    b.append(p("There are large quantities of apparatus designed and often "
               "certified/approved for operation in explosive atmospheres "
               "of gas, vapour or mist, and air. These are subject to "
               "detailed construction requirements which are not dissimilar "
               "or inferior to those required for apparatus for use in "
               "explosive atmospheres of dust and air. Third-party "
               "certification of construction of apparatus for "
               "gas/vapour/mist air risks is provided which gives a high "
               "degree of confidence in its construction. In addition many "
               "hazardous areas are created by both dust/air and "
               "gas/vapour/mist/air risks requiring apparatus to be "
               "suitable for operational situations as, even though "
               "apparatus may be incapable of igniting a dust/air mixture, "
               "it may ignite a gas/air mixture which itself may form the "
               "source of ignition of the dust/air mixture. For the above "
               "reasons (and also economy of design and construction) it is "
               "advantageous to utilize one type of apparatus for both "
               "risks whether they occur together or separately. For this "
               "reason consideration has been given to the suitability of "
               "apparatus constructed to the BS/EN 500 range of Standards "
               "in relation to BS 6941¹⁰ for use in dust risks with the "
               "following results."))
    b.append(note("<b>Note on the line-break word joins.</b> The OCR layer "
                  "splits 'certified/approved' as 'certi-fied/approved' and "
                  "'consideration' as 'considera-tion'; the render shows "
                  "normal words. They are rejoined here."))
    b.append(note("<b>Note on the page boundary between printed pp.468 and "
                  "469.</b> The paragraph ends printed p.468 with '...both "
                  "dust/air and gas/vapour/mist/air' and continues at the "
                  "top of printed p.469 with 'risks requiring apparatus to "
                  "be suitable for operational situations ...'. The two "
                  "halves are joined as one continuous paragraph."))
    b.append(note("<b>Note on the footnote marker 'BS 6941¹⁰'.</b> The "
                  "render shows a superscript ¹⁰ after 'BS 6941'; the OCR "
                  "layer flattens it to a straight double quotation mark. "
                  "The superscript is retained."))

    # C11 - heading 15.6.1 (printed p.469 / PDF p.490).
    b.append(h3("15.6.1 Spark ignition", "15.6.1 Spark ignition"))

    # C12 (printed p.469 / PDF p.490, raw 20122-20130).
    b.append(p("Apparatus used in explosive atmospheres of gas, vapour or "
               "mist, and air and in which sparking in either normal or "
               "recognized fault conditions occurs, is required to provide "
               "protection for sparking by the use of such techniques as "
               "intrinsic safety (Chapter 13), flameproof enclosure "
               "(Chapter 10) or use of non-incendive techniques (Chapter "
               "14). This is because it is not normally possible to exclude "
               "mixtures of gas/vapour/mist and air from enclosures. In the "
               "case of dust/air mixtures it is, however, possible to do "
               "this and so, provided the enclosure of apparatus is "
               "adequate, sparking becomes less of a problem for dusts in "
               "general."))

    # C13 - heading 15.6.2 (printed p.469 / PDF p.490).
    b.append(h3("15.6.2 Hot surface ignition",
                "15.6.2 Hot surface ignition"))

    # C14 (printed p.469 / PDF p.490, raw 20132-20138).
    b.append(p("Surface temperature classification as carried out for "
               "gas/vapour/mist and air risks is not immediately "
               "appropriate to dust situations, as it often includes "
               "temperatures within the apparatus which are accessible to "
               "the gas/vapour/mist and air mixture but not to dusts where "
               "the enclosure criteria for dust exclusion are applied. In "
               "addition, the factors used in surface temperature "
               "classification are different to those applied for the dust "
               "risks already explained in this chapter."))

    # C15 (printed p.469 / PDF p.490, raw 20139-20146).
    b.append(p("The simplest method of selection of gas or vapour risk "
               "apparatus for use in dust risks on the basis of Surface "
               "Temperature Classification is to use Table 15.1, but it "
               "must be recognized that this will often give a very "
               "onerous solution because of its consideration of internal "
               "temperatures. Alternatively, the apparatus could be tested "
               "for maximum external surface temperature and the figure "
               "resulting used for selection purposes. In this latter "
               "case, however, the 10 °C safety factor explained earlier "
               "in this chapter should be used."))
    b.append(note("<b>Note on the spacing in '10 °C'.</b> The render shows "
                  "a thin gap between '10' and '°C'; the OCR layer reads "
                  "'10°C'. The render reading is used."))

    # C16 - heading 15.6.3 (printed p.469 / PDF p.490, raw 20147-20148).
    b.append(h3("15.6.3 Basis of selection of apparatus with protection "
                "concepts appropriate to gas/vapour/mist and air risks",
                "15.6.3 Basis of selection of apparatus with protection "
                "concepts appropriate to gas/vapour/mist and air risks"))

    # C17 + C18 (printed pp.469-470 / PDF pp.490-491, raw 20149-20155).
    b.append(p("As already shown, the basic requirements for apparatus for "
               "use in dust risks are almost the same in many cases to "
               "those required for apparatus for gas and vapour risks. "
               "This means that, with little or no modification, such "
               "apparatus may be shown to be suitable for dust risks "
               "subject to temperature classification selection as already "
               "described."))
    b.append(note("<b>Note on the page boundary between printed pp.469 and "
                  "470.</b> The paragraph ends printed p.469 with '...those "
                  "required for apparatus for' and continues at the top of "
                  "printed p.470 with 'gas and vapour risks. This means "
                  "that ...'. The two halves are joined as one continuous "
                  "paragraph."))

    # C19 - unnumbered subheading (printed p.470 / PDF p.491, raw 20156).
    b.append(h4("Oil-immersed apparatus ‘0’ (Chapter 9)",
                "Oil-immersed apparatus ‘0’ (Chapter 9)"))
    b.append(note("<b>Note on the symbol ‘0’ in this heading.</b> The print "
                  "shows a digit zero between the curly quotes in 'Oil-"
                  "immersed apparatus ‘0’ (Chapter 9)'; the intended "
                  "oil-immersion protection symbol is the letter ‘o’. The "
                  "printed digit is kept in the English heading; the "
                  "Vietnamese follows the intended meaning."))

    # C20 (printed p.470 / PDF p.491, raw 20157).
    b.append(p("This type of apparatus will be suitable in the following "
               "circumstances."))

    # C21 (printed p.470 / PDF p.491, raw 20158-20162).
    b.append(p("First, its enclosure must be IP5X or IP6X, depending on the "
               "intended Zone of use (IP5X for Zone Y or Zone 22, and IP "
               "6X for Zone Z or Zone 21). While the variation of enclosure "
               "integrity for conducting dusts is not appropriate here, "
               "there is a risk that some dusts may degrade the oil and in "
               "such cases IP6X is always required."))
    b.append(note("<b>Note on the spacing in 'IP 6X'.</b> The print has a "
                  "space between 'IP' and '6X' in 'IP 6X for Zone Z or "
                  "Zone 21' (elsewhere it is 'IP6X'). The printed spacing "
                  "is kept in the English text; the Vietnamese follows the "
                  "intended meaning."))

    # C22 (printed p.470 / PDF p.491, raw 20163-20168).
    b.append(p("Second, in the case of this protection concept, the surface "
               "temperature classification is for the surface of the oil, "
               "which is practically equivalent to the enclosure "
               "temperature and no advantage can be gained by added "
               "surface temperature testing. The maximum surface "
               "temperature reached should therefore be the maximum "
               "permitted for the surface temperature class given."))

    # C23 - unnumbered subheading (printed p.470 / PDF p.491, raw 20169).
    b.append(h4("Pressurized apparatus ‘p’ (Chapter 11)",
                "Pressurized apparatus ‘p’ (Chapter 11)"))

    # C24 (printed p.470 / PDF p.491, raw 20170).
    b.append(p("This type of apparatus will be acceptable in the following "
               "circumstances."))

    # C25 (printed p.470 / PDF p.491, raw 20171-20178).
    b.append(p("First, the general requirement for the enclosure is that "
               "it satisfies IP6X (for Zone Z or 21) or IP5X (for Zone Y or "
               "22) in circumstances where the pressure is not present. In "
               "this case the conducting dust requirement of IP6X in all "
               "cases is relevant as consideration is given in the absence "
               "of pressurization. Additionally it is necessary to consider "
               "the effects of outlets for exhaust of gas in the hazardous "
               "area. These need to be considered in the IP-rating, unlike "
               "the gas inlets which do not as they will not be exposed to "
               "the dust atmosphere."))
    b.append(note("<b>Note on the spelling 'pressurization'.</b> The print "
                  "uses the American spelling 'pressurization' rather than "
                  "'pressurisation'. The printed spelling is kept in the "
                  "English text."))

    # C26 (printed p.470 / PDF p.491, raw 20179-20183).
    b.append(p("Second, surface temperature classification will have been "
               "carried out on the outer surface of the enclosure and "
               "there is no advantage in attempting a determination of "
               "external surface temperature. Thus the surface temperature "
               "will be assumed to be the maximum permitted for the surface "
               "temperature class awarded."))

    # C27 - unnumbered subheading (printed p.470 / PDF p.491, raw 20184).
    b.append(h4("Powder-filled apparatus ‘q’ (Chapter 9)",
                "Powder-filled apparatus ‘q’ (Chapter 9)"))

    # C28 (printed p.470 / PDF p.491, raw 20185).
    b.append(p("This type of apparatus is acceptable in the following "
               "circumstances."))

    # C29 + C30 (printed pp.470-471 / PDF pp.491-492, raw 20186-20193).
    b.append(p("First, this type of apparatus should be selected on the "
               "basis of the IP-selection criteria (IP6X for Zone Z and 21 "
               "and IP5X for Zone Y and 22). Once again, however, it is "
               "necessary to have IP6X in all cases where the dust is "
               "conducting as, if it enters the enclosure and mixes with "
               "the powder, it could adversely affect the operation of the "
               "apparatus. There is little likelihood of the dust reacting "
               "with the powder as the latter is normally quartz or glass."))
    b.append(note("<b>Note on the page boundary between printed pp.470 and "
                  "471.</b> The paragraph ends printed p.470 with '...There "
                  "is little' and continues at the top of printed p.471 "
                  "with 'likelihood of the dust reacting with the powder "
                  "...'. The two halves are joined as one continuous "
                  "paragraph."))

    # C31 (printed p.471 / PDF p.492, raw 20194-20198).
    b.append(p("Second, surface temperature classification will have been "
               "carried out on the surface of the powder, which is "
               "effectively the enclosure temperature, and thus no "
               "advantage will accrue by measuring enclosure temperature. "
               "The surface temperature will, be the maximum temperature "
               "permitted by the surface temperature classification "
               "awarded."))
    b.append(note("<b>Note on the comma in 'will, be'.</b> The print has a "
                  "comma after 'will' in 'The surface temperature will, be "
                  "the maximum temperature permitted ...'. The comma is "
                  "kept in the English text; the Vietnamese follows the "
                  "intended meaning."))

    # C32 - unnumbered subheading (printed p.471 / PDF p.492, raw 20199).
    b.append(h4("Flameproof enclosure ‘d’ (Chapter 10)",
                "Flameproof enclosure ‘d’ (Chapter 10)"))

    # C33 (printed p.471 / PDF p.492, raw 20200).
    b.append(p("This type of apparatus is acceptable in the following "
               "circumstances."))

    # C34 (printed p.471 / PDF p.492, raw 20201-20205).
    b.append(p("First, the choice of flameproof apparatus for use in dust "
               "risks is on the basis of enclosure integrity. IP6X is "
               "required for Zone Z and 21 and IP5X for Zone Y and 22. For "
               "conducting dusts IP6X is always required as entry of dust "
               "into the enclosure could give rise to an internal dust "
               "explosion, and the performance of the enclosure in such "
               "circumstances is not known."))

    # C35 (printed p.471 / PDF p.492, raw 20206-20209).
    b.append(p("Second, temperature classification of flameproof enclosures "
               "is carried out on the enclosure outer surface and no "
               "advantage will result from measuring enclosure temperature. "
               "The surface temperature is assumed to be the maximum "
               "permitted by the surface temperature classification "
               "awarded."))

    # C36 - unnumbered subheading (printed p.471 / PDF p.492, raw 20210).
    b.append(h4("Increased safety apparatus ‘e’ (Chapter 12)",
                "Increased safety apparatus ‘e’ (Chapter 12)"))

    # C37 (printed p.471 / PDF p.492, raw 20211).
    b.append(p("This type of apparatus is acceptable in the following "
               "circumstances."))

    # C38 (printed p.471 / PDF p.492, raw 20212-20218).
    b.append(p("First, increased safety is a technique which relies in part "
               "on enclosure integrity and requires an IP54 enclosure, "
               "making it normally usable in Zone Y and 22. Increasing its "
               "enclosure integrity to a minimum of IP64 will make it "
               "suitable for Zone Z an 21. One point to be stressed is that "
               "increased safety relies to a significant extent on the "
               "protection equipment in its supply, particularly in the "
               "case of rotating machines. This is no less true in the case "
               "of dust risks and te time particularly must be adhered to."))
    b.append(note("<b>Note on 'Zone Z an 21'.</b> The print reads 'will make "
                  "it suitable for Zone Z an 21.', with 'an' in place of "
                  "'and'. The printed wording is kept in the English text; "
                  "the Vietnamese follows the intended meaning."))
    b.append(note("<b>Note on the phrase 'te time'.</b> The print reads "
                  "'and te time particularly must be adhered to.', with "
                  "'te' in place of 'the'. The printed wording is kept in "
                  "the English text; the Vietnamese follows the intended "
                  "meaning."))

    # C39 (printed p.471 / PDF p.492, raw 20219-20225).
    b.append(p("One significant point is that temperature classification is "
               "based upon the hottest part of the apparatus, be it within "
               "or outside the enclosure. If its temperature classification "
               "is found to be too restrictive using Table 15.1 then "
               "temperature measurement of the outside of the enclosure "
               "may produce significant gains. This is even true of "
               "rotating machines when the machine is rotor sensitive "
               "(i.e., the rotor temperature decides the surface "
               "temperature classification)."))
    b.append(note("<b>Note on '(i.e.,'.</b> The render shows '(i.e., the "
                  "rotor temperature decides ...)' while the OCR layer "
                  "reads 'Le.'. The render reading is used."))

    # C40 - unnumbered subheading (printed p.471 / PDF p.492, raw 20226).
    b.append(h4("Intrinsic safety ‘i’ (Chapter 13)",
                "Intrinsic safety ‘i’ (Chapter 13)"))
    b.append(note("<b>Note on the symbol '‘i’' in this heading.</b> The "
                  "render shows 'Intrinsic safety ‘i’ (Chapter 13)'; the "
                  "OCR layer garbles the symbol to '7’'. The render reading "
                  "is used."))

    # C41 + C42 (printed pp.471-472 / PDF pp.492-493, raw 20227-20236).
    b.append(p("Apparatus of this type will be acceptable in the following "
               "circumstances but as intrinsic safety does not rely on its "
               "enclosure for security then a more flexible approach is "
               "possible. If the intrinsically safe apparatus has an "
               "enclosure of IP6X it will be suitable for use in Zone Z or "
               "21 and if it has an enclosure of IP5X for Zone Y or 22 "
               "without further consideration. As before, taking this "
               "approach the enclosure will need to be IP6X even for Zones "
               "Y or 22 if the dust is conducting."))
    b.append(note("<b>Note on the page boundary between printed pp.471 and "
                  "472.</b> The paragraph ends printed p.471 with '...a "
                  "more flexible approach is possible.' and continues at "
                  "the top of printed p.472 with 'If the intrinsically safe "
                  "apparatus has an enclosure of IP6X ...'. The two halves "
                  "are joined as one continuous paragraph."))

    # C43 (printed p.472 / PDF p.493, raw 20237-20247).
    b.append(p("The above approach takes no account of the added security "
               "of intrinsic safety in that faults are required before an "
               "installation can become ignition capable. This is true "
               "whether the installation is ‘ia’ or ‘ib’. In this case, "
               "however, there is much to be gained by considering the "
               "internal circuits. If the enclosure is not of sufficient "
               "integrity then the dust can enter. When, for instance the "
               "dust is non-conducting then it will only have the effect of "
               "providing a layer over the components in the enclosure. "
               "This is unlikely to significantly alter the temperature "
               "classification of the apparatus and as, ‘without fault’, "
               "‘with one fault’ in the case of ‘ib’ and with two faults in "
               "the case of ‘ia’, any internal sparking is non-incendive "
               "the apparatus should be suitable for Zone Z."))
    b.append(note("<b>Note on the curly quotes in '‘ia’' and '‘ib’'.</b> "
                  "The render uses curly quotes in 'whether the "
                  "installation is ‘ia’ or ‘ib’' and in '‘without fault’, "
                  "'‘with one fault’ ...'; the OCR layer uses straight "
                  "quotes. The render reading is used."))
    b.append(note("<b>Note on OCR misreadings in the intrinsic-safety "
                  "paragraph.</b> The OCR layer reads 'non-conducting' as "
                  "'non-conduding' and 'significantly alter' as "
                  "'sigruficantly alter'; the render shows the words given "
                  "above. The render readings are used."))

    # C44 (printed p.472 / PDF p.493, raw 20248-20255).
    b.append(p("If the dust is conducting then any conducting parts within "
               "the apparatus may be assumed to be interconnected unless "
               "they are either coated (varnished), encapsulated or "
               "insulated. In these circumstances the apparatus should be "
               "assessed on this basis and if sparking and hot surfaces can "
               "still be shown not to be incendive in conditions of two "
               "faults for ‘ia’ with these additional internal connections, "
               "then the equipment remains suitable for Zone Z or 21. "
               "Likewise, if the same evaluation is done for ‘ib’ apparatus "
               "it will be suitable for Zone 22 or Zone Y. In conditions of "
               "humidity or other situations in which the dust can be "
               "assumed to be moist then it should be treated as conducting "
               "dust, even if when dry it is non-conducting."))
    b.append(note("<b>Note on the spacing in 'Zone Z or 21'.</b> The render "
                  "has a space in 'the equipment remains suitable for Zone "
                  "Z or 21'; the OCR layer runs it together as 'ZoneZ'. The "
                  "render reading is used."))

    # C45 (printed p.472 / PDF p.493, raw 20256-20262).
    b.append(p("Extending this approach, an item of ‘ia’ apparatus which "
               "satisfies the above requirements for either nonconducting "
               "or conducting (or moist) dusts, and which is also enclosed "
               "in an IP6X enclosure, has a much higher level of protection "
               "than any other of the foregoing equipment. This apparatus "
               "should be safely usable in the new Zone 20 for the relevant "
               "type of dust for which no other protected equipment is "
               "currently available."))
    b.append(note("<b>Note on the unhyphenated 'nonconducting'.</b> The "
                  "print reads 'for either nonconducting or conducting (or "
                  "moist) dusts', with 'nonconducting' unhyphenated, whereas "
                  "an earlier paragraph on the same page has "
                  "'non-conducting'. The printed wording is kept in the "
                  "English text; the Vietnamese follows the intended "
                  "meaning."))

    # C46 - unnumbered subheading (printed p.472 / PDF p.493, raw 20263).
    b.append(h4("Encapsulation ‘m’ (Chapter 9)",
                "Encapsulation ‘m’ (Chapter 9)"))

    # C47 (printed p.472 / PDF p.493, raw 20264-20268).
    b.append(p("Encapsulated apparatus, by definition, excludes dust to at "
               "least IP6X and such apparatus is suitable for Zone Z and 21 "
               "(and thus Zone Y and 22) without further consideration. "
               "The surface temperature class is based upon the external "
               "temperature of the encapsulant and the maximum temperature "
               "should normally be taken as the maximum permitted by the "
               "surface temperature classification."))

    # C48 (printed p.472 / PDF p.493, raw 20269-20271).
    b.append(p("It should, however, be noted that the connection facilities "
               "for such apparatus will normally utilize alternative "
               "protection concepts and their requirements should also be "
               "considered."))

    # C49 - unnumbered subheading (printed p.473 / PDF p.494, raw 20274).
    b.append(h4("Apparatus with type of protection ‘N’ (n) (Chapter 14)",
                "Apparatus with type of protection ‘N’ (n) (Chapter 14)"))
    b.append(note("<b>Note on the lowercase '(n)' in the final heading.</b> "
                  "The print reads 'Apparatus with type of protection ‘N’ "
                  "(n) (Chapter 14)': uppercase ‘N’ inside curly quotes but "
                  "a lowercase (n) in plain parentheses. The printed casing "
                  "is kept in the English text."))

    # C50 - last paragraph before 'References' (printed p.473 / PDF p.494,
    # raw 20275-20280).
    b.append(p("This type of apparatus is normally only acceptable in Zone "
               "Y or 22 and only then if it has an enclosure integrity of "
               "IP5X for non-conducting dusts and IP6X for conducting "
               "dusts. As its surface temperature may be produced on the "
               "basis of internal components, measurement of the enclosure "
               "temperature may be helpful when the maximum temperature "
               "permitted by the surface temperature classification is not "
               "acceptable."))

    # Source quirks of the printed reference list, which belongs to the
    # chapter shell; recorded here rather than reproducing the list.
    b.append(note("<b>Note on 'Part 1, (1985).' in reference 1.</b> The "
                  "comma after 'Part 1' is printed and is retained in the "
                  "reference list printed by the chapter shell."))
    b.append(note("<b>Note on the printed form '1000V ac and 1200V dc' in "
                  "reference 6.</b> The render shows digits in '1000V ac "
                  "and 1200V dc'; the OCR layer reads the first value as "
                  "'1OOOV' with the letter O. The render reading is "
                  "retained."))
    b.append(note("<b>Note on lower-case 'Electrical machines' in reference "
                  "8.</b> Reference 8 prints 'General Requirements for "
                  "Rotating Electrical machines.' with a lower-case "
                  "'machines', whereas reference 7 has 'Machines.'. The "
                  "printed casing is kept."))
    b.append(note("<b>Note on the two-column OCR order of the reference "
                  "list.</b> The OCR layer places the descriptions of "
                  "references 3, 7, 8, 9 and 10 before their left-column "
                  "labels; the render establishes the pairings 3 RoSPA/ICI, "
                  "7 EN 60034, 8 BS 4999, 9 BS/EN 50014 (1993) and 10 BS "
                  "6941 (1988). The render pairings are used."))

    return "".join(b)
