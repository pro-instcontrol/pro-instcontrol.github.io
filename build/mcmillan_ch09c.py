# -*- coding: utf-8 -*-
"""Chapter 9, module C (writer W3) - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), raw lines 10122-10212 / printed pp.215-217
(PDF pp.236-238).

Covers the opening of 9.2 Oil immersion - 'o' with its BS/EN 50015 (1994)
standard line, the printed "9.2.7" construction section (preserved with a
bilingual note: almost certainly 9.2.1), and 9.2.2 Containment of the oil:
sealed and non-sealed enclosures, the breathing device and the Fig. 9.1
legend A-E, oil-level indicators, and the protection of fasteners. Owns
Figure 9.1 only; emits fig(1, ...) at the source position in both bodies.
No tables, no chapter h2, no references and no end matter. Wording,
standards designations, reference superscripts and printed quirks follow
the verified survey brief and the page renders, not the garbled PDF text
layer. VI follows the intended meaning; EN retains the printed quirks.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h2, h3, h4, p, note, table, fig
import mcmillanfig09 as F


def body_vi():
    b = []

    b.append(h3("9.2 Ngâm dầu – 'o'",
                "9.2 Oil immersion – 'o'"))
    b.append(p("<b>(BS/EN 50015, (1994))¹³</b>"))
    b.append(p("Đây lại là một loại hình bảo vệ trong đó khí quyển nổ bị ngăn "
               "không tiếp cận được các mạch điện nhờ việc nhúng các mạch đó "
               "trong dầu. Ban đầu Tiêu chuẩn này bao phủ một phạm vi thiết bị "
               "rộng hơn, bao gồm cả thiết bị đóng cắt (xem BS 5501, Phần 2 "
               "(1977))¹⁴, nhưng ấn bản thứ hai, BS/EN 50015 (1994)¹³, giới hạn "
               "khái niệm bảo vệ này ở những thiết bị không có khả năng gây cháy "
               "nổ khí quyển nổ trong vận hành bình thường (xem Chương 15) và "
               "có thể được sử dụng ở Khu vực 2 mà không cần ngâm dầu. Thiết bị "
               "theo BS 5501, Phần 2 (1977)¹⁴ sẽ không được thảo luận ở đây, vì "
               "ở Anh chưa từng dùng thiết bị nào khác ngoài thiết bị tuân thủ "
               "BS/EN 50015 (1994)¹³, và không nên dùng loại nào khác trong "
               "tương lai. Nếu bất kỳ thiết bị nào được chế tạo để ngâm dầu "
               "trước Chỉ thị 76/117/EEC¹, nên cho thiết bị đó tuân thủ các "
               "yêu cầu trong BS/EN 50015 (1994)¹³ về kết cấu của chính thiết "
               "bị điện."))

    b.append(h4("9.2.7 Kết cấu của thiết bị",
                "9.2.7 Construction of the apparatus"))
    b.append(note("<b>Lưu ý về số mục được in.</b> Tiêu đề trong bản in ghi là "
                  "'9.2.7'. Vì đây là mục đầu tiên của loại hình bảo vệ ngâm "
                  "dầu, ngay sau phần mở đầu của 9.2 và trước mục 9.2.2, số này "
                  "hầu như chắc chắn là lỗi in của 9.2.1. Bản dịch giữ nguyên "
                  "số in 9.2.7 thay vì sửa lặng lẽ."))
    b.append(p("Các yêu cầu cơ bản về kết cấu của chính thiết bị không xuất "
               "hiện trong Tiêu chuẩn này. Thay vào đó, Tiêu chuẩn viện dẫn "
               "thiết bị tuân thủ IEC 79-15 (1987)¹⁵, vốn bao phủ các thiết bị "
               "có loại hình bảo vệ 'n'. Tiêu chuẩn này vẫn chưa được chấp nhận "
               "đầy đủ ở Anh, vì vậy các yêu cầu về kết cấu nên lấy theo văn bản "
               "tương đương của Anh là BS 6941 (1988).¹⁶ Trên thực tế, điều này "
               "tạo ra rất ít khác biệt, vì sự khác nhau giữa Tiêu chuẩn Anh và "
               "Tiêu chuẩn IEC tập trung quanh khái niệm thở hạn chế, vốn dĩ "
               "không phù hợp với việc ngâm dầu. Nên tham khảo Chương 15 của "
               "cuốn sách này để biết các yêu cầu cơ bản về kết cấu thiết bị."))

    b.append(h4("9.2.2 Chứa đựng dầu",
                "9.2.2 Containment of the oil"))
    b.append(p("Dầu được yêu cầu phải được chứa bên trong thiết bị bằng một "
               "trong hai phương pháp sau. Dầu có thể nằm trong thiết bị được "
               "bịt kín ngay trong giai đoạn chế tạo; khi đó vỏ bọc phải có khả "
               "năng chịu được áp suất bên trong lớn nhất xảy ra ở nhiệt độ tối "
               "đa khi thiết bị đang vận hành và dầu ở mức tối đa. Tiêu chuẩn "
               "yêu cầu lắp một thiết bị giảm áp ngay trong giai đoạn chế tạo; "
               "thiết bị này hoạt động ở mức 1,1 lần áp suất đó và được bịt kín "
               "để ngăn can thiệp. Bịt kín trong trường hợp này không nhất thiết "
               "có nghĩa là hàn kín kiểu nóng chảy, và các vỏ bọc có gioăng đệm "
               "được chấp nhận cho mục đích này. Mặc dù việc bịt kín vỏ bọc "
               "không được BS 5501, Phần 2 (1977)¹⁴ nêu rõ như một phương pháp "
               "chứa dầu, nhưng từ ngữ trong Tiêu chuẩn đó đủ mơ hồ để cho phép "
               "cách làm này. Các vỏ bọc bịt kín phải chịu thử quá áp ở mức 1,5 "
               "lần giá trị cài đặt của thiết bị giảm áp và thử rò rỉ ở áp suất "
               "giảm để bảo đảm độ bền và khả năng bịt kín của chúng. Những "
               "phép thử này không được yêu cầu bởi BS 5501, Phần 2 (1977)¹⁴."))
    b.append(p("Hoặc dầu phải nằm trong một vỏ bọc có ít nhất mức bảo vệ IP66 "
               "theo BS/EN 60529 (1991)¹⁷ (xem cũng Chương 8). Trong trường hợp "
               "này, phải có một thiết bị cho phép hơi từ dầu thoát ra mà không "
               "gây áp suất trong vỏ bọc, và thiết bị thở này phải có chất hút "
               "ẩm để ngăn nước hoặc hơi nước xâm nhập làm suy giảm chất lượng "
               "dầu. Tiêu chuẩn yêu cầu thiết bị thở đạt ít nhất IP 23 theo "
               "BS/EN 60529 (1991)¹⁷. Dù đây là mức bảo vệ chống xâm nhập khá "
               "thấp, cần cẩn trọng bảo đảm mọi thiết bị thở đều phù hợp với "
               "các vị trí lắp đặt dự kiến. Ví dụ, nếu thiết bị nằm ở các vị trí "
               "ngoài trời thông thường của nhà máy công nghiệp, phải dự kiến "
               "việc xịt rửa các vị trí đó bằng vòi nước, và thiết bị thở sẽ "
               "cần một dạng cửa thoát hướng xuống để ngăn nước xâm nhập làm "
               "quá tải chất hút ẩm. Một bố trí điển hình được thể hiện trong "
               "Hình 9.1."))
    b.append(p("Thiết bị không bịt kín được yêu cầu có một cơ cấu ngắt để cắt "
               "nguồn điện cung cấp cho thiết bị trong điều kiện sự cố (hồ "
               "quang bên trong hoặc nhiệt độ quá cao do dòng quá tải đáng kể "
               "gây ra bởi các sự cố bên trong) khi có khả năng phân hủy dầu. "
               "Vì các hoàn cảnh gây ra vấn đề này gần như chắc chắn sẽ tạo ra "
               "dòng quá tải thoáng qua hoặc liên tục, cơ cấu ngắt quá tải là "
               "phương pháp có khả năng nhất để thực hiện việc này, nhưng cũng "
               "cần lưu ý rằng cơ cấu ngắt không được tự thiết lập lại hoặc có "
               "thể thiết lập lại từ xa. Cơ cấu ngắt như vậy chỉ được phép "
               "thiết lập lại tại chỗ và bằng tay. Vỏ bọc không bịt kín không "
               "cần thử rò rỉ nhưng phải chịu được phép thử áp suất ở mức "
               "1,5 × 10⁵ N/m² tuyệt đối để bảo đảm độ bền đủ. Phép thử này "
               "không được yêu cầu bởi BS 5501, Phần 2 (1977)¹⁴."))

    b.append(fig(1, F.fig_f901()))
    b.append(p("Chú giải Hình 9.1 trong bản in: 'Ví dụ về thiết bị thở để ngăn "
               "nước. A = Vỏ bọc, B = Chất hút ẩm, C = Gioăng, D = Giá đỡ chất "
               "hút ẩm, trong đó cả ba bộ phận được cố định với nhau bằng hàn, "
               "hàn thiếc, xi măng hoặc có các gioăng xen kẽ để ngăn hơi ẩm xâm "
               "nhập; E = Cửa thoát hướng xuống được cố định vào giá đỡ chất "
               "hút ẩm bằng hàn, hàn thiếc hoặc vặn vít. Lưu ý: Giá đỡ chất hút "
               "ẩm được cố định vào vỏ bọc theo cách được BS/EN 50015 (1994) "
               "chấp nhận.'"))

    b.append(p("Tất cả thiết bị, dù bịt kín hay không bịt kín, đều cần có một "
               "chỉ báo xác định mức dầu tối đa và tối thiểu được chấp nhận "
               "trong mọi điều kiện bình thường. Đối với thiết bị không bịt "
               "kín, chỉ báo này có thể là que thăm dầu nếu que được cố định "
               "vào thiết bị trong điều kiện bình thường (nghĩa là nó tạo thành "
               "một phần của vỏ bọc và đáp ứng các yêu cầu bảo vệ chống xâm "
               "nhập vào những lúc không sử dụng để kiểm tra mức dầu). Hoặc nó "
               "có thể là một thiết bị như ống nhìn xuyên hoặc các cửa sổ quan "
               "sát mức trên vỏ bọc; khi đó vật liệu không được dầu làm suy "
               "giảm theo cách gây mất độ bền hoặc làm mờ khuất tầm nhìn, và "
               "phải được bố trí sao cho, trừ khi nó được bảo vệ khỏi những thứ "
               "như va đập để có thể bỏ qua hư hỏng trong vận hành bình thường, "
               "sự hỏng của nó không cho phép mức dầu giảm xuống dưới mức tối "
               "thiểu được chấp nhận."))
    b.append(p("Tất cả các chi tiết bắt vít liên quan trực tiếp đến khái niệm "
               "bảo vệ đều cần được bảo vệ khỏi bị tháo hoặc nới lỏng ngoài ý "
               "muốn bởi nhân viên, hoặc bởi các yếu tố như rung động. Mặc dù "
               "Tiêu chuẩn này hay Tiêu chuẩn tiền nhiệm đều không yêu cầu dùng "
               "ốc vít đặc biệt (xem BS/EN 50014 (1993)⁵), BS/EN 50015 "
               "(1994)¹³ đưa ra gợi ý về những gì được chấp nhận, và các biện "
               "pháp sau được nêu: mũ che quanh đầu bu lông; xi măng hóa ren; "
               "lắp vòng đệm khóa; và buộc dây đầu bu lông. Việc chọn bất kỳ "
               "biện pháp nào trong số đó hoặc biện pháp tương đương là tùy "
               "thuộc vào nhà sản xuất trong từng trường hợp cụ thể, nhưng tính "
               "phù hợp sẽ cần được chứng minh và, trong trường hợp dùng biện "
               "pháp tương đương, cần chứng minh cả tính tương đương."))
    return "".join(b)


def body_en():
    b = []

    b.append(h3("9.2 Oil immersion – 'o'",
                "9.2 Oil immersion – 'o'"))
    b.append(p("<b>(BS/EN 50015, (1994))¹³</b>"))
    b.append(p("This type of protection is again one where the explosive "
               "atmosphere is prevented from accessing the electrical circuits "
               "by their immersion in oil. Originally a wide range of apparatus "
               "was covered by the Standard including switchgear (see BS 5501, "
               "Part 2 (1977))¹⁴ but the second edition, BS/EN 50015 (1994)¹³, "
               "limits the protection concept to apparatus which is not capable "
               "of causing an ignition of an explosive atmosphere in normal "
               "operation (see Chapter 15) and would be usable in Zone 2 without "
               "oil immersion. Apparatus in accordance with BS 5501, Part 2 "
               "(1977)¹⁴ will not be discussed as no apparatus other than that "
               "which would comply with BS/EN 50015 (1994)¹³ has been used in "
               "the UK and it is not recommended that any is in the future. If "
               "any apparatus is constructed for oil immersion before Directive "
               "76/117/EEC¹ it is recommended that it complies with the "
               "requirements in BS/EN 50015 (1994)¹³ in respect of construction "
               "of the electrical apparatus itself."))

    b.append(h4("9.2.7 Construction of the apparatus",
                "9.2.7 Construction of the apparatus"))
    b.append(note("<b>Note on the printed section number.</b> The printed "
                  "heading reads '9.2.7'. Since this is the first section of "
                  "the oil-immersion protection concept, following the opening "
                  "of 9.2 and preceding section 9.2.2, this is almost certainly "
                  "a printing error for 9.2.1. The translation retains the "
                  "printed number 9.2.7 rather than silently correcting it."))
    b.append(p("The basic constructional requirements for the apparatus itself "
               "do not appear in this Standard. Instead, it refers to apparatus "
               "complying with IEC 79-15 (1987)¹⁵ which covers apparatus with "
               "type of protection 'n'. This standard is not yet fully accepted "
               "in the UK and the constructional requirements should be those "
               "given in the UK equivalent which is BS 6941 (1988).¹⁶ In "
               "reality, this makes little difference as the differences between "
               "the British Standard and the IEC Standard centre around the "
               "restrictive breathing concept which does not lend itself to oil "
               "immersion in any event. Chapter 15 of this book should be "
               "consulted for the basic apparatus construction requirements."))

    b.append(h4("9.2.2 Containment of the oil",
                "9.2.2 Containment of the oil"))
    b.append(p("The oil is required to be contained within the apparatus by one "
               "of the following two methods. It may be within an apparatus "
               "sealed at the manufacturing stage, in which case the enclosure "
               "must be capable of withstanding the maximum internal pressure "
               "which occurs at maximum temperature with the apparatus in "
               "operation and the oil at maximum level. The Standard requires a "
               "pressure relief device installed at the time of manufacture "
               "which operates at 1.1 times that pressure, and is sealed to "
               "prevent interference. Sealing in this context does not "
               "necessarily mean fusion-type sealing and gasketted enclosures "
               "are acceptable for this purpose. While sealing of enclosures is "
               "not specifically identified in BS 5501, Part 2 (1977)¹⁴ as a "
               "means of oil containment, the wording in that Standard is "
               "sufficiently vague to permit it. Sealed enclosures are subject "
               "to overpressure tests at 1.5 times the setting of the pressure "
               "relief device and leakage tests at reduced pressure to ensure "
               "their strength and sealing capabilities. These tests were not "
               "required by BS 5501, Part 2 (1977)¹⁴."))
    b.append(p("Alternatively, it must be in an enclosure which has at least an "
               "IP rating of IP66 to BS/EN 60529 (1991)¹⁷ (see also Chapter 8). "
               "In this case, there must be a device to permit breathing of "
               "vapours from the oil without any pressurization of the enclosure "
               "and the breathing device will have to have a desiccant to "
               "prevent the ingress of water or water vapour which will degrade "
               "the oil. The Standard requires the breathing device to achieve "
               "at least IP 23 to BS/EN 60529 (1991)¹⁷. While this is a fairly "
               "low level of ingress protection, care needs to be taken to "
               "ensure that any breathing device is suitable for intended "
               "locations of installation. If, for example, the apparatus is in "
               "normal outdoor process plant locations hosing of those locations "
               "must be expected and the breathing device will need some form "
               "of downward facing outlet to stop ingress of water which would "
               "overburden the desiccant. A typical arrangement is shown in "
               "Fig. 9.1."))
    b.append(p("Non-sealed apparatus is required to have a trip which isolates "
               "the electrical supply to the apparatus in conditions of fault "
               "(internal arcs or excessively high temperatures caused by "
               "significant overcurrent due to internal faults) where oil "
               "decomposition is likely. Because the circumstances giving rise "
               "to this problem are almost certain to produce either transient "
               "or continuous overcurrent, an overcurrent trip is the most "
               "likely method of achieving this, but it must also be noted that "
               "the trip must not be self resetting or capable of being reset "
               "remotely. Such a trip must only be capable of being reset "
               "locally and manually. Non-sealed enclosures need no leakage "
               "test but must be capable of withstanding a pressure test at "
               "1.5 × 10⁵ N/m² absolute to ensure they have sufficient "
               "strength. This test was not required by BS 5501, Part 2 "
               "(1977)¹⁴."))

    b.append(fig(1, F.fig_f901()))
    b.append(p("The printed legend to Fig. 9.1 reads: 'Example of breathing "
               "device to exclude Water. A = Enclosure Wall, B = Desiccant, "
               "C = Gasket, D = Desiccant holder where all three parts are "
               "secured together by welding, soldering, cementing or have "
               "interposing gaskets to prevent moisture entry, E = Downward "
               "facing vent secured to desiccant holder by welding, soldering "
               "or screwing. Note: The desiccant Holder is fixed to the "
               "enclosure in a manner acceptable to BS/EN 50015 (1994)'."))

    b.append(p("All apparatus, both sealed and non-sealed, needs to have an "
               "indicator which identifies the maximum and minimum oil levels "
               "acceptable in all normal conditions. In the case of apparatus "
               "which is not sealed, this may take the form of a dipstick if it "
               "is secured to the apparatus in normal conditions (this means it "
               "forms part of the enclosure and satisfies the ingress protection "
               "requirements at times when not in use, to check oil levels). "
               "Alternatively, it may be a device, such as a sight tube or level "
               "windows in the enclosure, in which case the material must not "
               "be degraded by the oil in a way that will cause loss of strength "
               "or obscuration, and it must be arranged so that, unless it is "
               "protected from such things as impact so that damage can be "
               "ignored in normal service, its failure will not permit the oil "
               "level to fall below the minimum acceptable level."))
    b.append(p("All fasteners which are germane to the protection concept need "
               "to be protected against accidental removal or loosening by "
               "personnel, or such things as vibration. While neither this "
               "Standard or its predecessor calls up special fasteners (see "
               "BS/EN 50014 (1993)⁵) suggestions are made in BS/EN 50015 "
               "(1994)¹³ as to what is acceptable and the following are "
               "mentioned: shrouds around boltheads; cementing of threads; "
               "fitting of locking washers; and wiring of boltheads. The choice "
               "of any of these or equivalents is up to the manufacturer in "
               "particular cases, but appropriateness will need to be justified "
               "and, in the case of equivalents, equivalence."))
    return "".join(b)
