# -*- coding: utf-8 -*-
"""Book 9, Chapter 8 (part G) — reduction rates over 53 seismic excitations,
period-change study, CONCLUSION, ACKNOWLEDGMENTS and the 38 verbatim
REFERENCES (EN/VI bilingual).

Source: Ling-Yun Peng, Ying-Jie Kang, Zong-Rui Lai and Yu-Ke Deng, in L. N.
Jalali (ed.), *Handbook on Power Plant Instrumentation and Control* (Bibliotex,
2019), PDF pp. 205-214, printed pp. 189-198 (absolute lines 5197-5484 of
work/ppic_raw.txt). Figures 19-21 are embedded from the shared `ppicfig8`
supplier; while that supplier is still being written, non-overwriting
callable stubs are installed so this module can be compiled and QA'd on its
own. The reference list is English bibliographic data in both languages and
is reproduced verbatim (apart from OCR line-break artefacts and the
HTML-escaped ampersand in ref. 25).
"""
try:
    import ppicfig8 as F  # noqa: F401  (shared supplier import style)
except ImportError:                       # supplier not written yet
    class _SupplierNamespace(object):
        pass
    F = _SupplierNamespace()

from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401


# ------------------------------------------------------- figure fallback stubs
def _stub_svg(title):
    """A neutral framed placeholder, replaced by the real figure callable."""
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="680" height="300" '
            'viewBox="0 0 680 300">'
            '<rect x="12" y="12" width="656" height="276" fill="none" '
            'stroke="#9aa0a6" stroke-width="1"/>'
            '<line x1="60" y1="250" x2="620" y2="250" stroke="#9aa0a6"/>'
            '<line x1="60" y1="250" x2="60" y2="50" stroke="#9aa0a6"/>'
            '<text x="340" y="150" text-anchor="middle" font-size="15" '
            'fill="#555">%s</text></svg>' % title)


if not hasattr(F, "fig_f19"):
    F.fig_f19 = lambda: (
        _stub_svg("Figure 19 - reduction rates, 53 excitations"),
        "Hình 19 · Tỷ lệ giảm chấn dưới 53 bộ tác động địa chấn. Tỷ lệ giảm của "
        "(a) dịch chuyển và (b) gia tốc.",
        "Figure 19 · Reduction rates under 53 sets of seismic excitations. "
        "Reduction rates of (a) displacement and (b) acceleration.",
        "Biểu đồ phân tán tỷ lệ giảm dịch chuyển và gia tốc.",
        "Scatter plots of displacement and acceleration reduction rates.")
if not hasattr(F, "fig_f20"):
    F.fig_f20 = lambda: (
        _stub_svg("Figure 20 - excitations 23 and 38"),
        "Hình 20 · Tỷ lệ giảm chấn dưới 53 bộ tác động địa chấn. (a) Phổ biên độ "
        "Fourier của tác động thứ 23 và thứ 38 và dải tần hoạt động của kết cấu "
        "có CBD. (b) So sánh tỷ lệ giảm độ lệch giữa các tầng giữa hai tác động. "
        "(c) So sánh phổ phản ứng giữa hai tác động.",
        "Figure 20 · Reduction rates under 53 sets of seismic excitations. "
        "(a) Fourier amplitude spectrum of the 23rd and the 38th seismic "
        "excitations and the operating range of the structure with CBDs. "
        "(b) Comparison of interstory drift reduction rate between the 23rd "
        "and the 38th seismic excitations. (c) Response spectrum comparison "
        "between the 23rd and the 38th seismic excitations.",
        "Phổ Fourier, lịch sử độ lệch tầng và phổ phản ứng.",
        "Fourier spectra, interstory drift histories and response spectra.")
if not hasattr(F, "fig_f21"):
    F.fig_f21 = lambda: (
        _stub_svg("Figure 21 - reduction rates vs structural frequency"),
        "Hình 21 · Tỷ lệ giảm của (a) dịch chuyển và (b) gia tốc theo sự thay đổi "
        "tần số kết cấu.",
        "Figure 21 · Reduction rates of (a) displacement and (b) acceleration "
        "with variation in structural frequency.",
        "Đồ thị tỷ lệ giảm theo tỷ số chu kỳ kết cấu T/T1.",
        "Reduction-rate curves versus structural frequency ratio T/T1.")


# The 38 source bibliography entries, identical in both language editions.
_REFS_ITEMS = [
    'B. J. Tang, R. Li, X. Y. Li, and H. Chen, "An optimal production planning model of coal-fired power industry in China: considering the process of closing down inefficient units and developing CCS technologies," Applied Energy, vol. 206, pp. 519–530, 2017.',
    'Z. Shu, S. Li, J. Zhang, and M. He, "Optimum seismic design of a power plant building with pendulum tuned mass damper system by its heavy suspended buckets," Engineering Structures, vol. 136, pp. 114–132, 2017.',
    'J. T. P. Yao, "Concept of structural control," Journal of the Structural Division, vol. 98, no. 7, pp. 1567–1574, 1972.',
    'T. Wu, G. Bai, and B. Liu, "Experimental study on seismic behavior of RC frame-bent structure of a large-scale power plant," Journal of Building Structures, vol. 28, no. 3, pp. 46–52, 2007, in Chinese.',
    'J. Den Hartog, Mechanical Vibrations, McGraw-Hill, New York, NY, USA, 1956.',
    'G. B. Warburton, "Optimum absorber parameters for various combinations of response and excitation parameters," Earthquake Engineering and Structural Dynamics, vol. 10, no. 3, pp. 381–401, 1982.',
    'H. C. Tsai and G. C. Lin, "Explicit formulae for optimum absorber parameters for force-excited and viscously damped systems," Journal of Sound and Vibration, vol. 176, no. 5, pp. 585–596, 1994.',
    'M. Gutierrez Soto and H. Adeli, "Tuned mass dampers," Archives of Computational Methods in Engineering, vol. 20, no. 4, pp. 419–431, 2013.',
    'C. C. Chang, "Mass dampers and their optimal designs for building vibration control," Engineering Structures, vol. 21, no. 5, pp. 454–463, 1999.',
    'D. Wang, T. K. T. Tse, Y. Zhou, and Q. Li, "Structural performance and cost analysis of wind-induced vibration control schemes for a real super-tall building," Structure and Infrastructure Engineering, vol. 11, no. 8, pp. 990–1011, 2015.',
    'N. Longarini and M. Zucca, "A chimney\'s seismic assessment by a tuned mass damper," Engineering Structures, vol. 79, pp. 290–296, 2014.',
    'N. Hoang, Y. Fujino, and P. Warnitchai, "Optimal tuned mass damper for seismic applications and practical design formulas," Engineering Structures, vol. 30, no. 3, pp. 707–715, 2008.',
    'K. Xu and T. Igusa, "Dynamic characteristics of multiple substructures with closely spaced frequencies," Earthquake Engineering and Structural Dynamics, vol. 21, no. 12, pp. 1059–1070, 1992.',
    'H. Yamaguchi and N. Harnpornchai, "Fundamental characteristics of multiple tuned mass dampers for suppressing harmonically forced oscillations," Earthquake Engineering and Structural Dynamics, vol. 22, no. 1, pp. 51–62, 1993.',
    'T. Igusa and K. Xu, "Vibration control using multiple tuned mass dampers," Journal of Sound and Vibration, vol. 175, no. 4, pp. 491–503, 1994.',
    'R. S. Jangid and T. Datta, "Performance of multiple tuned mass dampers for torsionally coupled system," Earthquake Engineering and Structural Dynamics, vol. 26, no. 3, pp. 307–317, 1997.',
    'A. S. Joshi and R. S. Jangid, "Optimum parameters of multiple tuned mass dampers for base-excited damped systems," Journal of Sound and Vibration, vol. 202, no. 5, pp. 657–667, 1997.',
    'R. Rana and T. T. Soong, "Parametric study and simplified design of tuned mass dampers," Engineering Structures, vol. 20, no. 3, pp. 193–204, 1998.',
    'C. Li, "Performance of multiple tuned mass dampers for attenuating undesirable oscillations of structures under the ground acceleration," Earthquake Engineering and Structural Dynamics, vol. 29, no. 9, pp. 1405–1421, 2000.',
    'C. Li, "Optimum multiple tuned mass dampers for structures under the ground acceleration based on DDMF and ADMF," Earthquake Engineering and Structural Dynamics, vol. 31, no. 4, pp. 897–919, 2002.',
    'W. Tu and Y Zou, "Analysis of multistory structures with MTMD in frequency domain," Engineering Mechanics, vol. 20, no. 3, pp. 78–88, 2003.',
    'C. Li and Y. Liu, "Optimum multiple tuned mass dampers for structures under the ground acceleration based on the uniform distribution of system parameters," Earthquake Engineering and Structural Dynamics, vol. 32, no. 5, pp. 671–690, 2003.',
    'C. C. Lin, J. F. Wang, C. H. Lien, H. W. Chiang, and C. S. Lin, "Optimum design and experimental study of multiple tuned mass dampers with limited stroke," Earthquake Engineering and Structural Dynamics, vol. 39, no. 14, pp. 1631–1651, 2010.',
    'C. C. Lin and J. F. Wang, "Optimal design and practical considerations of tuned mass dampers for structural control," in Design Optimization of Active and Passive Structural Control Systems, Chapter 6, pp. 126–149, IGI global, Hershey, PA, USA, 2013.',
    'C. Lin, G. Lin, and C. Chiu, "Robust design strategy for multiple tuned mass dampers with consideration of frequency bandwidth," International Journal of Structural Stability &amp; Dynamics, vol. 17, no. 01, pp. 151–177, 2017.',
    'Z. Shu, S. Li, X. Sun, and M. He, "Performance-based seismic design of a pendulum tuned mass damper system," Journal of Earthquake Engineering, 2017, In press.',
    'S. He, L. Peng, N. Lin et al., "Research on bearing type coal scuttle of main power building in large thermal power plant in highly seismic region," Engineering Journal of Wuhan University, vol. 46, pp. 85–89, 2013, in Chinese.',
    'G. Chen and J. Wu, "Optimal placement of multiple tune mass dampers for seismic structures," Journal of Structural Engineering, vol. 127, no. 9, pp. 1054–1062, 2001.',
    'Y. Arfiadi and M. Hadi, "Optimum placement and properties of tuned mass dampers using hybrid genetic algorithms," International Journal of Optimization in Civil Engineering, vol. 1, no. 1, pp. 167–187, 2011.',
    'R. Frans and Y. Arfiadi, "Designing optimum locations and properties of MTMD systems," Procedia Engineering, vol. 125, pp. 892–898, 2015.',
    'T. Nagase and T. Hisatoku, "Tuned-pendulum mass damper installed in crystal tower," The Structural Design of Tall and Special Buildings, vol. 1, no. 1, pp. 35–56, 1992.',
    'J. Connor and S. Laflamme, Structural Motion Engineering, Springer International Publishing, New York, NY, USA, 2014.',
    'M. H. Chey and J. U. Kim, "Parametric control of structural responses using an optimal passive tuned mass damper under stationary Gaussian white noise excitations," Frontiers of Structural Civil Engineering, vol. 6, no. 3, pp. 267–280, 2012.',
    'R. Soto-Brito and S. E. Ruiz, "Influence of ground motion intensity on the effectiveness of tuned mass dampers," Earthquake Engineering and Structural Dynamics, vol. 28, no. 11, pp. 1255–1271, 1999.',
    'GB 50011-2010, Code for Seismic Design of Buildings, Ministry of Construction, General Administration of Quality Supervision, Inspection and Quarantine, Beijing, China, 2010.',
    'C. C. Lin, J. F. Wang, and J. M. Ueng, "Vibration control identification of seismically excited m.d.o.f. structure-PTMD systems," Journal of Sound and Vibration, vol. 240, no. 1, pp. 87–115, 2001.',
    'CSI, CSI Analysis Reference Manual for SAP2000, ETABS, SAFE and CSiBridge, Computers and Structures, Inc., Berkeley, CA, USA, 2015.',
    'ATC 63, Quantification of Building Seismic Performance Factors (Report ATC-63), Applied Technology Council, Redwood City, CA, USA, 2010.',
]


def _curly_quotes(text):
    """Restore the source's typographic quotes; literals stay readable above."""
    out = []
    opening = True
    for ch in text:
        if ch == '"':
            out.append("\u201c" if opening else "\u201d")
            opening = not opening
        elif ch == "'":
            out.append("\u2019")
        else:
            out.append(ch)
    return "".join(out)


_REFS_ITEMS = [_curly_quotes(r) for r in _REFS_ITEMS]


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 8."""
    b = []

    # --------------------------- reduction rates over 53 seismic excitations
    P(b, lang,
      "Tính ngẫu nhiên của sóng động đất có ảnh hưởng đáng kể đến hiệu quả giảm "
      "chấn của kết cấu được trang bị CBD. Với các thông số thiết kế tối ưu, mức "
      "giảm dịch chuyển và gia tốc của kết cấu dưới 53 bộ điều kiện địa chấn được "
      "đánh giá được thể hiện ở Hình 19(a) và (b). Tỷ lệ giảm RMS và tỷ lệ giảm "
      "đỉnh của dịch chuyển lần lượt là 17,2% và 9,6%; tỷ lệ giảm RMS và tỷ lệ "
      "giảm đỉnh của gia tốc lần lượt là 2,1% và −1,9%. Ngoài ra, có thể rút ra "
      "các kết luận sau từ kết quả phân tích:",
      "The randomness of seismic waves has a significant influence on the "
      "damping effect of a structure equipped with CBDs. Under the optimal "
      "design parameters, the structural displacement and acceleration damping "
      "under the 53 evaluated sets of seismic conditions are shown in Figures "
      "19(a) and (b). The displacement RMS and the peak reduction rates were "
      "17.2% and 9.6%, respectively, and the acceleration RMS and peak reduction "
      "rates were 2.1% and −1.9%, respectively. In addition, the following "
      "conclusions can be drawn from the analysis results:")

    L(b, lang,
      ["Khi sử dụng CBD ở các thông số tối ưu, tỷ lệ giảm dịch chuyển và gia tốc "
       "dưới mỗi điều kiện động đất có sự phân tán nhất định. Ví dụ, RMS của tỷ "
       "lệ giảm và giá trị đỉnh của dịch chuyển dưới sóng động đất thứ 23 lần "
       "lượt là 40,0% và 28,3%, trong khi RMS và giá trị đỉnh dưới sóng động đất "
       "thứ 38 tăng thêm 7,7% và 6%. Hình 20(a) mô tả phổ biên độ Fourier của "
       "sóng động đất thứ 23 và thứ 38. Có thể thấy rõ rằng trong dải tần hoạt "
       "động, thành phần của sóng thứ 23 lớn hơn thành phần của sóng thứ 38. Do "
       "đó, hiệu năng của CBD rất tốt dưới sóng động đất thứ 23 nhưng kém hiệu "
       "quả dưới sóng thứ 38, như đã được dự đoán trong miền tần số. Hình 20(b) "
       "và 20(c) lần lượt so sánh độ lệch giữa các tầng và phổ phản ứng gia tốc "
       "của sóng động đất giữa điều kiện thứ 23 và điều kiện thứ 38. Trong phổ "
       "phản ứng của sóng thứ 23, biên độ của thành phần ứng với chu kỳ phương "
       "thức kiểm soát của kết cấu nằm gần cực đại cục bộ của phổ phản ứng. Tuy "
       "nhiên, trong phổ phản ứng của sóng thứ 38, biên độ đó lại nằm gần giá "
       "trị cực tiểu của phổ. Điều này dẫn đến sự khác biệt về đóng góp của "
       "phương thức kiểm soát vào phản ứng của kết cấu. Đóng góp của phương "
       "thức kiểm soát chính càng lớn thì hiệu quả kiểm soát càng tốt.",
       "Theo phổ phản ứng của sóng động đất được trình bày ở Hình 18, biên độ "
       "trung bình của phổ phản ứng ứng với chu kỳ phương thức kiểm soát của kết "
       "cấu trong 28 sóng động đất trường gần rõ ràng lớn hơn so với 22 sóng "
       "động đất trường xa. Mức giảm dưới các sóng động đất trường gần tốt hơn "
       "dưới các sóng trường xa, phù hợp với kết quả phổ phản ứng của sóng động "
       "đất.",
       "Dưới 53 sóng động đất khác nhau, chất lượng của tỷ lệ giảm dịch chuyển "
       "của kết cấu khác với chất lượng của tỷ lệ giảm gia tốc. Tỷ lệ giảm RMS "
       "dịch chuyển lớn nhất và nhỏ nhất ứng với điều kiện sóng động đất thứ 23 "
       "và thứ 38, trong khi tỷ lệ giảm RMS gia tốc lớn nhất và nhỏ nhất ứng với "
       "điều kiện thứ 23 và thứ 9. Đáng chú ý là hiệu quả kiểm soát dịch chuyển "
       "của CBD rất rõ rệt, còn hiệu quả kiểm soát gia tốc chưa thực sự lý "
       "tưởng."],
      ["When using the CBDs at their optimal parameters, the displacement and "
       "acceleration reduction rates under each earthquake condition have a "
       "certain discreteness. For example, the RMS of the reduction rate and "
       "the peak value of displacement under the 23rd seismic wave were 40.0% "
       "and 28.3%, respectively, while the RMS and peak value under the 38th "
       "seismic wave increased by 7.7% and 6%, respectively. Figure 20(a) "
       "depicts the Fourier amplitude spectrum of the 23rd seismic wave and the "
       "38th seismic wave. It can clearly be observed that the components of "
       "the 23rd seismic wave are larger than those of the 38th seismic wave in "
       "the operating range. Therefore, the performance of the CBDs is "
       "obviously excellent under the 23rd seismic wave, but not good under the "
       "38th seismic wave, as expected in the frequency domain. Figures 20(b) "
       "and 20(c) show a comparison of interstory drift and seismic wave "
       "acceleration response spectra, respectively, between the 23rd condition "
       "and the 38th condition. In the response spectrum of the 23rd seismic "
       "wave, the amplitude of the component corresponding to the structure "
       "control mode period is near the local maxima of the response spectrum. "
       "However, in the 38th seismic wave response spectrum, that amplitude is "
       "near the minimum of the response spectrum. This leads to a difference "
       "in the contribution of the control mode to the structural response. The "
       "higher the contribution of the main control mode, the better the "
       "control effect.",
       "According to the seismic wave response spectrum shown in Figure 18, the "
       "average amplitude of the response spectrum, corresponding to the "
       "structure control mode period, of the 28 near-field seismic waves is "
       "clearly greater than that of the 22 far-field seismic waves. The "
       "reductions under the near-field seismic waves are better than those "
       "under the far-field seismic waves, which are consistent with the "
       "seismic wave response spectrum results.",
       "Under the 53 different seismic waves, the qualities of the structural "
       "displacement reduction rate are different from those of the acceleration "
       "reduction rate. The largest and smallest displacement RMS reduction "
       "rates are under the 23rd and the 38th seismic wave conditions, "
       "respectively, while the largest and the smallest acceleration RMS "
       "reduction rates are under the 23rd and the 9th seismic wave conditions. "
       "Notably, the displacement control effect of the CBDs is obvious, while "
       "the acceleration control is less than ideal."],
      ordered=True)

    FIG(b, 19, F.fig_f19(), lang)
    FIG(b, 20, F.fig_f20(), lang)

    P(b, lang,
      "Nhìn chung, hiệu quả kiểm soát của CBD thể hiện sự phân tán nhất định. Dù "
      "CBD kém hữu ích bên ngoài điều kiện cộng hưởng, phản ứng của kết cấu trong "
      "trường hợp này lại nhỏ. Đáng chú ý, tần số dao động cơ bản của kết cấu "
      "nhà máy điện than thông thường thường nằm trong vùng có biên độ Fourier "
      "lớn hơn. Vì CBD kiểm soát rung động hiệu quả, đặc tính dao động cơ bản "
      "này cho thấy CBD có thể được sử dụng thành công trong các kết cấu nhà "
      "máy điện than nhằm đảm bảo ổn định động đất.",
      "Overall, the control effect of the CBDs illustrates a certain "
      "discreteness. Although the CBDs are less useful outside of their "
      "resonant conditions, the structural response is small in this situation. "
      "Notably, the basic vibration frequency of a conventional coal-fired "
      "power plant structure is often located in a region with a larger Fourier "
      "amplitude. Because the CBDs provide efficient vibration control, this "
      "basic vibration behaviour suggests that they can be successfully used "
      "in coal-fired power plant structures to ensure seismic stability.")

    # ------------------------------- influence of structural period change
    H(b, lang, "Ảnh hưởng của sự thay đổi chu kỳ kết cấu đến tỷ lệ giảm chấn",
      "Influence of Structural Period Change on Reduction Rates", level=3)
    P(b, lang,
      "Dưới ảnh hưởng kết hợp của các yếu tố xây dựng, vòng đời và môi trường "
      "liên quan đến kết cấu nhà máy điện than, đặc tính động của kết cấu hiện "
      "hữu sẽ khác với đặc tính của kết cấu được thiết kế ban đầu. Hơn nữa, khi "
      "kết cấu chịu động đất mạnh, nó sẽ bị hư hỏng và độ cứng giảm theo. Điều "
      "này dẫn đến sai lệch giữa chu kỳ phản ứng thực của kết cấu và chu kỳ phản "
      "ứng thiết kế, từ đó ảnh hưởng đến hiệu quả kiểm soát rung của CBD. Để xác "
      "định ảnh hưởng của sự thay đổi chu kỳ kết cấu đến tỷ lệ giảm do CBD mang "
      "lại, người ta đã phân tích hiệu quả giảm rung của các kết cấu có chu kỳ "
      "khác nhau được thiết kế bằng các thông số tối ưu ban đầu. Sự thay đổi chu "
      "kỳ kết cấu được mô phỏng bằng cách thay đổi thông số mô đun đàn hồi của "
      "vật liệu trong mô hình. Hình 21(a) và 21(b) lần lượt cho thấy tỷ lệ giảm "
      "dịch chuyển và gia tốc của các kết cấu có chu kỳ khác nhau. Có thể thấy "
      "rằng khi tỷ số giữa chu kỳ kết cấu hiện tại (T) và chu kỳ kết cấu thiết "
      "kế (T1) nằm trong khoảng 0,85–1,4, hiệu quả giảm chấn tương đối ổn định, "
      "tỷ lệ giảm RMS dịch chuyển duy trì trên 16% và tỷ lệ giảm đỉnh dịch "
      "chuyển trên 9%. Khi chu kỳ kết cấu (T) vượt quá 1,4T1, hiệu quả kiểm soát "
      "của kết cấu bước vào giai đoạn suy giảm đáng kể, nhưng tỷ lệ giảm RMS và "
      "tỷ lệ giảm đỉnh của dịch chuyển vẫn được duy trì. Đáng chú ý, sự thay đổi "
      "chu kỳ kết cấu ít ảnh hưởng đến tỷ lệ giảm gia tốc. Nhìn chung, khi chu "
      "kỳ kết cấu lệch khỏi chu kỳ thiết kế ban đầu, hoặc khi kết cấu chịu động "
      "đất có cường độ hiếm gặp, sự hiện diện của CBD trên kết cấu vẫn tiếp tục "
      "phát huy tác dụng, duy trì một mức độ ổn định động đất nhất định.",
      "Under the combined influence of construction, lifecycle, and "
      "environmental factors associated with coal-fired power plant structures, "
      "the dynamic characteristics of the existing structure will differ from "
      "those of the originally designed structure. Furthermore, when the "
      "structure is subjected to a strong earthquake, it will experience damage "
      "and a subsequent decrease in stiffness. This will lead to a deviation "
      "between the real structural response cycle and the designed structural "
      "response cycle, which will, in turn, influence the vibration control "
      "effect of the CBDs. To determine the influence of the structural period "
      "change on the reduction rate provided by the CBDs, the vibration "
      "reduction effect on structures with different periods, designed using "
      "initially optimized parameters, was analyzed. The structural period "
      "change was simulated by changing the elastic modulus parameters of the "
      "material in the model. Figures 21(a) and 21(b) show the displacement and "
      "acceleration reduction rates, respectively, of structures with different "
      "periods. It can be seen that when the ratio of the current structure "
      "period (T) to the design structure period (T1) is within the range of "
      "0.85–1.4, the reduction effect is relatively stable, the displacement RMS "
      "reduction rate is maintained above 16%, and the displacement peak "
      "reduction rate is above 9%. When the structure period (T) exceeds 1.4T1, "
      "the control effect of the structure enters a period of significant "
      "decline, but the displacement RMS and the peak reduction rates are still "
      "maintained. Notably, the structural period change has little influence "
      "on the acceleration reduction rate. Overall, when the structure period "
      "deviates from the initial design period, or the structure is subjected "
      "to earthquakes of rare intensity, the presence of CBDs on a structure "
      "can continue to work to maintain a certain degree of seismic stability.")
    FIG(b, 21, F.fig_f21(), lang)

    # ------------------------------------------------------------- CONCLUSION
    H(b, lang, "KẾT LUẬN", "CONCLUSION", level=2)
    P(b, lang,
      "Trong tương lai gần, các nhà máy điện than sẽ tiếp tục chiếm vị trí quan "
      "trọng trên thị trường phát điện. Tuy nhiên, nhiều nhà máy điện than "
      "trọng yếu trong và ngoài nước nằm trong vùng dễ xảy ra động đất. Xét đến "
      "sự phức tạp riêng biệt của các kết cấu nhà máy này, việc đảm bảo an toàn "
      "động đất cho chúng là rất quan trọng. Vì mục đích này, các phễu than "
      "khối lớn có thể được thiết kế để đóng vai trò là bộ giảm chấn phễu than, "
      "biến bất lợi về khối lượng lớn thành lợi thế trong việc giảm dao động "
      "động đất. Trong bài báo này, một phương pháp tối ưu để thiết kế thông số "
      "CBD được thiết lập dựa trên lý thuyết giảm chấn MTMD, và hiệu quả giảm "
      "rung cũng như đóng góp của chúng vào độ ổn định động đất của kết cấu nhà "
      "máy điện than được nghiên cứu bằng cả thí nghiệm bàn rung và mô phỏng số "
      "phần tử hữu hạn. Các kết luận chính như sau:",
      "Coal-fired power plants will continue occupy a significant place in the "
      "electricity generation market for the foreseeable future. However, many "
      "critical domestic and foreign coal-fired power plants are prone to "
      "earthquakes. Considering the unique complexity of these plant structures, "
      "it is important to ensure their seismic safety. To this end, massive "
      "coal buckets can be designed to act as coal bucket dampers, turning the "
      "disadvantage of high mass into an advantage in damping seismic "
      "vibrations. In this paper, an optimized method for designing CBD "
      "parameters is established based on MTMD damping theory, and their "
      "vibration reduction effects and contributions to the seismic stability "
      "of a coal-fired power plant structure are studied using both shaking "
      "table tests and finite element numerical simulations. The main "
      "conclusions are as follows:")

    L(b, lang,
      ["Việc thiết kế tối ưu thông số CBD cho kết cấu nhà máy điện than có thể "
       "thực hiện theo lý thuyết MTMD. CBD với các thông số tối ưu thể hiện hiệu "
       "quả kiểm soát rung tốt đối với phản ứng dịch chuyển của kết cấu nhà máy "
       "điện than. Đồng thời, hiệu quả kiểm soát gia tốc trên tầng lắp đặt CBD "
       "và các tầng phía trên cho kết quả tốt, trong khi ở các tầng thấp hơn lại "
       "kém. Nhìn chung, hiệu năng động đất của kết cấu trang bị CBD được đánh "
       "giá trong nghiên cứu này thúc đẩy tiềm năng ứng dụng kỹ thuật của công "
       "nghệ, và phương án CBD được áp dụng trong nghiên cứu cung cấp tài liệu "
       "tham khảo tốt cho thiết kế kỹ thuật thực tế.",
       "Phản ứng động đất của kết cấu trang bị CBD dưới các sóng động đất khác "
       "nhau thể hiện sự phân tán nhất định. Trong điều kiện cộng hưởng, tức là "
       "khi phản ứng của kết cấu mạnh, CBD hoạt động hiệu quả để kiểm soát rung. "
       "Tuy nhiên, CBD kém hữu ích bên ngoài điều kiện cộng hưởng, dù phản ứng "
       "của kết cấu trong trường hợp này là nhỏ. Nhìn chung, việc áp dụng CBD để "
       "cải thiện hiệu năng động đất của kết cấu nhà máy điện có tính phổ quát "
       "nhất định, bất kể thiết kế cụ thể của nhà máy.",
       "Khi chu kỳ kết cấu lệch khỏi chu kỳ thiết kế, dù do thay đổi kết cấu, "
       "yếu tố môi trường hay hư hỏng do động đất mạnh, kết cấu trang bị CBD "
       "vẫn duy trì được một mức độ giảm chấn nhất định so với kết cấu truyền "
       "thống, cho thấy kết cấu nhà máy điện than trang bị CBD có thể duy trì "
       "khả năng giảm chấn bền vững ngay cả khi chu kỳ kết cấu thay đổi."],
      ["The parameter optimization design of CBDs for coal-fired power plant "
       "structures can be conducted according to MTMD theory. The CBDs with "
       "optimized parameters exhibit good vibration control effects on the "
       "displacement response of a coal-fired power plant structure. At the "
       "same time, the acceleration control effect on the story containing the "
       "CBDs and the floors above shows good results, while that of the lower "
       "stories is poor. Overall, the seismic performance of the CBD-equipped "
       "structure evaluated in this research advances the potential engineering "
       "applications of this technology, and the CBD scheme adopted in this "
       "study provides a good reference for practical engineering design.",
       "The seismic response of a CBD-equipped structure under different "
       "seismic waves shows a certain discreteness. Under resonant conditions, "
       "that is, when the structural response is intense, the CBDs operate "
       "efficiently to provide vibration control. However, CBDs are less useful "
       "outside the resonant conditions, though the structural response is "
       "small in this situation. As a whole, the application of CBDs to improve "
       "the seismic performance of a power plant structure has a certain "
       "universal quality, regardless of the specific design of the plant.",
       "When the structural period deviates from the design period, whether "
       "because of structural changes, environmental factors, or damage from "
       "strong earthquakes, the CBD-equipped structure can maintain a certain "
       "damping effect compared to a more traditional structure, demonstrating "
       "that a CBD-equipped coal-fired power plant structure can maintain "
       "robust damping behavior even when the structural period changes."],
      ordered=True)

    P(b, lang,
      "Khi áp dụng phương pháp tối ưu được trình bày chi tiết trong bài báo này, "
      "phản ứng động đất của các nhà máy điện than trang bị CBD được cải thiện "
      "rõ rệt. Phản ứng kiểm soát của kết cấu dưới các sóng động đất khác nhau "
      "thể hiện sự phân tán nhất định. Một mặt, điều này là do đặc tính kiểm "
      "soát rung của TMD. Mặt khác, điều này là do lựa chọn bỏ qua kiểm soát các "
      "phương thức rung bậc cao. Xét các khía cạnh này, nghiên cứu tương lai sẽ "
      "hướng đến đạt được hiệu quả giảm chấn tốt hơn bằng kiểm soát đa phương "
      "thức của kết cấu trang bị CBD.",
      "When applying the optimization method detailed in this article, the "
      "seismic response of coal-fired power plants equipped with CBDs is "
      "obviously improved. The control response of the structure under "
      "different seismic waves exhibits a certain discreteness. On one hand, "
      "this is because of the characteristics of TMD vibration control. On the "
      "other hand, this is due to the choice to ignore the control of high-order "
      "vibration modes. Considering these aspects, future research will involve "
      "achieving an improved damping effect using the multimode control of the "
      "CBD-equipped structure.")

    # -------------------------------------------------------- ACKNOWLEDGMENTS
    H(b, lang, "LỜI CẢM ƠN", "ACKNOWLEDGMENTS", level=2)
    P(b, lang,
      "Nghiên cứu này được hỗ trợ bởi khoản tài trợ số 51478023 của Quỹ Khoa học "
      "Tự nhiên Quốc gia Trung Quốc.",
      "This research was supported by Grant no. 51478023 from the National "
      "Natural Science Foundation of China.")

    # ------------------------------------------------------------- REFERENCES
    H(b, lang, "TÀI LIỆU THAM KHẢO", "REFERENCES", level=2)
    REFS(b, lang, _REFS_ITEMS)

    return b
