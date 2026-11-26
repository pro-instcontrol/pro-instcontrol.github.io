# -*- coding: utf-8 -*-
"""Book 9, Chapter 10 (part A) — byline note, ABSTRACT and the opening of
INTRODUCTION (EN/VI bilingual).

Source: ppic_raw.txt lines 6373-6505 (PDF pp. 245-248, printed pp. 229-232).
The printed title, chapter number, authors and affiliations are rendered by
the page shell, so this module does not repeat title markup; the byline
material appears only as a source note. Bracketed citations [1]-[8] are kept
inline; no reference list is emitted here. There are no figures, tables or
equations in this section.
"""
import ppicfig10 as F  # noqa: F401  (shared supplier import style)
from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401


def section(lang):
    b = []

    # --------------------------------------------------------- byline source note
    NOTE(b, lang,
      "<b>Ghi chú nguồn.</b> Các tác giả thuộc Ủy ban Năng lượng Nguyên tử "
      "Quốc gia, Rio de Janeiro, RJ, Brazil, và Chương trình Sau đại học về "
      "Kỹ thuật Hạt nhân, COPPE, Đại học Liên bang Rio de Janeiro, Rio de "
      "Janeiro, RJ, Brazil.",
      "<b>Source note.</b> The authors are affiliated with the National "
      "Commission of Nuclear Energy, Rio de Janeiro, RJ, Brazil, and the "
      "Graduate Program of Nuclear Engineering, COPPE, Federal University "
      "of Rio de Janeiro, Rio de Janeiro, RJ, Brazil.")

    # ---------------------------------------------------------------- ABSTRACT
    H(b, lang, "TÓM TẮT", "ABSTRACT", level=2)
    P(b, lang,
      "Mục tiêu của chương này là thảo luận hai cách tiếp cận để phân tích độ "
      "tin cậy của các hệ thống điều khiển và thiết bị đo số trong nhà máy "
      "điện hạt nhân, có tính đến khía cạnh quản lý. Phương pháp Đồ thị Động "
      "(Dynamic Flowgraph Methodology, DFM) và Kỹ thuật Ánh xạ Từng ô sang "
      "Từng ô (Markov/Cell-to-Cell Mapping Technique, CCMT) được thảo luận và "
      "các nghiên cứu điển hình đã phát triển được trình bày. Các nghiên cứu "
      "điển hình này liên quan đến các hệ thống điều khiển đơn giản hóa cho "
      "một máy phát hơi và một bình áp lực của nhà máy lò phản ứng nước áp "
      "lực (Pressurized Water Reactor, PWR), nhằm đánh giá từng phương pháp. "
      "Ưu điểm và hạn chế của từng cách tiếp cận được đề cập. Đối với cách "
      "tiếp cận DFM, ba mối quan tâm trong tài liệu được giải quyết: mô hình "
      "hóa bản thân hệ thống, tích hợp kết quả của phương pháp vào các Đánh "
      "giá An toàn Xác suất (Probabilistic Safety Assessment, PSA) hiện có, "
      "và nhận diện các lỗi phần mềm. Phương pháp Markov/CCMT, vốn đã được "
      "sử dụng trong các đánh giá an toàn xác suất động, được tiếp cận thông "
      "qua một hệ thống điều khiển thể tích nước đơn giản hóa có điều khiển "
      "số. Phương pháp Markov/CCMT cho ra dữ liệu chi tiết về hành vi độ tin "
      "cậy của hệ thống theo thời gian. Tuy nhiên, phương pháp này đòi hỏi "
      "nỗ lực tính toán cao hơn bình thường khi độ phức tạp của hệ thống "
      "(tức là số lượng linh kiện và trạng thái hỏng hóc) tăng lên. Như một "
      "kết luận nghiên cứu về mặt quản lý, các phương pháp trình bày có thể "
      "được dùng trong đánh giá rủi ro PSA, góp phần hỗ trợ công tác quản lý.",
      "The objective of this chapter is to discuss two approaches for "
      "reliability analysis of digital instrumentation and control systems "
      "in nuclear power plants taking into account the regulatory side. "
      "Dynamic Flowgraph Methodology (DFM) and Markov/Cell-to-Cell Mapping "
      "Technique (CCMT) are discussed and case studies developed are "
      "presented. These case studies involve simplified control systems for "
      "a steam generator and a pressurizer of a Pressurized Water Reactor "
      "(PWR) plant for the purpose of evaluating each method. Advantages "
      "and limitations of each approach are addressed. For the DFM approach, "
      "three concerns in the literature are addressed: modeling of the "
      "system itself, incorporation of the methodology results into existing "
      "Probabilistic Safety Assessments (PSA), and identification of "
      "software failures. The Markov/CCMT, which has been used in dynamic "
      "probabilistic safety assessments, is approached by means of a "
      "simplified digitally controlled water volume control system. The "
      "Markov/CCMT methodology results in detailed data of the system "
      "reliability behavior in relation to time. However, it demands a "
      "higher computational effort than usual as the complexity (i.e., "
      "number of components and failure states) of the system increases. As "
      "a regulatory research conclusion, the methodologies presented can be "
      "used on PSA risk informed assessment, contributing to the regulatory "
      "side.")

    P(b, lang,
      "<b>Từ khóa:</b> DFM, MARKOV/CCMT, hệ thống điều khiển và thiết bị đo "
      "số, độ tin cậy",
      "<b>Keywords:</b> DFM, MARKOV/CCMT, digital I&amp;C systems, "
      "reliability")

    # ------------------------------------------------------------ INTRODUCTION
    H(b, lang, "GIỚI THIỆU", "INTRODUCTION", level=2)

    # Role of I&amp;C in nuclear plants
    H(b, lang,
      "Vai trò của hệ thống I&amp;C trong nhà máy điện hạt nhân",
      "The role of I&amp;C systems in nuclear power plants", level=3)
    P(b, lang,
      "Hệ thống Điều khiển và Thiết bị đo (Instrumentation and Control "
      "Systems, I&amp;C) là một yếu tố thiết yếu trong vận hành bình thường, "
      "bất thường và khẩn cấp của các nhà máy điện hạt nhân [1]. Các hệ "
      "thống này đo hàng ngàn biến số và kích hoạt nhiều thiết bị để điều "
      "khiển và bảo vệ nhà máy [2].",
      "Instrumentation and Control Systems (I&amp;C) are an essential "
      "element in the normal, abnormal, and emergency operation of nuclear "
      "power plants [1]. These systems measure thousands of variables and "
      "activate several devices to control and protect the plant [2].")
    P(b, lang,
      "Các hệ thống I&amp;C được thiết kế để giữ các biến số công nghệ trong "
      "giới hạn thiết kế của nhà máy. I&amp;C bảo đảm an toàn và hiệu quả "
      "sản xuất của nhà máy bằng cách phản ứng phù hợp với các hỏng hóc và "
      "sự kiện bất thường [2, 3].",
      "The I&amp;C are designed to keep the process variables within plant "
      "design limits. I&amp;C ensure plants' safety and efficient production "
      "by reacting appropriately to failures and abnormal events [2, 3].")

    # Digital systems: benefits and the software-reliability problem
    H(b, lang,
      "Hệ thống số: lợi ích và bài toán độ tin cậy của phần mềm",
      "Digital systems: benefits and the software-reliability problem",
      level=3)
    P(b, lang,
      "Do các hệ thống số ngày càng được tích hợp vào các nhà máy điện hạt "
      "nhân nhờ nhiều ưu điểm so với hệ thống tương tự, một cách tiếp cận "
      "riêng biệt đối với phân tích độ tin cậy và rủi ro đã trở nên cần "
      "thiết [4]. Các hệ thống này phản ánh nhiều tương tác giữa các thành "
      "phần của chúng (biến số công nghệ, phần cứng, phần mềm và hành động "
      "của con người). Bên cạnh đó, các linh kiện vật lý của hệ thống đã có "
      "một cách tiếp cận độ tin cậy được xác định rõ. Điều này không đúng "
      "đối với thành phần phần mềm [5, 6].",
      "Given the increasing incorporation of digital systems in nuclear "
      "power plants, due to their numerous advantages over analog systems, "
      "a specific approach to reliability and risk analysis has been "
      "required [4]. These systems reflect many interactions between their "
      "components (process variables, hardware, software, and human "
      "actions). Besides, physical system components have a well-defined "
      "reliability approach. The same is not true in terms of software "
      "component [5, 6].")
    P(b, lang,
      "Trong các hệ thống số, phần mềm thúc đẩy tính linh hoạt, giảm chi phí "
      "và nâng cao độ tin cậy nhờ khả năng chỉnh sửa cao mà không cần thay "
      "thế. Nếu có thể gỡ lỗi hoàn toàn phần mềm, nó sẽ tiếp tục hoạt động "
      "vô thời hạn và do đó không có khả năng lão hóa [5]. Tuy nhiên, không "
      "có phần mềm nào là hoàn hảo. Quá trình phát triển của nó tiềm ẩn cả "
      "lỗi của con người lẫn sai sót về tài liệu và sai lầm nhận thức. Vì "
      "vậy, cần một cách tiếp cận độ tin cậy mô phỏng được hành vi của các "
      "yếu tố này.",
      "On digital systems, software promotes flexibility, cost reduction, "
      "and reliability through its high capacity of modification without "
      "the need of replacements. If one can complete debugs software, it "
      "will continue working indefinitely, and therefore, there is no "
      "possibility of aging [5]. However, there is no perfect software. Its "
      "development process presumes human failures besides documentation "
      "and cognitive errors. Therefore, a reliability approach that models "
      "the behavior of these elements is necessary.")

    # Licensing and regulatory preparedness
    H(b, lang,
      "Cấp phép và sự sẵn sàng của cơ quan quản lý",
      "Licensing and regulatory preparedness", level=3)
    P(b, lang,
      "Việc xây dựng các lò phản ứng mới và hiện đại hóa hệ thống I&amp;C "
      "trong các lò đang vận hành đang đặt ra yêu cầu về các hoạt động cấp "
      "phép và đánh giá an toàn từ phía các cơ quan quản lý, đặc biệt là sự "
      "sẵn sàng về quản lý đối với việc cấp phép các hệ thống I&amp;C dựa "
      "trên máy tính.",
      "The construction of new reactors and the I&amp;C modernization in "
      "the operating ones are demanding licensing and safety evaluation "
      "activities by the regulatory bodies, particularly, regulatory "
      "preparedness concerning computer-based I&amp;C systems licensing.")

    # Deterministic defence-in-depth and diversity
    H(b, lang,
      "Phòng thủ theo chiều sâu và đa dạng",
      "Defence-in-depth and diversity", level=3)
    P(b, lang,
      "An toàn của các lò phản ứng điện hạt nhân dựa trên các khái niệm xác "
      "định như phòng thủ theo chiều sâu và đa dạng nhằm giảm thiểu rủi ro "
      "từ các sự kiện bên trong hoặc bên ngoài, những sự kiện có thể dẫn "
      "đến lỗi nguyên nhân chung của các hệ thống thụ động và chủ động. Các "
      "nghiên cứu rủi ro và bài học kinh nghiệm từ các lò phản ứng đang vận "
      "hành đã góp phần cải thiện độ tin cậy của thiết kế hệ thống I&amp;C "
      "số mới, nhưng lợi ích của công nghệ số có thể bị suy giảm do độ phức "
      "tạp ngày càng tăng của các linh kiện và của kiến trúc I&amp;C, gây "
      "khó khăn trong quá trình rà soát của cơ quan quản lý [7].",
      "The safety of nuclear power reactors is centered on deterministic "
      "concepts like defense-in-depth and diversity to minimize risks from "
      "internal or external events, which may lead to common cause failures "
      "of passive and active systems. Risk studies and lessons learned of "
      "operating reactors have contributed to improve the reliability of "
      "the new digital I&amp;C design, but the benefits of digital "
      "technology could be impaired by the growing complexity of the "
      "components and I&amp;C architecture due to difficulties during the "
      "regulatory review [7].")
    P(b, lang,
      "Sự kết hợp giữa các cách tiếp cận xác định và xác suất, kiến trúc hệ "
      "thống được thiết kế với Phòng thủ theo chiều sâu và đa dạng (khái "
      "niệm D-in-D), và việc sử dụng phương pháp ước tính tốt nhất cho các "
      "sự kiện vượt quá cơ sở thiết kế, như Lỗi nguyên nhân chung của phần "
      "mềm (Software Common Cause Failure, SCCF), đã được chấp nhận để "
      "chứng minh tính đầy đủ của các kiến trúc I&amp;C số và việc chức năng "
      "của chúng đáp ứng các tiêu chí chấp nhận.",
      "The combination of deterministic and probabilistic approaches, "
      "system architecture designed with Defense-in-Depth and diversity "
      "(D-in-D concept), the use of the best-estimate methodology for "
      "beyond design base events, like Software Common Cause Failure "
      "(SCCF), have been accepted to demonstrate the adequacy of digital "
      "I&amp;C architectures and their functionality to meet the acceptance "
      "criteria.")

    # Risk-informed acceptance and operational-experience caveats
    H(b, lang,
      "Chấp nhận dựa trên rủi ro và những lưu ý từ kinh nghiệm vận hành",
      "Risk-informed acceptance and operational-experience caveats", level=3)
    P(b, lang,
      "Trong bối cảnh này, việc định lượng phân tích rủi ro xác suất nhằm "
      "chứng minh các thuộc tính chất lượng và độ tin cậy đã phát sinh nhiều "
      "cách hiểu khác nhau từ phía ngành công nghiệp và các cơ quan quản lý, "
      "ngay cả khi xét đến xác suất rất thấp của sự kết hợp giữa một số tai "
      "nạn theo cơ sở thiết kế [như Tai nạn mất chất làm mát do vỡ lớn "
      "(Large Break Loss of Coolant Accident, LBLOCA), kết hợp với Lỗi "
      "nguyên nhân chung của phần mềm].",
      "In this context, the quantification of probabilistic risk analysis "
      "to demonstrate the quality and reliability attributes has been "
      "arisen many different interpretations from the industries and "
      "regulators, even considering the very low probability of the "
      "combination of some design-based accidents [like Large Break Loss "
      "of Coolant Accident (LBLOCA), in conjunction with Software Common "
      "Cause Failure].")
    P(b, lang,
      "Ở một mức độ nhất định, khó khăn trong ra quyết định quản lý đã phát "
      "sinh do các quan điểm và cách giải thích khác nhau giữa ngành công "
      "nghiệp và các cơ quan quản lý trong việc giải thích và áp dụng một "
      "số con số về xác suất tỷ lệ hỏng hóc đối với công nghệ thiết bị đo "
      "số.",
      "To some extent, difficulties of regulatory decision making have "
      "been arisen because of different positions and interpretations from "
      "industry and regulators in explaining and applying some numbers of "
      "failure rate probabilities on digital instrumentation technologies.")
    P(b, lang,
      "Việc sử dụng kinh nghiệm vận hành trong trường hợp đánh giá đủ điều "
      "kiện an toàn của thiết bị đo số cần được xử lý thận trọng tương đối, "
      "do có các cách tiếp cận khác nhau trong xử lý dữ liệu kinh nghiệm "
      "vận hành và do thiếu dữ liệu thống kê đầy đủ liên quan đến thiết bị "
      "đo an toàn.",
      "The use of operational experience in case of safety qualification "
      "of digital instrumentation should be processed with relative care "
      "because of different approaches in processing operational experience "
      "data and the lack of sufficient statistical data related to safety "
      "instrumentation.")
    P(b, lang,
      "Việc áp dụng các khái niệm an toàn truyền thống và triết lý thiết kế "
      "của lò phản ứng hạt nhân, trong trường hợp các hệ thống I&amp;C số "
      "mới, đã cho thấy những cách giải thích và đánh giá khác nhau về độ "
      "tin cậy và tư cách đủ điều kiện của các chức năng, cũng như của các "
      "linh kiện và kiến trúc hệ thống I&amp;C số.",
      "The application of traditional safety concepts and design "
      "philosophy of nuclear reactors, in the case of the new digital "
      "I&amp;C systems, have been shown different interpretations and "
      "evaluations for the reliability and qualification of functions, and "
      "components of digital I&amp;C systems and architectures.")

    # National frameworks and quantitative software reliability analysis
    H(b, lang,
      "Khung quản lý quốc gia và phân tích độ tin cậy phần mềm định lượng",
      "National regulatory frameworks and quantitative software "
      "reliability analysis", level=3)
    P(b, lang,
      "Mỗi quốc gia có hệ thống pháp luật và quy trình cấp phép riêng để "
      "thực hiện rà soát và đánh giá các phân tích an toàn. Vì các chức năng "
      "an toàn có thể bị suy giảm do hỏng hóc của hệ thống dự phòng I&amp;C "
      "số (thông qua Lỗi nguyên nhân chung [CCF] tiềm ẩn của phần mềm), cách "
      "tiếp cận hiện nay gọi là Phân tích Độ tin cậy Phần mềm Định lượng "
      "(Quantitative Software Reliability Analysis, QSRA) đã cho thấy những "
      "khó khăn trong ra quyết định quản lý. Việc áp dụng cách tiếp cận "
      "thận trọng của khái niệm D-in-D (với đa dạng cả về phần mềm lẫn phần "
      "cứng) từ Ủy ban Điều hòa Hạt nhân (Nuclear Regulatory Commission, "
      "NRC) [7] đã được một số cơ quan quản lý của các quốc gia đang tham "
      "gia cấp phép lò phản ứng mới củng cố thêm (tức là thiết kế lò áp lực "
      "châu Âu, European Pressurizer Reactors, EPR).",
      "Each country has its own legislation and a particular licensing "
      "process to implement the review and assessment of safety analyses. "
      "As the safety functions could be impaired by the failure of digital "
      "I&amp;C systems redundancies (through potential software Common "
      "Cause Failure [CCF]), the currently approach know as Quantitative "
      "Software Reliability Analysis (QSRA) have been shown difficulties "
      "for regulatory decision making. The application of the D-in-D "
      "concept conservative approach (with diversity of both software and "
      "hardware) from the Nuclear Regulatory Commission (NRC) [7] has been "
      "strengthened by some regulators of countries involved with new "
      "reactor licensing (i.e., European Pressurizer Reactors, EPR design).")
    P(b, lang,
      "Ngành công nghiệp cho rằng các con số độ tin cậy của hệ thống "
      "I&amp;C số mới đã cho thấy tỷ lệ hỏng hóc bằng hoặc tốt hơn so với "
      "hỏng hóc của phần cứng và của con người. Thông tin thêm về các quan "
      "điểm quản lý gần đây và các nghiên cứu về phân tích độ tin cậy phần "
      "mềm định lượng có thể xem trong tài liệu tham khảo [7]. Có những ví "
      "dụ về nghiên cứu quản lý quốc tế nhằm cải thiện cơ sở và công cụ sử "
      "dụng phân tích rủi ro định lượng trong rà soát quản lý đối với công "
      "nghệ I&amp;C số có kiến trúc phức tạp hơn, bao gồm màn hình số và "
      "phân tích yếu tố con người của các phòng điều khiển số được tích hợp "
      "cao.",
      "The industries claim that the reliability figures of new digital "
      "I&amp;C systems have been shown equal or better failure rates than "
      "hardware and human failures. More information on recent regulatory "
      "positions and studies of quantitative software reliability analysis "
      "can be found in reference [7]. There are examples of international "
      "regulatory research to improve the bases and tools on using "
      "quantitative risk analysis for regulatory review of digital "
      "I&amp;C technologies with more complex architecture, which include "
      "digital displays and human-factor analysis of highly integrated "
      "digital control rooms.")

    # Chapter organisation
    H(b, lang, "Tổ chức chương", "Chapter organisation", level=3)
    P(b, lang,
      "Có những tương tác động hiện diện trong các hệ thống mà các cách "
      "tiếp cận truyền thống (phương pháp cây lỗi) không xử lý được. Bên "
      "cạnh đó, còn tồn tại các yêu cầu trong phân tích độ tin cậy và an "
      "toàn (ví dụ: cung cấp thông tin liên quan cho người sử dụng dưới "
      "dạng tập cắt và xác suất hỏng hóc, và khả năng tích hợp kết quả vào "
      "Đánh giá An toàn Xác suất (Probabilistic Safety Assessment, PSA)) "
      "phải được đáp ứng cùng với các tương tác động [4, 5, 8].",
      "There are dynamic interactions present in the systems that are not "
      "treated by the traditional approaches (fault trees methodology). In "
      "addition, there are existing requirements in reliability and safety "
      "analysis (e.g., the availability of relevant information to users "
      "(as cut sets and failure probabilities) and the possibility of "
      "incorporating the results into Probabilistic Safety Assessment "
      "(PSA)) that must be met in conjunction with the dynamic interactions "
      "[4, 5, 8].")
    P(b, lang,
      "Các phương pháp phù hợp để đánh giá an toàn và độ tin cậy là chìa "
      "khóa để xác lập tính chấp nhận được của các hệ thống I&amp;C số "
      "trong các hệ thống an toàn và điều khiển của nhà máy điện hạt nhân "
      "(phần cứng và phần mềm). Các mô hình độ tin cậy phù hợp với hệ "
      "thống I&amp;C số đang trong quá trình phát triển hoặc trong quá "
      "trình thẩm định.",
      "Appropriate methods for assessing safety and reliability are the "
      "key to establishing the acceptability of digital I&amp;C systems in "
      "safety and control systems of nuclear power plants (hardware and "
      "software). Reliability models suitable for digital I&amp;C systems "
      "are in development process or in validation process.")

    return b
