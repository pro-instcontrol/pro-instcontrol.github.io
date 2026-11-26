# -*- coding: utf-8 -*-
import ppicfig10 as F
from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS


def _stub(n, cap_vi, cap_en, desc_vi, desc_en, detail):
    """Inert but valid five-tuple used only while a supplier figure is absent."""
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 300" '
           'role="img" aria-label="Figure 10.%d">'
           '<rect x="8" y="8" width="664" height="284" fill="none" '
           'stroke="#888888"/>'
           '<text x="340" y="130" text-anchor="middle" font-size="15">'
           'Figure 10.%d</text>'
           '<text x="340" y="160" text-anchor="middle" font-size="11">%s</text>'
           '</svg>') % (n, n, detail)
    return (svg, cap_vi, cap_en, desc_vi, desc_en)


if not hasattr(F, "fig_f02"):
    F.fig_f02 = lambda: _stub(
        2, "Hình 10.2 · Sơ đồ chuyển tiếp Markov cho van nước cấp",
        "Figure 10.2 · Markov transition diagram for the Feedwater Valve",
        "Sơ đồ gồm trạng thái (0) VPC0 ở bên trái, với hai mũi tên tới (1) VPC1 và (2) VPC2.",
        "States (0) VPC0 at left with arrows to (1) VPC1 and (2) VPC2.",
        "Feedwater valve Markov states VPC0, VPC1, VPC2")
if not hasattr(F, "fig_f03"):
    F.fig_f03 = lambda: _stub(
        3, "Hình 10.3 · Sơ đồ chuyển tiếp Markov cho CPU chính và CPU dự phòng",
        "Figure 10.3 · Markov transition diagram for the Main CPU and the Backup CPU",
        "Hai sơ đồ: CPU chính MC0 tới MC1, MC2, MC3, MC4 và CPU dự phòng BC0 tới BC1, BC2, BC3, BC4, được nối bởi mũi tên đứt nét từ MC3.",
        "Two diagrams: Main CPU MC0 to MC1, MC2, MC3, MC4 and Backup CPU BC0 to BC1, BC2, BC3, BC4, joined by a dashed arrow from MC3.",
        "Main and Backup CPU Markov diagrams MC0-MC4 and BC0-BC4")
if not hasattr(F, "fig_f04"):
    F.fig_f04 = lambda: _stub(
        4, "Hình 10.4 · Xác suất xảy ra một sự kiện đỉnh",
        "Figure 10.4 · Probability of occurrence of a Top Event",
        "Đồ thị theo thời gian 0 đến 40 giờ; đường đứt nét tăng mạnh sau 30 giờ tới 2,7E-06, đường liền gần như nằm ngang.",
        "Chart versus time 0 to 40 hours; dashed curve rising steeply after 30 h to 2.7E-06, solid curve almost flat.",
        "Top-event probability chart, t = 0 to 40 hours")


_T7_HEAD_VI = ["Mã", "Chế độ hỏng", "Ảnh hưởng", "Tỷ lệ hỏng (/h)"]
_T7_HEAD_EN = ["Code", "Failure mode", "Effects", "Failure rate (/h)"]
_T7_ROWS_VI = [
    ["MC1", "Mất tín hiệu của một cảm biến",
     "Máy tính vận hành chỉ với tín hiệu của cảm biến còn lại.",
     "λ<sub>MC1</sub> = 16,4 × 10<sup>−7</sup>/h"],
    ["MC2", "Mất tín hiệu của cả hai cảm biến",
     "Má tính duy trì van điều khiển mở hoàn toàn.",
     "λ<sub>MC2</sub> = 8,2 × 10<sup>−7</sup>/h"],
    ["MC3", "Lỗi xử lý dữ liệu nhận bởi máy tính",
     "Điều khiển được chuyển sang Máy tính Dự phòng.",
     "λ<sub>MC3</sub> = 1,2 × 10<sup>−6</sup>/h"],
    ["MC4", "Lỗi liên lạc với van",
     "Tín hiệu đưa tới van là 0,0 V, giữ van đóng hoàn toàn.",
     "λ<sub>MC4</sub> = 1,8 × 10<sup>−6</sup>/h"],
]
_T7_ROWS_EN = [
    ["MC1", "Signal loss of one sensor",
     "Computer operates solely with the signal of the remaining sensor.",
     "λ<sub>MC1</sub> = 16.4 × 10<sup>−7</sup>/h"],
    ["MC2", "Signal loss of both sensors",
     "Computer maintains the control valve completely open.",
     "λ<sub>MC2</sub> = 8.2 × 10<sup>−7</sup>/h"],
    ["MC3", "Processing failure of the data received by the computer",
     "Control is transferred to the Backup Computer.",
     "λ<sub>MC3</sub> = 1.2 × 10<sup>−6</sup>/h"],
    ["MC4", "Failure to communicate with the valve",
     "Signal fed to the valve is 0.0 V, keeping it completely closed.",
     "λ<sub>MC4</sub> = 1.8 × 10<sup>−6</sup>/h"],
]

_T8_HEAD_VI = ["Mã", "Chế độ hỏng", "Ảnh hưởng", "Tỷ lệ hỏng (/h)"]
_T8_HEAD_EN = ["Code", "Failure mode", "Effects", "Failure rate (/h)"]
_T8_ROWS_VI = [
    ["BC1", "Mất tín hiệu của một cảm biến",
     "Máy tính vận hành chỉ với tín hiệu của cảm biến còn lại.",
     "λ<sub>BC1</sub> = 16,4 × 10<sup>−7</sup>/h"],
    ["BC2", "Mất tín hiệu của cả hai cảm biến",
     "Máy tính duy trì van điều khiển mở hoàn toàn.",
     "λ<sub>BC2</sub> = 8,2 × 10<sup>−7</sup>/h"],
    ["BC3", "Lỗi xử lý dữ liệu nhận bởi máy tính",
     "Mất điều khiển tự động của quá trình và van được duy trì ở trạng thái đóng.",
     "λ<sub>BC3</sub> = 1,2 × 10<sup>−6</sup>/h"],
    ["BC4", "Lỗi liên lạc với van",
     "Tín hiệu đưa tới van là 0,0 V, giữ van đóng hoàn toàn.",
     "λ<sub>BC4</sub> = 1,8 × 10<sup>−6</sup>/h"],
]
_T8_ROWS_EN = [
    ["BC1", "Signal loss of one sensor",
     "The computer operates solely with the signal of the remaining sensor.",
     "λ<sub>BC1</sub> = 16.4 × 10<sup>−7</sup>/h"],
    ["BC2", "Signal loss of both sensors",
     "The computer maintains the control valve completely open.",
     "λ<sub>BC2</sub> = 8.2 × 10<sup>−7</sup>/h"],
    ["BC3", "Processing failure of the data received by the computer",
     "Automatic control of the process is lost and the valve is maintained closed.",
     "λ<sub>BC3</sub> = 1.2 × 10<sup>−6</sup>/h"],
    ["BC4", "Failure to communicate with the valve",
     "The signal fed to the valve is 0.0 V, keeping it completely closed.",
     "λ<sub>BC4</sub> = 1.8 × 10<sup>−6</sup>/h"],
]

_T9_HEAD_VI = ["Mã", "Chế độ hỏng", "Ảnh hưởng", "Tỷ lệ hỏng (/h)"]
_T9_HEAD_EN = ["Code", "Failure mode", "Effects", "Failure rate (/h)"]
_T9_ROWS_VI = [
    ["V1", "Van bị kẹt hoàn toàn ở trạng thái đóng.",
     "Lưu lượng nước cấp bằng 0 và mức nước giảm liên tục.",
     "λ<sub>VPC1</sub> = 1,7 × 10<sup>−5</sup>/h"],
    ["V2", "Van bị kẹt hoàn toàn ở trạng thái mở.",
     "Lưu lượng nước cấp là lớn nhất và mức nước tăng liên tục.",
     "λ<sub>VPC2</sub> = 1,7 × 10<sup>−5</sup>/h"],
]
_T9_ROWS_EN = [
    ["V1", "The valve gets stuck completely closed.",
     "The feedwater flowrate is 0 and the water level decreases continuously.",
     "λ<sub>VPC1</sub> = 1.7 × 10<sup>−5</sup>/h"],
    ["V2", "The valve gets stuck completely open.",
     "The feedwater flowrate is max and the water level increases continuously.",
     "λ<sub>VPC2</sub> = 1.7 × 10<sup>−5</sup>/h"],
]

_T10_HEAD_VI = ["Ô", "Miền giá trị", "Trạng thái"]
_T10_HEAD_EN = ["Cell", "Range", "State"]
_T10_ROWS_VI = [
    ["j = 1", "x ≤ 11,2 m", "Hỏng ở mức thấp"],
    ["j = 2", "11,2 m &lt; x ≤ 11,7 m", "Thấp"],
    ["j = 3", "11,7 m &lt; x ≤ 12,2 m", "Trung bình-thấp"],
    ["j = 4", "12,2 m &lt; x ≤ 12,7 m", "Trung bình-cao"],
    ["j = 5", "12,7 cm &lt; x ≤ 13,2 cm", "Cao"],
    ["j = 6", "x &gt; 13,2 cm", "Hỏng ở mức cao"],
]
_T10_ROWS_EN = [
    ["j = 1", "x ≤ 11.2 m", "Failed low"],
    ["j = 2", "11.2 m &lt; x ≤ 11.7 m", "Low"],
    ["j = 3", "11.7 m &lt; x ≤ 12.2 m", "Normal-low"],
    ["j = 4", "12.2 m &lt; x ≤ 12.7 m", "Normal-high"],
    ["j = 5", "12.7 cm &lt; x ≤ 13.2 cm", "High"],
    ["j = 6", "x &gt; 13.2 cm", "Failed high"],
]

_T11_HEAD = ["K", "t", "P1(k)", "P5(k)", "PET(k)"]
_T11_ROWS = [
    ["0", "0", "0.0", "0.0", "0"],
    ["1", "10", "0.0", "0.0", "0"],
    ["2", "20", "0.0", "0.0", "0"],
    ["3", "30", "3.5E-08", "1.78955E-08", "5.3E-08"],
    ["4", "40", "2.7E-06", "1.1427E-07", "2.8E-06"],
]


def section(lang):
    b = []

    H(b, lang, "CÁCH TIẾP CẬN MARKOV/CCMT", "MARKOV/CCMT APPROACH", level=2)

    P(b, lang,
      "Cách tiếp cận Markov/CCMT [4, 21–23] kết hợp các quá trình ngẫu nhiên "
      "Markov với CCMT nhằm biểu diễn các phụ thuộc giữa các sự kiện hỏng có "
      "thể phát sinh từ sự tương tác động giữa hệ thống điều khiển và thiết bị "
      "đo số với quá trình được điều khiển, cũng như giữa các thành phần khác "
      "nhau của chính hệ thống điều khiển và thiết bị đo số đó.",
      "Markov/CCMT [4, 21–23] is an approach that combines Markov stochastic "
      "processes with the CCMT to represent the dependencies between failure "
      "events that can originate from the dynamic interactions between the "
      "digital I&amp;C system and the controlled process, and also among the "
      "different components of the digital I&amp;C system itself.")

    H(b, lang, "Quá trình Markov và CCMT", "Markov processes and CCMT", level=3)

    P(b, lang,
      "Các quá trình Markov có thể xử lý các phụ thuộc giữa các sự kiện, chẳng "
      "hạn như hỏng do nguyên nhân chung, các thành phần dùng chung tải và việc "
      "sửa chữa. CCMT [22–24] là một thủ tục có hệ thống mô tả động lực học của "
      "cả hệ thống tuyến tính và phi tuyến trong thời gian rời rạc và không gian "
      "trạng thái hệ thống được rời rạc hóa, giống như các quá trình Markov.",
      "Markov processes can treat dependencies among events, such as "
      "common-cause failures, shared-load components and repair. CCMT [22–24] "
      "is a systematic procedure for describing the dynamics of both linear "
      "and nonlinear systems in discrete time and a discretized system state "
      "space, just as Markov processes do.")

    P(b, lang,
      "CCMT cung cấp một công cụ rất hiệu quả để tính đến các bất định nhận "
      "thức, các khía cạnh phi tuyến của động lực học hệ thống và các dao động "
      "ngẫu nhiên trong vận hành của hệ thống động. CCMT tạo ra một mô hình "
      "tương thích với cách tiếp cận quá trình Markov trong việc biểu diễn "
      "các hỏng [20, 22, 23].",
      "CCMT provides a very effective means of accounting for epistemic "
      "uncertainties, nonlinear aspects of system dynamics and stochastic "
      "fluctuations in dynamic system operation. CCMT produces a model that "
      "is compatible with the Markov process approach for representing "
      "failures [20, 22, 23].")

    P(b, lang,
      "Chuỗi Markov thông thường biểu diễn sự tiến hóa ngẫu nhiên của một hệ "
      "thống thông qua các xác suất chuyển tiếp giữa các trạng thái có thể có "
      "của hệ thống. Các chuyển tiếp giữa các trạng thái có thể được biểu diễn "
      "bằng đồ thị thông qua các liên kết có hướng (cạnh) trong sơ đồ chuyển "
      "tiếp Markov. Ngay cả khi không có dữ liệu hỏng, mô hình Markov/CCMT vẫn "
      "có thể được dùng ở cả bước quy nạp và bước suy diễn của PSA — tức là "
      "lần lượt là xác định chuỗi sự cố và phân tích hỏng của hệ thống an toàn. "
      "Kết quả của bước đầu có thể dùng để thu được các quan hệ giữa sự kiện "
      "khởi phát và sự kiện đỉnh hoặc trạng thái vận hành (quan hệ "
      "nguyên nhân–hệ quả), còn kết quả của bước sau đó dùng để điều tra các "
      "nguyên nhân chính dẫn tới một sự kiện đỉnh hoặc trạng thái hệ thống cụ "
      "thể [4].",
      "The conventional Markov chain represents the stochastic evolution of a "
      "system through the transition probabilities among its possible states. "
      "Transitions between states can be represented graphically by directed "
      "links (edges) in Markov transition diagrams. Even when failure data are "
      "unavailable, a Markov/CCMT model can be used in both the inductive and "
      "deductive steps of a PSA — that is, the identification of accident "
      "sequences and safety system failure analysis, respectively. The results "
      "of the former can be used to obtain the relations between initiating "
      "events and top events or the operational state (cause–consequence "
      "relations), while the results of the latter investigate the primary "
      "causes leading to a specific top event or system state [4].")

    H(b, lang, "Tích hợp vào PSA và giới hạn tính toán",
      "Integration with PSA and computational limits", level=3)

    P(b, lang,
      "Các phân tích tầm quan trọng (sắp xếp theo tần suất của các sự kiện "
      "trong chuỗi hoặc của các thành phần) có thể được thực hiện bằng các "
      "công cụ PSA tiêu chuẩn [4, 18]. Nếu có dữ liệu hỏng, tần suất kịch bản "
      "và xác suất của sự kiện đỉnh có thể được định lượng. Mô hình "
      "Markov/CCMT có thể được tích hợp vào các PSA tiêu chuẩn bằng chính các "
      "công cụ PSA tiêu chuẩn đó [4, 8, 18, 24].",
      "Importance analyses (frequency ordering of sequence events or "
      "components) can be carried out with standard PSA tools [4, 18]. If "
      "failure data are available, the scenario frequency and the top event "
      "probability can be quantified. The Markov/CCMT model can be integrated "
      "into standard PSAs using standard PSA tools [4, 8, 18, 24].")

    P(b, lang,
      "Một mô hình Markov/CCMT đầy đủ rời rạc hóa toàn bộ hệ thống thành các "
      "trạng thái do người dùng định nghĩa và thể hiện mọi chuyển tiếp có thể "
      "giữa các trạng thái đó. Phân tích được thực hiện bằng cách xác định các "
      "sự kiện đỉnh hoặc sự kiện khởi phát cần quan tâm và quan sát hành vi "
      "của hệ thống. Việc xây dựng các mô hình lớn bằng Markov/CCMT có thể "
      "không khả thi về mặt tính toán — thường thì các mô hình này có vài "
      "nghìn trạng thái hệ thống [4, 23, 24].",
      "A full Markov/CCMT discretizes the whole system into states defined by "
      "the user and shows all possible transitions between those states. The "
      "analysis is carried out by defining the top events or initiating events "
      "of interest and observing system behaviour. It may not be "
      "computationally feasible to construct large Markov/CCMT models, which "
      "generally contain several thousand system states [4, 23, 24].")

    P(b, lang,
      "Các bước áp dụng Markov/CCMT được mô tả dưới đây [4]:",
      "The steps in applying Markov/CCMT are described below [4]:")
    L(b, lang,
      ["Xây dựng mô hình Markov/CCMT biểu diễn hệ thống cần nghiên cứu.",
       "Phân tích mô hình Markov/CCMT.",
       "Định lượng các kết quả phân tích suy diễn và quy nạp."],
      ["Construct the Markov/CCMT model to represent the system of interest.",
       "Analyse the Markov/CCMT model.",
       "Quantify the deductive and inductive analytical results."],
      ordered=True)

    P(b, lang,
      "Đầu vào của việc xây dựng mô hình Markov/CCMT là tập hợp các trạng thái "
      "hệ thống đã được rời rạc hóa. Các trạng thái này được xác định từ phân "
      "tích chế độ hỏng và ảnh hưởng (FMEA) cũng như từ logic điều khiển của "
      "hệ thống. Phải định nghĩa các khoảng loại trừ lẫn nhau cho các biến "
      "quá trình liên tục, giống như cách làm trong phương pháp sai phân hữu "
      "hạn; các khoảng này được gọi là các ô. Sau đó, thông qua các mô phỏng "
      "với điều kiện ban đầu, điều kiện cuối và khoảng bước thời gian, xác "
      "suất chuyển tiếp giữa các ô được tìm ra. Xác suất chuyển tiếp trạng "
      "thái của hệ thống cũng phải được mô phỏng và kết hợp với xác suất "
      "chuyển tiếp của các biến liên tục nêu trên. Dù một số bước trong xây "
      "dựng mô hình đã được cơ giới hóa, phần mềm đa năng để xây dựng mô hình "
      "vẫn chưa có sẵn [4].",
      "The input to Markov/CCMT model construction is the set of discretized "
      "system states. These states are identified from a Failure Mode and "
      "Effects Analysis (FMEA) and from the system control logic. Mutually "
      "exclusive intervals must be defined for continuous process variables, "
      "just as in finite difference methods; these intervals are called cells. "
      "Transition probabilities between cells are then found through "
      "simulations that define final and initial conditions as well as a "
      "time-step interval. The state transition probabilities of the system "
      "must also be simulated and combined with the transition probabilities "
      "of the continuous variables. Although some steps of model construction "
      "have been mechanized, general purpose software for model construction "
      "is not yet available [4].")

    P(b, lang,
      "Tài liệu [8] chỉ ra một số hạn chế của phương pháp. Các hạn chế này gồm "
      "khó khăn về tính toán phát sinh từ khối lượng trạng thái mô hình được "
      "định nghĩa (độ phức tạp của mô hình), cũng như việc lựa chọn bước thời "
      "gian và thời gian nhiệm vụ trong phân tích. Ngoài ra, Markov/CCMT đòi "
      "hỏi lượng kiến thức kỹ thuật lớn hơn đáng kể so với phân tích cây sự "
      "kiện/cây lỗi truyền thống [4]. Phương pháp tạo ra một lượng dữ liệu "
      "lớn; vì vậy cần có một số xử lý hậu kết quả. Ở đây trình bày một ví dụ "
      "đơn giản hóa về áp dụng phương pháp cho một hệ thống điều khiển số "
      "được điều chỉnh dành cho mức nước của một máy phát hơi nước PWR điển "
      "hình [10].",
      "Reference [8] shows some limitations of the methodology. These "
      "comprise computational difficulties arising from the volume of model "
      "states defined (model complexity), as well as the choice of time step "
      "and mission time in the analysis. Markov/CCMT also requires a "
      "substantially larger amount of technical knowledge than a traditional "
      "event tree/fault tree analysis [4]. The methodology produces a large "
      "amount of data, so some post-processing of the results is required. "
      "Here, a simplified example of the application of the methodology to an "
      "adapted digital control system for the water level of a typical PWR "
      "steam generator is presented [10].")

    H(b, lang,
      "Hệ thống điều khiển số điều chỉnh cho mức nước máy phát hơi nước PWR",
      "Adapted digital control of PWR steam-generator water level", level=3)

    P(b, lang,
      "Trong hệ thống số được điều chỉnh này, mức nước được đo bằng hai cảm "
      "biến mức và tín hiệu trung bình của chúng được đưa tới bộ điều khiển, "
      "nơi so sánh tín hiệu này với giá trị đặt. Sai lệch được đưa vào một "
      "chương trình điều khiển PI (Tỷ lệ–Tích phân) tạo ra tín hiệu hiệu "
      "chỉnh; tín hiệu này điều khiển một van nước cấp có động cơ và do đó "
      "điều khiển lượng nước đi vào máy phát hơi nước. Từ sự điều chỉnh này, "
      "một mô phỏng của hệ thống đã được xây dựng và phương pháp Markov/CCMT "
      "đã được áp dụng cho hệ thống đó.",
      "In the adapted digital system, the water level is measured by two "
      "level sensors and their average signal is fed to the controller, which "
      "compares it with the set point. The difference is fed to a PI "
      "(Proportional–Integral) control routine that generates a correction "
      "signal; this signal controls a motorized feedwater valve and hence the "
      "water entering the steam generator. From this adaptation, a simulation "
      "of the system was built and the Markov/CCMT methodology was applied to "
      "the system.")

    H(b, lang, "Các phân tích chế độ hỏng và ảnh hưởng",
      "Failure mode and effects analyses", level=3)

    P(b, lang,
      "Bước tiếp theo là thực hiện FMEA cho hệ thống. Trong trường hợp này "
      "chỉ các thành phần chính được xem xét. Các hỏng do hiện tượng bên "
      "ngoài như cháy và bức xạ không được tính đến, cũng như không xét đến "
      "việc sửa chữa hoặc thay thế linh kiện. Những hạn chế này không được áp "
      "dụng trong một PSA đầy đủ. Tỷ lệ hỏng được lấy từ tài liệu [25].",
      "The next step is to perform an FMEA of this system. Only its main "
      "components were considered in this case. Failures induced by external "
      "phenomena such as fire and radiation were not considered, and neither "
      "was component repair or replacement. These restrictions are not taken "
      "into account in a complete PSA. The failure rates were taken from "
      "reference [25].")

    P(b, lang,
      "Hai máy tính làm việc cùng nhau để bảo đảm vận hành đúng đắn của hệ "
      "thống. Nếu xảy ra hỏng ở CPU chính, CPU dự phòng sẽ tiếp nhận điều "
      "khiển hệ thống. Có thể xét các chế độ hỏng của cảm biến cũng như của "
      "các CPU, vì hậu quả của những hỏng này là như nhau [4]. Bảng 7 trình "
      "bày FMEA của CPU chính và Bảng 8 trình bày FMEA của CPU dự phòng.",
      "Two computers work together to ensure correct system operation. If a "
      "failure occurs in the Main CPU, the Backup CPU assumes control of the "
      "system. Failure modes of the sensors as well as those of the CPUs may "
      "be considered, since the consequences of these failures are the same "
      "[4]. Table 7 gives the FMEA of the Main CPU and Table 8 the FMEA of "
      "the Backup CPU.")

    TBL(b, lang, _T7_HEAD_VI, _T7_HEAD_EN,
        _T7_ROWS_VI if lang == "vi" else _T7_ROWS_EN,
        caption_vi="Bảng 10.7 · FMEA của CPU chính",
        caption_en="Table 10.7 · FMEA of the main CPU")

    TBL(b, lang, _T8_HEAD_VI, _T8_HEAD_EN,
        _T8_ROWS_VI if lang == "vi" else _T8_ROWS_EN,
        caption_vi="Bảng 10.8 · FMEA của CPU dự phòng",
        caption_en="Table 10.8 · FMEA of the backup CPU")

    P(b, lang,
      "Các chế độ hỏng khác của CPU là có thể xảy ra nhưng đã được bỏ qua "
      "nhằm đơn giản hóa phân tích; chúng phải được xét trong một PSA đầy "
      "đủ. Bảng 9 trình bày phân tích chế độ hỏng và ảnh hưởng của van nước "
      "cấp. Cũng như đối với các CPU, các chế độ hỏng khác của van nước cấp "
      "là có thể xảy ra nhưng đã được bỏ qua để đơn giản hóa phân tích.",
      "Other failure modes are possible for the CPUs but were ignored in "
      "order to simplify the analysis; they must be considered in a full "
      "PSA. Table 9 presents the Failure Mode and Effects Analysis of the "
      "Feedwater Valve. As with the CPUs, other failure modes of the "
      "Feedwater Valve are possible but were ignored to simplify the "
      "analysis.")

    TBL(b, lang, _T9_HEAD_VI, _T9_HEAD_EN,
        _T9_ROWS_VI if lang == "vi" else _T9_ROWS_EN,
        caption_vi="Bảng 10.9 · FMEA cho van nước cấp",
        caption_en="Table 10.9 · FMEA for the feedwater valve")

    H(b, lang, "Giả định về chuyển tiếp trạng thái của CPU",
      "Assumptions for CPU state transitions", level=3)

    P(b, lang,
      "Ví dụ, các giả định sau đã được đưa ra cho các chuyển tiếp trạng thái "
      "của các CPU:",
      "For example, the following assumptions were made for the state "
      "transitions of the CPUs:")
    L(b, lang,
      ["Việc chuyển giao điều khiển giữa hai CPU được thực hiện tức thời ngay "
       "khi CPU chính đạt đến trạng thái MC3.",
       "Chế độ hỏng duy nhất còn có thể xảy ra sau khi một trong hai cảm biến "
       "hỏng là hỏng của cảm biến còn lại.",
       "CPU dự phòng chỉ có thể hỏng sau khi nó bắt đầu vận hành."],
      ["The transfer of control between the two CPUs is made instantly once "
       "the Main CPU reaches state MC3.",
       "The only other failure mode possible after the failure of one of the "
       "sensors is the failure of the other sensor.",
       "The Backup CPU can only fail after it begins operating."],
      ordered=True)

    H(b, lang, "Các sơ đồ chuyển tiếp Markov",
      "Markov transition diagrams", level=3)

    P(b, lang,
      "Hình 2 trình bày sơ đồ chuyển tiếp Markov cho van nước cấp và Hình 3 "
      "trình bày sơ đồ chuyển tiếp Markov cho cả CPU chính và CPU dự phòng.",
      "Figure 2 presents the Markov transition diagram for the Feedwater "
      "Valve, and Figure 3 presents the Markov transition diagram for both "
      "the Main CPU and the Backup CPU.")

    FIG(b, 2, F.fig_f02(), lang)
    FIG(b, 3, F.fig_f03(), lang)

    H(b, lang, "Phương trình vi phân và nghiệm sai phân hữu hạn",
      "Differential equations and finite-difference solution", level=3)

    P(b, lang,
      "Từ các sơ đồ chuyển tiếp, các hệ phương trình vi phân được thu được. "
      "Các hệ phương trình vi phân này được giải bằng phương pháp sai phân "
      "hữu hạn. Cần xác định một bước thời gian, phải như nhau cho cả hai sơ "
      "đồ chuyển tiếp. Bước thời gian phải thỏa mãn điều kiện của Phương "
      "trình (1):",
      "From the transition diagrams, sets of differential equations are "
      "obtained. These sets of differential equations were solved using the "
      "finite difference method. A time step, identical for both transition "
      "diagrams, must be defined. The time step must respect the following "
      "condition of Eq. (1):")
    E(b, lang, "Δt ≤ 1/λ", "Δt ≤ 1/λ", num="1")

    P(b, lang,
      "Do đó, vì tỷ lệ chuyển tiếp lớn nhất của toàn hệ thống là "
      "3,4 × 10<sup>−5</sup> hỏng/h, bước thời gian phải thỏa mãn Phương "
      "trình (2):",
      "Therefore, since the largest transition rate of the whole system is "
      "3.4 × 10<sup>−5</sup> failures/h, the time step must respect Eq. (2):")
    E(b, lang,
      "λ<sup>VPC</sup><sub>1</sub> + λ<sup>VPC</sup><sub>2</sub> = 3.4 × 10<sup>−5</sup> failures/h"
      "<br>Δt ≤ 29411.76 h",
      "λ<sup>VPC</sup><sub>1</sub> + λ<sup>VPC</sup><sub>2</sub> = 3.4 × 10<sup>−5</sup> failures/h"
      "<br>Δt ≤ 29411.76 h",
      num="2")

    P(b, lang,
      "Tuân thủ điều kiện này, bước thời gian được chọn là 10 h. Giá trị này "
      "được chọn vì nó đủ dài để có thể quan sát các thay đổi trong hành vi "
      "của hệ thống và đủ nhỏ để tính đến các thay đổi trong kịch bản vận "
      "hành.",
      "Respecting this condition, the time step was chosen to be 10 h. This "
      "value was chosen because it was long enough for changes in system "
      "behaviour to be observed and small enough to account for changes in "
      "the operating scenario.")

    H(b, lang,
      "Phân vùng CCMT và không gian trạng thái biến được điều khiển",
      "CCMT partitioning and the controlled variables state space", level=3)

    P(b, lang,
      "Giai đoạn tiếp theo là áp dụng CCMT cho hệ thống. Bước đầu tiên là "
      "phân vùng Không gian trạng thái biến được điều khiển (CVSS); biến được "
      "điều khiển duy nhất trong ví dụ này là mức nước của máy phát hơi "
      "nước. Bảng 10 cho thấy các ô CVSS được chọn cho nghiên cứu này. Các ô "
      "này sau đó được chia tiếp thành bốn ô con (P = 4).",
      "The next stage is applying CCMT to the system. Its first step is "
      "partitioning the Controlled Variables State Space (CVSS); the sole "
      "Controlled Variable in this example is the steam generator water "
      "level. Table 10 shows the CVSS cells chosen for this study. These "
      "cells are subsequently divided into four subcells (P = 4).")

    TBL(b, lang, _T10_HEAD_VI, _T10_HEAD_EN,
        _T10_ROWS_VI if lang == "vi" else _T10_ROWS_EN,
        caption_vi="Bảng 10.10 · Các ô của CVSS",
        caption_en="Table 10.10 · Cells of the CVSS")

    NOTE(b, lang,
      "Lưu ý về nguồn: Bảng 10 in đơn vị “cm” cho các hàng j = 5 và j = 6 "
      "(12,7 cm &lt; x ≤ 13,2 cm; x &gt; 13,2 cm), trong khi các hàng j = 1–4 "
      "dùng “m”. Đây là cách in của tài liệu gốc; chúng tôi giữ nguyên thay "
      "vì tự ý đổi đơn vị.",
      "Source note: Table 10 prints the unit “cm” in rows j = 5 and j = 6 "
      "(12.7 cm &lt; x ≤ 13.2 cm; x &gt; 13.2 cm), while rows j = 1–4 use "
      "“m”. This is as printed in the original source; we preserve it rather "
      "than silently converting the unit.")

    P(b, lang,
      "Khi các ô con đã được định nghĩa, có thể thu được xác suất "
      "g(j|j′, nc′, nv′, k) — tức là xác suất để mức nước đi từ ô V<sub>j′</sub> "
      "tới ô V<sub>j</sub>, biết rằng nó ở ô V<sub>j′</sub>, các CPU ở trạng "
      "thái nc′ và van ở trạng thái nv′ tại thời điểm t = k·Δt. Mô phỏng hệ "
      "thống được dùng cho mục đích này.",
      "Once the subcells are defined, the probability g(j|j′, nc′, nv′, k) "
      "— that is, the probability that the water level goes from cell "
      "V<sub>j′</sub> to cell V<sub>j</sub>, given that it was at cell "
      "V<sub>j′</sub>, the CPUs were in state nc′ and the valve was in state "
      "nv′ at instant t = k·Δt — may be obtained. Simulation of the system is "
      "used for this purpose.")

    P(b, lang,
      "Mô phỏng được điều chỉnh sao cho các CPU ở trạng thái nc′, van ở trạng "
      "thái nv′ và mức nước ban đầu ở điểm giữa của mỗi ô con của "
      "V<sub>j′</sub>. Số A lần đi đến ô V<sub>j</sub> được quan sát và "
      "g(j|j′, nc′, nv′, k) được thu được qua Phương trình (3):",
      "The simulation is adjusted so that the CPUs are in state nc′, the "
      "valve in state nv′ and the initial water level is at the midpoint of "
      "each subcell of V<sub>j′</sub>. The number A of arrivals at cell "
      "V<sub>j</sub> is observed and g(j|j′, nc′, nv′, k) is obtained through "
      "Eq. (3):")
    E(b, lang,
      "g(j|j′, nc′, nv′, k) = A/P",
      "g(j|j′, nc′, nv′, k) = A/P",
      num="3")

    P(b, lang,
      "Xác suất xảy ra các sự kiện đỉnh và độ tin cậy của hệ thống được thu "
      "được từ các phương trình sau.",
      "The probability of occurrence of Top Events and the reliability of "
      "the system are obtained from the following equations.")

    P(b, lang,
      "Xác suất để hệ thống ở ô V<sub>j</sub> tại t = (k+1)·Δt, biết rằng nó "
      "ở ô V<sub>j′</sub> tại thời điểm t = k·Δt, là [4]:",
      "The probability that the system is in cell V<sub>j</sub> at "
      "t = (k+1)·Δt, given that it was in cell V<sub>j′</sub> at time "
      "t = k·Δt, is [4]:")
    E(b, lang,
      "q<sub>j</sub>(k+1|j′,k) = Σ<sub>n′=1</sub><sup>N</sup> g(j|j′,n′,k) h<sub>n′</sub>(k)",
      "q<sub>j</sub>(k+1|j′,k) = Σ<sub>n′=1</sub><sup>N</sup> g(j|j′,n′,k) h<sub>n′</sub>(k)",
      num="4")

    P(b, lang,
      "trong đó h<sub>n′</sub>(k) là xác suất để thành phần ở trạng thái n′ "
      "tại t = k, thu được từ mô hình Markov. Do đó:",
      "where h<sub>n′</sub>(k) is the probability that the component was in "
      "state n′ at t = k, obtained from the Markov model. Therefore:")
    E(b, lang,
      "p<sub>j</sub>(k+1) = Σ<sub>j′=1</sub><sup>J</sup> g(j,k+1|j′,k) p<sub>j′</sub>(k)",
      "p<sub>j</sub>(k+1) = Σ<sub>j′=1</sub><sup>J</sup> g(j,k+1|j′,k) p<sub>j′</sub>(k)",
      num="5")

    P(b, lang,
      "Vì các ô bao phủ toàn bộ CVSS và loại trừ lẫn nhau đồng thời đầy đủ, "
      "có thể khẳng định rằng:",
      "Since the cells cover the whole CVSS and are mutually exclusive and "
      "exhaustive, it is possible to state that:")
    E(b, lang,
      "Σ<sub>j=1</sub><sup>J</sup> p<sub>j</sub>(k) = 1",
      "Σ<sub>j=1</sub><sup>J</sup> p<sub>j</sub>(k) = 1",
      num="6")

    P(b, lang,
      "Sau khi đã xác định các sự kiện đỉnh, tức là các ô mà tại đó hệ thống "
      "được coi là hỏng (V<sub>i</sub>), có thể thu được xác suất hệ thống "
      "hỏng tại một thời điểm:",
      "Having defined the Top Events, that is, the cells in which the system "
      "is considered failed (V<sub>i</sub>), it is possible to obtain the "
      "probability that the system is failed at an instant:")
    E(b, lang,
      "p<sub>ET</sub>(k) = Σ<sub>i=1</sub><sup>I</sup> p<sub>i</sub>(k)",
      "p<sub>ET</sub>(k) = Σ<sub>i=1</sub><sup>I</sup> p<sub>i</sub>(k)",
      num="7")

    P(b, lang,
      "Do đó, độ tin cậy của hệ thống có thể được thu được từ:",
      "Therefore, the reliability of the system can be obtained from:")
    E(b, lang,
      "R(k) = 1 − Σ<sub>i=1</sub><sup>I</sup> p<sub>i</sub>(k) = 1 − p<sub>ET</sub>(k)",
      "R(k) = 1 − Σ<sub>i=1</sub><sup>I</sup> p<sub>i</sub>(k) = 1 − p<sub>ET</sub>(k)",
      num="8")

    H(b, lang, "Xác suất xảy ra sự kiện đỉnh",
      "Top-event probability", level=3)

    TBL(b, lang, _T11_HEAD, _T11_HEAD, _T11_ROWS,
        caption_vi="Bảng 10.11 · Xác suất xảy ra một sự kiện đỉnh",
        caption_en="Table 10.11 · Probability of occurrence of a top event")

    P(b, lang,
      "Bảng 11 và Hình 4 trình bày xác suất xảy ra sự kiện đỉnh thu được, còn "
      "Bảng 12 và Hình 5 trình bày độ tin cậy của hệ thống thu được.",
      "Table 11 and Figure 4 present the resulting Top Event occurrence "
      "probability, while Table 12 and Figure 5 present the resulting "
      "reliability of the system.")

    FIG(b, 4, F.fig_f04(), lang)

    return b
