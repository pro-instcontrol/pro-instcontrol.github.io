# -*- coding: utf-8 -*-
"""Chapter 8, module A - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 178-182 (PDF pp. 199-203).

Covers the unfoliated chapter opener "Apparatus to European Standards"
(the shall / should / must distinction, general versus protection-concept
Standards, the several issues of BS/EN 50014 and their amendments), the
opening of 8.1 with its eight basic matters, 8.1.1 Definitions, and the
opening of 8.1.2 with Group I / Group II and the intrinsic-safety
sub-groups IIA, IIB and IIC. The flameproof grouping and Fig. 8.1 belong
to the next module. Prose only: no figures, tables, equations or reference
list. The chapter shell owns the chapter h2, references and end matter.
Wording, standards designations, footnote markers and printed quirks
follow the verified survey brief and the page renders, not the garbled
PDF text layer.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h2, h3, h4, p, note, table, fig


def body_vi():
    b = []
    b.append(h3("Thiết bị theo Tiêu chuẩn Châu Âu",
                "Apparatus to European Standards"))

    b.append(p("Trước khi đi vào xem xét chi tiết Tiêu chuẩn về các yêu cầu "
               "chung¹, cần hiểu rõ cách dùng từ trong Tiêu chuẩn này và các "
               "Tiêu chuẩn khác. Trước hết, Tiêu chuẩn không có hiệu lực bắt "
               "buộc như pháp luật và không thể quy định điều gì phải hoặc "
               "không phải làm để tuân thủ pháp luật ở bất kỳ quốc gia nào."))
    b.append(p("Những từ quan trọng trong Tiêu chuẩn này và các Tiêu chuẩn "
               "khác, thứ nhất là <i>shall</i>, việc dùng từ này cho thấy một "
               "yêu cầu là điều bắt buộc theo như Tiêu chuẩn. Nếu không tuân "
               "thủ điều đó thì không thể tuyên bố là đã tuân thủ Tiêu chuẩn."))
    b.append(p("Thứ hai là việc dùng từ <i>should</i>, cho thấy một khuyến "
               "nghị mạnh mẽ nhưng vẫn cho phép một số linh hoạt trong việc "
               "áp dụng Tiêu chuẩn. Nói cách khác, đôi khi có thể chấp nhận "
               "một cách tiếp cận thay thế cho kết quả thực chất như nhau. Ở "
               "đây trọng tâm nằm ở từ <i>occasional</i>, vì sự nới lỏng này "
               "không nhằm mục đích 'cho một cỗ xe ngựa chạy qua' Tiêu chuẩn. "
               "Cần lưu ý rằng dù sao thì từ <i>should</i> cũng chỉ được dùng "
               "ở một số ít trường hợp."))
    b.append(p("Từ <i>must</i> ít khi được dùng trong các Tiêu chuẩn nhưng khi "
               "nó xuất hiện thì có nghĩa là đã có một đạo luật tồn tại vào "
               "thời điểm Tiêu chuẩn được biên soạn, và việc dùng mệnh lệnh "
               "thức là phù hợp. Trong trường hợp này, Tiêu chuẩn không phải "
               "là đang đặt ra pháp luật mà chỉ là thu hút sự chú ý đến sự tồn "
               "tại của pháp luật."))
    b.append(p("Chương 7 xác định các Tiêu chuẩn Châu Âu hiện có cho các loại "
               "thiết bị điện được bảo vệ chống nổ khác nhau. Chương đó lưu ý "
               "rằng, khác với các Tiêu chuẩn Quốc gia trước đây ở Anh vốn "
               "chứa toàn bộ yêu cầu trong Tiêu chuẩn dành cho từng loại hình "
               "bảo vệ cụ thể, các Tiêu chuẩn Châu Âu chỉ chứa những yêu cầu "
               "riêng cho loại hình bảo vệ cụ thể đó, trong khi các yêu cầu "
               "mang tính tổng quát hơn (tức là những yêu cầu áp dụng cho một "
               "số loại hình bảo vệ) được chứa trong một Tiêu chuẩn về các yêu "
               "cầu chung¹ mà các Tiêu chuẩn dành cho từng loại hình bảo vệ "
               "viện dẫn đến. Khi đó, các yêu cầu của Tiêu chuẩn này được coi "
               "là áp dụng cho tất cả các Tiêu chuẩn dành cho từng loại hình "
               "bảo vệ cụ thể, trừ khi một Tiêu chuẩn cụ thể loại trừ riêng "
               "một hoặc nhiều yêu cầu chung nói trên. Cách tiếp cận này được "
               "xem là giúp giảm thiểu sự trùng lặp công sức của các ủy ban "
               "soạn thảo Tiêu chuẩn và đưa ra cách tiếp cận hợp lý hơn. Trên "
               "thực tế, cách tiếp cận này đã cho thấy những nhược điểm đáng "
               "kể, vì bất kỳ thay đổi nào đối với Tiêu chuẩn yêu cầu chung "
               "cũng tự động ảnh hưởng đến các Tiêu chuẩn dành cho từng loại "
               "hình bảo vệ cụ thể, vốn được soạn thảo bởi các ủy ban Châu Âu "
               "khác nhau, gồm những nhóm người khác với những người tham gia "
               "soạn thảo Tiêu chuẩn yêu cầu chung. Để khắc phục điều này, các "
               "Tiêu chuẩn dành cho từng loại hình bảo vệ cụ thể quy định một "
               "lần xuất bản cụ thể của Tiêu chuẩn yêu cầu chung, nhưng điều "
               "đó có nghĩa là, vì các Tiêu chuẩn dành cho từng loại hình bảo "
               "vệ cụ thể được soạn thảo trong những khung thời gian khác "
               "nhau, nên cần có hơn một lần xuất bản của Tiêu chuẩn yêu cầu "
               "chung có hiệu lực tại cùng một thời điểm. Trừ khi hết sức "
               "cẩn trọng, sự nhầm lẫn có thể phát sinh. Dù tình hình chưa "
               "thật sự hoàn hảo, rất khó có thể thay đổi và bất cứ khi nào "
               "đề cập đến một loại hình bảo vệ cụ thể, cần đảm bảo rằng nó "
               "được đề cập đến cùng với lần xuất bản phù hợp của Tiêu chuẩn "
               "yêu cầu chung."))
    b.append(p("Lần xuất bản mới nhất của Tiêu chuẩn yêu cầu chung là BS/EN "
               "50014 (ấn bản thứ hai) (1993)¹, áp dụng cho tất cả các loại "
               "hình bảo vệ ngoại trừ Ex m (BS 5501, Phần 8 (1988) – EN 50028 "
               "(1987) hiện nay. Tiền nhiệm của nó áp dụng cho Ex m là BS 5501, "
               "Phần 1 (1977) – EN 50014 (1977), ấn bản thứ nhất. Một sự phức "
               "tạp khác là cả hai Tiêu chuẩn này đều đã được sửa đổi sau khi "
               "xuất bản (bảy lần đối với BS 5501 phần 1 (1977) và một lần đối "
               "với BS/EN 50014 (1993)¹). Nói chung, các sửa đổi được coi là "
               "một phần của tiêu chuẩn và do đó sẽ áp dụng cho tất cả các "
               "Tiêu chuẩn dành cho từng loại hình bảo vệ kể từ ngày sửa đổi "
               "được ban hành, trừ khi chính các Tiêu chuẩn sau đó được sửa "
               "đổi để loại trừ sửa đổi đối với Tiêu chuẩn yêu cầu chung. Vì "
               "vậy, để đơn giản hóa tình hình, ấn bản thứ hai của Tiêu chuẩn "
               "(BS/EN 50014 (1993)¹, bao gồm sửa đổi 1) sẽ là cơ sở cho nội "
               "dung của chương này, và những khác biệt giữa nó với ấn bản "
               "thứ nhất (BS 5501, phần 1 (1977), bao gồm các sửa đổi 1 đến 7) "
               "sẽ được làm rõ để bao phủ tình hình cho đến khi Chỉ thị "
               "76/117/EEC được sửa đổi, như đã thảo luận trước đó."))
    b.append(note("<b>Lưu ý về 'Ex m' và 'Exm'.</b> Ảnh các trang in cho thấy "
                  "'Ex m' có dấu cách ở cả hai vị trí trong đoạn này ('with "
                  "the exception of Ex m' và 'applies to Ex m'); lớp văn bản "
                  "trích xuất lại ghi lần đầu là 'Exm'. Bản dịch giữ nguyên "
                  "dạng in có dấu cách ở cả hai nơi và ghi nhận biến thể vì "
                  "cả hai cách viết đều xuất hiện trong nguồn."))

    b.append(h3("8.1 BS/EN 50014 (1993) (bao gồm sửa đổi 1 (1994))",
                "8.1 BS/EN 50014 (1993) (including amendment 1 (1994))"))
    b.append(p("Tốt hơn hết là giải quyết sửa đổi đối với Tiêu chuẩn này "
               "trước để tránh bất kỳ sự nhầm lẫn nào. Có thể thấy việc phải "
               "sửa đổi một Tiêu chuẩn ngay sau khi xuất bản là đáng lo ngại, "
               "nhưng sửa đổi chỉ được ban hành cho bản văn tiếng Anh của "
               "Tiêu chuẩn, vì bản này đã bỏ sót đoạn giới hạn hiệu lực của "
               "Tiêu chuẩn chỉ áp dụng cho các ấn bản thứ hai của các Tiêu "
               "chuẩn dành cho từng loại hình bảo vệ. (Tất cả các Tiêu chuẩn "
               "Châu Âu được viết bằng ba ngôn ngữ, tiếng Anh, tiếng Pháp và "
               "tiếng Đức, và trong trường hợp này bản văn tiếng Anh đã bỏ sót "
               "một đoạn hiện có trong bản tiếng Pháp và tiếng Đức). Đáng lưu "
               "ý ở đây là các Tiêu chuẩn EN có thể xuất hiện bằng các ngôn "
               "ngữ khác, nhưng đó là các bản dịch quốc gia, và trong bất kỳ "
               "tranh chấp nào về ý nghĩa của các Tiêu chuẩn, phải viện dẫn "
               "các bản văn tiếng Anh, tiếng Pháp và tiếng Đức để làm rõ."))
    b.append(p("BS/EN 50014 (1993)¹ đề cập đến những vấn đề chung cho hơn một "
               "loại hình bảo vệ. Một số nội dung của nó có thể không phù hợp "
               "với một Tiêu chuẩn dành cho loại hình bảo vệ cụ thể nào đó, "
               "và trong trường hợp đó, Tiêu chuẩn cụ thể sẽ xác định — trong "
               "phạm vi áp dụng nếu loại trừ là toàn bộ, hoặc trong văn bản "
               "chi tiết nếu loại trừ chỉ là một phần — những phần của "
               "BS/EN 50014 (1993)¹ không áp dụng."))
    b.append(p("Những vấn đề cơ bản được đề cập trong BS/EN 50014 (1993)¹ và "
               "người tiền nhiệm của nó là BS 5501, phần 1 (1977) như sau:"))
    b.append(p("1. Định nghĩa các thuật ngữ dùng trong BS/EN 50014 (1993)¹ và "
               "các Tiêu chuẩn dành cho từng loại hình bảo vệ bổ trợ của nó."))
    b.append(p("2. Phương pháp phân chia thiết bị thành các nhóm và các cấp "
               "nhiệt độ để sử dụng."))
    b.append(p("3. Yêu cầu đối với vỏ bọc."))
    b.append(p("4. Yêu cầu đối với chốt vít dùng để cố định vỏ bọc, cơ cấu "
               "liên khóa dùng để ngăn không cho bỏ qua bảo vệ, các ống lót "
               "dùng cho kết nối, và các chất xi măng có thể dùng trong cấu "
               "tạo vỏ bọc."))
    b.append(p("5. Yêu cầu đối với việc kết nối dẫn điện vào thiết bị và việc "
               "đưa cáp vào thiết bị."))
    b.append(p("6. Yêu cầu bổ sung áp dụng cho các loại thiết bị cụ thể như "
               "máy quay, đèn chiếu sáng, cầu chì, v.v."))
    b.append(p("7. Yêu cầu đối với các linh kiện Ex, là những linh kiện cấu "
               "thành một phần của thiết bị nhưng có thể được dùng trong "
               "nhiều loại thiết bị, và được kiểm tra sự phù hợp với các phần "
               "thích hợp của tiêu chuẩn riêng để tránh đánh giá lặp lại."))
    b.append(p("8. Yêu cầu về đấu ghi nhận thiết bị đạt yêu cầu nhằm đảm bảo "
               "thông tin thích hợp được cung cấp cho người mua."))
    b.append(p("Đáng lưu ý là BS/EN 50014 (1993)¹ thu hút sự chú ý đến việc "
               "những người chế tạo thiết bị cũng cần đảm bảo đáp ứng các "
               "yêu cầu an toàn điện cơ bản, và được coi là bảo đảm điều đó "
               "bằng cách áp dụng việc đấu ghi nhận theo yêu cầu của Tiêu "
               "chuẩn. (BS 5501, phần 1 (1977) yêu cầu một hình thức khai báo "
               "cụ thể cho mục đích này.)"))

    b.append(h4("8.1.1 Định nghĩa", "8.1.1 Definitions"))
    b.append(p("Có khoảng 25 định nghĩa trong Tiêu chuẩn, một số đề cập đến "
               "các thuật ngữ như thiết bị và một số đề cập đến ý nghĩa của "
               "một vài ký hiệu dùng trong Tiêu chuẩn và các Tiêu chuẩn dành "
               "cho từng loại hình bảo vệ bổ trợ của nó. Cũng như các chương "
               "trước, chúng sẽ được trình bày chi tiết ở cuối sách này. Dù "
               "nhìn chung các định nghĩa này bao phủ toàn bộ nhóm Tiêu "
               "chuẩn, chúng chưa đầy đủ mà cần được bổ sung bằng các định "
               "nghĩa thêm trong các Tiêu chuẩn dành cho từng loại hình bảo "
               "vệ (cho thấy những vấn đề liên quan đến việc giới hạn ý nghĩa "
               "của thuật ngữ bằng định nghĩa)."))

    b.append(h4("8.1.2 Phân chia thiết bị thành các phân nhóm và các cấp "
                "nhiệt độ bề mặt",
                "8.1.2 Division of apparatus into sub-groups and surface "
                "temperature classes"))
    b.append(p("Như đã nêu trước đó, thiết bị điện được phân thành các nhóm "
               "và các cấp theo khả năng gây bắt lửa của nó. Ban đầu, thiết bị "
               "được chia thành Nhóm I, dành cho sử dụng trong các hầm mỏ có "
               "khí (chủ yếu nhưng không chỉ là hầm mỏ than), và Nhóm II bao "
               "gồm thiết bị dùng trong các ngành công nghiệp khác (thực chất "
               "là công nghiệp trên mặt đất). Sách này đề cập đến thiết bị "
               "Nhóm II và sẽ không đi sâu vào các yêu cầu đối với Nhóm I."))

    b.append(h4("Phân nhóm thiết bị", "Apparatus sub-grouping"))
    b.append(p("Như đã nói, thiết bị được chia thành Nhóm I và Nhóm II. Thiết "
               "bị Nhóm II có thể được phân nhóm tiếp để xác định các yếu tố "
               "cụ thể phù hợp với việc sử dụng của nó. Hiện tại chỉ có một "
               "hệ thống phân nhóm được sử dụng phổ biến, liên quan đến năng "
               "lượng có thể giải phóng trong một tia lửa bên trong khí quyển "
               "nổ, hoặc với khả năng ngọn lửa truyền qua các khe hở nhỏ và "
               "bắt lửa bất kỳ khí quyển nổ nào ở phía sau khe hở."))
    b.append(p("Bảo vệ nội tại và các loại hình bảo vệ tương tự không tìm "
               "cách ngăn ngừa sự giải phóng năng lượng điện, mà chỉ giới hạn "
               "giá trị của nó ở mức không gây bắt lửa. Thiết bị và hệ thống "
               "được cho là bảo vệ nội tại sẽ được phân nhóm như sau:-"))
    b.append(p("Phân nhóm IIA: Thiết bị và hệ thống sẽ không bắt lửa hỗn hợp "
               "dễ bắt lửa nhất của propan/không khí khi được thử nghiệm theo "
               "Điều 10.4 của BS/EN 50020 (1993). Phép thử này tương ứng xấp "
               "xỉ với năng lượng giải phóng tương đương 160 µJ từ một mạch "
               "cảm ứng mà tại đó sự giải phóng năng lượng rất hiệu quả. Các "
               "khí, hơi và sương mù ở dạng hỗn hợp với không khí được xếp vào "
               "phân nhóm này khi dòng điện tối thiểu cần để gây bắt lửa "
               "(MIC) lớn hơn 0.8 lần dòng điện cần để bắt lửa hỗn hợp dễ bắt "
               "lửa nhất của mê-tan phòng thí nghiệm và không khí (mê-tan "
               "phòng thí nghiệm có độ tinh khiết lớn hơn 95 phần trăm) trong "
               "thiết bị thử tia lửa (xem Phụ lục B của BS/EN 50020 (1993)¹, "
               "dùng mạch hiệu chuẩn quy định trong Phụ lục đó)."))
    b.append(p("Phân nhóm IIB: Thiết bị và hệ thống sẽ không bắt lửa hỗn hợp "
               "dễ bắt lửa nhất của etilen/không khí khi được thử nghiệm theo "
               "Điều 10.4 của BS/EN 50020 (1993). Phép thử này tương ứng xấp "
               "xỉ với năng lượng giải phóng 80 µJ từ một mạch cảm ứng mà tại "
               "đó sự giải phóng năng lượng rất hiệu quả. Các khí, hơi và "
               "sương mù ở dạng hỗn hợp với không khí được xếp vào phân nhóm "
               "này khi MIC của chúng nằm giữa 0.45 và 0.8 lần giá trị cần để "
               "bắt lửa hỗn hợp dễ bắt lửa nhất của mê-tan phòng thí nghiệm và "
               "không khí khi thử trong thiết bị thử tia lửa (xem Phụ lục B "
               "của BS/EN 50020 (1993)¹, dùng mạch hiệu chuẩn quy định trong "
               "Phụ lục đó)."))
    b.append(p("Phân nhóm IIC: Thiết bị hoặc hệ thống sẽ không bắt lửa hỗn "
               "hợp dễ bắt lửa nhất của hydro/không khí khi được thử nghiệm "
               "theo Điều 10.4 của BS/EN 50020 (1993). Phép thử này tương ứng "
               "xấp xỉ với năng lượng giải phóng 40 µJ từ một mạch cảm ứng mà "
               "tại đó sự giải phóng năng lượng rất hiệu quả. Các khí, hơi và "
               "sương mù ở dạng hỗn hợp với không khí được xếp vào phân nhóm "
               "này khi MIC của chúng nhỏ hơn 0.45 lần giá trị cần để bắt lửa "
               "hỗn hợp dễ bắt lửa nhất của mê-tan phòng thí nghiệm và không "
               "khí khi thử trong thiết bị thử tia lửa (xem Phụ lục B của "
               "BS/EN 50020 (1993), dùng mạch hiệu chuẩn quy định trong Phụ "
               "lục đó)."))
    b.append(p("Trong trường hợp phân nhóm IIC, phát biểu này có vẻ hơi lạ vì "
               "thiết bị hoặc hệ thống được thử bằng hydro/không khí có MIC "
               "vào khoảng 0.45, và các hỗn hợp khí/không khí nhạy hơn có thể "
               "được thiết bị bắt lửa. Thực tế là hydro/không khí là khí nhạy "
               "nhất đã biết và các hỗn hợp khí nhạy hơn chỉ có thể tạo ra "
               "bằng cách bổ sung thêm oxy vào hỗn hợp. Những hỗn hợp như vậy "
               "nằm ngoài phạm vi của Tiêu chuẩn này và cần được xử lý riêng."))
    return "".join(b)


def body_en():
    b = []
    b.append(h3("Apparatus to European Standards",
                "Apparatus to European Standards"))

    b.append(p("Before embarking upon a detailed examination of the general "
               "requirements¹ Standard it is necessary to understand the "
               "wording used in this and other Standards. First, the Standard "
               "does not have the imperative of legislation and cannot "
               "dictate what must or must not be done to comply with the law "
               "in any country."))
    b.append(p("The words which are important in this and other Standards "
               "are, first <i>shall</i>, the use of which indicates that a "
               "requirement is a necessity as far as the Standard is "
               "concerned. If this is not complied with compliance with the "
               "Standard cannot be claimed."))
    b.append(p("Second, the use of <i>should</i>, which indicates a strong "
               "recommendation but allows some flexibility in application of "
               "the Standard. In other words, it may be that, occasionally, "
               "an alternative approach producing the same effective result "
               "will be acceptable. The stress here is on the word "
               "<i>occasional</i> as the relaxation is not intended to allow "
               "a coach and horses to be driven through the Standard. It "
               "should be noted that the word <i>should</i> is only "
               "occasionally used in any event."))
    b.append(p("The word <i>must</i> is seldom used in Standards but where it "
               "does appear it means that a law exists at the time the "
               "Standard was written, and an imperative is appropriate. The "
               "Standard is not in this case making law but drawing attention "
               "to the existence of law."))
    b.append(p("Chapter 7 identifies the European Standards which exist for "
               "the differing types of explosion protected equipment. It "
               "draws attention to the fact that, unlike the preceding "
               "National Standards in the UK where all of the requirements "
               "were contained within the particular protection concept "
               "Standard, the European Standards contain only those "
               "requirements specific to the particular protection concept, "
               "with the more general requirements (i.e., those which applied "
               "to several of the protection concepts) being contained in a "
               "general requirements¹ Standard to which the protection "
               "concept Standards refer. The requirements of this Standard "
               "are then considered to apply to all of the particular "
               "protection concept Standards, unless a particular Standard "
               "specifically excludes one or more of these general "
               "requirements. This approach is considered to minimize the "
               "duplication of effort by the Standards writing committees "
               "and give a more rational approach. In practice, this approach "
               "has been shown to have significant drawbacks, in that any "
               "change to the general requirements Standard automatically "
               "impinges upon the particular protection concept Standards "
               "which are written by different European committees, "
               "comprising different sets of people to those involved in the "
               "writing of the general requirements Standard. To overcome "
               "this, particular protection concept Standards specify a "
               "particular issue of the general requirements Standard, but "
               "this means that, as the particular protection concept "
               "Standards are written in different time frames, it is "
               "necessary to have more than one issue of the general "
               "requirements Standard valid at any one time. Unless one is "
               "very careful, confusion can result. While the situation is "
               "less than perfect, it is unlikely to change and whenever a "
               "particular protection concept is addressed, it is necessary "
               "to ensure that it is addressed with the appropriate issue of "
               "the general requirements Standard."))
    b.append(p("The latest issue of the general requirements Standard is "
               "BS/EN 50014 (second edition) (1993)¹ which applies to all of "
               "the protection concepts with the exception of Ex m (BS 5501, "
               "Part 8 (1988) – EN 50028 (1987) at present. Its predecessor "
               "which applies to Ex m was BS 5501, Part 1 (1977) – EN 50014 "
               "(1977), first edition. A further complication is the fact "
               "that both of these Standards have been the subject of "
               "amendments issued after the publication of the Standards "
               "(seven in the case of BS 5501 part 1 (1977) and one in the "
               "case of BS/EN 50014 (1993)¹). In general terms, amendments are "
               "considered to be part of the standard and thus will apply to "
               "all of the protection concept Standards from the date of "
               "amendment issue, unless these latter Standards are themselves "
               "amended to exclude the amendment to the general requirements "
               "Standard. To simplify the situation, therefore, the second "
               "edition of the Standard (BS/EN 50014 (1993)¹, including "
               "amendment 1) will form the basis of the content of this "
               "chapter and differences between it and the first edition "
               "(BS 5501, part 1 (1977), including amendments 1 to 7) will be "
               "highlighted to cover the situation until Directive 76/117/EEC "
               "is amended, as previously discussed."))
    b.append(note("<b>Note on 'Ex m' and 'Exm'.</b> The page images print 'Ex "
                  "m' with a space in both places in this passage ('with the "
                  "exception of Ex m' and 'applies to Ex m'); the extracted "
                  "text layer renders the first occurrence as 'Exm'. The "
                  "printed form with the space is retained in both places "
                  "here, and the variant is recorded because both spellings "
                  "appear in the source."))

    b.append(h3("8.1 BS/EN 50014 (1993) (including amendment 1 (1994))",
                "8.1 BS/EN 50014 (1993) (including amendment 1 (1994))"))
    b.append(p("It is better to deal with the amendment to this Standard "
               "first to avoid any confusion. It may appear that the "
               "necessity to amend a Standard so soon after its publication "
               "is worrying, but the amendment was issued only to the English "
               "text of the Standard which omitted the limitation of validity "
               "of the Standard to the second editions of the protection "
               "concept standards only. (All European Standards are written "
               "in three languages, English, French and German and in this "
               "case the English language text omitted a paragraph present "
               "in the French and German texts). It is worthy of note here "
               "that EN Standards may appear in other languages but those are "
               "national translations and in any dispute as to the meaning of "
               "the Standards the English, French and German texts must be "
               "referred to for clarification."))
    b.append(p("BS/EN 50014 (1993)¹ deals with those matters common to more "
               "than one of the protection concepts. Some of its content may "
               "not be appropriate to a particular protection concept "
               "Standard and, in this case, that Standard will, in its scope "
               "where exclusion is total, or in its detailed text where "
               "exclusion is only partial, define those parts of BS/EN 50014 "
               "(1993)¹ which do not apply."))
    b.append(p("The basic matters dealt with in BS/EN 50014 (1993)¹ and its "
               "predecessor, BS 5501, part 1 (1977) are as follows:"))
    b.append(p("1. Definitions of terms used in BS/EN 50014 (1993)¹ and its "
               "subsidiary protection concept Standards."))
    b.append(p("2. The method by which apparatus is divided into groups and "
               "temperature classes for utilization purposes."))
    b.append(p("3. Requirements for enclosures."))
    b.append(p("4. Requirements for fasteners used for enclosure securing, "
               "interlocking devices used to prevent protection being "
               "bypassed, bushings used for connections, and cements which "
               "may be used in enclosure construction."))
    b.append(p("5. Requirements for connection of conductors to the apparatus "
               "and for entry of cables to the apparatus."))
    b.append(p("6. Requirements which additionally apply to particular types "
               "of apparatus such as rotating machines, luminaires, fuses, "
               "etc."))
    b.append(p("7. Requirements for ex-components, which are components which "
               "form part of an apparatus but may be used in several types of "
               "apparatus, and be examined for compliance with the appropriate "
               "parts of the standard separately to avoid repeat evaluation."))
    b.append(p("8. Requirements for marking of complying apparatus to ensure "
               "that appropriate information is given to the purchaser."))
    b.append(p("It is worthy of note that BS/EN 50014 (1993)¹ draws attention "
               "to the fact that apparatus constructors need also to ensure "
               "that basic electrical safety requirements are met, and are "
               "assumed to guarantee this by application of the marking "
               "required by the Standard. (BS 5501, part 1 (1977) required a "
               "specific form of declaration for this purpose.)"))

    b.append(h4("8.1.1 Definitions", "8.1.1 Definitions"))
    b.append(p("There are some 25 definitions in the Standard, some dealing "
               "with terms such as apparatus and some dealing with the "
               "meaning of some of the symbols used in the Standard and its "
               "supplementary protection concept Standards. In common with "
               "earlier chapters they will be detailed at the end of this "
               "book. While in the main, these definitions cover all of the "
               "group of Standards, they are not complete but need to be "
               "added to by additional definitions in the protection concept "
               "Standards (showing the problems associated with limiting the "
               "meaning of terms by definition)."))

    b.append(h4("8.1.2 Division of apparatus into sub-groups and surface "
                "temperature classes",
                "8.1.2 Division of apparatus into sub-groups and surface "
                "temperature classes"))
    b.append(p("As earlier indicated, electrical apparatus is divided into "
               "groups and classes according to its performance with regard "
               "to ignition capability. Initially, the apparatus is divided "
               "into Group I, which is intended for use in gassy mines "
               "(principally but not exclusively coal mines), and Group II "
               "which covers apparatus for use in other industries (which in "
               "effect means surface industry). This book is concerned with "
               "Group II Apparatus and the requirements for Group I will not "
               "be further explored."))

    b.append(h4("Apparatus sub-grouping", "Apparatus sub-grouping"))
    b.append(p("As already stated, apparatus is divided into Group I and "
               "Group II. Group II apparatus may be further divided into "
               "sub-groups to identify particular factors appropriate to its "
               "use. At the moment, only one sub-grouping system is in common "
               "use and that is related to the energy which may be released "
               "in a spark within an explosive atmosphere, or with the ability "
               "of flame to transmit through small gaps and ignite any "
               "explosive atmosphere downstream of the gap."))
    b.append(p("Intrinsic safety and similar protection concepts do not seek "
               "to prevent the release of electrical energy, but only to "
               "limit its value to that which cannot cause ignition. Apparatus "
               "and systems which are said to be intrinsically safe will be "
               "sub-grouped as follows:-"))
    b.append(p("Sub-group IIA: Apparatus and systems which will not ignite "
               "the most easily ignitable mixture of propane/air when tested "
               "in accordance with Clause 10.4 of BS/EN 50020 (1993). This "
               "test corresponds approximately to an equivalent released "
               "energy of 160 µJ from an inductive circuit where energy "
               "release is very efficient. Gases, vapours and mists in "
               "mixture with air are associated with this sub-group where the "
               "minimum current required to cause their ignition (MIC) is "
               "more than 0.8 of that needed to ignite the most easily "
               "ignitable mixture of laboratory methane and air (laboratory "
               "methane is more than 95 per cent pure) in a spark test "
               "apparatus (see Annex B of BS/EN 50020 (1993)¹ using the "
               "calibration circuit specified in that Annex)."))
    b.append(p("Sub-group IIB: Apparatus and systems which will not ignite "
               "the most easily ignitable mixture of ethylene/air when tested "
               "in accordance with Clause 10.4 of BS/EN 50020 (1993). This "
               "test corresponds approximately to a released energy of 80 µJ "
               "from an inductive circuit where energy release is very "
               "efficient. Gases, vapours and mists in mixture with air are "
               "associated with this sub-group when their MIC is between 0.45 "
               "and 0.8 of that needed to ignite the most easily ignitable "
               "mixture of laboratory methane and air when tested in a spark "
               "test apparatus (see Annex B of BS/EN 50020 (1993)¹ using the "
               "calibration circuit specified in that Annex)."))
    b.append(p("Sub-group IIC: Apparatus or systems which will not ignite the "
               "most easily ignitable mixture of hydrogen/air when tested in "
               "accordance with Clause 10.4 of BS/EN 50020 (1993). This test "
               "corresponds approximately to a released energy of 40 µJ from "
               "an inductive circuit where energy release is very efficient. "
               "Gases, vapours and mists in mixture with air are associated "
               "with this sub-group when their MIC is less than 0.45 of that "
               "necessary to ignite the most easily ignitable mixture of "
               "laboratory methane and air when tested in a spark test "
               "apparatus (see Annex B of BS/EN 50020 (1993) using the "
               "calibration circuit specified in that Annex)."))
    b.append(p("In the case of sub-group IIC, the statement may sound a little "
               "odd as the apparatus or system is tested with hydrogen/air "
               "which has an MIC of around 0.45, and more sensitive gas/air "
               "mixtures may be ignited by the apparatus. The fact is that "
               "hydrogen/air is the most sensitive gas known and more "
               "sensitive gas mixtures can only be produced by additional "
               "oxygen in the mixture. Such mixtures are outside the scope of "
               "this Standard and need to be treated specially."))
    return "".join(b)
