# -*- coding: utf-8 -*-
import ppicfig10 as F
from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# Table 12 — values re-read from the rendered printed page (PDF p.264).
_RELIABILITY_ROWS = [
    ["0", "0", "0", "1.00"],
    ["1", "10", "0", "1.00"],
    ["2", "20", "0", "1.00"],
    ["3", "30", "5.3E-08", "9.9999995E-01"],
    ["4", "40", "2.8E-06", "9.9999718E-01"],
]


# Printed reference list, in order 1-25. C.refs() supplies the <ol>, so the
# leading "N. " markers are omitted; every other bibliographic detail, DOI
# and printed oddity is kept verbatim. Ampersands are HTML-escaped.
_REFS_ITEMS = [
    "IAEA. Modern Instrumentation and Control for Nuclear Power Plants: "
    "Guidebook. Vienna: International Atomic Energy Agency; 1999.",
    "Hashemian H. M. Nuclear Power Plant Instrumentation and Control. In: "
    "P. Tsvetkov, editor. Nuclear Power—Control, Reliability and Human "
    "Factors. Texas: Intechopen; 2011. DOI: 10.5772/18768.",
    "NRC. Digital Instrument and Controls. Washington, DC: Nuclear "
    "Regulatory Commission; 2011.",
    "Aldemir T., Stovsky M. P., Krischenbaum J., Mandelli D., Bucci P., "
    "Mangan L. A., Miller D. W., Sun X., Ekici E., Guarro S., Yau M., "
    "Johnson B., Elks C., Arndt S. A. S. Dynamic Reliability Modeling of "
    "Digital Instrumentation and Control Systems for Nuclear Reactor "
    "Probabilistic Risk Assessments, NUREG/CR-6942. Washington, DC: "
    "Nuclear Regulatory Commission; 2007.",
    "Pinto J. M. O., Frutuoso e Melo P. F., Saldanha P. L. C. A DFM/"
    "ATHEANA Human Failure Analysis of a Digital Control System for a "
    "Pressurizer. In: Proceedings of the European Safety and Reliability "
    "Conference, Taylor &amp; Francis, Netherlands; 2013.",
    "Stamatelatos M. Probabilistic Risk Assessment Procedures Guide for "
    "NASA Managers and Practitioners. Washington, DC: NASA; 2002.",
    "Furieri E. B. Internal Guideline on Review and Assessment of Digital "
    "I&amp;C System. Brazil: National Commission of Nuclear Energy, CNEN; 2016.",
    "Aldemir T., Miller D. W., Stovsky M. P., Kirschenbaum J., Bucci P., "
    "Fentman A. W., Mangan L. T. Current State of Reliability Modeling "
    "Methodologies for Digital Systems and Their Acceptance Criteria for "
    "Nuclear Power Plant Assessment, NUREG/CR-6901. Washington, DC: "
    "Nuclear Regulatory Commission; 2006.",
    "Pinto J. M. O., Frutuoso e Melo P. F., Saldanha P. L. C. A Dynamic "
    "Failures Evaluation of a Simplified Digital Control System for a "
    "Nuclear Power Plant Pressurizer. In: Proceedings of the European "
    "Safety and Reliability Conference, Taylor &amp; Francis, Greece; 2010.",
    "Gomes I. G., Frutuoso e Melo P. F., Saldanha P. L. C. A Cell-to-Cell "
    "Markovian Model for the Reliability of a Digital Control System of a "
    "Steam Generators. In: International Nuclear Atlantic Conference, "
    "ABEN, Brazil; 2013.",
    "Pinto J. M. O., Frutuoso e Melo P. F., Saldanha P. L. C. A DFM/"
    "Fuzzy/ATHEANA Human Failure Analysis of a Digital Control System for "
    "a Pressurizer. Nuclear Technology. 2014;188:20–33. "
    "DOI: 10.13182/NT13-48.",
    "Aldemir T., Stovsky M. P., Krischenbaum J., Mandelli D., Bucci P., "
    "Mangan L. A., Miller D. W., Sun X., Guarro S., Yau M., Johnson B., "
    "Elks C., Arndt S. A., Dion J., Nguyen Q., Ekici, E. A Benchmark "
    "Implementation of Two Dynamic Methodologies for the Reliability "
    "Modeling of Digital Instrumentation and Control Systems, NUREG/"
    "CR-6985. Washington, DC: Nuclear Regulatory Commission; 2009.",
    "Yau M., Apostolakis G., Guarro S. The Use of Prime Implicants in "
    "Dependability Analysis of Software Controlled Systems. Reliability "
    "Engineering and System Safety. 1998;62:23–32.",
    "Guarro S., Yau M., Apostolakis G. Demonstration of the Dynamic "
    "Flowgraph Methodology using the Titan II Space Launch Vehicle "
    "Digital Flight Control Software. Reliability Engineering and System "
    "Safety. 1995;49:335–353.",
    "Guarro S., Yau M., Motamed M. Development of Tools for Safety "
    "Analysis of Control Software in Advanced Reactors. Washington, DC: "
    "Nuclear Regulatory Commission; 1996.",
    "Garret C. J., Apostolakis G. Automated Hazard Analysis of Digital "
    "Control Systems. Reliability Engineering and System Safety. "
    "2002;77:1–17.",
    "IEEE. Equipment Reliability Data for Nuclear-Power Generating "
    "Stations. New York: IEEE and John Wiley &amp; Sons; 1984.",
    "Smith C. L., Wood S. T., Galyean W. J., Schroeder J. A., Beck S. "
    "T., Sattison M. B. Systems analysis Programs for Hands-On 17 "
    "Integrated Reliability Evaluations (SAPHIRE) Summary Manual, "
    "NUREG/CR-6116. 18 Washington, DC: Nuclear Regulatory Commission; 2008.",
    "Guarro S., Yau M., Motamed M. Development of Tools for Safety "
    "Analysis of Control Software in Advanced Reactors, NUREG/CR-6465. "
    "Washington, DC: Nuclear Regulatory Commission; 1996.",
    "Aldemir T., Kirschenbaum J., Mandelli D., Bucci P., Mangan L. A., "
    "Miller D. W., Sun X., Guarro S., Yau M., Arndt S. A., Ekici, E. "
    "Probabilistic Risk Assessment Modeling of Digital Instrumentation "
    "and Control Systems Using Two Dynamic Methodologies. Reliability "
    "Engineering and System Safety. 2010;95:1011–1039.",
    "Aldemir T. Computer-Assisted Markov Failure Modeling of Process "
    "Control Systems. IEEE Transactions on Reliability. 1987;R-36:133–144.",
    "Hsu C. S. Cell-to-Cell Mapping: A Method of Global Analysis for "
    "Nonlinear Systems. New York: Springer-Verlag; 1987.",
    "Aldemir T. Utilization of the Cell-to-Cell Mapping Technique to "
    "Construct Markov Failure Models for Process Control Systems. In: "
    "Probabilistic Safety and Assessment and Management, PSAM-1, "
    "Elsevier, Greece; 1991.",
    "Aldemir T., Bucci P., Mangan L. A., Kirschenbaum J., Mandelli D., "
    "Arndt S. A. Incorporation of Markov Reliability Models for Digital "
    "Instrumentation and Control Systems into Existing PRAs. In: "
    "Proceedings of NPIC&amp;HMIT 2006, American Nuclear Society, "
    "La Grange Park, IL; 2006.",
    "IAEA. Component Reliability Data for Use in Probabilistic Safety "
    "Assessment. Vienna: International Atomic Energy Agency; 1988.",
]


# The figure supplier runs in parallel. Install a fallback only when the
# aggregator has not registered fig_f05, and never replace a real callable.
if not hasattr(F, "fig_f05"):
    def _fallback_f05():
        import ppicfig10_common as FC
        o = []
        xt = [(v, str(v)) for v in (0, 10, 20, 30, 40)]
        yt = [(1.0, "1"), (0.9999992, "0.9999992"),
              (0.9999984, "0.9999984"), (0.9999976, "0.9999976"),
              (0.9999968, "0.9999968"), (0.999996, "0.999996")]
        frame, mx, my = FC._frame(
            74, 46, 500, 224, (0, 40), (0.999996, 1.0), xt, yt,
            "t (giờ) · t (hours)", "R(t)")
        o.append(frame)
        o.append(FC._series(
            [(0, 1.0), (10, 1.0), (20, 1.0), (30, 0.99999995),
             (40, 0.99999718)], mx, my, FC.BLUE))
        return FC._mk(
            5, o, "Reliability of the digital water level control system",
            "Độ tin cậy của hệ thống điều khiển mức nước số",
            "Reliability of the digital water level control system",
            "Đồ thị độ tin cậy R(t), giảm mạnh giữa 30 và 40 giờ.",
            "Reliability R(t), dropping sharply between 30 and 40 hours.")
    F.fig_f05 = _fallback_f05


def section(lang):
    b = []
    H(b, lang, "Kết quả độ tin cậy", "Reliability results", level=3)
    TBL(b, lang,
        ["k", "t", "PET(t)", "R(t)"],
        ["k", "t", "PET(t)", "R(t)"],
        _RELIABILITY_ROWS,
        caption_vi="Bảng 10.12 · Độ tin cậy của hệ thống điều khiển mức nước số",
        caption_en="Table 10.12 · Reliability of the digital water level "
                   "control system")
    FIG(b, 5, F.fig_f05(), lang)
    P(b, lang,
      "Từ các kết quả, có thể thu được thông tin về sự phát triển của độ tin "
      "cậy của hệ thống điều khiển mức nước số được xây dựng cho nghiên cứu "
      "này. Quan sát Hình 4, có thể xác nhận rằng sự hỏng có xác suất xuất "
      "hiện lớn nhất là mức nước thấp. Mặc dù tỷ lệ hỏng của cả hai chế độ "
      "hỏng của van là như nhau, các chế độ hỏng của bộ vi xử lý làm tăng "
      "xác suất hệ thống hỏng theo hướng mức nước thấp.",
      "From the results it is possible to obtain information regarding the "
      "development of the reliability of the digital water level control "
      "system created for this study. Observing Figure 4, it is possible "
      "to verify that the failure with the largest probability of "
      "occurrence is low water level. In spite of the failure rates for "
      "both failure modes of the valve being the same, the failure modes "
      "of the CPUs increase the probability that the system fails low.")
    P(b, lang,
      "Điều quan trọng cần lưu ý là dữ liệu trong tài liệu tham khảo [25], "
      "được dùng để xác định tỷ lệ hỏng của các thành phần hệ thống, đã "
      "được công bố năm 1988. Kể từ khi công bố, các thành phần hệ thống "
      "điều khiển và thiết bị đo đã được cải tiến liên tục, do đó làm tăng "
      "độ tin cậy của chúng.",
      "It is important to observe that the data in reference [25], used to "
      "obtain the failure rates of the system components, were published "
      "in 1988. Since its publication, I&amp;C system components have been "
      "constantly improved, consequently increasing their reliability.")
    H(b, lang, "KẾT LUẬN", "CONCLUSIONS", level=2)
    P(b, lang,
      "Các phương pháp thích hợp để đánh giá an toàn và độ tin cậy là then "
      "chốt để cơ quan quản lý thiết lập tính chấp nhận được của các hệ "
      "thống điều khiển và thiết bị đo số trong các hệ thống an toàn và "
      "điều khiển của nhà máy điện hạt nhân.",
      "Appropriate methods for assessing safety and reliability are the "
      "key to establishing the acceptability of digital I&amp;C systems in "
      "safety and control systems of nuclear power plants by the "
      "regulatory side.")
    P(b, lang,
      "Các mô hình độ tin cậy phù hợp với hệ thống điều khiển và thiết bị "
      "đo số đang trong quá trình phát triển hoặc trong quá trình thẩm định.",
      "Reliability models suitable for digital I&amp;C systems are in "
      "development process or in validation process.")
    P(b, lang,
      "Cách tiếp cận truyền thống sử dụng cây lỗi không xem xét các tương "
      "tác động hiện diện trong các hệ thống đó; vì vậy, cần tìm một "
      "phương pháp luận về độ tin cậy tính đến những vấn đề này mà không "
      "vi phạm các yêu cầu hiện hành về phân tích an toàn.",
      "The traditional approach of using fault trees does not consider the "
      "dynamic interactions present in those systems; therefore, it is "
      "necessary to find a reliability methodology that takes into account "
      "these issues without violating the existing requirements concerning "
      "safety analysis.")
    P(b, lang,
      "Công trình này thảo luận việc áp dụng DFM và MARKOV/CCMT để mô hình "
      "hóa độ tin cậy của các hệ thống số. Như đã nêu trước đó, các phương "
      "pháp luận này đáp ứng hầu hết các yêu cầu đối với loại hệ thống "
      "này. DFM hiệu quả trong việc mô hình hóa các tương tác giữa các "
      "thành phần khác nhau của một hệ thống số (các thiết bị vật lý và "
      "phần mềm, với phần mềm được biểu thị ngầm trong logic điều khiển "
      "một hoặc nhiều bảng quyết định). Thông qua các prime implicant, "
      "phương pháp cho phép hình dung các trạng thái có thể của hệ thống, "
      "hỏng hoặc không hỏng. Phân tích suy diễn cho phép nghiên cứu hiệu "
      "quả các sự hỏng bằng cách truy tìm nguyên nhân của một sự kiện "
      "đỉnh nhất định. Phân tích quy nạp có thể được dùng để giảm thiểu "
      "các sự hỏng phát hiện được trong phân tích suy diễn và để kiểm "
      "chứng các đặc tả của hệ thống. Phương pháp cũng có thể được dùng "
      "để chuẩn bị FMEA, điều tra hậu quả của các điều kiện ban đầu nhất "
      "định.",
      "This work discusses the application of DFM and MARKOV/CCMT to model "
      "the reliability of digital systems. As stated previously, these "
      "methodologies fulfilled the most the requirements concerning these "
      "type of systems. DFM is effective in modeling the interactions of "
      "the various components of a digital system (physical devices and "
      "software, the latter being implicit in the logic driving one or "
      "more decision tables). Through prime implicants, it allows the "
      "visualization of possible system states, failed, or not. Its "
      "deductive analysis allows an efficient study of failures tracing "
      "the causes of a given top event. Its inductive analysis can be "
      "used in the mitigation of failures found in deductive analyses and "
      "for the verification of system specifications. It can also be used "
      "for FMEA preparation, investigating the consequences of given "
      "initial conditions.")
    P(b, lang,
      "Một hạn chế của phương pháp luận là cần có hiểu biết về toàn bộ hệ "
      "thống, cả trong mô hình hóa lẫn trong công tác giảm thiểu. Nhưng "
      "sau khi được xây dựng, hệ thống có thể được phân tích cho nhiều "
      "chế độ hỏng và sự kiện đỉnh đáng quan tâm khác nhau.",
      "A limitation of the methodology is that the knowledge of the whole "
      "system both for modeling and for mitigations is necessary. But "
      "once built, the system can be analyzed for various failure modes "
      "and top events of interest.")
    P(b, lang,
      "Vì nhiều hệ thống số vẫn cùng tồn tại với các vòng lặp tương tự, "
      "điều quan trọng là kết quả do bất kỳ phương pháp luận nào báo cáo "
      "cũng có thể được đưa vào các PSA hiện có. Chỉ khi đó, các nghiên "
      "cứu về độ bất định và tầm quan trọng, chẳng hạn, mới có thể được "
      "phát triển cho các hệ thống số như đã thực hiện cho các hệ thống "
      "khác trong phân tích hỏng hóc.",
      "As many digital systems still coexist with analog loops, it is "
      "important that the results reported by any methodology can be "
      "incorporated into existing PSAs. Only then, uncertainty and "
      "importance studies, for example, can be developed for digital "
      "systems such as those performed for other systems in failure "
      "analysis.")
    P(b, lang,
      "Vì thành phần chính của một hệ thống số là phần mềm (và thực tế là "
      "phần mềm chưa có cách tiếp cận độ tin cậy được xác định rõ), sự "
      "hiện diện của các công cụ cho phép kiểm chứng lỗi và sau đó hiệu "
      "chỉnh các thành phần này là rất thuận tiện.",
      "As the main element of a digital system is the software (and the "
      "fact that it does not have a defined reliability approach), it is "
      "quite convenient the existence of tools that enable the "
      "verification of faults and subsequent corrections in these "
      "elements.")
    P(b, lang,
      "Về phương pháp Markov/CCMT, chúng tôi dự định áp dụng phương pháp "
      "này cho hệ thống điều khiển bình sinh hơi của PWR để đánh giá khả "
      "năng của nó. Mô hình Markov/CCMT có thể được dùng ở cả bước quy nạp "
      "và bước suy diễn (tức là, xác định các chuỗi tai nạn và phân tích "
      "hỏng của hệ thống an toàn, tương ứng) của một PSA để tạo ra, "
      "tương ứng, các quan hệ nguyên nhân–hậu quả (chuỗi và kịch bản sự "
      "kiện) giữa các sự kiện khởi phát và các sự kiện đỉnh, hoặc các "
      "trạng thái vận hành và các prime implicant dẫn đến một sự kiện "
      "đỉnh hoặc trạng thái vận hành nhất định. Khả năng của DFM trong "
      "việc tìm các nguyên nhân khả dĩ nhất cho một Sự kiện đỉnh cụ thể "
      "có thể được dùng để xác định các điều kiện ban đầu cho "
      "Markov/CCMT, từ đó cho ra dữ liệu xác suất chi tiết hơn về hành vi "
      "độ tin cậy của hệ thống theo thời gian. Tuy nhiên, phương pháp "
      "luận này đòi hỏi nỗ lực tính toán cao hơn bình thường khi độ phức "
      "tạp (tức là số lượng thành phần và trạng thái hỏng) của hệ thống "
      "tăng lên.",
      "In what concerns the Markov/CCMT approach, we intend to apply it "
      "to a PWR steam generator control system in order to assess its "
      "capabilities. The Markov/CCMT model can be used in both the "
      "inductive and deductive steps (that is, identification of accident "
      "sequences and safety system failure analysis, respectively) of a "
      "PSA to produce respectively the cause–consequence relations (event "
      "sequences and scenarios) between initiating events and top events, "
      "or operational states and the prime implicants leading to a "
      "specified top events or operational states. The ability of DFM to "
      "find the most probable causes for a specific Top Event can be used "
      "to determine the initial conditions for Markov/CCMT, which results "
      "in more detailed probabilistic data of the system’s reliability "
      "behavior in relation to time. However, this methodology demands a "
      "higher computational effort than usual as the complexity (i.e., "
      "the number of components and failure states) of the system "
      "increases.")
    P(b, lang,
      "Các mô hình trình bày có liên quan đến các quyết định dựa trên rủi "
      "ro do cơ quan quản lý đưa ra, trong đó các mô hình và kết quả PSA "
      "bổ sung cho các yêu cầu mang tính xác định chính (liên quan đến "
      "cấu trúc, hệ thống và thành phần) mà đơn vị vận hành phải đáp ứng "
      "trong quá trình cấp phép.",
      "The models presented are relevant for Risk Informed decisions taken "
      "by the regulatory side where PSA models and results complement the "
      "primary deterministic requirements (regarding structures, systems, "
      "and components) to be met by the utility in the licensing process.")
    H(b, lang, "TÀI LIỆU THAM KHẢO", "REFERENCES", level=2)
    REFS(b, lang, _REFS_ITEMS)
    return b
