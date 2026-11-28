# -*- coding: utf-8 -*-
"""Chapter 12, module F - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 325-330 (PDF pp. 346-351).

Covers the continuation of 12.3.7 "Rotating machines" (rotor/stator
clearances and the air-gap formula, insulation of conductors, machine
temperatures, the te time and its starting-current ratio, the stalled-rotor
current limit and discharges in rotating machines) and 12.3.8 "Other types
of apparatus". Figures 12.15 and 12.16 sit at their printed positions across
printed pp. 327-328. The chapter shell owns the chapter h2, the printed
sixteen-item reference list, the glossary, the source-quirk note and the
copyright; this module emits no reference list of its own.

Printed quirks are kept in the English text (the brace-like air-gap formula
with its juxtaposed brackets, the bare '50/780', the curly 'sag' quotes,
'300 °C', '(see Fig. 12.15.).', 'temperature raise which this infers',
'as again', '3000V' beside '3000 V', the ¹⁵/¹⁶ markers, 'invertors' and lower
case 'ac') with bilingual notes; the Vietnamese follows the intended meaning.
This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, fig
import mcmillanfig12_d as FD


def body_vi():
    b = []

    # Printed p.325. Continuation of the 12.3.7 rotating-machines paragraph
    # from the previous module; the sentence starts mid-flight in the print.
    b.append(p("chúng cần được bảo vệ bằng một nguyên lý bảo vệ khác và thường "
               "là dạng chống cháy, tạo thành một dạng bảo vệ phức hợp cho máy."))
    b.append(note("<b>Lưu ý về ranh giới câu đầu.</b> Đoạn đầu tiên trong phạm "
                  "vi này bắt đầu giữa câu, được tiếp nối từ trang in trước "
                  "(nằm ngoài phạm vi module); chữ 'chúng' được giữ ở dạng tiếp "
                  "nối như trong bản in."))

    b.append(h4("Khe hở rô-to/stator", "Rotor/stator clearances"))
    b.append(p("Điều cần thiết trước hết là ngăn ngừa va chạm giữa rô-to và "
               "stator ở mức tối đa có thể trong mọi điều kiện vận hành, cũng "
               "như các ứng suất do những điều kiện đó tạo ra. Điều này được "
               "thực hiện bằng cách quy định một khe hở tối thiểu giữa rô-to "
               "và stator khi máy đang đứng yên — đây là trường hợp xấu nhất "
               "vì bất kỳ độ võng nào của rô-to do khối lượng của nó sẽ hiện "
               "ra. Khe hở tối thiểu này được suy ra từ một công thức thoạt "
               "nhìn có vẻ phức tạp như sau:"))
    b.append(note("<b>Lưu ý về dấu ngoặc đơn cong trong bản in.</b> Bản in "
                  "viết 'any ‘sag’ of the rotor' với một cặp dấu ngoặc đơn "
                  "cong; dạng này được giữ trong bản tiếng Anh, còn bản tiếng "
                  "Việt dịch theo nghĩa 'độ võng'."))
    b.append(p("<b>Khe hở không khí = {0.15 + [D − 50/780][0.25 + "
               "(0.75 × n/1000)]}</b>      mm"))
    b.append(note("<b>Lưu ý về công thức khe hở không khí trong bản in.</b> "
                  "Bản in viết 'Air gap = {0.15 + [D − 50/780][0.25 + "
                  "(0.75 × n/1000)]}      mm': hai nhóm ngoặc vuông đứng kề "
                  "nhau không có dấu nhân, dấu ngoặc ngoài giống ngoặc nhọn, "
                  "và mẫu số là '50/780' chứ không phải phân số xếp chồng. "
                  "Lớp văn bản OCR đọc nhầm thành '(0.15 + [D - 50/780][0.25 "
                  "+ (0.75 x n/1000)]1 mm'. Có thể ý định là (0.15 + "
                  "[D − 50]/780) × [0.25 + (0.75 × n/1000)], nhưng không tự "
                  "ý sửa; dấu nhân '×' thật từ trang render được giữ."))
    b.append(p("trong đó D = đường kính rô-to tính bằng mm (với giá trị tối "
               "thiểu là 75 mm và giá trị tối đa là 750 mm)"))
    b.append(p("n = tốc độ máy tính bằng vòng/phút (tần số × 50/số cặp cực "
               "trên mỗi pha)"))
    b.append(note("<b>Lưu ý về thứ tự dòng trong khối 'where'.</b> Lớp văn bản "
                  "OCR gán sai các dòng gói: 'and a maximum of 750 mm)' bị "
                  "dính vào dòng D và 'per phase)' bị dính vào dòng n; trang "
                  "render cho thấy cách ghép đúng như các dòng trên."))
    b.append(p("Giá trị trên được nhân với một giá trị suy ra từ chiều dài "
               "lõi (mm)/1,75 × đường kính lõi (mm) khi giá trị này vượt quá "
               "1, rồi lại được nhân với 1,5 khi dùng ổ trượt kiểu bọc thay "
               "vì ổ lăn. Phép tính này trông phức tạp hơn nhiều so với phép "
               "tính dùng trong ấn bản đầu tiên của Tiêu chuẩn Châu Âu "
               "(BS 5501, Phần 6) nhưng, trên thực tế, không ảnh hưởng đáng "
               "kể đến yêu cầu về khe hở, cho ra trung bình một giá trị thấp "
               "hơn giá trị từng cần thiết trước đây nhưng thường nằm trong "
               "khoảng 10 phần trăm so với giá trị đó."))
    b.append(note("<b>Lưu ý về cách ghi 'European Standard (BS 5501, Part "
                  "6)'.</b> Bản in gọi BS 5501 — một Tiêu chuẩn Anh — là "
                  "'ấn bản đầu tiên của Tiêu chuẩn Châu Âu'. Cụm này được giữ "
                  "nguyên theo bản in và được ghi chú rõ, không tự ý chỉnh "
                  "cho khớp."))

    b.append(h4("Cách điện cho dây quấn stator và rô-to",
                "Insulation of stator and rotor conductors"))
    b.append(note("<b>Lưu ý về chữ hoa ở tiêu đề.</b> Lớp văn bản OCR viết "
                  "thường 'insulation of stator and rotor conductors'; trang "
                  "render cho thấy chữ I viết hoa. Tiêu đề dùng dạng đúng từ "
                  "trang render."))
    b.append(p("Các yêu cầu cách điện thông thường áp dụng cho cả stator và "
               "rô-to quấn dây nhưng, trong trường hợp máy, các ứng suất từ "
               "tính có nghĩa là phải đặc biệt chú ý đến việc đảm bảo độ chắc "
               "chắn của các dây quấn để ngăn hư hỏng cách điện do chuyển "
               "động. Khi dùng rô-to lồng sóc, các thanh rô-to không được "
               "cách điện với phần lõi từ tính của rô-to và, ngoài sự cần "
               "thiết phải đảm bảo liên kết chắc chắn giữa các thanh với "
               "nhau, tiếp xúc giữa các thanh và lõi rô-to cần cực kỳ chặt "
               "chẽ để đảm bảo không phát sinh tia lửa giữa các thanh rô-to "
               "và giữa các thanh rô-to với lõi, đặc biệt trong lúc khởi "
               "động khi ứng suất ở mức lớn nhất. Để đạt được điều này, lồng "
               "sóc kể cả các vòng đầu thường được đúc thành một khối duy "
               "nhất hoặc các vòng và thanh được hàn đồng hay hàn lại với "
               "nhau. Độ chặt của chúng trong các rãnh rô-to đạt được bằng "
               "cách đúc nhôm vào các rãnh, nhưng cũng chấp nhận các phương "
               "pháp lót rãnh bổ sung, nêm hoặc chốt. Hình 12.14 cho thấy "
               "một lồng sóc điển hình đơn giản."))
    b.append(note("<b>Lưu ý về cách gọi số hình trong bản in.</b> Trang in "
                  "325 viết đầy đủ 'Figure 12.14', còn các trang in 327 và "
                  "328 dùng 'Fig. 12.15' và 'Fig. 12.16'. Mỗi dạng được giữ "
                  "nguyên theo bản in."))

    # Printed p.326.
    b.append(h4("Nhiệt độ máy", "Machine temperatures"))
    b.append(p("Không nhiệt độ nào bên trong máy được vượt quá nhiệt độ tối "
               "đa của cấp nhiệt độ hoặc nhiệt độ giới hạn của các vật liệu "
               "dùng trong máy, và có một giới hạn trên chung là 300 °C ngay "
               "cả khi các giá trị đó vượt quá nhiệt độ này. Các điều kiện "
               "cần được tính đến là khởi động và chạy ở tải đầy với các quá "
               "tải được thừa nhận, kể cả điều kiện rô-to bị kẹt. Với một máy "
               "thông thường như máy lồng sóc, không có cách nào đo nhiệt độ "
               "rô-to khi đang chạy, và việc giới hạn nhiệt độ phải đạt được "
               "bằng cách phát hiện nhiệt độ stator hoặc giám sát dòng máy "
               "tiêu thụ, mối quan hệ giữa nhiệt độ stator và rô-to được xác "
               "nhận trong thiết kế của máy."))
    b.append(note("<b>Lưu ý về ký hiệu độ.</b> Bản in ghi '300 °C' với ký hiệu "
                  "độ; lớp văn bản OCR đọc nhầm thành '300 \"C'. Dấu ° được "
                  "giữ theo bản in."))
    b.append(p("Đối với các máy chỉ khởi động không thường xuyên và không có "
               "điều kiện khởi động khắc nghiệt (ví dụ, được khởi động với "
               "tải đầy), có thể kiểm soát nhiệt độ bằng một bộ khởi động "
               "trực tiếp thông thường có thiết bị bảo vệ quá tải nhiệt "
               "(bảo vệ quá tải trễ thời gian nghịch). Điều này được chấp "
               "nhận với điều kiện thiết bị không chỉ giám sát dòng khởi "
               "động và ngắt nếu dòng quá lớn, mà còn ngắt máy nếu rô-to bị "
               "kẹt, trước khi nhiệt độ của bất kỳ phần nào của máy vượt quá "
               "nhiệt độ hoạt động tối đa của vật liệu cách điện, hoặc đạt "
               "đến giới hạn cấp nhiệt độ. Điều sau cùng được thực hiện bằng "
               "cách đo thời gian"))
    b.append(note("<b>Lưu ý về ranh giới câu ở cuối trang in 326.</b> Đoạn "
                  "trên kết thúc bằng 'measurement of the time' vì câu tiếp "
                  "tục sang trang in 327, trước Hình 12.15; không thêm dấu "
                  "chấm cuối."))

    # Printed p.327.
    b.append(p("cần để máy đạt đến điều kiện giới hạn nếu, khi máy đã chạy ở "
               "nhiệt độ môi trường cực đại và ở tải định mức cho đến khi "
               "nhiệt độ ổn định, rô-to bị kẹt. Thời gian này được gọi là "
               "thời gian tₑ (xem Hình 12.15). Do tốc độ tăng nhiệt độ có thể "
               "có trong điều kiện rô-to kẹt, giá trị tối thiểu được quy định "
               "cho thời gian này tùy theo tỷ số giữa dòng kẹt (khởi động) "
               "(Iₐ) và dòng chạy định mức ở tải đầy (Iₙ), và các giá trị này "
               "được thể hiện trong Hình 12.16. Việc giảm thời gian tₑ chỉ "
               "có thể thực hiện nếu chứng minh được rằng thiết bị bảo vệ "
               "cụ thể được dùng ngắt máy trong thời gian quy định, và trong "
               "bất kỳ trường hợp nào thời gian tₑ dưới 5 giây không được coi "
               "là chấp nhận được vì tốc độ tăng nhiệt độ mà điều đó hàm ý. "
               "Việc quy định thời gian tₑ là không cần thiết khi máy được "
               "bảo vệ bằng các thiết bị cảm biến nhiệt trong dây quấn stator "
               "ngắt máy trước khi đạt đến nhiệt độ giới hạn."))
    b.append(note("<b>Lưu ý về chỉ số dưới và một lỗi đọc OCR trong đoạn "
                  "này.</b> Bản in dùng tₑ, Iₐ và Iₙ dạng chỉ số dưới; lớp "
                  "văn bản OCR đọc nhầm thành 't,', 'Ia' và 'In'. Nó cũng đọc "
                  "nhầm 'machine' thành 'machme'. Bản dịch dùng dạng đúng từ "
                  "trang render."))
    b.append(note("<b>Lưu ý về dấu chấm sau dấu ngoặc.</b> Bản in viết '(see "
                  "Fig. 12.15.).' với một dấu chấm sau dấu ngoặc đóng; dạng "
                  "này được giữ nguyên trong bản tiếng Anh, trong bản tiếng "
                  "Việt dùng dạng gọn '(xem Hình 12.15)' theo ý định."))
    b.append(note("<b>Lưu ý về cách diễn đạt 'rate of temperature raise which "
                  "this infers'.</b> Bản in dùng 'raise' và 'infers' ở những "
                  "chỗ thường dùng 'rise' và 'implies'; dạng này được giữ "
                  "nguyên trong bản tiếng Anh, còn bản tiếng Việt dịch theo "
                  "nghĩa 'tốc độ tăng nhiệt độ mà điều đó hàm ý'."))
    b.append(p("Khi một máy phải chịu điều kiện khởi động khắc nghiệt, hoặc "
               "do được khởi động với tải đầy hoặc theo các khoảng thời gian "
               "đều đặn (chế độ làm việc chu kỳ), người ta cho rằng chỉ cảm "
               "biến nhiệt bên trong stator được chấp nhận làm phương tiện "
               "giới hạn nhiệt độ vì độ tăng nhiệt là lớn nhất hoặc máy đã ở "
               "nhiệt độ cao khi khởi động. Trong những điều kiện đó, thời "
               "gian tₑ không còn liên quan. Việc đưa các phần tử cảm biến "
               "vào dây quấn stator đương nhiên phải đáp ứng các yêu cầu đối "
               "với cảm biến nhiệt trong dây quấn nói chung. Một phương pháp "
               "xác định cái gọi là điều kiện khắc nghiệt liên quan đến tải "
               "khởi động (nhưng không phải chu kỳ làm việc) là xác định "
               "thời gian máy đạt đến tốc độ danh định. Thời gian này không "
               "được vượt quá 1,7 tₑ. Chu kỳ làm việc là khi một máy được "
               "khởi động"))
    b.append(fig(15, FD.fig_f1215()))

    # Printed p.328. Figure 12.16 heads the page; the sentence interrupted
    # above resumes below it.
    b.append(fig(16, FD.fig_f1216()))
    b.append(note("<b>Lưu ý về vị trí Hình 12.15 và 12.16.</b> Câu 'Duty "
                  "cycling is where a machine is started' kết thúc trang in "
                  "327 ngay trước Hình 12.15; phần tiếp theo nằm ở đầu trang "
                  "in 328 sau Hình 12.16. Chú thích in của hai hình giữ các "
                  "dạng 't, time determination', 'IJn ratios' và '5 second' "
                  "(dạng OCR của tₑ và Iₐ/Iₙ, với 'second' số ít); không sửa "
                  "chú thích."))
    b.append(p("thường xuyên như một phần của cách sử dụng theo thiết kế của "
               "nó, và việc khởi động lặp lại như vậy có khả năng xảy ra khi "
               "máy, sau khi dừng, có khả năng được khởi động lại trước khi "
               "nguội về nhiệt độ môi trường. Thời gian nguội như vậy thường "
               "vượt quá một giờ và, để an toàn, bất kỳ máy nào được khởi "
               "động thường xuyên hơn một lần sau mỗi hai giờ nên được coi "
               "là làm việc theo chu kỳ."))
    b.append(note("<b>Lưu ý về ranh giới câu sau hai hình.</b> Đoạn trên tiếp "
                  "nối câu bị ngắt trước Hình 12.15 trên trang in 327; trong "
                  "bản in, Hình 12.16 đứng đầu trang in 328 trước phần tiếp "
                  "nối này."))

    b.append(h4("Dòng rô-to kẹt/khởi động", "Starting/stalled rotor current"))
    b.append(p("Là yêu cầu cuối cùng, không được phép để bất kỳ máy nào có "
               "dòng rô-to kẹt (khởi động) lớn hơn mười lần dòng chạy ở tải "
               "đầy, vì một lần nữa điều đó sẽ cho thấy tốc độ tăng nhiệt độ "
               "rất cao."))
    b.append(note("<b>Lưu ý về cụm 'as again'.</b> Bản in viết 'as again this "
                  "would indicate a very high rate of temperature rise'; dạng "
                  "này được giữ nguyên trong bản tiếng Anh, còn bản tiếng Việt "
                  "dịch theo ý định."))

    b.append(h4("Phóng điện trong máy quay", "Discharges in rotating machines"))
    b.append(p("Bất chấp các yêu cầu này, đã có nhiều lo ngại đáng kể được "
               "bày tỏ về việc sử dụng máy an toàn tăng cường, đặc biệt là "
               "những máy làm việc ở điện áp cao, do một số lần bầu khí quyển "
               "chất nổ bị cháy nổ bởi các máy như vậy trong điều kiện khởi "
               "động. Công trình do ERA Technology Ltd¹⁵ thực hiện theo yêu "
               "cầu của Ban Điều hành An toàn và Sức khỏe cho thấy có nguy cơ "
               "thực sự phát sinh cháy nổ do tia lửa ở cả rô-to và stator. "
               "Tia lửa phát sinh trong các dây quấn đầu stator trong điều "
               "kiện khởi động, trong nhiều trường hợp, có khả năng gây cháy "
               "nổ và điều này đã dẫn đến việc Ban Điều hành An toàn và Sức "
               "khỏe (Health &amp; Safety Executive) đưa ra cảnh báo¹⁶ không "
               "sử dụng các máy làm việc ở điện áp đường dây vượt quá "
               "3000 V. Các cuộc điều tra về vấn đề này vẫn đang tiếp tục "
               "nhưng sẽ là khôn ngoan nếu xem xét giải pháp thay thế là máy "
               "chống cháy"))
    b.append(note("<b>Lưu ý về ký hiệu chú thích và khoảng cách ở 3000 V.</b> "
                  "Bản in dùng ¹⁵ sau 'ERA Technology Ltd' và ¹⁶ sau "
                  "'warning', có dấu phẩy ngay sau ¹⁶, và viết 'the Health and "
                  "Safety Executive' rồi 'the Health &amp; Safety Executive' "
                  "trong cùng một đoạn. Trang in 328 ghi '3000V' (không dấu "
                  "cách), trang in 329 ghi '3000 V' (có dấu cách); cả hai được "
                  "giữ theo bản in. Hai ký hiệu tương ứng với tài liệu tham "
                  "khảo 15 và 16 do phần shell của chương cung cấp."))

    # Printed p.329.
    b.append(p("máy chống cháy, ít nhất là đối với những máy làm việc ở điện "
               "áp trên 3000 V, cho đến khi vấn đề này được giải quyết trọn "
               "vẹn. Dĩ nhiên, cũng có thể khôn ngoan nếu chỉ dùng máy chống "
               "cháy cho mọi lắp đặt cho đến khi vấn đề được giải quyết, vì "
               "hiểu biết hiện tại về nó vẫn chưa đầy đủ."))

    b.append(h4("12.3.8 Các loại thiết bị khác",
                "12.3.8 Other types of apparatus"))
    b.append(p("An toàn tăng cường về nguyên tắc áp dụng được cho các loại "
               "thiết bị khác ngoài những loại đã thảo luận. Tuy nhiên, để "
               "áp dụng được, thiết bị phải được xác định đầy đủ thông số và "
               "các yêu cầu dùng sẽ cần được chọn từ các yêu cầu cơ bản phù "
               "hợp với loại thiết bị, cũng như từ các yêu cầu bổ sung phù "
               "hợp cho các loại thiết bị đã thảo luận. Không thể áp dụng an "
               "toàn tăng cường cho thiết bị dùng chất bán dẫn và các phần tử "
               "tương tự vì chúng không có tiêu chí thiết kế vật lý được xác "
               "định rõ để có thể áp dụng an toàn tăng cường."))
    b.append(p("Sự nóng lên của máy quay cũng bị ảnh hưởng bởi dạng sóng nguồn "
               "cấp. Dù điều này thường không gây vấn đề vì dạng sóng chính là "
               "của nguồn cấp, nó có thể trở thành vấn đề trong trường hợp máy "
               "tốc độ thay đổi. Các máy này thường được chạy từ bộ biến tần "
               "tạo ra dòng xoay chiếu ở tần số thay đổi để đạt được sự thay "
               "đổi tốc độ. Đầu ra của các thiết bị này không dễ đoán như "
               "nguồn lưới thông thường và chúng thường chứa nhiều hài hơn "
               "đáng kể (hài này không hỗ trợ gì cho bộ truyền mà lại tỏa "
               "nhiệt trong máy). Vì vậy, khi dùng bộ biến tần như vậy với máy "
               "an toàn tăng cường, phải chứng minh được rằng máy vẫn giữ "
               "được các đặc tính an toàn tăng cường khi dùng với bộ biến tần "
               "cụ thể đang xét. Điều quan trọng cần lưu ý là loại biến tần "
               "cụ thể được dùng không chỉ là một thiết bị cùng dòng sản "
               "phẩm hoặc một thiết bị tương tự."))
    b.append(note("<b>Lưu ý về 'invertors' và 'ac' trong bản in.</b> Bản in "
                  "viết 'Where such invertors are used' (chính tả cũ) nhưng "
                  "dùng 'inverter'/'inverters' ở các chỗ khác trong cùng một "
                  "đoạn, và viết thường 'ac' mà không giải thích. Các dạng "
                  "này được giữ trong bản tiếng Anh; bản tiếng Việt dùng "
                  "'bộ biến tần' và 'dòng xoay chiếu' theo ý định."))
    return "".join(b)


def body_en():
    b = []

    # Printed p.325. Continuation of the 12.3.7 rotating-machines paragraph
    # from the previous module; the sentence starts mid-flight in the print.
    b.append(p("they need to be protected by another protection concept and "
               "are usually flameproof giving a composite form of protection "
               "to the machine."))
    b.append(note("<b>Note on the opening sentence boundary.</b> The first "
                  "paragraph in this span begins mid-sentence, carried over "
                  "from the preceding printed page (outside this module); the "
                  "opening 'they' is left lower-case as printed."))

    b.append(h4("Rotor/stator clearances", "Rotor/stator clearances"))
    b.append(p("The first necessity is to prevent rotor/stator clashes as far "
               "as possible in all operating conditions, and the stresses "
               "created by those conditions. This is done by specifying a "
               "minimum clearance between rotor and stator when the machine "
               "is at rest which is the worst case as any ‘sag’ of the rotor, "
               "due to its mass, will be present. This minimum clearance is "
               "derived from a formula which at first glance appears complex "
               "and is as follows:"))
    b.append(note("<b>Note on the printed curly quotes.</b> The print reads "
                  "'any ‘sag’ of the rotor' with a pair of curly single "
                  "quotation marks; they are retained in the English text "
                  "while the Vietnamese follows the intended sense."))
    b.append(p("<b>Air gap = {0.15 + [D − 50/780][0.25 + "
               "(0.75 × n/1000)]}</b>      mm"))
    b.append(note("<b>Note on the printed air-gap formula.</b> The print reads "
                  "'Air gap = {0.15 + [D − 50/780][0.25 + (0.75 × n/1000)]}    "
                  "  mm': the two square-bracket groups are juxtaposed with "
                  "no multiplication sign, the outer glyphs are brace-like, "
                  "and the denominator is '50/780' rather than a stacked "
                  "fraction. The OCR text layer reads '(0.15 + [D - "
                  "50/780][0.25 + (0.75 x n/1000)]1 mm'. The likely intent is "
                  "(0.15 + [D − 50]/780) × [0.25 + (0.75 × n/1000)], but the "
                  "printed form is reproduced without silent correction; the "
                  "true multiplication sign '×' is kept."))
    b.append(p("where D = rotor diameter in mm (subject to a minimum of "
               "75 mm and a maximum of 750 mm)"))
    b.append(p("n = machine speed in revs/min (frequency × 50/pole pairs per "
               "phase)"))
    b.append(note("<b>Note on the line order of the 'where' block.</b> The OCR "
                  "text layer misorders the wrapped lines: 'and a maximum of "
                  "750 mm)' is attached to the D line and 'per phase)' to the "
                  "n line, whereas the page render associates them as "
                  "transcribed above."))
    b.append(p("The above figure is multiplied by a figure derived from core "
               "length (mm)/1.75 × core diameter (mm) where this exceeds 1 and "
               "further multiplied by 1.5 where sleeve, rather than rolling "
               "element bearings, are used. This calculation looks much more "
               "complex than that used in the first edition of the European "
               "Standard (BS 5501, Part 6) but, in effect, does not "
               "significantly affect the clearance requirements, giving on "
               "average a figure which is lower than the figure which would "
               "previously have been necessary but normally within around "
               "10 per cent of that figure."))
    b.append(note("<b>Note on 'the first edition of the European Standard "
                  "(BS 5501, Part 6)'.</b> The print attributes BS 5501, a "
                  "British Standard, to a European Standard. The wording is "
                  "kept verbatim and flagged rather than silently corrected."))

    b.append(h4("Insulation of stator and rotor conductors",
                "Insulation of stator and rotor conductors"))
    b.append(note("<b>Note on the heading capitalisation.</b> The OCR text "
                  "layer has a lower-case 'insulation of stator and rotor "
                  "conductors'; the page render shows a capital I. The "
                  "heading follows the render."))
    b.append(p("The normal insulation requirements apply to both stators and "
               "wound rotors but, in the case of machines, the magnetic "
               "stresses will mean that special attention must be given to "
               "ensuring the security of windings to prevent insulation "
               "damage due to movement. Where squirrel cage rotors are used "
               "the rotor bars are not insulated from the rotor magnetic "
               "base and, in addition to the necessity to ensure secure "
               "interconnection between the bars themselves, the contact "
               "between the bars and the rotor core needs to be extremely "
               "firm to ensure that sparking does not occur between rotor "
               "bars and between rotor bars and the core, particularly during "
               "starting when stresses are at their maximum. To achieve this "
               "the squirrel cage including its end rings, is normally either "
               "cast as a single unit or the rings and bars are brazed or "
               "welded together. Their tightness of fit in the rotor slots is "
               "achieved by casting them in the slots with aluminium but "
               "supplementary slot lining, wedging or keying are also "
               "acceptable methods. Figure 12.14 shows a typical simple "
               "squirrel cage."))
    b.append(note("<b>Note on the figure-reference forms.</b> Printed p. 325 "
                  "spells out 'Figure 12.14' while printed pp. 327-328 use "
                  "'Fig. 12.15' and 'Fig. 12.16'. Each form is kept as "
                  "printed."))

    # Printed p.326.
    b.append(h4("Machine temperatures", "Machine temperatures"))
    b.append(p("No temperature within the machine should exceed either the "
               "maximum temperature for the temperature class or the limiting "
               "temperature for the materials used in the machine, and there "
               "is an overall upper limit of 300 °C even if these figures "
               "exceed that temperature. The conditions which need to be "
               "taken into account are starting and running under full load "
               "with recognized overloads, including locked rotor conditions. "
               "With a normal machine such as a squirrel cage machine there "
               "is no way of measuring the rotor temperature in service, and "
               "temperature limitation must be achieved by detecting the "
               "stator temperature or monitoring the current drawn by the "
               "machine, the relationship between the stator and rotor "
               "temperature being confirmed in the design of the machine."))
    b.append(note("<b>Note on the degree sign.</b> The print reads '300 °C' "
                  "with a degree sign; the OCR text layer reads '300 \"C'. "
                  "The degree sign is kept as printed."))
    b.append(p("For machines which are only started infrequently and do not "
               "have arduous starting conditions (e.g., being started on full "
               "load for instance) temperature control can be achieved by a "
               "normal direct on-line starter with a thermal overload release "
               "device (inverse time delay overload protection). This is "
               "acceptable provided the device not only monitors starting "
               "current and disconnects if this is excessive, but also "
               "disconnects the machine if the rotor is stalled, before the "
               "temperature of any part of the machine exceeds the maximum "
               "temperature of operation of the insulation, or the temperature "
               "class limit is reached. This latter is achieved by measurement "
               "of the time"))
    b.append(note("<b>Note on the sentence boundary on printed p. 326.</b> "
                  "The paragraph above ends with 'measurement of the time' "
                  "because the sentence continues on printed p. 327 before "
                  "Figure 12.15; no full stop is added."))

    # Printed p.327.
    b.append(p("taken for the machine to reach the limiting condition if, when "
               "it has been operating at its maximum ambient temperature and "
               "at rated load until its temperature has stabilized, the rotor "
               "is stalled. This time is called the tₑ time (see Fig. 12.15.). "
               "Because of the possible rate of rise of temperature in the "
               "stalled rotor condition, minimum figures are set for this "
               "time dependent upon the ratio of stalled (starting) current "
               "(Iₐ) to rated running current at full load (Iₙ) and these are "
               "shown in Fig. 12.16. Reduction of tₑ time is only possible if "
               "it can be shown that the particular protective device used "
               "isolates the machine within the time specified, and in no "
               "circumstances is a tₑ time of less than 5 secs considered as "
               "acceptable because of the rate of temperature raise which "
               "this infers. The specification of tₑ time is not necessary "
               "where a machine is protected by thermal sensing devices in "
               "the stator windings which isolate the machine before the "
               "limiting temperature is reached."))
    b.append(note("<b>Note on subscripts and an OCR misread in this "
                  "paragraph.</b> The print uses subscript tₑ, Iₐ and Iₙ; the "
                  "OCR text layer reads 't,', 'Ia' and 'In'. It also misreads "
                  "'machine' as 'machme'. The translation follows the render."))
    b.append(note("<b>Note on the full stop after the parenthesis.</b> The "
                  "print reads '(see Fig. 12.15.).' with a full stop after the "
                  "closing parenthesis; it is kept verbatim in English, while "
                  "the Vietnamese follows the intended form without the "
                  "stray stop."))
    b.append(note("<b>Note on 'rate of temperature raise which this "
                  "infers'.</b> The print has 'raise' and 'infers' where 'rise' "
                  "and 'implies' would be expected; the wording is kept "
                  "verbatim in English while the Vietnamese follows the "
                  "intended sense."))
    b.append(p("Where a machine is subjected to arduous starting conditions, "
               "either by being started on full load or at regular intervals "
               "(duty cycle operation), it is considered that only temperature "
               "sensing within the stator is acceptable as a means for "
               "temperature limitation because the temperature rise is at its "
               "greatest or the machine is already at elevated temperature "
               "when started. In these circumstances, tₑ time is not relevant. "
               "The inclusion of sensing elements in stator windings must, of "
               "course, satisfy the requirements for temperature sensors in "
               "windings in general. A method of determination of what are "
               "called arduous conditions in relation to starting load (but "
               "not duty cycling) is to determine the time for the machine to "
               "reach full speed. This should not exceed 1.7 tₑ. Duty cycling "
               "is where a machine is started"))
    b.append(fig(15, FD.fig_f1215()))

    # Printed p.328. Figure 12.16 heads the page; the sentence interrupted
    # above resumes below it.
    b.append(fig(16, FD.fig_f1216()))
    b.append(note("<b>Note on the placement of Figures 12.15 and 12.16.</b> "
                  "The sentence 'Duty cycling is where a machine is started' "
                  "ends printed p. 327 just before Figure 12.15; its "
                  "continuation is on printed p. 328 after Figure 12.16. The "
                  "printed captions keep the text-layer forms 't, time "
                  "determination', 'IJn ratios' and '5 second' (OCR forms of "
                  "tₑ and Iₐ/Iₙ, with 'second' in the singular); the captions "
                  "are not corrected."))
    b.append(p("regularly as part of its designed use and such repeat "
               "startings are likely to occur where the machine, after "
               "stopping, is likely to be restarted before it has cooled to "
               "ambient temperature. Such a cooling time is often in excess "
               "of one hour and to be secure, any machine which is started "
               "more frequently than once every two hours should be assumed "
               "to be on a duty cycle."))
    b.append(note("<b>Note on the sentence boundary after the figures.</b> "
                  "The paragraph above resumes the sentence broken before "
                  "Figure 12.15 on printed p. 327; in the print, Figure 12.16 "
                  "heads printed p. 328 ahead of this continuation."))

    b.append(h4("Starting/stalled rotor current",
                "Starting/stalled rotor current"))
    b.append(p("As a final requirement it is not acceptable for any machine "
               "to have a stalled rotor (starting) current of more than ten "
               "times its full load running current as again this would "
               "indicate a very high rate of temperature rise."))
    b.append(note("<b>Note on 'as again'.</b> The print reads 'as again this "
                  "would indicate a very high rate of temperature rise'; the "
                  "wording is retained in English, while the Vietnamese "
                  "follows the intended meaning."))

    b.append(h4("Discharges in rotating machines",
                "Discharges in rotating machines"))
    b.append(p("Notwithstanding these requirements, there has been "
               "considerable concern expressed at the use of increased safety "
               "machines, particularly those operating at high voltages "
               "because of several ignitions of explosive atmospheres by such "
               "machines under starting conditions. Work carried out by ERA "
               "Technology Ltd¹⁵ at the behest of the Health and Safety "
               "Executive showed that there was a real risk of ignition due "
               "to sparking in both the rotor and the stator. The sparking "
               "occurring in the stator end windings in starting conditions "
               "is, in many cases, ignition capable and this has led the "
               "Health &amp; Safety Executive to issue a warning¹⁶, against "
               "the use of machines operating at line voltages in excess of "
               "3000V. Investigations into this problem are ongoing but it "
               "would be wise to consider the alternative of flameproof"))
    b.append(note("<b>Note on footnote markers and the 3000 V spacing.</b> "
                  "The print uses superscript ¹⁵ after 'ERA Technology Ltd' "
                  "and ¹⁶ after 'warning', with a comma after ¹⁶, and writes "
                  "'the Health and Safety Executive' then 'the Health &amp; "
                  "Safety Executive' in the same paragraph. Printed p. 328 "
                  "reads '3000V' without a space while printed p. 329 reads "
                  "'3000 V' with a space; both are kept as printed. The "
                  "markers resolve to references 15 and 16, supplied by the "
                  "chapter shell."))

    # Printed p.329.
    b.append(p("machines at least for those operating at more than 3000 V "
               "until this problem has been fully resolved. It may, of "
               "course, be wise to use only flameproof machines for all "
               "installations until resolution of the problem as the current "
               "understanding of it is not complete."))

    b.append(h4("12.3.8 Other types of apparatus",
                "12.3.8 Other types of apparatus"))
    b.append(p("Increased safety is in principle applicable to other types "
               "of apparatus than those discussed. To apply it, however, the "
               "apparatus must be fully specifiable and the requirements used "
               "will need to be chosen from those basic requirements "
               "appropriate to the type of equipment and those appropriate "
               "from the additional requirements for the types of apparatus "
               "discussed. It is not possible to apply increased safety to "
               "apparatus using semiconductor and similar devices as these "
               "do not have clearly defined physical design criteria to "
               "which increased safety could be applied."))
    b.append(p("The heating of rotating machines is also affected by their "
               "supply waveform. While this is not normally a problem, as the "
               "waveform is that of the supply, it can become so in the case "
               "of variable speed machines. These are often run from inverters "
               "which generate ac at a varying frequency to achieve speed "
               "variation. The output of these devices is not nearly so "
               "predictable as normal mains supplies and they often contain "
               "significantly more harmonic content (which does not assist "
               "the drive but dissipates heat in the machine). Where such "
               "invertors are used with increased safety machines therefore, "
               "the machines must be shown to retain their increased safety "
               "properties when used with the particular inverter in "
               "question. It is important to note that the particular type "
               "of inverter used is not just one of the same range, or a "
               "similar one."))
    b.append(note("<b>Note on 'invertors' and 'ac' in the print.</b> The print "
                  "reads 'Where such invertors are used' (an older spelling) "
                  "while other occurrences in the same paragraph use "
                  "'inverter'/'inverters', and it writes 'ac' in lower case "
                  "without expansion. Both are retained in English; the "
                  "Vietnamese uses the intended terms."))
    return "".join(b)
