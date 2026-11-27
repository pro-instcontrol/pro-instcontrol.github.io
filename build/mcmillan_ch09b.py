# -*- coding: utf-8 -*-
"""Chapter 9, module B - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), raw lines 9971-10121, printed pp.212-215
(PDF pp.233-236).

Covers the close of section 9.1.3, sections 9.1.4-9.1.6 with Table 9.1,
the Fuses and Cells or batteries subsections, and the printed '9.7.7'
Type testing section (almost certainly 9.1.7; retained with a note).
Figure 9.1 is only referred to in prose here; it belongs to module W3.
The chapter h2, the references and the end matter belong to the shell.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h2, h3, h4, p, note, table, fig
import mcmillan_tbl91_93 as T91


def body_vi():
    b = []

    # --- printed p.212 (PDF 233): close of 9.1.3 ---------------------------
    b.append(p("Với quan điểm nêu trên, các yêu cầu của nguyên lý bảo vệ trở nên "
               "dễ hiểu và thực tế hơn."))

    # --- 9.1.4 Encapsulated circuits and components ------------------------
    b.append(h3("9.1.4 Mạch và linh kiện được bọc kín",
                "9.1.4 Encapsulated circuits and components"))
    b.append(p("Tiêu chuẩn cho phép bọc kín nhiều loại linh kiện điện và điện tử, "
               "miễn là nhiệt độ làm việc của các linh kiện đó không vượt quá giá "
               "trị định mức của chúng ở nhiệt độ môi trường tối đa dự kiến khi "
               "vận hành (thường là 40 °C). Ngay cả các linh kiện như rơ le và công "
               "tắc cũng được phép, với điều kiện là bản thân chúng được bao bọc "
               "trước khi bọc kín. Tuy nhiên, đối với các linh kiện này, thể tích "
               "tối đa của vỏ bọc bị giới hạn ở 100 cm² và, nếu chúng đóng cắt dòng "
               "lớn hơn 6 A, vỏ bọc phải làm bằng vật liệu vô cơ để ngăn vật liệu "
               "bị cháy khi có hồ quang hoặc tia lửa. Định mức của các linh kiện "
               "được dùng cần đủ để bảo đảm chúng luôn nằm trong giới hạn đó trong "
               "trường hợp có một hư hỏng ở nơi khác, hoặc khi sự hư hỏng của chính "
               "chúng theo cách tồi tệ nhất được giả định là một phần của hư hỏng "
               "đó. Các loại hư hỏng được xét đến gồm nhưng không giới hạn ở: ngắn "
               "mạch hoặc hở mạch của bất kỳ linh kiện nào, hoặc các hư hỏng trong "
               "mạch in chẳng hạn như hở mạch hoặc ngắn mạch giữa các đường dẫn."))
    b.append(p("Thiết bị không được phép vượt quá phạm vi nhiệt độ làm việc quy "
               "định tại bất kỳ điểm nào trong vận hành bình thường hoặc trong "
               "điều kiện hư hỏng, và điều này có thể bảo đảm bằng một bộ cắt nhiệt "
               "bên trong, miễn là bộ cắt đó không tự thiết lập lại — về thực tế, "
               "điều này có nghĩa là nếu nó tác động thì thiết bị đã hết tuổi thọ "
               "sử dụng."))
    b.append(p("Một số linh kiện được coi là không chịu hư hỏng trong nguyên lý "
               "bảo vệ nếu trong vận hành bình thường chúng làm việc ở mức dưới "
               "hai phần ba định mức điện áp và công suất, và trong điều kiện hư "
               "hỏng ở mức dưới định mức điện áp và công suất; đó là: điện trở loại "
               "màng carbon hoặc màng kim loại; điện trở dây quấn với dây được "
               "quấn thành một lớp xoắn ốc đơn; tụ điện bằng màng nhựa, giấy và gốm."))
    b.append(p("Ngoài ra, các linh kiện sau đây được coi là không chịu hư hỏng khi "
               "chúng đáp ứng các yêu cầu áp dụng cho chúng trong vận hành bình "
               "thường và không vượt quá định mức của mình trong tình huống một hư "
               "hỏng đơn lẻ."))
    b.append(p("Thứ nhất, các optocoupler tạo cách ly giữa các mạch riêng biệt, nếu "
               "tổng điện áp của các mạch được cách ly nhỏ hơn 1000 V rms và điện "
               "áp định mức của optocoupler giữa các mạch đó ít nhất bằng 1,5 lần "
               "tổng điện áp này."))
    b.append(p("Thứ hai, máy biến áp và các cuộn dây khác tuân thủ BS 5501, Phần 6 "
               "(1977)⁹ (bao gồm cả ấn bản thứ hai là BS/EN 50019 (1994)¹⁰, có yêu "
               "cầu không khác biệt nhiều). Ngoài ra, các cuộn dây dùng dây có đường "
               "kính nhỏ hơn 0,25 mm mà BS 5501, Phần 6 (1977)⁹ hoặc bản kế tiếp là "
               "BS/EN 50019 (1994)¹⁰ không cho phép thì vẫn được chấp nhận, miễn là "
               "chúng bằng cách khác tuân thủ các tiêu chuẩn đó và, bổ sung thêm, "
               "được bảo vệ chống lại nhiệt độ bên trong không được phép bằng các "
               "bộ cắt nhiệt nhúng hoặc thiết bị tương tự."))
    b.append(p("Thứ ba, máy biến áp tuân thủ các yêu cầu đối với máy biến áp nguồn "
               "không thể hư hỏng trong BS 5501, Phần 7 (1977)⁶ (và bản kế tiếp là "
               "BS/EN 50020 (1994)⁷, cũng không khác biệt nhiều), trừ loại có một "
               "cuộn dây quấn chồng lên cuộn kia và không được tách bằng một màn "
               "chắn nối đất (máy biến áp loại 2a)."))

    # --- printed p.213 (PDF 234) -------------------------------------------
    # --- 9.1.5 The encapsulation process ------------------------------------
    b.append(h3("9.1.5 Quá trình bọc kín", "9.1.5 The encapsulation process"))
    b.append(p("Tiêu chuẩn công nhận hai loại bọc kín. Thứ nhất là nhúng chìm "
               "(embedding), tức là tình huống thông thường chất đóng gói được đổ "
               "vào các mạch điện trong một khuôn sau đó được tháo bỏ, để chất đóng "
               "gói trở thành bộ phận bên ngoài của thiết bị. (Không nhất thiết "
               "phải có khuôn; điểm quan trọng là chất đóng gói là bộ phận bên "
               "ngoài của thiết bị và tiếp xúc với môi trường.)"))
    b.append(p("Thứ hai là đúc bọc (potting), một quá trình tương tự nhưng khuôn "
               "vẫn dính vào chất đóng gói và tạo thành bề mặt bên ngoài của thiết "
               "bị, bảo vệ chất đóng gói khỏi môi trường. Trường hợp khuôn không có "
               "nắp, có thể chấp nhận phủ chất đóng gói bằng một chất đóng gói khác "
               "bám dính vào chất chính nhưng bảo vệ nó khỏi môi trường."))
    b.append(p("Tiêu chuẩn quy định chiều dày tối thiểu của chất đóng gói giữa các "
               "dây dẫn và bề mặt của chất đóng gói là 3 mm, nhưng giảm yêu cầu này "
               "xuống 1 mm khi thiết bị được bọc kín không có bề mặt đơn nào lớn "
               "hơn 2 cm² hoặc được đúc bọc trong khuôn hoặc vỏ bằng kim loại. Khi "
               "khuôn làm bằng vật liệu cách điện thì không có giới hạn tối thiểu, "
               "miễn là khuôn dày ít nhất 1 mm. Ngoài ra, chiều dày của chất đóng "
               "gói quanh một khoảng rỗng, chẳng hạn như hộp rơ le nằm trong chất "
               "đóng gói, phải là 3 mm, trừ khi khoảng rỗng nhỏ hơn 1 cm³ thì chiều "
               "dày có thể giảm xuống 1 mm."))
    b.append(p("Bất cứ thứ gì đi ra khỏi chất đóng gói đều là đường dẫn có thể cho "
               "khí quyển nổ xâm nhập và phải được bịt kín hiệu quả. Tiêu chuẩn gợi "
               "ý rằng 5 mm dây dẫn trần nằm bên trong chất đóng gói là đủ để bảo "
               "đảm bịt kín hiệu quả các cáp nối đi ra khỏi chất đóng gói."))
    b.append(p("Cũng có các yêu cầu tối thiểu về khoảng cách giữa các phần mang "
               "điện trần, dù là trong cùng một mạch, trong hai mạch riêng biệt, "
               "hoặc giữa một mạch với khung (đất) của thiết bị, và các yêu cầu này "
               "được cho trong Bảng 9.1. Rõ ràng là chúng chỉ áp dụng, cũng như mọi "
               "yêu cầu khác, khi hư hỏng sẽ ảnh hưởng đến nguyên lý bảo vệ."))

    # --- 9.1.6 Particular component problems -------------------------------
    b.append(h3("9.1.6 Vấn đề riêng của một số linh kiện",
                "9.1.6 Particular component problems"))
    b.append(p("Như ở nhiều Tiêu chuẩn khác, một số loại linh kiện được tách riêng "
               "vì có vấn đề đặc biệt liên quan đến nguyên lý bảo vệ."))
    b.append(h4("Cầu chì", "Fuses"))
    b.append(p("Để tránh tình trạng chất đóng gói lọt vào bên trong hộp cầu chì, "
               "cầu chì phải thuộc loại có vỏ bọc theo BS 4265 (1977) (1984)¹¹ hoặc "
               "IEC 269.¹² Người ta thừa nhận rằng trong lúc cầu chì bị ngắt, nhiệt "
               "độ của nó có thể vượt quá"))

    # --- printed p.214 (PDF 235): Table 9.1 at its printed source position --
    b.append(table(T91.HEAD91_VI, T91.ROWS91, T91.CAPTION91_VI))
    b.append(note(T91.NOTE91_VI))

    b.append(p("giới hạn nhiệt độ áp dụng cho thiết bị, nhưng miễn là điều đó không "
               "làm hỏng chất đóng gói hoặc không làm nhiệt độ bề mặt ngoài của "
               "chất đóng gói vượt quá phân loại nhiệt độ, thì tình huống đó được "
               "chấp nhận."))
    b.append(h4("Pin hoặc ắc quy", "Cells or batteries"))
    b.append(p("Chỉ các pin, ắc quy hoặc bình ắc quy sơ cấp và thứ cấp không giải "
               "phóng khí hoặc chất điện giải trong điều kiện vận hành bình thường "
               "do nhà chế tạo pin hoặc ắc quy quy định mới được phép bọc kín. Tuy "
               "nhiên, người ta thừa nhận rằng trong hoàn cảnh bất thường các pin "
               "hoặc ắc quy đó có thể giải phóng khí (nhưng không phải chất điện "
               "giải), và phải có phương thức xả khí không làm mất hiệu lực nguyên "
               "lý bảo vệ. Phương thức này thường có dạng một nút chất đóng gói xốp "
               "hoặc một ống mao dẫn dẫn từ đỉnh của pin hoặc ắc quy ra bên ngoài "
               "chất đóng gói. Cũng cần xét đến bất kỳ sự thay đổi kích thước nào do "
               "các yếu tố như nạp điện; thường thì điều này được bù trừ bằng cách "
               "bao quanh pin hoặc ắc quy bằng chất đóng gói mềm trước khi áp dụng "
               "lớp bọc kín tổng thể. Trong những trường hợp đó, cũng cần xác định "
               "cẩn thận các điều kiện nạp điện cần thiết để đạt được mục tiêu này "
               "nếu bộ nạp không phải là một bộ phận cấu thành của thiết bị được "
               "bọc kín."))

    # --- printed p.215 (PDF 236): printed '9.7.7' Type testing --------------
    b.append(h3("9.7.7 Thử nghiệm kiểu", "9.7.7 Type testing"))
    b.append(note("<b>Lưu ý về đánh số.</b> Lớp văn bản in ghi tiêu đề là '9.7.7 "
                  "Type testing', trong khi trang render cho thấy '9.1.7'; vì mục "
                  "này nằm ngay sau 9.1.6 và thuộc phần bọc kín, số đúng gần như "
                  "chắc chắn là 9.1.7. Số in được giữ nguyên thay vì sửa lặng lẽ."))
    b.append(p("Thiết bị được bọc kín phải chịu các thử nghiệm kiểu để bảo đảm "
               "nguyên lý bảo vệ không bị vi phạm trong các điều kiện vận hành "
               "quy định."))
    b.append(p("Thử nghiệm nhiệt độ được tiến hành để bảo đảm sự nóng lên bên "
               "trong không làm vượt quá nhiệt độ tối đa của chất đóng gói hoặc "
               "nhiệt độ làm việc tối đa của thiết bị."))
    b.append(p("Thiết bị cũng được thử nghiệm chu trình nhiệt (xem Hình 9.1) để "
               "bảo đảm không có sự suy giảm nào xảy ra. Các thử nghiệm này được "
               "tiến hành ở điện áp vào tồi tệ nhất trong phạm vi của thiết bị. "
               "Đối với nguồn điện lưới, người ta giả định đó là cộng hoặc trừ 10 "
               "phần trăm. Ngoài ra còn có các thử nghiệm độ bền điện giữa các mạch "
               "riêng biệt, thử nghiệm phóng điện ở nhiệt độ cao hơn nhiệt độ môi "
               "trường tối đa đối với pin và ắc quy, và thử nghiệm kéo đối với các "
               "cáp đi ra khỏi chất đóng gói nhằm bảo đảm tính toàn vẹn của chúng. "
               "Tất cả các thử nghiệm này được quy định chi tiết trong BS 5501, "
               "Phần 8 (1988)³."))
    return "".join(b)


def body_en():
    b = []

    # --- printed p.212 (PDF 233): close of 9.1.3 ---------------------------
    b.append(p("Taking the view above then, the requirements of the concept "
               "become more understandable and realistic."))

    # --- 9.1.4 Encapsulated circuits and components ------------------------
    b.append(h3("9.1.4 Encapsulated circuits and components",
                "9.1.4 Encapsulated circuits and components"))
    b.append(p("The Standard permits a wide range of electrical and electronic "
               "components to be encapsulated, provided that the operating "
               "temperature of such components does not exceed their rating at "
               "the maximum ambient temperature envisaged for operation "
               "(normally 40 °C). Even components such as relays and switches are "
               "permitted, provided that they are themselves enclosed before "
               "being encapsulated. In the case of these components, however, "
               "the maximum volume of their enclosure is limited to 100 cm² and, "
               "if they switch more than 6 A, their enclosure is required to be "
               "inorganic to prevent combustion of its material on arcing or "
               "sparking. The rating of the components used needs to be "
               "sufficient to ensure that they remain within it in case of a "
               "single fault elsewhere, or their failure in the worst possible "
               "way assumed to be a part of that fault. The types of fault which "
               "are considered include, but are not limited to, short or open "
               "circuit of any component, or faults in printed circuitry such as "
               "open circuit failures or shorts between tracks."))
    b.append(p("The apparatus is not permitted anywhere to exceed its specified "
               "operating temperature range in normal operation or fault "
               "conditions, and this may be ensured by an internal thermal trip "
               "provided such a trip is not self-resetting which, in effect, "
               "means that if it operated the apparatus would be at the end of "
               "its useful life."))
    b.append(p("Some components are considered as not subject to faults in the "
               "protection concept if operated at less than two third of their "
               "voltage and power ratings in normal operation, and less than "
               "their voltage and power ratings in a fault condition and these "
               "are: carbon or metal film type resistors; wire wound resistors "
               "with the wire in a single helical layer; plastic foil, paper and "
               "ceramic capacitors."))
    b.append(p("In addition, the following components are considered as not "
               "subject to fault when they satisfy the requirements applied to "
               "them in normal operation and do not exceed their ratings in a "
               "single fault situation."))
    b.append(p("First, optocouplers supplying isolation between separate "
               "circuits if the sum of the voltages of the separated circuits is "
               "less than 1000 V rms and the rated voltage of the optocoupler "
               "between these circuits is at least 1.5 times that voltage sum."))
    b.append(p("Second, transformer and other windings complying with BS 5501, "
               "Part 6 (1977)⁹ (this will include its second edition BS/EN 50019 "
               "(1994)¹⁰, the requirements of which are not dissimilar). In "
               "addition, windings which use wire of less than 0.25mm diameter "
               "which are not permitted by BS 5501, Part 6 (1977)⁹ or its "
               "successor BS/EN 50019 (1994)¹⁰ are permitted, provided they "
               "otherwise comply with those standards and, in addition, are "
               "protected against inadmissible internal temperatures by embedded "
               "thermal cut-outs or similar devices."))
    b.append(p("Third, transformers complying with the requirements for "
               "infallible mains transformers in BS 5501, Part 7 (1977)⁶ (and its "
               "successor BS/EN 50020 (1994)⁷ which is not dissimilar), except "
               "those which have one winding wound over the other and are not "
               "separated by an earthed screen (type 2a transformers)."))

    # --- printed p.213 (PDF 234) -------------------------------------------
    # --- 9.1.5 The encapsulation process ------------------------------------
    b.append(h3("9.1.5 The encapsulation process",
                "9.1.5 The encapsulation process"))
    b.append(p("The standard recognizes two types of encapsulation which are, "
               "first, embedding, which is the situation where normally the "
               "encapsulant is poured over the electrical circuits in a mould "
               "which is later removed, leaving the encapsulant as the outer "
               "part of the apparatus. (A mould may not be necessary, the "
               "important fact being that the encapsulant is the outer part of "
               "the apparatus and is in contact with the environment.)"))
    b.append(p("Second, potting, which is a similar process except that the "
               "mould remains adhered to the encapsulant and forms the external "
               "surface of the apparatus protecting the encapsulant from the "
               "environment. Where the mould does not have a lid, it is "
               "acceptable to cover the encapsulant with another encapsulant "
               "which adheres to the main encapsulant but protects it from the "
               "environment."))
    b.append(p("The Standard defines the minimum thickness of encapsulant "
               "between conductors and the surface of the encapsulant as 3 mm "
               "but reduces this requirement to 1 mm where the encapsulated "
               "apparatus has no single surface greater than 2 cm² or is potted "
               "in a metallic mould or housing. Where the mould is an insulator "
               "there is no minimum limit, provided the mould is at least 1 mm "
               "thick. In addition, the thickness of encapsulant round a void, "
               "such as a relay box within the encapsulant, is required to be "
               "3 mm unless the void is less than 1 cm³ when the thickness is "
               "reducible to 1 mm."))
    b.append(p("Anything exiting the encapsulant is a possible route for entry "
               "of explosive atmosphere and must be effectively sealed. The "
               "Standard suggests that 5 mm of bare conductor within the "
               "encapsulant is acceptable to ensure effective sealing of "
               "connection cables which exit the encapsulant."))
    b.append(p("There are also minimum requirements for separation of bare live "
               "parts be they within the same circuit, in two separate circuits "
               "or one circuit and the frame (earth) of the apparatus and these "
               "are given in Table 9.1. Obviously they only apply, as do all "
               "other requirements, where failure will affect the protection "
               "concept."))

    # --- 9.1.6 Particular component problems -------------------------------
    b.append(h3("9.1.6 Particular component problems",
                "9.1.6 Particular component problems"))
    b.append(p("As in many of the other Standards, certain types of component "
               "are singled out as having particular problems insofar as the "
               "protection concept is concerned."))
    b.append(h4("Fuses", "Fuses"))
    b.append(p("To avoid problems with ingress of encapsulant into the fuse "
               "cartridge, fuses are required to be enclosed types to BS 4265 "
               "(1977) (1984)¹¹ or IEC 269.¹² It is recognized that during "
               "rupturing such fuses might exceed the"))

    # --- printed p.214 (PDF 235): Table 9.1 at its printed source position --
    b.append(table(T91.HEAD91_EN, T91.ROWS91, T91.CAPTION91_EN))
    b.append(note(T91.NOTE91_EN))

    b.append(p("limits applied to the apparatus, but provided this does not "
               "damage the encapsulant or cause the external encapsulant "
               "temperature to exceed the temperature classification, such a "
               "situation is acceptable."))
    b.append(h4("Cells or batteries", "Cells or batteries"))
    b.append(p("Only primary and secondary cells, batteries or accumulators "
               "which do not release gas or electrolyte in the normal operating "
               "conditions specified by the manufacturer of the cell or battery "
               "may be encapsulated. It is, however, recognized that in abnormal "
               "circumstances such cells or batteries may release gas (but not "
               "electrolyte) and there must be a method of release of the gas "
               "which does not defeat the protection concept. This often takes "
               "the form of a plug of porous encapsulant or a capillary from the "
               "top of the cell or battery to the outside of the encapsulant. "
               "It is also necessary to consider any dimension variation due to "
               "such things as charging and this is usually accommodated by "
               "surrounding the cells or batteries in soft encapsulant before "
               "the overall encapsulation is applied. In such cases it is also "
               "necessary to carefully define the charging conditions necessary "
               "to achieve this objective if the charger is not a component "
               "part of the encapsulated apparatus."))

    # --- printed p.215 (PDF 236): printed '9.7.7' Type testing --------------
    b.append(h3("9.7.7 Type testing", "9.7.7 Type testing"))
    b.append(note("<b>Numbering note.</b> The printed text layer gives this "
                  "heading as '9.7.7 Type testing' while the page render reads "
                  "'9.1.7'; since this section follows 9.1.6 and belongs to "
                  "encapsulation, the intended number is almost certainly "
                  "9.1.7. The printed form is retained rather than being "
                  "silently corrected."))
    b.append(p("Encapsulated apparatus is subject to type tests to ensure that "
               "the protection concept is not breached within the specified "
               "operating conditions."))
    b.append(p("Temperature testing is carried out to ensure that internal "
               "heating does not cause the maximum temperature of the "
               "encapsulant, or the maximum operating temperature of the "
               "apparatus, to be exceeded."))
    b.append(p("The apparatus is also subjected to a temperature cycling test "
               "(see Fig. 9.1) to ensure that no deterioration takes place. "
               "These tests are carried out at the worst possible input voltage "
               "in the range of the apparatus. For mains supplies this is "
               "assumed to be plus or minus 10 per cent. There are also electric "
               "strength tests between separate circuits, discharge tests at "
               "above maximum ambient temperature for cells and batteries, and "
               "pull tests on cables which exit the encapsulant to ensure their "
               "integrity. These are all detailed in BS 5501, Part 8 (1988)³."))
    return "".join(b)
