# -*- coding: utf-8 -*-
"""Chapter 10, module C (writer W3) - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), raw lines 10954-11217 / printed pp.236-244
(PDF pp.257-265).

Covers numbered section "2 Spigot joints" and its four italic sub-subsections:
composite spigot joints, joints with all of the flamepath in the cylindrical
part, gaskets for weatherproofing (printed "efc."), and fixings in the plane
parts of composite spigot joints. Owns Figures 10.6-10.10 and Tables 10.5
and 10.6, emitted at their printed positions in both bodies. No chapter h2,
no references and no end matter. Wording, standards designations and printed
quirks follow the verified survey brief and the page renders, not the garbled
PDF text layer. VI follows the intended meaning; EN retains the printed
quirks with bilingual notes.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, table, fig
import mcmillanfig10a as FA
import mcmillan_tbl10_1_5 as T1
import mcmillan_tbl10_6_10 as T2


def body_vi():
    b = []
    b.append(h3("2 Mối nối spigot", "2 Spigot joints"))

    # printed p.236 (PDF 257), LF 10955-10968 - definition of spigot joints
    b.append(p("Mối nối spigot là loại mối nối trong đó khe hở then chốt tạo "
               "thành đường dẫn ngọn lửa được chứa hoàn toàn trong phần hình "
               "trụ của mối nối ('a' trong Hình 10.6), hoặc được chứa một "
               "phần trong phần hình trụ và một phần trong phần mặt phẳng, "
               "giống như mặt bích (sự kết hợp của 'a' và 'b' trong Hình "
               "10.6). Ngay cả những mối nối mà đường dẫn ngọn lửa nằm hoàn "
               "toàn trong phần hình trụ của mối nối cũng thường có một phần "
               "mặt phẳng để bố trí khả năng đặt bu lông cố định, dù phần đó "
               "không nhất thiết là một phần của đường dẫn then chốt (đường "
               "dẫn ngọn lửa) mà khí cháy đi qua trong trường hợp nổ bên "
               "trong. Tuy nhiên, điều này không phải lúc nào cũng đúng, vì "
               "có thể dùng các phương pháp khác để bảo đảm mối nối ổn định, "
               "ví dụ cố định bằng kẹp bên ngoài hoặc bằng ren trên phần "
               "hình trụ ở bên ngoài hoặc bên trong đường dẫn ngọn lửa. Mối "
               "nối dễ chế tạo hơn nếu đường dẫn ngọn lửa nằm hoàn toàn trong "
               "phần hình trụ của mối nối, nhưng điều này có thể làm vỏ bọc "
               "lớn hơn đáng kể so với phương án đầu tiên."))

    # printed p.237 (PDF 258): Fig. 10.6 then the advantage paragraph
    b.append(fig(6, FA.fig_f1006()))
    b.append(p("Ưu điểm chung của mối nối spigot là vì loại mối nối này có "
               "một góc vuông ở bên ngoài hoặc bên trong nên khả năng phát "
               "ra các hạt có khả năng gây cháy thấp hơn nhiều; do đó, không "
               "có hạn chế cụ thể nào đối với việc sử dụng loại mối nối này "
               "trong môi trường axetilen, khác với trường hợp các mối nối "
               "mặt bích phẳng tương ứng."))

    # italic sub-subsection 1 (LF 10982-10983)
    b.append(h4("Mối nối spigot ghép (đường dẫn ngọn lửa một phần nằm trong "
                "phần mặt phẳng của mối nối và một phần nằm trong phần hình "
                "trụ)",
                "Composite spigot joints (flamepath partly in the plane part "
                "of the joint and partly in the cylindrical part)"))
    b.append(p("Giới hạn khe hở tối đa cho các chiều dài khác nhau của mối "
               "nối ghép, khi đường dẫn ngọn lửa được chia giữa phần mặt "
               "phẳng và phần hình trụ"))

    # printed p.238 (PDF 259): Table 10.5 at its printed position
    b.append(table(T1.HEAD105_VI, T1.ROWS105, T1.CAPTION105_VI))
    b.append(note(T1.NOTE105_VI))
    b.append(note("<b>Lưu ý về cách in.</b> Chú đề bảng in 'maximum' với chữ "
                  "m thường, trong khi Bảng 10.6 in 'Maximum' với chữ M hoa; "
                  "tiêu đề bên trái của bảng này in 'L¹' có chỉ số trên, trong "
                  "khi Bảng 10.6 in '(L)'. Cả hai hình thức in đều được giữ "
                  "nguyên."))

    b.append(p("trong các môi trường nổ khác nhau và đối với các kích thước "
               "vỏ bọc khác nhau, được cho trong Bảng 10.5. Ngoài ra, còn có "
               "giới hạn về sự phân chia đường dẫn ngọn lửa giữa phần mặt "
               "phẳng và phần hình trụ của mối nối, cụ thể là phần mặt phẳng "
               "của mối nối phải rộng ít nhất 3 mm đối với mối nối dùng trong "
               "vỏ bọc thuộc nhóm IIA và IIB, và 6 mm đối với mối nối dùng "
               "trong vỏ bọc thuộc nhóm IIC. Ngoài ra, đối với mối nối dùng "
               "trong vỏ bọc thuộc nhóm IIC, phần hình trụ của mối nối phải "
               "dài ít nhất bằng một nửa tổng chiều dài ngắn nhất yêu cầu "
               "của đường dẫn ngọn lửa. Không có hạn chế tương tự đối với mối "
               "nối dùng trong vỏ bọc thuộc nhóm IIA hoặc IIB."))
    b.append(p("Trong những trường hợp đó, rất có thể gặp khó khăn đáng kể "
               "trong gia công các góc vuông ở cả hai phần của mối nối và "
               "bảo đảm sự khớp hợp giữa chúng. Vì lý do này, tình huống "
               "trong đó góc vuông phía đực có vát mép hoặc bán kính đã được "
               "nghiên cứu kỹ. Tình huống này được minh họa cho cả mối nối "
               "spigot bên trong và bên ngoài trong Hình 10.7, và người ta "
               "đã chứng minh rằng, nếu vát mép hoặc bán kính không có kích "
               "thước tuyến tính lớn hơn 1 mm ở cả phần mặt phẳng và phần "
               "hình trụ của mối nối, và nếu bán kính là lồi thay vì lõm "
               "(dẫn đến ít vật liệu bị loại bỏ hơn), thì khe hở tạo ra "
               "không làm giảm đáng kể độ an toàn của mối nối được tạo "
               "thành từ cả phần mặt phẳng và phần chốt. Do đó, miễn là phần "
               "còn lại và phần hình trụ ('a' và 'b' trong Hình 10.7) cộng "
               "lại ít nhất bằng chiều rộng mối nối tối thiểu yêu cầu quy "
               "định trong Bảng 10.5, và được phân chia giữa hai phần của "
               "mối nối theo các hạn chế bổ sung nêu trong chương này, thì "
               "cách bố trí đó được chấp nhận. Tuy nhiên, cần hiểu rõ rằng "
               "các phần vật liệu bị loại bỏ do bán kính hoặc vát mép không "
               "tính vào chiều dài yêu cầu ('f' trong Hình 10.7 không tính "
               "vào chiều dài mối nối)."))

    # printed p.239 (PDF 260): Fig. 10.7
    b.append(fig(7, FA.fig_f1007()))

    # printed p.240 (PDF 261)
    b.append(p("Như đã nêu trong đoạn trước, có các yêu cầu bổ sung về sự "
               "phân chia chiều dài mối nối yêu cầu giữa phần mặt phẳng và "
               "phần hình trụ của mối nối như sau: thứ nhất, chiều rộng tối "
               "thiểu của phần mặt phẳng của mối nối phải ít nhất là 3 mm "
               "đối với nhóm IIA và IIB và 6 mm đối với nhóm IIC; và thứ "
               "hai, chiều dài tối thiểu của phần hình trụ của mối nối phải "
               "ít nhất bằng một nửa chiều dài tối thiểu quy định trong "
               "Bảng 10.5 đối với vỏ bọc dùng cho nhóm IIC. Không áp dụng "
               "hạn chế nào trong trường hợp này đối với vỏ bọc dùng cho "
               "nhóm IIA hoặc IIB, vì yêu cầu đối với mối nối mặt bích và "
               "mối nối spigot là như nhau."))
    b.append(p("Như đã nêu trước đó, không có hạn chế cụ thể nào đối với "
               "việc sử dụng các mối nối này trong môi trường axetilen, và "
               "điều này đã dẫn đến các hạn chế về chiều dài ngắn nhất cho "
               "phép của đường dẫn ngọn lửa trong nhóm IIC. Lý do là hiệu "
               "suất kém của các mối nối ghép (phần hình trụ cộng phần mặt "
               "phẳng) có chiều dài ngắn trong môi trường axetilen và, ở một "
               "mức độ nhất định, hiệu suất của các mối nối ghép ngắn trong "
               "môi trường hydro. Thay vì tạo ra một tình huống rất phức "
               "tạp, vì vậy các hạn chế sau đây được áp dụng:"))
    b.append(p("Không cho phép mối nối ghép nào có chiều dài ngắn hơn "
               "12,5 mm đối với vỏ bọc thuộc nhóm IIC."))
    b.append(p("Không cho phép mối nối ghép nào có chiều dài ngắn hơn "
               "25 mm trong vỏ bọc có thể tích lớn hơn 2000 cm³ đối với "
               "nhóm IIC."))
    b.append(p("Không cho phép mối nối ghép nào có chiều dài ngắn hơn "
               "9,5 mm trong vỏ bọc có thể tích lớn hơn 100 cm³ đối với "
               "nhóm IIA và IIB."))
    b.append(p("Không cho phép mối nối ghép nào có chiều dài ngắn hơn "
               "12,5 mm trong vỏ bọc có thể tích lớn hơn 500 cm³ đối với "
               "nhóm IIA và IIB."))
    b.append(p("Các yêu cầu trên nghiêm ngặt hơn so với các yêu cầu áp dụng "
               "cho mối nối spigot mà toàn bộ đường dẫn ngọn lửa nằm trong "
               "phần hình trụ của mối nối và sẽ được xét trong phần sau."))

    # italic sub-subsection 2 (LF 11076)
    b.append(h4("Mối nối spigot có toàn bộ đường dẫn ngọn lửa nằm trong phần "
                "hình trụ của mối nối",
                "Spigot joints with all of the flamepath in the cylindrical "
                "part of the joint"))
    b.append(p("Yêu cầu về chiều dài đường dẫn ngọn lửa cũng giống như đối "
               "với mối nối ghép trong trường hợp mối nối có toàn bộ đường "
               "dẫn ngọn lửa nằm trong phần hình trụ của mối nối ('a' trong "
               "Hình 10.6) và được dùng trong vỏ bọc thuộc nhóm IIA và IIB, "
               "nhưng có sự nới lỏng đáng kể đối với mối nối dùng trong vỏ "
               "bọc thuộc nhóm IIC, như có thể thấy từ Bảng 10.6, bảng xác "
               "định khe hở tối đa cho loại mối nối này đối với các kích "
               "thước vỏ bọc khác nhau và ba nhóm IIA, IIB và IIC. Sự giảm "
               "khe hở cho phép đối với mối nối dùng trong vỏ bọc thuộc nhóm "
               "IIC là 0,15 mm khi toàn bộ đường dẫn ngọn lửa nằm trong phần "
               "hình trụ và chiều dài mối nối ≤ 25 mm. (So sánh với 0,18 mm "
               "đối với mối nối ghép)."))
    b.append(p("Những khác biệt khác là cho phép chiều dài mối nối nhỏ hơn "
               "trong trường hợp toàn bộ mối nối nằm trong phần hình trụ và "
               "các hạn chế về chiều dài mối nối gần sát hơn với các hạn chế "
               "đối với mối nối mặt bích, mặc dù mối nối spigot có ưu điểm "
               "bổ sung là có thể dùng trong môi trường axetilen"))

    # printed p.241 (PDF 262): Table 10.6 at its printed position
    b.append(table(T2.HEAD106_VI, T2.ROWS106, T2.CAPTION106_VI))
    b.append(note(T2.NOTE106_VI))
    b.append(note("<b>Lưu ý về một điểm bất thường trong bản in.</b> Ở dòng "
                  "≥ 12,5, cột ≤ 100 cm³ / IIB, bảng in 0,02 [sic], gần như "
                  "chắc chắn là lỗi in của 0,2; số liệu được giữ nguyên như "
                  "bản in. Ô cuối cùng (≥ 40,0, > 2000 cm³, IIC) in 0,2 thay "
                  "vì 0,20 và số chữ số thập phân được giữ nguyên."))

    b.append(p("Các hạn chế này là: thứ nhất, các mối nối có chiều dài dưới "
               "6 mm không được phép dùng trong vỏ bọc có thể tích lớn hơn "
               "100 cm³ đối với nhóm IIC. (Các mối nối ghép phải có chiều "
               "dài 12,5 mm cho mục đích sử dụng đó.) và thứ hai, các mối "
               "nối có chiều dài dưới 9,5 mm không được phép dùng trong vỏ "
               "bọc có thể tích lớn hơn 500 cm³ để dùng trong môi trường "
               "IIC. (Các mối nối ghép phải có chiều dài tối thiểu 12,5 mm "
               "cho mục đích sử dụng đó.)"))
    b.append(p("Như có thể thấy, các hạn chế này nhẹ hơn đáng kể so với các "
               "hạn chế đối với mối nối ghép và gần sát hơn với các hạn chế "
               "đối với mối nối mặt bích, ngoại trừ việc trong trường hợp "
               "này không có hạn chế chung về kích thước vỏ bọc như trong "
               "trường hợp mối nối mặt bích dành cho các mối nối mặt bích "
               "tương ứng; có thể lắp đệm kín hoặc vòng '0' để làm mối nối "
               "spigot chống thấm nước, miễn là chúng không làm giảm chiều "
               "dài đường dẫn ngọn lửa đạt được xuống dưới mức tối thiểu "
               "quy định trong Bảng 10.5, và không làm cho phần chốt hoặc "
               "phần mặt bích của bất kỳ mối nối nào không còn đáp ứng các "
               "chiều dài tối thiểu quy định trước đó trong chương này."))

    # italic sub-subsection 3 (LF 11126) - printed 'efc.' preserved
    b.append(h4("Đệm kín để chống thấm nước, efc. [sic], của cả hai loại mối "
                "nối spigot",
                "Gaskets for weatherproofing, efc. [sic], of both types of "
                "spigot joint"))
    b.append(note("<b>Lưu ý về tiêu đề in.</b> Tiêu đề in ghi 'efc.' [sic], rõ "
                  "ràng là lỗi in của 'etc.'; hình thức in được giữ nguyên. "
                  "Ngoài ra, nguyên bản in '0' ring với chữ số 0; đây là vòng "
                  "đệm O-ring thông thường và hình thức in được giữ nguyên "
                  "khi trích dẫn."))
    b.append(p("Việc sử dụng đệm kín dạng vòng '0', tương tự như loại dùng "
               "trong mối nối mặt bích phẳng, được minh họa trong Hình 10.8 "
               "đối với vòng '0' ở phần mặt phẳng và phần hình trụ của mối "
               "nối. Trong trường hợp sau, vòng có thể nằm bên trong hoặc "
               "bên ngoài đường dẫn ngọn lửa. Vòng '0' luôn phải nằm bên "
               "ngoài hoặc bên trong đường dẫn ngọn lửa, chứ không được nằm "
               "trong đó, và như có thể thấy từ Hình 10.8, đường dẫn ngọn "
               "lửa phải nằm hoàn toàn trong phần hình trụ khi vòng '0' nằm "
               "bên ngoài đường dẫn ngọn lửa nhưng vẫn nằm trong phần hình "
               "trụ của mối nối. Khi vòng '0' nằm ở phần mặt phẳng của mối "
               "nối bên ngoài đường dẫn ngọn lửa, hoặc ở phần hình trụ bên "
               "trong đường dẫn ngọn lửa, thì đương nhiên vẫn có thể dùng "
               "mối nối ghép. Rãnh lắp phải chứa hoàn toàn vòng '0' để mối "
               "nối không bị biến dạng."))

    # printed p.242 (PDF 263): Fig. 10.8
    b.append(fig(8, FA.fig_f1008()))
    b.append(p("Điều này đặc biệt quan trọng trong trường hợp mối nối ghép "
               "mà vòng '0' nằm ở phần mặt phẳng của mối nối. Một lần nữa, "
               "đối với vỏ bọc bằng kim loại, giải pháp ưu tiên để chống "
               "thấm nước là đặt đệm kín ở bên ngoài đường dẫn ngọn lửa nhằm "
               "tránh ăn mòn mối nối có thể làm hỏng đặc tính chống cháy "
               "của nó."))
    b.append(p("Trong trường hợp này, đệm kín phẳng cũng được phép sử dụng, "
               "ở bên trong hoặc bên ngoài đường dẫn ngọn lửa, và vị trí "
               "của chúng được thể hiện trong Hình 10.9. Trong trường hợp "
               "này, đường dẫn ngọn lửa phải nằm hoàn toàn trong phần hình "
               "trụ của mối nối vì đệm kín sẽ ngăn không cho xác định rõ "
               "phần mặt phẳng của mối nối. Ngoài ra, cần bảo đảm rằng đường "
               "dẫn ngọn lửa trong phần hình trụ luôn đủ dài, và cách duy "
               "nhất hiệu quả để bảo đảm điều này là đường dẫn ngọn lửa "
               "trong phần hình trụ của mối nối đáp ứng các yêu cầu của "
               "Bảng 10.6 trước khi nén đệm kín, khi vỏ bọc được lắp với đệm "
               "kín có kích thước tối đa."))

    # italic sub-subsection 4 (LF 11157)
    b.append(h4("Chốt cố định trong các phần mặt phẳng của mối nối spigot "
                "ghép",
                "Fixings in the plane parts of composite spigot joints"))
    b.append(p("Tuy nhiên, kết cấu của các mối nối này phức tạp hơn nhiều, "
               "đặc biệt là khi phần mặt phẳng của mối nối tạo thành một "
               "phần của đường dẫn ngọn lửa (khe hở) và bu lông cố định đi "
               "qua phần đó."))

    # printed p.242 (Fig. 10.9) and p.243 (Fig. 10.10)
    b.append(fig(9, FA.fig_f1009()))
    b.append(fig(10, FA.fig_f1010()))
    b.append(note("<b>Lưu ý về ký hiệu trong bản in.</b> Nguyên bản in biến "
                  "số là chữ l thường trong chú giải hình và trong văn bản, "
                  "trong khi lớp văn bản OCR đọc nhầm thành '1' hoặc 'i'; ở "
                  "đây dùng chữ l. Chú giải ghi 'l = 0,2 mm tối đa' cho nhóm "
                  "IIA/IIB và '0,1 mm tối đa' cho IIC, dù văn bản xung quanh "
                  "xem các giá trị này là khe hở tối đa cho phép trong phần "
                  "hình trụ."))
    b.append(p("đi qua phần đó. Việc bu lông đi qua thực sự chia đường dẫn "
               "ngọn lửa theo cách tương tự như trường hợp mối nối mặt "
               "bích, đối với mối nối spigot bên ngoài thì đầu bu lông có "
               "thể nằm bên trong hoặc bên ngoài vỏ bọc (xem Hình 10.10), "
               "hoặc đối với mối nối spigot bên trong thì đầu bu lông nằm "
               "bên trong vỏ bọc. Trong tất cả các trường hợp này, cần lưu "
               "ý rằng chiều dài của đường đi giữa lỗ lọt bu lông và bên "
               "ngoài vỏ bọc, khi đầu bu lông nằm bên trong vỏ bọc, và giữa "
               "lỗ lọt bu lông và bên trong vỏ bọc, khi đầu bu lông nằm "
               "bên ngoài vỏ bọc, được tạo hoàn toàn trong phần mặt phẳng "
               "của mối nối, do đó các yêu cầu của Bảng 10.2 áp dụng cho "
               "giá trị tối thiểu của 'l'."))
    b.append(p("Trong trường hợp mối nối spigot bên trong mà đầu bu lông "
               "nằm bên ngoài, tuy nhiên, tình huống lại rất khác. Ở đây, "
               "khoảng cách 'l' giữa bên trong vỏ bọc và lỗ lọt bu lông là "
               "ghép, được tạo thành"))

    # printed p.244 (PDF 265), LF 11195-11217
    b.append(p("từ một phần của phần mặt phẳng của mối nối và phần hình trụ "
               "của mối nối. Điều này càng trở nên phức tạp hơn khi có vát "
               "mép hoặc bán kính trên phần đực của mối nối để hỗ trợ việc "
               "lắp khớp. Trong trường hợp này, cũng như đối với đường dẫn "
               "ngọn lửa, khoảng cách 'l' được tạo thành từ chiều dài của "
               "phần hình trụ của mối nối ('a' trong Hình 10.10) tính đến "
               "nhưng không bao gồm vát mép hoặc bán kính, và khoảng cách "
               "giữa mép của vát mép hoặc bán kính và lỗ lọt bu lông trong "
               "phần mặt phẳng của mối nối ('c' trong Hình 10.10)."))
    b.append(note("<b>Lưu ý về một mâu thuẫn trong nguyên bản.</b> Đoạn đầu "
                  "nói về mối nối spigot ngoài với đầu bu lông nằm bên trong "
                  "hoặc bên ngoài vỏ bọc, hoặc mối nối spigot trong với đầu "
                  "bu lông nằm bên trong; đoạn sau lại phân tích mối nối "
                  "spigot trong với đầu bu lông nằm bên ngoài [sic — trường "
                  "hợp ngược lại]. Mâu thuẫn trong nguyên bản được giữ "
                  "nguyên."))
    b.append(p("Độ toàn vẹn của mối nối spigot dựa trên hai tiêu chí. Thứ "
               "nhất, Khe hở an toàn thử nghiệm tối đa (MESG) lớn hơn khe hở "
               "tối đa được Tiêu chuẩn cho phép, cho phép giảm khe hở tại lỗ "
               "lọt bu lông như quy định trong Bảng 10.2; và thứ hai, thể "
               "tích tạo ra do vát mép hoặc bán kính trên phần đực của mối "
               "nối spigot, dù ảnh hưởng bất lợi đến hiệu suất của mối nối, "
               "sẽ không được cộng vào sự giảm của khoảng cách 'l' vì nó "
               "không nằm trong đường đi đó. Rất tiếc, trong trường hợp đầu "
               "bu lông nằm bên ngoài vỏ bọc khi dùng mối nối spigot bên "
               "trong, điều này không đúng, vì khoảng cách 'l' đã giảm là "
               "ghép, chứa một phần mặt phẳng từ lỗ lọt bu lông đến mép của "
               "vát mép hoặc bán kính, và một phần hình trụ từ mép bên trong "
               "của mối nối đến mép của vát mép hoặc bán kính. Điều này cho "
               "thấy 'tệ nhất của cả hai' trong trường hợp có vát mép, và "
               "cần một hạn chế bổ sung. Điều này được thực hiện bằng cách "
               "hạn chế khe hở cho phép trong phần hình trụ của mối nối ở "
               "mức 0,2 mm đối với mối nối dùng trong vỏ bọc thuộc nhóm IIA "
               "và IIB và 0,1 mm đối với mối nối dùng trong nhóm IIC."))
    return "".join(b)


def body_en():
    b = []
    b.append(h3("2 Spigot joints", "2 Spigot joints"))

    # printed p.236 (PDF 257), LF 10955-10968 - definition of spigot joints
    b.append(p("Spigot joints are joints in which the critical gap forming "
               "the flamepath is contained, either totally within the "
               "cylindrical part of the joint ('a' in Fig. 10.6), or where "
               "it is partly contained within the cylindrical joint and "
               "partly within the plane part, which is similar to a flange "
               "(a combination of 'a' and 'b' in Fig. 10.6). Even joints "
               "where the flamepath is totally within the cylindrical part "
               "of the joint usually have a plane part to provide for the "
               "possibility of fixing bolts, even though this may not form "
               "part of the critical path (flamepath) through which the "
               "burning gases pass in case of an internal explosion. This "
               "is not, however, always true as alternative methods may be "
               "used to ensure that the joint is stable, for example, the "
               "fixing may be by an external clamp or by a thread on the "
               "cylindrical part outside, or inside the flamepath. The "
               "joint is more simple to manufacture if the flamepath is "
               "fully within the cylindrical part of the joint, but this "
               "may cause an enclosure to be significantly larger than if "
               "the first alternative is adopted."))

    # printed p.237 (PDF 258): Fig. 10.6 then the advantage paragraph
    b.append(fig(6, FA.fig_f1006()))
    b.append(p("The overall advantage of spigot joints is the fact that, as "
               "this type of joint has a right angle either outside it or "
               "inside it, it is much less likely to emit ignition-capable "
               "particles and, as a result, there is no specific restriction "
               "in the use of such joints in acetylene atmospheres, unlike "
               "the situation in respect of their flat flanged counterparts."))

    # italic sub-subsection 1 (LF 10982-10983)
    b.append(h4("Composite spigot joints (flamepath partly in the plane part "
                "of the joint and partly in the cylindrical part)",
                "Composite spigot joints (flamepath partly in the plane part "
                "of the joint and partly in the cylindrical part)"))
    b.append(p("The limits of maximum gap size for various lengths of "
               "composite joints, where the flamepath is divided between the "
               "plane part and the cylindrical"))

    # printed p.238 (PDF 259): Table 10.5 at its printed position
    b.append(table(T1.HEAD105_EN, T1.ROWS105, T1.CAPTION105_EN))
    b.append(note(T1.NOTE105_EN))
    b.append(note("<b>Note on the printed notation.</b> The caption prints "
                  "'maximum' with a lowercase m, whereas Table 10.6 prints "
                  "'Maximum' with a capital M; the left header of this table "
                  "prints 'L¹' with a superscript 1, whereas Table 10.6 "
                  "prints '(L)'. Both printed forms are retained."))

    b.append(p("part in various explosive atmospheres and for various sizes "
               "of enclosure, are given in Table 10.5. In addition, there "
               "are limits to the division of the flamepath between the "
               "plane part and the cylindrical part of the joint, in that "
               "the plane part of the joint must be at least 3 mm for joints "
               "in enclosures for use in sub-groups IIA and IIB, and 6 mm "
               "for those for use in sub-group IIC. In addition for joints "
               "in enclosures for use in sub-group IIC the cylindrical part "
               "of the joint must be at least half the total minimum "
               "required length of flamepath. No similar restriction exists "
               "for joints in enclosures for sub-group IIA or IIB."))
    b.append(p("In these circumstances it is likely that considerable "
               "machining difficulties would be encountered in forming the "
               "right angles in both the parts of the joint, and ensuring "
               "proper mating. For this reason the situation whereby the "
               "male right angle has a chamfer or radius on it has been "
               "carefully investigated. Such a situation is shown for both "
               "internal and external spigot joints in Fig. 10.7 and it has "
               "been shown that, provided the chamfer or radius does not "
               "have a linear dimension in either the plane of the plane "
               "part of the joint and in the cylindrical part of greater "
               "than 1 mm and, if a radius is convex rather than concave "
               "(resulting in less material removal), the aperture so "
               "produced will not cause any significant reduction in the "
               "security of joints made up of both plane and spigot portions "
               "of the joint. Therefore, provided the remaining parts and "
               "cylindrical parts ('a' and 'b' in Fig. 10.7) add up to at "
               "least the minimum required joint width specified in Table "
               "10.5, and is divided between the two parts of the joint in "
               "accordance with the additional restrictions given in this "
               "chapter, the situation is acceptable. It has to be clearly "
               "understood, however, that the parts of the joint removed by "
               "the radius or chamfer do not form part of the length "
               "required ('f' in Fig. 10.7 does not form part of the joint "
               "length)."))

    # printed p.239 (PDF 260): Fig. 10.7
    b.append(fig(7, FA.fig_f1007()))

    # printed p.240 (PDF 261)
    b.append(p("As stated in the previous paragraph there are additional "
               "requirements for the division of the required length of "
               "joint between the plane part and the cylindrical part of "
               "joints which are as follows: first, the minimum width of "
               "the plane part of the joint must be at least 3 mm for "
               "sub-groups IIA and IIB and 6 mm for sub-group IIC; and "
               "second, the minimum length of the cylindrical part of the "
               "joint must be at least half of the minimum length specified "
               "in Table 10.5 for enclosures intended for sub-group IIC use. "
               "No restriction applies in this respect for enclosures "
               "intended for sub-group IIA or IIB use as the requirements "
               "for flanged joints and spigot joints are the same."))
    b.append(p("As previously stated, there is no specific restriction to "
               "the use of these joints in acetylene atmospheres and this "
               "has led to restrictions in the minimum length of flamepath "
               "permitted in sub-group IIC. The reason for this is the "
               "performance of composite (cylindrical part plus plane part) "
               "joints of shorter length in acetylene atmospheres and, to a "
               "degree, the performance of composite joints of short length "
               "in hydrogen atmospheres. Rather than create a very complex "
               "situation, therefore, the following restrictions apply:"))
    b.append(p("No composite joint with a length of less than 12.5 mm is "
               "permitted for enclosures for sub-group IIC."))
    b.append(p("No composite joint with a length of less than 25 mm is "
               "permitted in enclosures with volumes greater than "
               "2000 cm³ for sub-group IIC."))
    b.append(p("No composite joint with a length less than 9.5 mm is "
               "permitted in enclosures of greater than 100 cm³ volume for "
               "sub-group IIA and IIB."))
    b.append(p("No composite joint with a length of less than 12.5 mm is "
               "permitted in enclosures of greater than 500 cm³ for "
               "sub-group IIA and IIB."))
    b.append(p("The above requirements are more severe than those applied "
               "to spigot joints where all of the flamepath is in the "
               "cylindrical part of the joint and which are dealt with in "
               "the following text."))

    # italic sub-subsection 2 (LF 11076)
    b.append(h4("Spigot joints with all of the flamepath in the cylindrical "
                "part of the joint",
                "Spigot joints with all of the flamepath in the cylindrical "
                "part of the joint"))
    b.append(p("The requirements for flamepath length are the same as for a "
               "composite joint in the case of joints where the entire "
               "flamepath is in the cylindrical part of the joint ('a' in "
               "Fig. 10.6) and which are used in enclosures for sub-group "
               "IIA and IIB, but there are significant relaxations for "
               "joints in enclosures for sub-group IIC, as can be seen from "
               "Table 10.6 which defines the maximum gaps for this type of "
               "joint for various sizes of enclosure and the three "
               "subgroups, IIA, IIB and IIC. The reduction of permissible "
               "gap for joints of enclosures intended for sub-group IIC use "
               "is 0.15 mm for joints where all of the flamepath is within "
               "the cylindrical part and the joint length is ≤ 25 mm. (This "
               "compares with 0.18 mm for composite joints)."))
    b.append(p("The other differences are the permissibility of smaller "
               "joint lengths in cases where all of the joint is in the "
               "cylindrical part and the restrictions in joint length are "
               "much more in-line with those of flanged joints, although "
               "the spigot joint has the added advantage that it may be used "
               "in acetylene"))

    # printed p.241 (PDF 262): Table 10.6 at its printed position
    b.append(table(T2.HEAD106_EN, T2.ROWS106, T2.CAPTION106_EN))
    b.append(note(T2.NOTE106_EN))
    b.append(note("<b>Note on a printed anomaly.</b> In the row ≥ 12.5, "
                  "column ≤ 100 cm³ / IIB, the table prints 0.02 [sic], "
                  "almost certainly a typographical error for 0.2; the "
                  "figure is retained as printed. The final cell (≥ 40.0, "
                  "> 2000 cm³, IIC) prints 0.2 rather than 0.20, and the "
                  "decimal places are retained exactly."))

    b.append(p("atmospheres. These restrictions are: first, joints of less "
               "than 6 mm length are not permitted in enclosures of more "
               "than 100 cm³ for sub-group IIC use. (Composite joints must "
               "have a length of 12.5 mm for such use.) and second, joints "
               "with lengths of less than 9.5 mm are not permitted in "
               "enclosures of greater volume than 500 cm³ for use in IIC "
               "atmospheres. (Composite joints must have minimum lengths of "
               "12.5 mm for such use.)."))
    b.append(p("As can be seen, these restrictions are considerably less "
               "than those for composite joints and more in-line with those "
               "for flanged joints, except that in this case there is no "
               "overall restriction on enclosure size as there is in the "
               "case of flanged joints for their flanged counterparts "
               "gaskets, or '0' rings may be fitted to make spigot joints "
               "weatherproof, provided these do not reduce the length of "
               "the flamepath achieved to less than that minimum specified "
               "in Table 10.5, and do not cause the spigot part or the flange "
               "part of any joint to cease to comply with the minimum "
               "lengths specified earlier in this chapter."))

    # italic sub-subsection 3 (LF 11126) - printed 'efc.' preserved
    b.append(h4("Gaskets for weatherproofing, efc. [sic], of both types of "
                "spigot joint",
                "Gaskets for weatherproofing, efc. [sic], of both types of "
                "spigot joint"))
    b.append(note("<b>Note on the printed heading.</b> The printed heading "
                  "reads 'efc.' [sic], evidently a typographical error for "
                  "'etc.'; the printed form is retained. The original also "
                  "prints '0' ring with the digit-like zero; this is the "
                  "standard O-ring and the printed form is retained in "
                  "quotations."))
    b.append(p("The use of '0' ring-type gaskets, similar to those used in "
               "flat flanged joints, is shown in Fig. 10.8 for an '0' ring "
               "in the plane part and the cylindrical part of the joint. In "
               "the latter case, both inside the flamepath and outside the "
               "flamepath. The '0' ring must always be outside or inside the "
               "flamepath, not within it, and as can be seen from Fig. 10.8, "
               "the flamepath must be totally within the cylindrical part "
               "where the '0' ring is outside the flamepath, but in the "
               "cylindrical part of the joint. Where the '0' ring is in the "
               "plane part of the joint outside the flamepath, or in the "
               "cylindrical part inside the flamepath, composite joints "
               "are, of course, possible. The recess must fully accommodate "
               "the '0' ring to ensure that the joint is not distorted."))

    # printed p.242 (PDF 263): Fig. 10.8
    b.append(fig(8, FA.fig_f1008()))
    b.append(p("This is particularly important in the case of the composite "
               "joint, where the '0' ring is in the plane part of the joint. "
               "Again, for metallic enclosures the preferred solution for "
               "weatherproofing is to have the gasket outside the flamepath "
               "to avoid corrosion of the joint which could damage its "
               "flameproof properties."))
    b.append(p("Flat gaskets are, in this case, also permitted, either "
               "inside or outside the flamepath, and their position is "
               "shown in Fig. 10.9. In this case, the flamepath must be "
               "totally within the cylindrical part of the joint as the "
               "gaskets will prevent clear definition of the plane part of "
               "the joint. In addition, it will be necessary to ensure that "
               "the flamepath in the cylindrical part is always of adequate "
               "length, and the only effective way to ensure this is to "
               "ensure that the flamepath in the cylindrical part of the "
               "joint satisfies the requirements of Table 10.6 before "
               "compression of the gasket when the enclosure is fitted with "
               "a gasket of maximum dimension."))

    # italic sub-subsection 4 (LF 11157)
    b.append(h4("Fixings in the plane parts of composite spigot joints",
                "Fixings in the plane parts of composite spigot joints"))
    b.append(p("The construction of the joints is, however, much more "
               "complex particularly where the plane part of the joint "
               "forms part of the flamepath (gap) and fixing"))

    # printed p.242 (Fig. 10.9) and p.243 (Fig. 10.10)
    b.append(fig(9, FA.fig_f1009()))
    b.append(fig(10, FA.fig_f1010()))
    b.append(note("<b>Note on the printed symbol.</b> The original prints "
                  "the variable as a lowercase l (ell) in the figure legend "
                  "and in the prose, where the OCR text layer misreads it "
                  "as '1' or 'i'; the letter l is used here. The legend "
                  "writes 'l = 0.2 mm max' for sub-groups IIA/IIB and "
                  "'0.1 mm max' for IIC, although the surrounding prose "
                  "treats these values as permitted gaps in the cylindrical "
                  "part."))
    b.append(p("bolts pass through it. The passage of the bolt actually "
               "divides the flamepath in a similar way to that which occurs "
               "with flange joints with an external spigot joint with the "
               "bolt head either inside or outside the enclosure (see Fig. "
               "10.10) or an internal spigot where the bolt head is inside "
               "the enclosure. In all of these cases it should be noted "
               "that the length of path between the bolt clearance hole and "
               "the outside of the enclosure, where the bolt head is inside "
               "the enclosure and the bolt clearance hole, and the interior "
               "of the enclosure where the bolt head is outside the "
               "enclosure, is formed totally in the plane part of the joint "
               "and thus the requirements of Table 10.2 apply to the minimum "
               "value of 'l'."))
    b.append(p("In the case of the internal spigot joint where the bolt head "
               "is external, however, the situation is very different. Here, "
               "the distance 'l' between the interior of the enclosure and "
               "the bolt clearance hole is composite, being"))

    # printed p.244 (PDF 265), LF 11195-11217
    b.append(p("made up of the part of the plane part of the joint and its "
               "cylindrical part of the joint. This is further exacerbated "
               "where there is a chamfer or radius on the male part of the "
               "joint to aid seating of the joint. In this case, as for the "
               "flamepath, the distance 'l' is made up of the length of the "
               "cylindrical part of the joint ('a' in Fig. 10.10) up to, but "
               "not including, the chamfer or radius and the distance "
               "between the edge of the chamfer or radius and the bolt "
               "clearance hole in the plane part of the joint ('c' in Fig. "
               "10.10)."))
    b.append(note("<b>Note on an inconsistency in the original.</b> The "
                  "first paragraph lists an external spigot joint with the "
                  "bolt head either inside or outside the enclosure, or an "
                  "internal spigot where the bolt head is inside; the "
                  "following paragraph then analyses the internal spigot "
                  "joint where the bolt head is external [sic - the "
                  "opposite case]. The contradiction in the original is "
                  "preserved."))
    b.append(p("The integrity of spigot joints is based on two criteria. "
               "First, the Maximum Experimental Safe Gap (MESG) is larger "
               "than the gap permitted as maximum by the Standard, thus "
               "permitting the reduction to the bolt clearance hole "
               "specified in Table 10.2, and second, the volume created by "
               "the chamfer or radius in the male part of a spigot joint "
               "while adversely affecting the joint performance will not be "
               "added to the reduction of the distance 'l' as it does not "
               "form part of that path. Unfortunately, where the bolt head "
               "is outside the enclosure in cases where an internal spigot "
               "is used, this is not true as the reduced distance 'l' is "
               "composite, containing a plane part which is from the bolt "
               "clearance hole to the edge of the chamfer or radius, and a "
               "cylindrical part which is from the internal edge of the "
               "joint to the edge of the chamfer or radius. This gives the "
               "worst of both worlds in cases where a chamfer is present and "
               "a further restriction is necessary. This is achieved by "
               "restriction in the gap permitted in the cylindrical part of "
               "the joint to 0.2 mm for joints of enclosures intended for "
               "use in sub-group IIA and IIB and 0.1 mm for those intended "
               "for use in sub-group IIC."))
    return "".join(b)
