# -*- coding: utf-8 -*-
"""Chapter 10, module B — bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998). Covers the flat-flange-joint discussion:
the opening of "Flat flange joints" (printed p. 230), weather proofing,
facilities for fixings, flange geometry and bolt clearance through printed
p. 235, plus the continuation and the IIB/IIA restrictions on printed p. 236
that precede "2 Spigot joints" (module C). Figures 10.1–10.5 and Tables
10.1–10.4 are placed at their printed positions. Printed quirks are kept in
the English text (micro sign, superscript footnote markers, 'o' rings, the
singular "Fig. 10.4 and 10.5", 'rivetting', the printed 'cm³' unit, and the
figure legends), with bilingual notes; the Vietnamese follows the intended
meaning. The shell owns the chapter h2, references and end matter.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, table, fig
import mcmillanfig10a as FA
import mcmillan_tbl10_1_5 as T1


def body_vi():
    b = []
    b.append(fig(1, FA.fig_f1001()))
    b.append(h4("Mối nối mặt bích phẳng", "Flat flange joints"))
    b.append(p("Mối nối mặt bích phẳng là dạng mối nối cổ nhất (cùng với các "
               "mối nối hình trụ) và có lẽ là dạng dễ chế tạo nhất. Hình 10.2 "
               "cho thấy các cấu hình cơ bản của mối nối mặt bích. Các mối nối "
               "được yêu cầu phải có chất lượng giới hạn nhất định. Ví dụ, "
               "mỗi trong hai bề mặt của mặt bích phải có độ nhám không thô "
               "hơn 6.3 μm theo ISO 468 (1982)¹⁰. Đây không phải là một yêu "
               "cầu đặc biệt nghiêm ngặt"))
    b.append(fig(2, FA.fig_f1002()))
    b.append(p("nhưng nó loại trừ các hiện tượng như lỗ rỗng do đúc và các "
               "vết xước sâu trên bề mặt, cả hai đều có thể tạo điều kiện cho "
               "ngọn lửa truyền ra khỏi vỏ bọc. Chiều dài tối thiểu của mối "
               "nối cũng được quy định, cùng với khe hở tối đa tương ứng giữa "
               "các mặt bích, và các số liệu hiện hành cho những thông số này "
               "được cho trong Bảng 10.1, bảng liên quan đến Hình 10.2."))
    b.append(note("<b>Lưu ý về ký hiệu và chỉ số chú thích trong nguyên bản.</b> "
                  "Trang in ghi '6.3 μm' (ký hiệu micro), 'ISO 468 (1982)¹⁰' "
                  "và các chỉ số chú thích ở dạng mũ như 'BS 5501, Part 5⁵' "
                  "và 'BS/EN 50018⁶'; lớp văn bản OCR đọc nhầm thành "
                  "'6.3~m', 'IS0' và các ký tự thường. Bản tiếng Anh giữ nguyên "
                  "cách in."))
    b.append(table(T1.HEAD101_VI, T1.ROWS101, T1.CAPTION101_VI))
    b.append(note(T1.NOTE101_VI))

    b.append(h4("Chống thấm thời tiết cho mối nối mặt bích phẳng",
                "Weather proofing of flat flanged joints"))
    b.append(p("Trước đây người ta đã nhận ra rằng việc đưa các vật như đệm "
               "kín hoặc vòng ‘o’ vào giữa các bề mặt mối nối để chống thấm "
               "thời tiết có thể gây ra vấn đề, vì đệm kín hoặc vòng ‘o’ có thể "
               "làm cho không thể bảo đảm khe hở tối đa yêu cầu; điều này dẫn "
               "đến việc gần như cấm các kỹ thuật chống thấm thời tiết đó "
               "trong các mối nối mặt bích. Tình trạng này đã được nới lỏng ở "
               "mức độ nhất định trong BS 5501, Part 5⁵"))
    b.append(fig(3, FA.fig_f1003()))
    b.append(p("(ấn bản đầu tiên của Tiêu chuẩn châu Âu) bằng cách bỏ đi mọi "
               "phát biểu cấm đoán, và trong BS/EN 50018⁶ (ấn bản thứ hai của "
               "Tiêu chuẩn châu Âu) đã được loại bỏ hoàn toàn nhờ đưa vào hướng "
               "dẫn lắp đệm kín theo cách duy trì được tính toàn vẹn của mối "
               "nối. Hướng dẫn này yêu cầu tạo một rãnh nằm bên trong đường "
               "mối nối thực tế hoặc bên ngoài nó, và lắp một vòng ‘o’ hoặc "
               "loại đệm kín tương tự vào rãnh đó (xem Hình 10.3). Điều này làm "
               "rộng mặt bích và làm cho vỏ bọc cồng kềnh hơn nhưng thực sự "
               "giải quyết được vấn đề chống thấm thời tiết cho vỏ bọc. Người "
               "ta khuyến nghị rằng đệm kín dạng vòng ‘o’ luôn được lắp ở phía "
               "ngoài mặt bích vì, đặc biệt trong trường hợp mối nối kim loại, "
               "các mặt bích bị ăn mòn khi lắp đặt ngoài trời và trong các môi "
               "trường tương tự khắc nghiệt, và sự ăn mòn đó có thể làm hỏng "
               "mối nối và cho phép truyền ngọn lửa."))
    b.append(note("<b>Lưu ý về vòng ‘o’ và cụm 'weather proofing'.</b> Nguyên "
                  "bản in ‘o’ ring với chữ o thường trong dấu ngoặc kép, không "
                  "phải số 0; lớp OCR ghi là ‘0’ ring. Cụm 'weather proofing' "
                  "luôn được in thành hai từ, kể cả trong tiêu đề; bản tiếng "
                  "Anh giữ nguyên."))

    b.append(h4("Phương tiện cố định cho các bộ phận của vỏ mặt bích phẳng",
                "Facilities for fixings for parts of flat flanged enclosures"))
    b.append(p("Người ta thừa nhận rằng các bộ phận của vỏ bọc tạo thành mối "
               "nối sẽ cần được cố định, và nếu các chi tiết cố định nằm bên "
               "ngoài mặt bích thì chiều rộng của mặt bích sẽ tăng đáng kể. Vì "
               "mục đích đó, sau nhiều năm thử nghiệm, người ta đã xác định "
               "được một tình huống trong đó các lỗ để cố định có thể đi xuyên "
               "qua chính mặt bích. Điều này dựa trên kết luận rằng lỗ hở cho "
               "bulông là một đường dẫn ra môi trường bên ngoài hoặc vào bên "
               "trong vỏ bọc và, cũng như các khe hở ngọn lửa khác, thường trở "
               "nên rõ rệt nhất trong một vụ nổ bên trong, ngay cả sau khi đã "
               "đáp ứng các yêu cầu về kích thước của mối nối. Sự mở rộng này "
               "được xử lý bằng một thử nghiệm hệ số an toàn."))
    b.append(p("Chiều dài của đường đi (xem Hình 10.4 và 10.5) được yêu cầu "
               "giữa lỗ bulông không được bảo vệ và bên trong hoặc bên ngoài "
               "vỏ bọc (tùy theo hình học của vỏ bọc) được xác định trong Bảng "
               "10.2. Cần lưu ý rằng các lỗ hở cho chi tiết cố định và các lỗ "
               "ren phải đáp ứng một số tiêu chí nhất định."))
    b.append(fig(4, FA.fig_f1004()))
    b.append(p("Các ren và độ bền của bulông sẽ được đề cập sau trong chương "
               "này nhưng các lỗ hở phải đáp ứng các yêu cầu của Bảng 10.3."))
    b.append(p("Khi các bulông cố định đi vào thân chính của vỏ bọc từ bên "
               "ngoài, có một số yêu cầu nhất định áp dụng để bảo đảm chúng "
               "không ảnh hưởng xấu đến tính chất chống cháy của vỏ bọc. Yêu "
               "cầu thứ nhất là nếu ren xuyên qua vỏ bọc và do đó trở thành "
               "một khe hở ngọn lửa thì nó phải tuân thủ yêu cầu đối với mối "
               "nối ren. Để tránh mòn, nó cũng phải được cố định vào vỏ bọc "
               "bằng hàn, đinh tán (rivetting) hoặc một phương pháp cố định "
               "tương tự."))
    b.append(note("<b>Lưu ý về trích dẫn hình và chính tả.</b> Nguyên bản viết "
                  "'see Fig. 10.4 and 10.5' với một chữ 'Fig.' cho cả hai số; "
                  "giữ nguyên cách viết này. Nguyên bản cũng viết 'rivetting' "
                  "với hai chữ t và dùng 'bolt hole' (hai từ) trong văn bản, "
                  "trong khi chú giải hình dùng 'Bolthole' (Hình 10.4) và "
                  "'bolthole' (Hình 10.5)."))
    b.append(fig(5, FA.fig_f1005()))
    b.append(note("<b>Lưu ý về chú giải các Hình 10.3–10.5.</b> Chú giải Hình "
                  "10.3 dùng ký hiệu Hy Lạp α cho khe hở tối đa và có cụm "
                  "'Table 10.2' đính kèm dòng chú giải như trong bản in. Ký "
                  "hiệu kích thước là chữ 'l' thường (không phải số 1 hay chữ "
                  "I). Chú thích của Hình 10.5 thiếu dấu apostrophe trong cụm "
                  "'enclosures walls' đúng như bản in."))
    b.append(p("Khi lỗ ren không xuyên qua thành vỏ bọc thì độ dày của vật "
               "liệu vỏ bọc giữa lỗ ren và bên trong vỏ bọc, khi đầu bulông "
               "nằm bên ngoài vỏ bọc (xem Hình 10.5), hoặc giữa lỗ ren và bên "
               "ngoài vỏ bọc, khi đầu bulông nằm bên trong vỏ bọc, phải có ít "
               "nhất độ dày cho trong Bảng 10.4 để bảo đảm vỏ bọc và chi tiết "
               "cố định có độ bền thỏa đáng."))
    b.append(table(T1.HEAD102_VI, T1.ROWS102, T1.CAPTION102_VI))
    b.append(note(T1.NOTE102_VI))
    b.append(table(T1.HEAD103_VI, T1.ROWS103, T1.CAPTION103_VI))
    b.append(note(T1.NOTE103_VI))
    b.append(p("Do mức độ nghiêm trọng của vụ nổ khi có hydro, có những giới "
               "hạn nghiêm ngặt về kích thước vỏ bọc có mối nối mặt bích phẳng "
               "đối với thiết bị nhóm IIC. Vỏ bọc có thể tích lớn hơn 500 cm³ "
               "với mối nối mặt bích không được phép dùng với bất kỳ chiều "
               "rộng mặt bích nào, và những vỏ trên 100 cm³ phải có mặt bích "
               "rộng hơn 9.5 mm. Tương tự, mối nối mặt bích không được phép "
               "dùng trong môi trường axetilen, dù axetilen theo danh nghĩa "
               "thuộc nhóm con IIC, vì sự hình thành cacbon liên quan đến các "
               "vụ nổ axetilen và khả năng sự hình thành này ngăn không cho "
               "mối nối ngồi đúng chỗ khi lắp lại. Cũng có khả năng thực sự là "
               "sự phóng ra"))
    b.append(table(T1.HEAD104_VI, T1.ROWS104, T1.CAPTION104_VI))
    b.append(note(T1.NOTE104_VI))
    b.append(p("các hạt cacbon nóng rực trong một vụ nổ và những hạt này có "
               "thể mang đủ năng lượng để gây cháy."))
    b.append(p("Các hạn chế tương tự nhưng ít nghiêm ngặt hơn tồn tại đối với "
               "vỏ bọc thuộc nhóm con IIB và IIA: mặt bích nhỏ hơn 9.5 mm "
               "không được phép dùng cho vỏ bọc IIB có thể tích vượt quá 100 "
               "cm³, và mặt bích nhỏ hơn 12.5 mm không được phép dùng cho "
               "những vỏ có thể tích trên 500 cm³ — dù trong trường hợp này, "
               "khác với tình trạng ở nhóm con IIC, vỏ lớn hơn vẫn được phép "
               "và không có giới hạn về kích thước, miễn là chiều rộng mặt "
               "bích không nhỏ hơn 12.5 mm."))
    b.append(note("<b>Lưu ý về đơn vị trong nguyên bản.</b> Đoạn này in "
                  "'flanges of less than 12.5 cm³'; theo ngữ cảnh, đơn vị đúng "
                  "phải là mm. Bản tiếng Anh giữ nguyên 'cm³' như bản in, còn "
                  "bản tiếng Việt dùng mm theo ý định của tác giả."))
    return "".join(b)


def body_en():
    b = []
    b.append(fig(1, FA.fig_f1001()))
    b.append(h4("Flat flange joints", "Flat flange joints"))
    b.append(p("Flat flange joints are the oldest form of joint (together "
               "with cylindrical joints) and probably the easiest to "
               "construct. Figure 10.2 shows the basic flange-joint "
               "configurations. The joints are required to be of certain "
               "limiting quality. For example, the two faces of the flange "
               "are each required to be no rougher than 6.3 μm in accordance "
               "with ISO 468 (1982)¹⁰. This is not a particularly"))
    b.append(fig(2, FA.fig_f1002()))
    b.append(p("stringent specification but precludes such things as casting "
               "blowholes and deep scores in the surfaces, both of which "
               "could assist flame transmission out of the enclosure. The "
               "minimum length of joints is also specified, together with "
               "the matching maximum gap between flanges, and the current "
               "figures for these are given in Table 10.1 which relates to "
               "Fig. 10.2."))
    b.append(note("<b>Source note on symbols and footnote markers.</b> The "
                  "print reads '6.3 μm' (micro sign), 'ISO 468 (1982)¹⁰' and "
                  "superscript footnote markers such as 'BS 5501, Part 5⁵' "
                  "and 'BS/EN 50018⁶'; the OCR text layer rendered these as "
                  "'6.3~m', 'IS0' and ordinary characters. The printed forms "
                  "are kept here."))
    b.append(table(T1.HEAD101_EN, T1.ROWS101, T1.CAPTION101_EN))
    b.append(note(T1.NOTE101_EN))

    b.append(h4("Weather proofing of flat flanged joints",
                "Weather proofing of flat flanged joints"))
    b.append(p("Historically it has been recognized that the introduction of "
               "such things as gaskets or ‘o’ rings for weather proofing "
               "between the joint surfaces could cause problems, as the "
               "gasket or ‘o’ ring could make it impossible to guarantee the "
               "maximum gap required, and this led to the virtual prohibition "
               "of such weather proofing techniques in flanged joints. This "
               "situation was"))
    b.append(fig(3, FA.fig_f1003()))
    b.append(p("relaxed to a degree in BS 5501, Part 5⁵ (the first edition of "
               "the European Standard) by removal of any prohibitive "
               "statements and in BS/EN 50018⁶ (the second edition of the "
               "European Standard) has been fully removed by the inclusion of "
               "guidance on the fitting of gaskets in a way which maintains "
               "the joint integrity. This guidance requires a groove to be "
               "inserted either inside the actual joint path or outside it "
               "and the fitting of an ‘o’ ring or similar style of gasket in "
               "that groove (see Fig. 10.3). This widens the flange and makes "
               "the enclosure more cumbersome but does overcome the problem "
               "of weather proofing the enclosure. It is recommended that the "
               "‘o’ ring-type gasket is always fitted on the outside of the "
               "flange as, particularly in the case of metal joints, the "
               "flanges are subject to corrosion in the case of installation "
               "in outdoor and similar hostile environments, and such "
               "corrosion could damage the joint and permit flame "
               "transmission."))
    b.append(note("<b>Source note on the ‘o’ ring and 'weather proofing'.</b> "
                  "The print gives ‘o’ ring with a lowercase letter o in "
                  "curly quotes, not the digit 0; the OCR text layer read "
                  "‘0’ ring. The phrase 'weather proofing' is printed as two "
                  "words throughout, including in the heading."))

    b.append(h4("Facilities for fixings for parts of flat flanged enclosures",
                "Facilities for fixings for parts of flat flanged enclosures"))
    b.append(p("It is recognized that the parts of the enclosure forming the "
               "joint will require fixing, and if the fixings are outside the "
               "flanges the width of the flanges would be significantly "
               "increased. To this end, as a result of experimentation over "
               "the years, a situation where the holes for fixing may pass "
               "through the flange itself has been identified. This is based "
               "upon the conclusion that the bolt clearance hole is a passage "
               "to the outside environment or the interior of the enclosure "
               "and, in common with the other flamepaths, is usually most "
               "pronounced during an internal explosion, even after satisfying "
               "the dimensional requirements for joints. This enlargement is "
               "taken care of by a safety factor test."))
    b.append(p("The length of path (see Fig. 10.4 and 10.5) required between "
               "the unprotected bolt hole and the interior or exterior of "
               "the enclosure (depending upon the enclosure geometry) is "
               "defined in Table 10.2. It should be noted that the clearance "
               "holes for the fasteners and the threaded holes are required "
               "to satisfy certain criteria."))
    b.append(fig(4, FA.fig_f1004()))
    b.append(p("The threads and bolt strengths will be dealt with later in "
               "this chapter but the clearance holes should satisfy the "
               "requirements of Table 10.3."))
    b.append(p("Where the fixing bolts enter the main body of the enclosure "
               "from outside there are certain requirements which apply to "
               "ensure they do not adversely affect the flameproof properties "
               "of the enclosure. The first is that if the thread penetrates "
               "the enclosure and therefore becomes a flamepath it must "
               "comply with the requirement for threaded joints. To avoid "
               "wear, it must also be secured to the enclosure by welding, "
               "rivetting or a method of similar security."))
    b.append(note("<b>Source note on the figure reference and spelling.</b> "
                  "The print has 'see Fig. 10.4 and 10.5' with a single 'Fig.' "
                  "governing both numbers; the wording is kept as printed. "
                  "The print also has 'rivetting' with double t, and uses "
                  "'bolt hole' (two words) in the prose while the figure "
                  "legends use 'Bolthole' (Fig. 10.4) and 'bolthole' "
                  "(Fig. 10.5)."))
    b.append(fig(5, FA.fig_f1005()))
    b.append(note("<b>Source note on the Fig. 10.3–10.5 legends.</b> The "
                  "Fig. 10.3 legend uses the Greek letter α for the maximum "
                  "gap and carries the stray 'Table 10.2' at the end of that "
                  "legend line exactly as printed. The dimension symbol is "
                  "lowercase italic 'l', not the digit 1 or the letter I. The "
                  "Fig. 10.5 caption reads 'enclosures walls' without the "
                  "apostrophe, as printed."))
    b.append(p("Where the threaded hole does not penetrate the enclosure wall "
               "the thickness of enclosure material between the threaded hole "
               "and the inside of the enclosure where the bolt head is "
               "outside the enclosure (see Fig. 10.5) or between the threaded "
               "hole, and the outside of the enclosure where the bolt head is "
               "inside the enclosure must have at least the thickness given "
               "in Table 10.4 to ensure that the enclosure and fixing have "
               "adequate strength."))
    b.append(table(T1.HEAD102_EN, T1.ROWS102, T1.CAPTION102_EN))
    b.append(note(T1.NOTE102_EN))
    b.append(table(T1.HEAD103_EN, T1.ROWS103, T1.CAPTION103_EN))
    b.append(note(T1.NOTE103_EN))
    b.append(p("Because of the severity of explosions where hydrogen is "
               "present there are severe limits on the size of enclosures "
               "with plane flanged joints for group IIC apparatus. Enclosures "
               "greater than 500 cm³ volume with flanged joints are not "
               "permitted with any width of flange, and those over 100 cm³ "
               "must have flanges which exceed 9.5 mm in width. Likewise, "
               "flanged joints are not permitted for acetylene atmospheres, "
               "even though acetylene is nominally in sub-group IIC because "
               "of the carbon formation associated with acetylene explosions, "
               "and the possibility that this formation will prevent proper "
               "seating of the joint when remade. There is also a real "
               "possibility of ejection"))
    b.append(table(T1.HEAD104_EN, T1.ROWS104, T1.CAPTION104_EN))
    b.append(note(T1.NOTE104_EN))
    b.append(p("of incandescent carbon particles during an explosion and "
               "these may contain sufficient energy to cause ignition."))
    b.append(p("Similar, but less onerous, restrictions exist for sub-group "
               "IIB and IIA enclosures in that flanges of less than 9.5 mm are "
               "not permitted for IIB enclosures exceeding 100 cm³ in volume, "
               "and flanges of less than 12.5 cm³ are not permitted for those "
               "of more than 500 cm³ although in this case, unlike the "
               "situation in sub-group IIC, larger enclosures are permitted "
               "and there is no limit on size provided the flange width is "
               "not less than 12.5 mm."))
    b.append(note("<b>Source note on the printed unit.</b> The passage prints "
                  "'flanges of less than 12.5 cm³'; the intended unit in "
                  "context is evidently mm. The printed 'cm³' is kept in the "
                  "English text; the Vietnamese follows the intended meaning."))
    return "".join(b)
