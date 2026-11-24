# -*- coding: utf-8 -*-
"""Book 7, Chapter 3 — What Valve Type Shall I Choose? (EN/VI bilingual).

Source: Baumann, *Control Valve Primer: A User's Guide*, 5th ed. (ISA / Wiley),
printed pp. 13-19 (PDF pp. 21-27). Three source figures: 3-1 cage-type valve,
3-2 single-seated globe valve with V-port plug, 3-3 rotary control valve.
"""
from cvp_common import (fig, h2, h3, note, p, ul)
import cvpfig as F

PAGES_SRC = 7
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "What Valve Type Shall I Choose?"
TITLE_VI = "Nên chọn loại van nào?"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 3.</b> van kiểu lồng (cage valve) · nút cân bằng áp "
                "(pressure-balanced plug) · dẫn hướng bằng lồng (cage-guided) · vòng đế "
                "(seat ring) · xâm thực (cavitation) · hóa hơi (flashing) · xói mòn "
                "dạng sợi dây (wire drawing) · bộ lót tôi cứng (hardened trim) · van góc "
                "(angle valve) · phục hồi áp suất thấp (low-pressure recovery, "
                "F<sub>L</sub> cao) · tiết lưu hai cấp (dual-stage throttling) · dải điều "
                "tiết (rangeability) · vùng chết (deadband) · bộ định vị (positioner) · "
                "độ hở (backlash) · đoạn dẹt đầu thân (stem tang) · ma sát khởi động "
                "(breakaway friction) · van bướm hiệu năng cao (high-performance "
                "butterfly) · C<sub>v</sub> hệ số lưu lượng · điều khiển điều tiết liên "
                "tục (modulating control).")
    return ("<b>Key terms.</b> cage valve · pressure-balanced plug · cage-guided · seat "
            "ring · cavitation · flashing · wire drawing · hardened trim · angle valve · "
            "low-pressure recovery (high F<sub>L</sub>) · dual-stage throttling · "
            "rangeability · deadband · positioner · backlash · stem tang · breakaway "
            "friction · high-performance butterfly valve · C<sub>v</sub> flow coefficient "
            "· modulating control.")


def body_vi():
    b = []
    b.append(h2("Chọn thân van và kiểu nối đầu",
                "Selecting the valve body and end connections"))
    b.append(p("…thân van. Hãy nhớ rằng bất cứ thứ gì người thợ bảo trì có thể dùng làm "
               "thang đứng thì sẽ được dùng làm thang! Khi dùng thân van bằng kim loại lót "
               "nhựa, phải đảm bảo vỏ bao quanh kín áp và có thêm một lớp bao bình thân dự "
               "phòng cùng kết nối báo rò (telltale) để đề phòng hỏng lớp lót hoặc ống sóp "
               "nhựa. Ống sóp làm bằng tetrafluoroethylene (TFE) — Teflon có vòng đời đặc "
               "biệt ngắn và thấm được clo."))
    b.append(p("Đầu nối của van có thể kiểu ren đối với cỡ 2 in trở xuống khi dùng cho chất "
               "lưu không nguy hiểm, nhưng nên dùng mặt bích khi xử lý hóa chất. Van hơi áp "
               "suất cao thường được hàn vào đường ống, cũng như một số van vô trùng trong "
               "hệ thống chế biến sinh học."))
    b.append(p("Việc để nhà cung cấp van quen thuộc của bạn chọn kiểu van thường cũng được "
               "(điều đó giúp tôi khỏi phải đưa thêm các trang catalog quen thuộc vào cuốn "
               "sách này), nhưng hãy dựa trên các tiêu chí nêu ở đây để ra quyết định cuối "
               "cùng. Khả năng bảo trì và kinh nghiệm đã có với một kiểu van cụ thể luôn là "
               "một yếu tố quan trọng cần cân nhắc."))
    b.append(p("Một trong những điều ngượng ngùng nhất có thể xảy ra là thấy van bạn đã chọn "
               "sáu tháng trước nằm trên đống rác, rồi còn phải nghe những lời nhận xét "
               "chẳng hay ho gì từ người giám sát bảo trì."))

    b.append(h2("Các nguyên nhân thường gặp nhất gây hỏng van sớm",
                "The most common causes of premature valve failure"))
    b.append(p("Xa hơn cả, các nguyên nhân thường gặp nhất gây hỏng van sớm là:"))
    b.append(ul([
        "Hư hỏng do xâm thực (cavitation) (thường là chênh áp lớn với nước);",
        "Xói mòn dạng sợi dây của bộ lót (wire drawing) (xâm thực hoặc hóa hơi của "
        "nước và nước ngưng);",
        "Mài mòn bộ lót (có chất rắn lẫn trong chất lưu);",
        "Rung nút van (dòng chảy không ổn định với chất lỏng);",
        "Ăn mòn (chất lưu ăn mòn);",
        "Rò rỉ bao bình thân quá mức (van hoặc cơ cấu chấp hành có thể đang dao động "
        "liên tục).",
    ]))
    b.append(p("Có thể tránh hư hỏng do xâm thực bằng cách chọn bộ lót phục hồi áp suất "
               "thấp (F<sub>L</sub> cao), lắp thêm một thiết bị tiết lưu thứ cấp, hoặc "
               "chọn vị trí lắp van tốt hơn. Xói mòn dạng sợi dây của bộ lót thường gặp với "
               "hơi ẩm (nước ngưng). Ở đây, thép cacbon của vỏ van có thể bị ăn mòn ngay bên "
               "dưới vòng đế bằng thép không gỉ nếu không có lớp đệm hoặc mối hàn kín. Bài "
               "học: Luôn chỉ định hợp kim crom-molypden hoặc thép không gỉ làm vật liệu "
               "thân van ở những nơi có nước bão hòa hoặc nơi bạn nghi ngờ hơi có thể ngưng "
               "tụ (thực tế là bất kỳ đường ống hơi công nghệ nào bị tắt vào ban đêm hoặc "
               "cuối tuần)."))
    b.append(p("Với vấn đề thứ ba là mài mòn bộ lót, hãy chỉ định bộ lót tôi cứng hoặc dùng "
               "van góc. Theo tôi, chỉ có hai trường hợp nên dùng van góc: (1) nước ngưng "
               "hóa hơi ở đầu vào của bình ngưng và (2) chất lưu gây mài mòn. Trong cả "
               "hai trường hợp, dòng chảy nên hướng theo chiều đóng nút van (hãy kiểm tra "
               "độ ổn định của cơ cấu chấp hành). Với dịch vụ mài mòn, dùng bộ lót thu nhỏ "
               "và một đoạn ống phía sau dài, thẳng (tốt nhất là lớn hơn cỡ yêu cầu) để "
               "tránh hạt va đập vào thành ống bên trong."))
    b.append(p("Rung nút van đôi khi có thể khắc phục bằng cách đảo ngược chiều dòng chảy; "
               "nếu không, hãy tăng đường kính thân nút hoặc giảm khối lượng của nút van. "
               "Ăn mòn có thể được xử lý khi chọn vật liệu với sự trợ giúp của một sổ tay "
               "tốt (xem Chương 13, “Van tôi mua tốt đến mức nào?”). Để biết gợi ý giải "
               "quyết rò rỉ bao bình thân quá mức, xem Chương 24, “Tránh rò rỉ bao bình "
               "thân van”."))

    b.append(h2("Van cầu cỡ lớn và thiết kế kiểu lồng",
                "Larger globe valves and the cage design"))
    b.append(p("Van cầu cỡ lớn có thể có nút cân bằng áp và dẫn hướng bằng lồng. Hình 3-1 là "
               "một ví dụ điển hình về thiết kế van lồng được cải tiến. Van lồng có một số "
               "ưu điểm. Chúng dễ bảo trì hơn vì tháo vòng đế tương đối dễ so với tháo vòng "
               "đế vặn ren trong van cầu một đế, đặc biệt sau nhiều năm sử dụng. Nút "
               "cân bằng áp suất làm giảm đáng kể lực tác dụng lên thân nút và có thể tiết "
               "kiệm khoản tiền đáng kể vì dùng được cơ cấu chấp hành nhỏ hơn."))
    b.append(p("Tuy nhiên, có thể phát sinh một số vấn đề. Thứ nhất, nút dẫn hướng bằng lồng "
               "dễ bị các hạt lẫn trong dòng gây ma sát và kẹt dính. Thứ hai, có thể gặp vấn "
               "đề giãn nở nhiệt của lồng trong dịch vụ nhiệt độ cao, dẫn đến ép vỡ (rò rỉ) "
               "các lớp đệm của lồng. Thứ ba, chi phí của thân van lồng (và trọng lượng của "
               "nó) cao hơn van cầu một đế do các bulông bắt nắp van rất nặng. Cuối "
               "cùng, hầu hết các nút lồng (piston) được làm kín với thành lồng bằng các ghen "
               "piston (bằng kim loại hoặc nhựa), có thể gây ma sát đáng kể trong khi vận "
               "hành và dẫn đến vùng chết. Có thể phải chỉnh lại (de-tune) bộ định vị để "
               "ngăn cơ cấu chấp hành dao động liên tục (mất ổn định của van). Không nên "
               "nhầm lẫn sự mất ổn định của cơ cấu chấp hành này với sự mất ổn định "
               "(hunting) của vòng điều khiển, dù cả hai có thể tác động qua lại."))
    b.append(fig(1, F.fig_f31()))

    b.append(h2("Tiết lưu hai cấp — khắc phục nhược điểm của van lồng",
                "Dual-stage throttling — overcoming the cage valve's drawbacks"))
    b.append(p("Sơ đồ van lồng lý tưởng trong Hình 3-1 cho thấy có thể khắc phục các nhược "
               "điểm cố hữu của van lồng như thế nào. Điểm hấp dẫn nhất là ý tưởng tiết lưu "
               "hai cấp. Ở đây, thay vì nút van có bề mặt định hình thông thường (quyết định "
               "đặc tính lưu lượng của nó), bề mặt định hình này giờ là một phần của thành "
               "lồng trong giãn ra theo phương hướng tâm, nằm ngay phía trên đế van của "
               "van."))
    b.append(p("Khe hở giữa đầu nút van (mũi tên dưới của ký tự A) và thành lồng trong định "
               "hình giờ trở thành cấp tiết lưu thứ nhất. Đồng thời, ta thấy một phần nhô ra "
               "thứ hai của nút (mũi tên trên của ký tự A) bắt đầu để lộ một phần cửa sổ đúc "
               "trên lồng. Khe hở tạo thành vì thế trở thành cấp thứ hai của phần tử tiết lưu "
               "kép này. Chất lưu đi qua đế van van và đầu dưới của nút vào một vùng lõm, "
               "rồi từ đó, bị tiết lưu bởi điểm A phía trên, đi vào các vùng cửa sổ mở và "
               "cuối cùng ra khỏi thân van."))
    b.append(p("Nút van cho phép tiết lưu hai cấp (A trong Hình 3-1) nhằm tăng khả năng "
               "chống xâm thực và dải điều tiết rộng. Ma sát do các phớt trượt gây ra được "
               "tránh bằng cách dùng phớt trên mềm (B), cho phép cân bằng lực và chịu được "
               "sai số gia công cùng giãn nở nhiệt. Một đặc điểm tương tự được dùng để làm "
               "kín nắp van với lồng bằng phớt trên nén dẻo (C). Lồng được vặn ren vào vỏ "
               "(D), loại bỏ các bulông nặng vốn cần thiết để ép hai lớp đệm ở van lồng "
               "thông thường. Cuối cùng, liên kết giữa thân và nút được ép chốt (E) thay vì "
               "dùng chốt hầm, vì chốt hầm có thể bị lỏng [1]."))

    b.append(h2("Van cầu cỡ nhỏ",
                "Smaller globe valves"))
    b.append(p("Van cầu cỡ nhỏ thường có thiết kế một đế như Hình 3-2. Chúng đơn giản "
               "hơn nhiều và có thể dùng cơ cấu chấp hành nhỏ hơn vì lực trên thân nút thấp "
               "do lỗ tiết lưu nhỏ hơn và áp suất nói chung thấp hơn. Điều này cũng cho phép "
               "đường kính thân nút nhỏ hơn và ma sát bao bình thấp hơn (vùng chết nhỏ hơn). "
               "Nhiều van trong số này có thể làm việc không cần bộ định vị nếu dùng tín "
               "hiệu khí nén 3 đến 15 psi."))
    b.append(fig(2, F.fig_f32()))

    b.append(h2("Van điều khiển quay",
                "Rotary control valves"))
    b.append(p("Van điều khiển quay chia thành hai nhóm lớn:"))
    b.append(ul([
        "1. Những van được thiết kế riêng cho điều khiển điều tiết liên tục",
        "2. Van đóng/mở được cải tạo bằng cách lắp thêm cơ cấu chấp hành và bộ định vị "
        "(còn gọi là van tự động hóa)",
    ]))
    b.append(p("Van thuộc nhóm thứ nhất có nhiều đặc điểm thường thấy ở van cầu, chẳng hạn "
               "bao bình thân có thể chỉnh, tùy chọn bộ lót bọc cứng, nắp van kéo dài, và "
               "quan trọng nhất là liên kết không hở giữa “cơ cấu đóng” quay và thân cơ cấu "
               "chấp hành. Một số kiểu tinh vi hơn còn có giảm áp hai cấp ở hành trình thấp, "
               "cũng như các chi tiết chống xâm thực, giảm ồn có thể lắp tại hiện trường "
               "(xem Hình 3-3)."))
    b.append(fig(3, F.fig_f33()))
    b.append(p("Nhóm thứ hai, dù thừa nhận là rẻ hơn, có thể gây rủi ro. Ở đây, mối lo chính "
               "nên là độ hở hoặc khe đệm giữa"))
    b.append(ul([
        "quả bóng (trường hợp van bi) và đoạn dẹt ở đầu thân van<sup>1</sup>;",
        "thân van và đoạn dẹt ở đầu thân cơ cấu chấp hành; và",
        "liên kết phản hồi của bộ định vị và đoạn dẹt ở đầu thân cơ cấu chấp hành.",
    ]))
    b.append(note("<sup>1</sup> Đoạn được dẹt phẳng ở đầu của thân van."))
    b.append(p("Dưới đây là một ví dụ minh họa các vấn đề nêu trên: Giả sử van có đường kính "
               "thân 1 inch và khe hở đoạn dẹt 0,015 inch, một phép tính đơn giản sẽ cho "
               "thấy cơ cấu chấp hành phải di chuyển 2,5° hay 2,8% của hành trình 90° trước "
               "khi quả bóng bắt đầu chuyển theo hướng ngược lại. Điều này chấp nhận được "
               "trong một số ứng dụng, nhưng không cho điều khiển yêu cầu cao."))
    b.append(p("Một vấn đề đáng lưu ý khác là ma sát “khởi động” (breakaway) ở một số van bi "
               "hoặc van bướm. Đây là lực cần để thắng ma sát tĩnh của quả bóng hoặc đĩa van "
               "nhằm mở van — một vấn đề đặc biệt khó chịu ở cái gọi là van bướm hiệu năng "
               "cao. Khi khởi động, cơ cấu chấp hành có thể được nạp áp suất khí đến mức van "
               "gần như bật mở hoàn toàn (sau khi thoát khỏi bệ van) trước khi bộ định vị "
               "kịp đưa van về vị trí mong muốn."))
    b.append(p("Một quy tắc nên nhớ là giới hạn hành trình làm việc bình thường của van bi "
               "và van bướm hiệu năng cao ở mức 15% độ mở tối đa, tức là đảm bảo lưu lượng "
               "của bạn không đòi hỏi C<sub>v</sub> (hệ số lưu lượng) thấp hơn giá trị ứng "
               "với độ mở 15%."))

    b.append(h2("Tiêu chí lựa chọn van: Tóm tắt",
                "Criteria for Valve Selection: A Summary"))
    b.append(h3("Khả năng điều khiển tốt (Hiệu năng)",
                "Ability to Control Well (Performance)"))
    b.append(ul([
        "Van đã được định cỡ đúng chưa?",
        "Van có vùng chết thấp không (đôi khi bị nhầm với độ trễ hysteresis)?",
        "Van có làm việc được không cần bộ định vị không (cũng là yếu tố chi phí)? Có dải "
        "điều tiết đầy đủ không?",
        "Đặc tính lưu lượng có chấp nhận được không (độ khuếch đại lắp đặt)?",
        "Hiệu năng động của van thế nào (đáp ứng tần số, hằng số thời gian)?",
    ]))
    b.append(h3("Lắp đặt và ảnh hưởng đến môi trường",
                "Installation and Effects on the Environment"))
    b.append(ul([
        "Kích thước mặt bích đến mặt bích có cho phép thay bằng van của hãng khác không? "
        "Van nặng bao nhiêu? Có cần giá đỡ đường ống không? Van có quá cao không?",
        "Van có đóng kín không (nếu yêu cầu)?",
        "Van có gây ồn trong điều kiện dòng chảy đã cho không? Rò rỉ bao bình có gây nguy "
        "hiểm không?",
        "Áp suất khí có đủ không (trường hợp cơ cấu chấp hành xi lanh)? Van có chịu được "
        "tác động ăn mòn của chất lưu và môi trường không? Van có bị xâm thực trong điều "
        "kiện dòng chảy đã cho không?",
        "Nếu lắp ngoài trời, van và bộ định vị có chịu được điều kiện thời tiết khắc "
        "nghiệt không?",
    ]))
    b.append(h3("Khả năng bảo trì và kiểm soát chi phí dài hạn",
                "Maintainability and Long-Term Cost Control"))
    b.append(ul([
        "Van có dễ sửa chữa không?",
        "Chi phí phụ tùng thay thế thế nào?",
        "Bộ định vị có xử lý được khí bẩn không (nếu áp dụng)? Có chịu được môi trường rung "
        "động không? Cơ cấu chấp hành được bảo vệ khỏi ăn mòn như thế nào?",
        "Bao bình thân có thay được tại hiện trường không? Có phải xả van không?",
        "Bộ định vị có khả năng chẩn đoán van không?",
    ]))
    b.append(p("Chỉ sau khi xem xét các tiêu chí này và quyết định kiểu van phù hợp, người ta "
               "mới nên đưa vấn đề chi phí vào bàn cân."))

    b.append(note("Bản trích nguồn bắt đầu giữa câu ở tr. in 14 và kết thúc ở tr. in 20, với "
                  "tiêu đề chạy trang xen kẽ giữa tên chương và tên sách. Một vài từ bị gạch "
                  "nối khi xuống dòng (“rela-tively”, “bolt-ing”, “disad - vantages”); mục "
                  "“Corrosion(corrosive fluids)” thiếu dấu cách; trích dẫn số [1] được giữ "
                  "nguyên như in, nhưng danh mục tham khảo không nằm trong phần trích này. "
                  "Bản dịch tiếng Việt hiệu theo nghĩa đúng."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 3 chiếm tr. in 13–19 của ấn bản in (PDF tr. 21–27). Nguyên bản có ba "
               "hình: Hình 3-1 van kiểu lồng, Hình 3-2 van cầu một đế với nút cổng chữ "
               "V và Hình 3-3 van quay với chi tiết giảm ồn thay được tại hiện trường. Cả ba "
               "được vẽ lại dạng vector trong bản dịch này."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Selecting the valve body and end connections",
                "Chọn thân van và kiểu nối đầu"))
    b.append(p("bodies. Remember, anything that can be used by a maintenance person as a "
               "stepladder will be used as such! When using a plastic-lined metal valve body, "
               "make sure the surrounding housing is pressure-tight and that a secondary stem "
               "packing and telltale connection are provided to protect against liner or "
               "plastic bellows failure. Bellows made of tetrafluoroethylene (TFE) — Teflon "
               "have particularly limited life cycles and are permeable to chlorine."))
    b.append(p("Valve end connections may be threaded in sizes 2 in and below for "
               "nonhazardous fluids but should be flanged for the handling of chemicals. "
               "High-pressure steam valves usually are welded into the pipe, as are some "
               "aseptic valves in bioprocessing systems."))
    b.append(p("While it is usually OK to have your favorite valve vendor select the valve "
               "type (which saves me from adding all the usual catalog pages to this volume), "
               "base your final judgment on the criteria mentioned here. The maintenance and "
               "past experience of a given type of valve is always an important "
               "consideration."))
    b.append(p("One of the most embarrassing things that can happen is seeing a valve you "
               "chose six months earlier on the trash heap and then listening to "
               "unflattering remarks made by the maintenance supervisor."))

    b.append(h2("The most common causes of premature valve failure",
                "Các nguyên nhân thường gặp nhất gây hỏng van sớm"))
    b.append(p("By far, the most often encountered causes of premature valve failures are:"))
    b.append(ul([
        "Cavitation damage (usually high-pressure drop with water);",
        "Wire drawing of trim (cavitation or flashing of water, condensate);",
        "Erosion of trim (embedded solids in fluid);",
        "Plug vibration (unstable flow pattern with liquids);",
        "Corrosion(corrosive fluids);",
        "Excessive stem packing leakage (valve/actuator may be cycling).",
    ]))
    b.append(p("Cavitation damage can be avoided by selecting a low-pressure recovery trim "
               "(high F<sub>L</sub>), by installing a secondary flow restrictor, or by "
               "choosing a better valve location. Wire drawing of trim is usually encountered "
               "with wet steam (condensate). Here the carbon steel of valve housings can get "
               "eaten away underneath the stainless-steel seat ring if there is no gasket or "
               "weld seal. The moral: Always specify chrome-molybdenum alloy or stainless "
               "steel as the body material where saturated water is encountered or where you "
               "suspect steam may condense (practically any process steam line that gets shut "
               "down at night or on weekends)."))
    b.append(p("For the third problem, erosion of trim, specify hardened trim or use angle "
               "valves. There are, in my book, only two cases when you should use an angle "
               "valve: (1) for flashing condensate at the inlet of a condenser and (2) for "
               "erosive fluids. In both cases, the flow should be in the direction to close "
               "the plug (check the actuator for stability). For erosive service, use a "
               "reduced trim and a long, straight, (ideally) oversized downstream pipe to "
               "avoid particle impingement on the pipe interior."))
    b.append(p("Plug vibration can sometimes be cured by reversing the flow direction; "
               "otherwise, increase the stem diameter or reduce the weight (mass) of the "
               "valve plug. Corrosion can be dealt with when selecting materials with the aid "
               "of a good handbook (see Chapter 13, “How Good Is the Valve I Purchased?”). "
               "For hints on solving the problem of excessive stem packing leakage, see "
               "Chapter 24, “Avoiding Leaky Valve Stem Packing.”"))

    b.append(h2("Larger globe valves and the cage design",
                "Van cầu cỡ lớn và thiết kế kiểu lồng"))
    b.append(p("Larger globe valves may have a pressure-balanced plug and could be "
               "cage-guided. Figure 3-1 is a typical example of an improved cage valve "
               "design. Cage valves have several advantages. They are easier to maintain "
               "because removal of a seat ring is relatively easy compared to removal of a "
               "threaded seat ring in a single-seated globe valve, especially after years of "
               "service. Pressure-balanced plugs greatly reduce the stem forces and can save "
               "considerable amounts of money because smaller actuators can be used."))
    b.append(p("However, some problems can arise. First, cage-guided plugs are susceptible "
               "to entrained particles leading to friction and stickiness. Second, there can "
               "be a problem with thermal expansion of the cage on high-temperature service "
               "that could result in crushing (leakage) of the cage gaskets. Third, the cost "
               "of a cage valve body (and its weight) is higher than that of a single-seated "
               "globe valve due to the heavy bonnet bolting. Finally, most cage plugs "
               "(pistons) are sealed against the gauge bore using piston rings (either metal "
               "or plastics), which can cause considerable friction during operation and "
               "lead to deadbands. The positioner may have to be de-tuned to prevent cycling "
               "of the actuator (valve instability). Such valve actuator instability should "
               "not be confused with instability (hunting) of the control loop, although "
               "both may interact."))
    b.append(fig(1, F.fig_f31()))

    b.append(h2("Dual-stage throttling — overcoming the cage valve's drawbacks",
                "Tiết lưu hai cấp — khắc phục nhược điểm của van lồng"))
    b.append(p("The diagram of an idealized cage valve in Figure 3-1 shows how the inherent "
               "disadvantages of cage valves can be overcome. Most intriguing is the concept "
               "of dual-stage throttling. Here, instead of the plug having a conventional "
               "contoured surface (which determines its flow characteristic), the contoured "
               "surface is now part of a radially expanding inner cage wall, located just "
               "above the valve seat."))
    b.append(p("The clearance between the tip of the plug (lower arrow of letter A) and the "
               "contoured inner cage wall now becomes the first throttling stage. At the same "
               "time, we see that a second protrusion of the plug (upper arrow of letter A) "
               "starts to expose a portion of a window cast into the cage. The resultant "
               "opening thus becomes the second stage of this dual throttling element. Fluid "
               "will pass past the valve seat and lower tip of the plug into a concave "
               "indentation, and from there, restricted by upper point A, into the open "
               "window areas and finally exiting the valve body."))
    b.append(p("The valve plug allows for double-stage throttling (A in Figure 3-1) for "
               "increased cavitation resistance and high rangeability. Friction that causes "
               "sliding seals is avoided by using a flexible top seal (B) allowing for "
               "balanced forces and for enduring machining tolerances and thermal expansion. "
               "A similar feature is used to seal the bonnet against the cage by using a "
               "compressible top seal (C). The cage is screwed into the housing (D) "
               "eliminating the heavy bolting required to compress two gaskets on "
               "conventional cage valves. Finally, the stem connection to the plug is staked "
               "(E) instead of using a pin, which may become loose [1]."))

    b.append(h2("Smaller globe valves", "Van cầu cỡ nhỏ"))
    b.append(p("Smaller globe valves usually feature single-seated designs as shown in "
               "Figure 3-2. These are much simpler and can use smaller actuators because of "
               "low stem forces due to smaller orifices and generally lower pressures. This "
               "also allows for smaller stem diameters and lower packing friction (less "
               "deadband). Many of these valves can operate without a positioner if operated "
               "using a 3 to 15 psi pneumatic signal."))
    b.append(fig(2, F.fig_f32()))

    b.append(h2("Rotary control valves", "Van điều khiển quay"))
    b.append(p("Rotary control valves fall into two broad categories:"))
    b.append(ul([
        "1. Those designed exclusively for modulating control",
        "2. On-off valves modified by the addition of an actuator and positioner (also "
        "called automated valves)",
    ]))
    b.append(p("Valves in the first category have many features commonly seen in globe "
               "valves, such as adjustable stem packing, the option of a hard-faced trim, "
               "extension bonnets, and, most important, a backlash-free connection between "
               "the rotating “closure member” and the actuator stem. Some more refined types "
               "even have two-stage pressure reduction at low travel, as well as "
               "field-attachable, low-noise, anticavitation inserts (see Figure 3-3)."))
    b.append(fig(3, F.fig_f33()))
    b.append(p("The second category, while admittedly less expensive, can be perilous. Here "
               "the main concern should be the backlash or play between"))
    b.append(ul([
        "the ball (in case of a ball valve) and the valve stem tang<sup>1</sup>;",
        "the valve stem and the actuator stem tang; and",
        "the positioner feedback connection and the actuator stem tang.",
    ]))
    b.append(note("<sup>1</sup> The flattened portion at the end of a valve stem."))
    b.append(p("Here is an example to illustrate the abovementioned problems: Assuming the "
               "valve has a 1-inch stem diameter and 0.015-inch tang clearance, a little "
               "mathematics will prove that the actuator will have to move 2.5° or 2.8% of "
               "90° travel before the ball will move in the opposite direction. This is "
               "acceptable in some applications, but not for critical control."))
    b.append(p("Another area of concern is “breakaway” friction with some ball or butterfly "
               "valves. This is overcoming the static friction of the ball or disk in order "
               "to open the valve, a problem especially irksome on so-called high-performance "
               "butterfly valves. On start-up, the actuator might be so charged up with air "
               "pressure that the valve may fly almost wide open (after breaking out of the "
               "seat) before the positioner can move the valve back to the desired position."))
    b.append(p("A good rule to remember is to limit the normal valve travel of the ball and "
               "high-performance butterfly valves to 15% of the maximum opening, that is, "
               "make sure your flow rate does not require a C<sub>v</sub> (flow coefficient) "
               "that is less than that given for a 15% opening."))

    b.append(h2("Criteria for Valve Selection: A Summary",
                "Tiêu chí lựa chọn van: Tóm tắt"))
    b.append(h3("Ability to Control Well (Performance)",
                "Khả năng điều khiển tốt (Hiệu năng)"))
    b.append(ul([
        "Is the valve sized properly?",
        "Does the valve have low deadband, sometimes confused with hysteresis?",
        "Will it be able to operate without a positioner (also a cost factor)? Does it have "
        "adequate rangeability?",
        "Is the flow characteristic acceptable (installed gain)?",
        "How is its dynamic performance (frequency response, time constant)?",
    ]))
    b.append(h3("Installation and Effects on the Environment",
                "Lắp đặt và ảnh hưởng đến môi trường"))
    b.append(ul([
        "Is the face-to-face such that it can be replaced with another make? How heavy is "
        "it? Are pipe supports needed? Is it too tall?",
        "Does it shut off tightly (if required)?",
        "Is it going to be noisy under the given flow conditions? Would packing leakage "
        "produce a hazard?",
        "Is there adequate air pressure (in case of cylinder actuators)? Can it withstand "
        "the corrosive effects of fluid and the environment? Would the valve be cavitating "
        "under the given flow conditions?",
        "If outdoors, can the valve and positioner stand extreme weather conditions?",
    ]))
    b.append(h3("Maintainability and Long-Term Cost Control",
                "Khả năng bảo trì và kiểm soát chi phí dài hạn"))
    b.append(ul([
        "Is it easy to repair?",
        "What are the costs of spare parts?",
        "Can the positioner handle dirty air (if applicable)? Can the positioner tolerate a "
        "vibrating environment? How is the actuator protected from corrosion?",
        "Is the stem packing field-replaceable? Must the valve be drained?",
        "Is the positioner able to diagnose the valve?",
    ]))
    b.append(p("Only after reviewing these criteria and deciding on the proper valve type "
               "should the subject of cost be considered."))

    b.append(note("The extracted source begins mid-sentence on printed p. 14 and ends on "
                  "printed p. 20, with running heads alternating between the chapter title "
                  "and the book title. A few words are hyphenated at line breaks "
                  "(“rela-tively”, “bolt-ing”, “disad - vantages”); one bullet reads "
                  "“Corrosion(corrosive fluids)” without a space; the numbered citation [1] "
                  "is retained as printed, but its reference list is not part of this "
                  "extract. The translation follows the intended meaning."))
    b.append(h3("About the source", "Về nguồn tài liệu"))
    b.append(p("Chapter 3 occupies printed pp. 13-19 (PDF pp. 21-27). The source has three "
               "figures: Figure 3-1 the cage-type valve, Figure 3-2 the single-seated globe "
               "valve with V-port plug, and Figure 3-3 the rotary valve with a "
               "field-replaceable low-noise insert. All three are redrawn as vectors here."))
    return "".join(b)
