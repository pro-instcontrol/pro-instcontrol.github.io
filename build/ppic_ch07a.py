# -*- coding: utf-8 -*-
"""Book 9, Chapter 7 (part A) — ABSTRACT, INTRODUCTION and the opening of the
METHODOLOGICAL FRAMEWORK (EN/VI bilingual).

Source: Boško Josimović and Saša Milijić, in L. N. Jalali (ed.), *Handbook on
Power Plant Instrumentation and Control* (Bibliotex, 2019), PDF pp. 141-145,
printed pp. 125-129 (absolute lines 3758-3896 of work/ppic_raw.txt). The
printed chapter title and byline are rendered by the page shell in
`ppic_ch07.py` (TITLE_EN/TITLE_VI and BYLINE); this module therefore starts
with the ABSTRACT heading, as the other chapter parts do.

The source span ends with the prose that leads into Figure 1; the figure
itself and Tables 7.1-7.3 are inserted by the next module. Printed bracketed
citations [1]-[33] are retained inline; no reference list is emitted here.
There are no equations, tables or figures in this module.
"""
try:
    import ppicfig7 as F  # noqa: F401  (shared supplier import style)
except ImportError:                       # supplier not written yet
    class _SupplierNamespace(object):
        pass
    F = _SupplierNamespace()


def _stub_tuple(n):
    """A minimal valid 5-tuple used only while the supplier is unavailable."""
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 60" '
        'role="img"><rect x="1" y="1" width="678" height="58" '
        'fill="#f4f6fa" stroke="#9aa7bd"/>'
        '<text x="340" y="35" text-anchor="middle" '
        'style="font:14px Helvetica,sans-serif;fill:#24364f">'
        'Figure 7.%d</text></svg>' % n
    )
    return (svg,
            "Hình 7.%d · Hình minh họa." % n,
            "Figure 7.%d · Illustration." % n,
            "Hình 7.%d" % n,
            "Figure 7.%d" % n)


# Never replace a real supplier callable: these stubs only fill missing names.
if not hasattr(F, "fig_f71"):
    F.fig_f71 = lambda: _stub_tuple(1)
if not hasattr(F, "fig_f72"):
    F.fig_f72 = lambda: _stub_tuple(2)

from ppic_ch07_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 7."""
    b = []

    # ---------------------------------------------------------------- ABSTRACT
    H(b, lang, "TÓM TẮT", "ABSTRACT", level=2)
    P(b, lang,
      "Đánh giá môi trường chiến lược (SEA) là một trong những công cụ chính để "
      "thực hiện các chiến lược phát triển bền vững trong quy hoạch nói chung, "
      "cụ thể là để phân tích và đánh giá các quan niệm phát triển không gian, "
      "trong trường hợp này là trong lĩnh vực năng lượng và quy hoạch nhà máy "
      "điện. SEA trong quy hoạch ngành năng lượng đã trở thành công cụ để xem "
      "xét các lợi ích và hậu quả của những thay đổi được đề xuất trong không "
      "gian, đồng thời tính đến khả năng của không gian duy trì việc thực hiện "
      "các hoạt động đã được quy hoạch. Chương này xem xét phương pháp đánh giá "
      "đa tiêu chí (MCE) để tiến hành SEA cho các nhà máy điện trong Chiến lược "
      "phát triển ngành năng lượng của Cộng hòa Serbia (nghiên cứu điển hình). "
      "Phương pháp MCE đã được ứng dụng trong phân tích và đánh giá các tác "
      "động không gian của ngành năng lượng đối với môi trường và các yếu tố "
      "phát triển bền vững và, trong bối cảnh này, cũng xem xét tầm quan trọng "
      "của các tác động, sự phân tán không gian của chúng, xác suất và tần suất "
      "xuất hiện, cùng với việc trình bày các kết quả thu được một cách cụ "
      "thể, đơn giản và rõ ràng. Chương tập trung vào xem xét các khía cạnh "
      "tác động môi trường của mọi loại nhà máy điện, không đi vào chi tiết "
      "các khía cạnh khác của phát triển ngành năng lượng được đề cập trong "
      "nghiên cứu điển hình.",
      "Strategic Environmental Assessment (SEA) is one of the key instruments "
      "for implementing sustainable development strategies in planning in "
      "general, namely for analysing and assessing the spatial development "
      "concepts, in this case in the field of energy and planning of power "
      "plants. The SEA in energy sector planning has become a tool for "
      "considering the benefits and consequences of the proposed changes in "
      "space, also taking into account the capacity of space to sustain the "
      "implementation of the planned activities. This chapter examines the "
      "multi-criteria evaluation (MCE) method for carrying out an SEA for the "
      "power plants in Energy Sector Development Strategy of the Republic of "
      "Serbia (case study). The MCE method has found its use in the analysis "
      "and assessment of the energy sector spatial impacts on the environment "
      "and elements of sustainable development and, in this context, also "
      "considering the importance of impacts, spatial dispersion of impacts, "
      "their probability and frequency of occurrence, along with the "
      "elaboration of the obtained results in a specific, simple and "
      "unambiguous way. The chapter focuses on the consideration of aspects "
      "of environmental impact of all kinds of power plants, without taking "
      "into account the details regarding other aspects of energy sector "
      "development that are dealt with in the case study.")

    # ---------------------------------------------------------------- KEYWORDS
    P(b, lang,
      "<b>Từ khóa:</b> đánh giá môi trường chiến lược, nhà máy điện, đánh giá "
      "đa tiêu chí",
      "<b>Keywords:</b> strategic environmental assessment, power plants, "
      "multi-criteria evaluation")

    # ------------------------------------------------------------ INTRODUCTION
    H(b, lang, "GIỚI THIỆU", "INTRODUCTION", level=2)
    P(b, lang,
      "Đánh giá môi trường chiến lược (SEA) có thể được coi là công cụ quan "
      "trọng nhất, tổng quát nhất và toàn diện nhất để định hướng quá trình "
      "quy hoạch chiến lược theo các nguyên tắc và mục tiêu bảo vệ môi "
      "trường, cũng như để đưa ra các quyết định tối ưu cho phát triển không "
      "gian bền vững trong tương lai [1] có thể được coi là một. Ngay từ đầu "
      "thập niên cuối cùng của thế kỷ hai mươi cho đến nay, nhiều tác giả "
      "[2–7] đã viết về tầm quan trọng của việc thực hiện SEA trong quá trình "
      "ra quyết định tối ưu về phát triển không gian bền vững và về quan niệm "
      "chính sách phát triển trong các lĩnh vực hoạt động xã hội khác nhau "
      "(năng lượng, quản lý tài nguyên nước, hạ tầng, du lịch, v.v.). Vì vậy, "
      "vấn đề này rất đáng quan tâm cả về mặt khoa học lẫn chuyên môn, và có "
      "tầm quan trọng lớn trong việc xây dựng bất kỳ chính sách môi trường "
      "nào.",
      "The strategic environmental assessment (SEA) can be considered as the "
      "most important, the most general and the most comprehensive instrument "
      "for directing the strategic planning process towards the principles "
      "and objectives of environmental protection, as well as for making "
      "optimum decisions on future sustainable spatial development [1] can be "
      "considered one. Since the very beginning of the last decade of the "
      "twentieth century until now, many authors [2–7] have written about the "
      "importance of the implementation of SEA in the process of making "
      "optimum decisions on sustainable spatial development and on the concept "
      "of development policy in different fields of social activities "
      "(energy, water resource management, infrastructure, tourism, etc.). "
      "The issue is therefore quite interesting, from both scientific and "
      "professional aspects, and is of great importance in creating any "
      "environmental policy.")

    P(b, lang,
      "Chỉ thị Đánh giá Môi trường Chiến lược châu Âu 2001/42/EC [8] quy định "
      "nghĩa vụ tiến hành SEA cho các kế hoạch, chương trình và văn bản khung "
      "trong các lĩnh vực khác nhau, do đó cả trong lĩnh vực năng lượng. Nhờ "
      "SEA, có thể xem xét các hệ quả tích cực và tiêu cực của những thay đổi "
      "được đề xuất ở giai đoạn sớm nhất của việc xây dựng chính sách phát "
      "triển và từ đó định hướng quá trình quy hoạch theo hướng tăng tác động "
      "tích cực, giảm thiểu hệ quả tiêu cực. Quá trình SEA không tránh khỏi "
      "việc huy động sự tham gia của công chúng ở mọi giai đoạn của quá trình "
      "quy hoạch, qua đó nhấn mạnh đóng góp vào việc ra quyết định, trong "
      "trường hợp này là trong lĩnh vực phát triển ngành năng lượng [9–13]. "
      "So với các phương pháp khác góp phần vào việc ra quyết định, chẳng hạn "
      "như “đánh giá vòng đời” (LCA) truyền thống [14–17] chủ yếu được dùng để "
      "phân tích tác động trong các đơn vị lãnh thổ nhỏ hơn, SEA góp phần "
      "tích hợp các tác động ở cấp chiến lược của quy hoạch nhà máy điện (cấp "
      "quốc gia, khu vực và, nếu cần, cấp quốc tế). Với việc cấp chiến lược "
      "của quy hoạch đòi hỏi xem xét đa chiều các hiện tượng và quá trình, và "
      "việc đưa ra quyết định phù hợp về các tác động không gian và phát "
      "triển không gian là một quá trình phức tạp, cần có cách tiếp cận vấn đề "
      "và phương pháp luận phù hợp để đưa ra quyết định đúng đắn về tính bền "
      "vững của các phương án phát triển được đề xuất. Điều này đặc biệt cần "
      "thiết khi xây dựng chính sách ngành năng lượng, nơi xu hướng phát "
      "triển có thể có hệ quả đáng kể đối với không gian và môi trường. Phân "
      "tích đa tiêu chí đã được nhiều tác giả có chuyên môn trong lĩnh vực "
      "năng lượng khuyến nghị mạnh mẽ [18, 19].",
      "The European Strategic Environmental Assessment Directive 2001/42/EC "
      "[8] prescribes the obligation to undertake SEA for plans, programmes "
      "and framework documents in different fields, thus also in the field of "
      "energy sector. By using the SEA, it is possible to consider the "
      "positive and negative implications of the proposed changes in the "
      "earliest stages of creating a development policy and accordingly "
      "direct the planning process in a way to increase positive impacts and "
      "minimize negative implications. The SEA process unavoidably implies "
      "the participation of the public in all stages of the planning process, "
      "thus emphasizing the contribution in decision-making, in this case in "
      "the field of the energy sector development [9–13]. Compared to other "
      "methods that contribute to decision-making, such as the traditional "
      "’life cycle assessment’ (LCA) [14–17] which is mainly used for the "
      "analysis of impacts in smaller territorial units, the SEA contributes "
      "to integrating the impacts at the strategic level of power plants "
      "planning (national, regional and, if necessary, international level). "
      "Given that the strategic level of planning requires a multi-dimensional "
      "consideration of phenomena and processes and that making appropriate "
      "decisions on spatial impacts and spatial development is a complex "
      "process, it is necessary to have an appropriate problem and "
      "methodological approach to making appropriate decisions on "
      "sustainability of offered concepts of development. This is particularly "
      "necessary in conceiving an energy sector policy, where the development "
      "tendencies can have significant implications for space and the "
      "environment. Multi-criteria analysis has been strongly advised by "
      "various authors with expertise in the energy sector [18, 19].")

    P(b, lang,
      "Chương này sẽ trình bày khả năng và tầm quan trọng của việc sử dụng SEA "
      "để phân tích tác động không gian của các nhà máy điện, bất kể đó là nhà "
      "máy điện nhiên liệu hóa thạch hay nhà máy điện sử dụng nguồn năng lượng "
      "tái tạo (RESs), vì cả hai đều có thể có tác động có ý nghĩa chiến lược "
      "(tích cực và tiêu cực) đối với không gian nơi chúng được xây dựng. "
      "Chương sẽ xem xét phương pháp đánh giá đa tiêu chí (MCE) để tiến hành "
      "SEA cho nghiên cứu điển hình – Chiến lược phát triển ngành năng lượng "
      "của Cộng hòa Serbia đến năm 2025, với dự báo đến năm 2030 [20] (sau "
      "đây gọi là “Chiến lược”).",
      "The chapter will present the possibility and importance of using the "
      "SEA for analysing spatial impact of power plants, regardless of whether "
      "it comes to fossil fuel power plants or power plants using renewable "
      "energy sources (RESs) because both can have strategically significant "
      "impacts (positive and negative) on the space where they are built. The "
      "chapter will examine the multi-criteria evaluation (MCE) method for "
      "carrying out an SEA for the case study–Energy Sector Development "
      "Strategy of the Republic of Serbia by 2025 with projections until 2030 "
      "[20] (herein after referred to as the ‘Strategy’).")

    # --------------------------------------------------- METHODOLOGICAL FRAMEWORK
    H(b, lang, "KHUNG PHƯƠNG PHÁP", "METHODOLOGICAL FRAMEWORK", level=2)
    P(b, lang,
      "Khái niệm về phương pháp luận SEA, khác với các công cụ đa dạng, chính "
      "xác và dễ vận hành cao được dùng trong kỹ thuật môi trường hoặc các "
      "lĩnh vực dựa trên khoa học khác, khá mơ hồ [21]. Một số tác giả [22–24] "
      "cho rằng không có cách tiếp cận phương pháp luận thống nhất đối với "
      "quá trình SEA, vì việc sử dụng nó trong các quá trình quy hoạch rất "
      "khác nhau về chủ đề là không phù hợp, mà cách phù hợp nhất là dùng các "
      "cách tiếp cận phương pháp luận khác nhau hoặc sự kết hợp giữa chúng, "
      "phù hợp với điều kiện cụ thể mà quá trình quy hoạch được tiến hành "
      "[22, 25]. Theo những điều đã nêu trên, có thể kết luận rằng quá trình "
      "SEA nên dựa trên cách tiếp cận liên ngành và mở đối với việc sử dụng "
      "các cách tiếp cận phương pháp luận khác nhau. Sự linh hoạt này trong "
      "cách tiếp cận quá trình SEA để ngỏ khả năng tìm ra các giải pháp tốt "
      "nhất phù hợp với cách tiếp cận cụ thể đối với quá trình quy hoạch.",
      "The concept of the SEA methodologies, unlike the diverse, precise and "
      "highly operable tools used in environmental engineering or other "
      "science-based areas, is rather fuzzy [21]. Some authors [22–24] believe "
      "that there is no uniform methodological approach to the SEA process "
      "because its use in very thematically different planning processes is "
      "not appropriate, but it is the most appropriate to use different "
      "methodological approaches or their combination that would be aligned "
      "with specific conditions in which the planning process is carried out "
      "[22, 25]. In accordance with the above-mentioned, it can be concluded "
      "that the SEA process should be based on an interdisciplinary approach "
      "and open to the use of different methodological approaches. Such "
      "flexibility in the approach to the SEA process leaves the possibility "
      "of finding the best solutions in accordance with specific approaches "
      "to the planning process.")

    P(b, lang,
      "Nói chung, các kỹ thuật và phương pháp luận SEA bắt nguồn từ Đánh giá "
      "Tác động Môi trường (EIA) truyền thống và các nghiên cứu đánh giá "
      "chính sách/đánh giá kế hoạch [25, 26], đảm bảo rằng các phương pháp "
      "luận không trở thành rào cản đối với việc thúc đẩy SEA trong các tổ "
      "chức [27]. Nhiều kỹ thuật khác nhau để tiến hành các bước khác nhau của "
      "SEA đã được các tác giả khác phân tích và thảo luận thêm "
      "[1, 25, 27–29]. Ngoài ra, Marsden [30] chỉ ra rằng, về mặt phương pháp "
      "luận, quá trình SEA chủ yếu dựa trên cách tiếp cận định tính hoặc bán "
      "định lượng, phụ thuộc rất nhiều vào kỹ năng và kiến thức của các chuyên "
      "gia tham gia vào quá trình đánh giá. Cách tiếp cận như vậy cũng hàm ý "
      "một mức độ chủ quan nhất định cần được giảm thiểu bằng cách sử dụng "
      "các gói phần mềm khác nhau (như hệ thống thông tin địa lý [GIS]) kết "
      "hợp với kinh nghiệm sử dụng phù hợp tích lũy được qua các nghiên cứu "
      "so sánh về các sơ đồ và ứng dụng trước đây [21].",
      "Generally speaking, the SEA techniques and methodologies derive from "
      "the traditional Environmental Impact Assessment (EIA) and policy "
      "appraisal/plan evaluation studies [25, 26], ensuring that methodologies "
      "would not become a barrier for institutional promotion of the SEA "
      "[27]. A variety of possible techniques for conducting the different "
      "steps of SEA have been further analysed and discussed by others "
      "[1, 25, 27–29]. In addition, Marsden [30] pointed out that, in terms "
      "of methodologies, the SEA process is dominantly based on the "
      "qualitative or semi-quantitative approach which to a great extent "
      "depends on the skills and knowledge of experts involved in the "
      "evaluation process. Such an approach also implies a certain degree of "
      "subjectivity that should be minimized by using different software "
      "packages (like geographic information system [GIS]) in combination "
      "with their adequate use experiences accumulated through comparative "
      "studies of past schemes and applications [21].")

    P(b, lang,
      "Khung thủ tục và phương pháp luận cho SEA được thể hiện trong Hình 1. "
      "Quá trình SEA bắt đầu bằng việc ra quyết định về tiến hành SEA, cũng "
      "như về phạm vi và nội dung của nó. Giai đoạn này bao gồm việc xác định "
      "khung cho các cuộc điều tra sẽ được tiến hành trong quá trình SEA, "
      "cùng với sự tham gia không thể thiếu của công chúng, các tổ chức liên "
      "quan và các tổ chức phi chính phủ (NGOs). Giai đoạn tiếp theo gồm phần "
      "phân tích của quá trình SEA, bao hàm việc phân tích tình trạng môi "
      "trường trong khu vực được điều tra bằng công nghệ GIS [31–33]; phân "
      "tích quan niệm chiến lược phát triển (trong trường hợp này là ngành "
      "năng lượng); phân tích so sánh các văn bản quy hoạch và chiến lược "
      "liên quan đến không gian được điều tra và đến lĩnh vực điều tra cụ "
      "thể; cùng các cuộc điều tra và phân tích khác có tầm quan trọng đối "
      "với lĩnh vực điều tra cụ thể. Giai đoạn tiếp theo là xác định các mục "
      "tiêu SEA, các chỉ số liên quan (Bảng 1) và tiêu chí đánh giá (Bảng 2 "
      "và 3), tiếp theo là quy trình đánh giá tác động trong đó bước đầu tiên "
      "gồm đánh giá các kịch bản thay thế và lựa chọn phương án phù hợp nhất. "
      "Sau đó, quá trình đánh giá đa tiêu chí (phương pháp bán định lượng) "
      "được tiến hành, là điểm trọng tâm của chương này (trình bày ở mục 3 "
      "trong bài). Vai trò của đánh giá đa tiêu chí là xác định ảnh hưởng của "
      "các hoạt động được quy hoạch trong không gian nơi chúng được thực "
      "hiện (dự báo các ảnh hưởng không gian) theo các mục tiêu SEA. Khi các "
      "tác động của Chiến lược đã được xác định theo cách này, có thể trình "
      "bày và diễn giải chúng một cách đơn giản, rõ ràng và dễ hiểu đối với "
      "tất cả các chủ thể trong quá trình SEA, cụ thể là các chủ thể tham gia "
      "vào quá trình ra quyết định.",
      "The procedural and methodological framework for SEA is shown in Figure "
      "1. The SEA process begins with decision-making on undertaking the SEA, "
      "as well as on its scope and contents. This stage involves the defining "
      "of framework for investigations to be carried out in the SEA process "
      "along with the unavoidable participation of the public, relevant "
      "institutions and non-governmental organizations (NGOs). The next stage "
      "includes the analytical part of the SEA process implying the analysis "
      "of the state of the environment in the area under investigation using "
      "the GIS technologies [31–33]; analysis of the strategic concept of "
      "development (in this case in the energy sector); comparative analysis "
      "of the planning and strategic documents relating to the space that is "
      "subject of investigation and to the specific field of investigation; "
      "other investigations and analyses of importance for the specific field "
      "of investigation. The next stage included the setting of the SEA "
      "objectives, relevant indicators (Table 1) and evaluation criteria "
      "(Tables 2 and 3), followed by an impact assessment procedure in which "
      "the first stage included the evaluation of alternative scenarios and "
      "the selection of the most suitable alternative. Then, the process of "
      "multi-criteria evaluation (a semi-quantitative method) followed, "
      "representing the focal point of this chapter (presented in point 3 "
      "herein). The role of multi-criteria evaluation is to identify the "
      "influence of the activities planned in the space in which they are "
      "being undertaken (the prediction of spatial influences) according to "
      "the SEA objectives. When the impacts of the Strategy are identified in "
      "such a way, then it is possible to elaborate and present them in a "
      "simple and unambiguous way and in a way that is clear to all actors in "
      "the SEA process, namely the actors included in the decision-making "
      "process.")

    return b
