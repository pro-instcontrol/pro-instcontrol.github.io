# -*- coding: utf-8 -*-
"""Chapter 8, module C - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 188-194 (PDF pp. 209-215).

Covers section 8.1.3, Requirements for enclosures: impact and drop tests,
Table 8.3, the IP code and Table 8.4, typical IP20/IP54/IP65 ratings,
residual-charge limits, non-metallic (plastics) enclosures, Figure 8.2,
warning labels, conducting loading, cast-in metal thread bosses and light
metal enclosures. Tables 8.3/8.4 come from mcmillan_tbl83_84 and Figure 8.2
from mcmillanfig08. The chapter shell owns the chapter h2, the references
and the end matter.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h2, h3, h4, p, note, table, fig
import mcmillanfig08 as F
import mcmillan_tbl83_84 as T83


def body_vi():
    b = []
    b.append(h3("8.1.3 Yêu cầu đối với vỏ bọc",
                "8.1.3 Requirements for enclosures"))

    b.append(p("Trong mọi khái niệm bảo vệ, vỏ bọc của thiết bị, ở một mức độ "
               "nào đó, đều quan trọng đối với sự an toàn liên tục được bảo "
               "đảm cho thiết bị. Rõ ràng là điều quan trọng phải duy trì được "
               "tính toàn vẹn của vỏ bọc, và cần hiểu rằng thường có những "
               "linh kiện bên trong vỏ bọc hoặc giữ lại điện tích có khả năng "
               "gây cháy, hoặc giữ lại nhiệt độ có khả năng gây cháy sau khi "
               "đã ngắt điện thiết bị trong một khoảng thời gian xác định "
               "được. Vì những lý do này, vỏ bọc phải chịu các thử nghiệm va "
               "đập và rơi đáng kể để bảo đảm rằng chúng có đủ độ bền cho mục "
               "đích sử dụng. Chúng được thử nghiệm cùng với nội dung bên "
               "trong, và độ bền của các chi tiết gắn kết bên trong cũng được "
               "thử nghiệm đồng thời."))
    b.append(p("Mọi thiết bị đều phải chịu thử nghiệm va đập ở mức cơ bản là "
               "7 joules hoặc, nếu thiết bị dự định được lắp đặt ở nơi có nguy "
               "cơ va đập nhỏ, là 4 joules. Nhìn chung, điều này có nghĩa là "
               "cách tiếp cận 7 joules được dùng để bảo đảm tính linh hoạt tối "
               "đa trong sử dụng, mặc dù trong những trường hợp như nguy cơ "
               "trong nhà tại các nhà máy dược phẩm, mức giảm nhẹ có thể hữu "
               "ích. Các tấm che chắn trên một số bộ phận của thiết bị cũng "
               "có thể làm giảm yêu cầu thử nghiệm va đập, và Bảng 8.3 cho "
               "thấy các mức giảm mức độ va đập có thể có."))
    b.append(table(T83.HEAD83_VI, T83.ROWS83, T83.CAPTION83_VI))
    b.append(note(T83.NOTE83_VI))
    b.append(p("Ngoài ra, thiết bị mang xách sẽ được thử nghiệm rơi từ độ cao "
               "1 m để kiểm chứng độ tin cậy khi sử dụng. Các thử nghiệm thường "
               "được tiến hành ở nhiệt độ phòng thí nghiệm bình thường vì "
               "ảnh hưởng của sự thay đổi nhiệt độ môi trường (thường từ "
               "−20 °C đến +40 °C) không được coi là đáng kể. Tuy nhiên, nếu "
               "điều này không đúng do những biến đổi bất thường của nhiệt độ "
               "môi trường hoặc do những đặc tính riêng của vật liệu vỏ bọc "
               "(vỏ bọc bằng nhựa được đề cập sau trong mục này), có thể cần "
               "tiến hành thử nghiệm va đập và, nếu thích hợp, thử nghiệm rơi "
               "ở các giới hạn nhiệt độ môi trường dự kiến."))
    b.append(p("Thủy tinh được công nhận là một điểm yếu khi được dùng cho "
               "những thứ như cửa sổ quan sát trên vỏ bọc, và phải chịu thử "
               "nghiệm sốc nhiệt bằng cách phun nước ở nhiệt độ tương đối "
               "thấp lên nó khi nó được nâng đến nhiệt độ dịch vụ tối đa."))
    b.append(p("Một số khái niệm bảo vệ xác định yêu cầu về tính toàn vẹn của "
               "vỏ bọc chống sự xâm nhập của các vật thể lạ rắn hoặc lỏng, "
               "hoặc cả hai. Điều này được xác định bằng một số 'IP', chẳng "
               "hạn IP54. Chữ số thứ nhất xác định mức bảo vệ chống các vật "
               "thể lạ rắn, chẳng hạn dụng cụ hoặc bụi, và chữ số thứ hai xác "
               "định mức bảo vệ chống sự xâm nhập của chất lỏng. Thông số IP "
               "được xác định bằng cách thử nghiệm vỏ bọc theo "
               "BS/EN 60529 1991², và Bảng 8.4 xác định các chữ số dùng trong "
               "đánh giá IP. Các mức IP điển hình là:"))
    b.append(p("IP20: Đây được coi là mức bảo vệ đủ để ngăn việc luồn ngón tay "
               "v.v. vào và được giả định là ngăn được điện giật. IP54: Đây "
               "được coi là chống được thời tiết khi lắp đặt ngoài trời. Mọi "
               "thiết bị lắp ngoài trời, dù dùng cho việc lắp đặt trong khu "
               "vực nguy hiểm hay không, đều nên đáp ứng ít nhất tiêu chí "
               "này. IP65: Đây được coi là kín bụi. Một lần nữa cần nhấn mạnh "
               "rằng tính toàn vẹn của vỏ bọc thường được xác định bởi tình "
               "huống chung chứ không phải bởi mức tối thiểu được phép của "
               "khái niệm bảo vệ. Ví dụ, thiết bị ngoài trời gần như luôn là "
               "IP54 để bảo đảm độ tin cậy vận hành, và thiết bị dùng khi có "
               "sự hiện diện của bụi dẫn điện cũng gần như luôn được yêu cầu "
               "là IP65."))
    b.append(p("Về điện tích dư hoặc nhiệt độ còn lại sau khi ngắt điện, cách "
               "duy nhất để khắc phục vấn đề này nếu không thể tránh được bằng "
               "thiết kế là xác định thời gian cần để điện tích suy giảm, và "
               "dán nhãn cảnh báo lên thiết bị, ghi rõ khoảng thời gian chờ "
               "cần tuân thủ trước khi mở vỏ. Đối với điện tích dư, các giá "
               "trị được đưa ra như sau: Nhóm IIA — Điện tích dư không được "
               "vượt quá 0.2 mJ khi mở vỏ bọc; Nhóm IIB — Điện tích dư không "
               "được vượt quá 0.06 mJ khi mở vỏ bọc; Nhóm IIC — Điện tích dư "
               "không được vượt quá 0.02 mJ khi mở vỏ bọc. Các giá trị này "
               "cho phép tính toán thời gian cần thiết để ghi vào nhãn cảnh "
               "báo."))
    b.append(p("Trong trường hợp điện tích không thể được tiêu tán trong một "
               "thời gian hợp lý, hoặc nhiệt độ tương tự được duy trì trong "
               "thời gian rất dài, một cách tiếp cận thay thế là cảnh báo rằng "
               "không nên mở vỏ bọc trừ khi có thể xác định khu vực lắp đặt là "
               "không có khí tại thời điểm mở."))
    b.append(p("Hợp kim nhôm và nhựa có thể gây ra những vấn đề bổ sung đáng "
               "kể khi được dùng làm vật liệu vỏ bọc, cả về mặt độ bền lẫn về "
               "khả năng trở thành nguồn bắt lửa. Vì mục đích này, cả hai đều "
               "được đề cập thêm chi tiết trong BS/EN 50014 (1993)."))

    b.append(h4("Yêu cầu cụ thể đối với vỏ bọc bằng nhựa (không kim loại)",
                "Specific requirements for non-metallic (plastic) enclosures"))
    b.append(p("Để bảo đảm hiệu năng của vỏ bọc có thể lặp lại, loại nhựa (hoặc "
               "các loại nhựa) làm vỏ bọc cần được xác định rõ bằng thành phần "
               "đầy đủ, bao gồm cả chất độn v.v., và tên của nhà sản xuất. Ngoài "
               "ra, cần quy định cả xử lý bề mặt (ví dụ, sơn mài). Để hỗ trợ "
               "việc này, tốt nhất luôn là dùng công thức nhựa phù hợp với "
               "Tiêu chuẩn của Tổ chức Quốc tế về Tiêu chuẩn Hóa (ISO)³, vì "
               "trong trường hợp nhà sản xuất ngừng sản xuất một loại nhựa cụ "
               "thể, việc tìm kiếm chất thay thế sẽ dễ dàng hơn."))
    b.append(p("Chỉ số nhiệt độ (TI) (lấy từ điểm 20.000 giờ trên đồ thị độ bền "
               "nhiệt của nhựa) cần chứng minh rằng ở mức 20 °C trên nhiệt độ "
               "tối đa đạt được của bất kỳ bộ phận nào của vỏ bọc ở nhiệt độ "
               "vận hành tối đa của thiết bị, nhựa đã mất chưa tới 50 phần "
               "trăm độ bền uốn, để chứng minh rằng nhựa có độ bền đủ cho mục "
               "đích sử dụng. (Mặc dù việc chứng minh điều này cho mục đích của "
               "BS/EN 50014 (1993) được thực hiện bằng cách nhà sản xuất thiết "
               "bị quy định giá trị cụ thể, Tiêu chuẩn cũ BS 5501, phần 1 "
               "(1977) yêu cầu phải đưa toàn bộ đồ thị để xác nhận tình huống "
               "này.) Cần tham khảo IEC 216-1⁴, IEC 216-2⁵ và ISO 178⁶ hoặc "
               "ISO R527⁷ để biết các phương pháp lập giá trị này."))
    b.append(p("Ngoài việc được chọn để đáp ứng giá trị đó, vỏ bọc làm bằng "
               "nhựa cần được thử nghiệm khả năng chịu nhiệt, lạnh và, khi vỏ "
               "bọc hoặc các bộ phận của nó không được che chắn khỏi ánh sáng "
               "thông thường chiếu tới (đây là tình huống phổ biến), khả năng "
               "chịu ánh sáng. Tương tự, các thử nghiệm va đập và, nếu thích "
               "hợp, thử nghiệm rơi thường được tiến hành ở nhiệt độ phòng thí "
               "nghiệm, sẽ cần được tiến hành ở nhiệt độ dịch vụ tối đa và tối "
               "thiểu, với hệ số an toàn khoảng 10 °C đối với vỏ bọc bằng "
               "nhựa."))
    b.append(p("Hầu hết nhựa cũng có khuynh hướng giữ điện tích khi bị ma sát, "
               "chẳng hạn như bị chà xát bằng khăn khô, và điện tích tĩnh này "
               "thường có khả năng gây cháy một bầu khí quyển nổ. Vì vậy, cần "
               "bảo đảm rằng vật liệu như vậy không thể duy trì điện tích đó "
               "hoặc, nếu có thể phát sinh điện tích, phải thực hiện biện pháp "
               "phòng ngừa để bảo đảm không phát sinh điện tích. Nói chung, "
               "điện tích tĩnh chỉ trở thành vấn đề khi một vỏ bọc có khả năng "
               "duy trì điện tích đó bị chà xát bằng khăn khô hoặc tương tự. "
               "BS/EN 50014 (1993)¹ xác định đây là những điều kiện duy nhất "
               "cần được giải quyết bằng cách giới hạn các yêu cầu phòng ngừa "
               "hoặc xử lý điện tích tĩnh đối với bề mặt nhựa của thiết bị "
               "mang xách và thiết bị có thể mang đi (không cố định), và thiết "
               "bị có khả năng bị chà xát hoặc vệ sinh tại chỗ. Trong trường "
               "hợp sau, chỉ thiết bị trong phòng sạch hoặc những nơi như nhà "
               "máy dược phẩm, nơi độ sạch rất quan trọng, mới có khả năng bị "
               "ảnh hưởng. Ví dụ, tại các nhà máy hóa chất thông thường hoặc "
               "nhà máy lọc dầu, thiết bị có khả năng được tưới rửa bằng vòi "
               "nước hơn là được lau bằng khăn khô."))
    b.append(p("Có hai phương pháp xử lý vỏ bọc bằng nhựa để ngăn sự tích tụ "
               "điện tích tĩnh có khả năng gây cháy. Thứ nhất, chọn vật liệu "
               "sao cho có điện trở bề mặt nhỏ hơn 1 GΩ khi đo giữa hai đường "
               "dẫn điện 100 mm cách nhau 10 mm, được sơn lên bề mặt vỏ bọc "
               "nhựa hoặc bề mặt của một tấm phẳng làm bằng cùng loại nhựa, "
               "hoặc thiết kế vỏ bọc sao cho khó phát sinh điện tích. Thứ hai, "
               "giới hạn bề mặt của vỏ bọc chiếu theo bất kỳ hướng nào (bất kỳ "
               "bề mặt đơn nào) ở các kích thước tối đa sau. Đối với thiết bị "
               "được xếp vào Nhóm IIA hoặc IIB, cần giới hạn ở 100 cm², trừ khi "
               "bề mặt nhựa được bao quanh bởi một khung dẫn điện được nối "
               "tiếp địa (xem Hình 8.2), khi đó diện tích của bề mặt cụ thể có "
               "thể tăng lên 400 cm²; và đối với thiết bị được xếp vào Nhóm "
               "IIC, cần giới hạn ở 20 cm², trừ khi bề mặt nhựa được bao quanh "
               "bởi một khung dẫn điện được nối tiếp địa (xem Hình 8.2), khi "
               "đó diện tích của bề mặt cụ thể có thể tăng lên 100 cm²."))
    b.append(fig(2, F.fig_f802()))
    b.append(table(T83.HEAD84_VI, T83.ROWS84, T83.CAPTION84_VI))
    b.append(note(T83.NOTE84_VI))
    b.append(p("Tiêu chuẩn cũng cho phép sử dụng nhãn cảnh báo ghi rõ cách tránh "
               "điện tích nếu các biện pháp trên không thể thực hiện được. Theo "
               "truyền thống, ở Vương quốc Anh, cụm từ 'không thể' được hiểu là "
               "'đã không được thực hiện' vì khó xác định thế nào là có thể và "
               "thế nào là không thể. Vì vậy, trên thực tế, hai giải pháp phổ "
               "biến nhất cho thiết bị cố định là thêm một chất dẫn điện vào "
               "vật liệu nhựa, chẳng hạn carbon (mặc dù điều này có thể gây vấn "
               "đề về cách điện bên trong thiết bị), hoặc sử dụng nhãn cảnh "
               "báo. Thiết bị mang xách có xu hướng dựa vào một lớp vỏ bao phủ "
               "toàn bộ bằng vật liệu không phải nhựa, chẳng hạn da, hoặc lại "
               "là thêm chất dẫn điện vào nhựa. BS 5501 phần 1 (1977). (Ấn bản "
               "đầu tiên của Tiêu chuẩn này không giới hạn yêu cầu đối với "
               "thiết bị không cố định và thiết bị có khả năng được vệ sinh, "
               "nhưng việc đưa vào giới hạn này khó có thể có tác động đáng kể "
               "đến thiết kế vì nhà sản xuất có xu hướng thiết kế thiết bị cho "
               "thị trường rộng nhất có thể."))
    b.append(p("Vấn đề cuối cùng với vỏ bọc nhựa là vấn đề có thể phát sinh từ "
               "việc dùng vít bắt chặt (ví dụ, để giữ nắp đậy tại chỗ). Vì nhựa "
               "nhìn chung mềm hơn kim loại trong hầu hết trường hợp, ren dễ "
               "bị tuột hơn, và khi ren dùng cho vít giữ nắp đậy và các bộ phận "
               "khác có khả năng được mở ra trong quá trình sử dụng để điều "
               "chỉnh v.v. được cắt trực tiếp vào nhựa, Tiêu chuẩn yêu cầu dạng "
               "ren phải tương thích với vật liệu nhựa. Không có hướng dẫn thêm, "
               "nhưng nên tránh ren quá mảnh hoặc quá nông vì các ren này dễ "
               "tuột hơn, đặc biệt nếu dùng vít nhựa. Nhiều nhà sản xuất giải "
               "quyết vấn đề này bằng cách đúc sẵn vào nhựa các bạc ren kim "
               "loại, và đây có lẽ là cách tốt nhất để giải quyết vấn đề."))

    b.append(h4("Yêu cầu cụ thể đối với vỏ bọc bằng kim loại nhẹ (nhôm và "
                "tương tự)",
                "Specific requirements for light metal (aluminium and "
                "similar) enclosures"))
    b.append(p("Mặc dù các vỏ bọc này có ưu điểm tương tự như vỏ bọc nhựa về "
               "trọng lượng và dễ đúc, chúng chủ yếu có độ bền lớn hơn. Tuy "
               "nhiên, chúng có những nhược điểm tương tự về ren dùng cho vít "
               "bắt chặt và các ren này nên được xử lý theo cách giống như ren "
               "của vỏ bọc nhựa. Cũng có một vấn đề liên quan đến cái gọi là "
               "tia lửa nhiệt nhôm (thermite sparking), khi hàm lượng magiê "
               "trong hợp kim vỏ bọc cao. Điều này có nghĩa là khi vỏ bọc tiếp "
               "xúc mạnh với sắt hoặc thép đã bị oxy hóa (gỉ), tia lửa tạo ra "
               "được tăng cường nhờ sự hiện diện của magiê và tia lửa mạnh hơn "
               "nhiều, trong hầu hết trường hợp có khả năng gây cháy. Để tránh "
               "tình huống này, Tiêu chuẩn không cho phép dùng hợp kim có hàm "
               "lượng magiê vượt quá 6%."))
    return "".join(b)


def body_en():
    b = []
    b.append(h3("8.1.3 Requirements for enclosures",
                "8.1.3 Requirements for enclosures"))

    b.append(p("In all protection concepts, the enclosure of the apparatus is, "
               "to some degree, important to the continued security afforded "
               "to the apparatus. It is clearly important that the integrity "
               "of the enclosure is maintained and it has to be understood "
               "that there are often components within the enclosure which "
               "either retain ignition capable electrical charge, or ignition "
               "capable temperature after isolation of the apparatus for some "
               "identifiable time. For these reasons enclosures are subjected "
               "to significant impact and drop tests to ensure that they have "
               "sufficient strength for their purpose. They are tested with "
               "the contents inside them and the strength of fixings within "
               "are also tested at the same time."))
    b.append(p("All apparatus is subjected to impact tests at a basic level of "
               "7 joules or, if the apparatus is intended to be installed "
               "where impact risks are small, 4 joules. In general, this means "
               "the 7 joule approach is used to give maximum flexibility of "
               "use, although in such cases as indoor risks in pharmaceutical "
               "plants, the reduced level can be of assistance. Guards on "
               "parts of the apparatus can also mitigate the impact test "
               "requirement and Table 8.3 shows the possible reductions of "
               "impact severity."))
    b.append(table(T83.HEAD83_EN, T83.ROWS83, T83.CAPTION83_EN))
    b.append(note(T83.NOTE83_EN))
    b.append(p("In addition, portable apparatus will be subjected to a drop "
               "test from a height of 1 m to verify its reliability in "
               "service. The tests are normally carried out at normal "
               "laboratory temperature as the effects of changes in ambient "
               "temperature (normally −20 °C to +40 °C) are not considered "
               "significant. If, however, this is not true because of unusual "
               "ambient temperature variations or particular features of "
               "enclosure material (plastic enclosures are dealt with later "
               "in this section) it may be necessary to carry out impact and, "
               "if appropriate, drop tests at the limits of ambient "
               "temperature envisaged."))
    b.append(p("Glass is recognized as a weakness, when used for such things "
               "as viewports in enclosures, and is subjected to a thermal "
               "shock test by spraying water at a relatively low temperature "
               "onto it when it is elevated to its maximum service "
               "temperature."))
    b.append(p("Several of the protection concepts identify a required "
               "enclosure integrity against the ingress of solid or liquid "
               "foreign bodies, or both. This is identified as an 'IP' number, "
               "such as IP54. The first numeral identifies the protection "
               "against solid foreign bodies, such as tools or dust, and the "
               "second numeral identifies the protection afforded against "
               "liquid ingress. IP specification is derived by testing "
               "enclosures in accordance with BS/EN 60529 1991² and Table 8.4 "
               "identifies the numerals used in IP rating. Typical IP ratings "
               "are:"))
    b.append(p("IP20: This is considered as sufficient protection to prevent "
               "insertion of fingers, etc., and is assumed to prevent electric "
               "shock. IP54: This is considered as weather proof for outdoor "
               "mounting. All outdoor-mounted apparatus be it for hazardous-"
               "area mounting or not should meet at least this criterion. "
               "IP65: This is considered to be dust tight. Once again it must "
               "be stressed that the enclosure integrity is often identified "
               "by the general situation and not by the minimum permitted by "
               "the protection concept. For example, outdoor apparatus is "
               "almost always IP54 to ensure operational reliability, and "
               "apparatus for use in the presence of conducting dusts is "
               "likewise almost always required to be IP65."))
    b.append(p("As far as residual charge or temperature after isolation is "
               "concerned, the only way to overcome this problem if it cannot "
               "be avoided by design is to identify the time taken for decay, "
               "and label the apparatus with a warning indicating a delay "
               "which should be observed before opening. For residual charge, "
               "figures are given as follows: Group IIA — The residual charge "
               "must not exceed 0.2 mJ when the enclosure is opened; Group "
               "IIB — The residual charge must not exceed 0.06 mJ when the "
               "enclosure is opened; Group IIC — The residual charge must not "
               "exceed 0.02 mJ when the enclosure is opened. These figures "
               "allow the calculation of the necessary time to be included on "
               "the warning label."))
    b.append(p("Where the charge cannot be dissipated in a sensible time, or "
               "the temperature likewise is retained for a very long time, an "
               "alternative approach is to warn that the enclosure should not "
               "be opened unless the area of installation can be specified as "
               "gas-free at the time of opening."))
    b.append(p("Aluminium alloys and plastics can present significant "
               "additional problems when used as enclosure material, both "
               "from the strength point of view, and in respect of their "
               "ability to become ignition sources. To this end, both are "
               "additionally addressed in detail in BS/EN 50014 (1993)."))

    b.append(h4("Specific requirements for non-metallic (plastic) enclosures",
                "Specific requirements for non-metallic (plastic) enclosures"))
    b.append(p("In order to ensure that the performance of the enclosure is "
               "repeatable, the plastic(s) of which the enclosure is made "
               "needs to be clearly identified by its complete composition, "
               "including fillers etc., and its manufacturer's name. In "
               "addition, its surface treatment (e.g., varnish) needs to be "
               "specified. To assist in this it is always better to use a "
               "plastics formulation which is in-line with International "
               "Standards Organization (ISO)³ Standard as, in cases where a "
               "manufacturer ceases production of a particular plastic, the "
               "search for a substitute will be easier."))
    b.append(p("The Temperature Index (TI) (taken from the 20,000 hour point "
               "on the thermal endurance graph for the plastic) needs to "
               "demonstrate that at 20 °C above the maximum temperature "
               "achieved by any part of the enclosure at maximum operating "
               "temperature for the apparatus, the plastic has lost less than "
               "50 per cent of its flexing strength to demonstrate that the "
               "plastic is of sufficient strength for the purpose. (While "
               "demonstration of this for the purposes of BS/EN 50014 (1993) "
               "is by the manufacturer of the apparatus specifying the "
               "particular value, the older Standard BS 5501, part 1 (1977) "
               "required that the entire graph be produced to confirm this "
               "situation.) IEC 216-1⁴, IEC 216-2⁵ and ISO 178⁶ or ISO R527⁷ "
               "will need to be consulted for the methods of producing this "
               "figure."))
    b.append(p("In addition to being chosen to comply with this figure, "
               "enclosures made of plastics need to be tested for their "
               "resistance to heat, cold and, where the enclosure or parts "
               "thereof are not protected from normal incident light which is "
               "the general situation, their resistance to light. Likewise "
               "the impact tests and, if appropriate, drop tests normally "
               "carried out at laboratory temperature, will need to be "
               "carried out at the maximum and minimum service temperatures, "
               "with safety factors of around 10 °C for plastics enclosures."))
    b.append(p("Most plastics also have the propensity to hold charge when "
               "subjected to friction, such as being rubbed with a dry cloth, "
               "and this static charge is often capable of igniting an "
               "explosive atmosphere. It is necessary, therefore, to ensure "
               "that such the material cannot support such charge or, if its "
               "generation is possible, precautions are taken to ensure that "
               "it is not generated. In general terms, electrostatic charges "
               "only become a problem where an enclosure, which is capable of "
               "sustaining such a charge is rubbed with a dry cloth or similar. "
               "BS/EN 50014 (1993)¹ identifies these conditions as the only "
               "conditions needing to be addressed by limiting the "
               "requirements for prevention of, or dealing with, electrostatic "
               "charge to plastics surfaces of portable and transportable "
               "(non-fixed) apparatus, and apparatus which is likely to be "
               "rubbed or cleaned on site. In the latter case, only apparatus "
               "in clean rooms or such places as pharmaceutical plants, where "
               "cleanliness is of great importance, is likely to be affected. "
               "On typical chemical plants or oil refineries, for example, it "
               "is more likely that equipment will be hosed down rather than "
               "cleaned with dry cloths."))
    b.append(p("There are two methods of dealing with plastics enclosures to "
               "prevent the build up of ignition-capable electrostatic charge. "
               "First, selection of material so that it has a surface "
               "resistance of less than 1 GΩ when measured between two 100 mm "
               "conducting lines, 10 mm apart, which are painted on the "
               "plastics enclosure surface or the surface of a flat plate of "
               "the same plastic, or by design of the enclosure such that "
               "development of charge is unlikely. Second, by limitation of "
               "the surface of the enclosure projected in any direction (any "
               "single surface) to the following maximum sizes. For apparatus "
               "given Group IIA or IIB, limitation to 100 cm² is necessary "
               "unless the plastic surface is surrounded with a conductive "
               "frame which is earthed (see Fig. 8.2), when the area of the "
               "particular surface can be increased to 400 cm², and for "
               "apparatus given Group IIC, limitation to 20 cm² is necessary "
               "unless the plastic surface is surrounded with a conducting "
               "frame which is earthed (see Fig. 8.2), when the area of the "
               "particular surface can be increased to 100 cm²."))
    b.append(fig(2, F.fig_f802()))
    b.append(table(T83.HEAD84_EN, T83.ROWS84, T83.CAPTION84_EN))
    b.append(note(T83.NOTE84_EN))
    b.append(p("The Standard also permits the use of a warning label "
               "indicating how charge is to be avoided if the above measures "
               "are not possible. Historically, the words 'not possible' have "
               "been taken in the UK to mean 'have not been taken' because of "
               "the difficulty in defining what is and is not possible. In "
               "practice, therefore, the two most common solutions for fixed "
               "apparatus have been to either load the plastics material with "
               "some conducting medium, such as carbon (although ths can give "
               "problems with insulation within the apparatus) or to utilize "
               "the warning label. Portable apparatus has tended to rely on "
               "an overall cover of non-plastics material, such as leather or, "
               "again, loading the plastic with conducting material. BS 5501 "
               "part 1 (1977). (The first edition of this Standard did not "
               "limit the requirements to non-fixed apparatus and apparatus "
               "likely to be cleaned but the introduction of this limitation "
               "is unlikely to have significant effect upon design as "
               "manufacturers tend to design their apparatus for the widest "
               "possible market."))
    b.append(p("The final problem with plastic enclosures is the problem which "
               "can be associated with using fastening screws (for example, "
               "to hold the lid, in place). Plastic being somewhat softer than "
               "metal in most cases, it is more subject to thread stripping "
               "and where threads for fixing screws, which hold covers in "
               "place and other parts likely to be opened in service for "
               "adjustment etc., are tapped directly into the plastic, the "
               "Standard requires the thread form to be compatible with the "
               "plastics material. No further guidance is given but fine or "
               "shallow threads should be avoided as these are more likely to "
               "strip, particularly if plastic screws are used. Many "
               "manufacturers solve this problem by casting into the plastic "
               "metal thread bosses and this is probably the best way to "
               "solve the problem."))

    b.append(h4("Specific requirements for light metal (aluminium and similar) "
                "enclosures",
                "Specific requirements for light metal (aluminium and "
                "similar) enclosures"))
    b.append(p("While such enclosures offer a similar advantage to plastic "
               "enclosures in weight and ease of casting, they mainly exhibit "
               "greater strength. They do, however, have similar drawbacks in "
               "respect of threads for fastening screws and such threads "
               "should be treated in the same way as those for plastics "
               "enclosures. There is also a problem associated with so-called "
               "thermite sparking, where magnesium content of alloy enclosures "
               "is high. This means that where the enclosure comes forcibly "
               "into contact with oxidized iron or steel (rust), the resultant "
               "spark is enhanced by the presence of the magnesium and the "
               "spark is much more powerful and is ignition capable in most "
               "cases. To avoid this situation, alloys with more than 6 per "
               "cent magnesium are not permitted by the standard."))
    return "".join(b)
