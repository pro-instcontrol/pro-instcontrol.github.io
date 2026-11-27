# -*- coding: utf-8 -*-
"""Chapter 10, module E - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 252-256 (PDF pp. 273-277).

Covers the tail of 10.2.3 Joints for shafts and rotating machines,
10.2.4 Bearing greasing arrangements, 10.2.5 Tests for flameproof
joints (recovered from the image-only printed p.254), 10.3 Construction
of flameproof enclosures, entry facilities, fasteners and component
parts, and the opening of 10.3.1 Enclosure construction (printed p.256).

Figures 10.13-10.15 and Tables 10.12-10.13 are inserted at their printed
positions. Printed quirks are kept in the English text (the 'k' reference
to Fig. 10.14, the '<1.4' safety factor, the '500 cm3' unit slip, and the
'ISO 1851' footnote marker), with bilingual notes; the Vietnamese text
follows the intended meaning. The chapter shell owns the chapter h2,
references and end matter.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, table, fig
import mcmillanfig10b as FB
import mcmillan_tbl10_11_15 as T3


def body_vi():
    b = []

    # Tail of 10.2.3 (printed p.252; the heading itself belongs to module D).
    b.append(p("Cách tiếp cận này luôn cần thiết đối với các máy điện quay. "
               "Trong trường hợp ổ trục dạng bạc, các hạn chế tương tự áp dụng "
               "cho mối nối hình trụ và kích thước mối nối phải đáp ứng các "
               "yêu cầu của Bảng 10.10. Chiều dài mối nối phải ít nhất bằng "
               "đường kính trục nếu đường kính này dưới 25 mm. Tuy nhiên, "
               "không nhất thiết phải chế tạo mối nối dài hơn 25 mm. Khe hở "
               "xuyên tâm nhỏ nhất trong mối nối phải ít nhất là 0,05 mm "
               "(xem 'k' trong Hình 10.14) và các mối nối chỉ được sử dụng "
               "trong vỏ bọc dự định dùng cho nhóm con IIA và IIB. Trong "
               "trường hợp mối nối mê cung (xem Hình 10.12), cũng cần có khe "
               "hở xuyên tâm nhỏ nhất như vậy. Yêu cầu về khe hở tối đa của "
               "mối nối trong trường hợp sau có thể được miễn bỏ, như đối với "
               "thanh truyền, nếu có thể chứng minh bằng thử nghiệm là mối "
               "nối chống cháy, nhưng tất cả các yêu cầu khác vẫn như đối với "
               "mối nối hình trụ."))
    b.append(note("<b>Lưu ý về trích dẫn hình.</b> Bản in ghi \"(xem 'k' trong "
                  "Hình 10.14)\", nhưng k lại được vẽ trong Hình 10.13; Hình "
                  "10.14 là hình minh họa mối nối trục nổi. Giữ nguyên trích "
                  "dẫn theo bản gốc (có vẻ bị đảo trong nguyên bản)."))

    # Printed p.253: Fig. 10.13 stands at the head of the page.
    b.append(fig(13, FB.fig_f1013()))
    b.append(p("Vì tốc độ quay có thể gây mòn nhanh, trong trường hợp ổ trục "
               "dạng bạc cũng cần đảm bảo rằng một phần của mối nối hình trụ "
               "hoặc mối nối mê cung là vật liệu không tạo tia lửa (ví dụ, "
               "đồng thau chì) để ngăn phát sinh tia lửa khi ổ trục hỏng; và "
               "khi khe hở xuyên tâm nhỏ nhất của mối nối (0,05 mm) nhỏ hơn "
               "khe hở giữa stato và rôto khi máy chạy, thì phần mối nối đó "
               "phải dày hơn khe hở chạy máy đó để tránh phát sinh tia lửa "
               "tại mối nối."))
    b.append(p("Đối với ổ lăn, các quy tắc tương tự được áp dụng, ngoại trừ "
               "hạn chế chỉ dùng cho nhóm con IIA và IIB — ở đây máy có ổ lăn "
               "được chấp nhận — và yêu cầu phải có một phần của mối nối làm "
               "bằng vật liệu không tạo tia lửa cũng được miễn bỏ. Tuy nhiên, "
               "khe hở xuyên tâm tối đa của mối nối được giảm và phải phù hợp "
               "với Bảng 10.12."))
    b.append(p("Trong mọi trường hợp, trục quay có thể nằm trong một mối nối "
               "nổi kết hợp cả mối nối mặt bích phẳng và mối nối hình trụ "
               "(xem Hình 10.14). Không một máy quay nào có mối nối như vậy "
               "được phép dùng trong nhóm con IIC."))

    b.append(h4("10.2.4 Sắp xếp bôi mỡ cho ổ trục",
                "10.2.4 Bearing greasing arrangements"))
    b.append(p("Khi các rãnh bôi mỡ được khắc trên trục để giữ mỡ quanh ổ "
               "trục, các rãnh này không được can thiệp vào mối nối. Hình "
               "10.15 cho thấy một cách sử dụng chấp nhận được."))

    # Printed p.254 exists only in the page image (OCR text layer blank).
    b.append(note("<b>Lưu ý về nguồn nội dung trang 254.</b> Hình 10.14, Bảng "
                  "10.12 và toàn bộ mục 10.2.5 chỉ có trong hình ảnh trang "
                  "in; lớp văn bản OCR của trang này trống. Nội dung được "
                  "dịch từ trang in."))
    b.append(fig(14, FB.fig_f1014()))
    b.append(table(T3.HEAD1012_VI, T3.ROWS1012, T3.CAPTION1012_VI))
    b.append(note(T3.NOTE1012_VI))

    b.append(h4("10.2.5 Thử nghiệm mối nối chống cháy",
                "10.2.5 Tests for flameproof joints"))
    b.append(p("Thử nghiệm đường dẫn ngọn lửa về sự truyền ngọn lửa mang tính "
               "động, vì nó bao gồm việc nạp vào vỏ bọc một khí quyển nổ quy "
               "định và bao quanh vỏ bọc bằng chính khí quyển đó. Khí quyển "
               "nổ bên trong sau đó được đốt cháy và phải chứng minh được sự "
               "không truyền ngọn lửa trong một số thử nghiệm quy định trong "
               "BS/EN 50018."))

    # Printed p.255: Fig. 10.15, then Table 10.13, then body text.
    b.append(fig(15, FB.fig_f1015()))
    b.append(table(T3.HEAD1013_VI, T3.ROWS1013, T3.CAPTION1013_VI))
    b.append(note(T3.NOTE1013_VI))
    b.append(p("Trong Tiêu chuẩn này, thử nghiệm thường được tiến hành với "
               "tất cả các đường dẫn ngọn lửa, trừ mối nối ren và mối nối xi "
               "măng, được đặt ở giá trị ít nhất bằng 90 phần trăm giá trị "
               "thiết kế tối đa, có tính đến dung sai. Các đường dẫn ngọn lửa "
               "ren được xử lý như quy định chi tiết trong Bảng 10.13. Khí "
               "quyển nổ dùng để nạp và bao quanh vỏ bọc sau đó được chọn để "
               "cho"))

    # Printed p.256.
    b.append(p("hệ số an toàn < 1,4 đối với vỏ bọc dùng cho nhóm con IIA và "
               "IIB (hệ số an toàn thực tế trong từng trường hợp được xác định "
               "trong BS/EN 50018), và một số thử nghiệm được tiến hành với "
               "các điểm đốt cháy bên trong được chọn sao cho tạo ra tình "
               "huống xấu nhất có thể, có tính đến nội dung bên trong vỏ bọc. "
               "Ngoài ra, đối với nhóm con IIA và IIB, có thể dùng hỗn hợp "
               "nguy hiểm hơn với khe hở nhỏ hơn 0,9 lần khe hở thiết kế tối "
               "đa (chi tiết lại được nêu trong Tiêu chuẩn), hoặc bằng cách "
               "tăng khe hở theo quy định và dùng khí quyển thử nghiệm nổ ít "
               "nguy hiểm hơn."))
    b.append(note("<b>Lưu ý về hệ số an toàn.</b> Bản in ghi hệ số an toàn "
                  "< 1,4; lớp văn bản OCR đọc nhầm thành 11,4. Bản tiếng Anh "
                  "giữ giá trị in là <1,4."))
    b.append(p("Tình huống đối với nhóm con IIC phức tạp hơn, vì cách duy nhất "
               "để tăng độ nhạy của thử nghiệm là làm giàu oxy khí quyển nổ "
               "thử nghiệm; thay vì làm như vậy, các thử nghiệm được tiến "
               "hành với hỗn hợp hydro hoặc axetylen và không khí, với đường "
               "dẫn ngọn lửa được mở rộng vượt quá khe hở thiết kế tối đa, "
               "hoặc với khí quyển nổ thử nghiệm có áp suất cao hơn áp suất "
               "khí quyển. Các yêu cầu thử nghiệm trong BS/EN 50018 (ấn bản "
               "thứ hai của EN 50018) khác biệt đáng kể so với BS 5501, Phần "
               "5 và nghiêm ngặt hơn nhiều đối với nhóm con IIA và IIB. Vì "
               "vậy, không nên cho rằng vỏ bọc đã đáp ứng yêu cầu của ấn bản "
               "thứ nhất thì nhất thiết sẽ đáp ứng được yêu cầu của ấn bản "
               "thứ hai. Đây lại là lý do chính đáng để khuyến nghị chọn "
               "thiết bị theo BS/EN 50018 trong tương lai."))

    b.append(h3("10.3 Kết cấu vỏ chống cháy, phương tiện đấu nối đầu vào, "
                "chi tiết bắt chặt và các bộ phận cấu thành",
                "10.3 Construction of flameproof enclosures, entry facilities, "
                "fasteners and component parts"))
    b.append(h4("10.3.1 Kết cấu vỏ bọc", "10.3.1 Enclosure construction"))
    b.append(p("Vỏ chống cháy có thể được chế tạo bằng kim loại hoặc bằng vật "
               "liệu phi kim thích hợp (thường là nhựa). Vỏ hoàn toàn phi kim "
               "bị giới hạn thể tích đến 3000 cm³, nhưng khi vỏ về cơ bản là "
               "kim loại và các phần phi kim chỉ tạo thành một số bộ phận của "
               "vỏ thì giới hạn thể tích này không áp dụng, miễn là không bề "
               "mặt phi kim nào vượt quá 500 cm³. Hạn chế 500 cm² này không "
               "áp dụng cho các bộ phận truyền sáng của đèn chiếu sáng, theo "
               "đó ngoại lệ có thể có các phần phi kim có diện tích bề mặt "
               "đến 8000 cm²."))
    b.append(note("<b>Lưu ý về đơn vị.</b> Bản in ghi \"no non-metallic surface "
                  "exceeds 500 cm³. This 500 cm² restriction...\"; cm³ ở đây "
                  "gần như chắc chắn là lỗi in của cm², vì trang sau ghi lại "
                  "\"500 cm²\". Giữ nguyên cả hai cách ghi như bản in."))
    b.append(p("Khi vỏ bọc bằng kim loại được chế tạo bằng gang, cần lưu ý đến "
               "việc một số loại gang rất giòn và, để tránh dùng các loại đó, "
               "gang được yêu cầu phải có chất lượng thấp nhất là 150 như "
               "quy định trong ISO 1851⁴. Đồng thau và nhôm cũng nằm trong số "
               "vật liệu được chấp nhận và kết cấu có thể là đúc hoặc chế tạo "
               "bằng cách hàn các loại chi tiết bắt chặt tương tự của vỏ bọc "
               "lại với nhau. Khi vỏ bọc được chế tạo, luôn yêu cầu thử nghiệm "
               "áp suất định kỳ — được miễn đối với vỏ bọc đã thử nghiệm kiểu "
               "ở áp suất bằng bốn lần áp suất phát sinh trong vụ nổ bên trong "
               "của hỗn hợp khí/không khí đặc trưng của nhóm con (áp suất "
               "tham chiếu) — để đảm bảo chất lượng chế tạo, vì mức độ tin cậy "
               "vào khả năng lặp lại của chất lượng hàn không cao bằng đối với "
               "việc đúc."))
    return "".join(b)


def body_en():
    b = []

    # Tail of 10.2.3 (printed p.252; the heading itself belongs to module D).
    b.append(p("This approach is always necessary for rotating electrical "
               "machines. With sleeve bearings, the same restrictions apply "
               "in the case of cylindrical joints and the joint dimensions "
               "must satisfy the requirements of Table 10.10. The joint length "
               "must be at least equal to the shaft diameter if that is below "
               "25 mm. It is not, however, necessary to make the joint longer "
               "than 25 mm. The minimum radial clearance in the joint must be "
               "at least 0.05 mm (see 'k' in Fig. 10.14) and the joints are "
               "usable only in enclosures intended for sub-group IIA and IIB. "
               "In the case of labyrinth joints (see Fig. 10.12) the same "
               "minimum radial clearance is necessary. Joint maximum gap "
               "requirements may, in this latter case, be waived as is the "
               "case for operating rods if the joint can be shown by test to "
               "be flameproof, but all other requirements are as for "
               "cylindrical joints."))
    b.append(note("<b>Note on figure reference.</b> The print reads \"(see 'k' "
                  "in Fig. 10.14)\", but k is drawn in Fig. 10.13; Fig. 10.14 "
                  "is the floating-shaft-joint figure. Figure reference as "
                  "printed (apparently swapped in the original)."))

    # Printed p.253: Fig. 10.13 stands at the head of the page.
    b.append(fig(13, FB.fig_f1013()))
    b.append(p("As, because of the speed of rotation, wear can be rapid it is "
               "also necessary in the case of sleeve bearings to ensure that "
               "one part of a cylindrical or labyrinth joint is non-sparking "
               "(e.g., leaded brass) to prevent sparking on bearing failure "
               "and, where the minimum radial clearance of the joint (0.05mm) "
               "is smaller than the running stator rotor clearance of the "
               "machine, this joint part needs to be thicker than that running "
               "clearance to avoid joint sparking."))
    b.append(p("In the case of rolling element bearings, the same rules apply "
               "with the exception of the restriction to sub-group IIA and "
               "IIB, where machines with rolling element bearings are "
               "acceptable and the need to have one part of the joint "
               "non-sparking is also waived. The maximum radial joint gap is, "
               "however, reduced and must comply with Table 10.12."))
    b.append(p("In all cases the rotating shaft may be in a floating joint "
               "using both a flat flanged joint and a cylindrical joint (see "
               "Fig. 10.14). In no case is a rotating machine with such a joint "
               "permissible in sub-group IIC."))

    b.append(h4("10.2.4 Bearing greasing arrangements",
                "10.2.4 Bearing greasing arrangements"))
    b.append(p("Where grease grooves are used in shafts to retain grease "
               "around the bearing, these should not interfere with the joint. "
               "Figure 10.15 shows an acceptable way of their use."))

    # Printed p.254 exists only in the page image (OCR text layer blank).
    b.append(note("<b>Note on the source of printed page 254.</b> Fig. 10.14, "
                  "Table 10.12 and all of Section 10.2.5 occur only in the "
                  "page image; the OCR text layer for this page is blank. The "
                  "translation follows the printed page."))
    b.append(fig(14, FB.fig_f1014()))
    b.append(table(T3.HEAD1012_EN, T3.ROWS1012, T3.CAPTION1012_EN))
    b.append(note(T3.NOTE1012_EN))

    b.append(h4("10.2.5 Tests for flameproof joints",
                "10.2.5 Tests for flameproof joints"))
    b.append(p("Testing of flamepaths for flame transmission is dynamic in "
               "that it involves filling the enclosure with a specified "
               "explosive atmosphere and surrounding it with the same "
               "atmosphere. The internal explosive atmosphere is then ignited "
               "and non-transmission has to be proved in a number of tests "
               "prescribed in BS/EN 50018."))

    # Printed p.255: Fig. 10.15, then Table 10.13, then body text.
    b.append(fig(15, FB.fig_f1015()))
    b.append(table(T3.HEAD1013_EN, T3.ROWS1013, T3.CAPTION1013_EN))
    b.append(note(T3.NOTE1013_EN))
    b.append(p("In this Standard the test is normally carried out with all "
               "flamepaths, excluding threaded and cemented joints, set at a "
               "figure which is at least 90 per cent of the maximum design "
               "figure, taking account of tolerances. Threaded flamepaths are "
               "dealt with as detailed in Table 10.13. The explosive "
               "atmosphere used to fill and surround the enclosure is then "
               "chosen to give"))

    # Printed p.256.
    b.append(p("a safety factor of <1.4 for enclosures for sub-group IIA and "
               "IIB (the actual safety factor in each case is defined in "
               "BS/EN 50018) and several tests are carried out with internal "
               "ignition points chosen to give the worst possible situation "
               "taking account of the contents of the enclosure. Alternatively, "
               "for sub-group IIA and IIB more onerous mixtures may be used "
               "with gaps which are at less than 0.9 times the maximum design "
               "gap (details again being given in the Standard), or by "
               "specified enlargement of the gap and the use of less onerous "
               "test explosive atmospheres."))
    b.append(note("<b>Note on safety factor.</b> The print reads a safety "
                  "factor of <1.4; the OCR text layer reads 11.4, which is "
                  "wrong. The printed value <1.4 is retained."))
    b.append(p("The situation in respect of sub-group IIC is more complex in "
               "that the only way to increase test sensitivity would be to "
               "enrich the test explosive atmosphere with oxygen and, rather "
               "than do this, the tests are carried out with hydrogen or "
               "acetylene air mixtures with the flamepaths enlarged to greater "
               "than the maximum design gaps or with the test explosive "
               "atmosphere at greater than atmospheric pressure. The test "
               "requirements in BS/EN 50018 (the second edition of EN 50018) "
               "differ significantly from those in BS 5501, Part 5 and are "
               "considerably more onerous for sub-group IIA and IIB. It should "
               "not be assumed, therefore, that an enclosure which satisfied "
               "the requirements of the first edition will necessarily satisfy "
               "those of the second. This, again, is a good reason for "
               "recommending that equipment to BS/EN 50018 should be chosen "
               "in the future."))

    b.append(h3("10.3 Construction of flameproof enclosures, entry facilities, "
                "fasteners and component parts",
                "10.3 Construction of flameproof enclosures, entry facilities, "
                "fasteners and component parts"))
    b.append(h4("10.3.1 Enclosure construction",
                "10.3.1 Enclosure construction"))
    b.append(p("Flameproof enclosures may be constructed of metal or "
               "appropriate non-metallic material (usually plastic). "
               "Non-metallic enclosures are limited to volumes up to 3000 cm³ "
               "if they are totally non-metallic, but where they are basically "
               "metallic with the non-metallic parts forming only parts of the "
               "enclosure this volume limit does not apply, provided that no "
               "non-metallic surface exceeds 500 cm³. This 500 cm² restriction "
               "does not apply to light-transmitting parts of luminaires which "
               "exceptionally may have non-metallic parts up to 8000 cm² in "
               "surface area."))
    b.append(note("<b>Note on units.</b> The print reads \"no non-metallic "
                  "surface exceeds 500 cm³. This 500 cm² restriction...\"; the "
                  "cm³ here is almost certainly a misprint for cm², as the "
                  "next page restates \"500 cm²\". Both printed forms are "
                  "retained."))
    b.append(p("Where a metallic enclosure is constructed of cast iron, "
               "account needs to be taken of the fact that some grades of cast "
               "iron are very brittle, and to avoid their use the cast iron is "
               "required to comply with, at worst, quality 150 as described in "
               "ISO 1851⁴. Brass and aluminium are also among the materials "
               "acceptable and construction may be by casting or fabrication "
               "with welding of similar types of securing parts of the "
               "enclosure together. Where enclosures are fabricated a routine "
               "pressure test, waived for enclosures type tested at four times "
               "the pressure developed in an internal explosion of the "
               "sub-group characteristic gas/air mixture (reference pressure), "
               "is always required to ensure the quality of fabrication as the "
               "level of confidence in repeatability of welding excellence is "
               "not as high as that for casting."))
    return "".join(b)
