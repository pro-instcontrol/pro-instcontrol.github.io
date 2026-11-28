# -*- coding: utf-8 -*-
"""Chapter 13, module C - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 363-378 (PDF pp. 384-399).

Covers the tail of 13.7 (cells/batteries, semiconductors, connectors,
soldered joints, external terminals, piezo devices and relays), 13.8
component and circuit failure modes, and the opening of 13.9 apparatus
construction requirements. Figures 13.13-13.18 and Table 13.7 sit at their
printed positions. The chapter shell owns the chapter h2, the printed
references, the glossary, the source-quirk note and the copyright.

Printed quirks are kept in the English text and bilingual notes are added
for every divergence listed in survey C section 6; the Vietnamese follows
the intended meaning. The survey ends mid-sentence on printed p.378 and
that unfinished sentence is carried forward exactly as printed. This is an
unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, eq, note, table, fig
import mcmillanfig13_c as FC
import mcmillan_tbl13_5_8 as T2


def body_vi():
    b = []

    # C1 (printed p.363 / PDF p.384, raw 15814-15837; continues from module B).
    b.append(note("<b>Lưu ý về ký tự dòng tiêu đề chạy.</b> Các trang in chẵn "
                  "mang dòng tiêu đề 'Protection concept intrinsic safety "
                  "‘i’ NNN' với một dấu nhấc nhỏ lạ sau dấu ngoặc kép đóng; "
                  "lớp văn bản chỉ ghi '‘i’'. Dấu ngoặc kép kiểu cong được "
                  "giữ nguyên và dấu lạ chỉ được ghi nhận, không tái tạo."))
    b.append(note("<b>Lưu ý về dấu ngoặc không được đóng trong bản in.</b> "
                  "Câu 'Charging terminals ... must be enclosed to IP20 "
                  "(BS/EN 60529¹⁵ and in these circumstances ...' không bao "
                  "giờ đóng dấu ngoặc mở đã mở. Cách ghi này được giữ nguyên "
                  "trong bản tiếng Anh, còn bản tiếng Việt theo nghĩa đúng."))
    b.append(p("Mặc dù việc ngắn mạch bên trong của cell và ắc quy thỏa mãn "
               "các yêu cầu nêu trên không được coi là nằm trong vùng nguy "
               "hiểm cho mục đích đánh lửa do tia lửa, nhưng ngắn mạch bên "
               "ngoài thì có. Cần đảm bảo rằng dòng chảy qua là an toàn nội "
               "tại, và phương pháp làm điều này là đảm bảo sự tách biệt "
               "giữa các cực của cell hoặc ắc quy là không thể hỏng, hoặc "
               "không được coi là chịu sự cố, rồi đưa các thiết bị hạn chế "
               "dòng điện mắc nối tiếp với một hoặc cả hai cực, hạn chế dòng "
               "ngắn mạch tới mức an toàn nội tại. Các thiết bị hạn chế dòng "
               "này cần được bao bọc hoặc đóng khuôn cùng với cell hoặc ắc "
               "quy nếu định thay đổi chúng trong vùng nguy hiểm hoặc, nếu "
               "không phải vậy, cell hoặc ắc quy cần nằm trong vỏ bọc bắt "
               "chặt bằng các chốt đặc biệt như mô tả trong Chương 5, và khi "
               "đó cần có cảnh báo để đảm bảo chúng chỉ được thay đổi ở vùng "
               "không nguy hiểm. Các cực sạc cho cell hoặc ắc quy có thể sạc "
               "lại phải được bao bọc đạt IP20 (BS/EN 60529¹⁵ và trong "
               "những trường hợp đó việc sạc lại phải diễn ra ở vùng không "
               "nguy hiểm. Ngoài ra, các cực sạc có thể được bảo vệ bằng "
               "đi-ốt (hai cho ‘ib’ và ba cho ‘ia’) ngăn không cho lấy dòng "
               "ra khỏi chúng, hoặc bằng một điện trở không thể hỏng tạo "
               "thành một mạch an toàn nội tại. Trong những trường hợp này, "
               "nếu việc sạc được thực hiện bằng một bộ sạc có đầu ra không "
               "an toàn nội tại, các đi-ốt hoặc điện trở phải được bảo vệ "
               "bằng một cầu chì ngăn dòng quá tải chảy trong quá trình sạc "
               "và, nếu cầu chì mang dòng bình thường (tức là nằm cả trong "
               "mạch xả lẫn mạch sạc), nó nên được đóng khuôn để ngăn khí "
               "quyển nổ tiếp cận phần tử của nó. Khi đầu ra của bộ sạc "
               "không an toàn nội tại, việc sạc chỉ nên được thực hiện ở "
               "vùng không nguy hiểm."))

    # C2 - italic spot heading, printed p.363 (see survey section 2).
    b.append(h4("Thiết bị bán dẫn (đi-ốt, đi-ốt zener, thyristor, bóng bán "
                "dẫn, mạch tích hợp v.v.)",
                "Semiconductor devices (diodes, zener diodes, thyristors, "
                "transistors, integrated circuits etc.)"))
    b.append(note("<b>Lưu ý về dấu câu ở tiêu đề không đánh số.</b> "
                  "'Semiconductor devices (... etc.)' và 'Internal connectors "
                  "(... etc.)' có dấu chấm bên trong dấu ngoặc đóng, trong "
                  "khi 'Connectors for external connections (... etc)' và "
                  "'13.9.2 Internal layout (... etc)' thì không. Sự không "
                  "nhất quán này được giữ nguyên theo bản in."))

    # C3 (printed p.363 / PDF p.384, raw 15840-15855).
    b.append(p("Hỏng hóc của các thiết bị bán dẫn được chọn đúng định mức "
               "thường được coi là một sự cố đếm được nhưng do bản chất của "
               "chúng, chúng phải được chứng minh là chịu được các xung quá "
               "tải. Trong trường hợp thiết bị liên kết, khi thiết bị này "
               "được cấp nguồn từ hoặc nối khác với nguồn điện lưới, các "
               "dòng xung tạm thời xảy ra được xác định bởi lưới điện và, ở "
               "mức xấu nhất, các dòng này sẽ là giá trị đỉnh của điện áp "
               "lưới chia cho bất kỳ điện trở nối tiếp không thể hỏng nào "
               "hiện có trong mạch giữa lưới và thiết bị bán dẫn. Vì vậy, "
               "các chất bán dẫn phải có khả năng chịu được các xung điện "
               "áp và dòng điện đáng kể mà không bị hư hại, ngay cả khi có "
               "một máy biến áp không thể hỏng được đưa vào mạch để cung "
               "cấp điện áp thấp làm nguồn cho mạch an toàn nội tại. Đây là "
               "một yêu cầu nặng nề nhưng chỉ áp dụng cho những thiết bị "
               "bán dẫn mà an toàn nội tại phụ thuộc vào, chẳng hạn như các "
               "thiết bị hạn chế điện áp song song, v.v. Sau khi ra khỏi "
               "thiết bị liên kết, các xung tạm thời có thể được bỏ qua vì "
               "người ta giả định rằng chúng sẽ bị triệt tiêu ở mức lớn "
               "trong thiết bị liên kết và phần còn lại sẽ không gây ra "
               "vấn đề gì."))

    # C4 (printed p.364 / PDF p.385, raw 15858-15864).
    b.append(p("Ngoài ba đi-ốt được phép dùng để chặn trong mạch ‘ia’, các "
               "chất bán dẫn dùng để hạn chế nối tiếp chỉ được dùng trong "
               "mạch ‘ib’ vì chúng cho các xung tạm thời đi qua, điều này "
               "rất đáng lo ngại trong các mạch đi vào Vùng 0 do sự hiện "
               "diện liên tục của khí quyển nổ và khả năng chúng cho qua "
               "một xung tạm thời ngắn có khả năng đánh lửa, trong trường "
               "hợp đó xung sẽ trùng với sự có mặt của khí quyển nổ, khác "
               "với trường hợp ở Vùng 1 nơi sự trùng hợp này ít có khả năng "
               "xảy ra hơn."))

    # C5 (printed p.364 / PDF p.385, raw 15865-15874).
    b.append(p("Khi chất bán dẫn được dùng làm thiết bị hạn chế điện áp song "
               "song, chúng chỉ có thể bao gồm các bóng bán dẫn nối đi-ốt "
               "(ví dụ, những bóng được nối để chúng ở trạng thái dẫn hoàn "
               "toàn hoặc ngắt hoàn toàn), thyristor, đi-ốt zener và các "
               "thiết bị tương tự. Chúng phải có định mức dòng thuận bằng "
               "1.5 lần dòng lớn nhất có thể chảy, kể cả trong điều kiện "
               "sự cố nếu chúng bị ngắn mạch. Yêu cầu này cũng áp dụng cho "
               "đi-ốt zener và được xác định bằng cách xem xét giới hạn "
               "dòng khi đi-ốt được dùng theo hướng thuận (cực tính ngược "
               "với hướng zener). Đi-ốt zener cũng cần làm việc ở mức không "
               "quá hai phần ba công suất tiêu tán zener tối đa định mức "
               "khi được vận hành trong mạch như các đi-ốt zener với các "
               "sự cố áp dụng trong mạch."))

    # C6 (printed p.364 / PDF p.385, raw 15875-15882).
    b.append(p("Việc sử dụng các chất bán dẫn có thể điều khiển, chẳng hạn "
               "như bóng bán dẫn, bộ điều chỉnh điện áp và thyristor, nhìn "
               "chung chỉ giới hạn trong mạch ‘ib’, trừ trường hợp cả mạch "
               "vào và mạch ra đều an toàn nội tại, hoặc có thể chứng minh "
               "rằng không phát sinh xung tạm thời từ nguồn cấp. Trong các "
               "mạch đó, hai thiết bị song song được coi là không thể hỏng, "
               "ngay cả trong mạch ‘ia’. Ngoài ra, ngay cả khi có thể phát "
               "sinh xung tạm thời, ba thyristor song song được chấp nhận "
               "trong mạch ‘ia’ nếu chúng chịu được các xung đó và năng "
               "lượng vượt qua của chúng bị giới hạn ở các giá trị sau khi "
               "chúng hoạt động:"))

    # C7 - displayed let-through energy list (printed p.364, raw 15883-15885).
    b.append(eq("IIA = 160 μJ<br>IIB = 80 μJ<br>IIC = 20 μJ"))
    b.append(note("<b>Lưu ý về danh sách năng lượng vượt qua.</b> Lớp văn "
                  "bản thô ghi 'IIB = WpJ' nhưng trang in cho thấy "
                  "'IIB = 80 μJ'; giá trị trên trang in được dùng, cùng với "
                  "'IIA = 160 μJ' và 'IIC = 20 μJ'."))

    # C8 - italic spot heading, printed p.364 (see survey section 2).
    b.append(h4("Đầu nối bên trong (cọc đấu nối, thẻ cắm, phích cắm và ổ cắm, "
                "v.v.)",
                "Internal connectors (terminals, plug-in cards, plugs and "
                "sockets, etc.)"))
    b.append(note("<b>Lưu ý về tên tiêu chuẩn trong BS/EN 50020.</b> Lớp văn "
                  "bản thô ghi 'BS/EN 5O02O1O' với chữ O hoa thay số 0; "
                  "trang in cho thấy 'BS/EN 50020¹⁰' với số 10 ở dạng mũ. "
                  "Số tham chiếu dạng mũ được giữ nguyên."))

    # C9 (printed p.364 / PDF p.385, raw 15887-15894).
    b.append(p("Nhìn chung, không có yêu cầu nào về chất lượng của các phần "
               "tử đấu nối của đầu nối bên trong ngoài các yêu cầu áp dụng "
               "cho sử dụng công nghiệp bình thường, và hỏng của các phần "
               "tử đấu nối thành điện trở cao hoặc mạch hở được coi là một "
               "sự cố đếm được. Trường hợp hỏng thành điện trở cao rõ ràng "
               "sẽ có vấn đề tiềm ẩn về nhiệt độ, nhưng các yêu cầu của "
               "khái niệm bảo vệ trong BS/EN 50020¹⁰ nêu rõ rằng cấp nhiệt "
               "độ T6 phải được áp dụng cho các thiết bị như vậy, do đó "
               "không cần đánh giá thêm về điểm này. Lý do là vì kinh "
               "nghiệm về hỏng hóc ở các đầu nối như vậy cho thấy sự cố "
               "thường là mạch hở hoặc điện trở rất cao, và khả năng tiêu "
               "tán công suất đáng kể trong đầu nối như vậy được coi là "
               "cực kỳ nhỏ."))

    # C10 (printed p.365 / PDF p.386, raw 15897-15914; continues on p.366).
    b.append(p("Khi có một đầu nối trong một thiết bị, bố trí phải sao cho "
               "không thể nối ngược nếu cách nối đó ảnh hưởng xấu đến an "
               "toàn nội tại. Sự an toàn cần thiết thường đạt được bằng "
               "cách khóa đầu nối để nó chỉ lắp được một chiều và hầu hết "
               "các phích cắm và ổ cắm thương mại được cấu hình theo cách "
               "đó. Với đầu nối bo mạch in, cách khóa thường là thay một "
               "trong các đầu nối bằng một khe trên bo mạch và bịt một vị "
               "trí ổ cắm trong ổ (xem Hình 13.13). Rõ ràng nếu không phải "
               "như vậy thì việc nối ngược không quan trọng, trừ lý do vận "
               "hành, nhưng những lý do đó có thể vẫn đòi hỏi cùng các biện "
               "pháp phòng ngừa. Nếu thiết bị chứa nhiều hơn một đầu nối, "
               "không được cho phép sự trao đổi lẫn nhau giữa các đầu nối "
               "khi điều đó có thể ảnh hưởng xấu đến an toàn nội tại. Khóa "
               "hoặc cách tiếp cận tương tự là cách tối ưu cho cả việc nối "
               "sai một đầu nối và sự trao đổi ngoài ý muốn giữa các đầu "
               "nối. Người ta thừa nhận rằng cách tiếp cận như vậy không "
               "phải lúc nào cũng kinh tế, và việc nhận diện các đầu nối "
               "để làm rõ nối sai, ví dụ bằng một dạng mã hóa màu, được coi "
               "là giải pháp thay thế. Khi các đầu nối mang các nối đất cần "
               "thiết để cung cấp an toàn nội tại, các tiếp điểm cần được "
               "nhân đôi cho ‘ib’"))
    b.append(note("<b>Lưu ý về dấu chấm bị thiếu ở cuối trang in 365.</b> "
                  "Đoạn trên kết thúc bằng '...cho ‘ib’' không có dấu chấm; "
                  "câu tiếp tục ở trang in 366 bằng 'và nhân ba cho ‘ia’...'. "
                  "Hai nửa được giữ như một câu liên tục."))
    b.append(note("<b>Lưu ý về lỗi gạch nối trong lớp văn bản thô.</b> Lớp "
                  "văn bản thô cho một dạng méo của 'connectors' (có một ký "
                  "tự lạ ở giữa); trang in cho thấy 'connectors'. Cách đọc "
                  "theo trang in được dùng."))

    # Fig. 13.13 - printed p.365 (PDF p.386), after C10.
    b.append(fig(13, FC.fig_f1313()))
    b.append(note("<b>Lưu ý về số hiệu chú thích của Hình 13.13.</b> Lớp văn "
                  "bản thô ghi 'Fig. 13.1 3' với một dấu cách lạc; trang in "
                  "cho thấy 'Fig. 13.13'. Chú thích của hình được lấy theo "
                  "bản in."))
    b.append(note("<b>Lưu ý về nhãn trong hình 'Out out'.</b> Mũi tên chỉ "
                  "đầu nối có chốt định vị mang nhãn 'Out out' trong bản in "
                  "(viết thường trong lớp văn bản thô). Nhãn này được giữ "
                  "nguyên trong hình, không suy diễn ý nghĩa."))

    # Fig. 13.14 - printed p.366 (PDF p.387), at top of page before C11.
    b.append(fig(14, FC.fig_f1314()))
    b.append(note("<b>Lưu ý về các nhãn trong Hình 13.14.</b> Lớp văn bản thô "
                  "làm méo các nhãn phía trên; trang in cho hai nhãn số ít "
                  "'Joint not subject to fault (infallible)' ở bên trái, hai "
                  "nhãn số nhiều 'Joints not subject to fault (infallible)' "
                  "ở bên phải, 'Pins and sockets' (số nhiều) bên trái và "
                  "'Pin and socket' (số ít) bên phải; các nối đất từ trái "
                  "sang phải là 1, 3, 2. Cách đọc theo trang in được giữ."))

    # C11 - continuation of C10 (printed p.366, raw 15938-15943).
    b.append(p("và nhân ba cho ‘ia’ theo cách đạt được các mục tiêu thể hiện "
               "trong Hình 13.14. Ngoài ra, trong trường hợp đầu nối nối "
               "tiếp tuyến tính chẳng hạn như loại dùng cho bo mạch in, khi "
               "việc rút ra có thể ở một góc, các kết nối cần được phân bố "
               "dọc theo đầu nối để đảm bảo ít nhất một trong số chúng vẫn "
               "tiếp xúc cho đến khi đầu nối được rút hoàn toàn. Điều này "
               "đòi hỏi một kết nối ở (hoặc rất gần) mỗi đầu của đầu nối."))

    # C12 (printed p.366 / PDF p.387, raw 15944-15948).
    b.append(p("Các cọc đấu nối không cần tuân thủ yêu cầu nào khác ngoài "
               "các yêu cầu áp dụng cho sử dụng công nghiệp và, giống như "
               "đầu nối, chúng sẽ được coi là hỏng thành điện trở rất cao "
               "hoặc mạch hở như một sự cố đếm được duy nhất. Do đó, chúng "
               "sẽ được xem xét về cấp nhiệt độ theo cách giống như đầu nối "
               "và sẽ là T6."))

    # C13 - italic spot heading, printed p.366.
    b.append(h4("Mối hàn", "Soldered joints"))

    # C14 (printed p.366 / PDF p.387, raw 15950-15951; continues on p.367).
    b.append(p("Không có yêu cầu cụ thể nào đối với mối hàn và các mối hàn "
               "thông thường chỉ được coi là hỏng như một sự cố đếm được. "
               "Nhiệt độ"))

    # C15 - continuation of C14 (printed p.367, raw 15954-15958).
    b.append(p("cấp của các mối nối đó sẽ, như đối với cọc đấu nối và các "
               "đầu nối khác, được coi là T6. Khi một dây bị bung ra do hỏng "
               "mối hàn nối dây đó với bất kỳ bộ phận dẫn điện nào khác "
               "trong phạm vi dịch chuyển kết quả của nó, dây đó sẽ, như "
               "các dây bị ngắt kết nối khác, được coi là một sự cố đếm "
               "được thứ hai."))

    # C16 - italic spot heading, printed p.367.
    b.append(h4("Đầu nối dùng cho kết nối bên ngoài (cọc đấu nối, phích cắm "
                "và ổ cắm, v.v)",
                "Connectors for external connections (terminals, plugs and "
                "sockets, etc)"))

    # C17 (printed p.367 / PDF p.388, raw 15960-15964).
    b.append(p("Các cọc đấu nối dùng để nối mạch bên ngoài phải tuân thủ "
               "các yêu cầu đối với cọc dùng bên trong và, bổ sung thêm, "
               "phải tuân thủ các yêu cầu sau. Thứ nhất, chúng phải có "
               "khoảng cách giữa các cọc với nhau và giữa chúng với bất kỳ "
               "nối đất nào ít nhất bằng các số liệu đã cho về đường bò, "
               "khoảng hở và khoảng tách cần thiết để có thể bỏ qua sự nối "
               "liên kết."))

    # C18 (printed p.367 / PDF p.388, raw 15965-15968).
    b.append(p("Thứ hai, chúng phải được tách biệt với nhau ít nhất 6 mm và "
               "với đất ít nhất 3 mm (khoảng cách đang xét được đo như thể "
               "hiện trong Hình 13.15) khi tất cả các mạch đang xét đều là "
               "mạch an toàn nội tại, và cách ít nhất 50 mm so với các mạch "
               "không an toàn nội tại."))

    # C19 (printed p.367 / PDF p.388, raw 15969-15976).
    b.append(p("Thứ ba, bất kỳ vách ngăn nào dùng để hỗ trợ tách biệt phải "
               "dày ít nhất 0.9 mm nếu làm bằng vật liệu cách điện và dày "
               "0.45 mm nếu làm bằng kim loại. Trong cả hai trường hợp, "
               "vách ngăn phải vượt qua thử nghiệm áp dụng lực ngang 30 N "
               "để xác định độ cứng của chúng và, nếu bằng kim loại, phải "
               "được nối đất hoặc có độ dày đủ để chứng minh rằng không xảy "
               "ra cháy thủng trong trường hợp sự cố. Ngoài ra, nối đất của "
               "chúng phải được thực hiện sao cho loại trừ được khả năng "
               "mất nối đất. Nếu điều này đạt được bằng một nối đất riêng "
               "thay vì việc chúng là một phần của khung nối đất, thì kết "
               "nối đó phải thỏa mãn yêu cầu đối với kết nối không thể hỏng."))

    # C20 (printed p.367 / PDF p.388, raw 15977-15979).
    b.append(p("Cuối cùng, khi dùng vách ngăn, có thể miễn khoảng cách 50 mm "
               "nếu các vách ngăn được bố trí sao cho khoảng cách giữa các "
               "đầu mút của chúng với thành và nắp của vỏ bọc nằm trong "
               "vòng 1.5 mm."))

    # C21 (printed p.367 / PDF p.388, raw 15980-15984).
    b.append(p("Vấn đề cháy thủng không phải là vấn đề thực sự đối với hầu "
               "hết các mạch vì mức tiêu thụ công suất của chúng thấp đến "
               "mức độ dày tối thiểu nêu trên là đủ. Tuy nhiên, cần xem xét "
               "cẩn thận vấn đề này trong các mạch dùng năng lượng cao, "
               "chẳng hạn như các mạch liên quan đến một số tiếp điểm ngõ "
               "ra của rơ-le trong thiết bị liên kết."))
    b.append(note("<b>Lưu ý về lỗi chính tả in 'hgh'.</b> Bản in ghi '...in "
                  "circuits which use hgh energy...'; 'hgh' có trong bản "
                  "gốc, không phải lỗi OCR, và được giữ nguyên trong bản "
                  "tiếng Anh. Bản tiếng Việt dịch theo nghĩa đúng là 'cao'."))

    # C22 (printed p.367 / PDF p.388, raw 15985-15994).
    b.append(p("Bản thân các cọc đấu nối phải thỏa mãn yêu cầu công nghiệp "
               "thông thường nhưng cũng phải thỏa mãn các yêu cầu bổ sung "
               "khi dùng để nối các nối đất quan trọng cho an toàn nội tại. "
               "Chúng không được có cạnh sắc nào có thể làm hỏng hoặc cắt "
               "đứt dây đã nối và không được dựa vào vật liệu cách điện để "
               "truyền lực ép cần thiết nhằm đảm bảo kẹp chặt dẫn. Khi dùng "
               "dây bọc sợi mà không có đầu ép ống, cần đưa một tấm ép giữa "
               "vít cọc và dây để đảm bảo kết nối tốt mà không làm hỏng các "
               "sợi dây, và nếu kích thước dẫn tối đa cho phép của chúng "
               "nhỏ hơn 4 mm² thì chúng phải được bố trí sao cho cũng có "
               "thể kẹp hiệu quả các dẫn nhỏ hơn."))

    # Fig. 13.15 - printed p.368 (PDF p.389), before C23.
    b.append(fig(15, FC.fig_f1315()))
    b.append(note("<b>Lưu ý về các dấu '≥' trong Hình 13.15.</b> Lớp văn bản "
                  "thô ghi '2 6 mm' và '2 50mm'; trang in cho thấy '≥ 6 mm' "
                  "và '≥ 50 mm' trong chú thích, cùng 'd ≥ 3', 'd ≥ 6', "
                  "'d ≥ 6 mm' trong hình. Dấu '≥' được giữ; lưu ý là một "
                  "phần của chú thích in, không phải dòng ghi chú riêng."))

    # C23 (printed p.368 / PDF p.389, raw 16000-16005).
    b.append(p("Phích cắm và ổ cắm cần tuân thủ các yêu cầu như phích cắm và "
               "ổ cắm bên trong về kết cấu và khả năng thay thế lẫn nhau "
               "và, bổ sung thêm, các phương tiện đấu dây vào phích cắm và "
               "ổ cắm nên tuân thủ các yêu cầu như đối với cọc đấu nối, trừ "
               "khi có biện pháp phòng ngừa đặc biệt khi kết thúc dây trong "
               "phích cắm hoặc ổ cắm, hoặc cáp được gắn trong quá trình chế "
               "tạo."))

    # C24 - italic spot heading, printed p.368.
    b.append(h4("Thiết bị áp điện", "Piezo electric devices"))

    # C25 (printed p.368 / PDF p.389, raw 16007-16008; continues on p.369).
    b.append(p("Thiết bị áp điện tương đối đặc biệt ở chỗ chúng có khả năng "
               "chuyển hóa ứng suất cơ thành tín hiệu điện. Vì lý do này "
               "chúng có thể"))

    # C26 - continuation of C25 (printed p.369, raw 16011-16017).
    b.append(p("cộng thêm vào năng lượng điện trong một mạch an toàn nội tại. "
               "Năng lượng điện có thể phát sinh được đo bằng cách cho các "
               "bộ phận bên ngoài của thiết bị mà chúng được lắp vào chịu "
               "các thử nghiệm va đập thường dùng để xác định độ bền (xem "
               "Chương 8), và ghi lại điện áp cực đại phát sinh trong thiết "
               "bị trong quá trình thử va đập đó. Nếu sau đó đo điện dung "
               "của các thiết bị này, năng lượng ngõ ra cực đại có thể được "
               "tính từ:"))

    # C27 - displayed formula, where-block and energy limits (printed p.369).
    b.append(eq("e = 0.5CV²x                                              μJ"))
    b.append(p("where   e = năng lượng phát sinh                          J<br>"
               "        C = điện dung                                   μF<br>"
               "        V = điện áp cực đại phát sinh                     V"))
    b.append(p("Năng lượng này không được vượt quá các giá trị cực đại sau:"))
    b.append(eq("IIA = 950 μJ<br>IIB = 250 μJ<br>IIC = 50 μJ"))
    b.append(note("<b>Lưu ý về công thức áp điện.</b> Bản in viết "
                  "'e = 0.5CV²x' với một chữ 'x' nhỏ sau V² (có thể là dấu "
                  "nhân lạc) và đơn vị 'μJ' ở đầu bên phải dòng; các đơn vị "
                  "trong khối giải thích là 'J', 'μF' và 'V'. Chữ 'x' cuối "
                  "được giữ nguyên, không sửa thành 'e = 0.5CV²'."))

    # C28 (printed p.369 / PDF p.390, raw 16026-16031).
    b.append(p("Có thể lắp các tấm che để giảm ảnh hưởng của va đập trong "
               "trường hợp này nhưng chúng không được bị hư hại theo cách "
               "làm giảm hiệu quả của chúng do va đập nếu được dùng như "
               "vậy. Ngoài ra, trong những trường hợp đặc biệt, thiết bị có "
               "thể được coi là không chịu các va đập đó nhưng trong những "
               "trường hợp như vậy điều cần thiết là người sử dụng phải "
               "được thông báo rõ ràng về những gì phải đạt được trong bất "
               "kỳ lắp đặt nào để đạt được điều đó."))

    # C29 - italic spot heading, printed p.369.
    b.append(h4("Rơ-le", "Relays"))

    # C30 (printed p.369 / PDF p.390, raw 16033-16048).
    b.append(p("Kết cấu của rơ-le quan trọng khi chúng được dùng để tách các "
               "phần của cùng một mạch an toàn nội tại, tách các mạch an "
               "toàn nội tại riêng biệt, hoặc tách mạch an toàn nội tại khỏi "
               "mạch không an toàn nội tại. Các nối liên kết giữa cuộn dây "
               "và tiếp điểm và giữa tiếp điểm với tiếp điểm khác có thể "
               "quan trọng và được đề cập trong Mục 13.6 và 13.7. Tuy nhiên, "
               "có những giới hạn thiết kế trong trường hợp rơ-le mà cuộn "
               "dây nằm trong mạch an toàn nội tại và tiếp điểm nằm trong "
               "mạch không an toàn nội tại, hoặc rơ-le có hai bộ tiếp điểm, "
               "mỗi bộ thuộc một loại mạch. Những giới hạn này được xác "
               "định bởi nhu cầu đảm bảo sự ion hóa phát sinh do đánh lửa "
               "không gây vấn đề và như sau. Thứ nhất, các tiếp điểm trong "
               "mạch không an toàn nội tại nhìn chung không nên đóng cắt "
               "mạch làm việc ở điện áp trên 250 V rms với công suất định "
               "mức lớn hơn 100 VA và dòng đã đóng cắt không nên vượt quá "
               "5 Arms. Thứ hai, các số liệu này có thể tăng lên 10 A rms và "
               "500 VA, nhưng khi không được phép xảy ra đánh thủng, khoảng "
               "cách giữa cuộn dây và tiếp điểm hoặc giữa hai bộ tiếp điểm "
               "phải được tăng so với các giá trị trong Bảng 13.7 lên hệ "
               "số 4."))
    b.append(note("<b>Lưu ý về cách viết '5 Arms'.</b> Đoạn về rơ-le in giới "
                  "hạn dòng đóng cắt là '5 Arms' không có dấu cách, trong "
                  "khi cùng đoạn đó lại in '250 V rms', '10 A rms' và "
                  "'500 VA' có dấu cách. Cách viết được giữ theo bản in."))

    # Table 13.7 - printed p.370 (PDF p.391), before C31.
    b.append(table(T2.HEAD137_VI, T2.ROWS137_VI, T2.CAPTION137_VI))
    b.append(note(T2.NOTE137_VI))
    b.append(note("<b>Lưu ý về lớp văn bản thô của Bảng 13.7.</b> Chú thích "
                  "thô có các ký tự rác cuối dòng và phần tiêu đề bị méo; "
                  "cách đọc theo trang in được dùng. Các ô CTI in literal "
                  "là các từ 'Note 2' ở hàng 10 V và 'Note 3' ở bốn hàng "
                  "điện áp cao nhất, cột đầu in số thuần túy đến 1575 rồi "
                  "đến các giá trị kV; dòng nguồn và tiêu đề 'Notes:' được "
                  "in nghiêng."))

    # C31 (printed p.370 / PDF p.391, raw 16187-16192).
    b.append(p("Thứ ba, nếu các số liệu 250 V rms hoặc 10 A rms hoặc 500 VA "
               "bị vượt quá trong vận hành bình thường, thì các mạch khác "
               "nhau trên rơ-le (cuộn dây và tiếp điểm và, khi thích hợp, "
               "các bộ tiếp điểm riêng biệt) cần được tách bằng các kỹ "
               "thuật dùng để tách các phương tiện đấu nối ngoài của mạch "
               "an toàn nội tại khỏi phương tiện của mạch không an toàn nội "
               "tại (được nêu chi tiết trước đó trong mục này)."))
    b.append(note("<b>Lưu ý về dấu cách trong C31.</b> Lớp văn bản thô ghi "
                  "'250Vrms or 10Arms or 500VA' không có dấu cách, nhưng "
                  "trang in cho rõ '250 V rms or 10 A rms or 500 VA' có "
                  "dấu cách. Cách đọc theo trang in được dùng ở đây và "
                  "trong bản tiếng Việt; dạng gộp của lớp thô được ghi "
                  "lại trong ghi chú này."))

    # C32 - heading 13.8, printed p.370 (see survey section 2).
    b.append(h3("13.8 Chế độ hỏng của linh kiện và mạch",
                "13.8 Component and circuit failure modes"))

    # C33 (printed p.370 / PDF p.391, raw 16194-16195; continues on p.371).
    b.append(p("Các hỏng hóc của linh kiện và của các kết nối mạch cần được "
               "xác định trong số đếm sự cố, trừ khi chúng không được coi "
               "là chịu sự cố do"))

    # C34 - continuation of C33 (printed p.371, raw 16198-16200).
    b.append(p("các yêu cầu kết cấu bổ sung được mô tả sau trong chương này. "
               "Các chế độ hỏng cần được tính đến tùy thuộc vào linh kiện "
               "đang xét."))

    # C35 - heading 13.8.1, printed p.371.
    b.append(h4("13.8.1 Dây và đường dẫn bo mạch in",
                "13.8.1 Wire and printed circuit tracks"))

    # C36 (printed p.371 / PDF p.392, raw 16202-16212).
    b.append(p("Có thể coi dây hoặc đường dẫn trên bo mạch in bị ngắt kết "
               "nối hoặc đứt và trong cả hai trường hợp hành động này được "
               "coi là một sự cố đếm được duy nhất, với điều kiện chúng chỉ "
               "mang hai phần ba dòng định mức tối đa (hệ số an toàn 1,5 "
               "được áp dụng). Khi liên quan đến dây thay vì đường dẫn in, "
               "dây có thể dịch chuyển và khi dịch chuyển có thể chạm vào "
               "các dẫn không cách điện khác trong thiết bị. Khả năng này "
               "phải được xem xét và bất kỳ sự nối liên kết nào như vậy sẽ "
               "được coi là sự cố đếm được thứ hai và không phải là một "
               "phần của sự cố thứ nhất (tức là dây bị đứt). Vì vậy, sự nối "
               "liên kết do dịch chuyển của dây chỉ quan trọng trong trường "
               "hợp mạch ‘ia’. Các dây được ép chặt với nhau không được coi "
               "là một dây duy nhất mà là hai dây được nối với nhau."))
    b.append(note("<b>Lưu ý về một lỗi OCR.</b> Lớp văn bản thô ghi "
                  "'Th~s possibility' ở chỗ trang in cho 'This possibility'; "
                  "cách đọc theo trang in được dùng."))

    # C37 - heading 13.8.2, printed p.371.
    b.append(h4("13.8.2 Kết nối", "13.8.2 Connections"))

    # C38 (printed p.371 / PDF p.392, raw 16214-16223).
    b.append(p("Hỏng của các kết nối thuộc bất kỳ loại nào khác ngoài phích "
               "cắm và ổ cắm (ví dụ, cọc đấu nối, mối ép, mối hàn, v.v.), với "
               "điều kiện chúng được thực hiện đúng cách và, không vận hành "
               "quá hai phần ba định mức của chúng (hệ số an toàn 1,5), được "
               "coi là hỏng thành mạch hở như một sự cố đếm được duy nhất. "
               "Chúng không được coi là hỏng thành điện trở cao hơn, như "
               "trường hợp các phần tử phích cắm và ổ cắm, vì người ta cho "
               "rằng các kết nối như vậy có mức độ bền vững cao hơn so với "
               "kết nối bằng phích cắm và ổ cắm, nơi sự mòn của các phần tử "
               "đấu nối do nhiều lần tháo và cắm làm phát sinh yếu tố hao "
               "mòn không có trong các hệ thống đấu nối khác."))
    b.append(note("<b>Lưu ý về dấu phẩy lạ sau 'and'.</b> Bản in ghi 'provided "
                  "that they are properly made and, are not operated...'; "
                  "dấu phẩy sau 'and' được giữ trong bản tiếng Anh, còn bản "
                  "tiếng Việt theo cấu trúc đúng nghĩa."))

    # C39 - heading 13.8.3, printed p.371.
    b.append(h4("13.8.3 Tụ điện và cuộn cảm",
                "13.8.3 Capacitors and inductors"))

    # C40 (printed p.371 / PDF p.392, raw 16225-16235; continues on p.372).
    b.append(p("Tụ điện và cuộn cảm làm việc ở mức không quá hai phần ba "
               "định mức thích hợp của chúng (lại là hệ số an toàn 1,5) được "
               "coi là hỏng thành mạch hở, ngắn mạch, hoặc thành các giá trị "
               "thấp hơn của điện cảm hoặc điện dung. Điều này là do cấu "
               "tạo của chúng, trong đó giá trị phản kháng của cả hai thường "
               "được quyết định bởi chiều dài của dây hoặc lá kim loại được "
               "quấn. Trường hợp cuộn cảm, đó là một cuộn dây và điện cảm "
               "không thể tăng lên mà không tăng số vòng dây. Vì vậy, điều "
               "duy nhất có thể xảy ra là giảm số vòng dây, sẽ làm giảm điện "
               "cảm và, trong hầu hết các trường hợp, điều đó xảy ra do ngắn "
               "mạch một số vòng - cuộn cảm sẽ có một vòng bị ngắn mạch làm "
               "giảm mạnh điện cảm xuống giá trị điện cảm rò rỉ được xác "
               "định bởi hiệu quả của sự liên kết giữa phần còn lại"))

    # C41 - continuation of C40 (printed p.372, raw 16238-16240).
    b.append(p("của cuộn cảm và vòng bị ngắn mạch. Trường hợp tụ điện, điện "
               "dung được xác định bởi chiều dài của hai bản cực song song "
               "được quấn bằng lá kim loại và không thể tăng lên, trừ khi "
               "tăng chiều dài."))

    # C42 - heading 13.8.4, printed p.372.
    b.append(h4("13.8.4 Điện trở", "13.8.4 Resistors"))

    # C43 (printed p.372 / PDF p.393, raw 16242-16251).
    b.append(p("Điện trở có thể hỏng thành bất kỳ giá trị nào cao hơn hoặc "
               "thấp hơn giá trị quy định của chúng. Một lần nữa điều này là "
               "do cấu tạo của chúng. Mặc dù vật liệu và chi tiết cấu tạo "
               "rất đa dạng, nhưng phải giả định trường hợp xấu nhất. Ví dụ, "
               "vật liệu thành phần carbon được dùng thay cho carbon nguyên "
               "chất trong nhiều trường hợp chứa các tạp chất mà người ta "
               "biết có khả năng cho phép hỏng thành điện trở giảm. Ngoài "
               "ra, sự xói mòn có thể làm giảm kích thước của các đường điện "
               "trở bên trong điện trở. Vì vậy, tình huống chung chắc chắn "
               "là hỏng thành điện trở cao hơn hoặc thấp hơn. Hỏng của điện "
               "trở thành một giá trị cụ thể được coi là một sự cố đếm được "
               "duy nhất trong bất kỳ bài toán đếm sự cố nào, miễn rằng các "
               "hệ số định mức được tuân thủ, và sau khi đã giả định sự cố "
               "thì không giả định thêm sự thay đổi nào khác xảy ra."))

    # C44 - heading 13.8.5, printed p.372.
    b.append(h4("13.8.5 Chất bán dẫn", "13.8.5 Semiconductors"))

    # C45 (printed p.372 / PDF p.393, raw 16253-16254).
    b.append(p("Chất bán dẫn có các chế độ hỏng tương đối phức tạp tùy thuộc "
               "vào cấu tạo của chúng."))

    # C46 - italic spot heading, printed p.372.
    b.append(h4("Đi-ốt và đi-ốt zener", "Diodes and zener diodes"))

    # C47 (printed p.372 / PDF p.393, raw 16256-16263).
    b.append(p("Đi-ốt và đi-ốt zener không vận hành quá hai phần ba định mức "
               "dòng hoặc công suất tối đa của chúng (hệ số an toàn 1,5) có "
               "thể, ví dụ, được giả định là hỏng thành mạch hở, ngắn mạch "
               "và trạng thái phù hợp. Hai chế độ đầu thường quan trọng "
               "nhất khi liên quan đến truyền công suất tới hoặc bảo vệ các "
               "linh kiện khác nhưng trạng thái phù hợp thường quan trọng "
               "nhất khi xét đến nhiệt độ bề mặt của đi-ốt hoặc đi-ốt zener. "
               "Hở mạch, ngắn mạch hoặc hỏng thành một giá trị điện trở khác "
               "được coi là một sự cố đếm được."))

    # C48 - italic spot heading, printed p.372.
    b.append(h4("Bóng bán dẫn", "Transistors"))

    # C49 (printed p.372 / PDF p.393, raw 16265-16271; continues on p.373).
    b.append(p("Tình huống đối với bóng bán dẫn làm việc ở mức không quá hai "
               "phần ba định mức dòng, điện áp và công suất tối đa của chúng "
               "(lại là hệ số an toàn 1,5) thì khác, vì chúng thường có ba "
               "chân. Cần xét đến ngắn mạch của bất kỳ chân nào đó với bất "
               "kỳ chân nào khác (hoặc với cả hai chân còn lại), cùng với "
               "sự nối liên kết giữa chúng, theo cách cho sự truyền công "
               "suất lớn nhất tới các linh kiện khác, để đánh giá an toàn "
               "nội tại của thiết bị. Bóng bán dẫn cũng cần được xem xét"))
    b.append(note("<b>Lưu ý về cách viết 'hệ số an toàn' trong đoạn Bóng bán "
                  "dẫn.</b> Lớp văn bản thô ghi '1.5V safety factor' (không "
                  "có dấu cách), trong khi các đoạn tương tự đều ghi "
                  "'1.5 safety factor'; trang in cho thấy '1.5 V safety "
                  "factor'. Sự có mặt của chữ 'V' là lỗi của bản gốc; dạng "
                  "của lớp thô được ghi lại ở đây, bản tiếng Anh dùng cách "
                  "đọc theo trang in và bản tiếng Việt dùng hệ số 1,5 đúng "
                  "nghĩa."))

    # C50 - continuation of C49 (printed p.373, raw 16274-16279).
    b.append(p("về phân loại nhiệt độ trên cơ sở công suất lớn nhất có sẵn "
               "cho nó được tiêu tán bên trong nó. Sau khi đã áp một sự cố "
               "(ví dụ ngắn mạch), không được giả định bóng bán dẫn lại hỏng "
               "theo chế độ khác trong cùng một đánh giá sự cố, nhưng tất cả "
               "các chế độ hỏng đều cần được xem xét trong các bài tập đếm "
               "sự cố khác nhau đã thực hiện (ví dụ, hở mạch như một phần "
               "của một chuỗi sự cố, ngắn mạch như một phần của chuỗi khác, "
               "v.v.)."))

    # C51 - italic spot heading, printed p.373.
    b.append(h4("Mạch tích hợp", "Integrated circuits"))

    # C52 (printed p.373 / PDF p.394, raw 16281-16292).
    b.append(p("Mạch tích hợp, mặc dù được xử lý như bóng bán dẫn, còn phức "
               "tạp hơn vì chúng có nhiều khả năng hỏng. Với mục đích phân "
               "loại nhiệt độ, sự cố được xét là sự cố làm toàn bộ công suất "
               "có sẵn phải tiêu tán trong thiết bị. Sự cố đếm được duy nhất "
               "cũng được coi là sự nối liên kết của bất kỳ tổ hợp chân nào "
               "và hở mạch của bất kỳ số chân nào xảy ra đồng thời (ví dụ, "
               "trong mạch mười chân, có thể coi tất cả các chân, nhiều nối "
               "liên kết giữa một hoặc nhiều chân trong số đó, và ngắn mạch "
               "hoàn toàn giữa tất cả chúng đều là những phần hợp lệ của sự "
               "cố duy nhất). Một lần nữa, kết nối điện trở giữa các chân "
               "không được xét để đánh giá mạch bên ngoài mạch tích hợp "
               "trong những trường hợp đó nhưng được xét khi quan tâm đến "
               "nhiệt độ của thiết bị."))

    # C53 - italic spot heading, printed p.373.
    b.append(h4("Linh kiện vượt quá định mức của chúng",
                "Components which exceed their ratings"))

    # C54 (printed p.373 / PDF p.394, raw 16294-16301).
    b.append(p("Nếu bất kỳ linh kiện, cụm lắp ráp hoặc phương pháp đấu nối "
               "nào không đáp ứng yêu cầu định mức (hệ số an toàn vận hành "
               "hai phần ba trên các thông số thích hợp) thì bất kỳ hỏng "
               "hóc nào được mô tả ở đây đều được coi là sự cố không đếm "
               "được; nghĩa là, chúng được áp dụng bổ sung ngoài các sự cố "
               "đếm được do cấp an toàn nội tại yêu cầu (‘ia’ hoặc ‘ib’). Khi "
               "chúng đáp ứng trong vận hành bình thường nhưng không còn "
               "đáp ứng khi bất kỳ sự cố đếm được hoặc không đếm được nào "
               "được áp ở nơi khác trong mạch, hỏng của chúng được coi là "
               "một phần của sự cố hoặc các sự cố đó và không được đếm "
               "riêng."))

    # C55 - italic spot heading, printed p.373.
    b.append(h4("Ứng dụng thiết bị thử để đánh lửa do tia lửa",
                "Application of the test apparatus for spark ignition"))

    # C56 (printed p.373 / PDF p.394, raw 16303-16310; continues on p.374).
    b.append(p("Thử nghiệm an toàn nội tại được thực hiện bằng cách đưa thiết "
               "bị thử tia lửa vào. Thiết bị này được đặt giữa các điểm "
               "trong mạch mà tại đó có thể coi là phát sinh tia lửa. Thiết "
               "bị có thể được đặt giữa bất kỳ dẫn nào và linh kiện nào, "
               "hoặc mắc nối tiếp với bất kỳ linh kiện nào, khi hỏng ngắn "
               "mạch một phần hoặc toàn bộ hoặc hỏng điện trở cao/mạch hở "
               "được coi là sự cố không đếm được sau khi đã áp các sự cố "
               "thích hợp. Ngoài ra, thiết bị thử tia lửa có thể được đặt "
               "trong các tình huống tương tự khi hỏng được coi là sự cố "
               "đếm được, và trong những trường hợp đó việc đặt và sử dụng "
               "thiết bị thử sẽ"))

    # C57 - continuation of C56 (printed p.374, raw 16313-16317).
    b.append(p("không được coi là một sự cố đếm được bổ sung. Quan điểm này "
               "được đưa ra vì, mặc dù sự cố đang xét được coi là đếm được, "
               "một vấn đề xung tạm thời do ngắt kết nối một phần hoặc ngắn "
               "mạch một phần có thể gây đánh lửa tại đây trong một thời "
               "gian đáng kể và trùng với các chế độ sự cố khác làm cho tia "
               "lửa trở nên có khả năng đánh lửa."))

    # C58 - heading 13.9, printed p.374.
    b.append(h3("13.9 Yêu cầu kết cấu của thiết bị",
                "13.9 Apparatus construction requirements"))

    # C59 (printed p.374 / PDF p.395, raw 16319-16322).
    b.append(p("Ngoài các yêu cầu đối với linh kiện, còn có các yêu cầu tối "
               "thiểu về việc lắp ráp chúng thành thiết bị để đảm bảo duy "
               "trì an toàn nội tại. Các yêu cầu này bao gồm yêu cầu về vỏ "
               "bọc, dây dẫn, kết nối, đường bò, khoảng hở và khoảng cách "
               "tách."))

    # C60 - heading 13.9.1, printed p.374.
    b.append(h4("13.9.1 Vỏ bọc", "13.9.1 Enclosures"))

    # C61 (printed p.374 / PDF p.395, raw 16324-16337).
    b.append(p("Yêu cầu đối với vỏ bọc của thiết bị an toàn nội tại và thiết "
               "bị liên kết là vỏ bọc như vậy chỉ cần tồn tại khi cần thiết "
               "để bảo vệ các dẫn trần hoặc các khoảng tách không thể hỏng "
               "khỏi bị suy giảm bởi các ảnh hưởng bên ngoài, chẳng hạn như "
               "sự tiếp cận. Trong những trường hợp này, vỏ bọc chỉ cần có "
               "mức bảo vệ IP20, phù hợp với BS/EN 60529¹⁵, về thực chất là "
               "mức bảo vệ cần thiết để ngăn chạm vào các bộ phận mang điện. "
               "Tuy nhiên, nói chung thiết bị được lắp vỏ bọc có mức độ "
               "nguyên vẹn cao hơn nhiều vì các lý do khác, ví dụ chống "
               "thời tiết. Điều này có nghĩa là, trừ những trường hợp rất "
               "đặc biệt, vỏ bọc của thiết bị sẽ được xác định bởi độ tin "
               "cậy công nghiệp và các yêu cầu an toàn cơ bản, chứ không "
               "phải bởi các yêu cầu của an toàn nội tại. Điều này có nghĩa "
               "là các yêu cầu về vỏ bọc cần thiết cho các khái niệm bảo vệ "
               "khác vì những lý do sau đây không được áp dụng trong trường "
               "hợp an toàn nội tại:"))
    b.append(note("<b>Lưu ý về sự nhấn mạnh nghiêng trong 13.9.1.</b> Các từ "
                  "'not applied' được in nghiêng và lớp văn bản thô ghi méo "
                  "thành 'nof applied'; cách đọc theo trang in và sự in "
                  "nghiêng được giữ nguyên."))
    b.append(note("<b>Lưu ý về số tham chiếu mũ sau BS/EN 60529.</b> Lớp văn "
                  "bản thô ghi 'BS/EN 6052915' còn trang in cho thấy "
                  "'BS/EN 60529¹⁵'; số tham chiếu dạng mũ được giữ nguyên."))

    # C62 - indented seven-line list, printed p.374 (raw 16338-16347).
    b.append(p("chậm mở vỏ bọc để cho phép xả năng lượng của các thiết bị "
               "lưu trữ năng lượng;<br>"
               "yêu cầu cụ thể đối với vật liệu nhựa để đảm bảo hiệu năng "
               "thích hợp<br>(không bao gồm khả năng tích điện tĩnh);<br>"
               "yêu cầu cụ thể đối với lỗ ren trong vỏ bằng nhựa và kim "
               "loại nhẹ<br>(nhôm, v.v.);<br>"
               "yêu cầu về kết cấu của các bạc lót, thiết bị liên khóa và<br>"
               "chốt;<br>"
               "yêu cầu đối với vật liệu xi măng dán và các thao tác;<br>"
               "yêu cầu đối với phương tiện đấu nối, cọc đấu nối và các "
               "khoang đầu nối;<br>"
               "yêu cầu thử va đập đối với vỏ bọc để xác định độ bền của "
               "chúng."))
    b.append(note("<b>Lưu ý về cách trình bày bảy mục loại trừ.</b> Chúng "
                  "được in thành một danh sách thụt lề không có dấu đầu dòng "
                  "hay số thứ tự và mục thứ sáu được ngắt giữa từ thành "
                  "'compart-ments'. Ngắt dòng và thụt lề treo được giữ trong "
                  "bản tiếng Anh; bản tiếng Việt dịch ý từng mục."))

    # C63 (printed p.374 / PDF p.395, raw 16348-16350; continues on p.375).
    b.append(p("Vì vậy, với ngoại lệ là thử rơi đối với thiết bị cầm tay, "
               "trong những trường hợp như vậy chỉ có các yêu cầu được quy "
               "định trong các Tiêu chuẩn liên quan đến bản thân khái niệm "
               "bảo vệ. Điều này là vì"))

    # C64 - continuation of C63 (printed p.375, raw 16353-16359).
    b.append(p("sự bảo vệ nằm trong chính các linh kiện và cụm lắp ráp được "
               "bao bọc, và không nằm ở vỏ bọc. Vì vậy, việc để lộ các mạch "
               "sẽ không dẫn đến tình trạng nguy hiểm vì các mạch vẫn an "
               "toàn nội tại. Tình huống không có vỏ bọc do hư hại sẽ không "
               "được chấp nhận trong thời gian dài vì không thể chấp nhận "
               "khả năng các tác động môi trường gây hoạt động sai của thiết "
               "bị, ngay cả khi thiết bị vẫn an toàn nội tại."))

    # C65 (printed p.375 / PDF p.396, raw 16360-16373).
    b.append(p("Khác với các khái niệm bảo vệ khác, an toàn nội tại cho "
               "phép, trong những trường hợp đặc biệt, thiết bị nằm trong "
               "nhiều hơn một vỏ bọc miễn là có thể chứng minh rằng hai phần "
               "của thiết bị là duy nhất trong sự liên kết giữa chúng. Điều "
               "này là do việc sử dụng kỹ thuật này trong các thiết bị như "
               "máy phát thu vô tuyến cầm tay và các thiết bị tương tự. Sau "
               "trong chương này, các hệ thống an toàn nội tại sẽ được thảo "
               "luận và sẽ thấy có một số điểm tương đồng giữa chúng và máy "
               "phát thu vô tuyến cầm tay có micrô cầm tay trên dây ngắn. Việc "
               "dùng khái niệm hệ thống cho thiết bị như vậy, khi hai phần "
               "được chế tạo và cung cấp cùng nhau, sẽ quá cồng kềnh và vì "
               "vậy có thể nói rằng chúng thuộc định nghĩa thiết bị an toàn "
               "nội tại. Có thể có nhiều tình huống tương tự khác nhưng phải "
               "nhấn mạnh rằng chúng là ngoại lệ và phải rõ ràng là gần như "
               "không có khả năng trao đổi giữa các phần khác nhau của các "
               "thiết bị ghép khác nhau thuộc loại này."))

    # C66 - heading 13.9.2, printed p.375.
    b.append(h4("13.9.2 Bố trí bên trong (dây dẫn, bo mạch in, v.v)",
                "13.9.2 Internal layout (wiring, printed circuit boards, etc)"))

    # C67 (printed p.375 / PDF p.396, raw 16375-16382).
    b.append(p("Dây dẫn và đường dẫn trên bo mạch in về nguyên tắc có thể là "
               "dẫn không cách điện (trần). Nếu vậy, chúng có thể tiếp xúc "
               "với nhau và tạo ra sự cố. Điều này không phải là vấn đề lớn "
               "đối với đường dẫn bo mạch in vì chúng được bố trí cứng nhắc, "
               "nhưng dẫn thông thường hoặc dẫn trên nền dây in mềm thì "
               "không. Ngoài ra, còn có khả năng dây hoặc đường dẫn đã cách "
               "điện cũng có thể tiếp xúc và trong những trường hợp đó chất "
               "lượng của lớp cách điện là quan trọng. Cách điện thường có "
               "nghĩa là lớp phủ bằng nhựa hoặc cao su trên dẫn và sơn véc-"
               "ni được xác định rõ là không được coi là cách điện."))

    # C68 (printed p.375 / PDF p.396, raw 16383-16394).
    b.append(p("Lớp cách điện trên dây của mạch an toàn nội tại và mạch không "
               "an toàn nội tại cũng phải đáp ứng một số yêu cầu tối thiểu "
               "khi hỏng của lớp cách điện có thể ảnh hưởng xấu đến an toàn "
               "nội tại và độ dày của nó không phù hợp với Bảng 13.7 và "
               "13.8. Nếu không thể chấp nhận sự cố giữa các dây, dây đã "
               "cách điện của một trong hai mạch, hoặc mạch an toàn nội tại "
               "hoặc mạch không an toàn nội tại, phải nằm trong một lớp màn "
               "che được nối đất và đủ chắc chắn để mang bất kỳ dòng nào có "
               "thể chảy từ một trong hai mạch trong thời gian hoạt động của "
               "các thiết bị bảo vệ như cầu chì. Nếu không có màn che như "
               "vậy, giải pháp "
               "thay thế là cách điện dây an toàn nội tại bằng lớp cách điện "
               "chịu được điện áp thử xoay chiều rms ít nhất 2000V. Giải "
               "pháp sau chỉ được chấp nhận trong mạch ‘ib’. Thường thì cần "
               "bổ sung một ống lót cách điện trên dây để đạt được điều "
               "này."))
    b.append(note("<b>Lưu ý về cách viết '2000V'.</b> Bản in ghi '2000V' "
                  "không có dấu cách trong C68, trong khi C73 lại ghi '30V'. "
                  "Cách ghi được giữ nguyên theo bản in."))

    # C69 (printed p.376 / PDF p.397, raw 16397-16400).
    b.append(p("Có một số giá trị tối thiểu (xem Bảng 13.8) mà bên dưới đó "
               "hỏng của các khoảng tách được coi là sự cố không đếm được, "
               "các khoảng tách này được đo với sự dịch chuyển có thể của "
               "các dẫn được chọn để cho giá trị nhỏ nhất. Các tình huống "
               "cần xem xét như sau."))

    # C70 - italic spot heading, printed p.376.
    b.append(h4("Khoảng hở", "Clearance"))

    # C71 (printed p.376 / PDF p.397, raw 16402-16408).
    b.append(p("Đây là khoảng cách ngắn nhất giữa hai dẫn không cách điện "
               "được đo qua không khí. Nó không nhất thiết là phép đo theo "
               "đường nhìn thẳng vì có thể đo vòng qua một vách cách điện "
               "phải dày ít nhất 0.9 mm và đủ cứng để chịu áp lực ngang "
               "30 N. Hình 13.16 cho thấy cách đo khoảng hở. Khi một vách "
               "kim loại nối đất được đặt giữa hai dẫn thì không cần đo "
               "khoảng hở giữa chúng, nhưng khi vách kim loại bị cô lập thì "
               "cần đo và độ dày của vách phải được trừ vào giá trị thu "
               "được."))

    # C72 - italic spot heading, printed p.376.
    b.append(h4("Đường bò", "Creepage"))

    # C73 (printed p.376 / PDF p.397, raw 16410-16431).
    b.append(p("Khoảng cách bò được đo tương tự như khoảng hở nhưng ở đây "
               "khoảng cách phải đo dọc theo bề mặt cách điện (ví dụ, bề "
               "mặt của bo mạch in hoặc một khối cọc đấu nối. Chỉ số theo "
               "dõi so sánh (CTI, xem BS 5901¹⁶) của bề mặt cách điện quan "
               "trọng ở đây vì nó phải đạt giá trị tối thiểu để đảm bảo "
               "chất lượng cách điện đủ, trừ khi điện áp giữa hai dẫn dưới "
               "30V vì ở điện áp thấp như vậy người ta cho rằng CTI kém "
               "quan trọng hơn nhiều. Nếu cả vật liệu cách điện và các dẫn "
               "đều được phủ bởi một lớp phủ cách điện, lớp phủ này bảo vệ "
               "cách điện khỏi bị suy giảm và CTI không còn quan trọng và, "
               "nhờ sự bảo vệ khỏi môi trường do lớp phủ cung cấp, khoảng "
               "cách bò có thể giảm đáng kể. Tuy nhiên, khi vật liệu cách "
               "điện và/hoặc các dẫn đi ra khỏi lớp phủ, không được phép "
               "giảm như vậy và vật liệu cách điện và/hoặc lớp phủ phải có "
               "CTI tối thiểu yêu cầu. Lớp phủ phải là lớp phủ đồng dạng "
               "bám chặt và phủ hoàn toàn các dẫn và lớp cách điện mà sự "
               "miễn giảm được áp dụng cho chúng. Nếu lớp phủ được quét "
               "bằng cọ, tạo ra bằng cách nhúng cụm vào lớp phủ, hoặc tạo "
               "ra bằng ngâm tẩm chân không thì chỉ cần một lớp. Khi được "
               "áp bằng các phương pháp khác, chẳng hạn phun, cần áp hai "
               "lớp riêng biệt. Nếu dùng mặt nạ hàn và mặt nạ này không bị "
               "hỏng trong quá trình hàn thì chỉ cần một lớp bổ sung bất kể "
               "phương pháp áp. Phương pháp đo khoảng cách bò được thể hiện "
               "trong Hình 13.17, 13.18 và 13.19."))
    b.append(note("<b>Lưu ý về số tham chiếu mũ sau BS 5901.</b> Lớp văn bản "
                  "thô ghi 'BS 590116' còn trang in cho thấy 'BS 5901¹⁶'; "
                  "số mũ được giữ nguyên."))
    b.append(note("<b>Lưu ý về dấu ngoặc không được đóng trong đoạn Đường "
                  "bò.</b> Câu '...along an insulating surface (e.g., the "
                  "surface of a printed circuit board or a terminal block. "
                  "The Comparative Tracking Index (CTI, see BS 5901¹⁶)...' "
                  "không bao giờ đóng dấu ngoặc mở thứ nhất trong bản in. "
                  "Cách ghi này được giữ trong bản tiếng Anh, bản tiếng Việt "
                  "theo nghĩa đúng."))

    # C74 - italic spot heading, printed p.376.
    b.append(h4("Khoảng tách", "Separation"))

    # C75 (printed p.376 / PDF p.397, raw 16433-16435; continues on p.377).
    b.append(p("Khoảng cách tách là khoảng cách phải đạt được giữa các dẫn "
               "mang điện trần, hoặc thông qua cách điện rắn hoặc qua các "
               "khoảng tách bằng lớp đổ khuôn, trong đó khoảng cách qua cách "
               "điện rắn nhỏ hơn qua lớp đổ khuôn, phản ánh chất lượng cách "
               "điện thường cao hơn của cách điện rắn. "))

    # C76 - continuation of C75 (printed p.377, raw 16438-16444; sentence
    # continues beyond PDF p.399, outside this module's scope).
    b.append(p("Phương pháp đo khoảng cách tách là đo khoảng cách ngắn nhất "
               "giữa hai dẫn xuyên qua lớp cách điện. Các vách cách điện "
               "không liên quan trong trường hợp các vách được nhúng trong "
               "cách điện rắn nhưng trong trường hợp ít xảy ra là một vách "
               "cách điện được nhúng trong hợp chất đổ khuôn, có thể tính "
               "đến ảnh hưởng của vách. Các phương pháp đo được thể hiện "
               "trong Hình 13.16. Bảng 13.8 cho các giá trị tối thiểu của "
               "khoảng hở, khoảng cách bò và khoảng tách cần đạt, để sự "
               "đánh thủng giữa"))
    b.append(note("<b>Lưu ý về ranh giới câu ở cuối phạm vi.</b> Phạm vi này "
                  "kết thúc giữa câu ở 'so that breakdown between' trên trang "
                  "in 378 (PDF 399); phần tiếp theo nằm ở trang sau, ngoài "
                  "phạm vi của mô-đun này, và không được suy diễn."))

    # Fig. 13.16 - printed p.377 (PDF p.398), after C76.
    b.append(fig(16, FC.fig_f1316()))
    b.append(note("<b>Lưu ý về nhãn vách trong Hình 13.16.</b> Lớp văn bản "
                  "thô ghi 'Rib (20.9 mm width)' và làm méo các đường kích "
                  "thước; trang in cho thấy 'Rib (≥0.9 mm width)' và "
                  "'Rib (<0.9 mm width)'. Cách đọc theo trang in được giữ "
                  "và chú thích không có dấu chấm cuối."))

    # Fig. 13.17 and Fig. 13.18 - printed p.378 (PDF p.399), figure-only page.
    b.append(fig(17, FC.fig_f1317()))
    b.append(fig(18, FC.fig_f1318()))
    b.append(note("<b>Lưu ý về các nhãn trong Hình 13.18.</b> Lớp văn bản "
                  "thô rút gọn các nhãn thành 'tl', 'Insulant' và 'd = "
                  "creepage distance'; trang in cung cấp 'Conductor', "
                  "'Insulant', 'Metal screw (earthed)', '<3', '≥3' và '≥1', "
                  "trong đó '<' là dấu nhỏ hơn nghiêm ngặt còn '≥' có gạch "
                  "ngang bằng. Các chú thích kết thúc bằng dấu chấm."))
    return "".join(b)


def body_en():
    b = []

    # C1 (printed p.363 / PDF p.384, raw 15814-15837; continues from module B).
    b.append(note("<b>Note on the running header glyph.</b> Even-numbered "
                  "printed pages carry the header 'Protection concept "
                  "intrinsic safety ‘i’ NNN' with a small stray raised mark "
                  "after the closing quote; the text layer reads plain "
                  "'‘i’'. The curly quotes are kept and the stray mark is "
                  "noted, but not reproduced."))
    b.append(note("<b>Note on the unclosed parenthesis in the print.</b> The "
                  "sentence 'Charging terminals ... must be enclosed to "
                  "IP20 (BS/EN 60529¹⁵ and in these circumstances ...' never "
                  "closes its opening parenthesis in the print. It is kept "
                  "open; the Vietnamese follows the intended meaning."))
    b.append(p("While the internal short circuiting of cells and batteries "
               "satisfying the foregoing requirements is not considered to "
               "be within a hazardous area for spark ignition purposes, "
               "external short circuiting is. It is necessary to ensure "
               "that the current which flows is intrinsically safe and the "
               "method of doing this is to ensure that the separation of "
               "cell or battery terminals is infallible, or not considered "
               "as subject to fault, and then to introduce current limiting "
               "devices in series with one or both of the terminals limiting "
               "the short circuit current to an intrinsically safe level. "
               "These current limiting devices need to be enclosed or "
               "encapsulated with the cell or battery if it is intended to "
               "be changed in a hazardous area or, where this is not so, the "
               "cell or battery needs to be in an enclosure fastened with "
               "special fasteners as described in Chapter 5, and warnings "
               "are then necessary to ensure that it will only be changed "
               "in a non-hazardous area. Charging terminals for rechargeable "
               "cells or batteries must be enclosed to IP20 (BS/EN 60529¹⁵ "
               "and in these circumstances the recharging must take place "
               "in a non-hazardous area. Alternatively, the charging "
               "terminals can be protected by diodes (two for ’ib’ and three "
               "for ’ia’) which prevent removal of current from them, or by "
               "an infallible resistor which forms an intrinsically safe "
               "circuit. Where, in these circumstances, charging is carried "
               "out by a charger whose output is not intrinsically safe, the "
               "diodes or resistor must be protected by a fuse which "
               "prevents excess current flowing during charging and, if the "
               "fuse carries current normally (i.e., is in the discharging "
               "circuit as well as the charging circuit), it should be "
               "encapsulated to prevent access of the explosive atmosphere "
               "to its element. Where the charger output is not "
               "intrinsically safe charging should only be carried out in "
               "the non-hazardous area."))

    # C2 - italic spot heading, printed p.363 (see survey section 2).
    b.append(h4("Semiconductor devices (diodes, zener diodes, thyristors, "
                "transistors, integrated circuits etc.)",
                "Semiconductor devices (diodes, zener diodes, thyristors, "
                "transistors, integrated circuits etc.)"))
    b.append(note("<b>Note on heading punctuation.</b> 'Semiconductor "
                  "devices (... etc.)' and 'Internal connectors (... etc.)' "
                  "have a full stop inside the closing parenthesis, while "
                  "'Connectors for external connections (... etc)' and "
                  "'13.9.2 Internal layout (... etc)' have none. The "
                  "inconsistency is kept as printed."))

    # C3 (printed p.363 / PDF p.384, raw 15840-15855).
    b.append(p("Failure of properly rated semiconductor devices is normally "
               "considered as a countable fault but because of their nature "
               "they must be shown to be proof against transients. In the "
               "case of associated apparatus, where this is fed from or "
               "otherwise connected to the mains supplies, the transient "
               "currents which occur are determined by the mains and such "
               "currents will, at worst, be the peak value of the mains "
               "voltage divided by any infallible series resistance present "
               "in the circuit between the mains and the semiconductor "
               "device. Thus the semiconductors must be capable of suffering "
               "significant voltage and current transients without damage, "
               "even when an infallible transformer is included in the "
               "circuit to provide a low voltage from which to derive the "
               "intrinsically safe circuit. This is an onerous requirement "
               "but it is only applied to those semiconductor devices upon "
               "which intrinsic safety depends, such as shunt voltage "
               "limiting devices, etc. Once out of the associated apparatus "
               "transients can be ignored as it is assumed that they will "
               "be suppressed to a large extent in the associated apparatus "
               "and what remains will not cause problems."))

    # C4 (printed p.364 / PDF p.385, raw 15858-15864).
    b.append(p("Apart from the three diodes permitted for blocking in ‘ia’ "
               "circuits, semiconductors used for series limiting are "
               "restricted to ’ib’ circuits because of their transparency "
               "to transients which would be of very great concern in "
               "circuits which entered Zone 0 because of the permanent "
               "presence of an explosive atmosphere and the possibility of "
               "their passing of a brief ignition capable transient, which "
               "would in that case coincide with the presence of the "
               "explosive atmosphere, unlike the case in Zone 1 where "
               "coincidence is much less likely."))

    # C5 (printed p.364 / PDF p.385, raw 15865-15874).
    b.append(p("Where semiconductors are used as shunt voltage limiting "
               "devices they can only include diode connected transistors "
               "(e.g., those connected so that they are either fully on or "
               "fully off), thyristors, zener diodes and similar devices. "
               "They must have a forward current rating of 1.5 times the "
               "maximum current which can flow including fault conditions "
               "if they were short circuited. This requirement is also "
               "applied to zener diodes and is determined by consideration "
               "of the current limit when the diode is used in the forward "
               "diode direction (the opposite polarity to the zener "
               "direction). Zener diodes need also to operate at no more "
               "than two thirds of their rated zener maximum power "
               "dissipation when operated in the circuit as zener diodes "
               "with faults applied in the circuit."))

    # C6 (printed p.364 / PDF p.385, raw 15875-15882).
    b.append(p("The use of controllable semiconductors, such as transistors, "
               "voltage regulators and thyristors is generally restricted "
               "to ’ib’ circuits, except in situations where both input and "
               "output circuits are intrinsically safe, or where it can be "
               "shown that transients from the power supplies do not occur. "
               "In such circuits two parallel devices are considered as "
               "infallible, even in ‘ia’ circuits. In addition, even where "
               "transients can occur three shunt thyristors are acceptable "
               "in ’ia’ circuits if they can handle the transients and their "
               "let-through energy is limited to the following when they "
               "operate:"))

    # C7 - displayed let-through energy list (printed p.364, raw 15883-15885).
    b.append(eq("IIA = 160 μJ<br>IIB = 80 μJ<br>IIC = 20 μJ"))
    b.append(note("<b>Note on the let-through energy list.</b> The raw text "
                  "layer reads 'IIB = WpJ' but the page render shows "
                  "'IIB = 80 μJ'; the render value is authoritative and is "
                  "retained, together with 'IIA = 160 μJ' and 'IIC = 20 μJ'."))

    # C8 - italic spot heading, printed p.364 (see survey section 2).
    b.append(h4("Internal connectors (terminals, plug-in cards, plugs and "
                "sockets, etc.)",
                "Internal connectors (terminals, plug-in cards, plugs and "
                "sockets, etc.)"))
    b.append(note("<b>Note on the standard designation in BS/EN 50020.</b> "
                  "The raw layer reads 'BS/EN 5O02O1O' with capital O for "
                  "zeros; the render shows 'BS/EN 50020¹⁰' with superscript "
                  "10. The superscript reference numeral is preserved."))

    # C9 (printed p.364 / PDF p.385, raw 15887-15894).
    b.append(p("In general there are no requirements for the quality of the "
               "connecting elements of internal connectors which are "
               "additional to those required for normal industrial use, and "
               "failure of connecting elements to high resistance or open "
               "circuit are considered as a countable fault. In failure to "
               "high resistance there will obviously be a potential heating "
               "problem but the requirements for the protection concept in "
               "BS/EN 50020¹⁰ specifically state that a temperature "
               "classification of T6 is to be applied to such devices and "
               "therefore no evaluation in this regard is necessary. The "
               "reason for this lies in the fact that experience of failures "
               "in such connectors is that such failure is to open circuit "
               "or to a very high resistance, and the possibility of "
               "significant power dissipation in such connector is "
               "considered to be extremely small."))

    # C10 (printed p.365 / PDF p.386, raw 15897-15914; continues on p.366).
    b.append(p("Where there is a connector in an item of apparatus, the "
               "arrangement must be such that it cannot be reverse connected "
               "if such connection adversely affects intrinsic safety. The "
               "required security is normally achieved by keying the "
               "connector so that it will only fit one way and most "
               "commercial plugs and sockets are configured in such a "
               "manner. With printed circuit connectors keying is normally "
               "by replacing one of the connectors with a slot in the board "
               "and blocking one of the receptacle positions in the socket "
               "(see Fig. 13.13). Obviously if such is not the case then "
               "reverse connection is not important except for operational "
               "reasons, but these would probably require the same "
               "precautions in any event. Where the apparatus contains more "
               "than one connector interchangeability between connectors "
               "must not be possible where it could adversely affect "
               "intrinsic safety. Keying or a similar approach is the "
               "optimum approach both for incorrect connection of a single "
               "connector and inadvertent interchange between connectors. "
               "It is recognized that such an approach is not always "
               "economic and the identification of connectors to make "
               "incorrect connection obvious, for example, by some form of "
               "colour coding, is regarded as an alternative. Where "
               "connectors carry earth connections which are necessary for "
               "the provision of intrinsic safety, the contacts need to be "
               "duplicated for ‘ib’"))
    b.append(note("<b>Note on the missing full stop at the foot of printed "
                  "p.365.</b> The paragraph above ends '...the contacts need "
                  "to be duplicated for ‘ib’' with no full stop; the sentence "
                  "resumes on printed p.366 with 'and triplicated for ‘ia’ "
                  "...'. The two halves are kept as a single continuous "
                  "sentence."))
    b.append(note("<b>Note on a hyphenation artefact in the text layer.</b> "
                  "The raw layer shows a garbled form of 'connectors' with a "
                  "stray glyph in the middle; the render reads 'connectors'. "
                  "The render reading is used."))

    # Fig. 13.13 - printed p.365 (PDF p.386), after C10.
    b.append(fig(13, FC.fig_f1313()))
    b.append(note("<b>Note on the Fig. 13.13 caption number.</b> The raw "
                  "layer reads 'Fig. 13.1 3' with a stray space; the render "
                  "reads 'Fig. 13.13'. The figure caption follows the print."))
    b.append(note("<b>Note on the in-figure label 'Out out'.</b> The arrow to "
                  "the keyed connector is labelled 'Out out' in the print "
                  "(lower-case in the raw layer). The label is retained "
                  "verbatim in the figure; no meaning is inferred."))

    # Fig. 13.14 - printed p.366 (PDF p.387), at top of page before C11.
    b.append(fig(14, FC.fig_f1314()))
    b.append(note("<b>Note on the labels of Fig. 13.14.</b> The raw layer "
                  "garbles the upper labels; the render gives two singular "
                  "'Joint not subject to fault (infallible)' labels on the "
                  "left, plural 'Joints not subject to fault (infallible)' "
                  "on the right, 'Pins and sockets' (plural) left and 'Pin "
                  "and socket' (singular) right; the earth connections read "
                  "1, 3, 2 from left to right. The render reading is "
                  "retained."))

    # C11 - continuation of C10 (printed p.366, raw 15938-15943).
    b.append(p("and triplicated for ‘ia’ in a manner which achieves the "
               "objectives shown in Fig. 13.14. In addition, in the case of "
               "in-line connectors such as those used for printed circuit "
               "boards, where withdrawal could be at an angle, the "
               "connections need to be distributed along the connector to "
               "ensure that at least one of them remains in contact until "
               "the connector is fully removed. This requires one connection "
               "at (or very close to) each end of the connector."))

    # C12 (printed p.366 / PDF p.387, raw 15944-15948).
    b.append(p("Terminals need not comply with any requirements other than "
               "those applied for industrial use and, like connectors, they "
               "will be considered to fail to a very high resistance or open "
               "circuit as a single countable fault. Therefore, they will be "
               "considered in respect of temperature classification in the "
               "same way as connectors and will be T6."))

    # C13 - italic spot heading, printed p.366.
    b.append(h4("Soldered joints", "Soldered joints"))

    # C14 (printed p.366 / PDF p.387, raw 15950-15951; continues on p.367).
    b.append(p("There are no specific requirements for soldered joints and "
               "normal soldered joints will be considered only to fail as a "
               "countable fault. Temperature"))

    # C15 - continuation of C14 (printed p.367, raw 15954-15958).
    b.append(p("classification of such joints will, as for terminals and "
               "other connectors, be considered as T6. Where a wire becomes "
               "detached as a result of the failure of a soldered joint "
               "connection of that wire to any other conducting part within "
               "its resultant range of movement, it will, as with other "
               "disconnected wires, be considered as a second countable "
               "fault."))

    # C16 - italic spot heading, printed p.367.
    b.append(h4("Connectors for external connections (terminals, plugs and "
                "sockets, etc)",
                "Connectors for external connections (terminals, plugs and "
                "sockets, etc)"))

    # C17 (printed p.367 / PDF p.388, raw 15960-15964).
    b.append(p("Terminals for connection of external circuits must comply "
               "with the requirements for those used internally and must, in "
               "addition, comply with the following requirements. First, "
               "they must have a separation between each other and between "
               "them and any earth connection of at least the figures given "
               "for creepage, clearance and separation needed so that "
               "interconnection can be ignored."))

    # C18 (printed p.367 / PDF p.388, raw 15965-15968).
    b.append(p("Second, they must be separated from one another by at least "
               "6 mm and from earth by at least 3 mm (the distance in "
               "question being measured as shown in Fig. 13.15) when all "
               "circuits in question are intrinsically safe circuits, and by "
               "at least 50 mm from non-intrinsically safe circuits."))

    # C19 (printed p.367 / PDF p.388, raw 15969-15976).
    b.append(p("Third, any partitions used to assist in separation must be "
               "at least 0.9 mm thick if made of insulating material and "
               "0.45 mm thick if made from metal. In both cases the "
               "partitions must pass a test which applies a lateral force of "
               "30 N to determine their rigidity and, if metallic, must be "
               "earthed or of sufficient thickness that it can be "
               "demonstrated that burn through will not occur in case of "
               "fault. Also, their earth connection must be such as to "
               "preclude loss of earth. If this is achieved by an earth "
               "connection rather than their forming part of an earthed "
               "frame the connection must satisfy the requirements for "
               "infallible connections."))

    # C20 (printed p.367 / PDF p.388, raw 15977-15979).
    b.append(p("Finally, where partitions are used the 50 mm separation may "
               "be waived if the partitions used are arranged so that the "
               "separation between their extremities are within 1.5 mm of "
               "the walls and cover of the enclosure."))

    # C21 (printed p.367 / PDF p.388, raw 15980-15984).
    b.append(p("The burn-through problem is not a real problem for most "
               "circuits as their power consumption is so low as to make the "
               "minimum thickness quoted sufficient. It must, however, be "
               "carefully considered in circuits which use hgh energy, such "
               "as those associated with some relay output contacts in "
               "associated apparatus."))
    b.append(note("<b>Note on the printed typo 'hgh'.</b> The print reads "
                  "'...in circuits which use hgh energy...'; the word is in "
                  "the source, not an OCR error, and is kept verbatim in "
                  "English. The Vietnamese follows the intended meaning."))

    # C22 (printed p.367 / PDF p.388, raw 15985-15994).
    b.append(p("The terminals themselves must satisfy the normal industrial "
               "requirements but must also satisfy additional requirements "
               "when used for connection of earths important to intrinsic "
               "safety. They need to be free of any sharp edges which could "
               "damage or sever any connected wires and not rely on "
               "insulating materials to transmit the pressure necessary to "
               "ensure conductor clamping. When stranded conductors are used "
               "without crimped ferrules it is necessary to introduce a "
               "pressure plate between the terminal screw and the wire to "
               "ensure good connection without damage to the strands, and if "
               "they have a maximum allowable conductor size below 4 mm² "
               "they must be arranged so that they can effectively clamp "
               "smaller conductors also."))

    # Fig. 13.15 - printed p.368 (PDF p.389), before C23.
    b.append(fig(15, FC.fig_f1315()))
    b.append(note("<b>Note on the inequality signs in Fig. 13.15.</b> The "
                  "raw layer reads '2 6 mm' and '2 50mm'; the render shows "
                  "'≥ 6 mm' and '≥ 50 mm' in the caption and 'd ≥ 3', 'd ≥ 6', "
                  "'d ≥ 6 mm' in the figure. The ≥ signs are kept; the note "
                  "is part of the printed caption, not a separate note line."))

    # C23 (printed p.368 / PDF p.389, raw 16000-16005).
    b.append(p("Plugs and sockets need to comply with the same requirements "
               "as internal plugs and sockets for construction and "
               "interchangeability and, in addition, the facilities for "
               "wiring to the plugs and sockets should comply with the same "
               "requirements as terminals unless special precautions are "
               "taken in terminating the wires in the plug or socket, or the "
               "cable is attached during manufacture."))

    # C24 - italic spot heading, printed p.368.
    b.append(h4("Piezo electric devices", "Piezo electric devices"))

    # C25 (printed p.368 / PDF p.389, raw 16007-16008; continues on p.369).
    b.append(p("Piezo electric devices are relatively unique in that they "
               "have the ability to translate mechanical stresses into "
               "electrical signals. Because of this they can"))

    # C26 - continuation of C25 (printed p.369, raw 16011-16017).
    b.append(p("add to the electrical energy in an intrinsically safe "
               "circuit. The possible electrical energy can be measured by "
               "subjecting external parts of the apparatus into which they "
               "are fitted to the impact tests usually used for strength "
               "determination (see Chapter 8), and noting the maximum voltage "
               "generated in the device during such impact testing. If the "
               "capacitance of the devices is then measured the maximum "
               "output energy can then be calculated from:"))

    # C27 - displayed formula, where-block and energy limits (printed p.369).
    b.append(eq("e = 0.5CV²x                                              μJ"))
    b.append(p("where   e = energy generated                              J<br>"
               "        C = capacitance                                   μF<br>"
               "        V = maximum voltage generated                     V"))
    b.append(p("This energy must not exceed the following maximum values:"))
    b.append(eq("IIA = 950 μJ<br>IIB = 250 μJ<br>IIC = 50 μJ"))
    b.append(note("<b>Note on the piezo-electric energy formula.</b> The "
                  "print reads 'e = 0.5CV²x' with a small trailing 'x' after "
                  "V² (possibly a stray multiplication mark) and the unit "
                  "'μJ' at the far right; the where-block units are 'J', "
                  "'μF' and 'V'. The trailing 'x' is preserved and not "
                  "silently corrected."))

    # C28 (printed p.369 / PDF p.390, raw 16026-16031).
    b.append(p("Guards may be fitted to reduce the effects of impacts in "
               "this regard but they must not be damaged in a way which "
               "reduces their effectiveness by the impact if so used. Also, "
               "in special circumstances, the apparatus may be deemed to be "
               "free of such impacts but in such circumstances it is "
               "essential that users are clearly informed of what must be "
               "achieved by any installation to achieve this."))

    # C29 - italic spot heading, printed p.369.
    b.append(h4("Relays", "Relays"))

    # C30 (printed p.369 / PDF p.390, raw 16033-16048).
    b.append(p("The construction of relays is important when they are used "
               "to separate parts of the same intrinsically safe circuit, "
               "separate intrinsically safe circuits, or intrinsically safe "
               "circuits and non-intrinsically safe circuits. "
               "Interconnections between coils and contacts and contacts "
               "and other contacts can be important and are dealt with in "
               "Sections 13.6 and 13.7. There are, however, design limits in "
               "the case of relays where the coils are in intrinsically safe "
               "circuits and the contacts in non-intrinsically safe circuits, "
               "or where the relay has two sets of contacts one in each type "
               "of circuit. These are determined by the need to ensure that "
               "ionization arising from sparking is not a problem and are as "
               "follows. First, the contacts in non-intrinsically safe "
               "circuits should not normally switch circuits operating at "
               "more than 250 V rms with a rating of more than 100 VA and the "
               "switched current should not exceed 5 Arms. Second, these "
               "figures may be increased to 10 A rms and 500 VA, but, where "
               "breakdown must not occur the spacings between the coil and "
               "contacts or the two sets of contacts must be increased over "
               "those in Table 13.7 by a factor of 4."))
    b.append(note("<b>Note on '5 Arms'.</b> The relay paragraph prints the "
                  "switched-current limit as '5 Arms' with no space, while "
                  "the same paragraph prints '250 V rms', '10 A rms' and "
                  "'500 VA' with spaces. The spacing is kept as printed."))

    # Table 13.7 - printed p.370 (PDF p.391), before C31.
    b.append(table(T2.HEAD137_EN, T2.ROWS137_EN, T2.CAPTION137_EN))
    # The supplier's English translator note quotes the two Vietnamese row
    # labels with diacritics; name them descriptively on the EN page so no
    # Vietnamese diacritics leak into the English body.
    b.append(note(T2.NOTE137_EN.replace(
        "'Ghi chú 2' / 'Ghi chú 3'", "their Vietnamese equivalents")))
    b.append(note("<b>Note on the text layer of Table 13.7.</b> The raw "
                  "caption has spurious trailing characters and the raw "
                  "header is mangled; the render is followed. The CTI cells "
                  "print the literal words 'Note 2' in the 10 V row and "
                  "'Note 3' in the four highest-voltage rows, the first "
                  "column prints bare numbers up to 1575 followed by kV "
                  "values, and the source line and 'Notes:' heading are "
                  "italic in print."))

    # C31 (printed p.370 / PDF p.391, raw 16187-16192).
    b.append(p("Third, if the figures of 250 V rms or 10 A rms or 500 VA are "
               "exceeded in normal operation, then the different circuits on "
               "the relay (coil and contacts and, where appropriate, "
               "separate sets of contacts) need to be separated by the "
               "techniques used to separate intrinsically safe circuit "
               "external connection facilities from those for "
               "non-intrinsically safe circuits (which are detailed earlier "
               "in this section)."))
    b.append(note("<b>Note on the spacing in C31.</b> The raw text layer "
                  "reads '250Vrms or 10Arms or 500VA' with no spaces, but the "
                  "page render clearly shows '250 V rms or 10 A rms or 500 "
                  "VA' with spaces. The render reading is used here and in "
                  "the Vietnamese; the unspaced raw form is recorded in "
                  "this note."))

    # C32 - heading 13.8, printed p.370 (see survey section 2).
    b.append(h3("13.8 Component and circuit failure modes",
                "13.8 Component and circuit failure modes"))

    # C33 (printed p.370 / PDF p.391, raw 16194-16195; continues on p.371).
    b.append(p("Failures of components and circuit connections need to be "
               "identified in the fault count unless they are not considered "
               "as subject to fault by virtue of"))

    # C34 - continuation of C33 (printed p.371, raw 16198-16200).
    b.append(p("of additional constructional requirements described later "
               "in this chapter. The fault modes which need to be taken into "
               "account depend upon the component in question."))

    # C35 - heading 13.8.1, printed p.371.
    b.append(h4("13.8.1 Wire and printed circuit tracks",
                "13.8.1 Wire and printed circuit tracks"))

    # C36 (printed p.371 / PDF p.392, raw 16202-16212).
    b.append(p("Wires or printed circuit tracks may be considered to become "
               "disconnected or break and in either case the action will be "
               "considered as a single countable fault, provided that they "
               "only carry two thirds of their maximum rated current (the "
               "1.5 safety factor is applied). Where wires are involved, "
               "rather than printed tracks, it is possible for them to move "
               "and in doing so they may contact other uninsulated "
               "conductors in the apparatus. This possibility must be "
               "considered and any such interconnection will be considered "
               "as a second countable fault and not part of the first one "
               "(i.e., the wire break). Thus the interconnection described "
               "by wire movement is only important in the case of ‘ia’ "
               "circuits. Wires which are crimped together are not "
               "considered as a single wire but as two wires which are "
               "connected together."))
    b.append(note("<b>Note on an OCR artefact.</b> The raw layer reads "
                  "'Th~s possibility' where the render reads 'This "
                  "possibility'; the render reading is used."))

    # C37 - heading 13.8.2, printed p.371.
    b.append(h4("13.8.2 Connections", "13.8.2 Connections"))

    # C38 (printed p.371 / PDF p.392, raw 16214-16223).
    b.append(p("Failure of connections of any type other than plugs and "
               "sockets (e.g., terminals, crimps, soldering, etc.), provided "
               "that they are properly made and, are not operated at more "
               "than two thirds of their ratings (the 1.5 safety factor), "
               "are considered to fail to open circuit only as a single "
               "countable fault. They are not considered to fail to a higher "
               "resistance, as is the case for plug and socket elements, as "
               "such connections are assumed to have a greater degree of "
               "permanence to those made by a plug and socket where wear on "
               "the connecting parts, due to multiple removals and "
               "insertions, adds a wear element to the consideration not "
               "present in the case of other connection systems."))
    b.append(note("<b>Note on the comma after 'and'.</b> The print reads "
                  "'provided that they are properly made and, are not "
                  "operated...'; the comma after 'and' is preserved in "
                  "English, while the Vietnamese follows the intended "
                  "construction."))

    # C39 - heading 13.8.3, printed p.371.
    b.append(h4("13.8.3 Capacitors and inductors",
                "13.8.3 Capacitors and inductors"))

    # C40 (printed p.371 / PDF p.392, raw 16225-16235; continues on p.372).
    b.append(p("Capacitors and inductors operated at not more than two thirds "
               "of their appropriate ratings (again the 1.5 safety factor) "
               "are considered to fail to open circuit, to short circuit, or "
               "to lower values of inductance or capacitance. This is "
               "because of their construction where the reactance value of "
               "both is usually governed by wound lengths of wire or foil. "
               "In the case of inductors, it is a wire winding and the "
               "inductance cannot increase without increasing the number of "
               "turns. All that can happen, therefore, is a reduction of the "
               "number of turns which will reduce the inductance and, as in "
               "most cases, it will be by short circuit of some turns - the "
               "inductor will have a short circuit turn which will "
               "dramatically reduce the inductance to the leakage inductance "
               "value defined by the efficiency of the coupling between the "
               "remaining part"))

    # C41 - continuation of C40 (printed p.372, raw 16238-16240).
    b.append(p("of the inductor and the short circuit turn. In the case of "
               "capacitors, the capacitance is determined by the length of "
               "two parallel wound plates of foil and cannot be increased, "
               "except by increase of length."))

    # C42 - heading 13.8.4, printed p.372.
    b.append(h4("13.8.4 Resistors", "13.8.4 Resistors"))

    # C43 (printed p.372 / PDF p.393, raw 16242-16251).
    b.append(p("Resistors can fail to any value higher or lower than their "
               "specified value. Again this is because of their "
               "construction. While this is varied in both materials and "
               "detail the worst case has to be assumed. For example, a "
               "carbon composition material used in preference to pure "
               "carbon in many cases contains impurities which are known to "
               "have the possibility to allow failure to reduced resistance. "
               "In addition, it is possible for erosion to reduce dimensions "
               "of resistance tracks within a resistor. Thus the general "
               "situation has to be failure to higher or lower resistance. "
               "Failure of a resistor to a particular value is considered as "
               "a single countable fault in any fault-counting exercise, "
               "providing rating factors are honoured, and once the failure "
               "has been assumed further change is not assumed to occur."))

    # C44 - heading 13.8.5, printed p.372.
    b.append(h4("13.8.5 Semiconductors", "13.8.5 Semiconductors"))

    # C45 (printed p.372 / PDF p.393, raw 16253-16254).
    b.append(p("Semiconductors have relatively complex modes of failure "
               "which depends upon their construction."))

    # C46 - italic spot heading, printed p.372.
    b.append(h4("Diodes and zener diodes", "Diodes and zener diodes"))

    # C47 (printed p.372 / PDF p.393, raw 16256-16263).
    b.append(p("Diodes and zener diodes which are not operated at more than "
               "two thirds of their maximum current or power ratings (the "
               "1.5 safety factor) can, for example, be assumed to fail to "
               "open circuit, short circuit and to a matched condition. The "
               "former two modes are usually most important when power "
               "transfer to, or protection of, other components is involved "
               "but the matched condition is usually the most important "
               "where the surface temperature of the diode or zener diode is "
               "concerned. Open circuit, short circuit or failure to another "
               "resistance value is considered as one countable fault."))

    # C48 - italic spot heading, printed p.372.
    b.append(h4("Transistors", "Transistors"))

    # C49 (printed p.372 / PDF p.393, raw 16265-16271; continues on p.373).
    b.append(p("The situation in regard to transistors operated at no more "
               "than two thirds of their maximum current, voltage and power "
               "ratings (again the 1.5 V safety factor) is different in that "
               "they normally have three leads. Short circuit of any one of "
               "those to any one of the others (or both of the others) needs "
               "to be considered, together with their interconnection, in a "
               "manner which gives the maximum power transfer to other "
               "components, for evaluation of the intrinsic safety of the "
               "apparatus. The transistor also needs to be considered"))
    b.append(note("<b>Note on the 'safety factor' wording in the Transistors "
                  "paragraph.</b> The raw layer reads '1.5V safety factor' "
                  "(with no space) whereas all parallel passages read '1.5 "
                  "safety factor'; the page render shows '1.5 V safety "
                  "factor'. The presence of the 'V' is the printed source "
                  "error; the raw form is recorded here, the render reading "
                  "is used in the English paragraph and the Vietnamese "
                  "follows the intended 1.5 factor."))

    # C50 - continuation of C49 (printed p.373, raw 16274-16279).
    b.append(p("for temperature classification on the basis of the maximum "
               "power available to it being dissipated within it. Once "
               "having applied a fault (e.g., a short circuit) the transistor "
               "cannot then be assumed to fail in another mode within the "
               "same fault evaluation but all modes of failure need to be "
               "considered in the various fault-count exercise undertaken "
               "(e.g., open circuit as part of the one fault train, short "
               "circuit as part of another, etc.)."))

    # C51 - italic spot heading, printed p.373.
    b.append(h4("Integrated circuits", "Integrated circuits"))

    # C52 (printed p.373 / PDF p.394, raw 16281-16292).
    b.append(p("Integrated circuits, while being treated in the same way as "
               "transistors, are even more complex as they have a "
               "multiplicity of fault possibilities. For the purposes of "
               "temperature classification the fault considered is that "
               "which will cause all the available power to be dissipated in "
               "the unit. The single countable fault will also be considered "
               "as interconnections of any combination of pins and open "
               "circuits of any number of pins all occurring simultaneously "
               "(e.g., in a ten pin circuit all pins can be considered, "
               "several interconnections between one or more of them, and "
               "total short circuit between them all are valid parts of the "
               "single fault). Again resistance interconnection between pins "
               "is not considered for evaluation of the circuit outside the "
               "integrated circuit in such cases but is considered where "
               "device temperature is concerned."))

    # C53 - italic spot heading, printed p.373.
    b.append(h4("Components which exceed their ratings",
                "Components which exceed their ratings"))

    # C54 (printed p.373 / PDF p.394, raw 16294-16301).
    b.append(p("If any component or assembly or connection method does not "
               "satisfy the rating requirements (two thirds operational "
               "safety factor on appropriate parameters) then any of the "
               "failures described here are considered as non-countable "
               "faults; that is, they are applied in addition to the "
               "countable faults required by the grade of intrinsic safety "
               "(‘ia’ or ‘ib’). Where they do comply in normal operation, "
               "but cease to do so when any permissible countable or "
               "non-countable fault or faults are applied elsewhere in the "
               "circuit, their failure is considered a part of that or those "
               "other faults and is not separately counted."))

    # C55 - italic spot heading, printed p.373.
    b.append(h4("Application of the test apparatus for spark ignition",
                "Application of the test apparatus for spark ignition"))

    # C56 (printed p.373 / PDF p.394, raw 16303-16310; continues on p.374).
    b.append(p("Testing for Intrinsic Safety is by insertion of the spark "
               "test apparatus. This is placed between points in the circuit "
               "where sparking may be considered to occur. It can be placed "
               "between any conductors and components, or in series with any "
               "components, where partial or total short or high "
               "resistance/open circuit failure is considered as a "
               "non-countable fault after the appropriate faults have been "
               "applied. In addition, the spark test apparatus can be placed "
               "in similar situations where failure would be considered as a "
               "countable fault, and in such cases the placement and use of "
               "the test apparatus will"))

    # C57 - continuation of C56 (printed p.374, raw 16313-16317).
    b.append(p("not be considered as an additional countable fault. This "
               "position is taken because, although the failure in question "
               "would be considered as countable, a transient problem caused "
               "by partial disconnection or partial short circuit could "
               "cause sparking here for a considerable time and coincide "
               "with other fault modes which would make the spark incendive."))

    # C58 - heading 13.9, printed p.374.
    b.append(h3("13.9 Apparatus construction requirements",
                "13.9 Apparatus construction requirements"))

    # C59 (printed p.374 / PDF p.395, raw 16319-16322).
    b.append(p("In addition to the requirements for components there are "
               "minimum requirements for their assembly into items of "
               "apparatus to ensure that intrinsic safety is maintained. "
               "These requirements include requirements for enclosures, "
               "wiring, connections, creepages, clearances and separations."))

    # C60 - heading 13.9.1, printed p.374.
    b.append(h4("13.9.1 Enclosures", "13.9.1 Enclosures"))

    # C61 (printed p.374 / PDF p.395, raw 16324-16337).
    b.append(p("The requirements for enclosures for intrinsically safe and "
               "associated apparatus are that such an enclosure need only "
               "exist when necessary to protect bare conductors or "
               "infallible separations from being degraded by external "
               "influences, such as access. In these cases enclosures need "
               "only to have a degree of protection IP20, in accordance with "
               "BS/EN 60529¹⁵, which is effectively the degree of protection "
               "necessary to prevent live parts being touched. In general, "
               "however, apparatus is fitted with an enclosure of a much "
               "higher integrity for other reasons, for example, as "
               "weatherproofing. What this means is that, except in very "
               "special circumstances, the apparatus enclosure will be "
               "determined by industrial reliability and basic safety "
               "requirements, rather than those of intrinsic safety. This "
               "means that requirements for enclosures which are necessary "
               "for the other protection concepts for the following reasons "
               "are not applied in the case of intrinsic safety:"))
    b.append(note("<b>Note on the italic emphasis in 13.9.1.</b> The words "
                  "'not applied' are italic in the print and the raw layer "
                  "garbles them as 'nof applied'; the render reading and the "
                  "italic emphasis are retained."))
    b.append(note("<b>Note on the footnote superscript after BS/EN 60529.</b> "
                  "The raw layer reads 'BS/EN 6052915' while the render shows "
                  "'BS/EN 60529¹⁵'; the superscript reference numeral is "
                  "preserved."))

    # C62 - indented seven-line list, printed p.374 (raw 16338-16347).
    b.append(p("enclosure opening delay to allow discharge of energy storing "
               "devices;<br>"
               "specific requirements for plastics material to ensure "
               "adequate performance<br>(excluding static charge "
               "capability);<br>"
               "specific requirements for threaded holes in plastics and "
               "light metal<br>(aluminium, etc.) enclosures;<br>"
               "requirements for construction of bushings, interlocking "
               "devices and<br>fasteners;<br>"
               "requirements for cementing materials and actions;<br>"
               "requirements for connection facilities, terminals and "
               "terminal compart-<br>ments;<br>"
               "impact testing requirements for enclosures to ascertain "
               "their strength."))
    b.append(note("<b>Note on the seven enclosure exclusions.</b> They are "
                  "printed as an indented list without bullets or numbers, "
                  "and the sixth wraps mid-word as 'compart-ments'. The line "
                  "breaks and hanging indentation are kept in the English "
                  "text; the Vietnamese translates the items."))

    # C63 (printed p.374 / PDF p.395, raw 16348-16350; continues on p.375).
    b.append(p("With the exception of drop testing for portable apparatus, "
               "therefore, the only requirements in such cases are those "
               "which are specified within the Standards related to the "
               "protection concept itself. This is because the"))

    # C64 - continuation of C63 (printed p.375, raw 16353-16359).
    b.append(p("protection is within the enclosed components and assemblies "
               "themselves, and not the enclosure. Thus exposure of the "
               "circuits will not lead to a dangerous condition as the "
               "circuits remain intrinsically safe. A situation where there "
               "was no enclosure because of damage would not be tolerated "
               "for long periods as the possibility of environmental attack "
               "causing maloperation of the apparatus could not be "
               "tolerated, even though it remained intrinsically safe."))

    # C65 (printed p.375 / PDF p.396, raw 16360-16373).
    b.append(p("Unlike other protection concepts intrinsic safety permits, "
               "in special circumstances, apparatus to be in more than one "
               "enclosure provided the two parts of the apparatus can be "
               "shown to be unique in their interconnection. This is because "
               "of the use of the technique in such things as portable radio "
               "transceivers and similar devices. Later in this chapter "
               "intrinsically safe systems will be discussed and there will "
               "be seen to be some similarity between these and the portable "
               "radio transceiver with a hand microphone on a short lead. To "
               "use the system concept for such equipment, where the two "
               "parts are manufactured and supplied together, would be "
               "excessively cumbersome and therefore they can be said to "
               "fall within the definition of apparatus for intrinsic safety. "
               "There may well be other similar situations but it must be "
               "stressed that they are exceptional and there must clearly "
               "be little possibility of interchange between different "
               "parts of different composite apparatus of this type."))

    # C66 - heading 13.9.2, printed p.375.
    b.append(h4("13.9.2 Internal layout (wiring, printed circuit boards, etc)",
                "13.9.2 Internal layout (wiring, printed circuit boards, etc)"))

    # C67 (printed p.375 / PDF p.396, raw 16375-16382).
    b.append(p("Wiring and tracks on printed circuit boards can, in "
               "principle, be uninsulated (bare) conductors. If this is so "
               "they may come into contact with one another and create "
               "faults. This is not a great problem with printed circuit "
               "tracks as they are rigidly placed, but normal conductors or "
               "conductors on flexible printed wiring substrates are not. In "
               "addition, there is the possibility that insulated wires or "
               "tracks may also come into contact and in such cases the "
               "quality of the insulation is important. Insulation normally "
               "means a plastic or elastomeric coating on the conductor, and "
               "varnishes are specifically identified as not being "
               "considered as insulation."))

    # C68 (printed p.375 / PDF p.396, raw 16383-16394).
    b.append(p("The insulation on wires of intrinsically safe circuits and "
               "non-intrinsically safe circuits also has to meet certain "
               "minimum requirements where its failure could adversely "
               "affect intrinsic safety and its thickness is not in "
               "accordance with Tables 13.7 and 13.8. If no fault between "
               "wires can be tolerated the insulated wires of either the "
               "intrinsically safe circuit or the non-intrinsically safe "
               "circuit must be within a screen which is earthed, and "
               "sufficiently robust to carry any current which may flow from "
               "either circuit during the operating time of protection "
               "devices such as fuses. If no such screen exists an "
               "alternative is to insulate the intrinsically safe wires with "
               "insulation which will withstand an rms ac test voltage of at "
               "least 2000V. This latter solution is only acceptable in ’ib’ "
               "circuits. It is often necessary to include an additional "
               "insulating sleeve over the wire to achieve this."))
    b.append(note("<b>Note on '2000V'.</b> The print writes '2000V' with no "
                  "space in C68, whereas C73 prints '30V'. The spacing is "
                  "kept as printed."))

    # C69 (printed p.376 / PDF p.397, raw 16397-16400).
    b.append(p("There are certain minimum values (see Table 13.8) below which "
               "failure of separations will be considered as a non-countable "
               "fault, such separations being measured with possible movement "
               "of conductors being chosen to give minimum values. The "
               "situations which need consideration are as follows."))

    # C70 - italic spot heading, printed p.376.
    b.append(h4("Clearance", "Clearance"))

    # C71 (printed p.376 / PDF p.397, raw 16402-16408).
    b.append(p("This is the shortest distance between two uninsulated "
               "conductors measured through air. It is not necessarily a "
               "line-of-sight measurement as it could be around an "
               "insulating barrier which must be at least 0.9 mm thick and "
               "sufficiently rigid to withstand a lateral pressure of 30 N. "
               "Figure 13.16 shows how clearance is measured. Where an "
               "earthed metallic barrier is placed between two conductors it "
               "is not necessary to measure the clearance between them, but "
               "where the metallic barrier is isolated it is and the "
               "thickness of the barrier should be deducted from the value "
               "obtained."))

    # C72 - italic spot heading, printed p.376.
    b.append(h4("Creepage", "Creepage"))

    # C73 (printed p.376 / PDF p.397, raw 16410-16431).
    b.append(p("Creepage distances are measured in a similar way to "
               "clearances but here the distance must be along an insulating "
               "surface (e.g., the surface of a printed circuit board or a "
               "terminal block. The Comparative Tracking Index (CTI, see BS "
               "5901¹⁶) of the insulating surface is important here as it "
               "must reach a minimum value to ensure sufficient insulation "
               "quality, except where the voltage between the two conductors "
               "is below 30V as at such low voltages it is considered that "
               "CTI is much less important. If the insulating material and "
               "the conductors are all covered by an insulating coating, "
               "this protects the insulation from degradation and CTI ceases "
               "to be important and, because of the protection from the "
               "environment provided by the coating, the creepage distances "
               "can be significantly reduced. Where, however, the insulating "
               "materials and/or the conductors exit the coating, such "
               "reductions are not permitted and the insulating material "
               "and/or the coating must have the minimum required CTI. The "
               "coating must be a conformal coating which adheres to and "
               "completely covers the conductors and insulation to which "
               "the relaxation is applied. If the coating is brushed on, "
               "produced by dipping the assembly into the coating, or "
               "produced by vacuum impregnation only one coat is necessary. "
               "Where it is applied by other methods, such as spraying, then "
               "two separate coats need to be applied. If a solder mask is "
               "applied and is not damaged during the soldering operation, "
               "only one additional coat is required whatever the method of "
               "application. The method of measuring creepage distances is "
               "shown in Fig. 13.17, 13.18 and 13.19."))
    b.append(note("<b>Note on the footnote superscript after BS 5901.</b> "
                  "The raw layer reads 'BS 590116' while the render shows "
                  "'BS 5901¹⁶'; the superscript is preserved."))
    b.append(note("<b>Note on the unclosed parenthesis in the Creepage "
                  "paragraph.</b> '...along an insulating surface (e.g., the "
                  "surface of a printed circuit board or a terminal block. "
                  "The Comparative Tracking Index (CTI, see BS 5901¹⁶)...' "
                  "— the first parenthesis is never closed in the print. It "
                  "is kept open; the Vietnamese follows the intended "
                  "meaning."))

    # C74 - italic spot heading, printed p.376.
    b.append(h4("Separation", "Separation"))

    # C75 (printed p.376 / PDF p.397, raw 16433-16435; continues on p.377).
    b.append(p("Separation distances are the distances which must be "
               "achieved between bare live conductors, either through solid "
               "insulation or encapsulation separations through solid "
               "insulation, being less than that through encapsulation "
               "reflecting the higher quality of insulation which is "
               "normally the case. The "))

    # C76 - continuation of C75 (printed p.377, raw 16438-16444; sentence
    # continues beyond PDF p.399, outside this module's scope).
    b.append(p("method of measurement of separation distances is to measure "
               "the shortest distance between the two conductors through "
               "the insulation. Insulating partitions are not relevant in "
               "the case of those embedded in solid insulation but in the "
               "unlikely case of an insulating partition embedded in "
               "encapsulant, the effects of the partition can be taken into "
               "account. Methods of measurement are shown in Fig. 13.16. "
               "Table 13.8 gives the minimum values of clearances, creepage "
               "distances and separations which need to be achieved, so that "
               "breakdown between"))
    b.append(note("<b>Note on the sentence at the page boundary.</b> The "
                  "span ends mid-sentence at 'so that breakdown between' on "
                  "printed p.378 (PDF p.399); the continuation is on the next "
                  "page, outside this module's scope, and is not supplied "
                  "from conjecture."))

    # Fig. 13.16 - printed p.377 (PDF p.398), after C76.
    b.append(fig(16, FC.fig_f1316()))
    b.append(note("<b>Note on the rib labels in Fig. 13.16.</b> The raw layer "
                  "reads 'Rib (20.9 mm width)' and garbles the dimension "
                  "lines; the render shows 'Rib (≥0.9 mm width)' and 'Rib "
                  "(<0.9 mm width)'. The render reading is retained and the "
                  "caption has no final full stop."))

    # Fig. 13.17 and Fig. 13.18 - printed p.378 (PDF p.399), figure-only page.
    b.append(fig(17, FC.fig_f1317()))
    b.append(fig(18, FC.fig_f1318()))
    b.append(note("<b>Note on the labels of Fig. 13.18.</b> The raw layer "
                  "reduces the labels to 'tl', 'Insulant' and 'd = creepage "
                  "distance'; the render supplies 'Conductor', 'Insulant', "
                  "'Metal screw (earthed)', '<3', '≥3' and '≥1', with '<' "
                  "strict and '≥' carrying the equality bar. The captions "
                  "end with a full stop."))
    return "".join(b)
