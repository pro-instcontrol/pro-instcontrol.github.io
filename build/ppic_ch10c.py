# -*- coding: utf-8 -*-
import ppicfig10 as F
from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS

_T4_VI = [
    ["Rất thấp", "Tắt", "Tắt", "Đóng", "Đóng", "Rất thấp"],
    ["Rất thấp", "Tắt", "Tắt", "Đóng", "Mở", "Rất thấp"],
    ["Thấp", "Tắt", "Bật", "Mở", "Mở", "Thấp"],
    ["Thấp", "Bật", "Tắt", "Đóng", "Đóng", "Thấp hơn"],
    ["Bình thường", "Bật", "Tắt", "Mở", "Mở", "Thấp hơn"],
    ["Bình thường", "Bật", "Bật", "Đóng", "Đóng", "Thấp hơn"],
    ["Rất cao", "Bật", "Bật", "Đóng", "Mở", "Thấp hơn"],
    ["Rất cao", "Bật", "Bật", "Mở", "Mở", "Bình thường"],
]
_T4_EN = [
    ["Very low", "Off", "Off", "Closed", "Closed", "Very low"],
    ["Very low", "Off", "Off", "Closed", "Opened", "Very low"],
    ["Low", "Off", "On", "Opened", "Opened", "Low"],
    ["Low", "On", "Off", "Closed", "Closed", "Lower"],
    ["Normal", "On", "Off", "Opened", "Opened", "Lower"],
    ["Normal", "On", "On", "Closed", "Closed", "Lower"],
    ["Very high", "On", "On", "Closed", "Opened", "Lower"],
    ["Very high", "On", "On", "Opened", "Opened", "Normal"],
]

_T5_VI = [
    ["SS", "Hỏng cao", "0.033"],
    ["SS", "Hỏng thấp", "0.033"],
    ["HTS", "Hỏng bật", "0.018"],
    ["HTS", "Hỏng tắt", "0.018"],
    ["SPS", "Hỏng bật", "0.046"],
    ["SPS", "Hỏng tắt", "0.046"],
    ["RVS", "Hỏng mở", "0.004"],
    ["RVS", "Hỏng đóng", "0.004"],
    ["SVS", "Hỏng mở", "0.007"],
    ["SVS", "Hỏng đóng", "0.007"],
    ["P", "Rất cao", "&lt;10E-166"],
    ["P", "Cao", "&lt;10E-96"],
    ["P", "Cao hơn", "&lt;10E-14"],
    ["P", "Bình thường", "9.0 10E-1"],
    ["P", "Thấp hơn", "9.2 10E-2"],
    ["P", "Thấp", "&lt;10E-81"],
    ["P", "Rất thấp", "&lt;10E-295"],
]
_T5_EN = [
    ["SS", "Failed high", "0.033"],
    ["SS", "Failed low", "0.033"],
    ["HTS", "Failed on", "0.018"],
    ["HTS", "Failed off", "0.018"],
    ["SPS", "Failed on", "0.046"],
    ["SPS", "Failed off", "0.046"],
    ["RVS", "Failed opened", "0.004"],
    ["RVS", "Failed closed", "0.004"],
    ["SVS", "Failed opened", "0.007"],
    ["SVS", "Failed closed", "0.007"],
    ["P", "Very high", "&lt;10E-166"],
    ["P", "High", "&lt;10E-96"],
    ["P", "Higher", "&lt;10E-14"],
    ["P", "Normal", "9.0 10E-1"],
    ["P", "Lower", "9.2 10E-2"],
    ["P", "Low", "&lt;10E-81"],
    ["P", "Very low", "&lt;10E-295"],
]

_T6_VI = [
    ["Xác suất Prime Implicant = 1.0609E-06"],
    ["Áp suất ở trạng thái Bình thường tại thời điểm −1"],
    ["Trạng thái cảm biến ở mức Bình thường tại thời điểm −1"],
    ["Trạng thái nhóm gia nhiệt ở mức Bình thường tại thời điểm −1"],
    ["Trạng thái van an toàn ở mức Hỏng mở tại thời điểm −1"],
    ["Trạng thái van xả ở mức Hỏng mở tại thời điểm −1"],
    ["Trạng thái vòi phun ở mức Hỏng bật tại thời điểm −1"],
    ["trạng thái vòi phun đã hỏng ở chế độ bật tại thời điểm −1"],
]
_T6_EN = [
    ["Prime Implicant Probability = 1.0609E-06"],
    ["Pressure was Normal at time −1"],
    ["Sensor State was Normal at time −1"],
    ["Heaters State was Normal at time −1"],
    ["Safety Valve State was Failed Opened at time −1"],
    ["Relief Valve State was Failed Opened at time −1"],
    ["Sprays State was Failed On at time −1"],
    ["Sprays state was failed on at time −1"],
]

# The printed .ftl example is kept verbatim, including its two internal spaces.
_FTL_A = [
    "pressure_very_low",
    "= pressure_very_low or",
    "pressure_very_low_subsystem_1",
    "pressure_very_low_subsystem_2",
    "pressure_very_low_pressurizer",
    "etc",
    "…",
]
_FTL_B = [
    "pressure_very_low _pressurizer or",
    "prime_implicant_1",
    "prime_implicant _1 and",
    "pressure_normal_t-1",
    "heaters_normal_t-1",
    "sensor_normal_t-1",
    "sprays_failed_on_t-1",
    "reliefvalve_failed_opened_t-1",
    "safetyvalve_failed_opened_t-1",
]


def section(lang):
    b = []
    H(b, lang, "Bảng quyết định TT 1 và xác suất của các biến",
      "The TT 1 Decision Table and Variable Probabilities", level=3)
    P(b, lang,
      "Bước tiếp theo là liên kết các biến của mô hình thông qua các hộp truyền và hộp chuyển "
      "tiếp. Mỗi phần tử này có một bảng quyết định tương ứng, thể hiện mối quan hệ nhân–quả "
      "tồn tại giữa các biến.",
      "The next step consists in interconnecting the model variables through transfer and "
      "transition boxes. Each of these elements has an associated decision table showing the "
      "causality relationship that exists between the variables.")
    P(b, lang,
      "Logic tác động của nhóm gia nhiệt và van xả được thể hiện trên bảng quyết định liên kết "
      "với một TB (Bảng 3). Bảng quyết định liên quan đến một TT được trình bày tại Bảng 4. "
      "Bảng quyết định này cho thấy các cơ chế điều khiển của hệ thống [5].",
      "The group of heaters and relief valve action logic is shown on the decision table linked "
      "to a TB (Table 3). The decision table related to a TT is shown in Table 4. This decision "
      "table shows the control mechanisms of the system [5].")
    TBL(b, lang,
        ["P (áp suất)", "HT (gia nhiệt)", "SP (vòi phun)", "RV (van xả)",
         "SV (van an toàn)", "P+"],
        ["P", "HT", "SP", "RV", "SV", "P+"],
        _T4_VI if lang == "vi" else _T4_EN,
        caption_vi="Bảng 10.4 · Mô hình TT 1",
        caption_en="Table 10.4 · Model TT 1")
    H(b, lang, "Xác suất của các biến trong mô hình",
      "Variable Probabilities of the Model", level=3)
    TBL(b, lang,
        ["Biến", "Trạng thái", "Xác suất"],
        ["Var", "State", "Prob"],
        _T5_VI if lang == "vi" else _T5_EN,
        caption_vi="Bảng 10.5 · Xác suất của các biến trong mô hình",
        caption_en="Table 10.5 · Model variable probabilities")
    P(b, lang,
      "Mô hình DFM cung cấp một phân tích định lượng các kết quả thu được từ xác suất trạng thái "
      "của các biến. Sử dụng dữ liệu hỏng hóc từ tài liệu tham khảo [17] và phân bố xác suất ước "
      "tính cho áp suất, các xác suất đã được xác định và trình bày tại Bảng 5.",
      "The DFM model provides a quantitative analysis of the results from the state "
      "probabilities of its variables. Using failure data from reference [17] and the "
      "probability distribution estimated for pressure, the probabilities were obtained and "
      "are shown in Table 5.")
    P(b, lang,
      "Đối với các thiết bị điều khiển ở chế độ liên tục, thời gian vận hành 1 năm trong một nhà "
      "máy điện hạt nhân đã được xem xét trong phép tính. Đối với các thiết bị điều khiển ở chế "
      "độ yêu cầu, một lần tác động theo yêu cầu đã được xem xét. Các chế độ hỏng chung cho từng "
      "thiết bị đã được xem xét.",
      "For control devices in continuous mode, 1 year of operation time in a nuclear power plant "
      "has been considered for the calculation. For control devices in demand mode, one demand "
      "operation has been considered. Generic failure modes for each device have been "
      "considered.")
    P(b, lang,
      "Xác suất của áp suất ở mỗi trạng thái được tính từ hàm mật độ xác suất trong từng khoảng.",
      "The pressure probabilities in each state were calculated from the probability density "
      "function in each interval.")
    H(b, lang, "Sự kiện đỉnh “Áp suất rất thấp” và các prime implicant",
      "Top Event “Pressure Very Low” and Prime Implicants", level=3)
    P(b, lang,
      "Trong phân tích này, sự kiện đỉnh “Áp suất rất thấp”, đại diện cho một trong các hỏng hóc "
      "trong điều khiển thiết bị tạo áp và dẫn đến ngắt lò phản ứng sau đó, là một trong những "
      "sự kiện đỉnh được quan tâm [5, 9, 11].",
      "Regarding the analysis, the top event “Pressure Very Low”, representing one of the "
      "failures in the pressurizer control and later reactor trip, is one of the top events of "
      "interest [5, 9, 11].")
    P(b, lang,
      "Bộ công cụ DYAMONDA® [15] của ASCA® Inc. đã được sử dụng.",
      "The toolset DYAMONDA® [15], from ASCA® Inc., was utilized.")
    P(b, lang,
      "Các prime implicant, hay nói cách khác, là số nhỏ nhất các tổ hợp trạng thái của các biến "
      "trong hệ thống dẫn đến sự kiện đỉnh hỏng hóc, đã được tìm kiếm. Thiết lập câu lệnh "
      "“Pressure Very Low @ t = 0”, trong đó t = 0 là ký hiệu chỉ thời điểm kết thúc phân tích, "
      "thu được kết quả là 32 prime implicant.",
      "The prime implicants or, in other words, the smallest number of combinations of variable "
      "states in the system that lead to the failure top event are searched. Setting the "
      "sentence “Pressure Very Low @ t = 0”, where t = 0 is a notation indicating the end of "
      "the analysis time, the results are 32 prime implicants.")
    P(b, lang,
      "Giả sử các điều kiện biên gồm cảm biến mức hoạt động đúng và nhóm gia nhiệt ở trạng thái "
      "tắt và đang chạy, kết quả là prime implicant được trình bày tại Bảng 6 [5, 9, 11].",
      "Assuming boundary conditions consisting of a proper work of the level sensor and heaters "
      "off and running, the result is the prime implicant shown in Table 6 [5, 9, 11].")
    TBL(b, lang,
        ["Prime implicant"],
        ["Prime Implicant"],
        _T6_VI if lang == "vi" else _T6_EN,
        caption_vi="Bảng 10.6 · Prime implicant cho “áp suất rất thấp”",
        caption_en="Table 10.6 · Prime implicant for “pressure very low”")
    NOTE(b, lang,
      "Lưu ý về nguồn: dòng cuối cùng của Bảng 10.6 — “Sprays state was failed on at time −1” — "
      "được in trùng lại trong tài liệu gốc, ngay sau dòng “Sprays State was Failed On at time "
      "−1”. Chúng tôi giữ nguyên dòng trùng này để phản ánh trung thực bản in.",
      "Source note: the final row of Table 6 — “Sprays state was failed on at time −1” — is "
      "printed a second time in the source, immediately after the “Sprays State was Failed On "
      "at time −1” row. The duplicated row is retained here to reflect the printed source "
      "faithfully.")
    P(b, lang,
      "Với prime implicant này, các hỏng hóc của van và vòi phun đưa áp suất xuống mức “Rất "
      "thấp”. Ngay cả việc cảm biến mức ở trạng thái “Bình thường”, cũng như nhóm gia nhiệt, "
      "cũng không cho phép tăng áp suất để bù đắp sự sụt giảm do các cơ chế khác gây ra.",
      "For this prime implicant, valve and, spray failures lead the pressure to “Very Low”. Not "
      "even the fact that the level sensor is in “Normal,” as are the group heaters, allows an "
      "increase of pressure to compensate the drop provided by the other mechanisms.")
    H(b, lang, "Tích hợp kết quả DFM vào phân tích an toàn xác suất",
      "Integrating DFM Results into Probabilistic Safety Analysis", level=3)
    P(b, lang,
      "Việc thay thế các vòng lặp tương tự bằng các hệ thống số diễn ra dần dần, do đó nhiều hệ "
      "thống số vẫn cùng tồn tại với các hệ thống tương tự tại nhiều nhà máy công nghiệp. Cần "
      "thiết là kết quả phân tích hỏng hóc của các hệ thống số phải có thể được tích hợp vào các "
      "báo cáo phân tích an toàn xác suất hiện có liên quan đến các vòng lặp tương tự. Chỉ khi "
      "đó mới có thể thực hiện các phân tích độ bất định và độ quan trọng, ví dụ trên chính các "
      "kết quả này, như đã thực hiện cho các cây lỗi khác.",
      "The replacement of analog loops by digital systems is gradual and, therefore, several "
      "digital systems still coexist with analog systems in various industrial plants. It is "
      "necessary that the results of failure analysis in digital systems can be incorporated "
      "into the existing probabilistic safety analysis reports related to analog loops. Only "
      "then it will be possible to perform uncertainty and importance analyses, for example, on "
      "these results, such as those carried out for other fault trees.")
    P(b, lang,
      "Các kết quả của DFM đáp ứng yêu cầu này. Có thể tích hợp chúng bằng cách sử dụng một công "
      "cụ truyền thống trong phân tích hỏng hóc, chẳng hạn như phần mềm SAPHIRE [18]. Quy trình "
      "này được minh họa dưới đây.",
      "The results of the DFM meet this requirement. One can incorporate them by using a "
      "traditional tool in failure analysis, as the SAPHIRE code [18], for instance. This "
      "procedure is illustrated below.")
    P(b, lang,
      "Phần mềm SAPHIRE yêu cầu một tệp văn bản được nhập với phần mở rộng .ftl, được viết theo "
      "một định dạng cụ thể. Lấy ví dụ kết quả của sự kiện đỉnh “Áp suất rất thấp”, tệp .ftl "
      "sẽ được viết như sau [9]:",
      "The SAPHIRE code requires a text file to be imported in an extension .ftl written in a "
      "specific format. Taking as an example the results of the top event “Pressure Very Low”, "
      "the .ftl would be written as follows [9]:")
    L(b, lang, _FTL_A, _FTL_A, ordered=False)
    L(b, lang, _FTL_B, _FTL_B, ordered=False)
    P(b, lang,
      "trong đó “pressure_very_low” là sự kiện đỉnh, “pressure_very_low_subsystem1, 2, etc...” "
      "đại diện cho các tín hiệu ngắt áp suất “Very_Low” trong các hệ thống tương tự khác, và "
      "“pressure_very_low_pressurizer” đại diện cho tín hiệu ngắt của điều khiển thiết bị tạo áp "
      "số.",
      "where “pressure_very_low” is the top event, “pressure_very_low_subsystem1, 2, etc...” "
      "represent the trips of “Very_Low” pressure in the other analog systems, and "
      "“pressure_very_low_pressurizer” represents the trip of the digital pressurizer control.")
    P(b, lang,
      "Có thể tìm thêm chi tiết về việc tích hợp vào PSA trong các tài liệu tham khảo [4, 8], nơi "
      "cung cấp các hướng dẫn liên quan.",
      "More details regarding incorporation on PSA can be found on references [4, 8], where "
      "guidelines are made available.")
    H(b, lang, "Nhận diện lỗi phần mềm và phân tích độ tin cậy con người",
      "Identifying Software Failures and Human Reliability Analysis", level=3)
    P(b, lang,
      "DFM có thể được dùng để nhận diện các hỏng hóc phần mềm của hệ thống được phản ánh trong "
      "mô hình thông qua định nghĩa của một số bảng quyết định, bằng hai chế độ của nó (quy nạp "
      "và suy diễn), như trình bày trong các tài liệu tham khảo [8, 19]. Sau khi sử dụng chế độ "
      "suy diễn, có thể dùng chế độ quy nạp từng bước để kiểm chứng tính đúng đắn của logic "
      "phần mềm.",
      "DFM can be used to identify system software failures reflected in the model on the "
      "definition of some decision tables through its two modes (inductive and deductive), as "
      "shown in references [8, 19]. Once the deductive mode is utilized, one can utilize the "
      "inductive mode, step by step, to verify the correctness of the software logic.")
    P(b, lang,
      "DFM cũng có thể tích hợp Phân tích độ tin cậy con người (HRA) vào phân tích hỏng hóc của "
      "hệ thống, như trình bày trong tài liệu tham khảo [20].",
      "DFM can also incorporate Human Reliability (HRA) on the system failure analysis, as shown "
      "in reference [20].")
    return b
