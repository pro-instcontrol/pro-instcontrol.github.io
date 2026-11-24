# -*- coding: utf-8 -*-
"""Book 9, Chapter 4 (part A) — Nuclear Power Plant Instrumentation Fault
Detection Using Fuzzy Logic (EN/VI bilingual).

Source: Keith E. Holbert and Kang Lin, in L. N. Jalali (ed.), *Handbook on
Power Plant Instrumentation and Control* (Bibliotex, 2019), PDF pp. 65–69,
printed pp. 49–53: ABSTRACT, INTRODUCTION (deregulation, predictive
maintenance, the three maintenance approaches and Figure 1) and
APPLICATIONS OF FUZZY LOGIC (fault detection and isolation, cited
applications). Figure 1 is redrawn as a vector in `ppicfig4_a`; its caption
strip is supplied by `ppicfig4_common._mk`, while the descriptive sentence
printed beneath the figure is kept here as a NOTE. No tables or numbered
equations occur in this source range.
"""
import ppicfig4 as F
from ppic_ch04_lib import H, P, L, E, FIG, TBL, NOTE, REFS


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 4."""
    b = []

    # ---------------------------------------------------------------- ABSTRACT
    H(b, lang, "TÓM TẮT", "ABSTRACT", level=2)
    P(b, lang,
      "Áp lực về kinh tế đang thúc đẩy ngành công nghiệp điện lực tìm kiếm các "
      "phương pháp cải tiến cho việc giám sát, điều khiển và chẩn đoán. Để tăng "
      "khả năng sẵn sàng của nhà máy, nhiều kỹ thuật đã được áp dụng trong công "
      "nghiệp nhằm đánh giá tình trạng thiết bị, ngăn ngừa hệ thống ngừng hoạt "
      "động. Sự sẵn có của một số lượng lớn tín hiệu đo được, cùng với thông tin "
      "bổ sung về thành phần và số lượng ngày càng tăng các tùy chọn xử lý tín "
      "hiệu để phân tích dữ liệu lấy mẫu, thúc đẩy việc tích hợp thông tin đa "
      "dạng này vào một hệ thống giám sát tình trạng trên phạm vi toàn nhà máy. "
      "Bài viết trình bày việc sử dụng logic mờ để ra quyết định về trạng thái "
      "hệ thống và nhu cầu bảo trì thành phần có thể xảy ra. Giám sát chẩn đoán "
      "dựa trên logic mờ được áp dụng cho dữ liệu thu được từ các thiết bị đo "
      "trong các cơ sở đang vận hành.",
      "Economic constraints are driving the electric power industry to seek "
      "improved methods for monitoring, control, and diagnostics. To increase "
      "plant availability, various techniques have been implemented in industry "
      "to assess equipment condition to prevent system inoperability. The "
      "availability of a large number of measured signals and additional "
      "component information and the increasing number of signal processing "
      "options to analyze sampled data motivate the assimilation of such diverse "
      "information into a plantwide condition monitor. The use of fuzzy logic "
      "is described herein for the purpose of performing the decision making "
      "regarding the system status and the possible need for component "
      "maintenance. Fuzzy-logic-based diagnostic monitoring is applied to data "
      "acquired from instrumentation within operating facilities.")

    # ------------------------------------------------------------ INTRODUCTION
    H(b, lang, "GIỚI THIỆU", "INTRODUCTION", level=2)
    P(b, lang,
      "Cạnh tranh do việc bãi bỏ quy định của ngành điện đã tạo thêm động lực "
      "cho chủ sở hữu nhà máy điện triển khai các chương trình bảo trì dự báo "
      "(PM). Việc giám sát tình trạng thiết bị được biết đến qua nhiều hoạt động "
      "liên quan, bao gồm bảo trì theo tình trạng và bảo trì lấy độ tin cậy làm "
      "trung tâm (RCM). Để thực hiện PM mà không làm gián đoạn hoạt động của "
      "thiết bị cần sử dụng các công cụ giám sát trực tuyến để phân tích dấu "
      "hiệu đặc trưng. Đến lượt mình, các dấu hiệu này phải được xem xét kỹ để "
      "xác định xem hệ thống hoặc thành phần có đang tiến tới tình trạng hỏng "
      "hóc hay không. Các tín hiệu ban đầu thường là kết quả của các quá trình "
      "ngẫu nhiên (stochastic).",
      "Competition due to the deregulation of the electric power industry has "
      "provided additional motivation for power plant owners to implement "
      "predictive maintenance (PM) programs. Equipment health monitoring is "
      "known by a variety of related endeavors including condition-based and "
      "reliability-centered maintenance. To accomplish the PM without "
      "interrupting equipment operation necessitates the use of online "
      "monitoring tools for signature analysis. Those signatures, in turn, must "
      "be scrutinized to ascertain whether the system or component is trending "
      "toward a failure condition. The originating signals are often the result "
      "of stochastic (random) processes.")
    P(b, lang,
      "Hình 1 minh họa ba cách tiếp cận cơ bản đối với việc bảo trì thiết bị. "
      "Bảo trì khắc phục (hay phản ứng) chỉ được thực hiện sau khi thành phần "
      "đã hỏng. Để ngăn ngừa sự cố, các cách tiếp cận phòng ngừa bao gồm các "
      "hành động dự báo dựa trên lịch trình hoặc dự đoán. Bảo trì theo lịch "
      "trình, có thể bao gồm kiểm tra và/hoặc thay thế phòng ngừa, được thực "
      "hiện theo cơ sở lịch hoặc theo mức sử dụng của thiết bị. Bảo trì dự đoán "
      "được khởi xướng khi phát hiện dấu hiệu khởi phát của sự cố hoặc hỏng hóc "
      "thiết bị. Bảo trì lấy độ tin cậy làm trung tâm kết hợp cả ba cách tiếp "
      "cận, đồng thời xét đến tầm quan trọng của thiết bị đối với nhiệm vụ của "
      "cơ sở và thường dựa trên phân tích chế độ và tác động của hỏng hóc (FMEA).",
      "Figure 1 illustrates three basic approaches to equipment maintenance. "
      "Corrective (or reactive) maintenance is taken only after the component "
      "has failed. To avert breakdown, preventive approaches involve "
      "anticipatory actions based on a schedule or prediction. Scheduled "
      "maintenance, which may involve inspections and/or preemptive "
      "replacements, can be performed on either calendar or equipment use bases. "
      "Predictive maintenance is initiated because of a detected onset of "
      "equipment malfunction or failure. Reliability-centered maintenance "
      "incorporates all three approaches while considering the importance of "
      "the equipment to the facility mission and is generally based upon "
      "failure modes and effects analysis.")
    FIG(b, 1, F.fig_f01(), lang)
    NOTE(b, lang,
         "Chú thích Hình 4.1: Các phần trăm thể hiện cách phân loại chương trình "
         "bảo trì tại Hoa Kỳ và được lấy từ [8] dựa trên một cuộc khảo sát năm "
         "2000.",
         "Figure 4.1 caption: The percentages represent the categorization of "
         "maintenance program in the USA and are taken from [8] based on a "
         "survey in 2000.")
    P(b, lang,
      "Ngành công nghiệp mong muốn có khả năng phát hiện lỗi và thay thế các "
      "thành phần ngay trước khi xảy ra hỏng hóc. Bằng cách này, có thể tránh "
      "được hậu quả của những sự cố thiết bị bất ngờ. Giám sát trực tuyến thành "
      "phần có thể mang lại khả năng sẵn sàng cao hơn, kéo dài tuổi thọ và giảm "
      "chi phí. Phát hiện sớm hỏng hóc không chỉ giúp tránh sự cố thảm khốc mà "
      "còn hỗ trợ lập kế hoạch hành động khắc phục (tức là bảo trì phòng ngừa). "
      "Phát hiện sớm hỏng hóc có khả năng hỗ trợ đạt được các mục tiêu bảo trì "
      "theo tình trạng.",
      "The capability to detect faults and to replace the components just prior "
      "to failure is desired by industry. By doing so, the consequences of "
      "unexpected equipment failures can be avoided. Online component monitoring "
      "can yield higher availability, extended life, and reduced costs. "
      "Incipient failure detection serves not only to avoid catastrophic "
      "failure, but also to assist in planning corrective actions (i.e., "
      "preventive maintenance). Incipient failure detection has the ability to "
      "assist in achieving condition-based maintenance objectives.")
    P(b, lang,
      "Nhiều kỹ thuật phát hiện và cô lập lỗi (FDI) đã được phát triển qua các "
      "năm. Cách tiếp cận trình bày trong bài báo này nhằm kế thừa các phương "
      "pháp FDI đã được chứng minh để kiểm chứng cảm biến. Trong khi đại đa số "
      "nghiên cứu tập trung vào một phương pháp chẩn đoán cụ thể, công trình "
      "này tìm kiếm một cách để tích hợp thông tin chẩn đoán đa dạng do nhiều "
      "kỹ thuật cung cấp—logic mờ được chọn làm tác nhân thực hiện sự hợp nhất "
      "dữ liệu này.",
      "Many fault detection and isolation (FDI) techniques have been developed "
      "over the years. The approach presented in this paper seeks to build upon "
      "proven FDI methods for sensor validation. Whereas the vast majority of "
      "research focuses on a specific diagnostic approach, this work seeks a "
      "means by which the diverse diagnostic information provided by multiple "
      "techniques may be integrated—fuzzy logic is chosen as the agent to "
      "achieve this data fusion.")
    P(b, lang,
      "Bài báo bắt đầu bằng một khảo sát ngắn về các ứng dụng của logic mờ trong "
      "chẩn đoán và trong nhà máy điện. Phần tiếp theo mô tả triết lý đằng sau "
      "giám sát chẩn đoán bằng logic mờ (FLDM). Sau đó là mô tả về cách FLDM có "
      "thể được triển khai để giám sát tình trạng. Kết quả phân tích từ việc áp "
      "dụng giám sát tình trạng bằng logic mờ cho dữ liệu thu được từ các hệ "
      "thống lò phản ứng hạt nhân được trình bày cùng với mô tả về phương pháp "
      "luận.",
      "This paper begins with a brief survey of the applications of fuzzy logic "
      "to diagnostics and power plants. The next section then describes the "
      "philosophy behind the fuzzy logic diagnostic monitoring (FLDM). This is "
      "followed by a description of how the FLDM can be implemented for "
      "condition monitoring. Analysis results from applying the fuzzy logic "
      "health monitoring to data acquired from nuclear reactor systems are "
      "presented in conjunction with the methodology description.")

    # ----------------------------------------------- APPLICATIONS OF FUZZY LOGIC
    H(b, lang, "ỨNG DỤNG CỦA LOGIC MỜ", "APPLICATIONS OF FUZZY LOGIC", level=2)
    P(b, lang,
      "Một ứng dụng phổ biến của logic mờ (FL) nằm trong lĩnh vực điều khiển. "
      "Việc triển khai điều khiển mờ tại các nhà máy điện bao gồm nhà máy nhiệt "
      "điện mặt trời [1, 2], điều khiển mức nước bình hơi của tổ máy hạt nhân "
      "[3–5] và bơm nước ngầm tại một tổ máy than [6]. Nhằm minh họa sự kết nối "
      "giữa điều khiển và chẩn đoán, Holmes và Ray đã nghiên cứu việc phát "
      "triển hệ thống điều khiển cho một nhà máy điện hóa thạch, trong đó bộ "
      "điều khiển dựa trên logic mờ được giao nhiệm vụ đưa ra phán đoán giữa "
      "hiệu năng động của hệ thống và độ bền cấu trúc của các thành phần then "
      "chốt [7].",
      "A popular application of fuzzy logic (FL) has been in the area of control. "
      "Implementations of fuzzy control in electrical power stations include "
      "solar thermal power plants [1, 2], nuclear unit steam generator level "
      "control [3–5], and groundwater pumping at a coal-fired unit [6]. As an "
      "example bridging control and diagnostics, Holmes and Ray studied control "
      "system development for a fossil power plant in which a fuzzy-logic-based "
      "controller was tasked with making judgments between system dynamic "
      "performance versus structural durability in critical components [7].")
    P(b, lang,
      "Vì bài báo này tập trung vào chẩn đoán nhà máy điện, phần còn lại của mục "
      "này khảo sát ngắn gọn một số ứng dụng của logic mờ trong các lĩnh vực "
      "đó. Choi và các cộng sự đã phát triển một hệ thống chuyên gia mờ trực "
      "tuyến nhằm cung cấp cho người vận hành các màn hình báo động gọn gàng và "
      "thông tin về sự cố trên toàn hệ thống trong các điều kiện bất thường, "
      "đồng thời thực hiện dự báo báo động để cảnh báo người vận hành về các "
      "bất thường của quá trình trong nhà máy điện hạt nhân [9]. Holbert và các "
      "cộng sự áp dụng logic mờ cho phát hiện xâm nhập trong các hệ thống giám "
      "sát và thu thập dữ liệu (SCADA) [10]. Pareek và Kar trình bày một minh "
      "chứng thành công của việc áp dụng hệ thống logic mờ type 2 để dự đoán "
      "áp suất khí thải của tua-bin khí trong nhà máy điện [11]. Köppen-Seliger "
      "và các cộng sự dùng cơ sở luật mờ để đánh giá các phần dư thu được từ "
      "bất kỳ kiến thức phân tích sẵn có nào của nhiều hệ thống con nhằm chẩn "
      "đoán lỗi cho bộ gia nhiệt sơ cấp áp suất cao của một nhà máy điện [12]. "
      "Trong công trình của Na và các cộng sự, một cảm biến phần mềm thông minh "
      "dùng mô hình mờ được phát triển để ước tính trực tuyến chính xác lưu "
      "lượng nước cấp và đồng thời giám sát tình trạng của các cảm biến phần "
      "cứng hiện có trong lò phản ứng nước áp lực [13]. Chẩn đoán dựa trên logic "
      "mờ đã được áp dụng cho nhiều loại nhà máy phát điện, bao gồm cơ sở kết "
      "hợp pin nhiên liệu và tua-bin khí [14] và nhà máy chu trình kết hợp [15].",
      "As this paper is focused on power plant diagnostics, the remainder of "
      "this section briefly surveys some of the fuzzy logic applications in "
      "these domains. Choi et al. developed an online fuzzy expert system to "
      "provide the operator with uncluttered alarm displays and systemwide "
      "failure information during anomalous conditions and carry out alarm "
      "prognosis to warn the operator of process abnormalities in nuclear power "
      "plants [9]. Holbert et al. applied fuzzy logic to intrusion detection in "
      "supervisory control and data acquisition (SCADA) systems [10]. Pareek and "
      "Kar presented a successful demonstration of the application of a type 2 "
      "fuzzy logic system to predict the compressor discharge pressure of a "
      "power plant gas turbine [11]. Köppen-Seliger et al. used a fuzzy logic "
      "rule base to evaluate the residuals obtained by any available analytical "
      "knowledge from several subsystems to perform fault diagnosis for the "
      "high-pressure preheater of a power plant [12]. In the work of Na et al., "
      "a smart software sensor using a fuzzy model was developed to perform "
      "accurate online estimation of the feedwater flow rate and also to monitor "
      "the status of the existing hardware sensors for pressurized water "
      "reactors [13]. Fuzzy-logic-based diagnostics have been applied to a "
      "variety of electric generating stations including a hybrid fuel "
      "cell—gas turbine facility [14] and a combined cycle power plant [15].")
    P(b, lang,
      "Logic mờ cũng đã được áp dụng cho chẩn đoán thành phần và quá trình "
      "trong các bài toán có tính chất tổng quát [16]. Chẳng hạn, Mendonça và "
      "các cộng sự dùng một mô hình mờ để thực hiện FDI cho một van khí nén có "
      "cơ cấu chấp hành servo trong công nghiệp [17]. Yui và Lee sử dụng lý "
      "thuyết tập mờ để tích hợp thông tin định lượng vào một hệ thống chẩn "
      "đoán dựa trên mô hình định tính [18]. Aubrun và các cộng sự thử nghiệm "
      "một phương pháp đánh giá và tái cấu trúc dựa trên FL cho các lỗi cơ cấu "
      "chấp hành bằng dữ liệu mô phỏng từ một nhà máy nhiệt [19]. Trong công "
      "trình của họ, FL được dùng cho cả đánh giá phần dư lẫn tái cấu trúc hệ "
      "thống điều khiển bằng các luật mờ. Liên quan đến cô lập lỗi, họ kết luận "
      "rằng FL cho kết quả tốt hơn về độ mạnh của mô hình so với các phương "
      "pháp cổ điển [19]. Amin và các cộng sự áp dụng hệ thống suy luận mờ, hợp "
      "nhất tri thức và trích xuất đặc trưng để tạo ra một hệ thống giám sát "
      "tình trạng mạnh mẽ nhằm xác định và phân loại sự suy giảm của bơm [20]. "
      "Để tạo ra một hệ thống phát hiện lỗi dành cho các quá trình phức tạp "
      "như nhà máy hóa chất, Vaija và các cộng sự đề xuất dùng hệ thống mờ "
      "đa cấp [21]. Mechefske áp dụng các kỹ thuật logic mờ để phân loại quang "
      "phổ tần số đại diện cho nhiều loại lỗi ổ bi lăn [22]. Uriu và các cộng "
      "sự đã biểu diễn thành công biên độ dập (quench margin) của một hệ thống "
      "nam châm siêu dẫn dưới dạng «yếu tố nguy hiểm» được tạo ra bằng cách "
      "kết hợp dữ liệu thu được từ nhiều cảm biến [23].",
      "Fuzzy logic has also been applied to component and process diagnostics "
      "in problems of a general nature [16]. For instance, Mendonça et al. "
      "employed a fuzzy model to perform FDI for an industrial servoactuated "
      "pneumatic valve [17]. Yui and Lee utilized fuzzy set theory to integrate "
      "quantitative information into a qualitative model-based diagnostics "
      "system [18]. Aubrun et al. tested an FL-based evaluation and "
      "reconfiguration method for actuator failures using simulation data from "
      "a thermal plant [19]. In their work, FL was used for both residual "
      "evaluation and to reconfigure the control system using fuzzy rules. "
      "Regarding the fault isolation, they concluded that FL provides better "
      "results in terms of the robustness of the models as compared with the "
      "classical methods [19]. Amin et al. applied fuzzy inference systems, "
      "knowledge fusion, and feature extraction to create a robust health "
      "monitoring system for the determination and classification of pump "
      "degradation [20]. For creating a failure detection system destined for "
      "complex processes such as a chemical plant, Vaija et al. proposed the "
      "use of a multilevel fuzzy system [21]. Mechefske applied fuzzy logic "
      "techniques to classify frequency spectra that represent various rolling "
      "element bearing faults [22]. Uriu et al. successfully expressed the "
      "quench margin of a superconducting magnet system in terms of a “danger "
      "factor” that is generated by incorporating data gathered from numerous "
      "sensors [23].")
    P(b, lang,
      "Một số nhà nghiên cứu cũng đã đề xuất FL trong ngữ cảnh phát hiện lỗi "
      "thiết bị đo. Việc áp dụng FL để kiểm chứng tín hiệu dường như được Heger "
      "và các cộng sự đề xuất lần đầu vào năm 1993 [24]. Như họ đã nêu, logic "
      "mờ hữu ích cho phát hiện lỗi thiết bị vì nó có ưu điểm chuyển đổi thông "
      "tin ngôn ngữ thành giá trị số để xử lý rồi sau đó chuyển ngược trở lại "
      "miền ngôn ngữ [25, 26]. Mourot và các cộng sự đề xuất dùng nhận dạng mô "
      "hình mờ cho các bài toán phát hiện sai số lớn [27] như có thể gặp khi "
      "dùng phương trình chẵn lẻ để tạo phần dư. Sauter và các cộng sự nghiên "
      "cứu việc dùng FL để chẩn đoán lỗi cảm biến và cơ cấu chấp hành trong một "
      "hệ thống cơ khí mô phỏng. Cụ thể, họ đánh giá phần dư theo cách thích "
      "ứng và dùng kỹ thuật FL để chẩn đoán dấu hiệu lỗi từ một sơ đồ quan sát "
      "chuyên biệt [28]. Bên cạnh đó, Hines và các cộng sự dùng FL để mô hình "
      "hóa và ước tính các trạng thái quá trình như một phần của hệ thống suy "
      "luận thần kinh-mờ thích ứng nhằm thực hiện kiểm chứng hiệu chuẩn kênh "
      "thiết bị đo [29]. Các triển khai lai khác của FL để kiểm chứng cảm biến "
      "bao gồm việc kết hợp FL với các kỹ thuật ước tính trạng thái [30].",
      "A few researchers have also promoted FL in the context of instrumentation "
      "fault detection. Application of FL to signal validation appears to have "
      "been first proposed by Heger et al. in 1993 [24]. As they stated, fuzzy "
      "logic is useful for instrument fault detection, as it possesses the "
      "advantage of transforming linguistic information to numerical values for "
      "processing and then later back to the linguistic domain [25, 26]. Mourot "
      "et al. suggested the use of fuzzy pattern recognition for gross error "
      "detection problems [27] as may be encountered when utilizing parity "
      "equations to generate residuals. Sauter et al. investigated the use of "
      "FL to diagnose sensor and actuator faults in a simulated mechanical "
      "system. In particular, they evaluated residuals in an adaptive manner, "
      "and they used an FL technique to diagnose fault signatures from a "
      "dedicated observer scheme [28]. In addition, Hines et al. used FL to "
      "model and estimate process states as part of an adaptive neural-fuzzy "
      "inference system intended to perform instrument channel calibration "
      "verification [29]. Other hybrid implementations of FL for sensor "
      "validation include the coupling of FL with state estimation techniques "
      "[30].")
    P(b, lang,
      "Vì cảm biến cung cấp phương tiện để người vận hành và hệ thống điều "
      "khiển điều chỉnh các hệ thống, lĩnh vực phát hiện và cô lập lỗi thiết bị "
      "đo đã chứng kiến nhiều nghiên cứu qua các năm. Đối với độc giả muốn xem "
      "lại tài liệu khoa học trong lĩnh vực FDI, xin tham khảo các bài tổng quan "
      "gần đây [31, 32], các báo cáo [33] và các sách [34, 35].",
      "As sensors provide the means by which operators and control systems "
      "regulate systems, the field of instrumentation fault detection and "
      "isolation has seen many studies over the years. For those readers "
      "seeking to review the scientific literature in the field of FDI, see the "
      "recent review papers [31, 32], reports [33], and books [34, 35].")

    return b
