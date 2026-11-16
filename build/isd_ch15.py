# -*- coding: utf-8 -*-
"""Book 5, Chapter 15 — Conclusions (EN/VI bilingual).

Source: Heikkilä, *Inherent Safety in Process Plant Design — An Index-Based
Approach*, VTT Publications 384 (1999), pp. 118–120.  The doctoral thesis
conclusions: motivation, the two-part index (chemical + process), estimation
difficulties (equipment safety, process structure via CBR), flexible use and
weighting, relative nature of the indices, CBR for reuse of experience, GA
synthesis with the ISI as fitness, and the call for concurrent engineering.
"""

from isd_common import h2, p

PAGES_SRC = 3            # source pages 118–120
BYLINE = "Anna-Mari Heikkilä · VTT Publications 384 (1999)"
TITLE_EN = "Conclusions"
TITLE_VI = "Kết luận"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 15.</b> đánh giá an toàn sơ bộ · chỉ số "
                "an toàn nội tại hóa học / quá trình · tính tương đối của các "
                "chỉ số (relative, not absolute) · hồ sơ an toàn nội tại "
                "(inherent safety profile) · tái sử dụng kinh nghiệm thiết kế · "
                "kỹ thuật đồng thời (concurrent engineering).")
    return ("<b>Key terms.</b> preliminary safety evaluation · chemical / "
            "process inherent safety index · the relative (not absolute) "
            "nature of the indices · inherent safety profile · reuse of "
            "design experience · concurrent engineering.")


def body_vi():
    b = []

    b.append(h2("15. Kết luận", "15. Conclusions"))

    b.append(p("Mục tiêu của luận án tiến sĩ này là phát triển một phương pháp "
               "đánh giá an toàn nội tại trong thiết kế sơ bộ quá trình. Động "
               "lực của công việc là nhu cầu ngày càng tăng về đánh giá an "
               "toàn của quá trình ở giai đoạn đầu thiết kế — một phần do quy "
               "định của chính phủ, một phần vì lý do kỹ thuật thực tiễn. Để "
               "tránh mối nguy, việc nghiên cứu các đặc tính thay thế phải "
               "được thực hiện sớm trong thiết kế — ở giai đoạn sơ đồ công "
               "nghệ và thậm chí sớm hơn, khi quyết định sản phẩm gì sẽ được "
               "chế tạo và bằng lộ trình nào. <b>Ảnh hưởng đến an toàn nội tại "
               "dễ dàng hơn nhiều trong thiết kế khái niệm</b> so với các giai "
               "đoạn sau của thiết kế quá trình, vì lộ trình quá trình và các "
               "lựa chọn chính khác được đưa ra trong giai đoạn khái niệm; "
               "những quyết định này có tác động lớn đến an toàn nội tại. Thời "
               "gian và tiền bạc cũng được tiết kiệm khi cần ít sửa đổi an "
               "toàn đắt giá và ít thiết bị an toàn bổ sung hơn trong giải "
               "pháp quá trình cuối cùng."))

    b.append(p("Đánh giá an toàn có thể được xem như một phần của tổng hợp quá "
               "trình — gồm các khía cạnh kinh tế, môi trường và an toàn. Các "
               "phương án quá trình khác nhau phải được so sánh dựa trên tất "
               "cả các tiêu chí này. Vấn đề của các đánh giá an toàn sơ bộ "
               "nảy sinh từ <b>sự thiếu thông tin</b>; để giải quyết vấn đề "
               "này, cần một phương pháp chuyên dụng cho đánh giá an toàn nội "
               "tại sơ bộ."))

    b.append(p("Trong luận án, một <b>chỉ số an toàn nội tại</b> để đánh giá "
               "an toàn nội tại trong thiết kế sơ bộ quá trình đã được trình "
               "bày. An toàn nội tại của một quá trình chịu ảnh hưởng của cả "
               "khía cạnh hóa học lẫn kỹ thuật quá trình; hai khía cạnh được "
               "xét riêng vì chỉ số được chia thành <b>chỉ số an toàn nội tại "
               "hóa học</b> và <b>chỉ số an toàn nội tại quá trình</b>. Hai chỉ "
               "số này gồm nhiều chỉ số thành phần mô tả cụ thể hơn các khía "
               "cạnh an toàn riêng biệt. Chỉ số hóa học mô tả an toàn nội tại "
               "của các hóa chất trong quá trình: nhiệt phản ứng chính, nhiệt "
               "tối đa của các phản ứng phụ có thể, khả cháy, khả nổ, độc "
               "tính, khả ăn mòn và tương tác của các chất hiện diện. Chỉ số "
               "quá trình thể hiện an toàn của bản thân quá trình: tồn kho tối "
               "đa, nhiệt độ và áp suất quá trình tối đa, an toàn thiết bị và "
               "an toàn cấu trúc quá trình."))

    b.append(p("Các yếu tố hóa học và phần lớn yếu tố quá trình ảnh hưởng đến "
               "chỉ số khá trực tiếp để ước tính. Khó khăn hơn là an toàn thiết "
               "bị và an toàn cấu trúc quá trình. Chỉ số an toàn thiết bị được "
               "phát triển dựa trên đánh giá thống kê tai nạn và thông tin bố "
               "trí; đánh giá chỉ số cấu trúc quá trình an toàn dựa trên "
               "<b>suy luận dựa trên tình huống (CBR)</b>, đòi hỏi thông tin "
               "kinh nghiệm về các tình huống tai nạn và đặc tính vận hành của "
               "các cấu hình quá trình khác nhau."))

    b.append(p("Chỉ số an toàn nội tại có thể tính cho từng phân đoạn quá "
               "trình riêng hoặc cho cả quá trình, có hoặc không có OSBL. Các "
               "nhóm hóa học và quá trình có thể dùng cùng nhau hoặc riêng "
               "biệt. Các yếu tố riêng lẻ có thể được đề cao khác nhau tùy "
               "chính sách công ty và bài toán; do đó người dùng có thể đưa "
               "vào các trọng số khác nhau — thậm chí một trọng số chuẩn dựa "
               "trên xếp hạng chuyên gia đã được đưa ra. Cách tiếp cận này cho "
               "phép so sánh linh hoạt và tương tác các phương án quá trình "
               "theo an toàn nội tại. Cần nhớ rằng các chỉ số này là <b>đại "
               "lượng tương đối chứ không tuyệt đối</b> và không bao hàm đầy "
               "đủ mọi yếu tố. Để có một <b>hồ sơ an toàn nội tại</b>, cần xét "
               "các chỉ số thành phần riêng, chứ không chỉ chỉ số tổng; kết "
               "quả cũng nên được đọc với phán đoán."))

    b.append(p("Trong thiết kế, cùng một sai lầm thường được lặp lại vì việc "
               "sử dụng thông tin sẵn có không được tổ chức. Việc dùng CBR "
               "<b>tăng tái sử dụng kinh nghiệm sẵn có</b>, giảm khả năng cùng "
               "sai lầm xảy ra hơn một lần. Trong công trình này, CBR được dùng "
               "để đánh giá an toàn nội tại của cấu trúc quá trình; kho tình "
               "huống được thu thập từ tiêu chuẩn thiết kế, tài liệu tai nạn "
               "và thực hành kỹ thuật tốt."))

    b.append(p("ISI cũng có thể được dùng làm <b>hàm mục tiêu trong tổng hợp "
               "quá trình trên máy tính</b>. Tổng hợp quá trình có thể được "
               "xem như một bài toán tối ưu hóa; vì mô hình không liên tục, "
               "các phương pháp tối ưu thông thường không dùng được, thay vào "
               "đó một giải thuật di truyền được sử dụng: cấu trúc quá trình "
               "được biểu diễn dưới dạng chuỗi số nguyên mô tả các thao tác "
               "cần thiết và cách chúng được nối với nhau."))

    b.append(p("Hiện tại, các nghiên cứu an toàn chuyên sâu trong các dự án "
               "nhà máy quá trình chủ yếu diễn ra ở <b>các giai đoạn muộn của "
               "thiết kế</b> — khi tất cả những gì có thể làm là thêm thiết bị "
               "bảo vệ để tránh mối nguy. <b>Thiết kế an toàn nội tại sẽ không "
               "xuất hiện nếu không có thay đổi trong quy trình thiết kế</b>: "
               "nghĩa là dành thời gian cho việc nghiên cứu hệ thống các "
               "phương án trong giai đoạn đầu thiết kế. Chỉ số an toàn nội tại "
               "hỗ trợ nhà thiết kế chọn an toàn nội tại ngay từ đầu thiết kế "
               "nhà máy quá trình — thực chất đây là <b>kỹ thuật đồng thời "
               "(concurrent engineering)</b>: xem xét các chủ đề thiết kế đồng "
               "thời hơn thay vì cách tuần tự truyền thống."))

    return "".join(b)


def body_en():
    b = []

    b.append(h2("15. Conclusions", "15. Kết luận"))

    b.append(p("The aim of this doctoral thesis was to develop a method for "
               "inherent-safety evaluation in preliminary process design. The "
               "motivation has been an increasing need to evaluate the safety "
               "of processes in the early stage of process design — partly "
               "because of government regulations and also for practical "
               "engineering reasons. To avoid hazards, the studies of "
               "alternative features have to be carried out early in design, "
               "at the flowsheet stage and even earlier, when it is decided "
               "which product to make and by what route. It is much easier to "
               "affect inherent safety in the conceptual design than in the "
               "later phases of process design, because the process route and "
               "other main selections are made in the conceptual phase — and "
               "these decisions have a major effect on inherent safety. Time "
               "and money are also saved when fewer expensive safety "
               "modifications are needed and less added-on safety equipment "
               "is added to the final process solution."))

    b.append(p("The safety evaluation can be seen as a part of process "
               "synthesis, which includes economical, environmental and "
               "safety aspects. Different process alternatives have to be "
               "compared based on all of these criteria. The problems of "
               "preliminary safety evaluations arise from the <b>lack of "
               "information</b>; to solve this problem, a dedicated "
               "methodology for preliminary inherent-safety evaluations is "
               "required."))

    b.append(p("In this thesis an <b>inherent safety index</b> for evaluating "
               "inherent safety in preliminary process design was presented. "
               "The inherent safety of a process is affected by both chemical "
               "and process-engineering aspects; these have been dealt with "
               "separately, since the index was divided into the <b>Chemical "
               "Inherent Safety Index</b> and the <b>Process Inherent Safety "
               "Index</b>. These two indices consist of several subindices "
               "which further depict specific safety aspects. The Chemical "
               "Index describes the inherent safety of the chemicals in the "
               "process: the heat of the main reaction, the maximum heat of "
               "possible side reactions, flammability, explosiveness, "
               "toxicity, corrosiveness and the interaction of the substances "
               "present. The Process Index expresses the safety of the "
               "process itself: maximum inventory, maximum process "
               "temperature and pressure, equipment safety and the safety of "
               "the process structure."))

    b.append(p("The chemical and most process factors affecting the index are "
               "quite straightforward to estimate. More problematic are the "
               "equipment safety and the safety of the process structure. The "
               "equipment-safety subindex was developed based on the "
               "evaluation of accident statistics and layout information; the "
               "evaluation of the safe process structure subindex is based on "
               "<b>case-based reasoning (CBR)</b>, which requires "
               "experience-based information on accident cases and on the "
               "operation characteristics of different process "
               "configurations."))

    b.append(p("The Inherent Safety Index can be calculated either for "
               "separate process sections or for the process as a whole, with "
               "or without OSBL. The chemical and process categories can be "
               "used either together or separately. The individual factors "
               "may be emphasized differently depending on the company "
               "policies and the problem in hand; thus different weightings "
               "may be introduced by the user — even a standard weighting "
               "based on expert ranking has been given. This approach allows "
               "a flexible and interactive comparison of process alternatives "
               "in terms of inherent safety. It should be remembered that the "
               "various indices are <b>relative, not absolute, quantities</b> "
               "and they do not fully encompass all factors. To give an "
               "<b>inherent safety profile</b>, the separate subindices "
               "should be considered and not just the total index; the "
               "results should also be read with judgment."))

    b.append(p("In design it is typical that the same mistakes are done again, "
               "since the use of available information is not organized. The "
               "use of CBR <b>enhances the reuse of available experience</b>, "
               "which reduces the possibility that the same errors are done "
               "more than once. In this work, CBR was used for the evaluation "
               "of the inherent safety of the process structure; the casebase "
               "was collected from design standards, accident documents and "
               "good engineering practice."))

    b.append(p("The ISI can also be used as an <b>objective function in "
               "computerized process synthesis</b>. Process synthesis can be "
               "considered as an optimization task; because the model is "
               "uncontinuous, ordinary optimization methods could not be used, "
               "but a genetic algorithm was employed instead: the structure of "
               "the process was represented as a string of integers, which "
               "describes the operations required and how they are connected "
               "together."))

    b.append(p("At the moment, the more intensive safety studies in process "
               "plant projects take place mainly in the <b>late stages of "
               "design</b>, when all that can be done is to add protective "
               "equipment to avoid the hazard. <b>Inherently safer designs "
               "will not come about without a change in the design process</b>: "
               "this means making time available for the systematic study of "
               "alternatives during the early stages of design. The Inherent "
               "Safety Index assists designers to choose inherent safety from "
               "the very start of process plant design — in fact this refers "
               "to <b>concurrent engineering</b>: an approach where design "
               "topics are considered more concurrently instead of the "
               "traditional sequential way."))

    return "".join(b)
