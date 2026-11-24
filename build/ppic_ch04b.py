# -*- coding: utf-8 -*-
"""Book 9, Chapter 4 (part B) — Fuzzy Logic Diagnostic Monitoring, part 1.

Source: ppic_raw.txt lines 1785-1966 (PDF pp. 70-75, printed pp. 54-59).
Covers the overall FLDM scheme, the philosophical approach, Stage 1 signal
processing modules, the four temperature signals with signal noise, the fuzzy
noise detector and the simple rule set for signal noise assessment.

Source Figures 2, 3 and 4 are redrawn in the ppicfig4_a supplier and inserted
here as Figures 4.2, 4.3 and 4.4. Source Table 1 is transcribed as Table 4.1.
No numbered equations occur in this range.
"""
from ppic_ch04_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401
import ppicfig4 as F


def section(lang):
    b = []

    # ------------------------------------------- FUZZY LOGIC DIAGNOSTIC MONITORING
    H(b, lang,
      "GIÁM SÁT CHẨN ĐOÁN BẰNG LOGIC MỜ",
      "FUZZY LOGIC DIAGNOSTIC MONITORING")

    P(
        b, lang,
        "Các chương trình bảo trì dự đoán thường sử dụng các kỹ thuật xử lý tín hiệu "
        "để giám sát tình trạng của thiết bị và hệ thống cụ thể trong nhà máy. Những "
        "nỗ lực này có thể khai thác rất nhiều phương pháp xử lý tín hiệu số đã được "
        "phát triển và có thể hướng tới các đặc trưng lỗi cụ thể. Các cách tiếp cận "
        "này được thử thách trong việc thực hiện FDI và đặc trưng hóa bất thường, "
        "trong đó hai nhiệm vụ này được liệt kê theo thứ tự độ khó tăng dần.",
        "Predictive maintenance programs generally employ signal processing techniques "
        "to perform condition monitoring on particular plant equipment and systems. "
        "Such efforts have the potential to draw upon a plethora of digital signal "
        "processing methods which have been developed and can be targeted toward "
        "specific fault signatures. These approaches are challenged to perform FDI and "
        "anomaly characterization, where these two tasks are listed in order of "
        "increasing difficulty.")

    P(
        b, lang,
        "Hơn nữa, một số thuật toán FDI cung cấp chẩn đoán trực tiếp, áp dụng được cho "
        "nhiều loại bất thường, trong khi các cách tiếp cận FDI khác là những công cụ "
        "tính toán phức tạp dành riêng cho việc phân tích các chế độ hỏng cụ thể. Ví dụ, "
        "một số phương pháp hữu ích hơn trong việc đánh giá các lỗi đột ngột, trong khi "
        "những phương pháp khác lại nhắm đến các lỗi mới phát sinh. Tình huống này dẫn "
        "đến các bộ giám sát tình trạng thường chỉ dành cho một thiết bị đơn lẻ, với "
        "phần mềm có phạm vi áp dụng hạn chế đối với các chế độ hỏng mà một thành phần "
        "có thể gặp phải. Không thể kỳ vọng các công ty điện lực nhỏ và các tổ máy phát "
        "điện riêng lẻ có đủ nhân sự chuyên trách am hiểu và thành thạo mọi phương pháp "
        "FDI hiện có. Do đó, cần có một công cụ hỗ trợ vận hành dưới dạng hệ thống giám "
        "sát thông minh. Tình trạng này là động lực thúc đẩy sự phát triển của giám sát "
        "chẩn đoán bằng logic mờ dựa trên luật (FLDM) được trình bày ở đây.",
        "Furthermore, some FDI algorithms provide straightforward diagnostics with "
        "applicability to a variety of anomalies while other FDI approaches are complex "
        "computational tools dedicated to the analysis of specific failure modes. As a "
        "case in point, some methods are more useful for evaluating abrupt faults while "
        "others are intended for incipient failures. This situation leads to condition "
        "monitors that are often dedicated to a single piece of equipment and "
        "incorporating software with limited applicability in terms of the potential "
        "failure modes that a component may experience. Small electric utilities and "
        "individual generating units cannot be expected to employ a dedicated staff "
        "that is cognizant of and conversant with all the available FDI methods. "
        "Consequently, an operational aid in the form of an intelligent monitoring "
        "system is needed. This state of affairs is an impetus for the development of "
        "the rule-based fuzzy logic diagnostic monitoring (FLDM) to be described here.")

    # ------------------------------------------------------------- Philosophical Approach
    H(b, lang, "Cách tiếp cận triết học", "Philosophical Approach", level=3)

    P(
        b, lang,
        "Một khía cạnh của cách tiếp cận triết học trong phát triển FLDM là xem xét "
        "phương pháp thường được áp dụng khi một người bị ốm. Thông thường, bác sĩ trước "
        "tiên thực hiện nhiều biện pháp đơn giản (ví dụ, đo nhiệt độ cơ thể), sau đó có "
        "thể chỉ định thêm các xét nghiệm chẩn đoán (ví dụ, chụp X-quang) dựa trên đánh "
        "giá ban đầu về bệnh nhân. Quá trình suy nghĩ này dẫn đến một thuộc tính bổ sung "
        "của FLDM, nhằm cung cấp một bộ giám sát sức khỏe hiệu quả, cụ thể là đưa vào "
        "cơ sở dữ liệu thông tin về lịch sử vận hành của thiết bị, bao gồm dữ liệu độ tin "
        "cậy của nhà sản xuất và các hồ sơ bảo trì khác. Tương tự như hồ sơ bệnh nhân, "
        "các chữ ký cơ sở (khi thiết bị hoạt động bình thường, không có lỗi) được thu "
        "thập và lưu trữ để tham khảo và so sánh sau này.",
        "One facet of the philosophical approach taken in developing the FLDM was to "
        "consider the methodology often taken when a person is ill. Typically, a "
        "physician first employs a variety of simple measures (e.g., body temperature) "
        "and afterwards may order additional diagnostic tests (e.g., X-ray) to be "
        "performed based on the initial evaluation of the patient. This thought process "
        "led to an additional FLDM attribute in a further effort to provide an effective "
        "health monitor, specifically the incorporation of a knowledge (data) base of "
        "information concerning the equipment operational history including manufacturer "
        "reliability data and other maintenance records. Similar to patient records, "
        "baseline signatures (when the equipment is functioning in a normal, fault-free "
        "manner) are acquired and stored for future reference and comparisons.")

    P(
        b, lang,
        "Khi thực hiện FDI, bốn giai đoạn, được liệt kê theo thứ tự độ khó tăng dần, "
        "như sau (xem Sơ đồ 1):",
        "When performing FDI, the four stages, listed in order of increasing difficulty, "
        "are as follows (see Scheme 1):")

    # Scheme 1 — the four FDI stages, in order of increasing difficulty.
    L(
        b, lang,
        ["Phát hiện rằng một lỗi thực sự đã xảy ra",
         "Cô lập các thành phần hoặc thiết bị bị lỗi",
         "Xác định loại và/hoặc nguyên nhân của lỗi",
         "Giảm thiểu hậu quả của lỗi (ví dụ, sửa chữa)"],
        ["Detection that an actual fault has occurred",
         "Isolation of the fault components/devices",
         "Identification of the fault type and/or cause",
         "Mitigation of the fault (e.g., repair)"],
        ordered=True)

    P(
        b, lang,
        "Giám sát sức khỏe bằng logic mờ trên phạm vi toàn nhà máy sử dụng nhiều mô-đun "
        "xử lý tín hiệu để thực hiện phát hiện, cô lập và đặc trưng hóa lỗi. Các tín hiệu "
        "dữ liệu vận hành được lấy mẫu từ các cảm biến hiện có và cảm biến lắp bổ sung "
        "trên khắp nhà máy điện. Kiến trúc mô-đun của FLDM cho phép phân tích tín hiệu "
        "song song, tức là tình trạng của một thành phần hoặc hệ thống nhất định có thể "
        "được đánh giá bằng nhiều kỹ thuật xử lý tín hiệu độc lập. Như minh họa trong "
        "Hình 4.2, FLDM dùng cách tiếp cận hai giai đoạn, trong đó giai đoạn đầu sử dụng "
        "các kỹ thuật phổ biến hơn để phát hiện lỗi chắc chắn. Sau đó, các thuật toán "
        "giai đoạn hai vốn phức tạp hơn được dùng để đặc trưng hóa bất thường. Công việc "
        "đặc trưng hóa này rất quan trọng để xác định phản ứng bảo trì phù hợp.",
        "The plantwide fuzzy logic health monitoring employs multiple signal processing "
        "modules to perform fault detection, isolation, and characterization. "
        "Operational data signals are sampled from existing and retrofitted sensors "
        "throughout the power plant. The modular architecture of the FLDM then allows "
        "signal analyses in parallel, that is, the health of a given component or system "
        "can be assessed using multiple independent signal processing techniques. As "
        "depicted in Figure 4.2, the FLDM uses a two-stage approach in which the first "
        "phase employs the more common techniques for robust fault detection. "
        "Subsequently, the second stage algorithms, which are intricate in nature, are "
        "intended to characterize the anomaly. The characterization effort is critical "
        "to determining the proper maintenance response.")

    FIG(b, 2, F.fig_f02(), lang)

    P(
        b, lang,
        "Việc xây dựng FLDM đòi hỏi lựa chọn các mô-đun xử lý tín hiệu phù hợp. Cần thừa "
        "nhận rằng mỗi cách tiếp cận đều có ưu điểm và nhược điểm. Carnero đã lưu ý, "
        "trong bối cảnh chương trình bảo trì dự đoán cho máy nén vít, rằng phải chọn được "
        "các kỹ thuật chẩn đoán phù hợp nhất, nếu không chương trình PM có thể thất bại "
        "[36]. Hơn nữa, các điều kiện công nghệ (ví dụ, những thay đổi quá độ và điểm "
        "vận hành ổn định cụ thể) có thể ảnh hưởng bất lợi đến khả năng phân tích chính xác "
        "dữ liệu của một số kỹ thuật xử lý tín hiệu. Dĩ nhiên, các triển khai thương mại "
        "đáng tin cậy ưu tiên những phương pháp có tỷ lệ bỏ sót và tỷ lệ báo động giả "
        "thấp.",
        "Creating the FLDM then requires the selection of suitable signal processing "
        "modules. It must be recognized that each approach has its advantages and "
        "disadvantages. Carnero noted, in the context of a screw compressor predictive "
        "maintenance program, that the most suitable diagnostic techniques must be "
        "selected or the PM program may fail [36]. Furthermore, process conditions "
        "(e.g., transient changes and the particular steady-state operating point) can "
        "adversely affect the ability of some signal processing techniques to accurately "
        "analyze the data. Of course, reliable commercial implementations favor those "
        "methods with low-missed and false alarm rates.")

    P(
        b, lang,
        "Phát hiện lỗi tức thì dựa trên kết luận từ một lần quan sát chỉ phù hợp với "
        "những trường hợp xảy ra lỗi nghiêm trọng. Thay vào đó, cần giám sát dài hạn để "
        "nhận diện các lỗi phát triển chậm như những lỗi dự kiến trong ứng dụng bảo trì "
        "dự đoán. Nhằm nâng cao độ tin cậy tổng thể của công tác giám sát sức khỏe, chúng "
        "tôi đề xuất dùng nhiều phương pháp để giải quyết các cơ chế hỏng (nhóm) đa dạng, "
        "đồng thời triển khai nhiều kỹ thuật trong cùng một nhóm lỗi nhằm cải thiện việc "
        "phát hiện lỗi.",
        "Instantaneous failure detection using single-observation conclusions is "
        "appropriate only in those cases in which gross failure is experienced. "
        "Alternatively, long-term monitoring is required to identify slowly developing "
        "faults such as those anticipated in a predictive maintenance application. In "
        "order to improve the overall reliability of the health monitoring, we promote "
        "the use of multiple methods to address the diverse failure mechanisms "
        "(categories) and the implementation of multiple techniques within a failure "
        "category to improve the fault detection.")

    P(
        b, lang,
        "Một đặc điểm nổi bật của cách tiếp cận trình bày trong bài báo này là nó xây "
        "dựng trên các kỹ thuật phát hiện và cô lập lỗi đã được kiểm chứng. Một thách "
        "thức đối với hệ thống giám sát tình trạng tích hợp là tổng hợp các kết quả đa "
        "dạng từ các mô-đun xử lý tín hiệu thành một quyết định trạng thái cuối cùng. Theo "
        "thời gian, kinh nghiệm có thể cho thấy cần loại bỏ một mô-đun do hiệu quả kém, "
        "hoặc nếu có một kỹ thuật tiên tiến mới xuất hiện thì kỹ thuật đó có thể được đưa "
        "vào hệ thống giám sát sức khỏe tích hợp hiện có. Để làm được điều này, chúng tôi "
        "dùng một bộ ra quyết định logic mờ dựa trên luật.",
        "A salient feature of the approach presented in this paper is that it builds "
        "upon proven fault detection and isolation techniques. A challenge to an "
        "integrated condition monitoring system is the assimilation of the diverse "
        "results from the signal processing modules into a final status decision. Over "
        "time, experience may demonstrate the need to remove a module due to poor "
        "performance, or if a new state-of-the-art technique becomes available, then it "
        "can be inserted into the existing integrated health monitor. To accomplish "
        "this, we employ a rule-based fuzzy logic decision maker.")

    P(
        b, lang,
        "Nhiều phương pháp chỉ nhắm vào phát hiện một chế độ hỏng duy nhất và vì thế "
        "thiếu độ bền cần thiết cho bất kỳ ứng dụng thực tế nào. Hơn nữa, tồn tại nhiều "
        "chế độ hỏng khác nhau của thiết bị và thành phần. Hai trường hợp hỏng bổ sung "
        "cần được xem xét là khả năng xảy ra nhiều lỗi (thông qua cùng một hoặc các chế "
        "độ hỏng khác nhau) và lỗi chung. Phát hiện nhiều chế độ hỏng có những ưu điểm rõ "
        "ràng; tuy nhiên, chế độ hỏng càng phức tạp thì càng khó phát hiện và sơ đồ phát "
        "hiện lỗi càng tiến sâu vào lĩnh vực chẩn đoán lỗi công nghệ.",
        "Many methods are geared toward the detection of a single failure mode and, "
        "therefore, lack the robustness required for any practical application. "
        "Furthermore, various equipment and component failure modes exist. Two "
        "additional failure cases which must be considered are the possibilities of "
        "multiple failures (via the same or different failure modes) and common-mode "
        "failure. Detection of multiple failure modes has obvious advantages; however, "
        "the more complex the failure mode, the more difficult it is to detect and the "
        "further the fault detection scheme tends into the area of process fault "
        "diagnostics.")

    # ----------------------------------------------- Stage 1 Signal Processing Modules
    H(b, lang,
      "Giai đoạn 1 — Các mô-đun xử lý tín hiệu",
      "Stage 1 Signal Processing Modules", level=3)

    P(
        b, lang,
        "Để đạt được khả năng áp dụng rộng rãi trong toàn bộ một nhà máy công nghiệp, "
        "chẳng hạn như nhà máy điện hạt nhân, cần có các kỹ thuật xử lý tín hiệu đa mục "
        "đích. Các mô-đun xử lý tín hiệu này cung cấp phân tích ban đầu về dữ liệu nhà "
        "máy nhằm xác định sự tồn tại của bất thường. Có thể thực hiện các phân tích sâu "
        "hơn nếu cần để đặc trưng hóa vấn đề rõ ràng hơn.",
        "To achieve wide applicability throughout an entire industrial plant, such as a "
        "nuclear generating station, general-purpose signal processing techniques are "
        "needed. These signal processing modules provide the initial analyses of plant "
        "data to ascertain whether an anomaly exists. The more in-depth analyses can be "
        "performed, if desired, to more definitively characterize the problem.")

    P(
        b, lang,
        "Để minh họa việc sử dụng các phương pháp phân tích chữ ký đa mục đích, hãy xét "
        "bốn tín hiệu nhiệt độ được cho trong Hình 4.3. Các tín hiệu này thu được từ "
        "buồng chứa phía trên của Lò phản ứng sinh sản thực nghiệm II (EBR-II) trong quá "
        "trình khởi động từ 0% đến 100% công suất định mức. Tín hiệu thứ nhất "
        "(Hình 4.3(a)) cho thấy mức nhiễu đồng đều về mặt thị giác bất kể mức công suất; "
        "tuy nhiên, ba tín hiệu còn lại có mức nhiễu tăng dần khi công suất lò tăng, trong "
        "đó giá trị nhiệt độ cuối cùng (Hình 4.3(d)) đặc biệt nhiều nhiễu. Nhiễu tín hiệu "
        "có thể do cảm biến hoạt động sai hoặc do bất thường trong quá trình. Hoặc có thể "
        "nhiễu tăng lên là hoàn toàn bình thường, và chính tín hiệu không có nhiễu tăng "
        "mới là tín hiệu thực sự bất thường. Bộ ra quyết định FL phải kết hợp kết quả "
        "phân tích tín hiệu với các luật do chuyên gia xây dựng để xác định chẩn đoán đúng.",
        "To illustrate the use of the general-purpose signature analysis methods, "
        "consider the four temperature signals shown in Figure 4.3. These signals were "
        "obtained from the upper plenum of the Experimental Breeder Reactor II during a "
        "startup from 0% to 100% full power. The first signal (Figure 4.3(a)) visually "
        "shows a uniform amount of noise regardless of the power level; however, the "
        "other three signals exhibit increasing levels of noise as the reactor power "
        "rises, with the last temperature reading (Figure 4.3(d)) being especially noisy. "
        "The signal noise could be due to sensor maloperation or a process irregularity. "
        "Or perhaps the increased noise is perfectly normal and it is the signal without "
        "increased noise that is actually abnormal. The FL decision maker must combine "
        "the signal analysis results with expert derived rules to ascertain the correct "
        "diagnosis.")

    FIG(b, 3, F.fig_f03(), lang)

    P(
        b, lang,
        "Hãy xét một bộ phát hiện nhiễu mờ chỉ dùng hai đầu vào: giá trị rms và tần số "
        "vượt qua không của tín hiệu. Giá trị rms và tần số vượt qua không trước tiên được "
        "đo và mờ hóa riêng biệt. Giá trị rms có thể được mờ hóa thành các giá trị bằng "
        "không, thấp, thường và cao. Giá trị bằng không là cần thiết để xét đến các tình "
        "huống như bão hòa tín hiệu hoặc mất tín hiệu. Tần số vượt qua không (ZCR) tương "
        "tự được mờ hóa thành các giá trị thưa thớt, đều đặn và thường xuyên. Trong ví dụ "
        "đầu tiên, một bộ luật đơn giản được xây dựng và trình bày trong Bảng 4.1. Các "
        "luật 3 và 4 xét đến các tình huống như bão hòa tín hiệu và mất tín hiệu.",
        "Consider a fuzzy noise detector that utilizes only two inputs: the rms and "
        "zero-crossing rates of the signals. The rms and zero-crossing rate are first "
        "measured and individually fuzzified. The rms value may be fuzzified into zero, "
        "low, ordinary and elevated values. The zero value is necessary to account for "
        "situations such as signal saturation and loss of signal. The zero crossing rate "
        "(ZCR) is similarly fuzzified into infrequent, regular, and frequent. For our "
        "first example, a simple rule set is produced and delineated in Table 4.1. Rules "
        "3 and 4 account for situations such as signal saturation and loss of signal.")

    # -------------------------------------------------------------- Table 4.1 (rule set)
    # The printed table draws an overline over "Infrequent" in Rules 1 and 2,
    # read as "not infrequent".  It is retained with text-decoration:overline.
    _overline_vi = '<span style="text-decoration:overline">Không thường xuyên</span>'
    _overline_en = '<span style="text-decoration:overline">Infrequent</span>'
    _rows_vi = [
        ["1", "Thấp", _overline_vi, "Bình thường"],
        ["2", "Thường", _overline_vi, "Ồn"],
        ["3", "Bằng không", "Không thường xuyên", "Đáng ngờ"],
        ["4", "Thấp", "Không thường xuyên", "Đáng ngờ"],
        ["5", "Cao", "Thường xuyên", "Rất ồn"],
    ]
    _rows_en = [
        ["1", "Low", _overline_en, "Normal"],
        ["2", "Ordinary", _overline_en, "Noisy"],
        ["3", "Zero", "Infrequent", "Suspect"],
        ["4", "Low", "Infrequent", "Suspect"],
        ["5", "Elevated", "Frequent", "Very Noisy"],
    ]
    TBL(
        b, lang,
        ["Quy tắc", "Giá trị RMS", "Tần số vượt qua không", "Trạng thái nhiễu tín hiệu"],
        ["Rule", "RMS value", "Zero-crossing rate", "Signal noise status"],
        _rows_vi if lang == "vi" else _rows_en,
        caption_vi="Bảng 4.1: Một bộ luật đơn giản để đánh giá nhiễu tín hiệu",
        caption_en="Table 4.1: A simple set of rules for signal noise assessment")

    P(
        b, lang,
        "Trường hợp của cảm biến nhiệt độ thứ hai (Hình 4.3(b)), giá trị rms được tính là "
        "0,80°F và ZCR là 2,75 lần/phút tại khoảng t = 350 phút. Giá trị rms được mờ hóa "
        "và có độ thuộc 1,0 trong nhóm thấp. Tương tự, ZCR được mờ hóa và có độ thuộc bằng "
        "1 trong lớp thưa thớt (lưu ý: dấu gạch ngang phía trên được đọc là không thưa "
        "thớt). Sau khi áp dụng các luật và thực hiện phi mờ hóa trọng tâm, trạng thái "
        "nhiễu tín hiệu tổng thể là bình thường vì chỉ Luật 1 được kích hoạt, dù cảm nhận "
        "của con người dựa trên Hình 4.3(b) có thể cho rằng tín hiệu này nhiều nhiễu.",
        "In the case of the second temperature sensor (Figure 4.3(b)), the rms value is "
        "computed as 0.80°F and the ZCR is 2.75 per min at around t = 350 min. The rms "
        "value is fuzzified and found to have a membership of 1.0 in the low group. "
        "Likewise, the ZCR is fuzzified and determined to have a unity membership in the "
        "infrequent (note: the overline is read as not infrequent) class. After applying "
        "the rules and performing the centroid defuzzification, the overall signal noise "
        "status is normal as only Rule 1 is activated, even though the human perception "
        "based on Figure 4.3(b) might be to consider it noisy.")

    P(
        b, lang,
        "Kết quả cho tín hiệu thứ ba và thứ tư tương tự, ngoại trừ việc tín hiệu thứ tư "
        "được phân loại là rất ồn còn tín hiệu thứ ba chỉ được coi là ồn. Giá trị "
        "σ = 1,69°F của nhiệt độ thứ ba cho độ thuộc 0,39 và 1,0 lần lượt trong các nhóm "
        "thấp và thường; ZCR = 5,22/phút kích hoạt cả nhóm thường xuyên và nhóm thưa thớt "
        "(có gạch trên: không thưa thớt) ở mức độ bằng 1, như thấy trong Hình 4.4. Kết quả "
        "chẩn đoán cho tín hiệu thứ ba là ồn dù cả Luật 1 và Luật 2 đều được kích hoạt.",
        "The results for the third and fourth signals are similar, except that the "
        "fourth signal is classified as very noisy and the third signal is deemed simply "
        "noisy. The σ = 1.69°F of the third temperature produces memberships of 0.39 and "
        "1.0 in the low and ordinary groups, respectively; the ZCR = 5.22/min activates "
        "both the frequent and infrequent (overline: not infrequent) to a degree of unity "
        "as seen in Figure 4.4. The diagnostic result for the third signal is noisy even "
        "though both Rules 1 and 2 are triggered.")

    FIG(b, 4, F.fig_f04(), lang)

    P(
        b, lang,
        "Các phân tích trong ví dụ này được thực hiện trên một tín hiệu đơn lẻ, và rms "
        "cùng ZCR được mờ hóa theo các đặc trưng tín hiệu cơ sở được lưu trong cơ sở dữ "
        "liệu của nhà máy, sẽ được trình bày sau. Dù ví dụ này chỉ cho thấy phân tích dựa "
        "trên một cảm biến duy nhất mà không xét đến hành vi của các tín hiệu tương tự "
        "khác, các đặc trưng từ tín hiệu dư và tín hiệu liên quan cũng có thể được so "
        "sánh để nâng cao độ tin cậy của kết quả. Hơn nữa, những so sánh như vậy giúp "
        "giải quyết việc nhiễu là hệ quả của bất thường thiết bị hay bất thường công nghệ.",
        "The analyses of this example have been performed on a single signal, and the "
        "rms and ZCR are fuzzified according to the baseline signal features that are "
        "stored in the plant database, which is described later. Although this example "
        "has shown analyses based on examining a single sensor without regard to the "
        "behavior of other similar signals, the features from redundant and related "
        "signals can also be compared to further enhance the confidence of the result. "
        "Moreover, such comparisons aid in resolving whether the noise is the consequence "
        "of an equipment anomaly or a process abnormality.")

    P(
        b, lang,
        "Như một ví dụ về tính phụ thuộc lẫn nhau giữa chẩn đoán công nghệ và chẩn đoán "
        "thiết bị, hãy xét đỉnh đột biến trong tín hiệu nhiệt độ đầu ra lõi lò phản ứng "
        "được cho trong Hình 5. Một sự kiện như vậy cần được đánh giá xem xung này là "
        "thay đổi công nghệ thực sự hay là kết quả đọc sai. Trong tình huống này, có thể "
        "dùng kiểm tra giới hạn tốc độ thay đổi để xác nhận rằng trên thực tế sự thay đổi "
        "vật lý đó là rất khó xảy ra, nhưng không phải là không thể. Tuy nhiên, khả năng "
        "này lại là cơ sở của một số luật phụ thuộc vào biến quan tâm và độ lớn của tốc độ "
        "thay đổi được xác định bằng các hàm thuộc mờ. Hơn nữa, có thể đưa thêm thông tin "
        "vào quá trình ra quyết định bằng cách xem xét các biến công nghệ liên quan khác. "
        "Chẳng hạn, một sự tăng nhiệt độ lớn như vậy sẽ đòi hỏi tăng công suất đáng kể "
        "và/hoặc mất khả năng tản nhiệt như có thể xảy ra khi mất dòng chất làm mát. Tình "
        "huống này cho thấy sự cần thiết của cơ sở tri thức luật mờ trong việc phân biệt "
        "sai chức năng thiết bị với các bất thường công nghệ.",
        "As an example of the interdependency between process and equipment diagnostics, "
        "consider the spike in the reactor core exit temperature signal shown in Figure 5. "
        "Such an occurrence requires an evaluation as to whether this impulse is an "
        "actual process change or an erroneous reading. Rate-of-change limit checking can "
        "be used in this situation to ascertain that, in fact, such a physical change is "
        "improbable, but not impossible. Nevertheless, this possibility forms the basis "
        "of several rules which depend on the variable of interest and the magnitude of "
        "the rate of change as defined by fuzzy membership functions. Furthermore, "
        "additional information can be incorporated in the decision-making process by "
        "looking at other related process variables. For instance, such a large "
        "temperature rise would require a significant increase in power and/or a loss of "
        "heat rejection capability as might be experienced during a loss of coolant flow. "
        "This situation demonstrates the need for the fuzzy rule knowledge base to "
        "discriminate equipment malfunction from process abnormalities.")

    return b
