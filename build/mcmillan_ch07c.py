# -*- coding: utf-8 -*-
"""Chapter 7, module C - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas* (1998),
printed pp. 169-172 (PDF pp. 190-193): section 7.3 on Zone 2 apparatus
and type of protection 'n' (historically UK 'N'), section 7.4 on dust
risks, section 7.5 on apparatus construction Standards and harmonisation,
and section 7.5.1 on Zone 0/Zone 1 compatible apparatus through the
BS/EN 50014 (1993) General requirements block. This is a pure prose
span: no figures, tables, equations, worked examples or reference list.
Unofficial study translation; the integration module owns the page shell.
"""
from mcmillan_common import h3, h4, p, note


def body_vi():
    b = []

    # --- 7.3 --------------------------------------------------------------
    b.append(h3("7.3 Tình hình liên quan đến thiết bị Vùng 2",
                "7.3 Situation in respect of Zone 2 apparatus"))
    b.append(p("Trong khi các kỹ thuật bảo vệ thiết bị được mô tả trong các "
               "Mục 7.2.1 đến 7.2.5 đều phù hợp cho ít nhất Vùng 1 và Vùng 2 "
               "(ngoại trừ tình hình hiện tại liên quan đến các khái niệm bảo "
               "vệ ‘o’ và ‘q’) thì chúng lại đưa mức độ bảo vệ cao hơn mức cần "
               "thiết cho Vùng 2. Vì lý do này, một loại hình bảo vệ khác đã "
               "được phát triển."))
    b.append(p("<b>Loại bảo vệ ‘n’ (trước đây ở Anh là loại bảo vệ ‘N’)</b>"))
    b.append(p("Loại bảo vệ này bao gồm thiết bị công nghiệp không bị nóng lên "
               "hoặc phát tia lửa, vốn trước đây do người sử dụng lựa chọn, và "
               "bổ sung các dạng bảo vệ đơn giản hóa cho thiết bị phát tia lửa "
               "hoặc thiết bị bị nóng, dựa trên các loại hình bảo vệ Vùng 1. "
               "Bằng cách đưa ra các yêu cầu chi tiết, nó xóa bỏ sự nghi ngờ "
               "từng tồn tại khi việc lựa chọn theo các tiêu chí khá chung "
               "chung là cách làm thông thường, dẫn đến việc sử dụng quá mức "
               "thiết bị Vùng 1 ở Vùng 2 và làm tăng không cần thiết chi phí "
               "vận hành."))

    # --- 7.4 --------------------------------------------------------------
    b.append(h3("7.4 Bảo vệ thiết bị điện đối với nguy cơ do bụi",
                "7.4 Protection of electrical apparatus for dust risks"))
    b.append(p("Khác với tình hình đối với khí, hơi và sương mù, các vấn đề "
               "liên quan đến bụi là tính chất lắng đọng của bụi và tính dẫn "
               "điện của nó. Nếu bụi xâm nhập vào vỏ bọc thiết bị với số lượng "
               "đáng kể, nó sẽ lắng đọng trên các linh kiện điện và, bằng cách "
               "cách điện các linh kiện này, có thể gây nóng quá mức và, nếu "
               "bụi dẫn điện, gây ngắn mạch cục bộ và các lỗi tương tự. Do đó, "
               "mục tiêu đối với bụi luôn là ngăn không cho một lượng đáng kể "
               "xâm nhập vào vỏ bọc. Điều này dẫn đến một tình hình đơn giản "
               "hơn nhiều so với tình hình đối với khí, hơi và sương mù, vì "
               "trên thực tế chỉ có một dạng bảo vệ, đó là bảo đảm bụi nằm ở "
               "bên ngoài vỏ bọc."))
    b.append(p("Mặc dù một số thiết bị được chế tạo cho nguy cơ "
               "khí/hơi/sương mù cũng phù hợp cho bụi, nhưng điều này không "
               "nhất thiết phải đúng, và không nên giả định rằng vì thiết bị "
               "phù hợp với một loại môi trường thì tự động phù hợp với loại "
               "còn lại. Cần nhớ điều này rất quan trọng vì nguy cơ bụi và nguy "
               "cơ khí/hơi/sương mù thường cùng tồn tại và, trong những "
               "trường hợp đó, thiết bị điện phải được bảo vệ để sử dụng trong "
               "cả hai loại nguy cơ, và các yếu tố của sự bảo vệ đó có thể "
               "tách riêng trong từng trường hợp."))

    # --- 7.5 --------------------------------------------------------------
    b.append(h3("7.5 Tiêu chuẩn chế tạo thiết bị điện",
                "7.5 Apparatus construction Standards"))
    b.append(p("Việc hài hòa hóa các Tiêu chuẩn có tầm quan trọng tối cao đối "
               "với các nước thành viên EU vì các Tiêu chuẩn này sẽ được chấp "
               "nhận trên toàn EU và, theo một thỏa thuận giữa EU và Hiệp hội "
               "Thương mại Tự do Châu Âu (EFTA), cả ở các nước EFTA. Vì mục "
               "đích này, những Tiêu chuẩn đã được hài hòa có thể được viện "
               "dẫn trong các Chỉ thị EU như những Tiêu chuẩn mà sự tuân thủ "
               "của chúng chứng minh việc đáp ứng Chỉ thị, miễn là điều này "
               "được một tổ chức chứng nhận được công nhận (được thông báo) "
               "xác minh. Do đó, các Tiêu chuẩn bảo vệ thiết bị đối với nguy cơ "
               "khí, hơi và sương mù (ngoại trừ những phương pháp chỉ giới hạn "
               "sử dụng ở Vùng 2) đã theo truyền thống được viện dẫn trong "
               "76/117/EEC² và việc tuân thủ chúng cho phép sử dụng Dấu hiệu "
               "Cộng đồng đặc trưng (xem Chương 1). Với việc đưa ra Chỉ thị mới "
               "94/9/EC⁵, chính sách của EEC đã thay đổi theo hướng đưa các "
               "yêu cầu kỹ thuật thiết yếu vào trong bản thân Chỉ thị."))
    b.append(p("Các yêu cầu này được đưa vào ở dạng tương đối chung và người "
               "ta dự định xác định các tiêu chuẩn hài hòa (EN’S) như một "
               "phương thức đáp ứng các yêu cầu thiết yếu, thông qua việc phê "
               "duyệt bằng cách công bố trên European Journal⁷. Rất tiếc, "
               "người ta đã nhận ra rằng các ấn bản thứ hai của những Tiêu "
               "chuẩn hiện hành này không nhất thiết đáp ứng các yêu cầu thiết "
               "yếu và cơ quan soạn thảo Tiêu chuẩn, Centre Europeen de "
               "Normalization Electrique (CENELEC), đã được giao nhiệm vụ xây "
               "dựng các ấn bản thứ ba mà nhìn chung là vào năm 1997. Điều này "
               "có nghĩa là Chỉ thị mới⁵ không thể được đưa vào áp dụng trên "
               "thực tế cho đến một thời điểm nào đó trong năm 1997, và trong "
               "thời gian chờ đó Chỉ thị cũ² vẫn sẽ là phương tiện duy nhất để "
               "trao Dấu hiệu Cộng đồng đặc trưng. Rất tiếc, Chỉ thị này vẫn đề "
               "cập đến các ấn bản thứ nhất của các Tiêu chuẩn hài hòa và các "
               "ấn bản thứ hai, hiện đang có hiệu lực, sẽ không cho phép sử "
               "dụng dấu hiệu. Hành động khẩn cấp đang được tiến hành để đưa "
               "các ấn bản thứ hai của các Tiêu chuẩn hài hòa vào 76/117/EEC² "
               "nhưng cho đến lúc đó việc chứng nhận theo Chỉ thị này sẽ dựa "
               "trên các ấn bản thứ nhất."))
    b.append(note("<b>Ghi chú về ‘European Journal⁷’.</b> Thân văn bản in cụm "
                  "'European Journal⁷' với chỉ số chân trang ⁷, trong khi "
                  "tiêu mục tham chiếu 7 lại ghi là 'Official Journal of the "
                  "European Communities'. Hai cách gọi này được giữ nguyên "
                  "theo bản in và không được đồng nhất hóa."))
    b.append(note("<b>Ghi chú về cụm 'in general, in 1997'.</b> Nguyên văn in "
                  "'third editions which do in general, in 1997' trong câu về "
                  "nhiệm vụ của CENELEC. Cấu trúc và các dấu phẩy của cụm này "
                  "được giữ lại thay vì được viết lại cho trơn tru."))
    b.append(note("<b>Ghi chú về cách viết tên CENELEC trong bản in.</b> Bản in "
                  "ghi 'Centre Europeen de Normalization Electrique (CENELEC)' "
                  "— không có dấu tiếng Pháp và dùng 'Normalization' (cách "
                  "viết Mỹ) thay vì 'Normalisation'. Cách viết này được sao "
                  "chép nguyên văn và không được sửa lại."))
    b.append(p("Mặc dù điều này có vẻ là một vấn đề, nhưng thực ra không phải, "
               "vì các ấn bản thứ hai không khác biệt nhiều so với các ấn bản "
               "thứ nhất, và hầu hết các nhà sản xuất thiết bị đang bảo đảm "
               "thiết bị của họ tuân thủ cả hai cho đến khi Chỉ thị mới⁵ có "
               "hiệu lực. Khi Chỉ thị⁵ này được ban hành, các ấn bản thứ ba của "
               "các Tiêu chuẩn hài hòa sẽ tồn tại, và mọi thiết bị được chứng "
               "nhận sau đó sẽ tuân thủ các quy định mới."))

    # --- 7.5.1 ------------------------------------------------------------
    b.append(h4("7.5.1 Thiết bị tương thích Vùng 0 và/hoặc Vùng 1 cho khí, hơi "
                "và sương mù",
                "7.5.1 Zone 0 and/or Zone 1 compatible apparatus for gases, "
                "vapours and mists"))
    b.append(p("Như đã nêu, đã có một lịch sử lâu dài trên toàn thế giới là chỉ "
               "sử dụng thiết bị được chứng nhận bên thứ ba ở Vùng 0 và Vùng 1, "
               "và ở một số quốc gia điều này được pháp luật yêu cầu. Hiện tại "
               "thì không phải vậy ở Anh, nhưng Chỉ thị Khí quyển nổ mới⁵ của "
               "EU sẽ trên thực tế bảo đảm điều đó bằng cách yêu cầu mọi thiết "
               "bị được đưa ra thị trường trong EU đều phải tuân thủ Chỉ thị "
               "này (bản thân Chỉ thị yêu cầu chứng nhận kiểu bên thứ ba ở mức "
               "tối thiểu). Mặc dù điều này sẽ gây ra một số hạn chế ở Anh nhưng "
               "tác động sẽ không lớn, vì ngành công nghiệp Anh theo truyền "
               "thống đã chỉ sử dụng thiết bị được chứng nhận bên thứ ba theo "
               "lựa chọn của mình. Vì vậy, tùy thuộc vào việc giải quyết các "
               "khó khăn đã xác định trong chương này, tình hình sẽ không thay "
               "đổi nhiều."))
    b.append(p("Điều mà tình hình lịch sử đó dẫn đến là mức độ chi tiết rất cao "
               "của các Tiêu chuẩn chế tạo, vốn ngày càng mang tính quốc tế do "
               "quy mô hoạt động quốc tế của ngành công nghiệp cần đến thiết "
               "bị. Tình hình hiện nay là các Tiêu chuẩn dành cho thiết bị điện "
               "nói chung dự định cho Vùng 0 hoặc Vùng 1 (hoặc cả hai) là các "
               "Tiêu chuẩn Châu Âu được hài hòa đầy đủ, và trong vòng 10 năm tới "
               "sẽ trở thành các Tiêu chuẩn Quốc tế được hài hòa đầy đủ. Tuy "
               "nhiên, vẫn còn các Tiêu chuẩn quốc gia và châu Âu lịch sử đề "
               "cập đến lĩnh vực này và thiết bị tuân thủ các Tiêu chuẩn đó vẫn "
               "còn sẵn có. Không có gì cho rằng nhìn chung thiết bị như vậy "
               "không còn an toàn khi sử dụng trong nhiều trường hợp, và tên "
               "của các Tiêu chuẩn đó được đề cập trong các Chương 8 đến 15. "
               "Tuy nhiên, nhiều tiêu chuẩn trong số đó đã lỗi thời hoặc bị "
               "bãi bỏ và không nên được dùng để chế tạo thiết bị mới. Khi có "
               "thiết bị tuân thủ cả Tiêu chuẩn hiện hành lẫn Tiêu chuẩn lịch "
               "sử, thì thiết bị theo các tiêu chuẩn hiện hành luôn được ưu "
               "tiên."))
    b.append(p("Số lượng tương đối lớn các phương pháp bảo vệ thiết bị điện đã "
               "dẫn đến sự tồn tại của rất nhiều Tiêu chuẩn, và người ta đã "
               "nhận ra rằng nhiều yêu cầu của các tiêu chuẩn này là chung. Vì "
               "vậy, cấu trúc chuẩn hóa là có một Tiêu chuẩn chung và một loạt "
               "Tiêu chuẩn bổ sung viện dẫn Tiêu chuẩn chung cho nhiều yêu cầu "
               "của chúng, nhưng chứa các yêu cầu bổ sung riêng cho phương pháp "
               "bảo vệ thiết bị được sử dụng. Tất cả những điều này là các "
               "Tiêu chuẩn Châu Âu và được cấu trúc như sau."))

    # --- BS/EN 50014 (1993) block -----------------------------------------
    b.append(p("<b>BS/EN 50014 (1993) – General requirements (see Chapter 8)</b>"))
    b.append(p("Đây là Tiêu chuẩn chung và chứa mọi yêu cầu áp dụng cho hơn một "
               "phương pháp bảo vệ cụ thể. Các yêu cầu của nó áp dụng cho tất cả "
               "các khái niệm bảo vệ (ngoại trừ ‘n’ hiện tại), trừ khi được "
               "loại trừ cụ thể, và cần được đọc cùng với tất cả các Tiêu chuẩn "
               "bảo vệ riêng lẻ sau đây. Hiện nó đang ở giai đoạn ấn bản thứ "
               "hai, ấn bản này phải thay thế ấn bản thứ nhất, nhưng thiết bị "
               "được chứng nhận theo ấn bản này và một trong các Tiêu chuẩn "
               "bảo vệ phụ sẽ không thể, như đã mô tả ở trên, mang Dấu hiệu "
               "Cộng đồng đặc trưng được đề cập trong Chương 1, trừ khi nó cũng "
               "đáp ứng ấn bản thứ nhất của Tiêu chuẩn. Do đó, nó sẽ không được "
               "tự do tiếp cận các nước thành viên EU (và các nước EFTA)."))
    b.append(p("Điều này, như đã xác định ở trên, là vì Chỉ thị 76/117/EEC² hiện "
               "đề cập đến ấn bản thứ nhất và dấu hiệu được kiểm soát bởi Chỉ "
               "thị, không phải bởi Tiêu chuẩn. Một lần nữa, như đã xác định ở "
               "trên, công tác đang được tiến hành để sửa đổi 76/117/EEC² và dự "
               "kiến sẽ cho phép sử dụng các ấn bản thứ hai của Tiêu chuẩn này "
               "và các Tiêu chuẩn phụ của nó cho thiết bị liên quan đến Chỉ thị "
               "vào cuối năm 1996. Một biến chứng nữa đang cản trở việc kích "
               "hoạt Chỉ thị mới⁵ là thực tế có vẻ như tồn tại sự khác biệt "
               "giữa các ấn bản thứ hai của những Tiêu chuẩn này và các yêu cầu "
               "thiết yếu nêu trong Chỉ thị mới. (Như đã nêu, tất cả các Chỉ "
               "thị tiếp cận mới đều mang các yêu cầu an toàn thiết yếu trong "
               "nội bộ chúng, khác với các Chỉ thị cũ hơn vốn viện dẫn các "
               "Tiêu chuẩn). Điều này có nghĩa là cần phải xây dựng các ấn bản "
               "thứ ba của These standards và việc xây dựng dự kiến hoàn thành "
               "vào cuối năm 1997. Khi được công bố, thiết bị tuân thủ các ấn "
               "bản thứ ba của những Tiêu chuẩn này sẽ được coi là tuân thủ "
               "Chỉ thị và do đó sẽ có thể mang 'Dấu hiệu Cộng đồng đặc trưng' "
               "theo các quy định của Chỉ thị. Sự cần thiết phải tiếp tục dùng "
               "Chỉ thị cũ, 76/117/EEC², sẽ chấm dứt đối với thiết bị mới, mặc "
               "dù thiết bị cũ vẫn tiếp tục được chấp nhận cho đến đầu thế kỷ "
               "hai mươi mốt (xem Chương 1)."))
    b.append(note("<b>Ghi chú về chữ 'These' viết hoa.</b> Câu in gốc 'This "
                  "means that third editions of These standards will need to "
                  "be produced' viết hoa chữ 'These' giữa câu. Cách viết đó "
                  "được giữ nguyên trong cả hai bản văn và không được sửa "
                  "thành 'these'."))
    return "".join(b)


def body_en():
    b = []

    # --- 7.3 --------------------------------------------------------------
    b.append(h3("7.3 Situation in respect of Zone 2 apparatus",
                "7.3 Situation in respect of Zone 2 apparatus"))
    b.append(p("While the techniques described in Sections 7.2.1 to 7.2.5 are "
               "all suitable for, at least, Zone 1 and 2 (with the exception "
               "of the current situation in respect of protection concepts "
               "‘o’ and ‘q’) they offer a standard of protection which is "
               "higher than is necessary for Zone 2. For this reason a further "
               "type of protection has been developed."))
    b.append(p("<b>Type of protection ‘n’ (historically in the UK, type of "
               "protection ‘N’)</b>"))
    b.append(p("This type of protection includes industrial equipment which "
               "does not get hot or spark, which was historically selected by "
               "users, and adds simplified forms of protection for sparking "
               "equipment or that which gets hot, based upon the Zone 1 types "
               "of protection. By producing detailed requirements, it removes "
               "the doubt which used to exist when only selection by somewhat "
               "general criteria was the order of the day, which led to "
               "excessive use of Zone 1 equipment in Zone 2, needlessly "
               "increasing operational expense."))

    # --- 7.4 --------------------------------------------------------------
    b.append(h3("7.4 Protection of electrical apparatus for dust risks",
                "7.4 Protection of electrical apparatus for dust risks"))
    b.append(p("Unlike the situation in respect of gases, vapours and mists, "
               "the problems in relation to dusts are the settling properties "
               "which dusts have, and their conductivity. If dust enters an "
               "equipment enclosure in significant quantities, it will settle "
               "on the electrical components and by insulating them could "
               "cause excessive heating and, if it is conductive, partial "
               "short circuits and similar faults. The objective with dusts, "
               "therefore, is always to prevent significant amounts "
               "penetrating the enclosure. This leads to a very much simpler "
               "situation than that which exists with gases, vapours and "
               "mists, as there is effectively only one form of protection, "
               "which is to ensure the dust remains on the outside of the "
               "enclosure."))
    b.append(p("While some equipment constructed for gas/vapour/mist risks is "
               "also suitable for dusts, this does not necessarily follow, and "
               "it should not be assumed that because equipment is suitable "
               "for the one type of medium it is automatically suitable for "
               "the other. It is very important to remember this as dust risks "
               "and gas/vapour/mist risks often coincide and, in such cases, "
               "the electrical equipment must be protected for use in both "
               "types of risk, and the elements of this protection may be "
               "separate in each case."))

    # --- 7.5 --------------------------------------------------------------
    b.append(h3("7.5 Apparatus construction Standards",
                "7.5 Apparatus construction Standards"))
    b.append(p("The harmonization of Standards is of paramount importance for "
               "members of the EU as these Standards will be acceptable "
               "throughout the EU and, by an agreement between the EU and the "
               "European Free Trade Association (EFTA), in EFTA countries "
               "also. To this end, those Standards which are harmonized may be "
               "called up in EU Directives as Standards with which compliance "
               "demonstrates fulfilment of the Directive, provided this is "
               "verified by a recognized (notified) certification body. "
               "Therefore, the Standards for equipment protection for gas, "
               "vapour and mist risks (with the exception of those methods "
               "restricted to Zone 2 use only) have been historically "
               "referred to in 76/117/EEC² and compliance with them allows the "
               "use of the Distinctive Community Mark (see Chapter 1). With "
               "the introduction of the newer Directive 94/9/EC⁵, the EEC "
               "policy was changed to include essential technical requirements "
               "within the Directive."))
    b.append(p("These are included in a relatively general form and it is "
               "intended to identify the harmonized standards (EN’S) as a "
               "method of satisfying the essential requirements, by their "
               "approval by publication in the European Journal⁷. "
               "Unfortunately, it has been realized that the second editions "
               "of these current Standards do not necessarily satisfy the "
               "essential requirements and the Standards writing body, the "
               "Centre Europeen de Normalization Electrique (CENELEC), has "
               "been remitted to produce third editions which do in general, "
               "in 1997. This means that the new Directive⁵ cannot be "
               "practically introduced until some time in 1997, and in the "
               "meantime the older Directive² will remain the only vehicle by "
               "which the Distinctive Community Mark can be awarded. "
               "Unfortunately, this Directive still refers to the first "
               "editions of the harmonized Standards and the second editions, "
               "now current, will not permit the use of the mark. Urgent "
               "action is being taken to introduce the second editions of the "
               "harmonized Standards into 76/117/EEC² but until that time "
               "certification in accordance with that Directive will be in "
               "line with the first editions."))
    b.append(note("<b>Note on ‘European Journal⁷’.</b> The body text prints "
                  "the italic phrase 'European Journal⁷' with footnote marker "
                  "⁷, whereas reference 7 is titled 'Official Journal of the "
                  "European Communities'. Both printed forms are preserved "
                  "here and are not reconciled."))
    b.append(note("<b>Note on 'in general, in 1997'.</b> The phrase 'third "
                  "editions which do in general, in 1997' is printed verbatim "
                  "in the sentence about the CENELEC remit. The wording and "
                  "the commas are retained rather than being rewritten."))
    b.append(note("<b>Note on the CENELEC expansion as printed.</b> The print "
                  "reads 'Centre Europeen de Normalization Electrique "
                  "(CENELEC)' — without French accents and with the US spelling "
                  "'Normalization'. It is reproduced verbatim and has not been "
                  "corrected to 'Normalisation'."))
    b.append(p("While this seems to be a problem, it is not really, since the "
               "second editions do not vary widely from the first, and most "
               "equipment manufacturers are ensuring that their equipment "
               "will comply with both until the new Directive⁵ comes into "
               "force. When this Directive⁵ is enacted the third editions of "
               "the harmonized Standards will exist, and any equipment "
               "certified after that will comply to the new provisions."))

    # --- 7.5.1 ------------------------------------------------------------
    b.append(h4("7.5.1 Zone 0 and/or Zone 1 compatible apparatus for gases, "
                "vapours and mists",
                "7.5.1 Zone 0 and/or Zone 1 compatible apparatus for gases, "
                "vapours and mists"))
    b.append(p("As already stated, there is a long world-wide history of "
               "utilizing only third-party certified equipment in Zone 0 and "
               "1 and in some countries this is required by law. At the moment "
               "this is not the case in the UK, but the new Explosive "
               "Atmosphere Directive⁵ from the EU will effectively ensure this "
               "by requiring that all equipment marketed in the EU complies "
               "with it (the Directive itself requiring third-party type "
               "certification as a minimum). While this will cause some "
               "restriction in the UK the impact will not be great, as "
               "industry in the UK has historically used only third-party "
               "certified equipment by choice. Therefore, subject to the "
               "resolution of the difficulties already identified in this "
               "chapter, the situation will not change greatly."))
    b.append(p("What this historic situation has led to is a very high degree "
               "of detailed construction Standards which have become more and "
               "more international due to the international level of operation "
               "of the industry which needs the equipment. The current "
               "situation is that the Standards for electrical equipment "
               "intended generally for Zone 0 or Zone 1 (or both) are fully "
               "harmonized European Standards, and within the next 10 years "
               "will become fully harmonized International Standards. There "
               "are, however, historic national and European Standards which "
               "address this area and equipment is still available complying "
               "with these Standards. There is no suggestion that, in general, "
               "such equipment is not still safely usable in many "
               "circumstances, and the titles of those Standards are referred "
               "to in Chapters 8 to 15. Many of those standards are, however, "
               "obsolete or withdrawn and they should not be used for "
               "construction of new equipment. Where equipment complying with "
               "both current and historic Standards is available, the "
               "equipment to the current standards is always preferable."))
    b.append(p("The relatively large number of methods by which electrical "
               "equipment may be protected has meant that a large number of "
               "Standards exist, and it has been recognized that many of the "
               "requirements of these standards are common. The "
               "standardization structure is therefore to have a general "
               "Standard and a series of additional Standards which refer to "
               "the general Standard for many of their requirements, but "
               "contain additional requirements particular to the method used "
               "to protect the equipment. These are all European Standards "
               "and are structured as follows."))

    # --- BS/EN 50014 (1993) block -----------------------------------------
    b.append(p("<b>BS/EN 50014 (1993) – General requirements (see Chapter 8)</b>"))
    b.append(p("This is the general or common Standard and contains any "
               "requirements which apply to more than one of the specific "
               "methods of protection. Its requirements apply to all of the "
               "protection concepts (with the current exception of ‘n’), "
               "unless they are specifically excluded and should be read in "
               "conjunction with all of the following individual protection "
               "concept Standards. It is currently at its second edition stage "
               "which should supersede the first edition, but equipment "
               "certified in accordance with this and one of the subsidiary "
               "protection concept Standards cannot, as already described, "
               "bear the Distinctive Community Mark referred to in Chapter 1, "
               "unless it also satisfies the first edition of the Standard. "
               "Therefore, it will not have free access to EU Member States "
               "(and EFTA States)."))
    b.append(p("This, as already identified, is because Directive 76/117/EEC² "
               "currently refers to the first edition and the mark is "
               "controlled by the Directive, not the Standard. Again, as "
               "already identified, work is in hand to modify 76/117/EEC² and "
               "it is expected to allow the use of the second editions of "
               "this, and its subsidiary Standards, for equipment relating to "
               "the Directive in late 1996. A further complication which is "
               "preventing the activating of the new Directive⁵ is the fact "
               "that there appear to be discrepancies between the second "
               "editions of these Standards and the essential requirements "
               "given in the new Directive. (As already stated, all new "
               "approach Directives carry the essential safety requirements "
               "within them, unlike their older counterparts which referred "
               "to Standards). This means that third editions of These "
               "standards will need to be produced and the production is "
               "expected to be complete in late 1997. When published, "
               "equipment complying with the third editions of these Standards "
               "will be deemed to comply with the Directive and will "
               "consequently be able to carry the ‘Distinctive Community "
               "Mark’ in accordance with the Directive’s provisions. The need "
               "for continuing with the older Directive, 76/117/EEC², will "
               "then cease to exist for new equipment, although the older "
               "equipment will continue to be acceptable until the beginning "
               "of the twenty-first century (see Chapter 1)."))
    b.append(note("<b>Note on the capital 'These'.</b> The printed sentence "
                  "'This means that third editions of These standards will "
                  "need to be produced' capitalizes 'These' in mid-sentence. "
                  "That capitalisation is retained verbatim above and has not "
                  "been silently corrected."))
    return "".join(b)
