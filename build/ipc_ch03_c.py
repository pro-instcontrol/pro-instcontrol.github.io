# -*- coding: utf-8 -*-
"""Chapter 3, "Transducers - III", section 3.1.5 and the opening of 3.2
(EN/VI bilingual).

Source: Prasad, Jayaswal & Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 149-157, printed pp. 137-145,
decoded text lines 5600-5876.  Figures 3.11-3.20 are placed at the prose
locations that refer to them; equation (3.7) is the emf relation
e = a + bt + ct².  The final sentence hands over to section 3.2.3 in the
next module, which also inserts Figure 3.21.
"""

import ipcfig3 as F
from ipc_ch03_lib import H, P, L, E, FIG, TBL, NOTE


def _ensure_figure_suppliers():
    """Stand-ins only while the parallel figure suppliers are not yet loaded.

    A registered ``F.fig_fNN`` always wins; this shim merely lets the prose
    module be imported and QA'd on its own in an incomplete workspace.
    """
    missing = [n for n in range(11, 21)
               if not hasattr(F, "fig_f%02d" % n)]
    if not missing:
        return
    from ipcfig3_common import INK, T, _ar, _b, _mk

    subjects = {
        11: ("Thermocouple element; beads; head; extension cable",
             "Phần tử cặp nhiệt điện; hạt cách điện; đầu cặp; cáp nối dài",
             ["Thermocouple element", "Beads", "Head", "Extension cable"]),
        12: ("Thermocouple head; adjustable coupling; thermowell",
             "Đầu cặp nhiệt điện; khớp nối chỉnh được; thermowell",
             ["Thermocouple head", "Adjustable coupling", "Thermowell"]),
        13: ("Taper shank threaded thermowell",
             "Thermowell ren có thân côn",
             ["Threaded shank", "Taper", "Tip"]),
        14: ("Thermonozzle construction", "Cấu tạo thermonozzle",
             ["Thermowell", "Threaded socket", "Nozzle body"]),
        15: ("Thermonozzle installation on pipeline",
             "Lắp thermonozzle trên đường ống",
             ["Thermowell", "Pipeline", "Seal weld"]),
        16: ("Thermowell and thermonozzle on main pipeline",
             "Thermowell và thermonozzle trên đường ống chính",
             ["Thermowell", "Thermonozzle", "Main pipeline", "Centreline"]),
        17: ("Angled thermowell installation", "Lắp thermowell nghiêng",
             ["Pipeline", "Angle", "Thermowell"]),
        18: ("Thermowell installed in an elbow", "Lắp thermowell ở khúc cong",
             ["Elbow", "Main pipeline", "Thermowell"]),
        19: ("Gasifier B-type thermocouple",
             "Cặp nhiệt điện loại B cho lò khí hóa",
             ["Ceramic protection tube", "High pressure seal",
              "Gasifier head"]),
        20: ("Surface (skin) temperature thermocouple",
             "Cặp nhiệt điện nhiệt độ bề mặt",
             ["Magnets", "Thermocouple tip", "Extension wire"]),
    }
    for n in missing:
        en, vi, parts = subjects[n]
        o = []
        x = 24
        width = min(150, (632 - (len(parts) - 1) * 12) // len(parts))
        for i, part in enumerate(parts):
            o.append(_b(x, 74, width, 50, part))
            if i < len(parts) - 1:
                o.append(_ar(x + width + 1, 99, x + width + 11, 99))
            x += width + 12
        o.append(T(340, 150, vi + " / " + en, 7.4, color=INK))
        _tup = _mk(n, o, en, vi, en, vi, en)
        setattr(F, "fig_f%02d" % n, (lambda _t=_tup: _t))


_ensure_figure_suppliers()


def section(lang):
    b = []

    # ----------------------------------------------------------- 3.1.5
    H(b, lang, "3.1.5 Đặc điểm cấu tạo của cặp nhiệt điện",
      "3.1.5 Constructional Features of Thermocouples", level=3)

    P(b, lang,
      "Các phần tử cặp nhiệt điện được nung chảy kết dính với nhau ở nhiệt độ "
      "cao, và từng phần tử được luồn qua hai ống cách điện nằm trong lòng ống "
      "gọi là hạt (bead), như minh họa trong Hình 3.11.",
      "Thermocouple elements are fused together at elevated temperature and "
      "the individual elements are passed through two in-bore insulators "
      "called beads as shown in Figure 3.11.")

    FIG(b, 11, F.fig_f11(), lang)

    P(b, lang,
      "Các hạt được làm bằng vật liệu chịu lửa.",
      "The beads are made of refractory material.")

    FIG(b, 12, F.fig_f12(), lang)

    P(b, lang,
      "Chiều dài thông thường của hạt chỉ từ 50 mm đến 75 mm. Trong những "
      "trường hợp đặc biệt mà nhiệt độ cần đo là cực cao, có thể cần lắp thêm "
      "một lớp phủ chịu lửa chồng lên các hạt hiện có vì lý do cơ học. Tuy "
      "nhiên, cách này có xu hướng làm chậm đáp ứng của cặp nhiệt điện. Sau "
      "khi ra khỏi ống cách điện, các phần tử cặp nhiệt điện được nối vào "
      "thanh đấu dây trên đầu cặp nhiệt điện. Sau đó, cáp nối dài/cáp bù được "
      "đấu qua thanh đấu dây và dẫn về phòng điều khiển trung tâm qua hệ "
      "thống đi dây trên máng nhôm. Thanh đấu dây được cố định bên trong đầu "
      "cặp nhiệt điện. Một cặp nhiệt điện hoàn chỉnh sẵn sàng lắp đặt được "
      "minh họa trong Hình 3.12.",
      "Normal length of the bead is from 50 mm to 75 mm only. In special "
      "cases where temperature to be measured is extremely high, an additional "
      "refractory cover may be required to be put on the existing beads for "
      "mechanical reasons. However, it tends to slow down the response of the "
      "thermocouple. The thermocouple elements after coming out of the "
      "insulator are terminated at the strip on the thermocouple head. "
      "Thereafter, the extension cable/compensating cable are connected "
      "through the terminal strip and taken to central control room through "
      "cable routing on aluminium trays. The terminal strip is fixed inside "
      "the thermocouple head. A complete thermocouple ready for installation "
      "has been shown in Figure 3.12.")

    P(b, lang,
      "Việc lựa chọn vật liệu chịu lửa để cách điện cho cặp nhiệt điện phụ "
      "thuộc vào điều kiện vận hành cụ thể. Trong môi trường oxy hóa, silica "
      "nung chảy chịu được sốc nhiệt và dùng được đến 1000 °C. Hỗn hợp "
      "alumina-silica chịu được 1700 °C và alumina tinh khiết dùng được đến "
      "1850 °C, nhưng kém chống sốc nhiệt hơn.",
      "The choice of refractory material for thermocouple insulation depend "
      "upon particular operating condition. In oxidizing atmosphere fused "
      "silica withstand thermal shock and can be used upto 1000°C. "
      "Alumina-Silica mixture can withstand 1700 °C and pure alumina upto "
      "1850 °C but are less resistant to thermal shock.")

    P(b, lang,
      "Trong môi trường khử hoặc chân không, không dùng vật liệu chịu lửa gốc "
      "silica vì chúng làm giòn phần tử cặp nhiệt điện. Trong điều kiện này "
      "dùng alumina tinh khiết.",
      "In reducing atmosphere or under vacuum, silica refractories are not "
      "used because it embrittles the thermocouple element. In this "
      "condition, pure alumina is used.")

    # ------------------------------------------------------------- 3.2
    H(b, lang, "3.2 Các vấn đề cần lưu ý khác",
      "3.2 Other Considerations")

    # ------------------------------------------- 3.2 Mathematical Expression
    H(b, lang, "Biểu thức toán học", "Mathematical Expression", level=4)

    P(b, lang,
      "Phương trình toán học chi phối sự phát sinh sức điện động của một loại "
      "cặp nhiệt điện xác định được cho như sau:",
      "The mathematical equation that governs emf generation of a particular "
      "type of thermocouple is given by:")

    E(b, lang, "e = a + bt + ct²", "e = a + bt + ct²", num="3.7")

    P(b, lang,
      "Ở đây a, b và c là các hằng số được xác định bằng cách đo sức điện động "
      "do cùng một lô cặp nhiệt điện sinh ra tại điểm đông đặc của antimon "
      "(630.5 °C), điểm sôi của bạc (960.8 °C) và điểm sôi của vàng "
      "(1064.43 °C), tương ứng.",
      "Here a, b and c are constants found by measuring the emf produced by "
      "the same lot of thermocouple at freezing point of antimony (630.5°C), "
      "boiling point of silver (960.8°C) and boiling point of gold "
      "(1064.43°C) respectively.")

    # ----------------------------------------- 3.2 Annealing of Thermocouple
    H(b, lang, "Ủ nhiệt cặp nhiệt điện", "Annealing of Thermocouple", level=4)

    P(b, lang,
      "Khi phần tử cặp nhiệt điện được đưa vào vùng quá trình nóng để đo, các "
      "đoạn của dây phần tử chịu ứng suất. Hệ quả là làm xáo trộn tính đồng "
      "nhất của cấu trúc hạt của phần tử, dẫn đến sai số đo.",
      "Thermocouple element when put in the hot process for measurement "
      "purposes, the parts of the wire element come under strain. The effect "
      "is disturbance in homogeneity of the grain structure of the element "
      "resulting in measurement error.")

    P(b, lang,
      "Để giảm thiểu ảnh hưởng này, phần tử cặp nhiệt điện được ủ nhiệt trước "
      "khi đưa vào vận hành. Quá trình ủ được thực hiện trong không khí, ở "
      "nhiệt độ tối đa mà cặp nhiệt điện sẽ dùng khi vận hành. Quá trình ủ chỉ "
      "kéo dài từ 2 đến 3 phút. Việc ủ được thực hiện bằng cách cho dòng điện "
      "chạy qua phần tử cặp nhiệt điện được treo trong không khí.",
      "To minimize this effect, the thermocouple element is annealed before "
      "put in operation. Annealing process is carried out in presence of air "
      "upto the maximum temperature to which the thermocouple shall be used "
      "while in operation. The annealing process continues for a period of "
      "2 to 3 minutes only. The annealing is done by passing electric current "
      "through the thermocouple element which is kept hanging in the air.")

    # ------------------------------------------- 3.2 Life of Thermocouple
    H(b, lang, "Tuổi thọ của cặp nhiệt điện", "Life of Thermocouple", level=4)

    P(b, lang,
      "Không thể dự đoán chắc chắn tuổi thọ của cặp nhiệt điện, vì trong một "
      "số trường hợp người ta thấy cặp nhiệt điện hỏng ngay trong giai đoạn "
      "chạy thử. Vì vậy, mỗi cặp nhiệt điện cần có lịch kiểm tra định kỳ so "
      "với một cặp nhiệt điện chuẩn được giữ riêng cho mục đích này. Bất kỳ "
      "sự suy giảm nào của phần tử cặp nhiệt điện sẽ được phát hiện ngay qua "
      "các bất thường trong kết quả đọc trong lúc kiểm tra. Sự suy giảm của "
      "cặp nhiệt điện là mất tính đồng nhất do ứng suất hoặc nhiễm bẩn.",
      "The life of thermocouple cannot be predicted with full confidence "
      "because in some cases it has been seen that it failed during "
      "commissioning period itself. Therefore, every thermocouple should have "
      "checking schedule for checking the same on regular interval against a "
      "standard thermocouple kept for this purpose only. Any degradation in "
      "thermocouple element shall be immediately known by irregularities in "
      "measurement reading during checking. Degradation in thermocouple is "
      "loss of homogeneity caused by strain or contamination.")

    P(b, lang,
      "Nhìn chung, cách khắc phục là thay thế chính cặp nhiệt điện. Tuy nhiên, "
      "đôi khi có thể loại bỏ ứng suất bằng cách ủ lại toàn bộ cặp nhiệt điện "
      "và đôi khi bằng cách thay đổi cả phương pháp lắp đặt. Mặt khác, nhiễm "
      "bẩn có thể tránh được bằng cách thao tác cẩn thận với phần tử cặp nhiệt "
      "điện và dùng đúng vật liệu chịu lửa. Hỏng hóc cặp nhiệt điện là chủ đề "
      "được thảo luận và nghiên cứu trong hầu hết mọi loại ngành công nghiệp "
      "quá trình sử dụng cặp nhiệt điện.",
      "Generally, the solution to this problem is replacement of the "
      "thermocouple itself. However, sometimes strain can be removed by "
      "reannealing of the entire thermocouple and sometimes changing the "
      "method of installation as well. Contamination, on the other hand, can "
      "be avoided by careful handling of thermocouple element and by use of "
      "proper refractory. Failure of thermocouples have been subject of "
      "discussion and also research in almost all type of process industries "
      "using thermocouples.")

    # ------------------------------------------ 3.2 Installation Practice
    H(b, lang, "Thực hành lắp đặt", "Installation Practice", level=4)

    P(b, lang,
      "Lắp đặt đúng cách vừa bảo vệ cặp nhiệt điện vừa đảm bảo độ chính xác "
      "của phép đo nhiệt độ. Lựa chọn phụ kiện cặp nhiệt điện và dây nối dài, "
      "lựa chọn thermonozzle và thermowell, và lựa chọn đúng điểm đo đại "
      "diện, tức là vị trí lắp cặp nhiệt điện, là những xem xét thông thường "
      "thuộc về thực hành lắp đặt. Chúng ta đã thảo luận dài về cặp nhiệt "
      "điện và dây nối dài của nó. Ở đây chúng ta bắt đầu từ thermonozzle và "
      "thermowell.",
      "Proper installation of thermocouple provides protection of "
      "thermocouple as well as accuracy of temperature measurement. Selection "
      "of thermocouple accessories and extension wire, selection of "
      "thermonozzle and thermowell and selection of installation – "
      "representative point of measurement, i.e. location of thermocouple are "
      "the normal considerations that come under installation practice. We "
      "have already discussed at length regarding thermocouple and its "
      "extension wire. Here we shall start our discussion with thermonozzle "
      "and thermowell.")

    P(b, lang,
      "Để bảo vệ cặp nhiệt điện khỏi tác động của quá trình oxy hóa nhanh "
      "hoặc các dạng hư hỏng khác do chất lưu khó xử lý mà cặp nhiệt điện "
      "được nhúng vào, người ta dùng vỏ bọc/ống bảo vệ cặp nhiệt điện. Đối "
      "với sơ đồ đo nhiệt độ dưới 500 °C mà phản ứng nhanh có thể là yếu tố "
      "quan trọng, tránh dùng thermowell. Đến nhiệt độ 1000 °C dùng vỏ bọc "
      "bằng thép không gỉ 316. Trên 1000 °C nên dùng vỏ bọc chịu lửa. Cần "
      "thận trọng khi chọn hình dạng của cặp nhiệt điện để giữ thời gian "
      "đáp ứng nhỏ nhất, đồng thời vẫn đủ bền để kéo dài tuổi thọ của cả "
      "thermowell và phần tử cặp nhiệt điện. Cấu tạo thân côn (taper shank) "
      "của thermowell là cần thiết để tạo độ bền cơ học ngăn rung do vận tốc "
      "dòng chảy của chất lưu. Một thermowell được minh họa trong Hình 3.13.",
      "To protect the thermocouple from the effects of rapid oxidation or "
      "other forms of deterioration due to action of difficult fluids in "
      "which these thermocouples are immersed, thermocouple sheaths/"
      "thermowells are used. For temperature measurement scheme of below "
      "500°C where fast response can be an important consideration, the use "
      "of thermowell is avoided. Upto a temperature of 1000°C sheath of 316 "
      "stainless steel is used. Above 1000C refractory sheathing is "
      "recommended. Care must be exercised in selecting the shape of the "
      "thermocouple to keep the response time minimum, yet provide adequate "
      "strength to prolong the life of thermowell as well as thermocouple "
      "element. A taper shank construction of thermowell is necessary to "
      "provide mechanical strength needed to prevent vibration caused by the "
      "velocity of the fluid flow. A thermowell has been shown in "
      "Figure 3.13.")

    FIG(b, 13, F.fig_f13(), lang)

    P(b, lang,
      "Trong trường hợp bình thường, khi đường kính của đường ống chính lớn "
      "và cho phép chiều dài ngâm đủ, thermowell được hàn trực tiếp vào đường "
      "ống (kiểu hàn ổ cắm, socket-weld). Một phương án khác là hàn một ống "
      "ren có kích thước phù hợp vào đường ống chính rồi vặn thermowell vào "
      "chặt chẽ. Đối với đường ống không có đủ chiều sâu hoặc chiều dài ngâm, "
      "trước hết phải hàn một thermonozzle vào đường ống.",
      "In normal cases, where diameter of the main pipeline is larger and "
      "allows sufficient immersion length, this thermowell is directly welded "
      "to the pipeline (socket-weld type). Another alternative is to weld a "
      "threaded socket of approximate size to the main pipeline and then the "
      "thermowell is screwed properly. For the pipeline where such allowance "
      "for sufficient immersion length or depth is not available, a "
      "thermonozzle is first welded onto the pipeline.")

    P(b, lang,
      "Thermonozzle thường được chế tạo bằng thép không gỉ 316 cho dịch vụ "
      "oxy và bằng thép carbon cho các dịch vụ khác. Lắp đặt điển hình được "
      "minh họa trong Hình 3.15, trong khi Hình 3.14 cho thấy cấu tạo thực tế "
      "của thermonozzle.",
      "Thermonozzle is usually made of 316 stainless steel for oxygen service "
      "and of carbon steel for other services. Typical installation have been "
      "shown in Figure 3.15 whereas Figure 3.14 shows actual construction of "
      "thermonozzle.")

    FIG(b, 14, F.fig_f14(), lang)
    FIG(b, 15, F.fig_f15(), lang)

    P(b, lang,
      "Thermowell như đã trình bày trong Hình 3.13 được vặn chặt vào "
      "thermonozzle này sao cho đáy của thermowell hơi thấp hơn đường tâm của "
      "đường ống chính. Toàn bộ cụm lắp đặt (cả ba bộ phận) được minh họa "
      "trong Hình 3.16.",
      "Thermowell which has been shown in Figure 3.13 is tightened properly "
      "onto this thermonozzle so that the bottom of the thermowell reaches "
      "slightly below the centreline of the main pipeline. The entire "
      "installation (all three components) has been shown in Figure 3.16.")

    FIG(b, 16, F.fig_f16(), lang)

    P(b, lang,
      "Cách lắp đặt này cho nhiệt độ hiệu dụng ở giữa vùng dòng chảy của chất "
      "lưu, vì vận tốc khối lớn nhất tại điểm này. Điều này đảm bảo truyền "
      "nhiệt tốt hơn bằng đối lưu. Tuy nhiên, khi vận tốc dòng chảy cực cao "
      "(ví dụ hơi quá nhiệt có áp suất rất cao), có thể hoàn toàn không cần "
      "ngâm sâu cặp nhiệt điện.",
      "Installation of this type gives the effective temperature in the "
      "middle of the fluid flow pattern. This is because the mass velocity is "
      "highest at this point. This ensures better heat transfer by "
      "convection. However, when the velocity of the fluid flow is extremely "
      "high (for instance, superheated steam of very high pressure), deep "
      "immersion of thermocouple may not be required at all.")

    P(b, lang,
      "Cần chọn đúng điểm lắp đặt trên đường ống để có được kết quả đọc nhiệt "
      "độ đại diện. Một phương pháp tìm điểm lắp đặt tốt nhất là dùng cặp "
      "nhiệt điện di động để đo nhiệt độ tại nhiều vị trí.",
      "Proper point of installation should be selected on the pipeline so "
      "that a representative reading of temperature can be obtained. One "
      "method for finding best installation point is to use a portable "
      "thermocouple for taking measurement of temperature at several places.")

    P(b, lang,
      "Vị trí lắp cặp nhiệt điện cũng là một xem xét quan trọng. Thermowell "
      "phải được lắp vuông góc với đường ống hoặc bình chứa, dù là thiết bị "
      "gì. Nếu không thể lắp vuông góc, có thể cân nhắc lắp nghiêng một góc "
      "hoặc lắp ở khúc cong (elbow) như minh họa trong Hình 3.17 và "
      "Hình 3.18.",
      "Positioning of thermocouple is also an important consideration. "
      "Thermowells should be installed perpendicular to the pipeline or the "
      "vessel whatever it may be. If perpendicular installation is not at all "
      "possible, installation at an angle or in an elbow may be considered as "
      "shown in Figures 3.17 and 3.18.")

    FIG(b, 17, F.fig_f17(), lang)
    FIG(b, 18, F.fig_f18(), lang)

    P(b, lang,
      "Trong sơ đồ đo nhiệt độ của lò nhiệt độ cao, nên lắp đặt thẳng đứng từ "
      "đỉnh lò. Cách này sẽ ngăn không cho phần tử bị cong.",
      "In temperature measurement scheme of high temperature furnace, "
      "vertical installation from top of the furnace is recommended. This "
      "will prevent bending of the element.")

    NOTE(b, lang,
      "Trong tất cả các cách lắp đặt nêu trên, không cần nối đất dây dẫn cặp "
      "nhiệt điện ở đầu thiết bị, vì thân cặp nhiệt điện đã được nối đất qua "
      "ống kim loại nơi nó được lắp đặt.",
      "In all the installation mentioned above, grounding of thermocouple "
      "leads at the instrument end is not required, because the thermocouple "
      "body is already grounded through the metallic pipe where it is "
      "installed.")

    # -------------------------------------- 3.2 Special Class Thermocouple
    H(b, lang, "Cặp nhiệt điện loại đặc biệt",
      "Special Class Thermocouple", level=4)

    P(b, lang,
      "Trong đa số trường hợp, phân tích hỏng hóc của các cặp nhiệt điện lắp "
      "trong điều kiện vận hành khắc nghiệt đã thúc đẩy việc cải tiến thiết "
      "kế hiện có. Các cặp nhiệt điện loại đặc biệt là kết quả của những đổi "
      "mới thiết kế này. Chúng được chế tạo để đo nhiệt độ cho các quá trình "
      "khó khăn cũng như cho một số môi trường vận hành điển hình. Đôi khi "
      "các dịch vụ này còn đòi hỏi tinh chỉnh và thay đổi cả hình dạng ban "
      "đầu của cặp nhiệt điện. Chúng ta sẽ mô tả bốn loại cặp nhiệt điện đặc "
      "biệt đang được sử dụng trong ngành công nghiệp quá trình:",
      "In majority of the cases, the failure analysis of thermocouples "
      "installed in severe operating conditions has prompted to enhance the "
      "existing design consideration. Special class thermocouples are result "
      "of such design innovations. These are constructed for the measurement "
      "of temperature for difficult processes as well as for some typical "
      "operating environments. These services sometimes call for refinement "
      "and changes in the original shape of the thermocouple as well. We "
      "shall describe following four types of special thermocouples which "
      "are in use in process industries:")

    L(b, lang,
      ["Cặp nhiệt điện lò khí hóa (gasifier thermocouple).",
       "Cặp nhiệt điện nhiệt độ bề mặt.",
       "Cặp nhiệt điện kim loại bộ quá nhiệt.",
       "Cặp nhiệt điện nhúng nhanh."],
      ["Gasifier thermocouple.",
       "Surface temperature thermocouple.",
       "Superheater metal thermocouple.",
       "Quick immersion thermocouple."],
      ordered=True)

    # ---------------------------------------- 1. Gasifier thermocouple
    H(b, lang, "1. Cặp nhiệt điện lò khí hóa",
      "1. Gasifier thermocouple", level=4)

    P(b, lang,
      "Lò khí hóa là bình phản ứng đơn vị, nơi xảy ra quá trình oxy hóa một "
      "phần các hydrocarbon (naphtha, dầu nhiên liệu hoặc LSHS) hoặc than thô "
      "nghiền nát, cùng với hỗn hợp oxy tinh khiết và hơi nước quá nhiệt "
      "(64 kg/cm²), tạo thành khí thô. Khí thô chứa chủ yếu hydro và carbon "
      "monoxide, là đầu vào chính để sản xuất amonia khan và phân bón urê.",
      "Gasifier is a unit operation reactor vessel where partial oxidation "
      "of hydrocarbons (naphtha or fuel oil or LSHS) or of raw crushed coal "
      "takes place along with mixture of pure oxygen and superheated steam "
      "(of 64 kg/cm2), resulting in formation of raw gas. Raw gas contains "
      "mainly hydrogen and carbon monoxide and constitutes the main inputs "
      "for the production of anhydrous ammonia as well as urea fertilizer.")

    P(b, lang,
      "Ba thành phần nêu trên được phun vào lò khí hóa qua một súng đặc biệt "
      "gọi là súng lò khí hóa (gasifier-gun). Phản ứng bên trong lò là tỏa "
      "nhiệt, nên nhiệt độ tăng trong khoảng 1250 °C đến 1350 °C. Xét đến "
      "môi trường và nhiệt độ cao bên trong lò, phép đo nhiệt độ được thực "
      "hiện bằng cặp nhiệt điện loại B được chế tạo đặc biệt. Dây cặp nhiệt "
      "điện gần đầu được làm kín bằng các gioăng chịu áp lực cao có thể chịu "
      "áp suất tối đa 150 kg/cm². Chi tiết cấu tạo của cặp nhiệt điện được "
      "minh họa trong Hình 3.19.",
      "The three ingredients described above are injected into the gasifier "
      "through special gun called gasifier-gun. The reaction inside the "
      "gasifier being exothermic, the temperature rises between 1250 °C and "
      "1350 °C. Considering the environment of the gasifier and the high "
      "temperature inside, the measurement of temperature is carried out by "
      "means of especially constructed B-type thermocouple. The thermocouple "
      "wires near the head are sealed with high pressure seals which can "
      "withstand a maximum pressure of 150 kg/cm2. The constructional details "
      "of the thermocouple has been shown in Figure 3.19.")

    FIG(b, 19, F.fig_f19(), lang)

    P(b, lang,
      "Các phần tử cặp nhiệt điện bị nhiễm silica vì silica bắt đầu tấn công "
      "các phần tử ở nhiệt độ từ 1160 °C trở lên. Sự có mặt của silica trong "
      "vỏ bảo vệ gốm và trong vật liệu chịu lửa của bình phản ứng là nguyên "
      "nhân làm đứt dây cặp nhiệt điện. Trong cặp nhiệt điện lò khí hóa, "
      "alumina được dùng làm vỏ bảo vệ gốm thay cho silica. Phân tích hóa "
      "học của alumina như sau:",
      "thermocouple elements get contaminated with silica because silica "
      "starts attacking the elements at or above 1160°C temperature. The "
      "presence of silica in the ceramic protection sheath and the refractory "
      "materials of the reactor vessel have been responsible for the breaking "
      "of thermocouple wires. In gasifier thermocouple, alumina has been used "
      "as ceramic protection sheath in place of silica. The chemical analysis "
      "of alumina is:")

    TBL(b, lang,
        ["Thành phần", "Hàm lượng"], ["Constituent", "Percentage"],
        [["Al₂O₃", "99.0%"],
         ["SiO₂", "0.7%"],
         ["MgO", "0.07%"],
         ["Na₂O", "0.05%"],
         ["CaO", "0.03%"],
         ["Fe₂O₃", "0.07%"]],
        caption_vi="Thành phần hóa học của alumina (theo bản gốc)",
        caption_en="Chemical analysis of alumina (as printed)")

    P(b, lang,
      "Tuy nhiên, các biện pháp bảo vệ này chỉ an toàn cho cặp nhiệt điện khi "
      "lò khí hóa vận hành bình thường. Chúng không chịu được cú sốc nhiệt "
      "khổng lồ xảy ra khi lò bị dừng đột ngột hoặc ngay cả khi khởi động lò. "
      "Thêm vào đó, trong lúc dừng đột ngột, nguồn cung cấp dầu hydrocarbon và "
      "oxy bị cắt cùng lúc bởi các van đóng nhanh, nhưng vẫn còn một lượng "
      "dầu dư có tính nhớt. Trong điều kiện thiếu oxy, dầu này tạo cặn carbon "
      "trên vật liệu chịu lửa cũng như trên đầu cặp nhiệt điện. Các cặn carbon "
      "này bắt đầu cháy khi tháo súng (một thao tác bảo trì thường làm trong "
      "điều kiện dừng đột ngột của lò) và khi bắt đầu cấp nhiệt bằng LPG có "
      "mặt không khí (lại là thao tác thường làm sau khi dừng đột ngột hoặc "
      "khởi động lại). Việc carbon cháy trên đầu cặp nhiệt điện làm hỏng cả "
      "vỏ bọc và dây cặp nhiệt điện, và tuyệt đối không có giải pháp nào "
      "khác ngoài việc thay thế cặp nhiệt điện bằng cặp mới. Tuổi thọ của các "
      "cặp nhiệt điện loại B làm việc trong điều kiện khắc nghiệt như vậy "
      "thường tối đa từ 2500 đến 3000 giờ.",
      "However, these protective arrangements can safeguard the thermocouple "
      "only while the gasifier is under normal operation. These arrangements "
      "cannot withstand the tremendous thermal shock which occur during "
      "sudden trip conditions of the gasifier or even during start-up of the "
      "gasifier. In addition to this, during sudden trip, supply of hydrocarbon "
      "oil and oxygen are cut-off simultaneously, by the quick closing "
      "valves, but some residual oil being viscous in nature is left. This "
      "oil, in absence of oxygen forms carbon deposits on the refractory as "
      "well as on the thermocouple tips. These carbon deposits start burning "
      "when gun removal (an usual maintenance practice performed on trip "
      "condition of the gasifier) takes place and LPG heating is started in "
      "the presence of air (again a normal practice after sudden-trip or "
      "restart-up). Such burning of carbon on thermocouple tip damages the "
      "sheathing as well as thermocouple wires and there is absolutely no "
      "solution to this problem except replacement of thermocouple with a new "
      "one. Life of these B-type thermocouples working under such severe "
      "conditions is usually between 2500 to 3000 hrs maximum.")

    # ------------------------------ 2. Surface (Skin) temperature thermocouple
    H(b, lang, "2. Cặp nhiệt điện nhiệt độ bề mặt (da)",
      "2. Surface (Skin) temperature thermocouple", level=4)

    P(b, lang,
      "Các bình phản ứng quá trình được thiết kế kiểu không cách nhiệt thường "
      "vận hành ở áp suất và nhiệt độ cao. Ở nhiệt độ và áp suất cao, hư hỏng "
      "hoặc nứt lớp lót của thành trong bình phản ứng có thể tạo ra các điểm "
      "nóng trên bề mặt ngoài. Điều này làm giảm độ bền của bình, đôi khi "
      "phá hủy hoàn toàn, gây nguy hiểm cho nhân viên vận hành cũng như cho "
      "nhà máy. Việc đo và theo dõi liên tục nhiệt độ bề mặt có thể chỉ ra "
      "ngay khu vực có khả năng xuất hiện điểm nóng.",
      "The process reactor vessels which are designed non-insulating type "
      "are normally operated at higher pressure and temperature. At elevated "
      "temperature and pressure, damage or crack in the lining of the internal "
      "wall of the process reactor vessels may lead to creation of hot spots "
      "on the outer surface. This results in reduction of strength of the "
      "vessel and sometimes complete destruction creating safety hazard for "
      "the operating personnel in addition to the plant. Measurement of skin "
      "temperature and continuous monitoring thereof can immediately point "
      "out the area in which there is possibility of creation of hot spot.")

    P(b, lang,
      "Cặp nhiệt điện dùng cho mục đích này chỉ là loại K thông thường, nhưng "
      "cấu tạo khác đôi chút so với cặp nhiệt điện thường. Đầu của cụm cặp "
      "nhiệt điện được gắn vào bề mặt bình phản ứng quá trình bằng các nam "
      "châm rỗng hình trụ. Hai nam châm được bắt đối xứng vào một bản lắp "
      "cứng chung và được treo ở vị trí thẳng đứng qua bề mặt ngoài của bình "
      "phản ứng quá trình. Các nam châm có",
      "Thermocouple used for this purpose is of ordinary K-type only but the "
      "construction is somewhat different from the usual one. The tip of the "
      "thermocouple assembly is attached to the surface of the process "
      "reactor vessel by means of cylindrical shaped hollow magnets. The two "
      "magnets are bolted symmetrically to a common rigid fixing plate and is "
      "hanged in vertical position through the outer surface of the process "
      "reactor vessel. The magnets have")

    FIG(b, 20, F.fig_f20(), lang)

    P(b, lang,
      "một đầu của thanh thép dẹt kích thước 3/8 inch được hàn hoặc vặn vào "
      "bản chính và đầu kia của thanh được nối vào một vỏ cặp nhiệt điện "
      "nhỏ. Đầu cặp nhiệt điện được cố định chắc vào phần dưới của vỏ, phần "
      "này tựa trên bề mặt ngoài của bình phản ứng quá trình. Dây dẫn đi ra "
      "từ vỏ và được nối vào máy ghi nhiệt độ hoặc hệ thống giám sát. Loại "
      "cặp nhiệt điện này có thể di chuyển trên bề mặt ngoài của bình phản "
      "ứng qua các nam châm để biết nhiệt độ bề mặt tại các điểm khác nhau "
      "bằng cách di chuyển toàn bộ cụm. Nam châm giữ chặt bề mặt ở bất kỳ vị "
      "trí nào cụm được di chuyển tới. Cách bố trí này cũng được dùng trên "
      "bình phản ứng lò khí hóa.",
      "one end of a 3/8 inch size flat of steel is welded or screwed onto the "
      "main plate and the other end of the flat is attached to a small "
      "thermocouple housing. The tip of the thermocouple is securely fixed to "
      "the lower portion of the housing which rests on the outer surface of "
      "the process reactor vessel. The lead wires come out of the housing and "
      "are connected to the temperature recorder or monitoring system. This "
      "type of thermocouple can be moved on the outer surface of the process "
      "reactor vessel here and there through the magnet to know the skin "
      "temperature at different points by moving the complete assembly. The "
      "magnets hold the surface wherever the assembly is moved. This "
      "arrangement is used on the gasifier reactor vessel as well.")

    # --------------------------------- 3. Superheater metal thermocouple
    H(b, lang, "3. Cặp nhiệt điện kim loại bộ quá nhiệt",
      "3. Superheater metal thermocouple", level=4)

    P(b, lang,
      "Trong các nồi hơi sinh hơi có áp suất và nhiệt độ cao, bộ quá nhiệt "
      "được bố trí trong vùng khói nóng có nhiệt độ cao của lò nồi hơi để hấp "
      "thụ mức bức xạ cao từ lò. Trong tình huống này, phải đảm bảo cung cấp "
      "hơi nước liên tục và không bị gián đoạn cho các ống quá nhiệt. Ngay cả "
      "khi tổng tải của nồi hơi đã giảm, bộ quá nhiệt vẫn phải được cấp một "
      "lượng hơi tối thiểu để giữ nhiệt độ kim loại bộ quá nhiệt trong giới "
      "hạn hợp lý. Điều này có lợi cho việc lựa chọn vật liệu bộ quá nhiệt "
      "một cách kinh tế. Vì vậy, nhiệt độ kim loại bộ quá nhiệt phải được "
      "giám sát bằng phương pháp đo phù hợp cho nhiệt độ kim loại.",
      "In high pressure and high temperature steam producing boilers, "
      "superheaters are located in high flue gas temperature zone of the "
      "boiler furnace to absorb high rate of furnace radiation. In such "
      "situation the superheater tubes must be ensured of continuous and "
      "uninterrupted supply of feed steam. Even if the total load on the "
      "boiler have been reduced, the superheater must be fed with certain "
      "minimum amount of steam to keep the superheather metal temperature "
      "within reasonable limit. This is advantageous for economic selection "
      "of superheater material. Therefore, the temperature of superheater "
      "metal has to be monitored by applying suitable method of measurement "
      "for metal temperature.")

    P(b, lang,
      "Với mục đích này, người ta dùng các cặp nhiệt điện loại K được chế tạo "
      "đặc biệt. Đầu của cặp nhiệt điện được chế tạo thành dạng vòng cung "
      "chữ nhật như minh họa trong Hình 3.21.",
      "For this purpose, especially constructed K-type thermocouples are "
      "used. The tip of the thermocouples is constructed in rectangular arc "
      "shape as shown in Figure 3.21.")

    return b
