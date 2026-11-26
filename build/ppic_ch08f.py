# -*- coding: utf-8 -*-
"""Book 9, Chapter 8 (part F) - experimental results, displacement and
acceleration reduction effects, FEA model validation and seismic-wave
discreteness (EN/VI).

Source: work/ppic_raw.txt absolute lines 4989-5198 (PDF pp. 189-204, printed
pp. 173-188; printed = PDF - 16).  The span opens with the heading
"EXPERIMENTAL RESULTS AND NUMERICAL SIMULATION ANALYSIS" and runs through the
Figure 18 caption.  Figures 11-18 are embedded in source order.  All printed
numbers (3.16 Hz, 2.2%, 11.4%, 17.7%, 14.0%, 23.0%, -3.4%, 3.3%, 1.2%, 8.8%,
22/28/53 waves) were checked against the page renders p190.png-p204.png.

Figures are supplied by ``ppicfig8_b`` (11-14) and ``ppicfig8_c`` (15-18).
The neutral bilingual stubs below only fill gaps in a partial build; they
never overwrite a callable the real supplier has registered.
"""
import ppicfig8 as F
from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401

# ------------------------------------------------------- figure stubs
# Short subject-only captions; _mk() prefixes "Figure 8.N" / "Hinh 8.N" and
# appends the bilingual bottom strip.
_STUBS = {
    11: ("Hàm truyền của mô hình dưới kích thích nhiễu trắng",
         "Transfer function of model under white-noise input",
         "Hàm truyền gia tốc của tầng trên cùng ở điều kiện nhiễu trắng W1 và W4, với ba mốc tần số riêng NF.",
         "Acceleration transfer function of the top story under white-noise conditions W1 and W4, with three natural-frequency marks NF."),
    12: ("Tỷ lệ giảm dịch chuyển dưới các điều kiện địa chấn",
         "Displacement reduction rates under applied seismic conditions",
         "Bốn biểu đồ tỷ lệ giảm dịch chuyển RMS và đỉnh theo tầng, cho động đất cường độ thường gặp và trung bình.",
         "Four plots of RMS and peak displacement reduction rates by story under frequent- and moderate-intensity earthquakes."),
    13: ("So sánh lịch sử thời gian dịch chuyển giữa các tầng dưới động đất thường gặp",
         "Time-history comparison of interstory displacements under frequent earthquakes",
         "Ba nhóm đường cong dịch chuyển các tầng 2 và 4, có và không có CBD, cho El Centro, Impvall và RGB.",
         "Three sets of story-2 and story-4 displacement traces, with and without CBDs, for El Centro, Impvall and RGB."),
    14: ("So sánh lịch sử thời gian dịch chuyển giữa các tầng dưới động đất trung bình",
         "Time-history comparison of interstory displacements under moderate earthquakes",
         "Ba nhóm đường cong dịch chuyển các tầng 2 và 4, có và không có CBD, cho El Centro, Impvall và RGB.",
         "Three sets of story-2 and story-4 displacement traces, with and without CBDs, for El Centro, Impvall and RGB."),
    15: ("Tỷ lệ giảm gia tốc dưới động đất thường gặp và trung bình",
         "Acceleration reduction rates under frequent and moderate earthquakes",
         "Bốn biểu đồ tỷ lệ giảm gia tốc đỉnh và RMS theo tầng, cho động đất cường độ thường gặp và trung bình.",
         "Four plots of peak and RMS acceleration reduction rates by story under frequent- and moderate-intensity earthquakes."),
    16: ("Mô hình phần tử hữu hạn của kết cấu nghiên cứu",
         "Finite element model of the subject structure",
         "Mô hình SAP2000 của kết cấu thí nghiệm với CBD1, CBD2 và CBD3.",
         "SAP2000 model of the test structure with CBD1, CBD2 and CBD3."),
    17: ("So sánh phản ứng giữa mô hình thí nghiệm và mô hình FEA",
         "Comparison of responses between test and FEA models",
         "Ba nhóm đường cong đối chiếu phản ứng thí nghiệm và FEA cho El Centro, Impvall và dịch chuyển của CBD3.",
         "Three sets of test-versus-FEA response traces for El Centro, Impvall and the displacement of CBD3."),
    18: ("Phổ phản ứng của sóng địa chấn trường xa và trường gần",
         "Response spectra of far-field and near-field seismic waves",
         "Phổ gia tốc tuyệt đối cho 22 sóng trường xa và 28 sóng trường gần, kèm đường trung bình.",
         "Absolute acceleration spectra for 22 far-field and 28 near-field waves, with a mean curve."),
}

for _n, (_cvi, _cen, _avi, _aen) in _STUBS.items():
    _name = "fig_f%02d" % _n
    if not hasattr(F, _name):
        from ppicfig8_common import _mk
        _tuple = _mk(_n, [], "Figure 8.%d" % _n, _cvi, _cen, _avi, _aen)
        setattr(F, _name, (lambda _t=_tuple: _t))


def section(lang):
    b = []

    # ----------------------------- EXPERIMENTAL RESULTS AND NUMERICAL -----
    H(b, lang,
      "KẾT QUẢ THÍ NGHIỆM VÀ PHÂN TÍCH MÔ PHỎNG SỐ",
      "EXPERIMENTAL RESULTS AND NUMERICAL SIMULATION ANALYSIS", level=2)
    H(b, lang,
      "Kết quả thí nghiệm trên bàn rung",
      "Shaking Table Test Results", level=3)
    P(b, lang,
      "Kết quả thí nghiệm trên bàn rung chủ yếu gồm kết quả quét tần số, kết quả "
      "phản ứng dịch chuyển giữa các tầng và kết quả phản ứng gia tốc tuyệt đối "
      "của từng tầng. Hiệu quả giảm chấn của các CBD được tính toán bằng giá trị "
      "đỉnh và giá trị căn bậc hai của trung bình bình phương (RMS) của dịch "
      "chuyển và gia tốc, tương ứng.",
      "The results of the shaking table test mainly include the frequency "
      "scanning results, interstory displacement response results, and absolute "
      "acceleration response results for each story. The reduction effects of "
      "the CBDs were calculated using the peak value and the root mean square "
      "(RMS) of the displacement and acceleration, respectively.")

    # --------------------------------------------- Model Test Results ----
    H(b, lang, "Kết quả thí nghiệm trên mô hình", "Model Test Results", level=4)
    P(b, lang,
      "Hình 11 thể hiện hàm truyền gia tốc của tầng trên cùng của kết cấu thí "
      "nghiệm ở điều kiện kích thích nhiễu trắng thứ nhất và thứ tư. Tần số bậc "
      "nhất của kết cấu thí nghiệm là 3.16 Hz, và sai số giữa kết quả thí nghiệm "
      "với kết quả mô phỏng số là 2.2%. Sai số nhỏ này cho thấy các thông số "
      "thiết kế của CBD thí nghiệm vẫn đáp ứng yêu cầu thiết kế tối ưu. Hơn "
      "nữa, kết quả thí nghiệm phương thức cho thấy trước điều kiện động đất "
      "hiếm, tần số riêng bậc nhất và bậc hai của kết cấu thay đổi rất ít, chứng "
      "tỏ rằng trong điều kiện động đất cường độ thường gặp và trung bình, tần "
      "số thiết kế của các CBD không sai lệch đáng kể.",
      "Figure 11 shows the acceleration transfer function of the top story of "
      "the test structure at the first and the fourth white-noise excitation "
      "conditions. The first-order frequency of the test structure was 3.16 Hz, "
      "and the error between the test result and the numerical simulation "
      "result was 2.2%. This low error indicates that the design parameters of "
      "the test CBDs still meet the optimal design requirements. Furthermore, "
      "the modal test results show that prior to the rare earthquake condition, "
      "the first and second natural frequencies of the structure changed very "
      "little, indicating that under frequent- and moderate-intensity "
      "earthquake conditions, the design frequency of the CBDs does not "
      "significantly deviate.")
    FIG(b, 11, F.fig_f11(), lang)

    # --------------------------------------- Displacement Reduction -----
    H(b, lang,
      "Hiệu quả giảm dịch chuyển",
      "Displacement Reduction Effect", level=4)
    P(b, lang,
      "Giá trị đỉnh và giá trị RMS trung bình của dịch chuyển giữa các tầng cho "
      "ba bộ điều kiện động đất cường độ thường gặp được đánh giá lần lượt là "
      "11.4% và 17.7%. Trong điều kiện động đất cường độ trung bình, giá trị "
      "đỉnh và giá trị RMS của dịch chuyển giữa các tầng tăng lên lần lượt "
      "14.0% và 23.0%.",
      "The average peak and RMS interstory drift values for the three sets of "
      "frequent earthquake conditions evaluated were 11.4% and 17.7%, "
      "respectively. Under moderate earthquake conditions, the peak and RMS "
      "of interstory drift increased by 14.0% and 23.0%, respectively.")
    P(b, lang,
      "Tỷ lệ giảm dịch chuyển đỉnh và tỷ lệ giảm dịch chuyển RMS trung bình của "
      "từng tầng dưới điều kiện động đất cường độ thường gặp và trung bình được "
      "thể hiện trên Hình 12, trong đó có thể rút ra các nhận xét sau:",
      "The peak and average RMS displacement reduction rates of each story "
      "under frequent and moderate earthquake conditions are seen in Figure 12, "
      "in which the following can be observed:")
    L(b, lang,
      ["Tỷ lệ giảm RMS của dịch chuyển giữa các tầng rõ ràng tốt hơn tỷ lệ giảm "
       "đỉnh, và tỷ lệ giảm RMS ổn định hơn. Tuy nhiên, dịch chuyển giữa tầng "
       "đỉnh của tầng trên cùng không cho thấy hiệu quả giảm rõ rệt dưới tác "
       "động của địa chấn Impvall. Tỷ lệ giảm đỉnh và tỷ lệ giảm RMS của dịch "
       "chuyển giữa các tầng là tối ưu dưới tác động của địa chấn El Centro.",
       "Tỷ lệ giảm RMS không nhất quán với tỷ lệ giảm đỉnh. Tỷ lệ giảm đỉnh dưới "
       "tác động của địa chấn RGB tốt hơn dưới tác động của địa chấn Impvall, "
       "nhưng tỷ lệ giảm RMS của nó lại kém hơn so với dưới tác động của địa "
       "chấn Impvall.",
       "Tỷ lệ giảm đỉnh có xu hướng giảm nhẹ ở các tầng nằm phía trên các CBD, "
       "trong khi tỷ lệ giảm RMS có xu hướng tăng nhẹ trong cùng khu vực. Hiện "
       "tượng này rất rõ rệt dưới tác động của địa chấn cường độ trung bình."],
      ["The RMS reduction rates of interstory drift are obviously better than "
       "the peak reduction rate, and the RMS reduction rates are more stable. "
       "However, the peak inter-story drift of the top story shows no obvious "
       "reduction effect under the application of the Impvall seismic "
       "excitation. The peak and RMS reduction rates of interstory drift are "
       "optimal under the El Centro seismic excitation.",
       "The RMS reduction rates are not consistent with the peak reduction "
       "rates. The peak reduction rate under the RGB seismic excitation is "
       "better than under the Impvall seismic excitation, but its RMS reduction "
       "rates are worse than those under the Impvall seismic excitation.",
       "The peak reduction rates have a certain downward trend in the story "
       "above the CBDs, while the RMS reduction rates have a certain upward "
       "trend in the same region. This phenomenon is obvious under the action "
       "of moderate-intensity seismic excitation."], ordered=True)
    FIG(b, 12, F.fig_f12(), lang)

    P(b, lang,
      "Hình 13 và Hình 14 thể hiện dịch chuyển giữa tầng của tầng thứ hai và thứ "
      "tư của kết cấu nghiên cứu trong cả hai trường hợp thí nghiệm (có và "
      "không có CBD) khi chịu động đất cường độ thường gặp và trung bình, tương "
      "ứng. Có thể thấy rằng khả năng hấp thụ dịch chuyển của kết cấu là tương "
      "tự nhau trong mọi điều kiện đã thử. Ở giai đoạn đầu của mỗi trận động "
      "đất, dịch chuyển của kết cấu có và không có CBD là đồng bộ, nhưng cuối "
      "cùng biên độ dao động của kết cấu có CBD cho thấy sự giảm chấn rõ rệt, "
      "gợi ý rằng các CBD có đặc tính trễ rõ ràng, rất giống các TMD thụ động "
      "truyền thống. Khả năng hấp thụ dịch chuyển của kết cấu dưới tác động "
      "địa chấn Impvall được thể hiện trên Hình 13(b) và 14(b). Có thể thấy "
      "rằng dịch chuyển kết cấu đạt giá trị đỉnh sau một thời gian ngắn và các "
      "CBD chưa kịp phát huy vai trò giảm dịch chuyển, dẫn đến tỷ lệ giảm đỉnh "
      "rất nhỏ. Tuy nhiên, ở giai đoạn sau của động đất, dao động của kết cấu "
      "có CBD suy giảm nhanh cho đến khi không còn dao động. Điều này chứng tỏ "
      "tỷ lệ giảm RMS của dịch chuyển giữa các tầng vẫn rất lý tưởng. Trong ba "
      "bộ điều kiện sóng địa chấn, tỷ lệ giảm RMS của tác động RGB là nhỏ nhất, "
      "như thể hiện trên Hình 13(c) và 14(c).",
      "Figures 13 and 14 show the interstory drift of the second and fourth "
      "stories of the subject structure for both test cases (with and without "
      "CBDs) when subjected to frequent- and moderate-intensity earthquakes, "
      "respectively. It can be seen that the displacement shock absorption of "
      "the structure is similar under all tested conditions. At the beginning "
      "of each earthquake, the displacement of the structures with and without "
      "CBDs is synchronous, but eventually the vibration amplitude of the "
      "CBD-equipped structure indicates obvious dampening, suggesting that the "
      "CBDs provide obvious hysteresis characteristics, much like traditional "
      "passive TMDs. The displacement shock absorption of the structure under "
      "the Impvall seismic excitation is shown in Figures 13(b) and 14(b). It "
      "can be seen that the structural displacement reaches a peak after a "
      "short time, and that the CBDs have not yet played a role in reducing it, "
      "leading to a very small peak reduction rate. However, in the later "
      "stages of the applied earthquakes, it is obvious that the vibration of "
      "the structure with CBDs rapidly decays until it no longer vibrates. "
      "This illustrates that the RMS reduction rates of interstory drift are "
      "still ideal. Among the three sets of seismic wave conditions, the RMS "
      "reduction rate of the RGB excitation is the smallest, as shown in "
      "Figures 13(c) and 14(c).")
    FIG(b, 13, F.fig_f13(), lang)
    FIG(b, 14, F.fig_f14(), lang)

    P(b, lang,
      "Có những điểm tương đồng và khác biệt rõ rệt giữa khả năng hấp thụ "
      "dịch chuyển của kết cấu có CBD dưới điều kiện động đất thường gặp và "
      "trung bình. Điểm tương đồng chính là tính trễ của tác động, tức là các "
      "CBD chỉ bắt đầu hoạt động sau khi kết cấu đã dịch chuyển một mức nhất "
      "định, sau đó tốc độ suy giảm dịch chuyển mới tăng lên, chứng tỏ tỷ số "
      "cản tương đương của kết cấu đã tăng và đạt được hiệu quả kiểm soát rung "
      "mong muốn.",
      "There are clearly some similarities and differences between the "
      "displacement shock absorption of the CBD-equipped structure under "
      "frequent and moderate earthquake conditions. The main similarity is "
      "the action hysteresis, that is, the CBDs begin to function after a "
      "certain displacement occurs in the structure, following which the "
      "displacement decay rate begins to grow, demonstrating that the "
      "equivalent damping ratio of the structure has increased, achieving the "
      "desired vibration control effect.")

    P(b, lang,
      "Điểm khác biệt chính giữa phản ứng của kết cấu dưới động đất thường gặp "
      "và trung bình là tỷ lệ giảm dịch chuyển dưới động đất cường độ thường "
      "gặp tốt hơn dưới động đất cường độ trung bình. Lý do của hành vi này khá "
      "phức tạp: do giá trị đỉnh của chuyển động nền đầu vào tăng lên, biên độ "
      "dao động của kết cấu lớn hơn và thời gian các CBD tác động dài hơn, "
      "đồng thời sự tăng biên độ dao động của các CBD làm thay đổi một số đặc "
      "tính hiệu năng của chúng. Nhìn chung, biên độ dao động của CBD càng lớn "
      "thì khả năng tiêu tán năng lượng càng tốt, hay nói cách khác là tỷ số "
      "cản càng lớn. Thực tế, một số nghiên cứu hiện có cho thấy tăng tỷ số cản "
      "của TMD có thể làm tăng tỷ lệ giảm dịch chuyển của kết cấu [27].",
      "The main difference between structure responses under frequent and "
      "moderate earthquake conditions is that the reduction rates of "
      "displacement under a frequent-intensity earthquake are better than "
      "those under a moderate-intensity earthquake. The reasons for this "
      "behavior are complex: due to the increase in the peak value of the "
      "input ground motion, the vibration amplitude of the structure becomes "
      "larger and the duration over which the CBDs act becomes longer, and the "
      "increase in the vibration amplitude of the CBDs causes some of the "
      "performance characteristics of the CBDs to change. Generally, the "
      "larger the vibration amplitude of the CBDs, the better their energy "
      "dissipation capability, or, in other words, the larger their damping "
      "ratio. Indeed, some existing research indicates that increasing the "
      "damping ratio of a TMD can increase the displacement reduction rate of "
      "the structure [27].")

    P(b, lang,
      "Nhìn chung, phản ứng dịch chuyển của kết cấu có CBD vượt trội rõ rệt so "
      "với kết cấu truyền thống, cho thấy công nghệ CBD có thể làm tăng tỷ số "
      "cản của kết cấu và phát huy hiệu quả kiểm soát vượt trội đối với phản "
      "ứng dịch chuyển của kết cấu.",
      "Overall, the displacement response of the CBD-equipped structure is "
      "obviously superior to that of the traditional structure, indicating "
      "that CBD technology can increase the damping ratio of the structure and "
      "exert a superior control effect on the displacement response of the "
      "structure.")

    # --------------------------------------- Acceleration Reduction -----
    H(b, lang,
      "Hiệu quả giảm gia tốc",
      "Acceleration Reduction Effect", level=4)
    P(b, lang,
      "Phản ứng gia tốc của kết cấu có CBD được thể hiện trên Hình 15, từ đó có "
      "thể suy ra rằng các CBD không có hiệu quả kiểm soát rõ rệt đối với phản "
      "ứng gia tốc đỉnh và RMS của tầng thứ nhất và thứ hai, thậm chí xuất hiện "
      "hiện tượng làm tăng phản ứng. Tuy nhiên, phản ứng gia tốc của tầng thứ "
      "ba và thứ tư cho thấy tỷ lệ giảm đầy hứa hẹn. Trong điều kiện động đất "
      "cường độ thường gặp, giá trị trung bình của tỷ lệ giảm gia tốc đỉnh và "
      "RMS cho tất cả các tầng lần lượt là −3.4% và 3.3%, và trong điều kiện "
      "động đất cường độ trung bình, các giá trị trung bình tăng lên lần lượt "
      "là 1.2% và 8.8%, cho thấy khi đỉnh của chuyển động nền đầu vào tăng lên "
      "thì tỷ lệ giảm gia tốc tăng theo, phù hợp với tỷ lệ giảm của dịch "
      "chuyển giữa các tầng. Nhìn chung, hiệu quả kiểm soát của CBD đối với "
      "phản ứng gia tốc của tầng mà chúng được lắp đặt và tầng phía trên được "
      "cải thiện, nhưng các tầng bên dưới CBD vẫn có hành vi chưa thực sự lý "
      "tưởng.",
      "The acceleration responses of the CBD-equipped structure are shown in "
      "Figure 15, from which it can be inferred that the CBDs have no obvious "
      "control effect on the peak and RMS acceleration response of the first "
      "and second stories, where the phenomenon of aggravating response even "
      "appears. However, the acceleration responses of the 3rd and 4th stories "
      "show promising reduction rates. Under frequent-intensity earthquake "
      "conditions, the average values of the peak and RMS acceleration "
      "reduction rates for all stories are −3.4% and 3.3%, respectively, and "
      "under moderate-intensity earthquake conditions, the average values "
      "increase to 1.2% and 8.8%, respectively, indicating that as the peak of "
      "the input ground motion increases, the acceleration reduction rate "
      "increases, which is consistent with the reduction rates of interstory "
      "drift. Overall, the control effect of the CBDs on the acceleration "
      "response of the story in which they are located and that above is "
      "improved, but the stories below the CBDs still exhibit behavior that is "
      "less than ideal.")
    FIG(b, 15, F.fig_f15(), lang)

    # ------------------------------------------ FEA Results and Analysis --
    H(b, lang,
      "Kết quả phân tích phần tử hữu hạn",
      "FEA Results and Analysis", level=3)
    P(b, lang,
      "Trong thí nghiệm trên bàn rung, kết cấu có CBD cho thấy hiệu quả giảm "
      "chấn đầy hứa hẹn về phản ứng dịch chuyển. Để đánh giá những hành vi "
      "không thể nhìn thấy rõ hoặc không thu được ngay từ thí nghiệm trên bàn "
      "rung, độ ổn định địa chấn của kết cấu có CBD cũng được phân tích bằng "
      "mô phỏng số.",
      "In the shaking table test, the CBD-equipped structure exhibited "
      "promising damping effects in terms of displacement response. To "
      "evaluate behaviors not immediately obvious or obtainable in shaking "
      "table tests, the seismic stability of the CBD-equipped structure was "
      "also analyzed by numerical simulation.")

    H(b, lang,
      "So sánh mô hình phân tích phần tử hữu hạn với kết quả thí nghiệm trên bàn rung",
      "Comparison of Finite Element Analysis Model with Shaking Table Test Results",
      level=4)
    P(b, lang,
      "Mô hình phân tích phần tử hữu hạn (FEA) của kết cấu thí nghiệm, có và "
      "không có CBD, được xây dựng bằng gói phần mềm SAP2000 [37] và được thể "
      "hiện trên Hình 16. Quan hệ hiến định đàn hồi được dùng cho vật liệu "
      "trong mô hình FEA. Trong mô hình FEA của kết cấu thí nghiệm có CBD, khối "
      "lượng của các phễu than được mô phỏng bằng cách gán thuộc tính khối "
      "lượng cho các nút. Phần tử LINK được dùng để nối nút với kết cấu, và "
      "đặc tính độ cứng và cản của phần tử này được điều chỉnh để mô phỏng đặc "
      "tính động của các CBD.",
      "A finite element analysis (FEA) model of the test structure with and "
      "without CBDs was constructed using the SAP2000 software package [37] "
      "and is shown in Figure 16. The elastic constitutive relation was used "
      "for the materials in the FEA model. In the FEA model of the "
      "CBD-equipped test structure, the mass of the coal buckets was simulated "
      "by assigning mass attributes to the nodes. The LINK element was used to "
      "connect the node and the structure, and the stiffness and damping "
      "properties of this element were adjusted to simulate the dynamic "
      "characteristics of the CBDs.")
    FIG(b, 16, F.fig_f16(), lang)

    P(b, lang,
      "Dựa trên phương pháp phân tích lịch sử thời gian, phản ứng động của mô "
      "hình FEA kết cấu, có và không có CBD, đã được phân tích và so sánh. Kết "
      "quả của phân tích số này sau đó được đối chiếu với kết quả thí nghiệm. "
      "Trong quá trình thí nghiệm, hiệu năng của cả kết cấu lẫn các CBD đều bị "
      "ảnh hưởng bởi tác động tích lũy của nhiều điều kiện thử. Tuy nhiên, mô "
      "hình FEA là mô hình lý tưởng và kết quả của từng điều kiện đã thử là "
      "độc lập, không ảnh hưởng lẫn nhau. Vì lý do này, kết quả tính toán FEA "
      "cho thấy sai số nhỏ khi so sánh với kết quả thí nghiệm. Hình 17(a) và "
      "17(b) thể hiện hiệu quả kiểm soát dịch chuyển giữa tầng của các CBD "
      "trong mô hình thí nghiệm và mô hình FEA dưới tác động của địa chấn El "
      "Centro và Impvall, tương ứng. Hình 17(c) cho thấy sự so sánh dịch "
      "chuyển tương đối của CBD3 giữa mô hình thí nghiệm và mô hình FEA. Như "
      "đã chỉ ra trên Hình 17(c), dịch chuyển tương đối của các CBD phản ánh "
      "phản ứng tương tác giữa khung và các CBD, cho thấy các bộ phận giảm "
      "chấn của CBD chủ động tiêu tán năng lượng địa chấn.",
      "Based on the time-history analysis method, the dynamic response of the "
      "structural FEA model with and without CBDs was analyzed and compared. "
      "The results of this numerical analysis were then compared with the test "
      "results. In the test process, the performance of both the structure and "
      "the CBDs was affected by the cumulative effect of multiple test "
      "conditions. However, the FEA model is an ideal model, and the results "
      "from each tested condition are independent and do not affect one "
      "another. Because of this, the FEA calculation results showed small "
      "error when compared to the test results. Figures 17(a) and 17(b) show "
      "the interstory drift control effect of the CBDs in the test model and "
      "the FEA model under the action of the El Centro and Impvall seismic "
      "excitations, respectively. Figure 17(c) shows a comparison of the "
      "relative displacements of CBD3 in the test model and the FEA model. As "
      "indicated in Figure 17(c), the relative displacements of the CBDs "
      "reflect interactive responses between the frame and CBDs, indicating "
      "that the damping components of the CBDs actively dissipate seismic "
      "energy.")
    FIG(b, 17, F.fig_f17(), lang)

    P(b, lang,
      "Có thể thấy từ những kết quả này rằng xu hướng phản ứng tổng thể giữa mô "
      "hình thí nghiệm và mô hình FEA là nhất quán, và hiệu quả giảm chấn của "
      "các CBD cho thấy sự phù hợp tốt.",
      "It can be seen from these results that the overall response trend "
      "between the test model and the FEA model is consistent, and the "
      "indicated reduction effects of the CBDs are in good agreement.")

    # -------------------------- Influence of Seismic Wave Discreteness ---
    H(b, lang,
      "Ảnh hưởng của tính rời rạc của sóng địa chấn đến tỷ lệ giảm chấn",
      "Influence of Seismic Wave Discreteness on Reduction Rate", level=4)
    P(b, lang,
      "Các nghiên cứu trước đây đã chứng minh rằng các kết cấu có bộ giảm chấn "
      "khối điều chỉnh bị ảnh hưởng đáng kể bởi tính ngẫu nhiên của chuyển động "
      "nền, và hiệu quả địa chấn của TMD phụ thuộc rất nhiều vào tần số, theo "
      "đó nó chỉ hoạt động hiệu quả trong điều kiện cộng hưởng [36]. Để xác "
      "định độ tin cậy hấp thụ chấn động của các CBD trong kết cấu được đánh "
      "giá, 22 chuyển động nền trường xa và 28 chuyển động nền trường gần được "
      "đề xuất bởi ATC-63 [38] đã được chọn làm sóng địa chấn đầu vào. Ba tác "
      "động địa chấn dùng trong thí nghiệm trên bàn rung cũng được áp dụng, "
      "tổng cộng có 53 sóng địa chấn. Phổ phản ứng gia tốc tuyệt đối của 22 sóng "
      "địa chấn trường xa và 28 sóng địa chấn trường gần được thể hiện trên "
      "Hình 18(a) và 18(b), tương ứng. Các sóng địa chấn được tỷ lệ hóa cho "
      "phân tích số theo hệ số tương tự thời gian cho trong Bảng 1.",
      "Previous studies have demonstrated that structures with tuned mass "
      "dampers are significantly affected by the randomness of ground motions, "
      "and that the seismic effectiveness of a TMD is highly dependent on "
      "frequency, in that it only operates efficiently under resonant "
      "conditions [36]. To determine the shock absorption reliability of the "
      "CBDs in the evaluated structure, 22 far-field ground motions and 28 "
      "near-field ground motions suggested by ATC-63 [38] were selected as "
      "input seismic waves. The three seismic excitations used in the shaking "
      "table test were also applied, making 53 seismic waves in total. The "
      "absolute acceleration response spectra of the 22 far-field seismic "
      "waves and the 28 near-field seismic waves are shown in Figures 18(a) "
      "and 18(b), respectively. The seismic waves were scaled for numerical "
      "analysis according to the time similarity coefficients provided in "
      "Table 1.")
    FIG(b, 18, F.fig_f18(), lang)

    return b
