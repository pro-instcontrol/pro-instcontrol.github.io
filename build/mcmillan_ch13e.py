# -*- coding: utf-8 -*-
"""Chapter 13, module E - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 395-410 (PDF pp. 416-431).

Covers survey blocks E1-E65: the tail of 13.10.3, 13.10.4 blocking
capacitors, 13.10.5 shunt safety assemblies, 13.10.6 internal wiring and
connections, 13.10.7 galvanic separation, 13.11 diode safety barriers and
13.12 input and output specifications. Figures 13.28-13.35 sit at their
printed positions. The chapter shell owns the chapter h2, the printed
reference list, the glossary, the general source-quirk note and the
copyright.

The survey begins mid-paragraph on printed p.395 and ends mid-sentence on
printed p.410; both boundaries are preserved. Printed quirks are kept in
the English text and explained in bilingual notes; the Vietnamese follows
the intended meaning. This is an unofficial study translation. The source
PDF is not republished.
"""
from mcmillan_common import h3, h4, p, eq, note, table, fig
import mcmillanfig13_e as FE


def body_vi():
    b = []

    # §6 quirk 1 - brief/line-number mismatch.
    b.append(note("<b>Lưu ý về sự lệch số dòng giữa brief và tệp nguồn.</b> "
                  "Brief ghi dòng 17254 là === PAGE 416 ===; trong tệp thực "
                  "tế dòng 17254 là === PAGE 417 ===, còn === PAGE 416 === "
                  "nằm ở dòng 17208. Phạm vi 17208–17778 được dùng để gồm "
                  "đủ 16 trang in được yêu cầu."))
    # §6 quirk 22 - running-header punctuation.
    b.append(note("<b>Lưu ý về dấu ngoặc đơn ở tiêu đề chạy trang.</b> Các "
                  "trang in chẵn mang dòng 'N Electrical installations in "
                  "hazardous areas'; các trang lẻ mang dòng 'Protection "
                  "concept intrinsic safety 'i' N'. Dấu ngoặc đơn ở 'i' "
                  "thẳng trên các trang 395, 399, 405 và cong trên các "
                  "trang 397, 401, 403, 407, 409; OCR ở PDF 426 đọc nhầm "
                  "thành '7''. Tiêu đề chạy trang thuộc về phần trình bày "
                  "của shell, không nằm trong thân bài này."))

    # Printed p.395 / BLOCK A. E1 opens mid-paragraph from printed p.394.
    # E1
    b.append(p("dòng điện tới một linh kiện để phân loại nhiệt độ, hoặc để "
               "hạn chế tốc độ phóng điện của các tụ điện mà nếu không thì "
               "có khả năng gây cháy. Các điện trở này phải không hỏng khi "
               "bị hỏng theo chiều giảm giá trị điện trở nhưng có thể tăng "
               "điện trở hoặc đứt mạch. Để đạt được điều đó, các điện trở "
               "phải thuộc những kiểu cấu tạo đặc biệt như sau. Thứ nhất, "
               "loại màng carbon hoặc kim loại, trong đó phần tử điện trở "
               "về thực chất là một lớp carbon hoặc kim loại tinh khiết "
               "được cách điện, lắng đọng trên một nền thường bằng gốm hoặc "
               "vật liệu cách điện tương tự, được khắc xoắn ốc để cho ra "
               "điện trở yêu cầu, rồi được bảo vệ bằng men cách điện hoặc "
               "sơn vecni để ngăn tiếp xúc bên ngoài với phần tử; thứ hai, "
               "được quấn dây trên một lõi gốm hoặc lõi bằng vật liệu tương "
               "tự, rồi được gia cố bằng men, sơn vecni, v.v., để ngăn dây "
               "bị tuột khi đứt hoặc bị tiếp xúc từ bên ngoài điện trở; và "
               "thứ ba, các điện trở in dùng trong mạch lai, trong đó điện "
               "trở được in trên một nền cách điện bằng mực dẫn điện, được "
               "tạo ra bằng cách lắng đọng kim loại, hoặc được chế tạo theo "
               "cách tương tự rồi được phủ một lớp phủ bảo vệ cách điện hoặc "
               "được bọc kín."))
    # E2
    b.append(p("Các điện trở thành phần carbon thông thường có sẵn trên "
               "thị trường không phù hợp cho mục đích này vì kinh nghiệm cho "
               "thấy chúng có thể hỏng theo cách tạo ra các giá trị điện trở "
               "thấp hơn do các tạp chất được đưa vào carbon trong quá "
               "trình chế tạo."))

    b.append(h3("13.10.4 Tụ điện chặn", "13.10.4 Blocking capacitors"))
    # E3
    b.append(p("Khi các tụ điện được dùng để ngăn truyền dòng một chiều và "
               "được yêu cầu phải không hỏng, chỉ có thể dùng hai tụ điện "
               "trong mạch 'ia' để đạt được điều này, với điều kiện các tụ "
               "điện có độ tin cậy đủ. Điều này thực chất loại trừ các loại "
               "điện phân và tantalum và giới hạn lựa chọn ở các tụ có điện "
               "môi rắn như gốm, giấy, polyester và các vật liệu tương tự. "
               "Khi hai tụ điện có kiểu cấu tạo được chấp nhận được nối tiếp "
               "với nhau, chúng được coi là không hỏng và điện dung hiệu "
               "dụng sẽ là điện dung tồn tại nếu một trong hai bị hỏng thành "
               "ngắn mạch. Như vậy một hỏng hóc của một tụ điện được coi "
               "tương đương với hai lỗi có thể đếm được. Ngoài kiểu cấu tạo, "
               "mỗi tụ điện trong hai tụ còn phải chịu được các tình huống "
               "sau."))
    # E4
    b.append(p("Thứ nhất, mỗi tụ điện phải chịu được, không bị đánh thủng, "
               "điện áp xoay chiều rms 50 Hz và điện áp một chiều bằng "
               "2 U + 1000 V với giá trị tối thiểu 1500 V. Phép thử được "
               "thực hiện như đã mô tả trước đó cho các thử nghiệm chịu điện "
               "áp (tức là tăng điện áp đều đặn trong 10 giây rồi duy trì "
               "trong 60 giây) và, cũng như trước, dòng lớn nhất có thể chạy "
               "là 5 mA, phải đang giảm hoặc ổn định trong suốt 60 giây của "
               "phép thử. Đối với phép thử xoay chiều, dòng chạy qua đương "
               "nhiên sẽ phụ thuộc vào phản kháng của tụ điện, nhưng sự tăng "
               "dòng trong quá trình thử được coi là dấu hiệu hỏng hóc."))
    # E5 - continues on printed p.396.
    b.append(p("Thứ hai, khi các tụ điện được nối giữa mạch an toàn nội tại "
               "và đất, hoặc giữa các mạch an toàn nội tại riêng biệt, và "
               "hỏng xuống đất có thể tạo ra tình trạng không an toàn, ví dụ "
               "bằng cách vòng qua các linh kiện an toàn, thì điện áp thử ở "
               "trên phải được giảm xuống còn 2 U với giá trị tối thiểu "
               "500 V."))

    # Printed p.396 / BLOCK B.
    # E6 - continuation of E5.
    b.append(p("Trong cả hai trường hợp trên, cách lắp đặt các tụ điện phải "
               "tuân thủ Bảng 13.10 nếu cụm được coi là không hỏng đối với "
               "sự nối trực tiếp giữa hai mạch được tụ điện ngăn cách."))
    # E7
    b.append(p("Điện áp U quy định trong các thử nghiệm độ bền điện ở trên "
               "là điện áp lớn nhất có thể xuất hiện trên tổ hợp tụ điện "
               "khi sử dụng, trong trường hợp có tổ hợp tụ điện."))

    b.append(h3("13.10.5 Cụm an toàn song song",
                "13.10.5 Shunt safety assemblies"))
    # E8
    b.append(p("Cụm an toàn song song là cụm thường hạn chế sự phóng điện "
               "của các cuộn cảm (dùng các diode thường bị phân cực ngược) "
               "hoặc hạn chế điện áp trên các phần của mạch an toàn nội tại "
               "nhằm đảm bảo an toàn. Tác động hạn chế đó phải không hỏng và "
               "các cụm này được coi là không hỏng đối với hỏng hóc đứt mạch. "
               "Cách lắp đặt và đấu nối của các cụm này phải sao cho có thể "
               "bỏ qua khả năng đứt mạch của các dây nối (xem 13.10.6)."))
    # E9
    b.append(p("Các cụm an toàn song song chỉ dùng linh kiện bán dẫn vì cần "
               "phải tin tưởng rằng bản thân các linh kiện có tỉ lệ hỏng "
               "đứt mạch thấp và, gần như duy nhất, kiểu hỏng của một tiếp "
               "giáp bán dẫn là ngắn mạch hoặc điện trở thấp hơn, do sự suy "
               "giảm của tiếp giáp trong chất bán dẫn. Điều này cho phép "
               "giảm số phần tử của bảo vệ song song từ ba xuống hai trong "
               "mạch 'ia'."))
    # E10
    b.append(p("Cách dùng đặc biệt của thyristor gây ra vấn đề do thời gian "
               "hoạt động và năng lượng truyền qua kéo theo. Khi các linh "
               "kiện này được dùng làm cụm an toàn song song, năng lượng "
               "truyền qua này không được vượt quá các giới hạn sau:"))
    b.append(eq("IIA = 160 µJ<br>IIB = 80 µJ<br>IIC = 20 µJ"))
    # §6 quirk 2 - micro sign lost in OCR.
    b.append(note("<b>Lưu ý về dấu micro bị OCR đọc sai.</b> Bản in ghi "
                  "'160 µJ / 80 µJ / 20 µJ', '50 µs' và '35 µm'; lớp văn bản "
                  "OCR đọc thành '160pJ / 80~J / 20pJ', '50p' và '35 pm'. "
                  "Dấu µ được khôi phục theo bản in."))
    # §6 quirk 3 - IIA misread as IJA.
    b.append(note("<b>Lưu ý về nhóm IIA trong danh sách năng lượng truyền "
                  "qua.</b> Dòng OCR đọc 'IJA = 160pJ'; bản in rõ ràng ghi "
                  "'IIA'. Chữ 'IIA' được giữ theo bản in."))

    b.append(h4("Cụm an toàn song song hạn chế điện áp trong mạch an toàn "
                "nội tại",
                "Shunt safety assemblies which limit voltages within "
                "intrinsically safe circuits"))
    # E11
    b.append(p("Các cụm an toàn song song hạn chế điện áp là những cụm được "
               "đặt giữa nguồn cấp và mạch an toàn nội tại, giữa các mạch "
               "khác (ví dụ, các thiết bị nhận đầu ra) và mạch an toàn nội "
               "tại, hoặc được dùng để hạn chế thêm điện áp trong một mạch "
               "an toàn nội tại khi điện áp nguồn chính đã được xác định. "
               "Trong hai trường hợp đầu, phải giả định rằng các mạch bên "
               "ngoài chứa quá độ trừ khi nguồn cấp của chúng được cấp từ "
               "điện lưới qua một máy biến áp không hỏng hoặc là ắc quy. Khi "
               "bộ hạn chế điện áp đang xét không phải là bộ hạn chế điện áp "
               "chính (ví dụ, có một bộ hạn chế điện áp không hỏng khác giữa "
               "nó với mạch hoặc nguồn bên ngoài), cũng có thể giả định là "
               "không có quá độ."))
    # §6 quirk 17 - capitalisation shift in E11.
    b.append(note("<b>Lưu ý về chữ hoa ở đầu E11.</b> Câu đầu bản in bắt đầu "
                  "bằng 'Shunt Safety Assemblies which limit voltage...' "
                  "với chữ S hoa ở Safety Assemblies, dù tiêu đề ngay trên "
                  "được in ở dạng thường. Cách viết hoa được giữ nguyên."))

    # Printed p.397 / BLOCK C.
    # E12
    b.append(p("Bộ ổn áp, diode thyristor, diode zener và các linh kiện tương "
               "tự được phép sử dụng với điều kiện các mạch chứa chúng không "
               "có quá độ như mô tả ở trên. (Rõ ràng đây không phải là "
               "trường hợp khi các phần tử này được nối ở phía đầu ra của "
               "máy biến áp điện lưới hoặc được dùng để hạn chế điện áp đi "
               "vào mạch an toàn nội tại từ các mạch khác, vì sự thiếu xác "
               "định và kiểm soát của các nguồn và mạch đó làm không thể "
               "xác định được là không có quá độ.) Trong những trường hợp đó "
               "cần có hai đường song song riêng biệt, thường nghĩa là hai "
               "linh kiện hoặc cụm song song mắc song song với nhau. Mỗi "
               "linh kiện, cụm hoặc đường phải có khả năng chịu không chỉ "
               "điện áp cực đại được cấp cho nó và công suất cực đại mà nó "
               "có thể tiêu tán khi vận hành, mà còn phải chịu được dòng sẽ "
               "chạy qua nó nếu nó hỏng thành ngắn mạch (kiểu hỏng thông "
               "thường của chất bán dẫn). Điều này đặc biệt quan trọng đối "
               "với chất bán dẫn và các linh kiện tương tự, vì các dây nối "
               "bên trong liên kết vật liệu bán dẫn với các chân ra thường "
               "rất mảnh và dòng quá lớn có thể làm chảy chúng, nghĩa là một "
               "hỏng ngắn mạch sẽ dẫn tất yếu đến hỏng đứt mạch. Do yêu cầu "
               "không có quá độ, các linh kiện hoặc cụm này thường được thấy "
               "thực hiện các chức năng như hạn chế điện áp có thể xuất hiện "
               "trên một tụ điện trong mạch an toàn nội tại, cung cấp nguồn "
               "điện áp thấp hơn trong mạch đó khi điện áp chính đã được các "
               "linh kiện hoặc cụm khác xác định, hoặc hạn chế điện áp nguồn "
               "trong các nguồn dùng máy biến áp không hỏng để cách ly điện "
               "lưới. Lý do là các linh kiện như transistor và thyristor "
               "cùng các bộ ổn áp dùng những linh kiện đó không dập tắt hiệu "
               "quả các quá độ và có thể xảy ra tia lửa liên quan đến những "
               "quá độ đó. Trong Vùng 0, nơi các mạch 'ia' đi vào, sẽ có bầu "
               "khí quyển nổ trong phần lớn thời gian và điều đó là không "
               "được chấp nhận."))
    # §6 quirk 5 - "thyristors diodes".
    b.append(note("<b>Lưu ý về cụm 'thyristors diodes'.</b> Bản in viết "
                  "'Voltage regulator assemblies, thyristors diodes, zener "
                  "diodes...' thiếu dấu phẩy sau 'thyristors'. Cụm này được "
                  "giữ nguyên, không sửa thành 'thyristors, diodes'."))
    # E13
    b.append(p("Khi các linh kiện hoặc cụm an toàn song song được dùng để "
               "xác định điện áp trong những tình huống có thể có quá độ, "
               "chẳng hạn bên trong các nguồn không được cấp qua máy biến áp "
               "không hỏng, nơi có thể xuất hiện quá độ từ điện lưới, thì "
               "transistor, bộ ổn áp và thyristor không thể dùng trong mạch "
               "'ia' và lựa chọn hiệu quả còn lại chỉ là diode và diode "
               "zener. Một lần nữa, hai linh kiện hoặc cụm được coi là không "
               "hỏng nhưng trong những trường hợp này các phần tử dùng phải "
               "chịu được mọi quá độ có thể xảy ra. Trong một số trường hợp "
               "có thể xác định điều đó bằng cách so sánh thông số kỹ thuật "
               "của linh kiện với đặc tính thời gian của cầu chì để xác định "
               "kích thước và thời gian của quá độ và khả năng của linh kiện "
               "song song xử lý chúng mà không hư hỏng. Tuy nhiên, khi không "
               "thể làm vậy, cần thử nghiệm các linh kiện. Việc này được "
               "thực hiện bằng cách xác định dòng lớn nhất có thể chạy từ "
               "điện lưới hoặc nguồn khác, chia điện áp lớn nhất của nguồn "
               "cho giá trị nhỏ nhất của điện trở nguội của cầu chì cộng với "
               "mọi điện trở nối tiếp không hỏng khác hiện diện. Sau đó "
               "linh kiện bị tác động bằng năm xung dòng có biên độ đó, mỗi "
               "xung rộng 50 µs (hoặc bằng thời gian trước khi cầu chì cắt "
               "nếu thời gian đó tại dòng này dài hơn), cách nhau 20ms. Điện "
               "áp của linh kiện sau phép thử không được tăng quá 5 phần "
               "trăm."))
    # §6 quirk 6 - "20ms".
    b.append(note("<b>Lưu ý về '20ms'.</b> Bản in viết 'at intervals of "
                  "20ms' không có dấu cách trước đơn vị, trong khi các đơn "
                  "vị khác trong đoạn ('50 Hz', '60 seconds', '5 mA', "
                  "'50 µs') có dấu cách. Cách viết '20ms' được giữ nguyên."))

    # Printed p.398 / BLOCK D.
    b.append(h4("Cụm an toàn song song bảo vệ mạch và năng lượng linh kiện",
                "Circuit protection and component energy safety shunts"))
    # E14
    b.append(p("Nhìn chung các linh kiện này không hoạt động trong điều kiện "
               "bình thường mà chỉ hoạt động khi có sự cố ở nơi khác. Điều "
               "này không nhất thiết có nghĩa là chúng không dẫn điện hoặc "
               "không thực hiện một chức năng vận hành trong điều kiện bình "
               "thường, mà chỉ là chức năng an toàn nội tại của chúng không "
               "được gọi đến trong vận hành bình thường. Một lần nữa, hai "
               "linh kiện được chấp nhận với hạn chế như đối với cụm song "
               "song hạn chế điện áp khi có thể có quá độ, và giả định về quá "
               "độ như đã nêu ở trên. Không xét đến quá độ trong trường hợp "
               "này khi các linh kiện và cụm đó được dùng để hạn chế sự "
               "phóng điện của cuộn cảm hoặc điện áp xuất hiện trên tụ điện "
               "trong mạch an toàn nội tại."))

    b.append(h3("13.10.6 Dây dẫn và đầu nối bên trong",
                "13.10.6 Internal wiring and connections"))
    # E15
    b.append(p("Đã thảo luận ở phần trước rằng các cọc vít được chế tạo đúng "
               "cách có thể được giả định là không làm đứt dẫn dây của "
               "chúng, và các yêu cầu mà các cọc đó phải đáp ứng. Dĩ nhiên "
               "các cọc này cũng có thể dùng cho các nối bên trong và được "
               "coi là không chịu hỏng hóc (không hỏng). Tương tự, sự cần "
               "thiết phải dự phòng ở phích cắm và ổ cắm cho các nối đất đã "
               "cho thấy các nối đó không thể coi là không hỏng và phải chịu "
               "đếm lỗi bình thường. Bên trong, cần xem xét độ tin cậy của "
               "cách bố trí dây dẫn và đầu nối thông thường. Cả dây (và đường "
               "mạch in) lẫn các đầu nối của chúng đều có thể trở nên không "
               "hỏng bằng cách đạt đến một tiêu chuẩn cấu tạo tối thiểu."))

    b.append(h4("Dây và đường mạch in", "Wires and printed circuit tracks"))
    # E16
    b.append(p("Các yêu cầu cần thiết để dây đạt được tính không hỏng như "
               "sau. Thứ nhất, sự nối song song của hai dây được coi là "
               "không hỏng miễn là chúng đạt tiêu chuẩn cấu tạo thông "
               "thường. Điều này có nghĩa là không được có chuyển động rõ "
               "ràng hay cạnh sắc có thể làm giảm độ tin cậy và tăng nguy cơ "
               "đứt dây. Các biện pháp phòng ngừa trong vấn đề này không "
               "hơn gì những gì mong đợi trong thực hành công nghiệp tốt. "
               "Trong trường hợp này, mỗi dây được định mức về khả năng "
               "mang dòng với giả định dây kia đã hỏng."))
    # E17
    b.append(p("Thứ hai, có thể giảm còn một dây để đạt tính không hỏng khi "
               "dây đó có một lõi dẫn duy nhất đường kính ít nhất 0.5 mm, "
               "được cố định ngay tại mỗi điểm nối để tránh ứng suất tại "
               "điểm nối, và không có đoạn dài không được đỡ (đoạn không cố "
               "định) vượt quá 50 mm."))
    # §6 quirk 7 - OCR numeric construction rules.
    b.append(note("<b>Lưu ý về các giá trị cấu tạo bị OCR đọc sai.</b> Bản in "
                  "ghi '50 mm', '0.125 mm²' và '1 mm'; lớp OCR đọc thành "
                  "'50 111111', '0.125mm2' và 'lmm'. Các giá trị và dấu cách "
                  "được khôi phục theo bản in."))
    # E18 - continues on printed p.399.
    b.append(p("Thứ ba, một dây bện đơn chịu cùng yêu cầu cố định như một dây "
               "có lõi dẫn duy nhất, không yêu cầu kích thước tối thiểu của "
               "từng sợi, được chấp nhận là không hỏng, miễn là tổng diện "
               "tích tiết diện dẫn (tổng diện tích tiết diện của tất cả các "
               "sợi) lớn hơn 0.125 mm² (tương đương một dẫn thể đơn 0.4 mm). "
               "Diện tích này nhỏ hơn"))

    # Printed p.399 / BLOCK E.
    # E19 - continuation of E18.
    b.append(p("so với giá trị mong đợi đối với một dẫn thể đơn vì dây bện "
               "mềm hơn và ít có khả năng đứt dẫn hơn."))
    # E20
    b.append(p("Các yêu cầu đối với đường mạch in có khác đôi chút vì các "
               "đường này không chịu chuyển động theo cùng cách. Đúng là "
               "đường mạch in mềm có thể uốn cong nhưng phải chấp nhận các "
               "đường này tương tự như dây dẫn và áp dụng yêu cầu cho dây "
               "dẫn cho chúng. Đối với bảng mạch in cứng, các yêu cầu sau là "
               "cần thiết để đạt tính không hỏng. Thứ nhất, cần có độ dày "
               "tối thiểu của lớp đồng lắng đọng tạo thành đường mạch, và "
               "độ dày tối thiểu này là 35 µm. Các đường mỏng hơn giá trị "
               "này sẽ được coi là hỏng như một lỗi có thể đếm được nếu được "
               "định mức đúng. Thứ hai, hai đường mạch có độ dày ít nhất "
               "bằng giá trị nêu trên, mỗi đường có chiều rộng tối thiểu "
               "1 mm, được coi là không hỏng. Trong trường hợp này, mỗi "
               "đường cần được định mức để mang dòng sẽ chạy qua nếu đường "
               "kia bị đứt. Thứ ba, một đường mạch đơn có độ dày ít nhất "
               "bằng giá trị nêu trên được coi là không hỏng nếu chiều rộng "
               "của nó ít nhất bằng 1 phần trăm chiều dài, với giá trị tối "
               "thiểu 2 mm."))
    # E21
    b.append(p("Các dây và đường mạch cần được định mức trong các điều kiện "
               "đã nêu ở trên, giả định rằng phạm vi lỗi yêu cầu (cả lỗi có "
               "thể đếm được lẫn không đếm được) đã xảy ra trong thiết bị và "
               "cần áp dụng hệ số an toàn 1.5. Điều này có nghĩa là trong "
               "trường hợp cấu hình hai dẫn thể song song, dòng qua mỗi dẫn "
               "thể được xác định trong mọi điều kiện lỗi có thể rồi nhân "
               "với 1.5 để xác định định mức cần thiết cho dẫn thể."))

    b.append(h4("Dây nối và đầu nối", "Connections and connectors"))
    # E22
    b.append(p("Vì dây được coi là không hỏng trong một số trường hợp, các "
               "đầu nối của những dây này cũng phải có độ tin cậy tương tự, "
               "nếu không tính không hỏng của dây sẽ vô nghĩa. Như đã nêu, "
               "phích cắm và ổ cắm không đạt được mức an toàn đó và một số "
               "lỗi bình thường được áp dụng cho chúng, đòi hỏi ba nối song "
               "song. Đối với các nối ổn định hơn, có thể đạt tính không "
               "hỏng và để đạt được điều đó cần đáp ứng các yêu cầu sau."))
    # E23
    b.append(p("Thứ nhất, hai nối vĩnh cửu song song, chẳng hạn hai nối vặn "
               "vít, hai mối hàn thiếc hoặc hai nối quấn dây, luôn được coi "
               "là không hỏng miễn là chúng đáp ứng yêu cầu bình thường của "
               "thực hành công nghiệp tốt. Điều này khớp tốt với tình huống "
               "dùng hai dây song song hoặc hai đường mạch in, và đầu nối "
               "phải được định mức cho dòng lớn nhất có thể chạy qua nó, "
               "giả định nối kia đã bị đứt mạch. Thứ hai, một mối hàn đơn "
               "bằng hàn nóng chảy (welded), hàn đồng (brazed) hoặc ép "
               "(crimped) được chấp nhận là không hỏng."))
    # E24 - continues on printed p.400.
    b.append(p("Thứ ba, và là phương án thay thế, một mối hàn thiếc đơn được "
               "coi là không hỏng, miễn là nó còn được cố định cơ học thêm "
               "chống lại sự tách rời. Đối với dây, cách này ít mang lại lợi "
               "thế vì các phương pháp cố định bổ sung như ép (crimping) tự "
               "thân đã không hỏng, nhưng đối với các mối nối mạch in thì có "
               "lợi thế đáng kể. Nếu dây được luồn qua một lỗ mạ xuyên của "
               "bảng mạch rồi bẻ cong sang"))

    # Printed p.400 / BLOCK F. Fig. 13.28 sits above the continuation.
    b.append(fig(28, FE.fig_f1328()))
    # E25 - continuation of E24.
    b.append(p("phía bên kia (xem Hình 13.28), khi được hàn thiếc, chất hàn "
               "sẽ thấm vào lỗ ở một mức độ và tạo ra độ chắc chắn của mối "
               "nối cao hơn nhiều cùng với thể tích chất hàn lớn hơn dùng "
               "trên dây được bẻ cong. Khi dùng phương pháp hàn thiếc có độ "
               "tin cậy và khả năng lặp lại cao, chẳng hạn hàn bằng máy, thì "
               "không cần bẻ cong dây."))
    # E26
    b.append(p("Một mối nối vặn vít đơn (mối nối cọc) cũng được chấp nhận, "
               "miễn là nó đáp ứng yêu cầu đối với cọc nối đất đã mô tả "
               "trước đó trong chương này."))
    # E27
    b.append(p("Như trước, mỗi mối nối cần được định mức để mang dòng lớn "
               "nhất sẽ chạy trong các điều kiện lỗi đã được công nhận với "
               "hệ số an toàn 1.5. Điều này áp dụng cho mỗi mối nối khi dùng "
               "hai mối nối song song."))

    b.append(h3("13.10.7 Cách ly galva", "13.10.7 Galvanic separation"))
    # E28
    b.append(p("Cách ly galva (cách điện galva) thường được yêu cầu giữa mạch "
               "an toàn nội tại và mạch không an toàn nội tại để ngăn điện "
               "áp và dòng không chấp nhận được xuyên qua, giữa các mạch an "
               "toàn nội tại riêng biệt vì lý do tương tự, và giữa các điểm "
               "nối đất riêng biệt. Yêu cầu sau có thể được xem là hơi bất "
               "ngờ nhưng phải nhớ rằng trong trường hợp sự cố điện, dòng "
               "điện lớn có thể chạy trong các dây nối đất và điện áp tại "
               "một điểm gọi là nối đất có thể khác với điện áp tại điểm "
               "khác. Vì an toàn nội tại dựa trên việc kiểm soát năng lượng "
               "trong vùng nguy hiểm, một mạch được nối đất tại nhiều hơn "
               "một điểm có thể, do sự khác biệt của điện áp tại các điểm "
               "nối, có thêm vào nó một điện áp không xác định và về cơ bản "
               "không kiểm soát được. Do đó các mạch chỉ được nối đất tại "
               "một điểm hoặc không nối đất chút nào, dù trường hợp sau "
               "không phổ biến do những vấn đề liên quan đến việc tích điện "
               "của các mạch bị cách ly."))

    b.append(h4("Cách ly galva khỏi đất bằng cách cách điện",
                "Galvanic separation from earth by insulation"))
    # E29 - continues on printed p.401.
    b.append(p("Trừ khi có thể có nhiều hơn một điểm nối đất vòng qua một "
               "linh kiện an toàn khi các yêu cầu bình thường về cách điện "
               "và ngăn cách của nguyên lý được áp dụng, thì chỉ cần"))

    # Printed p.401 / BLOCK G.
    # E30 - continuation of E29.
    b.append(p("cách điện một mạch an toàn nội tại sao cho mạch chịu được "
               "điện áp thử cách điện xoay chiều ít nhất gấp hai lần điện áp "
               "mạch, với khả năng chịu tối thiểu 500 V rms. Khi có thể vòng "
               "qua các linh kiện an toàn, phải áp dụng yêu cầu của Bảng "
               "13.7."))
    # §6 quirk 8 - "Tables 13.7" plural.
    b.append(note("<b>Lưu ý về 'Tables 13.7'.</b> Bản in dùng số nhiều "
                  "'Tables 13.7' dù chỉ một bảng được đề cập. Chữ 'Tables' "
                  "được giữ nguyên, không sửa thành 'Table 13.7'."))
    # §6 quirk 26 - no tables in this span.
    b.append(note("<b>Lưu ý về việc không có bảng nào trong đoạn này.</b> "
                  "Dù Bảng 13.7 và Bảng 13.10 được trích dẫn lặp lại trong "
                  "văn bản, không bảng nào được in trên các trang 395–410. "
                  "Các lần trích dẫn chỉ là tham chiếu bằng văn bản, không "
                  "phải bảng được tái hiện."))

    b.append(h4("Cách ly galva giữa các mạch an toàn nội tại riêng biệt",
                "Galvanic separation between separate intrinsically safe "
                "circuits"))
    # E31
    b.append(p("Có thể đạt được sự ngăn cách giữa các mạch an toàn nội tại "
               "riêng biệt bằng cách cách điện hoặc ngăn cách giữa chúng "
               "dùng các phần tử như máy biến áp, rơle, optocoupler, tụ "
               "điện, v.v. Khi yêu cầu sự ngăn cách phải không hỏng, khoảng "
               "cách vật lý phải tuân thủ Bảng 13.7 hoặc phải dùng linh "
               "kiện, cụm không hỏng. Trong các trường hợp khác, yêu cầu "
               "bình thường của nguyên lý được áp dụng và hỏng hóc được coi "
               "là không đếm được hoặc là một lỗi có thể đếm được tùy theo "
               "cấu tạo hoặc khoảng cách ngăn cách."))
    # E32
    b.append(p("Optocoupler cũng được dùng để cách ly galva và chịu sự giảm "
               "định mức hai phần ba. Tuy nhiên, chúng không phải đáp ứng "
               "Bảng 13.7 nếu chịu được phép thử điện áp 2 U + 1000 V rms "
               "với giá trị tối thiểu 1500 V rms giữa các phần riêng biệt. "
               "Trong trường hợp này, U là định mức điện áp cao nhất do "
               "nhà sản xuất ghi cho linh kiện."))

    b.append(h4("Cách ly galva giữa mạch an toàn nội tại và mạch không an "
                "toàn nội tại",
                "Galvanic separation between intrinsically safe and "
                "non-intrinsically safe circuits"))
    # E33
    b.append(p("Ngăn cách bằng máy biến áp đã được xét khi bàn về máy biến áp "
               "không hỏng. Ngăn cách bằng rơle đã được xét một phần vì yêu "
               "cầu đối với tiếp điểm cuộn dây của rơle đã được xem xét. Tuy "
               "nhiên, cần nhắc lại rằng Bảng 13.7 áp dụng cho sự ngăn cách "
               "giữa bất kỳ hai phần tử nào của rơle (ví dụ, cuộn/tiếp điểm "
               "hoặc tiếp điểm/tiếp điểm để đạt được cách ly galva). Khi "
               "tiếp điểm của rơle nằm trong mạch không an toàn nội tại, "
               "điện áp được xét đã là điện áp điện lưới bình thường và mạch "
               "mà tiếp điểm được nối vào sẽ, nếu đáp ứng yêu cầu tiếp điểm "
               "VA tối đa trong vận hành bình thường, rất có thể có bảo vệ "
               "sự cố phù hợp để các định mức đó không bị vượt quá trong "
               "điều kiện sự cố. Cũng phải lưu ý rằng việc dùng những thứ "
               "như tăng khoảng cách hoặc hàng rào cho định mức VA cao hơn "
               "sẽ áp dụng khi sự ngăn cách là giữa các tiếp điểm riêng "
               "biệt, cũng như giữa cuộn và tiếp điểm. Ngoài ra, khi còn có "
               "bất kỳ sự nghi ngờ nào về định mức VA tối đa của các tiếp "
               "điểm trong điều kiện sự cố của mạch không an toàn nội tại "
               "mà chúng được nối vào, cần có bảo vệ như cầu chì trong các "
               "mạch tiếp điểm."))
    # §6 quirk 9 - "Also, where any doubt exists".
    b.append(note("<b>Lưu ý về chữ 'Also,' trong E33.</b> Lớp OCR đọc "
                  "'-41~0, where any doubt exists'; bản in rõ ràng ghi "
                  "'Also, where any doubt exists'. Chữ 'Also,' được khôi "
                  "phục theo bản in."))
    # §6 quirk 10 - "coillcontact".
    b.append(note("<b>Lưu ý về 'coil/contact'.</b> OCR đọc nhầm thành "
                  "'coillcontact'; bản in ghi '(e.g., coil/contact or "
                  "contact/contact...)'. Dấu gạch chéo được khôi phục theo "
                  "bản in."))
    # E34
    b.append(p("Ngăn cách bằng tụ điện chặn cũng là một khả năng nhưng một "
               "lần nữa các tụ điện phải đáp ứng yêu cầu không hỏng và các "
               "khoảng cách ngăn cách bên ngoài phải đáp ứng yêu cầu của "
               "Bảng 13.7."))
    # E35 - continues on printed p.402.
    b.append(p("Optocoupler được dùng cho mục đích cách ly galva nhưng thường "
               "nằm trong mạch điện áp thấp. Vì có khả năng của"))

    # Printed p.402 / BLOCK H.
    # E36 - continuation of E35.
    b.append(p("mạch không an toàn nội tại đang ở điện áp điện lưới do không "
               "được đánh giá, cần có một dạng bảo vệ nào đó cho optocoupler "
               "ngoài việc các phần riêng biệt của nó phải đáp ứng yêu cầu "
               "của Bảng 13.10. Điều này thường đạt được bằng cách dùng một "
               "diode zener song song qua các đầu nối không an toàn nội tại "
               "và bảo vệ nó bằng một cầu chì có định mức phù hợp. Tổ hợp "
               "cầu chì/diode zener được chọn theo cách giống như đối với "
               "cụm an toàn song song để đảm bảo cầu chì luôn cắt trước khi "
               "diode zener bị hư hỏng."))

    b.append(h3("13.11 Hàng rào an toàn diode",
                "13.11 Diode safety barriers"))
    # E37
    b.append(p("Được phát triển vào cuối những năm 1960, hàng rào an toàn "
               "diode (hay còn gọi là hàng rào zener song song) đã cung cấp "
               "một công cụ làm thay đổi hoàn toàn an toàn nội tại như một "
               "kỹ thuật. Thiết bị được thiết kế để lắp tại giao diện vùng "
               "nguy hiểm/vùng không nguy hiểm của một mạch an toàn nội tại "
               "và chống lại sự xuyên qua của điện áp nguy hiểm vào vùng "
               "nguy hiểm. Vì vậy, khi có thiết bị này, điện áp và dòng lớn "
               "nhất cần xét chính là điện áp và dòng truyền qua của chính "
               "thiết bị hàng rào, bất kể thiết bị được nối ở phía vùng không "
               "nguy hiểm. Như vậy, lần đầu tiên không cần dùng thiết bị "
               "liên kết được chế tạo đặc biệt và gần như mọi thiết bị công "
               "nghiệp thông thường đều dùng được, mang lại tính linh hoạt "
               "tăng rất nhiều và chi phí giảm đáng kể. Vấn đề duy nhất là "
               "sự cần thiết phải có nối đất an toàn của các thiết bị này, "
               "điểm nối đất của mạch an toàn nội tại vì thế bị bắt buộc, "
               "nhưng đây chỉ là vấn đề trong một tỉ lệ nhỏ trường hợp (như "
               "một số hệ thống phát thanh công cộng) và trong những trường "
               "hợp đặc biệt đó có thể chế tạo thiết bị liên kết riêng."))
    # §6 quirk 12 - "as it also known".
    b.append(note("<b>Lưu ý về 'as it also known'.</b> Bản in viết '(or shunt "
                  "zener barrier as it also known)' thiếu chữ 'is'. Cụm này "
                  "được giữ nguyên, không sửa thành 'as it is also known'."))
    # E38
    b.append(p("Thiết bị hàng rào ở dạng sớm nhất dựa vào đặc tính của diode "
               "zener hay diode thác lũ, dù là diode thường theo chiều thuận "
               "nhưng được chế tạo đặc biệt để chịu sự phá hủy thác lũ có "
               "thể phục hồi theo chiều ngược (xem Hình 13.29. Các linh kiện "
               "này được lắp ráp, như thể hiện trong Hình 13.30, để tạo "
               "thành một cụm chống lại sự xuyên qua của điện lưới (hoặc "
               "xuyên qua của nguồn cấp cho thiết bị ở phía không nguy hiểm) "
               "vào vùng nguy hiểm và xác định điện áp hở mạch cực đại, dòng "
               "ngắn mạch và công suất truyền qua lớn nhất sẵn có cho mạch "
               "trong vùng nguy hiểm. Hoạt động của thiết bị như sau:"))
    # §6 quirk 11 - unclosed parenthesis.
    b.append(note("<b>Lưu ý về dấu ngoặc không được đóng.</b> Câu trong bản "
                  "in bắt đầu '(see Fig. 13.29. These devices were "
                  "assembled...' nhưng dấu ngoặc mở không bao giờ được đóng. "
                  "Lỗi này của nguyên bản được giữ nguyên; không thêm dấu ')'."))
    # §6 quirk 15 - "let through power" vs "let-through energy".
    b.append(note("<b>Lưu ý về dấu gạch nối trong 'let through'.</b> E38 in "
                  "'and let through power' không có dấu gạch nối, trong khi "
                  "E10 và E38 dùng 'let-through energy'. Cả hai cách viết "
                  "được giữ nguyên theo từng vị trí."))
    # E39 - numbered item 1.
    b.append(p("1. Điện áp được kiểm soát bởi hai diode zener song song, Z1 "
               "và Z2 trong Hình 13.30, tạo thành một mạng hạn chế điện áp "
               "song song. Vì độ nhạy của các linh kiện này và việc chúng "
               "thường được bọc kín ở công đoạn cuối, các diode được thử "
               "định kỳ ở 150°C trong 2 giờ rồi thử xung dành cho bộ hạn chế "
               "điện áp song song."))
    # E40 - numbered item 2.
    b.append(p("2. Để tin tưởng vào tác động của các diode, chúng cần được "
               "bảo vệ bằng một cầu chì, F1 trong Hình 13.30, mang sự bảo vệ "
               "giống như cầu chì đã mô tả cho bộ hạn chế điện áp song song."))

    # Printed p.403 / BLOCK I. Fig. 13.29 at top of page.
    b.append(fig(29, FE.fig_f1329()))
    # E41 - numbered item 3.
    b.append(p("3. Một điện trở, R1 trong Hình 13.30, được đặt giữa các diode "
               "sao cho sau khi lắp ráp, khi không thể truy cập vào chúng, "
               "vẫn có thể thử sự hiện diện của chúng."))
    # E42 - numbered item 4, no full stop in the print.
    b.append(p("4. Một điện trở cuối cùng, R2 trong Hình 13.30, sau đó được "
               "đặt sau các diode zener để hạn chế dòng ngắn mạch tới vùng "
               "nguy hiểm ở mức an toàn tại điện áp diode zener cực đại"))
    # §6 quirk 16 - no full stop at end of item 4.
    b.append(note("<b>Lưu ý về mục số 4.</b> Mục 4 trong bản in kết thúc bằng "
                  "'maximum zener diode voltage' và không có dấu chấm. Không "
                  "thêm dấu chấm ở cuối mục này."))
    # E43
    b.append(p("Toàn bộ cụm sau đó được bọc kín hoặc chứa bằng một cách khác "
               "đảm bảo không thể tiếp cận các linh kiện mà không phá hủy "
               "hàng rào. Cụm cần được lắp một nối đất về thực chất không "
               "hỏng (hoặc một nối đơn không hỏng hoặc hai nối song song) "
               "chỉ dùng để nối đất hàng rào. Bất kỳ dây dẫn mạch nào đang ở "
               "điện thế đất không được dùng chung nối này mà phải có phương "
               "tiện nối riêng khác. Hệ thống lắp hàng rào cần làm cho việc "
               "lắp ngược là không thể, hoặc làm cho cách lắp đó quá rõ ràng "
               "để có thể giả định là không xảy ra. Điển hình cho các phương "
               "pháp này là lắp lệch dùng chính vị trí nối đất để gắn hàng "
               "rào lên thanh nối đất (phương pháp phổ biến nhất – xem Hình "
               "13.31) hoặc dùng then như đối với thanh cọc, chỉ cho phép "
               "lắp theo một hướng."))
    # E44 - continues on printed p.406.
    b.append(p("Hiện có hàng rào ở nhiều dạng khác nhau (xem Hình 13.32) và "
               "nhiều dải điện áp để đáp ứng hầu hết các yêu cầu có thể. Vấn "
               "đề là một khi hàng rào đã tác động trong chế độ bảo vệ của"))

    # Printed pp.404-405 / BLOCKS J and K. Figures only, no body prose.
    b.append(fig(30, FE.fig_f1330()))
    # §6 quirk 25 - Fig. 13.30 caption interleaving.
    b.append(note("<b>Lưu ý về dòng chú thích của Hình 13.30.</b> Ở lớp OCR, "
                  "chú thích bị cắt xen kẽ với các nhãn của đồ thị (dòng "
                  "17597–17603); thực tế chú thích là một đoạn văn liên tục "
                  "gồm cả hai Ghi chú (1) và (2) như đã tái hiện."))
    b.append(fig(31, FE.fig_f1331()))
    b.append(fig(32, FE.fig_f1332()))
    # §6 quirk 19 - two different Note 1 texts.
    b.append(note("<b>Lưu ý về hai Ghi chú 1 khác nhau trong Hình 13.32.</b> "
                  "Sơ đồ 2 kết thúc bằng '...if field wiring is s/c' (không "
                  "có dấu chấm), còn sơ đồ 3 kết thúc bằng '...if field wiring "
                  "is short circuit.' (có dấu chấm). Cả hai được giữ nguyên."))
    # §6 quirk 20 - R1 subscript in diagram 3.
    b.append(note("<b>Lưu ý về chỉ số R₁ trong Hình 13.32.</b> Phương trình "
                  "cuối của sơ đồ 3 in '2(V<sub>Z</sub> + V<sub>DIODE</sub>/"
                  "R₁)' với chỉ số 1, trong khi sơ đồ 2 in '± 2(V<sub>Z</sub> "
                  "+ V<sub>DIODE</sub>)/R₂' với chỉ số 2. Không chuẩn hóa "
                  "hai dạng này."))

    # Printed p.406 / BLOCK L.
    # E45 - continuation of E44.
    b.append(p("nó, thiết bị là đồ dùng một lần vì cầu chì bên trong đã cắt "
               "và do đó mạch bị hở. Để tránh điều này, hoàn toàn được phép "
               "lắp thêm một cầu chì có dòng cắt định mức thấp hơn nối tiếp "
               "với hàng rào ở phía vùng không nguy hiểm sao cho cầu chì này "
               "cắt trước cầu chì bên trong hàng rào."))
    # E46
    b.append(p("Cũng có sẵn các thiết bị hàng rào cung cấp cách ly galva và "
               "nhiều chức năng phức tạp hơn, và gần như tất cả các hệ thống "
               "an toàn nội tại hiện dùng đều sử dụng thiết bị hàng rào, "
               "xác nhận giá trị của chúng và cuộc cách mạng mà chúng đã "
               "tạo ra."))

    b.append(h3("13.12 Thông số đầu vào và đầu ra",
                "13.12 Input and output specifications"))
    # E47
    b.append(p("Do dải thiết bị an toàn nội tại rất rộng, cần xác định thiết "
               "bị nào có thể được nối với nhau. Vì mục đích đó, các thiết bị "
               "đều có thông số kèm theo và được yêu cầu ghi trên nhãn nếu "
               "có thể, nhưng dù sao vẫn phải đi kèm với thiết bị. Các thông "
               "số này khác nhau đối với thiết bị liên kết (kể cả hàng rào) "
               "và thiết bị an toàn nội tại."))
    # §6 quirk 13 - "Due to of the wide range".
    b.append(note("<b>Lưu ý về 'Due to of'.</b> Bản in bắt đầu 'Due to of the "
                  "wide range of intrinsically safe equipment...' với giới "
                  "từ bị lặp. Cụm này được giữ nguyên."))

    b.append(h4("Thiết bị liên kết", "Associated apparatus"))
    # E48
    b.append(p("Các thông số quan trọng của thiết bị liên kết như sau:"))
    b.append(h4("[ia] hoặc [ib]", "[ia] or [ib]"))
    # E49
    b.append(p("Thông số này xác định cấp an toàn nội tại và các ngoặc vuông "
               "cho biết thiết bị dùng để nối với thiết bị an toàn nội tại "
               "nhưng không định lắp trong vùng nguy hiểm. Tuy nhiên, thiết "
               "bị có thể được lắp trong vùng nguy hiểm nếu được bảo vệ bằng "
               "một phương pháp khác (ví dụ, bằng cách đặt trong vỏ chống "
               "cháy)."))
    b.append(h4("IIA, IIB hoặc IIC", "IIA, IIB or IIC"))
    # E50
    b.append(p("Thông số này cho biết phân nhóm và là chung với mọi loại bảo "
               "vệ khác."))
    b.append(h4("Uₘ", "Uₘ"))
    # E51
    b.append(p("Các cọc nguồn và cọc đầu ra của thiết bị liên kết được ghi "
               "Uₘ, là điện áp lớn nhất có thể nối vào các cọc đó mà không "
               "vi phạm an toàn nội tại. Thông thường người ta coi đây là "
               "điện áp nguồn cấp lớn nhất cho thiết bị được nối vào và "
               "thường giả định đó là điện áp điện lưới."))
    b.append(h4("U₀", "U₀"))
    # E52
    b.append(p("Đây là điện áp hở mạch lớn nhất mà thiết bị liên kết có thể "
               "cấp cho thiết bị an toàn nội tại được nối với nó. Thông số "
               "này xác định điện dung lớn nhất được phép trong mạch an toàn "
               "nội tại."))

    # Printed p.407 / BLOCK M.
    b.append(h4("I₀", "I₀"))
    # E53
    b.append(p("Đây là dòng ngắn mạch lớn nhất mà thiết bị liên kết có thể "
               "cấp cho vùng nguy hiểm và sẽ xác định độ tự cảm lớn nhất "
               "được chấp nhận trong mạch an toàn nội tại."))
    b.append(h4("P₀", "P₀"))
    # E54
    b.append(p("Đây là chỉ dẫn về công suất lớn nhất mà thiết bị liên kết "
               "có thể đưa vào vùng nguy hiểm. Thông số này cũng phần nào "
               "giúp xác định loại nguồn do thiết bị đó đại diện (ví dụ, "
               "giới hạn bằng điện trở hoặc giới hạn điện áp dòng không "
               "đổi)."))
    b.append(h4("L₀", "L₀"))
    # E55
    b.append(p("Thông số này quy định độ tự cảm lớn nhất có thể nối vào các "
               "cọc mạch an toàn nội tại của thiết bị liên kết, và do đó là "
               "độ tự cảm lớn nhất được chấp nhận cho tổ hợp cáp và thiết bị "
               "an toàn nội tại."))
    b.append(h4("C₀", "C₀"))
    # E56
    b.append(p("Thông số này quy định điện dung lớn nhất có thể nối vào các "
               "cọc mạch an toàn nội tại của thiết bị, và do đó là điện dung "
               "lớn nhất được chấp nhận của tổ hợp cáp nối và thiết bị an "
               "toàn nội tại."))
    # E57
    b.append(p("Các thông số này cho phép khả năng nối ghép lớn nhất giữa "
               "thiết bị liên kết và thiết bị an toàn nội tại mà không cần "
               "tính toán phức tạp. Thông số duy nhất khác đáng quan tâm là "
               "một thông số gọi là tỉ số Độ tự cảm/Điện trở (L₀/R₀), đo "
               "độ tự cảm lớn nhất trên một đơn vị điện trở có thể nối vào "
               "nguồn. Thông số này rất có giá trị vì người ta biết rằng khi "
               "chiều dài cáp tăng thì điện trở của cáp tăng và dòng giảm, "
               "nghĩa là độ tự cảm được phép tăng. Đối với nguồn giới hạn "
               "bằng điện trở (và phần lớn nguồn dùng trong an toàn nội tại "
               "thuộc loại này), có thể chứng minh thêm rằng năng lượng tích "
               "trữ cực đại xảy ra khi điện trở bên ngoài bằng điện trở của "
               "nguồn (xem Hình 13.33) và, nếu điều đó an toàn thì mọi tình "
               "huống khác cũng an toàn. Vì vậy, nếu áp dụng điều này cho "
               "cáp, không cần giới hạn chiều dài cáp mà nếu không sẽ bị áp "
               "đặt bởi độ tự cảm trên mỗi đơn vị chiều dài. Với bất kỳ tình "
               "huống nào, L₀/R₀ có thể được tính (xem Hình 13.34) và tỉ số "
               "này được cho bởi:-"))
    b.append(eq("L₀/R₀ = {8eRₓ + (64e²Rₓ² − 72U²eLₓ)^0.5}/4.5U      H/Ω"))
    b.append(p("trong đó  Rₓ = Điện trở của mạch không tính cáp  "
               "(Rₛ hoặc Rₛ + Rᵢ, tùy giá trị cho trường hợp xấu nhất)  Ω"
               "<br>U = Điện áp hở mạch của nguồn  V"
               "<br>Lₓ = Tổng giá trị độ tự cảm tập trung trong mạch  "
               "(Lₛ hoặc Lₛ + Lᵢ tùy giá trị cho trường hợp xấu nhất)  H"
               "<br>e = Năng lượng đánh lửa tối thiểu  J"))
    # §6 quirk 4 - subscript/superscript loss in OCR.
    b.append(note("<b>Lưu ý về mất chỉ số dưới và chỉ số trên trong OCR.</b> "
                  "Bản in dùng Rₓ, Rₛ, Rᵢ, Lₓ, Lₛ, Lᵢ, L₀, R₀, U₀, I₀, Uᵢ, "
                  "Iᵢ, Pᵢ, Lᵢ, Cᵢ, mm², 10⁻⁶, V₂ và V₁; lớp OCR làm phẳng "
                  "hết thành 'R,', 'Lo', 'U,,', 'loT6', '4 mm2'. Tất cả được "
                  "khôi phục theo bản in."))

    # Printed p.408 / BLOCK N. Fig. 13.33 at top of page.
    b.append(fig(33, FE.fig_f1333()))
    # E58
    b.append(p("Với mục đích của phép tính này, năng lượng tối thiểu được lấy "
               "từ các đường cong (xem Hình 13.35 và 13.36) và như sau:"))
    b.append(eq("IIA = 320 × 10⁻⁶       J<br>IIB = 160 × 10⁻⁶       J<br>"
                "IIC = 40 × 10⁻⁶        J"))
    # E59
    b.append(p("Khi không có độ tự cảm tập trung ở thiết bị liên kết lẫn "
               "thiết bị an toàn nội tại, công thức trên đơn giản hóa thành:"))
    b.append(eq("L₀/R₀ = 3.56eRₓ/U      H/Ω"))
    # E60 - continues on printed p.409.
    b.append(p("Đáng tiếc là không có phương pháp tương tự để xác định điện "
               "dung, dù rõ ràng điện trở cáp sẽ có tác động làm giảm"))

    # Printed p.409 / BLOCK O. Fig. 13.34 at top of page.
    b.append(fig(34, FE.fig_f1334()))
    # §6 quirk 18 - Fig. 13.34 key line 3.
    b.append(note("<b>Lưu ý về dòng thứ ba của chú giải Hình 13.34.</b> Bản in "
                  "ghi 'L₀ = Cable capacity (varies with length)' dùng chữ "
                  "'capacity' thay vì 'capacitance'. Các ký tự chỉ thiết bị "
                  "nhận trong hình giống 'L1'/'R1' nhưng trong chú giải là "
                  "Lᵢ/Rᵢ. Cả hai được giữ theo bản in."))
    # E61 - continuation of E60.
    b.append(p("tốc độ phóng điện dung. Vấn đề ở đây là cáp gồm một tập các "
               "điện trở nối tiếp và các tụ điện song song, phức tạp hơn "
               "nhiều để phân tích so với trường hợp cảm ứng, khi tất cả linh "
               "kiện đều nối tiếp. Vì vậy, trong hầu hết trường hợp, giới hạn "
               "chiều dài cáp sẽ là điện dung của cáp, dù kinh nghiệm cho "
               "thấy với cáp thông thường, vấn đề chiều dài cáp chỉ trở "
               "thành thực sự đáng kể trong trường hợp lắp đặt phân nhóm IIC, "
               "vì điện dung của IIA và IIB cho mọi mạch dưới 30 V, nơi phần "
               "lớn mạch an toàn nội tại được tập trung, đủ lớn để chứa bất "
               "kỳ chiều dài cáp hợp lý nào được yêu cầu."))
    # E62
    b.append(p("Đối với nguồn dòng không đổi giới hạn điện áp, việc tính L/R "
               "bề ngoài có vẻ khó hơn. Tuy nhiên, bằng cách dùng một đường "
               "tiếp tuyến như thể hiện trong Hình 13.35, có thể tính được "
               "và, dù kết quả hơi bị giới hạn, thông số này thường hữu ích "
               "để có."))
    # §6 quirk 14 - "as shown is Fig. 13.35".
    b.append(note("<b>Lưu ý về 'as shown is Fig. 13.35'.</b> Bản in dùng 'is' "
                  "thay vì 'in' trong cụm 'By using a tangent line as shown "
                  "is Fig. 13.35'. Lỗi này được giữ nguyên."))

    b.append(h4("Thiết bị an toàn nội tại",
                "Intrinsically safe apparatus"))
    # E63 - continues on printed p.410.
    b.append(p("Trong trường hợp thiết bị an toàn nội tại, các thông số cần "
               "thiết trong hầu hết trường hợp là các thông số bên trong "
               "thiết bị, vì thiết bị được nối vào một nguồn. Những gì bắt "
               "buộc phải ghi hoặc đề cập cho thiết bị là:"))
    # §6 quirk 24 - line-break hyphenation "appa-/ratus".
    b.append(note("<b>Lưu ý về gạch nối do ngắt dòng.</b> Ở cuối trang in 409 "
                  "và đầu trang in 410, chữ 'apparatus' bị ngắt thành "
                  "'appa-/ratus'. Đây là ngắt dòng, không phải gạch nối của "
                  "nguyên bản, nên được chép lại thành 'apparatus'."))

    # Printed p.410 / BLOCK P. Fig. 13.35 at top of page.
    b.append(fig(35, FE.fig_f1335()))
    # §6 quirk 21 - caption wordings across Figs. 13.34 and 13.35.
    b.append(note("<b>Lưu ý về cách ghi chú thích L/R.</b> Chú thích Hình "
                  "13.34 ghi 'Calculation of L/R ratio' (có 'ratio'), còn "
                  "chú thích Hình 13.35 ghi 'Calculation of L/R' (không có "
                  "'ratio'). Trong hình còn có 'Equivalent load line for "
                  "L/R calculation' và 'Equivalent circuit used for L/R "
                  "calculations' (số nhiều). Cả ba cách ghi được giữ nguyên."))
    # E64 - the five parameter definitions, verbatim.
    b.append(p("Uᵢ – điện áp lớn nhất mà một nguồn có thể đưa vào thiết bị;<br>"
               "Iᵢ – dòng ngắn mạch lớn nhất mà bất kỳ nguồn nào nối vào "
               "thiết bị có thể đưa ra;<br>"
               "Pᵢ – khả năng đưa công suất lớn nhất của bất kỳ nguồn nào nối "
               "vào thiết bị;<br>"
               "Lᵢ – độ tự cảm lớn nhất bên trong thiết bị xuất hiện trên "
               "các cọc đầu vào;<br>"
               "Cᵢ – điện dung bên trong lớn nhất xuất hiện trên các cọc đầu "
               "vào của thiết bị;"))
    # E65 - ends mid-sentence on printed p.410, continues on printed p.411.
    b.append(p("Độ tự cảm bên trong có thể được nêu thêm dưới dạng tỉ số L/R "
               "và đôi khi cách này hỗ trợ việc nối ghép. Ngoài ra, khi "
               "thiết bị là chẳng hạn bộ phát nhiệt độ và được nối với một "
               "phần tử sơ cấp ngoài việc nối với nguồn, U₀, I₀ và P₀ cũng "
               "có thể cần"))
    # §6 quirk 23 - printed page number 410.
    b.append(note("<b>Lưu ý về số trang 410.</b> Lớp OCR đọc số trang cuối "
                  "là '41 0'; bản in rõ ràng ghi '410'."))
    return "".join(b)


def body_en():
    b = []

    # §6 quirk 1 - brief/line-number mismatch.
    b.append(note("<b>Note on the brief/line-number mismatch.</b> The brief "
                  "states that line 17254 is === PAGE 416 ===; in the file "
                  "line 17254 is === PAGE 417 === and === PAGE 416 === is at "
                  "line 17208. The range 17208-17778 is used here so that "
                  "all 16 requested printed pages are included."))
    # §6 quirk 22 - running-header punctuation.
    b.append(note("<b>Note on the running-header punctuation.</b> Even "
                  "printed pages carry 'N Electrical installations in "
                  "hazardous areas'; odd pages carry 'Protection concept "
                  "intrinsic safety 'i' N'. The apostrophe in 'i' is straight "
                  "on pages 395, 399 and 405 and curly on pages 397, 401, "
                  "403, 407 and 409; the OCR of PDF 426 reads '7''. Running "
                  "headers belong to the page shell and are not part of this "
                  "body text."))

    # Printed p.395 / BLOCK A. E1 opens mid-paragraph from printed p.394.
    # E1
    b.append(p("current to a component for temperature classification "
               "purposes, or to limit discharge rates of otherwise ignition "
               "capable capacitors. These resistors need to be infallible "
               "against failure to a lower resistance value but may increase "
               "in resistance or become open circuit. In order to achieve "
               "this the resistors must be of particular types of "
               "construction as follows. First, carbon or metal film type, "
               "where the resistance element is effectively an insulated "
               "layer of pure carbon or metal deposited on a substrate which "
               "is normally ceramic or similar insulating material, helically "
               "etched to give the required resistance, and then protected by "
               "insulating enamel or varnish to prevent external contact "
               "with the element; second, wound in wire on a ceramic former "
               "or a former of similar material and then consolidated by "
               "enamelling, varnishing, etc., to prevent the wire from "
               "unwinding on breakage or being contacted from the outside of "
               "the resistor; and third, printed resistors used in hybrid "
               "circuits where the resistor is printed on an insulating "
               "substrate using conducting inks, produced by metal "
               "deposition, or constructed in a similar manner and then "
               "covered with an insulating conformal coating or "
               "encapsulated."))
    # E2
    b.append(p("The commonly available carbon composition resistors are not "
               "suitable for this use as experience has shown they can fail "
               "in a way which produces lower resistance values due to the "
               "impurities introduced into the carbon in their "
               "construction."))

    b.append(h3("13.10.4 Blocking capacitors", "13.10.4 Blocking capacitors"))
    # E3
    b.append(p("Where capacitors are used to prevent the transmission of dc "
               "and are required to be infallible it is possible to use only "
               "two capacitors in 'ia' circuits to achieve this, provided "
               "the capacitors are of sufficient reliability. This "
               "effectively excludes electrolytic and tantalum types and "
               "restricts the choice of capacitor to those with solid "
               "dielectrics such as ceramic, paper, polyester and similar "
               "materials. Where two capacitors of acceptable types of "
               "construction are connected in series they are considered as "
               "infallible and the effective capacitance will be that "
               "present if either of them fails to short circuit. Thus a "
               "single capacitor failure is equated to two countable faults. "
               "Apart from their construction type each of the two capacitors "
               "needs also to be proof against the following situations."))
    # E4
    b.append(p("First, each capacitor must withstand, without breakdown, a "
               "50 Hz rms ac and dc voltage of 2 U + 1000 V with a minimum "
               "of 1500 V. The test is applied as previously described for "
               "withstand tests (i.e., raising the voltage steadily over 10 "
               "seconds and then maintaining it over 60 seconds) and also, "
               "as previously, the maximum current which may flow is 5 mA "
               "which must be either falling or stable during the 60 seconds "
               "of the test. For the ac test the current passing will, of "
               "course, be dependent on the reactance of the capacitor but "
               "increases during the test are taken as a sign of failure."))
    # E5 - continues on printed p.396.
    b.append(p("Second, where the capacitors are connected between the "
               "intrinsically safe circuit and earth, or separate "
               "intrinsically safe circuits, and failure to earth could "
               "create an unsafe condition by, for example, by-passing safety "
               "components, the test voltage above should be reduced to "
               "2 U with a minimum of 500 V."))

    # Printed p.396 / BLOCK B.
    # E6 - continuation of E5.
    b.append(p("In both of the above cases the mounting of the capacitors "
               "must be such as to comply with Table 13.10 if the assembly "
               "is to be considered as infallible against direct "
               "interconnection of the two circuits separated by the "
               "capacitors."))
    # E7
    b.append(p("The voltage U, specified in the electric strength tests "
               "above, is the maximum voltage which can appear across the "
               "capacitor combination in service in the case of capacitor "
               "combinations."))

    b.append(h3("13.10.5 Shunt safety assemblies",
                "13.10.5 Shunt safety assemblies"))
    # E8
    b.append(p("A shunt safety assembly is one which typically limits "
               "discharge of inductors (using normally reverse biased "
               "diodes) or limits voltage across parts of intrinsically safe "
               "circuits so as to ensure safety. Such limiting action must "
               "be infallible and such assemblies are considered as "
               "infallible against open circuit failure. The mounting and "
               "connection of such assemblies needs to be such that open "
               "circuit of connections can be ignored (see Section 13.10.6)."))
    # E9
    b.append(p("Shunt safety assemblies are limited to semiconductor devices "
               "as it is necessary to have confidence that the devices "
               "themselves have a low rate of failure to open circuit and, "
               "almost uniquely, the mode of failure of a semiconductor "
               "junction is a short circuit or lower resistance as it "
               "results from degradation of the junction in the "
               "semiconductor. This permits the number of elements of the "
               "shunt protection to be reduced from three to two in 'ia' "
               "circuits."))
    # E10
    b.append(p("The particular use of thyristors presents a problem due to "
               "their operating time and resultant let-through energy. Where "
               "such devices are used as safety shunts this let-through "
               "energy must not exceed the following limits:"))
    b.append(eq("IIA = 160 µJ<br>IIB = 80 µJ<br>IIC = 20 µJ"))
    # §6 quirk 2 - micro sign lost in OCR.
    b.append(note("<b>Note on the micro sign lost in OCR.</b> The print reads "
                  "'160 µJ / 80 µJ / 20 µJ', '50 µs' and '35 µm'; the OCR text "
                  "layer reads '160pJ / 80~J / 20pJ', '50p' and '35 pm'. The "
                  "micro sign is restored as printed."))
    # §6 quirk 3 - IIA misread as IJA.
    b.append(note("<b>Note on IIA in the let-through list.</b> The OCR line "
                  "reads 'IJA = 160pJ'; the render clearly prints 'IIA'. "
                  "'IIA' is kept as printed."))

    b.append(h4("Shunt safety assemblies which limit voltages within "
                "intrinsically safe circuits",
                "Shunt safety assemblies which limit voltages within "
                "intrinsically safe circuits"))
    # E11
    b.append(p("Shunt Safety Assemblies which limit voltage are those which "
               "are interposed between power supplies and intrinsically safe "
               "circuits, between other circuits (e.g., output receptors) and "
               "intrinsically safe circuits, or used to further limit "
               "voltages within an intrinsically safe circuit where the "
               "principal supply voltage has already been defined. In the "
               "two former cases the external circuits must be assumed to "
               "contain transients unless their power supplies are fed from "
               "the mains via an infallible transformer or are batteries. "
               "Where the voltage limiter in question is not the prime "
               "voltage limiter (e.g., it has a further infallible voltage "
               "limiter between it and the external circuit or power supply) "
               "it can also be assumed that transients do not occur."))
    # §6 quirk 17 - capitalisation shift in E11.
    b.append(note("<b>Note on the capitalisation shift in E11.</b> The printed "
                  "sentence begins 'Shunt Safety Assemblies which limit "
                  "voltage...' with capitals on Safety Assemblies, although "
                  "the heading above is in sentence case. The capitalisation "
                  "is retained as printed."))

    # Printed p.397 / BLOCK C.
    # E12
    b.append(p("Voltage regulator assemblies, thyristors diodes, zener "
               "diodes, and similar devices are permissible provided the "
               "circuits in which they occur are free from transients as "
               "described above. (Clearly this is not the case where such "
               "elements are connected on the output side of mains "
               "transformers or used to limit voltages entering the "
               "intrinsically safe circuits from other circuits as the lack "
               "of definition and control of such supplies and circuits "
               "makes it impossible to identify freedom from transients.) In "
               "such cases there need to be two parallel shunt paths which "
               "normally means two of the shunt components or assemblies in "
               "parallel. Each shunt component, assembly or path needs to be "
               "able to withstand not only the maximum voltage with which it "
               "is supplied and the maximum power which it may dissipate in "
               "operation, but needs to be able to carry the current which "
               "would flow through it if it failed to short circuit (the "
               "normal mode of failure for semiconductors). This is "
               "particularly important in the case of semiconductors and "
               "similar devices, as the internal leads connecting the "
               "semiconductor material to the leads are usually very fine "
               "and excessive current could fuse them which would mean that "
               "a short circuit failure would inevitably lead to an open "
               "circuit failure. Because of the requirement for the absence "
               "of transients, these components or assemblies are normally "
               "to be found carrying out such functions as limiting the "
               "voltage which can occur across a capacitor within an "
               "intrinsically safe circuit, providing a lower voltage supply "
               "in such a circuit where the principal voltage has already "
               "been defined by other components or assemblies, or limiting "
               "power supply voltages in power supplies using infallible "
               "transformers to provide mains isolation. The reason for this "
               "is that devices such as transistors and thyristors and "
               "voltage regulators using such devices do not effectively "
               "quench transients and sparking associated with such "
               "transients could occur. In Zone 0, where 'ia' circuits enter, "
               "there will be an explosive atmosphere for much of the time "
               "and this is not acceptable."))
    # §6 quirk 5 - "thyristors diodes".
    b.append(note("<b>Note on 'thyristors diodes'.</b> The print reads "
                  "'Voltage regulator assemblies, thyristors diodes, zener "
                  "diodes...' without a comma after 'thyristors'. The wording "
                  "is kept exactly, not corrected to 'thyristors, diodes'."))
    # E13
    b.append(p("Where the shunt safety components or assemblies are used to "
               "define voltages in situations where transients are possible, "
               "such as within power supplies not fed from infallible "
               "transformers where mains-borne transients can occur, "
               "transistors, voltage regulators and thyristors cannot be used "
               "in 'ia' circuits and the only effective options left are "
               "diodes and zener diodes. Again two components or assemblies "
               "are considered as infallible but in such cases the elements "
               "used have to withstand any transients which may occur. In "
               "some cases this can be determined by comparing the component "
               "specification with the fuse/time characteristic to determine "
               "the size and duration of transients and the ability of the "
               "shunt component to deal with them without damage. Where this "
               "is not the case, however, it is necessary to test the "
               "devices. This is done by determining the maximum current "
               "which can flow from the mains or other power source by "
               "dividing its maximum voltage by the minimum value for the "
               "cold resistance of the fuse and any other infallible series "
               "resistance present. The device is then subjected to five "
               "current pulses of that amplitude, each 50 µs wide (or if the "
               "fuse pre-arcing time at that current is longer the pre-arcing "
               "time) at intervals of 20ms. The voltage of the device after "
               "that test must not have risen by more than 5 per cent."))
    # §6 quirk 6 - "20ms".
    b.append(note("<b>Note on '20ms'.</b> The print writes 'at intervals of "
                  "20ms' with no space before the unit, while other units in "
                  "the same span ('50 Hz', '60 seconds', '5 mA', '50 µs') do "
                  "have a space. The spelling '20ms' is kept as printed."))

    # Printed p.398 / BLOCK D.
    b.append(h4("Circuit protection and component energy safety shunts",
                "Circuit protection and component energy safety shunts"))
    # E14
    b.append(p("In general, these devices do not operate normally but only "
               "in case of a fault elsewhere. This does not necessarily mean "
               "that they do not normally conduct or perform an operational "
               "function but only that their intrinsic safety function is "
               "not called upon in normal operation. Again, two devices are "
               "acceptable with the restriction as for voltage limiting "
               "shunts where transients may occur and the assumption of "
               "transients as already specified. Transients are not "
               "considered in this case when such components and assemblies "
               "are used to limit discharge of inductors or voltage appearing "
               "across capacitors in intrinsically safe circuits."))

    b.append(h3("13.10.6 Internal wiring and connections",
                "13.10.6 Internal wiring and connections"))
    # E15
    b.append(p("It has already been discussed how properly constructed screw "
               "terminals may be assumed not to allow disconnection of their "
               "conductors and the requirements which such terminals must "
               "satisfy. These terminals can, of course, also be used for "
               "internal connection and will be considered as not subject to "
               "fault (infallible). Likewise, the need for redundancy in "
               "plugs and sockets for earth connections has shown that such "
               "connections cannot be considered as infallible and need to "
               "be subjected to the normal fault count. Internally the normal "
               "wiring and connection arrangements need addressing as to "
               "their reliability. Both wires (and printed circuit tracks) "
               "and their end connections can be made infallible by reaching "
               "a minimum standard of construction."))

    b.append(h4("Wires and printed circuit tracks",
                "Wires and printed circuit tracks"))
    # E16
    b.append(p("The necessary requirements for wires to achieve "
               "infallibility are as follows. First, an interconnection of "
               "two wires in parallel is considered as infallible provided "
               "that they reach normal standards of construction. This means "
               "that there must be no obvious movement or sharp edges which "
               "could be expected to reduce their reliability and increase "
               "the risk of their breaking. The precautions taken in this "
               "regard are no more than would be expected in good industrial "
               "practice. In this case each wire will be rated for current "
               "carrying capacity assuming the other has failed."))
    # E17
    b.append(p("Second, the connection may be reduced to one wire for "
               "infallibility where the wire has a single conductor of at "
               "least 0.5 mm diameter, is secured adjacent to each point of "
               "connection to avoid stresses at the connection point, and "
               "has no unsupported length (unsecured length) which exceeds "
               "50 mm."))
    # §6 quirk 7 - OCR numeric construction rules.
    b.append(note("<b>Note on the construction numbers garbled by OCR.</b> "
                  "The print reads '50 mm', '0.125 mm²' and '1 mm'; the OCR "
                  "text layer reads '50 111111', '0.125mm2' and 'lmm'. The "
                  "values and spacing are restored as printed."))
    # E18 - continues on printed p.399.
    b.append(p("Third, a single stranded wire subject to the same fixing "
               "requirements as a single wire with a single conductor "
               "without any minimum size of strand is accepted as "
               "infallible, provided the total conductor cross sectional "
               "area (the addition of the cross sectional area of all of the "
               "strands) is greater than 0.125 mm² (equivalent to a 0.4 mm "
               "single conductor). This area is less"))

    # Printed p.399 / BLOCK E.
    # E19 - continuation of E18.
    b.append(p("than would be expected for a single conductor as stranded "
               "wires are more flexible and less prone to conductor "
               "breakage."))
    # E20
    b.append(p("The requirements for printed circuit tracks are a little "
               "different as such tracks are not subject to movement in the "
               "same way. It is true that flexible printed circuit tracks "
               "can flex but these must be accepted as similar to wiring and "
               "the requirements for wiring will apply to these. For rigid "
               "printed circuit boards the following requirements are "
               "necessary for infallibility. First, a minimum thickness of "
               "deposited copper forming the track is necessary and this "
               "minimum is 35 µm. Tracks of less than this thickness will be "
               "considered to fail as a single countable fault if properly "
               "rated. Second, two tracks of at least the above thickness, "
               "each having a minimum width of 1 mm, are considered as "
               "infallible. In this case each track needs to be rated to "
               "carry the current which would flow if the other track were "
               "broken. Third, a single track of at least the above thickness "
               "is considered as infallible if it has a width of at least "
               "1 per cent of its length, with a minimum of 2 mm."))
    # E21
    b.append(p("The wires and tracks require to be rated in the conditions "
               "stated above assuming the required range of faults (both "
               "countable and non-countable) have occurred in the apparatus "
               "and the 1.5 safety factor needs to be applied. This means "
               "that in the case of a two parallel conductor configuration, "
               "the current through each conductor will be determined in all "
               "possible fault conditions and then multiplied by 1.5 to "
               "determine the necessary rating for the conductor."))

    b.append(h4("Connections and connectors",
                "Connections and connectors"))
    # E22
    b.append(p("As wires are deemed to be infallible in certain circumstances "
               "the end connections of these wires must also have that "
               "credibility or the infallibility of wires would be pointless. "
               "As already stated, plugs and sockets cannot attain this level "
               "of security and a normal fault count is applied to these "
               "requiring three parallel connections. For more stable "
               "connections infallibility is possible and, to achieve this, "
               "the following requirements need to be met."))
    # E23
    b.append(p("First, two permanent connections in parallel, such as two "
               "screwed connections, two soldered joints or two wire wrapped "
               "connections are always considered as infallible provided "
               "they satisfy the normal requirements of good industrial "
               "practice. This matches up well with the situation where two "
               "parallel wires or printed circuit tracks are used and the "
               "connection must be rated for the maximum current which could "
               "flow in it, assuming the other connection has become open "
               "circuit. Second, a single welded, brazed or crimped joint is "
               "accepted as infallible."))
    # E24 - continues on printed p.400.
    b.append(p("Third, and alternatively, a single soldered joint is "
               "considered as infallible, provided it is additionally "
               "mechanically secured against separation. For wires this "
               "offers little advantage as the methods of additional "
               "securing, such as crimping, are infallible in themselves but "
               "for printed circuit joints considerable advantage exists. If "
               "the wire is inserted through a plated-through hole in the "
               "printed circuit board and then bent over on the other"))

    # Printed p.400 / BLOCK F. Fig. 13.28 sits above the continuation.
    b.append(fig(28, FE.fig_f1328()))
    # E25 - continuation of E24.
    b.append(p("side (see Fig. 13.28), when it is soldered the solder will "
               "penetrate the hole to a degree and give much more security "
               "of joint together with the larger volume of solder used on "
               "the bent conductor. Where a high reliability and "
               "repeatability form of soldering, such as machine soldering, "
               "is used then bending over the wire is not necessary."))
    # E26
    b.append(p("A single screwed type joint (terminal joint) is also "
               "acceptable, provided that it satisfies the requirements for "
               "earth connection terminals described earlier in this "
               "chapter."))
    # E27
    b.append(p("As before, each joint needs to be rated to carry the maximum "
               "current which would flow in the recognized conditions of "
               "fault with a safety factor of 1.5. This applies to each joint "
               "where two parallel joints are used."))

    b.append(h3("13.10.7 Galvanic separation",
                "13.10.7 Galvanic separation"))
    # E28
    b.append(p("Galvanic separation (galvanic isolation) is often required "
               "between intrinsically safe and non-intrinsically safe "
               "circuits to prevent breakthrough of unacceptable voltages "
               "and currents, between separate intrinsically safe circuits "
               "for the same reasons, and between separate earths. This "
               "latter requirement may be considered as somewhat surprising "
               "but it must be borne in mind that in cases of electrical "
               "fault heavy electrical currents can flow in earth "
               "connections, and the voltage at one so-called grounded point "
               "can be different to that at another. As intrinsic safety "
               "relies upon control of energy in the hazardous area, a circuit "
               "which is connected to earth at more than one point may, due "
               "to different voltages existing at its points of connection, "
               "have added into it an unknown and essentially uncontrolled "
               "voltage. Thus circuits are earthed at only one point or not "
               "at all, although the latter is not common due to the problems "
               "associated with charging of isolated circuits."))

    b.append(h4("Galvanic separation from earth by insulation",
                "Galvanic separation from earth by insulation"))
    # E29 - continues on printed p.401.
    b.append(p("Unless more than one earth can by-pass a safety component "
               "when the normal insulation and separation requirements of "
               "the concept apply, it"))

    # Printed p.401 / BLOCK G.
    # E30 - continuation of E29.
    b.append(p("is only necessary to insulate an intrinsically safe circuit "
               "so that it will withstand an ac insulation test voltage of "
               "at least twice the circuit voltage with a minimum withstand "
               "of 500 V rms. Where safety components may be by-passed, the "
               "requirements of Tables 13.7 must be applied."))
    # §6 quirk 8 - "Tables 13.7" plural.
    b.append(note("<b>Note on 'Tables 13.7'.</b> The print uses the plural "
                  "'Tables 13.7' although only one table is meant. 'Tables' "
                  "is retained and is not changed to 'Table 13.7'."))
    # §6 quirk 26 - no tables in this span.
    b.append(note("<b>Note on the absence of tables in this span.</b> Although "
                  "Table 13.7 and Table 13.10 are repeatedly cited in the "
                  "text, no table is printed on pp.395-410. The citations are "
                  "prose references only, not reproduced table elements."))

    b.append(h4("Galvanic separation between separate intrinsically safe "
                "circuits",
                "Galvanic separation between separate intrinsically safe "
                "circuits"))
    # E31
    b.append(p("Separation between separate intrinsically safe circuits may "
               "be achieved by insulation or separation between them using "
               "such elements as transformers, relays, optocouplers, "
               "capacitors, etc. Where the separation is required to be "
               "infallible, the physical separation must comply with Table "
               "13.7 or infallible components or assemblies must be used. In "
               "other cases, the normal requirements of the concept apply "
               "and failure is taken as non-countable or a countable fault "
               "according to the construction or separation."))
    # E32
    b.append(p("Optocouplers are also used for galvanic separation and are "
               "subject to the two thirds rating reduction. They will not "
               "have to satisfy Table 13.7, however, if they withstand a "
               "voltage test of 2 U + 1000 V rms with a minimum of 1500 V rms "
               "between their separate parts. In this case, U is the highest "
               "manufacturers voltage rating for the device."))

    b.append(h4("Galvanic separation between intrinsically safe and "
                "non-intrinsically safe circuits",
                "Galvanic separation between intrinsically safe and "
                "non-intrinsically safe circuits"))
    # E33
    b.append(p("Separation by transformers has already been dealt with in "
               "consideration of infallible transformers. Separation by "
               "relays has been partially dealt with in that the coil contact "
               "requirements for relays have already been considered. It is "
               "necessary, however, to remind ourselves that Table 13.7 "
               "applies to the separation between any two elements of the "
               "relay (e.g., coil/contact or contact/contact to achieve "
               "galvanic separation). Where the contacts of the relay are in "
               "the non-intrinsically safe circuit, the voltage considered "
               "is already the normal mains voltage and the circuit to which "
               "the contacts are connected will, if satisfying the maximum "
               "VA contact requirements in normal operation, in all "
               "probability have suitable fault protection so that these "
               "ratings are not exceeded in fault conditions. It must also "
               "be noted that the use of such things as increased separations "
               "or barriers for higher VA ratings will apply where the "
               "separation is between separate contacts, as well as between "
               "coil and contacts. Also, where any doubt exists as to the "
               "maximum VA rating of the contacts in conditions of fault in "
               "the non-intrinsically safe circuits to which they are "
               "connected, protection such as fusing will be necessary in "
               "the contact circuits."))
    # §6 quirk 9 - "Also, where any doubt exists".
    b.append(note("<b>Note on 'Also, where any doubt exists'.</b> The OCR at "
                  "line 17488 reads '-41~0, where any doubt exists'; the "
                  "render clearly reads 'Also, where any doubt exists'. The "
                  "printed word 'Also,' is restored."))
    # §6 quirk 10 - "coillcontact".
    b.append(note("<b>Note on 'coil/contact'.</b> The OCR reads "
                  "'coillcontact'; the print reads '(e.g., coil/contact or "
                  "contact/contact...)'. The slash is restored as printed."))
    # E34
    b.append(p("Separation by blocking capacitors is also a possibility but "
               "again the capacitors must satisfy the requirements for "
               "infallibility and the external separations must satisfy the "
               "requirements of Table 13.7."))
    # E35 - continues on printed p.402.
    b.append(p("Optocouplers are used for the purposes of galvanic separation "
               "but are usually in low voltage circuits. As there is a "
               "possibility of the"))

    # Printed p.402 / BLOCK H.
    # E36 - continuation of E35.
    b.append(p("non-intrinsically safe circuit being at mains potential "
               "because it is not evaluated, some form of protection for the "
               "optocoupler will be necessary in addition to the separation "
               "of its two parts having to meet Table 13.10 requirements. "
               "This is normally achieved by using a shunt zener diode across "
               "the non-intrinsically safe connections and protecting it with "
               "a suitable rated fuse. The fuse/zener diode combination is "
               "chosen in the same way as for safety shunts to ensure that "
               "the fuse will always clear before the zener diode is "
               "damaged."))

    b.append(h3("13.11 Diode safety barriers",
                "13.11 Diode safety barriers"))
    # E37
    b.append(p("Developed in the late 1960s the diode safety barrier (or "
               "shunt zener barrier as it also known) provided a tool which "
               "revolutionized intrinsic safety as a technique. The device "
               "was designed to fit at the hazardous area/non-hazardous area "
               "interface of an intrinsically safe circuit and be proof "
               "against breakthrough of dangerous voltages into the "
               "hazardous area. When one is fitted, therefore, the maximum "
               "voltage and current which needs to be considered is the "
               "let-through voltage and current of the barrier device "
               "whatever the apparatus connected on the non-hazardous area "
               "side of the device. Thus, for the first time, it was not "
               "necessary to use specially constructed associated apparatus "
               "and almost any normal industrial apparatus was usable "
               "resulting in great increases in flexibility and decreases in "
               "cost. The only problem was the necessity for the devices to "
               "have safety earths which dictated the point at which the "
               "intrinsically safe circuit was earthed, but this was only a "
               "problem in a small minority of cases (such as some public "
               "address systems) and in these special associated apparatus "
               "could be constructed."))
    # §6 quirk 12 - "as it also known".
    b.append(note("<b>Note on 'as it also known'.</b> The print reads '(or "
                  "shunt zener barrier as it also known)', missing the word "
                  "'is'. The wording is kept as printed, not corrected to "
                  "'as it is also known'."))
    # E38
    b.append(p("The barrier device in its earliest form relied on the "
               "characteristics of the zener or avalanche diode which, "
               "although a normal diode in the forward direction was "
               "specially constructed so that it suffered recoverable "
               "avalanche breakdown in the reverse direction (see Fig. 13.29. "
               "These devices were assembled, as shown in Fig. 13.30, to form "
               "an assembly which was proof against mains breakthrough (or "
               "breakthrough of the supplies to the apparatus on the "
               "non-hazardous side) into the hazardous area and define the "
               "maximum open circuit voltage, short circuit current, and let "
               "through power available to the circuit in the hazardous "
               "area. The operation of the device is as follows:"))
    # §6 quirk 11 - unclosed parenthesis.
    b.append(note("<b>Note on the unclosed parenthesis.</b> The printed "
                  "sentence begins '(see Fig. 13.29. These devices were "
                  "assembled...' and the opening parenthesis is never "
                  "closed. The source error is preserved; no ')' is added."))
    # §6 quirk 15 - "let through power" vs "let-through energy".
    b.append(note("<b>Note on 'let through' hyphenation.</b> E38 prints 'and "
                  "let through power' without a hyphen, whereas E10 and E38 "
                  "use 'let-through energy'. Each spelling is kept at its "
                  "own place."))
    # E39 - numbered item 1.
    b.append(p("1. The voltage is controlled by two shunt zener diodes, Z1 "
               "and Z2 in Fig. 13.30, forming a shunt voltage limiting "
               "network. Because of the sensitivity of such devices and "
               "their usual ultimate encapsulation, the diodes are routinely "
               "subjected to a 150°C storage test for 2 hours and then the "
               "pulse test for shunt voltage limiters."))
    # E40 - numbered item 2.
    b.append(p("2. To allow confidence in the action of the diodes they need "
               "to be protected by a fuse, F1 in Fig. 13.30, offering the "
               "same protection as the fuse described for shunt voltage "
               "limiters."))

    # Printed p.403 / BLOCK I. Fig. 13.29 at top of page.
    b.append(fig(29, FE.fig_f1329()))
    # E41 - numbered item 3.
    b.append(p("3. A resistor, R1 in Fig. 13.30, is placed between the diodes "
               "so that after assembly, when they cannot be accessed, it is "
               "still possible to test for their presence."))
    # E42 - numbered item 4, no full stop in the print.
    b.append(p("4. A final resistor, R2 in Fig. 13.30, is then placed after "
               "the zener diodes to limit the short circuit current to the "
               "hazardous area to a safe level at the maximum zener diode "
               "voltage"))
    # §6 quirk 16 - no full stop at end of item 4.
    b.append(note("<b>Note on numbered item 4.</b> Item 4 ends with 'maximum "
                  "zener diode voltage' in the print and carries no full "
                  "stop. No full stop is added."))
    # E43
    b.append(p("The whole is then encapsulated or enclosed by some other "
               "means which ensures that access to the components will not "
               "be possible without destroying the barrier. The assembly "
               "needs to be fitted with an earth connection which is "
               "effectively infallible (either a single infallible connection "
               "or two connections in parallel) which is used to earth the "
               "barrier only. Any circuit conductors which are at earth "
               "potential may not share this connection but must have other "
               "separate connection facilities. Mounting systems for barriers "
               "need to make it impossible for them to be reverse mounted or "
               "make such mounting so obvious that it can be assumed not to "
               "occur. Typical of such methods is asymmetrical mounting using "
               "the earth connection facility to effect mounting on the earth "
               "bar (the most common method – see Fig. 13.31) or keying such "
               "as used for terminal rails where it is only possible to mount "
               "in one orientation."))
    # E44 - continues on printed p.406.
    b.append(p("Barrier devices are now available in a wide variety of "
               "formats (see Fig. 13.32) and a wide range of voltages to "
               "cater for most possible requirements. The problem is that "
               "once the barrier has acted in its protective"))

    # Printed pp.404-405 / BLOCKS J and K. Figures only, no body prose.
    b.append(fig(30, FE.fig_f1330()))
    # §6 quirk 25 - Fig. 13.30 caption interleaving.
    b.append(note("<b>Note on the Fig. 13.30 caption line-break.</b> In the "
                  "OCR text layer the caption is interleaved with the graph "
                  "labels (lines 17597-17603); the caption itself is "
                  "continuous prose with both Notes (1) and (2), as "
                  "reproduced here."))
    b.append(fig(31, FE.fig_f1331()))
    b.append(fig(32, FE.fig_f1332()))
    # §6 quirk 19 - two different Note 1 texts.
    b.append(note("<b>Note on the two Note 1 texts in Fig. 13.32.</b> "
                  "Diagram 2 ends '...if field wiring is s/c' with no final "
                  "full stop; diagram 3 ends '...if field wiring is short "
                  "circuit.' with one. Both are preserved verbatim."))
    # §6 quirk 20 - R1 subscript in diagram 3.
    b.append(note("<b>Note on the R₁ subscript in Fig. 13.32.</b> The last "
                  "equation of diagram 3 prints '2(V<sub>Z</sub> + "
                  "V<sub>DIODE</sub>/R₁)' with subscript 1, while diagram 2 "
                  "prints '± 2(V<sub>Z</sub> + V<sub>DIODE</sub>)/R₂' with "
                  "subscript 2. The two are not harmonised."))

    # Printed p.406 / BLOCK L.
    # E45 - continuation of E44.
    b.append(p("mode, it is a throw-away item as its fuse will have operated "
               "and thus it will be open circuit. To prevent this it is "
               "perfectly acceptable to insert a fuse of lower rated "
               "rupturing current in series with the barrier on the "
               "non-hazardous area side so that it will rupture before that "
               "in the barrier."))
    # E46
    b.append(p("Barrier devices offering galvanic isolation and many other "
               "more complex functions are also available, and almost all of "
               "the intrinsically safe installations now used utilize "
               "barrier devices which confirms their value and the revolution "
               "which they produced."))

    b.append(h3("13.12 Input and output specifications",
                "13.12 Input and output specifications"))
    # E47
    b.append(p("Due to of the wide range of intrinsically safe equipment it "
               "is necessary to identify that which can be interconnected. "
               "To this end items of apparatus have specifications which "
               "accompany them and are required to be identified on their "
               "labels if possible, but in any event to accompany them. These "
               "differ for associated apparatus (including barriers) and "
               "intrinsically safe apparatus."))
    # §6 quirk 13 - "Due to of the wide range".
    b.append(note("<b>Note on 'Due to of'.</b> The print begins 'Due to of the "
                  "wide range of intrinsically safe equipment...' with a "
                  "duplicated preposition. The wording is retained as "
                  "printed."))

    b.append(h4("Associated apparatus", "Associated apparatus"))
    # E48
    b.append(p("The important parameters for associated apparatus are as "
               "follows:"))
    b.append(h4("[ia] or [ib]", "[ia] or [ib]"))
    # E49
    b.append(p("This identifies the level of intrinsic safety and the square "
               "brackets indicate that the apparatus is for connection to "
               "intrinsically safe apparatus but is not intended for "
               "hazardous area mounting. It may be hazardous area mounted if, "
               "however, it is protected by another method (e.g., by being "
               "placed in a flameproof enclosure)."))
    b.append(h4("IIA, IIB or IIC", "IIA, IIB or IIC"))
    # E50
    b.append(p("This indicates the sub-grouping and is common with all other "
               "types of protection."))
    b.append(h4("Uₘ", "Uₘ"))
    # E51
    b.append(p("The supply terminals and output terminals of associated "
               "apparatus will be marked with Uₘ which is the maximum voltage "
               "which may be connected to them without violating intrinsic "
               "safety. This is normally considered to be the maximum supply "
               "voltage to the apparatus to which they are connected, and is "
               "normally assumed to be the mains."))
    b.append(h4("U₀", "U₀"))
    # E52
    b.append(p("This is the maximum open circuit voltage which the associated "
               "apparatus can supply to the intrinsically safe apparatus with "
               "which they are interconnected. It determines the maximum "
               "capacitance which will be permitted in the intrinsically safe "
               "circuit."))

    # Printed p.407 / BLOCK M.
    b.append(h4("I₀", "I₀"))
    # E53
    b.append(p("This is the maximum short circuit current which the "
               "associated apparatus can supply to the hazardous area and "
               "will determine the maximum inductance acceptable in the "
               "intrinsically safe circuit."))
    b.append(h4("P₀", "P₀"))
    # E54
    b.append(p("This is an indication of the maximum power which the "
               "associated apparatus can deliver into the hazardous area. It "
               "also goes some way to identifying the type of source "
               "represented by that apparatus (e.g., resistively limited or "
               "constant current voltage limited)."))
    b.append(h4("L₀", "L₀"))
    # E55
    b.append(p("This specifies the maximum inductance which can be connected "
               "to the intrinsically safe circuit terminals of the associated "
               "apparatus, and hence the maximum inductance acceptable for "
               "the combination of cable and intrinsically safe apparatus."))
    b.append(h4("C₀", "C₀"))
    # E56
    b.append(p("This specifies the maximum capacitance which can be connected "
               "to the intrinsically safe circuit terminals of the apparatus, "
               "and hence the maximum acceptable capacitance of the "
               "combination of interconnecting cable and intrinsically safe "
               "apparatus."))
    # E57
    b.append(p("These parameters allow the maximum facility for "
               "interconnection of associated and intrinsically safe "
               "apparatus without carrying out complex calculations. The only "
               "other parameter which is of interest is a parameter called "
               "Inductance/Resistance ratio (L₀/R₀) which is a measure of the "
               "maximum inductance per unit of resistance which may be "
               "connected to the power source. This is valuable because it is "
               "known that as cable length increases so does its resistance "
               "and current will fall, which means the permitted inductance "
               "will rise. For a resistively limited source (and these "
               "comprise most of the sources used in intrinsic safety) it can "
               "further be shown that the maximum stored energy occurs when "
               "the external resistance equals the source resistance (see "
               "Fig. 13.33) and, if this is safe, then any other situation is "
               "also safe. If this is applied to cable, therefore, no limit "
               "of cable length which would otherwise be imposed by "
               "inductance per unit length is necessary. For any situation "
               "the L₀/R₀ can be calculated (see Fig. 13.34) and this ratio "
               "is given by:-"))
    b.append(eq("L₀/R₀ = {8eRₓ + (64e²Rₓ² − 72U²eLₓ)^0.5}/4.5U      H/Ω"))
    b.append(p("where  Rₓ = The circuit resistance excluding the cable  "
               "(Rₛ or Rₛ + Rᵢ, whichever gives the worst case)  Ω"
               "<br>U = The open circuit voltage of the power source  V"
               "<br>Lₓ = The total value of lumped inductance in the circuit  "
               "(Lₛ or Lₛ + Lᵢ whichever gives the worst case)  H"
               "<br>e = The minimum ignition energy  J"))
    # §6 quirk 4 - subscript/superscript loss in OCR.
    b.append(note("<b>Note on subscript and superscript loss in OCR.</b> The "
                  "print uses Rₓ, Rₛ, Rᵢ, Lₓ, Lₛ, Lᵢ, L₀, R₀, U₀, I₀, Uᵢ, Iᵢ, "
                  "Pᵢ, Lᵢ, Cᵢ, mm², 10⁻⁶, V₂ and V₁; the OCR flattens them "
                  "into 'R,', 'Lo', 'U,,', 'loT6' and '4 mm2'. All are "
                  "restored as printed."))

    # Printed p.408 / BLOCK N. Fig. 13.33 at top of page.
    b.append(fig(33, FE.fig_f1333()))
    # E58
    b.append(p("For the purposes of this calculation the minimum energy is "
               "derived from the curves (see Figs. 13.35 and 13.36) and is as "
               "follows:"))
    b.append(eq("IIA = 320 × 10⁻⁶       J<br>IIB = 160 × 10⁻⁶       J<br>"
                "IIC = 40 × 10⁻⁶        J"))
    # E59
    b.append(p("Where there is no lumped inductance in either the associated "
               "or the intrinsically safe apparatus this formula simplifies "
               "to:"))
    b.append(eq("L₀/R₀ = 3.56eRₓ/U      H/Ω"))
    # E60 - continues on printed p.409.
    b.append(p("Regrettably there is no similar method of identifying "
               "capacitance, although clearly the cable resistance will have "
               "an effect of reducing the"))

    # Printed p.409 / BLOCK O. Fig. 13.34 at top of page.
    b.append(fig(34, FE.fig_f1334()))
    # §6 quirk 18 - Fig. 13.34 key line 3.
    b.append(note("<b>Note on line 3 of the Fig. 13.34 key.</b> The print "
                  "reads 'L₀ = Cable capacity (varies with length)', using "
                  "'capacity' rather than 'capacitance'. The receptor "
                  "designators look like 'L1'/'R1' in the drawing but are "
                  "Lᵢ/Rᵢ in the key. Both are kept as printed."))
    # E61 - continuation of E60.
    b.append(p("rate of capacitive discharge. The problem here is that the "
               "cable comprises a set of series resistors and shunt "
               "capacitors which is much more difficult to analyse than is "
               "the inductive case, where all components are in series. Thus "
               "in most cases the limit on cable length will be the cable "
               "capacitance, although experience has shown that with normal "
               "cables the problem of cable length only becomes real in the "
               "case of sub-group IIC installations as the capacitance for "
               "IIA and IIB for all circuits below 30 V, where most "
               "intrinsically safe circuits are concentrated, is large enough "
               "to accommodate any reasonable length of cable required."))
    # E62
    b.append(p("Where voltage limited constant current supplies are "
               "concerned the calculation of L/R is on the face of it more "
               "difficult. By using a tangent line as shown is Fig. 13.35 it "
               "can, however, be calculated and, although the result is "
               "somewhat limiting, it is often useful to have."))
    # §6 quirk 14 - "as shown is Fig. 13.35".
    b.append(note("<b>Note on 'as shown is Fig. 13.35'.</b> The print uses "
                  "'is' for 'in' in the phrase 'By using a tangent line as "
                  "shown is Fig. 13.35'. The source error is kept."))

    b.append(h4("Intrinsically safe apparatus",
                "Intrinsically safe apparatus"))
    # E63 - continues on printed p.410.
    b.append(p("In the case of intrinsically safe apparatus the required "
               "parameters in most cases are those within the apparatus, as "
               "the apparatus is connected to a power source. What is "
               "necessarily marked on or referred to for the apparatus is:"))
    # §6 quirk 24 - line-break hyphenation "appa-/ratus".
    b.append(note("<b>Note on the line-break hyphenation.</b> At the foot of "
                  "printed p.409 and the top of printed p.410 the word "
                  "'apparatus' is split as 'appa-/ratus'. This is a line "
                  "break, not a source hyphen, and is rejoined as "
                  "'apparatus'."))

    # Printed p.410 / BLOCK P. Fig. 13.35 at top of page.
    b.append(fig(35, FE.fig_f1335()))
    # §6 quirk 21 - caption wordings across Figs. 13.34 and 13.35.
    b.append(note("<b>Note on the L/R caption wordings.</b> The Fig. 13.34 "
                  "caption reads 'Calculation of L/R ratio' with 'ratio', "
                  "while the Fig. 13.35 caption reads 'Calculation of L/R' "
                  "without it. The figures also carry 'Equivalent load line "
                  "for L/R calculation' and 'Equivalent circuit used for L/R "
                  "calculations' (plural). All three wordings are kept."))
    # E64 - the five parameter definitions, verbatim.
    b.append(p("Uᵢ – the maximum voltage which a power source may deliver to "
               "the apparatus;<br>"
               "Iᵢ – the maximum short circuit current which any power source "
               "connected to the apparatus may deliver;<br>"
               "Pᵢ – the maximum power delivery capability of any source "
               "connected to the apparatus;<br>"
               "Lᵢ – the maximum inductance within the apparatus which "
               "appears on the input terminals;<br>"
               "Cᵢ – the maximum internal capacitance which appears on the "
               "input terminals of the apparatus;"))
    # E65 - ends mid-sentence on printed p.410, continues on printed p.411.
    b.append(p("The internal inductance can be additionally stated as an L/R "
               "ratio and this sometimes assists in connection. Also, where "
               "the apparatus is something such as a temperature transmitter "
               "and is connected to a primary element in addition to its "
               "connection to a power source, U₀, I₀ and P₀ may also need"))
    # §6 quirk 23 - printed page number 410.
    b.append(note("<b>Note on the printed page number 410.</b> The OCR reads "
                  "the final page number as '41 0'; the render clearly reads "
                  "'410'."))
    return "".join(b)
