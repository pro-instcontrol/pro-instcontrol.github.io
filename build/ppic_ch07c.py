# -*- coding: utf-8 -*-
"""Chapter 7, section C - continuation of the MCE discussion and the opening
of the power-plants case study (printed pp. 132-136, PDF pp. 148-152).

Source: work/ppic_raw.txt, absolute lines 3907-4046. Stops immediately before
the Table 4 caption. No figures or tables are inserted here.
"""
from ppic_ch07_lib import H, P


def section(lang):
    b = []

    P(b, lang,
      "Các mục tiêu SEA cụ thể (Bảng 7.1) được xác lập trong một số lĩnh vực nhất định của bảo vệ "
      "môi trường. Các mục tiêu SEA cụ thể là những phát biểu cụ thể, được định tính một phần, dưới "
      "dạng các định hướng và hành động (biện pháp, công trình và hoạt động) nhằm thực hiện những "
      "thay đổi này. Trước hết, các mục tiêu SEA cụ thể là một biện pháp phương pháp luận, thông qua "
      "đó các tác động của nhà máy điện (và của ngành năng lượng nói chung) lên môi trường được nhận "
      "diện và kiểm tra. Việc đánh giá đa tiêu chí các phương án quy hoạch được thực hiện dựa trên "
      "các mục tiêu này nhằm có được cái nhìn rõ ràng về những tác động có thể có của quá trình quy "
      "hoạch, từ đó đưa ra các quyết định tối ưu cho phát triển không gian bền vững trong tương lai.",
      "The specific SEA objectives (Table 7.1) were set in certain fields of environmental "
      "protection. The specific SEA objectives are the concrete, partially qualified statements in "
      "a form of guidelines and actions (measures, works and activities) for the implementation of "
      "these changes. The specific SEA objectives are primarily a methodological measure through "
      "which the effects of power plants (and energy sector in general) on the environment are "
      "identified and checked. The multi-criteria evaluation of the planning solutions is carried "
      "out in relation to these objectives to obtain a clear idea about possible effects of the "
      "planning process and make optimum decisions on future sustainable spatial development "
      "accordingly.")

    P(b, lang,
      "Các chỉ số phát triển bền vững (Bảng 7.1) cần thiết để nhận diện các xu hướng tiến tới hoặc "
      "xa rời tính bền vững, cũng như để xác định các mục tiêu cải thiện phúc lợi chung. Năm 2008, "
      "Cộng hòa Serbia đã thông qua Chiến lược phát triển ngành năng lượng quốc gia [35], trong đó có "
      "các nguyên tắc và ưu tiên về phát triển bền vững, cũng như 76 chỉ số để theo dõi tiến trình "
      "của Serbia hướng tới phát triển bền vững. Các chỉ số này được lựa chọn từ bộ chỉ số của Liên "
      "Hợp Quốc, nhưng không phải chỉ số nào cũng được sử dụng ở Serbia. Các chỉ số được quy định "
      "trong Luật về Kế hoạch không gian của Cộng hòa Serbia [36]. Quy định về Danh mục quốc gia các "
      "chỉ số môi trường [37] đã quy định danh mục các chỉ số môi trường được sử dụng trong nghiên "
      "cứu này. Các chỉ số SEA được lựa chọn phù hợp với các mục tiêu SEA nêu trên. Bộ chỉ số này dựa "
      "trên khái niệm ‘nguyên nhân – tác động – phản ứng’ (‘cause-effect-response’). Các chỉ số "
      "nguyên nhân biểu thị các hoạt động, quá trình và mối quan hệ của con người ảnh hưởng đến môi "
      "trường; các chỉ số tác động biểu thị trạng thái của môi trường; trong khi các chỉ số phản ứng "
      "xác định các lựa chọn chiến lược và các phản ứng khác nhằm thay đổi ‘hậu quả’ đối với môi "
      "trường.",
      "The sustainable development indicators (Table 7.1) are needed to identify trends of moving "
      "towards or away from sustainability, as well as to set goals for improving general "
      "well-being. In 2008, the Republic of Serbia adopted the National Energy Sector Development "
      "Strategy [35] which contains principles and priorities in sustainable development, as well "
      "as 76 indicators for tracking the progress of Serbia towards sustainable development. These "
      "indicators have been selected from the set of UN indicators, but not all of indicators are "
      "used in Serbia. The indicators are specified in the Law on Spatial Plan of the Republic of "
      "Serbia [36]. The Regulation on the National List of Environmental Indicators [37] prescribes "
      "the list of environmental indicators, which have been used herein. The SEA indicators have "
      "been selected in accordance with the above-mentioned SEA objectives. This set of indicators "
      "is based on the ‘cause-effect-response’ concept. The indicators of cause denote human "
      "activities, processes and relationships affecting the environment, the indicators of effect "
      "denote the state of the environment, while the indicators of response define strategic "
      "options and other responses aimed at changing ‘consequences’ for the environment.")

    P(b, lang,
      "Dựa trên phân tích khả năng ưu tiên xem xét khía cạnh không gian, cũng như khía cạnh vấn đề "
      "của các tác động tiềm ẩn, ba nhóm tiêu chí với tổng số 14 tiêu chí riêng lẻ đã được xác định. "
      "Các tiêu chí được sử dụng trong đánh giá đa tiêu chí các phương án quy hoạch liên quan đến độ "
      "lớn (cường độ) của tác động, kích thước không gian của tác động và xác suất xảy ra tác động "
      "(Bảng 7.2).",
      "Based on an analysis of the possibility of primarily considering the spatial aspect, as well "
      "as the problematic aspect of potential impacts, three sets of criteria with a total of 14 "
      "individual criteria were defined. The criteria used in the MCE of the planning solutions "
      "were related to the magnitude (intensity) of the impact, the spatial dimension of the impact "
      "and the impact probability (Table 7.2).")

    P(b, lang,
      "Tầm quan trọng của các tác động đã được nhận diện đối với việc đạt được các mục tiêu SEA được "
      "đánh giá. Theo các tiêu chí trình bày tại Bảng 7.3, những tác động có ý nghĩa đối với Chiến "
      "lược đang xem xét là những tác động có ảnh hưởng mạnh hơn hoặc lớn hơn ở cấp quốc tế (xuyên "
      "biên giới), quốc gia hoặc khu vực.",
      "The importance of identified impacts for achieving the SEA objectives is evaluated. The "
      "impacts of importance for the subject Strategy are those which have stronger or greater "
      "effects on the international (transboundary), national or regional level, according to the "
      "criteria shown in Table 7.3.")

    P(b, lang,
      "Khung phương pháp luận cho SEA trình bày trong chương này tập trung vào cách tiếp cận dựa trên "
      "kế hoạch và việc sử dụng phương pháp MCE cho các hoạt động đã định và các yếu tố quyết định "
      "chiến lược liên quan đến sức chứa của không gian, làm cơ sở để đánh giá giá trị của không gian "
      "dành cho phát triển bền vững [38].",
      "The methodological framework for the SEA presented in this chapter is centred on a "
      "plan-based approach to and the use of MCE method for the planned activities and strategic "
      "determinants in relation to the capacity of space as a basis for the valorization of space "
      "earmarked for sustainable development [38].")

    P(b, lang,
      "Sự phát triển của phương pháp MCE gắn liền với những năm đầu thập niên 1970 của thế kỷ XX, khi "
      "nhiều tác giả [39–41] bắt đầu phát triển cách tiếp cận này. Khi mới ra đời, MCE được đặc trưng "
      "bởi nguyên tắc phương pháp luận về ra quyết định đa tiêu chí (MCDM), với ít hoặc không có cơ "
      "chế tham gia [42, 43]. Ý tưởng ban đầu là thu thập các ưu tiên rõ ràng từ người ra quyết định, "
      "sau đó giải quyết một bài toán có cấu trúc tốt bằng các thuật toán toán học (ví dụ: thiết kế "
      "một động cơ có xét đến công suất, trọng lượng và hiệu suất). Theo thời gian, ý tưởng đầy tham "
      "vọng này được hướng tới một cách tiếp cận duy lý hơn [44] và một cách tiếp cận mang tính xây "
      "dựng hoặc sáng tạo [45], dẫn đến một cách tiếp cận dựa trên sự phát triển của hỗ trợ ra quyết "
      "định đa tiêu chí (MCDA), đặc trưng bằng việc đặt quá trình ra quyết định về các tiến trình "
      "phát triển cụ thể vào trọng tâm, nghĩa là nâng cao mức độ và chất lượng của quá trình này "
      "đồng thời đưa công chúng tham gia thường xuyên ở mọi giai đoạn xây dựng tương lai phát triển "
      "[46–48]. Cách tiếp cận này đã dẫn đến sự xuất hiện của đánh giá đa tiêu chí có sự tham gia "
      "(PMCE) [46, 49] và đánh giá đa tiêu chí xã hội (SMCE) [50]. Ngày nay, phương pháp MCE thường "
      "được khuyến nghị như một công cụ hỗ trợ thuận tiện trong quá trình ra quyết định, nhờ khả năng "
      "chỉ ra theo nhiều cách các phương án phát triển đa dạng dựa trên việc đánh giá các tiêu chí "
      "liên quan đến môi trường và các khía cạnh kinh tế - xã hội của phát triển bền vững [51–54].",
      "The development of the MCE method is linked to the early 1970s of the twentieth century when "
      "many authors [39–41] began to develop such an approach. When first developed, the MCE was "
      "characterized by the methodological principle of multi-criteria decision-making (MCDM) with "
      "little or no participatory mechanisms included [42, 43]. The initial idea was to elicit clear "
      "preferences from a decision-maker and then solve a well-structured problem by means of "
      "mathematical algorithms (e.g. to design an engine by taking into account its power, weight "
      "and efficiency). Over time, this ambitious idea has been directed towards a more rational "
      "approach [44] and to a constructive or a creative approach [45], which has led to an approach "
      "based on the development of the multi-criteria decision aid (MCDA) that is characterized by "
      "placing in focus the process of decision-making on specific development processes, namely the "
      "raising of the level and quality of this process along with permanently including the public "
      "into all stages of creating the future development [46–48]. This approach has resulted in the "
      "emergence of the participatory multi-criteria evaluation (PMCE) [46, 49] and social "
      "multi-criteria evaluation (SMCE) [50]. Nowadays, the MCE method is often recommended as a "
      "convenient support in the decision-making process because of its capacity to point out in "
      "many ways multiple alternatives of development on the basis of assessing criteria related to "
      "the environment and socio-economic aspects of sustainable development [51–54].")

    P(b, lang,
      "Phương pháp MCE được trình bày và phân tích trong chương này ban đầu được xác định trong một dự "
      "án nghiên cứu khoa học có tên ‘Phương pháp đánh giá môi trường chiến lược trong quy hoạch’ "
      "(2005–2007). Sau đó, phương pháp này được phát triển và nâng cấp thông qua một số dự án khoa "
      "học trong nước và quốc tế, có sự tham gia của Viện Kiến trúc và Quy hoạch Đô thị &amp; Không "
      "gian Serbia (IAUS). Kết quả nghiên cứu và phát triển phương pháp đã được ứng dụng trong việc "
      "xây dựng nhiều văn bản chiến lược ở cấp quốc gia và khu vực, trong các lĩnh vực năng lượng, "
      "quản lý tài nguyên nước, quản lý chất thải, du lịch và các lĩnh vực khác. Một ví dụ về áp dụng "
      "phương pháp MCE được trình bày trong phần tiếp theo.",
      "The MCE method presented and elaborated in this chapter was originally defined in a "
      "scientific research project entitled ‘Method for Strategic Environmental Assessment in "
      "Planning’ (2005–2007). The method was later developed and upgraded through several domestic "
      "and international scientific projects, in which the Institute of Architecture and Urban "
      "&amp; Spatial Planning of Serbia (IAUS) also participated. The results of the research and "
      "method development have found their applicability in the drawing up of a number of strategic "
      "documents at national and regional levels, in the fields of energy, water resource "
      "management, waste management, tourism and so on. An example of the application of the MCE "
      "method is shown in the text that follows.")

    H(b, lang,
      "NGHIÊN CỨU ĐIỂN HÌNH: PHƯƠNG PHÁP MCE TRONG SEA CHO CÁC NHÀ MÁY ĐIỆN TRONG CHIẾN LƯỢC",
      "CASE STUDY: MCE METHOD IN THE SEA FOR THE POWER PLANTS IN THE STRATEGY", level=2)

    P(b, lang,
      "Các kết quả trình bày trong phần này của chương được lấy từ SEA cho Chiến lược [34] (nghiên "
      "cứu điển hình), do chính các tác giả của chương này thực hiện. Cách tiếp cận phương pháp luận "
      "nêu trên đã được sử dụng khi xây dựng văn bản đó; ở đây chỉ trình bày những kết quả nằm trong "
      "bối cảnh của chủ đề nghiên cứu này và đã được điều chỉnh nhẹ để phù hợp với thể thức của "
      "chương.",
      "The results presented in this part of the chapter have been taken from the SEA for the "
      "Strategy [34] (case study), conducted by the authors of this chapter. The mentioned "
      "methodological approach was used in drawing up the mentioned document, while only the "
      "results that are in the context of the theme of this research and that were partially "
      "slightly modified to adapt them to the format of this chapter are elaborated herein.")

    H(b, lang, "Đối tượng của Chiến lược và SEA",
      "Subject of the Strategy and SEA", level=3)

    P(b, lang,
      "Cách tiếp cận quy hoạch tích hợp và liên tục đã được sử dụng khi xây dựng Chiến lược và thực "
      "hiện SEA, tập trung vào việc tìm kiếm các biện pháp hướng tới tính bền vững thông qua kết hợp "
      "giữa, một mặt, các mục tiêu thực tế và tiềm năng trong lĩnh vực năng lượng, và mặt khác, các "
      "mục tiêu và nhu cầu về bảo vệ môi trường, chất lượng cuộc sống của người dân và phát triển "
      "kinh tế - xã hội. Chiến lược sẽ là khuôn khổ cho sự phát triển của hệ thống năng lượng của Cộng "
      "hòa Serbia với mọi hệ quả có thể có (tích cực và tiêu cực) đối với chất lượng môi trường. Mục "
      "đích của việc thực hiện SEA cho Chiến lược là xem xét các tác động xu hướng có thể có đối với "
      "chất lượng môi trường, cũng như xây dựng các định hướng nhằm giảm thiểu chúng, tức là đưa "
      "chúng vào trong giới hạn chấp nhận được mà không tạo ra xung đột trong không gian và có tính "
      "đến sức chứa môi trường của khu vực đang xem xét.",
      "The approach of integrated and continuous planning was used in creating the Strategy and "
      "carrying out the SEA with a focus on finding the measures for sustainability through "
      "integrating the realistic goals and the potentials in the field of energy, on the one hand, "
      "and the goals of and needs for environmental protection, quality of life of population and "
      "socio-economic development, on the other hand. The Strategy will be a framework for the "
      "development of the energy system of the Republic of Serbia with all possible (positive and "
      "negative) implications for the environmental quality. The purpose of carrying out the SEA "
      "for the Strategy is to consider possible negative effects on/trends of environmental "
      "quality, as well as to develop the guidelines for their reduction, namely bringing them "
      "within acceptable limits without creating the conflicts in space and taking into account "
      "the environmental capacity in the considered area.")

    P(b, lang,
      "SEA không chỉ tập trung vào phân tích các cam kết chiến lược có thể dẫn đến tác động và xu "
      "hướng tiêu cực, mà còn vào các cam kết chiến lược có thể góp phần bảo vệ môi trường và nâng "
      "cao chất lượng cuộc sống của người dân. Trong bối cảnh này, các tác động môi trường tiềm ẩn "
      "của các hoạt động đã định đã được phân tích trong SEA và được đánh giá dựa trên các mục tiêu "
      "và chỉ số.",
      "The SEA is not focused only on the analysis of strategic commitments that can imply "
      "negative impacts and trends but also on the strategic commitments that can contribute to "
      "environmental protection and quality of life of population. In this context, the potential "
      "environmental impacts of planned activities were analysed in the SEA and were evaluated "
      "relative to the objectives and indicators.")

    P(b, lang,
      "Chương của Chiến lược liên quan đến các ưu tiên phát triển ngành năng lượng nhắc đến nhà máy "
      "điện như một trong những yếu tố then chốt và tiềm năng thiết yếu cho phát triển, nhưng cũng là "
      "nguyên nhân có thể gây ra các vấn đề đáng kể về môi trường. Vì lý do này, chương nhấn mạnh sự "
      "cần thiết phải đưa các công nghệ mới nhất vào sản xuất năng lượng, cả trong các nhà máy nhiệt "
      "điện lẫn trong lĩnh vực nguồn năng lượng tái tạo (RES), vốn có tiềm năng rất lớn nhưng chưa "
      "được sử dụng đầy đủ ở Cộng hòa Serbia.",
      "The chapter of the Strategy related to the priorities of the energy sector development "
      "mentions the power plants as one of the keys and essential potentials for development, but "
      "also as a possible cause of significant problems in the environment. For this reason, the "
      "chapter emphasizes that there is the need to introduce the latest technologies in energy "
      "generation, both in the thermal power plants and in the field of renewable energy sources "
      "(RES) for which there are significant potentials, but they have not been sufficiently used "
      "in the Republic of Serbia.")

    P(b, lang,
      "Mặc dù Chiến lược cũng đề cập đến các ưu tiên chiến lược quan trọng khác trong lĩnh vực năng "
      "lượng, nhưng do nhà máy điện có tác động đáng kể đến môi trường của không gian nơi chúng được "
      "xây dựng, SEA dành sự chú ý đặc biệt cho khía cạnh này, và chính khía cạnh này được phân tích "
      "kỹ hơn trong phần tiếp theo.",
      "Although other important strategic priorities in the field of energy are also dealt with in "
      "the Strategy, due to the fact that power plants have significant environmental impacts on "
      "the space in which they are built, the SEA gives special attention to this aspect, and "
      "exactly this aspect is elaborated further herein.")

    H(b, lang, "Đánh giá tác động của nhà máy điện bằng phương pháp MCE",
      "Evaluation of Power Plant Impacts Using the MCE Method", level=3)

    P(b, lang,
      "SEA cho Chiến lược đã chọn ra tổng số 29 hoạt động đã định/ưu tiên chiến lược được đưa vào quá "
      "trình đánh giá đa tiêu chí. Trong 29 ưu tiên chiến lược thì có 9 liên quan đến các dự án nhà "
      "máy điện (Bảng 7.4). Tuy nhiên, ngoại trừ các địa điểm được xác định trong văn bản có tên "
      "'Cadaster for Small Hydro Power Plants in Serbia' [55], Chiến lược không xác định vị trí vi "
      "mô cho hầu hết các nhà máy điện (đặc biệt là các nhà máy điện sử dụng RES), do đó việc đánh "
      "giá chỉ có thể dựa trên các dự báo và việc theo dõi xu hướng trong không gian trên cơ sở xác "
      "định vị trí vi mô và hiểu biết về các quy luật chung cũng như các tác động môi trường tiềm ẩn "
      "mà từng loại nhà máy điện gây ra.",
      "The SEA for the Strategy singles out the total of 29 planned activities/strategic priorities "
      "that was included in the multi-criteria evaluation process. Nine out of 29 strategic "
      "priorities relate to the projects of power plants (Table 7.4). However, save for the "
      "locations defined by the document entitled 'Cadaster for Small Hydro Power Plants in "
      "Serbia' [55], the Strategy does not determine micro-locations for the majority of power "
      "plants (this particularly refers to the power plants using RES), so the evaluation could be "
      "based on predictions and on keeping pace with trends in space on the basis of micro-location "
      "determination and knowledge of general regularities and potential environmental impacts "
      "that certain types of power plants imply.")

    return b
