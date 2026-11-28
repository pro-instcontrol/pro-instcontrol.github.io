# -*- coding: utf-8 -*-
"""Chapter 12, module C - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 305-311 (PDF pp. 326-332).

Covers the tail of 12.2.4 Insulation (whose sentence is interrupted by the
figure-only printed p. 306 and resumes on p. 307), 12.2.5 Windings and the
opening of 12.3 with 12.3.1 Terminal enclosures. Figures 12.7-12.9 and
Tables 12.2-12.4 sit at their printed positions. The chapter shell owns the
chapter h2, the printed references, the glossary, the source-quirk note and
the copyright.

Printed quirks are kept in the English text (the split sentence, the uneven
'mm' spacing, 'then' for 'than', the missing full stop after 'rms', the
superscript reference on HD 555, the printed source line and 'e.g.,' forms of
the tables, and the unpunctuated final note of Table 12.4) with bilingual
notes; the Vietnamese follows the intended meaning. This is an unofficial
study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, table, fig
import mcmillanfig12_b as FB
import mcmillanfig12_c as FC
import mcmillan_tbl12_1_4 as T1


def body_vi():
    b = []

    # Printed p.306 (PDF p.327) is figure-only; Fig. 12.7 continues at the
    # top of printed p.307. The first half of the 12.2.4 sentence was printed
    # on p.305 (module B); the paragraph below completes it.
    b.append(fig(7, FB.fig_f1207()))
    b.append(note("<b>Lưu ý về trang bản in chỉ có hình.</b> Trang in 306 chỉ "
                  "có Hình 12.7; câu bắt đầu ở trang in 305 ('...hoặc làm một "
                  "lớp') chỉ tiếp tục ở trang in 307 ('giữa các phần dẫn "
                  "điện...'). Hai nửa được giữ như một câu liên tục theo bản "
                  "in, không tách thành hai đoạn rời rạc."))
    b.append(note("<b>Lưu ý về cách ghi 'mm' trong Hình 12.7.</b> Bản in ghi "
                  "'1 mm' ở chú thích (1) nhưng '2.5mm' ở chú thích (2), và "
                  "trên các sơ đồ thì chỗ ghi '≥1mm', chỗ ghi '≥1 mm' và "
                  "'<1mm'. Sự không nhất quán về dấu cách này được giữ nguyên "
                  "theo bản in."))
    b.append(p("giữa các phần dẫn điện. Với lớp cách điện được dùng trên dây "
               "dẫn, không có yêu cầu đặc biệt nào đối với lớp cách điện bằng "
               "nhựa hoặc cao su dùng trên dây, hay các loại sơn véc-ni thường "
               "được dùng làm lớp cách điện trên dây quấn khi đã khô. Điều "
               "duy nhất được yêu cầu là chúng phải duy trì được chức năng ở "
               "nhiệt độ tối đa đạt được trong dịch vụ định mức (các điều kiện "
               "dịch vụ đã quy định, không bao gồm sự cố). Điều này có nghĩa "
               "là nhiệt độ hoạt động tối đa quy định của chúng cần cao hơn "
               "nhiệt độ tối đa mà chúng đạt được trong thiết bị. Tuy nhiên, "
               "các bộ phận cách điện, chẳng hạn như tấm đặc và khối ép, lại "
               "cần một hệ số an toàn vì chúng không chỉ cách điện mà còn có "
               "vai trò hỗ trợ chức năng. Chúng phải duy trì được khả năng "
               "làm việc ở nhiệt độ ít nhất cao hơn 20 °C so với nhiệt độ tối "
               "đa mà chúng đạt được khi sử dụng, với giới hạn nhiệt độ trên "
               "tối thiểu là 80°C. Việc lấy con số 80°C khá tùy tiện nhưng vẫn "
               "hợp lý vì nó trùng với nhiệt độ hoạt động tối đa của các vật "
               "liệu như PVC và, vì lý do đó, loại trừ các vật liệu như sáp, "
               "celluloid và shellac. Điều quan trọng cần lưu ý là"))

    # Printed p.308: Fig. 12.8 sits above Table 12.2.
    b.append(fig(8, FB.fig_f1208()))
    b.append(note("<b>Lưu ý về lỗi in 'then' trong định nghĩa b.</b> Bản in ghi "
                  "'b = Separation equal to or less then 2.5 mm', dùng 'then' "
                  "thay vì 'than' như mong đợi. Cách ghi này được giữ nguyên "
                  "trong bản tiếng Anh; bản tiếng Việt dịch theo nghĩa đúng "
                  "là 'bằng hoặc nhỏ hơn'."))
    b.append(table(T1.HEAD122_VI, T1.ROWS122_VI, T1.CAPTION122_VI))
    if T1.NOTE122_VI:
        b.append(note(T1.NOTE122_VI))
    b.append(note("<b>Lưu ý về dòng nguồn và chú thích của Bảng 12.2.</b> Bản "
                  "in ghi nguồn là '(from BS/EN 50019)' và chú thích là 'Note: "
                  "For lamps of over 250 V Table 12.1 applies'; dấu gạch chéo "
                  "trong tên tiêu chuẩn và dấu cách ở '250 V' được giữ nguyên, "
                  "kể cả việc bảng này nằm ngoài phạm vi dịch và được nhắc "
                  "đến bằng số hiệu."))

    # Printed p.309: Table 12.3, then the closing paragraph of 12.2.4.
    b.append(table(T1.HEAD123_VI, T1.ROWS123_VI, T1.CAPTION123_VI))
    if T1.NOTE123_VI:
        b.append(note(T1.NOTE123_VI))
    b.append(note("<b>Lưu ý về cách ghi trong Bảng 12.3.</b> Bản in dùng "
                  "'e.g.,' có dấu phẩy ở mọi ví dụ đặt trong ngoặc và dùng dấu "
                  "'+' ở '200–700+' cùng '700+'; các tên nhãn hàng như "
                  "makrolon, tufnol, maranyl và permaglass được viết thường. "
                  "Tất cả được giữ nguyên theo bản in."))
    b.append(p("nếu CTI của lớp cách điện rắn bị giảm do gia công hoặc các "
               "hoạt động tương tự, tình huống có thể được khắc phục bằng "
               "cách dùng lớp phủ sơn véc-ni, v.v. có CTI theo yêu cầu. Những "
               "vật liệu này không cần đáp ứng giới hạn tối thiểu 80°C vì "
               "chúng không thực hiện chức năng hỗ trợ."))

    b.append(h4("12.2.5 Dây quấn", "12.2.5 Windings"))
    b.append(p("Dây quấn được xem là một nguồn nguy hiểm đặc biệt và có các "
               "yêu cầu bổ sung áp dụng cho chúng. Dây chế tạo nên chúng, nếu "
               "được tráng men, cần tuân thủ HD 555¹¹, một quy định kỹ thuật "
               "quốc tế về dây quấn tráng men. Chúng nên tuân thủ cấp 2 của "
               "Tiêu chuẩn đó. Chúng cũng có thể được chấp nhận nếu chỉ tuân "
               "thủ cấp 1 nhưng, bổ sung thêm, có điện áp đánh thủng phù hợp "
               "với cấp 2 và đáp ứng yêu cầu an toàn tăng cường khi thử "
               "nghiệm đánh thủng. Chi tiết của các yêu cầu bổ sung đối với "
               "dây cấp 1 được nêu trong BS/EN 50019. Dây không tuân thủ "
               "HD 555 có thể được cách điện bằng nhựa hoặc lớp cách điện "
               "tương tự, hoặc có thể được phủ sơn cách điện. Tuy nhiên, "
               "trong mọi trường hợp đó, lớp cách điện phải đủ cho điện áp "
               "liên quan và phải có hai lớp cách điện hoàn chỉnh."))
    b.append(note("<b>Lưu ý về ký hiệu chú thích mũ sau HD 555.</b> Bản in viết "
                  "'HD 555¹¹' với số 11 ở dạng mũ; đây là số tham chiếu, không "
                  "phải một phần của tên tiêu chuẩn, vì cùng đoạn sau đó chỉ "
                  "ghi 'HD 555'. Ký hiệu mũ được giữ nguyên theo bản in."))
    b.append(p("Để tránh nguy cơ dây bị dịch chuyển gây hỏng cách điện, dây "
               "quấn thường được yêu cầu phải được ngâm tẩm hoàn toàn bằng "
               "một phương pháp loại trừ việc hình thành các khoảng rỗng bên "
               "trong cụm. Vì lý do đó, việc chỉ phủ vật liệu ngâm tẩm thường "
               "không đủ và có thể cần một phương pháp như ngâm tẩm chân "
               "không. Khi dung môi được dùng để làm vật liệu ngâm tẩm lỏng "
               "ra, thao tác ngâm tẩm cần được thực hiện ít nhất hai lần, lần "
               "thứ hai để đảm bảo các khoảng rỗng tạo ra do dung môi bay hơi "
               "sau lần xử lý đầu tiên được lấp đầy. Có thể thay đổi yêu cầu "
               "này trong trường hợp dây quấn dự định lắp vào các rãnh của máy "
               "hoặc các vị trí tương tự và không thể tiếp cận sau khi lắp. "
               "Trong những trường hợp này, việc ngâm tẩm hoặc"))
    # Printed p.310: the sentence continues across the page break.
    b.append(p("quy trình cách điện và củng cố thay thế phù hợp có thể được "
               "thực hiện trước khi lắp đối với dây quấn làm việc trên "
               "1100 V rms. Dưới mức này, người ta cho rằng không có khả năng "
               "phát sinh vấn đề này."))
    b.append(note("<b>Lưu ý về dấu chấm bị thiếu trong bản in.</b> Bản in không "
                  "có dấu chấm giữa 'rms' và 'Below' trong cụm '...windings "
                  "operating above 1100 V rms Below this figure...'. Cách ghi "
                  "này được giữ nguyên trong bản tiếng Anh; bản tiếng Việt "
                  "dùng dấu chấm theo ý định."))
    b.append(p("Không có dây nào có đường kính dẫn nhỏ hơn 0,25 mm được xem là "
               "đủ bền chắc để tránh đứt gãy, và những dây như vậy không được "
               "phép dùng cho dây quấn an toàn tăng cường. Điều này sẽ loại "
               "trừ dây quấn của nhiệt kế điện trở thường được dùng để ngăn "
               "dây quấn bị quá nhiệt, và đó không phải là ý định. Vì vậy, "
               "nhiệt kế điện trở được miễn yêu cầu tuân thủ giới hạn kích "
               "thước này. Tuy nhiên, cần lưu ý rằng hiệu năng của các thiết "
               "bị đó bị ảnh hưởng bởi vị trí gần của chúng với dây quấn được "
               "bảo vệ và chúng cần được ngâm tẩm hiệu quả cùng với dây "
               "quấn. Điều này đặc biệt đúng trong trường hợp máy quay, nơi "
               "chúng cần nằm trong rãnh cùng với dây quấn để đảm bảo hoạt "
               "động hiệu quả."))
    b.append(p("Mặc dù cần tuân thủ yêu cầu cơ bản (tức là không bộ phận nào "
               "của thiết bị mà khí quyển nổ có thể tiếp cận được vượt quá "
               "nhiệt độ giới hạn của cấp nhiệt độ của thiết bị, và không bộ "
               "phận nào của thiết bị vượt quá nhiệt độ tối đa mà vật liệu và "
               "cụm lắp ráp của nó được thiết kế, ngay cả khi khí quyển nổ "
               "không tiếp cận được), vẫn có các giới hạn nhiệt độ bổ sung mà "
               "dây quấn phải tuân thủ để đảm bảo độ tin cậy và được nêu "
               "trong Bảng 12.4. Những giới hạn này cần được đáp ứng ngay cả "
               "khi xảy ra hư hỏng vật lý (ví dụ, rô-to bị khóa trong trường "
               "hợp máy quay), và nếu bản thân dây quấn không thể đáp ứng các "
               "yêu cầu này thì các thiết bị cảm biến nhiệt độ đã được nhắc "
               "đến ở trên phải, cùng với các thiết bị liên quan, đảm bảo "
               "hạn chế nhiệt độ hoặc cách ly điện để không vượt quá các giới "
               "hạn."))

    # Table 12.4 closes printed p.310, after the windings paragraphs.
    b.append(table(T1.HEAD124_VI, T1.ROWS124_VI, T1.CAPTION124_VI))
    if T1.NOTE124_VI:
        b.append(note(T1.NOTE124_VI))
    b.append(note("<b>Lưu ý về Chú thích 2 của Bảng 12.4.</b> Đây là lời chú "
                  "giải mang tính biên tập của bản gốc những năm 1980, nói "
                  "rằng các số liệu được đưa vào tạm thời cho đến khi có số "
                  "liệu trong BS 2757; được giữ nguyên theo bản in."))
    b.append(note("<b>Lưu ý về Chú thích 3 và ký hiệu tₑ.</b> Chú thích 3 kết "
                  "thúc không có dấu chấm trong bản in, và ký hiệu 'tₑ' trong "
                  "dòng 'Rotating machines (temp at tₑ time)' không được giải "
                  "thích trong phạm vi này. Cả hai được giữ nguyên theo bản "
                  "in."))

    # Printed p.311: Fig. 12.9, then the opening of 12.3 and 12.3.1.
    b.append(fig(9, FC.fig_f1209()))
    b.append(note("<b>Lưu ý về công thức trong Hình 12.9.</b> Bản in viết "
                  "'Clearance = D + d,' có dấu phẩy cuối, rồi 'Creepage "
                  "distance = D + d' với phần giải thích đặt trong nhiều cặp "
                  "ngoặc lồng nhau. Cách đặt dấu được giữ nguyên theo bản in."))
    b.append(h3("12.3 Yêu cầu bổ sung đối với các loại thiết bị cụ thể",
                "12.3 Additional requirements for specific types of apparatus"))
    b.append(p("Ngoài các yêu cầu cơ bản đã nêu đối với an toàn tăng cường, "
               "còn có những thay đổi cụ thể cần thiết trong trường hợp các "
               "loại thiết bị đặc biệt như vỏ đầu nối, đèn chiếu sáng nguồn "
               "chính, đèn đội đầu, dụng cụ đo bao gồm máy biến áp, ắc quy "
               "thứ cấp, thiết bị gia nhiệt điện và máy quay. Các loại thiết "
               "bị cụ thể khác có thể cần các yêu cầu kết cấu bổ sung riêng "
               "nhưng không được quy định chi tiết. Tiêu chuẩn (BS/EN 50019) "
               "yêu cầu rằng, khi phù hợp, các yêu cầu kết cấu nêu sau đây "
               "nên được áp dụng cho các loại thiết bị khác ngoài các yêu "
               "cầu kết cấu chung cần thiết cho an toàn tăng cường, khi phù "
               "hợp."))
    b.append(h4("12.3.1 Vỏ đầu nối", "12.3.1 Terminal enclosures"))
    b.append(p("Thường thì người ta cho phép một mức độ linh hoạt nhất định "
               "đối với hộp đầu nối an toàn tăng cường về số lượng và loại "
               "đầu nối được lắp. Điều này có thể gây ra vấn đề vì kết nối của "
               "một dây với một đầu nối có điện trở hữu hạn, cũng như lượng "
               "dây bên trong vỏ bọc. Dây bên ngoài vỏ bọc nói chung có thể "
               "bỏ qua do sự làm mát tăng cường thường thấy trong trường hợp "
               "này, nhưng dây bên trong thì không. Công suất sẽ được tiêu "
               "thụ ở cả dẫn bên trong và đầu nối, dẫn đến tăng nhiệt độ và, "
               "khi có nhiều đầu nối được lắp gần nhau, các đầu nối kề bên "
               "cũng có ảnh hưởng. Ngoài ra, nhiệt độ môi trường trong vỏ bọc "
               "cũng sẽ bị ảnh hưởng bởi"))
    b.append(note("<b>Lưu ý về ranh giới câu cuối.</b> Câu cuối cùng trong "
                  "phạm vi này kết thúc bằng cụm 'bởi' vì tiếp tục sang trang "
                  "in tiếp theo (nằm ngoài phạm vi của mô-đun này). Cách kết "
                  "thúc này được giữ nguyên theo bản in."))
    return "".join(b)


def body_en():
    b = []

    # Printed p.306 (PDF p.327) is figure-only; Fig. 12.7 continues at the
    # top of printed p.307. The first half of the 12.2.4 sentence was printed
    # on p.305 (module B); the paragraph below completes it.
    b.append(fig(7, FB.fig_f1207()))
    b.append(note("<b>Note on the figure-only printed page.</b> Printed p. 306 "
                  "carries only Fig. 12.7; the sentence begun on printed p. 305 "
                  "('...or as a layer') resumes only on printed p. 307 "
                  "('between conducting parts...'). The two halves are a single "
                  "continuous sentence in the print and are kept as such, not "
                  "split into two detached fragments."))
    b.append(note("<b>Note on the 'mm' spacing in Fig. 12.7.</b> The print has "
                  "'1 mm' in Note (1) but '2.5mm' in Note (2), and the diagram "
                  "dimensions read '≥1mm', '≥1 mm' and '<1mm' in different "
                  "places. The inconsistent spacing is retained as printed."))
    b.append(p("between conducting parts. With insulation used on conductors "
               "there is no special requirement for either the plastic or "
               "elastomeric insulation used on wires or varnishes which are "
               "typically used as insulation on winding wires when cured. All "
               "that is required is that they remain functional at the maximum "
               "temperature achieved in rated service (the service conditions "
               "specified which do not include faults). This means that their "
               "specified maximum operating temperature needs to be in excess "
               "of the maximum temperature which they achieve in the "
               "apparatus. Insulating parts, such as solid sheets and moulded "
               "blocks do, however, need a safety factor as they not only "
               "insulate but have a functional support role to play. They must "
               "remain viable at a temperature of at least 20 °C higher than "
               "the maximum temperature which they achieve in service, with a "
               "minimum upper temperature limit of 80°C. The derivation of the "
               "80°C is fairly arbitrary but nonetheless reasonable as it "
               "coincides with the maximum operating temperature of such "
               "things as PVC and, because of this, excludes such materials as "
               "waxes, celluloid and shellac. It is important to note that"))

    # Printed p.308: Fig. 12.8 sits above Table 12.2.
    b.append(fig(8, FB.fig_f1208()))
    b.append(note("<b>Note on 'then' in definition b.</b> The print reads "
                  "'b = Separation equal to or less then 2.5 mm', using 'then' "
                  "where 'than' would be expected. The printed wording is "
                  "retained in English; the Vietnamese follows the intended "
                  "meaning of 'equal to or less than'."))
    b.append(table(T1.HEAD122_EN, T1.ROWS122, T1.CAPTION122_EN))
    if T1.NOTE122_EN:
        b.append(note(T1.NOTE122_EN))
    b.append(note("<b>Note on the source line and note of Table 12.2.</b> The "
                  "print gives the source as '(from BS/EN 50019)' and the note "
                  "as 'Note: For lamps of over 250 V Table 12.1 applies'; the "
                  "slash in the standard designation and the space in '250 V' "
                  "are kept as printed, including the cross-reference to a "
                  "table outside this span."))

    # Printed p.309: Table 12.3, then the closing paragraph of 12.2.4.
    b.append(table(T1.HEAD123_EN, T1.ROWS123, T1.CAPTION123_EN))
    if T1.NOTE123_EN:
        b.append(note(T1.NOTE123_EN))
    b.append(note("<b>Note on the wording of Table 12.3.</b> The print uses "
                  "'e.g.,' with a comma in every bracketed example and uses a "
                  "plus suffix in '200–700+' and '700+'; brand names such as "
                  "makrolon, tufnol, maranyl and permaglass are lower-case. "
                  "All are kept as printed."))
    b.append(p("if the CTI of solid insulation is reduced by machining or "
               "similar activities, the situation may be recovered by using "
               "coatings of varnishes, etc. with the required CTI. Such "
               "materials should not need to satisfy the 80°C minimum limit as "
               "they do not carry out a supporting function."))

    b.append(h4("12.2.5 Windings", "12.2.5 Windings"))
    b.append(p("Windings are recognized as a particular source of danger and "
               "have additional requirements applied. The wires of which they "
               "are made, if enamelled, need to comply with HD 555¹¹ which is "
               "an international specification for enamelled winding wires. "
               "They should comply with grade 2 of that Standard. They may "
               "also be acceptable if they only comply with grade 1 but, in "
               "addition, have breakdown voltages appropriate to grade 2 and "
               "satisfy an enhanced security requirement when breakdown "
               "tested. The detail of the additional requirements for grade 1 "
               "wires are given in BS/EN 50019. Wires not complying with "
               "HD 555 may be insulated with plastics or similar insulation "
               "or may be covered with insulating varnish. In all such cases, "
               "however, the insulation must be adequate for the voltage "
               "involved and there must be two complete layers of such "
               "insulation."))
    b.append(note("<b>Note on the superscript reference after HD 555.</b> The "
                  "print writes 'HD 555¹¹' with the 11 raised; it is a "
                  "reference numeral, not part of the standard designation, "
                  "since the same paragraph later writes simply 'HD 555'. The "
                  "superscript is retained as printed."))
    b.append(p("To avoid the risk of wire movement causing insulation failure, "
               "windings are normally required to be fully impregnated by a "
               "means which precludes the formation of voids within the "
               "assembly. For this reason, coating with impregnation material "
               "is not normally sufficient and a method such as vacuum "
               "impregnation is likely to be necessary. Where solvents are "
               "used to make the impregnation material fluid, the "
               "impregnation operation needs to be carried out at least twice, "
               "the second time to ensure that any voids created by the later "
               "evaporation of solvent after the first process, are filled. "
               "Variations to this requirement are possible in the case of "
               "windings which are intended for fitting into the slots of "
               "machines or similar locations and are not accessible after "
               "fitting. In these cases their impregnation, or suitable"))
    # Printed p.310: the sentence continues across the page break.
    b.append(p("alternative insulation and consolidation procedure, may be "
               "carried out before fitting for windings operating above "
               "1100 V rms Below this figure it is not considered likely that "
               "this problem will arise."))
    b.append(note("<b>Note on the missing full stop in the print.</b> The print "
                  "has no full stop between 'rms' and 'Below' in '...windings "
                  "operating above 1100 V rms Below this figure...'. The "
                  "wording is kept as printed; the Vietnamese supplies the "
                  "full stop of the intended sentence."))
    b.append(p("No wires of conductor diameters of less than 0.25mm are "
               "considered sufficiently robust to be secure against breakage "
               "and such wires are not permitted for increased safety "
               "windings. This would exclude the windings of resistance "
               "thermometers which are often used to prevent the winding from "
               "overheating and this is not the intention. Therefore, "
               "resistance thermometers are absolved from the necessity of "
               "satisfying the size limitation. It should be noted, however, "
               "that the performance of such devices is affected by their "
               "proximity to the winding being protected and that they need "
               "to be effectively impregnated with the windings. This is "
               "especially so in the case of rotating machines where they "
               "need to be in the slots with the windings to ensure efficient "
               "operation."))
    b.append(p("While needing to comply with the basic requirement (i.e., that "
               "no part of the apparatus to which an explosive atmosphere has "
               "access may exceed the limiting temperature of the temperature "
               "class for the apparatus, and no part of the apparatus may "
               "exceed the maximum temperature for which its material and "
               "assembly is designed, even if the explosive atmosphere does "
               "not have access) there are further limits of temperature with "
               "which windings must comply to ensure reliability and these "
               "are given in Table 12.4. These need to be satisfied even when "
               "physical faults occur (e.g., a locked rotor in the case of a "
               "rotating machine), and if the winding alone cannot satisfy "
               "these requirements then the temperature sensing devices "
               "already referred to must, together with associated devices, "
               "ensure temperature limitation or electrical isolation so that "
               "the limits are not exceeded."))

    # Table 12.4 closes printed p.310, after the windings paragraphs.
    b.append(table(T1.HEAD124_EN, T1.ROWS124, T1.CAPTION124_EN))
    if T1.NOTE124_EN:
        b.append(note(T1.NOTE124_EN))
    b.append(note("<b>Note on Note 2 of Table 12.4.</b> This is an editorial "
                  "note from the original 1980s text, saying that the figures "
                  "are included on a temporary basis pending their inclusion "
                  "in BS 2757. It is kept as printed."))
    b.append(note("<b>Note on Note 3 and the tₑ subscript.</b> Note 3 ends "
                  "without a full stop in the print, and the 'tₑ' in the row "
                  "'Rotating machines (temp at tₑ time)' is not defined within "
                  "this span. Both are kept as printed."))

    # Printed p.311: Fig. 12.9, then the opening of 12.3 and 12.3.1.
    b.append(fig(9, FC.fig_f1209()))
    b.append(note("<b>Note on the formulas in Fig. 12.9.</b> The print writes "
                  "'Clearance = D + d,' with a trailing comma, then 'Creepage "
                  "distance = D + d' followed by an explanation in nested "
                  "brackets. The punctuation is kept as printed."))
    b.append(h3("12.3 Additional requirements for specific types of apparatus",
                "12.3 Additional requirements for specific types of apparatus"))
    b.append(p("In addition to the basic requirements for increased safety "
               "already identified, there are specific variations necessary "
               "in the case of particular types of apparatus such as terminal "
               "enclosures, mains luminaires, cap lamps, measuring instruments "
               "including transformers, secondary batteries, electric heating "
               "apparatus, and rotating machines. Other specific types of "
               "apparatus may require additional specific constructional "
               "requirements but these are not specified in detail. The "
               "Standard (BS/EN 50019) requires that, where appropriate, the "
               "constructional requirements which follow should be applied to "
               "other types of apparatus in addition to the general "
               "constructional requirements necessary for increased safety as "
               "appropriate."))
    b.append(h4("12.3.1 Terminal enclosures", "12.3.1 Terminal enclosures"))
    b.append(p("It is normal to give a degree of flexibility to increased "
               "safety terminal boxes as to the number and types of terminals "
               "fitted. This can cause problems in that the connection of a "
               "wire to a terminal has a finite resistance, as does the amount "
               "of wire inside the enclosure. Wiring outside the enclosure may "
               "generally be ignored because of the enhanced cooling which is "
               "normally apparent in this case, but that within the enclosure "
               "cannot. Power will be dissipated in both internal conductor "
               "and terminal which will give rise to temperature elevation "
               "and, where several terminals are fitted in close proximity, "
               "adjacent terminals also have an effect. In addition, the "
               "ambient temperature in the enclosure will also be affected by "
               "the"))
    b.append(note("<b>Note on the final sentence boundary.</b> The last "
                  "sentence in this span ends with 'by the' because it "
                  "continues onto the next printed page (outside this "
                  "module's range). The incomplete ending is kept as printed."))
    return "".join(b)
