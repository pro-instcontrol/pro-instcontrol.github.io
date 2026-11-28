# -*- coding: utf-8 -*-
"""Chapter 16, module B - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 478-479 (PDF pp. 499-500).

Covers Fig. 16.2 at the head of printed p. 478, identification by type,
serial number and year, section 16.2.2 Materials of construction with the
three numbered items, sections 16.2.3 and 16.2.4, and the unnumbered
Category 1 subheading through the printed p. 479 break. The final paragraph
ends with the single word 'Flameproof'; its continuation belongs to module C.

Printed quirks are kept in the English text (16.2.2 against the OCR reading
76.2.2, 'expected be capable', 'in much the same vane', 'not has been fully
addressed', the superscript 3 on 'EU journal') with bilingual notes; the
Vietnamese follows the intended meaning. This is an unofficial study
translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, fig, ul, ol
import mcmillanfig16 as F


def body_vi():
    b = []

    # Fig. 16.2 (printed 478), at the head of the page.
    b.append(fig(2, F.fig_f1602()))

    # B2 (raw 20460-20461).
    b.append(p("Thiết bị và hệ thống bảo vệ cũng được yêu cầu phải được nhận "
               "dạng theo kiểu, số seri và năm chế tạo, trong đó năm chế tạo "
               "là một yêu cầu trước đây chưa từng được áp dụng."))

    # Heading 16.2.2 (printed 478).
    b.append(h4("16.2.2 Vật liệu chế tạo",
                "16.2.2 Materials of construction"))
    b.append(note("<b>Lưu ý về ‘16.2.2’.</b> Lớp OCR đọc tiêu đề là "
                  "'76.2.2 Materials of construction'; ảnh trang in cho "
                  "thấy rõ '16.2.2 Materials of construction'. Bản tiếng "
                  "Anh giữ theo ảnh trang in."))

    # B4 (raw 20463-20464).
    b.append(p("Các ‘yêu cầu thiết yếu’ bao gồm các yêu cầu cơ bản đối với "
               "vật liệu dùng để chế tạo, cụ thể là:"))

    # B5-B7 (raw 20465-20479): the three printed numbered items.
    b.append(ol([
        "Chúng không được tự mình gây ra vụ nổ trong bất kỳ ứng suất nào "
        "tác dụng khi sử dụng. Yêu cầu này làm nổi bật các vấn đề có thể "
        "xảy ra nếu kim loại nhẹ được dùng không hạn chế ở các bộ phận bên "
        "ngoài của vỏ bọc, do nguy cơ phát tia lửa ma sát (nhiệt nhôm) mà "
        "một số trong các vật liệu này thể hiện khi bị thép gỉ va đập.",
        "Vật liệu chế tạo không được có tính chất phản ứng với bất kỳ khí "
        "dễ cháy, hơi, sương mù hoặc bụi dễ cháy nào theo cách làm suy "
        "giảm khả năng bảo vệ chống nổ. Vấn đề chính nhiều khả năng liên "
        "quan đến các bộ phận bằng nhựa và vật liệu cao su đàn hồi có thể "
        "bị suy giảm khi tiếp xúc với hóa chất, làm hư hỏng tính toàn vẹn "
        "của vỏ bọc hoặc giảm chất lượng cách điện. Cần xem xét mọi phản "
        "ứng như vậy giữa bất kỳ vật liệu chế tạo nào với khí quyển nổ.",
        "Vật liệu chế tạo phải ổn định trong phạm vi dung sai vận hành của "
        "thiết bị. Phải nhận dạng các điểm không ổn định (ví dụ, sự ăn mòn "
        "hoặc thay đổi trạng thái của vật liệu do nhiệt độ) và chứng minh "
        "là chúng không ảnh hưởng đến khả năng bảo vệ chống nổ hoặc hoạt "
        "động của hệ thống bảo vệ.",
    ]))

    # Heading 16.2.3 (printed 479).
    b.append(h4("16.2.3 Yêu cầu chung về thiết kế và cấu tạo",
                "16.2.3 General design and constructional requirements"))

    # B9 (raw 20483-20487).
    b.append(p("Các yêu cầu cơ bản đối với các bộ phận dùng trong thiết bị "
               "được bảo vệ và hệ thống bảo vệ là chúng chỉ được sử dụng "
               "trong giới hạn định mức của nhà sản xuất và, xét theo trình "
               "độ kiến thức kỹ thuật tại thời điểm chế tạo, chúng sẽ có "
               "khả năng thực hiện chức năng của mình trong suốt thời gian "
               "sử dụng dự kiến. (Thiết bị dùng nói chung thường được kỳ "
               "vọng là có khả năng hoạt động, với mức bảo trì tối thiểu, "
               "trong khoảng mười năm)."))
    b.append(note("<b>Lưu ý về ‘expected be capable’.</b> Bản in viết "
                  "'would normally be expected be capable of operating', "
                  "thiếu chữ 'to' sau 'expected'. Cụm được giữ nguyên trong "
                  "bản tiếng Anh; bản tiếng Việt theo nghĩa đúng."))

    # B10 (raw 20488-20493).
    b.append(p("Chỉ thị tiếp tục xác định các yêu cầu về kiểm soát rò rỉ từ "
               "thiết bị, cho phép hình thành lớp bụi mà không gây nguy "
               "hiểm, quá tải thiết bị, nhận dạng các nguy cơ phát sinh do "
               "phải mở thiết bị, và kiểm soát các điểm đánh lửa bên trong. "
               "Ngoài ra, chỉ thị còn xác định tia lửa, hồ quang, nhiệt độ "
               "bề mặt, tĩnh điện và sự thay đổi áp suất là các nguồn đánh "
               "lửa tiềm ẩn cần được phòng tránh."))

    # B11 (raw 20494-20497).
    b.append(p("Các yêu cầu chung tiếp tục theo cách tương tự nhưng trong "
               "mọi trường hợp đều xác định các vấn đề và yêu cầu phải "
               "phòng tránh chúng mà không nêu chi tiết cách thực hiện. Vì "
               "vậy, việc xây dựng các Tiêu chuẩn và viện dẫn chúng trên "
               "Tạp chí EU³ có tầm quan trọng lớn, vì nếu không có chúng thì "
               "không thể tin tưởng vào sự tuân thủ Chỉ thị."))
    b.append(note("<b>Lưu ý về ‘vane’.</b> Bản in viết 'in much the same "
                  "vane' (không phải 'vein'); bản tiếng Anh giữ nguyên "
                  "cách viết này."))

    # Heading 16.2.4 (printed 479, set on two printed lines).
    b.append(h4("16.2.4 Yêu cầu cụ thể cho các loại thiết bị và hệ thống "
                "bảo vệ đặc thù",
                "16.2.4 Specific requirements for particular types of "
                "apparatus and protective systems"))

    # B13 (raw 20500-20504).
    b.append(p("Ngoài các yêu cầu chung áp dụng cho mọi thiết bị và hệ "
               "thống bảo vệ chống nổ, còn có các yêu cầu bổ sung áp dụng "
               "cho các loại thiết bị chống nổ cụ thể. Sự phân định về cơ "
               "bản dựa trên mức độ bảo vệ được áp dụng, liên quan đến Vùng "
               "sử dụng dự kiến."))

    # Unnumbered subheading "Category 1 apparatus and protective systems".
    b.append(h4("Thiết bị và hệ thống bảo vệ Loại 1",
                "Category 1 apparatus and protective systems"))

    # B15 (raw 20506-20513).
    b.append(p("Theo yêu cầu của mình, thiết bị và hệ thống bảo vệ Loại 1 "
               "được dự định hoạt động trong mọi khu vực nguy hiểm, bao gồm "
               "Vùng 0 nếu có nguy cơ khí, hơi hoặc sương mù và Vùng 20 nếu "
               "có nguy cơ bụi. Yêu cầu cơ bản không phân định giữa hai "
               "trường hợp này, đó là: thiết bị phải được bảo vệ bằng ít "
               "nhất hai phương tiện bảo vệ độc lập sao cho khi một phương "
               "tiện hỏng thì phương tiện kia vẫn hoạt động; hoặc thiết bị "
               "phải luôn không gây đánh lửa cả trong vận hành bình thường "
               "lẫn khi có tới hai lỗi được áp dụng."))

    # B16 (raw 20514-20519), ending the printed page at 'Flameproof'.
    b.append(p("Tiêu chí hai lỗi dễ dàng được nhận ra là tiêu chí dùng trong "
               "an toàn nội tại (xem Chương 13), nhưng cách tiếp cận bảo vệ "
               "kép là mới và chưa từng được giải quyết đầy đủ ở cấp quốc "
               "tế trong bất kỳ diễn đàn kỹ thuật nào. Vì vậy, nó đại diện "
               "cho một ẩn số và là vấn đề sẽ cần được xem xét kỹ lưỡng về "
               "mặt kỹ thuật trước khi có thể triển khai đầy đủ. Câu hỏi về "
               "thế nào là một ‘phương pháp bảo vệ độc lập’ vẫn còn là vấn "
               "đề gây tranh cãi. Chống cháy nổ"))
    b.append(note("<b>Lưu ý về ‘not has been fully addressed’.</b> Bản in "
                  "viết 'not has been fully addressed internationally'; "
                  "cách viết sai ngữ pháp này được giữ nguyên trong bản "
                  "tiếng Anh, bản tiếng Việt theo nghĩa đúng."))
    b.append(note("<b>Lưu ý về điểm kết thúc của mô-đun này.</b> Trang in "
                  "kết thúc bằng một từ duy nhất 'Flameproof'. Phần tiếp "
                  "nối 'enclosure ‘d’ (Chapter 10) …' nằm trên trang in "
                  "480 và thuộc về mô-đun tiếp theo."))

    return "".join(b)


def body_en():
    b = []

    # Fig. 16.2 (printed 478), at the head of the page.
    b.append(fig(2, F.fig_f1602()))

    # B2 (raw 20460-20461).
    b.append(p("Apparatus and protective systems are also required to be "
               "identified by type, serial number and the year of "
               "construction, the latter being a requirement not previously "
               "applied."))

    # Heading 16.2.2 (printed 478).
    b.append(h4("16.2.2 Materials of construction",
                "16.2.2 Materials of construction"))
    b.append(note("<b>Note on ‘16.2.2’.</b> The OCR layer reads the heading "
                  "as '76.2.2 Materials of construction'; the page render "
                  "clearly shows '16.2.2 Materials of construction'. The "
                  "English text follows the render."))

    # B4 (raw 20463-20464).
    b.append(p("The ‘essential requirements’ include basic requirements for "
               "the material used in construction in that:"))

    # B5-B7 (raw 20465-20479): the three printed numbered items.
    b.append(ol([
        "They must not themselves trigger off an explosion in any stress "
        "applied in use. This requirement identifies the problems which "
        "could occur if light metals were used without restriction on outer "
        "parts of an enclosure because of the frictional (thermite) "
        "sparking risk which certain of these materials exhibit when struck "
        "by rusty steel.",
        "The material of construction must not be such as to react with any "
        "flammable gases, vapours, mists or combustible dusts in a way which "
        "would impair explosion protection. The principal problem is likely "
        "to be in respect of plastic and elastomeric parts which could be "
        "degraded by contact with chemicals and damage enclosure integrity "
        "or reduce insulation quality. Any such reaction between any "
        "materials of construction and the explosive atmosphere needs to be "
        "considered.",
        "Material of construction must be stable within the operating "
        "tolerances of the apparatus. Instabilities (e.g., the possible "
        "corrosion or change of state of materials due to temperature) must "
        "be identified and shown not to affect explosion protection or the "
        "operation of protective systems.",
    ]))

    # Heading 16.2.3 (printed 479).
    b.append(h4("16.2.3 General design and constructional requirements",
                "16.2.3 General design and constructional requirements"))

    # B9 (raw 20483-20487).
    b.append(p("The basic requirements for the components used in protected "
               "apparatus and protective systems are that they should only "
               "be used within their manufacturer’s ratings and, in the "
               "light of the state of technical knowledge at the time of "
               "their construction, they will be capable of performing "
               "their duty throughout their projected lifetime. (Apparatus "
               "in general use would normally be expected be capable of "
               "operating, with a minimum of maintenance, for around ten "
               "years)."))
    b.append(note("<b>Note on ‘expected be capable’.</b> The print reads "
                  "'would normally be expected be capable of operating', "
                  "with no 'to' after 'expected'. The phrase is kept verbatim "
                  "in the English text; the Vietnamese follows the intended "
                  "meaning."))

    # B10 (raw 20488-20493).
    b.append(p("The Directive goes on to identify requirements for control "
               "of leakage from apparatus, allowance for dust layer "
               "formation without danger, overloading of equipment, "
               "identification of hazards introduced by necessary opening "
               "of apparatus, and the control of internal ignitions. In "
               "addition it identifies sparks, arcs, surface temperatures, "
               "static electricity, and pressure changes as possible "
               "ignition sources which need to be guarded against."))

    # B11 (raw 20494-20497).
    b.append(p("The general requirements go on in much the same vane but in "
               "all cases identify problems and require that they be guarded "
               "against without identifying in detail how this is to be "
               "done. Thus the production of Standards and their reference "
               "in the EU journal³ is of great importance as without them it "
               "is not possible to have confidence in compliance with the "
               "Directive."))
    b.append(note("<b>Note on ‘vane’.</b> The print reads 'in much the same "
                  "vane' (not 'vein'); the printed spelling is kept in the "
                  "English text."))

    # Heading 16.2.4 (printed 479, set on two printed lines).
    b.append(h4("16.2.4 Specific requirements for particular types of "
                "apparatus and protective systems",
                "16.2.4 Specific requirements for particular types of "
                "apparatus and protective systems"))

    # B13 (raw 20500-20504).
    b.append(p("In addition to the general requirements which apply to all "
               "explosion protected apparatus and protective systems there "
               "are additional requirements which apply to specific types "
               "of explosion protected apparatus. The delineation is "
               "basically by the level of safeguarding applied relating to "
               "the intended Zone of use."))

    # Unnumbered subheading "Category 1 apparatus and protective systems".
    b.append(h4("Category 1 apparatus and protective systems",
                "Category 1 apparatus and protective systems"))

    # B15 (raw 20506-20513).
    b.append(p("Category 1 apparatus and protective systems are, by their "
               "requirements, intended for operation in all hazardous areas "
               "including Zone 0 if for gas, vapour or mist risks and Zone "
               "20 if for dust risks. No delineation between the two is "
               "present in the basic requirement which is: that the "
               "apparatus must be protected by at least two independent "
               "means of protection such that, when one fails the other "
               "remains operative; or that the apparatus must remain "
               "non-incendive in both normal operation and with up to two "
               "faults applied."))

    # B16 (raw 20514-20519), ending the printed page at 'Flameproof'.
    b.append(p("The two-fault criteria is readily recognizable as that used "
               "in intrinsic safety (see Chapter 13) but the dual protection "
               "approach is new and not has been fully addressed "
               "internationally in any technical forum. It thus represents "
               "an unknown quantity and one which will require considerable "
               "technical consideration before it can be fully implemented. "
               "The question as to what is an ‘independent method of "
               "protection’ is a vexed one. Flameproof"))
    b.append(note("<b>Note on ‘not has been fully addressed’.</b> The print "
                  "reads 'not has been fully addressed internationally'; "
                  "the ungrammatical sequence is kept verbatim in the "
                  "English text, while the Vietnamese follows the intended "
                  "meaning."))
    b.append(note("<b>Note on the end of this module's span.</b> The printed "
                  "page ends with the single word 'Flameproof'. Its "
                  "continuation, 'enclosure ‘d’ (Chapter 10) …', lies on "
                  "printed p. 480 and belongs to the next module."))

    return "".join(b)
