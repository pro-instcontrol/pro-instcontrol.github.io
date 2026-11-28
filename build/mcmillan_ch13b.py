# -*- coding: utf-8 -*-
"""Chapter 13, module B - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 347-362 (PDF pp. 368-383).

Covers the tail of 13.5 (capacitive, resistive, composite and crowbar
spark-ignition mechanisms), 13.6 hot-surface ignition, and 13.7 basic
component and construction requirements.  Figures 13.6-13.12 and Tables
13.3-13.6 are embedded in printed order.  The chapter shell owns the
chapter h2, the printed references, the glossary, the source-quirk note
and the copyright.

Printed quirks are kept in the English text (the caption slash and
less-than sign of Fig. 13.6, the doubled 1.000 axis ends of Fig. 13.8,
the printed numeric oddities in Table 13.5, the acronym mismatch of
'Safety in Mines Research Establishment (HSE)', the singular 'item',
the missing 'that', 'is so doing', the wrong cross-reference 'Table 13.2',
the contradictory definition of k, and the superscript-footnote forms)
with bilingual notes; the Vietnamese follows the intended meaning.
This is an unofficial study translation.  The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, eq, note, table, fig
import mcmillanfig13_b as FB
import mcmillan_tbl13_1_4 as T1
import mcmillan_tbl13_5_8 as T2


def body_vi():
    b = []

    # Survey quirk 1 - the assignment's line offset; Survey B is 15070-15811.
    b.append(note("<b>Lưu ý về số dòng được giao.</b> Đề bài ghi dòng 15090 "
                  "là dấu '=== PAGE 368 ==='; thực tế dòng 15090 là dấu "
                  "'=== PAGE 369 ==='. Trang in 347 (PDF 368) bắt đầu ở dòng "
                  "thô 15070 và trang in 362 (PDF 383) kết thúc ở dòng 15811, "
                  "với '=== PAGE 384 ===' ở dòng 15812. Vì vậy Survey B phủ "
                  "các dòng 15070–15811."))
    # Survey quirk 2 - running-header OCR 7' -> 'i'.
    b.append(note("<b>Lưu ý về OCR của đầu đề chạy trang.</b> Lớp văn bản "
                  "OCR đọc đầu đề là 'Protection concept intrinsic safety 7'' "
                  "với dấu nháy sau chữ số 7 ở nhiều trang; ảnh trang in cho "
                  "thấy bản in viết 'Protection concept intrinsic safety "
                  "'i''. Cách đọc theo ảnh trang được dùng xuyên suốt."))

    # B-a / printed p.347 / PDF 368: Fig. 13.6, then heading and B1.
    b.append(fig(6, FB.fig_f1306()))
    # Survey quirk 3 - Fig. 13.6 caption OCR.
    b.append(note("<b>Lưu ý về nhan đề Hình 13.6.</b> Lớp OCR đọc 'Ignition "
                  "thresholdinductive circuits at t24 V' và 'fig. 13.4'; ảnh "
                  "trang in cho thấy 'Ignition threshold/inductive circuits "
                  "at <24 V' và 'Fig. 13.4'. Nhạn đề không có dấu chấm sau "
                  "'24 V' ở cuối, và câu Lưu ý dùng số ít 'inductive circuit'. "
                  "Tất cả được giữ nguyên trong bản tiếng Anh."))
    # Survey quirk 4 - Fig. 13.6 axis OCR.
    b.append(note("<b>Lưu ý về trục của Hình 13.6.</b> Lớp OCR đọc 'I' và "
                  "'Minimum igniting current L A'; ảnh trang in cho thấy "
                  "'Inductance L, mH' và 'Minimum igniting current I, A'. "
                  "Các nhãn đúng theo ảnh trang được dùng trong hình vẽ lại."))
    b.append(h4("Mạch điện dung", "Capacitive circuits"))
    # B1 (raw 15084-15089; continues on printed 348).
    b.append(p("Cơ chế đánh lửa do điện dung thường là tia lửa khi đóng, xảy "
               "ra khi các tiếp điểm đã tách ra đủ lâu để điện dung tích đến "
               "điện áp hở mạch, chứ không phải khi các tiếp điểm mở ra, vì "
               "lúc đó điện dung đã được xả gần như hết. Tia lửa này thường "
               "không phải là hồ quang vì điện áp trong hầu hết các mạch an "
               "toàn nội tại không đủ để đánh thủng một đường không khí, mà "
               "là tia lửa xảy ra khi"))
    # Survey quirk 25 - B1 begins mid-sentence from printed 346.
    b.append(note("<b>Lưu ý về điểm bắt đầu của đoạn.</b> Đoạn đầu của mục "
                  "'Mạch điện dung' bắt đầu giữa câu, tiếp nội dung từ trang "
                  "in 346 nằm ngoài phạm vi mô-đun này; câu được giữ nguyên "
                  "ở dạng chưa trọn vẹn theo bản in."))

    # B-b / printed p.348 / PDF 369.
    # B2 (raw 15092-15097).
    b.append(p("tiếp điểm đầu tiên được đóng và chỉ xuất hiện vì tiếp điểm "
               "đó chưa được ép chặt (tức là, nếu tiếp điểm được đóng rất "
               "chắc và rất nhanh thì gần như không có tia lửa nào phát "
               "sinh). Điện áp trên tia lửa bắt đầu từ điện áp trên tụ đã "
               "tích điện và giảm dần theo điện tích. Vì vậy việc phóng "
               "năng lượng không hiệu quả như trường hợp cảm ứng, và các "
               "giá trị năng lượng điển hình như sau:"))
    # B3 (raw 15098-15101), displayed values.
    b.append(eq("IIA = 4.0 mJ (ở 20 V) – 1.25 mJ (ở 100 V)"
                "<br>IIB = 1.0 mJ (ở 20 V) – 500 µJ (ở 100 V)"
                "<br>IIC = 200 µJ (ở 20 V) – 50 µJ (ở 100 V)"
                "<br>(240 µJ (ở 20 V) – 110 µJ (ở 100 V))"))
    # Survey quirk 5 - energy-value OCR.
    b.append(note("<b>Lưu ý về OCR của các giá trị năng lượng.</b> Lớp OCR "
                  "đọc '2OV'/'lOOV' thành '20 V'/'100 V', 'l.OmJ' thành "
                  "'1.0 mJ', 'llOpJ' thành '110 µJ' và 'pJ' thành 'µJ'. Hai "
                  "giá trị đầu của IIA và IIB thực sự là mJ, các giá trị còn "
                  "lại là µJ; không chuẩn hóa đơn vị."))
    # B4 (raw 15102-15103).
    b.append(p("Các số liệu IIC trong ngoặc là số liệu lấy từ BS 5501, Phần "
               "7⁴, cho thấy sự giảm đáng kể dung lượng cho phép trong "
               "BS/EN 50020¹⁰."))
    # Survey quirk 6 - superscript footnotes eaten by OCR.
    b.append(note("<b>Lưu ý về các số ghi chú dạng chỉ số trên.</b> Lớp OCR "
                  "đọc 'Part 74' thành 'Part 7⁴', '5002010' thành "
                  "'50020¹⁰', 'EN 60127 (1991).13' thành 'EN 60127 "
                  "(1991).¹³', 'GS 43.14' thành 'GS 43.¹⁴' và '5 \"C'/'10 "
                  "\"C' thành '5 °C'/'10 °C'. Dạng in có chỉ số trên và dấu "
                  "độ được giữ trong bản tiếng Anh."))
    # B5 (raw 15104-15109).
    b.append(p("Khác với trường hợp có độ tự cảm, điện áp trên tia lửa có "
               "xu hướng giảm nhanh khi năng lượng được giải phóng, làm cản "
               "trở việc giải phóng năng lượng vào tia lửa và do đó việc "
               "giải phóng năng lượng kém hiệu quả hơn, đặc biệt ở điện áp "
               "thấp. Hình 13.7 cho thấy cơ chế dùng để xác định năng lượng "
               "đánh lửa bằng tia lửa hiệu dụng, còn Hình 13.8 cho thấy các "
               "giá trị điển hình cho ba nhóm con."))
    # Survey quirk 21 - mixed Figure/Fig. in adjacent paragraphs.
    b.append(note("<b>Lưu ý về cách viết 'Figure' và 'Fig.' trộn lẫn.</b> "
                  "Bản in viết 'Figure 13.7' nhưng 'Fig. 13.8' trong cùng "
                  "một đoạn, và sau đó dùng 'Figure 13.9' rồi 'Figures "
                  "13.10 and 13.11'. Sự không nhất quán được giữ nguyên "
                  "trong bản tiếng Anh."))
    # B6 (raw 15110-15113).
    b.append(p("Một lần nữa, các đường cong trong Hình 13.8 dựa trên các tụ "
               "điện có chất điện giải rất hiệu quả và nhạy hơn nhiều so "
               "với trường hợp của các loại như tụ điện phân. Vì vậy chúng "
               "có thể được dùng với một độ tin cậy nhất định."))
    b.append(fig(7, FB.fig_f1307()))
    # Survey quirk 21 - Fig. 13.7 note cross-reference and unitless 0.5.
    b.append(note("<b>Lưu ý về Lưu ý của Hình 13.7.</b> Lưu ý in dẫn đến "
                  "'Fig. 12.11', tức hình của Chương 12, chứ không phải hình "
                  "của Chương 13, và giá trị '0.5' được in không kèm đơn vị. "
                  "Cả hai được giữ nguyên theo bản in."))

    # B-c / printed p.349 / PDF 370.
    b.append(fig(8, FB.fig_f1308()))
    # Survey quirk 7 - both axis ends printed 1.000.
    b.append(note("<b>Lưu ý về hai đầu trục của Hình 13.8.</b> Cả hai đầu "
                  "cao của trục đều được in là '1.000' theo kiểu dấu phân "
                  "cách hàng nghìn; không đổi thành 1000. Các nhãn II A, "
                  "II B và II C được giữ nguyên."))
    b.append(h4("Mạch điện trở", "Resistive circuits"))
    # B7 (raw 15138-15141; continues on printed 350).
    b.append(p("Các mạch điện trở, khác với các mạch tương ứng kiểu cảm ứng "
               "và điện dung, có điện áp và dòng điện bị giới hạn. Các tia "
               "lửa sinh ra thường yếu hơn các tia lửa do sự phóng của độ "
               "tự cảm hay điện dung, nhưng lặp đi lặp lại khi dây dẫn cọ "
               "qua bề mặt đĩa dưới. Cơ chế đánh lửa của các tia lửa này "
               "không được hiểu rõ bằng cơ chế liên quan đến"))
    # Survey quirk 12 - line-break hyphenations.
    b.append(note("<b>Lưu ý về các từ bị ngắt gạch nối khi xuống dòng.</b> "
                  "Bản in ngắt 'igni-tion', 'sub-groups', 'relation-ship' "
                  "(trong nhan đề Bảng 13.4), 'evalua-tion' (trong nhan đề "
                  "Bảng 13.6), 'de-energized', 'voltage/current', "
                  "'non-countable', 'cartridge-type' và 'plug-in'. Chỉ các "
                  "chỗ ngắt do xuống dòng ngoài ý muốn được nối lại; các "
                  "từ ghép thật sự được giữ nguyên."))

    # B-d / printed p.350 / PDF 371.
    # B8 (raw 15144-15145).
    b.append(p("một lần giải phóng năng lượng đơn lẻ như xảy ra trong tia "
               "lửa của trường hợp cảm ứng và điện dung."))
    # B9 (raw 15146-15154).
    b.append(p("Hình 13.9 cho thấy mạch điện trở và các mạch giới hạn dòng "
               "không đổi, giới hạn điện áp được dùng để tạo các đường cong "
               "dòng đánh lửa nhỏ nhất, và Hình 13.10 cùng Hình 13.11 cho "
               "thấy chính các đường cong đó cho ba nhóm con. Các mạch giới "
               "hạn dòng không đổi, giới hạn điện áp bắt nguồn từ một đề "
               "xuất của HSE gửi cho Viện Tiêu chuẩn Anh (BSI) để đưa vào "
               "BS/EN 50020¹⁰ và đã được chuyển tới ủy ban Châu Âu "
               "(CENELEC) nhưng hiện vẫn chưa được xử lý. Như đã nói ở "
               "trên, năng lượng giải phóng không thể xác định rõ và trong "
               "trường hợp này khả năng truyền công suất là thông số quan "
               "trọng. Điều này được thể hiện qua khả năng công suất sau "
               "đây của các mạch ngưỡng đánh lửa thuộc loại này:"))
    # B10 (raw 15155-15157), displayed values.
    b.append(eq("IIA = 2.5 W đến 8 W (ở 20 V) – 2.1 W đến 2.6 W (ở 50 V)"
                "<br>IIB = 2.2 W đến 6.5 W (ở 20 V) – 1.5 W đến 1.9 W (ở 50 V)"
                "<br>IIC = 0.95 W đến 2.5 W (ở 20 V) – 0.65 W đến 0.8 W (ở 50 V)"))
    # B11 (raw 15158-15159).
    b.append(p("Vì vậy, các mạch điện trở được cho là có khả năng đánh lửa "
               "cao hơn khi điện áp tăng."))
    b.append(fig(9, FB.fig_f1309()))
    # Survey quirk 8 - Fig. 13.9 label OCR and upper/lower profile difference.
    b.append(note("<b>Lưu ý về nhãn trong Hình 13.9.</b> Lớp OCR đọc 'Spark "
                  "test apbratus', 'Shoq circuit', 'Current limiting yi:;e', "
                  "'circui?', 'throu h' và 'loat'; ảnh trang in cho thấy "
                  "'Spark test apparatus', 'Short circuit', 'Current "
                  "limiting circuit' và 'Current through load'. Chú thích "
                  "phía trên viết 'voltage/current profile' (chữ v thường), "
                  "còn chú thích phía dưới viết 'Voltage current profile' "
                  "(không có dấu gạch chéo, chữ V hoa) — đây là khác biệt "
                  "thật sự trong bản in."))

    # B-e / printed p.351 / PDF 372.
    b.append(fig(10, FB.fig_f1310()))
    # Survey quirk 9 - Fig. 13.10 axis OCR.
    b.append(note("<b>Lưu ý về trục của Hình 13.10.</b> Lớp OCR đọc '1 "
                  "OOmA' và '1 OmA'; ảnh trang in cho thấy '100mA' và "
                  "'10mA'. Đơn vị được in không có dấu cách với chữ số "
                  "(như '5A', '10V'), và được giữ như vậy."))
    b.append(h4("Mạch phức hợp", "Composite circuits"))
    # B12 (raw 15212-15219; continues on printed 352).
    b.append(p("Hầu hết các mạch thực tế đều chứa một phần của cả ba loại "
               "công suất hay năng lượng và các thành phần này thường cùng "
               "tồn tại vì điều kiện lỗi tạo ra nguy cơ lớn nhất là khác "
               "nhau trong từng trường hợp. Điều này có nghĩa là khi một "
               "thông số ở giới hạn của nó thì các thông số khác còn cách "
               "xa giới hạn của chúng. Các thử nghiệm thực tế trong quá "
               "khứ đã cho thấy đúng là như vậy và có thể xác nhận bằng "
               "cách xem xét các đường cong đánh lửa khác nhau trong Hình "
               "13.5, 13.6, 13.8 và 13.10. Các hình này cho thấy ảnh hưởng "
               "của các phương pháp đánh lửa khác nhau khiến năng lượng "
               "sinh ra không cộng dồn trực tiếp và"))

    # B-f / printed p.352 / PDF 373.
    b.append(fig(11, FB.fig_f1311()))
    # Survey quirk 10 - Fig. 13.11 OCR.
    b.append(note("<b>Lưu ý về Hình 13.11.</b> Lớp OCR đọc nhầm thành 'Fig. "
                  "13.1 1'; ảnh trang in cho thấy 'Fig. 13.11'. Chỉ có "
                  "'Group IIB' và 'Group IIC' được ghi nhãn trong hình, "
                  "không có nhãn 'Group IIA'."))
    # B13 (raw 15225-15241).
    b.append(p("ảnh hưởng của việc có tia lửa cảm ứng cùng với tia lửa điện "
               "trở có khả năng đánh lửa thấp hơn mức dự kiến nếu cộng trực "
               "tiếp. Điều này mở ra khả năng dùng các đường cong cho các "
               "mạch phức hợp hơn, khi các thông số đánh lửa khác với thông "
               "số đang được đánh giá nhỏ hơn đáng kể so với các thông số "
               "giới hạn. Việc áp dụng các đường cong trong quá khứ cho "
               "thấy tổng năng lượng nhỏ hơn nhiều so với dự kiến và, dù "
               "chưa có xác nhận chắc chắn, một suy luận từ các mạch và "
               "đường cong cảm ứng (Hình 13.4 và 13.5) cho thấy rằng, miễn "
               "là độ tự cảm hiện diện nhỏ hơn 80 phần trăm giá trị cho "
               "phép tại dòng ngắn mạch sẵn có từ một mạch điện trở phù hợp "
               "với Hình 13.10, rất khó có khả năng xảy ra đánh lửa do độ "
               "tự cảm đó trong một mạch phức hợp. Vì vậy, như một hướng "
               "dẫn thiết kế, có thể dùng các đường cong khi tất cả trừ "
               "một trong các thông số đang xét (ví dụ độ tự cảm, điện dung "
               "và giới hạn điện trở) cho các giá trị nhỏ hơn 80 phần trăm "
               "giá trị giới hạn của chúng khi xét riêng lẻ. Điều này có "
               "thể không loại trừ sự cần thiết phải thử nghiệm về sau "
               "nhưng sẽ cho mức độ tin cậy cao rằng các mạch sẽ được "
               "chứng minh là an toàn nội tại trong bất kỳ thử nghiệm nào "
               "về sau."))

    # B-g / printed p.353 / PDF 374.
    b.append(h4("Mạch được bảo vệ bằng crowbar", "Crowbar protected circuits"))
    # B14 (raw 15245-15251).
    b.append(p("Các mạch kiểu crowbar, trong đó điện áp được bố trí để sụp "
               "đổ khi có quá tải, gây ra khó khăn riêng khi thử nghiệm. "
               "Cầu crowbar loại bỏ điện áp ở lần ngắn mạch ban đầu trong "
               "thiết bị thử nghiệm và, tùy thuộc vào sự phục hồi của tia "
               "lửa mạch, tia lửa bị ức chế trong một thời gian sau đó. Mạch "
               "phải được thử nghiệm bằng thiết bị thử tia lửa nhưng, để "
               "đảm bảo rằng tình huống mà thiết bị đó không tạo ra điều "
               "kiện khắc nghiệt nhất, phải chứng minh được rằng mạch không "
               "giải phóng năng lượng vượt quá giá trị cực đại sau đây "
               "trong quá trình hoạt động của crowbar:"))
    # B15 (raw 15252-15254), displayed values.
    b.append(eq("IIA = 160 µJ<br>IIB = 80 µJ<br>IIC = 20 µJ"))
    # B16 (raw 15255-15259).
    b.append(p("Các số liệu này xấp xỉ một nửa số liệu đánh lửa trong mạch "
               "cảm ứng và thấp hơn nữa trong trường hợp mạch điện dung. Vì "
               "cơ chế đánh lửa khác với cơ chế của mạch cảm ứng, nơi phép "
               "cộng là quan trọng hơn, trong thiết kế có thể bỏ qua ảnh "
               "hưởng cộng dồn với niềm tin rằng mọi thử nghiệm sẽ đạt."))

    # Survey quirk 24 - the four level-3 spark-mechanism headings are unnumbered.
    b.append(note("<b>Lưu ý về các tiêu đề không có số.</b> Bốn tiêu đề mục "
                  "từ trang in 347 đến 353 (Mạch điện dung, Mạch điện trở, "
                  "Mạch phức hợp, Mạch được bảo vệ bằng crowbar) là các tiểu "
                  "mục không đánh số của 13.5; chúng được trình bày như "
                  "tiêu đề, không phải thân bài. Mọi hình và bảng trong "
                  "phạm vi này đều có số."))

    b.append(h3("13.6 Xác nhận an toàn nội tại liên quan đến đánh lửa bề mặt nóng",
                "13.6 Confirmation of intrinsic safety in respect of hot surface ignition"))
    # B17 (raw 15262-15272).
    b.append(p("Như đã nêu, không có hệ số an toàn nào được áp dụng cho điện "
               "áp và dòng điện liên quan đến đánh lửa bề mặt nóng. Tuy "
               "nhiên, giống như các nguyên lý bảo vệ khác, một hệ số an "
               "toàn cơ bản là 5 °C được áp dụng trong trường hợp các cấp "
               "nhiệt độ T3 đến T6 và 10 °C trong trường hợp T1 và T2, bằng "
               "cách yêu cầu nhiệt độ bề mặt tối đa thấp hơn giới hạn của "
               "cấp đó một lượng tương ứng. Yêu cầu này trong BS/EN 50020¹⁰ "
               "thể hiện sự thay đổi so với BS 5501, Phần 7⁴, vốn theo cách "
               "diễn đạt trong các điều khoản loại trừ đã không yêu cầu mức "
               "chênh 5 °C hay 10 °C. Dĩ nhiên nhiệt độ bề mặt tối đa trong "
               "mọi trường hợp đều được đo trong các điều kiện xấu nhất "
               "thích hợp đã quy định cho 'ia' và 'ib', và các điều kiện lỗi "
               "cần xét đến rất có thể khác với các điều kiện dùng để đánh "
               "giá đánh lửa bằng tia lửa."))
    # Survey quirk 11 - the HSE acronym mismatch.
    b.append(note("<b>Lưu ý về cụm 'Safety in Mines Research Establishment "
                  "(HSE)'.</b> Tên viết đầy đủ không khớp với viết tắt HSE; "
                  "đây là lỗi của tài liệu gốc và được giữ nguyên trong bản "
                  "tiếng Anh. Các giá trị 5 °C và 10 °C đều có dấu độ."))
    # B18 (raw 15273-15282; continues on printed 354).
    b.append(p("Vì an toàn nội tại điển hình là một khái niệm dùng trong "
               "thiết bị đo đạc với các linh kiện điện tử nhỏ, các yêu cầu "
               "thông thường về nhiệt độ tối đa rất khắt khe, đặc biệt vì "
               "đó là trong điều kiện lỗi và người ta biết rằng khó đánh "
               "lửa bầu khí quyển nổ hơn bằng các linh kiện nhỏ. Một lượng "
               "công việc đáng kể do Viện Nghiên cứu An toàn Mỏ (HSE) tại "
               "Vương quốc Anh thực hiện đã dẫn đến tình huống cho phép "
               "nới lỏng đáng kể đối với linh kiện nhỏ. Đối với phân loại "
               "nhiệt độ T5, các linh kiện điển hình có tổng diện tích bề "
               "mặt nhỏ hơn 10 cm² (không tính các dây dẫn ra ngoài là một "
               "phần của linh kiện) được phép đạt nhiệt độ đo được 145 °C "
               "mà không gây ra"))

    # B-h / printed p.354 / PDF 375.
    # B19 (raw 15284-15289).
    b.append(p("đánh lửa, trong khi đối với linh kiện lớn hơn giá trị đó là "
               "95 °C (các giá trị này biểu thị mức tăng trên nhiệt độ môi "
               "trường tối đa cho phép cộng với chính nhiệt độ môi trường). "
               "Đối với phân loại T4, khi nhiệt độ đo được tối đa thông "
               "thường không được vượt quá 120 °C, tình huống linh hoạt "
               "hơn và Bảng 13.3 cho thấy các mức nới lỏng được phép."))
    # B20 (raw 15290-15294; resumes after the tables).
    b.append(p("Cũng có khả năng dây dẫn trong mạch an toàn nội tại có thể "
               "là nguồn gây đánh lửa và vì mục đích đó các yêu cầu cụ thể "
               "được áp dụng để đảm bảo không phải vậy. Dòng điện cực đại "
               "được quy định cho các loại dây dẫn khác nhau gặp phải nhằm "
               "đảm bảo chúng không vượt quá nhiệt độ giới hạn cho cấp "
               "nhiệt độ yêu cầu. Các số liệu cho dây đồng"))
    # Table 13.3 (printed p.354).
    b.append(table(T1.HEAD133_VI, T1.ROWS133_VI, T1.CAPTION133_VI))
    if T1.NOTE133_VI:
        b.append(note(T1.NOTE133_VI))
    # Survey quirk 13 - Table 13.3 source anomaly.
    b.append(note("<b>Lưu ý về hàng thứ ba của Bảng 13.3.</b> Hàng đó in "
                  "'≥20 mm²', trùng với cận dưới của hàng thứ hai; '≥10 cm²' "
                  "là cách đọc có thể định nhưng bất thường trong bản in "
                  "được giữ nguyên. OCR đọc '≥' thành 't'; ảnh trang in là "
                  "nguồn quyết định."))
    # Table 13.4 (printed p.354).
    b.append(table(T1.HEAD134_VI, T1.ROWS134_VI, T1.CAPTION134_VI))
    if T1.NOTE134_VI:
        b.append(note(T1.NOTE134_VI))
    # Survey quirk 14 - Table 13.4 source anomaly.
    b.append(note("<b>Lưu ý về Bảng 13.4.</b> Nhạn đề được in với chỗ ngắt "
                  "gạch nối 'relation- / ship' và 'temper- / ature'; cách "
                  "viết nối được đưa thành một chuỗi. Ở hàng 0.5 mm, giá "
                  "trị T6 in là 6.7 thấp hơn giá trị T5 là 6.9 — bất thường "
                  "trong bản in được giữ nguyên; OCR đọc đơn vị là '(m2)' "
                  "trong khi ảnh trang in cho '(mm²)'."))

    # B-i / printed p.355 / PDF 376 - Table 13.5.
    b.append(table(T2.HEAD135_VI, T2.ROWS135_VI, T2.CAPTION135_VI))
    if T2.NOTE135_VI:
        b.append(note(T2.NOTE135_VI))
    # Survey quirks 15 and 16 - Table 13.5 numeric oddities and x-ref error.
    b.append(note("<b>Lưu ý về bốn số liệu bất thường của Bảng 13.5.</b> "
                  "'01.3' có số 0 đứng đầu (hàng 0.3, T6 A), '195.0' có dấu "
                  "thập phân bị lệch (hàng 0.3, T6 B), '4.02' nằm ngoài "
                  "trình tự (hàng 1.5, T6 A) và '117.0' có chữ số 1 thừa "
                  "ở đầu (hàng 3.0, T5 C). Tất cả được tái hiện chính xác "
                  "theo bản in. Ghi chú 5 dẫn đến 'Bảng 13.2' dù bảng áp "
                  "dụng là Bảng 13.5 — lỗi dẫn chiếu của tài liệu gốc được "
                  "giữ nguyên."))
    # B21 (raw 15483-15485).
    b.append(p("và các đường mạch in trên bản mạch đồng được cho trong Bảng "
               "13.4 và Bảng 13.5 tương ứng. Không đưa số liệu cho các cấp "
               "nhiệt độ cao hơn (T1, T2 và T3) vì kinh nghiệm cho thấy các "
               "cấp này thường không cần thiết."))
    # B22 (raw 15486-15487; continues on printed 356).
    b.append(p("Cũng có một quy trình tính toán có thể dùng để bao phủ "
               "những trường hợp bất thường như các trường hợp này và các "
               "dẫn thể bằng kim loại khác như"))

    # B-j / printed p.356 / PDF 377.
    # B23 (raw 15490-15491).
    b.append(p("các dải mỏng trong đồng hồ cuộn dây di động v.v. Giới hạn "
               "dòng điện cho bất kỳ giới hạn nhiệt độ nào có thể được xác "
               "định bằng:"))
    # B24 (raw 15492), displayed equation.
    b.append(eq("Iₘₐₓ = I<sub>f</sub>{t(1 + αT)/T(1 + αt)}<sup>0.5</sup> amps"))
    # Survey quirk 17 - E4 formula OCR.
    b.append(note("<b>Lưu ý về công thức E4.</b> Lớp OCR đọc 'I, = If(t(1 + "
                  "aT)/T(l + amps'; ảnh trang in cho thấy Iₘₐₓ = I<sub>f</sub>"
                  "{t(1 + αT)/T(1 + αt)}<sup>0.5</sup> amps, với chữ 't' "
                  "đứng đầu trong ngoặc nhọn và chữ 't' ở cuối mẫu số — cả "
                  "hai đều có trong bản in. OCR đọc 'O.O04265/\"C' thành "
                  "'0.004265/°C'."))
    # B25 (raw 15493-15501), definition block.
    b.append(eq("ở đây Iₘₐₓ = dòng điện tối đa cho phép    Amps"
                "<br>I<sub>f</sub> = dòng điện mà tại đó dây chảy    Amps"
                "<br>t = giới hạn cấp nhiệt độ (−5 °C hoặc 10 °C)    °C"
                "<br>T = nhiệt độ mà tại đó dây chảy    °C"
                "<br>α = hệ số nhiệt độ của điện trở"
                "<br>cho vật liệu dây (α của đồng là 0.004265/°C)    /°C"))
    # B26 (raw 15502-15506).
    b.append(p("Công thức trên một lần nữa cho kịch bản xấu nhất vì các dây "
               "đang xét sẽ được nối vào các linh kiện đầu cuối có khối "
               "lượng đáng kể, do đó nhiệt độ thực tế có thể thấp hơn do "
               "hiệu ứng dẫn nhiệt của các thiết bị đó, trừ khi dây rất dài "
               "mà trong thiết bị thường không phải vậy."))
    # B27 (raw 15507-15521).
    b.append(p("Nếu cách tiếp cận này không cho kết quả mong muốn thì có "
               "cách tiếp cận cuối cùng có thể thực hiện nhưng cách này dựa "
               "trên một thử nghiệm và chỉ áp dụng cho T4. Linh kiện cần "
               "đánh giá được đặt trong một buồng chứa hỗn hợp không khí và "
               "ete etylic theo tỷ lệ 72% ± 2% không khí và 28% ± 2% ete "
               "etylic. Sau đó linh kiện được cấp công suất cực đại mà nó "
               "có thể tiêu tán trong điều kiện lỗi và nhiệt độ của hỗn hợp "
               "khí được nâng lên 25 °C trên nhiệt độ môi trường vận hành "
               "tối đa mong muốn. Không được xảy ra đánh lửa hay ngọn lửa "
               "lạnh (quầng xanh). Đánh lửa có thể được xác định bằng cách "
               "đo sự tăng nhiệt độ đột ngột bằng cặp nhiệt điện trong khí "
               "hoặc bằng các phương pháp trực quan hay phương pháp khác, "
               "nhưng ngọn lửa lạnh có khả năng chỉ nhận biết được bằng "
               "phương pháp trực quan. Để đảm bảo khả năng lặp lại, các "
               "thử nghiệm này nên được lặp lại trên ít nhất năm mẫu của "
               "linh kiện đang xét. Thay vì nâng nhiệt độ khí để đạt mức "
               "trên môi trường tối đa 25 °C, có thể nâng tương tự nhiệt độ "
               "của linh kiện."))
    # Survey quirk 18 - ether-mixture OCR.
    b.append(note("<b>Lưu ý về tỷ lệ hỗn hợp ete.</b> Lớp OCR đọc '72% f 2%' "
                  "và '28% f 2%'; ảnh trang in cho thấy '72% ± 2%' và "
                  "'28% ± 2%'. Dấu ± và các giá trị 25 °C, năm mẫu, cùng "
                  "cụm 'cold flames (blue coronas)' được giữ nguyên."))
    # B28 (raw 15522-15533).
    b.append(p("Nhiệt độ của cuộn dây của máy biến áp và cuộn cảm đôi khi "
               "khó đo trực tiếp và phương pháp đo gián tiếp được chấp "
               "nhận cho các linh kiện này. Phương pháp dùng là phương pháp "
               "biến đổi điện trở và dựa trên các phép đo điện trở ở nhiệt "
               "độ môi trường khi cuộn dây không được cấp điện, sau đó một "
               "phép đo khác được thực hiện sau khi cuộn dây đã được cấp "
               "điện đủ lâu để nhiệt độ ổn định. Không nêu giá trị cụ thể "
               "cho thời gian này nhưng thời gian đó nên đủ dài để dòng "
               "điện trong cuộn dây không thay đổi quá một phần trăm mỗi "
               "giờ sau khi đã tính đến sự thay đổi của điện áp nguồn ở "
               "nhiệt độ không đổi. Phép đo quan hệ điện áp/dòng điện ban "
               "đầu và quan hệ cuối cùng sẽ cho hai giá trị điện trở – một "
               "giá trị nguội và một giá trị ở trạng thái cân bằng nóng – "
               "miễn là dùng nguồn dc. Nếu nguồn là ac, điện trở nguội cần "
               "được đo và điện trở nóng được đo ngay sau khi ngắt nguồn "
               "ac. Sau đó có thể tính độ tăng nhiệt độ từ:"))
    # Survey quirk 21 - 'acceptable for these item'.
    b.append(note("<b>Lưu ý về lỗi ngữ pháp 'acceptable for these item'.</b> "
                  "Bản in dùng 'item' số ít ở đây; dạng này được giữ nguyên "
                  "trong bản tiếng Anh, còn bản tiếng Việt dùng 'các linh "
                  "kiện này' theo ý định."))
    # B29 (raw 15534), displayed equation.
    b.append(eq("t = {R(k + t₁)/r} − (k + t₂ − t₁)"))

    # B-k / printed p.357 / PDF 378.
    # B30 (raw 15537-15547), definition block.
    b.append(eq("ở đây t = độ tăng nhiệt độ    °C"
                "<br>t₁ = nhiệt độ môi trường ban đầu (khi đo r)    °C"
                "<br>t₂ = nhiệt độ môi trường cuối cùng (khi đo R)    °C"
                "<br>R = điện trở cuối cùng đo được (sau khi cấp điện)    Ohms"
                "<br>r = điện trở ban đầu đo được (trước khi cấp điện)    Ohms"
                "<br>k = hằng số (234.5 đối với đồng) (Hằng số này là α,"
                "<br>nghịch đảo của hệ số nhiệt độ của điện trở)"))
    # Survey quirks 19 and 20 - E6 formula OCR and k-definition wording.
    b.append(note("<b>Lưu ý về công thức E6 và định nghĩa k.</b> Lớp OCR đọc "
                  "'t = {R(k + tl)/r) - (k + t2 - tl)'; ảnh trang in cho thấy "
                  "t = {R(k + t₁)/r} − (k + t₂ − t₁), với dấu ngoặc nhọn "
                  "đóng chứ không phải ngoặc tròn. Định nghĩa in "
                  "'k = constant (234.5 for copper) (This constant is the "
                  "α, inverse of the temperature coefficient of "
                  "resistance)' tự mâu thuẫn về mặt diễn đạt nhưng được "
                  "giữ nguyên trong bản tiếng Anh."))
    # B31 (raw 15548-15551).
    b.append(p("Công thức này tính đến mọi thay đổi của nhiệt độ môi trường "
               "giữa thời điểm đo điện trở nguội của cuộn dây trước khi cấp "
               "điện và thời điểm nhiệt độ của cuộn dây lại được đo sau khi "
               "đã cấp điện và nhiệt độ đã ổn định ở giá trị cực đại."))
    b.append(h3("13.7 Yêu cầu cơ bản về linh kiện và cấu tạo",
                "13.7 Basic component and construction requirements"))
    b.append(h3("13.7.1 Hệ số an toàn trên định mức của linh kiện",
                "13.7.1 Safety factors on component rating"))
    # B32 (raw 15554-15564).
    b.append(p("Các linh kiện và đầu nối cần được vận hành ở mức không quá "
               "hai phần ba điện áp, dòng điện và công suất định mức tối đa "
               "tương ứng trong các điều kiện sử dụng nếu hỏng hóc của chúng "
               "được xem là lỗi có thể đếm được. Tiêu chí này cần đúng cả "
               "trong vận hành bình thường của mạch an toàn nội tại lẫn khi "
               "áp dụng các lỗi có thể đếm được và không đếm được thích hợp "
               "ở những nơi khác trong mạch (tiêu chí này thường được xác "
               "định bằng cách giới hạn lỗi trong nội bộ thiết bị và xác "
               "định các thông số nguồn cấp hoặc mạch ngoài cực đại mà phần "
               "còn lại của mạch an toàn nội tại không được vượt quá trong "
               "trường hợp xấu nhất của toàn bộ số lỗi được đếm và các lỗi "
               "không đếm được liên quan ở những nơi khác trong hệ thống). "
               "Rõ ràng yêu cầu như vậy không có ý nghĩa đối với những thứ "
               "như cầu chảy, rơ le, cầu ngắt nhiệt, máy biến áp và các "
               "thiết bị tương tự vì chúng hoạt động khác đi."))
    b.append(h4("Các linh kiện không chịu hệ số định mức 1.5",
                "Components not subjected to the 1.5 rating factor"))
    # B33 - Fuses (printed p.357).
    b.append(h4("Cầu chảy", "Fuses"))
    b.append(p("Đặc tả của các cầu chảy này liên quan đến khả năng ngắt dòng "
               "điện ở một mức cụ thể và việc áp dụng hệ số định mức nêu "
               "trên sẽ tạo ra điều kiện nguy hiểm hơn vì nhiều dòng điện "
               "hơn sẽ đi qua trước khi chúng đứt."))
    # B34 - Thermal trips.
    b.append(h4("Cầu ngắt nhiệt", "Thermal trips"))
    b.append(p("Cầu ngắt nhiệt được thiết kế để hoạt động ở các nhiệt độ cụ "
               "thể và không quy định giảm mức định mức nhiệt độ. Ngoài ra, "
               "nếu chúng hoạt động bằng dòng điện thì mọi nỗ lực áp dụng "
               "hệ số định mức có thể làm chúng kém hiệu quả hơn."))
    # B35 - Relays.
    b.append(h4("Rơ le", "Relays"))
    b.append(p("Việc áp dụng hệ số an toàn cho điện áp hoặc dòng điện của rơ "
               "le sẽ ngăn thiết bị hoạt động vì đặc tả của chúng là hoạt "
               "động ở một điện áp cụ thể."))

    # B-l / printed p.358 / PDF 379.
    # B36 - Transformers.
    b.append(h4("Máy biến áp", "Transformers"))
    b.append(p("Một lần nữa, việc áp dụng hệ số an toàn cho máy biến áp là "
               "không phù hợp vì nó chỉ làm giảm hiệu suất của thiết bị."))
    # B37 - Switches.
    b.append(h4("Công tắc", "Switches"))
    b.append(p("Vì công tắc không tiêu tán công suất nên không cần hệ số an "
               "toàn, miễn là cấu tạo vật lý của công tắc sao cho hỏng hóc "
               "của nó là lỗi có thể đếm được."))
    # B38 - group heading and paragraph.
    b.append(h4("Các linh kiện chịu hệ số định mức 1.5",
                "Components which are subject to the 1.5 rating factor"))
    b.append(p("Nhìn chung, tất cả các linh kiện khác đều chịu hệ số an toàn "
               "định mức trừ khi, như đã nêu, việc áp dụng hệ số đó làm giảm "
               "mức độ an toàn. Vì hệ số định mức lớn, phép tính toán của nó "
               "có thể thực hiện tương đối đơn giản để tránh sự cần thiết "
               "phải tính toán dài dòng và phức tạp mà không giúp ích nhiều "
               "cho độ an toàn của nguyên lý bảo vệ. Sau đây là các quy "
               "trình tiêu biểu được áp dụng."))
    # B39 - Resistors.
    b.append(h4("Điện trở", "Resistors"))
    b.append(p("Đối với điện trở, công suất tiêu tán được tính ở giá trị cực "
               "đại bao gồm cả dung sai thường được nhà sản xuất công bố, "
               "và ở nhiệt độ môi trường cực đại mà chúng sẽ được sử dụng "
               "theo đặc tả của nhà sản xuất. Công suất tính được này là "
               "công suất sẽ được nhân với hệ số định mức."))
    # B40 - Semiconductors.
    b.append(h4("Chất bán dẫn", "Semiconductors"))
    b.append(p("Đối với chất bán dẫn, cần tính dòng điện, điện áp và công "
               "suất tiêu tán cực đại của chúng. Những giá trị này được xác "
               "định từ thông tin của nhà sản xuất bằng cách xác định công "
               "suất sẽ cho nhiệt độ tiếp xúc chấp nhận được cực đại trong "
               "các điều kiện lắp đặt. Dòng điện cực đại không bị ảnh hưởng "
               "nhiều bởi nhiệt độ vì nó chỉ bị giới hạn bởi các kết nối "
               "mảnh giữa vật liệu bán dẫn và dây dẫn ra ngoài và, dù sao, "
               "cũng sẽ không bị vượt quá nếu công suất được xác định. Điện "
               "áp đánh thủng của bán dẫn nhạy với nhiệt độ do hoạt tính "
               "bán dẫn và điều này phải được quy định trong điều kiện lắp "
               "đặt. Chính các thông số này chịu giới hạn định mức hai phần "
               "ba."))
    # B41 - Zener diodes.
    b.append(h4("Diode Zener", "Zener diodes"))
    b.append(p("Điện áp trên các diode này, cũng quyết định công suất có thể "
               "tiêu tán, sẽ là điện áp do nhà sản xuất quy định trong điều "
               "kiện thử động với nhiệt độ môi trường cực đại trong điều "
               "kiện lắp đặt đã dùng, cộng với dung sai của nhà sản xuất. "
               "Không cần xét đến sự tăng điện áp do nhiệt độ tiếp xúc tăng. "
               "Chính công suất này chịu hệ số định mức áp dụng, chứ không "
               "phải điện áp, vì những lý do rõ ràng."))

    # B-m / printed p.359 / PDF 380.
    # B42 - Capacitors.
    b.append(h4("Tụ điện", "Capacitors"))
    b.append(p("Hệ số định mức cho tụ điện được áp dụng cho điện áp cực đại "
               "mà tụ điện được định mức và cho dòng ac cực đại."))
    b.append(h3("13.7.2 Yêu cầu cụ thể cho các linh kiện riêng biệt",
                "13.7.2 Specific requirements for particular components"))
    # B43 - Fuses under 13.7.2.
    b.append(h4("Cầu chảy", "Fuses"))
    b.append(p("Việc miễn hệ số định mức cho cầu chảy đã được thảo luận "
               "nhưng có một số yêu cầu thích hợp cho cầu chảy liên quan đến "
               "việc chúng bảo vệ các mạch khác và lắp đặt chúng trong khu "
               "vực nguy hiểm. Cầu chảy được dùng thường là loại hộp "
               "(cartridge-type) hoặc tương tự, và cầu chảy có thể thay dây "
               "chảy thường không được chấp nhận. Cầu chảy nên được lắp bên "
               "trong vỏ bọc của thiết bị, ngoại trừ cầu chảy nguồn trong "
               "thiết bị liên kết có thể tiếp cận từ phía trước của thiết bị "
               "nếu chúng dùng giá đỡ thích hợp được thiết kế cho mục đích "
               "đó. Vì cầu chảy thuộc loại được chấp nhận thường là cụm cắm "
               "thương mại, chúng không cần tuân thủ yêu cầu về chiều dài "
               "đường rò và khe hở của nguyên lý bảo vệ được mô tả sau trong "
               "chương này, trừ khi chúng được bọc kín để dùng trong khu vực "
               "nguy hiểm, nhưng chúng cần tuân thủ một Tiêu chuẩn được "
               "công nhận cho cầu chảy như EN 60127 (1991).¹³"))
    # B44.
    b.append(p("Trước hết, cầu chảy sẽ được giả định là liên tục cho qua 1.7 "
               "lần dòng định mức của nó (Iₙ), và các mạch nó bảo vệ nên được "
               "đánh giá trên cơ sở đó. Ngoài ra, đặc tính thời gian/dòng "
               "điện khi đứt của cầu chảy quan trọng vì nó xác định kích "
               "thước của bất kỳ xung nhất thời nào đi qua trong thời gian "
               "đứt. Nếu có thể thu được đặc tính này, các mạch được cầu "
               "chảy bảo vệ cần được đánh giá về hiệu quả của chúng khi có "
               "mặt các xung này để đảm bảo chúng không làm hỏng linh kiện "
               "bên trong. Nếu không có thông tin này thì cần thử nghiệm mười "
               "mẫu của bất kỳ linh kiện nào được cầu chảy bảo vệ bằng cách "
               "cho chúng chịu các xung ở điện áp nguồn của cầu chảy, với "
               "điện trở nguồn bằng điện trở nguội của cầu chảy cộng với bất "
               "kỳ điện trở không hỏng nào khác trong mạch trong điều kiện "
               "cầu chảy cháy, để đảm bảo không xảy ra hư hỏng."))
    # B45.
    b.append(p("Bản thân cầu chảy phải có điện áp định mức ít nhất bằng điện "
               "áp mà nó bảo vệ các mạch chống lại, và định mức dòng dự kiến "
               "đủ để đảm bảo nó sẽ đứt (dòng dự kiến là dòng mà nguồn có thể "
               "cung cấp vào một chỗ ngắn mạch liên tục vì, nếu cầu chảy "
               "không được định mức cho giá trị này, hồ quang sinh ra khi "
               "đứt có thể không dập tắt và dòng điện có thể tiếp tục "
               "chảy). Khi định mức dòng dự kiến của cầu chảy không đủ, dòng "
               "nó cắt có thể được giới hạn bằng cách đưa vào một điện trở "
               "không hỏng (xem sau trong chương này) có đặc tả sau:"))
    # B46 (raw 15654-15656), displayed 3-line specification.
    b.append(eq("điện áp định mức = điện áp nguồn hoặc mạch cực đại (Uₘ, Uᵢ)"
                "<br>dòng định mức = 1.5 × 1.7 × Iₙ (Định mức dòng của cầu chảy)"
                "<br>công suất định mức = 1.5 × (1.7 × Iₙ)² × giá trị điện trở"))

    # B-n / printed p.360 / PDF 381.
    # B47 (raw 15659-15660).
    b.append(p("Yêu cầu dòng dự kiến đối với cầu chảy nguồn thường là "
               "1500 A."))
    # B48 (raw 15661-15668).
    b.append(p("Khi cầu chảy nằm trong khu vực nguy hiểm, sự đứt của chính "
               "dây chảy có thể là nguồn gây đánh lửa và vì vậy bầu khí "
               "quyển nổ phải được ngăn không cho tiếp cận dây chảy. Cầu "
               "chảy phải được bọc kín để ngăn bầu khí quyển nổ xâm nhập và "
               "phương pháp thực hiện việc bọc kín này được mô tả sau trong "
               "chương này. Vấn đề với việc bọc kín là nếu chất bọc lọt vào "
               "cầu chảy nó có thể ảnh hưởng đến hoạt động của cầu chảy. Vì "
               "lý do này cần đảm bảo cụm cầu chảy được làm kín trước khi "
               "bắt đầu bất kỳ công đoạn bọc kín nào."))
    # B49 - Cells and batteries.
    b.append(h4("Cell và bộ pin", "Cells and batteries"))
    b.append(p("Cả cell sơ cấp (những cell không chịu sạc) và cell thứ cấp "
               "đều được phép trong an toàn nội tại miễn là chúng không có "
               "thông số đặc biệt không mong muốn. Ví dụ, cell lithium có "
               "thể nổ, quá nhiệt hoặc xả khí trong điều kiện có dòng điện "
               "chảy vào chúng từ nguồn khác, hoặc chúng bị ngắn mạch hoặc "
               "quá nhiệt. Khi những điều kiện đó có thể xảy ra thì không "
               "nên dùng pin lithium. Hướng dẫn được đưa ra trong HSE "
               "Guidance Note GS 43.¹⁴ Tương tự, cell niken cadmi có thể bị "
               "đảo cực khi xả sâu và sau đó có thể nổ khi sạc. Khi những "
               "điều kiện đó có thể xuất hiện theo cách ảnh hưởng xấu đến "
               "an toàn nội tại thì không cho phép dùng các cell và pin "
               "này. Cần lưu ý rằng đây không phải là lời mời dùng chúng ở "
               "nơi khác vì còn có các vấn đề an toàn khác."))
    # Survey quirk 21 - missing 'that'.
    b.append(note("<b>Lưu ý về câu 'It should be noted this is not an "
                  "invitation...'.</b> Bản in thiếu chữ 'that' sau 'noted'; "
                  "lỗi ngữ pháp này được giữ nguyên trong bản tiếng Anh."))
    # B50 (raw 15682-15695).
    b.append(p("Cell thường không được xác định rõ về bên trong vì nhà sản "
               "xuất liên tục cải tiến hiệu năng bằng cách thay đổi cấu trúc "
               "bên trong. Vì lý do này, người ta thường coi mỗi cell là một "
               "linh kiện được làm kín và chỉ xét các tia lửa và bề mặt nóng "
               "xảy ra bên ngoài nó để đánh giá khả năng đánh lửa. Ngoài ra, "
               "độ tin cậy của cell được xem là đủ để coi một lần ngắn mạch "
               "bên trong là một lỗi có thể đếm được. Tuy nhiên, cách tiếp "
               "cận này có giới hạn và các cell hoặc pin không được làm kín "
               "bằng cách ép nhựa, vòng đệm hoặc tương tự, không được làm "
               "kín bằng vỏ nhựa đúc, hoặc không được hàn kín thì không được "
               "coi là đã làm kín. Giới hạn này chủ yếu ảnh hưởng đến pin "
               "(cụm cell, chứ không phải bản thân các cell) và có nghĩa là "
               "khi vỏ pin chỉ được giữ lại bằng phương pháp ép kim loại "
               "hoặc keo dán giữa các bộ phận không rõ là kín khí, thì bên "
               "trong pin cần được xét đến về khả năng đánh lửa. Các phương "
               "pháp cấu tạo được chấp nhận cho cell hoặc pin là: cell hoặc "
               "pin kín (kín khí); cell hoặc pin kín (điều hòa van); và cell "
               "và pin kín không có van xả áp."))
    # B51 (raw 15696-15697; continues on printed 361).
    b.append(p("Ngoài việc đáp ứng các yêu cầu trên, các cell và pin này còn "
               "chịu giới hạn về cấu tạo ở chỗ chúng cần nằm trong một vỏ "
               "được ép hoặc đúc thành một khối duy nhất, ngoại trừ nắp cuối "
               "hoặc"))

    # B-o / printed p.361 / PDF 382.
    # B52 (raw 15699-15702).
    b.append(p("các nắp phải được hàn vào vỏ, dán vào vỏ bằng keo thích hợp "
               "đảm bảo mối nối kín khí, hoặc được làm kín bằng cách ép mép "
               "trên của vỏ và ép một vòng đệm cách điện khi làm như vậy "
               "(xem Hình 13.12)."))
    # Survey quirk 21 - 'is so doing'.
    b.append(note("<b>Lưu ý về cụm 'compressing an insulating washer is so "
                  "doing'.</b> Bản in dùng 'is' thay vì 'in'; lỗi này được "
                  "giữ nguyên trong bản tiếng Anh, còn bản tiếng Việt dùng "
                  "'khi làm như vậy' theo ý định."))
    # B53 (raw 15703-15711).
    b.append(p("Không có lệnh cấm cụ thể nào về việc rò chất điện giải từ cell "
               "và pin, nhưng nếu chất điện giải thoát ra trong điều kiện "
               "ngắn mạch (khi cell chịu dòng vào hoặc dòng sạc cực đại do "
               "nhà sản xuất quy định bất kể tình trạng của pin, và khi cell "
               "hoặc pin được sạc với một cell đã xả hết, kể cả đảo cực của "
               "một cell khi điều đó xảy ra lúc cell được xả) thì pin cần "
               "được lắp trong một vỏ ngăn không cho chất điện giải rò ra "
               "làm hỏng các mạch an toàn nội tại. (Các cell và pin kín khí "
               "và kín điều hòa van không được coi là giải phóng chất điện "
               "giải.)"))
    b.append(fig(12, FB.fig_f1312()))
    # Survey quirk 22 - Fig. 13.12 OCR.
    b.append(note("<b>Lưu ý về nhãn của Hình 13.12.</b> Lớp OCR đọc 'Fixed 8 "
                  "sealed' và gộp nhầm hai nhãn thành 'Compressed ither metal "
                  "/ insulating or plastic'; ảnh trang in cho thấy 'fixed "
                  "&amp; sealed' và hai nhãn riêng 'Compressed insulating "
                  "sealing washer (Note 1)' cùng 'Cell top either metal or "
                  "plastic'. Dấu &amp; và các nhãn tách riêng được giữ theo "
                  "bản in."))

    # B-p / printed p.362 / PDF 383.
    # B54 (raw 15738-15745).
    b.append(p("Khi cell và pin có thể xả khí (hydro, v.v.) — trường hợp này "
               "có khả năng nhất đối với cell có thể sạc lại — vỏ chứa pin "
               "nên được bố trí để xả trực tiếp khí đã giải phóng ra bên "
               "ngoài thiết bị. Lượng khí giải phóng nếu xử lý theo cách này "
               "khó có thể tạo ra một lượng đáng kể bầu khí quyển nổ bên "
               "trong vỏ và, vì việc sạc đáng kể thường được thực hiện ở khu "
               "vực không nguy hiểm (nếu không thì mạch sạc sẽ cần phải là "
               "mạch an toàn nội tại), việc giải phóng khí khó có thể ảnh "
               "hưởng đến các khu vực nguy hiểm nơi pin được sử dụng."))
    # B55 (raw 15746-15750).
    b.append(p("Các cell có cấu hình hóa học đặc biệt cho điện áp khác nhau "
               "và trong một số trường hợp các điện áp này có thể khác nhau "
               "giữa các cell. Ngoài ra, điện áp liên quan đến đánh lửa bằng "
               "tia lửa thường khác với điện áp thích hợp cho đánh lửa bằng "
               "bề mặt nóng, vì một loại là nhất thời còn loại kia phải tồn "
               "tại trong thời gian đáng kể để gây nóng. Vì vậy, để tránh "
               "nhầm lẫn, điện áp cực đại liên quan đến hai trường hợp này "
               "cho một loạt loại cell được đưa ra trong Bảng 13.6."))
    # Survey quirk 25 - B55 continues into Survey C.
    b.append(note("<b>Lưu ý về điểm kết thúc của đoạn.</b> Đoạn cuối kết "
                  "thúc bằng 'được đưa ra trong Bảng 13.6.'; nội dung tiếp "
                  "theo ở trang in 363 nằm ngoài phạm vi mô-đun này."))
    # Table 13.6 (printed p.362).
    b.append(table(T2.HEAD136_VI, T2.ROWS136_VI, T2.CAPTION136_VI))
    if T2.NOTE136_VI:
        b.append(note(T2.NOTE136_VI))
    # Survey quirk 23 - Table 13.6 OCR.
    b.append(note("<b>Lưu ý về OCR của Bảng 13.6.</b> Lớp OCR đọc 'IEC trpe "
                  "Code', 'Zinc - Ca-bon Leclanche', 'Nofes:' và '(from BSEN "
                  "50020)'; ảnh trang in cho thấy 'IEC type Code', 'Zinc – "
                  "Carbon Leclanche', 'Notes:' và '(from BS/EN 50020)'. "
                  "Đoạn '-zinc 1.6' trong dòng thô là phần cuối của tên loại "
                  "cell 'Mercury – Manganese Dioxide – Zinc' cộng với giá "
                  "trị 1.6."))
    return "".join(b)


def body_en():
    b = []

    # Survey quirk 1 - the assignment's line offset; Survey B is 15070-15811.
    b.append(note("<b>Note on the assigned line offset.</b> The assignment "
                  "states that line 15090 is the '=== PAGE 368 ===' marker; "
                  "in fact line 15090 is '=== PAGE 369 ==='. Printed p. 347 "
                  "(PDF p. 368) begins at raw line 15070 and printed p. 362 "
                  "(PDF p. 383) ends at raw line 15811, with '=== PAGE 384 "
                  "===' at 15812. Survey B therefore spans lines "
                  "15070–15811."))
    # Survey quirk 2 - running-header OCR 7' -> 'i'.
    b.append(note("<b>Note on the running-header OCR.</b> The OCR text layer "
                  "reads the running header as 'Protection concept intrinsic "
                  "safety 7' ' (an apostrophe after the digit 7) on several "
                  "pages; the page renders show 'Protection concept intrinsic "
                  "safety 'i''. The render reading is used throughout."))

    # B-a / printed p.347 / PDF 368: Fig. 13.6, then heading and B1.
    b.append(fig(6, FB.fig_f1306()))
    # Survey quirk 3 - Fig. 13.6 caption OCR.
    b.append(note("<b>Note on the Fig. 13.6 caption.</b> The OCR layer reads "
                  "'Ignition thresholdinductive circuits at t24 V' and "
                  "'fig. 13.4'; the render shows 'Ignition threshold/inductive "
                  "circuits at <24 V' and 'Fig. 13.4'. The caption has no "
                  "full stop after the final '24 V', and the printed note "
                  "uses the singular 'inductive circuit'. All are retained "
                  "verbatim in the English caption."))
    # Survey quirk 4 - Fig. 13.6 axis OCR.
    b.append(note("<b>Note on the axes of Fig. 13.6.</b> The OCR layer reads "
                  "'I' and 'Minimum igniting current L A'; the render shows "
                  "'Inductance L, mH' and 'Minimum igniting current I, A'. "
                  "The correct labels from the render are used in the "
                  "redraw."))
    b.append(h4("Capacitive circuits", "Capacitive circuits"))
    # B1 (raw 15084-15089; continues on printed 348).
    b.append(p("The capacitive sparking mechanism is usually a make spark "
               "occurring when the contacts have been separated for "
               "sufficiently long for the capacitance to charge to the open "
               "circuit voltage, and not when the contacts open for, at that "
               "time, the capacitance to be effectively discharged. The "
               "spark is not normally an arc as the voltage in most "
               "intrinsically safe circuits is not sufficient to break down "
               "an air path, but is a spark occurring when the"))
    # Survey quirk 25 - B1 begins mid-sentence from printed 346.
    b.append(note("<b>Note on the opening of the paragraph.</b> The first "
                  "paragraph of 'Capacitive circuits' begins mid-sentence, "
                  "continuing text from printed p. 346 which lies outside "
                  "this module's span. The sentence is kept incomplete as "
                  "printed."))

    # B-b / printed p.348 / PDF 369.
    # B2 (raw 15092-15097).
    b.append(p("first contact is made and only present because of the "
               "paucity of that contact (i.e., if the contact were made very "
               "firmly and completely at very high speed then almost no "
               "spark would occur). The voltage across the spark begins at "
               "the voltage across a charged capacitor and decays with "
               "charge. Thus energy discharge is not so efficient as in the "
               "inductive case and typical energy values are as follows:"))
    # B3 (raw 15098-15101), displayed values.
    b.append(eq("IIA = 4.0 mJ (at 20 V) – 1.25 mJ (at 100 V)"
                "<br>IIB = 1.0 mJ (at 20 V) – 500 µJ (at 100 V)"
                "<br>IIC = 200 µJ (at 20 V) – 50 µJ (at 100 V)"
                "<br>(240 µJ (at 20 V) – 110 µJ (at 100 V))"))
    # Survey quirk 5 - energy-value OCR.
    b.append(note("<b>Note on the OCR of the energy values.</b> The OCR layer "
                  "reads '2OV'/'lOOV' as '20 V'/'100 V', 'l.OmJ' as '1.0 mJ', "
                  "'llOpJ' as '110 µJ' and 'pJ' as 'µJ'. The first values of "
                  "IIA and IIB are genuinely mJ while the rest are µJ; the "
                  "units are not normalised."))
    # B4 (raw 15102-15103).
    b.append(p("The IIC figures in brackets are the figures from BS 5501, "
               "Part 7⁴ showing a significant reduction in permissible "
               "capacitance in BS/EN 50020¹⁰."))
    # Survey quirk 6 - superscript footnotes eaten by OCR.
    b.append(note("<b>Note on the superscript footnote numerals.</b> The OCR "
                  "layer reads 'Part 74' as 'Part 7⁴', '5002010' as "
                  "'50020¹⁰', 'EN 60127 (1991).13' as 'EN 60127 (1991).¹³', "
                  "'GS 43.14' as 'GS 43.¹⁴' and '5 \"C'/'10 \"C' as "
                  "'5 °C'/'10 °C'. The printed superscripts and degree signs "
                  "are retained in the English text."))
    # B5 (raw 15104-15109).
    b.append(p("Unlike the situation with inductance, the voltage across the "
               "spark tends to fall rapidly as the energy is released thus "
               "inhibiting the release of energy into the spark and, "
               "therefore, energy release is not as efficient, particularly "
               "at low voltages. Figure 13.7 shows the mechanism used for "
               "determination of effective spark ignition energy and Fig. "
               "13.8 shows typical values for the three sub-groups."))
    # Survey quirk 21 - mixed Figure/Fig. in adjacent paragraphs.
    b.append(note("<b>Note on the mixed 'Figure' and 'Fig.'.</b> The print "
                  "writes 'Figure 13.7' but 'Fig. 13.8' in the same "
                  "paragraph, and later uses 'Figure 13.9' followed by "
                  "'Figures 13.10 and 13.11'. The inconsistency is kept as "
                  "printed."))
    # B6 (raw 15110-15113).
    b.append(p("Again, the curves in Fig. 13.8 are based upon capacitors with "
               "very efficient electrolytes and are much more sensitive than "
               "would be the case for such things as electrolytic capacitors. "
               "They can therefore be used with some confidence."))
    b.append(fig(7, FB.fig_f1307()))
    # Survey quirk 21 - Fig. 13.7 note cross-reference and unitless 0.5.
    b.append(note("<b>Note on the note to Fig. 13.7.</b> The printed note "
                  "cross-references 'Fig. 12.11', a Chapter 12 figure rather "
                  "than a Chapter 13 figure, and the value '0.5' is printed "
                  "without a unit. Both are retained as printed."))

    # B-c / printed p.349 / PDF 370.
    b.append(fig(8, FB.fig_f1308()))
    # Survey quirk 7 - both axis ends printed 1.000.
    b.append(note("<b>Note on the axis ends of Fig. 13.8.</b> Both high ends "
                  "of the axes are printed '1.000' in thousands-separator "
                  "style; they are not converted to 1000. The curve labels "
                  "II A, II B and II C are kept as printed."))
    b.append(h4("Resistive circuits", "Resistive circuits"))
    # B7 (raw 15138-15141; continues on printed 350).
    b.append(p("Resistive circuits have, unlike their inductive and "
               "capacitive counterparts, limited voltages and currents. The "
               "sparks produced are usually less intense than the sparks "
               "produced by the discharge of an inductance or capacity but "
               "occur repeatedly as the wires scrape across the lower disc "
               "surface. The ignition mechanism for these is not as well "
               "understood as that associated with"))
    # Survey quirk 12 - line-break hyphenations.
    b.append(note("<b>Note on the line-break hyphenations.</b> The print "
                  "breaks 'igni-tion', 'sub-groups', 'relation-ship' (in the "
                  "Table 13.4 caption), 'evalua-tion' (in the Table 13.6 "
                  "caption), 'de-energized', 'voltage/current', "
                  "'non-countable', 'cartridge-type' and 'plug-in'. Only the "
                  "accidental line-end splits are de-hyphenated; genuine "
                  "compounds are retained."))

    # B-d / printed p.350 / PDF 371.
    # B8 (raw 15144-15145).
    b.append(p("a single application of energy as occurs during the spark in "
               "the inductive and capacitive case."))
    # B9 (raw 15146-15154).
    b.append(p("Figure 13.9 shows the resistive circuit and constant current "
               "voltage limited circuits used to produce minimum ignition "
               "current curves and Figures 13.10 and 13.11 show the curves "
               "themselves for the three sub-groups. The constant current "
               "voltage limited circuits come from a proposal made by the "
               "HSE to the British Standards Institution (BSI) for inclusion "
               "in BS/EN 50020¹⁰ and passed to the European (CENELEC) "
               "committee but not yet acted upon. As already mentioned, the "
               "energy released is not clearly definable and power transfer "
               "capability is the important parameter in this case. This is "
               "typified by the following power capability for ignition "
               "threshold circuits of this type:"))
    # B10 (raw 15155-15157), displayed values.
    b.append(eq("IIA = 2.5 W to 8 W (at 20 V) – 2.1 W to 2.6 W (at 50 V)"
                "<br>IIB = 2.2 W to 6.5 W (at 20 V) – 1.5 W to 1.9 W (at 50 V)"
                "<br>IIC = 0.95 W to 2.5 W (at 20 V) – 0.65 W to 0.8 W (at 50 V)"))
    # B11 (raw 15158-15159).
    b.append(p("Resistive circuits are therefore shown to be more ignition "
               "capable as the voltage rises."))
    b.append(fig(9, FB.fig_f1309()))
    # Survey quirk 8 - Fig. 13.9 label OCR and upper/lower profile difference.
    b.append(note("<b>Note on the labels in Fig. 13.9.</b> The OCR layer reads "
                  "'Spark test apbratus', 'Shoq circuit', 'Current limiting "
                  "yi:;e', 'circui?', 'throu h' and 'loat'; the render shows "
                  "'Spark test apparatus', 'Short circuit', 'Current limiting "
                  "circuit' and 'Current through load'. The upper profile "
                  "caption reads 'voltage/current profile' (lowercase v) "
                  "while the lower reads 'Voltage current profile' (no "
                  "slash, initial capital) — a genuine difference in the "
                  "print."))

    # B-e / printed p.351 / PDF 372.
    b.append(fig(10, FB.fig_f1310()))
    # Survey quirk 9 - Fig. 13.10 axis OCR.
    b.append(note("<b>Note on the axes of Fig. 13.10.</b> The OCR layer reads "
                  "'1 OOmA' and '1 OmA'; the render shows '100mA' and "
                  "'10mA'. Units are printed without a space after the "
                  "numeral (as in '5A' and '10V'), and are kept that way."))
    b.append(h4("Composite circuits", "Composite circuits"))
    # B12 (raw 15212-15219; continues on printed 352).
    b.append(p("Most practical circuits contain some of all three types of "
               "power or energy and these coexist normally because the fault "
               "conditions which give them the maximum risk condition are "
               "different in each case. This means that when one parameter "
               "is at its limit the others are well away from theirs. "
               "Practical testing historically has shown this to be the case "
               "and this can be confirmed by examination of the various "
               "ignition curves in Fig. 13.5, 13.6, 13.8 and 13.10. These "
               "figures show that the effect of the differing methods of "
               "sparking mean that the energies produced are not additive "
               "directly and"))

    # B-f / printed p.352 / PDF 373.
    b.append(fig(11, FB.fig_f1311()))
    # Survey quirk 10 - Fig. 13.11 OCR.
    b.append(note("<b>Note on Fig. 13.11.</b> The OCR layer reads 'Fig. 13.1 "
                  "1'; the render shows 'Fig. 13.11'. Only 'Group IIB' and "
                  "'Group IIC' are labelled in the figure; no 'Group IIA' "
                  "label appears."))
    # B13 (raw 15225-15241).
    b.append(p("the effect of having inductive sparking, together with "
               "resistive sparking, is less ignition capable than would be "
               "expected from a direct addition. This leads to the "
               "possibility of using the curves for more composite circuits "
               "where those sparking parameters, other than the one being "
               "evaluated, are significantly less than the limiting "
               "parameters. Historic application of the curves has shown "
               "that the addition of energies is much less than would be "
               "expected and, although no firm confirmation exists, a "
               "derivation from the inductive circuits and curves (Fig. "
               "13.4 and 13.5) shows that, provided the inductance present "
               "is less than 80 per cent of that permitted at the short "
               "circuit current available from a resistive circuit complying "
               "with Fig. 13.10, it is unlikely that an ignition would result "
               "from the presence of that inductance in a composite circuit. "
               "As a design guide, therefore, it is possible to use the "
               "curves where all but one of the parameters in question "
               "(e.g., inductance, capacitance and resistive limitation) "
               "give figures less than 80 per cent of their limiting figures "
               "in isolation. This may not exclude the necessity for later "
               "testing but will give a high degree of confidence that the "
               "circuits will prove to be intrinsically safe on any later "
               "test."))

    # B-g / printed p.353 / PDF 374.
    b.append(h4("Crowbar protected circuits", "Crowbar protected circuits"))
    # B14 (raw 15245-15251).
    b.append(p("Crowbar-type circuits, where voltage is arranged to collapse "
               "when overloads are applied, present particular problems when "
               "tested. The crowbar removes the voltage on the initial short "
               "circuit in the test apparatus and, depending upon the "
               "recovery of the circuit sparking, is inhibited for some time "
               "after that. The circuit must be tested with the spark test "
               "apparatus but, to ensure that the situation where that "
               "apparatus does not produce the most onerous condition, it "
               "must be shown not to deliver more than the following maximum "
               "energy during the crowbar operation:"))
    # B15 (raw 15252-15254), displayed values.
    b.append(eq("IIA = 160 µJ<br>IIB = 80 µJ<br>IIC = 20 µJ"))
    # B16 (raw 15255-15259).
    b.append(p("These figures are approximately half of those for ignition "
               "in inductive circuits and even less in the case of capacitive "
               "circuits. As the sparking mechanism is different to that for "
               "an inductive circuit, where the addition is more important, "
               "it is possible in design to ignore additive effects with "
               "confidence that any test will be passed."))

    # Survey quirk 24 - the four level-3 spark-mechanism headings are unnumbered.
    b.append(note("<b>Note on the unnumbered headings.</b> The four headings "
                  "on printed pp. 347–353 (Capacitive circuits, Resistive "
                  "circuits, Composite circuits, Crowbar protected circuits) "
                  "are unnumbered subsections of 13.5; they are presented as "
                  "headings rather than prose. Every figure and table in "
                  "this span is numbered."))

    b.append(h3("13.6 Confirmation of intrinsic safety in respect of hot surface ignition",
                "13.6 Confirmation of intrinsic safety in respect of hot surface ignition"))
    # B17 (raw 15262-15272).
    b.append(p("As already stated, there are no safety factors applied to "
               "voltages and currents in respect of hot surface ignition. "
               "Like the other protection concepts, however, a basic safety "
               "factor of 5 °C is applied in the case of temperature classes "
               "T3 to T6 and 10 °C in the case of T1 and T2, by requiring "
               "that maximum surface temperature is below the class limit by "
               "that amount. This requirement in BS/EN 50020¹⁰ represents a "
               "change for that in BS 5501, Part 7⁴ which, by wording in its "
               "exclusion clauses, did not require the 5 °C or 10 °C "
               "difference. The maximum surface temperature is, of course, "
               "measured in all cases in the appropriate worst case "
               "conditions specified for 'ia' and 'ib' and, the fault "
               "conditions which need to be taken into account may well be "
               "different to those used for spark ignition evaluation."))
    # Survey quirk 11 - the HSE acronym mismatch.
    b.append(note("<b>Note on 'Safety in Mines Research Establishment "
                  "(HSE)'.</b> The expanded name does not match the acronym "
                  "HSE; this is a source error and is preserved verbatim in "
                  "the English text. Both 5 °C and 10 °C carry the degree "
                  "sign."))
    # B18 (raw 15273-15282; continues on printed 354).
    b.append(p("As intrinsic safety is typically an instrumentation concept "
               "using small electronic components, the normal requirements "
               "for maximum temperature are very onerous, particularly as "
               "they are in fault conditions and it is known that it is more "
               "difficult to ignite explosive atmospheres by small "
               "components. Considerable work done by the Safety in Mines "
               "Research Establishment (HSE) in the UK has led to a situation "
               "where considerable relaxations are permitted for small "
               "components. For T5 temperature classification it is "
               "permissible for typical components with a total surface area "
               "of less than 10 cm² (excluding any lead-out wires forming "
               "part of the component) to reach a measured temperature of "
               "145 °C without causing"))

    # B-h / printed p.354 / PDF 375.
    # B19 (raw 15284-15289).
    b.append(p("ignition, whereas for larger components the figure is 95 °C "
               "(these figures representing elevations over the maximum "
               "ambient temperature permitted plus the ambient itself). For "
               "T4 classification, where the normal maximum measured "
               "temperature should not exceed 120 °C, the situation is more "
               "flexible and Table 13.3 indicates the relaxations "
               "permissible."))
    # B20 (raw 15290-15294; resumes after the tables).
    b.append(p("There is also the possibility that wiring in intrinsically "
               "safe circuits may be a source of ignition and to this end "
               "specific requirements are applied to ensure that this is not "
               "so. Maximum currents are specified for the various types of "
               "wiring encountered to ensure that these do not exceed the "
               "limiting temperature for the required temperature class. "
               "Figures for copper wire"))
    # Table 13.3 (printed p.354).
    b.append(table(T1.HEAD133_EN, T1.ROWS133, T1.CAPTION133_EN))
    if T1.NOTE133_EN:
        b.append(note(T1.NOTE133_EN))
    # Survey quirk 13 - Table 13.3 source anomaly.
    b.append(note("<b>Note on the third row of Table 13.3.</b> That row "
                  "prints '≥20 mm²', duplicating the lower bound of the "
                  "second row; '≥10 cm²' is the likely intended reading but "
                  "the printed anomaly is preserved. The OCR layer read '≥' "
                  "as 't'; the render governs."))
    # Table 13.4 (printed p.354).
    b.append(table(T1.HEAD134_EN, T1.ROWS134, T1.CAPTION134_EN))
    if T1.NOTE134_EN:
        b.append(note(T1.NOTE134_EN))
    # Survey quirk 14 - Table 13.4 source anomaly.
    b.append(note("<b>Note on Table 13.4.</b> The caption is printed with "
                  "the line-break splits 'relation- / ship' and 'temper- / "
                  "ature'; the unhyphenated wording is given as one string. "
                  "In the 0.5 mm row the printed T6 value 6.7 is lower than "
                  "the T5 value 6.9 — a source anomaly preserved here. The "
                  "OCR layer read the header unit as '(m2)' while the render "
                  "shows '(mm²)'."))

    # B-i / printed p.355 / PDF 376 - Table 13.5.
    b.append(table(T2.HEAD135_EN, T2.ROWS135, T2.CAPTION135_EN))
    if T2.NOTE135_EN:
        b.append(note(T2.NOTE135_EN))
    # Survey quirks 15 and 16 - Table 13.5 numeric oddities and x-ref error.
    b.append(note("<b>Note on the four numeric oddities in Table 13.5.</b> "
                  "'01.3' has a leading zero (row 0.3, T6 A), '195.0' has a "
                  "misplaced decimal point (row 0.3, T6 B), '4.02' is out of "
                  "sequence (row 1.5, T6 A) and '117.0' has a superfluous "
                  "leading 1 (row 3.0, T5 C). All are reproduced exactly as "
                  "printed. Note 5 cross-references 'Table 13.2' although "
                  "the applicable table is Table 13.5 — the source "
                  "cross-reference error is preserved."))
    # B21 (raw 15483-15485).
    b.append(p("and copper printed circuit board tracks are given in Tables "
               "13.4 and 13.5 respectively. No figures are given for higher "
               "temperature classes (T1, T2 and T3) as experience has shown "
               "that these are not normally required."))
    # B22 (raw 15486-15487; continues on printed 356).
    b.append(p("There is also a calculation procedure possible to cover "
               "unusual circumstances such as these cases and conductors of "
               "other metals such as"))

    # B-j / printed p.356 / PDF 377.
    # B23 (raw 15490-15491).
    b.append(p("ligaments in moving coil meters etc. The current limit for "
               "any temperature limit can be defined by:"))
    # B24 (raw 15492), displayed equation.
    b.append(eq("Iₘₐₓ = I<sub>f</sub>{t(1 + αT)/T(1 + αt)}<sup>0.5</sup> amps"))
    # Survey quirk 17 - E4 formula OCR.
    b.append(note("<b>Note on formula E4.</b> The OCR layer reads 'I, = If(t(1 "
                  "+ aT)/T(l + amps'; the render shows Iₘₐₓ = I<sub>f</sub>"
                  "{t(1 + αT)/T(1 + αt)}<sup>0.5</sup> amps, with the "
                  "leading 't' inside the brace and the trailing 't' in the "
                  "denominator — both are in the print. The OCR layer reads "
                  "'O.O04265/\"C' as '0.004265/°C'."))
    # B25 (raw 15493-15501), definition block.
    b.append(eq("where Iₘₐₓ = maximum permissible current    Amps"
                "<br>I<sub>f</sub> = current at which the wire melts    Amps"
                "<br>t = temperature class limit (−5 °C or 10 °C)    °C"
                "<br>T = temperature at which wire melts    °C"
                "<br>α = temperature coefficient of resistance"
                "<br>for wire material (α for copper is 0.004265/°C)    /°C"))
    # B26 (raw 15502-15506).
    b.append(p("The above formula will again give a worst case scenario as "
               "the wires in question will be connected to termination "
               "components which will have significant mass and therefore "
               "the actual temperature can be expected to be lower due to "
               "the thermal shunting effect of such devices, unless the wire "
               "is very long which is not normally the case in apparatus."))
    # B27 (raw 15507-15521).
    b.append(p("If this approach does not give the desired result there is a "
               "final approach which may be taken but this is based upon a "
               "test and applies only to T4. The component to be evaluated "
               "is placed in a chamber filled with a mixture of air and "
               "diethyl ether in the ratio 72% ± 2% air and 28% ± 2% diethyl "
               "ether. The component is then energized with the maximum "
               "power which it can dissipate in fault conditions and the "
               "temperature of the gas mixture raised by 25 °C above the "
               "maximum desired ambient temperature of operation. No "
               "ignitions or cold flames (blue coronas) should occur. "
               "Ignitions can be determined by measurement of sudden "
               "temperature elevation with a thermocouple in the gas or by "
               "visual or other methods, but cold flames are likely only to "
               "be identified by visual methods. To ensure repeatability "
               "these tests should be repeated on at least five samples of "
               "the components in question. As an alternative to raising "
               "the gas temperature to achieve the 25 °C above maximum "
               "ambient, the temperature of the component can be similarly "
               "raised."))
    # Survey quirk 18 - ether-mixture OCR.
    b.append(note("<b>Note on the ether-mixture OCR.</b> The OCR layer reads "
                  "'72% f 2%' and '28% f 2%'; the render shows '72% ± 2%' and "
                  "'28% ± 2%'. The ± signs, the 25 °C figure, the five "
                  "samples and the phrase 'cold flames (blue coronas)' are "
                  "all retained as printed."))
    # B28 (raw 15522-15533).
    b.append(p("The temperature of windings of transformers and coils are "
               "sometimes difficult to measure directly and an indirect "
               "method of measurement is acceptable for these item. The "
               "method used is the resistance variation method and relies "
               "upon measurements of the resistance at ambient temperature "
               "with the coil de-energized and then a further measurement "
               "taken after the coil has been energized for sufficient time "
               "for the temperature to stabilize. No figure for this time is "
               "given but it should be sufficient to utilize a time where "
               "the current in the coil does not change by more than one per "
               "cent per hour after taking account of the change in supply "
               "voltage at constant temperature. Measurement of the initial "
               "voltage/current relationship and the final relationship will "
               "give two values for resistance – one cold and one at heated "
               "equilibrium provided a dc supply is used. If the supply is "
               "ac, the cold resistance will need to be measured, and the "
               "hot resistance immediately after isolating the ac supply. "
               "The temperature rise can then be calculated from:"))
    # Survey quirk 21 - 'acceptable for these item'.
    b.append(note("<b>Note on 'acceptable for these item'.</b> The print uses "
                  "the singular 'item' here; the form is retained in the "
                  "English text while the Vietnamese follows the intended "
                  "plural meaning."))
    # B29 (raw 15534), displayed equation.
    b.append(eq("t = {R(k + t₁)/r} − (k + t₂ − t₁)"))

    # B-k / printed p.357 / PDF 378.
    # B30 (raw 15537-15547), definition block.
    b.append(eq("where t = temperature rise    °C"
                "<br>t₁ = initial ambient temperature (when r is measured)    °C"
                "<br>t₂ = final ambient temperature (when R is measured)    °C"
                "<br>R = measured final resistance (after energization)    Ohms"
                "<br>r = measured initial resistance (before energization)    Ohms"
                "<br>k = constant (234.5 for copper) (This constant is the α,"
                "<br>inverse of the temperature coefficient of resistance)"))
    # Survey quirks 19 and 20 - E6 formula OCR and k-definition wording.
    b.append(note("<b>Note on formula E6 and the definition of k.</b> The OCR "
                  "layer reads 't = {R(k + tl)/r) - (k + t2 - tl)'; the render "
                  "shows t = {R(k + t₁)/r} − (k + t₂ − t₁), with a closing "
                  "curly brace rather than a parenthesis. The printed "
                  "definition 'k = constant (234.5 for copper) (This constant "
                  "is the α, inverse of the temperature coefficient of "
                  "resistance)' is self-contradictory in wording but is "
                  "preserved verbatim in the English text."))
    # B31 (raw 15548-15551).
    b.append(p("This formula takes into account any variation of ambient "
               "temperature between the time when the cold resistance of "
               "the winding is measured prior to its energization and that "
               "when its temperature is again measured after it has been "
               "energized and its temperature has stabilized at its maximum "
               "value."))
    b.append(h3("13.7 Basic component and construction requirements",
                "13.7 Basic component and construction requirements"))
    b.append(h3("13.7.1 Safety factors on component rating",
                "13.7.1 Safety factors on component rating"))
    # B32 (raw 15554-15564).
    b.append(p("Components and connectors need to be operated at no more "
               "than two thirds of their relevant maximum rated operating "
               "voltage, current and power in their conditions of use if "
               "their failures are to be considered as countable faults. "
               "This criterion needs to be true in both normal operation of "
               "the intrinsically safe circuit and with the appropriate "
               "countable and non-countable faults applied elsewhere in that "
               "circuit (this criterion is normally determined by confining "
               "faults to within the apparatus itself and defining maximum "
               "supply or external circuit parameters which the rest of the "
               "intrinsically safe circuit must not exceed in the worst case "
               "of the entire fault count and associated non-countable faults "
               "elsewhere in the system). Clearly such a requirement does "
               "not make sense in the case of such things as fuses, relays, "
               "thermal trips, transformers and similar devices as these "
               "operate differently."))
    b.append(h4("Components not subjected to the 1.5 rating factor",
                "Components not subjected to the 1.5 rating factor"))
    # B33 - Fuses (printed p.357).
    b.append(h4("Fuses", "Fuses"))
    b.append(p("The specification for such fuses is concerned with their "
               "ability to interrupt current at a specific level and "
               "applying the rating factor above would produce a more "
               "dangerous condition as more current would be let through "
               "before they ruptured."))
    # B34 - Thermal trips.
    b.append(h4("Thermal trips", "Thermal trips"))
    b.append(p("Thermal trips are intended to operate at specific "
               "temperatures and no temperature rating reduction is "
               "specified. Also, if they are current operated any attempt "
               "at applying rating factors could cause them to be less "
               "effective."))
    # B35 - Relays.
    b.append(h4("Relays", "Relays"))
    b.append(p("Applying a safety factor to voltage or current to a relay "
               "would prevent operation of the device as their specification "
               "is to operate at a specific voltage."))

    # B-l / printed p.358 / PDF 379.
    # B36 - Transformers.
    b.append(h4("Transformers", "Transformers"))
    b.append(p("Again, application of safety factors to transformers is "
               "inappropriate as they would achieve nothing other than to "
               "damage the efficiency of the device."))
    # B37 - Switches.
    b.append(h4("Switches", "Switches"))
    b.append(p("As switches do not dissipate power then no safety factor is "
               "necessary provided the physical construction of the switch "
               "is such that its failure is a countable fault."))
    # B38 - group heading and paragraph.
    b.append(h4("Components which are subject to the 1.5 rating factor",
                "Components which are subject to the 1.5 rating factor"))
    b.append(p("In general, all other components are subjected to the rating "
               "safety factor unless, as already stated, the application of "
               "that factor produces a reduced level of security. As the "
               "rating factor is large, its calculation can be done in a "
               "relatively simplistic way to avoid the necessity for long "
               "and tortuous calculation which will do little to add to the "
               "security of the protection concept. Typical of the "
               "procedures adopted are the following."))
    # B39 - Resistors.
    b.append(h4("Resistors", "Resistors"))
    b.append(p("Resistors will have their power dissipation calculated at "
               "the maximum value including manufacturers tolerances "
               "normally quoted, and at the maximum ambient temperature in "
               "which they are to be used to the manufacturers "
               "specifications. The power so calculated will be the power "
               "subjected to multiplication by the rating factor."))
    # B40 - Semiconductors.
    b.append(h4("Semiconductors", "Semiconductors"))
    b.append(p("Semiconductors need to have their maximum current, voltage "
               "and power dissipation calculated. These are done using "
               "manufacturers information by determining the power which "
               "would give the maximum acceptable junction temperature in "
               "the mounting conditions. Maximum current is not seriously "
               "affected by the temperature as it is only limited by the "
               "fine connections between the semiconductor material and the "
               "outgoing wires and will not, in any event, be exceeded if "
               "the power is defined. Semiconductor breakdown voltage is "
               "temperature sensitive due to semiconductor activity and this "
               "must be specified in the conditions of mounting. It is these "
               "parameters which are subjected to the two thirds rating "
               "limitation."))
    # B41 - Zener diodes.
    b.append(h4("Zener diodes", "Zener diodes"))
    b.append(p("The voltage across these, which also determines the power "
               "which can be dissipated, will be the manufacturers specified "
               "voltage in dynamic test conditions at the maximum ambient "
               "temperature in the mounting conditions used, with the "
               "manufacturers tolerance added. Voltage elevation due to "
               "junction temperature elevation need not be considered. It is "
               "this power to which the rating factor is applied not, for "
               "obvious reasons, the voltage."))

    # B-m / printed p.359 / PDF 380.
    # B42 - Capacitors.
    b.append(h4("Capacitors", "Capacitors"))
    b.append(p("The rating factor for capacitors is applied to the maximum "
               "voltage for which the capacitor is rated and the maximum ac "
               "current."))
    b.append(h3("13.7.2 Specific requirements for particular components",
                "13.7.2 Specific requirements for particular components"))
    # B43 - Fuses under 13.7.2.
    b.append(h4("Fuses", "Fuses"))
    b.append(p("The exemption of rating factors for fuses has already been "
               "discussed but there are several requirements appropriate to "
               "fuses concerned with their protection of other circuits and "
               "their installation in a hazardous area. The fuses used are "
               "normally cartridge-type fuses or similar, and rewirable "
               "fuses are not normally acceptable. Fuses should be mounted "
               "inside any enclosure for the apparatus, except that mains "
               "fuses in associated apparatus may be accessible from the "
               "front of the apparatus if they use proper holders designed "
               "for that purpose. As fuses of the acceptable type are "
               "normally commercial plug-in assemblies, they do not need to "
               "comply with the creepage and clearance requirements of the "
               "protection concept which are described later in this chapter "
               "unless they are encapsulated for use in a hazardous area, "
               "but they do need to comply with a recognized Standard for "
               "fuses such as EN 60127 (1991).¹³"))
    # B44.
    b.append(p("First, the fuse will be assumed to continuously let through "
               "1.7 times its rated current (Iₙ), and the circuits which it "
               "protects should be evaluated on that basis. In addition, the "
               "rupturing time/current characteristic of the fuse is "
               "important in that it determines the size of any transient "
               "let through during the rupturing time. If this can be "
               "obtained the circuits protected by the fuse need to be "
               "evaluated in regard to their performance in the presence of "
               "these transients to ensure that they do not damage the "
               "components therein. If this information is not available "
               "then it is necessary to test ten samples of any component "
               "protected by the fuse by subjecting it to pulses at the fuse "
               "supply voltage, with a source resistance equal to the cold "
               "resistance of the fuse plus any other infallible resistance "
               "in the circuit in the condition where the fuse blows, to "
               "ensure no damage occurs."))
    # B45.
    b.append(p("The fuse itself must have a voltage rating of at least that "
               "of the voltage against which it is protecting circuits, and "
               "a prospective current rating sufficient to ensure that it "
               "will rupture (the prospective current is the current which "
               "the supply can provide into a short circuit continuously as, "
               "if the fuse is not rated for this, the arc produced on "
               "rupture may not extinguish and current may continue to "
               "flow). Where the prospective current rating of a fuse is not "
               "sufficient the current it ruptures can be limited by the "
               "inclusion of an infallible resistor (see later in this "
               "chapter) which has the following specification:"))
    # B46 (raw 15654-15656), displayed 3-line specification.
    b.append(eq("voltage rating = maximum supply or circuit voltage (Uₘ, Uᵢ)"
                "<br>current rating = 1.5 × 1.7 × Iₙ (The fuse current rating)"
                "<br>power rating = 1.5 × (1.7 × Iₙ)² × value of resistance"))

    # B-n / printed p.360 / PDF 381.
    # B47 (raw 15659-15660).
    b.append(p("The prospective current requirements for mains fuses are "
               "normally 1500 A."))
    # B48 (raw 15661-15668).
    b.append(p("Where the fuse is in a hazardous area the rupture of the "
               "fuse element itself could be a source of ignition and "
               "therefore the explosive atmosphere must be excluded from "
               "the fuse element. The fuse must be encapsulated to prevent "
               "explosive atmosphere access and the method of carrying out "
               "such encapsulation is described later in this chapter. The "
               "problem with encapsulation is that if it enters the fuse it "
               "can affect its operation. For this reason it is necessary "
               "to ensure the fuse assembly is sealed before any "
               "encapsulation is commenced."))
    # B49 - Cells and batteries.
    b.append(h4("Cells and batteries", "Cells and batteries"))
    b.append(p("Both primary cells (those not subject to charging) and "
               "secondary cells are permitted within intrinsic safety "
               "provided they do not exhibit particular unwelcome "
               "parameters. Lithium cells, for example, can explode, "
               "overheat, or vent in conditions where a current flows into "
               "them from another power source, or they are subjected to "
               "short circuit or overheating. Where these conditions can "
               "occur lithium batteries should not be used. Guidance is "
               "given in HSE Guidance Note GS 43.¹⁴ Likewise, nickel "
               "cadmium cells can suffer polarity reversal if deeply "
               "discharged, and may then explode on charge. Where these "
               "conditions can appear in a way which adversely affects "
               "intrinsic safety, such cells and batteries are not "
               "permitted. It should be noted this is not an invitation for "
               "their use elsewhere as other safety issues are present."))
    # Survey quirk 21 - missing 'that'.
    b.append(note("<b>Note on 'It should be noted this is not an "
                  "invitation...'.</b> The print omits 'that' after 'noted'; "
                  "the grammatical slip is preserved verbatim in the "
                  "English text."))
    # B50 (raw 15682-15695).
    b.append(p("Cells are normally ill defined as to their interiors as "
               "manufacturers are continually improving their performance "
               "by altering the internal construction. For this reason it is "
               "normal to consider each cell as a sealed component and "
               "consider only the sparks and hot surfaces which occur "
               "outside it for the purposes of ignition capability. In "
               "addition, the reliability of a cell is considered as "
               "sufficient to consider an internal short circuit as a "
               "countable fault. There are limits to this approach, however, "
               "and cells or batteries which are not sealed by compression "
               "of plastics, washers or similar, not sealed by moulded "
               "plastic enclosures, or not fusion sealed are not considered "
               "as sealed. This limit mainly affects batteries (assemblies "
               "of cells, rather than the cells themselves) and means that "
               "where battery enclosures are only held together by metal "
               "swageing or adhesion between parts which are not clearly "
               "gas tight, the interior of the battery needs to be considered "
               "as far as ignition possibilities are concerned. Acceptable "
               "methods of cell or battery construction are: sealed (gas "
               "tight) cells or batteries; sealed (valve regulated) cells or "
               "batteries; and sealed cells and batteries not having pressure "
               "relief valves."))
    # B51 (raw 15696-15697; continues on printed 361).
    b.append(p("In addition to satisfying the above requirements such cells "
               "and batteries have limits applied to their construction in "
               "that they need to be in an enclosure which is spun or "
               "moulded in one piece apart from the end cover or"))

    # B-o / printed p.361 / PDF 382.
    # B52 (raw 15699-15702).
    b.append(p("covers which must be either fused to the enclosure, stuck to "
               "it with appropriate adhesive ensuring the joint is gas "
               "tight, or sealed by swageing over the end of the enclosure "
               "and compressing an insulating washer is so doing (see Fig. "
               "13.12)."))
    # Survey quirk 21 - 'is so doing'.
    b.append(note("<b>Note on 'compressing an insulating washer is so "
                  "doing'.</b> The print writes 'is' where 'in' is intended; "
                  "the slip is preserved verbatim in the English text while "
                  "the Vietnamese follows the intended meaning."))
    # B53 (raw 15703-15711).
    b.append(p("There is no specific prohibition on the leakage of "
               "electrolyte from cells and batteries but if electrolyte is "
               "released either in short circuit conditions (when the cell "
               "is subjected to the maximum input or charging current "
               "specified by the manufacturer whatever the battery "
               "condition, and where the cell or battery is charged with "
               "one cell fully discharged including reversal of a single "
               "cell where this occurs when the cell is discharged) the "
               "battery needs to be fitted in an enclosure which prevents "
               "the leaked electrolyte from damaging the intrinsically safe "
               "circuits. (Sealed gas-tight and sealed valve-regulated cells "
               "and batteries are not considered to release electrolyte.)"))
    b.append(fig(12, FB.fig_f1312()))
    # Survey quirk 22 - Fig. 13.12 OCR.
    b.append(note("<b>Note on the labels in Fig. 13.12.</b> The OCR layer "
                  "reads 'Fixed 8 sealed' and merges two labels into "
                  "'Compressed ither metal / insulating or plastic'; the "
                  "render shows 'fixed &amp; sealed' and two separate labels, "
                  "'Compressed insulating sealing washer (Note 1)' and 'Cell "
                  "top either metal or plastic'. The ampersand and the "
                  "separate labels are retained as printed."))

    # B-p / printed p.362 / PDF 383.
    # B54 (raw 15738-15745).
    b.append(p("Where cells and batteries can vent gases (hydrogen, etc.) "
               "which is most likely in cases where they are chargeable "
               "cells, the battery container should be arranged to vent the "
               "released gases directly to the outside of the apparatus. The "
               "amount released if handled in this way is unlikely to create "
               "any significant amount of explosive atmosphere inside the "
               "enclosure and, as significant charging is normally done in a "
               "non-hazardous area because otherwise the charging circuit "
               "would need to be an intrinsically safe circuit, release is "
               "not likely to affect the hazardous areas in which the "
               "batteries are used."))
    # B55 (raw 15746-15750).
    b.append(p("Cells of particular chemical configuration will give "
               "different voltages and these can vary from cell to cell in "
               "some cases. In addition, the voltage relevant to spark "
               "ignition will often be different to that appropriate for hot "
               "surface ignition as one is transient and the other has to "
               "exist for considerable lengths of time to cause heating. To "
               "avoid confusion, therefore, the maximum voltages relevant "
               "in the two cases for a range of cell types are given in "
               "Table 13.6."))
    # Survey quirk 25 - B55 continues into Survey C.
    b.append(note("<b>Note on the end of the paragraph.</b> The final "
                  "paragraph ends with 'given in Table 13.6.'; text resumes "
                  "on printed p. 363, which lies outside this module's "
                  "span."))
    # Table 13.6 (printed p.362).
    b.append(table(T2.HEAD136_EN, T2.ROWS136, T2.CAPTION136_EN))
    if T2.NOTE136_EN:
        b.append(note(T2.NOTE136_EN))
    # Survey quirk 23 - Table 13.6 OCR.
    b.append(note("<b>Note on the OCR of Table 13.6.</b> The OCR layer reads "
                  "'IEC trpe Code', 'Zinc - Ca-bon Leclanche', 'Nofes:' and "
                  "'(from BSEN 50020)'; the render shows 'IEC type Code', "
                  "'Zinc – Carbon Leclanche', 'Notes:' and '(from BS/EN "
                  "50020)'. The '-zinc 1.6' fragment in the raw text is the "
                  "tail of the cell type 'Mercury – Manganese Dioxide – "
                  "Zinc' plus the value 1.6."))
    return "".join(b)
