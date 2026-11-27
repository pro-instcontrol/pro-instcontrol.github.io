# -*- coding: utf-8 -*-
"""Chapter 7, module B - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas* (1998),
printed pp. 167-169 (PDF pp. 188-190): sections 7.2.1 to 7.2.5, the
protection concepts following the 7.2 opening. Continues directly
after module A. Unofficial study translation; the integration module
owns the page shell and end matter.
"""
from mcmillan_common import h4, p, note


def body_vi():
    b = []
    b.append(h4("7.2.1 Loại trừ môi trường nổ (tiêu chí a)",
                "7.2.1 Exclusion of the explosive atmosphere (criterion a)"))
    b.append(p("Đã phát triển ba phương pháp nhằm đáp ứng yêu cầu này trong việc "
               "chế tạo thiết bị điện bảo vệ chống nổ, và cả ba đều đang được sử "
               "dụng phổ biến hiện nay. Đó là ngâm các mạch điện trong dầu, bọc "
               "kín các mạch điện, và cấp áp cho vỏ bọc chứa các mạch điện bằng "
               "khí không dễ cháy."))
    b.append(p("<b>Ngâm trong dầu (ký hiệu ‘o’).</b> Trong khái niệm bảo vệ "
               "(loại hình bảo vệ) này, các linh kiện điện được ngâm trong dầu "
               "bên trong vỏ bọc của chúng, nhờ đó ngăn không cho môi trường có "
               "khả năng gây nổ tiếp cận. Nội dung này được trình bày chi tiết "
               "trong Chương 9. Có những hạn chế về loại dầu được phép dùng và "
               "các yêu cầu nhằm bảo đảm dầu luôn được giữ chắc bên trong vỏ, "
               "để các mạch điện luôn được ngâm trong dầu. Kỹ thuật này hiện "
               "được coi là phù hợp chỉ cho Vùng 2 tại Vương quốc Anh, nhưng "
               "được dùng ở những khu vực nguy hiểm hơn tại các quốc gia khác. "
               "Tình hình này nhiều khả năng sẽ thay đổi trong tương lai không "
               "xa (xem Chương 9), khi đó nó sẽ là khái niệm bảo vệ được phép "
               "dùng cho Vùng 1."))
    b.append(p("<b>Bọc kín, hay đóng gói (ký hiệu ‘m’).</b> Khái niệm bảo vệ này "
               "được trình bày chi tiết trong Chương 9. Một lần nữa, môi trường "
               "có khả năng gây nổ và các mạch điện được tách biệt nhau, lần này "
               "bằng vật liệu bọc kín (đóng gói). Các loại vật liệu được sử dụng "
               "được quy định rõ, và khối được bọc kín được sắp xếp sao cho các "
               "bề mặt hướng ra ngoài đủ cứng để tạo nên sự bảo vệ. Kỹ thuật này "
               "được coi là phù hợp cho cả Vùng 1 và 2."))
    b.append(p("<b>Cấp áp khí (ký hiệu ‘p’).</b> Khái niệm bảo vệ này được trình "
               "bày chi tiết trong Chương 11. Trong kỹ thuật này, môi trường có "
               "khả năng gây nổ bị giữ ở bên ngoài vỏ bọc thiết bị nhờ áp suất "
               "của không khí hoặc khí trơ. Không khí thường được dùng vì khí trơ "
               "gây nguy cơ ngạt thở. Vì sự bảo vệ được thực hiện bằng một chất "
               "khí (không khí), gần như luôn cần có thiết bị phụ trợ để bảo đảm "
               "áp suất không khí được duy trì bất chấp những rò rỉ nhỏ gần như "
               "chắc chắn sẽ xảy ra. Vì lý do đó, kỹ thuật này gần như luôn đòi "
               "hỏi một hệ thống điều khiển áp suất, cùng với một hệ thống xả "
               "(purge) để bảo đảm khi khởi động mọi môi trường nổ bên trong được "
               "loại bỏ; điều này tạo ra sự phức tạp tăng thêm, phải được cân "
               "nhắc so với tính linh hoạt tăng thêm nhờ việc dễ dàng giảm áp để "
               "sửa chữa. Kỹ thuật này được coi là phù hợp cho cả Vùng 1 và 2, "
               "hoặc chỉ cho Vùng 2, tùy theo hệ thống điều khiển áp suất được "
               "sử dụng."))
    b.append(note(
        "<b>Đặc điểm in ấn — chữ ‘o’, không phải số không.</b> Ký hiệu ngâm "
        "trong dầu được in là chữ cái thường ‘o’ đặt trong dấu nháy đơn cong; "
        "lớp văn bản của PDF lại đọc nhầm thành chữ số không. Trang in kiểm "
        "chứng rõ đây là chữ cái. Tất cả các ký hiệu bảo vệ được giữ nguyên với "
        "dấu nháy đơn cong: ‘o’, ‘m’, ‘p’, ‘e’, ‘d’, ‘q’, ‘i’, ‘ia’, ‘ib’, ‘s’."))
    b.append(h4("7.2.2 Ngăn ngừa phát tia lửa (tiêu chí b)",
                "7.2.2 Prevention of sparking (criterion b)"))
    b.append(p("Trong lĩnh vực này chỉ có một khái niệm bảo vệ chính thức phù "
               "hợp cho cả Vùng 1 và 2."))
    b.append(p("<b>An toàn tăng cường (ký hiệu ‘e’).</b> Khái niệm bảo vệ này "
               "được trình bày chi tiết trong Chương 12. Kỹ thuật này chấp nhận "
               "rằng có năng lượng có khả năng bắt lửa bên trong thiết bị, nhưng "
               "dựa vào chất lượng chế tạo để bảo đảm năng lượng đó không được "
               "giải phóng theo cách có thể gây bắt lửa. Điều này đạt được nhờ "
               "chất lượng chế tạo của thiết bị. Kỹ thuật này được coi là phù "
               "hợp cho cả Vùng 1 và 2."))
    b.append(h4("7.2.3 Chứa ngăn vụ nổ (tiêu chí c)",
                "7.2.3 Containment of explosions (criterion c)"))
    b.append(p("Có hai khái niệm bảo vệ sử dụng kỹ thuật này."))
    b.append(p("<b>Thiết bị chống nổ (ký hiệu ‘d’).</b> Đây là kỹ thuật bảo vệ "
               "lâu đời nhất. Môi trường có khả năng gây nổ được cho phép đi vào "
               "bên trong vỏ bọc thiết bị và bị các linh kiện bên trong bắt lửa. "
               "Tuy nhiên, thiết bị được trang bị một vỏ bọc đặc biệt rất chắc "
               "chắn, có thể chịu được vụ nổ bên trong mà không bị hư hại, và "
               "thêm vào đó sẽ ngăn không cho ngọn lửa sinh ra từ vụ nổ bên "
               "trong thoát ra ngoài theo cách có thể bắt lửa bất kỳ môi trường "
               "nổ bao quanh nào. Kỹ thuật này được coi là phù hợp cho cả Vùng 1 "
               "và 2."))
    b.append(p("<b>Lấp đầy bằng bột trơ (ký hiệu ‘q’).</b> Ở đây vỏ bọc thiết bị "
               "được lấp đầy bằng thạch anh, cát hoặc một loại vật liệu trơ tương "
               "tự dạng hạt nhỏ. Kỹ thuật này là sự mở rộng của một kỹ thuật cũ "
               "dùng buồng đá để ngăn ngọn lửa đi ngược lên ống dẫn. Những buồng "
               "đó có tác dụng dập tắt ngọn lửa, hoặc ít ra là người ta từng "
               "nghĩ vậy. Vật liệu lấp đầy không ngăn được môi trường nổ tiếp "
               "cận thiết bị và đến gần nguồn bắt lửa. Tuy nhiên, vật liệu dạng "
               "hạt mịn có tác dụng dập tắt mọi sự bắt lửa, từ đó ngăn ngừa vụ "
               "nổ. Kỹ thuật này được coi là phù hợp chỉ cho Vùng 2 tại Vương "
               "quốc Anh, nhưng được dùng ở những khu vực nguy hiểm hơn tại các "
               "quốc gia khác, và dự kiến sẽ được chấp nhận cho Vùng 1 tại "
               "Vương quốc Anh trong tương lai không xa (xem Chương 9)."))
    b.append(note(
        "<b>Đặc điểm in ấn — ký hiệu ‘d’ của thiết bị chống nổ.</b> Lớp văn bản "
        "của PDF đọc ký hiệu này với một chữ I hoa thừa đứng trước chữ d; "
        "trang in cho thấy rõ đây là chữ cái thường ‘d’ đứng riêng. Tiêu đề được "
        "giữ nguyên là Thiết bị chống nổ (ký hiệu ‘d’). Trang in cũng xác nhận "
        "cụm từ hoặc ít ra là người ta từng nghĩ vậy trong đoạn lấp đầy bằng "
        "bột trơ; cụm này được giữ nguyên, không được sửa lại."))
    b.append(h4("7.2.4 Hạn chế năng lượng (tiêu chí d)",
                "7.2.4 Energy limitation (criterion d)"))
    b.append(p("Trong lĩnh vực này chỉ có một khái niệm bảo vệ, nhưng đó là khái "
               "niệm bảo vệ đưa mức an toàn cao nhất."))
    b.append(p("<b>An toàn nội tại (ký hiệu ‘i’).</b> Trong kỹ thuật này, năng "
               "lượng điện cấp cho thiết bị thấp hơn mức sẽ gây bắt lửa nếu được "
               "giải phóng dưới dạng tia lửa hoặc bề mặt nóng, và mọi sự tích trữ "
               "năng lượng trong thiết bị được kiểm soát chặt chẽ để bảo đảm "
               "năng lượng tích trữ bị giới hạn. Cũng như cấp áp khí, thiết bị "
               "này phụ thuộc rất nhiều vào thiết bị khác cấp điện cho nó, và kỹ "
               "thuật này tương đối phức tạp. Nó cũng bị giới hạn trong phạm vi "
               "thiết bị đo vì những hạn chế về năng lượng áp đặt, nhưng trong "
               "giới hạn đó lại rất linh hoạt."))
    b.append(p("Có hai cấp độ an toàn nội tại: cấp cao hơn ‘ia’ phù hợp cho Vùng "
               "0, Vùng 1 và Vùng 2, trong khi cấp thấp hơn ‘ib’ chỉ giới hạn "
               "cho Vùng 1 và Vùng 2."))
    b.append(h4("7.2.5 Các tình huống đặc biệt",
                "7.2.5 Special situations"))
    b.append(p("Mặc dù các phương pháp bảo vệ thiết bị nêu trong các Mục 7.2.1 "
               "đến 7.2.4 bao phủ hầu hết các tình huống thường gặp, vẫn có thêm "
               "một loại hình bảo vệ dùng cho những nơi mà các loại đã mô tả "
               "không phù hợp do những tiến bộ công nghệ hoặc do hoàn cảnh đặc "
               "biệt."))
    b.append(p("<b>Bảo vệ đặc biệt (ký hiệu ‘s’).</b> Bảo vệ đặc biệt không phải "
               "là một loại hình bảo vệ cố định như các loại nêu trên, mà được "
               "dùng để mô tả thiết bị phù hợp sử dụng trong môi trường có khả "
               "năng gây nổ trên cơ sở loại hình bảo vệ riêng của nó tương đương "
               "với một trong những loại cổ điển hơn, dù có khác biệt. Cách dùng "
               "điển hình của nó là cho phép các tiến bộ công nghệ mà không dễ "
               "xếp vào các loại hình bảo vệ tiêu chuẩn. Nó đã được dùng điển "
               "hình cho thiết bị được bọc kín ‘m’ trước khi công bố Tiêu chuẩn "
               "chế tạo cho loại hình bảo vệ đó, và cho các bộ ngăn ngọn lửa "
               "thiêu kết trước khi những thứ này được đưa vào loại hình bảo vệ "
               "‘d’ (vỏ chống nổ). Nó cũng được dùng khi áp dụng các kỹ thuật "
               "trái với tiêu chuẩn hiện hành, chẳng hạn ống bi-pin trong bộ "
               "đèn huỳnh quang loại ‘e’ (an toàn tăng cường), trên cơ sở an "
               "toàn tương đương. Nó cũng có thể được dùng khi thiết bị có hai "
               "loại hình bảo vệ độc lập, mỗi loại tự thân hoàn chỉnh (ví dụ, "
               "một buồng đầu cuối an toàn tăng cường ‘e’ đặt trong một vỏ "
               "chống nổ), với điều kiện hai khái niệm bảo vệ đó độc lập với "
               "nhau. Cách tiếp cận sau cùng này, tuy nhiên, phải được xử lý "
               "thận trọng."))
    b.append(p("Thiết bị loại ‘s’ được sử dụng theo quy định riêng trong từng "
               "trường hợp cụ thể, và chỉ được dùng ở Vùng 0 và 1 khi có nêu rõ "
               "điều đó."))
    b.append(note(
        "<b>Đặc điểm in ấn — sự khác biệt về mức phù hợp theo Vùng.</b> Cách "
        "diễn đạt về mức phù hợp được giữ nguyên như in: ‘o’ hiện chỉ phù hợp "
        "cho Vùng 2 tại Vương quốc Anh nhưng dự kiến sẽ trở thành khái niệm "
        "được phép dùng cho Vùng 1; ‘q’ cũng chỉ dành cho Vùng 2 tại Vương quốc "
        "Anh, với Vùng 1 dự kiến về sau; ‘m’, ‘e’ và ‘d’ phù hợp cho cả Vùng 1 "
        "và 2; ‘p’ phù hợp cho cả Vùng 1 và 2 hoặc chỉ Vùng 2 tùy vào hệ thống "
        "điều khiển áp suất; cấp cao hơn ‘ia’ bao phủ Vùng 0, Vùng 1 và Vùng 2 "
        "trong khi cấp thấp hơn ‘ib’ chỉ giới hạn ở Vùng 1 và 2; còn ‘s’ được "
        "dùng theo quy định riêng trong từng trường hợp, và chỉ dùng được ở "
        "Vùng 0 và 1 khi được nêu rõ. Những khác biệt này được giữ nguyên như "
        "in, không được thống nhất lại."))
    return "".join(b)


def body_en():
    b = []
    b.append(h4("7.2.1 Exclusion of the explosive atmosphere (criterion a)",
                "7.2.1 Exclusion of the explosive atmosphere (criterion a)"))
    b.append(p("Three methods of satisfying this requirement in the construction "
               "of explosion-protected apparatus have been developed and are in "
               "general current use. These are immersion of the electrical "
               "circuits in oil, encapsulation of the electrical circuits, and "
               "pressurization of the enclosure containing the electrical "
               "circuits with non-flammable gas."))
    b.append(p("<b>Oil immersion (symbol ‘o’).</b> In this protection concept "
               "(type of protection) the electrical components are immersed in "
               "oil within their enclosure, thus preventing access of the "
               "explosive atmosphere. It is dealt with in detail in Chapter 9. "
               "There are limitations on the type of oil which may be used and "
               "requirements to ensure the security of the oil within the "
               "enclosure, so that the electrical circuits remain immersed. The "
               "technique is considered as suitable for Zone 2 only, at present, "
               "within the UK but is used in more hazardous areas in other "
               "countries. This is likely to change in the not-too-distant "
               "future (see Chapter 9) and will be the protection concept "
               "permitted in Zone 1."))
    b.append(p("<b>Encapsulation (symbol ‘m’).</b> This protection concept is "
               "dealt with in detail in Chapter 9. Again, the explosive "
               "atmosphere and electrical circuits are separated from one "
               "another, this time by encapsulating (potting) material. The "
               "types of material used are defined and the encapsulated block "
               "is arranged so that surfaces presented to the outside are hard "
               "enough to give protection. The technique is considered as "
               "suitable for both Zone 1 and 2."))
    b.append(p("<b>Pressurization (symbol ‘p’).</b> This protection concept is "
               "dealt with in detail in Chapter 11. In this technique the "
               "explosive atmosphere is kept out of the equipment enclosure by "
               "pressure of air or inert gas. Air is normally used as there are "
               "asphyxiation problems with inert gas. Because the protection is "
               "by a gas (air) it is almost always necessary to provide "
               "ancillary equipment to ensure that the air pressure is "
               "maintained in spite of small leakages, which are almost certain "
               "to occur. Because of this the technique almost always requires "
               "a pressure-control system, together with a purge system to "
               "ensure that on start-up any internal explosive atmosphere is "
               "removed, and this gives added complication which must be set "
               "against its added flexibility because of the ease of "
               "depressurizing for repair. The technique is considered as "
               "suitable for both Zone 1 and 2 or only Zone 2, depending upon "
               "the pressure-control systems used."))
    b.append(note(
        "<b>Printed quirk — the letter ‘o’, not the digit zero.</b> The "
        "oil-immersion symbol is a lowercase letter ‘o’ inside curly quotes; "
        "the PDF text layer reads it as the digit zero. The rendered page "
        "confirms the letter form. All protection symbols are preserved here "
        "with curly single quotes: ‘o’, ‘m’, ‘p’, ‘e’, ‘d’, ‘q’, ‘i’, ‘ia’, "
        "‘ib’, ‘s’."))
    b.append(h4("7.2.2 Prevention of sparking (criterion b)",
                "7.2.2 Prevention of sparking (criterion b)"))
    b.append(p("There is only one formal protection concept which is suitable "
               "for both Zone 1 and 2 in this area."))
    b.append(p("<b>Increased safety (symbol ‘e’).</b> This protection concept "
               "is dealt with in detail in Chapter 12. The technique accepts "
               "that there is ignition-capable energy within the equipment but "
               "relies upon the quality of construction to ensure that the "
               "energy is not released in a way which could cause ignition. "
               "This is achieved by the quality of construction of the "
               "equipment. The technique is considered as suitable for both "
               "Zone 1 and 2."))
    b.append(h4("7.2.3 Containment of explosions (criterion c)",
                "7.2.3 Containment of explosions (criterion c)"))
    b.append(p("There are two protection concepts which use this technique."))
    b.append(p("<b>Flameproof equipment (symbol ‘d’).</b> This is the oldest "
               "protection technique. The explosive atmosphere is permitted to "
               "enter the equipment enclosure and to be ignited by the "
               "components within. The equipment is, however, provided with a "
               "very special strong enclosure which will withstand the internal "
               "explosion without sustaining damage and, in addition, will "
               "prevent the flames associated with the internal explosion from "
               "exiting the enclosure in a way which would permit them to "
               "ignite any surrounding explosive atmosphere. The technique is "
               "considered as suitable for both Zone 1 and 2."))
    b.append(p("<b>Powder filling (symbol ‘q’).</b> Here the equipment enclosure "
               "is filled with quartz, sand or some similar inert small-grained "
               "filling. The technique is an extension of an old technique "
               "involving the use of stone chambers to prevent the passage of "
               "flame up-ducting. These chambers served to quench the flame, or "
               "so it was thought. The filling does not prevent the explosive "
               "atmosphere from accessing the equipment and coming into the "
               "proximity of a source of ignition. The fine-grained filling, "
               "however, serves to quench any ignition, thus preventing an "
               "explosion. The technique is considered as suitable for Zone 2 "
               "only in the UK, but is used in more hazardous areas in other "
               "countries and is expected to be acceptable for use in Zone 1 in "
               "the UK in the not-too-distant future (see Chapter 9)."))
    b.append(note(
        "<b>Printed quirk — the flameproof symbol ‘d’.</b> The PDF text layer "
        "renders the heading symbol with a stray capital I before the d, "
        "but the rendered page shows the lowercase letter ‘d’ alone. The "
        "heading is preserved here as Flameproof equipment (symbol ‘d’). The "
        "same page confirms the phrase or so it was thought in the powder-filling "
        "paragraph; the wording is retained verbatim."))
    b.append(h4("7.2.4 Energy limitation (criterion d)",
                "7.2.4 Energy limitation (criterion d)"))
    b.append(p("There is only one protection concept in this area but it is the "
               "protection concept offering the highest level of security."))
    b.append(p("<b>Intrinsic safety (symbol ‘i’).</b> In this technique the "
               "electrical energy fed to the equipment is below that which will "
               "cause ignition if released in a spark or as a hot surface, and "
               "all energy storage in the equipment is closely controlled to "
               "ensure that stored energy is limited. As with pressurization, "
               "this equipment relies to a large extent upon other equipment, "
               "which feeds it with electricity, and the technique is somewhat "
               "complex. It is also limited in its application to instrumentation "
               "because of the energy limitations imposed, but within this "
               "limitation it is very flexible."))
    b.append(p("There are two grades of intrinsic safety, the higher grade ‘ia’ "
               "being suitable for Zone 0, Zone 1 and Zone 2, but the lower "
               "grade ‘ib’ being limited to Zone 1 and Zone 2."))
    b.append(h4("7.2.5 Special situations",
                "7.2.5 Special situations"))
    b.append(p("While the methods of equipment protection given in Sections "
               "7.2.1 to 7.2.4 cover most situations normally encountered, there "
               "is an additional type of protection for use where the types "
               "already described are not appropriate because of advances in "
               "technology or special circumstances."))
    b.append(p("<b>Special protection (symbol ‘s’).</b> Special protection is "
               "not a fixed type of protection, as in the above, but is used to "
               "describe equipment which is suitable for use in explosive "
               "atmospheres on the basis that its individual type of protection "
               "is equivalent to one of the more classic types, although "
               "different. Its typical use is to permit advances in technology "
               "where such advances do not easily fit into standard types of "
               "protection. It has been typically used for encapsulated "
               "equipment ‘m’ prior to the publication of the construction "
               "Standard for that type of protection, and for sintered flame "
               "arresters prior to those being included in type of protection "
               "‘d’ (flameproof enclosure). It has also been used where "
               "techniques contrary to existing standards such as bi-pin tubes "
               "in type ‘e’ (increased safety) fluorescent fittings are used on "
               "the basis of equivalent safety. It can also be used where "
               "equipment which has two independent types of protection, each "
               "of which is complete in itself (e.g., an increased safety ‘e’ "
               "terminal chamber in a flameproof enclosure), is used provided "
               "that the two protection concepts are each independent of the "
               "other. This latter approach must, however, be treated with "
               "caution."))
    b.append(p("Type ‘s’ equipment is usable as specified in each particular "
               "case, and is only usable in Zone 0 and 1 where this is "
               "specifically stated."))
    b.append(note(
        "<b>Printed distinctions — Zone suitability by protection concept.</b> "
        "The suitability wording is retained exactly: ‘o’ is suitable for Zone "
        "2 only at present in the UK but is expected to become the concept "
        "permitted in Zone 1; ‘q’ is likewise Zone 2 only in the UK with Zone 1 "
        "expected later; ‘m’, ‘e’ and ‘d’ are suitable for both Zone 1 and 2; "
        "‘p’ is suitable for both Zone 1 and 2 or only Zone 2 depending upon "
        "the pressure-control systems used; the higher grade ‘ia’ covers Zone "
        "0, Zone 1 and Zone 2 while the lower grade ‘ib’ is limited to Zone 1 "
        "and 2; and ‘s’ is usable as specified in each particular case, being "
        "usable in Zone 0 and 1 only where this is specifically stated. These "
        "distinctions are printed as given and are not harmonised."))
    return "".join(b)
