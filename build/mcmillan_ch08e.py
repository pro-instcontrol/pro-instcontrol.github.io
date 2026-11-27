# -*- coding: utf-8 -*-
"""Chapter 8, module E - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp.200-205 (PDF pp.221-226): the
closing paragraphs of section 8.1.5 (cable and conduit entries), section
8.1.6 (rotating machines, switchgear, fuses, plugs and sockets,
luminaires), section 8.1.7 (Ex components) and the opening of section
8.1.8 (marking requirements) through the protection-concept symbol list.
Owns Figures 8.5-8.7, supplied by mcmillanfig08.

The chapter h2, the 19 printed references and the end matter belong to the
integration shell and are not emitted here. Unofficial study translation.
"""
from mcmillan_common import h2, h3, h4, p, note, table, fig
import mcmillanfig08 as F


def body_vi():
    b = []

    # --- 8.1.5, continued: conductor entry -------------------------------
    b.append(h4("Cổng vào dẫn dây (cổng vào cáp hoặc ống dẫn)",
                "Conductor entry (cable or conduit entries)"))
    b.append(p("Ở Anh, việc dùng cáp là bình thường và các thiết bị cổng vào "
               "cáp là thông lệ. Chúng có thể là một phần của vỏ bọc (thường "
               "thấy trong thực hành của Đức) hoặc tách rời khỏi vỏ bọc và "
               "tạo thành một dãy thiết bị tiêu chuẩn (thường thấy trong "
               "thực hành của Anh). Yêu cầu trong cả hai trường hợp về cơ bản "
               "là như nhau."))
    b.append(p("Luôn phải có sự làm kín giữa vỏ bọc cáp và thân đầu nối cáp "
               "(tức là phần của đầu nối được cố định trực tiếp vào vỏ bọc), "
               "và điều này có thể thực hiện bằng một vòng đệm quanh vỏ bọc "
               "cáp hoặc bằng cách đổ hợp chất làm kín; trong trường hợp sau, "
               "vỏ bọc cáp được cắt ngắn và hợp chất làm kín dính cả vào vỏ "
               "bọc lẫn lớp cách điện của dẫn dây (xem Hình 8.5 và 8.6). Tiêu "
               "chuẩn cũng yêu cầu các hợp chất làm kín được xem như chất xi "
               "măng và các vòng đệm bằng cao su đàn hồi (thay vì kim loại) "
               "phải vượt qua thử nghiệm kiểu về lão hóa. Có thêm các yêu cầu "
               "về kẹp giữ nhằm bảo đảm cáp được kẹp qua vỏ bọc hoặc lớp giáp "
               "bảo vệ theo cách không gây ứng suất lên dẫn dây, cùng các "
               "yêu cầu về đoạn dẫn vào nhằm tránh hư hỏng vỏ bọc nếu cáp bị "
               "dịch chuyển (xem Hình 8.7). BS/EN 50014 (1993)¹ chứa một loạt "
               "thử nghiệm kiểu để bảo đảm cổng vào cáp về cơ bản là phù hợp, "
               "dẫn đến một dãy đầu nối tiêu chuẩn mà nhà chế tạo hoặc người "
               "sử dụng lựa chọn cho thiết bị của mình."))

    # --- Figures 8.5-8.7, in printed source order ------------------------
    b.append(fig(5, F.fig_f805()))
    b.append(fig(6, F.fig_f806()))

    b.append(p("Cổng vào bằng ống dẫn không phổ biến ở Anh nhưng vẫn có thể "
               "được dùng. Ống dẫn thường được chấp nhận là loại kéo liền để "
               "bảo đảm chống chịu môi trường, và được ren vặn vào thiết bị. "
               "Vì ống dẫn là một phần của mạng tiếp địa hoặc liên kết, dù cố "
               "ý hay không, các mối nối và cổng vào của nó cần được bảo vệ "
               "khỏi hư hại do môi trường, và việc ngăn không cho khí quyển nổ "
               "lan xuống bên trong ống nhờ làm kín, chẳng hạn bằng hộp chặn, "
               "là cần thiết."))
    b.append(p("Nhà chế tạo thiết bị thường cung cấp các lỗ vào cho cáp hoặc "
               "ống dẫn, và thường có nhiều hơn một lỗ để tạo tính linh hoạt. "
               "Việc bịt kín các lỗ này khi không sử dụng là thiết yếu để bảo "
               "vệ tính toàn vẹn của vỏ bọc, và các nút bịt lỗ đó cần chắc "
               "chắn. Chúng chỉ nên tháo được khi có sự trợ giúp của dụng cụ, "
               "với những vấn đề phát sinh từ điều đó (xem Mục 8.5.1)."))
    b.append(note("<b>Lưu ý về liên kết chéo trong bản in.</b> Nguyên bản kết "
                  "thúc bằng '(xem Mục 8.5.1)', nhưng cấu trúc chương này "
                  "không có mục 8.5.1. Liên kết in được giữ nguyên thay vì "
                  "được sửa lặng lẽ."))

    # --- 8.1.6 -----------------------------------------------------------
    b.append(h4("8.1.6 Yêu cầu bổ sung cho các loại thiết bị cụ thể",
                "8.1.6 Additional requirements for particular types of apparatus"))
    b.append(p("Một số loại thiết bị được coi là có những vấn đề riêng, vì "
               "vậy có thêm các yêu cầu đối với chúng."))

    b.append(fig(7, F.fig_f807()))

    b.append(h4("Máy quay", "Rotating machines"))
    b.append(p("Máy quay thường có quạt bên ngoài để làm mát. Dù các quạt này "
               "không thuộc bộ phận bảo vệ cơ bản của máy, không cho tiếp cận "
               "bên trong vỏ bọc của máy, chúng vẫn là các bộ phận quay và có "
               "thể sinh nhiệt do ma sát hoặc tia lửa khi quạt cạ vào lồng "
               "chắn. Vì lý do này, BS/EN 50014 (1993)¹ có các yêu cầu đối với "
               "quạt và mũ che đó nhằm ngăn không để chúng trở thành nguồn "
               "bắt lửa, hoặc ngăn không để máy bị quá tải vượt quá mức thiết "
               "kế và các mức đã được xét đến trong khái niệm bảo vệ của máy. "
               "Các yêu cầu này gồm hạn chế về vật liệu dùng, hạn chế về cách "
               "lắp đặt và yêu cầu về vỏ bọc, phần lớn lấy từ các yêu cầu cơ "
               "bản của Tiêu chuẩn (ví dụ, hạn chế đối với chất dẻo và hàm "
               "lượng magiê trong kim loại nhẹ)."))
    b.append(p("Các lỗ thông gió của quạt được yêu cầu đạt IP20 ở phía đầu vào "
               "khí và IP10 ở phía đầu ra, việc giảm mức ở đầu ra chỉ được "
               "phép khi hình học của đầu ra sao cho các vật lạ có kích thước "
               "lớn hơn 12,5 mm không thể tiếp cận các bộ phận chuyển động, "
               "dù là rơi vào chúng (ví dụ, nếu đầu ra thẳng đứng) hay rung "
               "động làm cho chúng có thể tiếp cận được. Mức IP trong trường "
               "hợp này đạt được bằng sự phù hợp với một Tiêu chuẩn riêng, BS "
               "4999, phần 105 (1988)¹⁹. Ngoài ra, khe hở khi chạy được yêu "
               "cầu tối thiểu bằng 1/100 đường kính tối đa của quạt, với giá "
               "trị tối đa là 5 mm. Giá trị tối đa này có thể giảm xuống 1 mm "
               "đối với quạt gia công chính xác cao và ổn định lâu dài."))
    b.append(note("<b>Lưu ý về ký hiệu IP trong bản in.</b> Trang in ghi mức "
                  "bảo vệ phía đầu ra là 'IP10'; lớp văn bản PDF đọc là "
                  "'IPlO'. Bản dịch giữ nguyên chữ số in ở trên."))

    b.append(h4("Thiết bị đóng cắt", "Switchgear"))
    b.append(p("Thiết bị đóng cắt là nguồn bắt lửa tiềm ẩn nếu xảy ra hư hỏng "
               "hoặc nếu nó được vận hành một cách vô tình. Vì những lý do "
               "này, Tiêu chuẩn có các hạn chế về loại thiết bị đóng cắt "
               "(tức là không cho phép thiết bị đóng cắt chứa dầu vì khả năng "
               "dầu cháy bị phun ra khi thiết bị hỏng). Ngoài ra, Tiêu chuẩn "
               "yêu cầu khả năng khóa để ngăn vận hành vô tình và, đối với "
               "cầu dao, tất cả các cực (kể cả cực tiếp địa) đều phải được "
               "ngắt để ngăn phát tia lửa do dòng chảy vòng qua tiếp địa "
               "trong các hoạt động như bảo trì."))
    b.append(p("Cũng yêu cầu có nhãn cảnh báo cho những thứ như cầu cách ly "
               "không tải để ngăn việc vận hành chúng khi có tải, điều có thể "
               "gây bắt lửa, và cho cửa hoặc nắp che cho phép tiếp cận thiết "
               "bị đóng cắt tự động, trừ khi những cửa hoặc nắp đó được khóa "
               "liên động. Ở những nơi một số phần cần duy trì có điện bên "
               "trong tủ chứa thiết bị đóng cắt sau khi cơ cấu liên động đã "
               "tác động, các phần đó phải tiếp tục được bảo vệ bằng một "
               "khái niệm bảo vệ được công nhận hoặc được bảo vệ theo mức "
               "IP20 (BS/EN 60529²)."))

    b.append(h4("Cầu chì", "Fuses"))
    b.append(p("Vỏ bọc chứa cầu chì phải được khóa liên động để ngăn mở khi "
               "cầu chì còn có điện, hoặc phải được lắp nhãn cảnh báo để nhận "
               "diệt nguy cơ tháo cầu chì khi còn có điện trong khu vực nguy "
               "hiểm."))

    b.append(h4("Phích cắm và ổ cắm", "Plugs and sockets"))
    b.append(p("Nhìn chung, không nên dùng phích cắm và ổ cắm trong khu vực "
               "nguy hiểm, nhưng khi dùng thì tình huống lý tưởng là chúng "
               "được khóa liên động để bảo đảm cắt điện trước khi tách rời. "
               "BS/EN 50014 (1993)¹ thừa nhận điều này không phải lúc nào "
               "cũng khả thi và cho phép thay bằng nhãn cảnh báo không được "
               "tách rời khi còn có điện. Nếu không thể cắt điện, cho phép "
               "cảnh báo không tách rời trong khu vực nguy hiểm, dù điều này "
               "được cho là ít có giá trị đối với thiết bị cố định. Tuy "
               "nhiên, điều đó thể hiện rõ sự chấp nhận việc tách rời khi còn "
               "có điện vào những thời điểm có thể bảo đảm là không có khí "
               "quyển nổ."))
    b.append(p("Ngoài ra, người ta thừa nhận có thể thiết kế ổ cắm sao cho "
               "trong lúc rút phích, hồ quang nằm trong một vỏ bọc được bảo "
               "vệ bằng một trong các khái niệm bảo vệ được công nhận và, "
               "sau khi tách rời, các dẫn dây có điện trong ổ cắm vẫn được "
               "bảo vệ như vậy. Điển hình là có thể dùng Ex-d trong lúc tách "
               "rời và Ex-e sau khi tách rời hoàn tất. Cần lưu ý rằng sự "
               "nhượng bộ này chỉ áp dụng cho ổ cắm (phần cố định của bộ "
               "thết bị) chứ không áp dụng cho phích cắm."))

    b.append(h4("Đèn (thiết bị chiếu sáng)", "Luminaires (lighting fittings)"))
    b.append(p("BS/EN 50014 (1993)¹ không cho phép dùng bóng đèn hoặc ống đèn "
               "trần trong thiết bị chiếu sáng mà yêu cầu chúng được che bằng "
               "một nắp cho ánh sáng truyền qua. Ngoài ra, Tiêu chuẩn yêu cầu "
               "phải cách ly trước khi mở để thay đèn, chẳng hạn, trừ khi nắp "
               "che tác động vào cơ cấu liên động cắt nguồn cung cấp cho đèn. "
               "Khi chọn phương án sau, công tắc cách ly phải có khái niệm "
               "bảo vệ được công nhận riêng vì nó vẫn có điện khi phần còn "
               "lại của đèn đã được cách ly, và tia lửa khi cắt cùng sự tách "
               "tiếp điểm sau khi cắt cần được bảo đảm an toàn. Các cọc đầu "
               "cuối bên ngoài của nó cũng cần tiếp tục được bảo vệ khỏi bị "
               "tác động trong trạng thái đó, vì vậy nó phải được bao bọc đạt "
               "mức IP20 (EN 60529 (1991)²) khi tháo nắp trong suốt."))

    # --- 8.1.7 -----------------------------------------------------------
    b.append(h4("8.1.7 Bộ phận Ex", "8.1.7 Ex components"))
    b.append(p("Vì bộ phận Ex không phải là một thiết bị hoàn chỉnh nên nó "
               "chỉ cần đáp ứng các yêu cầu thích hợp của BS/EN 50014 (1993)¹. "
               "Các yêu cầu này thay đổi theo loại bộ phận, nhưng Tiêu chuẩn "
               "xác định những điều sau đây <i>không áp dụng cho bất kỳ bộ "
               "phận nào</i>: Thứ nhất, các yêu cầu về phân loại nhiệt độ bề "
               "mặt. (Tuy nhiên, bộ phận phải có nhiệt độ làm việc tối đa "
               "được xác định); và Thứ hai, định nghĩa về thời gian trễ cần "
               "thiết để bảo đảm điện tích dư hoặc nhiệt độ cao còn lại sau "
               "khi cách ly được tiêu hết trước khi mở ra."))
    b.append(p("Các điều khoản khác của Tiêu chuẩn áp dụng tương ứng (tức "
               "là, các điều khoản liên quan đến vỏ bọc của thiết bị chỉ áp "
               "dụng nếu bộ phận là một vỏ bọc rỗng)."))

    # --- 8.1.8, opening through the concept-symbol list -------------------
    b.append(h4("8.1.8 Yêu cầu ghi nhãn", "8.1.8 Marking requirements"))
    b.append(p("Các yêu cầu ghi nhãn của Tiêu chuẩn gồm xác định nhà chế tạo, "
               "mã chứng nhận và các thông tin liên quan khác. Dù dấu chứng "
               "nhận không phải là bắt buộc trừ khi thiết bị được chứng "
               "nhận, vẫn có một số yêu cầu về sự can thiệp của 'trạm thử "
               "nghiệm' trong điều khoản ghi nhãn. Điều này có nghĩa là việc "
               "chứng nhận là thông thường và dấu đó thường sẽ có mặt. Sau "
               "đây là các ví dụ điển hình về mã chứng nhận."))
    b.append(p("EEx: Chữ 'E' đầu tiên cho thấy sự phù hợp với Tiêu chuẩn này "
               "và một trong các Tiêu chuẩn khái niệm bảo vệ tiếp theo, và "
               "'Ex' sau đó xác định thiết bị là thiết bị bảo vệ chống nổ. "
               "Mặc dù 'Ex' xuất hiện trên mọi thiết bị bảo vệ chống nổ, chữ "
               "'E' đầu tiên chỉ xuất hiện trên thiết bị được bảo vệ theo "
               "BS/EN 50014 (1993), tiêu chuẩn tiền nhiệm của nó và các Tiêu "
               "chuẩn khái niệm bảo vệ phụ thuộc của nó."))
    b.append(p("d: Ký hiệu của khái niệm bảo vệ theo sau 'EEx', ký hiệu được "
               "cho ở đây là dành cho vỏ bọc chống nổ. Ký hiệu này sẽ thay "
               "đổi tùy theo khái niệm bảo vệ được dùng như sau:"))
    b.append(p("o - ngâm trong dầu (Chương 9)<br>"
               "p - cấp áp (Chương 11)<br>"
               "q - nhồi bột (Chương 9)<br>"
               "d - vỏ bọc chống nổ (Chương 10)<br>"
               "e - an toàn tăng cường (Chương 12)<br>"
               "ia - an toàn nội tại (Chương 13)<br>"
               "ib - an toàn nội tại (Chương 13)<br>"
               "m - bọc kín (Chương 9)"))
    b.append(note("<b>Lưu ý về lỗi lớp văn bản.</b> Lớp văn bản PDF đọc tiêu "
                  "đề chạy ở trang in 205 là 'General requirements for "
                  "exptosion protected apparatus'; trang in cho thấy 'explosion'. "
                  "Bản dịch dùng dạng in đúng."))
    return "".join(b)


def body_en():
    b = []

    # --- 8.1.5, continued: conductor entry -------------------------------
    b.append(h4("Conductor entry (cable or conduit entries)",
                "Conductor entry (cable or conduit entries)"))
    b.append(p("In the UK it is normal to use cables and cable entry devices "
               "are the norm. These may form part of the enclosure (typical "
               "German practice) or be separate from the enclosure and form a "
               "range of standard devices (typical UK practice). The "
               "requirements in both cases are effectively the same."))
    b.append(p("There should always be sealing between the cable sheath and "
               "the gland body (i.e., that part of the gland which is directly "
               "fixed to the enclosure) and this may be either by a sealing "
               "ring around the cable sheath or by compound filling, in which "
               "case the sheath is cut back and the compound seals to both the "
               "sheath and conductor insulation (see Fig. 8.5 and 8.6). The "
               "Standard also requires that sealing compounds be treated as "
               "cements and elastomeric (rather than metal) sealing rings pass "
               "an ageing type test. There are also clamping requirements "
               "which are intended to ensure the cable is clamped by the "
               "sheath or armouring in such a way as to prevent stress on the "
               "conductors and lead in requirements to prevent sheath damage "
               "if the cable is moved (see Fig. 8.7). BS/EN 50014 (1993)¹ "
               "contains a whole range of type tests to ensure that cable "
               "entries are basically suitable and this results in a series "
               "of standard glands from which the manufacturer or user chooses "
               "for his apparatus."))

    # --- Figures 8.5-8.7, in printed source order ------------------------
    b.append(fig(5, F.fig_f805()))
    b.append(fig(6, F.fig_f806()))

    b.append(p("Conduit entries are not usual in the UK but may be used. The "
               "normally acceptable conduit is solid drawn to ensure "
               "protection from the environment, and screwed entry into the "
               "apparatus. As the conduit forms part of the earthing or "
               "bonding network, inadvertently if not deliberately, its joints "
               "and entries should be protected against environmental damage, "
               "and the prevention of passage of explosive atmosphere down "
               "its inside sealing, by such things as stopping boxes, is "
               "required."))
    b.append(p("The manufacturer of apparatus normally provides entry holes "
               "for cable or conduit, and often more than one to permit "
               "flexibility. It is essential that these are closed when not "
               "used to protect the enclosure integrity, and plugs for such "
               "holes need to be secure. They should only be removable with "
               "the aid of a tool with the problems which that creates (see "
               "Section 8.5.1)."))
    b.append(note("<b>Note on the printed cross-reference.</b> The original "
                  "ends with '(see Section 8.5.1)'; no section 8.5.1 exists in "
                  "this chapter's structure. The printed reference is retained "
                  "verbatim rather than silently corrected."))

    # --- 8.1.6 -----------------------------------------------------------
    b.append(h4("8.1.6 Additional requirements for particular types of "
                "apparatus",
                "8.1.6 Additional requirements for particular types of "
                "apparatus"))
    b.append(p("Certain types of apparatus are considered to have specific "
               "problems and there are thus additional requirements for "
               "these."))

    b.append(fig(7, F.fig_f807()))

    b.append(h4("Rotating machines", "Rotating machines"))
    b.append(p("Rotating machines often have external fans for cooling "
               "purposes. While these fans do not form part of the basic "
               "protection of the machine, not permitting access to the "
               "interior of the machine enclosure, they do form rotating "
               "parts and can generate friction heating or sparking due to "
               "the fan catching on its guard. For this reason BS/EN 50014 "
               "(1993)¹ contains requirements for such fans and hoods to "
               "prevent them from becoming sources of ignition, or to prevent "
               "the loading of the machine beyond its design rating and the "
               "ratings considered in its protection concept. These "
               "requirements include limitations on materials used, mounting "
               "restrictions, and enclosure requirements, most of which are "
               "drawn from the basic requirements of the Standard (e.g., "
               "limitations on plastics and on magnesium content of light "
               "metals)."))
    b.append(p("The ventilation openings of fans are required to be IP20 on "
               "the air inlet side, and IP10 on the outlet side, the latter "
               "reduction only being permitted when the geometry of the "
               "outlet is such that foreign bodies above 12.5mm in size cannot "
               "access the moving parts, either by falling into them (e.g., "
               "if the outlet is vertical) or by vibration causing their "
               "access to be possible. The IP rating in this case is produced "
               "by compliance with a special Standard, BS 4999, part 105 "
               "(1988)¹⁹. In addition, running clearances are required to be "
               "a minimum of 1/100 of the maximum fan diameter with a maximum "
               "figure of 5mm. This maximum figure may be reduced to 1 mm for "
               "fans of high machining accuracy and long-term stability."))
    b.append(note("<b>Note on the printed IP rating.</b> The printed page "
                  "gives the outlet-side rating as 'IP10'; the PDF text layer "
                  "reads 'IPlO'. The printed digits are retained above."))

    b.append(h4("Switchgear", "Switchgear"))
    b.append(p("Switchgear is a potential source of ignition if failure occurs "
               "or if it is operated inadvertently. For these reasons, the "
               "Standard contains limitations on the types of switchgear "
               "(i.e., no oil-filled switchgear is permitted because of the "
               "possibility of discharge of burning oil if the gear fails). In "
               "addition, it requires locking capability to prevent "
               "inadvertent operation and, in the case of disconnectors, all "
               "poles (including the earth) are required to be disconnected "
               "to prevent sparking due to circulating earth currents during "
               "such activities as maintenance."))
    b.append(p("Warning labels are also required for such things as off-load "
               "isolators to prevent their operation on-load, which could "
               "cause an ignition, and for doors and covers giving access to "
               "automatic switchgear, unless those doors or covers are "
               "interlocked. Where some parts need to remain energized within "
               "cabinets containing switchgear after an interlock has "
               "operated, those parts must remain protected by a recognized "
               "protection concept or be protected to IP20 (BS/EN 60529²)."))

    b.append(h4("Fuses", "Fuses"))
    b.append(p("Enclosures containing fuses are required to be either "
               "interlocked, to prevent opening while the fuses are "
               "energized, or are required to be fitted with a warning label "
               "to identify the danger of removing fuses live in a hazardous "
               "area."))

    b.append(h4("Plugs and sockets", "Plugs and sockets"))
    b.append(p("In general, plugs and sockets should not be used in a "
               "hazardous area but where they are, the ideal situation is one "
               "where they are interlocked to ensure that they are "
               "de-energized before separation. BS/EN 50014 (1993)¹ recognizes "
               "this as not always possible and allows as the alternative a "
               "label with a warning against energized separation. If "
               "de-energization is not possible, a warning not to separate in "
               "a hazardous area is permitted, although this is felt to be of "
               "little value for fixed equipment. It does, however, clearly "
               "identify the acceptance of energized separation at times when "
               "the absence of explosive atmosphere can be guaranteed."))
    b.append(p("In addition, it is recognized that a socket can be designed "
               "so that during removal of the plug, the arc is in an enclosure "
               "which has protection by one of the recognized protection "
               "concepts and, after separation, the energized conductors in "
               "the socket remain so protected. Typically Ex-d during "
               "separation and Ex-e after separation is complete is possible. "
               "It should be noted that this relaxation applies to the socket "
               "(fixed part of the arrangement) only and not the plug."))

    b.append(h4("Luminaires (lighting fittings)", "Luminaires (lighting fittings)"))
    b.append(p("BS/EN 50014 (1993)¹ does not permit naked bulbs or tubes in "
               "lighting fittings but requires them to be covered by a light "
               "transmitting cover. In addition, it requires isolation before "
               "opening to relamp, for example, unless the cover operates an "
               "interlock isolating the supplies to the luminaire. Where this "
               "latter route is chosen, the isolating switch is required to "
               "have its own recognized protection concept as it remains live "
               "when the rest of the luminaire is isolated, and the spark on "
               "isolation together with the contact separation after "
               "isolation needs to be secure. Its external terminals also "
               "need to remain protected against interference in this state "
               "and it must therefore be enclosed to IP20 (EN 60529 (1991)²) "
               "standard when the transparent cover is removed."))

    # --- 8.1.7 -----------------------------------------------------------
    b.append(h4("8.1.7 Ex components", "8.1.7 Ex components"))
    b.append(p("As an Ex component is not a complete item of apparatus it only "
               "needs to satisfy the appropriate requirements of BS/EN 50014 "
               "(1993)¹. These vary according to the type of component but "
               "the Standard identifies the following as <i>not being "
               "applicable to any components</i>: First, the requirements for "
               "surface temperature classification. (It must, however, have a "
               "maximum operating temperature defined); and Second, the "
               "definition of the delay time necessary to ensure that any "
               "residual charge or high temperature remaining after isolation "
               "is dissipated before opening."))
    b.append(p("The other clauses of the Standard apply as appropriate (i.e., "
               "the Clauses relating to an apparatus enclosure only apply if "
               "the component is an empty enclosure)."))

    # --- 8.1.8, opening through the concept-symbol list -------------------
    b.append(h4("8.1.8 Marking requirements", "8.1.8 Marking requirements"))
    b.append(p("The marking requirements of the Standard include "
               "identification of the manufacturer, the certification Code "
               "and other relevant information. While a certification mark is "
               "not a requirement, unless the apparatus is certified, there "
               "are several requirements for intervention of 'the test "
               "station' in the marking clause. This means that it is normal "
               "to have certification and such a mark will normally be "
               "present. Typical of the certification coding are the "
               "following."))
    b.append(p("EEx: The first 'E' shows compliance with this Standard and one "
               "of the subsequent protection concept Standards, and the "
               "subsequent 'Ex' identifies the equipment as explosion "
               "protected. Although the 'Ex' appears on all explosion "
               "protected apparatus the first 'E' only appears on that "
               "protected to BS/EN 50014 (1993), its predecessor and its "
               "subsidiary protection concept Standards."))
    b.append(p("d: The symbol for the protection concept follows the 'EEx', "
               "the one shown here being for flameproof enclosure. This "
               "symbol will vary depending on the protection concept used as "
               "follows:"))
    b.append(p("o - oil immersion (Chapter 9)<br>"
               "p - pressurization (Chapter 11)<br>"
               "q - powder filling (Chapter 9)<br>"
               "d - flameproof enclosure (Chapter 10)<br>"
               "e - increased safety (Chapter 12)<br>"
               "ia - intrinsic safety (Chapter 13)<br>"
               "ib - intrinsic safety (Chapter 13)<br>"
               "m - encapsulation (Chapter 9)"))
    b.append(note("<b>Note on the text-layer artifact.</b> The PDF text layer "
                  "renders the running header on printed p.205 as 'General "
                  "requirements for exptosion protected apparatus'; the "
                  "printed page reads 'explosion'. The printed spelling is "
                  "used above."))
    return "".join(b)
