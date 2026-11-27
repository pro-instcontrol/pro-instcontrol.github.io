# -*- coding: utf-8 -*-
"""Chapter 8, writer W4 - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 195-199 (PDF pp. 216-220).

Covers the printed '8.7.4' heading for fasteners (a printed error for 8.1.4,
retained with a bilingual note), fasteners and special fasteners with Figures
8.3 and 8.4, interlocking devices, bushings with Table 8.5, cements, and
section 8.1.5 connection facilities with Table 8.6. Owns Figures 8.3-8.4 and
Tables 8.5-8.6. The chapter shell owns the h2, references and end matter.

Footnote markers, standards designations (including 'IS0' with a zero), dates,
temperatures and other printed values follow the verified survey brief and the
page renders, not the garbled PDF text layer. This is an unofficial study
translation; the source PDF is not republished.
"""
from mcmillan_common import h2, h3, h4, p, note, table, fig
import mcmillanfig08 as F
import mcmillan_tbl85_86 as T85


def body_vi():
    b = []

    b.append(h3("8.7.4 Ốc vít, thiết bị khóa liên động, bạc lót và chất xi măng",
                "8.7.4 Fasteners, interlocking devices, bushings and cements"))
    b.append(note("<b>Lưu ý về số mục được in.</b> Tiêu đề trong bản in ghi là "
                  "'8.7.4'. Vì mục này nằm giữa các mục 8.1.3 và 8.1.5 và đề "
                  "cập đến ốc vít, thiết bị khóa liên động, bạc lót và chất xi "
                  "măng, số này hầu như chắc chắn là lỗi in của 8.1.4. Bản dịch "
                  "giữ nguyên số in 8.7.4 thay vì sửa lặng lẽ."))
    b.append(p("Một lần nữa, Tiêu chuẩn xác định những khía cạnh của ốc vít, "
               "thiết bị khóa liên động, bạc lót và chất xi măng mà hiệu năng "
               "của chúng quan trọng đối với khái niệm bảo vệ; các yêu cầu này "
               "áp dụng cho tất cả các Tiêu chuẩn về khái niệm bảo vệ cụ thể về "
               "sau, trừ khi Tiêu chuẩn về khái niệm bảo vệ cụ thể nào đó loại "
               "trừ chúng."))

    b.append(h4("Ốc vít (bao gồm cả ốc vít đặc biệt)",
                "Fasteners (including special fasteners)"))
    b.append(p("Tuyên bố chung duy nhất được đưa ra về các ốc vít dùng để cố "
               "định các bộ phận cần thiết để duy trì khái niệm bảo vệ (ngoài "
               "điều hiển nhiên là vật liệu và kết cấu của ốc vít phải tương "
               "thích với vỏ bọc mà nó cố định) là những ốc vít đó chỉ được "
               "tháo ra khi có sự trợ giúp của một dụng cụ. Thuật ngữ 'dụng cụ' "
               "không được định nghĩa, nhưng trong một điều khoản sau đó đề "
               "cập đến thiết bị khóa liên động, tuốc nơ vít và kìm được xác "
               "định cụ thể là không được chấp nhận làm phương pháp phá khóa "
               "liên động. Một số cơ quan chứng nhận đã dùng cách diễn đạt này "
               "hoặc cách diễn đạt có ý nghĩa tương tự trong BS 5501 part 1 "
               "(1977) làm cơ sở biện minh cho việc không dùng tuốc nơ vít và "
               "kìm cho ốc vít nói chung, và nên sử dụng các loại bulông và vít "
               "có đầu lục giác hoặc đầu lục giác chìm trong trường hợp này, "
               "trừ khi đã biết trước thái độ của cơ quan chứng nhận được chọn "
               "trước khi hoàn thành thiết kế của thiết bị cụ thể."))
    b.append(p("Một số Tiêu chuẩn về khái niệm bảo vệ quy định đến 'ốc vít đặc "
               "biệt' nhằm mang lại mức độ an toàn cao hơn mức thông thường. "
               "Để bảo đảm điều đó, vít, đai ốc và ren được xác định cẩn thận, "
               "cũng như các lỗ (hoặc lỗ hở để hở hoặc lỗ ren xuyên) mà vít "
               "hoặc chốt ren đi qua. Yêu cầu cơ bản đối với ren như sau: tất "
               "cả các ren phải là ren hệ mét bước thô theo IS0 262 (1973)⁸; "
               "dung sai lắp của ren phải là 6g/6H theo IS0 965 (1980)⁹."))
    b.append(p("Đầu vít hoặc đai ốc, khi chốt và đai ốc được dùng để cố định "
               "một nắp hoặc bộ phận tương tự thiết yếu cho khái niệm bảo vệ, "
               "được yêu cầu thuộc một trong các dạng sau:"))
    b.append(p("1. Vít có đầu lục giác theo IS0 4014 (1988)¹⁰ hoặc IS0 4017 "
               "(1988)¹¹. (Lưu ý: chỉ phần đầu phải phù hợp với Tiêu chuẩn "
               "được nêu.)"))
    b.append(p("2. Đai ốc lục giác theo IS0 4032 (1986)¹²."))
    b.append(p("3. Vít đầu lục giác chìm theo IS0 4762 (1989)¹³. (Lưu ý: chỉ "
               "phần đầu phải phù hợp với Tiêu chuẩn được nêu.)"))
    b.append(p("4. Vít hãm lục giác chìm theo IS0 4026 (1977)¹⁴, IS0 4027 "
               "(1977)¹⁵, IS0 4028 (1977)¹⁶ hoặc IS0 4029 (1977)¹⁷, với điều "
               "kiện vít hãm không nhô ra khỏi lỗ ren mà nó được lắp khi đã "
               "siết chặt."))
    b.append(p("Trong trường hợp vít có đầu, Tiêu chuẩn còn yêu cầu phần vai "
               "dưới đầu tính từ mép lỗ hở, hoặc lỗ ren trong trường hợp ốc "
               "vít có thân nhỏ hơn, không được lớn hơn phần sẽ xuất hiện với "
               "một vít tiêu chuẩn khi lỗ là lỗ hở có dung sai tối đa cho phép "
               "của lắp vừa trung bình H13 như xác định trong IS0 286-2 (1988)¹⁸."))
    b.append(p("BS 5501 part 1 (1977) đã đưa vào yêu cầu về mũ che trên ốc vít "
               "đặc biệt (xem Hình 8.3 và 8.4) nhằm gây khó khăn cho việc dùng "
               "các dụng cụ như cờ lê điều chỉnh để bám vào chúng. Yêu cầu này "
               "đã bị bỏ trong BS/EN 50014 (1993)¹, trừ các ứng dụng khai thác "
               "mỏ không được đề cập ở đây."))

    b.append(fig(3, F.fig_f803()))
    b.append(fig(4, F.fig_f804()))
    b.append(note("<b>Lưu ý về Hình 8.3 và 8.4.</b> Hai hình này mô tả yêu cầu "
                  "về mũ che và chỗ lõm lấy từ Tiêu chuẩn cũ BS 5501 part 1 "
                  "(1977); yêu cầu đó đã bị bỏ khỏi BS/EN 50014 (1993)¹, trừ "
                  "khi áp dụng cho khai thác mỏ. Chúng không phải là yêu cầu "
                  "hiện hành đối với thiết bị dùng trên mặt đất."))

    b.append(p("Mục đích của tất cả các điều nêu trên đối với ốc vít là tạo ra "
               "tình huống trong đó ốc vít không bị lỏng ra hoặc không dễ bị "
               "lỏng ngoài ý muốn. Sự khác biệt giữa ốc vít thường và ốc vít "
               "đặc biệt là mức độ an toàn được Tiêu chuẩn về khái niệm bảo vệ "
               "cụ thể xem là cần thiết. Đáng chú ý là trong hơn một trường "
               "hợp, Tiêu chuẩn về khái niệm bảo vệ còn yêu cầu mức độ an toàn "
               "cao hơn, như sẽ thấy khi thảo luận về các khái niệm bảo vệ cá "
               "biệt."))

    b.append(h4("Thiết bị khóa liên động", "Interlocking devices"))
    b.append(p("Trong một số trường hợp, thiết bị khóa liên động có thể được "
               "dùng thay cho ốc vít an toàn cao theo cách mà khóa liên động "
               "cách ly thiết bị điện và loại bỏ mọi nguồn bắt lửa còn dư (ví "
               "dụ năng lượng tích trữ) trước khi có thể mở vỏ bọc của thiết "
               "bị. Không có quy định kỹ thuật chính thức nào cho các thiết bị "
               "này trong BS/EN 50014 (1993)¹, ngoại trừ các chỉ dẫn nhằm đưa "
               "ra ý nghĩa về mức độ khó khăn mà những người tìm cách phá khóa "
               "sẽ gặp phải. Tiêu chuẩn yêu cầu chúng không thể bị phá bằng "
               "tuốc nơ vít hoặc kìm. Ngoài ra, vì không có quy định kỹ thuật "
               "nào được đưa ra cho chúng, chúng có thể là cơ khí hoặc điện."))
    b.append(p("Các yêu cầu này thoải mái hơn rất nhiều so với các yêu cầu "
               "trong BS 5501, Part 1 (1977) (ấn bản đầu tiên của Tiêu chuẩn "
               "này), theo đó khóa liên động chỉ có thể bị phá bằng một dụng "
               "cụ được thiết kế riêng cho mục đích đó và, theo suy luận, "
               "không nên dễ bị phá bằng bất kỳ dụng cụ nào trong dãy dụng cụ "
               "thông thường mà nhân viên sử dụng."))

    b.append(h4("Bạc lót", "Bushings"))
    b.append(p("Đôi khi bạc lót cách điện được dùng để thông tin giữa các phần "
               "khác nhau của vỏ bọc hoặc xuyên qua một vách ngăn bên trong vỏ "
               "bọc. Trong những trường hợp này, người ta áp dụng phương pháp "
               "công nghiệp thông thường. Tuy nhiên, đôi khi bạc lót được dùng "
               "làm đầu nối (cơ sở đấu nối) và có thể rằng nếu thực hiện mối "
               "nối bằng vít, hoặc nếu mối nối là đầu nối dạng chốt và đai ốc, "
               "thì một mô-men xoắn sẽ tác dụng lên đầu nối. Tiêu chuẩn yêu "
               "cầu đầu nối phải chịu được điều này khi áp dụng thử nghiệm mô- "
               "men xoắn tối đa quy định (xem Bảng 8.5). Nếu không thể làm bạc "
               "lót chắc chắn bằng cách siết chặt, có thể dùng vít hãm để ngăn "
               "nó quay. Khi vít hãm này nằm bên trong vỏ bọc (tức là không "
               "thể tiếp cận từ bên ngoài vỏ bọc), nó không cần tuân thủ các "
               "yêu cầu đối với ốc vít đặc biệt."))
    b.append(table(T85.HEAD85_VI, T85.ROWS85, T85.CAPTION85_VI))
    b.append(note(T85.NOTE85_VI))

    b.append(h4("Chất xi măng", "Cements"))
    b.append(p("Chất xi măng thường được dùng cho các việc như chế tạo vỏ bọc "
               "ghép chế tạo sẵn, hoặc cố định các thứ như bạc lót. Không có "
               "yêu cầu cụ thể nào cho chúng, ngoại trừ việc chúng phải giữ "
               "ổn định đến 20 °C trên nhiệt độ làm việc tối đa của chúng. Điều "
               "này thể hiện sự nới lỏng đáng kể so với BS 5501, part 1 (1977), "
               "vốn còn yêu cầu cả độ ổn định hóa học và khả năng chống dung "
               "môi đã được chứng minh hoặc sự bảo vệ khỏi tác động của chúng."))
    b.append(p("Tiêu chuẩn hiện hành chỉ yêu cầu rằng chất xi măng phải đạt "
               "yêu cầu trong một tập hợp điều kiện đã thỏa thuận giữa nhà sản "
               "xuất và người sử dụng, loại bỏ sự tham gia của cơ quan chứng "
               "nhận."))

    b.append(h3("8.1.5 Cơ sở đấu nối và cổng vào cáp",
                "8.1.5 Connection facilities and cable entries"))
    b.append(p("Có hai yếu tố cần xem xét ở đây. Thứ nhất, các đầu nối và hộp "
               "đấu nối của chúng (nếu có) được xem xét để bảo đảm có thể thực "
               "hiện mối nối hiệu quả, và thứ hai, phương thức mà cáp đi vào "
               "vỏ bọc được xem xét. Rõ ràng là không cơ sở đấu nối, hộp đấu "
               "nối, cũng như cơ chế dẫn điện hoặc cơ chế vào cáp nào được "
               "phép ảnh hưởng bất lợi đến khái niệm bảo vệ, nhưng cũng có các "
               "yêu cầu mang tính chung hơn."))

    b.append(h4("Cơ sở đấu nối và ngăn đấu nối",
                "Connection facilities and terminal compartments"))
    b.append(p("Các yêu cầu cơ bản trong BS/EN 50014 (1993)¹ đối với cơ sở đấu "
               "nối khá đơn giản, chỉ yêu cầu chúng cho phép đấu nối đúng cách "
               "dây dẫn và thực hiện điều đó mà không làm giảm các khoảng cách "
               "hở trong thiết bị. Dù phần lớn cách diễn đạt được dùng đề cập "
               "đến các ngăn đấu nối, rõ ràng là không bắt buộc phải có ngăn "
               "đấu nối và các đầu nối có thể nằm trong vỏ bọc chính. Tuy "
               "nhiên, trong trường hợp sau, cần nhấn mạnh rằng bố trí này cần "
               "bảo vệ thỏa đáng thiết bị điện bên trong vỏ bọc khỏi bị hư "
               "hại trong quá trình đấu nối."))
    b.append(p("Cơ sở đấu nối để tiếp địa (dây dẫn liên kết) cụ thể hơn, yêu "
               "cầu rằng cơ sở đấu nối phải chịu được dây dẫn có kích thước "
               "tối đa cụ thể ít nhất (xem Bảng 8.6) và, khi vỏ bọc thiết bị "
               "bằng kim loại, các cơ sở đấu nối đáp ứng các yêu cầu này phải "
               "hiện diện cả bên trong lẫn bên ngoài vỏ bọc, trong đó cơ sở "
               "bên ngoài phải có khả năng kết thúc ít nhất một dây dẫn 4 mm², "
               "nếu yêu cầu tiếp địa."))
    b.append(p("Điều lạ là ăn mòn và mối nối của dây dẫn kim loại nhẹ (nhôm) "
               "lại được xác định là một vấn đề đối với mối nối tiếp địa "
               "nhưng không phải cho các mối nối khác. Rõ ràng các mối nối khác "
               "cũng nên được kiểm tra về vấn đề này và, nếu có, nên thực hiện "
               "các bước để giảm thiểu nó."))
    b.append(table(T85.HEAD86_VI, T85.ROWS86, T85.CAPTION86_VI))
    b.append(note(T85.NOTE86_VI))

    return "".join(b)


def body_en():
    b = []

    b.append(h3("8.7.4 Fasteners, interlocking devices, bushings and cements",
                "8.7.4 Fasteners, interlocking devices, bushings and cements"))
    b.append(note("<b>Note on the printed section number.</b> The heading is "
                  "printed as '8.7.4'. Since this section sits between 8.1.3 "
                  "and 8.1.5 and deals with fasteners, interlocking devices, "
                  "bushings and cements, the number is almost certainly a "
                  "typographical error for 8.1.4. The printed number 8.7.4 is "
                  "retained rather than silently corrected."))
    b.append(p("Once again the Standard identifies those facets of fasteners, "
               "interlocking devices, bushings and cements, the performance of "
               "which are important to the protection concept and these apply "
               "to all the subsequent individual protection concept Standards, "
               "unless the particular protection concept Standard specifically "
               "excludes them."))

    b.append(h4("Fasteners (including special fasteners)",
                "Fasteners (including special fasteners)"))
    b.append(p("The only general statement made about fasteners which fix "
               "parts necessary to maintain the protection concept (apart from "
               "the obvious one that the fastener in material and construction "
               "must be compatible with the enclosure it fastens) is that such "
               "fasteners must be releasable only with the aid of a tool. The "
               "term 'tool' is not defined but in a subsequent Clause dealing "
               "with interlocking devices, screwdrivers and pliers are "
               "specifically defined as not being acceptable as a method of "
               "defeating an interlock. Some certification bodies have used "
               "this wording or wording of similar import in BS 5501 part 1 "
               "(1977) as justifying the non-use of screwdrivers and pliers for "
               "fasteners in general, and it is wise to utilize such things as "
               "hexagon and socket-headed bolts and screws in this regard, "
               "unless prior knowledge of the attitude of the chosen "
               "certification body is obtained in advance of completion of the "
               "particular apparatus design."))
    b.append(p("Some of the protection concept standards call up 'special "
               "fasteners' which are intended to give a greater degree of "
               "security than the norm. To ensure this, the screws, nuts and "
               "threads used are carefully defined, as are the holes, (either "
               "clearance or tapped through) which the screws or studs pass. "
               "The basic requirements for threads are as: all threads shall "
               "be coarse pitch metric in accordance with IS0 262 (1973)⁸; "
               "tolerance of fit of threads shall be 6g/6H in accordance with "
               "IS0 965 (1980)⁹."))
    b.append(p("The heads of screws or the nuts, where studs and nuts are used "
               "to secure a cover or similar part essential for the protection "
               "concept, are required to be one of the following:"))
    b.append(p("1. Screws with hexagon heads to IS0 4014 (1988)¹⁰ or IS0 4017 "
               "(1988)¹¹. (Note: only the head must comply with the named "
               "Standard.)"))
    b.append(p("2. Hexagon nuts to IS0 4032 (1986)¹²."))
    b.append(p("3. Cap screws with hexagon socket heads to IS0 4762 (1989)¹³. "
               "(Note: only the head must comply with the named Standard.)"))
    b.append(p("4. Hexagon socket set screws to IS0 4026 (1977)¹⁴, IS0 4027 "
               "(1977)¹⁵, IS0 4028 (1977)¹⁶ or IS0 4029 (1977)¹⁷ provided that "
               "the set screw does not protrude from the threaded hole in which "
               "it is fitted when it is tight."))
    b.append(p("In the case of screws with heads, the Standard also requires "
               "that the land under the head from the edge of the clearance "
               "hole, or the threaded hole in the case of a reduced shank "
               "fastener, is no more than that which would occur with a "
               "standard screw when the hole was a clearance hole with the "
               "maximum tolerance permitted by medium fit H13 as defined in "
               "IS0 286-2 (1988)¹⁸."))
    b.append(p("BS 5501 part 1 (1977) included a requirement for shrouds on "
               "special fasteners (see Fig. 8.3 and 8.4) to make it difficult "
               "to gain purchase on them by such things as adjustable wrenches, "
               "etc. This requirement has been dropped in the case of BS/EN "
               "50014 (1993)¹, except for mining applications which are not "
               "dealt with here."))

    b.append(fig(3, F.fig_f803()))
    b.append(fig(4, F.fig_f804()))
    b.append(note("<b>Note on Figures 8.3 and 8.4.</b> These figures show the "
                  "shroud and recess requirements taken from the old Standard "
                  "BS 5501 part 1 (1977); the requirement was dropped from "
                  "BS/EN 50014 (1993)¹ except for mining applications. They are "
                  "not current requirements for surface apparatus."))

    b.append(p("The objective of all of the above in the case of fasteners is "
               "to create a situation where fasteners do not become loose or "
               "cannot easily be inadvertently loosened. The difference between "
               "normal fasteners and special fasteners is the degree of "
               "security which is considered necessary by the particular "
               "protection concept standard. It is worthy of note that in more "
               "than one case the protection concept Standard requires even a "
               "higher level of security as will be seen when the individual "
               "protection concepts are discussed."))

    b.append(h4("Interlocking devices", "Interlocking devices"))
    b.append(p("Interlocking devices, may in some cases, be used instead of "
               "high security fasteners in such a way that the interlock "
               "isolates the electrical equipment and removes any residual "
               "sources of ignition (e.g., stored energy) before the apparatus "
               "enclosure can be opened. There is no formal specification for "
               "such devices in BS/EN 50014 (1993)¹ except indications to give "
               "some idea as to the difficulty which should be encountered by "
               "those seeking to circumvent them. The Standard requires that "
               "they are to be incapable of being defeated by screwdrivers or "
               "pliers. In addition, as no specification for them is given, "
               "they may be either mechanical or electrical."))
    b.append(p("The requirements are very much more relaxed then those in BS "
               "5501, Part 1 (1977) (the first edition of this Standard) as the "
               "requirements there were that the interlock could only be "
               "defeated by a tool specifically designed for the purpose and, "
               "by inference, it should not be susceptible to being defeated "
               "by any tool in the normal range of tools used by personnel."))

    b.append(h4("Bushings", "Bushings"))
    b.append(p("Insulated bushings are sometimes used for communication between "
               "different parts of an enclosure or through a barrier within "
               "the enclosure. In these cases, normal industrial practice is "
               "used. Sometimes however, the bushing is used as a terminal "
               "(connection facility) and it is possible that if a screw "
               "connection is made, or if the connection is by a post and nut "
               "terminal, a turning moment will be applied to the terminal. "
               "The Standard requires that the terminal be secure against this "
               "when a specified maximum torque test is applied (see Table "
               "8.5). If the bushing cannot be made secure by tightening then a "
               "set screw may be used to prevent turning. Where this set screw "
               "is within the enclosure (i.e., not accessible from outside the "
               "enclosure) it need not comply with the special fastener "
               "requirements."))
    b.append(table(T85.HEAD85_EN, T85.ROWS85, T85.CAPTION85_EN))
    b.append(note(T85.NOTE85_EN))

    b.append(h4("Cements", "Cements"))
    b.append(p("Cements are often used for such things as the construction of "
               "fabricated enclosures, or securing of such things as bushings. "
               "There are no specific requirements for these except that they "
               "must remain stable up to 20 °C above their maximum service "
               "temperature. This represents a significant relaxation with "
               "regard to BS 5501, part 1 (1977) which also required chemical "
               "stability and proven resistance to solvents or protection from "
               "their effects."))
    b.append(p("The current Standard merely requires that the cements be "
               "satisfactory in the set of conditions agreed by the "
               "manufacturer and user, removing the involvement of the "
               "certification body."))

    b.append(h3("8.1.5 Connection facilities and cable entries",
                "8.1.5 Connection facilities and cable entries"))
    b.append(p("There are two elements to be considered here. First, the "
               "terminals and their terminal box (if one is used) are addressed "
               "to ensure that effective connection can be made, and second, "
               "the method by which the cable enters the enclosure is "
               "addressed. Obviously, neither the connection facilities, "
               "connection box, nor the conductor or cable entry mechanisms "
               "should adversely affect the protection concept but there are "
               "also more general requirements."))

    b.append(h4("Connection facilities and terminal compartments",
                "Connection facilities and terminal compartments"))
    b.append(p("The basic requirements in BS/EN 50014 (1993)¹ for connection "
               "facilities are fairly straightforward, merely requiring that "
               "they allow proper connection of conductors and do this without "
               "reducing such things as clearances within the apparatus. While "
               "much of the wording used refers to terminal compartments, it "
               "is clear that a terminal compartment is not specifically "
               "required and the terminals may be in the main enclosure. In "
               "this latter case, however, it must be stressed that the "
               "arrangement needs to adequately protect the electrical "
               "equipment within the enclosure from damage during connection."))
    b.append(p("Connection facilities for earthing (bonding conductors) are "
               "more specific, requiring that the connection facilities can "
               "handle conductors of at least specific maximum sizes (see "
               "Table 8.6) and, where the apparatus enclosure is metal, that "
               "connection facilities satisfying these requirements appear "
               "both inside and outside the enclosure with the outside "
               "facility being capable of terminating a 4 mm² conductor as a "
               "minimum, if earthing is required."))
    b.append(p("Strangely, corrosion and connection of light metal (aluminium) "
               "conductors is identified as a problem with earth connections "
               "but not for other connections. Clearly other connections "
               "should be examined for this problem and, if present, steps "
               "should be taken to minimize it."))
    b.append(table(T85.HEAD86_EN, T85.ROWS86, T85.CAPTION86_EN))
    b.append(note(T85.NOTE86_EN))

    return "".join(b)
