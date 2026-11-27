# -*- coding: utf-8 -*-
"""Chapter 8, module F - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998). This module finishes printed p.205 and covers
printed pp.206-207 (PDF pp.226-228): the closing items of section 8.1.8
(marking requirements), Figures 8.8 and 8.9, and the 'Additional marking'
paragraph. It owns Figures 8.8-8.9, supplied by mcmillanfig08.

The chapter h2, the 19 printed references and the end matter belong to the
integration shell and are not emitted here.
"""
from mcmillan_common import h2, h3, h4, p, note, table, fig
import mcmillanfig08 as F


def body_vi():
    b = []
    b.append(p("II: Ký hiệu này cho biết thiết bị thuộc Nhóm II dùng trong công "
               "nghiệp mặt đất. (Thiết bị dùng trong hầm mỏ than thuộc Nhóm I.) "
               "Khi thiết bị công nghiệp mặt đất được chia thành các phân nhóm "
               "— thường vì thiết bị có bản chất an toàn nội tại hoặc có vỏ "
               "bọc chống nổ — và tính năng của nó khác nhau đối với các khí "
               "khác nhau về mặt bắt lửa do tia lửa hoặc truyền ngọn lửa, các "
               "ký hiệu sẽ là 'IIA', 'IIB' hoặc 'IIC'. (Nếu chỉ có Nhóm II thì "
               "thiết bị phù hợp với mọi khí, hơi và sương mù chất lỏng thuộc "
               "Nhóm II. Trong một số trường hợp, thiết bị có thể chỉ được "
               "dùng cho một loại khí hoặc hơi cụ thể; khi đó không dùng ký "
               "hiệu nhóm hay phân nhóm mà thay bằng công thức hóa học của khí "
               "hoặc hơi đang xét (ví dụ, NH3)."))
    b.append(p("T: Ký hiệu T1 đến T6 được ghi để thể hiện cấp nhiệt độ của "
               "thiết bị. Trong trường hợp ngoại lệ, nếu thiết bị có nhiệt độ "
               "bề mặt tối đa thấp hơn mức tối đa của một cấp nhất định, thiết "
               "bị có thể được ghi, ví dụ, 35 °C (T1). Nếu nhiệt độ tối đa mà "
               "thiết bị đạt được lớn hơn giới hạn của cấp T1 (>450 °C), thì "
               "không ghi giới hạn cấp nào mà chỉ ghi nhiệt độ tối đa thực tế "
               "đạt được (ví dụ, 600 °C). Khi thiết bị được ghi nhãn chỉ để "
               "dùng với một loại khí hoặc hơi cụ thể như nêu trên, sẽ không "
               "xuất hiện ký hiệu phân loại nhiệt độ nào."))
    b.append(note("<b>Lưu ý về giới hạn T1 trong bản in.</b> Lớp văn bản PDF "
                  "in '1450 °C' cho giới hạn cấp T1; trang in cho thấy '>450 "
                  "°C' và bảng liên quan cho giá trị 450 °C. Bản dịch tiếng "
                  "Anh giữ nguyên '1450 °C' theo bản in và ghi chú tại đây, "
                  "không sửa lặng lẽ; bản dịch tiếng Việt dùng giá trị theo ý "
                  "định là lớn hơn 450 °C."))
    b.append(p("Ti: Khi sử dụng dải nhiệt độ môi trường khác với −20 °C đến "
               "+40 °C, có thể xuất hiện ký hiệu 'Ta' hoặc 'Tamb' kèm theo dải "
               "nhiệt độ môi trường thực tế, ví dụ, Ta(−30 °C đến +55 °C)."))
    b.append(p("X: Ký hiệu 'X' xuất hiện khi cần có điều kiện đặc biệt để sử "
               "dụng an toàn thiết bị mà các điều kiện đó không thể thể hiện "
               "hiệu quả trên nhãn của thiết bị. Ký hiệu này không xuất hiện "
               "cùng với mã chứng nhận (ví dụ, EEx q II T4), mà đặt sau số "
               "chứng nhận hoặc mã tham chiếu của tổ chức thử nghiệm (ví dụ, "
               "BAS 92 3054X)."))
    b.append(p("U: Ký hiệu này xác định rằng thiết bị đang xét là một bộ phận "
               "Ex và không thể tự thân được dùng trong khí quyển nổ. Các bộ "
               "phận cũng thường không được ghi cấp nhiệt độ, vì cấp này do "
               "cách sử dụng cuối cùng của nó quyết định. Ngoài ra, thông "
               "thường không cho ký hiệu 'X' xuất hiện trên một bộ phận, vì "
               "ký hiệu này liên quan đến sử dụng an toàn và bộ phận không "
               "thể được dùng khi chưa có chứng nhận hoặc thử nghiệm thêm, "
               "nên điều đó là không phù hợp. Các ví dụ điển hình về ghi nhãn "
               "thiết bị được cho trong Hình 8.8 và 8.9."))

    # --- Figures 8.8-8.9, in printed source order -------------------------
    b.append(fig(8, F.fig_f808()))
    b.append(fig(9, F.fig_f809()))

    b.append(h4("Ghi nhãn bổ sung", "Additional marking"))
    b.append(p("Trong một số trường hợp, chẳng hạn như cấp áp 'p', cần cung "
               "cấp thông tin bổ sung, ví dụ tốc độ và thời gian thổi sạch cần "
               "thiết để bảo đảm người sử dụng biết các thiết lập phải áp dụng "
               "cho thiết bị điều khiển. Khi có thể, thông tin này nên được "
               "ghi trên chính thiết bị, nhưng nếu không thể thì phải được "
               "viện dẫn trong tài liệu chứng nhận/phê duyệt. Tiêu chuẩn riêng "
               "cho từng khái niệm bảo vệ xác định cách cung cấp thông tin đó "
               "và cách cần làm cho người sử dụng biết đến thông tin này. Trong "
               "một số trường hợp, phải đáp ứng các yêu cầu lắp đặt bất thường "
               "cụ thể. Những yêu cầu này phải được ghi trên thiết bị hoặc, nếu "
               "không thể, thiết bị phải được ghi ký hiệu 'X' và các điều kiện "
               "đó được viện dẫn trong tài liệu chứng nhận/phê duyệt."))
    return "".join(b)


def body_en():
    b = []
    b.append(p("II: this shows the apparatus is Group II for surface industry. "
               "(Equipment for coal mining use is Group I.) Where surface "
               "industry apparatus is sub-grouped, typically because it is "
               "intrinsically safe or flameproof, and its performance is "
               "different with different gases from the spark ignition or "
               "flame transmission point of view, the symbols will be 'IIA', "
               "'IIB' or 'IIC'. (If only Group II is present the apparatus is "
               "suitable for all Group II gases, vapours and mists. In some "
               "cases the apparatus may be intended for a specific gas or "
               "vapour only, and in these cases the group or sub-group marking "
               "is not used being replaced by the chemical formula of the gas "
               "or vapour in question (e.g., NH3)."))
    b.append(p("T: T1 to T6 is marked to show the temperature classification of "
               "the apparatus. Exceptionally, if the apparatus has a maximum "
               "surface temperature less than a particular class maximum, it "
               "may be marked, for example 35 °C (T1). If the maximum "
               "temperature reached by the equipment is greater than the T1 "
               "class limit (1450 °C), then no class limit is shown and the "
               "equipment is marked only with the actual maximum temperature "
               "reached (e.g. 600 °C). Where the apparatus is marked for use "
               "with one particular gas or vapour only, as above, no "
               "temperature classification marking will appear."))
    b.append(note("<b>Note on the printed T1 limit.</b> The PDF text layer "
                  "prints '1450 °C' as the T1 class limit; the printed page "
                  "shows '>450 °C' and the related table gives 450 °C. The "
                  "printed '1450 °C' is retained verbatim above and flagged "
                  "here rather than silently corrected."))
    b.append(p("Ti: Where an ambient temperature range, other than −20 °C to "
               "+40 °C is used the symbol 'Ta' or 'Tamb' may appear, together "
               "with the actual ambient temperature range, for example, "
               "Ta(−30 °C to +55 °C)"))
    b.append(p("X: The symbol 'X' appears when there are special conditions "
               "necessary for the safe use of the apparatus and these cannot "
               "be identified effectively on the apparatus label. This symbol "
               "does not appear with the certification code marking (e.g., "
               "EEx q II T4) but as after the certificate number or test house "
               "reference (e.g., BAS 92 3054X)"))
    b.append(p("U: This identifies the fact that the equipment in question is "
               "an Ex component and cannot alone be used in an explosive "
               "atmosphere. Components are also not normally marked with a "
               "temperature class as this is determined by its ultimate use. "
               "In addition, it is not normal for an 'X' mark to appear on a "
               "component as this is concerned with safe use, and as the "
               "component cannot be used without further certification or "
               "testing it is not appropriate. Typical examples of apparatus "
               "marking are given in Fig. 8.8 and 8.9."))

    # --- Figures 8.8-8.9, in printed source order -------------------------
    b.append(fig(8, F.fig_f808()))
    b.append(fig(9, F.fig_f809()))

    b.append(h4("Additional marking", "Additional marking"))
    b.append(p("In some cases, such as pressurization 'p' it is necessary to "
               "provide additional information, such as the purge rate and "
               "time necessary to ensure that the user is aware of the "
               "settings which must be applied to the control apparatus. Where "
               "possible, this should be marked on the apparatus but if it is "
               "not possible, then it must be referred to in the "
               "certification/approval documentation. The individual "
               "protection concept standard identifies how this information "
               "should be provided and how any user needs to be made aware of "
               "it. In some cases, specific unusual installation requirements "
               "must be met. These must be marked on the apparatus or, if this "
               "is not possible, the apparatus must be marked with an 'X' and "
               "these conditions referred to in the certification/approval "
               "documentation."))
    return "".join(b)
