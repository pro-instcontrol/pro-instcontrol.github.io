# -*- coding: utf-8 -*-
"""Book 9, Chapter 4 (part C) - Fuzzy Logic Diagnostic Monitoring, continued.

Source: work/ppic_raw.txt lines 1967-2076 (PDF pp. 75-81, printed pp. 59-65):
the spurious reactor core exit temperature signature, the link between fuzzy
logic decision making and signal validation, and the plant database.

Figures 5, 6 and 7 are redrawn in the ``ppicfig4_*`` suppliers; Table 2 of the
source is transcribed here as Table 4.2. No numbered equations occur in this
fragment.
"""
import ppicfig4 as F
from ppic_ch04_lib import H, P, FIG, TBL


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 4."""
    b = []

    # ------------------------------------------------- Figure 5 (core exit spike)
    FIG(b, 5, F.fig_f05(), lang)

    P(
        b, lang,
        "Các dạng chữ ký sơ cấp như thế này có khả năng áp dụng rộng rãi trong các "
        "hệ thống của nhà máy. Các chế độ hỏng có thể được nhận diện bằng những mô "
        "tả tín hiệu cơ bản gồm xung nhọn, trôi, lệch, nhiễu và kẹt. Nhận dạng mẫu "
        "và các mô-đun xử lý tín hiệu số bổ sung dùng kỹ thuật miền thời gian và "
        "miền tần số tiên tiến cũng có thể được đưa vào bộ chẩn đoán, nhưng những "
        "phương pháp đó thường là thế mạnh của giai đoạn đặc trưng hóa. Ngoài "
        "phân tích tín hiệu ngẫu nhiên, kết quả thử nghiệm mang tính xác định cũng "
        "có thể được dùng làm đầu vào cho bộ giám sát tình trạng, ví dụ như phân "
        "tích dầu bôi trơn máy và hạt mòn; tuy nhiên, đây lại là những phương pháp "
        "chuyên sâu và đặc thù cho từng hệ thống. Vì vậy, công việc cần làm để tạo "
        "ra một bộ giám sát chẩn đoán hiệu quả trở thành phân tích dữ liệu thu "
        "thập được nhằm xác định hệ thống hoặc thành phần cụ thể có đang biểu hiện "
        "những đặc điểm cảnh báo hỏng sớm hay không.",
        "Rudimentary signatures such as these have wide applicability across plant "
        "systems. The failure modes addressable by fundamental signal descriptors "
        "include spikes, drift, bias, noise, and stuck. Pattern recognition and "
        "additional digital signal processing modules employing advanced time and "
        "frequency domain techniques could also be included within the diagnostician, "
        "but those would generally be the forte of the characterization stage. "
        "Besides random signal analysis, deterministic test results can also be "
        "included as input to the condition monitor, for example, machine lubricating "
        "oil and wear particle analyses, but again those represent in-depth and "
        "system-specific methods. The effort in realizing an effective diagnostic "
        "monitor then becomes the analysis of the acquired data in order to determine "
        "whether the particular system or component is exhibiting characteristics "
        "that warn of incipient failure.")

    # ---------------------------------------------------------- Diagnostic Monitoring
    H(b, lang, "Giám sát chẩn đoán", "Diagnostic Monitoring", level=3)

    P(
        b, lang,
        "Hợp nhất, phân tích và giải thích dữ liệu quá trình là những rào cản chính "
        "để đạt được công tác giám sát tình trạng thiết bị tốt hơn. Kết quả cho "
        "thấy phát hiện lỗi phải được thực hiện bằng cách dùng nhiều kỹ thuật xử lý "
        "tín hiệu khác nhau nhằm phân tích tín hiệu một cách bền vững; tuy nhiên, "
        "các phương pháp luận này nên được kết hợp thành một sơ đồ phát hiện lỗi "
        "thống nhất, thay vì chỉ chạy song song mà không cho phép trao đổi thông tin "
        "giữa các kỹ thuật xử lý tín hiệu. Cách tiếp cận logic mờ dựa trên luật cho "
        "phép kết hợp thông tin từ nhiều miền khác nhau.",
        "Process data fusion, analysis, and interpretation represent key barriers to "
        "achieving better equipment health monitoring. Results have shown that fault "
        "detection must be accomplished by using diverse signal processing techniques "
        "to perform robust signal analysis; however, these methodologies should be "
        "melded into a cohesive fault detection scheme rather than combined in a "
        "parallel scheme that permits no crosstalk between the signal processing "
        "techniques. A rule-based fuzzy logic approach allows the combination of "
        "information from multiple domains.")

    P(
        b, lang,
        "Kỹ thuật xử lý tín hiệu nói chung thì hữu ích, nhưng giám sát tình trạng "
        "thiết bị chuyên sâu đòi hỏi các thuật toán phân tích riêng cho từng thiết "
        "bị. Ví dụ, hãy xem xét việc chẩn đoán tình trạng các đường dẫn áp suất trong "
        "nhà máy điện hạt nhân của chính các tác giả [37, 38]. Với chẩn đoán đường "
        "dẫn dụng cụ như vậy, mật độ phổ công suất của các dao động áp suất (nhiễu) "
        "được xác định rồi so sánh với các mô hình dựa trên hàm truyền của điều kiện "
        "bình thường và bất thường như tắc đường, gặp khí và rò rỉ [39]. Tuy nhiên, "
        "cuối cùng tất cả những kết quả đó phải được kết hợp thông qua một mô-đun "
        "ra quyết định ở cấp cao hơn — đây chính là vai trò của FLDM. Logic mờ được "
        "dùng ở vai trò ra quyết định (xem Hình 4.6) để chẩn đoán hệ thống bằng các "
        "mô-đun xử lý tín hiệu. Nhờ giữ cho bộ giám sát chẩn đoán linh hoạt đối với "
        "các loại thiết bị và hệ thống áp dụng, FLDM có thể được dùng trên quy mô "
        "toàn nhà máy. Hệ thống cũng có thể được mở rộng bằng cách bổ sung các "
        "phương pháp FDI khác (như lọc Kalman) để xử lý dữ liệu và thông tin thu "
        "thập được.",
        "General signal processing techniques are useful but in-depth equipment "
        "condition monitoring requires equipment-specific analysis algorithms. As an "
        "example, consider the authors' health diagnostics of pressure sensing lines "
        "in nuclear power plants [37, 38]. For such instrument line diagnostics, the "
        "power spectral density of the pressure fluctuations (noise) is determined "
        "and compared to transfer function based models of normal and anomalous "
        "conditions such as line blockage, gas entrapment, and leakage [39]. In the "
        "end, however, all of these results must be combined via a higher-level "
        "decision-making module—this is the role of the FLDM. Fuzzy logic is "
        "employed in a decision-making capacity (see Figure 4.6) for system "
        "diagnostics using signal processing modules. By keeping the diagnostic "
        "monitor flexible with respect to the applicable types of equipment and "
        "systems, the FLDM can be applied on a plantwide basis. The system can also "
        "be expanded through the addition of other FDI methods (such as Kalman "
        "filtering) to process the collected data and information.")

    # ------------------------------------------------- Figure 6 (FLDM connections)
    FIG(b, 6, F.fig_f06(), lang)

    P(
        b, lang,
        "Khi mã hóa FLDM, chúng tôi nhận ra rằng nhân viên nhà máy có lợi thế so "
        "với các phương pháp FDI nhờ kinh nghiệm cá nhân và khả năng của con người "
        "trong việc tiếp nhận nhiều thông tin và dữ liệu mới. Ngược lại, máy tính "
        "có ưu điểm là xử lý những thông tin đó nhanh hơn con người. Logic mờ, với "
        "tư cách là một công cụ trí tuệ nhân tạo, có thể tận dụng kinh nghiệm của "
        "người vận hành nhà máy cùng khả năng xử lý dữ liệu nhanh của máy tính. Kết "
        "quả số học từ các mô-đun xử lý tín hiệu khác nhau được mờ hóa để FLDM xử "
        "lý; FLDM đưa trí tuệ của kỹ sư-phân tích gia vào các luật mờ. Hệ mờ dựa trên "
        "luật được xây dựng ở đây dùng quá trình suy luận mờ Mamdani. Các luật mờ và "
        "hệ số trọng số được điều chỉnh cho phù hợp với thiết bị và kỹ thuật xử lý "
        "tín hiệu cụ thể. Ví dụ, hệ số trọng số bằng không có thể được dùng để cấm "
        "một mô-đun cụ thể phân tích dữ liệu từ một thành phần nhất định, đồng thời "
        "vẫn giữ mô-đun đó sẵn sàng kiểm tra các hệ thống khác trong nhà máy. Trọng "
        "số được chọn để phản ánh mức độ tin cậy mà một mô-đun xử lý tín hiệu có thể "
        "nhận diện đúng một chế độ hỏng nhất định trong thiết bị/hệ thống cụ thể đó. "
        "Chi phí tính toán của hệ mờ đủ thấp để phân tích tín hiệu có thể được thực "
        "hiện theo thời gian thực. Kiến trúc mô-đun cho phép chèn các kỹ thuật tiên "
        "tiến mới khi chúng được đánh giá là hữu ích cho các nhà máy phát điện.",
        "In encoding the FLDM, we recognize that plant personnels have an advantage "
        "over FDI methods in terms of their personal experience and the human "
        "capability to assimilate a wide range of information and new data. In "
        "contrast, computers have an edge in being able to process such information "
        "faster than their human counterparts can. Fuzzy logic, as an artificial "
        "intelligence tool, can take advantage of the plant operators' experience and "
        "the rapid data processing capability of computers. The numerical results of "
        "the various signal-processing modules are fuzzified for processing by the "
        "FLDM, which incorporates the intellect of the engineer-analyst into the "
        "fuzzy rules. The rule-based fuzzy system created here uses the Mamdani fuzzy "
        "inference process. The fuzzy rules and weighting factors are tailored to the "
        "particular equipment and signal processing techniques. For example, a zero "
        "weighting factor can be used to prohibit a particular module from analyzing "
        "data from a given component while still making the module available for "
        "examining other plant systems. The weights are chosen to reflect the "
        "confidence by which a given signal processing module can properly identify "
        "a given failure mode within that particular equipment/system. The "
        "computational overhead for the fuzzy system is such that signal analysis can "
        "be accomplished in real time. The modular architecture allows the insertion "
        "of new state-of-the-art techniques when they are deemed useful to electric "
        "generating stations.")

    P(
        b, lang,
        "Một cơ sở luật được xây dựng để biểu diễn nhận thức của con người về tình "
        "huống bằng toán học. Cơ sở luật của cách tiếp cận logic mờ mang tính tổng "
        "quát theo nghĩa các luật không phụ thuộc vào biến trạng thái cụ thể đang "
        "được đo. Các phép toán tập mờ được áp dụng cùng với các luật. Cuối cùng, "
        "một sơ đồ giải mờ được dùng để xác định vị trí trọng tâm và từ đó xác định "
        "trạng thái tín hiệu. Dù các mô-đun xử lý tín hiệu có thể áp dụng cho toàn bộ "
        "dữ liệu thu thập được, điều đó không có nghĩa là hệ số trọng số giống nhau "
        "cho mọi thành phần và hệ thống trong nhà máy. Trong khi các kỹ thuật khác "
        "nhau thường dùng ranh giới số nghiêm ngặt trong khi phát hiện lỗi, bộ giám "
        "sát được mô tả ở đây nới lỏng các ranh giới cứng bằng cách dùng lý thuyết "
        "tập mờ. Như vậy, phương pháp này nối liền các cách tiếp cận thống kê của "
        "kỹ thuật kiểm định giả thuyết với các phương pháp phỏng đoán do người vận "
        "hành hệ thống áp dụng.",
        "A rule base is created allowing the human perception of the situation to be "
        "represented mathematically. The rule base of the fuzzy logic approach is "
        "generic in the sense that the rules are oblivious to the particular state "
        "variable being measured. Fuzzy set operations are applied in conjunction "
        "with the rules. Finally, a defuzzification scheme is used to determine the "
        "centroid location and, therefore, the signal status. Although the signal "
        "processing modules may be applied to all the collected data, this is not to "
        "say that the weighting factors are the same for all plant components and "
        "systems. Whereas the various techniques generally utilize strict numeric "
        "boundaries during the fault detection, the monitor described here relaxes "
        "the hard boundaries by utilizing fuzzy set theory. As such, this method "
        "bridges the statistical approaches taken by hypothesis testing techniques "
        "with the heuristic methods applied by system operators.")

    P(
        b, lang,
        "Ngoài việc phân tích dữ liệu theo thời gian thực, có thể dùng cơ sở dữ liệu "
        "về độ tin cậy của thành phần để đưa ra quyết định chính xác hơn về tình "
        "trạng thiết bị. Danh sách một số thông tin có thể đưa vào cơ sở dữ liệu "
        "được cho trong Bảng 4.2.",
        "Besides the real-time data analyses, a database of component reliability can "
        "be utilized from which more accurate decisions can be made regarding "
        "equipment health. A list of some of the information that may be incorporated "
        "in the database is given in Table 4.2.")

    P(
        b, lang,
        "Thông tin dùng cho hệ thống giai đoạn hai được rút từ cơ sở dữ liệu chung, "
        "vốn cũng chứa một cơ sở dữ liệu dạng cây như minh họa trong Hình 4.7. Cơ sở "
        "dữ liệu dạng cây là một danh sách liên kết giúp tạo động các luật riêng cho "
        "từng hệ thống từ các quan hệ tổng quát. Nó cung cấp mô tả vật lý về cơ sở "
        "hạ tầng đang xét và tri thức về mạng lưới thiết bị đo của cơ sở đó, gồm loại "
        "cảm biến, vị trí, nhà sản xuất, số mô hình và các cảm biến lân cận. Cơ sở dữ "
        "liệu dạng cây được xây dựng để bảo đảm hệ mờ có thể mang sang các nhà máy "
        "điện khác nhau và thích ứng khi mạng lưới cảm biến hoặc cơ sở hạ tầng được "
        "thay đổi. Để giảm khả năng báo động giả do các bất thường chung của thiết bị "
        "đo, có thể dùng cấu trúc cây để tìm kiếm sự xuất hiện của những bất thường "
        "tương tự.",
        "The information employed for the second-stage system is derived from the "
        "general database, which also includes a tree-structured database as depicted "
        "in Figure 4.7. The tree-structured database is a linked list that facilitates "
        "the dynamic creation of system-specific rules from general relationships. It "
        "provides a physical description of the infrastructure of interest and "
        "knowledge of its instrumentation network, including sensor types, locations, "
        "manufacturers, model numbers, and nearby sensors. The tree-structured "
        "database is constructed to ensure that the fuzzy system is portable between "
        "diverse power plants and adaptable when either the sensory network or the "
        "infrastructure is modified. To reduce the possibility of false alarms due to "
        "common-cause instrument anomalies, the tree structure may be used to search "
        "for the occurrence of similar abnormalities.")

    # ------------------------------------------------- Table 4.2 (plant database)
    rows_vi = [
        ["Thiết bị đo", "Danh sách biến đo, cảm biến, độ chính xác"],
        ["Chữ ký cơ sở", "NRMS, độ xiên, độ nhọn, tần số vượt qua không"],
        ["Thông số kỹ thuật thiết bị", "Nhà sản xuất, số mô hình"],
        ["Hồ sơ bảo trì", "Ngày và kỹ thuật viên thực hiện hiệu chuẩn gần nhất và sửa chữa gần đây nhất; lịch sử độ tin cậy"],
    ]
    rows_en = [
        ["Instrumentation", "List of measured variables, sensors, accuracy"],
        ["Baseline signatures", "NRMS, skewness, kurtosis, zero-crossing rate"],
        ["Equipment specifications", "Manufacturer, model number"],
        ["Maintenance records", "Dates of and technician performing the last calibration and most recent repair; reliability history"],
    ]
    TBL(
        b, lang,
        ["Danh mục thông tin", "Thông tin cụ thể lưu trong cơ sở dữ liệu"],
        ["Information category", "Specific information stored in the database"],
        rows_vi if lang == "vi" else rows_en,
        caption_vi="Bảng 4.2: Cơ sở dữ liệu nhà máy",
        caption_en="Table 4.2: Plant database")

    # ------------------------------------------------ Figure 7 (tree database)
    FIG(b, 7, F.fig_f07(), lang)

    P(
        b, lang,
        "Một vấn đề khác là nhà máy đang vận hành ở điều kiện ổn định hay đang trải "
        "qua quá trình chuyển tiếp, ví dụ trong khởi động hoặc khi thay đổi tải. Một "
        "số kỹ thuật xử lý tín hiệu phù hợp hơn với điều kiện tĩnh, trong khi những "
        "phương pháp khác lại có thể thích hợp với điều kiện động. Trên thực tế, dữ "
        "liệu từ các nhà máy điện hạt nhân chạy tải cơ bản thường dễ phân tích hơn dữ "
        "liệu từ các nhà máy chạy tải đỉnh.",
        "Another issue is whether the plant is operating at steady-state conditions "
        "or whether it is undergoing a transient, for instance, during startup or "
        "load changes. Some signal processing techniques are better suited to static "
        "conditions whereas other methods may be adept at dynamic conditions. "
        "Practically speaking, the data from base load nuclear power plants are "
        "generally easier to analyze than those from peaking units.")

    return b
