# -*- coding: utf-8 -*-
import ppicfig10 as F
from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS

if not hasattr(F, "fig_f01"):
    F.fig_f01 = lambda: ("<svg xmlns='http://www.w3.org/2000/svg'></svg>",
                         "Hình 10.1 · Sơ đồ hệ thống điều khiển số đề xuất",
                         "Figure 10.1 · Proposed digital system",
                         "Mô tả", "Description")


def _rows(vi, en, lang):
    """Select one language's table rows; VI and EN stay separate literals."""
    return vi if lang == "vi" else en


def section(lang):
    b = []

    P(b, lang,
      "Tài liệu [8] nêu các đặc tính mong muốn mà một phương pháp luận đánh giá "
      "an toàn xác suất (PSA) của hệ thống số phải có để có thể áp dụng thỏa đáng. "
      "Trong số các phương pháp đáp ứng tốt nhất những yêu cầu đó có Phương pháp "
      "đồ thị luồng động (DFM) và phương pháp Markov/CCMT (Kỹ thuật ánh xạ ô sang ô).",
      "Reference [8] presents the desirable characteristics that a PSA methodology "
      "for a digital system must have in order to be applied satisfactorily. Among "
      "the methodologies that best fulfil these requirements are the Dynamic "
      "Flowgraph Methodology (DFM) and the Markov/CCMT (Cell-to-Cell Mapping "
      "Technique) approach.")
    P(b, lang,
      "Mục tiêu của chương này là trình bày hai cách tiếp cận khác nhau để phân tích "
      "độ tin cậy của hệ thống điều khiển và thiết bị đo số, áp dụng các phương pháp "
      "nêu trên cho những trường hợp nghiên cứu khác nhau [5, 9–11]. Sau đó, hai cách "
      "tiếp cận này được phân tích về mức độ chấp nhận được trong bối cảnh quản lý.",
      "The objective of this chapter is to present two different approaches to the "
      "reliability analysis of digital instrumentation and control systems, applying "
      "the methodologies cited above to different case studies [5, 9–11]. These "
      "approaches are then analysed in terms of their acceptability in the "
      "regulatory context.")
    P(b, lang,
      "Chương được tổ chức như sau: thảo luận về Phương pháp đồ thị luồng động và "
      "phương pháp Markov/CCMT (Kỹ thuật ánh xạ ô sang ô) được trình bày trong hai "
      "mục tiếp theo. Kết luận được đưa ra ở mục cuối cùng.",
      "This chapter is organized as follows: the discussion of the Dynamic Flowgraph "
      "Methodology and of Markov/CCMT (Cell-to-Cell Mapping Technique) is presented "
      "in the following two sections. Conclusions are presented in the last section.")

    H(b, lang, "PHƯƠNG PHÁP ĐỒ THỊ LUỒNG ĐỘNG",
      "DYNAMIC FLOWGRAPH METHODOLOGY", level=2)

    P(b, lang,
      "DFM rời rạc hóa các biến quan trọng nhất của hệ thống được phân tích thành "
      "những trạng thái phản ánh hành vi của chúng, thiết lập quan hệ liên kết các biến "
      "này thông qua các bảng quyết định và cuối cùng thực hiện phân tích hệ thống "
      "nhằm, ví dụ, xác định nguyên nhân gốc (các suy diễn chính) của một sự kiện "
      "đỉnh cho trước trong cây lỗi.",
      "DFM discretizes the most relevant variables of the analysed system into states "
      "that reflect their behaviour, sets the logic that connects them through "
      "decision tables, and finally performs a system analysis aimed, for example, at "
      "the root causes (prime implicants) of a given top event of a fault tree.")
    P(b, lang,
      "Kinh nghiệm tích lũy và được ghi nhận trong tài liệu cho thấy DFM [4, 8] là "
      "phương pháp đáp ứng tốt nhất các yêu cầu nêu trong mục trước đối với hệ thống số.",
      "The experience accumulated and reported in the literature indicates DFM [4, 8] "
      "as the methodology that best meets the requirements mentioned in the previous "
      "section for digital systems.")
    P(b, lang,
      "DFM mô tả các tương tác giữa hệ thống điều khiển và các hệ thống con khác, cũng "
      "như các biến quá trình. Phương pháp mô hình hóa toàn bộ hệ thống như một chỉnh "
      "thể. Có những ví dụ ứng dụng liên quan đến hỏng hóc của hệ thống điều khiển "
      "trong nhà máy điện hạt nhân và hỏng hóc trong các hệ thống điều khiển số "
      "không gian (bao gồm cả mô tả sự phụ thuộc) [11–14].",
      "DFM describes interactions among the control system and other subsystems, as "
      "well as process variables. It models a system as a whole. There are examples of "
      "applications concerning failures of control systems in nuclear power plants "
      "and failures in spatial digital control systems (including descriptions of "
      "dependencies) [11–14].")
    P(b, lang,
      "Mạng lưới được xây dựng dựa trên quan hệ nhân quả và quan hệ thời gian giữa "
      "các phần tử của hệ thống. Các phần tử này gồm Nút Quá trình (PN), Nút Điều "
      "kiện (CN), Cạnh Điều kiện (CO), Cạnh Nhân quả (CE), Hộp Truyền (TB) và Hộp "
      "Chuyển tiếp (TT). Thông tin chi tiết hơn có trong các tài liệu [5, 8, 9, 11, "
      "12, 15].",
      "A network is constructed on the basis of the causality and temporal "
      "relationships between the system elements. These elements are Process Nodes "
      "(PN), Condition Nodes (CN), Condition Edges (CO), Causality Edges (CE), "
      "Transfer Boxes (TB) and Transition Boxes (TT). More information can be found "
      "in references [5, 8, 9, 11, 12, 15].")
    P(b, lang,
      "Các phần tử chính của hệ thống vật lý và của hệ thống điều khiển là các PN "
      "của mô hình. Hành vi rời rạc của các phần tử này được biểu diễn bằng các CN "
      "[5]. Các TB và TT phản ánh quan hệ thời gian và nhân quả giữa các biến [5].",
      "The main elements of the physical system and of the control system are the PN "
      "of the model. The discrete behaviour of these elements is represented by CN "
      "[5]. TB and TT reflect the time and causality relationships between the "
      "variables [5].")
    P(b, lang,
      "Mỗi bảng quyết định, liên kết với TB/TT tương ứng, được xác định để phản ánh "
      "các tổ hợp trạng thái có thể có giữa các biến của mô hình [5].",
      "Decision tables, each associated with its respective TB/TT, are defined to "
      "reflect the possible combinations of states among the variables of the model "
      "[5].")
    P(b, lang,
      "Phân tích bao gồm việc xác định một sự kiện đỉnh cần quan tâm và tìm ra cách "
      "thức các phần tử có thể kết hợp các trạng thái của chúng trong mô hình [11].",
      "The analysis consists in defining a top event of interest and finding how the "
      "elements can possibly combine their states in the model [11].")
    P(b, lang,
      "DFM làm việc với khái niệm suy diễn chính [11, 13, 15, 16], tức là các tổ hợp "
      "tối thiểu của các trạng thái biến gây ra sự kiện đỉnh cần quan tâm. Tập hợp "
      "các suy diễn chính có thể được dùng để biểu diễn những trạng thái khác nhau "
      "mà hệ thống có thể có [11].",
      "DFM works with the concept of prime implicants [11, 13, 15, 16], which are the "
      "minimum combinations of variable states that cause the top event of interest. "
      "The set of prime implicants can be used to represent the various states in "
      "which the system can be found [11].")
    P(b, lang,
      "Ví dụ về phương pháp DFM và chi tiết của phương pháp có thể tìm thấy trong các "
      "tài liệu [12–15]. Có những ứng dụng về hỏng hóc phần mềm trong hệ thống điều "
      "khiển số, sai sót của con người, hỏng hóc của hệ thống điều khiển trong nhà máy "
      "điện hạt nhân và hỏng hóc trong hệ thống điều khiển số không gian. Nghiên cứu "
      "này trình bày một ví dụ đơn giản hóa [5, 9, 11] dựa trên bình điều áp thực tế "
      "của lò phản ứng nước áp lực (PWR) [5].",
      "Examples of the DFM methodology and its details can be found in references "
      "[12–15]. There are applications to software failures in digital control "
      "systems, human errors, failures of control systems in nuclear power plants, "
      "and failures in spatial digital control systems. This work presents a "
      "simplified example [5, 9, 11] based on a current PWR pressurizer [5].")
    P(b, lang,
      "Hệ thống đề xuất có chức năng tương tự như hệ thống hiện có nhưng được triển "
      "khai bằng hệ thống số, với một số đơn giản hóa và giả định về đối tượng được "
      "điều khiển. Hệ thống này và cách mô hình hóa được trình bày trong các tài "
      "liệu [5, 9, 11]. Hệ thống gồm máy gia nhiệt, vòi phun, một van xả và một van "
      "an toàn. Chế độ hỏng được xem xét cho từng thành phần. Hình 1 minh họa hệ thống "
      "số đề xuất. Bảng 1 tóm tắt mạch điều khiển của hệ thống, trong đó P là áp "
      "suất, HT là máy gia nhiệt, SP là vòi phun, RV là van xả và SV là van an toàn.",
      "The proposed system has the same functionality implemented by a digital "
      "system, but with some simplifications and assumptions in the controlled "
      "plant. This system and its modelling are presented in references [5, 9, 11]. "
      "It contains heaters, sprays, a relief valve and a safety valve. Failure modes "
      "are considered for each component. Figure 1 illustrates the proposed digital "
      "system. Table 1 summarizes the system control logic, where P is the pressure, "
      "HT the heaters, SP the sprays, RV the relief valve and SV the safety valve.")

    FIG(b, 1, F.fig_f01(), lang)

    TBL(b, lang,
        ["P", "HT", "SP", "RV", "SV"],
        ["P", "HT", "SP", "RV", "SV"],
        _rows([["Rất thấp", "Bật", "Tắt", "Đóng", "Đóng"],
               ["Thấp", "Bật", "Tắt", "Đóng", "Đóng"],
               ["Thấp hơn", "Bật", "Tắt", "Đóng", "Đóng"],
               ["Bình thường", "Tắt", "Tắt", "Đóng", "Đóng"],
               ["Cao hơn", "Tắt", "Bật", "Đóng", "Đóng"],
               ["Cao", "Tắt", "Bật", "Mở", "Đóng"],
               ["Rất cao", "Tắt", "Bật", "Mở", "Mở"]],
              [["Very low", "On", "Off", "Closed", "Closed"],
               ["Low", "On", "Off", "Closed", "Closed"],
               ["Lower", "On", "Off", "Closed", "Closed"],
               ["Normal", "Off", "Off", "Closed", "Closed"],
               ["Higher", "Off", "On", "Closed", "Closed"],
               ["High", "Off", "On", "Opened", "Closed"],
               ["Very high", "Off", "On", "Opened", "Opened"]], lang),
        caption_vi="Bảng 10.1 · Mạch điều khiển của hệ thống",
        caption_en="Table 10.1 · System control logic")
    NOTE(b, lang,
         "[i] — P: áp suất; HT: máy gia nhiệt; SP: vòi phun; RV: van xả; SV: van an toàn.",
         "[i] — P: pressure; HT: heaters; SP: sprays; RV: relief valve; SV: safety valve.")

    P(b, lang,
      "Hệ thống có bốn cơ chế điều khiển áp suất được kích hoạt bởi một bộ vi xử lý "
      "chạy mạch điều khiển bằng phần mềm. Các bộ phận chấp hành này — điều khiển "
      "gia nhiệt, điều khiển phun và hai điều khiển van — là những thông số chính của "
      "hệ thống điều khiển, do đó chúng sẽ trở thành PN trong mô hình DFM, cũng như "
      "biến áp suất, thông số chính của quá trình được điều khiển. Những trạng thái "
      "biến này được rời rạc hóa như Bảng 2, trong đó SS là trạng thái cảm biến; HTS "
      "là trạng thái máy gia nhiệt; SPS là trạng thái vòi phun; RVS là trạng thái van "
      "xả; và SVS là trạng thái van an toàn.",
      "The system has four mechanisms of pressure control triggered by a microprocessor "
      "that runs a control logic through software. These actuators — heating control, "
      "spraying control and the two valve controls — are the key parameters of the "
      "control system, and therefore they become PN in the DFM model, as does the "
      "pressure variable, which is the key parameter of the controlled process. These "
      "variable states are discretized as shown in Table 2, where SS is the sensor "
      "state; HTS the heaters state; SPS the sprays state; RVS the relief valve state; "
      "and SVS the safety valve state.")

    TBL(b, lang,
        ["PN", "Trạng thái", "CN", "Trạng thái"],
        ["PN", "State", "CN", "State"],
        _rows([["P", "Rất cao (169–175 bar)", "SS", "Hỏng ở mức cao"],
               ["P", "Cao (166–169 bar)", "SS", "Bình thường"],
               ["P", "Cao hơn (160–166 bar)", "SS", "Hỏng ở mức thấp"],
               ["P", "Bình thường (156–160 bar)", "HTS", "Hỏng ở trạng thái bật"],
               ["P", "Thấp hơn (148–156 bar)", "HTS", "Bình thường"],
               ["P", "Thấp (140–148 bar)", "HTS", "Hỏng ở trạng thái tắt"],
               ["P", "Rất thấp (131–140 bar)", "SPS", "Hỏng ở trạng thái bật"],
               ["RV", "Mở", "SPS", "Bình thường"],
               ["RV", "Đóng", "SPS", "Hỏng ở trạng thái tắt"],
               ["SV", "Mở", "RVS", "Hỏng ở trạng thái mở"],
               ["SV", "Đóng", "RVS", "Bình thường"],
               ["HT", "Bật", "RVS", "Hỏng ở trạng thái đóng"],
               ["HT", "Tắt", "SVS", "Hỏng ở trạng thái mở"],
               ["SP", "Bật", "SVS", "Bình thường"],
               ["SP", "Tắt", "SVS", "Hỏng ở trạng thái đóng"]],
              [["P", "Very high (169–175 bar)", "SS", "Failed high"],
               ["P", "High (166–169 bar)", "SS", "Normal"],
               ["P", "Higher (160–166 bar)", "SS", "Failed low"],
               ["P", "Normal (156–160 bar)", "HTS", "Failed on"],
               ["P", "Lower (148–156 bar)", "HTS", "Normal"],
               ["P", "Low (140–148 bar)", "HTS", "Failed off"],
               ["P", "Very low (131–140 bar)", "SPS", "Failed on"],
               ["RV", "Opened", "SPS", "Normal"],
               ["RV", "Closed", "SPS", "Failed off"],
               ["SV", "Opened", "RVS", "Failed opened"],
               ["SV", "Closed", "RVS", "Normal"],
               ["HT", "On", "RVS", "Failed closed"],
               ["HT", "Off", "SVS", "Failed opened"],
               ["SP", "On", "SVS", "Normal"],
               ["SP", "Off", "SVS", "Failed closed"]], lang),
        caption_vi="Bảng 10.2 · Nút quá trình và nút điều kiện của mô hình",
        caption_en="Table 10.2 · Model process and condition nodes")

    P(b, lang,
      "Mạch tác động của máy gia nhiệt và của van xả được mô hình hóa trong bảng "
      "quyết định liên kết với một hộp truyền (TB) như Bảng 3.",
      "The action logic of the heaters and of the relief valve is modelled in the "
      "decision table linked to a transfer box (TB), as shown in Table 3.")
    TBL(b, lang,
        ["SS", "P", "HT", "RV"],
        ["SS", "P", "HT", "RV"],
        _rows([["Bình thường", "Rất cao", "Tắt", "Mở"],
               ["Bình thường", "Cao", "Tắt", "Mở"],
               ["Bình thường", "Cao hơn", "Tắt", "Đóng"],
               ["Bình thường", "Bình thường", "Tắt", "Đóng"],
               ["Bình thường", "Thấp hơn", "Bật", "Đóng"],
               ["Bình thường", "Thấp", "Bật", "Đóng"],
               ["Bình thường", "Rất thấp", "Bật", "Đóng"],
               ["Hỏng ở mức thấp", "–", "Bật", "Đóng"],
               ["Hỏng ở mức cao", "–", "Tắt", "Mở"]],
              [["Normal", "Very high", "Off", "Opened"],
               ["Normal", "High", "Off", "Opened"],
               ["Normal", "Higher", "Off", "Closed"],
               ["Normal", "Normal", "Off", "Closed"],
               ["Normal", "Lower", "On", "Closed"],
               ["Normal", "Low", "On", "Closed"],
               ["Normal", "Very low", "On", "Closed"],
               ["Failed low", "–", "On", "Closed"],
               ["Failed high", "–", "Off", "Opened"]], lang),
        caption_vi="Bảng 10.3 · Mô hình TB 1",
        caption_en="Table 10.3 · Model TB 1")

    return b
