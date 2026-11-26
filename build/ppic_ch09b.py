# -*- coding: utf-8 -*-
"""Book 9, Chapter 9 (part B) - PREDICTIVE MAINTENANCE and the coal-grinding
subsystem (EN/VI bilingual).

Source: Kisic, Durovic and Petrovic, in L. N. Jalali (ed.), *Handbook on Power
Plant Instrumentation and Control* (Bibliotex, 2019), PDF pp. 217-223, printed
pp. 201-207 (absolute lines 5565-5745 of work/ppic_raw.txt). Figures 1 and 2
are embedded as 9.1 and 9.2; their captions and descriptions come from the
figure supplier. Printed bracketed citations [3]-[22] are kept inline; the
reference list itself is emitted by part E.
"""
import ppicfig9 as F
from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401


def _stub(n, cap_vi, cap_en, desc_vi, desc_en):
    """Minimal inert five-tuple, used only while the supplier is unfinished."""
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 300" '
           'role="img" aria-label="Figure 9.%d">'
           '<rect x="8" y="8" width="664" height="284" fill="none" '
           'stroke="#888888"/>'
           '<text x="340" y="150" text-anchor="middle" font-size="14">'
           'Figure 9.%d</text></svg>') % (n, n)
    return (svg, cap_vi, cap_en, desc_vi, desc_en)


if not hasattr(F, "fig_f01"):
    F.fig_f01 = lambda: _stub(1, "Hình 9.1 · Cấu hình hệ thống nghiền than",
                              "Figure 9.1 · Coal-grinding subsystem layout",
                              "Sơ đồ cấu hình hệ thống nghiền than.",
                              "Layout of the coal-grinding subsystem.")
if not hasattr(F, "fig_f02"):
    F.fig_f02 = lambda: _stub(2, "Hình 9.2 · Bàn nghiền mới và bàn nghiền đã mòn",
                              "Figure 9.2 · New grinding table and worn grinding table",
                              "Bàn nghiền mới (trái) và bàn nghiền đã mòn (phải).",
                              "A new grinding table (left) and a worn grinding table (right).")


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 9."""
    b = []

    # ------------------------------------------------------- PREDICTIVE MAINTENANCE
    H(b, lang, "BẢO TRÌ DỰ BÁO", "PREDICTIVE MAINTENANCE", level=2)
    P(b, lang,
      "Ngày nay, các quá trình công nghiệp rất phức tạp và không thể tưởng tượng "
      "được nếu thiếu công nghệ hiện đại, vì vậy cần có các chiến lược bảo trì tinh "
      "vi và rất tốn kém. Hậu quả của bảo trì kém hiệu quả là những tổn thất vật "
      "chất lớn; do đó cần liên tục phát triển và cải tiến các chương trình bảo "
      "trì hiện có.",
      "Nowadays, industrial processes are very complex and cannot be imagined "
      "without modern technologies, so highly sophisticated and very expensive "
      "maintenance strategies are needed. Consequences of inefficient maintenance "
      "are large material losses, and because of that it is necessary to constantly "
      "develop and improve the existing maintenance programmes.")
    P(b, lang,
      "Các chiến lược bảo trì đã phát triển qua thời gian. Chiến lược đầu tiên là "
      "bảo trì không theo kế hoạch, hay bảo trì theo kiểu chạy đến khi hỏng, nghĩa "
      "là chờ cho sự cố xảy ra. Rõ ràng với chiến lược này các hỏng hóc thảm khốc "
      "là không thể tránh khỏi, nên rất hiếm khi kiểu bảo trì này bền vững và có "
      "lợi nhuận. Sau đó, bảo trì phòng ngừa được đưa vào. Bảo trì phòng ngừa có "
      "thể thực hiện như bảo trì theo kế hoạch hoặc bảo trì theo thời gian, được "
      "triển khai tại các khoảng thời gian cố định, hoặc có thể thực hiện như bảo "
      "trì dự báo hay bảo trì theo tình trạng, trong đó hoạt động bảo trì được "
      "thực hiện dựa trên tình trạng của hệ thống. Mặc dù bảo trì theo thời gian "
      "đôi khi có thể làm giảm hỏng hóc thiết bị, nhưng nó không loại bỏ được các "
      "hỏng hóc thảm khốc và gây ra bảo trì không cần thiết.",
      "Maintenance strategies evolved over time. The first strategy was unplanned, "
      "or run-to-failure, maintenance, which implies waiting for failure to occur. "
      "It is obvious that with this strategy catastrophic failures are unavoidable, "
      "so this kind of maintenance is rarely sustainable and profitable. Later, "
      "preventive maintenance was introduced. Preventive maintenance can be "
      "conducted as planned maintenance or time-based maintenance, which is "
      "implemented at fixed time intervals, or it can be conducted as predictive "
      "maintenance, or condition-based maintenance, where maintenance activities "
      "are realized based on the condition of the system. Although time-based "
      "maintenance can sometimes reduce equipment failures, it does not eliminate "
      "catastrophic failures and causes unnecessary maintenance.")
    P(b, lang,
      "Trong tài liệu có ghi nhận rằng tại Hoa Kỳ, do bảo trì không hiệu quả, hơn "
      "60 tỉ đô la được chi tiêu mỗi năm [3]. Tình hình tương tự ở các quốc gia "
      "khác. Cụ thể, nhược điểm lớn nhất của bảo trì theo thời gian là thay thế các "
      "bộ phận của hệ thống quá thường xuyên, cũng như dừng hệ thống sớm trong khi "
      "nó vẫn đang vận hành, dẫn đến tổn thất vật chất lớn. Trong hầu hết các "
      "trường hợp, bảo trì dự báo là lựa chọn tốt nhất, đặc biệt khi bảo trì rất "
      "tốn kém và sự cố là không thể chấp nhận. Mục tiêu chính của bảo trì dự báo "
      "là kéo dài thời gian hệ thống hoạt động tốt, đồng thời giảm các lần dừng "
      "máy và hỏng hóc không cần thiết. Ngoài ra, mục tiêu của bảo trì dự báo là "
      "ngăn ngừa các hỏng hóc thảm khốc không chỉ gây chi phí vật chất mà còn gây "
      "mất mạng người và ô nhiễm môi trường. Danh sách các tai nạn dạng này không "
      "nhỏ và có thể tìm thấy trong tài liệu [4]. Chính vì những hỏng hóc thảm "
      "khốc thỉnh thoảng xảy ra trong công nghiệp hiện đại, người ta dành nhiều "
      "sự chú ý hơn cho việc cải tiến các chiến lược bảo trì dự báo hiện có, cũng "
      "như giới thiệu các chiến lược mới. Nếu được thiết lập thường xuyên và "
      "triển khai hiệu quả, bảo trì dự báo có thể giảm đáng kể chi phí bảo trì "
      "bằng cách cắt giảm các hoạt động bảo trì theo thời gian không cần thiết [5].",
      "In the literature it can be found that in the USA, because of ineffective "
      "maintenance, more than 60 billion dollars are spent every year [3]. A "
      "similar situation exists in other countries. Namely, the biggest shortcoming "
      "of time-based maintenance is too frequent replacement of system parts, as "
      "well as premature stopping of the system while it is operational, which "
      "leads to great material losses. In most situations, predictive maintenance "
      "is the best choice, especially when maintenance is very expensive and the "
      "occurrence of failure is unacceptable. The main goal of predictive "
      "maintenance is to extend the time in which the system functions well and, "
      "at the same time, to reduce unnecessary stoppages and failures. Also, the "
      "aim of predictive maintenance is to prevent catastrophic failures, which "
      "can produce not only material costs but also loss of lives and environmental "
      "pollution. The list of such accidents is not small and can be found in Ref. "
      "[4]. Because of these catastrophic failures that occasionally occur in "
      "modern industries, more attention is paid to improving the existing "
      "predictive maintenance strategies, as well as to introducing new ones. If "
      "it is regularly established and effectively implemented, predictive "
      "maintenance can significantly reduce maintenance expenses by cutting down "
      "unnecessary time-based maintenance operations [5].")
    P(b, lang,
      "Chẩn đoán và dự báo là hai khía cạnh rất quan trọng trong chương trình bảo "
      "trì dự báo. Chẩn đoán giải quyết việc phát hiện, cô lập và nhận dạng lỗi "
      "sau khi lỗi đã xảy ra. Phát hiện lỗi cho biết khi nào có sự cố trong hệ "
      "thống được giám sát, tức là phát hiện rằng hỏng hóc đã xảy ra. Cô lập lỗi "
      "có nhiệm vụ xác định vị trí thành phần bị lỗi, trong khi nhận dạng lỗi có "
      "nhiệm vụ xác định bản chất của lỗi khi nó được phát hiện. Chẩn đoán đã được "
      "phát triển trong nhiều năm và ngày nay là một lĩnh vực rất quan trọng "
      "trong kỹ thuật và điều khiển tự động [6, 7].",
      "Diagnostics and prognostics are two very important aspects of a predictive "
      "maintenance programme. Diagnostics deals with fault detection, isolation "
      "and identification after the fault has occurred. Fault detection indicates "
      "when something goes wrong in a monitored system, that is, it detects that "
      "failure has occurred. Fault isolation has the task of locating the faulty "
      "component, whereas fault identification has the task of determining the "
      "nature of the fault when it is detected. Diagnostics has been developed "
      "for years, and today it presents a very important area in engineering and "
      "automatic control [6, 7].")
    P(b, lang,
      "Dự báo giải quyết việc dự đoán lỗi trước khi lỗi xảy ra. Nói cách khác, "
      "chẩn đoán là phân tích hồi cứu các sự kiện, trong khi dự báo là phân tích "
      "tiên đoán các sự kiện. Dự báo hiệu quả hơn chẩn đoán trong việc đạt được "
      "hiệu năng không có thời gian chết. Mặt khác, chẩn đoán là cần thiết khi "
      "dự đoán lỗi trong dự báo thất bại và lỗi thực sự xảy ra. Các tài liệu về "
      "dự báo có thể tìm thấy trong tài liệu [8, 9]. Bảo trì dự báo có thể dùng "
      "cho chẩn đoán, cho dự báo, hoặc cho cả hai. Một số tài liệu mới hơn về bảo "
      "trì dự báo có thể tìm thấy trong tài liệu [10–12].",
      "Prognostics deals with fault prediction before the fault occurs. In other "
      "words, diagnostics is the posterior analysis of events, while prognostics "
      "is the a priori analysis of events. Prognostics is more efficient than "
      "diagnostics for achieving zero-downtime performances. On the other hand, "
      "diagnostics is necessary when failure prediction within prognostics fails "
      "and a fault occurs. References about prognostics can be found in Refs. [8, "
      "9]. Predictive maintenance can be used for diagnostics and prognostics, or "
      "for both. Some newer references about predictive maintenance can be found "
      "in Refs. [10–12].")
    P(b, lang,
      "Dù mục tiêu của bảo trì dự báo là gì, ba bước then chốt sau phải được tuân "
      "thủ khi triển khai:",
      "No matter what the goal of predictive maintenance is, three key steps must "
      "be followed for its implementation:")
    L(b, lang,
      ["Thu thập dữ liệu", "Xử lý dữ liệu", "Ra quyết định bảo trì"],
      ["Data acquisition", "Data processing", "Maintenance decision-making"],
      ordered=True)
    P(b, lang,
      "Thu thập dữ liệu là quá trình thu thập dữ liệu từ các nguồn vật lý cụ thể "
      "để triển khai bảo trì dự báo phù hợp. Đây là bước then chốt trong áp dụng "
      "bảo trì dự báo, cho cả chẩn đoán lẫn dự báo. Dữ liệu thu được có thể được "
      "phân thành hai nhóm chính: dữ liệu sự kiện và dữ liệu giám sát tình trạng. "
      "Dữ liệu sự kiện gồm thông tin về những gì đã xảy ra (hỏng hóc, sửa chữa, "
      "nguyên nhân, v.v.). Dữ liệu giám sát tình trạng là các phép đo về 'tình "
      "trạng sức khỏe' của nguồn tài nguyên vật lý.",
      "Data acquisition is the process of collecting data from specific physical "
      "resources in order to implement predictive maintenance properly. This "
      "process is the key step in applying predictive maintenance, both for "
      "diagnostics and for prognostics. Collected data can be classified into two "
      "major categories: event data and condition-monitoring data. Event data "
      "include information about what happened (faults, repairs, what were the "
      "causes, and so on). Condition-monitoring data are the measurements about "
      "the 'health condition' of the physical resource.")
    P(b, lang,
      "Bước đầu tiên trong xử lý dữ liệu là làm sạch dữ liệu. Bước này rất quan "
      "trọng, vì dữ liệu (đặc biệt là dữ liệu sự kiện), vốn luôn được nhập thủ "
      "công, luôn có một số sai sót. Nếu không làm sạch dữ liệu, chẩn đoán và dự "
      "báo có thể trở nên không chính xác. Bước tiếp theo trong xử lý dữ liệu là "
      "phân tích dữ liệu. Các mô hình, thuật toán và công cụ khác nhau để phân "
      "tích dữ liệu phụ thuộc chủ yếu vào loại dữ liệu [5]. Dữ liệu giám sát tình "
      "trạng có thể được phân thành ba nhóm: (1) dạng giá trị, (2) dạng sóng và "
      "(3) dạng đa chiều.",
      "The first step in data processing is data cleaning. This step is very "
      "important, because data (especially event data), which are always entered "
      "manually, have some mistakes. Without data cleaning, it is possible that "
      "diagnostics and prognostics will be inaccurate. The next step in data "
      "processing is data analysis. Different models, algorithms and tools for "
      "data analysis depend mostly on the data type [5]. Condition-monitoring "
      "data can be classified into three categories: (1) value type, (2) waveform "
      "type and (3) multidimensional type.")
    P(b, lang,
      "Bước cuối cùng trong chương trình bảo trì dự báo là ra quyết định. Các kỹ "
      "thuật ra quyết định có thể được chia thành hai nhóm: chẩn đoán và dự báo. "
      "Rõ ràng dự báo vượt trội hơn chẩn đoán, vì nó có thể ngăn hỏng hóc xảy ra "
      "và, nếu có thể, chuẩn bị phụ tùng và nhân lực đã được lên kế hoạch cho các "
      "vấn đề sẽ phát sinh. Nhờ đó có thể giảm tổn thất vật chất và tránh các "
      "hỏng hóc thảm khốc. Tuy nhiên, dự báo không thể thay thế hoàn toàn chẩn "
      "đoán, vì trong thực tế luôn tồn tại một số lỗi không thể đoán trước.",
      "The last step in the predictive maintenance programme is decision-making. "
      "Techniques for decision-making can be divided into two categories: "
      "diagnostics and prognostics. It is obvious that prognostics is superior "
      "to diagnostics, because it can prevent failure from occurring and, if "
      "possible, provides spare parts and planned human resources for problems "
      "that will occur. In this way, it is possible to reduce material losses and "
      "avoid catastrophic failures. However, prognostics cannot replace diagnostics "
      "completely, because in practice there will always be some unpredictable "
      "faults.")
    P(b, lang,
      "Ở đây chúng tôi tập trung vào dự báo. Khi nói đến dự báo hỏng hóc, có hai "
      "loại dự đoán. Loại thứ nhất là dự đoán còn bao nhiêu thời gian trước khi "
      "hỏng hóc xảy ra (một hoặc nhiều hỏng hóc), tùy thuộc vào trạng thái hiện "
      "tại của máy và lịch sử vận hành trong quá khứ. Thời gian còn lại trước khi "
      "phát hiện lỗi được gọi là tuổi thọ hữu ích còn lại (RUL). Trong một số "
      "tình huống, đặc biệt khi hỏng hóc mang tính thảm khốc (ví dụ như nhà máy "
      "điện hạt nhân), loại dự báo thứ hai được ưu tiên hơn, tức là dự đoán "
      "xác suất máy sẽ vận hành đến một thời điểm tương lai nhất định (ví dụ đến "
      "chu kỳ kiểm tra tiếp theo), tùy thuộc vào trạng thái hiện tại của máy và "
      "lịch sử vận hành trong quá khứ. Thực tế, trong mọi tình huống, điều tốt "
      "là biết xác suất máy chạy không hỏng cho đến lần kiểm tra hoặc giám sát "
      "tình trạng tiếp theo. Hầu hết các bài báo đề cập đến loại dự báo thứ "
      "nhất, tức là ước tính RUL [13, 14]. Chỉ có một vài bài báo đề cập đến loại "
      "dự báo thứ hai [15]. Theo tài liệu [8], dự báo hỏng hóc có thể được chia "
      "thành ba nhóm:",
      "Here, we focus on prognostics. There are two types of prediction when we "
      "talk about failure prognosis. The first type is the prediction of how much "
      "time is left before failure will occur (one or more failures), depending on "
      "the current state of the machine and the past operation profile. The time "
      "that is left before the fault is noticed is called remaining useful life "
      "(RUL). In some situations, especially when failure is catastrophic (for "
      "example, a nuclear plant), the second type of failure prognosis is much "
      "preferable, that is, the prediction of the probability that the machine "
      "will work until some future time (for example, until the next interval "
      "when inspection is needed), depending on the current state of the machine "
      "and the past operation profile. Actually, in any situation, it is good to "
      "know the probability that a machine will work without failure until the "
      "next inspection or condition monitoring. Most papers deal with the first "
      "type of failure prognosis, that is, RUL estimation [13, 14]. Only a few "
      "papers can be found that deal with the second type of prognosis [15]. "
      "According to Ref. [8], failure prediction can be divided into three "
      "different categories:")
    L(b, lang,
      ["Cách tiếp cận độ tin cậy truyền thống — dự báo dựa trên dữ liệu sự kiện "
       "(kinh nghiệm) [16]",
       "Cách tiếp cận dự báo — dự báo dựa trên dữ liệu giám sát tình trạng "
       "[17, 18]",
       "Cách tiếp cận tích hợp — dự báo dựa trên cả dữ liệu sự kiện và dữ liệu "
       "giám sát tình trạng [19]"],
      ["Traditional reliability approaches — prediction based on event data "
       "(experience) [16]",
       "Prognostics approaches — prediction based on condition-monitoring data "
       "[17, 18]",
       "Integrated approaches — prediction based on event data and "
       "condition-monitoring data [19]"])
    P(b, lang,
      "Mỗi cách tiếp cận đều có một số ưu điểm và hạn chế. Các cách kết hợp giữa "
      "chúng khác nhau về mức độ áp dụng, chi phí, độ chính xác và độ phức tạp "
      "[20].",
      "Every one of these approaches has some advantages and limitations. "
      "Combinations of these approaches are different according to their "
      "applicability, price, precision and complexity [20].")

    # -------------------------- DESCRIPTION OF THE COAL-GRINDING SUBSYSTEM
    H(b, lang,
      "MÔ TẢ HỆ THỐNG NGHIỀN THAN TRONG NHÀ MÁY NHIỆT ĐIỆN",
      "DESCRIPTION OF THE COAL-GRINDING SUBSYSTEM IN THERMOELECTRIC POWER PLANT",
      level=2)
    P(b, lang,
      "Các nhà máy nhiệt điện là những nhà sản xuất điện lớn nhất ở Serbia, "
      "đóng góp hơn 65% tổng nguồn cung cấp điện. Để đảm bảo tính ổn định và "
      "hiệu quả vận hành, cần giám sát các hệ thống chính và từng thành phần "
      "riêng lẻ. Nhờ đó có thể phát hiện đúng lúc mọi thay đổi về hành vi hoặc "
      "hỏng hóc, làm tăng hiệu quả năng lượng và giảm tổn thất tài chính của "
      "ngành công nghiệp điện.",
      "Thermoelectric power plants are the largest producers of electricity in "
      "Serbia, contributing with more than 65% of the total electricity supply. "
      "In order to ensure their stability and operational efficiency, it is "
      "necessary to monitor their major subsystems and individual components. In "
      "this way, it is possible to detect any change in behaviour, or failure, on "
      "time, which leads to the increase of energy efficiency and the reduction "
      "of the financial losses of the electric power industry.")
    P(b, lang,
      "Một trong những thành phần chính của nhà máy nhiệt điện là hệ thống nghiền "
      "than. Bố trí vật lý của hệ thống được thể hiện trong Hình 9.1. Than thô đi "
      "vào hệ thống qua một bộ cấp liệu và đi xuống máng dẫn tới bàn nghiền quay "
      "với tốc độ không đổi. Than sau đó được đẩy ra ngoài nhờ lực ly tâm và đi "
      "dưới ba con lăn cố định, nơi nó được nghiền. Than đầu ra tiến về phía cổ "
      "máy nghiền, nơi nó được trộn với không khí sơ cấp nóng. Các hạt than nặng "
      "hơn lập tức quay trở lại bàn nghiền để nghiền thêm, trong khi các hạt nhẹ "
      "hơn được dòng khí mang theo tới bộ tách.",
      "One of the key thermoelectric power plant components is the coal-grinding "
      "subsystem. Its physical layout is shown in Figure 9.1. Raw coal enters the "
      "subsystem through a feeder and goes down a chute to the grinding table "
      "that rotates at a constant speed. The coal is then moved outward by "
      "centrifugal force and goes under three stationary rollers where it is "
      "ground. The outgoing coal moves forward to the mill throat where it is "
      "mixed with hot primary air. The heavier coal particles immediately move "
      "back to the grinding table for additional grinding, while lighter particles "
      "are carried by the air flow to the separator.")
    FIG(b, 1, F.fig_f01(), lang)
    P(b, lang,
      "Bộ tách chứa một lượng lớn các hạt lơ lửng trong dòng khí mạnh. Ngoài ra, "
      "một số hạt bị hút vào hỗn hợp không khí sơ cấp và than sẽ mất vận tốc và "
      "rơi xuống bàn nghiền (như trong hình) để nghiền tiếp, trong khi các hạt "
      "đủ nhanh đi vào vùng phân loại. Các hạt này được xoáy bởi các tản lý. Các "
      "hạt nhẹ hơn được lấy ra dưới dạng nhiên liệu bột mịn đi tới đầu đốt, còn "
      "các hạt nặng hơn va vào hình nón của bộ phân loại và rơi ngược xuống bàn "
      "nghiền để nghiền thêm. Cả bộ tách lẫn bộ phân loại đều chứa một lượng "
      "than đáng kể. Khối than này, cùng với than trên bàn nghiền và ba tải "
      "tuần hoàn (sơ cấp, thứ cấp và thứ ba), đóng vai trò then chốt trong đặc "
      "tính động của máy nghiền [21, 22].",
      "The separator contains a large amount of particles suspended in the "
      "powerful air flow. Additionally, some of the particles drawn into the "
      "primary air-and-coal mix lose their velocity and fall onto the grinding "
      "table (as shown) for further grinding, while the particles that are fast "
      "enough enter the classifier zone. These particles are swirled by deflector "
      "plates. Lighter particles are removed as classified fuel in the form of "
      "fine powder that goes to burners, while heavier particles bounce off the "
      "classifier cone and fall back onto the grinding table for additional "
      "grinding. Both the separator and classifier contain a significant amount "
      "of coal. These coal masses, along with the coal on the grinding table and "
      "the three recirculating loads (primary, secondary and tertiary), play a "
      "key role in the dynamic performance of the mill [21, 22].")
    P(b, lang,
      "Trong nghiên cứu này, một hệ thống như vậy tại nhà máy nhiệt điện 'TEKO' "
      "(Serbia) được phân tích. Như đã mô tả ở trên, than bên trong máy nghiền "
      "được nghiền bằng va chạm và ma sát với bàn nghiền quay quanh đường tâm "
      "(CL) của máy nghiền. Cách duy nhất để xác định tình trạng hiện tại của "
      "bàn nghiền là dừng toàn bộ hệ thống và mở ra để kiểm tra trực quan. "
      "Phương pháp bảo trì theo thời gian này đảm bảo bàn nghiền được thay thế "
      "trước khi trở nên hư hỏng, nhưng đổi lại là phải dừng máy thường xuyên. "
      "Nếu kết quả kiểm tra cho thấy chưa cần thay bàn nghiền, tổn thất vật chất "
      "đáng kể sẽ phát sinh. Trong Hình 9.2, hai bàn nghiền được thể hiện: bên "
      "trái là bàn nghiền mới, ngay sau khi thay thế, và bên phải là bàn nghiền "
      "đã mòn, ngay trước khi thay thế.",
      "In this research, one such system at the thermoelectric power plant 'TEKO' "
      "(Serbia) is analyzed. As it is previously described, the coal inside the "
      "mill is ground by impact and friction against the grinding table that "
      "rotates around the mill center line (CL). The only way to determine the "
      "current condition of the grinding table is to shut down the entire "
      "subsystem and open it for visual inspection. This time-based maintenance "
      "method guarantees that grinding tables will be replaced before they become "
      "dysfunctional, but at a cost of frequent shutdowns. If inspection shows "
      "that grinding table replacement is not yet necessary, then significant "
      "material losses will incur. In Figure 9.2, two grinding tables are shown. "
      "On the left figure is a new grinding table, immediately after replacement, "
      "and on the right figure is a worn grinding table, straight before "
      "replacement.")
    FIG(b, 2, F.fig_f02(), lang)
    P(b, lang,
      "Trong thực tế thường gặp tại nhà máy A1 của nhà máy nhiệt điện 'TEKO' ở "
      "Kostolac, bàn nghiền được thay thế sau mỗi 1800 giờ. Tuy nhiên, do hàm "
      "lượng đá vôi, cát và các tạp chất khác trong than tăng lên, bàn nghiền "
      "thường xuống cấp ngay sau 1400 giờ, thậm chí sớm hơn. Khi đó hiệu quả của "
      "máy nghiền suy giảm, máy bị 'nghẽn' và phát sinh vấn đề nghiêm trọng "
      "trong nỗ lực điều chỉnh nhiệt độ của hỗn hợp không khí và áp suất hơi mới "
      "trước tuabin. Hiện tượng này dẫn đến mất cân bằng đáng kể về phân bố "
      "nhiệt độ bên trong buồng lửa, ảnh hưởng xấu đến việc tăng phun nước vào "
      "hơi mới, làm giảm hệ số hiệu suất lò hơi, v.v. Trong những điều kiện như "
      "vậy, máy nghiền thường phải dừng không theo kế hoạch để thay bàn nghiền "
      "và điều này gây tổn thất tài chính. Vì lý do đó, một hệ thống cung cấp "
      "bảo trì dự báo có tầm quan trọng rất lớn.",
      "In practice which is common on plant A1, at the thermoelectric power "
      "plant 'TEKO', Kostolac, grinding tables are replaced every 1800 h. However, "
      "it often happens that because of the increased presence of limestone, sand "
      "and other impurities in coal, grinding tables become deteriorated already "
      "after 1400 h, or even shorter. In that case, weaker effectiveness of the "
      "mill is noticeable, it is 'chocked', and a serious problem with regulation "
      "occurs in an attempt to regulate the temperature of the air mixture and "
      "pressure of fresh steam in front of the turbine. This appearance has for "
      "consequence significant misbalance of temperature distribution inside the "
      "firebox, which has negative influence on increased water injection in "
      "fresh steam, knockdown of coefficient of boiler efficiency and so on. In "
      "such conditions, usually, mill must be stopped unplanned for grinding "
      "table replacement and that incurs financial losses. Because of that, "
      "system which offers predictive maintenance is of great importance.")
    return b
