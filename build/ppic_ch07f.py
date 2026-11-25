# -*- coding: utf-8 -*-
"""Chapter 7, final prose section: closing impacts summary, discussion and acknowledgements.

Source: Josimović and Milijić, "Spatial Aspects of Environmental Impact of Power
Plants", in *Handbook on Power Plant Instrumentation and Control* (Bibliotex,
2019), work/ppic_raw.txt absolute lines 4178-4336 (PDF pp. 158-162, printed
pp. 142-146).  The span opens mid-bullet, continuing the "Environmental
quality" item of the summary of significant strategic positive impacts that
starts in ppic_ch07e, then covers the "Socio-economic development" item,
DISCUSSION AND CONCLUSIONS and ACKNOWLEDGEMENTS.  Bracketed citations are kept
as printed.  No figures, tables or equations occur in this span.
"""
try:
    import ppicfig7 as F  # noqa: F401  (supplier not used by this section)
except ImportError:                       # supplier not written yet
    class _SupplierNamespace(object):
        pass
    F = _SupplierNamespace()

from ppic_ch07_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401


def section(lang):
    b = []

    # ---- continuation of the summary of significant positive impacts -------
    # First item continues the "Environmental quality" bullet opened on the
    # previous page (end of ppic_ch07e); second item is the next printed bullet.
    L(b, lang,
      ["Phát triển kinh tế - xã hội: Cải thiện ngành năng lượng như một động "
       "lực của tăng trưởng và phát triển kinh tế, hình thành giá năng lượng và "
       "giá của các sản phẩm sinh năng lượng theo định hướng thị trường; phát "
       "triển công nghiệp trong nước và ngành nghiên cứu khoa học thương mại để "
       "chuyển giao các công nghệ tiên tiến nhất trong lĩnh vực năng lượng; thực "
       "hiện nghiêm ngặt các biện pháp tiết kiệm năng lượng trong tiêu thụ "
       "năng lượng cuối cùng; tính cơ động của thị trường lao động; cũng như sự "
       "phát triển chung của ngành năng lượng, sẽ đại diện cho một đóng góp dài "
       "hạn vào phát triển kinh tế bền vững và sử dụng hợp lý các nguồn năng "
       "lượng không tái tạo, tức là tăng tỷ trọng năng lượng từ RES."],
      ["Socio-economic development: Improvement of the energy sector as a "
       "driver of economic growth and development, the market-oriented formation "
       "of energy prices and prices for energy-generating products; the "
       "development of domestic industry and commercial scientific research "
       "sector for the transfer of leading edge technologies in the field of "
       "energy; strict implementation of energy-efficiency measures in final "
       "energy consumption; labour market mobility; as well as overall energy "
       "sector development, will represent a long-term contribution to "
       "sustainable economic development and rational use of non-renewable "
       "energy sources, that is, increasing the share of energy from RES."])

    # ------------------------------------------- DISCUSSION AND CONCLUSIONS --
    H(b, lang, "THẢO LUẬN VÀ KẾT LUẬN", "DISCUSSION AND CONCLUSIONS")

    P(b, lang,
      "Chiến lược đại diện cho một khung chiến lược để thực hiện các chính sách "
      "và biện pháp trong lĩnh vực năng lượng, đồng thời bao gồm cả khía cạnh "
      "sử dụng các tiềm năng năng lượng thông qua việc quy hoạch và xây dựng các "
      "nhà máy điện mới hoặc hiện đại hóa các nhà máy hiện có. Những hệ quả có "
      "thể có đối với môi trường do triển khai các dự án như vậy, cũng như sự "
      "tham gia đáng kể của công chúng (các tổ chức phi chính phủ, người dân, "
      "các nhóm chuyên gia, các tổ chức liên quan, nhà đầu tư và các doanh "
      "nghiệp năng lượng công lập) trong các quá trình ra quyết định, không "
      "nghi ngờ gì cho thấy sự cần thiết phải xem xét khía cạnh này khi xây "
      "dựng các chính sách trong lĩnh vực năng lượng, ở cấp quốc gia, khu vực "
      "hay địa phương. Lý do cho sự quan tâm của công chúng đối với các nhà máy "
      "điện, và nói chung là ngành năng lượng, nằm ở bản chất hoạt động của "
      "chúng và những tác động không gian/lãnh thổ có thể đáng kể. Trong bối "
      "cảnh này, bên cạnh các nghiên cứu khác nhau về bảo vệ môi trường được "
      "thực hiện ở cấp độ các dự án đầu tư cụ thể cho từng nhà máy điện (ví dụ "
      "EIA hoặc LCA), việc tiến hành đánh giá tác động môi trường ở cấp chiến "
      "lược của công tác quy hoạch là đặc biệt quan trọng; đánh giá này nên "
      "định hướng một văn bản quy hoạch chiến lược tới các mục tiêu bền vững và "
      "ngăn ngừa các xung đột tiềm ẩn về không gian ngay từ giai đoạn sớm nhất "
      "của việc xây dựng chính sách năng lượng. SEA chính là công cụ đáp ứng "
      "chính xác các yêu cầu cụ thể này. Điều này đã được viết nhiều trong tài "
      "liệu khoa học và được tóm tắt ngắn gọn trong mục ‘Mở đầu’ của chương này.",
      "The Strategy represents a strategic framework for implementing the "
      "policies and measures in the field of energy, also including the aspect "
      "of using the energy potentials by planning and building new power plants "
      "or by modernizing the existing ones. The possible implications for the "
      "environment as a result of the realization of such projects, as well as "
      "the significant public participation (NGO, population, expert groups, "
      "relevant institutions, investors and public companies in the field of "
      "energy) in the decision-making processes, undoubtedly indicate the need "
      "to consider this aspect in creating the policies in the field of energy, "
      "either at the national, regional or at the local level. The reason for "
      "the interest of the public in power plants, and energy sector in general, "
      "lies in the nature of their operation and possible significant "
      "spatial/territorial impacts. In this context, besides different studies "
      "on environmental protection carried out at the level of specific "
      "investment projects for individual power plants (e.g. EIA or LCA), it is "
      "of particular importance to carry out an environmental impact assessment "
      "at the strategic level of planning which should direct a strategic-"
      "planning document to the goals of sustainability and prevent potential "
      "conflicts in space in the earliest stage of creating an energy policy. "
      "The SEA is exactly the instrument that meets these specific requirements. "
      "This has been much written about in scientific literature, which is "
      "briefly summarized in the ‘Introduction’ section of this chapter.")

    P(b, lang,
      "Chiến lược Năng lượng [20] là một văn bản đặc thù bởi vì nó thiết lập một "
      "quan niệm hoàn toàn mới và được thay đổi về phát triển ngành năng lượng "
      "so với quan niệm hiện hành, vốn đã được đánh giá — ít nhất là ở Cộng hòa "
      "Serbia — là không bền vững và không thể chấp nhận về mặt sinh thái. Bên "
      "cạnh đó, Chiến lược đặc biệt chú ý đến các nhà máy điện (cả hiện có và dự "
      "kiến), những đối tượng đặc biệt quan trọng để phân tích dưới góc độ bảo "
      "vệ môi trường. Điều này quy định tính đặc thù của đối tượng SEA, trong "
      "đó cần thiết phải tạo ra sự cộng sinh giữa tất cả các hiện tượng và quá "
      "trình hiện có trong không gian và các dự báo về tác động tiềm ẩn của các "
      "nhà máy điện đối với môi trường.",
      "The Energy Strategy [20] is a specific document due to the fact that it "
      "establishes a completely new and altered concept of energy sector "
      "development relative to the existing one that has been, at least in the "
      "Republic of Serbia, assessed as unsustainable and ecologically "
      "unacceptable. In addition, the Strategy gives a special attention to "
      "power plants (the existing and the planned ones) that are particularly "
      "significant for analysis from the aspect of environmental protection. "
      "This conditioned the specificity of the subject SEA within which it was "
      "necessary to make a symbiosis of all existing phenomena and the processes "
      "in space and predictions about potential impacts of power plants on the "
      "environment.")

    P(b, lang,
      "Điều này phục vụ cho việc xác định các mục tiêu SEA và các chỉ số tương "
      "ứng, cũng như các tiêu chí làm cơ sở đánh giá các ưu tiên chiến lược liên "
      "quan đến nhà máy điện. Bằng cách sử dụng đánh giá đa tiêu chí và các "
      "phương pháp bán định lượng theo ba nhóm tiêu chí, cũng như trình bày kết "
      "quả dưới dạng ma trận và đồ thị, kết quả được thể hiện rõ ràng và không "
      "mơ hồ cho từng ưu tiên chiến lược. Các khía cạnh khác nhau của tác động "
      "(mức độ quan trọng, phạm vi không gian và xác suất) đã được bao quát. "
      "Kết quả của phương pháp MCE được sử dụng làm cơ sở để xác định các biện "
      "pháp/hướng dẫn thích hợp nhằm bảo vệ môi trường và giám sát, được sử "
      "dụng trong quá trình thực hiện Chiến lược, cụ thể là trong việc xác định "
      "vị trí vi mô cho các nhà máy điện mới và trong việc chuẩn bị các dự án "
      "đầu tư. Các biện pháp/hướng dẫn này xác định SEA cho từng loại nhà máy "
      "điện, đặc biệt tính đến các dự án nhà máy điện mới và hướng dẫn triển "
      "khai chúng theo cách đảm bảo bảo vệ phòng ngừa đối với không gian và môi "
      "trường, từ đó cho phép tất cả các chủ thể trong quá trình xây dựng và "
      "thông qua Chiến lược rút ra kết luận một cách đơn giản về các hệ quả tích "
      "cực và tiêu cực của mọi tác động đã xác định, trong khi SEA trong quá "
      "trình này cũng đóng vai trò là công cụ điều tiết và kiểm soát cho mọi "
      "khoản đầu tư tương lai trong ngành năng lượng.",
      "This served for defining the SEA objectives and corresponding indicators, "
      "but also the criteria, based on which the strategic priorities related to "
      "power plants were assessed. By using the multi-criteria evaluation and "
      "semi-quantitative methods according to three groups of criteria, as well "
      "as by presenting the results using the matrices and graphs, the results "
      "were shown in a clear and unambiguous way for each of the strategic "
      "priorities. Different aspects of impacts (significance, spatial extent "
      "and probability) were encompassed. The results of the used MCE method "
      "were taken as a basis for defining the appropriate measures/guidelines "
      "for the environmental protection and monitoring which should be used in "
      "implementing the Strategy, namely in determining the micro-locations for "
      "new power plants and in preparing the investment projects. These "
      "measures/guidelines defined the SEA by each type of power plant, "
      "particularly taking into account new power plant projects and "
      "instructions for their realization in a way that provides the preventive "
      "protection of space and the environment, thus enabling all actors in the "
      "process of creating and adopting the Strategy to make conclusions on "
      "positive and negative implications of all identified impacts in a simple "
      "way, while the SEA in this process also serves as a regulatory and "
      "control tool for all future investments in the energy sector.")

    P(b, lang,
      "Khác với một số SEA hướng đến việc xác định các phương án ‘ủng hộ và "
      "phản đối’, trong SEA cho Chiến lược này, việc đề xuất các chủ thể ra "
      "quyết định về giải pháp nào phù hợp nhất cho việc thực thi Chiến lược là "
      "tương đối đơn giản, bởi những thay đổi tích cực do việc thực thi mang lại "
      "lớn hơn nhiều lần so với các hệ quả tiêu cực có thể có. Điều này được ảnh "
      "hưởng bởi cách tiếp cận phương pháp luận mang tính khái niệm rõ ràng; "
      "cách trình bày kết quả đạt được một cách minh bạch, cho phép sự tham gia "
      "rộng rãi của công chúng vào các giai đoạn then chốt của SEA (xác định "
      "các tác động tích cực và tiêu cực có thể có của các ý tưởng quy hoạch); "
      "việc sử dụng các phương pháp bán định lượng trong đánh giá tác động và "
      "xác định các hướng dẫn phù hợp về bảo vệ môi trường và giám sát.",
      "Unlike some SEA that are oriented towards identifying ‘for and against’ "
      "alternatives, in the SEA for the Strategy it was relatively simple to "
      "propose to actors to make decisions on which solution is the most "
      "suitable for the implementation of the Strategy because positive changes "
      "brought by its implementation are many times greater relative to the "
      "possible negative implications. This was affected by the methodological "
      "approach that is conceptually conceivable; clear way of presenting the "
      "obtained results which enables great public participation in critical "
      "stages of the SEA (identification of possible positive and negative "
      "impacts of the planning concepts); the use of semi-quantitative methods "
      "in assessing the impacts and defining the appropriate guidelines for the "
      "environmental protection and monitoring.")

    P(b, lang,
      "Tính đặc thù của cách tiếp cận được trình bày thể hiện ở việc xác định "
      "các mục tiêu và chỉ số của SEA dựa trên phân tích một sự cộng sinh phức "
      "tạp giữa chất lượng môi trường, các khung chiến lược được xác định trong "
      "các văn bản chiến lược và quy hoạch khác nhau, và chính Chiến lược này. "
      "Các mục tiêu và chỉ số thu được qua quy trình này là cơ sở tốt để đánh "
      "giá các hệ quả phức tạp của các hoạt động dự kiến đối với không gian và "
      "những tương tác lẫn nhau có thể có giữa các quy định ngành khác nhau "
      "liên quan đến các yếu tố phát triển bền vững. Việc trình bày rõ ràng kết "
      "quả đánh giá đa tiêu chí dưới dạng ma trận, và đặc biệt là dưới dạng đồ "
      "thị, có ý nghĩa đặc biệt quan trọng trong các giai đoạn SEA có sự tham "
      "gia của công chúng. Tuy nhiên, việc sử dụng phương pháp bán định lượng "
      "trong ra quyết định của chuyên gia mang lại một mức độ chủ quan nhất "
      "định, có thể tạm thời được coi là một hạn chế của cách tiếp cận này. Mặt "
      "khác, việc sử dụng các phương pháp toán học khác như ARAS (đánh giá tỷ lệ "
      "cộng dồn) [58] hay AHP (quy trình phân cấp phân tích) [59] ở cấp quy "
      "hoạch và quản lý chiến lược là không cần thiết, và thường không thể "
      "thực hiện do thiếu các dữ liệu đầu vào phù hợp. Chẳng hạn, trong trường "
      "hợp này không có việc xác định vị trí vi mô cho các nhà máy điện dự kiến "
      "sử dụng nguồn năng lượng tái tạo, vì vậy dự báo tác động chỉ có thể được "
      "thực hiện dựa trên hiểu biết về tiềm năng năng lượng — ví dụ, năng lượng "
      "có thể thu được từ các nguồn tái tạo ở cấp vị trí vi mô, tình trạng môi "
      "trường tại các vị trí vi mô đó và công suất tiềm năng (công suất lắp "
      "đặt) tại các vị trí vi mô có thể phù hợp này. Những kết quả thu được từ "
      "đánh giá tác động không gian/lãnh thổ của các ưu tiên chiến lược như trên "
      "chính là cơ sở tốt để thiết lập các hướng dẫn thích hợp và để áp dụng "
      "các phương pháp toán học nêu trên ở cấp đánh giá tác động thấp hơn, cụ "
      "thể là trong thực hiện EIA — vốn thực chất cũng là một nghĩa vụ khi thực "
      "hiện SEA. Trong bối cảnh này, sự thiếu hụt đó nên được hiểu một cách tạm "
      "thời, nhưng không được bỏ qua trong quá trình thực hiện SEA và trong "
      "việc ra các quyết định phù hợp.",
      "The specificity of the presented approach is reflected in the "
      "identification of the objectives and indicators of the SEA that is based "
      "on the analysis of a complex symbiosis of environmental quality, "
      "strategic frameworks defined in different strategic and planning "
      "documents and the Strategy. The objectives and indicators obtained "
      "through this procedure are a good basis for assessing the complex "
      "implications of the planned activities for the space and possible mutual "
      "interactions between different sectorial determinations regarding the "
      "elements of sustainable development. A clear presentation of obtained "
      "results of multi-criteria evaluation in the form of matrices, and "
      "particularly in the form of graphs, is particularly important in the SEA "
      "stages involving public participation. However, the use of semi-"
      "quantitative method of expert decision-making brings a certain dose of "
      "subjectivity, which can be tentatively regarded as a lack of such an "
      "approach. On the other hand, the use of different mathematical methods "
      "like ARAS (additive ratio assessment) [58] or AHP (analytical hierarchy "
      "process) [59] at the level of strategic planning and management is not "
      "necessary, and often impossible because of a lack of appropriate inputs. "
      "In this case, for example, there was no determination of micro-locations "
      "for the planned power plants that will use renewable energy sources, so "
      "the prediction of impacts could be only made based on the knowledge on "
      "energy potentials, for example, the energy to be obtained from renewable "
      "sources at the micro-location level, the state of the environment on "
      "these micro-locations and potential capacities (installed power) in "
      "these potentially suitable micro-locations. Such obtained results of the "
      "assessment of spatial/territorial impacts of strategic priorities "
      "represent exactly a good basis for establishing adequate guidelines and "
      "for the use of the above-mentioned mathematical methods at a lower level "
      "of impact assessment, namely in carrying out the EIA, which is actually "
      "also an obligation in carrying out the SEA. In this context, this lack "
      "should be understood tentatively, but should in no way be ignored in the "
      "process of carrying out the SEA and in making appropriate decisions.")

    P(b, lang,
      "Các hướng dẫn về bảo vệ môi trường được thiết lập dựa trên kết quả đánh "
      "giá đa tiêu chí các ưu tiên chiến lược liên quan đến việc quy hoạch, xây "
      "dựng hoặc hiện đại hóa các nhà máy điện. Các hướng dẫn được đưa ra cho "
      "những cơ sở/dự án quan trọng nhất được dự kiến trong Chiến lược, cụ thể "
      "là các cơ sở/dự án năng lượng có thể là nguồn gây ô nhiễm đáng kể do bản "
      "chất hoạt động của chúng.",
      "The guidelines for environmental protection were established based on "
      "the results of multi-criteria evaluation of strategic priorities that "
      "relate to the planning, building or modernization of power plants. The "
      "guidelines were given for the most significant facilities/projects "
      "envisaged in the Strategy, namely for the energy facilities/projects "
      "which can be significant polluters by nature of their operation.")

    P(b, lang,
      "Một đóng góp đặc biệt của quá trình SEA nằm ở việc xác định các tác động "
      "xuyên biên giới có thể có và thiết lập hợp tác xuyên biên giới với các "
      "nước láng giềng. Trong bối cảnh này, hợp tác đã được thiết lập với Cộng "
      "hòa Croatia, Romania và Cộng hòa Bulgaria, những nước đã bày tỏ sự quan "
      "tâm tham gia vào quá trình SEA và chính thức gửi quan điểm về các tác "
      "động xuyên biên giới có thể có đã được xác định. Quan điểm của họ đã được "
      "xem xét thỏa đáng trong quá trình chuẩn bị Báo cáo Cuối cùng của SEA.",
      "A special contribution of the SEA process was laid in the identification "
      "of possible transboundary impacts and in the establishment of the "
      "transborder cooperation with the neighbouring countries. In this "
      "context, the cooperation has been established with the Republic of "
      "Croatia, Romania and Republic of Bulgaria, which have showed their "
      "interest including themselves into the SEA process and in officially "
      "submitting their views regarding the identified possible transboundary "
      "impacts. Their views were adequately taken into account in the "
      "preparation of the SEA Final Report.")

    P(b, lang,
      "Việc thực hiện SEA cho nhu cầu của Chiến lược đã dẫn đến việc đưa ra các "
      "quyết định phù hợp trong quá trình thiết lập phát triển bền vững của "
      "ngành năng lượng, trong khi việc triển khai các tài liệu này trên thực "
      "tế nên góp phần vào tính ứng dụng của kết quả và vào khả năng giám sát "
      "đóng góp của SEA trong quá trình quy hoạch cả nhà máy điện lẫn tất cả "
      "các kế hoạch khác trong ngành năng lượng.",
      "Performing the SEA for the needs of the Strategy resulted in making "
      "appropriate decisions in the process of establishing sustainable energy "
      "sector development, while the implementation of documentation in practice "
      "should contribute to the applicability of results and to the possible "
      "monitoring of SEA contribution in the process of planning both power "
      "plants and all other plans in the energy sector.")

    # ----------------------------------------------------- ACKNOWLEDGEMENTS --
    H(b, lang, "LỜI CẢM ƠN", "ACKNOWLEDGEMENTS")

    P(b, lang,
      "Chương này là kết quả của nghiên cứu được tiến hành trong khuôn khổ các "
      "dự án khoa học ‘Các khía cạnh không gian, sinh thái, năng lượng và xã hội "
      "của phát triển các khu định cư và biến đổi khí hậu – những tác động qua "
      "lại giữa chúng’, TR 36035; và ‘Phát triển không gian bền vững của vùng "
      "Serbia ven Danube’ TR36016; đều được tài trợ bởi Bộ Giáo dục, Khoa học "
      "và Phát triển Công nghệ của Cộng hòa Serbia trong giai đoạn 2011–2017.",
      "This chapter has resulted from the research conducted within the "
      "scientific projects ‘Spatial, ecological, energy, as well as social "
      "aspects of settlement development and climate change – their mutual "
      "impacts’, TR 36035; and ‘Sustainable spatial development of Danubian "
      "Serbia’ TR36016; all financed by the Ministry of Education, Science and "
      "Technological Development of the Republic of Serbia during the period "
      "2011–2017.")

    return b
