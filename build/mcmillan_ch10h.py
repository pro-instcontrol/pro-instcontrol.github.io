# -*- coding: utf-8 -*-
"""Chapter 10, module H - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed p. 269 (PDF p. 290).

Completes the Stopping boxes paragraph interrupted at the foot of printed
p. 268, with Fig. 10.25 in its printed position, then covers the opening of
10.3.6 Freestanding flameproof components, its printed wording quirk, and the
unnumbered subheading Empty flameproof enclosures with its lead-in sentence.
The six numbered rules and the references belong to module I / the shell.
"""
from mcmillan_common import h3, h4, p, note, fig
import mcmillanfig10c as FC


def body_vi():
    b = []
    b.append(fig(25, FC.fig_f1025()))
    b.append(p("hợp chất điền kín. Yêu cầu đối với hộp khi được lắp ráp và "
               "điền đầy hợp chất (và các dây dẫn) cũng giống như yêu cầu đối "
               "với các đầu nối cáp dùng hợp chất điền kín. Hình 10.25 cho "
               "thấy một hộp chặn điển hình."))
    b.append(h3("10.3.6 Linh kiện chống cháy độc lập",
                "10.3.6 Freestanding flameproof components"))
    b.append(p("Cũng như với các nguyên lý bảo vệ khác, những thiết bị chống "
               "cháy nhất định này có thể được phê duyệt là linh kiện và được "
               "sử dụng trong các thiết bị khác với mức độ kiểm tra bổ sung "
               "tối thiểu. Nguyên lý bảo vệ này dựa gần như hoàn toàn vào vỏ "
               "bọc để hoạt động, và các linh kiện bên trong vỏ bọc chỉ chịu "
               "một số yêu cầu tối thiểu. Có thể tạo ra một vỏ chống cháy với "
               "quy định về cách nó phải được điền đầy đủ linh hoạt để cho "
               "phép một loạt linh kiện bên trong với mức độ kiểm tra bổ sung "
               "tối thiểu. Điều này phụ thuộc vào chính vỏ bọc đã phải chịu "
               "các yêu cầu về kết cấu và thử nghiệm của nguyên lý bảo vệ khi "
               "ở trạng thái rỗng. Ngoài ra, một số phần tử như đui đèn được "
               "dùng trong các loại hình bảo vệ khác nhưng không thể đáp ứng "
               "yêu cầu của loại hình bảo vệ cụ thể đó. Nguyên lý bảo vệ chống "
               "cháy có thể được dùng như một dạng bảo vệ-phụ trong những "
               "trường hợp này."))
    b.append(note("<b>Lưu ý về nguyên bản.</b> Nguyên bản in 'these are "
                  "certain flameproof items' (không phải 'there are'); bản "
                  "dịch giữ nguyên cách diễn đạt in là 'những ... này'."))
    b.append(h4("Vỏ chống cháy rỗng", "Empty flameproof enclosures"))
    b.append(p("Một vỏ chống cháy đã được kiểm tra và thử nghiệm sau khi chế "
               "tạo với tất cả các lỗ vào, v.v., đã được bố trí đúng chỗ thì "
               "có khả năng vẫn giữ được tính chống cháy sau khi lắp các linh "
               "kiện bên trong, miễn là áp dụng được các quy tắc đơn giản sau:"))
    return "".join(b)


def body_en():
    b = []
    b.append(fig(25, FC.fig_f1025()))
    b.append(p("compound. The requirements for the box when assembled and "
               "filled with compound (and conductors) are the same as for "
               "cable glands using sealing compound. Figure 10.25 shows a "
               "typical stopping box."))
    b.append(h3("10.3.6 Freestanding flameproof components",
                "10.3.6 Freestanding flameproof components"))
    b.append(p("As with the other protection concepts, these are certain "
               "flameproof items which can be approved as components and used "
               "in other apparatus with a minimum of further investigation. "
               "This protection concept relies upon the enclosure almost "
               "exclusively for its operation, and the components within the "
               "enclosure are only subject to a minimum of requirements. It "
               "is possible to produce a flameproof enclosure with a "
               "specification of how it must be filled which is sufficiently "
               "flexible to permit a range of components therein with a "
               "minimum of further examination. This is dependent upon the "
               "enclosure itself having been subjected to the constructional "
               "and test requirements of the protection concept when empty. "
               "In addition certain elements, such as lampholders, are used "
               "in other types of protection but cannot satisfy the "
               "requirements of that particular type of protection. The "
               "flameproof protection concept can be used as a sub-protection "
               "in these cases."))
    b.append(note("<b>Source note.</b> The print reads 'these are certain "
                  "flameproof items' (not 'there are'); the wording is kept "
                  "as printed."))
    b.append(h4("Empty flameproof enclosures",
                "Empty flameproof enclosures"))
    b.append(p("A flameproof enclosure which has been examined and tested "
               "after construction with all entry holes, etc., in place is "
               "likely to remain flameproof after fitting of internal "
               "components, provided the following simple rules are applied:"))
    return "".join(b)
