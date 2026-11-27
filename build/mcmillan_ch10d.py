# -*- coding: utf-8 -*-
"""Chapter 10, module D - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 244-252 (PDF pp. 265-273),
raw lines 11218-11538.

Covers the tail of 10.2.1 "2 Spigot joints", the numbered joint types
3/4/5 (cylindrical / operating-rod / partial-cylindrical, threaded and
cemented joints), 10.2.2 joints for rotary or longitudinal shafts and
operating rods, and the opening of 10.2.3 joints for shafts and rotating
machines.  Figures 10.11-10.12 and Tables 10.7-10.11 are inserted at
their printed positions; the figure references on printed p.252 are
preserved as printed, with a translator note on the apparent swap.
"""
from mcmillan_common import h3, h4, p, note, table, fig
import mcmillanfig10b as FB
import mcmillan_tbl10_6_10 as T2
import mcmillan_tbl10_11_15 as T3


def body_vi():
    b = []

    # Printed p.244 - tail of 2 Spigot joints (continuation of module C).
    b.append(p("chiều dài mối nối 'L', chiều dài rút gọn 'l' đến lỗ thoát "
               "cho bu lông, và khe hở cho phép tại phần phẳng của mối nối "
               "không thay đổi, khe hở này được quy định trong Bảng 10.5. Nếu "
               "lớp vát hoặc bán kính có thể được thu nhỏ với mức xâm lấn "
               "không quá 0.5 mm, thì các giá trị này có thể tăng lên 0.2 mm "
               "đối với các mối nối nhóm IIC có chiều dài từ 25 mm trở lên, "
               "và 0.25 mm đối với các mối nối đó có chiều dài không dưới "
               "40 mm. Trong trường hợp không có lớp vát hoặc bán kính, hoặc "
               "khi 'l' đạt được hoàn toàn ở phần phẳng của mối nối, thì các "
               "giá trị khe hở này ở phần hình trụ của mối nối không áp dụng "
               "và khe hở yêu cầu là khe hở trong Bảng 10.5."))
    b.append(p("Dù điều này làm cho việc áp dụng mối nối lồng ghép phức tạp "
               "hơn đôi chút so với mối nối mặt bích tương ứng, nhưng việc "
               "đưa axetilen vào và khả năng giảm hiệu dụng kích thước vỏ bọc "
               "làm cho loại mối nối này trở nên hấp dẫn, đặc biệt cho các "
               "ứng dụng dụng cụ đo, và loại mối nối này ngày càng trở nên "
               "phổ biến."))
    b.append(p("Tất cả các thông tin trên đều dựa trên mối nối lồng ghép mà ở "
               "đó phần của mối nối không nằm trong phần phẳng (có thể tạo "
               "thành toàn bộ đường dẫn ngọn lửa) là hình trụ. Không có lý do "
               "gì phần này không thể là hình nón, miễn là khe hở đồng đều "
               "trong suốt phần hình nón của mối nối và phần hình nón đó đáp "
               "ứng các yêu cầu về chiều dài và khe hở của một mối nối lồng "
               "ghép thông thường. Tuy nhiên, có những hạn chế trong trường "
               "hợp các mối nối nhóm con IIC và trong những trường hợp đó độ "
               "côn của mối nối (góc côn) phải không vượt quá 5°. Dù là một "
               "trường hợp đặc biệt của mối nối lồng ghép, các mối nối này "
               "thường được gọi là mối nối hình nón."))

    # Printed p.245 - joint type 3.
    b.append(h4("3 Mối nối hình trụ, mối nối thanh truyền động và mối nối "
                "hình trụ một phần",
                "3 Cylindrical joints, operating rod joints, and partial "
                "cylindrical joints"))
    b.append(p("Một mối nối hình trụ cơ bản không khác gì một mối nối lồng "
               "ghép trong đó toàn bộ đường dẫn ngọn lửa nằm ở phần hình trụ "
               "của mối nối, và các kích thước giới hạn được nêu trong Bảng "
               "10.6. Tuy nhiên, các mối nối này chủ yếu được dùng cho thanh "
               "truyền động và trục quay, nơi có thể phát sinh vấn đề lệch "
               "tâm và mòn. Vì vậy, trong những trường hợp đó có các yêu cầu "
               "đặc biệt áp dụng cho chúng. Yêu cầu đối với trục sẽ được đề "
               "cập trong một phần sau của chương này, nhưng yêu cầu đối với "
               "thanh truyền động được đề cập ở đây."))
    b.append(p("Cần nhấn mạnh rằng nếu hai chi tiết của mối nối hình trụ được "
               "cố định chắc chắn và mối nối không chuyển động cũng như không "
               "quay trong quá trình hoạt động bình thường, thì các yêu cầu "
               "này không áp dụng và mối nối phải được xem như một mối nối "
               "lồng ghép có toàn bộ đường dẫn ngọn lửa nằm ở phần hình trụ "
               "của mối nối."))
    b.append(p("Trong trường hợp chi tiết bên trong của mối nối là một thanh "
               "truyền động, khi phải tính đến độ lệch tâm do lắp ráp hoặc do "
               "chuyển động, thì khe hở mối nối yêu cầu phải đạt được ngay cả "
               "khi thanh nằm lệch về một phía của mối nối (nghĩa là khi "
               "thanh nằm chính giữa lỗ thì khe hở quanh nó phải bằng một nửa "
               "khe hở thường yêu cầu). Ngoài ra, chiều dài mối nối phải tuân "
               "thủ chiều dài mối nối yêu cầu đối với các mối nối hình trụ "
               "tĩnh đã nêu trước đó trong chương này, nhưng đồng thời phải "
               "có chiều dài ít nhất bằng chính đường kính của thanh khi "
               "đường kính này nhỏ hơn 25 mm. Trường hợp thanh có đường kính "
               "vượt quá 25 mm thì chỉ áp dụng yêu cầu chiều dài mối nối hình "
               "trụ tĩnh."))
    b.append(p("Nếu chi tiết bên trong của mối nối là thanh truyền động và "
               "mối nối bị mòn trong tuổi thọ hoạt động bình thường của vỏ "
               "bọc do vật liệu chế tạo và/hoặc tần suất hoạt động, thì các "
               "chi tiết của mối nối phải có thể thay thế. Điều này có thể "
               "đạt được, ví dụ, bằng cách làm chi tiết ngoài của mối nối từ "
               "vật liệu bạc mềm hơn và cho phép thay thế nó. Nên quan theo "
               "hướng coi rằng mòn là có thể xảy ra trừ khi có thể chứng minh "
               "rõ ràng là không. Ngoài ra, thanh không được tháo ra từ bên "
               "ngoài vỏ bọc, cũng không được có khả năng di chuyển hoàn toàn "
               "vào bên trong vỏ bọc, vì một trong hai trường hợp đó sẽ loại "
               "bỏ mọi đường dẫn ngọn lửa và cho phép truyền nổ. Trong hầu "
               "hết các trường hợp, thanh nhiều khả năng đã được cố định ở "
               "mức cần thiết nhờ các chi tiết bắt giữ cần thiết cho hoạt "
               "động của nó bên trong vỏ bọc, nhưng nếu không thì cần cố "
               "định nó chống lại việc bị tháo ra bằng các chi tiết cố định "
               "bên trong (ví dụ vòng hãm chốt hoặc tương tự)."))
    b.append(p("Mối nối hình trụ một phần được phép dùng khi các tấm chẳng "
               "hạn được dùng làm nắp đậy trên các hình trụ rỗng, và một ví "
               "dụ được thể hiện ở Hình 10.11. Loại mối nối này nên được xử "
               "lý hoàn toàn như mối nối mặt bích về khe hở, chiều dài mối "
               "nối, gioăng và cách đưa bu lông bắt giữ vào, nhưng trong "
               "trường hợp này có lệnh cấm hoàn toàn loại mối nối này đối với "
               "vỏ bọc dự định dùng cho nhóm con IIC, nên khác với các loại "
               "mối nối khác, mối nối hình trụ một phần không được dùng trong "
               "vỏ bọc cho nhóm con IIC. Điều này có thể là do khó khăn lớn "
               "hơn trong việc đạt được sự trùng khớp bán kính cần thiết "
               "giữa hai chi tiết so với việc đạt được độ phẳng cần thiết "
               "của mối nối mặt bích."))

    # Printed p.246 - figure, then text on partial cylindrical joints.
    b.append(fig(11, FB.fig_f1011()))
    b.append(p("Đáng chú ý là các mối nối này không được xác định cụ thể "
               "trong BS 5501, Phần 5 (ấn bản đầu tiên của EN 50018). Tuy "
               "nhiên, sự tương tự của chúng với mối nối mặt bích có nghĩa là "
               "chúng có thể đã được ít nhất một số tổ chức chứng nhận liên "
               "quan xem xử lý như vậy, và có thể tồn tại trong một số thiết "
               "bị - thậm chí cả thiết bị có thể tích nhỏ hơn 500 cm³ dự định "
               "dùng cho nhóm con IIC. Yêu cầu trong BS/EN 50018⁶ (1995) (ấn "
               "bản thứ hai của EN 50018) là một hạn chế bổ sung đối với việc "
               "sử dụng các mối nối như vậy. Tuy nhiên, vì không có thông báo "
               "chính thức nào cho thấy cách làm trước đó là không an toàn, "
               "nên điều này không đòi hỏi hành động khắc phục hồi tố nào, "
               "dù vậy nên ưu tiên thiết bị theo BS/EN 50018⁶ trong tương "
               "lai."))
    b.append(note("<b>Lưu ý về số tham khảo in.</b> Bản in có số mũ ⁶ sau "
                  "'BS/EN 50018' ở hai chỗ (tài liệu tham khảo 6 là BS/EN "
                  "50018 (1995)); giữ nguyên số mũ này."))
    b.append(p("Một ống mao dẫn có thể được coi là một mối nối hình trụ có "
               "đường kính trong bằng 0. Do đó, các khe hở tối đa quy định "
               "trong Bảng 10.6 sẽ trở thành đường kính trong tối đa của ống "
               "mao dẫn."))

    # Printed p.246-247 - joint type 4, threaded joints.
    b.append(h4("4 Mối nối ren", "4 Threaded joints"))
    b.append(p("Các mối nối giữa các chi tiết của vỏ chống cháy cũng có thể "
               "là mối nối ren. Khi đó, các ren liên quan phải thuộc loại được "
               "nêu tên cụ thể với chất lượng lắp ghép cụ thể, hoặc phải được "
               "quy định, có thể ở mức chất lượng thấp hơn, và phải chịu các "
               "yêu cầu bổ sung khi thử nghiệm truyền ngọn lửa."))
    # Printed p.247 - Tables 10.7-10.8 interrupt the paragraph in mid-sentence.
    b.append(table(T2.HEAD107_VI, T2.ROWS107, T2.CAPTION107_VI))
    b.append(note(T2.NOTE107_VI))
    b.append(table(T2.HEAD108_VI, T2.ROWS108, T2.CAPTION108_VI))
    b.append(note(T2.NOTE108_VI))
    b.append(p("Kết quả là, một số thông số kỹ thuật có thể bị bỏ qua miễn là "
               "thử nghiệm nghiêm ngặt hơn được thực hiện. Các yêu cầu đối "
               "với mối nối ren được nêu trong Bảng 10.7 đối với ren trụ song "
               "song và Bảng 10.8 đối với ren trụ côn. Ngoài ra, cần tuân thủ "
               "các yêu cầu sau."))
    b.append(p("Khi dùng các mối nối ren này cho nắp đậy, cửa hoặc nắp che "
               "của vỏ chống cháy, luôn có khả năng chúng bị lỏng ra do nhân "
               "viên thiếu kinh nghiệm và, để tránh điều đó, các mối nối như "
               "vậy phải được cố định bằng các chi tiết bắt giữ có chất lượng "
               "và yêu cầu vận hành như bu lông hoặc vít của mối nối mặt bích "
               "và mối nối lồng ghép. Cách thông thường để làm điều này với "
               "một nắp che là lắp một vít chụp (cap screw) vào chi tiết "
               "ngoài, ngay ngoài phần"))

    # Printed p.248 - continuation, then italic run-in subheadings.
    b.append(p("ren, sao cho khi được siết chặt thì vít ép vào chi tiết bên "
               "trong, cũng nằm ngoài ren, ngăn không cho mối nối bị lỏng. "
               "Vít chụp (capscrew) phải bằng phẳng với mặt ngoài của vỏ bọc "
               "khi được siết chặt để không thể tháo ra bằng kìm, v.v."))
    b.append(note("<b>Lưu ý về cách viết in.</b> Bản in dùng 'cap screw' ở "
                  "đoạn trước và 'capscrew' ở đoạn này; giữ nguyên cả hai "
                  "cách viết."))
    b.append(p("<i>Ren trụ song song</i>"))
    b.append(p("Đối với ren trụ song song, cần tính đến các hạn chế sau. Thứ "
               "nhất, không cho phép dùng ren song song có bước ren nhỏ hơn "
               "0.7 mm vì ren quá mịn tạo nên độ sâu ren nhỏ và làm tăng khả "
               "năng tuột ren hoặc tuột một phần trong khi sử dụng, dẫn đến "
               "hư hại đặc tính chống cháy của ren."))
    b.append(p("Thứ hai, khi bước ren vượt quá 2 mm, sự kết hợp giữa bước ren "
               "thô và chất lượng lắp ghép có thể không đủ để đạt được các "
               "đặc tính chống cháy cần thiết và thiết bị có thể không vượt "
               "qua được các thử nghiệm trong Bảng 10.7. Trong những trường "
               "hợp đó, có thể cần tăng số ren ăn khớp lên hơn năm. Không thể "
               "đưa ra mức tăng cụ thể vì điều đó phụ thuộc vào mức bước ren "
               "vượt quá 2 mm, nhưng như một điểm khởi đầu, người ta đề xuất "
               "thêm một ren cho mỗi 0.5 mm mà bước ren vượt quá 2 mm. Ngoài "
               "ra, có thể thực hiện thử nghiệm tương tự như thử nghiệm dùng "
               "cho ren không tiêu chuẩn. Các phương án này nên được thảo "
               "luận với tổ chức chứng nhận phù hợp trước khi được áp dụng "
               "trong từng trường hợp cụ thể."))
    b.append(note("<b>Lưu ý về nguyên bản.</b> Bản in viết 'where the threads "
                  "pitch exceeds 2 mm'; giữ nguyên cách diễn đạt đó, còn bản "
                  "dịch hiểu theo ý định là bước ren vượt quá 2 mm."))
    b.append(p("Thứ ba, khi dùng dạng ren và/hoặc dung sai khác với những "
               "dạng được Bảng 10.7 cho phép, các mối nối sẽ chịu các yêu cầu "
               "bổ sung, thường ở dạng tăng mức độ rút ren khi thử nghiệm so "
               "với mức dùng cho các ren đáp ứng yêu cầu."))
    b.append(p("<i>Ren trụ côn</i>"))
    b.append(p("Dù ren trụ côn phải đáp ứng các yêu cầu của Bảng 10.8, người "
               "ta vẫn công nhận rằng ở giới hạn dung sai thì số ren ăn khớp "
               "có thể ít hơn năm."))
    b.append(p("<i>Cố định mối nối ren</i>"))
    b.append(p("Khác với mối nối mặt bích, mối nối lồng ghép và mối nối hình "
               "trụ, thông thường không thể cố định dễ dàng mối nối này, vì "
               "nó cần quay để đảm bảo được lắp lẫn hoàn toàn. Tuy nhiên, đây "
               "là một chi tiết dạng vít giống như các chi tiết bắt chặt và, "
               "miễn là cần dùng cờ lê lục giác hoặc chìa lục giác để tháo "
               "ra và không có phần nhô ra nào cho phép mở bằng cách khác, "
               "thì có thể chấp nhận là đã được cố định sau khi vặn chặt hoàn "
               "toàn. Nếu còn nghi ngờ về chất lượng cố định, thì một vít chụp "
               "đầu lục giác trong cụm hình trụ bên ngoài mối nối, được ren "
               "vào chi tiết ngoài của mối nối, bên ngoài phần ren tạo thành "
               "đường dẫn ngọn lửa, sẽ đủ để cố định. Điều này chỉ làm dài "
               "thêm hình trụ một chút. Trong trường hợp nắp đậy, cửa và nắp "
               "che, vít bổ sung luôn được coi là cần thiết"))

    # Printed p.249 - continuation, then joint type 5.
    b.append(p("và nên áp dụng cách này trong mọi trường hợp để tránh các vấn "
               "đề do quan điểm khác nhau."))
    b.append(h4("5 Mối nối xi măng", "5 Cemented joints"))
    b.append(p("Mối nối xi măng thường được dùng để lắp các thứ như cửa sổ "
               "quan sát vào vỏ chống cháy, và thường khó tạo được mối nối "
               "đáp ứng các yêu cầu về mối nối. Trong những trường hợp đó, có "
               "thể tạo mối nối bằng xi măng và mối nối này có thể ngắn hơn "
               "đáng kể so với mối nối thông thường tương ứng, chỉ cần đáp "
               "ứng yêu cầu về chiều dài trong Bảng 10.9."))
    b.append(p("Trường hợp mối nối sẽ đáp ứng các yêu cầu đối với mối nối mặt "
               "bích, mối nối lồng ghép, mối nối hình trụ hoặc mối nối ren khi "
               "không có xi măng, kể cả nhu cầu cố định của các mối nối đó, "
               "thì không áp dụng yêu cầu đặc biệt nào ngoài thử nghiệm rò rỉ "
               "nhằm đảm bảo lớp xi măng kín hoàn toàn, vì cả độ bền của mối "
               "nối lẫn đặc tính chống cháy của nó đều không phụ thuộc vào xi "
               "măng. (Cần đảm bảo lớp xi măng kín không để xảy ra tia phun "
               "gây hiệu năng chống cháy bất thường và một thử nghiệm làm kín "
               "được đưa vào trong BS/EN 50018 (1995). Ngoài ra, độ bền của "
               "mối nối không được phụ thuộc vào xi măng, và việc tháo ra và "
               "lắp lại mối nối phải thực hiện được mà không làm hỏng xi măng. "
               "Có thể đạt được điều này bằng cách chế tạo mối nối xi măng dưới "
               "dạng hộp nạp và dùng việc lắp nó vào một mối nối có thiết kế "
               "thông thường hơn làm phương pháp thay thế. Tuy nhiên, nếu mối "
               "nối là một phần của vỏ bọc và không định tháo ra, thì không "
               "cần hành động bổ sung nào."))
    b.append(note("<b>Lưu ý về nguyên bản.</b> Bản in viết 'neither the "
                  "strength of the joint or its flameproof performance rely "
                  "on the cement' (dùng 'or' thay vì 'nor'); bản dịch giữ nguyên "
                  "ý định là cả độ bền của mối nối lẫn đặc tính chống cháy của "
                  "nó đều không phụ thuộc vào xi măng."))
    b.append(table(T2.HEAD109_VI, T2.ROWS109, T2.CAPTION109_VI))
    b.append(note(T2.NOTE109_VI))
    b.append(p("Trường hợp mối nối không phù hợp với yêu cầu của các loại mối "
               "nối khác khi không có xi măng, mà chỉ phù hợp với yêu cầu về "
               "chiều dài của Bảng 10.9, thì phải có bố trí đảm bảo độ bền của "
               "mối nối không phụ thuộc vào xi măng. Ngoài ra, trong những "
               "trường hợp này, xi măng không được bị hư hại bởi các thử "
               "nghiệm khả năng chịu nhiệt và chịu lạnh quy định trong BS/EN "
               "50014 (1994)¹² (xem thêm Chương 7)."))
    b.append(note("<b>Lưu ý về số tham khảo in.</b> Bản in có số mũ ¹² sau "
                  "'BS/EN 50014 (1994)'; giữ nguyên số mũ này."))

    # Printed p.250 - 10.2.2 and Fig. 10.12.
    b.append(h4("10.2.2 Mối nối cho trục quay hoặc trục chuyển động dọc và "
                "thanh truyền động",
                "10.2.2 Joints for rotary or longitudinal shafts and "
                "operating rods"))
    b.append(p("Các thanh truyền động đi xuyên qua thành vỏ chống cháy "
               "chuyển động theo hướng dọc hoặc hướng quay. Trong cả hai "
               "trường hợp, mối nối hình trụ là phù hợp vì không dễ áp dụng "
               "mối nối mặt bích hoặc mối nối lồng ghép. Dù có thể hình dung "
               "một tình huống mà việc dùng mối nối lồng ghép đơn giản (mối "
               "nối có đường dẫn ngọn lửa hoàn toàn nằm ở phần hình trụ của "
               "mối nối) là có thể, thì việc cố định mối nối đó lại gây ra "
               "khó khăn thực sự. Khi chuyển động chỉ theo hướng quay, có thể "
               "lập luận rằng một loại mối nối chuyên biệt khác cũng phù "
               "hợp. Đó là mối nối mê cung thể hiện ở Hình 10.12. Mối nối này "
               "giống như mối nối hình trụ, chỉ khác là đường dẫn ngọn lửa đi "
               "qua một tập hợp các chi tiết hình trụ đan xen. Nếu dùng loại "
               "mối nối chuyên biệt này, nên đảm bảo rằng tổ chức chứng nhận "
               "liên quan sẽ chấp nhận nó, vì cách Tiêu chuẩn được viết ra "
               "có thể được hiểu là loại trừ nó tùy theo cách giải thích."))
    b.append(p("Khi dùng mối nối hình trụ trong cấu hình này, mối nối phải "
               "đáp ứng các yêu cầu đặc biệt vì một chi tiết của nó chuyển "
               "động và phải giả định có một số mòn. Dù cần có chiều dài mối "
               "nối tối thiểu và khe hở tối đa phù hợp với Bảng 10.6, chiều "
               "dài mối nối còn phải liên quan đến kích thước của thanh "
               "truyền động tạo thành chi tiết chuyển động của mối nối, và "
               "chiều dài mối nối ở một mức độ nhất định được xác định bởi "
               "chu vi của thanh. Ngoài việc tuân thủ Bảng 10.6, mối nối phải "
               "có chiều dài ít nhất bằng đường kính của thanh truyền động, "
               "đối với đường kính thanh lên tới 25 mm."))
    b.append(fig(12, FB.fig_f1012()))

    # Printed p.251 - continuation and Table 10.10.
    b.append(p("Ngoài ra, khi thanh không có ổ đỡ nào khác ngoài chi tiết cố "
               "định của mối nối và dự kiến mối nối bị mòn đáng kể trong hoạt "
               "động bình thường, thì chi tiết cố định của mối nối nên được "
               "làm thành một bạc có thể thay thế để có thể dễ dàng đổi mới "
               "mối nối khi cần."))
    b.append(p("Nếu xét thấy mối nối dạng mê cung (xem Hình 10.12) là phù hợp, "
               "thì được phép nới lỏng và không cần tuân thủ các giới hạn này "
               "đối với mối nối đó, miễn là có thể chứng minh nó chống cháy "
               "được bằng các thử nghiệm trong BS/EN 50018, dù nên đảm bảo "
               "chiều dài mối nối tối thiểu và khe hở tối đa theo Bảng 10.6 "
               "với khoảng dự phòng bổ sung cho đường kính trục. Sự nới lỏng "
               "này có thể thực hiện được vì hình học của mối nối có khả năng "
               "ngăn truyền ngọn lửa cao hơn mối nối hình trụ tương ứng."))
    b.append(p("Để tránh mòn mối nối ở cả hai loại mối nối, thanh có thể được "
               "lắp một ổ bi không thuộc mối nối nhưng giữ thanh cách xa bề "
               "mặt mối nối, từ đó thực sự ngăn được mòn. Về nguyên tắc có thể "
               "chấp nhận hai loại ổ bi: ổ bi dạng bạc, trong đó chi tiết "
               "ngoài của ổ bi đứng yên, và ổ bi có phần tử lăn, đưa các phần "
               "tử lăn vào giữa thanh và vỏ bọc. Trong cả hai trường hợp, độ "
               "hở xuyên tâm nhỏ nhất giữa chi tiết chuyển động và chi tiết "
               "cố định của mối nối không được nhỏ hơn 0.05 mm, có tính đến "
               "dung sai. Đối với mối nối hình trụ, độ hở xuyên tâm tối đa "
               "không được vượt quá giá trị quy định trong Bảng 10.10 đối với "
               "ổ bi dạng bạc và Bảng 10.11 đối với ổ bi có phần tử lăn, với "
               "chiều dài mối nối đang xét; nhưng vì có sự nới lỏng đối với "
               "mối nối mê cung, nên trong những trường hợp chấp nhận loại "
               "mối nối này, không quy định giới hạn tối đa của độ hở xuyên "
               "tâm. Yêu cầu duy nhất là vượt qua được các thử nghiệm truyền "
               "ngọn lửa. Việc dùng ổ bi dạng bạc cho bất kỳ mối nối nào liên "
               "quan đến máy điện quay chỉ giới hạn ở các nhóm con IIA và "
               "IIB."))
    b.append(table(T2.HEAD1010_VI, T2.ROWS1010, T2.CAPTION1010_VI))
    b.append(note(T2.NOTE1010_VI))

    # Printed p.252 - Table 10.11, floating joint, 10.2.3 opening.
    b.append(table(T3.HEAD1011_VI, T3.ROWS1011, T3.CAPTION1011_VI))
    b.append(note(T3.NOTE1011_VI))
    b.append(p("Có thể dùng sự kết hợp giữa một mối nối hình trụ (hoặc mối "
               "nối mê cung khi loại đó được chấp nhận) và một mối nối mặt "
               "bích để tạo thành mối nối nổi, cho phép một mức độ nhất định "
               "của chuyển động ngang (xem Hình 10.13). Trong những trường "
               "hợp đó, chiều dài của mặt bích phải ít nhất bằng chiều dài "
               "yêu cầu trong Bảng 10.1 cộng thêm một lượng bằng chuyển động "
               "ngang lớn nhất dự kiến trong hoạt động. Các mối nối như vậy "
               "cũng phải được cố định chống quay và chỉ giới hạn ở vỏ bọc "
               "dự định dùng trong các nhóm con IIA và IIB."))
    b.append(note("<b>Lưu ý về trích dẫn hình.</b> Trích dẫn hình theo bản "
                  "gốc (có vẻ bị đảo trong nguyên bản): mối nối nổi được "
                  "minh họa ở Hình 10.14, còn 'k' được định nghĩa ở Hình "
                  "10.13."))
    b.append(h4("10.2.3 Mối nối cho trục và máy quay",
                "10.2.3 Joints for shafts and rotating machines"))
    b.append(p("Trục quay là một trường hợp đặc biệt. Do sự quay, thường "
               "không nên để mối nối chống cháy đảm nhiệm việc đỡ trục và "
               "người ta dùng một ổ bi."))
    return "".join(b)


def body_en():
    b = []

    # Printed p.244 - tail of 2 Spigot joints (continuation of module C).
    b.append(p("joint length 'L', the reduced length 'l' to the bolt clearance "
               "hole, and the gap permitted for the plane part of the joint "
               "remain unchanged, the latter being as specified in Table "
               "10.5. If the chamfer or radius can be reduced to an "
               "encroachment of no more than 0.5 mm, then these figures may "
               "be increased to 0.2 mm for Group IIC joints of 25 mm or "
               "greater length, and 0.25 mm for such joints of not less than "
               "40 mm length. In cases where no chamfer or radius exists, or "
               "where 'l' is achieved completely in the plane part of the "
               "joint, these figures for gaps in the cylindrical part of the "
               "joint do not apply and the required gaps are those in Table "
               "10.5."))
    b.append(p("While this makes the application of spigot joints a little "
               "more complex than their flange counterparts, the inclusion "
               "of acetylene and the effective reduction in enclosure size "
               "which is possible makes this type of joint attractive "
               "particularly for instrument applications and the type of "
               "joint is becoming more and more popular."))
    b.append(p("The above information has all been based upon the spigot joint "
               "where of the part of the joint not in the plane part of the "
               "joint (which may form the entire flamepath) is cylindrical. "
               "There is no reason why this should not be conical, provided "
               "that the gap is uniform throughout the conical part of the "
               "joint and the conical part of the joint complies with the "
               "requirements of length and gap for a normal spigot joint. "
               "There are, however, restrictions in the case of sub-group IIC "
               "joints and in these cases the taper of the joint (the cone "
               "angle) is required not to exceed 5°. While being a special "
               "case of a spigot joint, these joints are normally referred to "
               "as conical joints."))

    # Printed p.245 - joint type 3.
    b.append(h4("3 Cylindrical joints, operating rod joints, and partial "
                "cylindrical joints",
                "3 Cylindrical joints, operating rod joints, and partial "
                "cylindrical joints"))
    b.append(p("A basic cylindrical joint is no different to a spigot joint "
               "where all of the flamepath is in the cylindrical part of the "
               "joint and the limiting dimensions are contained in Table "
               "10.6. These joints are, however, mainly used for operating "
               "rods and rotating shafts where eccentricity and wear can "
               "become problems. They have, therefore, special requirements "
               "applied to them in such circumstances. The requirements for "
               "shafts will be dealt with in a later section of this chapter "
               "but those for operating rods will be dealt with here."))
    b.append(p("It must be stressed, however, that if the two parts of the "
               "cylindrical joint are firmly fixed, and the joint does not "
               "move or rotate as part of its normal operation, these "
               "requirements do not apply and the joint should be treated as "
               "a spigot joint with all of the flamepath in the cylindrical "
               "part of the joint."))
    b.append(p("In cases where the inner part of the joint is an operating "
               "rod, whereby eccentricity in assembly or due to movement must "
               "be taken into account, the joint gap required must be "
               "achieved even when the rod is at one side of the joint (which "
               "means that when it is central in the hole then the gap around "
               "it must be half of that normally required). In addition, the "
               "length of joint must comply with the required length of joint "
               "for static cylindrical joints given earlier in this chapter, "
               "but must also have a length at least equal to the diameter of "
               "the rod itself where this is less than 25 mm. Where the rod "
               "is in excess of 25 mm diameter, then the joint length "
               "requirements for static cylindrical joints alone apply."))
    b.append(p("If the inner part of the joint is an operating rod and the "
               "joint is subject to wear during the normal operating life of "
               "the enclosure because of the materials of construction "
               "and/or the frequency of operation, then the parts of the "
               "joint must be replaceable. This can be achieved by, for "
               "example, making the outer part of the joint of softer bushing "
               "material and making it replaceable. It is recommended that "
               "the approach is to take the view that wear is possible unless "
               "it can be clearly proved that it is not. In addition, the rod "
               "must not be removable from the outside of the enclosure nor "
               "must it be capable of moving totally inside the enclosure as "
               "either event would remove any flamepath and permit "
               "transmission of an explosion. It is likely that in most cases "
               "the rod will be secured to the necessary degree by the "
               "fixings necessary for its operation inside the enclosure, but "
               "if not then it needs to be secured against removal by "
               "internal fasteners (e.g., circlips or similar)."))
    b.append(p("Partial cylindrical joints are permitted where such things as "
               "plates are used as covers on hollow cylinders, and an example "
               "is shown in Fig. 10.11. This type of joint should be treated "
               "exactly as for a flanged joint where gaps, joint lengths, "
               "gaskets, and introduction of fixing bolts are concerned but, "
               "in this case, a total prohibition of the type of joint for "
               "enclosures intended for sub-group IIC is applied so that, "
               "unlike the other types of joint, partial cylindrical joints "
               "may not be used in enclosures for sub-group IIC. This is "
               "probably because of the greater difficulty in achieving the "
               "coincidence of radius required between the two parts than is "
               "the case with achievement of the necessary flatness for "
               "flanged joints."))

    # Printed p.246 - figure, then text on partial cylindrical joints.
    b.append(fig(11, FB.fig_f1011()))
    b.append(p("It is worthy of note that these joints were not specifically "
               "identified in BS 5501, Part 5 (the first edition of EN 50018). "
               "Their similarity to the flanged joint, however, means that "
               "they were probably so treated by at least some of the "
               "certification bodies involved and may exist in some apparatus "
               "- even that with a volume of less than 500 cm³ intended for "
               "sub-group IIC use. The requirement in BS/EN 50018⁶ (1995) "
               "(the second edition of EN 50018) represents an additional "
               "restriction on the use of such joints. As there has been no "
               "official notice that previous practice is unsafe, however, "
               "this does not require any retrospective remedial action but "
               "it would be wise to favour apparatus to BS/EN 50018⁶ in the "
               "future."))
    b.append(note("<b>Source note.</b> The print carries superscript ⁶ after "
                  "'BS/EN 50018' in both places (reference 6 is BS/EN 50018 "
                  "(1995)); the marker is retained as printed."))
    b.append(p("A capillary can be considered as a cylindrical joint with the "
               "inside diameter equal to 0. Therefore, the maximum gaps "
               "specified in Table 10.6 will become the maximum internal "
               "diameter of the capillary."))

    # Printed p.246-247 - joint type 4, threaded joints.
    b.append(h4("4 Threaded joints", "4 Threaded joints"))
    b.append(p("Joints between parts of flameproof enclosures may also be "
               "threaded. Where this is so the threads involved require "
               "either to be of specific named types with specific qualities "
               "of fit or to be specified, possibly to a lower level of "
               "quality, and be subject to additional requirements when "
               "testing for flame"))
    # Printed p.247 - Tables 10.7-10.8 interrupt the paragraph in mid-sentence.
    b.append(table(T2.HEAD107_EN, T2.ROWS107, T2.CAPTION107_EN))
    b.append(note(T2.NOTE107_EN))
    b.append(table(T2.HEAD108_EN, T2.ROWS108, T2.CAPTION108_EN))
    b.append(note(T2.NOTE108_EN))
    b.append(p("transmission is carried out. As a result, some specifications "
               "can be sacrificed provided that more onerous testing is "
               "carried out. The requirements for threaded joints are "
               "included in Table 10.7 for parallel threads and Table 10.8 "
               "for taper threads. In addition, the following requirements "
               "need to be complied with."))
    b.append(p("Where these threaded joints are used for lids, doors or the "
               "covers of flameproof enclosures, there is always the "
               "possibility that they could be loosened by inexperienced "
               "personnel and, to avoid this, such joints are required to be "
               "secured by fasteners of the same quality and operational "
               "requirements as bolts or screws of flanged and spigot joints. "
               "The typical way this is done with a cover is to fit a cap "
               "screw into the outer part outside"))

    # Printed p.248 - continuation, then italic run-in subheadings.
    b.append(p("the thread, so that when it is tightened it impinges on the "
               "inner part, again outside the thread, preventing loosening of "
               "the joint. The capscrew should be flush with the enclosure "
               "outside when tightened to prevent it being removed with "
               "pliers, etc."))
    b.append(note("<b>Source note.</b> The print uses 'cap screw' in the "
                  "preceding paragraph and 'capscrew' here; both spellings "
                  "are retained."))
    b.append(p("<i>Parallel threads</i>"))
    b.append(p("In respect of parallel threads the following limitations need "
               "to be taken into account. First, parallel threads with a "
               "pitch of less than 0.7 mm are not permitted because of their "
               "fineness which gives rise to shallowness, and the added "
               "possibility of stripping or partial stripping in use with "
               "resultant damage to their flameproof properties."))
    b.append(p("Second, where the threads pitch exceeds 2 mm the combination "
               "of coarse pitch and quality of fit may not be sufficient to "
               "achieve the necessary flameproof qualities and the apparatus "
               "could fail the tests in Table 10.7. In such cases it may be "
               "necessary to increase the number of threads engaged to more "
               "than five. No specific increase can be given as it will "
               "depend upon how much the pitch exceeds 2 mm, but as a starting "
               "point it is suggested that an additional thread be added for "
               "each 0.5 mm by which the thread pitch exceeds 2 mm. "
               "Alternatively, a test could be performed similar to that used "
               "for non-standard threads. These alternatives should be "
               "discussed with the appropriate certification body before "
               "being adopted in any given case."))
    b.append(note("<b>Source note.</b> The print reads 'where the threads "
                  "pitch exceeds 2 mm'; the wording is retained verbatim."))
    b.append(p("Third, where threadforms and/or tolerances other than those "
               "permitted by Table 10.7 are used, the joints will be subjected "
               "to additional requirements which normally take the form of an "
               "increase in thread withdrawal for testing over that used for "
               "complying threads."))
    b.append(p("<i>Taper threads</i>"))
    b.append(p("While taper threads should comply with the requirements of "
               "Table 10.8 it is recognized that, at their limit of tolerance, "
               "the number of threads engaged may be less than five."))
    b.append(p("<i>Securing of threaded joints</i>"))
    b.append(p("Unlike flanged, spigot and cylindrical joints, it is not "
               "usually possible to secure this joint easily, as it needs to "
               "rotate in order to ensure it is fully made. It is, however, a "
               "screw similar to fastening devices and, provided that it "
               "needs a hexagon spanner or hexagon key for its removal, and "
               "should not have any protrusions which would make alternative "
               "opening possible, then it can be accepted as secured once it "
               "is fully screwed home. If there is doubt as to the quality of "
               "securing, then a socket-headed cap screw in the cylindrical "
               "assembly outside the joint threaded into the outside member "
               "of the joint, outside the thread forming the flamepath, will "
               "be adequate for securing purposes. This will elongate the "
               "cylinder only slightly. In the case of lids, doors and covers "
               "the additional screw is always considered"))

    # Printed p.249 - continuation, then joint type 5.
    b.append(p("necessary and it would be wise to utilize this approach in "
               "all cases to avoid problems due to differing views."))
    b.append(h4("5 Cemented joints", "5 Cemented joints"))
    b.append(p("Cemented joints are often used to insert such things as "
               "viewing ports into flameproof enclosures and it is often "
               "difficult to create a joint complying with joint requirements. "
               "In such circumstances, a joint may be made using cement and "
               "may be significantly shorter than its normal counterpart, "
               "needing only to comply with the length requirements of Table "
               "10.9."))
    b.append(p("Where the joint would comply with the requirements for "
               "flanged, spigot, cylindrical or threaded joints in the "
               "absence of the cement, including the securing needs of such "
               "joints, then no special requirements apply other than the "
               "leakage test to ensure the completeness of the cement seal, "
               "as neither the strength of the joint or its flameproof "
               "performance rely on the cement. (It is necessary to ensure "
               "that the cement seal allows no jets to cause abnormal "
               "flameproof performance and a sealing test is included in "
               "BS/EN 50018 (1995). In addition, the strength of the joint "
               "must not rely on the cement, and removal and replacement of "
               "the joint must be possible without damage to the cement. This "
               "can be achieved by making the cemented joint as a cartridge "
               "and its insertion into a further joint of more normal design "
               "the method of replacement. Where the joint forms part of the "
               "enclosure, however, and removal is not intended, then no "
               "additional action is necessary."))
    b.append(note("<b>Source note.</b> The print reads 'neither the strength "
                  "of the joint or its flameproof performance rely on the "
                  "cement'; the non-standard 'or' (for 'nor') is retained "
                  "verbatim."))
    b.append(table(T2.HEAD109_EN, T2.ROWS109, T2.CAPTION109_EN))
    b.append(note(T2.NOTE109_EN))
    b.append(p("Where the joint does not conform to the requirements of other "
               "joint types in the absence of the cement, but only to the "
               "length requirements of Table 10.9, an arrangement must be in "
               "place to ensure that the joint strength does not rely on the "
               "cement. Additionally, in these circumstances, the cement must "
               "not be damaged by the thermal resistance to heat and cold "
               "tests specified in BS/EN 50014 (1994)¹² (see also, Chapter "
               "7)."))
    b.append(note("<b>Source note.</b> The print carries superscript ¹² after "
                  "'BS/EN 50014 (1994)'; the marker is retained as printed."))

    # Printed p.250 - 10.2.2 and Fig. 10.12.
    b.append(h4("10.2.2 Joints for rotary or longitudinal shafts and "
                "operating rods",
                "10.2.2 Joints for rotary or longitudinal shafts and "
                "operating rods"))
    b.append(p("Operating rods which pass through the walls of flameproof "
               "enclosures move in a longitudinal or rotary direction. In "
               "either case, cylindrical joints are appropriate as the use "
               "of flanged or spigot joints is not easily applicable. Although "
               "one could identify a situation where the use of a simple "
               "spigot joint (one where the flamepath is totally in the "
               "cylindrical part of the joint) may be possible, the securing "
               "of the joint would produce real problems. Where movement is "
               "only in the rotary direction it could be argued that a "
               "further specialist type of joint is also suitable. This is "
               "the labyrinth joint shown in Fig. 10.12. This joint is like a "
               "cylindrical joint except that the flamepath is via a set of "
               "interleaved cylindrical parts. If this specialist joint is "
               "used it would be wise to ensure that any certification body "
               "involved would accept it, as the way in which the Standard is "
               "written could be taken as excluding it depending upon how it "
               "is interpreted."))
    b.append(p("Where a cylindrical joint is used in this configuration, it "
               "must satisfy special requirements as one part of it moves and "
               "some wear must be assumed. While it needs to have a minimum "
               "joint length and maximum gap complying with Table 10.6, the "
               "length of the joint must also relate to the size of the "
               "operating rod which forms the moving part of the joint, and "
               "the joint length is, to a degree, determined by the "
               "circumference of the rod. It must, in addition to complying "
               "with Table 10.6, have a length at least equal to the diameter "
               "of the operating rod, up to a rod diameter of 25 mm."))
    b.append(fig(12, FB.fig_f1012()))

    # Printed p.251 - continuation and Table 10.10.
    b.append(p("Also, where the rod does not have a supporting bearing, other "
               "than the fixed part of the joint and significant wear of the "
               "joint in normal operation is expected, the fixed part of the "
               "joint should form a replaceable bushing so that the joint can "
               "be renewed with ease when necessary."))
    b.append(p("If the labyrinth-type joint (see Fig. 10.12) is considered to "
               "be appropriate a relaxation is permitted and these limits "
               "need not be complied with in the case of this joint, provided "
               "that it can be shown to be flameproof using the tests in "
               "BS/EN 50018, although it would be wise to ensure a joint "
               "minimum length and maximum gap in accordance with Table 10.6 "
               "with further allowance made for shaft diameter. This "
               "relaxation is possible because of the geometry of the joint, "
               "which is more likely to prevent flame transmission than its "
               "cylindrical counterpart."))
    b.append(p("To avoid joint wear in both types of joint, the rod may be "
               "fitted with a bearing which does not form part of the joint "
               "but keeps the rod away from the joint surface, effectively "
               "preventing wear. Two types of bearing are acceptable in "
               "principle, the sleeve bearing, where the outer part of the "
               "bearing is static, and the rolling element bearing, which "
               "introduces rolling elements between the rod and the "
               "enclosure. In both cases the minimum radial clearance between "
               "the moving part of the joint and the fixed part of the joint "
               "should not be less than 0.05 mm taking account of tolerances. "
               "In the case of the cylindrical joint the maximum radial "
               "clearance must not exceed that specified in Table 10.10 for "
               "sleeve bearings, and Table 10.11 for rolling element bearings "
               "for the length of joint in question but, as there is a "
               "relaxation in the case of the labyrinth joint, in cases where "
               "this type of joint is acceptable, no maximum limit of radial "
               "clearance is specified. The only requirement is the passing "
               "of the flame transmission tests. The use of a sleeve bearing "
               "for any joint associated with a rotating electrical machine "
               "is limited to sub-group IIA and IIB only."))
    b.append(table(T2.HEAD1010_EN, T2.ROWS1010, T2.CAPTION1010_EN))
    b.append(note(T2.NOTE1010_EN))

    # Printed p.252 - Table 10.11, floating joint, 10.2.3 opening.
    b.append(table(T3.HEAD1011_EN, T3.ROWS1011, T3.CAPTION1011_EN))
    b.append(note(T3.NOTE1011_EN))
    b.append(p("It is possible to use a combination of a cylindrical joint "
               "(or labyrinth joint where such a joint is acceptable) and a "
               "flanged joint to make a floating joint so that some latitude "
               "of lateral movement is permitted (see Fig. 10.13). In such "
               "cases, the length of the flange should be at least that "
               "required by Table 10.1 plus an amount equal to the maximum "
               "lateral movement expected in operation. Such joints should "
               "also be secured against rotation and are limited to "
               "enclosures intended for use in sub-group IIA and IIB."))
    b.append(note("<b>Figure-reference note.</b> Figure reference as printed "
                  "(apparently swapped in the original): the floating joint "
                  "is drawn in Fig. 10.14, while 'k' is defined in Fig. "
                  "10.13."))
    b.append(h4("10.2.3 Joints for shafts and rotating machines",
                "10.2.3 Joints for shafts and rotating machines"))
    b.append(p("A rotating shaft is a special case. Due to the rotation it is "
               "often unwise to have the flameproof joint forming the shaft "
               "support and a bearing is used."))
    return "".join(b)
