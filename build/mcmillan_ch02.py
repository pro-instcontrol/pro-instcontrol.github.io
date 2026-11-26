# -*- coding: utf-8 -*-
"""Chapter 2 - Area classification / Phân loại khu vực (EN/VI bilingual).

EN/VI bilingual study reader of Alan McMillan, *Electrical Installations in
Hazardous Areas* (Butterworth-Heinemann, 1998), printed pp. 22-42.
Covers all nine printed sections (2.1-2.9), Table 2.1, six redrawn vector
figures (ignition-curve chart, three blank forms and two flowcharts) and six
numbered references.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import fig, h2, h3, h4, lead, note, p, refs, table

import mcmillanfig02_a as FA
import mcmillanfig02_b as FB
import mcmillanfig02_c as FC

PAGES_SRC = 21
BYLINE = "Alan McMillan · Electrical Installations in Hazardous Areas (Butterworth-Heinemann, 1998)"
TITLE_EN = "Area classification"
TITLE_VI = "Phân loại khu vực"

_REFS = [
    "BS/CP 1003 Electrical Apparatus and Associated Equipment for use in Explosive "
    "Atmospheres other than Mining Applications: Part 1 (1964). Choice Installation and "
    "Maintenance of Flameproof and Intrinsically Safe Equipment; Part 2 (1966). Methods of "
    "Meeting the Explosion Hazard other than by Use of Flameproof and Intrinsically Safe "
    "Equipment; Part 3 (1967). Division 2 Areas.",
    "BS 5345. Selection, Installation and Maintenance of Electrical Apparatus for use in "
    "Potentially Explosive Atmospheres (other than mining operations or explosives "
    "processing and manufacture). Part 2 (1983). Classification of hazardous areas.",
    "IEC 1241-3. Electrical apparatus with protection by enclosure for use in the presence "
    "of combustible dusts Part 2 (1988). Guide to Selection, Installation and Maintenance.",
    "BSI 94/213454 Draft IEC Publication IEC 1241-3. Electrical Apparatus for use in the "
    "presence of Combustible Dust. Part 3. Classification of areas where combustible dusts "
    "are or may be present.",
    "RoSPA/ICI Engineering Codes and Regulations, Electrical Installation in Flammable "
    "Atmosphere (1973). Group C (Electrical), Volume 1.5.",
    "CAF — term normally used to describe an unsupported gasket, historically made from "
    "compressed asbestos fibre.",
]

_T21_HEAD_VI = ["IEC/CENELEC/GB (Ghi chú 1)", "Đức (Ghi chú 2)",
                "Pháp (Ghi chú 3)", "Hoa Kỳ"]
_T21_HEAD_EN = ["IEC/CENELEC/GB (Note 1)", "German (Note 2)",
                "French (Note 3)", "USA"]
_T21_ROWS_VI = [
    ["Vùng 0", "Khu vực đặc biệt theo lệnh Ex", "Division 1", "Division 1"],
    ["Vùng 1", "Khu vực bình thường theo lệnh Ex", "Division 1", "Division 1"],
    ["Vùng 2", "Khu vực nguy hiểm không nằm trong lệnh Ex", "Division 2", "Division 2"],
]
_T21_ROWS_EN = [
    ["Zone 0", "Special area in Ex order", "Division 1", "Division 1"],
    ["Zone 1", "Normal area in Ex order", "Division 1", "Division 1"],
    ["Zone 2", "Hazardous area not within Ex order", "Division 2", "Division 2"],
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 2.</b> phân loại khu vực (area classification) · bầu khí "
                "quyển nổ · nguồn phát thải (source of release) · cấp phát thải liên tục / "
                "chính / phụ · vùng Zone 0, 1, 2 · vùng Zone Z, Y · vùng Zone 20, 21, 22 · "
                "giới hạn nổ dưới (LEL) · năng lượng đánh lửa tối thiểu · nhiệt độ đánh lửa · "
                "mật độ tương đối · tam giác nổ · điểm chớp cháy · nhóm khí IIA/IIB/IIC · "
                "cấp nhiệt độ T1–T6 · hệ thống phân tán · bảng LEAC · thông gió · bụi dẫn "
                "điện · lớp bụi 5 mm · đệm CAF · dập khí trơ (inert blanketing) · "
                "đường ống hàn toàn bộ · BS/CP 1003 · BS 5345 · IEC 1241-3")
    return ("<b>Key terms in Chapter 2.</b> area classification · explosive atmosphere · "
            "source of release · continuous / primary / secondary grade of release · "
            "Zones 0, 1 and 2 · Zones Z and Y · Zones 20, 21 and 22 · lower explosive "
            "limit (LEL) · minimum ignition energy · ignition temperature · relative "
            "density · explosion triangle · flashpoint · gas subgroups IIA/IIB/IIC · "
            "temperature classes T1–T6 · dispersion · LEAC sheet · ventilation · "
            "conducting dust · 5 mm dust layer · CAF gasket · inert blanketing · "
            "all-welded pipe · BS/CP 1003 · BS 5345 · IEC 1241-3")


def body_vi():
    b = []
    b.append(h2("Phân loại khu vực", "Area classification"))
    b.append(lead("Triết lý, mục tiêu và quy trình"))
    b.append(p("Mục tiêu cơ bản của phân loại khu vực (dù rủi ro do khí, hơi, sương mù hay "
               "bụi) là xác định khả năng tồn tại bầu khí quyển nổ tại một vị trí nhất định "
               "và, quan trọng hơn, ảnh hưởng đến thiết kế của nhà máy hoặc cơ sở để giảm "
               "thiểu các rủi ro đó. Đây là công cụ dùng cùng với yêu cầu vận hành trong "
               "thiết kế của mọi nhà máy, quy trình hoặc cơ sở, và kết quả luôn là sự thỏa "
               "hiệp giữa tiện lợi vận hành và an toàn chống nổ. Sự cân bằng này phải tính "
               "đến những tình huống nhìn chung không được phép, chẳng hạn sự hiện diện "
               "liên tục của bầu khí quyển nổ ở khu vực không bị hạn chế, và các giới hạn "
               "được đặt ra cho mức độ chấp nhận được của bất kỳ tình huống nào có thể có "
               "bầu khí quyển nổ. Chương này xác định các nguyên lý làm nền tảng cho phân "
               "loại khu vực, vai trò của những người tham gia thiết kế hoặc vận hành, và "
               "quy trình cần thực hiện để xác định các khu vực nguy hiểm."))

    b.append(h3("2.1 Tính chất cơ bản của vật liệu dễ cháy và cháy được",
                "2.1 Basic properties of flammable and combustible materials"))
    b.append(p("Vật liệu ta quan tâm là khí, hơi, sương mù và bụi. Mỗi loại cư xử khác đi "
               "và điều đó ảnh hưởng đến quá trình phân loại."))
    b.append(h4("2.1.1 Khí dễ cháy", "2.1.1 Flammable gases"))
    b.append(p("Khí là vật liệu ở trạng thái thông thường trong điều kiện nhiệt độ và áp "
               "suất môi trường là hơi. Những vật liệu này không thể hóa lỏng ở nhiệt độ "
               "môi trường chỉ bằng áp suất mà phải làm lạnh thêm. Vì vậy, chúng ít khi "
               "hiện diện dưới dạng lỏng và nếu có thì sẽ bay hơi nhanh sau khi thoát ra. "
               "Phân loại khu vực là thước đo diện tích bị nhiễm bởi sự phát thải và ít bị "
               "ảnh hưởng bởi hiệu ứng tồn dư sau khi phát thải chấm dứt, miễn là thông "
               "gió đủ để loại bỏ khí."))
    b.append(p("Các đặc tính quan trọng quyết định cách tiếp cận với thiết bị điện có thể "
               "tiếp xúc với khí gồm: mật độ tương đối so với không khí, quyết định cách "
               "khí phân tán khi không có ảnh hưởng khác (khí thoát ra với vận tốc cao phân "
               "tán theo năng lượng phát thải, không theo gió hay mật độ); năng lượng đánh "
               "lửa tối thiểu, tức năng lượng nhỏ nhất dưới dạng hồ quang hoặc tia lửa "
               "đánh cháy được hỗn hợp dễ đánh lửa nhất; khe hở an toàn thử nghiệm tối đa, "
               "đặc trưng khả năng cháy lan qua khe hở nhỏ của hỗn hợp khí/không khí lý "
               "tưởng; và nhiệt độ đánh lửa, nhiệt độ thấp nhất mà hỗn hợp lý tưởng tự "
               "bốc cháy."))
    b.append(p("Ngay khi thoát ra, khí trộn với không khí nhờ năng lượng của chính dòng "
               "thoát hoặc chuyển động nhiễu loạn của không khí. Khi phát thải ở vận tốc "
               "thấp và chuyển động không khí nhỏ (như trong nhà xưởng thông gió kém), "
               "trộn lẫn kém hiệu quả hơn và hỗn hợp thay đổi theo từng nơi, tạo ra các "
               "khu vực nguy hiểm lớn và khó dự báo."))
    b.append(h4("2.1.2 Hơi dễ cháy", "2.1.2 Flammable vapours"))
    b.append(p("Hơi dễ cháy rất giống khí vì cũng ở pha hơi, nhưng có thể hóa lỏng chỉ bằng "
               "áp suất. Hơi có thể chỉ là hơi phát ra từ một chất lỏng dễ cháy: mọi chất "
               "lỏng như vậy đều có áp suất hơi (áp suất riêng phần trong không khí) ở "
               "nhiệt độ thấp hơn nhiều so với điểm sôi, và khi tỷ lệ hơi trong không khí "
               "vượt giới hạn nổ dưới thì có thể tồn tại bầu khí quyển nổ dù chất thoát ra "
               "là chất lỏng. Thời gian tồn tại của bầu khí quyển do hơi thay đổi nhiều: "
               "thấp nếu thoát ra dưới dạng hơi hoặc chất lỏng có điểm sôi thấp hơn nhiều "
               "nhiệt độ môi trường, cao nếu bay hơi từ bề mặt chất lỏng có điểm sôi cao "
               "hơn nhiệt độ môi trường. Tiêu chí tạo hỗn hợp và các thông số quan trọng "
               "cũng giống như đối với khí."))
    b.append(h4("2.1.3 Sương mù dễ cháy", "2.1.3 Flammable mists"))
    b.append(p("Đây là tình huống hoàn toàn khác. Sương mù được tạo ra khi phát thải ở áp "
               "suất cao (đã hình thành ở áp suất đo tới 2 × 10⁵ N/m²) tạo ra các hạt lỏng "
               "rất mịn. Sương mù có thể tạo bầu khí quyển nổ với không khí ngay cả khi "
               "chất lỏng tạo ra nó được coi là có áp suất hơi không đủ. Các hạt này tái "
               "kết hợp thành lỏng dễ hơn khí hoặc hơi, nhưng nếu phân tán rất mịn thì "
               "sương mù tồn tại đáng kể và các hạt lơ lửng lâu trong không khí. Người ta "
               "biết ít về hành vi của sương mù trong không khí, nhưng khi phân loại khu "
               "vực chúng thường được xử lý như khí và hơi."))
    b.append(h4("2.1.4 Chất lỏng dễ cháy", "2.1.4 Flammable liquids"))
    b.append(p("Đây là cách gọi hơi sai vì chất lỏng không cháy. Chất lỏng dễ cháy là chất "
               "lỏng mà, ở nhiệt độ và áp suất môi trường thông thường hoặc ở điều kiện "
               "xử lý và cất giữ, có áp suất hơi (áp suất riêng phần) đủ để giải phóng đủ "
               "hơi tạo thành bầu khí quyển nổ."))
    b.append(h4("2.1.5 Bụi cháy được", "2.1.5 Combustible dusts"))
    b.append(p("Bụi cháy được là bụi cháy khi trộn với không khí, hoặc ở dạng lớp sẽ cháy "
               "nếu bị đánh lửa. Không nên nhầm với chất nổ. Bụi cần được xử lý khác khí, "
               "hơi và sương mù: dù phát thải thường ở dạng đám mây, bụi không phân tán "
               "như khí/hơi mà ban đầu tạo đám mây rồi lắng thành lớp. Sau khi thoát ra, "
               "chỉ công tác dọn dẹp mới ảnh hưởng được đến sự tồn tại của đám mây do lớp "
               "bụi bị khuấy động."))
    b.append(p("Các thông số quan trọng của bụi gồm: năng lượng đánh lửa đám mây, năng "
               "lượng nhỏ nhất dưới dạng hồ quang hoặc tia lửa để đánh cháy đám mây; "
               "nhiệt độ đánh lửa đám mây, nhiệt độ thấp nhất mà hỗn hợp lý tưởng giữa "
               "bụi lơ lửng và không khí bốc cháy (phụ thuộc cỡ hạt); nhiệt độ đánh lửa "
               "lớp bụi, nhiệt độ thấp nhất mà một lớp bụi có độ dày xác định bốc cháy; "
               "và cỡ hạt, ảnh hưởng đến khả năng đánh lửa."))

    b.append(h3("2.2 Cơ sở của phân loại khu vực", "2.2 Basis of area classification"))
    b.append(p("Phân loại khu vực dựa trên những tình huống có thể xảy ra trong vận hành "
               "nhà máy và nhà xưởng thực tế, tạo ra bầu khí quyển nổ với mức độ đều đặn "
               "đủ để cần xét đến việc đưa vào thiết bị có thể trở thành nguồn đánh lửa. "
               "Nó không nhằm giải quyết khả năng nổ trong điều kiện hỏng hóc thảm khốc, "
               "vốn nhìn chung khó dự báo. Dù vậy, vẫn cần có quy trình xử lý thảm họa, "
               "dù quy trình đó không thuộc phân loại khu vực."))
    b.append(p("Có ba tình huống có thể dự báo: (1) bầu khí quyển nổ hiện diện dài hạn hoặc "
               "liên tục do nhu cầu vận hành — bên trong bình chứa và thiết bị xử lý khí, "
               "hơi, sương mù hoặc bụi có không khí, bên trong bình chứa chất lỏng/khí/hơi "
               "có không khí, silo và nhà nghiền có bụi và không khí; (2) bầu khí quyển nổ "
               "xuất hiện đều đặn trong vận hành bình thường — quanh phớt quay bị mòn, điểm "
               "nạp thủ công, điểm nạp bao bột, khu vực phun sơn; và (3) bầu khí quyển nổ "
               "xuất hiện hiếm, thường do hỏng thiết bị hoặc sai quy trình — hỏng gioăng "
               "đường ống, tràn bình do lỗi điều khiển, phòng xử lý bột nơi lớp bụi bị "
               "khuấy thành đám mây."))

    b.append(h3("2.3 Cách tiếp cận chung", "2.3 General approach to area classification"))
    b.append(p("Phân loại khu vực hiện đại, khác với cách tiếp cận cũ trong BS/CP 1003, "
               "dựa trên việc xác định từng nguồn nguy hiểm và hệ quả của chúng. BS/CP 1003 "
               "dựa trên đánh giá chung khu vực có rủi ro rồi suy ra nguy hiểm từ đánh giá "
               "đó, dẫn đến cách áp dụng khác nhau giữa các tổ chức: có nơi phân loại quá "
               "mức, coi toàn nhà máy là rủi ro cao, và đáng lo hơn là có nơi phân loại "
               "thiếu, lắp thiết bị điện được bảo vệ không đầy đủ. Nhà máy cũ từng phân "
               "loại theo cách khái quát đó cần được đánh giá lại theo tư duy hiện đại."))
    b.append(p("Việc xác định nguồn nguy hiểm được chuẩn hóa cho khí, hơi và sương mù trong "
               "BS 5345 phần 2; dù BS 6467 phần 23 chưa có cách xác định tương tự cho bụi, "
               "văn bản dự kiến thay thế là IEC 1241-3 đã có dạng xác định tương tự. Vì "
               "vậy nguồn phát thải có thể được phân loại, dù là khí, hơi, sương mù hay bụi."))

    b.append(h3("2.4 Phân loại nguồn phát thải", "2.4 Classification of sources of release"))
    b.append(p("<b>Cấp phát thải liên tục (continuous).</b> Điểm hoặc vị trí mà khí, hơi, "
               "sương mù dễ cháy hoặc bụi cháy được có thể thoát ra liên tục hoặc trong "
               "thời gian dài, tạo được bầu khí quyển nổ trong thời gian đó."))
    b.append(p("<b>Cấp phát thải chính (primary).</b> Điểm hoặc vị trí mà vật liệu đó có thể "
               "thoát ra chu kỳ hoặc thỉnh thoảng trong vận hành bình thường, tạo được "
               "bầu khí quyển nổ trong thời gian đó."))
    b.append(p("<b>Cấp phát thải phụ (secondary).</b> Điểm hoặc vị trí mà vật liệu đó không "
               "được kỳ vọng thoát ra trong vận hành bình thường, nhưng có thể thoát ra "
               "thỉnh thoảng trong thời gian ngắn, hoặc nơi lớp bụi hình thành đến mức "
               "nếu bị khuấy sẽ tạo bầu khí quyển nổ."))
    b.append(p("Ba cấp trên là nền tảng để xác định cấp của từng nguồn phát thải. Một quy "
               "tắc công ty năm 1973 đưa ra hướng dẫn số lượng: liên tục là trên 1000 giờ "
               "mỗi năm (hơn 10% năm), chính là từ 10 đến 1000 giờ mỗi năm (0,1% đến 10%), "
               "phụ là dưới 10 giờ mỗi năm (dưới 0,1%). Hướng dẫn này chưa từng được đưa "
               "vào tiêu chuẩn hay quy phạm quốc gia/quốc tế, nhưng được dùng rộng rãi; "
               "nó nhằm phân biệt các loại phát thải chứ không phải ranh giới số nghiêm "
               "ngặt, nên chỉ nên dùng thận trọng."))
    b.append(p("Ví dụ, phớt quay theo hồ sơ của một nhà máy có thể chỉ rò rỉ ba năm một lần "
               "và vì thế bị gán cấp phụ. Nhưng điều đó có thể chỉ là ngẫu nhiên trong "
               "giai đoạn cụ thể đó; chọn một giai đoạn ba năm khác có thể cho thấy tần "
               "suất cao hơn nhiều. Trừ khi có độ tin cậy rất cao vào hoàn cảnh riêng, cần "
               "dùng trường hợp chung là cấp chính. Trường hợp ngoại lệ cực kỳ hiếm và phải "
               "có biện giải đầy đủ."))

    b.append(h3("2.5 Phân loại vùng nguy hiểm", "2.5 Hazardous zonal classification"))
    b.append(p("Sau khi xác định loại phát thải, có thể xác định rủi ro hiện diện bầu khí "
               "quyển nổ tại một vị trí, dựa trên khả năng phát thải, bản chất phát thải "
               "và thông gió tại chỗ. Trừ phát thải bên trong bình chứa, mức độ tồn tại "
               "của bầu khí quyển nổ phụ thuộc đáng kể vào thông gió và đặc tính phân tán "
               "của vật liệu."))
    b.append(h4("2.5.1 Khí, hơi và sương mù", "2.5.1 Gases, vapours and mists"))
    b.append(p("<b>Vùng 0</b> là vùng mà hỗn hợp khí, hơi hoặc sương mù/đám mây với không "
               "khí có liên tục hoặc trong thời gian dài. <b>Vùng 1</b> là vùng mà hỗn hợp "
               "đó có khả năng xuất hiện trong vận hành bình thường. <b>Vùng 2</b> là vùng "
               "mà hỗn hợp đó ít có khả năng xuất hiện trong vận hành bình thường và nếu "
               "có thì chỉ tồn tại trong thời gian ngắn. Các định nghĩa này nằm trong BS "
               "5345 phần 2 và có nhiều văn bản khác dùng cách diễn đạt tương đương. Nhiều "
               "quốc gia có hệ thống phân loại riêng, cũ hoặc hiện hành, liên quan đến "
               "hệ thống ba vùng được công nhận quốc tế như Bảng 2.1."))
    b.append(table(_T21_HEAD_VI, _T21_ROWS_VI,
                   "Bảng 2.1 · Quan hệ giữa các hệ thống phân loại khu vực quốc gia."))
    b.append(p("<small><b>Ghi chú 1.</b> Dù không gọi tên rõ ràng, Đức từng vận hành hệ "
               "thống rủi ro ba cấp; hiện dùng hệ thống IEC/CENELEC/GB. <b>Ghi chú 2.</b> "
               "Pháp từng gộp Vùng 0 và 1 thành một Division 1; hiện dùng hệ thống "
               "IEC/CENELEC/GB. <b>Ghi chú 3.</b> Hoa Kỳ từng vận hành giống Pháp nhưng gần "
               "đây bắt đầu dùng hệ thống ba vùng IEC/CENELEC/GB. Đánh số ghi chú trong "
               "bản in không khớp hoàn toàn với nhãn cột; giữ nguyên để đối chiếu.</small>"))
    b.append(h4("2.5.2 Bụi", "2.5.2 Dusts"))
    b.append(p("Với bụi, tình hình linh hoạt hơn và mức độ chuẩn hóa thấp hơn; ở Vương quốc Anh, vấn đề này chỉ "
               "được giải quyết hiệu quả trong 15–20 năm gần đây. <b>Vùng Z</b> là vùng mà "
               "bụi cháy được có thể hiện diện dưới dạng đám mây trong quá trình chế biến, "
               "xử lý hoặc dọn dẹp bình thường với số lượng đủ tạo nồng độ nổ được trong "
               "hỗn hợp với không khí. <b>Vùng Y</b> là khu vực không xếp vào Vùng Z nhưng "
               "có thể có lớp hoặc đống bụi cháy được trong điều kiện bất thường, tạo hỗn "
               "hợp bụi/không khí dễ đánh lửa. Các định nghĩa này giống BS 6467 phần 23; "
               "dù khác với định nghĩa cho khí, khi tính đến đặc tính bụi có thể thấy quan "
               "hệ giữa Vùng 1 và Vùng Z, và giữa Vùng 2 và Vùng Y."))
    b.append(p("IEC 1241-3 sẽ thay thế bằng ba định nghĩa mới: <b>Vùng 20</b> là nơi bụi "
               "cháy dưới dạng đám mây hiện diện liên tục hoặc thường xuyên trong vận hành "
               "bình thường, hoặc nơi có thể hình thành lớp bụi dày không kiểm soát được "
               "(ví dụ bên trong thiết bị chế biến); <b>Vùng 21</b> là nơi không thuộc Vùng "
               "20 nhưng bụi dưới dạng đám mây có khả năng xuất hiện trong vận hành bình "
               "thường (ví dụ ngay quanh điểm nạp hoặc xả bột); <b>Vùng 22</b> là nơi không "
               "thuộc Vùng 21 nhưng bụi có thể xuất hiện thỉnh thoảng và chỉ tồn tại ngắn, "
               "hoặc nơi lớp bụi có thể tạo nồng độ nổ. Về mặt lịch sử, người ta cố giới hạn "
               "lớp bụi dưới 5 mm ở Vùng 21 và 22 (Z và Y), thiết bị điện được thiết kế "
               "giả định lớp bụi 5 mm; IEC 1241-3 cũng xác định 1 mm là độ dày mà từ đó "
               "có thể hình thành bầu khí quyển nổ."))
    b.append(h4("2.5.3 Quan hệ giữa nguồn phát thải và các vùng",
                "2.5.3 Relationship between sources of release and Zones"))
    b.append(p("Với khí, hơi và sương mù ở nơi thông gió tốt như ngoài trời, có quan hệ rõ: "
               "phát thải liên tục cho Vùng 0, phát thải chính cho Vùng 1, phát thải phụ "
               "cho Vùng 2. Quan hệ này hết đúng khi tham số thay đổi: nguồn cấp chính có "
               "thể chỉ cho Vùng 2 nếu thông gió cục bộ pha loãng dưới nồng độ nổ ngay tại "
               "điểm rò; nguồn cấp phụ có thể cho Vùng 1 nếu thông gió cục bộ bị hạn chế. "
               "Với bụi, quan hệ yếu hơn vì hình thành lớp không thực sự đặc trưng theo "
               "vùng và việc phân loại phụ thuộc nhiều vào công tác dọn dẹp."))

    b.append(h3("2.6 Thu thập thông tin", "2.6 Collection of information"))
    b.append(p("Để thực hiện phân loại khu vực chính thức, trước hết cần thu thập thông tin "
               "về vật liệu dễ cháy, cách chứa nó và điều kiện thông gió tại chỗ."))
    b.append(h4("2.6.1 Thông tin về nhiên liệu (khí, hơi và sương mù)",
                "2.6.1 Information on fuels (gases, vapours and mists)"))
    b.append(p("Tối thiểu cần: <b>điểm chớp cháy</b>, nhiệt độ mà tại đó đủ hơi thoát ra để "
               "tạo bầu khí quyển nổ; <b>nhiệt độ đánh lửa</b>, nhiệt độ tối thiểu ở áp suất "
               "khí quyển để đánh cháy hỗn hợp lý tưởng, giới hạn nhiệt độ tối đa cho phép "
               "của thiết bị; <b>dải dễ cháy</b>, khoảng tỷ lệ phần trăm giữa giới hạn nổ "
               "dưới và trên — giới hạn dưới thường quan trọng hơn vì nó xác định phạm vi "
               "bầu khí quyển nổ (Hình 2.1); <b>mật độ khí/hơi</b> so với không khí, ảnh "
               "hưởng phân tán; <b>điểm sôi</b>; <b>khối lượng phân tử</b>; <b>nhiệt ẩn hóa "
               "hơi</b> và <b>nhiệt dung</b>, cần cho tính toán; <b>nhóm phụ</b> IIA, IIB "
               "hoặc IIC (không cần cho phân loại nhưng cần chọn thiết bị); và <b>cấp nhiệt "
               "độ bề mặt</b> T1–T6 dựa trên nhiệt độ đánh lửa."))
    b.append(fig(1, FA.fig_f201()))
    b.append(p("Hình 2.2 là mẫu trống điển hình để thu thập các thông số trên."))
    b.append(fig(2, FB.fig_f202()))
    b.append(h4("2.6.2 Thông tin về nhiên liệu (bụi)",
                "2.6.2 Information on fuels (dusts)"))
    b.append(p("Với bụi, yêu cầu khác đi. Nên ngăn bụi tiếp cận thiết bị có thể phát tia "
               "lửa, nhưng cả lớp bụi trên thiết bị lẫn đám mây bụi đều có thể bị đánh lửa "
               "bởi nhiệt độ. Đánh lửa bằng tia lửa hoặc hồ quang là không phổ biến do bụi "
               "bị loại khỏi bên trong thiết bị. Cần biết: nhiệt độ đánh lửa đám mây bụi; "
               "nhiệt độ đánh lửa lớp bụi dày 5 mm; cấp nhiệt độ; độ dẫn điện (bụi có điện "
               "trở nhỏ hơn 10⁸ Ωm được coi là bụi dẫn điện); và sản phẩm phân hủy — cần "
               "biến liệu bụi sinh ra khí hoặc hơi dễ cháy ở nhiệt độ dưới nhiệt độ đánh "
               "lửa của nó hay không. Hình 2.3 là mẫu thu thập thông tin tương ứng."))
    b.append(fig(3, FB.fig_f203()))
    b.append(h4("2.6.3 Thông tin về điều kiện quy trình",
                "2.6.3 Information on process conditions"))
    b.append(p("Sau khi có thông số của nhiên liệu, cần xác định cách chứa và khả năng thoát "
               "ra: <b>loại thiết bị chứa</b> (ví dụ mặt bích đường ống), <b>vị trí</b> trên "
               "nhà máy (ví dụ trong khu bình chứa, phía trên bình X), <b>vật liệu quy "
               "trình</b> và <b>điều kiện nhiệt độ, áp suất</b> tại điểm có thể rò — vật liệu "
               "có điểm chớp cháy cao hơn môi trường vẫn có thể bắt lửa nếu thoát ra ở "
               "nhiệt độ cao — và <b>mô tả thiết bị chứa</b>, ví dụ loại gioăng của mặt bích. "
               "Từ đó xác định cấp nguồn nguy hiểm và phạm vi khu vực. Một <b>Danh mục thiết "
               "bị để phân loại khu vực (LEAC)</b> như Hình 2.4 là phương pháp điển hình; "
               "bảng này cũng ghi nhóm IIA/IIB/IIC và cấp nhiệt độ T1–T6 của thiết bị điện "
               "và là hồ sơ cơ bản của đợt phân loại."))
    b.append(fig(4, FB.fig_f204()))

    b.append(h3("2.7 Quy trình", "2.7 Procedures"))
    b.append(p("Phân loại khu vực không chỉ nhằm xác định khu vực nguy hiểm sau khi thiết kế "
               "đã hoàn tất dựa trên yêu cầu vận hành và kinh tế, mà phải là một phần của "
               "quá trình thiết kế và ảnh hưởng đáng kể tới nó, loại bỏ khu vực nguy hiểm "
               "nhiều nhất có thể, chỉ giữ lại những khu vực thật cần thiết ở mức rủi ro "
               "chấp nhận được. Vì vậy nên bắt đầu ngay khi có sơ đồ đường ống quy trình "
               "và tinh chỉnh liên tục trong suốt thiết kế."))
    b.append(p("Cần hỏi: lượng vật liệu dễ cháy có nhỏ không? Ở phòng thí nghiệm có thể dùng "
               "nhân viên được đào tạo và quy trình đặc biệt thay cho phân loại khu vực, "
               "nhưng phải thận trọng cực kỳ. Nếu không biện minh được giải pháp thay thế "
               "và có lượng vật liệu đáng kể, hỏi tiếp: vật liệu có thể thoát ra không? "
               "Nếu không trộn được với không khí thì không hình thành bầu khí quyển nổ "
               "và không có khu vực nguy hiểm (ngoại lệ: đường ống hàn toàn bộ đi ngang "
               "qua một khu vực). Tiếp theo: phát thải xảy ra thế nào (bề mặt chất lỏng, "
               "hỏng mối nối, phớt chuyển động) để phân cấp."))
    b.append(p("Sau khi xác định cấp (liên tục, chính, phụ), cần hỏi có thể giảm cấp không "
               "— ví dụ từ chính xuống phụ — với mục tiêu ít nguồn và tổng cấp thấp nhất, "
               "nhưng sản phẩm vẫn phải bán được và hoạt động vẫn khả thi. Không được lạm "
               "dụng lập luận này: các vùng 0 và 1 lớn, không bị giới hạn nói chung là "
               "không chấp nhận được. Người thực hiện phân loại chịu trách nhiệm cá nhân "
               "bên cạnh trách nhiệm của tổ chức. Cách giảm nguồn nguy hiểm gồm dập không "
               "gian hơi bằng khí trơ (từ liên tục xuống phụ, miễn lớp đệm đủ nguyên vẹn; "
               "không ảnh hưởng tới cổng thông khí), dùng đường ống hàn toàn bộ thay "
               "gioăng hoặc mối ren, và pha loãng bằng nhiều không khí tại điểm rò để "
               "hỗn hợp dưới giới hạn nổ dưới (vẫn có vùng rất nhỏ tại chính điểm rò)."))
    b.append(p("Cần định lượng tốc độ phát thải để xác định phạm vi bầu khí quyển nổ. Ở "
               "ngoài trời đạt trạng thái cân bằng khi trộn với không khí, nhưng mục tiêu "
               "chính vẫn là giảm phát thải bằng cải tiến thiết bị chứa. Cải tiến điển "
               "hình: gioăng đỡ xoắn ốc thay gioăng CAF* không được đỡ (loại gioăng cao su "
               "ép truyền thống làm từ sợi amiăng ép); vòng O giữ lại có tác dụng tương tự "
               "nhưng cần xét nứt ngang; và bushing tiết lưu trên phớt quay để hạn chế "
               "lượng thoát khi hỏng bất thường (không áp dụng cho hỏng được coi là vận "
               "hành bình thường, tức nguồn cấp chính). Ngoài thiết bị cố định như ống, "
               "bơm và bình, phải xét cả hoạt động vận chuyển vật liệu, cách chứa và nạp/xả, "
               "cùng các cấu trúc vật lý: một bức tường đặc có thể ngăn bầu khí quyển nổ, "
               "nhưng cánh cửa trên tường đó phải được coi là nguồn nguy hiểm vì thông "
               "sang khu vực bên kia. Không được để bầu khí quyển nổ lan sang cơ sở lân "
               "cận. Hình 2.5 và 2.6 trình bày quy trình dưới dạng sơ đồ."))
    b.append(fig(5, FC.fig_f205()))
    b.append(fig(6, FC.fig_f206()))

    b.append(h3("2.8 Những người tham gia", "2.8 Personnel involved"))
    b.append(p("Quy trình phân loại ảnh hưởng lớn đến thiết kế và tính chấp nhận được của "
               "quy trình, phải là một trong những phần chính của thiết kế; chỉnh sửa sau "
               "khi xây dựng rất tốn kém và có thể đe dọa tính khả thi của dự án. Quy trình "
               "phải bắt đầu càng sớm càng tốt và do một nhóm được thành lập chính thức "
               "gồm: <b>quản lý dự án/quản lý nhà máy</b> chủ trì, bảo đảm thứ bậc và uy "
               "tín; <b>kỹ sư quy trình</b> (thường là kỹ sư hóa học) am hiểu tính chất vật "
               "liệu; <b>kỹ sư cơ khí/máy</b> am hiểu thiết bị chứa và khả năng cải tiến; "
               "<b>cán bộ an toàn</b> tư vấn các khía cạnh an toàn rộng hơn, kể cả độc tính, "
               "và chịu trách nhiệm chung về an toàn tại chỗ; <b>kỹ sư điện/đo lường</b> "
               "tư vấn giới hạn lắp đặt điện trong khu vực phân loại và độ tin cậy của hệ "
               "thống điện, vì chúng ảnh hưởng đến khả năng và mức độ phát thải; và "
               "<b>đại diện khu vực</b> nhận diện đặc thù của địa điểm chọn trong thiết kế."))

    b.append(h3("2.9 Kết quả phân loại và tần suất rà soát",
                "2.9 Results of area classification and frequency of repeats"))
    b.append(p("Nhóm nêu trên phải bắt đầu phân loại ngay trong thiết kế và tinh chỉnh liên "
               "tục đến khi xây dựng xong. Kết quả ghi vào phiếu LEAC và lập thành hồ sơ, "
               "cùng mọi thông tin hỗ trợ cần thiết, chuyển cho những người quản lý vận "
               "hành quy trình. Ngay sau khi đưa vào vận hành, chậm nhất trong vòng một năm, "
               "phải rà soát phân loại theo kinh nghiệm thực tế, sau đó rà soát định kỳ. "
               "Tần suất do kinh nghiệm quyết định nhưng khoảng cách không quá hai năm; nếu "
               "mỗi lần rà soát đều phát hiện thay đổi đáng kể thì rút ngắn chu kỳ, nếu "
               "không có thay đổi thì kéo dài tới giới hạn hai năm. Bất kỳ thay đổi nào về "
               "quy trình hoặc thiết bị tại chỗ đều phải rà soát ngay."))
    b.append(refs(_REFS))
    b.append(note("<b>Đặc điểm của nguyên bản.</b> Chương gồm 21 trang in (22–42; trang in "
                  "= trang PDF − 21), gồm chín mục, một bảng, sáu hình và sáu tài liệu "
                  "tham khảo. Sáu hình được vẽ lại dạng vector: biểu đồ năng lượng đánh lửa, "
                  "ba mẫu biểu trống và hai sơ đồ quy trình. Các giá trị gốc (2 × 10⁵ N/m², "
                  "1000 h/10 h, 10% và 0,1%, 5 mm và 1 mm, 10⁸ Ωm, 4,1/74,2 và 2,1/9,5, "
                  "260 µJ và 20 µJ, một năm và hai năm) được giữ nguyên. Đánh số ghi chú "
                  "của Bảng 2.1 không khớp với nhãn cột trong bản in; giữ nguyên và nêu rõ "
                  "trong chú thích."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung "
               "gốc © 1998 Reed Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Area classification", "Area classification"))
    b.append(lead("Philosophy, objectives and procedures"))
    b.append(p("The basic objective of area classification (be it for gas, vapour, mist or "
               "dust risks) is to identify the possibility of an explosive atmosphere "
               "existing in a given location and, more importantly, to influence the "
               "design of any plant or facility to minimize such risks. To this end, it is "
               "a tool to be used together with the operational requirements in the design "
               "of any plant, process or facility, and the result will invariably be a "
               "compromise between convenience of operation and security against explosion. "
               "This balance must take account of certain situations which are generally "
               "not permissible, such as the continuous presence of an explosive "
               "atmosphere in an unrestricted area, and the limits placed on the "
               "acceptability of any situation where an explosive atmosphere may be "
               "present. This chapter seeks to identify the principles upon which area "
               "classification is based, the part played by those involved in design or "
               "operation, and the procedures needed to identify hazardous areas."))

    b.append(h3("2.1 Basic properties of flammable and combustible materials",
                "2.1 Basic properties of flammable and combustible materials"))
    b.append(p("The materials with which we are concerned are gases, vapour mists and dusts. "
               "Each behaves in a different way and this affects the classification process."))
    b.append(h4("2.1.1 Flammable gases", "2.1.1 Flammable gases"))
    b.append(p("A gas is a material whose normal state at ambient temperatures and pressures "
               "is as a vapour. Such materials cannot be liquefied at ambient temperature "
               "by pressure alone and must also be cooled. They are therefore not likely "
               "to be present as a liquid and, if they are, they will rapidly vaporize once "
               "released. Area classification is a measure of the area contaminated by "
               "their release and is unlikely to be greatly influenced by any residual "
               "effect after the release ceases, provided there is sufficient ventilation "
               "for their removal."))
    b.append(p("The features of primary importance for electrical installations are: "
               "relative density in respect of air, which determines dispersion when no "
               "other influences are present (a gas released at high speed disperses "
               "according to the energy of release rather than wind and density); minimum "
               "ignition energy, the minimum energy released as an arc or spark that will "
               "ignite the most easily ignitable gas/air mixture; maximum experimental safe "
               "gap, which defines the burning characteristics of the ideal gas/air mixture "
               "insofar as its ability to burn through small gaps is concerned; and "
               "ignition temperature, the minimum temperature at which the ideal gas/air "
               "mixture spontaneously ignites."))
    b.append(p("As soon as it is released a gas mixes with air, either by the energy of its "
               "own rapidity of release or by turbulent air movement. Where release is at "
               "low velocity and air movement is small (as in badly ventilated buildings), "
               "mixing is less efficient and the mixture varies from place to place, giving "
               "large and unpredictable hazardous areas."))
    b.append(h4("2.1.2 Flammable vapours", "2.1.2 Flammable vapours"))
    b.append(p("Flammable vapours are very similar to gases in that they are in the vapour "
               "phase; the difference is that they can be liquefied by pressure alone. A "
               "flammable vapour may be only the vapour that exists because of a flammable "
               "liquid: all such liquids have vapour pressures (partial pressures in air) "
               "at temperatures well below their boiling points, and once the percentage "
               "of vapour in air created by that vapour pressure exceeds the lower "
               "explosive limit, an explosive atmosphere can exist even though the release "
               "is a liquid. Persistence after cessation varies significantly: it is low "
               "if released as a vapour or from a liquid whose boiling point is well below "
               "ambient temperature, and high if released from a liquid surface whose "
               "boiling point is above ambient temperature. The criteria and parameters "
               "are as described for gas."))
    b.append(h4("2.1.3 Flammable mists", "2.1.3 Flammable mists"))
    b.append(p("This is an entirely different situation. A mist is created by release at "
               "high pressure (mists have been formed by pressures as low as 2 × 10⁵ N/m² "
               "gauge) in such a way that very fine liquid droplets are produced. Mists can "
               "form explosive atmospheres in mixture with air even if the liquid forming "
               "them is considered not to have sufficient vapour pressure to do so. These "
               "particles recombine to form a liquid much more readily than gas or vapour, "
               "but if very finely divided the mist has a significant existence time and "
               "the particles remain suspended in air for a long period. Much less is "
               "known about mists in air, but they are normally treated in the same way as "
               "gases and vapours for area classification."))
    b.append(h4("2.1.4 Flammable liquids", "2.1.4 Flammable liquids"))
    b.append(p("This is something of a misnomer, as liquid does not burn. A flammable liquid "
               "is one which, at normal ambient temperature and pressure or at the "
               "temperature and pressure at which it is handled or stored, has a vapour "
               "pressure (partial pressure) sufficient to liberate enough vapour to form "
               "an explosive atmosphere."))
    b.append(h4("2.1.5 Combustible dusts", "2.1.5 Combustible dusts"))
    b.append(p("A combustible dust is a dust which will burn when mixed with air or which, "
               "in layer form, will burn if ignited. It should not be confused with an "
               "explosive. Dusts need different treatment from gases, vapours and mists: "
               "although a release is normally in cloud form, once released the dust does "
               "not disperse like a gas/vapour or mist but initially forms a cloud and then "
               "settles as a layer. After release only housekeeping can affect the "
               "persistence of clouds by disturbing layers."))
    b.append(p("The important parameters for dust are: cloud ignition energy, the minimum "
               "energy as an arc or spark required to ignite a dust cloud; cloud ignition "
               "temperature, the minimum temperature at which an ideal suspension of dust "
               "in air will ignite (which can depend on particle size); layer ignition "
               "temperature, the minimum temperature at which a layer of specific thickness "
               "will ignite and burn; and particle size, which affects ignition capability."))

    b.append(h3("2.2 Basis of area classification", "2.2 Basis of area classification"))
    b.append(p("Area classification is based upon situations which can occur in practical "
               "plant and factory operation producing an explosive atmosphere with a "
               "degree of regularity that requires consideration of equipment which may "
               "become an ignition source. It does not seek to address explosions in "
               "catastrophic failure conditions which, by and large, are not easily "
               "predictable. A procedure to deal with catastrophe is nevertheless "
               "necessary, even though it is not part of the area classification process."))
    b.append(p("Three situations can predictably occur. First, an explosive atmosphere is "
               "present for long periods or always as a result of operational necessity: "
               "the interiors of vessels or equipment processing gases, vapours, mists or "
               "dusts with air, the interiors of stock tanks, silos and mills. Second, "
               "explosive atmospheres occur regularly in normal operation: around worn "
               "rotating seals, manual loading points, powder bag loading points and paint "
               "spraying facilities. Third, they occur rarely and normally result from "
               "failure of equipment or procedures: a failed gasket in a process pipe, "
               "overflow of a vessel due to failed process control, or powder-handling "
               "rooms where dust deposits are agitated into clouds."))

    b.append(h3("2.3 General approach to area classification",
                "2.3 General approach to area classification"))
    b.append(p("Modern area classification, unlike its predecessor in BS/CP 1003, is based "
               "on identifying individual sources of hazard and their result. BS/CP 1003 "
               "relied on a general appraisal of areas at risk and identification of the "
               "hazard from that appraisal. This led to variation between organizations, "
               "in some cases to over-classification where entire plants were treated as "
               "high risk, and, more worryingly, to under-classification where inadequately "
               "protected electrical equipment was installed. Older plants classified in "
               "that generalized way therefore need reassessment according to modern "
               "thinking."))
    b.append(p("Identification of sources of hazard is formalized for gases, vapours and "
               "mists in BS 5345 Part 2. Although no such formal identification exists for "
               "dusts in BS 6467 Part 23, the document likely to succeed it (IEC 1241-3) "
               "contains a similar form of identification. Sources of release can therefore "
               "be categorized, be they gas, vapour, mist or dust."))

    b.append(h3("2.4 Classification of sources of release",
                "2.4 Classification of sources of release"))
    b.append(p("<b>Continuous grade of release.</b> A point or location from which "
               "flammable gas, vapour, mist or combustible dust may be released "
               "continuously or for long periods, so that an explosive atmosphere could "
               "be formed during the period of release."))
    b.append(p("<b>Primary grade of release.</b> A point or location from which such "
               "material may be released periodically or occasionally in normal operation, "
               "so that an explosive atmosphere could be formed during the period of "
               "release."))
    b.append(p("<b>Secondary grade of release.</b> A point or location at which such "
               "material is not expected to be released in normal operation but at which "
               "release may be expected infrequently and for short periods, or where dust "
               "layers form to an extent that, if disturbed, an explosive atmosphere would "
               "be formed."))
    b.append(p("These three levels are the basic elements in determining the grade of any "
               "particular source. One company code introduced numerical guidance in 1973: "
               "continuous release present for more than 1000 hours per year (more than "
               "about 10% of the year); primary release present for between 10 and 1000 "
               "hours per year (between about 0.1% and 10%); secondary release present for "
               "less than 10 hours per year (less than 0.1%). The guidance never achieved "
               "sufficient support to be included in any national or international Standard "
               "or Code, but it has been widely used since, and, being intended to help "
               "identify divisions between release types rather than impose strict numerical "
               "boundaries, has become generally accepted if used with care."))
    b.append(p("For example, a rotating seal may, according to plant records, leak once in "
               "say three years and be identified as secondary from that information. But "
               "that may be accidental to those particular circumstances; choose a "
               "different three-year period and releases may be much more frequent. The "
               "general case, which defines such a source as primary, should therefore be "
               "used unless very high confidence exists in the particular situation. Such "
               "cases are expected to be extremely rare and a full justification must be "
               "produced in all of them."))

    b.append(h3("2.5 Hazardous zonal classification", "2.5 Hazardous zonal classification"))
    b.append(p("Having identified the types of release expected, it is possible to identify "
               "the risk of an explosive atmosphere in a given area. This is determined by "
               "the likelihood of release, the nature of the release and the ventilation in "
               "the area of release. Except for releases inside vessels, persistence of "
               "explosive atmospheres depends significantly on the level of ventilation at "
               "the location of release and the dispersion characteristics of the "
               "flammable material."))
    b.append(h4("2.5.1 Gases, vapours and mists", "2.5.1 Gases, vapours and mists"))
    b.append(p("<b>Zone 0</b> is a zone in which an explosive gas, vapour, mist/air mixture "
               "is continuously present or present for long periods. <b>Zone 1</b> is a "
               "zone in which such a mixture is likely to occur in normal operation. "
               "<b>Zone 2</b> is a zone in which it is not likely to occur in normal "
               "operation and, if it occurs, it will only exist for a short time. These "
               "definitions are given in BS 5345 Part 2, with equivalent wording in many "
               "other documents. Many countries have national area classification systems, "
               "historic or current, related to the internationally recognized system "
               "shown in Table 2.1."))
    b.append(table(_T21_HEAD_EN, _T21_ROWS_EN,
                   "Table 2.1 · Relationships between national area classification systems."))
    b.append(p("<small><b>Note 1.</b> Although not specifically naming them, it is clear "
               "that Germany historically operated a three-level risk system; the "
               "IEC/CENELEC/GB system is now used. <b>Note 2.</b> France historically "
               "merged Zones 0 and 1 to form a single Division 1; it now uses the "
               "IEC/CENELEC/GB system. <b>Note 3.</b> The USA historically operated in the "
               "same way as France but has recently begun to use the IEC/CENELEC/GB "
               "three-Zone system. The note numbering in the printed table does not fully "
               "match the column labels; it is retained for comparison.</small>"))
    b.append(h4("2.5.2 Dusts", "2.5.2 Dusts"))
    b.append(p("For dusts the situation is more fluid and the degree of formality is lower; "
               "in the UK it has only been effectively addressed in the last 15–20 years. "
               "<b>Zone Z</b> is a zone in which combustible dust is, or may be, present as "
               "a cloud during normal processing, handling or cleaning in sufficient "
               "quantity to produce an explosible concentration in mixture with air. "
               "<b>Zone Y</b> is an area not classified as Zone Z in which accumulations or "
               "layers of combustible dust may be present under abnormal conditions and "
               "give rise to ignitable dust/air mixtures. These definitions are similar to "
               "BS 6467 Part 23; despite apparent differences from the gas definitions, "
               "allowing for dust behaviour there is an identifiable relationship between "
               "Zone 1 and Zone Z, and between Zone 2 and Zone Y."))
    b.append(p("IEC 1241-3 will replace these with three definitions: <b>Zone 20</b>, where "
               "combustible dust as a cloud is present continuously or frequently in normal "
               "operation, or where layers of uncontrollable and excessive thickness can "
               "form (for example the inside of processing equipment); <b>Zone 21</b>, not "
               "Zone 20, where a dust cloud is likely to occur in normal operation (for "
               "example immediately around powder filling or discharging sites); and "
               "<b>Zone 22</b>, not Zone 21, where a dust cloud can occur infrequently and "
               "persist only briefly, or where dust layers can give rise to an explosive "
               "concentration. Historically the approach in Zones 21 and 22 (Z and Y) has "
               "been to limit dust layers to less than 5 mm, and electrical equipment is "
               "designed assuming a 5 mm layer; IEC 1241-3 also identifies 1 mm as the "
               "layer thickness above which an explosive atmosphere is possible."))
    b.append(h4("2.5.3 Relationship between sources of release and Zones",
                "2.5.3 Relationship between sources of release and Zones"))
    b.append(p("For gases, vapours and mists where ventilation is good, for example outdoors, "
               "a continuous grade of release gives Zone 0, a primary grade gives Zone 1, "
               "and a secondary grade gives Zone 2. This relationship ceases to be true as "
               "soon as any parameter changes: a primary source may give only Zone 2 if "
               "special local ventilation dilutes the release below its explosive "
               "concentration at the point of leakage, while a secondary source may give "
               "Zone 1 if local ventilation is restricted. For dusts the situation is much "
               "more tenuous because layer formation is not really zone specific and "
               "classification depends heavily on housekeeping."))

    b.append(h3("2.6 Collection of information", "2.6 Collection of information"))
    b.append(p("To carry out a formal area classification exercise it is necessary first to "
               "collect information on the flammable material, the methods used to contain "
               "it and the local ventilation conditions."))
    b.append(h4("2.6.1 Information on fuels (gases, vapours and mists)",
                "2.6.1 Information on fuels (gases, vapours and mists)"))
    b.append(p("As a minimum: <b>flashpoint</b>, the temperature at which sufficient vapour "
               "is released from a liquid to allow an explosive atmosphere above its "
               "surface; <b>ignition temperature</b>, the minimum temperature at atmospheric "
               "pressure needed to ignite an ideal mixture, which sets the maximum permitted "
               "equipment temperature; <b>flammable range</b>, the percentage range between "
               "lower and upper explosive limits, the lower limit normally being the "
               "important one because it determines the extent of the explosive atmosphere "
               "(Figure 2.1); <b>gas/vapour density</b> relative to air, affecting "
               "dispersion; <b>boiling point</b>; <b>molecular weight</b>; <b>latent heat of "
               "vaporization</b> and <b>heat capacity</b>, needed for calculation; "
               "<b>sub-group</b> IIA, IIB or IIC (unnecessary for classification but "
               "important for equipment selection); and <b>surface temperature class</b> "
               "T1–T6 based on ignition temperature."))
    b.append(fig(1, FA.fig_f201()))
    b.append(p("Figure 2.2 is a typical blank form used to collect the necessary information."))
    b.append(fig(2, FB.fig_f202()))
    b.append(h4("2.6.2 Information on fuels (dusts)", "2.6.2 Information on fuels (dusts)"))
    b.append(p("For dusts the requirements differ. It is advisable to exclude dust from "
               "equipment which might spark, but both layers of dust on apparatus and dust "
               "clouds may be ignited by temperature; ignition by sparks or arcs is "
               "uncommon because dust is excluded from the interior of apparatus. Important "
               "information is: dust cloud ignition temperature; dust layer ignition "
               "temperature for a 5 mm layer; temperature class; conductivity (a dust with "
               "resistivity less than 10⁸ Ωm is considered conducting); and decomposition "
               "products — whether flammable gases or vapours are produced below the dust's "
               "ignition temperature. Figure 2.3 is a typical blank form for this information."))
    b.append(fig(3, FB.fig_f203()))
    b.append(h4("2.6.3 Information on process conditions",
                "2.6.3 Information on process conditions"))
    b.append(p("Having collected data on the fuel itself, it is necessary to identify how "
               "the fuel is contained and the likelihood of release. Typical examples are "
               "the <b>containment type</b> (for example a pipe flange), the <b>location</b> "
               "on the plant (for example in the tank farm above tank X), the <b>process "
               "material</b> handled, the <b>process conditions</b> of temperature and "
               "pressure at the possible release point (a material may have a flashpoint "
               "above ambient yet ignite if released hot), and the <b>description of "
               "containment</b>, for example the type of gasket. From this the grade of the "
               "possible source and the extent of any hazardous area can be established. A "
               "typical method is a List of Equipment for Area Classification (LEAC) table "
               "as in Figure 2.4, which also records the appropriate group IIA, IIB or IIC "
               "and temperature class T1–T6 and becomes the basic record of the exercise."))
    b.append(fig(4, FB.fig_f204()))

    b.append(h3("2.7 Procedures", "2.7 Procedures"))
    b.append(p("Area classification is not simply intended to identify hazardous areas on "
               "process plants where design has already been completed using only "
               "operational and economic factors; it should be part of the design process "
               "and significantly affect it, eliminating hazardous areas as far as possible "
               "and leaving only those absolutely necessary at an acceptable level of risk. "
               "It should therefore begin as soon as process-line diagrams are available "
               "and be constantly refined throughout design."))
    b.append(p("Ask first whether the quantity of flammable material is small. In places "
               "such as laboratories, security against explosion may be achieved by other "
               "means, such as continuously trained staff and special procedures, but such "
               "cases are few and must be treated with extreme caution. If an alternative "
               "cannot be justified and significant amounts are present, ask whether the "
               "material can be released. If it cannot mix with air, inside a vessel or "
               "externally, an explosive atmosphere cannot form (an exception is an "
               "all-welded pipeline passing through an area). Then determine how release "
               "occurs — from a liquid free surface in contact with air, a pipe joint "
               "failure or a moving seal — so it can be graded."))
    b.append(p("Once the grade (continuous, primary or secondary) is known, ask whether it "
               "can be reduced, for example from primary to secondary, aiming for the "
               "smallest number of sources at the lowest aggregate grade while the product "
               "remains saleable. This flexibility cannot be used to drive a coach and "
               "horses through the guide: large unconfined Zones 0 and 1 are generally "
               "unacceptable whatever the operational justification, and those who carry "
               "out classification bear personal as well as corporate responsibility. "
               "Methods of reducing or removing sources include blanketing a vessel vapour "
               "space with inert gas (reducing the liquid-surface source from continuous to "
               "secondary provided the blanketing has sufficient integrity, though this "
               "does not affect any atmospheric vent), using all-welded pipe instead of "
               "gaskets or screwed connections, and diluting with copious air at the "
               "release point so the mixture is below the lower explosive limit (a very "
               "small explosive volume remains at the actual point of release)."))
    b.append(p("Next quantify the rate of release to determine the amount of explosive "
               "atmosphere formed. Outdoors an equilibrium is reached as the release mixes "
               "with air, but the primary objective is to minimize the release by improved "
               "containment. Typical improvements are spirally supported gaskets instead "
               "of standard CAF* gaskets (the traditional unsupported gasket made from "
               "compressed asbestos fibre), which do not break transversely; retained 'O' "
               "rings, with a similar effect though transverse cracking must be considered; "
               "and throttle bushes on rotating seals to limit release on abnormal failure "
               "(not for failure considered normal operation, i.e. a primary source). "
               "Besides fixed sources such as pipes, pumps and vessels, the exercise must "
               "cover the transport of flammable materials, containment and loading/"
               "discharging methods, and physical structures: a solid wall may be an "
               "effective barrier, but any door in it must be treated as a source of hazard "
               "because it communicates with the area beyond. It is not generally "
               "acceptable to communicate an explosive atmosphere to neighbouring sites. "
               "Figures 2.5 and 2.6 present the procedure in tabular form."))
    b.append(fig(5, FC.fig_f205()))
    b.append(fig(6, FC.fig_f206()))

    b.append(h3("2.8 Personnel involved", "2.8 Personnel involved"))
    b.append(p("Area classification can significantly affect process design and the "
               "acceptability of the process, and must be one of the prime parts of design; "
               "corrections after design and construction can be very expensive and may "
               "challenge the viability of the activity. The procedure should start as soon "
               "as possible after inception and be carried out by a formally constituted "
               "group: the <b>project manager/works manager</b>, who chairs and gives the "
               "necessary seniority and credibility (a delegate must have sufficient "
               "seniority and be seen as their representative); the <b>process engineer</b>, "
               "usually a chemical engineer expert in material performance and chemical "
               "properties; the <b>mechanical/machines engineer</b>, for containment "
               "properties and practical modifications; the <b>safety officer</b>, to advise "
               "on wider safety including toxicity and to accept the results for the site; "
               "the <b>electrical/instrument engineer</b>, to advise on the limitations and "
               "reliability of electrical installations in classified areas, since these "
               "affect the possibility and severity of release; and the <b>site "
               "representative</b>, to identify particular facets of the chosen site."))

    b.append(h3("2.9 Results of area classification and frequency of repeats",
                "2.9 Results of area classification and frequency of repeats"))
    b.append(p("The exercise should begin as early as possible during design and be "
               "continually refined until construction is complete. Results should be "
               "recorded on LEAC sheets and form a dossier, with all necessary supporting "
               "information, accessible to or in the custody of those who manage operation. "
               "As soon as possible after commencement of operation, and certainly within "
               "one year, the classification should be reviewed against practical operating "
               "experience; regular reviews should follow. Frequency is experience-based "
               "but the interval must never exceed two years. If each review produces "
               "significant changes the period should be shortened; if none are found it "
               "may be lengthened up to the two-year limit. Any change in process or "
               "equipment on site should trigger an immediate review."))
    b.append(refs(_REFS))
    b.append(note("<b>Source quirks.</b> The chapter spans 21 printed pages (22–42; "
                  "printed = PDF − 21), with nine sections, one table, six figures and six "
                  "references. The six figures were redrawn as vectors: the ignition-curve "
                  "chart, three blank forms and two flowcharts. Original values are "
                  "retained: 2 × 10⁵ N/m², 1000 h and 10 h, 10% and 0.1%, 5 mm and 1 mm, "
                  "10⁸ Ωm, 4.1/74.2 and 2.1/9.5, 260 µJ and 20 µJ, one year and two years. "
                  "The note numbering of Table 2.1 does not match its column labels in the "
                  "printed source; it is retained and flagged in the caption note."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 1998 Reed Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)
