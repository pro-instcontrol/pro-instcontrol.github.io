# -*- coding: utf-8 -*-
"""Chapter 17, module C - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 497-501 (PDF pp. 518-522).

Covers the Zone 22 (Zone Y) list with all nine items, 17.4 (Selection of
conduit or cable systems), 17.4.1 (Zones 0/20, Cables and Conduits),
17.4.2 (Zones 1/21, with both non-intrinsically-safe and intrinsically-safe
cable requirements and all numbered items) and 17.4.3 (Zones 2/22).

The module stops at the end of the 17.4.3 paragraph on printed p.501; the
printed `References` heading and all ten references on printed p.502 belong
to the chapter shell and are not emitted here. No figures, no tables and no
`eq()` blocks are emitted. Printed quirks are kept verbatim in the English
text and flagged with bilingual notes; the Vietnamese follows the intended
meaning. This is an unofficial study translation; the source PDF is not
republished.
"""
from mcmillan_common import h3, h4, p, note, ol


def body_vi():
    b = []

    # ---- printed p.497: Zone 22 (Zone Y), lead-in and items 1-9 (C1-C11).
    b.append(h4("Vùng 22 (Vùng Y)", "Zone 22 (Zone Y)"))
    b.append(p("Đây lại là khu vực ít nguy hiểm nhất trong số các khu vực "
               "nguy hiểm liên quan đến bụi, có mức rủi ro tương tự như Vùng "
               "2. Tính phù hợp của thiết bị phản ánh điều này như sau:"))
    b.append(ol([
        "Thiết bị phù hợp cho Vùng 20 nhìn chung cũng phù hợp cho Vùng 22 "
        "(Vùng Y).",
        "Thiết bị phù hợp cho Vùng 21 (Vùng Z) nhìn chung cũng phù hợp cho "
        "Vùng 22 (Vùng Y).",
        "Thiết bị phù hợp với BS 6467, Phần 1⁴ (Xem Chương 15) với vỏ bọc ít "
        "nhất là IP5X, với điều kiện bụi không dẫn điện.",
        "Thiết bị ngâm dầu ‘o’ (xem các Chương 9 và 15) với vỏ bọc ít nhất "
        "IP5X, với điều kiện bụi không dẫn điện và bụi không gây làm hư hỏng "
        "dầu.",
        "Thiết bị tạo áp ‘p’ (xem các Chương 11 và 15), với điều kiện vỏ bọc "
        "là IP5X (không tính các lối xả) và bụi không dẫn điện. Hành động "
        "thực hiện khi mất áp nên ít nhất tương đương với yêu cầu ở Vùng 2.",
        "Thiết bị nhồi bột ‘q’ (xem các Chương 9 và 15), với điều kiện vỏ bọc "
        "ít nhất là IP5X và bụi không dẫn điện.",
        "Vỏ chống cháy ‘d’ (xem các Chương 10 và 15), với điều kiện vỏ bọc "
        "của nó ít nhất là IP5X và bụi không dẫn điện.",
        "Thiết bị an toàn tăng cường ‘e’ (xem các Chương 12 và 15), với điều "
        "kiện vỏ bọc của nó ít nhất là IP5X và bụi không dẫn điện.",
        "Mạch an toàn nội tại ‘ia’ hoặc ‘ib’ (xem các Chương 13 và 15), với "
        "điều kiện vỏ bọc của thiết bị ít nhất là IP5X và bụi không dẫn điện. "
        "Thiết bị an toàn nội tại ‘ib’ cũng được chấp nhận nếu vỏ bọc không "
        "đạt IP5X, với điều kiện thiết bị được đánh giá lại với giả định rằng "
        "mọi bộ phận dẫn điện không được phủ, bọc kín hoặc cách điện có thể "
        "được nối với nhau. Cách tiếp cận này cũng được chấp nhận đối với bụi "
        "dẫn điện.",
    ]))
    b.append(note("<b>Ghi chú về các mục trong danh sách Vùng 22.</b> Bản in "
                  "viết mục 3 là ‘(See Chapter 15)’ với chữ ‘S’ viết hoa, "
                  "khác với các dạng ‘see Chapter’ khác; mục 4 dùng chữ cái "
                  "‘o’ trong ‘Oil-immersed apparatus’ (OCR đọc là chữ số 0); "
                  "mục 7 viết ‘Flameproof enclosure ‘d’’ – ký hiệu đúng, "
                  "khác với mục 6 trên trang in 496 viết ‘p’; và mục 5 viết "
                  "‘provided the enclosure is IP5X’ mà bỏ qua cụm ‘at least’. "
                  "Bản tiếng Anh giữ nguyên, bản tiếng Việt theo nghĩa đúng."))

    # ---- 17.4, opening paragraph, joined across printed 497/498 (C13+C14).
    b.append(h3("17.4 Lựa chọn hệ thống ống dẫn hoặc cáp",
                "17.4 Selection of conduit or cable systems"))
    b.append(p("Cáp dùng để liên kết thiết bị trong khu vực nguy hiểm với "
               "thiết bị trong khu vực không nguy hiểm, và các thiết bị khác "
               "nhau trong khu vực nguy hiểm, phải chịu về cơ bản cùng một "
               "yêu cầu dù chúng liên quan đến rủi ro khí/hơi/sương mù hay "
               "rủi ro bụi. Hai đặc tính của cáp là quan trọng, cụ thể là mức "
               "đầy đủ của nó về các ứng suất điện (điện áp và dòng điện, kể "
               "cả sự tăng nhiệt phát sinh) và mức đầy đủ của chúng đối với "
               "môi trường (nhiệt, lạnh, độ ẩm, hóa chất trong không khí, "
               "v.v.). Các yêu cầu nêu ở đây phù hợp với môi trường ngoài "
               "trời bình thường nhưng bất kỳ tình huống bất thường nào "
               "(chẳng hạn như sự hiện diện của nồng độ dung môi bất thường "
               "cao trong khí quyển, v.v.) cần được giải quyết riêng về vật "
               "liệu chế tạo và vị trí lắp đặt cáp, mục tiêu là đạt ít nhất "
               "cùng mức độ an toàn mà các khuyến nghị nêu ở đây sẽ đạt được "
               "trong một môi trường công nghiệp bình thường."))

    # ---- printed p.498: 17.4.1, Zones 0/20 (C15-C20).
    b.append(h3("17.4.1 Vùng 0 và Vùng 20",
                "17.4.1 Zone 0 and Zone 20"))
    b.append(p("Khái niệm bảo vệ tiêu chuẩn duy nhất phù hợp để dùng ở Vùng "
               "0 và Vùng 20 là an toàn nội tại ở hạng cao hơn ‘ia’. Dạng "
               "bảo vệ này dựa trên giả định rằng mức năng lượng trong khu "
               "vực nguy hiểm là không gây cháy, do đó các yêu cầu đối với "
               "hệ thống cáp và ống dẫn là tối thiểu và chỉ là những yêu cầu "
               "cần thiết trong một lắp đặt bình thường không có khu vực "
               "nguy hiểm. Tương tự, trong trường hợp dùng ống dẫn thì chỉ "
               "cần đáp ứng các yêu cầu công nghiệp cơ bản."))
    b.append(p("Tuy nhiên, trong cả hai trường hợp, cần giải quyết nhu cầu "
               "ngăn bầu khí quyển nổ xâm nhập vào khu vực không nguy hiểm "
               "qua cáp hoặc ống dẫn. Điều này thường yêu cầu bịt kín các "
               "ống dẫn nhưng có thể không yêu cầu bố trí bổ sung nào cho "
               "cáp, trừ khi cáp có các khe hở mở hoặc khi nó được nối với "
               "một thiết bị, chẳng hạn như bộ phát, có thể có bầu khí quyển "
               "nổ ở áp suất lớn hơn áp suất khí quyển bên trong. Các biện "
               "pháp phòng ngừa như vậy thường gồm bịt kín cáp hoặc ống dẫn, "
               "hoặc thông hơi chúng để ngăn sự truyền sang bất kỳ khu vực "
               "nào có thể bị ảnh hưởng bất lợi (khu vực không nguy hiểm hoặc "
               "khu vực có mức nguy hiểm thấp hơn)."))
    b.append(p("Trong những trường hợp đặc biệt, người ta dùng các lắp đặt "
               "không an toàn nội tại được bảo vệ đặc biệt, trong đó cáp "
               "hoặc ống dẫn có thể mang năng lượng rất dễ gây cháy và cần "
               "một cách tiếp cận hoàn toàn khác. Hư hỏng hoặc suy giảm của "
               "cáp hoặc của các dẫn bên trong ống dẫn có thể gây hậu quả "
               "nghiêm trọng hơn nhiều và do đó việc lựa chọn cáp hoặc hệ "
               "thống ống dẫn trở nên quan trọng hơn nhiều."))
    b.append(h4("Cáp", "Cables"))
    b.append(p("Đối với mạch an toàn nội tại, về mặt lịch sử không có yêu "
               "cầu tối thiểu nào ngoài các yêu cầu đối với cáp nhiều lõi "
               "chứa hơn một mạch an toàn nội tại và yêu cầu mỗi mạch phải "
               "nằm trong một màn chắn riêng (xem trong Chương 22). Sự ra "
               "đời của BS/EN 60079⁶ được đề xuất đã lần đầu tiên đưa vào "
               "các khuyến nghị cho các loại cáp này, theo đó cáp không được "
               "có dẫn hoặc sợi dẫn nào nhỏ hơn 0,1 mm đường kính và lớp "
               "cách điện phải phù hợp cho vận hành xoay chiều 500 V rms. "
               "Vì cần phải quy định điện cảm và điện dung của cáp, một lớp "
               "vỏ bọc tổng thể cũng là cần thiết để xác định vị trí của các "
               "dẫn. Có thể dùng cáp chứa hơn một mạch an toàn nội tại để "
               "mang các mạch đi vào Vùng 0, nhưng loại cáp đó phải sao cho "
               "mỗi mạch được chứa riêng trong một màn chắn có thể được nối "
               "vào hệ thống cân bằng thế (nối liên kết) để loại trừ sự nối "
               "liên kết giữa các mạch (xem trong Chương 22). Ngoài ra, cáp "
               "chỉ được chứa các mạch ‘ia’ và các màn chắn phải hoặc được "
               "cách điện với nhau, hoặc đều được nối vào hệ thống cân bằng "
               "thế (nối liên kết) tại cùng một điểm và tại cùng điểm với "
               "các mạch chứa bên trong chúng."))
    b.append(note("<b>Ghi chú về các cụm in trong đoạn cáp an toàn nội tại.</b> "
                  "Bản in viết ‘has, for the first time introduced "
                  "recommendations’ (dấu phẩy sau ‘has’, không có dấu phẩy "
                  "sau ‘time’), ‘(see in Chapter 22)’ hai lần với chữ ‘in’ "
                  "thừa, và ‘potential equalization’ dùng cách viết Mỹ với "
                  "chữ ‘z’, hai lần. Bản tiếng Anh giữ nguyên, bản tiếng Việt "
                  "theo nghĩa đúng."))

    # ---- printed p.499: four recommendations, Conduits (C21-C30).
    b.append(p("Trong những trường hợp đặc biệt, khi các mạch không an toàn "
               "nội tại được bảo vệ đặc biệt được lắp đặt ở Vùng 0, khả năng "
               "hư hỏng cáp giải phóng năng lượng gây cháy nghiêm trọng hơn "
               "nhiều. Ở đây giải pháp thực sự duy nhất là ngăn sự giải "
               "phóng ra ngoài của năng lượng đó, và cách tốt nhất để làm "
               "điều này là bảo đảm rằng cáp mang các đặc tính cần thiết để "
               "giảm thiểu rủi ro đó. Các khuyến nghị cơ bản cho loại cáp "
               "này sẽ như sau:"))
    b.append(ol([
        "Cáp nên có lớp cách điện nhiệt dẻo hoặc elastomer (hoặc cách điện "
        "bằng vật liệu đáp ứng các yêu cầu tương tự, chẳng hạn như cách "
        "điện khoáng trong cáp bọc kim loại) trên các lõi của nó, đủ cho "
        "sử dụng công nghiệp bình thường.",
        "Các lõi nên được chứa trong một lớp lót bằng vật liệu tương tự, trừ "
        "khi cáp được cách điện khoáng, khi đó lớp cách điện khoáng là đủ.",
        "Cáp nên được bọc lớp giáp bằng dây thép hoặc dây bện lên lớp lót "
        "của nó, trừ khi nó có vỏ kim loại liên tục, chẳng hạn như cáp cách "
        "điện khoáng bọc kim loại, để giảm thiểu rủi ro hư hỏng. Điều này "
        "cũng tạo ra một đoạn ngắn mạch bên trong cáp trong trường hợp hư "
        "hỏng, giúp giảm thiểu rủi ro hồ quang hoặc tia lửa bên ngoài cáp "
        "trước khi bảo vệ mạch tác động.",
        "Mọi cáp, kể cả loại có vỏ kim loại liên tục, nên được lắp một lớp "
        "vỏ bên ngoài bằng polyvinyl chloride (PVC), polyethylene clo-sunfat "
        "(CSP), polychloropren (PCP), polyethylene clo hóa (CSP) hoặc vật "
        "liệu tương tự để ngăn các sự cố tiếp đất tới lớp giáp dọc chiều "
        "dài cáp và bảo vệ cáp khỏi môi trường.",
    ]))
    b.append(note("<b>Ghi chú về cụm ‘(CSP)’ lặp lại.</b> Mục 4 in ‘chloro-"
                  "sulphinated polyethylene (CSP), polychloroprene (PCP), "
                  "chlorinated polyethylene (CSP)’ – ‘(CSP)’ xuất hiện hai "
                  "lần, lần thứ hai có lẽ đáng lẽ là ‘(CPE)’ – được giữ nguyên. "
                  "Các đoạn khác cũng in ‘Zone 0 or 20’ mà không lặp lại chữ "
                  "‘Zone’; bản tiếng Anh giữ nguyên."))
    b.append(p("Hầu hết các Tiêu chuẩn về cáp được bảo vệ bằng lớp giáp để "
               "dùng trong công nghiệp bình thường sẽ đáp ứng các yêu cầu "
               "này mà không cần áp dụng thêm các khái niệm bảo vệ nào."))
    b.append(p("Một khuyến nghị mới được đưa vào BS/EN 60079-14⁶ là tất cả "
               "cáp, trừ loại dùng trong rãnh lấp cát hoặc tương tự, cần "
               "được chế tạo từ vật liệu có thể đáp ứng các yêu cầu của IEC "
               "332, Phần 1⁸ về khả năng truyền ngọn lửa khi đang cháy. Dù "
               "điều này chưa được đưa vào các khuyến nghị quốc gia, nên giải "
               "quyết vấn đề này vì nó sẽ giảm thiểu rủi ro lan truyền đám "
               "cháy khắp một lắp đặt nếu đám cháy xảy ra bên trong."))
    b.append(note("<b>Ghi chú về các ký hiệu tiêu chuẩn.</b> Ở đây bản in viết "
                  "‘BS/EN 60079-14⁶’ với dấu gạch ngang thường và ‘IEC 332, "
                  "Part 1⁸’ có dấu phẩy; bản tiếng Anh giữ nguyên."))
    b.append(p("Rất khó có khả năng thiết bị cầm tay hoặc có thể di chuyển "
               "không an toàn nội tại được xem xét để dùng ở Vùng 0 hoặc 20, "
               "nhưng trong trường hợp ít có khả năng đó được xem xét thì "
               "không có sự nới lỏng nào đối với yêu cầu về cáp được coi là "
               "hợp lý và, thêm vào đó, ảnh hưởng của sự uốn cong đối với "
               "lớp giáp nên được xem xét cẩn thận để bảo đảm rằng gãy do "
               "uốn cong là khó xảy ra."))
    b.append(h4("Ống dẫn", "Conduits"))

    # ---- C30+C31, first Conduits paragraph joined across printed 499/500.
    b.append(p("Đối với mạch an toàn nội tại, yêu cầu duy nhất đối với ống "
               "dẫn là nó phải ràng buộc các dẫn được chứa bên trong sao cho "
               "các thông số có thể được xác định và nó phải được lắp một "
               "thiết bị ngăn để ngăn khí, hơi, sương mù hoặc bụi đi từ khu "
               "vực nguy hiểm này sang khu vực nguy hiểm khác hoặc sang khu "
               "vực không nguy hiểm. Ngoài ra, mỗi mạch an toàn nội tại riêng "
               "lẻ bên trong ống dẫn nên, như trong trường hợp cáp, được "
               "chứa trong một màn chắn riêng và các màn chắn đó nên đáp ứng "
               "các yêu cầu như đối với màn chắn cáp."))

    # ---- printed p.500: 17.4.2 and non-intrinsically-safe cables (C32-C42).
    b.append(p("Đối với các mạch khác, nên dùng ống dẫn kéo liền hoặc hàn "
               "đường hàn theo BS 4568⁹, hoặc ống dẫn kim loại hoặc nhựa dẻo "
               "có phân loại độ bền cơ học cao và một lớp vỏ nhựa tổng thể "
               "(xem BS 731, Phần 1¹⁰) để giảm thiểu khả năng hư hỏng và ngăn "
               "sự xâm nhập của bầu khí quyển nổ. Các hệ thống ống dẫn như "
               "vậy được yêu cầu lắp các thiết bị bịt kín được công nhận "
               "(hộp bịt) tại những vị trí mà các ống dẫn đó đi ra khỏi khu "
               "vực nguy hiểm để vào một khu vực ít nguy hiểm hơn hoặc khu "
               "vực không nguy hiểm."))
    b.append(note("<b>Ghi chú về các chỉ số tham chiếu và ‘eg.’.</b> Bản in "
                  "nâng các chỉ số tham chiếu trong ‘BS 4568⁹’ và ‘BS 731, "
                  "Phần 1¹⁰’, và viết ‘(eg., where the risk of mechanical "
                  "damage is high’ – ‘eg.’ có dấu phẩy, không có dấu chấm sau "
                  "chữ ‘g’. Bản tiếng Anh giữ nguyên cả ba."))
    b.append(p("Nếu có thể, nên lấp đầy ống dẫn bằng khí trơ có áp, bột hoặc "
               "vật liệu độn tương tự để ngăn sự xâm nhập của bầu khí quyển "
               "nổ, dù điều này không bắt buộc chặt chẽ."))
    b.append(h3("17.4.2 Vùng 1 và Vùng 21",
                "17.4.2 Zone 1 and Zone 21"))
    b.append(p("Ở Vùng 1 và Vùng 21, khả năng cáp hoặc hệ thống ống dẫn bị "
               "hư hỏng theo cách và với tần suất gây ra sự trùng hợp giữa "
               "tia lửa có khả năng gây cháy và sự hiện diện của bầu khí "
               "quyển nổ thấp hơn nhiều. Do đó, trong một số trường hợp có "
               "thể áp dụng cách tiếp cận nới lỏng hơn một chút. Một lần nữa, "
               "BS/EN 60079–14⁶ yêu cầu cáp không nằm trong rãnh lấp cát phải "
               "tuân thủ IEC 332 Phần 1⁸ về sự truyền ngọn lửa."))
    b.append(note("<b>Ghi chú trong đoạn mở đầu của 17.4.2.</b> Bản in viết "
                  "‘BS/EN 60079–14⁶’ với dấu gạch ngang dài (so với dấu gạch "
                  "ngang thường ở ‘BS/EN 60079-14⁶’ nêu trên), ‘IEC 332 Part "
                  "1⁸’ không có dấu phẩy, và ‘requires’ (OCR đọc nhầm thành "
                  "‘requks’). Bản tiếng Anh giữ nguyên."))
    b.append(h4("Cáp cho lắp đặt không an toàn nội tại",
                "Cables for non-intrinsically safe installations"))
    b.append(p("Cáp bọc giáp dây thép và cáp bện thép được mô tả là phù hợp "
               "để dùng ở Vùng 0 và 20 cũng phù hợp để dùng ở Vùng 1 và 21 "
               "đối với các lắp đặt bình thường và đặc biệt đối với các lắp "
               "đặt có nguy cơ va đập cơ học cao hơn bình thường. Trong "
               "điều kiện lắp đặt bình thường, lớp giáp ít cần thiết hơn và "
               "cáp như đã mô tả để dùng ở Vùng 0 và 20, nhưng không có lớp "
               "giáp, sẽ phù hợp với điều kiện lớp vỏ bên ngoài phù hợp cho "
               "một lắp đặt công nghiệp tiêu chuẩn. Ngoài ra, cáp có lớp vỏ "
               "bán cứng có thể được dùng không cần lớp giáp ở những nơi có "
               "nguy cơ va đập cơ học cao hơn bình thường. Các Tiêu chuẩn về "
               "cáp công nghiệp thông thường loại này nhìn chung sẽ đủ để "
               "đáp ứng các yêu cầu này."))
    b.append(p("Đối với thiết bị cầm tay và có thể di chuyển, các loại cáp "
               "sau đây được chấp nhận để sử dụng:"))
    b.append(ol([
        "Cáp mềm bọc cao su chắc chắn loại thường hoặc loại chịu lực nặng;",
        "Cáp mềm bọc polychloropren loại thường hoặc loại chịu lực nặng;",
        "Cáp có kết cấu chắc chắn tương đương.",
    ]))

    # ---- C42+C43, armouring paragraph joined across printed 500/501.
    b.append(p("Trong mọi trường hợp, việc lựa chọn cáp nên được xác định "
               "bởi mục đích sử dụng (ví dụ, khi nguy cơ hư hỏng cơ học cao, "
               "cáp luôn nên được lắp lớp giáp dây thép hoặc dây bện và, đặc "
               "biệt trong trường hợp cáp mềm, nên dùng cáp chịu lực nặng). "
               "Dù không cần thiết trong mọi trường hợp, lớp giáp dây thép "
               "hoặc dây bện là một biện pháp phòng ngừa khôn ngoan nhờ giá "
               "trị bảo vệ và sự ngăn chứa các sự cố trong khi thiết bị bảo "
               "vệ đang hoạt động, và thông lệ thông thường ở Vương quốc "
               "Anh là dùng loại cáp đó ở các khu vực nguy hiểm trừ khi cáp "
               "được bảo vệ rất tốt khỏi hư hỏng (chẳng hạn như được dẫn "
               "trong rãnh lấp cát). Có thể cần các biện pháp phòng ngừa "
               "khác trong một số trường hợp, chẳng hạn như bổ sung lớp vỏ "
               "chì tổng thể, khi cáp có khả năng tiếp xúc với các sản phẩm "
               "dầu mỏ trong thời gian dài (chẳng hạn như khi được lắp trong "
               "rãnh hoặc chôn)."))

    # ---- printed p.501: intrinsically-safe cables, Conduits, 17.4.3 (C44-C51).
    b.append(h4("Cáp cho mạch an toàn nội tại",
                "Cables for intrinsically safe circuits"))
    b.append(p("Yêu cầu đối với các loại cáp này về cơ bản như đã nêu để dùng "
               "ở Vùng 0 và 20. Có thể dùng cáp nhiều lõi được bảo vệ kém hơn "
               "ở Vùng 1 và 21, tuy nhiên, không cần xét đến sự cố giữa các "
               "mạch an toàn nội tại riêng biệt trong cáp nhiều lõi. Yêu cầu "
               "tối thiểu đối với loại cáp này là sợi dẫn không được nhỏ hơn "
               "0,1 mm, mỗi dẫn phải có ít nhất 2 mm lớp cách điện polyethylene "
               "hoặc PVC hoặc độ dày tương đương bằng các loại cách điện khác "
               "(ví dụ, có thể chứng minh rằng cách điện mỏng hơn bằng "
               "polytetrafluoroethylene (PTFE) là tương đương) phải có khả "
               "năng chịu được thử nghiệm điện áp 500 V rms và cáp được cố "
               "định và bảo vệ ở những nơi có khả năng chịu ứng suất cơ học. "
               "Loại cáp này chỉ được dùng cho các mạch an toàn nội tại có "
               "điện áp thấp hơn 60 V đỉnh xoay chiều hoặc một chiều"))
    b.append(note("<b>Ghi chú ở cuối yêu cầu về cáp an toàn nội tại.</b> Đoạn "
                  "kết thúc bằng ‘…voltages of less than 60 V peak ac or dc’ "
                  "không có dấu chấm cuối; bản tiếng Anh giữ nguyên. Đoạn cũng "
                  "in ‘(e.g., thinner insulation of polytetrafluoroethylene "
                  "(PTFE)’ với dấu phẩy sau ‘e.g.’ và từ ‘polytetrafluoro-"
                  "ethylene’ bị gãy dòng trong bản in; được nối lại và giữ "
                  "nguyên."))
    b.append(p("Bất kỳ cáp nhiều lõi nào không đáp ứng các yêu cầu nêu trên "
               "hoặc các yêu cầu để dùng ở Vùng 0 hoặc 20 được giả định là có "
               "khả năng gây nối liên kết giữa các mạch an toàn nội tại riêng "
               "biệt bên trong nó, và do đó chỉ có thể được dùng nếu thực "
               "hiện đánh giá về các sự nối liên kết đó."))
    b.append(p("Thông tin chi tiết hơn về chủ đề cáp cho mạch an toàn nội tại "
               "được đưa ra trong Chương 22."))
    b.append(h4("Ống dẫn", "Conduits"))
    b.append(p("Yêu cầu đối với ống dẫn trong mạch an toàn nội tại hoặc không "
               "an toàn nội tại về cơ bản giống như yêu cầu đối với lắp đặt "
               "ống dẫn ở Vùng 0 và 20, ngoại trừ việc các lõi của từng mạch "
               "an toàn nội tại không cần nằm trong màn chắn riêng. Tuy "
               "nhiên, chúng phải có một dạng vỏ bọc tổng thể nào đó để bảo "
               "đảm rằng các thông số điện cảm và điện dung của chúng được "
               "biết rõ, trừ khi các thông số này dựa trên khoảng cách lớn "
               "nhất có thể xảy ra trong ống dẫn."))
    b.append(note("<b>Ghi chú về cụm ‘overall serving’.</b> Bản in viết ‘some "
                  "form of overall serving’ (không phải ‘sheathing’); bản "
                  "tiếng Anh giữ nguyên, bản tiếng Việt theo nghĩa đúng."))
    b.append(h3("17.4.3 Vùng 2 và Vùng 22",
                "17.4.3 Zone 2 and Zone 22"))
    b.append(p("Mọi hệ thống cáp và ống dẫn phù hợp cho Vùng 0 và 20 và các "
               "Vùng 1 và 21 cũng sẽ phù hợp cho Vùng 2 và 22. Ngoài ra, phải "
               "nhớ rằng rủi ro ở Vùng 2 và 22 thấp hơn nhiều và, với điều "
               "kiện loại trừ bụi cần thiết mà mọi cáp có lớp vỏ bọc tổng thể "
               "bằng nhựa hoặc elastomer hoặc tương đương sẽ đáp ứng, các "
               "yêu cầu đối với cáp và ống dẫn ở Vùng 2 và 22 không nặng nề "
               "hơn các yêu cầu áp dụng cho một lắp đặt công nghiệp trong "
               "tình huống tương tự khi không có bầu khí quyển nổ, ngoại trừ "
               "việc vật liệu chế tạo không được truyền ngọn lửa (IEC 332 "
               "Phần 1⁸)."))

    return "".join(b)


def body_en():
    b = []

    # ---- printed p.497: Zone 22 (Zone Y), lead-in and items 1-9 (C1-C11).
    b.append(h4("Zone 22 (Zone Y)", "Zone 22 (Zone Y)"))
    b.append(p("This again is the least hazardous of the dust-related "
               "hazardous areas, being similar in risk to Zone 2. The "
               "suitability of apparatus reflects this as follows:"))
    b.append(ol([
        "Apparatus suitable for Zone 20 is normally suitable for Zone 22 "
        "(Zone Y) also.",
        "Apparatus suitable for Zone 21 (Zone Z) is normally suitable for "
        "Zone 22 (Zone Y) also.",
        "Apparatus conforming to BS 6467, Part 1⁴ (See Chapter 15) with an "
        "enclosure which is at least IP5X, provided that the dust is "
        "non-conducting.",
        "Oil-immersed apparatus ‘o’ (see Chapters 9 and 15) with an enclosure "
        "of at least IP5X provided the dust is non-conducting and the dust "
        "does not cause deterioration of the oil.",
        "Pressurized apparatus ‘p’ (see Chapters 11 and 15), provided the "
        "enclosure is IP5X (excluding purge outlets) and the dust is "
        "non-conducting. The action taken on pressurization failure should "
        "be at least that required in Zone 2.",
        "Powder-filled apparatus ‘q’ (see Chapters 9 and 15), provided the "
        "enclosure is at least IP5X and the dust is non-conducting.",
        "Flameproof enclosure ‘d’ (see Chapters 10 and 15), provided its "
        "enclosure is at least IP5X and the dust is non-conducting.",
        "Increased safety apparatus ‘e’ (see Chapters 12 and 15), provided "
        "its enclosure is at least IP5X and the dust is non-conducting.",
        "Intrinsically safe circuits ‘ia’ or ‘ib’ (see Chapters 13 and 15), "
        "provided the apparatus enclosures are at least IP5X and the dust is "
        "non-conducting. Intrinsically safe apparatus ‘ib’ is also acceptable "
        "if the enclosure does not achieve IP5X, provided the apparatus is "
        "reassessed assuming that all conducting parts not coated, "
        "encapsulated or insulated may be interconnected. This approach is "
        "also acceptable for conducting dusts.",
    ]))
    b.append(note("<b>Source quirks: Zone 22 list.</b> Item 3 prints ‘(See "
                  "Chapter 15)’ with a capital ‘S’, unlike the other ‘see "
                  "Chapter’ forms; item 4 uses the letter ‘o’ in "
                  "‘Oil-immersed apparatus’ (the OCR has a digit 0); item 7 "
                  "prints ‘Flameproof enclosure ‘d’’ — the correct "
                  "designation, unlike item 6 on printed p.496, which prints "
                  "‘p’; and item 5 prints ‘provided the enclosure is IP5X’ "
                  "without ‘at least’. All retained as printed."))

    # ---- 17.4, opening paragraph, joined across printed 497/498 (C13+C14).
    b.append(h3("17.4 Selection of conduit or cable systems",
                "17.4 Selection of conduit or cable systems"))
    b.append(p("The cables used for interconnection of apparatus in the "
               "hazardous area to that in the non-hazardous area, and "
               "different items of apparatus in the hazardous area, are "
               "subject to essentially the same requirements whether they "
               "are associated with gas/vapour/mist risks or dust risks. Two "
               "features of the cable are important, namely its adequacy in "
               "respect of electrical stresses (voltage and current flow "
               "including temperature elevation resulting) and their "
               "adequacy for the environment (heat, cold, moisture, airborne "
               "chemicals, etc.). The requirements stated here are "
               "appropriate to a normal outside environment but any unusual "
               "situations (such as the presence of unusually high "
               "concentrations of solvents in the atmosphere, etc.) need to "
               "be individually addressed in respect of the materials of "
               "construction and siting of cables, the objective being to "
               "achieve at least the same level of security as the "
               "recommendations given here would achieve in a normal "
               "industrial environment."))

    # ---- printed p.498: 17.4.1, Zones 0/20 (C15-C20).
    b.append(h3("17.4.1 Zone 0 and Zone 20",
                "17.4.1 Zone 0 and Zone 20"))
    b.append(p("The only standard protection concept suitable for Zone 0 and "
               "Zone 20 use is intrinsic safety of the higher category ‘ia’. "
               "This type of protection is based upon the presumption that "
               "the energy levels in the hazardous area are non-incendive "
               "and thus the requirements for cable and conduit systems are "
               "minimal and are only those required in a normal installation "
               "where hazardous areas are not present. Likewise, in the "
               "event that conduit is used only basic industrial requirements "
               "need to be met."))
    b.append(p("In both cases, however, the need to prevent explosive "
               "atmospheres from entering a non-hazardous area via the cable "
               "or the conduit needs to be addressed. This will normally "
               "require sealing of conduits but will probably require no "
               "additional arrangements for cables except where the cable "
               "has open interstices or where it is connected to a device, "
               "such as a transmitter, which could have an explosive "
               "atmosphere at greater than atmospheric pressure within it. "
               "Such precautions will normally consist of sealing the cable "
               "or conduit or venting them to prevent transmission to any "
               "area which would be adversely affected (a non-hazardous area "
               "or one of lesser hazard)."))
    b.append(p("In exceptional cases specially protected non-intrinsically "
               "safe installations are used where the cable or conduit may "
               "carry highly incendive energies and an entirely different "
               "approach is needed. Damage or deterioration of the cable or "
               "conductors within the conduit may have much more serious "
               "results and thus the choice of cables or conduit system "
               "becomes much more critical."))
    b.append(h4("Cables", "Cables"))
    b.append(p("For intrinsically safe circuits there have historically been "
               "no minimum requirements save those for multicores which "
               "contain more than one intrinsically safe circuit and require "
               "each circuit to be in an individual screen (see in Chapter "
               "22). The advent of the proposed BS/EN 60079⁶ has, for the "
               "first time introduced recommendations for these which state "
               "that the cables should not have any conductor or conductor "
               "strand of less than 0.1 mm diameter and the insulation must "
               "be suitable for 500 V rms ac operation. Because of the "
               "necessity of specification of cable inductance and "
               "capacitance an overall sheath is also necessary to define "
               "the positions of the conductors. It is possible to utilize "
               "cables containing more than one intrinsically safe circuit "
               "to carry circuits entering Zone 0, but such cables should be "
               "such that each circuit is individually contained in a screen "
               "which can be connected to the potential equalization "
               "(bonding) system to preclude interconnections of circuits "
               "(see in Chapter 22). In addition, the cable must contain only "
               "‘ia’ circuits and the screens must either be insulated from "
               "one another or all connected to the potential equalization "
               "(bonding) system at the same point and at the same point as "
               "the circuits contained within them."))
    b.append(note("<b>Source quirks in the intrinsically safe cables "
                  "paragraph.</b> The print reads ‘The advent of the proposed "
                  "BS/EN 60079⁶ has, for the first time introduced "
                  "recommendations’ (a comma after ‘has’, none after "
                  "‘time’), ‘(see in Chapter 22)’ twice (with the extra "
                  "‘in’), and ‘potential equalization’ with the American "
                  "‘z’ spelling, twice; all retained."))

    # ---- printed p.499: four recommendations, Conduits (C21-C30).
    b.append(p("In exceptional cases, where specially protected "
               "non-intrinsically safe circuits are installed in Zone 0, the "
               "possibility of cable damage releasing incendive energy is "
               "much more serious. Here the only real solution is to prevent "
               "the external release of such energy and the best way to do "
               "this is to ensure that the cable carries the features "
               "necessary to minimize such a risk. The basic recommendations "
               "for such cables will be:"))
    b.append(ol([
        "The cable should have thermoplastic or elastomeric insulation (or "
        "insulation of material satisfying similar requirements such as the "
        "mineral insulation in metal sheathed cables) on their cores "
        "sufficient for normal industrial use.",
        "The cores should be contained within a bedding of similar material "
        "unless the cable is mineral insulated, when the mineral insulation "
        "will suffice.",
        "The cable should be fitted with a steel wire or braid armouring over "
        "its bedding unless it has a continuous metal sheath, such as with "
        "metal sheathed mineral insulated cable, to minimize the risk of "
        "damage. This also provides a short circuit within the cable in the "
        "event of damage which minimizes the risk of arcing or sparking "
        "outside the cable before circuit protection operates.",
        "All cables including those with continuous metal sheaths should be "
        "fitted with an outer polyvinyl chloride (PVC), chlorosulphinated "
        "polyethylene (CSP), polychloroprene (PCP), chlorinated polyethylene "
        "(CSP) sheath or sheath of similar material to prevent earth faults "
        "to the armouring along the cable length and to protect the cable "
        "from the environment.",
    ]))
    b.append(note("<b>Source quirk: duplicated ‘(CSP)’.</b> Item 4 prints "
                  "‘chlorosulphinated polyethylene (CSP), polychloroprene "
                  "(PCP), chlorinated polyethylene (CSP)’ — ‘(CSP)’ appears "
                  "twice, the second presumably intended as ‘(CPE)’; "
                  "retained as printed. Elsewhere the text prints ‘Zone 0 or "
                  "20’ without repeating ‘Zone’; retained."))
    b.append(p("Most Standards for cables protected by armouring for normal "
               "industrial use will satisfy these requirements without the "
               "application of additional protection concepts."))
    b.append(p("A new recommendation included in BS/EN 60079-14⁶ is that all "
               "cables except those used in sand-filled trenches or the like "
               "need to be constructed of material which can satisfy the "
               "requirements of IEC 332, Part 1⁸ insofar as their ability to "
               "transmit flame once burning are concerned. While this is not "
               "yet included in national recommendations it is wise to "
               "address it as this will minimize the risk of transmission of "
               "fire around an installation should a fire occur within it."))
    b.append(note("<b>Source quirks in the standards designations.</b> Here "
                  "the print reads ‘BS/EN 60079-14⁶’ with an ordinary hyphen "
                  "and ‘IEC 332, Part 1⁸’ with a comma; both retained."))
    b.append(p("It is highly unlikely that non-intrinsically safe portable or "
               "transportable apparatus will be considered for use in Zone 0 "
               "or 20, but in the unlikely event that such use should be "
               "considered no relaxation in cable requirements are considered "
               "as reasonable and, in addition, the effect of flexing on "
               "armouring should be carefully considered to ensure that "
               "breakage due to flexing is unlikely."))
    b.append(h4("Conduits", "Conduits"))

    # ---- C30+C31, first Conduits paragraph joined across printed 499/500.
    b.append(p("For intrinsically safe circuits the only requirement for "
               "conduit is that it should constrain the enclosed conductors "
               "so that parameters are definable and that it should be "
               "fitted with a stopping device to prevent gases, vapours, "
               "mists or dusts from moving from one hazardous area to another "
               "or to a non-hazardous area. In addition, each individual "
               "intrinsically safe circuit within the conduit should, as in "
               "the case of a cable, be enclosed in an individual screen and "
               "those screens should satisfy the same requirements as for "
               "cable screens."))

    # ---- printed p.500: 17.4.2 and non-intrinsically-safe cables (C32-C42).
    b.append(p("For other circuits it should be a solid drawn or seam welded "
               "conduit in accordance with BS 4568⁹ or flexible metal or "
               "plastic conduit with heavy mechanical strength classification "
               "and an overall plastic sheath (see BS 731, Part 1¹⁰) to "
               "minimize the possibility of damage and prevent ingress of an "
               "explosive atmosphere. Such conduit systems are required to be "
               "fitted with recognized sealing devices (stopper boxes) where "
               "such conduits exit the hazardous area to enter another less "
               "hazardous area or a non-hazardous area."))
    b.append(note("<b>Source quirks: reference numerals and ‘eg.’.</b> The "
                  "print raises the reference numerals in ‘BS 4568⁹’ and "
                  "‘BS 731, Part 1¹⁰’, and writes ‘(eg., where the risk of "
                  "mechanical damage is high’ — ‘eg.’ with a comma and no "
                  "full stop after the ‘g’; all retained."))
    b.append(p("If possible it is wise to fill the conduit with pressurized "
               "inert gas or powder or similar filler to prevent the ingress "
               "of explosive atmosphere although this is not strictly "
               "necessary."))
    b.append(h3("17.4.2 Zone 1 and Zone 21",
                "17.4.2 Zone 1 and Zone 21"))
    b.append(p("In Zone 1 and Zone 21 there is a much lower possibility that "
               "cables or conduit systems could become damaged in such a way "
               "and at such a frequency as to cause a coincidence between "
               "ignition-capable sparking and the presence of an explosive "
               "atmosphere. Thus in some cases a slightly more relaxed "
               "approach is possible. Again, BS/EN 60079–14⁶ requires cables "
               "not in sand-filled trenches to comply with IEC 332 Part 1⁸ "
               "for flame transmission."))
    b.append(note("<b>Source quirks in the 17.4.2 opening paragraph.</b> The "
                  "print reads ‘BS/EN 60079–14⁶’ with an en dash (compare the "
                  "hyphen in the earlier ‘BS/EN 60079-14⁶’), ‘IEC 332 Part "
                  "1⁸’ without a comma, and ‘requires’ (which the OCR "
                  "misreads as ‘requks’); retained as printed."))
    b.append(h4("Cables for non-intrinsically safe installations",
                "Cables for non-intrinsically safe installations"))
    b.append(p("The steel wire armoured and steel braided cables described as "
               "suitable for use in Zone 0 and 20 are also suitable for use "
               "in Zone 1 and 21 for normal installations and particularly "
               "for installations where risks of mechanical impact are higher "
               "than normal. In normal installation conditions the armouring "
               "is less necessary and cables as described for Zone 0 and 20 "
               "use, but without the armouring, will be suitable provided the "
               "outer sheath is suitable for a standard industrial "
               "installation. In addition, cables with a semi-rigid sheath "
               "may be used without armouring where the risk of mechanical "
               "impact is higher than normal. Standards for normal industrial "
               "cables of this type will normally be sufficient to satisfy "
               "these requirements."))
    b.append(p("For portable and transportable apparatus cables of the "
               "following types are acceptable for use:"))
    b.append(ol([
        "Standard or heavy-duty tough rubber sheathed flexible cables;",
        "Standard or heavy-duty polychloroprene sheathed flexible cables;",
        "Cables of equally robust construction.",
    ]))

    # ---- C42+C43, armouring paragraph joined across printed 500/501.
    b.append(p("In all cases the choice of cables should be determined by the "
               "intended use (eg., where the risk of mechanical damage is "
               "high, cables should always be fitted with steel wire or braid "
               "armouring and, particularly in the case of flexible cables, "
               "heavy-duty cables should be used). While not being necessary "
               "in all cases, steel wire or braid armouring is a wise "
               "precaution due to its protective value and its containment of "
               "faults during operation of protection equipment, and it is "
               "normal UK practice to use such cables in hazardous areas "
               "unless the cable is very well protected against damage (such "
               "as being led in a sand-filled trench). Other precautions may "
               "be necessary in certain cases, such as provision of an "
               "overall lead sheath, where the cable is likely to be in "
               "contact with petroleum products for long periods (such as "
               "when it is installed in trenches or buried)."))

    # ---- printed p.501: intrinsically-safe cables, Conduits, 17.4.3 (C44-C51).
    b.append(h4("Cables for intrinsically safe circuits",
                "Cables for intrinsically safe circuits"))
    b.append(p("The requirements for these are basically as given for Zones 0 "
               "and 20 use. Less well-protected multicores may be used in "
               "Zone 1 and 21, however, without the need to consider faults "
               "between separate intrinsically safe circuits in the "
               "multicore. The minimum requirements for such cables are that "
               "conductor strands should not be below 0.1 mm, each conductor "
               "should have at least 2 mm of polyethylene or PVC insulation "
               "or an equivalent thickness of other types of insulation "
               "(e.g., thinner insulation of polytetrafluoroethylene (PTFE) "
               "can be shown to be equivalent) which must be capable of "
               "withstanding a 500 V rms voltage test and the cable is fixed "
               "and protected where mechanical stresses are likely. This "
               "type of cable is restricted to intrinsically safe circuits "
               "with voltages of less than 60 V peak ac or dc"))
    b.append(note("<b>Source quirks at the end of the intrinsically safe "
                  "cables requirements.</b> The paragraph ends ‘…voltages of "
                  "less than 60 V peak ac or dc’ with no full stop; retained. "
                  "It also prints ‘(e.g., thinner insulation of "
                  "polytetrafluoroethylene (PTFE)’ with a comma after ‘e.g.’ "
                  "and the word ‘polytetrafluoroethylene’ broken at the line "
                  "end in the print; joined and retained."))
    b.append(p("Any multicore cable not satisfying the requirements above or "
               "those for Zone 0 or 20 use is assumed to be capable of "
               "causing interconnection between separate intrinsically safe "
               "circuits within it, and thus can only be used if an "
               "assessment of such interconnections is carried out."))
    b.append(p("More detailed information on the subject of cables for "
               "intrinsically safe circuits is given in Chapter 22."))
    b.append(h4("Conduits", "Conduits"))
    b.append(p("The requirements for conduits in either intrinsically safe or "
               "non-intrinsically safe circuits are essentially the same as "
               "those for conduit installations in Zone 0 and 20 with the "
               "exception that the cores of individual intrinsically safe "
               "circuits need not be in individual screens. They must, "
               "however, have some form of overall serving to ensure that "
               "their inductive and capacitive parameters are clearly known "
               "unless these are based upon the maximum separation which can "
               "occur in the conduit."))
    b.append(note("<b>Source quirk: ‘overall serving’.</b> The print reads "
                  "‘some form of overall serving’ (not ‘sheathing’); "
                  "retained."))
    b.append(h3("17.4.3 Zone 2 and Zone 22",
                "17.4.3 Zone 2 and Zone 22"))
    b.append(p("All cable and conduit systems suitable for Zone 0 and 20 and "
               "Zones 1 and 21 will also be suitable for Zone 2 and 22. In "
               "addition it must be remembered that the risk in Zone 2 and 22 "
               "is much less and, subject to the necessary exclusion of dust, "
               "which all cables with a plastic or elastomeric or equivalent "
               "overall sheath will meet, the requirements for cables and "
               "conduits in Zone 2 and 22 are no more onerous than those which "
               "would apply for an industrial installation in a similar "
               "situation where explosive atmospheres were not present, "
               "except that materials of construction should not transmit "
               "flame (IEC 332 Part 1⁸)."))

    return "".join(b)
