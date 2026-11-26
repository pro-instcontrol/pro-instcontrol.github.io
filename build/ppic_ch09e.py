# -*- coding: utf-8 -*-
"""Book 9, Chapter 9 (part E) - CONCLUSION and REFERENCES (EN/VI).

Source: Emilija Kisić, Željko Đurović and Vera Petrović, in L. N. Jalali (ed.),
*Handbook on Power Plant Instrumentation and Control* (Bibliotex, 2019), PDF
pp. 238-243, printed pp. 222-227 (absolute lines 6166-6370 of
work/ppic_raw.txt). The conclusion covers the confirmed assumption, the
originality of the method, the two prognostics approaches, advantages,
shortcomings and future work. All forty printed references are reproduced
verbatim in English on both language pages; ``REFS`` renders them in an
ordered list, so the printed numbers 1-40 are preserved by list numbering.
There are no figures, tables or equations in this module.
"""
try:
    import ppicfig9 as F  # noqa: F401  (shared supplier import style)
except ImportError:                       # supplier not written yet
    class _SupplierNamespace(object):
        pass
    F = _SupplierNamespace()

from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401


# The source list is English; ampersands are escaped for HTML but the rendered
# text is verbatim. Leading "N. " is omitted because C.refs() emits an <ol>.
_REFS_ITEMS = [
    "Rosmaini A, Shahrul K. An overview of time-based and condition-based "
    "maintenance in industrial application. Journal of Computers &amp; "
    "Industrial Engineering. 2012;63:135–149. DOI: 10.1016/j.cie.2012.02.002",
    "Bloch H, Geitner F. Machinery Failure Analysis and Trouble Shooting. "
    "USA: Gulf Professional Publishing; 1997",
    "Mobley R. An Introduction to Predictive Maintenance. USA: Elsevier "
    "Science; 2002",
    "Wikipedia. List of Industrial Disasters [Internet]. 2017. Available "
    "from: https://en.wikipedia.org/wiki/List_of_industrial_disasters"
    "#cite_note-18 [Accessed: 20 February 2016]",
    "Jardine A, Lin D, Banjevic D. A review on machinery diagnostics and "
    "prognostics implementing condition-based maintenance. Mechanical "
    "Systems and Signal Processing. 2006;20:483–1510. DOI: "
    "10.1016/j.ymssp.2005.09.012",
    "Vachtsevanos G, Lewis F, Roemer M, Hess A, Wu B. Intelligent Fault "
    "Diagnosis and Prognosis for Engineering Systems. NJ: Wiley; 2006",
    "Ding S. Model-Based Fault Diagnosis Techniques. Berlin: Springer; 2008",
    "Heng A, Zhang S, Tan A, Mathew J. Rotating machinery prognostics: "
    "State of the art, challenges and opportunities. Mechanical Systems and "
    "Signal Processing. 2009;23:724–739. DOI: 10.1016/j.ymssp.2008.06.009",
    "Ma L. Condition monitoring in engineering asset management. In: "
    "Proceedings of Asia-Pacific Vibration Conference; 6–9 August 2007; "
    "Sapporo, Japan: APVC2007; 2007. pp. 1–16",
    "Le Son K, Fouladirad M, Barros A, Levrat E, Iung B. Remaining useful "
    "life estimation based on stochastic deterioration models: A "
    "comparative study. Reliability Engineering and System Safety. "
    "2013;112:165–175. DOI: 10.1016/j.ress.2012.11.022",
    "Sankararaman S. Significance, interpretation, and quantification of "
    "uncertainty in prognostics and remaining useful life prediction. "
    "Mechanical Systems and Signal Processing. 2015;52–53:228–247. DOI: "
    "10.1016/j.ymssp.2014.05.029",
    "Asadzadeh S, Azadeh A. An integrated systemic model for optimization "
    "of condition based maintenance with human error. Reliability "
    "Engineering and System Safety. 2014;124:117–131. DOI: "
    "10.1016/j.ress.2013.11.008",
    "Banjevic D, Jardine A. Calculation of reliability function and "
    "remaining useful life for a Markov failure time process. IMA Journal "
    "of Management Mathematics. 2006;17:115–130. DOI: "
    "10.1093/imaman/dpi029",
    "Kacprzynski J, Sarlashkar A, Roemer M. Predicting remaining life by "
    "fusing the physics of failure modeling with diagnostics. Journal of "
    "Metal. 2004;56:29–35. DOI: 10.1007/s11837-004-0029-2",
    "Lin A, Makis V. Recursive filters for a partially observable system "
    "subject to random failure. Advances in Applied Probability. "
    "2003;35:207–227. DOI: 10.1017/S0001867800012155",
    "Groer P. Analysis of time-to-failure with a Weibull model. In: "
    "Proceedings of the Maintenance and Reliability Conference; "
    "Knoxville, TN, USA; 2000. pp. 59.01-59.04",
    "Schwabacher M. A survey of data-driven prognostics. In: Proceedings "
    "of the AIAA Infotech@Aerospace Conference; 2005; Arlington, Virginia: "
    "American Institute of Aeronautics and Astronautics; 2005. pp. 1–5",
    "Luo J, Pattipati K, Qiao L, Chigusa S. Model-based prognostic "
    "techniques applied to a suspension system. Transactions on Systems, "
    "Man, and Cybernetics. 2003;38:1156–1168. DOI: "
    "10.1109/TSMCA.2008.2001055",
    "Moubray J. Reliability-Centred Maintenance. Oxford: "
    "Butterworth-Heinemann; 1997",
    "Tobon-Mejia D, Medjaher K, Zerhouni N, Tripot G. Hidden Markov models "
    "for failure diagnostic and prognostic. In: Prognostics and Health "
    "Management Conference; 2011; Shenzhen, China. IEEE Catalog Number: "
    "CFPII6IH-PRT; 2011. pp. 1–8",
    "Flynn D. Thermal Power Plant Simulation and Control. London: The "
    "Institution of Electrical Engineers; 2003",
    "Pradeebha P, Pappa N. Modelling and outlet temperature control of "
    "coal mill using model predictive controller. IEEE International "
    "Conference on Control Applications (CCA); Hyderabad, India; 2013. "
    "pp. 1069–1074. DOI: 10.1109/CCA.2013.6662893",
    "Renwick J, Babson P. Vibration analysis – a proven technique as a "
    "predictive maintenance tool. IEEE Transaction on Industry "
    "Applications. 1985;IA-21:324–33.",
    "Baydar N, Ball A. A comparative study of acoustic and vibration "
    "signals in detection of gear failures using Wigner-Ville "
    "distribution. Mechanical Systems and Signal Processing. "
    "2001;15:1091–1107. DOI: 10.1006/mssp.2000.1338",
    "Cohen L. Time-frequency distribution – A review. Proceedings of the "
    "IEEE. 1989;77:941–981",
    "Kisić E, Đurović Ž, Kovačević B, Petrović V. Application of T2 "
    "control charts and hidden Markov models in condition-based "
    "maintenance at thermoelectric power plants. Shock and Vibration. "
    "2015;2015:1–11. DOI: 10.1155/2015/960349",
    "Andrade A, Esat I, Badi M. Gearbox fault detection using statistical "
    "methods, time-frequency methods (STFT and Wigner-Ville distribution) "
    "and harmonic wavelet-A comparative study. In: Proceedings of the "
    "COMADEM ’99; UK: Chipping Norton; 1999. pp. 77–85",
    "Montgomery D. Introduction to Statistical Quality Control. 5th ed. "
    "New York, NY: John Wiley &amp; Sons; 2005",
    "Mason R, Young J. Multivariate Statistical Process Control With "
    "Industrial Applications. USA: ASA-SIAM; 2002",
    "Hotelling A. Multivariate quality control. In: Eisenhart C, Hastay M, "
    "Wallis W, editors. Techniques of Statistical Analysis. New York, NY: "
    "McGraw-Hill; 1947. pp. 111–184",
    "Duda R, Hart P, Stork D. Pattern Classification. New York, NY: "
    "John Wiley &amp; Sons; 2001",
    "Rabiner L. A tutorial on hidden Markov models and selected "
    "applications in speech recognition. Proceedings of the IEEE. "
    "1989;77:257–286",
    "Tiplica T, Kobi A, Barreau A, Chassagnon R. Spectral control chart. "
    "Quality Engineering. 2005;17:695–702. DOI: "
    "10.1080/08982110500251287",
    "Lee S, Li L, Ni J. Online degradation assessment and adaptive fault "
    "detection using modified hidden Markov model. Journal of "
    "Manufacturing Science and Engineering. 2010;132:0210101-02101011. "
    "DOI: 10.1115/1.4001247",
    "Tai A, Ching W, Chan L. Detection of machine failure: Hidden Markov "
    "model approach. Computers &amp; Industrial Engineering. "
    "2009;57:608–619. DOI: 10.1016/j.cie.2008.09.028",
    "Chen K, Chen L, Chen M, Lee C. Using SVM based method for equipment "
    "fault detection in a thermal power plant. Computers in Industry. "
    "2011;62:42–50. DOI: 10.1016/j.compind.2010.05.013",
    "Yang S. A condition-based preventive maintenance arrangement for "
    "thermal power plants. Electric Power Systems Research. "
    "2004;72:49–62. DOI: 10.1016/j.epsr.2004.03.007",
    "Frank P, Ding S, Marcu T. Model-based fault diagnosis in technical "
    "processes. Transactions of the Institute of Measurement and Control. "
    "2000;22:57–101. DOI: 10.1177/014233120002200104",
    "Wang L, Mehrabi M, Kannatey-Asibu E. Hidden Markov model-based tool "
    "wear monitoring in turning. ASME Journal of Manufacturing Science "
    "and Engineering. 2002;124:651–658. DOI: 10.1115/1.1475320",
    "Li Z, Wu Z, He Y, Fulei C. Hidden Markov model-based fault diagnostics "
    "method in speed-up and speed-down process for rotating machinery. "
    "Mechanical Systems and Signal Processing. 2005;19:329–339. DOI: "
    "10.1016/j.ymssp.2004.01.001",
]


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 9."""
    b = []

    # ------------------------------------------------------------- CONCLUSION
    H(b, lang, "KẾT LUẬN", "CONCLUSION", level=2)
    P(b, lang,
      "Dựa trên các kết quả đã trình bày, chúng tôi có thể rút ra một số "
      "kết luận. Thứ nhất, giả thiết đặt ra ở đầu nghiên cứu — rằng có thể "
      "trích xuất thông tin hữu ích từ các thành phần phổ của tín hiệu âm "
      "thanh — đã được xác nhận. Dựa trên thông tin này, có thể nhận biết "
      "tình trạng của các bộ phận quay của máy nghiền. Như đã giải thích "
      "trước đó, trong các tài liệu nghiên cứu, tín hiệu dao động thường "
      "được ưu tiên hơn tín hiệu âm thanh khi xét đến nội dung thông tin. "
      "Vì việc ghi tín hiệu âm thanh rẻ hơn nhiều so với ghi tín hiệu dao "
      "động, và xử lý tín hiệu âm thanh đơn giản hơn nhiều so với xử lý "
      "tín hiệu dao động, việc xác nhận nội dung thông tin của tín hiệu "
      "âm thanh là rất quan trọng.",
      "Based on the presented results, we can make several conclusions. "
      "Firstly, the assumption set at the beginning of this research, that "
      "useful information from spectral components of acoustic signals can "
      "be extracted, is confirmed. Based on this information, the condition "
      "of the rotating elements of the mill can be recognized. As previously "
      "explained, in the literature vibration signals are mostly preferred "
      "to acoustic signals when it comes to informative content. Given that "
      "the recording of acoustic signals is much cheaper than the recording "
      "of vibration signals, and processing of acoustic signals is much "
      "simpler than vibration signal processing, this confirmation of the "
      "informative content of acoustic signals is very important.")

    P(b, lang,
      "Tính mới của phương pháp đề xuất là sự kết hợp giữa biểu đồ kiểm "
      "soát và HMM trong dự báo hỏng hóc, cũng như việc áp dụng biểu đồ "
      "kiểm soát cho các thành phần trích xuất được từ phổ tần số. Cụ thể, "
      "trong tài liệu có thể tìm thấy các biểu đồ kiểm soát được xây dựng "
      "dựa trên phân tích phổ của tín hiệu [33]. Ở đây, một cách tiếp cận "
      "khác được đề xuất, đó là áp dụng biểu đồ kiểm soát T² cho các thành "
      "phần phổ của tín hiệu. Dựa trên kết quả, cách tiếp cận này đã chứng "
      "minh là rất hiệu quả. Trong tài liệu cũng có thể tìm thấy việc áp "
      "dụng biểu đồ kiểm soát và HMM để chẩn đoán quá trình suy giảm [34] "
      "cũng như để phát hiện lỗi [35], nhưng các bài báo đó dùng biểu đồ p "
      "chuẩn và biểu đồ kiểm soát Hotelling T². Có thể tìm thấy các báo "
      "cáo về nghiên cứu khác liên quan đến phát hiện một số loại hỏng "
      "hóc nhất định tại nhà máy nhiệt điện [36–38]. Ngoài ra, các mô hình "
      "chẩn đoán dựa trên HMM được xây dựng dựa trên tình trạng của hệ "
      "thống có thể được tìm thấy trong [39, 40]. So với tất cả các tài "
      "liệu đã nêu, phương pháp đề xuất ở đây là một tiếp cận mới.",
      "The originality of the proposed method is the combination of control "
      "charts and HMMs in failure prognostics, as well as the application of "
      "control charts to components extracted from the spectrogram. Namely, "
      "the literature contains control charts whose construction is based on "
      "spectral analysis of the signal [33]. Here, a different approach is "
      "proposed, that is, to apply T² control charts to the spectral "
      "components of the signal. Based on the results, this approach has "
      "proven to be very efficient. The literature also reports the "
      "application of control charts and HMMs for degradation process "
      "diagnosis [34], as well as for fault detection [35], but those papers "
      "use standard p-charts and Hotelling T² control charts. Reports of "
      "other research dealing with the detection of certain types of "
      "failures at thermoelectric power plants can be found in the "
      "literature [36–38]. Also, HMM-based diagnostic models founded upon "
      "the condition of the system can be found in Refs. [39, 40]. With "
      "regard to all the mentioned references, the original approach is "
      "proposed here.")

    P(b, lang,
      "Như đã mô tả trước đó, trong dự báo hỏng hóc, cách tiếp cận phổ biến "
      "nhất trong tài liệu là cách tiếp cận thứ nhất, tức là ước tính thời "
      "điểm lỗi sẽ xảy ra (ước tính RUL). Trong nghiên cứu này, trọng tâm "
      "là cách tiếp cận thứ hai, tức là ước tính xác suất máy hoạt động "
      "không bị hỏng cho đến một thời điểm tương lai nhất định (trong "
      "trường hợp của chúng tôi, cho đến chu kỳ tiếp theo cần kiểm tra và "
      "thay thế bàn nghiền). Với phương pháp đề xuất, HMM cung cấp cho "
      "chúng ta thông tin về tình trạng của bàn nghiền, tức là khi nào bàn "
      "nghiền đã mòn và cần được thay thế.",
      "As previously described, in failure prognostics the most common "
      "approach in the literature is the first approach, that is, the "
      "estimation of when the fault will occur (RUL estimation). In this "
      "research, the accent is on the second approach, that is, on the "
      "estimation of the probability that the machine will work without "
      "failure until some future time (in our case, until the next interval "
      "when inspection and grinding table replacement are needed). With the "
      "proposed method, the HMM gives us information about the condition of "
      "the grinding tables, that is, when the grinding tables are worn out, "
      "so that their replacement is needed.")

    # ------------------------------------------------------------ ADVANTAGES
    H(b, lang, "Ưu điểm của phương pháp đề xuất",
      "Advantages of the proposed method", level=3)
    P(b, lang,
      "Ưu điểm của phương pháp đề xuất là không xâm lấn, vì để thu thập dữ "
      "liệu giám sát tình trạng không cần ngắt hoạt động của hệ thống "
      "nghiền than hay tắt toàn bộ hệ thống. Một ưu điểm khác là phương "
      "pháp dựa trên xử lý tín hiệu âm thanh, vốn đơn giản hơn để xử lý và "
      "thu thập so với tín hiệu dao động. Việc triển khai phần mềm của "
      "thuật toán đề xuất không quá phức tạp và không tốn nhiều thời gian "
      "khi HMM đã được huấn luyện.",
      "The advantage of the proposed method is that it is non-invasive, "
      "because for the acquisition of condition-monitoring data it is not "
      "necessary to interrupt coal-grinding subsystem operation and shut "
      "down the whole subsystem. Another advantage is that it is based on "
      "acoustic signal processing, which is simpler for processing and "
      "acquisition than vibration signals. The software realization of the "
      "proposed algorithm is not too complex and is not time-consuming once "
      "the HMM is trained.")

    # ---------------------------------------------------------- SHORTCOMINGS
    H(b, lang, "Hạn chế của phương pháp", "Shortcomings of the method", level=3)
    P(b, lang,
      "Một hạn chế của phương pháp này là việc ghi tín hiệu âm thanh trong "
      "điều kiện có nhiễu không thể tránh khỏi, có thể ảnh hưởng đến độ "
      "chính xác của kết quả. Các kết quả trình bày được thu thập ngoại "
      "tuyến, tức là HMM được huấn luyện dựa trên các tín hiệu đã ghi trước "
      "đó. Để áp dụng phương pháp này cho dữ liệu trực tuyến, cần một lượng "
      "dữ liệu lớn hơn nhiều để huấn luyện HMM phù hợp và xác định chính "
      "xác hơn thời điểm cần thay thế bàn nghiền. Dù sao đi nữa, phương "
      "pháp đề xuất vẫn có thể áp dụng theo thời gian thực và góp phần "
      "tăng tính ổn định và độ tin cậy cho một trong những hệ thống quan "
      "trọng nhất của nhà máy nhiệt điện.",
      "A shortcoming of this method is the recording of acoustic signals in "
      "the presence of unavoidable noise, which can influence the accuracy "
      "of the results. The presented results were gathered offline, that is, "
      "the HMM was trained based on the already recorded signals. For "
      "applying this method to online data, a much larger amount of data is "
      "needed for adequate HMM training and more accurate determination of "
      "the time moment when the grinding table replacement is needed. Anyhow, "
      "the proposed method can be applied in real time and used for higher "
      "stability and reliability of one of the most important subsystems in "
      "a thermoelectric power plant.")

    # ------------------------------------------------------------ FUTURE WORK
    H(b, lang, "Hướng nghiên cứu tiếp theo", "Future work", level=3)
    P(b, lang,
      "Hướng phát triển tiếp theo của nghiên cứu này là xây dựng một hệ "
      "thống thích ứng, có thể điều chỉnh theo các thống kê mới phát sinh "
      "do quá trình lão hóa của các bộ phận, không chỉ dựa trên tình trạng "
      "của tấm bàn nghiền. Ngoài ra, có thể thực hiện nghiên cứu đáng kể "
      "khi dữ liệu giám sát tình trạng là tín hiệu dao động ghi được, để "
      "phân tích so sánh với tín hiệu âm thanh. Dữ liệu sự kiện bổ sung có "
      "thể nâng cấp phương pháp đề xuất khi kết hợp với dữ liệu bảo trì "
      "theo tình trạng. Một số nghiên cứu tương lai có thể là xây dựng "
      "chính sách bảo trì tối ưu cho nhà máy nhiệt điện dựa trên các kết "
      "quả thu được.",
      "Further direction in this research would be the making of an adaptive "
      "system which would be adjustable to new statistics which are "
      "consequences of components ageing, not just the condition of grinding "
      "table plates. Also, a significant study could be made when "
      "condition-monitoring data would be recorded vibration signals, for "
      "comparative analysis with acoustic signals. Additional event data "
      "could upgrade the proposed method in combination with condition "
      "maintenance data. Some future research could be to make optimal "
      "maintenance policy in thermoelectric power plant, according to gain "
      "results.")

    # ------------------------------------------------------------- REFERENCES
    if lang == "vi":
        P(b, lang,
          "Dưới đây là danh sách 40 tài liệu tham khảo nguyên bản bằng tiếng "
          "Anh, giữ nguyên số hiệu.", "")
    H(b, lang, "TÀI LIỆU THAM KHẢO", "REFERENCES", level=2)
    REFS(b, lang, _REFS_ITEMS)

    return b
