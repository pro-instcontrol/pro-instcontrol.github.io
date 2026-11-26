# -*- coding: utf-8 -*-
"""Reader unit 3 of R. STAHL, *Basics of Explosion Protection* --
"Protection Methods and Enclosure Types" / "Phương pháp bảo vệ và loại vỏ bọc".

Printed A5-A6 (PDF pp. 6-7): the seven explosion-protection methods, the
Class II discussion, and the NEMA/CSA enclosure-type descriptions.
"""
from expb_common import p, lead, h2, h3, h4, ul, ol, note, table, fig

PAGES_SRC = 2
BYLINE = "R. STAHL · Basics of Explosion Protection (Innovative Explosion Protection)"
TITLE_EN = "Protection Methods and Enclosure Types"
TITLE_VI = "Phương pháp bảo vệ và loại vỏ bọc"

_PURGE_ROWS_VI = [
    ["X", "Chuyển khu vực bên trong thiết bị từ Class I, Division 1 sang không nguy hiểm"],
    ["Y", "Chuyển khu vực bên trong thiết bị từ Class I, Division 1 sang Class I, Division 2"],
    ["Z", "Chuyển khu vực bên trong thiết bị từ Class I, Division 2 sang không nguy hiểm"],
    "*Các phương pháp thổi tương tự được tìm thấy trong IEC, CENELEC và NEC 505.",
]
_PURGE_ROWS_EN = [
    ["X", "Changes the area within the unit from Class I, Division 1 to non-hazardous"],
    ["Y", "Changes the area within the unit from Class I, Division 1 to Class I, Division 2"],
    ["Z", "Changes the area within the unit from Class I, Division 2 to non-hazardous"],
    "*Similar purging methods are found in the IEC, CENELEC and NEC 505.",
]

_NEMA_TYPES_VI = [
    "<b>NEMA/CSA Type 1.</b> Dùng trong nhà, chủ yếu để bảo vệ ở mức độ nhất định "
    "khỏi một lượng nhỏ bụi bẩn rơi xuống. Loại này không được xác định cụ thể "
    "trong Tiêu chuẩn CSA.",
    "<b>NEMA/CSA Type 2.</b> Dùng trong nhà, chủ yếu để bảo vệ ở mức độ nhất định "
    "khỏi một lượng nhỏ nước và bụi bẩn rơi xuống.",
    "<b>NEMA/CSA Type 3.</b> Dùng ngoài trời, chủ yếu để bảo vệ ở mức độ nhất định "
    "khỏi mưa, mưa tuyết, bụi bay theo gió và hư hỏng do đóng băng từ bên ngoài.",
    "<b>NEMA/CSA Type 3R.</b> Dùng ngoài trời, chủ yếu để bảo vệ ở mức độ nhất định "
    "khỏi mưa, mưa tuyết và hư hỏng do đóng băng từ bên ngoài; phải có lỗ thoát nước.",
    "<b>NEMA/CSA Type 3S.</b> Dùng ngoài trời, chủ yếu để bảo vệ ở mức độ nhất định "
    "khỏi mưa, mưa tuyết, bụi bay theo gió và cho phép cơ cấu bên ngoài hoạt động "
    "khi bị đóng băng.",
    "<b>NEMA/CSA Type 4.</b> Dùng trong nhà hoặc ngoài trời, chủ yếu để bảo vệ ở mức "
    "độ nhất định khỏi bụi bay theo gió, mưa, nước văng, nước phun từ vòi và hư hỏng "
    "do đóng băng từ bên ngoài.",
    "<b>NEMA/CSA Type 4X.</b> Dùng trong nhà hoặc ngoài trời, chủ yếu để bảo vệ ở mức "
    "độ nhất định khỏi ăn mòn, bụi bay theo gió, mưa, nước văng, nước phun từ vòi và "
    "hư hỏng do đóng băng từ bên ngoài.",
    "<b>NEMA/CSA Type 5.</b> Dùng trong nhà, chủ yếu để bảo vệ khỏi bụi trong không "
    "khí lắng đọng, bụi bẩn rơi xuống và chất lỏng không ăn mòn nhỏ giọt.",
    "<b>NEMA/CSA Type 6.</b> Dùng trong nhà hoặc ngoài trời, chủ yếu để bảo vệ khỏi "
    "nước phun từ vòi, nước xâm nhập khi ngâm ngập tạm thời ở độ sâu hạn chế và hư "
    "hỏng do đóng băng từ bên ngoài.",
    "<b>NEMA/CSA Type 6P.</b> Dùng trong nhà hoặc ngoài trời, chủ yếu để bảo vệ khỏi "
    "nước phun từ vòi, nước xâm nhập khi ngâm ngập kéo dài ở độ sâu hạn chế và hư "
    "hỏng do đóng băng từ bên ngoài.",
    "<b>NEMA/CSA Type 12.</b> Dùng trong nhà, chủ yếu để bảo vệ khỏi bụi lưu thông, "
    "bụi bẩn rơi xuống và chất lỏng không ăn mòn nhỏ giọt.",
    "<b>NEMA/CSA Type 12K.</b> Loại có lỗ đục sẵn (knockouts), dùng trong nhà, chủ "
    "yếu để bảo vệ khỏi bụi lưu thông, bụi bẩn rơi xuống và chất lỏng không ăn mòn "
    "nhỏ giọt.",
    "<b>NEMA/CSA Type 13.</b> Dùng trong nhà, chủ yếu để bảo vệ khỏi bụi, nước phun, "
    "dầu và chất làm mát không ăn mòn.",
]
_NEMA_TYPES_EN = [
    "<b>NEMA/CSA Type 1.</b> Intended for indoor use primarily to provide a degree "
    "of protection against limited amounts of falling dirt. This type is not "
    "specifically identified in the CSA Standard.",
    "<b>NEMA/CSA Type 2.</b> Intended for indoor use primarily to provide a degree "
    "of protection against limited amounts of falling water and dirt.",
    "<b>NEMA/CSA Type 3.</b> Intended for outdoor use primarily to provide a degree "
    "of protection against rain, sleet, windblown dust; and damage from external "
    "ice formation.",
    "<b>NEMA/CSA Type 3R.</b> Intended for outdoor use primarily to provide a degree "
    "of protection against rain, sleet; and damage from external ice formation, and "
    "must have a drain hole.",
    "<b>NEMA/CSA Type 3S.</b> Intended for outdoor use primarily to provide a degree "
    "of protection against rain, sleet, windblown dust; and to provide for operation "
    "of external mechanisms when ice laden.",
    "<b>NEMA/CSA Type 4.</b> Intended for indoor or outdoor use primarily to provide "
    "a degree of protection against windblown dust and rain, splashing water, hose "
    "directed water; and damage from external ice formation.",
    "<b>NEMA/CSA Type 4X.</b> Intended for indoor or outdoor use primarily to provide "
    "a degree of protection against corrosion, windblown dust and rain, splashing "
    "water, hose directed water; and damage from external ice formation.",
    "<b>NEMA/CSA Type 5.</b> Intended for indoor use primary to provide a degree of "
    "protection against settling airborne dust, falling dirt, and dripping "
    "non-corrosive liquids.",
    "<b>NEMA/CSA Type 6.</b> Intended for indoor or outdoor use primarily to provide "
    "a degree of protection against hose-directed water, the entry of water during "
    "occasional temporary submersion at a limited depth; and damage from external "
    "ice formation.",
    "<b>NEMA/CSA Type 6P.</b> Intended for indoor or outdoor use primarily to provide "
    "a degree of protection against hose-directed water, the entry of water during "
    "prolonged submersion at a limited depth; and damage from external ice formation.",
    "<b>NEMA/CSA Type 12.</b> Intended for indoor use primarily to provide a degree "
    "of protection against circulating dust, falling dirt, and dripping "
    "non-corrosive liquids.",
    "<b>NEMA/CSA Type 12K.</b> Enclosures with knockouts are intended for indoor use "
    "primarily to provide a degree of protection against circulating dust, falling "
    "dirt, and dripping non-corrosive liquids.",
    "<b>NEMA/CSA Type 13.</b> Intended for indoor use primarily to provide a degree "
    "of protection against dust, spraying of water, oil, and non-corrosive coolant.",
]
_NEMA_HAZ_VI = [
    "<b>NEMA 7.</b> Dùng trong nhà tại các vị trí được phân loại là Class I, Groups "
    "A, B, C hoặc D theo NEC.",
    "<b>NEMA 8.</b> Dùng trong nhà hoặc ngoài trời tại các vị trí được phân loại là "
    "Class I, Groups A, B, C hoặc D theo NEC.",
    "<b>NEMA 9.</b> Dùng trong nhà tại các vị trí được phân loại là Class II, Groups "
    "E, F và G theo NEC.",
    "<b>NEMA 10.</b> Được chế tạo để đáp ứng các yêu cầu áp dụng của Mine Safety and "
    "Health Administration (MSHA).",
]
_NEMA_HAZ_EN = [
    "<b>NEMA 7.</b> Enclosures are intended for indoor use in locations classified "
    "as Class I, Groups A, B, C, or D, as defined in the NEC.",
    "<b>NEMA 8.</b> Enclosures are for indoor or outdoor use in locations classified "
    "as Class I, Groups A, B, C, or D, as defined in the NEC.",
    "<b>NEMA 9.</b> Enclosures are intended for indoor use in locations classified "
    "as Class II, Groups E, F, and G, as defined in the NEC.",
    "<b>NEMA 10.</b> Enclosures are constructed to meet the applicable requirements "
    "of the Mine Safety and Health Administration (MSHA).",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 3.</b> đóng gói / encapsulation · loại bảo vệ "
                "\"m\" · an toàn tăng cường / increased safety \"e\" · kín khít "
                "(hermetically sealed) · công tắc reed · an toàn nội tại / "
                "intrinsically safe \"i\", \"ia\", \"ib\" · NEC 504 · NEC 505 · "
                "IEC 60 079-11 · RST-49 · ngâm dầu / oil immersion \"o\" · thổi và "
                "tăng áp / purged and pressurized \"p\" · áp suất dương · khí trơ · "
                "liên khóa · X / Y / Z · CENELEC · nhồi bột / powder filling \"q\" · "
                "bột thủy tinh hoặc thạch anh · thiết bị Class II · kín bụi "
                "(dusttight) · Dust-ignition proof · nhiệt độ đánh lửa · nhiệt độ bề "
                "mặt · vỏ bọc NEMA / CSA · knockouts · MSHA")
    return ("<b>Key terms.</b> encapsulation · type of protection \"m\" · increased "
            "safety \"e\" · hermetically sealed · reed switch · intrinsically safe "
            "\"i\", \"ia\", \"ib\" · NEC 504 · NEC 505 · IEC 60 079-11 · RST-49 · "
            "oil immersion \"o\" · purged and pressurized \"p\" · positive pressure · "
            "inert gas · interlocked · X / Y / Z · CENELEC · powder filling \"q\" · "
            "glass or quartz powder · Class II equipment · dusttight · "
            "Dust-ignition proof · ignition temperature · surface temperature · "
            "NEMA / CSA enclosure · knockouts · MSHA")


def body_vi():
    b = []
    b.append(h2(TITLE_VI, TITLE_EN))
    b.append(lead("Mỗi phương pháp bảo vệ ngăn thiết bị điện trở thành nguồn đánh lửa "
                  "bằng một cơ chế riêng. Chương này trình bày các loại bảo vệ được "
                  "dùng trong môi trường nguy hiểm, sau đó mô tả các loại vỏ bọc "
                  "theo NEMA và CSA."))

    b.append(h3("Đóng gói – loại bảo vệ \"m\"", "Encapsulation – Type of Protection \"m\""))
    b.append(p("Đóng gói là loại bảo vệ trong đó các bộ phận có thể đánh lửa môi "
               "trường nổ được bao kín trong nhựa. Nhựa phải đủ chống chịu ảnh hưởng "
               "của môi trường để môi trường nổ không thể bị đánh lửa bởi tia lửa "
               "hoặc nhiệt có thể phát sinh bên trong thiết bị. Phương pháp này "
               "thường dùng với thiết bị điện tử."))

    b.append(h3("An toàn tăng cường – loại bảo vệ \"e\"",
                "Increased Safety – Type of Protection \"e\""))
    b.append(p("Loại bảo vệ áp dụng cho thiết bị điện không tạo ra hồ quang hay tia "
               "lửa trong điều kiện làm việc bình thường và trong các điều kiện bất "
               "thường quy định, trong đó các biện pháp bổ sung được áp dụng nhằm "
               "tăng cường an toàn chống lại khả năng nhiệt độ quá cao và sự xuất "
               "hiện của hồ quang và tia lửa."))

    b.append(h3("Kín khít (Hermetically Sealed)", "Hermetically Sealed"))
    b.append(p("Một ví dụ thường gặp của thiết bị kín khít là cụm tiếp điểm hoặc công "
               "tắc reed. Trong phương pháp này, các bộ phận tạo hồ quang của công "
               "tắc được bọc trong ống thủy tinh. Dây dẫn được nung chảy vào thủy "
               "tinh để bịt kín cụm, ngăn không cho khí dễ cháy xâm nhập. Thiết bị "
               "kín khít chỉ phù hợp cho Class I, Division 2 hoặc Zone 2."))

    b.append(h3("Thiết bị an toàn nội tại – các loại bảo vệ \"i\", \"ia\" và \"ib\"",
                "Intrinsically Safe Equipment – Types of Protection \"i\", \"ia\" and \"ib\""))
    b.append(p("Bắc Mỹ hiện xác định ba phiên bản của phương pháp bảo vệ này. Loại "
               "\"i\" (NEC 504) và loại \"ia\" (NEC 505) là như nhau vì loại \"i\" "
               "dựa trên Tiêu chuẩn IEC 60 079-11. Trong Zone 0, loại thiết bị được "
               "chấp nhận duy nhất là loại \"i\" và \"ia\". Loại \"ib\" được chấp "
               "nhận tại các vị trí Zone 1 và Zone 2."))
    b.append(p("(Để biết chi tiết hơn, xem Catalog RST-49 của R. STAHL Inc.)"))

    b.append(h3("Ngâm dầu – loại bảo vệ \"o\"", "Oil Immersion – Type of Protection \"o\""))
    b.append(p("Loại bảo vệ trong đó thiết bị điện được ngâm trong chất lỏng bảo vệ "
               "sao cho môi trường nổ có thể hiện diện phía trên chất lỏng hoặc bên "
               "ngoài vỏ bọc không thể bị đánh lửa."))

    b.append(h3("Thổi và tăng áp – loại bảo vệ \"p\"",
                "Purged and Pressurized – Type of Protection \"p\""))
    b.append(p("Loại bảo vệ này ngăn khí quyển bao quanh xâm nhập vào vỏ bọc bằng "
               "cách duy trì áp suất dương bên trong thiết bị. Không khí sạch hoặc "
               "khí trơ được dùng để duy trì áp suất cao hơn môi trường bao quanh. "
               "Khi thổi, thiết bị điện được liên khóa với một hệ thống tuần hoàn "
               "không khí sạch bên trong thiết bị để loại bỏ khí nổ trước khi khởi "
               "động."))
    b.append(p("Bắc Mỹ xác định ba loại tăng áp như sau:"))
    b.append(table(
        ["Loại", "Giải thích"],
        _PURGE_ROWS_VI,
        caption="Bảng 3-1. Ba loại tăng áp theo Bắc Mỹ (bản in A5), kèm chú thích "
                "của nguyên bản."))

    b.append(h3("Nhồi bột – loại bảo vệ \"q\"", "Powder Filling – Type of Protection \"q\""))
    b.append(p("Loại bảo vệ trong đó các bộ phận điện có khả năng đánh lửa môi "
               "trường nổ được cố định tại chỗ và được bao quanh hoàn toàn bằng vật "
               "liệu độn (bột thủy tinh hoặc thạch anh) để ngăn đánh lửa môi trường "
               "nổ bên ngoài."))

    b.append(h3("Thiết bị Class II", "Class II Equipment"))
    b.append(p("Thiết bị kín bụi được thiết kế để ngăn bụi xâm nhập vào vỏ bọc, nhằm "
               "ngăn các hạt nóng, hồ quang, tia lửa hoặc nhiệt phát sinh bên trong "
               "vỏ bọc đánh lửa đống bụi tích tụ bên ngoài hoặc hỗn hợp bụi lơ lửng "
               "trong không khí trên hoặc gần vỏ bọc. Vỏ bọc bằng vật liệu phi kim "
               "loại cũng phải ngăn sự tích tụ điện tích tĩnh trên chính vỏ bọc."))
    b.append(p("Chức năng chính của các mối nối của những vỏ bọc này là bịt kín để "
               "bụi không vào và giữ các hạt nóng ở bên trong, vì vậy thông thường "
               "các mối nối được lắp gioăng."))
    b.append(p("Vì phương pháp bảo vệ này giữ bụi dễ cháy ở bên ngoài, vỏ bọc không "
               "được kỳ vọng hoặc thiết kế để chịu một vụ nổ bên trong. Tuy nhiên, "
               "thiết kế phải đủ bền để chịu được tác động cơ học."))
    b.append(p("Nhiệt độ đánh lửa của bụi thường thấp hơn của khí và hơi, do đó việc "
               "kiểm soát nhiệt độ bề mặt bên ngoài nghiêm ngặt hơn đối với thiết bị "
               "Class II so với thiết bị Class I. Các lớp bụi phủ trên thiết bị có "
               "thể đóng vai trò như lớp cách nhiệt cho nhiệt sinh ra bên trong thiết "
               "bị, từ đó làm tăng nhiệt độ bề mặt của thiết bị ngay cả trong điều "
               "kiện vận hành bình thường."))
    b.append(p("NEC định nghĩa \"Dust-ignition proof\" là sự bảo vệ cho các vị trí "
               "Class II, Division 1 và 2 mà nó được phê duyệt, và \"Dusttight\" là "
               "loại vỏ bọc được chế tạo sao cho bụi không xâm nhập vào hộp trong "
               "các điều kiện thử nghiệm cụ thể. Theo NEC, một số ứng dụng cho "
               "Class II, Division 1 yêu cầu vỏ bọc Dust-ignition proof."))

    b.append(h3("Vỏ bọc theo loại NEMA và CSA", "NEMA and CSA Type Enclosure"))
    b.append(p("Các loại vỏ bọc sau đây được mô tả theo yêu cầu của NEMA và CSA; "
               "danh sách này được trình bày dưới dạng danh mục thay vì bảng để "
               "giữ nguyên văn phong của nguyên bản."))
    b.append(ul(_NEMA_TYPES_VI))
    b.append(h3("Định nghĩa liên quan đến yêu cầu NEMA cho vị trí nguy hiểm",
                "Definitions Referring To NEMA Requirements for Hazardous Location"))
    b.append(p("Các loại vỏ bọc NEMA sau đây đôi khi xuất hiện trong bản đặc tả và "
               "tài liệu sản phẩm:"))
    b.append(ul(_NEMA_HAZ_VI))
    b.append(note("<b>Đặc điểm của nguyên bản.</b> Chương trải trên hai trang in "
                  "(A5–A6). Bảng X/Y/Z là bảng duy nhất của đơn vị này và được giữ "
                  "nguyên cả chú thích \"*Similar purging methods are found in the "
                  "IEC, CENELEC and NEC 505.\" Các mã và tiêu chuẩn (m, e, i, ia, ib, "
                  "o, p, q, NEC 504, NEC 505, IEC 60 079-11, RST-49, Zone 0/1/2, "
                  "Class I/II, Division 1/2) được giữ nguyên. Mười ba loại vỏ bọc "
                  "NEMA/CSA và bốn loại dùng cho vị trí nguy hiểm được trình bày "
                  "dưới dạng danh mục, không phải bảng."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. "
               "Nội dung gốc © R. STAHL, Inc.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(h2(TITLE_EN, TITLE_EN))
    b.append(lead("Each method of protection keeps electrical equipment from "
                  "becoming an ignition source by a different mechanism. This "
                  "chapter presents the types of protection used in hazardous "
                  "locations and then describes the NEMA and CSA enclosure types."))

    b.append(h3("Encapsulation – Type of Protection \"m\"",
                "Encapsulation – Type of Protection \"m\""))
    b.append(p("Encapsulation is a type of protection in which the parts that can "
               "ignite an explosive atmosphere are enclosed in a resin. The resin "
               "must be sufficiently resistant to environmental influences so that "
               "the explosive atmosphere cannot be ignited by either sparking or "
               "heating, which may occur within the device. This is typically used "
               "with electronic devices."))

    b.append(h3("Increased Safety – Type of Protection \"e\"",
                "Increased Safety – Type of Protection \"e\""))
    b.append(p("Type of protection applied to electrical equipment that does not "
               "produce arcs or sparks in normal service and under specified "
               "abnormal conditions, in which additional measures are applied so as "
               "to give increased security against the possibility of excessive "
               "temperatures and of the occurrence of arcs and sparks."))

    b.append(h3("Hermetically Sealed", "Hermetically Sealed"))
    b.append(p("A common type of hermetically sealed equipment is a contact block "
               "or reed switch. In this method, the arcing components of the switch "
               "are encased in a glass tube. The connecting wires are fused to the "
               "glass sealing the unit to prevent any ingress of flammable gases. "
               "Hermetically sealed equipment is suitable for Class I, Division 2 "
               "or Zone 2 only."))

    b.append(h3("Intrinsically Safe Equipment – Types of Protection \"i\", \"ia\" and \"ib\"",
                "Intrinsically Safe Equipment – Types of Protection \"i\", \"ia\" and \"ib\""))
    b.append(p("North America now identifies three versions of this protection "
               "method. Types \"i\" (NEC 504) and \"ia\" (NEC 505) are identical "
               "since type \"i\" is based on the IEC 60 079-11 Standard. In Zone 0 "
               "the only acceptable type of equipment is types \"i\" and \"ia\". "
               "Type \"ib\" is acceptable in Zone 1 and 2 locations."))
    b.append(p("(For further details refer to R. STAHL Inc's Catalog RST-49.)"))

    b.append(h3("Oil Immersion – Type of Protection \"o\"",
                "Oil Immersion – Type of Protection \"o\""))
    b.append(p("Type of protection where electrical equipment is immersed in a "
               "protective liquid in such a way that an explosive atmosphere that "
               "may be above the liquid or outside the enclosure cannot be ignited."))

    b.append(h3("Purged and Pressurized – Type of Protection \"p\"",
                "Purged and Pressurized – Type of Protection \"p\""))
    b.append(p("This type of protection prevents the surrounding atmosphere from "
               "entering an enclosure by maintaining a positive pressure within the "
               "unit. Clean air or inert gas is used to maintain a higher pressure "
               "than the surrounding atmosphere. In purging, the electrical "
               "equipment is interlocked with a system which cycles clean air "
               "within the unit to remove explosive gases before start up."))
    b.append(p("North America Identifies three types of pressurization as follows:"))
    b.append(table(
        ["Type", "Explanation"],
        _PURGE_ROWS_EN,
        caption="Table 3-1. The three North American types of pressurization "
                "(printed A5), with the original footnote."))

    b.append(h3("Powder Filling – Type of Protection \"q\"",
                "Powder Filling – Type of Protection \"q\""))
    b.append(p("Type of protection where electrical parts capable of igniting an "
               "explosive atmosphere are fixed in position and completely "
               "surrounded by filling material (glass or quartz powder) to prevent "
               "the ignition of an external explosive atmosphere."))

    b.append(h3("Class II Equipment", "Class II Equipment"))
    b.append(p("Dusttight equipment is designed to exclude dust from entering the "
               "enclosure, to prevent hot particles, arcs, sparks or heat generated "
               "inside of the enclosure from igniting an exterior accumulation or "
               "atmospheric suspension of dusts on or in the vicinity of the "
               "enclosure. Nonmetallic enclosures must also prevent the accumulation "
               "of static charges on the enclosure itself."))
    b.append(p("The primary function of the joints of these enclosures is to seal "
               "dust out and keep the hot particles etc. inside, therefore, "
               "typically the joints are gasketed."))
    b.append(p("Since this protection method keeps the combustible dusts outside, "
               "the enclosure is not expected or designed to contain an internal "
               "explosion. The design must be sufficient though to withstand "
               "mechanical abuse."))
    b.append(p("The ignition temperature of dusts is usually lower than that of "
               "gases and vapors, and therefore the control of external surface "
               "temperatures is more rigorous for Class II equipment than for "
               "Class I equipment. Dust layers on the equipment can act as "
               "insulation for the heat generated inside the equipment, which in "
               "turn can increase the surface temperature of the unit even under "
               "normal operating conditions."))
    b.append(p("The NEC defines \"Dust-ignition proof\" as the protection for "
               "Class II, Division 1 and 2 locations for which it is approved, and "
               "\"Dusttight\" as a type of enclosure that is constructed so that "
               "dusts will not enter the enclosing case under specific test "
               "conditions. In the NEC, some applications for Class II, Division 1 "
               "require Dust-ignition proof enclosures."))

    b.append(h3("NEMA and CSA Type Enclosure", "NEMA and CSA Type Enclosure"))
    b.append(p("The following enclosure types are described to NEMA and CSA "
               "requirements. They are presented as a list rather than a table to "
               "follow the wording of the original."))
    b.append(ul(_NEMA_TYPES_EN))
    b.append(h3("Definitions Referring To NEMA Requirements for Hazardous Location",
                "Definitions Referring To NEMA Requirements for Hazardous Location"))
    b.append(p("The following NEMA type enclosures occasionally appear on "
               "specifications and product literature:"))
    b.append(ul(_NEMA_HAZ_EN))
    b.append(note("<b>Source quirks.</b> The unit spans two printed pages (A5-A6). "
                  "The X/Y/Z table is the only table in this unit and retains its "
                  "printed footnote, \"*Similar purging methods are found in the "
                  "IEC, CENELEC and NEC 505.\" All codes and standards (m, e, i, ia, "
                  "ib, o, p, q, NEC 504, NEC 505, IEC 60 079-11, RST-49, Zone 0/1/2, "
                  "Class I/II, Division 1/2) are kept verbatim. The thirteen NEMA/CSA "
                  "enclosure types and the four hazardous-location types are given "
                  "as lists, not tables."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original "
               "content © R. STAHL, Inc.</i>"))
    return "".join(b)
