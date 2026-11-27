# -*- coding: utf-8 -*-
"""Chapter 5, module A - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 125-127 (PDF pp. 146-148).

Covers the chapter opener and sections 5.1, 5.1.1-5.1.4, through the
below-ground-room discussion. Owns the chapter h2 and prose only; no
figures, tables or equations. The integration shell owns the page shell,
references and end matter.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h2, h3, h4, p, note


def body_vi():
    b = []
    b.append(h2("5 — Thực hành phân loại khu vực nguy hiểm đối với khí, hơi và "
                "sương mù chất lỏng ở những khu vực không được thông gió tự do",
                "5 — Area classification practice for gases, vapours and mists "
                "in areas which are not freely ventilated"))
    b.append(p("Trong chương 3, ảnh hưởng của các phát thải vật liệu dễ cháy ở "
               "những khu vực thông gió tự do đã được xem xét rất chi tiết. Cần "
               "nhớ rằng ở những khu vực đó, về mặt lý thuyết, có một lượng không "
               "khí pha loãng không hạn chế và sự nhiễu loạn lớn được tạo ra bởi "
               "gió và làn gió thông thường. Dù điều này hữu ích trong đa số các "
               "cơ sở lọc dầu và các nhà máy công nghiệp khác, có những trường hợp "
               "cần bao kín các nguồn phát thải tiềm ẩn vì lý do vận hành hoặc lý "
               "do an toàn khác. Chẳng hạn, phun sơn cần một môi trường được "
               "kiểm soát chặt chẽ, và ở những nơi xử lý các chất như xyanua, "
               "thường cần bao kín quá trình đó vì rò rỉ có thể gây hậu quả thảm "
               "khốc nếu không làm vậy. Tuy nhiên, một khi nguồn phát thải vật "
               "liệu dễ cháy được bao kín, nó bị từ chối lượng lớn không khí pha "
               "loãng và các điều kiện nhiễu loạn tự nhiên hiện có ở ngoài trời, "
               "và sự pha loãng cùng phân tán của nó trở thành một vấn đề đáng kể "
               "hơn. Không chỉ cực kỳ khó đưa đủ không khí pha loãng vào một "
               "không gian kín để mô phỏng chính xác tình huống bên ngoài ở mọi "
               "phần của không gian đó, mà điều này còn có thể gây phản ứng bất "
               "lợi cho nhân viên. Thường thì, trong điều kiện ngoài trời, "
               "chuyển động không khí vượt quá 1 m/s xảy ra trong phần lớn thời "
               "gian, nhưng trong điều kiện trong nhà bình thường, chuyển động "
               "không khí hơn 0.2 m/s có thể gây khó chịu cho những người làm "
               "việc trong nhà. Vì vậy, đây là một vấn đề phức tạp để giải quyết."))
    b.append(p("Dù những nơi có thông gió hạn chế thường được đồng nhất với các "
               "tòa nhà, nhiều nơi không phải là tòa nhà cũng nằm trong xem xét "
               "này. Thường thì, những nơi như bến bốc xếp xe tăng được che phủ "
               "để bảo vệ công việc khỏi tác động của môi trường. Khi làm vậy, "
               "phần bao kín thường chỉ là một cái mái và không có tường, và "
               "trong những trường hợp này, dù chuyển động không khí ở mặt đất "
               "sẽ tương tự như mức dự kiến trong tình huống thông gió tự do, vẫn "
               "có những vùng gần mái nơi thông gió bị hạn chế. Có bốn kịch bản "
               "trong đó thông gió tự nhiên phải được coi là bị hạn chế. Trong "
               "những trường hợp như vậy, mục tiêu quan trọng là bảo đảm rằng "
               "thông gió hiện có được sử dụng hiệu quả nhất, và điều này có "
               "nghĩa là cần xác định các nguồn phát thải và sắp xếp thông gió "
               "cần tính đến vị trí của chúng để thông gió tốt nhất tại những "
               "điểm có thể xảy ra phát thải."))

    b.append(h3("5.1 Các khu vực điển hình có thông gió hạn chế",
                "5.1 Typical areas of restricted ventilation"))
    b.append(p("Sau đây là những khu vực điển hình mà thông gió có thể được kỳ "
               "vọng là bị hạn chế. (tất nhiên, sự hạn chế cũng sẽ xuất hiện ở "
               "những khu vực khác)."))

    b.append(h4("5.1.1 Các khu vực hở được bao quanh bởi tường",
                "5.1.1 Open areas surrounded by walls"))
    b.append(p("Khi có tường hiện diện, bao quanh những khu vực lẽ ra là hở, thì "
               "những bức tường đó có thể hạn chế thông gió. BS 5345, phần 2¹ đề "
               "xuất rằng để có một khu vực hở, một tòa nhà không nên có tường "
               "bên dưới một độ cao đáng kể (chẳng hạn 3 m) thì mới được coi là "
               "thông gió tự do; nhưng một cách tiếp cận nới lỏng hơn được dùng "
               "trong Hướng dẫn của Tổng Giám đốc Lao động Hà Lan², theo đó giả "
               "định rằng, nếu 50 % tường của tòa nhà là kết cấu hở, tòa nhà được "
               "coi là khu vực thông gió tự do miễn là 50 % đó phân bố đều trên "
               "ít nhất ba bức tường và các lỗ mở có chiều cao ít nhất 2.5 m. Dù "
               "khác nhau về cách tiếp cận, cả hai phát biểu đều xác nhận thực "
               "tế là tường có tác động cản trở dòng khí cần được tính đến."))
    b.append(note("<b>Lưu ý về cách trích dẫn Hướng dẫn Hà Lan.</b> Thân văn bản "
                  "gọi đây là 'Hướng dẫn của Tổng Giám đốc Lao động Hà Lan²', "
                  "trong khi mục tài liệu tham khảo in là 'Directorate of Labour "
                  "(Netherlands)(1980)'. Cách gọi trong thân văn bản được giữ "
                  "nguyên theo bản in; không sửa cho khớp với danh mục."))

    b.append(h4("5.1.2 Các khu vực có mái che (kiểu chuồng Hà Lan)",
                "5.1.2 Covered areas (dutch-barn type)"))
    b.append(p("Ở những nơi như bến bốc xếp xe tăng, khu vực chứa thùng phuy và "
               "tương tự, thường cần cung cấp mái che để ngăn nước mưa thấm vào. "
               "Những mái che này có dạng mái phẳng (ví dụ như ở sân ga-ra) hoặc "
               "mái hồi (ví dụ như trong kiểu xây dựng chuồng Hà Lan), dạng sau "
               "thường có lỗ thông hơi ở đỉnh. Cả hai loại mái che này đều có "
               "thể có tác động bất lợi đến dòng khí, ngay cả trong trường hợp "
               "không có tường. Mức độ ảnh hưởng phụ thuộc vào khí hoặc hơi dễ "
               "cháy đang được xử lý và chiều cao của mái che, ngay cả khi các "
               "yêu cầu về tường hở nêu trên đã được đáp ứng."))

    b.append(h4("5.1.3 Các phòng trên mặt đất", "5.1.3 Above-ground rooms"))
    b.append(p("Các phòng trên mặt đất là phòng có bốn bức tường và một mái, "
               "không có thông gió chủ động hiệu quả. Trong những trường hợp này "
               "sẽ có chuyển động không khí do thông gió tự nhiên qua các vết "
               "nứt trong kết cấu hoặc quanh cửa ra vào và cửa sổ, v.v. Bảng 4.2 "
               "cho thấy mức thông gió có thể dự kiến trong những trường hợp "
               "này và mức này được xem là luồng khí tương đương với thể tích "
               "của phòng trong khoảng một giờ trong đa số trường hợp. Điều này "
               "không có nghĩa là không khí trong tòa nhà được thay đổi trong "
               "một giờ, vì các dòng khí bên trong sẽ không đồng đều và những "
               "vùng góc của phòng sẽ cần nhiều thời gian hơn để thay hết không "
               "khí. Để thay đổi hoàn toàn không khí trong phòng, dự kiến phải "
               "trôi qua nhiều giờ và do đó thời gian tồn lưu của bất kỳ khí hoặc "
               "hơi dễ cháy nào sẽ dài."))
    b.append(note("<b>Lưu ý về tài liệu tham chiếu 'Bảng 4.2'.</b> Văn bản in "
                  "nêu: 'Bảng 4.2 cho thấy mức thông gió có thể dự kiến'. Không "
                  "có bảng nào về thông gió được in trong chương 4 hay chương 5 "
                  "(Bảng 4.2 của chương 4 là bảng áp suất hơi). Số tham chiếu in "
                  "được giữ nguyên và không được gán cho bảng thực tế nào."))
    b.append(p("Thời gian tồn lưu này có thể đủ dài để làm gián đoạn mối quan hệ "
               "giữa nguồn phát thải và phân loại khu vực, chắc chắn là ở những "
               "vùng góc trong phòng. Dù thông gió có thể được cải thiện bằng "
               "cách bổ sung các lỗ mở trên tường phòng, đây không nhất thiết là "
               "lựa chọn tốt như thoạt nhìn. Hầu hết các lỗ mở như vậy được lắp "
               "cửa chớp (louvre), vốn cần thiết để duy trì tính toàn vẹn của "
               "phòng trong những trường hợp này. Cửa chớp và các thiết bị tương "
               "tự như lưới có tác động rất bất lợi đến thông gió. Các thí "
               "nghiệm đã chỉ ra, ví dụ, rằng các lỗ mở được bố trí chiến lược "
               "trên tường của tòa nhà tạo ra luồng khí đáng kể (lên tới 0.3 m/s) "
               "cách tường tới 10 m, nhưng việc lắp cửa chớp có tác động tiêu "
               "cực đáng kể, vì khi có cửa chớp trong một lỗ mở lẽ ra tạo ra "
               "luồng khí như mô tả ở trên, không phát hiện được luồng khí đáng "
               "kể nào ở khoảng cách hơn 3 m từ tường¹."))

    b.append(h4("5.1.4 Các phòng dưới mặt đất", "5.1.4 Below-ground rooms"))
    b.append(p("Các phòng dưới mặt đất tạo ra tình huống bất lợi nhất có thể vì "
               "chỉ có lối vào là ở trên mặt đất, không có khả năng bố trí hiệu "
               "quả các lỗ mở, và thông gió qua vết nứt về thực tế là không có. "
               "Thời gian để toàn bộ không khí trong phòng được thay đổi, dù "
               "không phải là vô hạn, là rất dài (nhiều giờ). Bất kỳ phát thải "
               "nào trong những phòng như vậy dự kiến sẽ tồn tại đủ lâu để "
               "khiến phòng được phân loại là Vùng 0, ngay cả khi phát thải đến "
               "từ một nguồn phát thải cấp phụ."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("5 — Area classification practice for gases, vapours and mists "
                "in areas which are not freely ventilated",
                "5 — Area classification practice for gases, vapours and mists "
                "in areas which are not freely ventilated"))
    b.append(p("In Chapter 3 the effects of releases of flammable materials in "
               "freely ventilated areas was considered in much detail. It will "
               "be remembered that in such areas there was, theoretically, an "
               "unlimited amount of diluting air and much turbulence was "
               "produced by normal winds and breezes. While this is useful in "
               "the majority of oil-refining installations and other process "
               "plants, there are cases where it is necessary to enclose the "
               "sources of possible release for operational or other safety "
               "reasons. Paint Spraying, for instance, needs a carefully "
               "controlled environment and where such things as cyanide are "
               "processed it is often necessary to enclose that process as "
               "leakage could have catastrophic effects if this were not done. "
               "Once a source of release of flammable material is enclosed, "
               "however, it is denied the large quantity of diluting air and "
               "the natural turbulent conditions present in an outside area, "
               "and its dilution and dispersion becomes a more significant "
               "problem. Not only is it extremely difficult to introduce "
               "sufficient diluting air into an enclosed space to accurately "
               "mimic the external situation in all parts of that enclosed "
               "space, but it can cause adverse personnel reaction. Typically, "
               "in external situations air movement in excess of 1 m/s occurs "
               "for much of the time, but in normal indoor conditions an air "
               "movement of more than 0.2 m/s is likely to cause discomfort to "
               "those normally working indoors. The problem is, therefore, a "
               "complex one to approach."))
    b.append(p("While places where ventilation is limited tend to be equated "
               "with buildings, many places which are not buildings are "
               "included in this consideration. Often, such places as tanker "
               "loading bays are covered to protect operations from the "
               "environment. Where this is done the enclosure is usually just "
               "a roof and without walls and in these circumstances, although "
               "the ground-level air movement will be similar to that which "
               "would be expected in a freely ventilated situation, there will "
               "be areas near the roof where ventilation is restricted. There "
               "are four scenarios in which natural ventilation must be "
               "considered as restricted. In such circumstances the important "
               "objective is to ensure that such ventilation as exists is used "
               "to best effect, and this means that sources of release need to "
               "be identified and ventilation arrangements need to take account "
               "of their location so that ventilation is best at points where "
               "releases can occur."))

    b.append(h3("5.1 Typical areas of restricted ventilation",
                "5.1 Typical areas of restricted ventilation"))
    b.append(p("The following are typical of the areas where ventilation can "
               "be expected to be restricted. (restriction will, of course, "
               "also appear in other areas)."))

    b.append(h4("5.1.1 Open areas surrounded by walls",
                "5.1.1 Open areas surrounded by walls"))
    b.append(p("Where walls are present, containing otherwise open areas, then "
               "such walls can restrict ventilation. BS 5345, Part 2¹ suggests "
               "that to have an open area, a building should have no walls "
               "below a significant height (say 3 m) to be assumed to be "
               "freely ventilated but a more relaxed approach is used in a "
               "Netherlands Directorate General of Labour Guide² which presumes "
               "that, provided 50 per cent of a building's walls are open "
               "construction, the building is considered as a freely ventilated "
               "area if the 50 per cent is evenly distributed over at least "
               "three walls and openings are at least 2.5 m high. While "
               "differing in approach, both of these statements confirm the "
               "fact that walls have an obstructing effect on airflow which "
               "must be taken into account."))
    b.append(note("<b>Note on the Netherlands guide citation.</b> The body text "
                  "calls this the 'Netherlands Directorate General of Labour "
                  "Guide²', while printed reference 2 is worded 'Directorate of "
                  "Labour (Netherlands)(1980)'. The body wording is preserved as "
                  "printed and is not aligned with the reference list."))

    b.append(h4("5.1.2 Covered areas (dutch-barn type)",
                "5.1.2 Covered areas (dutch-barn type)"))
    b.append(p("In areas, such as tanker loading bays, drum storage areas, and "
               "the like, it is often necessary to provide a cover to prevent "
               "rain penetration. These covers take the form of either flat "
               "roofs (e.g., as in garage forecourts) or hipped roofs (e.g., as "
               "those in dutch-barn type construction), the latter often having "
               "apex vents. Both of these types of cover have a possibly "
               "deleterious effect on airflow, even though there are no walls "
               "in such cases. The degree of effect depends upon the flammable "
               "gas or vapour being handled and the height of the cover, even "
               "though the open wall requirements specified above are met."))

    b.append(h4("5.1.3 Above-ground rooms", "5.1.3 Above-ground rooms"))
    b.append(p("Above-ground rooms constitute a room which has four walls and a "
               "roof with no effective deliberate ventilation. In such cases "
               "there will be air movement by natural ventilation via cracks "
               "in the structure or around doors and windows, etc. Table 4.2 "
               "shows the level of ventilation which may be expected in such "
               "cases and this will be seen as airflow equivalent to the volume "
               "of the room in around one hour in most cases. This will not "
               "mean an air change in the building in one hour as the internal "
               "air currents will not be uniform and pockets of the room will "
               "require more time to be purged of air. To completely change the "
               "air in the room it is expected that several hours will need to "
               "elapse and, therefore, the retention time of any flammable gas "
               "or vapour will be long."))
    b.append(note("<b>Note on the 'Table 4.2' cross-reference.</b> The printed "
                  "text states: 'Table 4.2 shows the level of ventilation which "
                  "may be expected'. No ventilation table is printed in Chapter "
                  "4 or Chapter 5 (Chapter 4's Table 4.2 is a vapour-pressure "
                  "table). The printed reference number is preserved verbatim "
                  "and has not been mapped to any real table."))
    b.append(p("This retention time may be sufficiently long to disrupt the "
               "source of release/classification of area relationship, "
               "certainly in pockets in the room. While this ventilation may "
               "be improved by the inclusion of openings in room walls, this "
               "is not necessarily as good an option as at first thought. Most "
               "such openings are fitted with louvres which are necessary to "
               "maintain the integrity of the room in such circumstances. "
               "Louvres and similar devices such as meshes have a severely "
               "deleterious effect on ventilation. Experiments have shown, for "
               "example that strategically placed openings in walls of "
               "buildings produce significant airflows (up to 0.3 m/s) up to "
               "10 m from the walls, but the inclusion of louvres has a "
               "significant negative effect in that when a louvre is present "
               "in an opening which would otherwise produce the airflow "
               "described above, no significant airflow is detectable more "
               "than 3 m from the walls¹."))

    b.append(h4("5.1.4 Below-ground rooms", "5.1.4 Below-ground rooms"))
    b.append(p("Below-ground rooms produce the most adverse situation possible "
               "because only the entry is above ground there is no possibility "
               "of effectively introducing openings, and crack ventilation is "
               "effectively absent. The time for the totality of the air in the "
               "room to change, while not being infinite, is very long (many "
               "hours). Any release in such rooms would be expected to persist "
               "for long enough to cause the room to be classified as Zone 0, "
               "even if the release was from a secondary source of release."))
    return "".join(b)
