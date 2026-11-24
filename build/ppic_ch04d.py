# -*- coding: utf-8 -*-
"""Chapter 4, Instrument Calibration Monitoring (EN/VI bilingual).

Source: decoded lines 2077-2280 of ``work/ppic_raw.txt`` (PDF pp. 80-87,
printed pp. 64-71).  Contains the sensor-validation and calibration-reduction
prose, the fuzzy deviation (delta), frequency (tau) and status (s) variables,
the three printed equations (1), (2) and (4) -- the source prints no (3) --
and Tables 3 and 4 plus Figures 8-11.
"""

import ppicfig4 as F
from ppic_ch04_lib import H, P, L, E, FIG, TBL, NOTE

# Figure 8 comes from the ppicfig4_b supplier.  In a partial build that
# supplier may not be integrated yet; a neutral placeholder keeps section()
# callable until the real vector figure is available.  The real supplier
# always wins when it has already been registered.
if not hasattr(F, "fig_f08"):
    from ppicfig4_common import _mk

    _PLACEHOLDER_8 = _mk(
        8, [],
        "Universe of discourse for the deviation (δ) fuzzy input variable",
        "Tập luận giải cho biến đầu vào mờ độ lệch (δ)",
        "Universe of discourse for the deviation (δ) fuzzy input variable",
        "Đồ thị các hàm thuộc nhỏ, trung bình và lớn theo độ lệch σ",
        "Membership functions for small, medium and large deviations versus σ")
    F.fig_f08 = lambda: _PLACEHOLDER_8

# ---------------------------------------------------------------- Table 3
# Printed column order: rule number, six deviation/frequency pairs,
# four status variables.  R-bar denotes "not rare", C-bar "not consistent".
_T3_HEAD = ["R", "δ₁₂", "τ₁₂", "δ₁₃", "τ₁₃", "δ₁₄", "τ₁₄",
            "δ₂₃", "τ₂₃", "δ₂₄", "τ₂₄", "δ₃₄", "τ₃₄",
            "s₁", "s₂", "s₃", "s₄"]

_T3_ROWS = [
    ["1",  "L", "R̄", "",   "",  "",   "",  "",  "",  "",  "",  "",  "",  "I",  "I",  "",   ""],
    ["2",  "",  "",   "L", "R̄", "",   "",  "",  "",  "",  "",  "",  "",  "I",  "",   "I",  ""],
    ["3",  "",  "",   "",  "",  "L",  "R̄", "",  "",  "",  "",  "",  "",  "I",  "",   "",   "I"],
    ["4",  "",  "",   "",  "",  "",   "",  "L", "R̄", "",  "",  "",  "",  "",  "I",  "I",  ""],
    ["5",  "",  "",   "",  "",  "",   "",  "",  "",  "L", "R̄", "",  "",  "",  "I",  "",   "I"],
    ["6",  "",  "",   "",  "",  "",   "",  "",  "",  "",  "",  "L", "R̄", "",  "",  "I",  "I"],
    ["7",  "S", "F",  "",  "",  "",   "",  "",  "",  "",  "",  "",  "",  "C",  "C",  "",   ""],
    ["8",  "",  "",   "S", "F",  "",   "",  "",  "",  "",  "",  "",  "",  "C",  "",   "C",  ""],
    ["9",  "",  "",   "",  "",  "S",  "F",  "",  "",  "",  "",  "",  "",  "C",  "",   "",   "C"],
    ["10", "",  "",   "",  "",  "",   "",  "S", "F",  "",  "",  "",  "",  "",  "C",  "C",  ""],
    ["11", "",  "",   "",  "",  "",   "",  "",  "",  "S", "F",  "",  "",  "",  "C",  "",   "C"],
    ["12", "",  "",   "",  "",  "",   "",  "",  "",  "",  "",  "S", "F",  "",  "",  "C",  "C"],
    ["13", "M", "R̄", "",  "",  "",   "",  "",  "",  "",  "",  "",  "",  "C̄", "C̄", "",   ""],
    ["14", "",  "",   "M", "R̄", "",   "",  "",  "",  "",  "",  "",  "",  "C̄", "",   "C̄", ""],
    ["15", "",  "",   "",  "",  "M",  "R̄", "",  "",  "",  "",  "",  "",  "C̄", "",   "",   "C̄"],
    ["16", "",  "",   "",  "",  "",   "",  "M", "R̄", "",  "",  "",  "",  "",  "C̄", "C̄", ""],
    ["17", "",  "",   "",  "",  "",   "",  "",  "",  "M", "R̄", "",  "",  "",  "C̄", "",   "C̄"],
    ["18", "",  "",   "",  "",  "",   "",  "",  "",  "",  "",  "M", "R̄", "",  "",  "C̄", "C̄"],
]

_T4_HEAD_VI = ["Cặp tín hiệu",
               "Trước ngày 200 — Độ lệch (δ)",
               "Trước ngày 200 — Tần suất xuất hiện (τˢ, τᴹ, τᴸ)",
               "Sau ngày 200 — Độ lệch (δ)",
               "Sau ngày 200 — Tần suất xuất hiện (τˢ, τᴹ, τᴸ)"]
_T4_HEAD_EN = ["Signal pair",
               "Before day 200 — Deviation (δ)",
               "Before day 200 — Frequency of occurrence (τˢ, τᴹ, τᴸ)",
               "After day 200 — Deviation (δ)",
               "After day 200 — Frequency of occurrence (τˢ, τᴹ, τᴸ)"]
_T4_ROWS = [
    ["1-2", "10.4", "0%, 16%, 99%",  "4.7", "32%, 100%, 0%"],
    ["1-3", "12.2", "0%, 4.5%, 98%", "3.5", "100%, 100%, 0%"],
    ["1-4", "12.8", "0%, 4%, 100%",  "6.8", "0%, 100%, 76%"],
    ["2-3", "2.24", "100%, 37%, 0%", "1.2", "100%, 4%, 0%"],
    ["2-4", "2.46", "100%, 30%, 0%", "2.1", "100%, 6%, 0%"],
    ["3-4", "2.36", "100%, 19%, 0%", "3.3", "100%, 100%, 0%"],
]


def section(lang):
    b = []

    H(b, lang,
      "GIÁM SÁT HIỆU CHUẨN THIẾT BỊ",
      "INSTRUMENT CALIBRATION MONITORING")

    P(b, lang,
      "Phần này trình bày ví dụ chi tiết hơn về việc áp dụng logic mờ để giám "
      "sát tình trạng của thiết bị đo trong quá trình. Ở đây đi sâu vào cách "
      "dùng logic mờ cho một ứng dụng cụ thể, đặc biệt bằng cách trình bày các "
      "luật tiêu biểu, hàm thuộc mờ và kết quả thực tế từ việc áp dụng FLDM "
      "vào dữ liệu thu được từ một nhà máy điện hạt nhân đang vận hành.",
      "This section presents a more detailed example of the application of fuzzy "
      "logic to health monitoring of process instrumentation. Here we detail "
      "the use of fuzzy logic for a specific application, in particular by showing "
      "representative rules, fuzzy membership function, and actual results from "
      "the application of the FLDM to data from an operating nuclear power "
      "plant.")

    # ---------------------------------------------------- Calibration Reduction
    H(b, lang, "Giảm hiệu chuẩn", "Calibration Reduction", level=3)

    P(b, lang,
      "Trong bất kỳ quá trình nào, điều kiện của hệ thống phải được đo để đạt "
      "được cấu hình vận hành mong muốn. Một phần nỗ lực nhằm cải thiện giám "
      "sát, điều khiển, an toàn và bảo trì quá trình bằng hệ thống máy tính tự "
      "động phải được dành để bảo đảm độ chính xác và độ tin cậy của các điều "
      "kiện quá trình được chỉ thị bởi hệ thống thiết bị đo [40]. Các chức năng "
      "chẩn đoán và giám sát tình trạng phải được thực hiện dựa trên các tín "
      "hiệu quá trình đã được kiểm chứng. Kiểm chứng cảm biến (hay phát hiện lỗi "
      "thiết bị đo) là việc xác định xem một chỉ thị quá trình có cung cấp kết "
      "quả đọc đáng tin cậy hay không. Động lực thực hiện kiểm chứng cảm biến "
      "nằm ở cả mối quan tâm về an toàn lẫn lợi ích kinh tế có thể đạt được. Các "
      "tín hiệu được kiểm chứng đúng cách làm tăng khả năng sẵn có của nhà máy "
      "và độ tin cậy của các hành động do người vận hành thực hiện.",
      "In any process, the system conditions must be measured in order to achieve "
      "the desired operating configuration. Part of the effort in improving process "
      "monitoring, control, safety, and maintenance using automated computer "
      "systems must be dedicated to insuring the accuracy and reliability of the "
      "indicated process conditions as obtained from the instrumentation system "
      "[40]. Diagnostic functions and condition monitoring must be performed "
      "based on validated process signals. Sensor validation (or instrument fault "
      "detection) is a determination whether a process indicator is providing "
      "a reliable reading. The incentives for performing sensor validation lie "
      "in both concerns for safety and the economic returns possible. Properly "
      "validated signals increase plant availability and the reliability of operator "
      "actions.")

    P(b, lang,
      "Nhiều cách tiếp cận đã được phát triển để thực hiện kiểm chứng tín hiệu. "
      "Nhiều phương pháp bắt nguồn từ ngành hàng không vũ trụ và hạt nhân. Hầu "
      "hết các kỹ thuật dùng quy trình hai giai đoạn: (1) tạo phần dư và (2) ra "
      "quyết định dựa trên ngưỡng cứng. Các tín hiệu phần dư (thường gần bằng "
      "không) lệch khỏi không theo những cách đặc trưng khi xảy ra một số lỗi "
      "nhất định. Các phương pháp tạo phần dư gồm:",
      "Various approaches have been developed to perform signal validation. "
      "Many methods originated from the aerospace and nuclear industries. "
      "Most techniques employ a two-stage process: (1) generation of residuals "
      "and (2) decision making based upon hard thresholds. The residual "
      "signals (nominally near zero) deviate from zero in characteristic ways "
      "when certain faults occur. The residual generation methodologies include "
      "the following.")

    L(b, lang,
      ["Không gian parity (xem bài tổng quan của Patton và Chen [41])",
       "Bộ quan sát chuyên dụng [42, 43]",
       "Bộ lọc Kalman [44, 45]"],
      ["Parity space (see review by Patton and Chen [41])",
       "Dedicated observers [42, 43]",
       "Kalman filters [44, 45]"],
      ordered=True)

    P(b, lang,
      "Việc ra quyết định dựa trên nhiều phép thử, trong đó có tỷ lệ khả năng "
      "tổng quát (GLR) [46–48], phép thử tỷ lệ xác suất tuần tự (SPRT) và các "
      "đặc tính đổi mới (kiểm tra tính trắng, giá trị trung bình, hiệp phương "
      "sai, chi bình phương, v.v.), áp dụng cho phần dư.",
      "The decision making is based upon various tests, including the generalized "
      "likelihood ratio (GLR) [46–48], sequential probability ratio test (SPRT), "
      "and innovation properties (tests for whiteness, mean, covariance, chi-"
      "square, etc.), applied to the residuals.")

    P(b, lang,
      "Có hai loại lỗi chính được kiểm chứng cảm biến giải quyết: (1) phát hiện "
      "lỗi mới phát sinh (thảm họa) và (2) phát hiện trôi hiệu chuẩn của thiết "
      "bị đo. Ví dụ, nếu hiệu chuẩn của thiết bị bị trôi theo thời gian, có thể "
      "thực hiện bảo trì phòng ngừa cho kênh thiết bị đó trước khi hỏng hoàn "
      "toàn. Khía cạnh bảo trì dự báo này có lợi ích là hỗ trợ lập lịch bảo trì, "
      "bao gồm khả năng đặt trước linh kiện, cũng như khả năng, trong trường hợp "
      "nghiêm trọng nhất, ngăn ngừa việc nhà máy điện hạt nhân bị dừng — tùy "
      "theo bản chất có thể phải nộp Báo cáo Sự kiện Người được cấp phép (LER) "
      "cho Ủy ban Điều hòa Hạt nhân Hoa Kỳ, một tình huống cần tránh.",
      "Two primary types of failure are addressed by sensor validation: (1) "
      "incipient (catastrophic) failure detection and (2) detection of instrument "
      "calibration drift. For instance, if instrument calibration is drifting over "
      "time, then preventive maintenance on the instrument channel may be "
      "performed before complete failure. This predictive maintenance aspect "
      "has the benefit of a maintenance scheduling aid, including the ability "
      "to preorder components, as well as the possibility in the severest case "
      "of preventing a nuclear plant trip, which depending on the nature could "
      "require the filing of a Licensee Event Report (LER) with the USA Nuclear "
      "Regulatory Commission—a situation to be avoided.")

    P(b, lang,
      "Giảm hiệu chuẩn là một ứng dụng cụ thể của kiểm chứng cảm biến. Giảm hiệu "
      "chuẩn không loại bỏ nhu cầu hiệu chuẩn thiết bị, mà chỉ giảm bớt công "
      "việc liên quan. Lợi ích rõ ràng của giám sát hiệu chuẩn là giảm nhu cầu "
      "nhân công nhờ khối lượng công việc ít đi. Vì một số cảm biến thường không "
      "thể tiếp cận được, công việc hiệu chuẩn lại có thể rơi đúng vào giai "
      "đoạn nhà máy đang bảo trì bận rộn — khi nhân lực đã trở nên khan hiếm. "
      "Tại nhà máy điện hạt nhân, giảm hiệu chuẩn cũng có thể rút ngắn thời "
      "gian làm việc trong khu vực có bức xạ, từ đó giảm liều chiếu xạ cho nhân "
      "viên.",
      "Calibration reduction is a particular application of sensor validation. "
      "Calibration reduction does not eliminate the need to perform instrument "
      "calibration, but lessens the effort involved. An obvious benefit of "
      "calibration monitoring is reduced manpower requirements due to the "
      "lessened workload. Since some sensors are normally inaccessible, this "
      "recalibration effort may come during an already busy plant outage—"
      "when labor is already at a premium. In a nuclear power plant, calibration "
      "reduction can also lower the amount of time spent in radiation areas, "
      "thereby reducing personnel exposure.")

    # ------------------------------------------- Fuzzy Logic Diagnostic Approach
    H(b, lang, "Cách tiếp cận chẩn đoán bằng logic mờ",
      "Fuzzy Logic Diagnostic Approach", level=3)

    P(b, lang,
      "Xét trường hợp có sẵn nhiều kết quả đọc của một biến quá trình nhất "
      "định, trực tiếp từ các cảm biến dự phòng vật lý và/hoặc gián tiếp thông "
      "qua các quan hệ phân tích hoặc thực nghiệm. Để bắt đầu phân tích, độ lệch "
      "tuyệt đối giữa mọi cặp tín hiệu có thể được tính theo:",
      "Consider that multiple readings of a given process variable are available "
      "directly with physically redundant sensors and/or indirectly via analytical "
      "or empirical relationships. To begin the analysis, an absolute deviation "
      "between all possible signal pairings is calculated according to")

    E(b, lang,
      "δᵢⱼ = |xᵢ − xⱼ|   for i = 1, 2, …, N;   i ≠ j",
      "δᵢⱼ = |xᵢ − xⱼ|   for i = 1, 2, …, N;   i ≠ j",
      num="1")

    P(b, lang,
      "trong đó N là số cảm biến dự phòng và xᵢ là phép đo từ cảm biến thứ i tại "
      "một thời điểm đã cho. Miền giá trị có thể, tức là tập luận giải, của δ "
      "thay đổi từ không khi cặp tín hiệu hoàn toàn đồng "
      "nhất đến dải đo của thiết bị, R, là độ lệch lớn nhất có thể. Tập luận "
      "giải này của δ được lượng hóa thành một số giá trị tập mờ chồng lấp lên "
      "nhau:",
      "where N is the number of redundant sensors and xᵢ is the measurement "
      "from the ith sensor at a given time instant. The range of possible values, "
      "that is, the universe of discourse, for δ varies from zero, when the signal "
      "pair is in complete agreement, to the instrument range, R, which is the "
      "maximum possible deviation. This universe of discourse for δ is quantized "
      "into several overlapping fuzzy-set values:")

    E(b, lang,
      "S(small δ): [0, 5σ]   M(medium δ): [3σ, 9σ]   L(large δ): [7σ, R]",
      "S(small δ): [0, 5σ]   M(medium δ): [3σ, 9σ]   L(large δ): [7σ, R]",
      num="2")

    P(b, lang,
      "Cụ thể, độ lệch này được chuẩn hóa dựa trên độ lệch chuẩn của tín hiệu, "
      "σ, dùng ba vùng: (1) độ lệch nhỏ, (2) độ lệch trung bình và (3) độ lệch "
      "lớn, như trong Hình 8.",
      "In particular, this deviation is normalized based on the signal standard "
      "deviation, σ, using three regions: (1) small, (2) medium, and (3) large "
      "deviations, as shown in Figure 8.")
    FIG(b, 8, F.fig_f08(), lang)

    P(b, lang,
      "Khi thực hiện giám sát hiệu chuẩn thiết bị, hai kết quả quan trọng là: "
      "(1) chỉ thị tức thời về cách một cảm biến hoạt động so với các cảm biến "
      "dự phòng của nó, và (2) xác định dài hạn xem một kênh thiết bị có hoạt "
      "động đúng hay không. Sự hiện diện của các dao động ngẫu nhiên đòi hỏi "
      "một số lượng mẫu dữ liệu có ý nghĩa thống kê, lấy trong một khoảng thời "
      "gian đại diện, nhằm giảm thiểu xác suất báo động giả.",
      "In performing instrument calibration monitoring, two results are "
      "important: (1) an instantaneous indication of how a sensor is performing "
      "relative to its redundant units, and (2) a long-term determination of "
      "whether an instrument channel is functioning properly. The presence of "
      "random fluctuations requires a statistically significant number of data "
      "samples taken over a representative period to minimize the false alarm "
      "probability.")

    P(b, lang,
      "Do đó, không chỉ phải giám sát độ lệch của cảm biến, mà còn phải giám "
      "sát tần suất xuất hiện của các độ lệch nhỏ, trung bình và lớn. Vì vậy, "
      "một biến đầu vào mờ thứ hai — tần suất, τ, mà tại đó loại độ lệch đã "
      "được quan sát thấy — được đưa vào. Trong thực tế, giá trị của τ thu được "
      "bằng cách duy trì một giá trị trung bình chạy trên một số mẫu liên tiếp "
      "tính đến thời điểm hiện tại, khi quyết định trạng thái được đưa ra. Đối "
      "với τ, tập luận giải trải từ 0% đến 100%, và các giá trị tập mờ là (xem "
      "Hình 9):",
      "Therefore, not only must the sensor deviations be monitored, but also the "
      "frequency of the small, medium and large deviations. Hence, a second "
      "fuzzy input variable—the frequency, τ, at which the deviation type has "
      "been observed—is introduced. In practice, the value of τ is obtained by "
      "maintaining a running average over a number of contiguous samples up "
      "to the current sample time, when the status decision is made. For τ, the "
      "universe of discourse ranges from 0% to 100%, and the fuzzy set values "
      "are (see Figure 9):")
    FIG(b, 9, F.fig_f09(), lang)

    P(b, lang,
      "Như vậy, có ba giá trị tần suất mờ (τ) cho mỗi độ lệch. Sau đó các luật "
      "được thiết lập để xác định xem các tín hiệu có nhất quán với nhau hay "
      "không. Thuật toán kiểm tra tính nhất quán có thể cho một số kết quả sau:",
      "Thus, there are three fuzzy frequency (τ) values for each deviation. "
      "Rules are then implemented to determine whether the signals are consistent "
      "with respect to one another. The consistency checking algorithm may "
      "find several possible results:")

    L(b, lang,
      ["Tín hiệu nhất quán: Khi tất cả các tín hiệu đồng nhất với nhau, thì "
       "hoặc (a) tất cả cảm biến đều tốt, hoặc (b) tất cả thiết bị đều bị lệch "
       "hiệu chuẩn (ví dụ do trôi tín hiệu).",
       "Tín hiệu nhất quán một phần: Nếu đa số kết quả đọc của cảm biến nhất "
       "quán với nhau, thì nhóm tín hiệu thiểu số bị nghi là đã trải qua sự "
       "dịch chuyển hiệu chuẩn. Trên thực tế, người ta biết rằng ít nhất một "
       "cảm biến có thể cần thay thế hoặc hiệu chuẩn lại, nên có thể lên kế "
       "hoạch bảo trì tương ứng.",
       "Tín hiệu không nhất quán: Trong trường hợp này, nhiều cảm biến có thể "
       "cần thay thế hoặc hiệu chuẩn lại. Chính trong những tình huống như vậy "
       "(hoặc khi chỉ có một hoặc hai tín hiệu dự phòng) thì một ước tính độc "
       "lập về trạng thái quá trình mới hữu ích, tức là một mô hình quá trình "
       "phân tích hoặc thực nghiệm cung cấp một phép đo ảo để so sánh với các "
       "giá trị ghi nhận."],
      ["Signals Consistent: When all the signals are in agreement with "
       "one another, then either (a) all the sensors are good, or (b) all "
       "the instruments are out of calibration (e.g., due to signal drift).",
       "Signals Partially Consistent: If the majority of sensor readings "
       "are consistent with respect to one another, then the minority "
       "group of signals is suspected of having experienced a "
       "calibration shift. In fact, it is known that at least one sensor "
       "may need to be replaced or recalibrated, so maintenance may "
       "be planned accordingly.",
       "Signals Inconsistent: In this case, multiple sensors may require "
       "replacement or recalibration. It is in situations such as this (or in "
       "those instances where only one or two redundant signals exist) "
       "that an independent estimate of the process state is useful, that "
       "is, an analytical or empirical process model provides a virtual "
       "measurement with which to compare the recorded values."],
      ordered=True)

    P(b, lang,
      "Vì vậy, bộ kiểm chứng mờ phân loại một tín hiệu là nhất quán, nhất quán "
      "một phần hoặc không nhất quán. Biến mờ trạng thái là trạng thái hợp lệ "
      "của tín hiệu, x, với các giá trị tập mờ là:",
      "The fuzzy validator therefore classifies a signal as being consistent, "
      "partially consistent, or inconsistent. The status fuzzy variable is the "
      "signal validity state, x, with fuzzy set values of")

    E(b, lang,
      "C(consistent): [0, 0.5]   P(partially consistent): [0.25, 0.75]   I(inconsistent): [0.5, 1]",
      "C(consistent): [0, 0.5]   P(partially consistent): [0.25, 0.75]   I(inconsistent): [0.5, 1]",
      num="4")

    P(b, lang,
      "được biểu diễn trong Hình 10.",
      "which are graphed in Figure 10.")
    FIG(b, 10, F.fig_f10(), lang)

    P(b, lang,
      "Các luật liên kết trạng thái tín hiệu với độ lệch giữa các kết quả đọc "
      "cảm biến và tần suất mà tại đó các độ lệch này đã được quan sát. Tập luật "
      "phải được thiết lập sao cho một kết quả trạng thái được đưa ra cho mỗi "
      "tín hiệu. Hơn nữa, các luật được xây dựng để xét đến ảnh hưởng của một "
      "cảm biến không nhất quán đến độ lệch và tần suất xuất hiện của một thiết "
      "bị đã hiệu chuẩn. Ví dụ, trong một phép so sánh cặp tín hiệu giữa một "
      "kết quả đọc chính xác và một kết quả đọc không chính xác, ban đầu cả hai "
      "cảm biến có thể bị coi là không nhất quán với nhau.",
      "Rules associate the signal state with the deviation between the sensor "
      "readings, and the frequency at which those deviations have been observed. "
      "The rule set must be established such that a status result is issued for each "
      "signal. Furthermore, the rules are constructed to consider the effects that "
      "an inconsistent sensor has on the deviation and frequency of occurrence "
      "for a calibrated instrument. For example, in a signal pairing comparison "
      "between an accurate and an inaccurate reading, both sensors may initially "
      "be deemed inconsistent with respect to one another.")

    P(b, lang,
      "Với một nhóm ba cảm biến trở lên đo cùng một biến trạng thái, có thể cô "
      "lập lỗi cảm biến. Trong trường hợp bốn cảm biến dự phòng, có mười hai "
      "biến mờ trạng thái và bốn biến mờ trạng thái đầu ra. Có sáu độ lệch được "
      "tính toán (ví dụ δ₁₂ và δ₂₃) và mười tám biến mờ tần suất (ví dụ τ₁₂ˢ và "
      "τ₁₂ᴸ). Các luật, được thể hiện trong Bảng 3, phức tạp hơn các luật trong "
      "ví dụ ở Mục 3.2. Luật đầu tiên trong bảng có thể được đọc như một hệ quả "
      "mức tập.",
      "With a group of three or more sensors measuring the same state-variable, "
      "sensor fault isolation is possible. In the case of four redundant sensors, "
      "there are twelve state fuzzy variables and four fuzzy status variables. "
      "There are six deviations computed (e.g., δ₁₂ and δ₂₃), and eighteen "
      "frequency fuzzy variables (e.g., τ₁₂ˢ and τ₁₂ᴸ). The rules, which are "
      "shown in Table 3, are more extensive than those in the example of Section "
      "3.2. The first rule in the table may be read as the set level implication.")

    TBL(b, lang, _T3_HEAD, _T3_HEAD, _T3_ROWS,
        caption_vi="Bảng 4.3 — Luật giám sát hiệu chuẩn cho bốn cảm biến.",
        caption_en="Table 4.3 — Rules for the calibration monitoring of four sensors.")

    P(b, lang,
      "Nếu độ lệch, δ₁₂, lớn và tần suất xuất hiện của nó, τ₁₂ᴸ, không hiếm, thì "
      "trạng thái của cảm biến số 1, s₁, là không nhất quán và trạng thái của "
      "cảm biến số 2, s₂, là không nhất quán.",
      "If the deviation, δ₁₂, is large and its frequency of occurrence, τ₁₂ᴸ, "
      "is not rare, then the sensor #1 status, s₁, is inconsistent and the "
      "sensor #2 status, s₂, is inconsistent.")

    P(b, lang,
      "Các trọng số khác nhau được gán cho các luật. Cụ thể, sáu luật đầu tiên "
      "dùng hệ số trọng số 0,3 vì ảnh hưởng bất lợi mà một cảm biến hỏng duy "
      "nhất có thể có đối với kết quả kiểm tra tính nhất quán của các thiết bị "
      "đáng tin cậy. Trọng số đơn vị được áp dụng cho các luật 7 đến 12 vì tình "
      "huống nhất quán này có mức độ tin cậy cao. Sáu luật cuối có trọng số 0,6 "
      "vì sự xuất hiện của chúng là điều được kỳ vọng trước, xét đến các dao "
      "động thống kê hiện có trong một quá trình và tính biến đổi của điều kiện "
      "vận hành nhà máy.",
      "Different weights are assigned for the rules. In particular, the first six "
      "rules use a weighting factor of 0.3 because of the adverse effect that "
      "a single faulty sensor can have on the consistency checking results for "
      "reliable instruments. Unit weights are applied to Rules 7 through 12 since "
      "this situation of consistency has a high degree of confidence. The last six "
      "rules have a weight of 0.6 since their occurrence is to be expected given "
      "the statistical fluctuations present in a process and the variability of "
      "plant operating conditions.")

    P(b, lang,
      "Tính gọn của cơ sở luật và sự đơn giản trong cách áp dụng đồng thời các "
      "biến mờ độ lệch và tần suất cùng với các luật cho phép xử lý tín hiệu "
      "theo thời gian thực. Cách tiếp cận logic mờ cũng có khả năng đánh giá "
      "các tình huống mà trong đó các mô hình phân tích được sử dụng. Độ lệch "
      "giữa các ước tính của mô hình phân tích và các phép đo phần cứng có thể "
      "xảy ra do (1) lỗi của cảm biến đo biến trạng thái đang xét hoặc (2) bất "
      "thường trong một tín hiệu đầu vào gửi tới mô hình phân tích.",
      "The compactness of the rule base and the simplicity with which the "
      "deviations and frequency fuzzy variables are applied together with the "
      "rules allow signal processing in real time. The fuzzy logic approach "
      "is also capable of evaluating situations in which analytical models are "
      "employed. Deviations between analytical model estimates and hardware "
      "measurements can occur due to (1) a failure in the sensor measuring the "
      "state variable of interest or (2) an anomaly in an input signal sent to "
      "the analytical model.")

    P(b, lang,
      "Cơ sở của việc giảm hiệu chuẩn (nhưng không phải loại bỏ hoàn toàn) là "
      "so sánh chéo các phép đo quá trình dự phòng. Các kết quả đọc quá trình "
      "được giám sát liên tục — trong nhiều tuần chẳng hạn. Trong khoảng thời "
      "gian này, các tín hiệu hoặc là đồng nhất hoặc là không đồng nhất. Nếu "
      "(như người ta hy vọng) các tín hiệu dự phòng đồng nhất với nhau, có thể "
      "rút ra một trong hai kết luận: (1) tất cả tín hiệu đều chính xác hoặc (2) "
      "tất cả tín hiệu đều hỏng theo một chế độ nguyên nhân chung chẳng hạn như "
      "trôi hiệu chuẩn. Khi đó bài toán được thu gọn về việc kiểm chứng hiệu "
      "chuẩn của một trong các cảm biến dự phòng (kênh). Nếu thiết bị được kiểm "
      "tra chứng tỏ nằm trong thông số hiệu chuẩn, có thể kết luận các cảm biến "
      "(chưa được kiểm tra) còn lại cũng nằm trong thông số hiệu chuẩn và "
      "không cần hiệu chuẩn lại.",
      "The basis of the calibration reduction (but not total elimination) is the "
      "intercomparison of redundant process measurements. The process "
      "readings are monitored on a continuous basis—over weeks for instance. "
      "During this time period either the signals will agree or they will disagree. "
      "If (as one would hope), the redundant signals concur with one another, "
      "one of two conclusions can be surmised: (1) the signals are all accurate "
      "or (2) the signals have all failed by some common-cause mode such "
      "as calibration drift. The problem is then reduced to verification of the "
      "calibration of one of the redundant sensors (channels). Should the tested "
      "instrument prove to be within calibration specifications, it may be "
      "concluded that the remaining (untested) sensors are within calibration "
      "specifications and they do not require recalibration.")

    # ---------------------------------------- Calibration Reduction Example
    H(b, lang, "Ví dụ giảm hiệu chuẩn", "Calibration Reduction Example", level=3)

    P(b, lang,
      "Dữ liệu trong Hình 11 là các phép đo áp suất nồi áp ghi nhận tại một "
      "nhà máy điện nước áp suất (PWR) thương mại. Dùng dữ liệu của 200 ngày "
      "đầu, người ta trước tiên tính các độ lệch và tần suất xuất hiện cho các "
      "kết quả đọc áp suất này và đưa vào Bảng 4. Các giá trị đã được mờ hóa sau "
      "đó được đánh giá bằng một hệ thống mờ kiểu Mamdani, dùng suy diễn cực "
      "tiểu, tổng hợp bằng phép cộng và giải mờ bằng trọng tâm. Trong kết quả "
      "cho dữ liệu nồi áp này, chỉ sáu trong mười tám luật được kích hoạt. Bộ "
      "giám sát chẩn đoán mờ xác định chính xác rằng Tín hiệu 1 là một bộ "
      "chuyển đổi áp suất bị lệch hiệu chuẩn. Tín hiệu 2 được xác định là nhất "
      "quán, còn Tín hiệu 3 và 4 được xem là nhất quán một phần. Kiểm tra kỹ các "
      "luật 1–3 và 10–12 cho thấy trạng thái sau không hoàn toàn là hệ quả của "
      "sự không nhất quán của tín hiệu thứ nhất, vì các tín hiệu 2–4 không liên "
      "kết chặt với nhau thành một nhóm. Ảnh hưởng của cảm biến không nhất quán "
      "có thể được loại bỏ bằng cách áp dụng lại hệ thống mờ chỉ cho các tín "
      "hiệu 2–4. Không cần tính lại độ lệch hay tần suất xuất hiện, và một tập "
      "luật ba cảm biến nhỏ hơn được sử dụng.",
      "The data shown in Figure 11 are pressurizer pressure measurements "
      "recorded at a commercial pressurized water reactor (PWR). Using "
      "the first 200 days worth of data, the deviations and the frequencies "
      "of occurrence for these pressure readings were first calculated and "
      "are given in Table 4. The fuzzified values are then evaluated using a "
      "Mamdani style fuzzy system, which employs minimum implication, "
      "summation aggregation, and centroid defuzzification. In the results for "
      "these pressurizer data, only six of the eighteen rules were activated. The "
      "fuzzy diagnostic monitor accurately identifies that Signal 1 is an out-"
      "of-calibration pressure transducer. Signal 2 is identified as consistent, "
      "and Signals 3 and 4 are deemed partially consistent. A close examination "
      "of Rules 1–3 and 10–12 reveals that this latter status is not entirely a "
      "consequence of the first signal’s inconsistency, as Signals 2–4 are not "
      "tightly coupled as a group. The effect of the inconsistent sensor can be "
      "removed by reapplying the fuzzy system to only Signals 2–4. Neither the "
      "deviations nor the frequencies of occurrence have to be recomputed and "
      "a smaller, three-sensor rule set is used.")

    TBL(b, lang, _T4_HEAD_VI, _T4_HEAD_EN, _T4_ROWS,
        caption_vi="Bảng 4.4 — Độ lệch và tần suất xuất hiện tính được cho tín "
                   "hiệu áp suất nồi áp.",
        caption_en="Table 4.4 — Deviations and frequencies of occurrence "
                   "computed for pressurizer pressure signals.")
    FIG(b, 11, F.fig_f11(), lang)

    P(b, lang,
      "Vào khoảng ngày 200, cảm biến hỏng đã được hiệu chuẩn lại sao cho, khi "
      "nhìn vào dữ liệu của Hình 11 bằng mắt thường, nó trở nên nhất quán hơn "
      "với ba bộ chuyển đổi kia. Các độ lệch và tần suất xuất hiện cụ thể cho 50 "
      "ngày cuối cũng được đưa vào Bảng 4. Kết quả phân tích mờ kết luận rằng "
      "Tín hiệu 2 và 3 nhất quán, còn Tín hiệu 1 và 4 nhất quán một phần. Có "
      "thể kiểm chứng trực quan các kết quả này bằng cách nhận thấy Tín hiệu 1 "
      "và 4 là các giá trị ngoại lệ trong dữ liệu của Hình 11.",
      "At approximately day 200, the faulty sensor was recalibrated such that it "
      "(visually speaking when looking at the data of Figure 11) becomes more "
      "consistent with the other three transducers. The particular deviations and "
      "frequencies of occurrence for the last 50 days are also given in Table 4. "
      "The fuzzy analysis results conclude that Signals 2 and 3 are consistent, "
      "and that Signals 1 and 4 are partially inconsistent. These results can be "
      "visually verified by noting that Signals 1 and 4 are the outliers in the "
      "data of Figure 11.")

    return b
