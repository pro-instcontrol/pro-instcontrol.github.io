# -*- coding: utf-8 -*-
"""Chapter 9, module D - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 218-220 (PDF pp. 239-241).

Covers 9.2.3 Requirements for the protective fluid (oil), 9.2.4 External
connections, 9.2.5 Type testing, the opening of 9.3 Powder filling - 'q',
9.3.1 The filling material and 9.3.2 The enclosure. Owns Figure 9.2, the
leakage measuring technique, emitted between the two parts of 9.3.2 at its
printed source position. The chapter h2, the references and the end matter
belong to the integration shell and are not emitted here.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h2, h3, h4, p, note, table, fig
import mcmillanfig09 as F


def body_vi():
    b = []

    # --- printed p.218 (PDF 239): 9.2.3 ---
    b.append(h4("9.2.3 Yêu cầu đối với chất lỏng bảo vệ (dầu)",
                "9.2.3 Requirements for the protective fluid (oil)"))
    b.append(p("Chất lỏng bảo vệ phải ngâm mọi mạch điện đến độ sâu ít nhất "
               "25mm khi dầu ở mức thấp nhất. Rõ ràng là giá trị 25mm này "
               "không áp dụng cho sự cách ly giữa các mạch đó và vỏ bọc, "
               "nhưng các sự cố chạm vỏ cần được xem xét trong quá trình "
               "thiết kế để đảm bảo vỏ bọc không thể bị vỡ do các sự cố điện."))
    b.append(p("BS 5501, Phần 2 (1977) chỉ cho phép dùng dầu phù hợp với IEC "
               "296 (1969).¹⁸ Điều này khá hạn chế và để khắc phục, BS/EN "
               "50015 (1994)¹³ trong khi vẫn cho phép các loại dầu theo Tiêu "
               "chuẩn IEC được cập nhật (IEC 296 (1982))¹⁹ cũng cho phép các "
               "loại dầu khác, miễn là chúng đáp ứng các yêu cầu sau:"))
    b.append(p("điểm cháy của chúng phải cao hơn 300 °C (IEC 836 (1988), "
               "phương pháp thứ nhất);²⁰"))
    b.append(p("điểm bốc cháy của chúng phải vượt quá 200 °C (BS 6664, Phần "
               "5 (1990), cốc kín);²²"))
    b.append(p("độ nhớt động học lớn nhất của chúng ở 25 °C không được vượt "
               "quá 100cSt (ISO 3104 (1976)).²¹"))
    b.append(p("độ bền điện môi của chúng phải ít nhất 27kV (BS 5874 "
               "(1980)²² hoặc, trong trường hợp chất lỏng silicon, IEC 836 "
               "(1988));²⁰"))
    b.append(p("điện trở suất thể tích của chúng phải ít nhất 10¹⁴ Ω ở "
               "25 °C (BS 5737 (1979));²³"))
    b.append(p("điểm đông đặc của chúng phải là −30 °C hoặc thấp hơn (BS "
               "2000 Phần 15 (1993));²⁴"))
    b.append(p("độ axit của chúng không được vượt quá 0.03mg KOH/g "
               "(IEC 588-2 (1978)).²⁵"))
    b.append(p("Rõ ràng đây là những đặc tính khá nghiêm ngặt nhưng lý do "
               "của từng đặc tính là rõ ràng và chúng thể hiện sự mở rộng "
               "lựa chọn, đặc biệt là vì tất cả những gì cần thiết chỉ là "
               "chứng minh rằng đặc tính của loại dầu do nhà chế tạo đưa ra "
               "đáp ứng các yêu cầu này, thay vì phải chứng minh bằng phép "
               "thử."))

    # --- printed p.218 (PDF 239): 9.2.4 ---
    b.append(h4("9.2.4 Đầu nối bên ngoài", "9.2.4 External connections"))
    b.append(p("Rất khó có khả năng các phương tiện đấu nối bên ngoài có thể "
               "thực tế được ngâm trong dầu và vì vậy phải giả định là chúng "
               "đi ra khỏi dầu. Do đó, để đạt được an toàn, chúng cần được "
               "bảo vệ bằng một khái niệm bảo vệ khác (ví dụ, An toàn tăng "
               "cường BS/EN 50019)¹⁰ tại nơi ngâm dầu không còn hiệu lực, "
               "nghĩa là kể từ điểm mà chúng đi ra khỏi vỏ bọc chứa dầu "
               "hoặc, nếu dầu có bề mặt tự do trong buồng đầu cuối, kể từ "
               "điểm nằm 25mm dưới bề mặt dầu trở lên và vượt qua bề mặt đó."))

    # --- printed pp.218-219 (PDF 239-240): 9.2.5 ---
    b.append(h4("9.2.5 Thử nghiệm kiểu", "9.2.5 Type testing"))
    b.append(p("Thử nghiệm kiểu riêng của thiết bị ngâm dầu chỉ giới hạn ở "
               "các phép thử sau đây đối với vỏ bọc. Vỏ bọc kín được thử cả "
               "áp suất dư và áp suất âm. Phép thử áp suất dư nhằm xác định "
               "độ bền của vỏ bọc và gồm một áp suất dư ít nhất bằng 1.5 lần "
               "giá trị cài đặt của thiết bị giảm áp áp dụng lên vỏ bọc, "
               "được chứa đầy dầu trong 60 giây. Không mong đợi có hư hỏng "
               "hoặc biến dạng đáng kể của vỏ bọc. Phép thử áp suất âm được "
               "thiết kế để kiểm tra độ kín. Phép thử này gồm việc đổ đầy "
               "dầu vào vỏ bọc đến mức tối đa rồi hạ mức xuống mức tối thiểu. "
               "Áp suất giảm phải được duy trì ít nhất 24 giờ với độ biến "
               "thiên không lớn hơn 5 phần trăm. Vỏ bọc không kín chỉ chịu "
               "phép thử áp suất dư, khi đó phép thử được thực hiện ở áp "
               "suất bằng 1.5 lần áp suất khí quyển, tất cả các thông số "
               "thử khác giữ nguyên."))

    # --- printed p.219 (PDF 240): opening of 9.3 ---
    b.append(h3("9.3 Nhồi bột – 'q'", "9.3 Powder filling - 'q'"))
    b.append(p("<b>BS/EN 50017 (1994)²⁶</b>"))
    b.append(p("Nhìn thoáng qua, khái niệm bảo vệ này là một phương pháp "
               "khác để cách ly các mạch điện khỏi khí quyển nổ bằng cách "
               "bao quanh chúng bằng bột. Tuy nhiên, điều này không hoàn "
               "toàn đúng, vì khác với các thứ như ngâm dầu, khí quyển nổ "
               "có thể thấm vào vật liệu điền đầy và, về mặt lý thuyết, có "
               "thể bị bắt lửa nếu các bộ phận có khả năng gây cháy nằm bên "
               "trong vật liệu điền đầy. Điều thực sự xảy ra ở đây là ngọn "
               "lửa không thể lan truyền ra ngoài vật liệu điền đầy do hiệu "
               "ứng dập tắt tạo ra. Trong ngữ cảnh này, vật liệu điền đầy có "
               "chức năng khá khác biệt và đóng vai trò quan trọng hơn."))

    # --- printed p.219 (PDF 240): 9.3.1 ---
    b.append(h4("9.3.1 Vật liệu điền đầy", "9.3.1 The filling material"))
    b.append(p("Vật liệu điền đầy chỉ được dùng hạt thạch anh hoặc hạt thủy "
               "tinh rắn với giới hạn kích thước cho phép nó đi qua một rây "
               "kim loại có lỗ 1 mm nhưng không đi qua rây có lỗ 0.5mm (xem "
               "ISO 565 (1990)²⁷). Vật liệu điền đầy cũng được yêu cầu có "
               "dòng rò nhỏ hơn 1 µA khi đặt 1OOOV dc vào hệ điện cực như "
               "thể hiện trên Hình 9.2, được nhúng trong vật liệu điền đầy "
               "sao cho nó được bao quanh đến khoảng cách ít nhất 1 cm (xem "
               "thêm Mục 9.3.5)."))
    b.append(note("<b>Ghi chú về điện áp trong bản in.</b> Nguyên bản in "
                  "'1OOOV dc' (với hai chữ O viết hoa) để chỉ 1000 V dc; "
                  "cách in này được giữ nguyên ở trên."))

    # --- printed pp.219-220 (PDF 240-241): 9.3.2 ---
    b.append(h4("9.3.2 Vỏ bọc", "9.3.2 The enclosure"))
    b.append(p("Nhìn chung, vỏ bọc phải chắc chắn về cơ khí nhưng không cần "
               "phép thử đặc biệt nào khác ngoài các phép thử trong BS/EN "
               "50014 (1993)⁵. Cách làm vỏ bọc cũng phải sao cho không có "
               "vật liệu điền đầy thoát ra và BS/EN 50017 (1994)²⁶ quy định "
               "khe hở của bất kỳ lỗ nào trên vỏ bọc phải nhỏ hơn kích "
               "thước nhỏ nhất của hạt điền đầy ít nhất 0.1 mm. IP54 theo "
               "BS/EN 60529¹⁷ được quy định là mức bảo vệ xâm nhập tối thiểu "
               "và, khi mức bảo vệ của vỏ bọc vượt quá IP55, cần có một "
               "thiết bị thở đạt IP54. Tất cả vỏ bọc đều chịu một phép thử "
               "kiểu ở 1.5 × 10⁵ N/m² tuyệt đối, để đảm bảo độ bền thích "
               "ứng, nhưng khi chúng không có lỗ thông hơi và có chứa các "
               "tụ điện phân lớn, ví dụ (thể tích tụ điện lớn hơn một phần "
               "tám thể tích vật liệu điền đầy), áp suất thử này được tăng "
               "lên 15 × 10⁵ N/m² tuyệt đối."))

    b.append(fig(2, F.fig_f902()))

    b.append(p("Khi điền đầy vỏ bọc, cần đảm bảo vật liệu điền đầy thấm "
               "toàn bộ và điều này có thể yêu cầu lắc trong khi điền. Vỏ "
               "bọc sau khi điền không được thiết kế để mở trong quá trình "
               "sử dụng và phải được đóng bằng cách hàn, hàn thiếc hoặc "
               "xi măng để ngăn điều đó."))

    return "".join(b)


def body_en():
    b = []

    # --- printed p.218 (PDF 239): 9.2.3 ---
    b.append(h4("9.2.3 Requirements for the protective fluid (oil)",
                "9.2.3 Requirements for the protective fluid (oil)"))
    b.append(p("The protective fluid is required to immerse any electrical "
               "circuits to a depth of at least 25mm with the oil at its "
               "lowest level. Clearly, this 25mm does not apply to separation "
               "between those circuits and the enclosure but faults to the "
               "enclosure need to be taken into consideration during design "
               "to ensure that the enclosure cannot be ruptured by electrical "
               "faults."))
    b.append(p("BS 5501, Part 2 (1977) limited the oil to that conforming to "
               "IEC 296 (1969).¹⁸ This was quite restrictive and to overcome "
               "this BS/EN 50015 (1994),¹³ while still permitting oils to the "
               "updated IEC Standard (IEC 296 (1982))¹⁹ also permits other "
               "oils provided they satisfy the following:"))
    b.append(p("their fire points must be above 300 °C (IEC 836 (1988), "
               "first method);²⁰"))
    b.append(p("their flash points shall exceed 200 °C (BS 6664, Part 5 "
               "(1990), closed cup);²²"))
    b.append(p("their maximum kinematic viscosity at 25 °C must not exceed "
               "100cSt (ISO 3104 (1976)).²¹"))
    b.append(p("their electrical breakdown strength must be at least 27kV "
               "(BS 5874 (1980)²² or, in the case of silicone fluids, "
               "IEC 836 (1988));²⁰"))
    b.append(p("their volume resistivity must be at least 10¹⁴ Ω at 25 °C "
               "(BS 5737 (1979));²³"))
    b.append(p("their pour point must be −30 °C or lower (BS 2000 Part 15 "
               "(1993));²⁴"))
    b.append(p("their acidity must not exceed 0.03mg KOH/g "
               "(IEC 588-2 (1978)).²⁵"))
    b.append(p("Clearly these are fairly restrictive specifications but the "
               "reason for each of them is apparent and they represent a "
               "widening of choice, particularly as all that is required is "
               "to demonstrate that the specification of the oil used by its "
               "manufacturer meets these requirements, rather than have to "
               "prove it by test."))

    # --- printed p.218 (PDF 239): 9.2.4 ---
    b.append(h4("9.2.4 External connections", "9.2.4 External connections"))
    b.append(p("It is highly unlikely that the external connection facilities "
               "could practically be immersed in oil and so it must be "
               "assumed that they exit the oil. To achieve safety, therefore, "
               "they need to be protected by another protection concept "
               "(e.g., Increased Safety BS/EN 50019)¹⁰ where the oil immersion "
               "is ineffective, which means from the point where they exit "
               "the oil-filled enclosure or, if the oil has a free surface "
               "within the terminal chamber, from a point 25mm below the oil "
               "surface to and beyond the surface."))

    # --- printed pp.218-219 (PDF 239-240): 9.2.5 ---
    b.append(h4("9.2.5 Type testing", "9.2.5 Type testing"))
    b.append(p("Specific type testing of oil-immersed apparatus is limited to "
               "following testing of enclosures. Sealed Enclosures are "
               "subjected to both overpressure and underpressure tests. The "
               "overpressure test is intended to identify enclosure strength "
               "and consists of an overpressure of at least 1.5 times the "
               "pressure setting of the pressure relief device applied to the "
               "enclosure, filled with oil for 60 seconds. No significant "
               "enclosure damage or distortion is expected. The underpressure "
               "test is designed to test the sealing. This consists of filling "
               "the enclosure to its maximum level with oil and then reducing "
               "the level to the minimum. The reduced pressure must be "
               "maintained for at least 24 hours with no variation greater "
               "than 5 per cent. Unsealed enclosures are subjected only to the "
               "overpressure test which, in this case, is carried out at 1.5 "
               "times atmospheric pressure, all other test parameters being "
               "the same."))

    # --- printed p.219 (PDF 240): opening of 9.3 ---
    b.append(h3("9.3 Powder filling – 'q'", "9.3 Powder filling – 'q'"))
    b.append(p("<b>BS/EN 50017 (1994)²⁶</b>"))
    b.append(p("At first glance, this protection concept is a further method "
               "of separating the electrical circuits from the explosive "
               "atmosphere by surrounding them with powder. This is not "
               "strictly true, however, as unlike such things as oil immersion "
               "the explosive atmosphere can penetrate the filling and, "
               "theoretically, may be ignited if ignition-capable parts are "
               "within the filling. What actually happens here is that the "
               "ignition cannot propagate outside the filling material "
               "because of the quenching effect produced. In this context "
               "the filling material has a somewhat different function and "
               "is more critical."))

    # --- printed p.219 (PDF 240): 9.3.1 ---
    b.append(h4("9.3.1 The filling material", "9.3.1 The filling material"))
    b.append(p("The filling material is limited to quartz or solid glass "
               "particles with size limits which will permit it to pass "
               "through a metal sieve of 1 mm aperture but not one with an "
               "aperture of 0.5mm (see ISO 565 (1990)²⁷). The filling material "
               "is also required to have a leakage current of less than 1 µA "
               "when 1OOOV dc is applied to an electrode system shown in "
               "Fig. 9.2, which is immersed in the filling material so that "
               "it is surrounded to a distance of at least 1 cm (see also "
               "Section 9.3.5)."))
    b.append(note("<b>Note on the printed voltage.</b> The original prints "
                  "'1OOOV dc' (with two capital letter O's) for 1000 V dc; "
                  "the printed form is retained above."))

    # --- printed pp.219-220 (PDF 240-241): 9.3.2 ---
    b.append(h4("9.3.2 The enclosure", "9.3.2 The enclosure"))
    b.append(p("In general terms the enclosures must be mechanically robust "
               "but no special tests other than those in BS/EN 50014 (1993)⁵ "
               "are considered necessary. The method of enclosure must also "
               "be such that no filling escapes and BS/EN 50017 (1994)²⁶ "
               "specifies any enclosure aperture as not having any opening "
               "more than 0.1 mm less than the minimum filling dimension. "
               "IP54 to BS/EN 60529¹⁷ is specified as the minimum ingress "
               "protection and, where the enclosure protection exceeds IP55, "
               "a breathing device giving IP54 is required. All enclosures "
               "are subjected to a type test of 1.5 × 10⁵ N/m² absolute, to "
               "ensure their adequate strength but where they do not contain "
               "breathing openings and do contain large electrolytic "
               "capacitors, for example, (capacitor volumes greater than one "
               "eighth of the filling material volume) this pressure test is "
               "increased to 15 × 10⁵ N/m² absolute."))

    b.append(fig(2, F.fig_f902()))

    b.append(p("When filling the enclosure it is necessary to ensure total "
               "penetration of the filling material and this may require "
               "shaking during filling. The filled enclosure is then not "
               "intended to be opened in service and closure should be by "
               "welding, soldering or cementing to prevent this."))

    return "".join(b)
