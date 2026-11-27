# -*- coding: utf-8 -*-
"""Chapter 5, module C - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas* (1998),
printed pp. 130-135 (PDF pp. 151-156): sections 5.3, 5.3.1, both printed
5.3.2 headings, 5.3.4 and the 5.4 introduction, with figures 5.5-5.10.
Unofficial study translation; the integration module owns the page
shell, sources, references and end matter.
"""
from mcmillan_common import h3, h4, p, note, fig
import mcmillanfig05_a as FA


def body_vi():
    b = []
    b.append(fig(5, FA.fig_f505()))
    b.append(h3("5.3 Mái không có tường hoặc liên kết với một, hai hoặc ba bức tường",
                "5.3 Roofs without walls or associated with one, two or three walls"))
    b.append(h4("5.3.1 Mái không có tường",
                "5.3.1 Roofs without walls"))
    b.append(p("Có hai tình huống cần xem xét ở đây. Thứ nhất là mái phẳng, rất điển "
               "hình cho mái che của trạm xăng; thứ hai là mái hồi (kiểu chuồng Hà "
               "Lan), phổ biến hơn ở các khu vực bốc dỡ hàng công nghiệp. Mái hồi có "
               "thể có hoặc không có lỗ thông hơi, tuy nhiên trong hầu hết các "
               "trường hợp đều có lỗ thông hơi, đặc biệt khi chất cháy là khí hoặc "
               "hơi nhẹ hơn không khí."))
    b.append(p("Khi không có tường nào, ảnh hưởng của mái phẳng phụ thuộc vào khoảng "
               "cách từ mái đến mép của khu vực nguy hiểm sẽ hình thành nếu nguồn "
               "phát thải ở trong không khí tự do (xem Hình 5.6). Nếu mái nằm cách "
               "quá 5 m về phía ngoài phạm vi khu vực nguy hiểm dự đoán theo Hình "
               "3.4 và 3.5 (trong Chương 3) thì mái ít có khả năng gây ảnh hưởng, "
               "nhưng trong các trường hợp khác thì khu vực nguy hiểm được dự kiến "
               "là chạm tới mái."))
    b.append(fig(6, FA.fig_f506()))
    b.append(p("Khi có mái hồi (kiểu chuồng Hà Lan) mà không có tường và nếu đỉnh của "
               "khu vực nguy hiểm xác định khi không có mái nằm trong vòng 5 m tính "
               "tới mái thì toàn bộ khu vực nằm dưới mái sẽ trở thành khu vực nguy "
               "hiểm có mức độ nghiêm trọng như nhau, với điều kiện là trong những "
               "trường hợp chất cháy không nặng hơn không khí thì phải bố trí lỗ "
               "thông hơi ở đỉnh mái. Hình 5.7 minh họa tình huống này và gợi ý một "
               "phạm vi tưởng tượng 1 m khu vực nguy hiểm quanh các lỗ thông hơi. "
               "Phạm vi sau cùng này khó dự đoán, nhưng ở mức 1 m thì được coi là "
               "đủ lớn cho hầu hết các tình huống thông thường."))
    b.append(fig(7, FA.fig_f507()))
    b.append(h4("5.3.2 Mái liên kết với một bức tường",
                "5.3.2 Roofs associated with one wall"))
    b.append(p("Khi có thêm một bức tường ngoài mái, tình huống trở nên phức tạp hơn "
               "và các khu vực nguy hiểm mô tả trong Hình 5.1 và 5.2 được biến đổi "
               "thành tình huống thể hiện trong Hình 5.8. Điểm chính cần lưu ý ở "
               "đây là phần khu vực nguy hiểm mở rộng qua khỏi mái một đoạn nhỏ, "
               "bằng hiệu số giữa phạm vi khu vực nguy hiểm khi có tường và chiều "
               "dài của bức tường. Người ta dùng chiều dài thay vì chiều cao vì sự "
               "chồng lấp chỉ xảy ra khi chiều dài tường nhỏ hơn phạm vi nằm ngang "
               "của khu vực nguy hiểm, vốn đã bị biến dạng do được kéo dài lên tới "
               "mức mái. Tình huống cũng tương tự như trường hợp mái hồi, nhưng ở "
               "đây phải tính thêm cả các ảnh hưởng thể hiện trong Hình 5.7."))
    b.append(fig(8, FA.fig_f508()))
    b.append(note("<b>Lưu ý về chú giải Hình 5.8.</b> Chú giải in định nghĩa V = độ "
                  "cao của nguồn phát thải, nhưng sau đó lại viết a = E − Y và "
                  "b = 2y − 2a, trong khi Y và y không được định nghĩa (nhiều khả "
                  "năng là lỗi in của V). Các ký hiệu in được giữ nguyên thay vì "
                  "được sửa lặng lẽ; phần mở rộng tối thiểu trên mái là 0,5 m."))
    b.append(h4("5.3.2 Mái liên kết với hai bức tường",
                "5.3.2 Roofs associated with two walls"))
    b.append(note("<b>Lưu ý về đánh số.</b> Trên cùng một trang in (tr. 132), bản in "
                  "ghi hai mục liên tiếp đều mang số 5.3.2: \"Mái liên kết với một "
                  "bức tường\" và \"Mái liên kết với hai bức tường\". Với trình tự "
                  "5.3.1, 5.3.2, 5.3.2, 5.3.4 thì mục thứ hai đáng lẽ là 5.3.3 về "
                  "mặt logic; cả hai số in được giữ nguyên và không được đánh số "
                  "lại lặng lẽ ở đây."))
    b.append(p("Khi có hai bức tường, toàn bộ vùng được bao phủ bởi khu vực nguy "
               "hiểm thể hiện trong Hình 5.3 và 5.4 sẽ tạo thành một phần của khu "
               "vực nguy hiểm tính lên tới mái và xuống tới mặt đất (xem Hình 5.9). "
               "Cũng như đối với một bức tường, các phạm vi khu vực nguy hiểm phía "
               "trên đường mái được xác định bằng Hình 5.3 và 5.4."))
    b.append(fig(9, FA.fig_f509()))
    b.append(h4("5.3.4 Mái liên kết với ba bức tường",
                "5.3.4 Roofs associated with three walls"))
    b.append(p("Khi có ba bức tường, tình huống hoàn toàn khác và khu vực đó phải "
               "được xem như một căn phòng như sẽ được mô tả sau trong chương này, "
               "cho khu vực nguy hiểm như mô tả trong Hình 5.10, dựa trên Bảng 3.2 "
               "theo cách tương tự như trường hợp một lỗ mở, chẳng hạn như cửa ra "
               "vào trong một căn phòng."))
    b.append(fig(10, FA.fig_f510()))
    b.append(h3("5.4 Phòng trên mặt đất", "5.4 Rooms above ground"))
    b.append(p("Như đã nêu trước đó, một phòng trên mặt đất mà không có bất kỳ nỗ "
               "lực thông gió nào sẽ có thời gian tồn lưu rất dài đối với bất kỳ sự "
               "phát thải nào của vật liệu dễ cháy. Một phương pháp tính toán giá "
               "trị này được đưa ra trong Chương 4 dựa trên một tiêu chuẩn Anh mới "
               "được đề xuất³. Tuy nhiên, khó có thể chắc chắn rằng mọi điểm bị "
               "khuất trong phòng sẽ được quét sạch trong thời gian quy định đó "
               "bằng thông gió qua khe hở, vì vậy phải giả định rằng thời gian tồn "
               "lưu có thể làm mất đi mối quan hệ giữa nguồn phát thải và phân loại "
               "khu vực. Không thể chấp nhận việc sử dụng một phòng không có yêu "
               "cầu thông gió được quy định rõ ràng cho bất kỳ mục đích nào làm cho "
               "phòng đó chứa nguồn phát thải nguy hiểm hơn nguồn phát thải cấp phụ. "
               "Trong những trường hợp như vậy, do thông gió kém, phân loại bên "
               "trong sẽ cho cấp Vùng 1, điều này rõ ràng gây khó khăn đáng kể trong "
               "việc sử dụng căn phòng."))
    b.append(p("Bất kỳ cửa nào dẫn vào phòng sẽ được xem như một nguồn phát thải "
               "tương đương với lượng hơi thoát ra bên trong phòng, và Bảng 3.2 phải "
               "được dùng để xác định phạm vi khu vực nguy hiểm bên ngoài phòng, "
               "quanh cửa hoặc lỗ mở khác. Khi trong phòng có chất lỏng ở nhiệt độ "
               "cao hơn điểm chớp cháy nhưng thấp hơn điểm sôi, phải bố trí hệ "
               "thống thoát nước để đảm bảo không hình thành vũng đáng kể, và khu "
               "vực nguy hiểm bên ngoài phải dựa trên Bảng 3.8 với giá trị tối "
               "thiểu 0,5 m trong trường hợp giả định không có sương mù. Đây là hệ "
               "số an toàn để tính đến các yếu tố chưa biết. Khi trong phòng chứa "
               "chất lỏng ở nhiệt độ cao hơn điểm sôi thì khu vực bên ngoài phòng "
               "(vốn là khu vực nguy hiểm) phải dựa trên Bảng 3.10. Các khu vực "
               "bên ngoài phòng này sẽ là Vùng 2 đối với nguồn phát thải cấp phụ "
               "(nguồn phát thải duy nhất được coi là chấp nhận được trong những "
               "trường hợp này), ngay cả khi vấn đề tồn lưu nhiều khả năng dẫn đến "
               "việc phân loại phòng là Vùng 1."))
    return "".join(b)


def body_en():
    b = []
    b.append(fig(5, FA.fig_f505()))
    b.append(h3("5.3 Roofs without walls or associated with one, two or three walls",
                "5.3 Roofs without walls or associated with one, two or three walls"))
    b.append(h4("5.3.1 Roofs without walls", "5.3.1 Roofs without walls"))
    b.append(p("There are two scenarios which must be considered here. The first is "
               "the flat roof, which is so typical of petrol station canopies, and "
               "the second, the hipped roof (dutch-barn construction) which is more "
               "common in industrial loading and unloading areas. This latter may "
               "be with vents or without vents, although, in most cases, vents are "
               "present particularly in cases where the flammable gas or vapour is "
               "lighter than air."))
    b.append(p("Where no walls are present the effect of a flat roof is dependent "
               "upon the proximity of the roof to the edge of the hazardous area "
               "which would be created if the release were in free air (see Fig. "
               "5.6). If the roof is more than 5 m beyond the extent of hazardous "
               "area predicted by Figs. 3.4 and 3.5 (in Chapter 3) the roof is "
               "unlikely to have any effect but in other cases the hazardous area "
               "is expected to reach the roof."))
    b.append(fig(6, FA.fig_f506()))
    b.append(p("Where a hipped (dutch-barn) type roof is present without walls and "
               "if the top of the hazardous area defined in the absence of the roof "
               "is within 5 m of the roof, the entire area contained by the roof "
               "will become a hazardous area of the same severity, provided that "
               "in cases where the flammable material is not heavier than air, "
               "vents must be provided in the apex of the roof. Figure 5.7 shows "
               "this situation and suggests a notional 1 m of hazardous area around "
               "the vents. This latter is difficult to predict but, at 1 m, is felt "
               "to be sufficiently large for most normal situations."))
    b.append(fig(7, FA.fig_f507()))
    b.append(h4("5.3.2 Roofs associated with one wall",
                "5.3.2 Roofs associated with one wall"))
    b.append(p("Where a wall is present in addition to the roof, the situation is "
               "further complicated and the hazardous areas described in Fig. 5.1 "
               "and 5.2 become modified to give the situation shown in Fig. 5.8. "
               "The main thing to notice here is the extension of the hazardous "
               "area over the roof for a small distance, given by the difference "
               "between the extent of the hazardous area produced when the wall is "
               "present and the length of the wall. The length is used in "
               "preference to the height as the overlap will only occur if the wall "
               "length is less than the horizontal extent of the hazardous area, "
               "which is already distorted by being extended up to the roof level. "
               "The situation is similar in respect of the situation with a hipped "
               "roof, but here the effects shown in Fig. 5.7 must also be taken into "
               "account."))
    b.append(fig(8, FA.fig_f508()))
    b.append(note("<b>Figure 5.8 legend note.</b> The printed legend defines V = "
                  "height of source of release but then gives a = E − Y and "
                  "b = 2y − 2a, with Y and y left undefined (likely misprints for "
                  "V). The printed symbols are preserved here rather than silently "
                  "corrected; the minimum extension over the roof is 0.5 m."))
    b.append(h4("5.3.2 Roofs associated with two walls",
                "5.3.2 Roofs associated with two walls"))
    b.append(note("<b>Numbering note.</b> On the same printed page (p. 132) the book "
                  "gives two consecutive sections both numbered 5.3.2: \"Roofs "
                  "associated with one wall\" and \"Roofs associated with two "
                  "walls\". With the sequence 5.3.1, 5.3.2, 5.3.2, 5.3.4 the second "
                  "section is logically 5.3.3; both printed numbers are preserved "
                  "here and are not silently renumbered."))
    b.append(p("Where two walls are present, then the entire area covered by the "
               "hazardous area shown in Figs. 5.3 and 5.4 will form part of the "
               "hazardous area up to the roof and down to the ground (see Fig. "
               "5.9). As for one wall, the extents of hazardous area above the roof "
               "line will be determined using Figs. 5.3 and 5.4."))
    b.append(fig(9, FA.fig_f509()))
    b.append(h4("5.3.4 Roofs associated with three walls",
                "5.3.4 Roofs associated with three walls"))
    b.append(p("Where three walls exist, the situation is entirely different and "
               "the area should be treated as a room as described later in this "
               "chapter, giving a hazardous area as described in Fig. 5.10, which "
               "is based on Table 3.2 in the same way as would be the case for an "
               "opening, such as a door in a room."))
    b.append(fig(10, FA.fig_f510()))
    b.append(h3("5.4 Rooms above ground", "5.4 Rooms above ground"))
    b.append(p("As previously stated, an above-ground room with no attempts made "
               "to give ventilation will have a very long retention of any release "
               "of flammable material. A method of calculating this is given in "
               "Chapter 4 based on a proposed new British Standard³. It is "
               "difficult, however, to be sure that all pockets of a room will be "
               "swept clear within this specified time by crack ventilation, and "
               "retention must be assumed to be capable of removing the source of "
               "hazard/classification relationship. It is not considered possible "
               "to countenance a room with no specifically included ventilation "
               "requirements being used for any purpose which means that it will "
               "contain sources of release more onerous than secondary grade "
               "sources of release. In such circumstances, the interior area "
               "classification will, because of the paucity of ventilation, give "
               "an internal classification of Zone 1, which will clearly introduce "
               "significant difficulty in the use of the room."))
    b.append(p("Any door which enters the room will be considered as a source of "
               "release equivalent to the quantity of vapour released within the "
               "room and Table 3.2 should be used to determine the extent of the "
               "hazardous area outside the room, around the door or other opening. "
               "Where liquids above their flashpoints but below their boiling "
               "points are contained within the room, drainage should be provided "
               "to ensure that a significant pool cannot form, and the external "
               "hazardous area should be based on Table 3.8 with a minimum of 0.5 "
               "m in cases where no mist is assumed. This latter is a safety factor "
               "to take account of unknowns. Where the room contains a liquid "
               "contained above its boiling point then the area outside the room "
               "(which is a hazardous area) should be based on Table 3.10. These "
               "areas outside the room will be Zone 2 in the case of secondary "
               "grade sources of release (the only sources of release considered "
               "as acceptable in these circumstances) even though the retention "
               "problem is likely to lead to the classification of the room as Zone "
               "1."))
    return "".join(b)
