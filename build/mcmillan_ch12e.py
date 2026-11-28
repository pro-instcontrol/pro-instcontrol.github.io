# -*- coding: utf-8 -*-
"""Chapter 12, module E - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 319-326 (PDF pp. 340-347).

Covers the tail of 12.3.4, 12.3.5 Secondary batteries, 12.3.6 Heating
devices and 12.3.7 Rotating machines through the rotor-bar and slot-wedge
discussion. Figures 12.12, 12.13 and 12.14 sit at their printed positions.
The chapter shell owns the chapter h2, the printed reference list, the
glossary, the source-quirk note and the copyright.

Printed quirks are kept in the English text (the superscript footnote
marker on BS 5501 Part 6, inconsistent voltage spacing, the megaohm and
ohm-per-volt symbols, the '1 mm' wire statement without a superscript,
the two displayed formulas with their juxtaposed brackets, the unnumbered
headings and the comma-ended sentence that continues onto the next page)
with bilingual notes; the Vietnamese follows the intended meaning. This
is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, eq, fig
import mcmillanfig12_c as FC
import mcmillanfig12_d as FD


def body_vi():
    b = []

    # Printed p.319. Continuation of the measuring-instruments paragraph
    # that ends on printed p.318 (owned by the preceding module).
    b.append(p("yêu cầu về cách điện và phân loại nhiệt độ. Chúng cũng phải "
               "đáp ứng các yêu cầu ổn định nhiệt và ổn định động tại "
               "I<sub>th</sub> và I<sub>dyn</sub> cùng giới hạn chung 200°C."))
    b.append(p("Các yêu cầu này khác đáng kể so với các yêu cầu trong "
               "BS 5501, Phần 6³, vốn dựa trên dòng định mức thay vì dòng "
               "ngắn mạch và vì thế kém thực tế hơn. Các con số trong Tiêu "
               "chuẩn đó giả định dòng ngắn mạch tối đa bằng 100 lần dòng "
               "định mức hiệu dụng (rms) đối với máy biến áp dòng, giảm "
               "xuống 50 lần đối với thiết bị đo, và 250 lần dòng định "
               "mức đỉnh đối với máy biến áp dòng, giảm xuống 125 lần đối "
               "với thiết bị đo. Cũng trong những trường hợp này chỉ có "
               "một hệ số an toàn bằng 1 cho I<sub>th</sub> và 1.3 cho "
               "I<sub>dyn</sub>. Các con số gần đây hơn vì thế gắn chặt "
               "với thực tế hơn nhiều."))
    b.append(note("<b>Lưu ý về ký hiệu chú thích dạng mũ.</b> Bản in ghi "
                  "'BS 5501, Phần 6³'; lớp văn bản OCR đọc nhầm thành "
                  "'Part 63'. Số 3 ở dạng mũ là ký hiệu chú thích, không "
                  "phải một phần của số tiêu chuẩn. Bản dịch giữ dạng mũ "
                  "như bản in."))
    b.append(note("<b>Lưu ý về dấu gạch nối trong bản in.</b> Bản in viết "
                  "'rated-current rms' và 'peak-rated current' có dấu "
                  "gạch nối, nhưng '5 hour rate' và 'one hour discharge "
                  "situation' lại không có. Cách viết này được giữ nguyên "
                  "trong bản tiếng Anh; bản tiếng Việt dịch theo nghĩa."))

    b.append(h3("12.3.5 Ắc quy thứ cấp", "12.3.5 Secondary batteries"))
    b.append(p("Ắc quy không thể được cắt điện như các nguồn cấp điện bên "
               "ngoài và dù các ắc quy gồm cả cell sơ cấp lẫn thứ cấp được "
               "cho phép một cách ngầm định qua việc đưa vào đèn đội đầu "
               "(cap lamp), vẫn có các yêu cầu bổ sung riêng đối với ắc "
               "quy gồm các cell thứ cấp. Tuy nhiên, các yêu cầu cơ bản "
               "của nguyên lý bảo vệ áp dụng cho các bộ phận bên ngoài "
               "của mọi cell và ắc quy. Trong trường hợp ắc quy chứa cell "
               "thứ cấp có nhiều yêu cầu bổ sung, đặc biệt vì khả năng "
               "tái tạo bằng cách sạc."))
    b.append(p("Thứ nhất, mọi cell thứ cấp phải có cấu tạo kiểu chì/axit, "
               "niken/sắt hoặc niken/cadmium và không cho phép các kiểu "
               "cấu tạo hóa học khác. Ngoài ra, đối với các ắc quy lớn hơn "
               "(nếu ắc quy gồm các cell thứ cấp có dung lượng lớn hơn 25 "
               "ampere giờ khi xả ở chế độ 5 giờ), nhiều yêu cầu bổ sung "
               "về cấu tạo được áp dụng. Các cell của những ắc quy lớn này "
               "cần đạt được chất lượng cấu tạo cơ bản để ngăn ngừa đoản "
               "mạch do sự dịch chuyển của bản cực, sự tích tụ bùn điện "
               "giải và sự ăn mòn. Để đạt được điều đó, cần đáp ứng các "
               "yêu cầu sau:"))
    b.append(p("1. Các bản cực cell phải được cố định chắc chắn để ngăn "
               "dịch chuyển, và được chế tạo cùng với các tai nối và "
               "thanh cái sao cho ngăn được sự ăn mòn đáng kể ở mức dung "
               "dịch điện giải thấp nhất trong suốt tuổi thọ dự kiến của "
               "cell."))
    b.append(p("2. Khi cần châm thêm dung dịch điện giải theo định kỳ, "
               "cell phải có chỉ báo rõ ràng về mức điện giải tối đa và "
               "tối thiểu được chấp nhận."))
    b.append(p("3. Cần bố trí các lớp bịt kín giữa mỗi cọc và nắp cell để "
               "ngăn rò rỉ dung dịch điện giải, và nắp cell cũng nên được "
               "bịt kín với vỏ ngoài của cell vì lý do tương tự. Cũng phải "
               "có đủ thể tích bên trong cell để đảm bảo sự giãn nở của "
               "dung dịch điện giải do nhiệt dự kiến không gây tràn dung "
               "dịch qua các núm rót."))
    b.append(p("4. Các núm rót dùng để bổ sung dung dịch điện giải cần có "
               "thiết kế ngăn việc phun trào dung dịch khi dung dịch trong "
               "cell"))

    # Printed p.320. Item 4 is split across the page break, and Fig. 12.12
    # sits between its two halves and the start of the container list.
    b.append(p("nằm trong thông số quy định và điều kiện vận hành của cell "
               "cũng nằm trong thông số quy định."))
    b.append(note("<b>Lưu ý về mục danh sách bị chia trang.</b> Mục 4 "
                  "được in tiếp từ trang in 319 sang trang in 320 mà "
                  "không có dấu hiệu tiếp nối; hai nửa được nối lại ở "
                  "đây mà không bỏ sót nửa nào."))
    b.append(p("5. Không gian bố trí ở đáy cell nên đủ lớn để ngăn bùn "
               "lắng tích tụ gây đoản mạch các bản cực trong tuổi thọ "
               "dự kiến của cell."))
    b.append(p("6. Lớp cách điện giữa bất kỳ cọc nào và bên ngoài vỏ cell "
               "phải có điện trở ít nhất 1 MΩ khi ắc quy còn mới. Nếu một "
               "cọc được nối với vỏ cell và điện trở cách điện giữa bên "
               "ngoài vỏ cell với cọc đó nhỏ hơn 1 MΩ thì cần bố trí cách "
               "điện bổ sung trong vỏ ắc quy (trái với vỏ cell) để đảm "
               "bảo cọc được cách điện hiệu quả khỏi các bộ phận dẫn "
               "điện khác theo tiêu chí 1 MΩ."))
    b.append(note("<b>Lưu ý về đơn vị megaohm.</b> Bản in ghi '1 MΩ' (ba "
                  "lần trong đoạn này); lớp văn bản OCR đọc nhầm thành "
                  "'1 MQ', '1MS2' và '1 MS2'. Đơn vị megaohm được khôi "
                  "phục theo bản in."))
    b.append(p("Cấu tạo cell điển hình được thể hiện trong Hình 12.12."))
    b.append(p("Vỏ của những ắc quy lớn này cũng phải tuân theo các yêu "
               "cầu bổ sung, về cơ bản như sau:"))
    b.append(p("1. Vỏ ắc quy có thể bằng kim loại hoặc nhựa, hoặc thực tế "
               "là bằng vật liệu phù hợp khác, miễn là tạo được vỏ cứng "
               "và, khi làm bằng vật liệu dẫn điện, được chế tạo với bề "
               "mặt bên trong được lắp vật liệu cách điện liên kết chặt "
               "để đảm bảo cách điện cho cell. Điều này áp dụng cho"))
    b.append(fig(12, FC.fig_f1212()))
    b.append(note("<b>Lưu ý về số hiệu và nhãn trong Hình 12.12.</b> Lớp "
                  "văn bản OCR đọc số hiệu thành 'Fig. 12.1 2' và chỉ ghi "
                  "được một số nhãn bên phải, bị gãy và thiếu; bản in và "
                  "bản vẽ lại dùng 'Fig. 12.12' với đầy đủ các nhãn hai "
                  "bên như 'Spillproof filling and vent plug', 'Sealed "
                  "lid', 'Post insulation/encapsulation' và 'Adequate "
                  "slurry space'."))

    # Printed p.321. The container-list item 1 continues from the previous
    # page beneath the figure.
    b.append(p("nắp cũng vậy, nhưng ở đây chỉ cần dùng sơn cách điện vì "
               "khả năng tiếp xúc với các cell thấp hơn."))
    b.append(p("2. Vỏ ắc quy cần có cấu tạo đủ chắc để chịu được mọi ứng "
               "suất cơ học có thể gặp khi sử dụng, và phải chống được "
               "sự tấn công của dung dịch điện giải cell. Để đạt được độ "
               "bền cần thiết, có thể lắp các vách ngăn giữa các cell "
               "nhưng phải được cách điện giống như vỏ bọc, không được "
               "áp dụng sự nới lỏng cho nắp ở đây."))
    b.append(p("3. Cần lắp các rào cách điện (có thể là vách ngăn cách "
               "điện) để đảm bảo không phần nào của ắc quy trong một ngăn "
               "của vỏ bọc vượt quá 40V. (Đây là giới hạn rất thường "
               "gặp, cũng thường dùng trong ắc quy thông thường để ngăn "
               "sốc điện đáng kể). Chiều cao của các rào cách điện này "
               "cần ít nhất bằng hai phần ba chiều cao cell và khoảng "
               "cách rò cần thiết giữa các bộ phận dẫn điện (mô tả trong "
               "Bảng 12.1) không được sử dụng bất kỳ khoảng cách nào "
               "quanh các khe hở do các rào này tạo ra, bất kể kích "
               "thước của khe (khoảng cách rò phải là đường nhìn thẳng)."))
    b.append(p("4. Khoảng cách rò giữa các cọc của cell kề nhau (các điểm "
               "nối) và giữa các cọc này với vỏ ắc quy (có cách điện hoặc "
               "không) cần ít nhất 35 mm khi điện áp giữa các cọc là 24V "
               "trở xuống, và khoảng cách này cần tăng thêm 1 mm cho mỗi "
               "2V mà điện áp đó vượt quá 24 V. Các khoảng cách này nhằm "
               "đảm bảo việc nối và ngắt an toàn."))
    b.append(note("<b>Lưu ý về khoảng cách giữa số và đơn vị điện áp.</b> "
                  "Bản in viết '40V' ở mục 3, '24V', '2V' và '24 V' ở mục "
                  "4, nhưng '40 V' ở mục 5. Cách viết từng chỗ được giữ "
                  "nguyên, không chuẩn hóa."))
    b.append(p("5. Không một vỏ đơn lẻ hay phần nào của vỏ được rào cách "
               "điện tách khỏi các phần khác, như đã mô tả, được chứa đủ "
               "cell để cho phép điện áp trong vỏ hoặc phần đó vượt quá "
               "40 V ngay sau khi điện áp ổn định trở lại sau khi sạc."))
    b.append(p("6. Vỏ bọc ắc quy có thể có giới hạn bảo vệ chống xâm nhập "
               "thấp hơn vỏ bọc thông thường để cho phép khí sinh ra "
               "trong quá trình sạc thoát ra, và IP23 theo BS/EN 60529 là "
               "giới hạn dưới. Tuy nhiên, vỏ bọc phải được thông gió đầy "
               "đủ để đảm bảo khi lượng hydro tối đa thoát ra từ các nút "
               "thông hơi của cell, bầu khí quyển chung trong hộp ắc quy "
               "không vượt quá 2 phần trăm hydro. Điều này có thể được "
               "thể hiện bằng cách cho hydro thoát ra từ nút thông hơi "
               "của mỗi cell với tốc độ xác định theo công thức;"))
    b.append(eq("Tốc độ H<sub>2</sub> = dung lượng cell (A H) × 5 × "
                "10<sup>−6</sup> m<sup>3</sup>/hr"))
    b.append(note("<b>Lưu ý về công thức tốc độ hydro.</b> Bản in ghi "
                  "'H₂ rate = cell capacity (A H) × 5 × 10⁻⁶ m³/hr' với "
                  "'(A H)' có dấu cách và 'm³/hr'. Lớp văn bản OCR đọc "
                  "nhầm thành 'HZ rate', 'lop6' và 'm3/h'. Ký hiệu và "
                  "dấu cách được giữ theo bản in."))
    b.append(p("Vỏ ắc quy cũng nên cho phép bất kỳ chất lỏng nào tích tụ "
               "bên trong, vì bất lý do gì, thoát đi. Thông thường chất "
               "lỏng này không phải là axit vì axit được chứa theo cách "
               "phải ngăn không cho thoát ra. Nếu không thể dễ dàng làm "
               "điều này thì cần bố trí vỏ sao cho chất lỏng có thể được "
               "lấy ra mà không làm xáo trộn các cell. Tuy nhiên, cách "
               "tiếp cận sau không lý tưởng vì nó đòi hỏi kiểm tra định "
               "kỳ vỏ trong khi sử dụng để đảm bảo không có chất lỏng nào "
               "tích tụ, và có quy trình lấy ra khi có."))

    # Printed p.322.
    b.append(p("Các nối giữa các cell và giữa ắc quy với phần còn lại của "
               "thiết bị cũng cần đáp ứng các yêu cầu cụ thể để đảm bảo "
               "không phát sinh tia lửa và không chạm bất ngờ. Mọi đầu "
               "nối cell phải có khả năng chịu dòng lớn nhất có thể chạy "
               "qua mà không quá nhiệt và, nếu không thể xác định dòng "
               "lớn nhất, chúng phải chịu được dòng từ ắc quy tương ứng "
               "với dòng trong trường hợp xả trong một giờ. Các đầu nối "
               "cũng cần được bảo vệ khỏi khả năng ăn mòn do dung dịch "
               "điện giải (ví dụ, điều này có nghĩa là chúng cần được "
               "phủ chì đối với ắc quy chì/axit). Ngoài ra, các đầu nối "
               "cần được cách điện để tránh tiếp xúc điện bất ngờ khi "
               "tháo nắp vỏ."))
    b.append(p("Khi dùng các nối mềm, chúng có thể được hàn hoặc hàn thiếc "
               "vào các cọc đầu cuối của cell, miễn là áp dụng các biện "
               "pháp phòng ngừa yêu cầu đối với mối hàn thiếc nói chung "
               "trong trường hợp đó, hoặc, khi dùng dẫn điện bằng đồng, "
               "chúng có thể được ép vào cọc đầu cuối bằng đồng hoặc đầu "
               "cuối được vặn vào cọc đầu cuối. Trong trường hợp sau, "
               "kết nối tới cọc đầu cuối phải có diện tích tiếp xúc ít "
               "nhất bằng diện tích kết nối của dẫn điện."))
    b.append(p("Khi dùng phích cắm và ổ cắm để nối ắc quy với phần còn lại "
               "của thiết bị, chúng không cần tuân thủ các quy định chung "
               "về phích cắm và ổ cắm, miễn là chỉ có thể tách ra bằng "
               "dụng cụ và không định tách ra trong vùng nguy hiểm. Đáng "
               "chú ý ở đây là tất cả các yêu cầu nêu trên đều chưa đủ để "
               "bao phủ tình huống sạc lại, và vì thế người ta giả định "
               "rằng ắc quy không được sạc lại trong vùng nguy hiểm."))

    b.append(h3("12.3.6 Thiết bị gia nhiệt", "12.3.6 Heating devices"))
    b.append(p("Thiết bị gia nhiệt an toàn tăng cường có thể là phần tử "
               "gia nhiệt điện trở như máy gia nhiệt dạng hộp (cartridge "
               "heater), cáp gia nhiệt được bảo vệ nhờ thiết kế sao cho ở "
               "điện áp tối đa máy gia nhiệt không thể vượt quá một nhiệt "
               "độ nhất định khi sử dụng trừ khi xảy ra sự cố, cáp gia "
               "nhiệt có thiết bị điều khiển nhiệt độ để giới hạn nhiệt "
               "độ, và cáp và băng tự giới hạn nhiệt. Vì thế việc gia "
               "nhiệt là do thiết bị được xác định, chứ không phải bằng "
               "cách chỉ đơn thuần cho dòng chạy qua chất lỏng công "
               "nghệ hoặc đường ống và dùng điện trở của chúng để tạo "
               "hiệu ứng gia nhiệt, hoặc bằng cách sinh dòng xoáy."))
    b.append(p("Phần tử gia nhiệt cơ bản có thể là điện trở (và ở đây các "
               "yêu cầu đối với cuộn dây không áp dụng cho các điện trở "
               "này) hoặc cáp điện trở quấn quanh vật cần gia nhiệt sẽ "
               "thường tiếp tục gia nhiệt cho đến khi đạt trạng thái cân "
               "bằng. Nhiệt độ đạt được sẽ là nhiệt độ của lớp cách điện "
               "bên ngoài máy gia nhiệt tại giao diện cách điện/vật được "
               "gia nhiệt và, nếu nhiệt độ này có thể vượt quá giới hạn "
               "vận hành của vật liệu gia nhiệt hoặc cho phép vượt quá "
               "phân loại nhiệt độ yêu cầu, cần lắp một thiết bị để ngăn "
               "điều đó. Thiết bị như vậy không được thực hiện chức năng "
               "điều khiển nhiệt độ bình thường, và nếu cần điều khiển "
               "nhiệt độ bình thường thì phải dùng một thiết bị riêng. Sự "
               "tăng nhiệt của máy gia nhiệt rõ ràng bị ảnh hưởng bởi chế "
               "độ sử dụng, và chế độ sử dụng yêu cầu phải được quy định "
               "trong mọi trường hợp, bao gồm"))

    # Printed p.323. The sentence continues from the previous page.
    b.append(p("những thứ như nhiệt độ của môi trường xung quanh bao gồm "
               "cả phôi gia công, bất kỳ chất lỏng nào đang chảy, v.v., và "
               "đặc tính truyền nhiệt của máy gia nhiệt."))
    b.append(p("Các thiết bị bảo vệ cần cảm biến nhiệt độ của máy gia nhiệt "
               "hoặc môi trường ngay sát nó, nhiệt độ cộng với các điều "
               "kiện khác như dòng chảy trong ống gia nhiệt, v.v., hoặc "
               "cảm biến các thông số khác ngoài nhiệt độ có ảnh hưởng "
               "đáng kể đến nhiệt độ. Mục tiêu luôn là ngăn không cho "
               "vượt quá cấp nhiệt độ và ngăn vật liệu chế tạo máy gia "
               "nhiệt vượt quá nhiệt độ thấp hơn 20°C so với nhiệt độ giới "
               "hạn của vật liệu đó. Vật liệu cách điện của máy gia nhiệt "
               "phải ngăn không cho bầu khí quyển nổ tiếp cận các phần tử "
               "gia nhiệt và do đó thạch anh, cát và các vật liệu tương "
               "tự sẽ không phù hợp."))
    b.append(p("Do bản chất của chúng, hầu hết cáp gia nhiệt điện trở và "
               "một số thiết bị có thể chịu ứng suất cơ học, đặc biệt "
               "trong quá trình lắp đặt cách điện. Để đảm bảo tính phù "
               "hợp, các thiết bị này được thử bằng cách bị ép bởi một "
               "thanh thép đường kính 6mm với lực 1500N tác dụng và bị "
               "uốn qua 90° trên trục gá thể hiện trong Hình 12.13 ở "
               "nhiệt độ vận hành thấp nhất của chúng. Các tác động này "
               "không được làm hư hại cả máy gia nhiệt lẫn lớp cách điện "
               "của nó. Thiết bị dự định dùng dưới nước hoặc các chất "
               "lỏng khác cũng sẽ được thử ngâm để đảm bảo không xảy ra "
               "rò rỉ."))
    b.append(note("<b>Lưu ý về ký hiệu độ và đơn vị trong thử nghiệm "
                  "uốn.</b> Bản in ghi '90°', '6mm' và '1500N' (không có "
                  "dấu cách ở hai đơn vị sau); lớp văn bản OCR đọc dấu độ "
                  "thành dấu nháy kép. Dấu độ và cách viết đơn vị được "
                  "giữ theo bản in."))
    b.append(fig(13, FD.fig_f1213()))

    # Printed p.324.
    b.append(p("Thiết bị gia nhiệt an toàn tăng cường, cũng như mọi thiết "
               "bị an toàn tăng cường khác, dựa trên thực tế là các yêu "
               "cầu cấu tạo nâng cao làm cho hỏng hóc rất khó xảy ra và "
               "nếu hỏng hóc xảy ra thì việc cắt điện sẽ diễn ra nhanh "
               "chóng. Thiết bị gia nhiệt, và đặc biệt là cáp gia nhiệt, "
               "phủ một diện tích khá lớn và loại bảo vệ điện phù hợp "
               "nhất cho sự cố cách điện là cầu dao chống giật (residual "
               "current circuit breaker), lý tưởng là loại tác động ở "
               "dòng rò 30 mA dù dòng tác động lên tới 300 mA vẫn được "
               "chấp nhận. Tuy nhiên, tốc độ tác động của thiết bị rất "
               "quan trọng vì sự cố cách điện có thể nằm trong vùng nguy "
               "hiểm, và yêu cầu là tối đa 5 s ở dòng tác động định mức "
               "tối thiểu, giảm xuống 0.15 s ở năm lần dòng đó. Dĩ nhiên "
               "những thiết bị này không dùng được khi nguồn là IT (trung "
               "tính được nối đất tại nguồn qua một trở kháng) và trong "
               "những trường hợp đó (ít gặp ở Anh) cần có thiết bị giám "
               "sát cách điện. Thiết bị giám sát này nên tác động khi "
               "điện trở cách điện giảm xuống dưới 50 Ω/V của điện áp "
               "định mức (ví dụ, 12,500 Ω ở điện áp nguồn định mức "
               "250V)."))
    b.append(note("<b>Lưu ý về ký hiệu ohm.</b> Bản in ghi '50 Ω/V' và "
                  "'12,500 Ω'; lớp văn bản OCR đọc nhầm thành '50 C!/V' và "
                  "'12,500 i2'. Ký hiệu Ω được khôi phục theo bản in; "
                  "'250V' được giữ không có dấu cách."))
    b.append(p("Dây nối từ các phần tử gia nhiệt tới cọc đầu cuối của "
               "thiết bị cần vượt quá 1 mm để đảm bảo độ tin cậy và, khi "
               "thiết bị gia nhiệt được bọc vỏ dẫn điện để hỗ trợ hoạt "
               "động của thiết bị bảo vệ chạm đất, vỏ đó nên có điện trở "
               "thấp hơn đáng kể so với máy gia nhiệt để đảm bảo nó "
               "không sinh thêm nhiệt trừ khi bị thiết bị bảo vệ quá "
               "nhiệt ngăn không cho làm vậy. Lớp phủ dẫn điện cũng phải "
               "phủ ít nhất 70 phần trăm bề mặt máy gia nhiệt để đảm bảo "
               "hoạt động đúng."))
    b.append(note("<b>Lưu ý về đơn vị '1 mm'.</b> Bản in viết dây nối 'cần "
                  "vượt quá 1 mm' mà không có số mũ 2; nhiều khả năng đây "
                  "là sự thiếu sót của nguyên bản đối với tiết diện "
                  "(mm²). Không tự ý chèn '²'; ký hiệu được giữ nguyên "
                  "theo bản in và được ghi nhận ở đây."))

    b.append(h3("12.3.7 Máy quay", "12.3.7 Rotating machines"))
    b.append(p("Máy điện quay, cùng với hộp đầu cuối, là ứng dụng phổ biến "
               "nhất của an toàn tăng cường vì cấu tạo của máy dễ hơn "
               "nhiều so với máy chống cháy và máy thu được nhẹ hơn rất "
               "nhiều. Tuy nhiên vẫn có vấn đề, vì máy có vòng bi và "
               "chuyển động tương đối giữa các bộ phận là có thể xảy ra. "
               "Vì điều này có thể dẫn đến các vấn đề như va chạm "
               "stator/rotor, cấu tạo phải cố gắng giảm thiểu khả năng "
               "đó. Ngoài ra, máy chạy với dòng lớn hơn nhiều trong khi "
               "khởi động và khả năng bắt lửa từ các thiết bị này phải "
               "tính đến một số điều kiện khác nhau."))
    b.append(p("Máy an toàn tăng cường nói chung là máy cảm ứng với rôto "
               "lồng sóc, vì với cấu tạo này không cần nối điện tới rôto, "
               "điều không thể thực hiện được trong khuôn khổ nguyên lý "
               "an toàn tăng cường. Máy an toàn tăng cường với rôto quấn "
               "được ngắn mạch vĩnh viễn cũng có thể dùng nhưng nói chung, "
               "khi rôto máy được quấn thì cần có nối điện tới rôto vì "
               "những lý do vận hành như hạn chế mô-men khởi động và "
               "điều khiển tốc độ (bằng điều khiển độ trượt). Trong những "
               "trường hợp này, các nối tới rôto là tiếp điểm quay dạng "
               "lò xo hoặc chổi than, tạo thành tiếp điểm phát tia lửa và "
               "không thể dùng trong bối cảnh an toàn tăng cường. Vì vậy, "
               "khi có các tiếp điểm này,"))

    # Printed p.325. The sentence carries over from printed p.324.
    b.append(p("chúng cần được bảo vệ bằng một nguyên lý bảo vệ khác và "
               "thường là chống cháy, tạo thành dạng bảo vệ phức hợp cho "
               "máy."))
    b.append(note("<b>Lưu ý về câu bị chia trang.</b> Câu ở cuối trang in "
                  "324 kết thúc bằng dấu phẩy và được nối tiếp ở đầu "
                  "trang in 325. Hai nửa được nối lại ở đây; dấu phẩy "
                  "không được thay bằng dấu chấm."))
    b.append(h4("Khe hở rôto/stator", "Rotor/stator clearances"))
    b.append(p("Điều cần thiết đầu tiên là ngăn va chạm rôto/stator trong "
               "mức có thể trong mọi điều kiện vận hành, và ngăn các ứng "
               "suất do những điều kiện đó tạo ra. Điều này được thực "
               "hiện bằng cách quy định khe hở tối thiểu giữa rôto và "
               "stator khi máy đứng yên, đây là trường hợp xấu nhất vì "
               "mọi sự 'võng' của rôto do khối lượng của nó sẽ hiện diện. "
               "Khe hở tối thiểu này được suy ra từ một công thức thoạt "
               "nhìn có vẻ phức tạp và như sau:"))
    b.append(eq("Khe hở không khí = {0.15 + [D − 50/780]"
                "[0.25 + (0.75 × n/1000)]}      mm"))
    b.append(note("<b>Lưu ý về công thức khe hở không khí.</b> Bản in thể "
                  "hiện công thức là 'Air gap = {0.15 + [D − 50/780]"
                  "[0.25 + (0.75 × n/1000)]} mm' với hai nhóm ngoặc đặt "
                  "cạnh nhau không có dấu nhân và ngoặc ngoài dạng ngoặc "
                  "nhọn; lớp văn bản OCR cũng đọc sai dấu nhân và ký tự "
                  "cuối. Không tự ý sửa công thức; nó được tái hiện như "
                  "bản in."))
    b.append(p("trong đó D = đường kính rôto tính bằng mm (tối thiểu 75 "
               "mm<br>và tối đa 750 mm)<br>n = tốc độ máy tính bằng "
               "vòng/phút (tần số × 50/số cặp cực<br>trên mỗi pha)"))
    b.append(p("Con số trên được nhân với một con số suy ra từ chiều dài "
               "lõi (mm)/1.75 × đường kính lõi (mm) khi giá trị này vượt "
               "quá 1 và lại được nhân thêm với 1.5 khi dùng vòng bi bạc "
               "thay vì vòng bi lăn. Phép tính này trông phức tạp hơn "
               "nhiều so với phép tính dùng trong ấn bản đầu tiên của "
               "Tiêu chuẩn Châu Âu (BS 5501, Phần 6) nhưng trên thực tế "
               "không ảnh hưởng đáng kể đến yêu cầu khe hở, cho ra trung "
               "bình một con số thấp hơn con số từng cần thiết trước đây "
               "nhưng thường nằm trong khoảng 10 phần trăm của con số "
               "đó."))
    b.append(note("<b>Lưu ý về cách ghi Tiêu chuẩn Châu Âu.</b> Bản in "
                  "viết 'ấn bản đầu tiên của Tiêu chuẩn Châu Âu (BS 5501, "
                  "Phần 6)', dù BS 5501 là Tiêu chuẩn Anh; cách ghi này "
                  "được giữ nguyên và ghi nhận ở đây."))
    b.append(h4("Cách điện dây dẫn stator và rôto",
                "Insulation of stator and rotor conductors"))
    b.append(note("<b>Lưu ý về các tiêu đề không đánh số.</b> Bản in đặt "
                  "'Rotor/stator clearances' và 'Insulation of stator and "
                  "rotor conductors' làm các tiêu đề in đậm không có số "
                  "dưới 12.3.7. Chúng được giữ không đánh số. Lớp văn bản "
                  "OCR viết thường chữ cái đầu của tiêu đề thứ hai; bản "
                  "in có chữ 'I' viết hoa."))
    b.append(p("Các yêu cầu cách điện thông thường áp dụng cho cả stator "
               "và rôto quấn nhưng, trong trường hợp máy, ứng suất từ "
               "tính sẽ có nghĩa là phải đặc biệt chú ý đảm bảo độ chắc "
               "chắn của cuộn dây để ngăn hư hại cách điện do chuyển "
               "động. Khi dùng rôto lồng sóc, thanh rôto không được cách "
               "điện với nền từ tính của rôto và, ngoài sự cần thiết phải "
               "đảm bảo nối chắc chắn giữa các thanh với nhau, tiếp xúc "
               "giữa các thanh và lõi rôto cần cực kỳ chặt để không phát "
               "sinh tia lửa giữa các thanh rôto và giữa thanh rôto với "
               "lõi, đặc biệt trong khi khởi động khi ứng suất ở mức tối "
               "đa. Để đạt được điều này, lồng sóc cùng với các vòng cuối "
               "thường được đúc thành một khối hoặc các vòng và thanh "
               "được hàn đồng hoặc hàn. Độ chặt của chúng trong các rãnh "
               "rôto đạt được bằng cách đúc nhôm vào các rãnh, nhưng lót "
               "rãnh bổ sung, nêm hoặc then cũng là các phương pháp được "
               "chấp nhận. Hình 12.14 cho thấy một lồng sóc đơn giản "
               "điển hình."))
    b.append(fig(14, FD.fig_f1214()))
    return "".join(b)


def body_en():
    b = []

    # Printed p.319. Continuation of the measuring-instruments paragraph
    # that ends on printed p.318 (owned by the preceding module).
    b.append(p("insulation requirements and temperature classification. "
               "They must also satisfy the thermal and dynamic stability "
               "requirements at I<sub>th</sub> and I<sub>dyn</sub> and the "
               "200°C overall limit."))
    b.append(p("These requirements are significantly different to those in "
               "BS 5501, Part 6³ which were based on rated current, rather "
               "than short-circuit current and thus were less realistic. "
               "The figures in that Standard assumed that short-circuit "
               "currents were a maximum of 100 times rated-current rms for "
               "current transformers, reducing to 50 times for measuring "
               "instruments, and 250 times peak-rated current for current "
               "transformers, reducing to 125 times for measuring "
               "instruments. There was only a safety factor of 1 for "
               "I<sub>th</sub> and 1.3 for I<sub>dyn</sub> in these cases "
               "also. The more recent figures are therefore much more "
               "closely related to reality."))
    b.append(note("<b>Note on the superscript footnote marker.</b> The "
                  "print reads 'BS 5501, Part 6³'; the OCR text layer reads "
                  "'Part 63'. The superscript 3 is a footnote marker, not "
                  "part of the standard number. It is retained as printed."))
    b.append(note("<b>Note on the hyphenation in the print.</b> The print "
                  "writes 'rated-current rms' and 'peak-rated current' with "
                  "hyphens, but '5 hour rate' and 'one hour discharge "
                  "situation' without. The distinction is kept as printed."))

    b.append(h3("12.3.5 Secondary batteries", "12.3.5 Secondary batteries"))
    b.append(p("Batteries cannot be switched off like external power "
               "supplies and although batteries comprising both primary "
               "and secondary cells are permitted tacitly by the inclusion "
               "of cap lamps, there are specific additional requirements "
               "for batteries comprising secondary cells. However, the "
               "basic requirements of the protection concept apply to the "
               "external parts of all cells and batteries. In the case of "
               "batteries containing secondary cells there are several "
               "additional requirements, particularly because of the "
               "possibility of their regeneration capability by charging."))
    b.append(p("First, all secondary cells must be of the lead/acid, "
               "nickel/iron or nickel/cadmium type construction and no "
               "other chemical type of constructions are permitted. In "
               "addition, for larger batteries (if the battery comprised "
               "of secondary cells has a capacity of greater than 25 "
               "ampere hours when discharged at the 5 hour rate) several "
               "additional constructional requirements apply. The cells of "
               "these larger batteries need to reach a basic quality of "
               "construction to prevent short circuits caused by plate "
               "movements, electrolyte slurry build up and corrosion. To "
               "this end the following requirements need to be addressed:"))
    b.append(p("1. The cell plates shall be positively secured to prevent "
               "movement, and constructed together with their lugs and "
               "busbars so as to prevent significant corrosion at lowest "
               "electrolyte level for the expected life of the cell."))
    b.append(p("2. Where it is necessary to top up an electrolyte from "
               "time to time, cells must have a clear indication of maximum "
               "and minimum levels of electrolyte acceptable."))
    b.append(p("3. Seals should be provided between each pole and the lid "
               "of the cell to prevent electrolyte leakage, and the cell "
               "lid should be sealed to the outer cell case for the same "
               "reason. There will also have to be sufficient volume inside "
               "the cell to ensure that expansion of electrolyte, due to "
               "expected heating, does not cause overflow of electrolyte "
               "from the filling plugs."))
    b.append(p("4. Filling plugs for electrolyte replenishment will need "
               "to be of a design which prevents ejection of electrolyte "
               "when the electrolyte in the cell"))

    # Printed p.320. Item 4 is split across the page break, and Fig. 12.12
    # sits between its two halves and the start of the container list.
    b.append(p("is within specification and the cell operating conditions "
               "are also within specification."))
    b.append(note("<b>Note on the list item split across the page.</b> "
                  "Item 4 continues from printed p.319 to printed p.320 "
                  "with no continuation marker; the two halves are joined "
                  "here without dropping either."))
    b.append(p("5. The space provided at the bottom of the cell should be "
               "sufficiently large to prevent build up of slurry from short "
               "circuiting the plates in the expected life of the cell."))
    b.append(p("6. The insulation between any poles and the outside of the "
               "cell container should have a resistance of at least 1 MΩ "
               "when the battery is new. If one pole is connected to the "
               "cell case and the insulation resistance between the outside "
               "of the cell case and that pole is less than 1 MΩ then it "
               "will be necessary to provide additional insulation in the "
               "battery container (as opposed to the cell container) to "
               "ensure that the pole is effectively insulated from other "
               "conducting parts using the 1 MΩ criterion."))
    b.append(note("<b>Note on the megaohm unit.</b> The print reads '1 MΩ' "
                  "three times in this paragraph; the OCR text layer reads "
                  "'1 MQ', '1MS2' and '1 MS2'. The megaohm unit is restored "
                  "as printed."))
    b.append(p("A typical cell construction is shown in Fig. 12.12."))
    b.append(p("The containers of these larger batteries likewise have "
               "additional requirements applied to them and these are "
               "basically as follows:"))
    b.append(p("1. Battery containers may be of metal or plastics, or "
               "indeed other suitable materials, provided they produce a "
               "rigid container and, where of conducting material, are "
               "manufactured with their internal surfaces fitted with "
               "bonded insulating material to ensure cell insulation. This "
               "applies to"))
    b.append(fig(12, FC.fig_f1212()))
    b.append(note("<b>Note on the number and labels of Figure 12.12.</b> "
                  "The OCR text layer reads the number as 'Fig. 12.1 2' and "
                  "captures only a few broken right-hand labels; the print "
                  "and the redraw use 'Fig. 12.12' with the full set of "
                  "labels on both sides, such as 'Spillproof filling and "
                  "vent plug', 'Sealed lid', 'Post "
                  "insulation/encapsulation' and 'Adequate slurry space'."))

    # Printed p.321. The container-list item 1 continues from the previous
    # page beneath the figure.
    b.append(p("covers also but here it is sufficient to use insulating "
               "paint because of the lower likelihood of contact with "
               "cells."))
    b.append(p("2. Battery containers need to be of sufficiently strong "
               "construction to withstand any mechanical stress to which "
               "they may be subjected in service, and must be resistant to "
               "attack by the cell electrolyte. To achieve the necessary "
               "strength, partition walls may be fitted between cells but "
               "must be insulated in the same way as the enclosure, the lid "
               "relaxation not being appropriate here."))
    b.append(p("3. Insulating barriers (which may be insulated partition "
               "walls) need to be fitted to ensure that no section of the "
               "battery in one compartment of the enclosure exceeds 40V. "
               "(This is a very common limitation often also used in normal "
               "batteries to prevent significant electric shock). The "
               "height of these insulating barriers needs to be at least "
               "two thirds of the cell height and the creepage distances "
               "necessary between conducting parts (described in Table "
               "12.1) must not utilize any distances around slots produced "
               "by such barriers, whatever the dimensions of the slot (the "
               "creepage distances must be line of sight)."))
    b.append(p("4. The creepage distance between poles of adjacent cells "
               "(the connection points) and between these poles and the "
               "battery container (insulated or otherwise) need to be at "
               "least 35 mm where the voltage between the poles is 24V or "
               "less, and this distance needs to be increased by 1 mm for "
               "every 2V by which this voltage exceeds 24 V. These "
               "distances are to ensure safe connecting and disconnecting."))
    b.append(note("<b>Note on voltage spacing in the print.</b> The print "
                  "writes '40V' in item 3, '24V', '2V' and '24 V' in item 4, "
                  "but '40 V' in item 5. Each spelling is kept as printed "
                  "and is not normalized."))
    b.append(p("5. No single container or part of a container separated "
               "from other parts of an insulated barrier, as already "
               "described, must contain sufficient cells to permit the "
               "voltage in that container or section to exceed 40 V "
               "immediately the voltage has stabilized after charging."))
    b.append(p("6. Battery enclosures may have a lower ingress protection "
               "limit than normal enclosure to permit dispersion of any "
               "gas produced during charging and IP23 to BS/EN 60529 is the "
               "lower limit. The enclosure must, however, be sufficiently "
               "well ventilated to ensure that when the maximum amount of "
               "hydrogen is released from the cell vent plugs, the general "
               "atmosphere within the battery box does not exceed 2 per "
               "cent hydrogen. This can be shown by releasing hydrogen from "
               "the vent plug of each cell at a rate determined by the "
               "formula;"))
    b.append(eq("H<sub>2</sub> rate = cell capacity (A H) × 5 × "
                "10<sup>−6</sup> m<sup>3</sup>/hr"))
    b.append(note("<b>Note on the hydrogen-rate formula.</b> The print "
                  "reads 'H₂ rate = cell capacity (A H) × 5 × 10⁻⁶ "
                  "m³/hr' with a space in '(A H)' and with 'm³/hr'; the OCR "
                  "text layer reads 'HZ rate', 'lop6' and 'm3/h'. The "
                  "symbols and spacing are kept as printed."))
    b.append(p("Battery containers should also allow any liquid which "
               "collects within them for whatever reason to drain away. "
               "This will not normally be acid as the acid is contained in "
               "a manner which should prevent release. If this cannot "
               "easily be done then the container should be arranged so "
               "that the liquid can be removed without disturbing the "
               "cells. This latter approach is, however, not ideal as it "
               "requires regular inspection of the container in service to "
               "ensure that no liquid has collected, and a removal "
               "procedure where it has."))

    # Printed p.322.
    b.append(p("The connections between cells and between the battery and "
               "the remainder of the apparatus also needs to meet specific "
               "requirements to ensure freedom from sparking and "
               "inadvertent contact. All cell connectors must be capable "
               "of carrying the maximum current which could flow without "
               "overheating and, if the maximum current cannot be "
               "specified, they must carry the current from the battery "
               "which relates to that flowing in a one hour discharge "
               "situation. Connectors also need to be protected from the "
               "possibility of corrosion by electrolyte (e.g., this will "
               "mean that they will need coating with lead for lead/acid "
               "batteries). In addition, connectors need to be insulated "
               "to avoid inadvertent electrical contact when the container "
               "lid is removed."))
    b.append(p("Where flexible connections are used they may be welded or "
               "soldered on to the cell terminal posts, provided the "
               "precautions required for general soldered joints are "
               "applied in that case, or, where copper conductors are used, "
               "they may be crimped into a copper terminal post or terminal "
               "screwed to a terminal post. In the latter case, the "
               "connection to the terminal post must have at least the "
               "same contact area as the conductor connection."))
    b.append(p("Where plugs and sockets are used to connect the battery to "
               "the remainder of the apparatus they do not need to comply "
               "with the general specifications for plugs and sockets, "
               "provided they can only be separated by a tool and are not "
               "intended to be separated in the hazardous area. It is "
               "worthy of note here that all of the foregoing requirements "
               "are not sufficient to cover the recharging situation and "
               "thus it is assumed that batteries are not recharged in a "
               "hazardous area."))

    b.append(h3("12.3.6 Heating devices", "12.3.6 Heating devices"))
    b.append(p("Increased safety heating devices may be heating resistance "
               "elements such as cartridge heaters, heating cables which "
               "are protected by design in that at maximum voltage the "
               "heater cannot exceed a particular temperature in service "
               "unless a fault occurs, heating cables which have temperature "
               "control devices to limit the temperature and self-limiting "
               "heating cables and tapes. Thus the heating is by defined "
               "apparatus, and not by merely applying a current to the "
               "process fluid or pipeline and using its resistance to "
               "create the heating effect or by production of eddy currents."))
    b.append(p("The basic heating element which may be a resistance (and "
               "here the requirements for windings are not applied to such "
               "resistances) or a resistance cable wound round the object "
               "to be heated will normally continue heating until "
               "equilibrium is reached. The temperature achieved will be "
               "that of the heater outside insulation at the "
               "insulation/heated object interface and, if this can exceed "
               "the heater materials operating limits or permit the "
               "required temperature classification to be exceeded, a "
               "device to prevent this needs to be fitted. Such a device "
               "must not perform a normal temperature control function, and "
               "if normal temperature control is necessary a separate "
               "device must be used. The heater temperature rise is "
               "obviously affected by its mode of use, and the required "
               "mode of use must be specified in all cases including"))

    # Printed p.323. The sentence continues from the previous page.
    b.append(p("such things as the temperature of its surroundings including "
               "the workpiece, any flowing fluid, etc., and the heat "
               "transfer characteristics of the heater."))
    b.append(p("Protective devices need to either sense the temperature of "
               "the heater or its immediate surroundings, the temperature "
               "plus other conditions such as flow in heated pipes, etc., "
               "or sense parameters other than temperature which have "
               "significant bearing on temperature. The objective is always "
               "to prevent the temperature class being exceeded and the "
               "material of construction of the heater from exceeding a "
               "temperature of 20°C less than the limiting temperature for "
               "that material. Heater insulating materials must prevent "
               "access of the explosive atmosphere to the heater elements "
               "and therefore quartz, sand and similar materials will not "
               "be suitable."))
    b.append(p("As a result of their nature most resistance heating cables, "
               "and some units, may be subjected to mechanical stress "
               "particularly during insulation. To ensure their suitability "
               "these devices are subjected to being crushed by a steel rod "
               "of 6mm diameter with a 1500N force applied and subjected to "
               "being bent through 90° on the mandrel shown in Fig. 12.13 "
               "at its lowest operating temperature. These actions should "
               "not damage either the heater or its insulation. Devices "
               "intended for use under water or other liquids will also be "
               "tested immersed to ensure that no leakage occurs."))
    b.append(note("<b>Note on the degree sign and units in the bend test.</b> "
                  "The print reads '90°', '6mm' and '1500N' (with no space "
                  "in the last two units); the OCR text layer reads the "
                  "degree sign as a double quote. The degree sign and the "
                  "unit spacing are kept as printed."))
    b.append(fig(13, FD.fig_f1213()))

    # Printed p.324.
    b.append(p("Increased safety heating devices are, as all other "
               "increased safety devices, based upon the fact that the "
               "enhanced constructional requirements make failure very "
               "unlikely and if failure does occur then isolation follows "
               "rapidly. Heating devices, and heating cables particularly, "
               "cover fairly large areas and the most suitable type of "
               "electrical protection for insulation failure is the "
               "residual current circuit breaker, ideally one which "
               "operates at a leakage current of 30 mA although operating "
               "currents up to 300 mA are acceptable. The rate of operation "
               "of the device is, however, important given that the failure "
               "of insulation may be in the hazardous area and a maximum "
               "of 5 s at minimum rated operating current falling to 0.15 s "
               "at five times that current is required. These are, of "
               "course, not usable where the supply is IT (its neutral is "
               "connected to earth at source through an impedance) and in "
               "such cases (which are unusual in the UK) an insulation "
               "monitor is necessary. This monitor should operate when the "
               "insulation falls to less than 50 Ω/V of rated voltage "
               "(e.g., 12,500 Ω at 250V rated supply voltage)."))
    b.append(note("<b>Note on the ohm symbols.</b> The print reads '50 Ω/V' "
                  "and '12,500 Ω'; the OCR text layer reads '50 C!/V' and "
                  "'12,500 i2'. The Ω symbol is restored as printed; '250V' "
                  "is kept without a space."))
    b.append(p("Wires connecting the heating elements to the device "
               "terminals need to exceed 1 mm to ensure reliability and, "
               "where the heating device is covered with a conducting "
               "sheath to assist in operation of earth fault devices, the "
               "sheath should have a significantly lower resistance than "
               "the heater to ensure it does not produce additional heating "
               "unless it is prevented from so doing by the over "
               "temperature protective device. The conductive covering "
               "must also extend over at least 70 per cent of the heater "
               "surface to ensure correct operation."))
    b.append(note("<b>Note on the unit '1 mm'.</b> The print says the wires "
                  "'need to exceed 1 mm' without a superscript 2; this is "
                  "likely an omission in the source for a cross-sectional "
                  "area (mm²). No '²' is silently inserted; the notation is "
                  "kept as printed and flagged here."))

    b.append(h3("12.3.7 Rotating machines", "12.3.7 Rotating machines"))
    b.append(p("Rotating electrical machines, together with terminal boxes, "
               "constitute the most common use for increased safety as the "
               "construction of the machine is much easier than its "
               "flameproof counterpart and the resulting machine is much "
               "lighter. There are problems, however, since the machines "
               "include bearings and relative movement of parts is likely. "
               "As this could lead to such problems as stator/rotor clashes, "
               "the construction must try to minimize their possibility. In "
               "addition, machines operate at much greater currents during "
               "starting and the possibility of ignition from such devices "
               "must take account of several different conditions."))
    b.append(p("Increased safety machines are generally induction machines "
               "with squirrel cage rotors as, with this construction, there "
               "is no necessity for electrical connections to the rotor "
               "which are not possible within the concept of increased "
               "safety. Increased safety machines with wound rotors which "
               "are permanently short circuited are also possible but, in "
               "general, when a machine rotor is wound electrical "
               "connections to that rotor are operationally required for "
               "such reasons as limiting of starting torque and speed "
               "control (by control of slip). In these cases, the "
               "connections to the rotor are by rotating spring contacts or "
               "brushes which constitute sparking contacts and are not "
               "possible in the increased safety context. Where these are "
               "present, therefore,"))

    # Printed p.325. The sentence carries over from printed p.324.
    b.append(p("they need to be protected by another protection concept and "
               "are usually flameproof giving a composite form of "
               "protection to the machine."))
    b.append(note("<b>Note on the sentence split across the page.</b> The "
                  "last sentence on printed p.324 ends with a comma and "
                  "continues at the top of printed p.325. The two halves "
                  "are joined here; the comma is not replaced by a full "
                  "stop."))
    b.append(h4("Rotor/stator clearances", "Rotor/stator clearances"))
    b.append(p("The first necessity is to prevent rotor/stator clashes as "
               "far as possible in all operating conditions, and the "
               "stresses created by those conditions. This is done by "
               "specifying a minimum clearance between rotor and stator "
               "when the machine is at rest which is the worst case as any "
               "'sag' of the rotor, due to its mass, will be present. This "
               "minimum clearance is derived from a formula which at first "
               "glance appears complex and is as follows:"))
    b.append(eq("Air gap = {0.15 + [D − 50/780][0.25 + (0.75 × "
                "n/1000)]}      mm"))
    b.append(note("<b>Note on the air-gap formula.</b> The print gives the "
                  "formula as 'Air gap = {0.15 + [D − 50/780][0.25 + "
                  "(0.75 × n/1000)]} mm', with two bracket groups "
                  "juxtaposed without a multiplication sign and with "
                  "brace-like outer glyphs; the OCR text layer also "
                  "misreads the multiplication sign and the final glyph. "
                  "The formula is not silently corrected; it is "
                  "reproduced as printed."))
    b.append(p("where D = rotor diameter in mm (subject to a minimum of 75 "
               "mm<br>and a maximum of 750 mm)<br>n = machine speed in "
               "revs/min (frequency × 50/pole pairs<br>per phase)"))
    b.append(p("The above figure is multiplied by a figure derived from "
               "core length (mm)/1.75 × core diameter (mm) where this "
               "exceeds 1 and further multiplied by 1.5 where sleeve, rather "
               "than rolling element bearings, are used. This calculation "
               "looks much more complex than that used in the first edition "
               "of the European Standard (BS 5501, Part 6) but, in effect, "
               "does not significantly affect the clearance requirements, "
               "giving on average a figure which is lower than the figure "
               "which would previously have been necessary but normally "
               "within around 10 per cent of that figure."))
    b.append(note("<b>Note on the standards attribution.</b> The print "
                  "reads 'the first edition of the European Standard (BS "
                  "5501, Part 6)', although BS 5501 is a British Standard; "
                  "the wording is retained as printed and flagged here."))
    b.append(h4("Insulation of stator and rotor conductors",
                "Insulation of stator and rotor conductors"))
    b.append(note("<b>Note on the unnumbered headings.</b> The print sets "
                  "'Rotor/stator clearances' and 'Insulation of stator and "
                  "rotor conductors' as bold, unnumbered headings under "
                  "12.3.7. They are kept unnumbered. The OCR text layer "
                  "lowercases the initial letter of the second heading; "
                  "the print has a capital 'I'."))
    b.append(p("The normal insulation requirements apply to both stators "
               "and wound rotors but, in the case of machines, the magnetic "
               "stresses will mean that special attention must be given to "
               "ensuring the security of windings to prevent insulation "
               "damage due to movement. Where squirrel cage rotors are used "
               "the rotor bars are not insulated from the rotor magnetic "
               "base and, in addition to the necessity to ensure secure "
               "interconnection between the bars themselves, the contact "
               "between the bars and the rotor core needs to be extremely "
               "firm to ensure that sparking does not occur between rotor "
               "bars and between rotor bars and the core, particularly "
               "during starting when stresses are at their maximum. To "
               "achieve this the squirrel cage including its end rings, is "
               "normally either cast as a single unit or the rings and bars "
               "are brazed or welded together. Their tightness of fit in "
               "the rotor slots is achieved by casting them in the slots "
               "with aluminium but supplementary slot lining, wedging or "
               "keying are also acceptable methods. Figure 12.14 shows a "
               "typical simple squirrel cage."))
    b.append(fig(14, FD.fig_f1214()))
    return "".join(b)
