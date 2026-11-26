# -*- coding: utf-8 -*-
"""Book 9, Chapter 8 (part A) — ABSTRACT and INTRODUCTION (EN/VI bilingual).

Source: Ling-Yun Peng, Ying-Jie Kang, Zong-Rui Lai and Yu-Ke Deng, in L. N.
Jalali (ed.), *Handbook on Power Plant Instrumentation and Control* (Bibliotex,
2019), PDF pp. 169-172, printed pp. 153-156 (absolute lines 4548-4674 of
work/ppic_raw.txt). The printed title, chapter number, authors and affiliation
are rendered by the page shell in `ppic_ch08.py` (TITLE_EN/TITLE_VI and
BYLINE); this module therefore starts with the ABSTRACT heading, as the other
chapter parts do. Printed bracketed citations [1]-[34] are retained inline;
no reference list is emitted here. There are no figures, tables or equations
in this module.
"""
try:
    import ppicfig8 as F  # noqa: F401  (shared supplier import style)
except ImportError:                       # supplier not written yet
    class _SupplierNamespace(object):
        pass
    F = _SupplierNamespace()

from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 8."""
    b = []

    # ---------------------------------------------------------------- ABSTRACT
    H(b, lang, "TÓM TẮT", "ABSTRACT", level=2)
    P(b, lang,
      "Bài báo đề xuất một phương pháp thiết kế tối ưu thông số cho nhiều bộ "
      "giảm chấn phễu than (CBD) nhằm giảm phản ứng động đất của các nhà máy "
      "điện than. Để kiểm chứng hiệu năng giảm chấn của các bộ CBD sau khi tối "
      "ưu, một mô hình thử nghiệm trên bàn rung tỷ lệ 1:30 của kết cấu nhà máy "
      "điện đã được chế tạo. Một chương trình thử nghiệm so sánh đã được tiến "
      "hành với ba tác động địa chấn trên mô hình có và không có CBD. Một mô "
      "hình phân tích phần tử hữu hạn tái tạo các điều kiện của thử nghiệm bàn "
      "rung đã được xây dựng để đối chiếu, và hiệu ứng giảm chấn của CBD dưới "
      "22 nhóm tác động địa chấn trường xa và 28 nhóm tác động địa chấn trường "
      "gần đã được phân tích. Cuối cùng, ảnh hưởng của sự thay đổi chu kỳ kết "
      "cấu đến phản ứng động đất của kết cấu có lắp CBD đã được khảo sát. Kết "
      "quả cho thấy việc sử dụng CBD trong kết cấu nhà máy điện than, dựa trên "
      "phương pháp thiết kế tối ưu cho các bộ giảm chấn khối điều chỉnh nhiều "
      "cấp (MTMD), làm giảm đáng kể phản ứng dịch chuyển của kết cấu, thể hiện "
      "một mức độ phân tán nhất định dưới các tác động khác nhau, đồng thời "
      "duy trì được sự ổn định giảm chấn nhất định ngay cả khi chu kỳ kết cấu "
      "thay đổi. Nhìn chung, việc sử dụng CBD là một triển vọng đầy hứa hẹn để "
      "cải thiện hiệu năng chống động đất của kết cấu nhà máy điện than.",
      "A parameter optimization design method is proposed for multiple coal "
      "bucket dampers (CBDs) to reduce the seismic response of coal-fired "
      "power plants. To test the damping effect of the optimized CBDs, a "
      "1:30 scale shaking table test model of a power plant structure was "
      "fabricated. A comparative testing program was conducted using three "
      "seismic excitations on a model with and without CBDs. A finite element "
      "analysis model, replicating the conditions of the shaking table test, "
      "was constructed for comparison, and the shock absorption effects of "
      "CBDs subjected to 22 groups of far-field seismic action and 28 groups "
      "of near-field seismic action were analyzed. Finally, the influence of "
      "changes in the structural period on the seismic response of the "
      "CBD-equipped structure was studied. The results indicate that the use "
      "of CBDs in a coal-fired power plant structure, based on an optimization "
      "design method for multiple-tuned mass dampers (MTMDs), results in a "
      "significant reduction in the structure displacement response, displays "
      "a certain discreteness under different excitations, and maintains a "
      "certain damping stability even as the structural period changes. "
      "Overall, the use of CBDs is a promising prospect for improving the "
      "seismic performance of coal-fired power plant structures.")

    # ------------------------------------------------------------ INTRODUCTION
    H(b, lang, "GIỚI THIỆU", "INTRODUCTION", level=2)
    P(b, lang,
      "Năm 2016, việc đốt than chiếm 71,60% tổng sản lượng điện tại Trung "
      "Quốc, và vị thế áp đảo của phát điện từ than khó có thể thay đổi trong "
      "tương lai gần [1]. Năm 2011, các nhà máy điện hạt nhân tại Nhật Bản đã "
      "bị đóng cửa rộng rãi sau cuộc khủng hoảng Fukushima, dẫn đến các đề "
      "xuất mở rộng quy mô lớn các nhà máy điện than tại quốc gia này. Bên "
      "cạnh đó, phát điện từ than cũng đóng vai trò rất quan trọng ở Ấn Độ, "
      "Hoa Kỳ và Thổ Nhĩ Kỳ, cũng như ở nhiều quốc gia khác [2]. Là cơ sở hạ "
      "tầng thiết yếu then chốt, an toàn chống động đất của các nhà máy điện "
      "than có tầm quan trọng đặc biệt. Vào những năm 1970, khái niệm kiểm "
      "soát rung kết cấu đã được đề xuất lần đầu tiên nhằm nâng cao tính an "
      "toàn và độ tin cậy của kết cấu dưới tác động kích thích [3]. Kết cấu "
      "của một nhà máy điện than điển hình thường là kết cấu khung bê tông "
      "cốt thép dạng khung ngang với nhiều liên kết yếu [4], vì vậy việc "
      "đánh giá các nhà máy điện theo hướng công nghệ kiểm soát rung kết cấu "
      "mang lại nhiều lợi ích.",
      "In 2016, burning of coal accounted for 71.60% of all power generation "
      "in China, and this dominant position of coal-fired power generation is "
      "unlikely to change in the near future [1]. In 2011, nuclear power "
      "plants in Japan were widely shut down after the Fukushima crisis, "
      "leading to proposals for the massive expansion of coal-fired power "
      "plants there. In addition, coal-fired power generation also plays a "
      "very important role in India, the United States, and Turkey, as well "
      "as in many other countries [2]. As critical lifeline infrastructure , "
      "the seismic safety of coal-fired power plants is very important. In "
      "the 1970s, the concept of structural vibration control was proposed "
      "for the first time to improve the safety and reliability of structures "
      "under excitation [3]. The structure of a typical coal-fired power "
      "plant often consists of a reinforced concrete frame-bent structure "
      "with many weak links [4], so it is advantageous to evaluate coal "
      "plants with an eye toward structure vibration control technology.")

    P(b, lang,
      "Ngay từ năm 1956, Den Hartog đã đưa ra một phương trình cơ bản mô tả "
      "ứng xử của bộ giảm chấn khối điều chỉnh (TMD) dưới kích thích điều hòa "
      "[5]. Sau đó, các thông số thiết kế tối ưu khi sử dụng TMD trong các "
      "điều kiện kích thích khác nhau đã được bổ sung và phát triển [6, 7]. "
      "Trong lĩnh vực kỹ thuật dân dụng, việc sử dụng TMD như một công nghệ "
      "kiểm soát rung đã được nghiên cứu và phát triển rộng rãi [8, 9]. Phạm "
      "vi ứng dụng của công nghệ TMD bao gồm các công trình siêu cao tầng "
      "[10], các công trình tháp cao [11] và các công trình nhịp lớn [12]. "
      "Tuy nhiên, một TMD đơn lẻ có một số nhược điểm, trong đó có tính nhạy "
      "cảm với tần số và tính bền vững kém. Vì vậy, bộ giảm chấn khối điều "
      "chỉnh kép và bộ giảm chấn khối điều chỉnh nhiều cấp (MTMD) đã được đề "
      "xuất nhằm nâng cao hiệu quả của TMD [13].",
      "As early as 1956, Den Hartog provided a basic equation for the behavior "
      "of a tuned mass damper (TMD) under harmonic excitation [5]. "
      "Subsequently, the optimal design parameters for the use of a TMD under "
      "different excitation conditions have been supplemented and developed "
      "[6, 7]. In the field of civil engineering, the use of TMDs has been "
      "widely studied and developed as a vibration control technology [8, 9]. "
      "The range of application of TMD technology includes super high-rise "
      "structures [10], towering structures [11], and large span structures "
      "[12]. However, a single TMD has some disadvantages, including frequency "
      "sensitivity and poor robustness. Therefore, double-tuned mass dampers "
      "and multiple-tuned mass dampers (MTMDs) were proposed to improve the "
      "effectiveness of TMD behavior [13].")

    P(b, lang,
      "Sau đó, các kết quả nghiên cứu cho thấy việc sử dụng MTMD mang lại khả "
      "năng giảm chấn và tính ổn định địa chấn tốt hơn so với một TMD đơn lẻ "
      "[14–18]. Việc ứng dụng MTMD được chia thành nhiều biến thể khác nhau "
      "tùy theo sự kết hợp của hệ số độ cứng, hệ số cản, tỷ số khối lượng và "
      "tỷ số cản của từng TMD thành phần. Dù có sự đa dạng trong cách ứng "
      "dụng, kết quả cho thấy mọi loại MTMD đều có hiệu quả giảm rung gần như "
      "tương đương và thể hiện tính bền vững tương tự khi ở các thông số tối "
      "ưu [19–22]. Trong những năm gần đây, nhiều cách tiếp cận khác nhau để "
      "thiết kế tối ưu hệ MTMD đã được đề xuất [20–25]. Tiêu chí tối ưu thường "
      "được chọn là cực tiểu hóa các hệ số khuếch đại động của dịch chuyển và "
      "gia tốc của kết cấu có lắp MTMD [20]. Bằng cách xét đến chuyển động của "
      "từng đơn vị MTMD so với vị trí lắp đặt của nó (hành trình), một quy "
      "trình tối ưu hóa hai giai đoạn để thiết kế các thông số MTMD đã được "
      "phát triển. Phân tích lý thuyết và kết quả thử nghiệm cho thấy hành "
      "trình của TMD có thể được giảm đáng kể với sự suy giảm rất nhỏ về hiệu "
      "quả kiểm soát phản ứng của kết cấu [23, 24]. Gần đây hơn, một phương "
      "pháp thiết kế mới đã được đề xuất, có khả năng nâng cao đáng kể tính "
      "bền vững của hệ thống với chỉ một chút ảnh hưởng bất lợi đến hiệu quả "
      "kiểm soát kết cấu [25].",
      "Subsequently, results have shown that the use of MTMDs provides "
      "improved shock absorption and seismic stability over a single TMD "
      "[14–18]. The application of MTMDs is divided into different variants "
      "according to the different combinations of stiffness coefficients, "
      "damping coefficients, and mass and damping ratios of each component "
      "TMD. Despite this diversity in application, results indicate that all "
      "types of MTMD have nearly the same effectiveness in reducing vibration "
      "and exhibit similar robustness under optimal parameters [19–22]. In "
      "recent years, different approaches for the optimal design of MTMD "
      "systems have been proposed [20–25]. The minimization of the dynamic "
      "magnification factors for displacement and acceleration of the "
      "MTMD-equipped structure has typically been selected as the criterion "
      "for optimization [20]. Considering the displacement of each MTMD unit "
      "relative to its installed position (the stroke), a two-stage "
      "optimization procedure for the design of MTMD parameters has been "
      "developed. Theoretical analysis and experimental results have indicated "
      "that the stroke of a TMD can be significantly reduced with little "
      "sacrifice in the control and effectiveness of the structural response "
      "[23, 24]. More recently, a new design method has been proposed that "
      "can significantly enhance system robustness with only slight detriment "
      "to structural control effectiveness [25].")

    P(b, lang,
      "Dựa trên khái niệm kiểm soát rung kết cấu, công nghệ TMD đã được đề "
      "xuất cho thiết kế chống động đất của các tòa nhà nhà máy điện than "
      "quy mô lớn. Một công nghệ đặc biệt là bộ giảm chấn phễu than (CBD) "
      "được áp dụng cho kết cấu, dùng chính khối lượng của các phễu than làm "
      "khối lượng của TMD. Cách tiếp cận này khác với các ứng dụng TMD truyền "
      "thống vốn dựa vào việc bổ sung khối lượng cho kết cấu để hoạt động. Ở "
      "giai đoạn hiện nay, các phương pháp chính để triển khai công nghệ CBD "
      "được đề xuất gồm treo và tựa [2, 26, 27]. Trong nhà máy điện than, các "
      "phễu than được bố trí ở độ cao tương đối lớn của kết cấu, gần với vị "
      "trí lắp đặt tối ưu của TMD [28–30]. Tỷ số giữa khối lượng phễu than và "
      "tổng khối lượng kết cấu có thể đạt khoảng 10% — một tỷ số khối lượng "
      "đáng kể đối với một thiết bị giảm chấn khối điều chỉnh — vì vậy khối "
      "lượng than trong các phễu có thể được dùng để tạo ra mức giảm rung "
      "đáng kể. Các CBD dạng treo và bộ giảm chấn khối điều chỉnh dạng con "
      "lắc (PTMD) có các thông số vận hành tương tự trong giảm rung [31]. Dù "
      "hệ thống tựa của CBD được liên kết với kết cấu chính thông qua các "
      "gối có độ cứng ngang thấp và hệ số cản cao, về cơ bản cả CBD dạng treo "
      "và dạng con lắc đều được xếp vào các dạng kiểm soát giảm chấn điều "
      "chỉnh [32]. Các công trình phân tích chi tiết sử dụng CBD làm TMD đã "
      "được thực hiện trong tài liệu [2], và kết quả cho thấy CBD có thể giảm "
      "đáng kể phản ứng động đất của kết cấu lớn hơn mà nó được lắp vào. Tuy "
      "nhiên, bản thân ứng xử của kết cấu lớn này vẫn chưa được phân tích có "
      "tính đến đóng góp của nhiều bộ giảm chấn phễu than.",
      "Based on the concept of structural vibration control, TMD technology "
      "has been proposed for the seismic design of large coal-fired power "
      "plant buildings. A unique coal bucket damper (CBD) technology is "
      "applied to the structure using the mass of coal buckets as the mass of "
      "the TMD. This approach differs from traditional TMD applications, which "
      "rely upon the addition of mass to a structure to function. At the "
      "present stage, the main methods for implementing the proposed CBD "
      "technology include suspension and support [2, 26, 27]. In a coal-fired "
      "power plant, the coal buckets are located at a relatively high "
      "elevation in the structure, an elevation close to the optimal placement "
      "of a TMD [28–30]. The ratio of coal bucket mass to the total structural "
      "mass can reach about 10%—a considerable mass ratio for a tuned mass "
      "damper device—and thus the mass of coal in the buckets can be used to "
      "provide a significant degree of vibration reduction. Suspension-type "
      "CBDs and pendulum-tuned mass dampers (PTMDs) have similar operational "
      "parameters in vibration damping [31]. Though the support system of a "
      "CBD is connected to the main structure by bearings with low horizontal "
      "stiffness and high damping coefficients, fundamentally speaking, both "
      "suspension-type and pendulum-type CBDs are classified as forms of "
      "tuned damping control [32]. Detailed analytical work using a CBD as a "
      "TMD has already been performed in the literature [2], and the results "
      "indicate that a CBD can significantly reduce the earthquake response "
      "of the larger structure in which it is incorporated. However, the "
      "behavior of this larger structure itself has not yet been analyzed "
      "with consideration of the contribution of multiple coal bucket "
      "dampers.")

    P(b, lang,
      "Dựa trên lý thuyết giảm rung dùng để mô hình hóa hệ MTMD, bài báo đề "
      "xuất một phương pháp thiết kế tối ưu cho tòa nhà nhà máy điện than sử "
      "dụng CBD như một hệ MTMD. Để thực hiện điều này, các thử nghiệm trên "
      "bàn rung đã được tiến hành đối với các khung bê tông cốt thép được lắp "
      "CBD tối ưu. Các phần tử con lắc đơn và phần tử đàn hồi ngang được sử "
      "dụng để cung cấp lực phục hồi đàn hồi cho CBD. Xét đến ảnh hưởng của "
      "tính ngẫu nhiên của sóng động đất [33] và cường độ sóng động đất [34] "
      "đến ứng xử của CBD, ba bộ điều kiện thử nghiệm sóng động đất với cường "
      "độ khác nhau đã được thiết lập và áp dụng cho các khung thí nghiệm. "
      "Bằng cách so sánh phản ứng động của kết cấu có và không có CBD, hiệu "
      "quả giảm rung của CBD đã được xác định. Đồng thời, một mô hình phần tử "
      "hữu hạn tương ứng với mô hình thử nghiệm đã được xây dựng. Hiệu năng "
      "chống động đất của kết cấu có lắp CBD đã được phân tích dưới 22 nhóm "
      "tác động địa chấn trường xa và 28 nhóm tác động địa chấn trường gần. "
      "Cuối cùng, tính ổn định địa chấn của kết cấu có lắp CBD sau sự thay đổi "
      "chu kỳ cơ bản được phân tích, và ứng xử của hệ thống đề xuất được so "
      "sánh với kết quả thử nghiệm bàn rung để rút ra kết luận về hiệu quả "
      "của hệ thống.",
      "Based on the reductive vibration theory used to model MTMD systems, an "
      "optimized design method for a coal-fired power plant building using "
      "CBDs as an MTMD system is proposed in this paper. To this end, shaking "
      "table tests of reinforced concrete frames equipped with optimized CBDs "
      "are conducted. Simple pendulum and horizontal elastic elements are used "
      "to provide resilient restoration force for the CBDs. Considering the "
      "influence of seismic wave randomness [33] and seismic wave intensity "
      "[34] on CBD behavior, three sets of seismic wave test conditions at "
      "different intensities are established and applied to the frames. By "
      "comparing the dynamic responses of structures with and without CBDs, "
      "the vibration reduction effectiveness of the CBDs is obtained. At the "
      "same time, a finite element model corresponding to the test model is "
      "constructed. The seismic performance of the CBD-equipped structure is "
      "analyzed under 22 sets of far-field seismic action and 28 sets of "
      "near-field seismic action. Finally, the seismic stability of the "
      "CBD-equipped structure after fundamental periodic change is analyzed, "
      "and the behavior of the proposed system is compared to that of the "
      "shaking table tests to provide conclusions on its effectiveness.")

    return b
