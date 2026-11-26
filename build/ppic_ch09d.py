# -*- coding: utf-8 -*-
"""Book 9, Chapter 9 (part D) - RESULTS (EN/VI bilingual).

Source: Kisic, Durovic and Petrovic, in L. N. Jalali (ed.), *Handbook on Power
Plant Instrumentation and Control* (Bibliotex, 2019), absolute lines 5991-6165
of ``work/ppic_raw.txt`` (PDF pp. 232-237, printed pp. 216-221). Covers the
Q-Q plot (Figure 6), the Hotelling T2 control charts at 2, 5 and 8 weeks
(Figures 7-9), Table 2 (points above the UCL for four alpha levels), the
estimated probability densities (Figure 10) and the HMM state sequence
(Figure 11). Printed bracketed citations [26] and [29] are kept inline; the
reference list itself is emitted by part E. Figures/tables are embedded as
9.6-9.11 and 9.2; captions come from the figure supplier when present.
"""
import ppicfig9 as F
from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401


def _stub(n, cap_vi, cap_en, desc_vi, desc_en, detail):
    """Minimal inert five-tuple, used only while the supplier is unfinished."""
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 300" '
           'role="img" aria-label="Figure 9.%d">'
           '<rect x="8" y="8" width="664" height="284" fill="none" '
           'stroke="#888888"/>'
           '<text x="340" y="132" text-anchor="middle" font-size="15">'
           'Figure 9.%d</text>'
           '<text x="340" y="162" text-anchor="middle" font-size="11">%s</text>'
           '</svg>') % (n, n, detail)
    return (svg, cap_vi, cap_en, desc_vi, desc_en)


if not hasattr(F, "fig_f06"):
    F.fig_f06 = lambda: _stub(
        6, "Hình 9.6 · Đồ thị Q-Q cho tín hiệu âm thanh ghi sau 6 ngày thay bàn nghiền",
        "Figure 9.6 · Q-Q plot for the acoustic signal recorded 6 days after grinding table replacement",
        "Đồ thị Q-Q: trục hoành là phân vị chi bình phương (0-28), trục tung là phân vị T² (0-27); các điểm nằm gần đường 45°.",
        "Q-Q plot: chi-squared quantiles on the x-axis (0-28), T2 quantiles on the y-axis (0-27); the points follow the 45 degree line.",
        "Q-Q plot: chi-squared quantiles (x) vs T2 quantiles (y); 45 degree line")
if not hasattr(F, "fig_f07"):
    F.fig_f07 = lambda: _stub(
        7, "Hình 9.7 · Biểu đồ kiểm soát T² cho tín hiệu ghi sau 2 tuần thay bàn nghiền",
        "Figure 9.7 · T2 control chart for acoustic signal recorded 2 weeks after grinding table replacement",
        "Biểu đồ kiểm soát T² sau 2 tuần: trục hoành Sample từ 0 đến 600, trục tung T² statistic từ 0 đến 80, đường UCL = 36,12.",
        "T2 control chart at 2 weeks: Samples 0-600 on the x-axis, T2 statistic 0-80 on the y-axis, UCL = 36.12.",
        "T2 chart: 2 weeks; Samples 0-600; T2 statistic 0-80; UCL = 36.12")
if not hasattr(F, "fig_f08"):
    F.fig_f08 = lambda: _stub(
        8, "Hình 9.8 · Biểu đồ kiểm soát T² cho tín hiệu ghi sau 5 tuần thay bàn nghiền",
        "Figure 9.8 · T2 control chart for acoustic signal recorded 5 weeks after grinding table replacement",
        "Biểu đồ kiểm soát T² sau 5 tuần: trục hoành Sample từ 0 đến 600, trục tung T² statistic từ 0 đến 120, đường UCL = 36,12.",
        "T2 control chart at 5 weeks: Samples 0-600 on the x-axis, T2 statistic 0-120 on the y-axis, UCL = 36.12.",
        "T2 chart: 5 weeks; Samples 0-600; T2 statistic 0-120; UCL = 36.12")
if not hasattr(F, "fig_f09"):
    F.fig_f09 = lambda: _stub(
        9, "Hình 9.9 · Biểu đồ kiểm soát T² cho tín hiệu ghi sau 8 tuần thay bàn nghiền",
        "Figure 9.9 · T2 control chart for acoustic signal recorded 8 weeks after grinding table replacement",
        "Biểu đồ kiểm soát T² sau 8 tuần: trục hoành Sample từ 0 đến 600, trục tung T² statistic từ 0 đến 180, gần như mọi điểm đều vượt UCL = 36,12.",
        "T2 control chart at 8 weeks: Samples 0-600 on the x-axis, T2 statistic 0-180 on the y-axis; nearly all points exceed UCL = 36.12.",
        "T2 chart: 8 weeks; Samples 0-600; T2 statistic 0-180; UCL = 36.12")
if not hasattr(F, "fig_f10"):
    F.fig_f10 = lambda: _stub(
        10, "Hình 9.10 · Các hàm mật độ xác suất ước lượng cho tín hiệu ghi sau 2, 5 và 8 tuần thay bàn nghiền",
        "Figure 9.10 · Estimated probability density functions for signals recorded 2, 5 and 8 weeks after grinding table replacement",
        "Ba hàm mật độ ước lượng: trục hoành Data từ -50 đến 200, trục tung Density từ 0 đến 0,08; đường đỏ (2 tuần), xanh lá (5 tuần), đen (8 tuần).",
        "Three estimated densities: Data -50 to 200 on the x-axis, Density 0 to 0.08 on the y-axis; red (2 weeks), green (5 weeks), black (8 weeks).",
        "Estimated densities: Data -50..200; Density 0..0.08; 2/5/8 weeks")
if not hasattr(F, "fig_f11"):
    F.fig_f11 = lambda: _stub(
        11, "Hình 9.11 · Các trạng thái HMM",
        "Figure 9.11 · HMM states",
        "Hai đồ thị xếp chồng: chuỗi quan sát (Số mẫu 0-1800, Quan sát 0-80) và các trạng thái HMM 1, 2, 3 theo số mẫu.",
        "Two stacked panels: the observation sequence (Number of samples 0-1800, Observations 0-80) and HMM states 1, 2, 3 versus number of samples.",
        "Sequence of observations (0-1800 samples) and HMM states 1, 2, 3")


# Printed column order (PDF p. 235): date, weeks after replacement, and four
# point-count columns for alpha = 0.001 / 0.005 / 0.01 / 0.025.
_T2_HEAD_VI = [
    "Ngày ghi",
    "Số tuần sau khi thay bàn nghiền",
    "Số điểm nằm trên UCL (%), α = 0,001, UCL = 36,12",
    "Số điểm nằm trên UCL (%), α = 0,005, UCL = 31,32",
    "Số điểm nằm trên UCL (%), α = 0,01, UCL = 29,14",
    "Số điểm nằm trên UCL (%), α = 0,025, UCL = 26,12",
]
_T2_HEAD_EN = [
    "Date of recording",
    "Number of weeks after grinding table replacement",
    "Number of points above UCL (%), α = 0.001, UCL = 36.12",
    "Number of points above UCL (%), α = 0.005, UCL = 31.32",
    "Number of points above UCL (%), α = 0.01, UCL = 29.14",
    "Number of points above UCL (%), α = 0.025, UCL = 26.12",
]
_T2_ROWS_VI = [
    ["2 tháng 2 năm 2012", "2 tuần", "1,43%", "2,14%", "2,46%", "5%"],
    ["24 tháng 2 năm 2012", "5 tuần", "68,27%", "79,5%", "83,78%", "88,41%"],
    ["15 tháng 3 năm 2012", "8 tuần", "84,85%", "90,91%", "92,87%", "95,54%"],
    ["5 tháng 4 năm 2012", "2 tuần", "16,75%", "27,63%", "32,98%", "43,14%"],
    ["19 tháng 4 năm 2012", "4 tuần", "57,58%", "70,05%", "74,87%", "81,64%"],
]
_T2_ROWS_EN = [
    ["2 February 2012", "2 weeks", "1.43%", "2.14%", "2.46%", "5%"],
    ["24 February 2012", "5 weeks", "68.27%", "79.5%", "83.78%", "88.41%"],
    ["15 March 2012", "8 weeks", "84.85%", "90.91%", "92.87%", "95.54%"],
    ["05 April 2012", "2 weeks", "16.75%", "27.63%", "32.98%", "43.14%"],
    ["19 April 2012", "4 weeks", "57.58%", "70.05%", "74.87%", "81.64%"],
]


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 9."""
    b = []

    H(b, lang, "KẾT QUẢ", "RESULTS", level=2)

    P(b, lang,
      "Trong chương này, kết quả thu được sau khi áp dụng kỹ thuật đề xuất cho "
      "bài toán bảo trì dự báo đã mô tả tại nhà máy nhiệt điện sẽ được trình "
      "bày. Như đã giải thích trước đó, sau khi thu thập dữ liệu và trích xuất "
      "đặc trưng từ các tín hiệu âm thanh ghi âm, các biểu đồ kiểm soát T² "
      "được thiết lập.",
      "In this chapter, the results obtained after applying the proposed "
      "technique for predictive maintenance to the described problem at the "
      "thermoelectric power plant will be presented. As was explained "
      "previously, after data acquisition and feature extraction from the "
      "recorded acoustic signals, T² control charts are formed.")

    P(b, lang,
      "Tín hiệu âm thanh ghi ngày 30 tháng 3 năm 2012 được dùng để ước lượng "
      "X̄ và S trong các phương trình (6) và (7), với kiến thức rằng một bàn "
      "nghiền mới đang vận hành. Theo cách này, tín hiệu này được xem như một "
      "tập dữ liệu lịch sử. Đây chính là Giai đoạn I của kiểm soát thống kê, "
      "khi toàn bộ hệ thống nghiền than nằm trong trạng thái kiểm soát thống "
      "kê. Các giá trị ước lượng của X̄ và S ở Giai đoạn I được dùng ở Giai "
      "đoạn II của phân tích đa biến. Giới hạn kiểm soát chi bình phương được "
      "lấy làm UCL, như trong phương trình (8). Với 14 đặc tính chất lượng, "
      "UCL = 36,12 (ứng với giá trị α = 0,001) và LCL = 0. Để chứng minh việc "
      "sử dụng giới hạn kiểm soát chi bình phương là hợp lý, Hình 9.6 trình "
      "bày đồ thị Q-Q [29] với các phân vị T² trên trục tung và các phân vị "
      "chi bình phương trên trục hoành. Để minh họa, đồ thị Q-Q của các giá "
      "trị T² được cho đối với tín hiệu ghi ngày 30 tháng 3 năm 2012, tức là "
      "tín hiệu ghi sau 6 ngày thay bàn nghiền. Trong quá trình nghiên cứu, "
      "phép kiểm tra này được thực hiện cho tất cả các tín hiệu nhằm xác nhận "
      "rằng lựa chọn giới hạn kiểm soát chi bình phương là hợp lý.",
      "The acoustic signal recorded on 30 March 2012 was used for the "
      "estimation of X̄ and S in Eqs. (6) and (7), knowing that a new grinding "
      "table was operational. In this way, this signal was observed as a "
      "historical data set. This was in effect Phase I of statistical control, "
      "where the entire coal-grinding subsystem was under statistical control. "
      "The estimated values of X̄ and S in Phase I were to be used in Phase II "
      "of the multivariate analysis. The chi-squared control limit was taken "
      "as the UCL, as in Eq. (8). For the 14 quality characteristics, UCL = "
      "36.12 (for the value α = 0.001) and LCL = 0. In order to justify the "
      "use of the chi-squared control limit, Figure 6 shows a Q-Q plot [29] "
      "with T² quantiles on the y-axis and chi-squared quantiles on the "
      "x-axis. For illustration, the Q-Q plot of T² values is shown for the "
      "signal recorded on 30 March 2012, that is, for the signal recorded "
      "6 days after grinding table replacement. During the research, this "
      "check was done for all the signals in order to confirm that the choice "
      "of the chi-squared control limit is justified.")
    FIG(b, 6, F.fig_f06(), lang)

    P(b, lang,
      "Từ Hình 9.6 có thể thấy các giá trị tuân theo phân phối chi bình "
      "phương, tức là hình vẽ cho thấy xu hướng tuyến tính xấp xỉ dọc theo "
      "đường 45°, ngoại trừ vài điểm cuối hơi lệch khỏi đường xu hướng dự kiến. "
      "Trước khi các biểu đồ kiểm soát T² được xây dựng, chúng tôi kỳ vọng số "
      "điểm ngoại lệ sẽ tăng lên khi bàn nghiền trở nên mòn hơn.",
      "From Figure 6, we can see that the values follow a chi-squared "
      "distribution, that is, the figure shows an approximately linear trend "
      "along the line of 45°, except the last few points which are slightly "
      "away from the projected trend line. Before the T² control charts were "
      "constructed, we expected that the number of outliers would increase as "
      "the grinding tables become worn out.")

    P(b, lang,
      "Hình 9.7 [26] trình bày biểu đồ kiểm soát T² cho tín hiệu âm thanh ghi "
      "ngày 2 tháng 2 năm 2012, tức 2 tuần sau khi thay bàn nghiền.",
      "Figure 7 [26] shows the T² control chart for the acoustic signal "
      "recorded on 2 February 2012, 2 weeks after grinding table replacement.")
    FIG(b, 7, F.fig_f07(), lang)

    P(b, lang,
      "Hình 9.8 [26] trình bày biểu đồ kiểm soát đa biến T² cho tín hiệu âm "
      "thanh ghi ngày 24 tháng 2 năm 2012, tức 5 tuần sau khi thay bàn nghiền.",
      "Figure 8 [26] shows the T² multivariate control chart for the acoustic "
      "signal recorded on 24 February 2012, 5 weeks after grinding table "
      "replacement.")
    FIG(b, 8, F.fig_f08(), lang)

    P(b, lang,
      "Hình 9.9 [26] trình bày biểu đồ kiểm soát T² cho tín hiệu âm thanh ghi "
      "ngày 15 tháng 3 năm 2012, tức 8 tuần sau khi thay bàn nghiền.",
      "Figure 9 [26] shows the T² control chart for the acoustic signal "
      "recorded on 15 March 2012, 8 weeks after grinding table replacement.")
    FIG(b, 9, F.fig_f09(), lang)

    P(b, lang,
      "Từ các Hình 9.7–9.9 rõ ràng là số điểm nằm trên UCL trên biểu đồ kiểm "
      "soát T² tăng lên khi bàn nghiền ngày càng mòn. Sau 8 tuần kể từ khi thay "
      "thế, gần như tất cả các điểm đều vượt quá UCL. Để xác nhận kết quả, "
      "phân tích đa biến được lặp lại với các tín hiệu ghi ngày 5 và 19 tháng "
      "4 năm 2012. Bảng 9.2 cho biết số chính xác các điểm ngoại lệ của tất cả "
      "các tín hiệu đã ghi đối với các giá trị UCL khác nhau (tức là các giá "
      "trị α khác nhau).",
      "It is apparent from Figures 7–9 that the number of points above the "
      "UCL on the T² control chart grew as the grinding table became "
      "increasingly worn. Eight weeks after replacement, nearly all the "
      "points were beyond the UCL. To confirm the results, the multivariate "
      "analysis was repeated using the signals recorded on 5 and 19 April "
      "2012. Table 2 shows the exact number of outliers for all the recorded "
      "signals for the different values of UCL (i.e. for different values of "
      "α).")

    P(b, lang,
      "Sự khác biệt về số điểm nằm trên UCL giữa các tín hiệu ghi ngày 2 "
      "tháng 2 và 19 tháng 4 năm 2012 có thể được giải thích. Cụ thể, cả hai "
      "tín hiệu đều được thu sau 2 tuần kể từ khi thay bàn nghiền, nhưng kết "
      "quả lại khác nhau vì hai lý do: (1) Điều kiện thu tín hiệu không lý "
      "tưởng do nhiễu. Tất cả các tín hiệu ghi được đều chịu ảnh hưởng của "
      "nhiễu này, cũng như của các nhiễu loạn khác (ví dụ khi một cục than "
      "lớn hoặc đá va vào máy nghiền). Các tín hiệu không được lọc, vì có thể "
      "mất thông tin. Tất cả những yếu tố này có thể đã ảnh hưởng đến độ "
      "chính xác của kết quả. (2) Độ mòn của bàn nghiền phụ thuộc vào chất "
      "lượng than và vào chất lượng của chính bàn nghiền. Vì vậy, không thể "
      "xác định thời điểm đúng để thay bàn nghiền trừ khi toàn bộ hệ thống "
      "con được dừng lại và mở ra để kiểm tra trực quan.",
      "The difference in the number of points above the UCL for the signals "
      "recorded on 2 February and 19 April 2012 can be explained. Namely, "
      "both signals were acquired 2 weeks after grinding table replacement, "
      "but the results are different for two reasons: (1) The signal "
      "acquisition conditions were not ideal because of noise. All the "
      "recorded signals reflect this noise, as well as other disturbances "
      "(e.g. when a large chunk of coal or stone hits the mill). The signals "
      "were not filtered, because of the possible information loss. All this "
      "could have influenced the accuracy of the results. (2) Grinding table "
      "wear depends on the quality of the coal and of the grinding table "
      "itself. It is therefore impossible to ascertain what the right time "
      "for grinding table replacement would be, unless the entire subsystem "
      "is shut down and opened for visual inspection.")

    P(b, lang,
      "Theo Bảng 9.2, có thể kết luận rằng với lựa chọn α = 0,001, biểu đồ "
      "kiểm soát được xây dựng bị kiểm soát quá mức, trong khi với lựa chọn "
      "α = 0,025, tỷ lệ báo động giả lại quá lớn. Dù chọn giá trị UCL nào, số "
      "điểm ngoại lệ vẫn lớn hơn khi bàn nghiền càng mòn. Cụ thể, trong "
      "phương pháp đề xuất, các biểu đồ kiểm soát không được dùng để phát "
      "hiện lỗi theo cách cổ điển, mà để hình thành các thống kê T² sẽ được "
      "tham số hóa nhằm tạo ra các quan sát cho HMM. Việc lựa chọn UCL không "
      "ảnh hưởng đến giá trị thống kê T², tức là đến việc hình thành các quan "
      "sát cho HMM. Do đó, việc lựa chọn α, tức là sự thỏa hiệp giữa sai loại "
      "một và sai loại hai, không ảnh hưởng đến giá trị quan sát của HMM — "
      "điều mà thường không đúng khi biểu đồ kiểm soát cổ điển cần phát hiện "
      "lỗi và khi việc lựa chọn α có ảnh hưởng lớn đến việc xác định đúng UCL.",
      "According to Table 2, we can conclude that with the choice of "
      "parameter α = 0.001, an ‘over controlling’ control chart is "
      "constructed, while with the choice of parameter α = 0.025, the false "
      "alarm rate is too large. Anyway, no matter which value of the UCL we "
      "have chosen, the number of outliers is larger as the grinding tables "
      "are getting worn out. Namely, in the proposed method the control "
      "charts were not used for classical fault detection, yet for forming "
      "the T² statistics that will be parameterized for making the HMM "
      "observations. The choice of the UCL does not have an influence on the "
      "T² statistics value, that is, on forming the observations for the HMM. "
      "Thus, the choice of parameter α, that is, making a compromise between "
      "the first type error and the second type error, does not have an "
      "influence on the observation values for the HMM, which is not usually "
      "the case when a classical control chart needs to detect the fault and "
      "when the choice of parameter α has a large influence on the correct "
      "determination of the UCL.")

    TBL(b, lang, _T2_HEAD_VI, _T2_HEAD_EN,
        _T2_ROWS_VI if lang == "vi" else _T2_ROWS_EN,
        caption_vi="Bảng 9.2 · Số điểm nằm trên UCL.",
        caption_en="Table 9.2 · Number of points above UCL.")

    P(b, lang,
      "Sau khi các biểu đồ kiểm soát T² được xây dựng, lượng hóa vectơ được "
      "thực hiện như đã mô tả ở mục trước, nhằm biểu diễn các mẫu trên biểu "
      "đồ kiểm soát thành một chuỗi các quan sát cho HMM. Hình 9.10 [26] cho "
      "thấy các hàm mật độ xác suất ước lượng của các mẫu trên biểu đồ kiểm "
      "soát T² đối với các tín hiệu ghi sau 2, 5 và 8 tuần kể từ khi thay bàn "
      "nghiền. Rõ ràng là các thống kê T² thay đổi theo thời gian và là hàm "
      "của tình trạng của bàn nghiền (tức là chúng thay đổi khi tình trạng "
      "của bàn nghiền thay đổi).",
      "After the T² control charts were constructed, vector quantization was "
      "undertaken, as described in the previous section, in order to "
      "represent the control chart samples as a sequence of observations for "
      "the HMM. Figure 10 [26] shows the estimated probability density "
      "functions of the T² control chart samples for the signals recorded "
      "2, 5 and 8 weeks after grinding table replacement. It is apparent "
      "that the T² statistics change over time and that they are a function "
      "of the condition of the grinding table (i.e. they change as the "
      "condition of the grinding table changes).")
    FIG(b, 10, F.fig_f10(), lang)

    P(b, lang,
      "Bước cuối cùng của thuật toán đề xuất là xây dựng HMM. Các trạng thái "
      "của HMM được chọn sao cho phản ánh tình trạng vật lý của bàn nghiền. "
      "Để minh họa phương pháp, người ta giả sử HMM có ba trạng thái. Trạng "
      "thái thứ nhất là tình trạng của bàn nghiền ngay sau khi thay thế (tức "
      "là bàn nghiền mới). Với việc ghi nhớ rằng thời gian sử dụng trung bình "
      "của bàn nghiền là khoảng 1600 giờ, việc HMM ở trạng thái thứ nhất có "
      "thể được hiểu là bàn nghiền đang ở trong một phần ba đầu của vòng đời. "
      "Trạng thái thứ hai là trạng thái trung gian, khi bàn nghiền đã mòn một "
      "phần nhưng vẫn còn thời gian trước khi cần thay thế. Do đó, hệ thống "
      "ở trạng thái thứ hai được hiểu là bàn nghiền bước vào phần ba thứ hai "
      "của vòng đời. Trạng thái thứ ba có nghĩa là tình trạng bàn nghiền đã "
      "xấu đi đến mức cần thay thế. Cần nói rằng nghiên cứu này bắt đầu từ "
      "giả định HMM chỉ có ba trạng thái, nhưng nếu cần đặc trưng chính xác "
      "hơn tình trạng bàn nghiền thì có thể tăng số trạng thái. Hình 9.11 "
      "[26] cho thấy chuỗi các quan sát và các trạng thái HMM tương ứng.",
      "The final step of the proposed algorithm was to construct the HMM. "
      "The states of the HMM are chosen so as to represent the physical "
      "condition of the mill-grinding plates. In order to illustrate the "
      "proposed method, it is assumed that the HMM has three states. The "
      "first state is the condition of the grinding table immediately after "
      "replacement (i.e. that of a new grinding table). Having in mind that "
      "the average length of mill-grinding table duration is approximately "
      "1600 h, the fact that the HMM is in the first state could be "
      "interpreted as the grinding tables being in the first third of their "
      "life. The second state was the ‘intermediate state’, where the "
      "grinding table becomes partially worn out, but there is still time "
      "before replacement is needed. Consequently, the system staying in the "
      "second state can be interpreted as the grinding tables entering the "
      "second third of their lifetime. The third state means that the "
      "condition of the grinding table had deteriorated to the point where "
      "replacement is necessary. Namely, this research started from the "
      "assumption that the HMM has only three states, but if it is needed "
      "that the grinding table conditions are characterized with greater "
      "precision, the number of states could be increased. Figure 11 [26] "
      "shows the sequence of observations and corresponding HMM states.")
    FIG(b, 11, F.fig_f11(), lang)

    P(b, lang,
      "Từ Hình 9.11 rõ ràng là HMM cung cấp thông tin về sự thay đổi tình "
      "trạng của bàn nghiền. Hiển nhiên là thời điểm HMM chuyển vào trạng "
      "thái thứ ba (bàn nghiền đã mòn) trùng với sự bắt đầu của các quan sát "
      "tương ứng với các mẫu trên biểu đồ kiểm soát đối với tín hiệu ghi sau "
      "8 tuần kể từ khi thay thế.",
      "It is apparent from Figure 11 that the HMM provides information about "
      "a change in the condition of the grinding table. It is obvious that "
      "the time of HMM entry into the third state (worn-out grinding table) "
      "coincides with the beginning of observations that correspond to the "
      "control chart samples for the signal recorded 8 weeks after "
      "replacement.")

    return b
