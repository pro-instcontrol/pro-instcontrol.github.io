# -*- coding: utf-8 -*-
"""Chapter 10, module I - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 270-273 (PDF pp. 291-294).

This is the final prose module of Chapter 10. It continues directly from the
"Empty flameproof enclosures" lead-in owned by module H: the six numbered
rules, the closing "above limitations" paragraph, the *Lampholders*
subsection and Figures 10.26-10.29 at their printed positions. It stops at
the printed ``References`` heading (LF 12205); the chapter shell owns all
seventeen references, the h2 chapter title, the glossary, the source-quirk
note and the copyright line. Printed quirks are kept in the English text and
flagged in notes rather than silently corrected. This is an unofficial study
translation; the source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, fig
import mcmillanfig10d as FD


def body_vi():
    b = []
    # Six numbered rules under "Empty flameproof enclosures" (lead-in in H).
    b.append(p("1. Không nên có thiết bị nào được lắp bên trong vỏ bọc lại có "
               "vỏ bọc riêng. Điều này sẽ hạn chế khả năng xảy ra hiện tượng "
               "chồng áp (pressure piling)."))
    b.append(p("2. Việc lắp đặt các linh kiện trong vỏ bọc phải sao cho bất kỳ "
               "mặt cắt ngang nào của thiết bị cũng có ít nhất 20 phần trăm "
               "không gian trống, được tạo thành từ các khoảng không gian "
               "không có linh kiện có kích thước tối thiểu 12,5 mm theo bất "
               "kỳ hướng nào."))
    b.append(p("3. Cấm dùng máy móc quay và các thiết bị khác quay gây nhiễu "
               "loạn đáng kể bên trong vỏ bọc, vì sự nhiễu loạn tạo ra có thể "
               "ảnh hưởng đến đặc tính chống cháy của vỏ bọc. Đây không phải "
               "là lệnh cấm hoàn toàn — các cơ cấu định vị và mô tơ đồng hồ "
               "nhỏ không có khả năng gây nhiễu loạn đáng kể và có thể được "
               "chấp nhận."))
    b.append(p("4. Khi có các thiết bị tích trữ năng lượng, chẳng hạn như tụ "
               "điện, bên trong vỏ bọc, chúng không được dễ dàng tiếp cận khi "
               "mở nắp vỏ bọc, nhằm tránh tạo ra hồ quang và tia lửa do can "
               "thiệp vào bên trong vỏ bọc."))
    b.append(p("5. Không nên đặt cầu chì có thể thay dây (cầu chì không phải "
               "loại hộp) bên trong vỏ bọc, vì khi các cầu chì này hoạt động "
               "có thể tạo ra các hạt nóng rực, sau đó có thể bị đẩy ra khỏi "
               "vỏ bọc qua các đường khe hở ngọn lửa."))
    b.append(p("6. Không nên đặt contactor chứa dầu bên trong vỏ bọc, vì có "
               "những nguy hiểm liên quan đến hoạt động của loại contactor "
               "này khi xảy ra sự cố điện, có thể làm thoát ra dầu nóng hoặc "
               "dầu đang cháy qua các đường khe hở ngọn lửa. Ngoài ra, còn có "
               "thể sinh ra khí do sự phân hủy của dầu."))
    b.append(p("Những hạn chế nêu trên giả định rằng cuối cùng vỏ bọc được "
               "phân loại theo nhiệt độ dựa trên công suất tiêu tán bên trong "
               "nó bởi các linh kiện được lắp đặt. Về mọi mặt khác (tức là "
               "việc bịt kín các lỗ không sử dụng và các đầu vào cáp), vỏ bọc "
               "phải được xử lý như bất kỳ vỏ chống cháy nào khác."))

    b.append(h4("Đui đèn", "Lampholders"))
    b.append(p("Người ta thừa nhận rằng việc tháo bóng đèn là chuyện thường "
               "xuyên và bóng đèn có thể bị lỏng trong quá trình sử dụng. Cũng "
               "rõ ràng rằng mặc dù có thể trang bị một cơ cấu để ngăn bóng "
               "đèn bị lỏng và gây tia lửa, cơ cấu này lại gây khó khăn cho "
               "việc thay thế bóng đèn một cách dễ dàng và vì thế không được "
               "chấp nhận trong nhiều trường hợp. Cần có một tình huống chống "
               "cháy tại cơ cấu kết nối của bóng đèn, để mọi tia lửa phát sinh "
               "khi bóng đèn bị ngắt có chủ đích hoặc vô tình đều được chứa "
               "trong cái mà thực chất là một vỏ chống cháy."))
    b.append(p("Với các bóng đèn thông thường, đui đèn vặn ren sẽ là E10, E14, "
               "E27 và E40. Đối với các cỡ nhỏ hơn (E10 và E14), người ta đã "
               "chứng minh rằng chỉ cần có ít nhất hai ren đầy đủ của bóng đèn "
               "được ăn khớp tại thời điểm các tiếp điểm tách ra (xem Hình "
               "10.26). Đối với ren lớn hơn (E27 và E40), người ta đã chứng "
               "minh rằng yêu cầu tương tự là chấp nhận được đối với nhóm phụ "
               "IIA nhưng không chấp nhận được đối với nhóm phụ IIB hoặc IIC. "
               "Với các cỡ ren lớn này, cũng cần bảo đảm rằng tiếp điểm được "
               "tạo bởi các phần tử tiếp điểm có lò xo nhằm giảm nguy cơ bị "
               "ngắt kết nối. Đối với nhóm phụ IIB và IIC, ngoài những điều "
               "nêu trên, ren ăn khớp giữa bóng đèn và đui đèn còn phải tự nó "
               "tạo thành một vỏ chống cháy, với mọi yêu cầu về truyền ngọn "
               "lửa và độ bền được áp dụng cho các mối nối ren (xem Hình "
               "10.27). Đối với ống huỳnh quang, thường dùng ống loại TLX "
               "catốt lạnh, với một chân ở mỗi đầu (xem Hình 10.28). Các ống "
               "này được quy định cùng với yêu cầu đối với đui đèn trong BS "
               "5101¹⁶ và việc tuân thủ sẽ đáp ứng các yêu cầu chống cháy cho "
               "cụm đèn như vậy."))
    b.append(note("<b>Lưu ý về chỉ số 16 sau BS 5101.</b> Nguyên bản in chỉ số "
                  "16 ngay sau BS 5101, dù BS 5101 thực chất là tài liệu tham "
                  "khảo 17 (tài liệu 16 là BS 5600). Bản dịch giữ nguyên chỉ "
                  "số in là 16, không sửa thành 17."))
    b.append(fig(26, FD.fig_f1026()))
    b.append(p("Đối với các trường hợp khác của bóng đèn/đui đèn, bóng đèn và "
               "đui đèn phải tạo thành một mối nối chống cháy dạng trụ, đáp "
               "ứng mọi yêu cầu đối với loại mối nối này tại điểm các tiếp "
               "điểm tách ra nhưng, bổ sung thêm, do bản chất của mối nối, cần "
               "có chiều dài tối thiểu của mối nối tại thời điểm tách là 10 "
               "mm (xem Hình 10.28 và 10.29)."))
    b.append(fig(27, FD.fig_f1027()))
    b.append(fig(28, FD.fig_f1028()))
    b.append(note("<b>Lưu ý về Hình 10.28.</b> Chú thích hình ghi 'data sheet "
                  "Fab of IEC 61' theo đúng bản in, trong khi bản văn trích "
                  "BS 5101 cho cùng yêu cầu về đui đèn. Bản dịch giữ nguyên "
                  "cả hai cách trích dẫn."))
    b.append(fig(29, FD.fig_f1029()))
    return "".join(b)


def body_en():
    b = []
    # Six numbered rules under "Empty flameproof enclosures" (lead-in in H).
    b.append(p("1. No equipment installed in the enclosure should have its own "
               "enclosure. This will limit the possibility of pressure piling."))
    b.append(p("2. The installation of components in the enclosure must be "
               "such that any cross section of the equipment will demonstrate "
               "at least 20 per cent free space, made up of component-free "
               "spaces of 12.5 mm minimum dimension in any direction."))
    b.append(p("3. Rotating machinery and other items which rotate and cause "
               "significant turbulence inside the enclosure are prohibited as "
               "the turbulence created could affect the flameproof properties "
               "of the enclosure. This is not a total prohibition — "
               "positioning devices and small clock motors are not likely to "
               "cause significant turbulence and may be acceptable."))
    b.append(p("4. Where energy-storing devices, such as capacitors, are "
               "present in the enclosure they should not be readily accessible "
               "on taking the lid off the enclosure to avoid the creation of "
               "arcs and sparks by intervention inside the enclosure."))
    b.append(p("5. Rewirable fuses (non-cartridge fuses) should not be placed "
               "inside the enclosure because of the possibility of production "
               "of incandescent particles on their operation, which may be "
               "ejected from the enclosures via the flamepaths."))
    b.append(p("6. Oil-filled contactors should not be placed inside the "
               "enclosures because of the dangers associated with the "
               "operation of such contactors in case of an electrical fault, "
               "which may cause the release of hot or burning oil via the "
               "flamepaths. In addition, there may be the production of gas "
               "due to decomposition of the oil."))
    b.append(p("The above limitations presuppose that the enclosure is "
               "ultimately temperature classified on the basis of the power "
               "dissipated within it by the components installed. In all other "
               "respects (i.e., the closing of unused apertures and cable "
               "entries) the enclosure must be treated in the same way as any "
               "other flameproof enclosure."))

    b.append(h4("Lampholders", "Lampholders"))
    b.append(p("It is recognized that lamp removal is a regular occurrence and "
               "that lamps can work loose in service. It is also clear that "
               "although a device to prevent lamps working loose and causing "
               "sparking can be provided, this device causes problems with the "
               "ease of lamp replacement and is, therefore, not acceptable in "
               "many circumstances. There is a need for a flameproof situation "
               "in the lamp connection mechanisms, so that any sparking which "
               "occurs when the lamp is either deliberately or accidentally "
               "disconnected is contained in what is effectively a flameproof "
               "enclosure."))
    b.append(p("With normal lamps the screwed lampcap will be E10, E14, E27 and "
               "E40. For the smaller sizes (E10 and E14) it has been shown that "
               "all that is necessary is for at least two complete threads of "
               "the lamp to be engaged at the moment of contact separation "
               "(see Fig. 10.26). For the larger threads (E27 and E40) it has "
               "been shown that the same requirement is acceptable for "
               "sub-group IIA but not for sub-group IIB or IIC. With these "
               "larger thread sizes it is also necessary to ensure that the "
               "contact is made by spring-loaded contact elements to lessen "
               "the risk of disconnection. For sub-group IIB and IIC, in "
               "addition to the above, the lamp and holder-engaged thread must "
               "also form a flameproof enclosure, with all of the requirements "
               "for flame transmission and strength which are applied to "
               "threaded joints (see Fig. 10.27). For fluorescent tubes, the "
               "cold cathode TLX-type tube, with one pin at each end, is "
               "normally used (see Fig. 10.28). These are specified together "
               "with the requirements for holders in BS 5101¹⁶ and compliance "
               "will satisfy the flameproof requirements for such lamp "
               "assemblies."))
    b.append(note("<b>Note on the 16 after BS 5101.</b> The print carries a "
                  "superscript 16 immediately after BS 5101, although BS 5101 "
                  "is reference 17 (reference 16 is BS 5600). The printed "
                  "marker 16 is retained here rather than silently corrected "
                  "to 17."))
    b.append(fig(26, FD.fig_f1026()))
    b.append(p("For other lamp/lampcap situations, the lamp and lampcap must "
               "form a cylindrical flameproof joint satisfying all of the "
               "requirements for such joints at the point of contact "
               "separation but, additionally, because of the nature of the "
               "joint, a minimum length of joint at the time of separation of "
               "10 mm is required (see Fig. 10.28 and 10.29)."))
    b.append(fig(27, FD.fig_f1027()))
    b.append(fig(28, FD.fig_f1028()))
    b.append(note("<b>Note on Fig. 10.28.</b> The printed caption reads 'data "
                  "sheet Fab of IEC 61', while the body text cites BS 5101 for "
                  "the same lamp-holder requirements. Both citations are "
                  "retained as printed."))
    b.append(fig(29, FD.fig_f1029()))
    return "".join(b)
