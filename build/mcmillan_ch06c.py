# -*- coding: utf-8 -*-
"""Chapter 6, module C - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas* (1998),
printed pp. 157-160 (PDF pp. 178-181): the tail of 6.2.2 (Zone 20 cloud
completion and the layer rules for continuous, primary and secondary
grade sources), the 50-100 g of dust per m³ conclusion, section 6.2.3
on extents, Figures 6.1-6.3, and the layer/storage prose on printed
p.160. Continues directly after module B; the 6.2.2 heading is not
re-emitted and this module owns no tables or equations. Unofficial
study translation; the integration module owns the page shell.
"""
from mcmillan_common import h4, p, note, fig
import mcmillanfig06 as F


def body_vi():
    b = []

    # --- 6.2.2, continued: Zone 20 completion and layer rules --------------
    b.append(p("Các lớp bụi hình thành cũng tạo ra các khu vực nguy hiểm sau "
               "đây. Một lớp bụi không kiểm soát (tức là lớp không bị giới hạn "
               "độ dày bằng công tác dọn dẹp) sẽ tạo ra Vùng 20. Những lớp này "
               "thường chỉ tồn tại bên trong các bình chứa, v.v., và vì chúng "
               "rất dày (vượt quá 5 mm) nên có thể có những tính chất khác với "
               "các lớp được kiểm soát. Những lớp như vậy sẽ không được chấp "
               "nhận bên ngoài phần che chắn như các bình chứa quá trình, xét "
               "theo Mục 31 của Factories Acts¹. Một lớp bụi được kiểm soát "
               "(tức là lớp được giới hạn độ dày dưới 5 mm bằng dọn dẹp hoặc "
               "các biện pháp khác) do nguồn phát thải cấp liên tục tạo ra sẽ "
               "chỉ cho Vùng 21 nếu bị xáo trộn thường xuyên, và chỉ cho Vùng "
               "22 nếu hiếm khi bị xáo trộn. Vấn đề chủ yếu là các đám mây bụi "
               "do lớp bụi tạo ra khi bị xáo trộn, vì thiết bị điện được thiết "
               "kế để làm việc trong độ dày lớp bụi này. Khi có thể kiểm soát "
               "chắc chắn độ dày lớp bụi dưới 0.5 mm thì ít có khả năng có đủ "
               "bụi để tạo thành khí quyển nổ và, do đó, không giả định tồn tại "
               "khu vực nguy hiểm nào do sự hiện diện của nó, vì khi bị xáo "
               "trộn nó không có khả năng tạo ra đám mây bụi có thể bắt lửa."))
    b.append(p("Nguồn phát thải cấp chính sẽ tạo ra Vùng 21 nếu nó tạo ra một "
               "đám mây bụi. Phạm vi của Vùng 21 đó sẽ phụ thuộc vào sự phân "
               "tán của đám mây bụi hoặc sự lắng đọng của bụi để tạo thành "
               "lớp. Như trước đó, lớp bụi được xét là tạo ra các Vùng sau. "
               "Khi hình thành một lớp bụi không kiểm soát (lớp không được "
               "giới hạn dưới 5 mm bằng dọn dẹp, v.v.) thì kết quả là Vùng 20 "
               "trong khu vực do lớp bụi đó phủ lên. Khi hình thành một lớp "
               "bụi được kiểm soát có độ dày dưới 5 mm nhưng bị xáo trộn đều "
               "xuyên thì kết quả là Vùng 21 trong khu vực quanh lớp bụi. Khi "
               "lớp bụi không bị xáo trộn đều xuyên thì khu vực nguy hiểm giảm "
               "xuống Vùng 22. Khi lớp bụi được kiểm soát ở độ dày dưới 0.5 mm "
               "thì không giả định tồn tại khu vực nguy hiểm, vì các lý do đã "
               "nêu ở trên."))
    b.append(p("Khi nguồn phát thải là cấp phụ thì bất kỳ đám mây nào được tạo "
               "ra cũng sẽ cho Vùng 22. Như trước đó, đối với các lớp bụi do "
               "đám mây này tạo ra thì các trường hợp sau đây áp dụng. Khi "
               "hình thành một lớp bụi không kiểm soát thì, một lần nữa, Vùng "
               "20 sẽ tồn tại trong vùng của lớp bụi. Khi lớp bụi được kiểm "
               "soát bằng dọn dẹp hoặc các biện pháp khác ở độ dày dưới 5 mm, "
               "Vùng 21 sẽ tồn tại ở nơi lớp bụi bị xáo trộn đều xuyên và Vùng "
               "22 sẽ hình thành ở nơi lớp bụi chỉ hiếm khi bị xáo trộn. Khi "
               "độ dày của mọi lớp bụi được tạo ra có thể kiểm soát dưới 0.5 mm "
               "thì không giả định tồn tại khu vực nguy hiểm."))
    b.append(p("Khi xem xét khả năng hình thành lớp bụi, phải nhận ra rằng "
               "không nhất thiết phải có một đám mây bụi có khả năng tạo thành "
               "khí quyển nổ thì mới có khả năng có một lớp bụi có thể tạo "
               "thành khí quyển như vậy hoặc bị bắt lửa. Như đã nêu ở trên, "
               "một đám mây bụi phải rất đặc mới trở thành khí quyển nổ "
               "(50-100 g bụi cho mỗi m³ không khí trung bình). Những nồng độ "
               "thấp hơn rất nhiều vẫn hoàn toàn có thể lắng đọng các lớp dày "
               "hơn 5 mm và các khu vực nguy hiểm do lớp bụi có thể tồn tại "
               "ngay cả khi không xác định được nguy cơ từ đám mây bụi. Thêm "
               "vào đó, trong mọi trường hợp sẽ cần thiết lập các hành động "
               "để bảo đảm các lớp bụi tạo ra ở bất kỳ khu vực nào không vượt "
               "quá 5 mm, vì chỉ trong những trường hợp đặc biệt mới đạt được "
               "sự hạn chế đó một cách tự nhiên. Việc hạn chế lớp bụi xuống "
               "dưới 0.5 mm thậm chí còn ít khả năng hơn và chỉ có thể mong "
               "đợi ở các khu vực ngoài trời nơi thông gió rất tốt, tạo ra "
               "sự tin cậy rằng bụi được tạo ra sẽ bị gió phân tán."))
    b.append(note("<b>Lưu ý về dấu gạch nối trong bản in.</b> Các cụm "
                  "'50-100 g of dust per m³ of air on average' và, ở đoạn sau, "
                  "'1-1.5 m' được in với dấu gạch nối; cả hai đều được giữ "
                  "nguyên ở đây thay vì được đổi sang gạch ngang dài (en dash)."))

    # --- 6.2.3 ------------------------------------------------------------
    b.append(h4("6.2.3 Phạm vi khu vực nguy hiểm",
                "6.2.3 Extents of hazardous areas"))
    b.append(p("Khi bụi được chế biến, rất có thể có một đám mây bụi bên trong "
               "thiết bị chế biến và, vì trong hầu hết các trường hợp không "
               "thể xác định được vị trí của nó, toàn bộ nội thất của thiết "
               "bị sẽ được giả định là bị nhiễm đám mây bụi. Một ngoại lệ là, "
               "ví dụ, trường hợp các hạt sản phẩm được tách khỏi bụi đi cùng "
               "chúng bằng một cyclone (xem Hình 6.1). Trong những trường hợp "
               "như vậy, dòng sản phẩm sau khi tách gần như sẽ không phải là "
               "khu vực nguy hiểm."))
    b.append(p("Khi các đám mây bụi hình thành do hỏng che chắn hoặc do các "
               "hoạt động nạp liệu và dỡ liệu, phạm vi bên ngoài bất kỳ dạng "
               "che chắn quá trình nào sẽ nhỏ, vì mật độ của đám mây khiến "
               "người ta không thể làm việc trong đó: đám mây sẽ không trong "
               "suốt và rất khó thở trong môi trường đó. Thiết bị quá trình "
               "đã được thiết kế để bảo đảm không xảy ra điều đó. Thêm vào đó, "
               "mật độ của đám mây sẽ giảm nhanh khi hỗn hợp bụi và không khí "
               "rời khỏi điểm phát thải, do không khí được bổ sung vào qua "
               "nhiễu loạn và do bụi lắng xuống — vốn nặng hơn không khí. "
               "Điều này dẫn đến kết luận rằng các đám mây bụi do phát thải từ "
               "thiết bị quá trình sẽ không lan xa quá 1-1.5 m tính từ nguồn "
               "phát thải. Một lần nữa, vì bụi nặng hơn không khí, phải giả "
               "định khu vực nguy hiểm tồn tại bên dưới nguồn phát thải cho "
               "tới mặt đất, trừ khi thiết kế quá trình ngăn điều đó (ví dụ "
               "bằng cách hút trở lại vào quá trình mọi bụi được phát thải). "
               "Phép chiếu xuống mặt đất cũng chỉ có giá trị nếu không có "
               "chuyển động không khí quá mức có thể làm méo nó, vì vậy các "
               "điểm nạp và dỡ liệu phải được che chắn khỏi chuyển động không "
               "khí quá mức như gió. Các ví dụ điển hình về cách bố trí nạp "
               "liệu và các khu vực nguy hiểm mà chúng tạo ra được cho trong "
               "Hình 6.2 và 6.3. (Xem thêm Bảng 6.3.)"))
    b.append(note("<b>Lưu ý về chữ 'once' viết thường.</b> Câu 'once again, "
                  "because the dust is heavier than air...' bắt đầu một câu "
                  "mới bằng chữ 'once' viết thường trong bản in. Cách viết "
                  "và văn phong đó được giữ nguyên trong phần văn bản tiếng "
                  "Anh ở trên và không được sửa lặng lẽ."))

    # --- Figures 6.1-6.3, in printed source order --------------------------
    b.append(fig(1, F.fig_f601()))
    b.append(fig(2, F.fig_f602()))
    b.append(note("<b>Ghi chú (3) của Hình 6.2 in 'Zone 2'.</b> Ghi chú (3) "
                  "của chú giải viết 'the Zone 2 may be limited to 2-2.5 m "
                  "around the hopper'. Cụm 'Zone 2' được giữ nguyên theo bản "
                  "in trong bản vẽ và chú giải; theo ngữ cảnh gần như chắc "
                  "chắn đây là Vùng 22 và không được sửa lặng lẽ."))
    b.append(fig(3, F.fig_f603()))

    # --- printed p.160 continuation ----------------------------------------
    b.append(p("Các lớp bụi được hình thành ở bất cứ nơi nào bụi được phát "
               "thải, ngay cả khi lần phát thải đó không đủ để tạo ra đám mây "
               "bụi có khả năng nổ. Phạm vi và độ dày của các lớp này phụ "
               "thuộc ở một mức độ nhất định vào mức độ dọn dẹp trong khu vực "
               "phát thải, đặc biệt nếu khu vực đó ở trong nhà. Mức độ dọn dẹp "
               "luôn cần đủ để bảo đảm không hình thành các lớp bụi dày và "
               "rộng lớn do các phát thải xảy ra trong vận hành bình thường "
               "(từ các nguồn phát thải cấp chính), nhưng chỉ một mức độ dọn "
               "dẹp rất cao mới có thể được giả định là có tác động hạn chế "
               "đáng kể đến phạm vi khu vực nguy hiểm do sự hình thành lớp "
               "bụi từ các nguồn phát thải cấp phụ. Những nguồn này thường do "
               "các hỏng hóc hiếm hoi của che chắn thiết bị quá trình và ít "
               "dự đoán được cũng như thường lớn hơn (ví dụ, do vỡ bao bì khi "
               "đưa đến điểm xả). Vì lý do này, không phải hiếm khi toàn bộ "
               "khu vực của một tòa nhà chứa thiết bị chế biến bụi được phân "
               "loại là Vùng 22."))
    b.append(p("Thêm vào đó, hoàn toàn bình thường khi phân loại toàn bộ chiều "
               "cao của tòa nhà như vậy là Vùng 22, dù lớp bụi chỉ nằm ở mức "
               "sàn. Các lớp bụi có thể hình thành trên dầm, cột chống và các "
               "vật tương tự tạo ra mặt bệ ở cao hơn, và những điều này phải "
               "được tính đến — đó là lý do thường không dùng giới hạn về "
               "chiều cao. Khi bụi được lưu trữ thay vì được chế biến, tình "
               "huống có thể khác đi tùy theo phương pháp che chắn. Khi dùng "
               "thùng và các container tương tự, khả năng rò rỉ là nhỏ và, "
               "kết hợp với dọn dẹp tốt, không khó bảo đảm không xuất hiện "
               "các lớp bụi nguy hiểm. Khi vật liệu được lưu trữ trong những "
               "thứ như bao giấy thì điều đó không còn đúng và rất có thể "
               "khu vực lưu trữ nên được phân loại là Vùng 22."))
    return "".join(b)


def body_en():
    b = []

    # --- 6.2.2, continued: Zone 20 completion and layer rules --------------
    b.append(p("The layers of dust formed also create the following hazardous "
               "areas. An uncontrolled dust layer (i.e., one not contained in "
               "depth by housekeeping) will produce a Zone 20. Such layers "
               "are normally limited to the inside of vessels, etc., and "
               "because they are so thick (in excess of 5 mm) may have "
               "properties which are different to those of controlled layers. "
               "Such layers would not be acceptable outside containment such "
               "as process vessels in view of Section 31 of the Factories "
               "Acts¹. A controlled dust layer (i.e., one which is contained "
               "in depth to less than 5 mm by housekeeping or other means) "
               "formed by a continuous grade source of release will only give "
               "a Zone 21 if disturbed often, and only a Zone 22 if rarely "
               "disturbed. The problems are principally the clouds produced "
               "by the layers when disturbed as the electrical equipment is "
               "designed to operate in this depth of dust layer. Where the "
               "layer of dust can be controlled to less than 0.5 mm thickness "
               "with confidence it is unlikely that there will be enough dust "
               "to create an explosive atmosphere and, therefore, no hazardous "
               "area is presumed to exist as a result of its presence, as when "
               "disturbed it is not capable of the production of an ignitable "
               "dust cloud."))
    b.append(p("A primary grade source of release will give rise to a Zone 21 "
               "if it produces a cloud. The extent of that Zone 21 will depend "
               "upon the dispersion of the dust cloud or the settling of the "
               "dust to form a layer. As before, the layer will be considered "
               "to produce the following Zones. Where an uncontrolled dust "
               "layer (one not controlled to less than 5 mm by housekeeping, "
               "etc.) is formed the result is a Zone 20 in the area covered by "
               "the layer. Where a controlled dust layer whose thickness is "
               "controlled to less than 5 mm is formed, but is regularly "
               "disturbed, then the result is a Zone 21 in the area around the "
               "layer. Where the layer is not regularly disturbed then the "
               "hazardous area reduces to Zone 22. Where a dust layer is "
               "controlled to less than 0.5 mm no hazardous area is presumed "
               "to exist for reasons already described."))
    b.append(p("Where the source of release is of secondary grade then any "
               "cloud produced will give a Zone 22. As before, in the case of "
               "layers produced by this cloud the following is the case. Where "
               "an uncontrolled dust layer is formed then, once again, a Zone "
               "20 will exist in the region of the layer. Where the dust layer "
               "is controlled by housekeeping or other means to less than 5 "
               "mm, a Zone 21 will exist where it is disturbed regularly, and "
               "a Zone 22 will be formed where it is only disturbed rarely. "
               "Where the thickness of any dust layer produced can be "
               "controlled to less than 0.5 mm, then no hazardous area is "
               "assumed to exist."))
    b.append(p("When considering the possibility of dust layer formation it "
               "has to be recognized that it is not necessary to have a dust "
               "cloud capable of forming an explosive atmosphere in order to "
               "have the possibility of a dust layer capable of forming such "
               "an atmosphere or being ignited. As already mentioned, a dust "
               "cloud has to be very dense to become an explosive atmosphere "
               "(50-100 g of dust per m³ of air on average). Very much lower "
               "concentrations are well capable of depositing layers exceeding "
               "5 mm, and hazardous areas due to dust layers may exist even "
               "when no dust cloud risk is identified. In addition, in all "
               "cases it will be necessary to institute actions to ensure that "
               "the dust layers produced in any area do not exceed 5 mm as "
               "only in exceptional circumstances will the situation be such "
               "that such limitation will be naturally achieved. The "
               "limitation of dust layers to less than 0.5 mm is even more "
               "unlikely and can only be expected to occur in outdoor areas "
               "where ventilation is very good, giving confidence of wind "
               "dispersion of any dust produced."))
    b.append(note("<b>Note on the printed hyphens.</b> The phrases "
                  "'50-100 g of dust per m³ of air on average' and, later, "
                  "'1-1.5 m' are printed with hyphens; both are retained here "
                  "with hyphens rather than being converted to en dashes."))

    # --- 6.2.3 ------------------------------------------------------------
    b.append(h4("6.2.3 Extents of hazardous areas",
                "6.2.3 Extents of hazardous areas"))
    b.append(p("Where dusts are processed it is likely that there will be a "
               "cloud within the processing equipment and, because it will "
               "not be possible to determine where in most cases, the entire "
               "interior of the equipment will be assumed to be contaminated "
               "with the dust cloud. An exception to this would be, for "
               "instance, where product particles were being separated from "
               "dust received with them by a cyclone (see Fig. 6.1). In such "
               "cases, the product stream after separation would probably "
               "not be a hazardous area."))
    b.append(p("Where dust clouds are formed due to failure of containment or "
               "loading or offloading activities, the extent will be small "
               "outside any sort of process containment as the density of the "
               "cloud would make it impossible for people to work because the "
               "cloud will be opaque and it will be difficult to breathe in "
               "such a cloud. The process equipment will have been designed "
               "to ensure this is not so. In addition, the density of the "
               "cloud will rapidly reduce as the mixture of dust and air "
               "leaves the point of release due to the addition of air by "
               "turbulence, and the settling of the dust which is, heavier "
               "than air. This leads to the conclusion that dust clouds caused "
               "by release of dusts from process equipment will extend no more "
               "than 1-1.5 m from the source of release. once again, because "
               "the dust is heavier than air, the hazardous area will have to "
               "be assumed to exist below the source of release down to the "
               "ground, unless the process design prevents this (for example "
               "by drawing into the process any dust released). The projection "
               "down to the ground will also only be valid if there is no "
               "excessive air movement which could distort it and so loading "
               "and unloading points should be protected from excessive air "
               "movement, such as wind. Typical examples of loading "
               "arrangements and the hazardous areas which they produce are "
               "given in Fig. 6.2 and 6.3. (See also Table 6.3.)"))
    b.append(note("<b>Note on the lowercase 'once'.</b> The sentence 'once "
                  "again, because the dust is heavier than air...' begins a "
                  "new sentence with a lowercase 'once' in print. That exact "
                  "wording and capitalisation are retained in the English "
                  "prose above and have not been silently corrected."))

    # --- Figures 6.1-6.3, in printed source order --------------------------
    b.append(fig(1, F.fig_f601()))
    b.append(fig(2, F.fig_f602()))
    b.append(note("<b>Figure 6.2 Note (3) prints 'Zone 2'.</b> Note (3) of the "
                  "caption reads 'the Zone 2 may be limited to 2-2.5 m around "
                  "the hopper'. The printed 'Zone 2' is retained verbatim in "
                  "the drawing and caption; in context it is almost certainly "
                  "Zone 22. It has not been silently corrected."))
    b.append(fig(3, F.fig_f603()))

    # --- printed p.160 continuation ----------------------------------------
    b.append(p("Layers of dust are formed wherever dust is released, even if "
               "that release is not sufficient to produce an explosive dust "
               "cloud. The extent and thickness of such layers is, to a "
               "degree, dependent upon the level of housekeeping in the area "
               "of release, particularly if this is indoors. While the level "
               "of housekeeping will always need to be sufficient to ensure "
               "that extensive, thick dust layers will not form from releases "
               "which occur in normal operation (from primary grade sources "
               "of release), only a very high level of such housekeeping can "
               "be assumed to have a significant limiting effect upon the "
               "extent of hazardous areas from dust-layer formation from "
               "secondary grade sources of release. These are usually from "
               "rare failures of process equipment containment and are less "
               "predictable and usually larger (for example, from the rupture "
               "of a bag being brought to the discharge point). For this "
               "reason it is not unusual to find the entire area of a building "
               "containing dust processing equipment classified as Zone 22."))
    b.append(p("In addition, it is quite normal to classify the entire height "
               "of such a building as Zone 22, even though the dust layer will "
               "only be at floor level. Dust layers can form on beams, "
               "stanchions and similar items which produce ledges at higher "
               "levels and these must be taken into account, which is why a "
               "height limit is often not used. Where dust is stored rather "
               "than processed the situation may be different depending upon "
               "the method of containment. Where drums and similar containers "
               "are used, the likelihood of leakage is small, and coupled with "
               "good housekeeping it is not difficult to ensure that dangerous "
               "layers of dust do not occur. Where the material is stored in "
               "such things as paper sacks this ceases to be true and it is "
               "likely that the storage area should be classified as Zone 22."))
    return "".join(b)
