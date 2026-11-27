# -*- coding: utf-8 -*-
"""Chapter 5, module B - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 127-130 (PDF pp. 148-151).

Section 5.2, "Effect of walls on hazardous areas": the single-wall
geometry of Figs. 5.1-5.2, the two- and three-wall rules of Figs. 5.3-5.4,
and the primary/secondary grade and retention caveats. The references to
Figs. 3.4/3.5 are preserved. Prose only; the vectors, captions and legends
of Figs. 5.1-5.5 belong to figure supplier Fig-S1 (mcmillanfig05_a), which
also owns Fig. 5.5. The page shell, references and legal line belong to
the integration module.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, fig

import mcmillanfig05_a as FA


def body_vi():
    b = []
    b.append(h3("5.2 Ảnh hưởng của tường đối với khu vực nguy hiểm",
                "5.2 Effect of walls on hazardous areas"))
    b.append(p("Ảnh hưởng của một bức tường đặt gần một khu vực được phân loại là "
               "nguy hiểm cũng giống như ảnh hưởng của sự gần mặt đất, dù tỷ trọng "
               "của vật liệu dễ cháy không có tác động rõ rệt như vậy. Nếu bỏ qua "
               "gió thịnh hành — vốn là giả định chung — thì sự hiện diện của một "
               "bức tường sẽ ảnh hưởng bất lợi đến sự trộn lẫn giữa khí và không "
               "khí, cũng như bất kỳ vật cản nào khác. Ảnh hưởng của sự hiện diện "
               "của một bức tường đơn là làm thay đổi hình học của một khu vực "
               "nguy hiểm theo cách tương tự như sự gần mặt đất (xem Hình 3.4 và "
               "3.5 để biết chi tiết). Khi bức tường không đủ dài hoặc đủ cao để "
               "chặn hoàn toàn hỗn hợp khí/không khí, khu vực nguy hiểm sẽ chảy "
               "vòng qua và phủ lên trên bức tường (xem Hình 5.1 và 5.2). Phạm vi "
               "bao quanh tạo ra này được xác định dựa trên toàn bộ lượng khí rò "
               "rỉ thoát ra ở mép của bức tường."))
    b.append(fig(1, FA.fig_f501()))
    b.append(fig(2, FA.fig_f502()))
    b.append(p("Cách tiếp cận này có thể mở rộng sang các trường hợp nguồn phát "
               "thải nằm trong một khu vực được giới hạn bởi hai hoặc ba bức "
               "tường. Hình 5.3, 5.4 và 5.5 cho thấy khu vực nguy hiểm bị ảnh "
               "hưởng như thế nào. Việc xác định khu vực nguy hiểm về cơ bản vẫn "
               "như trong trường hợp một bức tường, nhưng cần lưu ý rằng trừ khi "
               "các bức tường dài một cách bất thường trong kịch bản hai bức "
               "tường, khu vực nguy hiểm luôn kéo dài ít nhất tới đầu của cả hai "
               "bức tường. Trong kịch bản ba bức tường, phần kéo dài phải ít nhất "
               "tới đầu ngoài cùng của cả hai bức tường cánh, với toàn bộ diện "
               "tích bao quanh tạo thành khu vực nguy hiểm. Phạm vi thẳng đứng "
               "làm theo cách tiếp cận của trường hợp một bức tường."))
    b.append(fig(3, FA.fig_f503()))
    b.append(fig(4, FA.fig_f504()))
    b.append(p("Trong mọi trường hợp, cách tiếp cận này đều hợp lệ cho cả nguồn "
               "phát thải cấp chính lẫn cấp phụ và, nói chung, sự tồn lưu của hỗn "
               "hợp có khả năng nổ không đủ để tăng mức độ phân loại (tức là Vùng "
               "1 từ một nguồn phát thải cấp phụ)."))
    b.append(note(
        "<b>Ký hiệu trên hình, quy tắc tỷ trọng và các bẫy của bản gốc (Hình "
        "5.1–5.4).</b> Ở Hình 5.1 (tường cách nguồn phát thải 1.5–3 m): X = khoảng "
        "cách tường/nguồn phát thải; Y = khoảng cách từ nguồn tới mặt đất "
        "(Z − Y = 1.5–3 m); Z = phạm vi khu vực nguy hiểm; a = Z − X theo phương "
        "thẳng đứng hoặc Z − L theo phương nằm ngang; b = 0.5 Z chỉ khi tỷ trọng "
        "lớn hơn 1.3 × không khí; c = 0.5 Z chỉ khi tỷ trọng nhỏ hơn 0.7 × không "
        "khí; d = chiều dài tường tính từ các mép của khu vực nguy hiểm, và khi d "
        "nhỏ hơn Z thì nên kéo dài khu vực nguy hiểm qua mặt sau của bức tường. "
        "Ở Hình 5.2 (tường cách nguồn phát thải < 1.5 m): X = khoảng cách "
        "tường/nguồn phát thải (< 1.5 m); Y = khoảng cách từ nguồn tới mặt đất "
        "(Z − Y = < 1.5 m); Z = phạm vi khu vực nguy hiểm (chưa điều chỉnh); "
        "a = 1.5 Z − X; b = sự méo dạng của khu vực nguy hiểm (chỉ khi tỷ trọng "
        "lớn hơn 1.3); c = 0.75 Z (chỉ khi tỷ trọng nhỏ hơn 0.7). Ở Hình 5.3 và "
        "5.4: E = phạm vi nguy hiểm có tính đến sự gần tường; C = khoảng cách "
        "nguồn phát thải/đầu tường; a = E − C. <b>Bẫy của lớp văn bản:</b> chú "
        "giải in của Hình 5.1 viết a = Z − X (thẳng đứng) hoặc Z − L (nằm ngang), "
        "nhưng lớp văn bản PDF đọc chữ Z đầu tiên trong Z − L thành chữ số 2; "
        "hình ảnh in cho thấy chữ Z viết hoa và được giữ nguyên ở đây. Hình 5.2 "
        "in < 1.5 m cho X và Y (có thể định ý là ≤); ký tự in được giữ nguyên. "
        "Câu về ba bức tường được in với cách viết 'extention'; ở đây dùng "
        "'extension'."))
    return "".join(b)


def body_en():
    b = []
    b.append(h3("5.2 Effect of walls on hazardous areas",
                "5.2 Effect of walls on hazardous areas"))
    b.append(p("The effect of a wall close to an area which is classified as "
               "hazardous will be the same as that of ground proximity, although "
               "the density of the flammable material will not have such a marked "
               "effect. Neglecting prevailing winds, which has to be the case in "
               "general, the presence of a wall will adversely affect the mixing "
               "of gas and air, as will any other obstruction. The effects of the "
               "presence of a single wall will have the effect of changing the "
               "geometry of a hazardous area in the same way as ground proximity "
               "(see Figs. 3.4 and 3.5 for details). Where the wall is not of "
               "sufficient length or height to completely obstruct the gas/air "
               "mixture then the hazardous area will flow around and over it "
               "(see Figs. 5.1 and 5.2). The resultant wrap-around hazardous area "
               "has been based on the entire leak exiting the edge of the wall."))
    b.append(fig(1, FA.fig_f501()))
    b.append(fig(2, FA.fig_f502()))
    b.append(p("This approach may be extended to cases where the source of "
               "release is contained in an area bounded by two walls or by three "
               "walls. Figures 5.3, 5.4 and 5.5 indicate how the hazardous area "
               "is affected. Identification of the hazardous area will basically "
               "be as in the case of one wall, but it should be noted that unless "
               "the walls are extremely long in the case of the two-wall scenario, "
               "the hazardous area will always extend at least to the end of both "
               "walls. In the three-wall scenario, the extension should be at "
               "least as far as the outboard end of both wing walls, with all of "
               "the enclosed area forming the hazardous area. Vertical extents "
               "should follow the single wall approach."))
    b.append(fig(3, FA.fig_f503()))
    b.append(fig(4, FA.fig_f504()))
    b.append(p("In all cases this approach will be valid for both primary and "
               "secondary sources of release and, in general, the retention of "
               "explosive atmosphere will not be sufficient to increase the "
               "severity of classification (i.e., Zone 1 from a secondary source "
               "of release)."))
    b.append(note(
        "<b>Figure notation, density rules and source traps (Figs. 5.1–5.4).</b> "
        "In Fig. 5.1 (wall 1.5–3 m from the source): X = distance wall/source of "
        "release; Y = distance source to ground (Z − Y = 1.5–3 m); Z = extent of "
        "hazardous area; a = Z − X vertically or Z − L horizontally; b = 0.5 Z "
        "for densities greater than 1.3 × air only; c = 0.5 Z for densities less "
        "than 0.7 × air only; d = wall length from edges of hazardous area, and "
        "where d is less than Z it is prudent to continue the hazardous area "
        "across the rear face of the wall. In Fig. 5.2 (wall < 1.5 m from the "
        "source): X = distance wall/source of hazard (< 1.5 m); Y = distance "
        "source to ground (Z − Y = < 1.5 m); Z = extent of hazardous area "
        "(unmodified); a = 1.5 Z − X; b = distortion of hazardous area "
        "(densities greater than 1.3 only); c = 0.75 Z (densities less than 0.7 "
        "only). In Figs. 5.3 and 5.4: E = extent of hazard taking account of "
        "wall proximity; C = distance source of hazard/wall end; a = E − C. "
        "<b>Text-layer trap:</b> the printed legend of Fig. 5.1 reads "
        "a = Z − X (vertical) or Z − L (horizontal), but the PDF text layer "
        "renders the leading Z of Z − L as the digit 2; the image shows uppercase "
        "Z, which is retained here. Fig. 5.2 prints < 1.5 m for X and Y "
        "(possibly intended ≤); the printed glyph is retained. The three-wall "
        "sentence is printed with the spelling 'extention', given here as "
        "'extension'."))
    return "".join(b)
