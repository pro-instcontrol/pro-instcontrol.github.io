# -*- coding: utf-8 -*-
"""Chapter 10, module F — enclosure construction (continuation of 10.3.1),
10.3.2 Bushings, 10.3.3 Arrangements for entry facilities, 10.3.4 Fasteners
and the opening of 10.3.5 Component parts.

Printed pp. 257-263 (PDF pp. 278-284), raw LF 11654-11888. The sentence
"The explosion pressure" is interrupted by Table 10.14 on printed p.258 and
the fasteners paragraph is interrupted by Figs 10.20-10.22 on printed p.263;
both continuations are kept in printed reading order. The arcing/sparking
paragraph continues in module G, which also owns "Obstacles near flamepaths".
"""
from mcmillan_common import h3, h4, p, note, table, fig
import mcmillanfig10b as FB
import mcmillanfig10c as FC
import mcmillan_tbl10_11_15 as T3


def body_vi():
    b = []

    # ---- 10.3.1 continuation: non-metallic enclosures and pressure testing
    b.append(p("Vỏ chống cháy bằng vật liệu không kim loại có thể được chế tạo bằng "
               "phương pháp đúc hoặc chế tạo cơ khí, với các phương pháp tương tự để gắn "
               "một phần của vỏ vào phần khác, nhưng như đã nêu ở trên, chúng có giới hạn "
               "thể tích là 3000 cm³ trừ khi các bộ phận không kim loại chỉ chiếm một phần "
               "của vỏ về cơ bản là kim loại. Khi đó, giới hạn diện tích bề mặt riêng là "
               "500 cm² được áp dụng cho các bộ phận không kim loại (ngoại trừ các bộ phận "
               "truyền sáng của đèn, nơi giới hạn được tăng lên 8000 cm²). Sau khi được thử "
               "nghiệm để xác nhận khả năng chịu áp suất như mọi vỏ chống cháy khác, các vỏ "
               "không kim loại có bề mặt mối nối không kim loại hoặc chỉ có một phần không "
               "kim loại phải chịu các thử nghiệm xói mòn do ngọn lửa. Trong các thử nghiệm "
               "này, đường ngọn lửa của chúng bị tác động bởi dòng khí đang cháy thông qua "
               "việc tiến hành 50 lần thử, với các khe hở phẳng được mở đến giá trị cực đại, "
               "sử dụng hỗn hợp thử nổ dùng cho thử nghiệm áp suất nổ, và để xác nhận rằng "
               "không có sự xói mòn đáng kể nào xảy ra. Khi các bộ phận không kim loại làm "
               "bằng vật liệu nhựa, thử nghiệm cháy cũng được tiến hành trên vật liệu."))
    b.append(p("Ngoài ra, các vỏ không kim loại có tính cách điện có thể, không như vỏ kim "
               "loại, được dùng để đỡ trực tiếp các dây dẫn có điện áp khác nhau. Tuy nhiên, "
               "khi tận dụng ưu điểm này, cần cẩn thận bảo đảm chất lượng cách điện của vật "
               "liệu, vì khác với vật liệu được chọn chỉ để cách điện, vật liệu này được "
               "chọn chủ yếu vì khả năng về kích thước và độ bền của nó. Có các yêu cầu đối "
               "với mọi thiết bị trong môi trường nổ (xem Chương 8) nhằm giảm thiểu nguy cơ "
               "tích tụ tĩnh điện. Một cách để đáp ứng các yêu cầu này là nạp vào nhựa một "
               "vật liệu dẫn điện để hạn chế điện trở suất bề mặt của nó. Rõ ràng điều này "
               "sẽ làm đặt câu hỏi về tính cách điện của nó, và vì vậy cần bảo đảm rằng các "
               "vỏ không kim loại dùng để đỡ dây dẫn như vậy đáp ứng các yêu cầu của Bảng "
               "10.14. Chỉ số theo dõi so sánh (CTI) quy định trong bảng đó được xác định "
               "theo BS 5901: 1980¹⁵."))
    b.append(p("Tất cả các vỏ bọc, dù bằng kim loại hay không kim loại, đều được thử áp suất "
               "thủy lực ở mức 1,5 lần áp suất tham chiếu. Người ta thừa nhận rằng chúng có "
               "thể chịu chuyển động đàn hồi trong vụ nổ (chúng có thể giãn tạm thời do áp "
               "suất bên trong) nhưng không được phép biến dạng vĩnh cửu và cần phải đo đạc "
               "trên vỏ sau khi thử áp suất để xác nhận điều này. Biến dạng vĩnh cửu không "
               "được phép ở bản thân các bộ phận của vỏ (ví dụ, nắp bị cong) cũng như ở các "
               "đường ngọn lửa. Sự giãn đàn hồi của các đường ngọn lửa đương nhiên được tính "
               "đến trong các thử nghiệm truyền ngọn lửa. Áp suất tham chiếu được thu được "
               "bằng cách đốt cháy một hỗn hợp thử cụ thể bên trong vỏ mà không có khe hở "
               "nào được mở riêng, và theo dõi sự tăng và giảm áp suất bên trong vỏ trong "
               "suốt vụ nổ. Tiến hành nhiều lần thử và lấy áp suất của trường hợp xấu nhất "
               "làm áp suất tham chiếu. Hình 10.16 cho thấy một đường cong điển hình về tăng "
               "và giảm áp suất thu được từ các thử nghiệm như vậy. Có một vấn đề trong "
               "những trường hợp bên trong vỏ được chia thành các phần riêng biệt (xem Hình "
               "10.17) hoặc một bộ phận bên trong vỏ có vỏ bọc riêng của nó. Việc đốt cháy "
               "bên trong một vỏ có thể dẫn đến tăng áp sơ bộ cho khí ở vỏ kia vì các mặt "
               "sóng xung kích đi trước ngọn lửa truyền nhanh hơn ngọn lửa truyền với tốc độ "
               "âm thanh trong khí. Áp suất nổ"))

    # ---- Table 10.14 interrupts the sentence at the head of printed p.258
    b.append(table(T3.HEAD1014_VI, T3.ROWS1014, T3.CAPTION1014_VI))
    b.append(note(T3.NOTE1014_VI))

    b.append(p("là hàm của áp suất ban đầu tại thời điểm đánh lửa và nếu áp suất ban đầu này "
               "tăng lên thì áp suất nổ trong phần thứ hai của vỏ tăng đáng kể và, thêm vào "
               "đó, thời gian tăng áp suất trong vỏ thứ hai giảm xuống. Hiện tượng này được "
               "gọi là chồng áp suất (pressure piling). Dấu hiệu của hiện tượng này là thời "
               "gian tăng áp suất giảm xuống dưới 5 ms, hoặc các giá trị áp suất cực đại "
               "không ổn định có thể được nhận biết bằng sự thay đổi hơn 1,5 lần giữa các áp "
               "suất nổ đo được trong các thử nghiệm riêng biệt. Cần sắp xếp kết cấu của vỏ "
               "và thiết bị, trong phạm vi có thể, để ngăn ngừa hiện tượng này. Tuy nhiên, "
               "việc sử dụng các vỏ mà trong đó chồng áp suất xảy ra không bị cấm."))
    b.append(p("Trong các vỏ nhỏ, thường rất khó đo áp suất nổ và xác định áp suất cần dùng "
               "trong thử nghiệm áp suất. Trong những trường hợp này, các giá trị áp suất "
               "trong Bảng 10.15 được dùng."))

    b.append(fig(16, FB.fig_f1016()))
    b.append(fig(17, FB.fig_f1017()))

    b.append(p("Một vỏ chống cháy có thể là loại gọi là vào trực tiếp hoặc vào gián tiếp (xem "
               "Hình 10.18 và 10.19). Vỏ vào trực tiếp có các phương tiện kết nối (ví dụ, cọc "
               "đấu dây) để kết nối bên ngoài trong cùng vỏ với thiết bị được bao bọc, còn vỏ "
               "vào gián tiếp có một hộp đấu dây riêng. Hộp này có thể được nối với vỏ chính "
               "bằng, ví dụ, các ống lót và có ưu điểm là việc tiếp cận các phương tiện kết "
               "nối không đi vào vỏ chính và, vì vỏ chính có thể chứa"))

    # ---- Table 10.15 and Fig. 10.18 interrupt the entry paragraph on p.260
    b.append(table(T3.HEAD1015_VI, T3.ROWS1015, T3.CAPTION1015_VI))
    b.append(note(T3.NOTE1015_VI))
    b.append(fig(18, FB.fig_f1018()))

    b.append(p("các bộ phận thường phát tia lửa, người ta cho rằng đó là một lợi thế. Theo BS "
               "229, các vỏ không được phép vào trực tiếp và kiểu vào trực tiếp chỉ trở nên "
               "phổ biến với sự ra đời của BS 4683, Phần 2. Như sẽ thấy khi thảo luận về lắp "
               "đặt, có những khác biệt về thực hành lắp đặt được phép giữa hai loại vỏ."))

    b.append(fig(19, FB.fig_f1019()))

    # ---- 10.3.2
    b.append(h4("10.3.2 Ống lót", "10.3.2 Bushings"))
    b.append(note("<b>Ghi chú của người dịch.</b> Bản OCR ghi '70.3.2 Bushings' (chữ số 1 bị "
                  "đọc nhầm thành 7); bản in đúng là '10.3.2 Bushings'."))
    b.append(p("Ống lót là một phương pháp đưa dây dẫn xuyên qua thành vỏ hoặc giữa hai vỏ có "
               "thành chung. Nó thường làm bằng vật liệu cách điện chứa một hoặc nhiều dây "
               "dẫn. Các dây dẫn đi qua ống lót thường không được cách điện và sự bám dính "
               "của vật liệu cách điện của ống lót vào các dây dẫn tạo ra sự bịt kín cần "
               "thiết chống truyền ngọn lửa. Kết cấu thường dùng là hoặc các dây dẫn được "
               "dính xi măng lại với nhau và vào trong một vòng kim loại tạo thành một đường "
               "ngọn lửa với thành vỏ, hoặc nhựa được đúc vào các dây dẫn, trong trường hợp "
               "đó chính nhựa tạo thành đường ngọn lửa với thành vỏ. Các ống lót thường được "
               "thử nghiệm xói mòn do ngọn lửa và vật liệu của chúng, nếu là nhựa, được thử "
               "nghiệm cháy."))
    b.append(p("Tất cả các ống lót không dành riêng cho một vỏ chống cháy duy nhất cũng được "
               "thử áp suất ở 30 × 10⁶ N/m² để bảo đảm không có sự rò rỉ nào dọc theo các dây "
               "dẫn."))

    # ---- 10.3.3
    b.append(h4("10.3.3 Bố trí phương tiện vào dây", "10.3.3 Arrangements for entry facilities"))
    b.append(note("<b>Ghi chú của người dịch.</b> Bản OCR ghi '70.3.3 Arrangements for entry "
                  "facilities' (chữ số 1 bị đọc nhầm thành 7); bản in đúng là '10.3.3 "
                  "Arrangements for entry facilities'."))
    b.append(p("Phương pháp thông thường để cáp đi vào vỏ chống cháy là qua một đầu bịt cáp "
               "hoặc ống dẫn. Phương pháp phổ biến nhất ở Anh là đầu bịt cáp nhưng tình hình "
               "lại hoàn toàn ngược lại ở Hoa Kỳ – một thực tế khá quan trọng vì vỏ chống "
               "cháy ở Hoa Kỳ được thử nghiệm khi có một đoạn ống dẫn gắn vào, còn ở Anh thì "
               "không làm như vậy. Do đó, các yêu cầu về lắp hộp bịt (được mô tả sau) ở Anh "
               "khác với ở Hoa Kỳ."))
    b.append(p("Các đầu bịt đi vào vỏ xuyên qua thành vỏ và vị trí vào thường là một lỗ ren "
               "phải đáp ứng các yêu cầu đối với mối nối ren khi có đầu bịt cáp hoặc ống dẫn "
               "tại chỗ. Điều này đặt ra yêu cầu đáng kể đối với việc chế tạo các lỗ như vậy "
               "và vì lý do đó chúng thường được gia công vào vỏ tại thời điểm sản xuất. "
               "Điều này gây khó khăn vì các vị trí vào có thể cần ở những chỗ khác nhau cho "
               "các ứng dụng khác nhau. Để khắc phục điều này, nhà sản xuất gia công sẵn một "
               "số lỗ, trong đó có một số ít có khả năng được dùng trong các lắp đặt cụ thể. "
               "Để giải quyết vấn đề này, một loạt thiết bị bịt kín đã được phát triển [xem "
               "ghi chú] cho các lỗ ren không sử dụng. Các thiết bị này phải chắc chắn và tạo "
               "thành, cùng với lỗ, một đường ngọn lửa ren. Các phương pháp lắp được chấp "
               "nhận như sau: thứ nhất, thiết bị bịt kín chỉ có thể tháo ra từ bên trong vỏ. "
               "Nó phải được lắp từ bên trong hoặc được cố định từ bên trong sau khi lắp (xem "
               "Hình 10.20); thứ hai, thiết bị bịt kín có thể được lắp từ bên ngoài nhưng chỉ "
               "được có một vai nhỏ để giảm thiểu khả năng tháo nó bằng cờ lê, và việc lắp "
               "hoặc tháo phải dùng đầu lục giác hoặc lỗ lục giác có thông số kỹ thuật giống "
               "như loại dùng cho bu lông và vít giữ các vỏ với nhau (xem Hình 10.21); hoặc "
               "thứ ba, thiết bị bịt kín phải được lắp với đầu cắt để nó được lắp vĩnh cửu "
               "khi đầu đó bị cắt đứt (xem Hình 10.22)."))
    b.append(note("<b>Ghi chú của người dịch.</b> Bản in ghi 'a series of closing devices have "
                  "been develop for unused threaded openings' (thiếu '-ed'); bản tiếng Anh "
                  "giữ nguyên cụm từ in."))

    # ---- 10.3.4
    b.append(h4("10.3.4 Bộ phận bắt chặt", "10.3.4 Fasteners"))
    b.append(p("Các chi tiết bắt chặt dùng cho vỏ chống cháy gần như luôn là vít, bu lông, "
               "hoặc đai ốc và bu lông. Các thiết bị này phải giữ vỏ lại với nhau trong một "
               "vụ nổ nhưng thường không phải là một phần không thể thiếu của vỏ. Các bu lông "
               "hoặc vít này cần đáp ứng các yêu cầu sau: thứ nhất, hình dạng ren, dung sai "
               "và đầu của chúng phải phù hợp với những quy định đối với chi tiết bắt chặt "
               "đặc biệt theo BS/EN 50014 được thảo luận trong Chương 8; thứ hai, bất kỳ vít, "
               "bu lông hoặc đai ốc nào dùng"))

    b.append(fig(20, FB.fig_f1020()))
    b.append(fig(21, FC.fig_f1021()))
    b.append(fig(22, FC.fig_f1022()))

    b.append(p("làm chi tiết bắt chặt phải có giới hạn chảy thấp nhất là 240 N/mm² theo ISO "
               "6892 và, trừ khi thực sự cần thiết phải dùng chi tiết bắt chặt có giới hạn "
               "chảy cao hơn, nên luôn dùng loại này. Việc sử dụng bất kỳ chi tiết bắt chặt "
               "nào có giới hạn chảy cao hơn được coi là đặc biệt và sẽ yêu cầu ký hiệu 'X' "
               "được mô tả trong Chương 8; và thứ ba, nếu bất kỳ chốt vít hoặc bu lông nào đi "
               "xuyên qua thành vỏ thì nó phải tạo thành một mối nối chống cháy, như được mô "
               "tả trong Mục 10.2.1, và không thể tháo rời, được giữ vào vỏ bằng hàn hoặc một "
               "phương pháp có hiệu lực tương đương (ví dụ, đinh tán - rivetting)."))
    b.append(note("<b>Ghi chú của người dịch.</b> Bản in ghi 'at last 240 N/mm²' (lỗi in); "
                  "nghĩa đúng là 'at least' (ít nhất). Bản tiếng Anh giữ nguyên cụm từ in."))

    # ---- 10.3.5 opening
    b.append(h4("10.3.5 Các bộ phận cấu thành", "10.3.5 Component parts"))
    b.append(p("Nhìn chung, không có yêu cầu cụ thể nào đối với các bộ phận bên trong vỏ chống "
               "cháy, ngoại trừ các yêu cầu liên quan đến những thứ như bộ phận phát hồ "
               "quang."))
    b.append(h4("Bộ phận phát hồ quang hoặc tia lửa", "Arcing or sparking parts"))
    b.append(p("Người ta biết rằng các bộ phận phát hồ quang đặt gần và nằm trong mặt phẳng "
               "của khe hở mặt bích có thể ảnh hưởng nghiêm trọng đến tính chống cháy của vỏ "
               "và, khi điều đó xảy ra,"))

    return "".join(b)


def body_en():
    b = []

    # ---- 10.3.1 continuation: non-metallic enclosures and pressure testing
    b.append(p("Non-metallic enclosures may be constructed by moulding or fabrication, with "
               "similar methods of securing one part of an enclosure to another but, as "
               "already stated, they have a volume limit of 3000 cm³ unless the non-metallic "
               "parts form only part of an otherwise metallic enclosure. When this occurs an "
               "individual 500 cm² surface area limit is imposed on the non-metallic parts "
               "(excepting light transmitting parts of luminaires where the limit is "
               "increased to 8000 cm²). After being tested to confirm their capabilities to "
               "withstand pressure in common with all flameproof enclosures, non-metallic "
               "enclosures having non-metallic or partially non-metallic joint surfaces are "
               "subjected to flame erosion tests. In these their flamepaths are subjected to "
               "the passage of burning gas by the carrying out of 50 tests, with plane gaps "
               "opened to their maximum values, using the explosive test mixture for "
               "explosion pressure testing, and to confirm that no significant erosion has "
               "taken place. Where the non-metallic parts are of plastics material, "
               "flammability tests are also carried out on the material."))
    b.append(p("In addition, non-metallic enclosures which have insulating properties can, "
               "unlike metal enclosures, be used to directly support conductors of differing "
               "voltages. In utilizing this advantage, however, care needs to be taken to "
               "ensure the insulation quality of the material, as unlike material chosen for "
               "insulation alone, it is chosen principally for its dimensional ability and "
               "strength. There are requirements for all apparatus in explosive atmospheres "
               "(see Chapter 8) to minimize the risk of static build up. One way of satisfying "
               "these is to load the plastic with a conducting material to limit its surface "
               "resistivity. Clearly, this will bring its insulating properties into question "
               "and it is therefore necessary to ensure that non-metallic enclosures used for "
               "such support satisfy the requirements of Table 10.14. The comparative "
               "tracking index (CTI) specified in that table is determined in accordance with "
               "BS 5901: 1980¹⁵."))
    b.append(p("All enclosures, both metallic and non-metallic, are subjected to a hydraulic "
               "pressure test at 1.5 times the reference pressure. It is recognized that they "
               "may be subject to elastic movement during the explosion (they may temporarily "
               "enlarge due to their internal pressure) but no permanent distortion is "
               "acceptable and measurements on the enclosure after pressure testing are "
               "necessary to confirm this. Permanent distortion is not acceptable either in "
               "the enclosure parts themselves (e.g., bowed lids) or in the flamepaths. "
               "Elastic expansion of the flamepaths is, of course, taken account of during "
               "the flame transmission tests. The reference pressure is obtained by igniting "
               "a specific test mixture inside an enclosure with no gaps specially opened, "
               "and monitoring the rise and fall of pressure inside the enclosure during the "
               "explosion. Several tests are carried out and the worst case pressure taken "
               "as the reference pressure. Fig. 10.16 shows a typical pressure rise and decay "
               "curve obtained in such tests. There is a problem in cases where the interior "
               "of the enclosure is divided into separate parts (see Fig. 10.17) or a "
               "component within the enclosure has its own enclosure. An ignition within one "
               "enclosure can lead to pre-pressurization of the gas in the other as the shock "
               "fronts preceding the flame travel faster than the flame travelling at the "
               "speed of sound in the gas. The explosion pressure"))

    # ---- Table 10.14 interrupts the sentence at the head of printed p.258
    b.append(table(T3.HEAD1014_EN, T3.ROWS1014, T3.CAPTION1014_EN))
    b.append(note(T3.NOTE1014_EN))

    b.append(p("is a function of the initial pressure at the time of ignition and if this "
               "initial pressure is raised, the explosion pressure in the second part of the "
               "enclosure is significantly increased and, additionally, the pressure rise "
               "time in the second enclosure reduces. This phenomenon is called pressure "
               "piling. The evidence of such a phenomenon is the reduction of pressure rise "
               "time to less than 5 ms, or erratic maximum pressure values which can be "
               "identified by variation of more than a factor of 1.5 in the measured "
               "explosion pressures in separate tests. Enclosure and apparatus construction "
               "should, as far as possible, be arranged so as to prevent this. The use of "
               "enclosures where pressure piling does occur is not, however, precluded."))
    b.append(p("In small enclosures it is often very difficult to measure explosion pressure "
               "and to determine the pressure to be used in the pressure test. In these cases "
               "the values of pressure in Table 10.15 are used."))

    b.append(fig(16, FB.fig_f1016()))
    b.append(fig(17, FB.fig_f1017()))

    b.append(p("A flameproof enclosure may be what is called direct entry or indirect entry "
               "(see Fig. 10.18 and 10.19). A direct entry enclosure has the connection "
               "facilities (e.g., terminals) for external connection in the same enclosure, "
               "as the enclosed apparatus and an indirect entry enclosure has a separate "
               "terminal box. This may be connected to the main enclosure by, for example, "
               "bushings and has the advantage that entry to the connection facilities does "
               "not access the main enclosure and, as the main enclosure may contain"))

    # ---- Table 10.15 and Fig. 10.18 interrupt the entry paragraph on p.260
    b.append(table(T3.HEAD1015_EN, T3.ROWS1015, T3.CAPTION1015_EN))
    b.append(note(T3.NOTE1015_EN))
    b.append(fig(18, FB.fig_f1018()))

    b.append(p("normally sparking parts, it was felt to be an advantage. In BS 229 enclosures "
               "were not permitted to be direct entry and direct entry only became common "
               "with the advent of BS 4683, Part 2. As will be seen when installation is "
               "discussed, there are differences in permissible installation practices for "
               "the two types of enclosure."))

    b.append(fig(19, FB.fig_f1019()))

    # ---- 10.3.2
    b.append(h4("10.3.2 Bushings", "10.3.2 Bushings"))
    b.append(note("<b>Translator's note.</b> The OCR text reads '70.3.2 Bushings' (digit 1 "
                  "misread as 7); the printed heading is '10.3.2 Bushings'."))
    b.append(p("A bushing is a method of carrying a conductor through the wall of an enclosure "
               "or between two enclosures with a common wall. It is normally of insulating "
               "material containing one or more conductors. The conductors passing through "
               "the bushing are normally not insulated and adhesion of the bushing "
               "insulating material to the conductors gives the required seal against flame "
               "transmission. The normal construction used is either conductors cemented "
               "together and into a metal ring which forms a flamepath with the enclosure "
               "wall, or plastic moulded onto the conductors in which case the plastic itself "
               "forms the flamepath with the enclosure wall. The bushings are normally "
               "subjected to flame erosion tests and their material, if plastic, is subjected "
               "to flammability testing."))
    b.append(p("All bushings not unique to one flameproof enclosure are also subjected to "
               "pressure testing at 30 × 10⁶ N/m² to ensure that no leaks occur along the "
               "conductors."))

    # ---- 10.3.3
    b.append(h4("10.3.3 Arrangements for entry facilities",
                "10.3.3 Arrangements for entry facilities"))
    b.append(note("<b>Translator's note.</b> The OCR text reads '70.3.3 Arrangements for entry "
                  "facilities' (digit 1 misread as 7); the printed heading is '10.3.3 "
                  "Arrangements for entry facilities'."))
    b.append(p("The usual method by which cables enter flameproof enclosures is via a cable "
               "gland or conduit. The most common method in the UK is a cable gland but the "
               "situation is quite the reverse in the USA – a fact which is quite important "
               "as flameproof enclosures in the USA are tested with a length of conduit "
               "attached, whereas in the UK this is not done. Therefore, the requirements for "
               "fitting stopper boxes (described later) are different in the UK to those used "
               "in the USA."))
    b.append(p("Glands enter the enclosure through its wall and the entry is normally a "
               "threaded hole which must satisfy the requirements for a threaded joint with "
               "the cable gland or conduit in place. This places significant requirements on "
               "the production of such holes and for this reason they are normally machined "
               "into the enclosure at the time of manufacture. This causes problems as "
               "entries may be required in different places for different applications. To "
               "overcome this the manufacturer machines in several holes, some of which are "
               "unlikely to be used in particular installations. To overcome this problem a "
               "series of closing devices have been develop for unused threaded openings. "
               "These devices must be secure and form, with the opening, a threaded "
               "flamepath. The acceptable methods of mounting are as follows: first, the "
               "closing device must be removable only from the inside of the enclosure. It "
               "must be fitted from the inside or secured from the inside after fitting (see "
               "Fig. 10.20); second, the closing device may be fitted from the outside but "
               "shall only have a narrow shoulder to minimize the possibility of its removal "
               "with a wrench, and its installation or removal must be with a hexagon head or "
               "socket of the same specification as those used for bolts and screws holding "
               "enclosures together (see Fig. 10.21); or third, the closing device must be "
               "fitted with a shearing head so that it is permanently installed when the head "
               "has been sheared off (see Fig. 10.22)."))
    b.append(note("<b>Translator's note.</b> The printed text reads 'a series of closing "
                  "devices have been develop for unused threaded openings' (missing '-ed'); "
                  "the printed wording is retained here."))

    # ---- 10.3.4
    b.append(h4("10.3.4 Fasteners", "10.3.4 Fasteners"))
    b.append(p("The fasteners used for flameproof enclosures are almost invariably screws, "
               "bolts, or nuts and bolts. These devices have to hold the enclosure together "
               "during an explosion but are not usually an integral part of it. These bolts "
               "or screws need to comply with the following : first, their threadform, "
               "tolerances and heads should comply with those for special fasteners to "
               "BS/EN 50014 which are discussed in Chapter 8; second, any screws bolts or nuts "
               "used"))

    b.append(fig(20, FB.fig_f1020()))
    b.append(fig(21, FC.fig_f1021()))
    b.append(fig(22, FC.fig_f1022()))

    b.append(p("as fasteners should have a lower limit yield stress of at last 240 N/mm² in "
               "accordance with ISO 6892 and, unless there is a real necessity to use fixings "
               "of a higher yield stress, it is recommended that these are always used. The "
               "use of any higher yield stress fixings is considered as special and will "
               "require the 'X' mark described in Chapter 8; and third, if any stud screw or "
               "bolt passes through the wall of the enclosure it must form a flameproof "
               "joint, as described in Section 10.2.1, and be non-detachable, being held to "
               "the enclosure by welding or a method which is equally effective (e.g., "
               "rivetting)."))
    b.append(note("<b>Translator's note.</b> The printed text reads 'at last 240 N/mm²' (a "
                  "misprint for 'at least'); the printed wording is retained here."))

    # ---- 10.3.5 opening
    b.append(h4("10.3.5 Component parts", "10.3.5 Component parts"))
    b.append(p("In general there are no specific requirements for components within "
               "flameproof enclosures except those associated with such things as arcing "
               "parts."))
    b.append(h4("Arcing or sparking parts", "Arcing or sparking parts"))
    b.append(p("It is known that arcing parts placed near and in the plane of flange gaps can "
               "seriously affect the flameproof nature of an enclosure and, when this occurs,"))

    return "".join(b)
