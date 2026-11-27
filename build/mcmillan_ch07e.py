# -*- coding: utf-8 -*-
"""Chapter 7, module E - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas* (1998),
printed pp. 175-177 (PDF pp. 196-198): sections 7.5.3 and 7.5.4, the
Zone 2 type 'N' apparatus, the dust-risk Standards, the nine BS 5501
first-edition mapping lines and the two IEC documents. This is a
prose-only span: no figures, tables, equations or worked examples. The
shell owns the seven-item reference list; footnote markers 1, 3 and 6
stay in the body as printed. Unofficial study translation.
"""
from mcmillan_common import h4, p, note


def body_vi():
    b = []

    # --- 7.5.3 ---------------------------------------------------------------
    b.append(h4("7.5.3 Thiết bị tương thích Vùng 2 cho khí, hơi và sương mù",
                "7.5.3 Zone 2 compatible apparatus for gases, vapours and mists"))
    b.append(p("Trong trường hợp thiết bị Vùng 2, không có một lịch sử lâu dài "
               "về chứng nhận bên thứ ba như ở các vùng nguy hiểm hơn, và ngành "
               "đã lựa chọn thiết bị của mình theo cách truyền thống, với sự trợ "
               "giúp của một Hướng dẫn Tiêu chuẩn Anh¹. Tuy nhiên, tại Anh, ngành "
               "luôn cảm thấy hơi bất an về điều này và đã tìm kiếm chứng nhận "
               "bên thứ ba cho cả thiết bị Vùng 2. Về mặt lịch sử, không có con "
               "đường nào để làm việc đó và, vì không có các yêu cầu chứng nhận "
               "chi tiết, nên rất khó sắp xếp được một sự chứng nhận."))
    b.append(p("Tình huống không mấy dễ chịu này đã dẫn đến việc HM Factory "
               "Inspectorate cấp 'Letters of no Objection' ('Thư không phản đối') "
               "cho một số thiết bị, về thực chất là nói rằng Cơ quan Thanh tra "
               "Nhà máy không có kiến thức hay bằng chứng nào gợi ý thiết bị đó "
               "không phù hợp. Tình trạng rắc rối này lại dẫn đến việc xây dựng "
               "tại Anh một Tiêu chuẩn cho thiết bị Loại 'N'⁶ để cho phép chứng "
               "nhận chính thức. Chữ 'N' viết hoa được chọn vì đã có một ký hiệu "
               "quốc tế cho loại thiết bị này là 'n', và người ta hy vọng rằng "
               "việc dùng chữ cái viết hoa sẽ tránh nhầm lẫn với khái niệm quốc "
               "tế, vốn không có Tiêu chuẩn nào. Cho đến nay vẫn chỉ có một "
               "Tiêu chuẩn Quốc gia cho thiết bị Loại 'N' và, khác với tình hình "
               "trong Section 7.4.1, nơi chứng nhận có giá trị trên khắp châu Âu, "
               "các giấy chứng nhận Loại 'N' do Anh cấp chỉ có giá trị trong "
               "nước Anh. Tiêu chuẩn đang nói đến là:"))
    b.append(note("<b>Ghi chú về Section 7.4.1.</b> Bản in viết 'Section 7.4.1' "
                  "trong câu so sánh về chứng nhận có giá trị khắp châu Âu. Mục "
                  "7.4 là 'Protection of electrical apparatus for dust risks' "
                  "(Thiết bị điện cho rủi ro bụi); gần như chắc chắn ý định là Mục "
                  "7.5.1. Cụm in được giữ nguyên, không đổi thành 7.5.1."))
    b.append(p("<b>BS 6941 (1988) – Electrical apparatus for explosive "
               "atmospheres with type of protection 'N' (see Chapter 14)</b>"))
    b.append(p("Tiêu chuẩn này bao gồm mọi yêu cầu cho tất cả các phương pháp "
               "dùng để bảo vệ thiết bị điện dự định cho Vùng 2. Nó dựa trên một "
               "văn bản quốc tế do Ủy ban Kỹ thuật Điện Quốc tế công bố – IEC "
               "79/15 (1987) – nhưng vì Anh không đồng ý với một số nội dung của "
               "IEC 79/15 nên có những khác biệt đáng kể."))
    b.append(p("<b>IEC 79–15 (1987) – Electrical equipment for explosive gas "
               "atmospheres Part 15: electrical apparatus with type of "
               "protection 'n' (see Chapter 14)</b>"))
    b.append(p("Văn bản quốc tế này đã gây nhiều tranh cãi, vì một số quốc gia "
               "phản đối một số phần của nó. Phản đối chính của Anh là việc dùng "
               "\"restricted breathing concept\" (khái niệm hạn chế hô hấp) cho "
               "các tiếp điểm phát tia lửa, và khái niệm này không xuất hiện "
               "trong BS 6941. Vì những phản đối đó, IEC 79–15 chỉ có thể được "
               "ban hành dưới dạng Báo cáo IEC chứ không phải Tiêu chuẩn. Điều "
               "này có nghĩa là nó chỉ là một văn bản hướng dẫn, dù có bề ngoài "
               "của một Tiêu chuẩn."))
    b.append(note("<b>Ghi chú về cách ghi IEC.</b> Bản in dùng dạng gạch chéo "
                  "'IEC 79/15 (1987)' trong đoạn về BS 6941 và dạng gạch ngang "
                  "'IEC 79–15 (1987)' trong tiêu đề cùng câu về Báo cáo IEC. Dạng "
                  "có khoảng trắng 'IEC 1241 – 1' ở trang in sau là một biến thể "
                  "riêng. Mỗi dạng được giữ đúng như in."))

    # --- 7.5.4 ---------------------------------------------------------------
    b.append(h4("7.5.4 Thiết bị điện cho rủi ro bụi",
                "7.5.4 Electrical apparatus for dust risks"))
    b.append(p("Tiêu chuẩn Anh về bụi dựa trên Tiêu chuẩn Quốc tế chưa được công "
               "bố, và các Tiêu chuẩn Anh hiện hành³ chỉ giới hạn ở Vùng 21 và 22 "
               "(Vùng Z và Y). Do đó, hiện không có Tiêu chuẩn nào để chế tạo "
               "thiết bị điện cho Vùng 20."))
    b.append(p("Đối với Vùng 21 và 22, đã có các Tiêu chuẩn chế tạo thiết bị. "
               "Chúng chủ yếu đề cập đến mức độ bao kín của thiết bị, cùng với "
               "các yêu cầu chế tạo bổ sung về những vấn đề như độ bền, v.v. Trong "
               "một trường hợp, Tiêu chuẩn liên quan đề cập đến các yêu cầu bổ "
               "sung cần thiết để làm cho thiết bị chế tạo cho rủi ro khí/hơi và "
               "sương mù trở nên phù hợp dùng trong bầu khí quyển nổ của bụi cháy "
               "được. Các Tiêu chuẩn liên quan như sau:"))
    b.append(p("<b>BS 6467 (1985) – Electrical apparatus with protection by "
               "enclosure for use in the presence of combustible dusts, Part 1: "
               "specification for apparatus (see Chapter 15)</b>"))
    b.append(p("Cần lưu ý là Tiêu chuẩn đặc biệt nhấn mạnh việc bảo vệ bằng vỏ "
               "bao kín. Ngoài ra, Tiêu chuẩn phân biệt giữa thiết bị phù hợp cho "
               "Vùng 21 và Vùng 22 với thiết bị chỉ phù hợp cho Vùng 22."))
    b.append(note("<b>Ghi chú về ngày của BS 6467 Part 2.</b> Danh mục tài liệu "
                  "tham khảo của Chương 7 ghi BS 6467 Part 2 (1985), trong khi "
                  "tài liệu tham khảo 2 của Chương 6 ghi cùng Part 2 là (1988) "
                  "và dùng cách diễn đạt tiêu đề khác. Hai mốc này không được "
                  "đồng nhất hóa ở đây; phần thân bài chỉ trích Part 1 (1985)."))
    b.append(p("<b>BS 7353 (1992) – Guide to the use of electrical apparatus "
               "complying with BS 5501 or BS 6941 in the presence of combustible "
               "dust (see Chapter 15)</b>"))
    b.append(p("Về cơ bản, Tiêu chuẩn này quy định trong những trường hợp nào "
               "thiết bị phù hợp với các Tiêu chuẩn Châu Âu (EN's) thì dùng được "
               "trong bầu khí quyển nổ của bụi cháy được và không khí, và cần "
               "những đặc điểm chế tạo bổ sung nào. Nó gọi các Tiêu chuẩn Châu Âu "
               "đó là BS 5501, vì ấn bản đầu tiên của chúng được đánh số như "
               "sau:"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 1 (1977) – EN 50014, first edition</b>"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 2 (1997) – EN 50015, first edition</b>"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 3 (1977) – EN 50016, first edition</b>"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 4 (1977) – EN 50017, first edition</b>"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 5 (1977) – EN 50018, first edition</b>"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 6 (1977) – EN 50019, first edition</b>"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 7 (1977) – EN 50020, first edition</b>"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 8 (1988) – EN 50028, first edition</b>"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 9 (1982) – EN 50039, first edition</b>"))
    b.append(note("<b>Ghi chú về năm của Part 2.</b> Bản in ghi 'BS 5501, Part 2 "
                  "(1997) – EN 50015, first edition', trong khi mọi Part khác đều "
                  "là 1977 và chính EN 50015 được ghi là 1994 ở nơi khác. Năm bị "
                  "đảo chữ này được giữ nguyên theo bản in."))
    b.append(p("Như trước, các Tiêu chuẩn Châu Âu này hiện đang, hoặc sẽ sớm, "
               "được thay thế bằng các ấn bản thứ hai (được đánh số BS/EN50 trở "
               "lên, trừ BS 5501 Parts 8 và 9), nhưng những khác biệt sinh ra "
               "không có khả năng là đáng kể và rất có thể trong hầu hết trường "
               "hợp các ấn bản thứ hai, khi dùng cùng Tiêu chuẩn này, sẽ cho "
               "kết quả thỏa đáng."))
    b.append(p("<b>IEC 1241 – 1 – Electrical apparatus for use in the presence "
               "of combustible dust, Part 1: electrical apparatus protected by "
               "enclosure (see Chapter 6)</b>"))
    b.append(p("Đây là văn bản IEC liên quan đến rủi ro bụi và là văn bản mới hơn "
               "nhiều. Yêu cầu của Tiêu chuẩn này không khác biệt nhiều so với "
               "BS 6467, Part 1 và vào một thời điểm nào đó trong tương lai người "
               "ta kỳ vọng hai Tiêu chuẩn sẽ được hài hòa hóa. Cho đến lúc đó, "
               "thiết bị theo Tiêu chuẩn IEC hoặc theo BS 6467, Part 1 đều được "
               "kỳ vọng là chấp nhận được tại Anh. Một Part khác của IEC 1241 "
               "cũng đang được dự kiến và sẽ đề cập đến ít nhất một số vấn đề mà "
               "BS 7535 đề cập."))
    b.append(note("<b>Ghi chú về BS 7535 (lần thứ nhất).</b> Bản in viết 'BS "
                  "7535' ở đây, nhưng Tiêu chuẩn được mô tả ở trang in trước là "
                  "BS 7353 (1992). Số in được giữ nguyên, không sửa."))
    b.append(p("Công việc đang được tiến hành trên các mục để đề cập đến an toàn "
               "nội tại 'i' và cấp áp khí 'p' trong rủi ro bụi. Khi được công bố, "
               "trừ khi Anh bỏ phiếu chống lại, chúng được kỳ vọng sẽ được chấp "
               "nhận tại Anh như các phương án thay thế cho BS 7535."))
    b.append(note("<b>Ghi chú về BS 7535 (lần thứ hai).</b> 'BS 7535' lại được "
                  "in ở câu cuối. Cả hai lần xuất hiện đều được giữ nguyên theo "
                  "bản in; ký hiệu đúng ở nơi khác trong chương là BS 7353 (1992)."))
    return "".join(b)


def body_en():
    b = []

    # --- 7.5.3 ---------------------------------------------------------------
    b.append(h4("7.5.3 Zone 2 compatible apparatus for gases, vapours and mists",
                "7.5.3 Zone 2 compatible apparatus for gases, vapours and mists"))
    b.append(p("In the case of Zone 2 apparatus there is no long history of "
               "third-party certification as in the more hazardous zones, and "
               "industry has historically selected its own using a British "
               "Standard Guide¹ for assistance. Within the UK, however, industry "
               "has always been slightly uneasy at this and has sought "
               "third-party certification for Zone 2 equipment also. "
               "Historically, there was no avenue for this and, as no detailed "
               "certification requirements existed, it was difficult to arrange "
               "one."))
    b.append(p("This unhappy situation led to HM Factory Inspectorate issuing "
               "'Letters of no Objection' for some items of equipment, which "
               "effectively said that the Factory Inspectorate had no knowledge "
               "or evidence to suggest the equipment was unsuitable. This "
               "difficult state of affairs led to the production in the UK of a "
               "Standard for Type 'N' equipment⁶ to permit formal Certification. "
               "The upper case 'N' was chosen because there was an international "
               "symbol for this equipment, 'n', and it was hoped that the use of "
               "the upper case letter would avoid confusion with the "
               "international concept, for which there was no Standard. There "
               "still remains only a National Standard for Type 'N' equipment "
               "and, unlike the situation in Section 7.4.1 where certification "
               "is valid across Europe, type 'N' certificates issued within the "
               "UK are valid only in the UK. The Standard in question is:"))
    b.append(note("<b>Printed cross-reference note.</b> The print reads "
                  "'Section 7.4.1' in the comparison about certification valid "
                  "across Europe. Section 7.4 is 'Protection of electrical "
                  "apparatus for dust risks'; the intended section is almost "
                  "certainly 7.5.1. The printed reference is retained, not "
                  "silently corrected."))
    b.append(p("<b>BS 6941 (1988) – Electrical apparatus for explosive "
               "atmospheres with type of protection 'N' (see Chapter 14)</b>"))
    b.append(p("This Standard covers all of the requirements for all of the "
               "methods used for protection of electrical equipment which is "
               "intended for Zone 2. It is based upon an international document "
               "published by the International Electrotechnical Commission – "
               "IEC 79/15 (1987) – but because the UK did not agree with some of "
               "the contents of IEC 79/15 there are significant differences."))
    b.append(p("<b>IEC 79–15 (1987) – Electrical equipment for explosive gas "
               "atmospheres Part 15: electrical apparatus with type of "
               "protection 'n' (see Chapter 14)</b>"))
    b.append(p("This international document was the subject of considerable "
               "controversy as several countries objected to some parts of it. "
               "The principal objection of the UK was to the \"restricted "
               "breathing concept\" being used for sparking contacts, and this "
               "concept does not appear in BS 6941. Because of these objections "
               "it was only possible to issue IEC 79–15 as an IEC Report, not a "
               "Standard. This means that it is only a guidance document despite "
               "having the appearance of a Standard."))
    b.append(note("<b>IEC designation note.</b> The print gives the slash form "
                  "'IEC 79/15 (1987)' in the BS 6941 paragraph and the en-dash "
                  "form 'IEC 79–15 (1987)' in the heading and in the sentence "
                  "about the IEC Report. The spaced form 'IEC 1241 – 1' on the "
                  "next printed page is a separate variant. Each form is kept "
                  "as printed."))

    # --- 7.5.4 ---------------------------------------------------------------
    b.append(h4("7.5.4 Electrical apparatus for dust risks",
                "7.5.4 Electrical apparatus for dust risks"))
    b.append(p("The British Standard for dusts based upon the International "
               "Standard is not yet published and the current British "
               "Standards³ are limited to Zone 21 and 22 (Zone Z and Y). There "
               "are currently, therefore, no Standards for the construction of "
               "electrical equipment for Zone 20."))
    b.append(p("For Zone 21 and 22, equipment construction Standards exist. "
               "These mainly cover the degree of enclosure of the equipment, "
               "together with additional construction requirements covering "
               "such things as strength, etc. In one case, the relevant Standard "
               "covers the additional requirements necessary to make equipment "
               "constructed for gas/vapour and mist risks suitable for use in "
               "the explosive atmospheres of combustible dusts. The relevant "
               "Standards follow:"))
    b.append(p("<b>BS 6467 (1985) – Electrical apparatus with protection by "
               "enclosure for use in the presence of combustible dusts, Part 1: "
               "specification for apparatus (see Chapter 15)</b>"))
    b.append(p("It will be noted that the Standard particularly draws attention "
               "to the fact that protection is by enclosure. In addition, the "
               "Standard differentiates between equipment suitable for Zone 21 "
               "and Zone 22, and that suitable only for Zone 22."))
    b.append(note("<b>BS 6467 Part 2 date note.</b> The Chapter 7 reference "
                  "dates BS 6467 Part 2 (1985), while Chapter 6's reference 2 "
                  "dates the same Part 2 (1988) and uses different title "
                  "wording. The two dates are left unreconciled here; the body "
                  "cites only Part 1 (1985)."))
    b.append(p("<b>BS 7353 (1992) – Guide to the use of electrical apparatus "
               "complying with BS 5501 or BS 6941 in the presence of combustible "
               "dust (see Chapter 15)</b>"))
    b.append(p("This Standard essentially specifies in what circumstances "
               "equipment complying with European Standards (EN's) is suitable "
               "for use in explosive atmospheres of combustible dust and air "
               "and what extra constructional features are necessary. It refers "
               "to these European Standards as BS 5501, as their first editions "
               "were given the numbers that follow:"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 1 (1977) – EN 50014, first edition</b>"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 2 (1997) – EN 50015, first edition</b>"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 3 (1977) – EN 50016, first edition</b>"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 4 (1977) – EN 50017, first edition</b>"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 5 (1977) – EN 50018, first edition</b>"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 6 (1977) – EN 50019, first edition</b>"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 7 (1977) – EN 50020, first edition</b>"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 8 (1988) – EN 50028, first edition</b>"))
    b.append(p("\u00a0\u00a0<b>BS 5501, Part 9 (1982) – EN 50039, first edition</b>"))
    b.append(note("<b>Part 2 year note.</b> The print gives 'BS 5501, Part 2 "
                  "(1997) – EN 50015, first edition', while every other Part is "
                  "1977 and EN 50015 itself is dated 1994 elsewhere. The "
                  "transposed year is retained verbatim."))
    b.append(p("While, as before, these European Standards are now, or soon "
               "will be, replaced by their second editions (which are numbered "
               "BS/EN50 and upwards with the exception of BS 5501, Parts 8 and "
               "9), the differences so produced are not likely to be significant "
               "and it is likely that in most cases the second editions will, "
               "when used with this standard, produce satisfactory results."))
    b.append(p("<b>IEC 1241 – 1 – Electrical apparatus for use in the presence "
               "of combustible dust, Part 1: electrical apparatus protected by "
               "enclosure (see Chapter 6)</b>"))
    b.append(p("This is the IEC document which is relevant to dust hazards and "
               "is a much newer document. The requirements of this Standard are "
               "not dissimilar to BS 6467, Part 1 and at some time in the future "
               "it is expected that the two Standards will be harmonized. Until "
               "that time, however, it is expected that equipment to either the "
               "IEC Standard or BS 6467, Part 1 will be acceptable in the UK. A "
               "further Part of IEC 1241 is also envisaged and will address at "
               "least some of the matters addressed by BS 7535."))
    b.append(note("<b>BS 7535 note (first occurrence).</b> The print says 'BS "
                  "7535' here, but the Standard described on the preceding "
                  "printed page is BS 7353 (1992). The printed number is kept, "
                  "not corrected."))
    b.append(p("Work is in hand on sections to cover intrinsic safety 'i' and "
               "pressurization 'p' in dust risks. When they are published, "
               "unless the UK votes against them, they are expected to be "
               "acceptable in the UK as alternatives to BS 7535."))
    b.append(note("<b>BS 7535 note (second occurrence).</b> 'BS 7535' is printed "
                  "a second time in the final sentence. Both occurrences are "
                  "preserved as printed; the designation used elsewhere in the "
                  "chapter is BS 7353 (1992)."))
    return "".join(b)
