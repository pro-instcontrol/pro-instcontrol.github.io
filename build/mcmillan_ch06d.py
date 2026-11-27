# -*- coding: utf-8 -*-
"""Chapter 6, module D - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas* (1998),
printed pp. 161-163 (PDF pp. 182-184): section 6.3 Practical situations
and its three qualitative walkthroughs 6.3.1-6.3.3. Figures 6.1-6.3 are
cited by number only; the shell and the figure supplier own the drawings
and the reference list. Unofficial study translation.
"""
from mcmillan_common import h3, h4, p, note


def body_vi():
    b = []

    # --- 6.3 ---------------------------------------------------------------
    b.append(h3("6.3 Các tình huống thực tế",
                "6.3 Practical situations"))
    b.append(note("<b>Ghi chú khi đọc.</b> Mục 6.3 (trang in 161–163) đưa ra ba "
                  "cuộc phân loại minh họa mang tính định tính, không phải ví dụ "
                  "tính toán số học: không có tốc độ phát thải nào được tính và "
                  "không có phạm vi nào được suy ra bằng công thức. Việc gán "
                  "Vùng 20/21/22 dưới đây đi theo lập luận in trong sách; mỗi "
                  "hình chỉ được viện dẫn bằng số hiệu."))

    # --- 6.3.1 -------------------------------------------------------------
    b.append(h4("6.3.1 Cyclone và túi lọc bụi",
                "6.3.1 Cyclones and bag filters"))
    b.append(p("Hình 6.1 cho thấy một cyclone đang tách sản phẩm của một quá "
               "trình — sản phẩm này được tạo thành từ các hạt (granules) — khỏi "
               "bụi cùng vật liệu do chính quá trình đó tạo ra. Cyclone và túi "
               "lọc bụi được đặt trong hai phòng nhỏ riêng biệt, với khí từ túi "
               "lọc bụi thải ra ngoài tòa nhà. Tình trạng khu vực nguy hiểm như "
               "sau."))
    b.append(p("<b>Vùng 20.</b> Cả bên trong cyclone và túi lọc bụi ở phía bột "
               "của bộ lọc đều là Vùng 20, vì bụi luôn hiện diện ở cả hai. Vì "
               "quá trình vận hành bằng cách hút khí, hệ thống có áp suất thấp "
               "hơn một chút so với áp suất khí quyển, nên có thể bỏ qua sự rò "
               "rỉ từ đường ống và từ hai bình chứa."))
    b.append(p("<b>Vùng 21.</b> Vì hệ thống vận hành ở áp suất thấp hơn một chút "
               "so với khí quyển, không có bụi rò rỉ ra từ hệ thống trong vận "
               "hành bình thường. Tuy nhiên, bụi từ bộ lọc được xả vào một túi, "
               "và sự phát thải có thể xảy ra trong vận hành bình thường quanh "
               "ống xả. Vòi xả là nguồn phát thải cấp chính, và Vùng 21 sẽ tồn "
               "tại trong khoảng '1 m above and around it and down to floor "
               "level' — tức là 1 m phía trên và quanh vòi xả, và xuống tới mặt "
               "sàn."))
    b.append(note("<b>Lưu ý về cụm từ in.</b> Bản in viết Vùng 21 sẽ tồn tại "
                  "'for a distance of 1 m above and around it and down to floor "
                  "level', tức là '1 m above and around it and down to floor "
                  "level'. Cụm từ được giữ nguyên; đây là mô tả định tính bằng "
                  "lời, không phải kết quả tính toán."))
    b.append(p("<b>Vùng 22.</b> Sự phát thải bụi từ ống xả có thể tạo ra các lớp "
               "bụi lắng, nhưng trong vận hành bình thường người ta kỳ vọng "
               "công tác dọn dẹp sẽ giới hạn các lớp này trong Vùng 21. Tuy "
               "nhiên, thỉnh thoảng phải kỳ vọng rằng do sự lệch vị trí của "
               "thùng chứa bụi, hỏng cơ cấu làm kín giữa thùng và ống (thường là "
               "một gioăng giãn nở chạy bằng khí nén — air-operated expanding "
               "seal), một lượng bụi đáng kể hơn sẽ được giải phóng. Dù điều "
               "này không ảnh hưởng lớn đến phạm vi đám mây bụi vì những lý do "
               "đã nêu, nó sẽ làm tăng lượng bụi tạo lớp lắng và có lẽ công tác "
               "dọn dẹp sẽ không đủ để giới hạn phạm vi các lớp này trong trường "
               "hợp đó. Do đó, Vùng 22 sẽ tồn tại ở khoảng cách lớn hơn do "
               "những hoàn cảnh này và, vì khó xác định phạm vi của nó, người ta "
               "giả định nó bao phủ toàn bộ tòa nhà. Nếu trong tòa nhà không có "
               "mặt bệ, v.v., thì có thể giả định Vùng 22 bị giới hạn chiều cao "
               "ở mức '3m or so', tức là '3 m or so' — khoảng 3 m."))
    b.append(note("<b>Lưu ý về cụm từ in.</b> Bản in viết Vùng 22 có thể được "
                  "giả định là giới hạn chiều cao 'to 3m or so'. Cụm 'or so' "
                  "được giữ nguyên; '3 m or so' là ước lượng định tính, không "
                  "phải kích thước đo đạc chính xác."))

    # --- 6.3.2 -------------------------------------------------------------
    b.append(h4("6.3.2 Nạp liệu bằng phễu trong nhà",
                "6.3.2 Loading hoppers within buildings"))
    b.append(p("Việc dùng phễu làm phương tiện nạp bột vào quá trình là rất "
               "phổ biến, và thường thì các phễu này nằm ở tầng trên, với cơ cấu "
               "làm kín hiệu quả để ngăn bụi tràn đổ tiếp cận các tầng sản "
               "xuất. Trong những hoàn cảnh đó, phân loại Vùng của khu vực nạp "
               "liệu như sau. (Xem Hình 6.2.)"))
    b.append(p("<b>Vùng 20.</b> Phễu thường được nạp đầy hoặc nạp một phần bằng "
               "nguyên liệu, được đưa vào bằng cách đổ các thùng chứa, chẳng "
               "hạn như bao tải nguyên liệu. Thông thường sẽ có các lớp dày "
               "nguyên liệu và có thể có cả những đám mây nhỏ của vật liệu "
               "trong giới hạn của phễu. Vì lý do này, bên trong phễu được coi "
               "là Vùng 20."))
    b.append(p("<b>Vùng 21.</b> Khu vực quanh cửa nạp liệu sẽ bị nhiễm các đám "
               "mây bụi trong khi nạp bao tải nếu không hết sức cẩn thận và, vì "
               "tình huống này rất có khả năng xảy ra, các đám mây do việc đổ "
               "bao tải, v.v., vào phễu được coi là nguồn phát thải cấp chính, "
               "tạo Vùng 21 quanh cửa nạp, kéo dài '1 m above and around the "
               "manhole and down to the top of the manhole or the floor as "
               "appropriate' — tức là 1 m phía trên và quanh cửa nạp, và xuống "
               "tới đỉnh cửa nạp hoặc mặt sàn tùy trường hợp. Có thể loại bỏ "
               "hiệu quả Vùng 21 bằng cách hút không khí trong phòng vào trong "
               "phễu, để bụi phát thải được hút ngược vào phễu. Khi đó, không "
               "còn Vùng 21 quanh cửa nạp. Lưu lượng khí tối thiểu được coi là "
               "cần thiết để đạt được điều này sẽ tạo ra 'velocity of 1 m/s at "
               "the manhole mouth' — vận tốc 1 m/s tại miệng cửa nạp."))
    b.append(note("<b>Lưu ý về cụm từ in.</b> Bản in nêu lưu lượng khí tối thiểu "
                  "được coi là cần thiết sẽ tạo ra 'a velocity of 1 m/s at the "
                  "manhole mouth', tức là 'velocity of 1 m/s at the manhole "
                  "mouth'. Cụm từ được giữ nguyên; giá trị 1 m/s được nêu như "
                  "một vận tốc tại miệng cửa nạp, không phải lưu lượng thể "
                  "tích."))
    b.append(p("<b>Vùng 22.</b> Bụi sẽ lắng từ đám mây nhưng thường được xử lý "
               "bằng công tác dọn dẹp. Tuy nhiên, điều này không phải lúc nào "
               "cũng đúng và thỉnh thoảng sẽ có sự tràn đổ từ các bao tải trong "
               "phòng. Những tình huống này tạo thành các nguồn phát thải cấp "
               "phụ, dẫn đến Vùng 22 trong phòng. Như trước, trừ khi phòng lớn, "
               "Vùng 22 được giả định kéo dài toàn bộ diện tích và chiều cao "
               "của phòng, trừ khi có thể bảo đảm không có mặt bệ ở tầng cao, "
               "trong trường hợp đó có thể áp dụng giới hạn chiều cao 3 m. Nếu "
               "công tác dọn dẹp đạt mức mà sự tràn đổ được dọn ngay tại thời "
               "điểm xảy ra và phễu được bố trí để hút không khí từ phòng vào "
               "trong nó, thì Vùng 22 có thể được giới hạn ở 'around 2 m' — "
               "khoảng 2 m — quanh cửa nạp của phễu, vì bụi chỉ được giải phóng "
               "từ quá trình nạp một cách bất thường khi hệ thống hút khí bị "
               "hỏng."))
    b.append(note("<b>Lưu ý về cụm từ in.</b> Bản in viết Vùng 22 có thể được "
                  "giới hạn 'to around 2m surrounding the hopper manhole', tức "
                  "là 'around 2 m'. Cụm 'around' được giữ nguyên; đây là ước "
                  "lượng định tính, không phải ranh giới đo đạc chính xác."))

    # --- 6.3.3 -------------------------------------------------------------
    b.append(h4("6.3.3 Nạp liệu bằng phễu ngoài nhà",
                "6.3.3 Loading hoppers outside buildings"))
    b.append(p("Khi phễu nằm ở khu vực thông gió tốt (ngoài trời), các Vùng 20 "
               "và 21 được mô tả như trong Mục 6.3.2. Vùng 22 thì khác. (Xem "
               "Hình 6.3.)"))
    b.append(p("<b>Vùng 22.</b> Tình huống ngoài trời được giả định là có sự "
               "chuyển động không khí đáng kể, và điều này hạn chế sự lắng đọng "
               "của bụi nên Vùng 22 có kích thước hữu hạn. Do chuyển động không "
               "khí, bụi tràn đổ sẽ bị thổi bay nhanh chóng và công tác dọn dẹp "
               "bao phủ trường hợp hiếm hoi không bị thổi bay. Kích thước của "
               "Vùng 22 trong những hoàn cảnh này 'unlikely to exceed 3 m in "
               "dimension' — khó có thể vượt quá 3 m về kích thước. Tuy nhiên, "
               "cần thận trọng xác định những nơi mà các vật cản, chẳng hạn như "
               "tường, có thể gây tích tụ bụi do gió mang theo, tạo thành các "
               "lớp có độ dày nguy hiểm."))
    b.append(note("<b>Lưu ý về cụm từ in.</b> Bản in nêu kích thước của Vùng 22 "
                  "'is unlikely to exceed 3 m in dimension', tức là 'unlikely "
                  "to exceed 3 m'. Cụm từ được giữ nguyên; đây là nhận định "
                  "định tính về phạm vi, không phải giới hạn tính toán."))
    return "".join(b)


def body_en():
    b = []

    # --- 6.3 ---------------------------------------------------------------
    b.append(h3("6.3 Practical situations",
                "6.3 Practical situations"))
    b.append(note("<b>Reading note.</b> Section 6.3 (printed pp. 161–163) is a "
                  "set of three qualitative classification walkthroughs rather "
                  "than numerical worked examples: no release rates are "
                  "calculated and no extents are derived by formula. The Zone "
                  "20/21/22 assignments below follow the printed reasoning, "
                  "and each figure is cited by number only."))

    # --- 6.3.1 -------------------------------------------------------------
    b.append(h4("6.3.1 Cyclones and bag filters",
                "6.3.1 Cyclones and bag filters"))
    b.append(p("Figure 6.1 shows a cyclone which is separating the product of a "
               "process which is formed of granules from dust of the same "
               "material produced by the process. The cyclone and bag filter "
               "are in separate small rooms, with the bag filter air exhausting "
               "to the outside of the building. The hazardous area situation "
               "is as follows."))
    b.append(p("<b>Zone 20.</b> Both the interior of the cyclone and the bag "
               "filter on the powder side of the filter will be Zone 20, because "
               "dust is always present in both. As the process works by "
               "extracting air, the system is at a pressure slightly lower than "
               "that of the atmosphere and leakage from the pipework and the "
               "two vessels may be ignored."))
    b.append(p("<b>Zone 21.</b> As the system works at slightly lower than "
               "atmospheric pressure there is no leakage of dust from the "
               "system in normal operation. The dust from the filter is, "
               "however, discharged into a bag and release is possible in "
               "normal operation around the discharge duct. The discharge "
               "nozzle is a primary grade source of release and a Zone 21 will "
               "exist for a distance of 1 m above and around it and down to "
               "floor level."))
    b.append(note("<b>Printed-phrase note.</b> The print states that a Zone 21 "
                  "will exist 'for a distance of 1 m above and around it and "
                  "down to floor level', that is, '1 m above and around it and "
                  "down to floor level'. The phrase is retained verbatim; it is "
                  "a qualitative description in words, not a calculated "
                  "result."))
    b.append(p("<b>Zone 22.</b> The release of dust from the discharge duct can "
               "produce layers of dust, but in normal operation it is expected "
               "that housekeeping will limit the extent of these layers to "
               "within the Zone 21. It must occasionally be expected, however, "
               "that due to misalignment of the dust receptacle, failure of the "
               "receptacle/duct sealing arrangements (usually an air-operated "
               "expanding seal) significantly more dust will be released. While "
               "this will not greatly affect the extent of the dust cloud for "
               "reasons already mentioned, it will increase the amount of "
               "dust-forming layers and probably the housekeeping will not be "
               "sufficient to limit the extent of the layers in this case. "
               "Therefore, a Zone 22 will exist for a larger distance because "
               "of these circumstances and, as it will be difficult to define "
               "its extent, it will be assumed to cover the entire building. If "
               "there were no ledges, etc., in the building it may be possible "
               "to assume the Zone 22 is limited in height to 3m or so."))
    b.append(note("<b>Printed-phrase note.</b> The print says the Zone 22 might "
                  "be assumed limited in height 'to 3m or so' — that is, '3 m or "
                  "so' (about 3 m). The hedge 'or so' is retained verbatim; this "
                  "is a qualitative estimate, not a precise dimension."))

    # --- 6.3.2 -------------------------------------------------------------
    b.append(h4("6.3.2 Loading hoppers within buildings",
                "6.3.2 Loading hoppers within buildings"))
    b.append(p("It is quite common to use hoppers as a means of loading powders "
               "into process and quite often these hoppers will be on upper "
               "floors with effective sealing arrangements to prevent spilled "
               "dust from accessing the process floors. In these circumstances "
               "the following is the Zonal classification of the loading area. "
               "(See Fig. 6.2.)"))
    b.append(p("<b>Zone 20.</b> The hopper is normally filled, or partially "
               "filled, with feedstock which is loaded into it by discharging "
               "containers, such as sacks of raw material. There will normally "
               "be thick layers of feedstock and possibly small clouds of the "
               "material within the confines of the hopper. For this reason the "
               "interior of the hopper will be considered as Zone 20."))
    b.append(p("<b>Zone 21.</b> The area around the manhole will be contaminated "
               "with dust clouds during loading of sacks if extreme care is not "
               "exercised and, as it is so likely that this situation will "
               "occur, the clouds produced by emptying of sacks, etc., into the "
               "hopper will be considered as a primary grade source of release "
               "giving a Zone 21 around the charging manhole, extending to 1 m "
               "above and around the manhole and down to the top of the manhole "
               "or the floor as appropriate. The Zone 21 can effectively be "
               "removed by extracting room air into the hopper so that any dust "
               "released is effectively sucked into the hopper. In this case, "
               "there will be no Zone 21 around the manhole. The minimum airflow "
               "considered necessary to achieve this will produce a velocity of "
               "1 m/s at the manhole mouth."))
    b.append(note("<b>Printed-phrase note.</b> The print states that the minimum "
                  "airflow considered necessary 'will produce a velocity of 1 "
                  "m/s at the manhole mouth', that is, 'velocity of 1 m/s at the "
                  "manhole mouth'. The phrase is retained verbatim; 1 m/s is "
                  "given as a velocity at the mouth of the manhole, not as a "
                  "volumetric flow."))
    b.append(p("<b>Zone 22.</b> Dust will settle from the cloud but will "
               "normally be taken care of by housekeeping. This, however, will "
               "not always be so and occasionally there will be spillage from "
               "the bags in the room. These situations will constitute "
               "secondary grade sources of release, which will give rise to "
               "Zone 22 in the room. As before, unless the room is large the "
               "Zone 22 will be assumed to extend for the whole area of the "
               "room and its height, unless there can be guaranteed to be no "
               "ledges at high level in which case a height restriction of 3 m "
               "may be appropriate. If the housekeeping is of such a standard "
               "that spillages are removed at the time which they occur and the "
               "hopper is arranged so that air is extracted from the room into "
               "it, then the Zone 22 can be limited to around 2m surrounding "
               "the hopper manhole, as dust will only be released from the "
               "loading procedure abnormally when the air extract system "
               "fails."))
    b.append(note("<b>Printed-phrase note.</b> The print says the Zone 22 'can "
                  "be limited to around 2m surrounding the hopper manhole', "
                  "that is, 'around 2 m'. The word 'around' is retained "
                  "verbatim; this is a qualitative estimate, not a precise "
                  "boundary."))

    # --- 6.3.3 -------------------------------------------------------------
    b.append(h4("6.3.3 Loading hoppers outside buildings",
                "6.3.3 Loading hoppers outside buildings"))
    b.append(p("Where hoppers are in well-ventilated areas (outdoors) the Zones "
               "20 and 21 are as described in Section 6.3.2. The Zone 22 however "
               "is different. (See Fig. 6.3.)"))
    b.append(p("<b>Zone 22.</b> The outdoor situation is one in which there is "
               "assumed to be significant air movement and this will limit the "
               "deposition of dust so that the Zone 22 will have a finite size. "
               "Because of the air movement, spillage will be blown away "
               "rapidly and housekeeping will cover the unusual situation where "
               "it is not. The size of the Zone 22 in these circumstances is "
               "unlikely to exceed 3 m in dimension. Care should be taken, "
               "however, to identify any places where obstructions, such as "
               "walls, could cause build-up of wind-borne dust to allow layers "
               "of dangerous thickness."))
    b.append(note("<b>Printed-phrase note.</b> The print states that the size of "
                  "the Zone 22 'is unlikely to exceed 3 m in dimension', that "
                  "is, 'unlikely to exceed 3 m'. The phrase is retained "
                  "verbatim; it is a qualitative statement of extent, not a "
                  "calculated limit."))
    return "".join(b)
