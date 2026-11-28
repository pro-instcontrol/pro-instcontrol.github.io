# -*- coding: utf-8 -*-
"""Chapter 15, module B - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 462-467 (PDF pp. 483-488).

Covers the continuation of the enclosure-materials paragraph from printed
p. 461, sections 15.4.2-15.4.6 (joints, spindles and shafts, light-transmitting
parts, fasteners), section 15.5 and 15.5.1-15.5.3 (connection facilities,
cable and conduit entries, fuses and switchgear), with all unnumbered joint
subheadings. Figures 15.1-15.2 and Table 15.2 are embedded in printed order.
The last paragraph stops at the page break on printed p. 467 with the words
'The term ‘remotely'; its continuation belongs to printed p. 468 and module C.

Printed quirks are kept in the English text (0.5mm, 6.3μm, necessary
IP-rating, normal service, Semi-permanent, the five-item joint list, the ≥
inequalities in Fig. 15.1, IP-rating ‘dry’, the lowercase ‘o’ ring, the inline
Fig. 15.2 Note, the table operators, in principal, cylindrical conical, roll,
BS/EN 50014⁹) with bilingual notes; the Vietnamese follows the intended
meaning. This is an unofficial study translation. The source PDF is not
republished.
"""
from mcmillan_common import h3, h4, p, note, table, fig, ul, ol
import mcmillanfig15 as F
import mcmillan_tbl15_1_2 as T


def body_vi():
    b = []

    # B1 (raw 19855-19863; continuation of a paragraph from printed 461).
    b.append(p("các yêu cầu nhằm ngăn ngừa sự đánh lửa như vậy. Nếu điều đó "
               "xảy ra, có một nguy cơ thực sự là nhiệt độ tăng cao có thể "
               "làm hư hỏng tính toàn vẹn của vỏ bọc, dẫn đến đánh lửa bất kỳ "
               "đám mây hoặc lớp bụi nào bao quanh, và vì vậy yêu cầu này có "
               "tầm quan trọng lớn hơn trong bối cảnh này. Các phương pháp "
               "chứng minh tính không cháy và sự ngăn ngừa truyền lửa không "
               "được xác định cụ thể liên quan đến nguy cơ đặc biệt này và "
               "các phương pháp chứng minh công nghiệp điển hình được chấp "
               "nhận (ví dụ, BS 2782, BS 6458 và BS 6334 là các Tiêu chuẩn "
               "điển hình có thể được dùng cho mục đích này nhưng chúng "
               "không phải là duy nhất và có thể dùng các phương pháp được "
               "công nhận khác)."))
    b.append(note("<b>Lưu ý về đoạn mở đầu.</b> B1 là phần tiếp nối của một "
                  "đoạn bắt đầu ở trang in 461, nằm ngoài phạm vi mô-đun "
                  "này. Đoạn được giữ ở dạng chưa trọn vẹn ở đầu như bản in."))

    # Unnumbered subheading "Mechanical strength" (printed 462).
    b.append(h4("Độ bền cơ học", "Mechanical strength"))
    # B3 (raw 19865-19871).
    b.append(p("Độ bền cơ học của vỏ bọc được yêu cầu phải sao cho nó không "
               "bị hư hỏng, ngoại trừ hư hỏng bề mặt, bởi các thử nghiệm va "
               "đập và rơi. Các thử nghiệm này giống hệt với các thử nghiệm "
               "dùng cho thiết bị dùng cho nguy cơ khí và hơi (xem Chương 8), "
               "ngoại trừ việc, vì vỏ bọc là yếu tố then chốt, mức thử nghiệm "
               "va đập thấp hơn dành cho vỏ bọc dự định chỉ lắp đặt ở những "
               "khu vực có nguy cơ va đập cơ học thấp là không được chấp "
               "nhận; luôn luôn yêu cầu mức cao hơn."))

    # Heading 15.4.2 (printed 462).
    b.append(h3("15.4.2 Mối nối dự định được mở trong điều kiện sử dụng "
                "bình thường",
                "15.4.2 Joints intended to be opened in normal service"))
    b.append(note("<b>Lưu ý về ‘normal service’.</b> Lớp OCR đọc tiêu đề là "
                  "'15.4.2 Joints intended to be opened in normal setvice'; "
                  "ảnh trang in cho thấy rõ 'normal service'. Bản tiếng Anh "
                  "giữ cách đọc theo ảnh trang in."))

    # Unnumbered subheading "Non-gasketted joints" (printed 462).
    b.append(h4("Các mối nối không dùng gioăng", "Non-gasketted joints"))
    # B6 (raw 19874-19883).
    b.append(p("Các mối nối kim loại/kim loại và các mối nối tương tự trong "
               "vỏ bọc không dùng gioăng nén có thể được sử dụng miễn là có "
               "thể chứng minh vỏ bọc đạt được cấp IP mong muốn. Những mối "
               "nối này phải tuân theo các yêu cầu tối thiểu nhằm bảo đảm "
               "tính lặp lại, đó là mối nối phải khít chặt và có chiều rộng "
               "tối thiểu mà tại đó đạt được sự khít chặt, được định nghĩa "
               "là đường xâm nhập của bụi. Không đưa ra con số nào cho sự "
               "khít chặt nhưng khuyến nghị áp dụng giới hạn tách biệt tối "
               "đa là 0.5 mm, với điều kiện vỏ bọc phải đáp ứng cấp IP cần "
               "thiết. Điều này cho phép sử dụng tất cả các vỏ bọc chống "
               "cháy nổ đáp ứng phép thử IP cần thiết. Yêu cầu tối thiểu về "
               "độ phẳng của mối nối ít nhất là 6.3 μm cũng được áp dụng vì "
               "lý do tương tự. Các mối nối điển hình được cho trong Hình "
               "15.1."))
    b.append(note("<b>Lưu ý về ‘0.5mm’, ‘6.3μm’ và ‘necessary IP-rating’.</b> "
                  "Bản in viết 'a maximum separation limit of 0.5mm' (không "
                  "có dấu cách), 'at least 6.3μm' (chữ μ Hy Lạp, không dấu "
                  "cách; lớp OCR đã bỏ mất đơn vị) và 'the necessary "
                  "IP-rating' (OCR đọc 'necessary E'-rating'). Cả ba được "
                  "giữ nguyên trong bản tiếng Anh; bản tiếng Việt theo nghĩa "
                  "đúng."))

    # B7 (raw 19884-19890): intro plus the five-item list as printed.
    b.append(p("Đường xâm nhập bụi tối thiểu (chiều rộng) cho các mối nối như "
               "sau:"))
    b.append(ul([
        "Mối nối mặt bích phẳng – 5 mm",
        "Mối nối dạng chốt (spigot) – 3 mm",
        "Mối nối trụ – 3 mm",
        "Mối nối nón – 3 mm",
        "Mối nối ren – 5 mm",
    ]))
    b.append(note("<b>Lưu ý về danh sách năm mục.</b> Bản in liệt kê năm mục "
                  "với dấu gạch ngang (en dash) và không có dấu cách trước "
                  "giá trị: 'Flat flanged joints – 5mm', 'Spigot joints – "
                  "3mm', 'Cylindrical joints – 3mm', 'Conical joints – 3mm', "
                  "'Threaded joints – 5mm'. Cách viết và dấu gạch ngang được "
                  "giữ nguyên trong bản tiếng Anh."))

    # B8 (raw 19891-19892; continues on printed 463).
    b.append(p("Các mối nối này không được dùng các biện pháp bổ sung như "
               "hợp chất bịt kín không đông cứng để hỗ trợ đạt được cấp IP "
               "cần thiết mà phải"))

    # Fig. 15.1 (printed 463), at the head of the page.
    b.append(fig(1, F.fig_f1501()))
    b.append(note("<b>Lưu ý về các kích thước trong Hình 15.1.</b> Ảnh trang "
                  "in cho thấy rõ 'A ≥ 5 mm', '(X + Y) ≥ 5 mm' và 'B ≥ 3 mm' "
                  "(ba lần), cũng như '≥ 5 mm' cho mối nối ren; lớp OCR làm "
                  "phẳng các dấu ≥ thành '25'. Ba khối 'Note :' trong hình "
                  "cũng được giữ như bản in."))

    # B10 (raw 19915-19916; continuation of B8).
    b.append(p("đạt được cấp IP cần thiết ở trạng thái ‘khô’ chỉ bằng sự "
               "khít giữa hai phần của mối nối."))
    b.append(note("<b>Lưu ý về ranh giới trang in 462→463 và ‘IP-rating "
                  "‘dry’’.</b> Câu 'These joints may not use ... but must' "
                  "bị tách qua ranh giới trang; phần tiếp nối được giữ "
                  "thành một đoạn riêng như bản in. Bản in dùng dấu nháy "
                  "đơn cong trong '‘dry’' (OCR dùng dấu nháy thẳng) và cách "
                  "viết đó được giữ trong bản tiếng Anh."))

    # B11 (raw 19917-19922).
    b.append(p("Ngoài việc đáp ứng yêu cầu về chiều dài, các mối nối ren phải "
               "có ít nhất ba ren được ăn khít hoàn toàn, dù là ren song song "
               "hay ren côn. Cần nhận dạng các mối nối này nếu chúng dự định "
               "được mở trong điều kiện sử dụng bình thường, xét đến tầm "
               "quan trọng của chúng đối với sự bảo vệ do thiết bị cung "
               "cấp. Thêm vào đó, và đặc biệt, cần nhận dạng thực tế là "
               "không dùng hợp chất nào khi hoàn thiện chúng. Người mua "
               "thiết bị phải biết những vấn đề này để thiết bị được sử "
               "dụng an toàn."))

    # Unnumbered subheading "Joints having gaskets and other types of
    # sealing device" (printed 463).
    b.append(h4("Các mối nối có gioăng và các loại thiết bị bịt kín khác",
                "Joints having gaskets and other types of sealing device"))
    # B13 (raw 19924-19925; continues on printed 464).
    b.append(p("Các mối nối phẳng có thể dùng gioăng phẳng để ngăn bụi xâm "
               "nhập vào vỏ bọc như cho trong Hình 15.2, miễn là chiều rộng "
               "của gioăng ít nhất là"))

    # Fig. 15.2 (printed 464), at the head of the page.
    b.append(fig(2, F.fig_f1502()))
    b.append(note("<b>Lưu ý về chú thích của Hình 15.2 và ‘‘o’ ring’.</b> "
                  "Cụm 'Note: Gaskets must be secured to one face of joint "
                  "and ‘o’ rings in slots (by adhesive or other means which "
                  "does not adversely affect sealing of joint)' được in "
                  "ngay trên cùng dòng với nhan đề hình, không phải chú giải "
                  "riêng. Chữ 'o' là chữ cái thường đặt trong dấu nháy đơn "
                  "cong, không phải số không như lớp OCR đọc. Cả hai được "
                  "giữ nguyên trong nhan đề hình tiếng Anh."))

    # B15 (raw 19937-19945; continuation of B13).
    b.append(p("3 mm. Các mối nối này bao gồm các mối nối mặt bích thường và "
               "các mối nối dạng chốt (spigot), trong đó gioăng nằm ở phần "
               "phẳng và do đó phần chốt lồi không còn quan trọng nữa. Trong "
               "trường hợp này, các gioăng phải thực sự liên tục, nghĩa là "
               "mọi mối nối bên trong chúng cần được dán kết nối với nhau "
               "chứ không chỉ dựa vào áp lực. Gioăng nên được cố định vào "
               "một trong các phần của mối nối, có thể bằng keo dán, để ngăn "
               "sự dịch chuyển của chúng, nhưng vật liệu chế tạo gioăng phải "
               "sao cho chúng không dính ngoài ý muốn vào các bề mặt đối "
               "tiếp. Chúng cũng phải được chế tạo từ vật liệu không bị hư "
               "hỏng bởi các điều kiện sử dụng cực đoan, do lão hóa hoặc do "
               "hoạt động ngoài thông số kỹ thuật của vật liệu."))
    # B16 (raw 19946-19951).
    b.append(p("Có thể dùng các loại bộ phận bịt kín khác, chẳng hạn như vòng "
               "‘o’, và trong trường hợp này không cần cố định vòng vào một "
               "phía của mối nối vì những vòng như vậy cần được lắp trong "
               "các rãnh lõm, và chính điều này thực hiện tác vụ bịt kín cần "
               "thiết. Phớt môi (lip seal) cũng có thể dùng, trong đó sự bịt "
               "kín được thực hiện bằng một vòng định hình ở mép mối nối. "
               "Một lần nữa, các phớt này được tạo hình và định vị chắc chắn "
               "nhờ chính hình dạng của chúng."))

    # Heading 15.4.3 (printed 464).
    b.append(h3("15.4.3 Mối nối bán cố định",
                "15.4.3 Semi-permanent joints"))
    b.append(note("<b>Lưu ý về ‘Semi-permanent’.</b> Lớp OCR đọc "
                  "'15.4.3 Semipermanent joints'; ảnh trang in cho thấy rõ "
                  "'Semi-permanent' (có dấu gạch nối). Bản tiếng Anh giữ "
                  "theo ảnh trang in."))
    # B18 (raw 19953-19955; continues on printed 465).
    b.append(p("Các mối nối là một phần của thiết bị không được tiếp cận "
               "trong sử dụng bình thường và ít khi được mở ra, về nguyên "
               "tắc cần tuân thủ các yêu cầu nêu trên. Tuy nhiên, được phép "
               "nới lỏng trong trường hợp"))
    b.append(note("<b>Lưu ý về ‘in principal’.</b> Bản in viết 'need in "
                  "principal to comply' (không phải 'in principle'). Cụm "
                  "được giữ nguyên trong bản tiếng Anh."))

    # B19 (raw 19958-19963; continuation of B18).
    b.append(p("các mối nối mặt bích và mối nối ren, trong đó đường đi của "
               "bụi qua mối nối được giảm xuống còn 3 mm miễn là bề mặt mối "
               "nối được phủ một hợp chất bịt kín không đông cứng có thông "
               "số kỹ thuật thích hợp trước khi lắp ráp. Những hợp chất "
               "không đông cứng này, khác với trường hợp các mối nối thường "
               "xuyên được mở, có thể được dùng để hỗ trợ loại trừ bụi trong "
               "mọi trường hợp mà mối nối ít khi được mở trong sử dụng và là "
               "mối nối mặt bích, trụ, nón hoặc dạng chốt (spigot) và là mối "
               "nối tĩnh."))
    b.append(note("<b>Lưu ý về ‘cylindrical conical’.</b> Bản in viết 'is "
                  "flanged, cylindrical conical or a spigot joint' (không có "
                  "'or' hay dấu phẩy giữa hai tính từ). Cụm được giữ nguyên "
                  "trong bản tiếng Anh."))
    # B20 (raw 19964-19969).
    b.append(p("Yêu cầu cơ bản đối với những hợp chất không đông cứng này là "
               "chúng phải ổn định về hóa học và nhiệt, và trơ ở nhiệt độ "
               "thấp hơn 5 °C so với nhiệt độ môi trường tối thiểu quy định "
               "cho thiết bị và cao hơn 20 °C so với nhiệt độ tối đa mà "
               "chúng có thể đạt được, với thiết bị được vận hành ở nhiệt độ "
               "môi trường tối đa trong điều kiện nguồn điện và lắp đặt bất "
               "lợi nhất. Chúng cũng cần không bị suy giảm do môi trường "
               "(ví dụ, độ ẩm) hoặc được bảo vệ khỏi tiếp xúc với môi "
               "trường đó."))

    # Heading 15.4.4 (printed 465).
    b.append(h3("15.4.4 Trục và trục quay",
                "15.4.4 Spindles and shafts"))
    # B22 (raw 19971-19976).
    b.append(p("Các trục và trục quay chuyển động hoặc quay nên được bịt kín "
               "để ngăn bụi xâm nhập ở mức không chấp nhận được bằng các bạc "
               "lót phù hợp, việc lắp phớt loại trừ bụi, mối nối mê cung "
               "(labyrinth) hoặc sự kết hợp của các loại thiết bị này. Các "
               "mối nối trụ đơn giản không được coi là phù hợp cho mục đích "
               "này. Ngoài ra, đặc tính loại trừ bụi của các mối nối phải "
               "được duy trì khi không có bất kỳ mỡ hoặc dầu nào được bôi "
               "lên mối nối vì lý do vận hành và mối nối chỉ dựa vào các bộ "
               "phận rắn của nó để hoạt động."))
    # B23 (raw 19977-19979).
    b.append(p("Không quy định chiều dài tối thiểu của đường đi bụi cho các "
               "mối nối này và kích thước của chúng chỉ phụ thuộc vào khả "
               "năng đạt được cấp IP cần thiết."))

    # Heading 15.4.5 (printed 465).
    b.append(h3("15.4.5 Bộ phận truyền sáng",
                "15.4.5 Light-transmitting parts"))
    # B25 (raw 19981-19993).
    b.append(p("Các bộ phận truyền sáng cần được cố định vào vỏ bọc bằng một "
               "trong các kỹ thuật mối nối đã nêu ở trên hoặc được cố định "
               "bằng phương pháp dán xi măng hoặc tương tự. Bất kỳ vật liệu "
               "trong suốt hoặc bán trong suốt nào cũng có thể dùng miễn là "
               "nó đáp ứng các yêu cầu về vật liệu đã nêu, và việc cố định "
               "vào vỏ bọc chỉ bằng keo dán xi măng là được chấp nhận miễn "
               "là keo dính vào cả bộ phận truyền sáng lẫn vỏ bọc. Cụm lắp "
               "ráp bao gồm bộ phận truyền sáng cần đạt được cấp IP cần "
               "thiết và không bị hư hỏng bởi các thử nghiệm va đập đã mô "
               "tả ở trên. Các loại xi măng dùng cho cụm bộ phận truyền sáng "
               "dán xi măng cần đáp ứng các yêu cầu tương tự như đã quy định "
               "đối với hợp chất bịt kín không đông cứng (tất nhiên là ngoại "
               "trừ việc xi măng được yêu cầu phải đông cứng). Nếu bộ phận "
               "truyền sáng bằng kính thì yêu cầu thử nghiệm sốc nhiệt bằng "
               "cách phun tia nước 1 mm ở 10–15 °C lên kính khi kính đang ở "
               "nhiệt độ hoạt động tối đa."))
    b.append(note("<b>Lưu ý về ‘needs to satisfy’, ‘1 mm’ và ‘10–15 °C’.</b> "
                  "Bản in viết 'The cements used ... needs to satisfy' (số "
                  "ít 'needs' với chủ ngữ số nhiều), 'a 1 mm jet of water' "
                  "(có dấu cách sau chữ số 1) và '10–15 °C' (dấu gạch ngang "
                  "và dấu cách trước °C). Tất cả được giữ nguyên trong bản "
                  "tiếng Anh; bản tiếng Việt theo nghĩa đúng."))

    # Heading 15.4.6 (printed 466).
    b.append(h3("15.4.6 Chi tiết bắt vít", "15.4.6 Fasteners"))
    # B27 (raw 19997-20003).
    b.append(p("Các chi tiết bắt vít dùng để cố định các phần của vỏ bọc đóng "
               "một vai trò quan trọng trong khái niệm bảo vệ. Trừ khi có "
               "một thiết bị bổ sung cụ thể để ngăn bụi xâm nhập qua lỗ lắp "
               "hoặc lỗ bắt vít của chúng, các lỗ này không được xuyên vào "
               "bên trong vỏ bọc và độ dày của kim loại hoặc vật liệu vỏ bọc "
               "khác giữa thành và đáy lỗ với bên trong vỏ bọc cần không "
               "nhỏ hơn một phần ba đường kính lỗ, để bảo đảm vỏ bọc đủ bền, "
               "ngăn không bị nứt trong sử dụng."))
    b.append(note("<b>Lưu ý về ‘roll’.</b> Bản in viết 'play an important "
                  "roll in the protection concept' (không phải 'role'). Cụm "
                  "được giữ nguyên trong bản tiếng Anh."))
    # B28 (raw 20004-20006).
    b.append(p("Nắp bản lề được chấp nhận miễn là bản lề không tạo ra áp lực "
               "cần thiết cho việc bịt kín. Vì vậy, trong những trường hợp "
               "như vậy cần có bản lề mềm cho phép nắp dịch chuyển trong lúc "
               "siết các chi tiết bắt. Ngoài ra, vì chuyển động đó có thể "
               "làm nắp bị lệch trong lúc siết, có thể cần các chốt định vị."))

    # Heading 15.5 (printed 466, set on two printed lines).
    b.append(h3("15.5 Yêu cầu bổ sung cụ thể cho các loại thiết bị điện và "
                "kết nối đặc biệt",
                "15.5 Specific additional requirements for particular types "
                "of electrical apparatus and connections"))
    # B30 (raw 20009-20013).
    b.append(p("Như trường hợp các khái niệm bảo vệ khác, có những yêu cầu "
               "cụ thể liên quan đến các kết nối, đầu vào cáp và đối với các "
               "loại thiết bị cụ thể. Những yêu cầu này nhìn chung tương tự "
               "như các yêu cầu đối với các loại thiết bị dùng cho nguy cơ "
               "khí và hơi và thường có thể được mô tả là những yêu cầu áp "
               "dụng cho thiết bị công nghiệp nhưng kèm theo một số quy định "
               "bổ sung."))

    # Heading 15.5.1 (printed 466).
    b.append(h3("15.5.1 Phương tiện kết nối",
                "15.5.1 Connection facilities"))
    # B32 (raw 20015-20024).
    b.append(p("Các yêu cầu đối với kết nối với thiết bị rất tương tự như "
               "các yêu cầu đối với thiết bị dùng cho nguy cơ khí và hơi. "
               "Điều này đòi hỏi phải bố trí các phương tiện kết nối (trừ "
               "thiết bị được chế tạo với cáp nối cố định) sao cho: dễ tiếp "
               "cận và cho phép kẹp chặt hiệu quả cáp đầu vào; nối các dây "
               "dẫn mà không dựa vào bất kỳ bộ phận bằng nhựa nào trong "
               "trường hợp cọc đầu nối và các đầu nối khác dựa vào áp lực để "
               "giữ dây dẫn; có khoảng cách đủ để giảm thiểu nguy cơ đoản "
               "mạch ngoài ý muốn theo mức công nghiệp thông thường; và có "
               "vỏ bọc bảo đảm cấp IP yêu cầu sau khi lắp và nối các dây "
               "dẫn."))
    # B33 (raw 20025-20033; continues on printed 467).
    b.append(p("Yêu cầu nối đất trong hộp cọc đầu nối, gần các kết nối mạch "
               "khác, và khi vỏ bọc hoặc bất kỳ bộ phận có thể tiếp cận nào "
               "của nó dẫn điện, thì cũng yêu cầu nối đất bên ngoài vỏ bọc. "
               "Các phương tiện nối đất bên trong và bên ngoài cần có khả "
               "năng chứa một dây dẫn có kích thước ít nhất bằng kích thước "
               "yêu cầu theo Bảng 15.2, với kích thước tối thiểu của dây dẫn "
               "bên ngoài là 4 mm, không khác nhiều so với yêu cầu cụ thể "
               "đối với thiết bị dùng cho nguy cơ khí và hơi. Không cần "
               "phương tiện nối đất bên ngoài đối với vỏ bọc hoàn toàn cách "
               "điện vì mục đích của nó là liên kết vỏ bọc tại chỗ để loại "
               "bỏ mọi nguy cơ nó có điện thế khác với"))

    # Table 15.2 (printed 467), at the top of the page.
    b.append(table(T.HEAD152_VI, T.ROWS152_VI, T.CAPTION152_VI))
    if T.NOTE152_VI:
        b.append(note(T.NOTE152_VI))
    b.append(note("<b>Lưu ý về các toán tử trong Bảng 15.2.</b> Bản in viết "
                  "'≤16', '>16 but ≤35' và '>35' (không có dấu cách sau toán "
                  "tử) và dùng '(mm²)' ở cả hai tiêu đề cột; lớp OCR đọc sai "
                  "các dấu này. Cách viết theo bản in được giữ trong bản "
                  "tiếng Anh."))

    # B35 (raw 20047-20049; continuation of B33).
    b.append(p("điện thế so với các bộ phận kim loại tại chỗ. Phương tiện "
               "nối đất bên trong cũng có thể bỏ qua khi nó không có mục "
               "đích gì (ví dụ, trong thiết bị cách điện kép) hoặc khi nó "
               "bị cấm cụ thể đối với một loại thiết bị nhất định."))
    b.append(note("<b>Lưu ý về ranh giới trang in 466→467 và ‘4mm’.</b> Câu "
                  "'... risk of it being at a different' bị tách qua ranh "
                  "giới trang; phần tiếp nối được giữ thành một đoạn riêng "
                  "như bản in. Bản in cũng viết 'of 4mm' (không có dấu "
                  "cách) và cách viết đó được giữ trong bản tiếng Anh."))

    # Heading 15.5.2 (printed 467).
    b.append(h3("15.5.2 Đầu vào cáp và ống dẫn",
                "15.5.2 Cable and conduit entries"))
    # B37 (raw 20051-20054).
    b.append(p("Khi cáp hoặc ống dẫn đi vào vỏ bọc, phương pháp vào phải bảo "
               "đảm duy trì được tính toàn vẹn của vỏ bọc. Điều này có thể "
               "bao gồm việc lắp vòng đệm tại điểm vào và bịt kín các khe hở "
               "của cáp, đặc biệt khi dùng cáp được bọc băng (tape bedded "
               "cable)."))
    # B38 (raw 20055-20057).
    b.append(p("Ống dẫn gần như chắc chắn sẽ cần lắp hộp chặn (stopper box) "
               "gần điểm vào, nếu không ống dẫn sẽ phải được coi là một phần "
               "của vỏ bọc."))
    # B39 (raw 20058-20064).
    b.append(p("Đầu nối cáp (cable gland) phải kẹp chặt vỏ bọc hoặc lớp giáp "
               "của cáp để cố định cáp và ngăn ứng suất tác dụng lên các "
               "kết nối điện. Các yêu cầu ở đây giống hệt với yêu cầu đối "
               "với đầu vào cáp của thiết bị dùng cho nguy cơ khí và hơi "
               "(xem Chương 8), yêu cầu thử nghiệm trên cáp đã kẹp, bao gồm "
               "việc áp dụng một ứng suất kéo cụ thể với các giá trị cụ thể "
               "trong những thời gian cụ thể cho cáp đã kẹp mà không có sự "
               "dịch chuyển đáng kể của cáp. Chi tiết về các thử nghiệm này "
               "được cho trong BS/EN 50014⁹."))
    b.append(note("<b>Lưu ý về ‘BS/EN 50014⁹’.</b> Bản in có chỉ số trên ⁹ "
                  "sau '50014'; lớp OCR viết '500149'. Chỉ số trên được giữ "
                  "nguyên trong bản tiếng Anh."))

    # Heading 15.5.3 (printed 467).
    b.append(h3("15.5.3 Cầu chảy và thiết bị đóng cắt",
                "15.5.3 Fuses and switchgear"))
    # B41 (raw 20066-20070; continues on printed 468, outside this span).
    b.append(p("Vỏ bọc của cầu chảy và của thiết bị đóng cắt điều khiển từ "
               "xa, bao gồm cả thiết bị có tiếp điểm đóng cắt, nên được liên "
               "khóa để ngăn mở vỏ bọc khi thiết bị đang có điện và, trong "
               "cả hai trường hợp, liên khóa phải được định mức cho hoạt "
               "động có tải (on-load rated). Nếu không bổ sung liên khóa, "
               "vỏ bọc cần được dán nhãn cảnh báo không được mở trong khu "
               "vực nguy hiểm khi cầu chảy hoặc thiết bị đóng cắt bên trong "
               "đang có điện. Thuật ngữ ‘điều khiển từ"))
    b.append(note("<b>Lưu ý về điểm kết thúc của mô-đun này.</b> Đoạn cuối "
                  "kết thúc ở trang in 467 tại cụm chưa trọn 'The term "
                  "‘remotely' với dấu nháy mở chưa đóng. Phần tiếp nối "
                  "'operated’ is used in relation to switchgear ...' nằm ở "
                  "trang in 468 và thuộc về mô-đun tiếp theo."))

    return "".join(b)


def body_en():
    b = []

    # B1 (raw 19855-19863; continuation of a paragraph from printed 461).
    b.append(p("requirements to prevent such ignition. If it did occur there "
               "is a real danger that the elevated temperature may damage the "
               "enclosure integrity leading to ignition of any surrounding "
               "dust cloud or layer and thus the requirement assumes a "
               "greater importance in this context. Methods of demonstrating "
               "non-combustibility and prevention of flame transmission are "
               "not specifically defined in relation to this particular risk "
               "and typical industrial methods of demonstration are "
               "acceptable (e.g., BS 2782, BS 6458 and BS 6334 are typical "
               "Standards which may be used for this purpose but they are "
               "not exclusive and other recognized methods may be used)."))
    b.append(note("<b>Note on the opening paragraph.</b> B1 continues a "
                  "paragraph begun on printed p. 461, which lies outside "
                  "this module's span. It is kept incomplete at the start as "
                  "printed."))

    # Unnumbered subheading "Mechanical strength" (printed 462).
    b.append(h4("Mechanical strength", "Mechanical strength"))
    # B3 (raw 19865-19871).
    b.append(p("The mechanical strength of the enclosure is required to be "
               "such that it will not be damaged other than superficially by "
               "impact and drop tests. These tests are identical to those "
               "used for apparatus for gas and vapour risks (see Chapter 8) "
               "except that, because the enclosure is all important, the "
               "lower level of impact test for enclosures intended for "
               "installation only in areas where the risk of mechanical "
               "impact is low is not acceptable, the higher figure always "
               "being required."))

    # Heading 15.4.2 (printed 462).
    b.append(h3("15.4.2 Joints intended to be opened in normal service",
                "15.4.2 Joints intended to be opened in normal service"))
    b.append(note("<b>Note on ‘normal service’.</b> The OCR layer reads the "
                  "heading as '15.4.2 Joints intended to be opened in normal "
                  "setvice'; the page render clearly shows 'normal service'. "
                  "The English text keeps the render reading."))

    # Unnumbered subheading "Non-gasketted joints" (printed 462).
    b.append(h4("Non-gasketted joints", "Non-gasketted joints"))
    # B6 (raw 19874-19883).
    b.append(p("Metal/metal and similar joints in enclosures which do not "
               "use compressible gaskets may be used provided that the "
               "enclosure may be shown to achieve the desired IP-rating. "
               "Such joints have minimum requirements applied to them to "
               "ensure that they are repeatable and these are that the joint "
               "be close fitting and have a minimum width over which this is "
               "achieved, defined as the dust ingress path. No figure is "
               "given for close fitting but it is recommended that a maximum "
               "separation limit of 0.5mm be applied with the proviso that "
               "the enclosure has to satisfy the necessary IP-rating. This "
               "would allow the use of all flameproof enclosures which "
               "satisfied the necessary IP test. A minimum joint flatness "
               "requirement of at least 6.3μm be applied for the same reason. "
               "Typical joints are shown in Fig. 15.1."))
    b.append(note("<b>Note on ‘0.5mm’, ‘6.3μm’ and ‘necessary IP-rating’.</b> "
                  "The print reads 'a maximum separation limit of 0.5mm' "
                  "(no space), 'at least 6.3μm' (Greek mu, no space; the OCR "
                  "layer dropped the unit) and 'the necessary IP-rating' "
                  "(OCR: 'necessary E'-rating'). All three are kept as "
                  "printed; the Vietnamese follows the intended meaning."))

    # B7 (raw 19884-19890): intro plus the five-item list as printed.
    b.append(p("The minimum dust ingress paths (widths) for such joints need "
               "to be as follows:"))
    b.append(ul([
        "Flat flanged joints – 5mm",
        "Spigot joints – 3mm",
        "Cylindrical joints – 3mm",
        "Conical joints – 3mm",
        "Threaded joints – 5mm",
    ]))
    b.append(note("<b>Note on the five-item list.</b> The print lists five "
                  "items with an en dash separator and no space before the "
                  "value: 'Flat flanged joints – 5mm', 'Spigot joints – 3mm', "
                  "'Cylindrical joints – 3mm', 'Conical joints – 3mm', "
                  "'Threaded joints – 5mm'. The dashes and spacing are kept "
                  "as printed."))

    # B8 (raw 19891-19892; continues on printed 463).
    b.append(p("These joints may not use additional measures such as "
               "non-setting sealing compounds to assist in the achievement "
               "of the necessary IP-rating but must"))

    # Fig. 15.1 (printed 463), at the head of the page.
    b.append(fig(1, F.fig_f1501()))
    b.append(note("<b>Note on the Figure 15.1 dimensions.</b> The page render "
                  "clearly shows 'A ≥ 5 mm', '(X + Y) ≥ 5 mm' and 'B ≥ 3 mm' "
                  "(three times), as well as '≥ 5 mm' for the threaded joint; "
                  "the OCR layer flattened the ≥ signs to '25'. The three "
                  "'Note :' blocks in the figure are also kept as printed."))

    # B10 (raw 19915-19916; continuation of B8).
    b.append(p("achieve the necessary IP-rating ‘dry’ on the basis of the fit "
               "of the two parts of the joint alone."))
    b.append(note("<b>Note on the printed-page break 462→463 and ‘IP-rating "
                  "‘dry’’.</b> The sentence 'These joints may not use ... but "
                  "must' is split across the page break; its continuation "
                  "is kept as a separate paragraph as printed. The print "
                  "uses curly single quotes in '‘dry’' (the OCR used straight "
                  "quotes), and that spelling is kept in the English text."))

    # B11 (raw 19917-19922).
    b.append(p("Threaded joints, in addition to satisfying the length "
               "requirements, must have at least three threads fully "
               "engaged, whether parallel or taper threads. It is necessary "
               "to identify these joints if they are intended to be opened "
               "in normal service in view of their importance to the "
               "protection offered by the apparatus. Additionally and "
               "particularly it is necessary to identify the fact that no "
               "compound is used in their completion. The purchaser of the "
               "apparatus must be aware of these matters if the apparatus is "
               "to be used safely."))

    # Unnumbered subheading "Joints having gaskets and other types of
    # sealing device" (printed 463).
    b.append(h4("Joints having gaskets and other types of sealing device",
                "Joints having gaskets and other types of sealing device"))
    # B13 (raw 19924-19925; continues on printed 464).
    b.append(p("Plane joints may use flat gaskets to prevent the ingress of "
               "dust into enclosures as shown in Fig. 15.2, provided that the "
               "gasket width is at least"))

    # Fig. 15.2 (printed 464), at the head of the page.
    b.append(fig(2, F.fig_f1502()))
    b.append(note("<b>Note on the Figure 15.2 caption Note and ‘‘o’ ring’.</b> "
                  "The words 'Note: Gaskets must be secured to one face of "
                  "joint and ‘o’ rings in slots (by adhesive or other means "
                  "which does not adversely affect sealing of joint)' are "
                  "printed on the same line as the figure caption, not as a "
                  "separate footnote. The letter 'o' is a lowercase letter "
                  "inside curly single quotes, not the digit zero read by "
                  "the OCR layer. Both are kept as printed in the English "
                  "caption."))

    # B15 (raw 19937-19945; continuation of B13).
    b.append(p("3mm. These joints include plain flanged joints and spigot "
               "joints where the gasket is in the plane part and thus the "
               "spigot ceases to be important. In this case the gaskets must "
               "be effectively continuous in that any joints within them "
               "need to be bonded together and not just rely on pressure. "
               "The gaskets should be fixed to one of the joint parts, "
               "possibly with adhesive, to prevent their displacement but "
               "their material of construction should be such that they do "
               "not stick inadvertently to mating faces. They must also be "
               "fabricated of a material which is not damaged by the "
               "extremities of their service conditions either by ageing or "
               "operation outside their material specification."))
    # B16 (raw 19946-19951).
    b.append(p("Other types of sealing unit, such as ‘o’ rings, may also be "
               "used and in this case securing of the ring to one side of the "
               "joint will not be necessary as such rings need to be fitted "
               "in recesses which effectively perform the necessary action. "
               "Lip seals are also possible where the seal is by a shaped "
               "ring at the edge of the joint. Again, these seals are "
               "profiled and positively located by their form."))

    # Heading 15.4.3 (printed 464).
    b.append(h3("15.4.3 Semi-permanent joints",
                "15.4.3 Semi-permanent joints"))
    b.append(note("<b>Note on ‘Semi-permanent’.</b> The OCR layer reads "
                  "'15.4.3 Semipermanent joints'; the page render clearly "
                  "shows 'Semi-permanent' (with the hyphen). The English "
                  "text follows the render."))
    # B18 (raw 19953-19955; continues on printed 465).
    b.append(p("Joints which form part of an apparatus which is not addressed "
               "in normal service and which are seldom opened, need in "
               "principal to comply with the foregoing requirements. A "
               "relaxation is, however, permitted in the case of"))
    b.append(note("<b>Note on ‘in principal’.</b> The print reads 'need in "
                  "principal to comply' (not 'in principle'). The phrase is "
                  "kept as printed."))

    # B19 (raw 19958-19963; continuation of B18).
    b.append(p("flanged joints and threaded joints, whereby the dust path "
               "through the joint is reduced to 3mm provided the joint "
               "surfaces are coated with a non-setting sealing compound of "
               "adequate specification before assembly. Such non-setting "
               "compounds may, unlike the situation in the case of regularly "
               "opened joints, be used to assist exclusion of dust in all "
               "cases where the joint is seldom opened in service and is "
               "flanged, cylindrical conical or a spigot joint and is "
               "static."))
    b.append(note("<b>Note on ‘cylindrical conical’.</b> The print reads 'is "
                  "flanged, cylindrical conical or a spigot joint' (with no "
                  "'or' or comma between the two adjectives). The phrase is "
                  "kept as printed."))
    # B20 (raw 19964-19969).
    b.append(p("The basic requirements for such non-setting compounds is that "
               "they be chemically and thermally stable, and inert between a "
               "temperature 5 °C below the minimum ambient temperature "
               "specified for the apparatus and 20 °C above the maximum "
               "temperature which they can reach, with the apparatus "
               "operated at the maximum ambient temperature in the most "
               "adverse supply and mounting conditions. They also need to be "
               "impervious to deterioration as a result of the environment "
               "(e.g., moisture) or be protected from contact with it."))

    # Heading 15.4.4 (printed 465).
    b.append(h3("15.4.4 Spindles and shafts",
                "15.4.4 Spindles and shafts"))
    # B22 (raw 19971-19976).
    b.append(p("Spindles and shafts which move or rotate should be sealed "
               "against the unacceptable entry of dust by suitable bushings, "
               "the fitting of a dust exclusion seal, a labyrinth joint or a "
               "combination of these types of device. Simple cylindrical "
               "joints are not considered as suitable for this use. In "
               "addition, the dust exclusion properties of the joints must "
               "be maintained when any grease or oil applied to the joint for "
               "operational reasons is absent and the joint relies only on "
               "its solid parts for its performance."))
    # B23 (raw 19977-19979).
    b.append(p("No minimum lengths of dust path are specified for such joints "
               "and their dimensions are solely affected by their ability to "
               "achieve the necessary IP-rating."))

    # Heading 15.4.5 (printed 465).
    b.append(h3("15.4.5 Light-transmitting parts",
                "15.4.5 Light-transmitting parts"))
    # B25 (raw 19981-19993).
    b.append(p("Light-transmitting parts need to be fixed to the enclosure by "
               "one of the joint techniques already mentioned or be fixed by "
               "cementing or similar methods. Any transparent or translucent "
               "material may be used provided it complies with the materials "
               "requirements already stated, and securing to the enclosure "
               "by cement alone is acceptable provided that the cement "
               "adheres to both the light-transmitting part and the "
               "enclosure. The assembly including the light-transmitting "
               "part needs to achieve the necessary IP-rating and must not "
               "be damaged by the impact tests already described. The cements "
               "used for cemented light-transmitting part assemblies needs "
               "to satisfy the same requirements as those for non-setting "
               "sealing compounds already specified (except of course that "
               "the cement is required to set). If the light-transmitting "
               "part is glass then a thermal shock test of spraying a 1 mm "
               "jet of water at 10–15 °C onto the glass when it is at its "
               "maximum operating temperature is required."))
    b.append(note("<b>Note on ‘needs to satisfy’, ‘1 mm’ and ‘10–15 °C’.</b> "
                  "The print reads 'The cements used ... needs to satisfy' "
                  "(singular 'needs' with a plural subject), 'a 1 mm jet of "
                  "water' (a space after the digit 1) and '10–15 °C' (an en "
                  "dash and a space before °C). All are kept as printed; the "
                  "Vietnamese follows the intended meaning."))

    # Heading 15.4.6 (printed 466).
    b.append(h3("15.4.6 Fasteners", "15.4.6 Fasteners"))
    # B27 (raw 19997-20003).
    b.append(p("The fasteners used to secure parts of the enclosure play an "
               "important roll in the protection concept. Unless there is a "
               "specific additional device to prevent the ingress of dust "
               "via their mounting or fixing holes, these should not enter "
               "the enclosure and the thickness of metal or other enclosure "
               "material between their sides and bottom and the inside of "
               "the enclosure needs to be not less than one third of the "
               "hole diameter to ensure the enclosure is strong enough to "
               "prevent cracking in service."))
    b.append(note("<b>Note on ‘roll’.</b> The print reads 'play an important "
                  "roll in the protection concept' (not 'role'). The phrase "
                  "is kept as printed."))
    # B28 (raw 20004-20006).
    b.append(p("Hinged lids are acceptable provided that the hinge does not "
               "apply the pressure necessary for sealing. A flexible hinge "
               "which allows lid movement during tightening of fixings is "
               "therefore necessary in such cases. Also, because such "
               "movement may allow the displacement of the lid during "
               "tightening, locating pins may be necessary."))

    # Heading 15.5 (printed 466, set on two printed lines).
    b.append(h3("15.5 Specific additional requirements for particular types "
                "of electrical apparatus and connections",
                "15.5 Specific additional requirements for particular types "
                "of electrical apparatus and connections"))
    # B30 (raw 20009-20013).
    b.append(p("As is the case with other protection concepts there are "
               "specific requirements concerning connections, cable entry "
               "and for specific types of apparatus. These are generally "
               "similar to those required for types of apparatus used in gas "
               "and vapour risks and may generally be described as those "
               "applied to industrial apparatus but with a few additional "
               "specifications."))

    # Heading 15.5.1 (printed 466).
    b.append(h3("15.5.1 Connection facilities",
                "15.5.1 Connection facilities"))
    # B32 (raw 20015-20024).
    b.append(p("The requirements for connections to apparatus are very "
               "similar to those required for apparatus for gas and vapour "
               "risks. This requires the provision of connection facilities "
               "(except for apparatus manufactured with a permanently "
               "connected cable) which are: accessible and allow effective "
               "clamping of incoming cable, connection of conductors without "
               "relying on any plastic part in the case of terminals and "
               "other connectors which rely on pressure to hold the "
               "conductor; have sufficient separation so as to minimize the "
               "risk of inadvertent short circuits to the normal industrial "
               "degree; and have enclosures which ensure the required "
               "IP-rating after fitting and connection of the conductors."))
    # B33 (raw 20025-20033; continues on printed 467).
    b.append(p("Earth connections are required within the terminal enclosure "
               "close to the other circuit connections and, where the "
               "enclosure or any accessible part of it is conducting, outside "
               "the enclosure also. The internal and external earth "
               "connection facilities need to be able to accommodate a "
               "conductor of at least the size required by Table 15.2, with a "
               "minimum size for the external conductor of 4mm which is not "
               "dissimilar to the specific requirement for apparatus for gas "
               "and vapour risks. No external earth connection facility is "
               "necessary for an enclosure which is wholly insulating as the "
               "objective of this is to bond the enclosure locally to remove "
               "any risk of it being at a different"))

    # Table 15.2 (printed 467), at the top of the page.
    b.append(table(T.HEAD152_EN, T.ROWS152, T.CAPTION152_EN))
    if T.NOTE152_EN:
        b.append(note(T.NOTE152_EN))
    b.append(note("<b>Note on the Table 15.2 operators.</b> The print reads "
                  "'≤16', '>16 but ≤35' and '>35' (with no space after the "
                  "operator) and uses '(mm²)' in both column headers; the "
                  "OCR layer misread these signs. The printed spelling is "
                  "kept in the English text."))

    # B35 (raw 20047-20049; continuation of B33).
    b.append(p("potential to the local metalwork. The internal earth "
               "connection facility may also be omitted where it has no "
               "purpose (e.g., in double insulated apparatus) or where it is "
               "specifically not permitted for a particular type of "
               "apparatus."))
    b.append(note("<b>Note on the printed-page break 466→467 and ‘4mm’.</b> "
                  "The sentence '... risk of it being at a different' is "
                  "split across the page break; its continuation is kept as "
                  "a separate paragraph as printed. The print also reads "
                  "'of 4mm' (with no space), and that spelling is kept in the "
                  "English text."))

    # Heading 15.5.2 (printed 467).
    b.append(h3("15.5.2 Cable and conduit entries",
                "15.5.2 Cable and conduit entries"))
    # B37 (raw 20051-20054).
    b.append(p("Where cables or conduits enter the enclosure, the method of "
               "entry must be such as to ensure that the enclosure integrity "
               "is maintained. This may involve the fitting of washers at the "
               "entry point and sealing of the interstices of the cable, "
               "particularly where tape bedded cable is used."))
    # B38 (raw 20055-20057).
    b.append(p("Conduits will almost certainly require to have a stopper box "
               "fitted close to the point of entry as otherwise the conduit "
               "will need to be considered as part of the enclosure."))
    # B39 (raw 20058-20064).
    b.append(p("Cable glands need to clamp the cable sheath or armour to "
               "secure the cable and prevent stress on the electrical "
               "connections. The requirements here are identical to those "
               "for cable entries for apparatus for gas and vapour risks "
               "(see Chapter 8), requiring a test on the clamped cable "
               "constituting application of a specific tensile stress of "
               "specific values for specific times to the clamped cable "
               "without any significant movement of the cable. Details for "
               "these tests are given in BS/EN 50014⁹."))
    b.append(note("<b>Note on ‘BS/EN 50014⁹’.</b> The print carries a "
                  "superscript ⁹ after '50014'; the OCR layer wrote "
                  "'500149'. The superscript is kept in the English text."))

    # Heading 15.5.3 (printed 467).
    b.append(h3("15.5.3 Fuses and switchgear",
                "15.5.3 Fuses and switchgear"))
    # B41 (raw 20066-20070; continues on printed 468, outside this span).
    b.append(p("Enclosures of fuses and remotely operated switchgear, "
               "including apparatus with switching contacts, should be "
               "interlocked to prevent the enclosure being opened while the "
               "apparatus is energized and, in both cases, the interlock "
               "needs to be on-load rated. If interlocking is not provided, "
               "the enclosure needs to be fitted with a label warning against "
               "opening in a hazardous area while the fuses or switchgear "
               "enclosed are energized. The term ‘remotely"))
    b.append(note("<b>Note on the end of this module's span.</b> The last "
                  "paragraph ends on printed p. 467 with the incomplete "
                  "phrase 'The term ‘remotely' and an unclosed curly opening "
                  "quote. Its continuation, 'operated’ is used in relation "
                  "to switchgear ...', lies on printed p. 468 and belongs to "
                  "the next module."))

    return "".join(b)
