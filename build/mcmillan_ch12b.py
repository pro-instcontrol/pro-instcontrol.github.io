# -*- coding: utf-8 -*-
"""Chapter 12, module B - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 302-305 (PDF pp. 323-326).

Covers the tail of 12.2.3 Separation of conducting parts (creepage distances,
clearances, Table 12.1, Fig. 12.5 and Fig. 12.6) and the beginning of 12.2.4
Insulation. Figures 12.3 and 12.4, printed on p. 301 at the end of 12.2.2,
open this module's figure run so that Figures 12.3-12.6 are emitted together.
The chapter shell owns the chapter h2, the printed references, the glossary,
the source-quirk note and the copyright.

Printed quirks are kept in the English text (the Arabic "1" against Roman
"II", uneven number/unit spacing, "Fig 12.6" without a period, the capitalised
"Standards", the comma after "of course", the note-marker case, and the final
comma where a sentence continues beyond the span) with bilingual notes; the
Vietnamese follows the intended meaning. This is an unofficial study
translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, table, fig
import mcmillanfig12_a as FA
import mcmillanfig12_b as FB
import mcmillan_tbl12_1_4 as T1


def body_vi():
    b = []

    # Figures 12.3 and 12.4 are printed on p.301 (end of 12.2.2); they open
    # this module's figure run. Printed pp.302-305 follow.
    b.append(note("<b>Lưu ý về vị trí của Hình 12.3 và Hình 12.4.</b> Hai hình "
                  "này được in ở trang 301, cuối mục 12.2.2 về đầu nối và "
                  "phương tiện nối dây, nhưng được đưa vào đầu mô-đun này để "
                  "toàn bộ Hình 12.3 đến Hình 12.6 được trình bày cùng nhau. "
                  "Chú thích và nhãn của bản in được giữ nguyên."))
    b.append(fig(3, FA.fig_f1203()))
    b.append(fig(4, FA.fig_f1204()))

    # Printed p.302, first paragraph (continuation of 12.2.3).
    b.append(p("Vì sự phá hủy cách điện thường có khả năng xảy ra cao hơn sự "
               "phá hủy của không khí, các giá trị chiều dài đường rò thường "
               "lớn hơn các giá trị khe hở (xem Bảng 12.1). Giá trị điện áp "
               "làm việc trong Bảng 12.1 là giá trị điện áp cao nhất có thể "
               "xuất hiện giữa các dây dẫn đang xét, hoặc với những biến động "
               "được công nhận của nguồn cấp và tải, hoặc với các mạch hở đặt "
               "trong thiết bị khi những điều đó tạo ra điều kiện xấu hơn. "
               "Điện áp quá trình được bỏ qua vì chúng thường không ảnh hưởng "
               "đến sự theo dõi (tracking) trên bề mặt cách điện. Hình 12.5 "
               "cho thấy sự khác biệt cơ bản giữa chiều dài đường rò và khe hở."))
    b.append(note("<b>Lưu ý về cách đọc OCR của 'occur'.</b> Lớp văn bản OCR "
                  "đọc 'can occw' trong đoạn đầu; bản render cho thấy bản in "
                  "viết 'can occur'. Bản tiếng Anh dùng 'can occur' theo bản in."))

    # Table 12.1 sits after the first paragraph on printed p.302.
    b.append(table(T1.HEAD121_VI, T1.ROWS121_VI, T1.CAPTION121_VI))
    if T1.NOTE121_VI:
        b.append(note(T1.NOTE121_VI))
    b.append(note("<b>Lưu ý về các ký hiệu trong Bảng 12.1.</b> Lớp văn bản "
                  "OCR làm mất các dấu bất đẳng thức trong cột điện áp (ví dụ "
                  "đọc '15< U 530' thay vì '15< U ≤30', '550~ U5750' thay vì "
                  "'550< U ≤750') và đọc nhầm 'Material Group IIIa³' thành "
                  "'Material Group ma3' cùng 'Material Group IIIa' thành "
                  "'Materid Group ma' ở chú thích 3. Các ký tự đúng được lấy "
                  "từ bản render. Dòng nguồn '(from BS EN 50019)' được giữ "
                  "nguyên, kể cả dạng viết không có dấu cách giữa BS và EN."))

    # Printed p.302 ends mid-sentence: '...in all cases where ribs'; Fig. 12.5
    # occupies the top of printed p.303; the sentence resumes below the figure.
    b.append(p("Dù phần trên xử lý hiệu quả tình huống bề mặt cách điện "
               "phẳng, như thể hiện trong Hình 12.5, nó không bao phủ đầy đủ "
               "nhiều tình huống thường gặp có rãnh trong lớp cách điện, hoặc "
               "có các gờ tách các dây dẫn, cả hai tình huống này thường xuất "
               "hiện trong các khối cọc nối. Trong những trường hợp đó, đôi "
               "khi có thể phát sinh thêm vấn đề. Rãnh có thể bị lấp một phần "
               "bởi bụi bẩn có thể dẫn điện, và gờ có thể đóng vai trò là rào "
               "cản cho phép bụi bẩn tích tụ ở góc vuông giữa chúng và lớp "
               "cách điện. Vì những lý do này, trong mọi trường hợp dùng gờ"))
    b.append(fig(5, FB.fig_f1205()))
    b.append(note("<b>Lưu ý về nhãn trong Hình 12.5.</b> Lớp văn bản OCR của "
                  "hình này gồm chủ yếu là các nét machine-drawn vô nghĩa "
                  "(như 'k---\\--- ---_ +/' và '\\/ \\'); các nhãn lấy từ "
                  "bản render - 'Creepage distance', 'Clearance', 'Conductors', "
                  "'Conductor', 'Insulator' và 'Insulation' - được dùng trong "
                  "hình vẽ lại."))
    b.append(p("hoặc rãnh để tăng chiều dài đường rò, các khoảng cách đó cần "
               "lớn hơn các khoảng cách trên bề mặt cách điện phẳng để đem "
               "lại mức độ an toàn như nhau. Điều này đạt được bằng cách dùng "
               "các giá trị của nhóm cách điện có giá trị CTI thấp hơn liền "
               "kề với nhóm đang xét để xác định chiều dài đường rò tối thiểu. "
               "Điều này có nghĩa là đối với vật liệu thuộc Nhóm I (CTI >600) "
               "có rãnh hoặc gờ, chiều dài đường rò tối thiểu sẽ được lấy từ "
               "cột của Bảng 12.1 tương ứng với vật liệu cách điện thuộc Nhóm "
               "II (CTI 400–600). Điều này thực tế loại trừ vật liệu cách điện "
               "Nhóm IIIa khi bất kỳ rãnh hoặc gờ nào được dùng để tăng chiều "
               "dài đường rò. Dĩ nhiên những vật liệu đó vẫn có thể được dùng, "
               "với điều kiện là phần tăng khoảng cách do chiều cao của gờ "
               "hoặc độ sâu của rãnh không được tính đến. Hình 12.6, 12.7 và "
               "12.8 cho thấy cách đo chiều dài đường rò khi có rãnh và gờ, "
               "và khi có vít cố định nằm trong rãnh."))
    b.append(note("<b>Lưu ý về các hình được viện dẫn.</b> Hình 12.7, 12.8 và "
                  "12.9 được nhắc đến trong thân bài nhưng nằm ngoài phạm vi "
                  "trích này; chỉ Hình 12.5 và Hình 12.6 được tái dựng tại đây."))

    b.append(p("Để được xem là rãnh phục vụ việc đo chiều dài đường rò, rãnh "
               "phải sâu ít nhất 2.5 mm và rộng ít nhất 2.5 mm nếu thành và "
               "đáy rãnh vuông góc. Tuy nhiên, nếu rãnh không có dạng đều đặn "
               "như vậy, ví dụ đáy rãnh được bo tròn, thì bất kỳ phần nào của "
               "khoảng cách mà khoảng cách theo mặt phẳng nhỏ hơn 2.5 mm sẽ "
               "bị bỏ qua (xem Hình 12.6). Khi hiệu điện áp sao cho chiều dài "
               "đường rò yêu cầu nhỏ hơn 3 mm (khoảng 150 V đối với vật liệu "
               "nhóm I và 50 V đối với vật liệu thuộc Nhóm II), chiều rộng "
               "rãnh có thể giảm xuống 1.5 mm vì mức độ nghiêm trọng thấp hơn "
               "ở điện áp thấp như vậy. Khi các rãnh đó chứa vít, tình huống "
               "được thể hiện trong Hình 12.8, cho thấy các cân nhắc hiệu dụng "
               "tương tự được áp dụng."))
    b.append(note("<b>Lưu ý về 'group 1' và cách viết số với đơn vị.</b> Bản "
                  "in dùng chữ số Ả Rập '1' trong cụm 'materials of group 1' "
                  "nhưng chữ số La Mã 'II' trong 'materials of Group II'. Sự "
                  "không nhất quán này được giữ nguyên trong bản tiếng Anh; "
                  "bản tiếng Việt dùng 'nhóm I' theo ý định. Cách viết số và "
                  "đơn vị cũng được giữ theo bản in: '2.5mm', '3mm', '1.5mm' "
                  "và '50V' không có dấu cách, nhưng '150 V' có dấu cách."))
    b.append(note("<b>Lưu ý về 'Fig 12.6' không có dấu chấm.</b> Trong đoạn "
                  "này bản in viết 'Fig 12.6' không có dấu chấm, trong khi "
                  "những chỗ khác viết 'Fig. 12.5' và 'Fig. 12.8', và đoạn "
                  "trước đó viết đầy đủ 'Figure 12.6, 12.7 and 12.8'. Sự "
                  "không nhất quán được giữ nguyên trong bản tiếng Anh."))

    # Printed p.303 ends mid-sentence; printed p.304 is entirely Fig. 12.6;
    # the sentence resumes at the top of printed p.305.
    b.append(p("Để được xem là gờ phục vụ việc đo chiều dài đường rò, gờ phải "
               "cao ít nhất 2.5 mm. Chiều dày tối thiểu của gờ cho mục đích "
               "này là 1 mm, nhưng mọi gờ phải đủ cứng vững để tránh bị đẩy "
               "sang một bên hoặc hư hỏng do bất kỳ hoạt động hợp lệ nào "
               "liên quan"))
    b.append(fig(6, FB.fig_f1206()))
    b.append(note("<b>Lưu ý về chú thích và nhãn trong Hình 12.6.</b> Ở trang "
                  "304, chú thích của hình dùng '(note 1)', '(note 2)', "
                  "'(note 3)' viết thường, nhưng nhãn trong hình lại dùng "
                  "'(Note 3)' viết hoa; ở trang 305 dùng '(Note 2)', '(Note 1)' "
                  "và 'Note 3' không có ngoặc. Các nhãn kích thước mà lớp OCR "
                  "đọc là '22.5 mm' và 'e.5 mm' thực chất là dạng nhỏ hơn "
                  "2.5 mm và dạng không nhỏ hơn 2.5 mm theo bản render. Tất "
                  "cả được giữ theo bản in trong hình vẽ lại."))
    b.append(p("đến gờ, chẳng hạn như việc nối dây dẫn. Điều này không có "
               "nghĩa là gờ phải có độ bền tương tự như vỏ bọc, mà là nó phải "
               "có độ bền đầy đủ cho mục đích sử dụng của nó. Gờ có thể là "
               "một phần nguyên khối của khối cách điện đúc, hoặc có thể được "
               "dán vào lớp cách điện, với điều kiện toàn bộ bề mặt tiếp xúc "
               "giữa gờ và lớp cách điện được dán kín. Khi không phải vậy, "
               "chiều dài đường rò sẽ được giả định là đi bên dưới gờ nếu "
               "đường đó ngắn hơn (xem Hình 12.7)."))

    b.append(p("Chỉ có hai biến thể so với phần trên. Thứ nhất là trường hợp "
               "các bộ phận dẫn điện liên quan đến phương tiện nối dây dẫn "
               "bên ngoài. Trong những trường hợp này có chiều dài đường rò "
               "và khe hở tuyệt đối tối thiểu là 3 mm. Điều này được xem là "
               "mức tối thiểu cần thiết để đảm bảo có thể thực hiện các mối "
               "nối mà không có nguy cơ ngắn mạch và do đó là một giới hạn "
               "vật lý."))
    b.append(p("Biến thể thứ hai liên quan đến chụp đèn và đui đèn kiểu vặn "
               "ren (đây là kiểu kết hợp chụp đèn/đui đèn duy nhất được công "
               "nhận là an toàn tăng cường mà không cần phải thử nghiệm để "
               "đảm bảo chúng không truyền lửa do đánh lửa trong khi tháo "
               "hoặc lắp). Trong trường hợp này đã có các Tiêu chuẩn hiện "
               "hành quản lý cấu tạo của chúng, và các Tiêu chuẩn đó đưa ra "
               "các giá trị hơi khác so với trường hợp chung của thiết bị an "
               "toàn tăng cường. Để tránh phải phát triển một dây đèn đặc "
               "biệt cho đui đèn kiểu vặn ren, các giá trị khác nhau nêu "
               "trong Bảng 12.2 được dùng cho cả lớp cách điện trên chụp ren "
               "của đèn và trong đui đèn. Đây là các giá trị lấy từ Tiêu "
               "chuẩn công nghiệp phù hợp và đủ tin cậy để dùng nguyên không "
               "thay đổi trong trường hợp này. Tuy nhiên, CTI của lớp cách "
               "điện được yêu cầu thuộc Nhóm I."))
    b.append(note("<b>Lưu ý về 'lampholder/cap' và chữ 'Standards' viết hoa.</b> "
                  "Lớp OCR chèn thêm dấu cách thành 'lampholder /cap'; bản in "
                  "viết 'lampholder/cap' không có dấu cách trước dấu gạch "
                  "chéo. Bản in cũng viết hoa 'Standards' hai lần giữa câu "
                  "và viết 'industrial Standard'. Các dạng này được giữ "
                  "nguyên trong bản tiếng Anh."))
    b.append(p("Để cho thấy ví dụ về các loại vật liệu thuộc các mức CTI "
               "khác nhau, Bảng 12.3 được đưa vào. Bảng này chỉ mang tính "
               "hướng dẫn và không nhằm liệt kê đầy đủ, vì nhiều vật liệu "
               "thuộc một loại nhất định có thể, nếu xử lý theo những cách "
               "nhất định, có CTI khác khá nhiều so với giá trị trong bảng. "
               "Tuy nhiên, bảng cũng cho thấy phần nào các loại cách điện "
               "cần tìm cho một ứng dụng cụ thể."))

    b.append(h3("12.2.4 Cách điện", "12.2.4 Insulation"))
    b.append(p("Cách điện bên trong thiết bị về cơ bản gồm hai loại, đó là "
               "loại dùng trên dây dẫn và loại dùng trong các thứ như khối "
               "cọc nối hoặc làm một lớp"))
    b.append(note("<b>Lưu ý về ranh giới câu cuối.</b> Câu cuối của mục 12.2.4 "
                  "trong phạm vi này kết thúc bằng dấu phẩy vì tiếp tục ở "
                  "trang in 306 (nằm ngoài phạm vi). Dấu phẩy được giữ nguyên "
                  "theo bản in."))
    return "".join(b)


def body_en():
    b = []

    # Figures 12.3 and 12.4 are printed on p.301 (end of 12.2.2); they open
    # this module's figure run. Printed pp.302-305 follow.
    b.append(note("<b>Note on the placement of Figures 12.3 and 12.4.</b> These "
                  "two figures are printed on p. 301 at the end of 12.2.2 on "
                  "terminals and connection facilities, but are reproduced at "
                  "the opening of this module so that Figures 12.3-12.6 appear "
                  "together. The printed captions and labels are retained."))
    b.append(fig(3, FA.fig_f1203()))
    b.append(fig(4, FA.fig_f1204()))

    # Printed p.302, first paragraph (continuation of 12.2.3).
    b.append(p("As the breakdown of insulation is usually more likely than the "
               "breakdown of air, the creepage distance figures are normally "
               "greater than those for clearance (see Table 12.1). The working "
               "voltage figure in Table 12.1 is the highest figure of voltage "
               "which can occur across the conductors in question, either with "
               "recognized supply and load variations or with open circuits "
               "applied in the apparatus where these give worse conditions. "
               "Transient voltages are ignored as these do not normally "
               "influence tracking. Fig. 12.5 shows the basic difference "
               "between creepage distances and clearances."))
    b.append(note("<b>Note on the OCR reading of 'occur'.</b> The OCR text layer "
                  "reads 'can occw' in the first paragraph; the page render "
                  "shows that the print reads 'can occur'. The English text "
                  "follows the print."))

    # Table 12.1 sits after the first paragraph on printed p.302.
    b.append(table(T1.HEAD121_EN, T1.ROWS121, T1.CAPTION121_EN))
    if T1.NOTE121_EN:
        b.append(note(T1.NOTE121_EN))
    b.append(note("<b>Note on the symbols in Table 12.1.</b> The OCR text layer "
                  "lost the inequality signs in the voltage column (for "
                  "example it reads '15< U 530' where the print has "
                  "'15< U ≤30', and '550~ U5750' where the print has "
                  "'550< U ≤750') and misreads 'Material Group IIIa³' as "
                  "'Material Group ma3' and 'Material Group IIIa' as 'Materid "
                  "Group ma' in footnote 3. The correct characters are taken "
                  "from the page render. The source line '(from BS EN 50019)' "
                  "is kept as printed, including the unspaced 'BS EN'."))

    # Printed p.302 ends mid-sentence: '...in all cases where ribs'; Fig. 12.5
    # occupies the top of printed p.303; the sentence resumes below the figure.
    b.append(p("While the above deals effectively with the situation where the "
               "insulating surface is even, as shown in Fig. 12.5, it does not "
               "adequately cover many normal situations where there are grooves "
               "in the insulation, or where there are ribs which separate "
               "conductors, both of which situations often occur in terminal "
               "blocks. In these circumstances, additional problems can "
               "sometimes occur. Grooves can be partially filled with dirt "
               "which may conduct, and ribs can act as barriers allowing dirt "
               "to build up in the right angle between themselves and the "
               "insulation. For these reasons, in all cases where ribs"))
    b.append(fig(5, FB.fig_f1205()))
    b.append(note("<b>Note on the labels in Figure 12.5.</b> The OCR text layer "
                  "of this figure consists mainly of meaningless machine-drawn "
                  "strokes (such as 'k---\\--- ---_ +/' and '\\/ \\'); the "
                  "labels taken from the render - 'Creepage distance', "
                  "'Clearance', 'Conductors', 'Conductor', 'Insulator' and "
                  "'Insulation' - are used in the redraw."))
    b.append(p("or grooves are used to increase creepage distances those "
               "distances will need to be larger than those which occur on flat "
               "insulation to give the same assurance of security. This is "
               "achieved by using the figures for the group of insulation with "
               "the adjacent lower CTI value to that in question for "
               "determination of minimum creepage distances. This means that "
               "for materials of Group I (CTI >600) with grooves or ribs, the "
               "minimum creepage distances will be taken from the column of "
               "Table 12.1 appropriate to insulating materials of Group II "
               "(CTI 400–600). This effectively excludes Group IIIa insulating "
               "materials where any grooves or ribs are used to enhance "
               "creepage distances. Such materials may of course, be used "
               "provided the added separation given by the rib height or the "
               "groove depth is ignored. Figure 12.6, 12.7 and 12.8 show how "
               "creepage distances are measured in the presence of grooves and "
               "ribs, and where fixing screws are included in grooves."))
    b.append(note("<b>Note on the cited figures.</b> Figures 12.7, 12.8 and "
                  "12.9 are mentioned in the prose but fall outside this "
                  "extracted span; only Figures 12.5 and 12.6 are redrawn here."))

    b.append(p("To be considered as a groove for the purposes of measuring "
               "creepage distances, a groove must be at least 2.5mm deep and "
               "2.5mm wide if it has square sides and bottom. If it is not of "
               "such regular shape, however, as is the case when the bottom is, "
               "for example, radiused, then any part of the separation where "
               "the plane distance is less than 2.5mm is ignored (see Fig "
               "12.6). Where the voltage difference is such that less than 3mm "
               "of creepage distance is required (approximately 150 V for "
               "materials of group 1 and 50V for materials of Group II) the "
               "groove width may be reduced to 1.5mm because of the lower level "
               "of criticality at such low voltages. Where such grooves contain "
               "screws, the situation is shown in Fig. 12.8, which shows the "
               "same effective considerations are applied."))
    b.append(note("<b>Note on 'group 1' and number/unit spacing.</b> The print "
                  "uses the Arabic digit '1' in 'materials of group 1' but the "
                  "Roman numeral 'II' in 'materials of Group II'. The "
                  "inconsistency is kept as printed; the Vietnamese follows "
                  "the intended Group I. The number/unit spacing is also kept "
                  "as printed: '2.5mm', '3mm', '1.5mm' and '50V' have no space, "
                  "while '150 V' has one."))
    b.append(note("<b>Note on 'Fig 12.6' without a period.</b> In this paragraph "
                  "the print writes 'Fig 12.6' with no full stop, whereas "
                  "elsewhere it writes 'Fig. 12.5' and 'Fig. 12.8', and the "
                  "previous paragraph spells out 'Figure 12.6, 12.7 and 12.8'. "
                  "The inconsistency is kept as printed."))

    # Printed p.303 ends mid-sentence; printed p.304 is entirely Fig. 12.6;
    # the sentence resumes at the top of printed p.305.
    b.append(p("To be considered as a rib for the purposes of measurement of "
               "creepage distances, the rib must be at least 2.5 mm high. The "
               "minimum thickness of a rib for this purpose is 1 mm, but any "
               "rib must be sufficiently rigid to avoid being pushed aside or "
               "damaged by any legitimate activity associated"))
    b.append(fig(6, FB.fig_f1206()))
    b.append(note("<b>Note on the notes and labels in Figure 12.6.</b> On "
                  "printed p. 304 the figure caption uses lowercase '(note 1)', "
                  "'(note 2)', '(note 3)', while the in-figure marker reads "
                  "'(Note 3)' with a capital; on printed p. 305 the markers are "
                  "'(Note 2)', '(Note 1)' and a bare 'Note 3'. The dimension "
                  "labels that the OCR layer reads as '22.5 mm' and 'e.5 mm' "
                  "are, in the render, the less-than-2.5 mm and at-least-2.5 mm "
                  "forms. All are retained as printed in the redraw."))
    b.append(p("with the rib, such as terminating conductors. This does not "
               "mean that it must have similar strength to the enclosure, but "
               "that it must have adequate strength for the use to which it is "
               "put. Ribs may be either an integral part of the insulation "
               "moulding or may be cemented into the insulation, provided that "
               "the entire interface between the rib and the insulation is "
               "cemented. Where this is not so, the creepage distance will be "
               "assumed to be under the rib if this is shorter (see Fig. 12.7)."))

    b.append(p("There are only two variations to the above. The first is where "
               "the conducting parts are associated with connection facilities "
               "for external conductors. In these cases there is an absolute "
               "minimum creepage distance and clearance of 3mm. This is "
               "considered as the minimum necessary to ensure that connections "
               "can be made without risks of short circuit and is therefore a "
               "physical limitation."))
    b.append(p("The second variation relates to screw lamp caps and holders "
               "(the only type of lampholder/cap combination recognized as "
               "increased safety without having to be tested to ensure they do "
               "not transmit flame as a result of sparking during removal or "
               "fitting). In this case there are Standards already in existence "
               "governing their construction and those Standards give slightly "
               "different figures than is the case for increased safety "
               "equipment in general. To avoid having the necessity to develop "
               "a special series of lamp for screw lampholders, the different "
               "figures given in Table 12.2 are used for both the insulation on "
               "the screw cap of the lamp and in the lampholder. These are the "
               "figures from the appropriate industrial Standard and give "
               "sufficient confidence to be used without change in this case. "
               "The CTI of the insulation is, however, required to be of Group I."))
    b.append(note("<b>Note on 'lampholder/cap' and the capitalised "
                  "'Standards'.</b> The OCR layer inserts a space, giving "
                  "'lampholder /cap'; the print reads 'lampholder/cap' with no "
                  "space before the slash. The print also capitalises "
                  "'Standards' twice mid-sentence and writes 'industrial "
                  "Standard'. These forms are kept as printed."))
    b.append(p("To give some idea of the types of material falling into the "
               "various CTI levels Table 12.3 is included. This is for "
               "indication only and does not seek to be exhaustive, as many "
               "materials of a particular type can, if treated in certain ways, "
               "have a CTI quite different from that in the table. The table "
               "does, however, give some idea of the types of insulation to be "
               "sought for a particular use."))

    b.append(h3("12.2.4 Insulation", "12.2.4 Insulation"))
    b.append(p("Insulation within apparatus is basically of two types, namely "
               "that used on conductors and that used in such things as "
               "terminal blocks or as a layer"))
    b.append(note("<b>Note on the final sentence boundary.</b> The last "
                  "sentence of 12.2.4 within this span ends with a comma "
                  "because it continues on printed p. 306 (outside the span). "
                  "The comma is kept as printed."))
    return "".join(b)
