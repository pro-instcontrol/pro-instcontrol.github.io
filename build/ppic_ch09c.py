# -*- coding: utf-8 -*-
"""Chapter 9, span C - proposed predictive-maintenance technique.

Source: work/ppic_raw.txt lines 5746-5990, PDF pp. 223-231, printed pp. 207-215.
Table 1, Figures 3-5 and the mathematical expressions were re-read from the
page renders p224.png ... p230.png because the PDF text layer scatters the
symbols. Equations are emitted unnumbered, as required by the chapter brief.

Only this module is modified; figure suppliers are never overwritten.
"""
import ppicfig9 as F
from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401


# --------------------------------------------------------------------------
# Non-overwriting figure fallbacks.  A real supplier callable always wins.
# --------------------------------------------------------------------------
def _stub_tuple(n, topic, cvi, cen, avi, aen):
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 300" role="img">'
        '<rect x="1" y="1" width="678" height="298" fill="#f4f6fa" stroke="#9aa7bd"/>'
        '<text x="340" y="140" text-anchor="middle" '
        'style="font:17px Helvetica,sans-serif;fill:#24364f">Figure 9.%d</text>'
        '<text x="340" y="168" text-anchor="middle" '
        'style="font:12px Helvetica,sans-serif;fill:#5a6b82">%s</text>'
        '</svg>' % (n, topic)
    )
    return (svg, cvi, cen, avi, aen)


if not hasattr(F, "fig_f03"):
    F.fig_f03 = lambda: _stub_tuple(
        3, "Spectrogram of an acoustic signal",
        "Hình 9.3 · Phổ đồ của tín hiệu âm thanh.",
        "Figure 9.3 · Spectrogram of an acoustic signal.",
        "Phổ đồ của tín hiệu âm thanh ghi sau khi thay bàn nghiền 6 ngày.",
        "Spectrogram of the acoustic signal recorded six days after grinding "
        "table replacement.")
if not hasattr(F, "fig_f04"):
    F.fig_f04 = lambda: _stub_tuple(
        4, "Hidden Markov model with three states",
        "Hình 9.4 · Mô hình Markov ẩn với ba trạng thái.",
        "Figure 9.4 · Hidden Markov model with three states.",
        "Ba trạng thái ẩn được nối với nhau bởi các xác suất chuyển.",
        "Three hidden states linked by transition probabilities.")
if not hasattr(F, "fig_f05"):
    F.fig_f05 = lambda: _stub_tuple(
        5, "Offline and online procedure of the proposed algorithm",
        "Hình 9.5 · Lưu đồ thuật toán đề xuất: thủ tục ngoại tuyến và trực tuyến.",
        "Figure 9.5 · Flow diagram of the proposed algorithm: offline and "
        "online procedures.",
        "Lưu đồ gồm thủ tục ngoại tuyến ở bên trái và thủ tục trực tuyến ở bên phải.",
        "Flow diagram with the offline procedure at left and the online "
        "procedure at right.")


# --------------------------------------------------------------------------
# Equations (transcribed from the page renders; printed form preserved).
# --------------------------------------------------------------------------
_EQ_SP = "S<sub>p</sub> = STFFT{y[n]} = S<sub>p</sub>[f, n]"
_EQ_FP = ("f<sub>p</sub> = [14  18.7  23.4  28.1  32.8  60.93  126.5  "
          "178.1  187.5  262.5  346.8  754.6  1200  2025]")
_EQ_X = ("X[n] = [x<sub>1</sub>[n]   x<sub>2</sub>[n]   …   "
         "x<sub>14</sub>[n]]<sup>T</sup>")
_EQ_XI = ("x<sub>i</sub>[n] = Σ<sub>j=n−L<sub>w</sub></sub><sup>n</sup> "
          "S<sub>p</sub>[f<sub>i</sub>, j]")
_EQ_T2 = ("T<sup>2</sup>[n] = (X[n] − X̄)<sup>T</sup> S<sup>−1</sup> "
          "(X[n] − X̄)")
_EQ_MEAN = "X̄ = (1/N) Σ<sub>i=0</sub><sup>N−1</sup> X[i]"
_EQ_COV = ("S = (1/(N − 1)) Σ<sub>i=0</sub><sup>N−1</sup> "
           "(X[i] − X̄)(X[i] − X̄)<sup>T</sup>")
_EQ_UCL2 = "UCL = χ<sup>2</sup><sub>(α,p)</sub>, LCL = 0"
_EQ_UCLB = ("UCL = [(n − 1)<sup>2</sup>/n] "
            "β<sub>(α;p/2,(n−p−1)/2)</sub>, LCL = 0")
_EQ_O = ("O[n] = [T<sup>2</sup>[n − 9]   T<sup>2</sup>[n − 8]   …   "
         "T<sup>2</sup>[n]]<sup>T</sup>")
_EQ_Q = ("min<sub>i</sub> ‖O[n] − C<sub>i</sub>‖<sup>2</sup> = "
         "‖O[n] − C<sub>k</sub>‖ ⇒ O&#770;[n] = C<sub>k</sub>")
_EQ_LAM = "λ = (A, B, π)"

_TBL_HEAD_VI = ["Ngày thu thập", "Thời lượng tín hiệu",
                "Thời gian kể từ lần bảo trì trước"]
_TBL_HEAD_EN = ["Date of acquisition", "Signal duration",
                "Time since last maintenance"]
_TBL_VI = [
    ["2 tháng 2 năm 2012", "10 phút 51 giây", "14 ngày"],
    ["24 tháng 2 năm 2012", "8 phút 8 giây", "36 ngày"],
    ["1 tháng 3 năm 2012", "8 phút 8 giây", "42 ngày"],
    ["15 tháng 3 năm 2012", "7 phút 3 giây", "54 ngày"],
    ["30 tháng 3 năm 2012", "6 phút", "6 ngày"],
    ["5 tháng 4 năm 2012", "5 phút", "12 ngày"],
    ["19 tháng 4 năm 2012", "6 phút", "26 ngày"],
]
_TBL_EN = [
    ["2 February 2012", "10 min 51 s", "14 days"],
    ["24 February 2012", "8 min 8 s", "36 days"],
    ["1 March 2012", "8 min 8 s", "42 days"],
    ["15 March 2012", "7 min 3 s", "54 days"],
    ["30 March 2012", "6 min", "6 days"],
    ["5 April 2012", "5 min", "12 days"],
    ["19 April 2012", "6 min", "26 days"],
]


def section(lang):
    """Return the bilingual HTML fragments of Chapter 9, span C."""
    b = []

    H(b, lang, "KỸ THUẬT BẢO TRÌ DỰ BÁO MỚI ĐƯỢC ĐỀ XUẤT",
      "PROPOSED NEW PREDICTIVE MAINTENANCE TECHNIQUE", level=2)
    P(b, lang,
      "Giải pháp đề xuất cho bài toán đã mô tả dựa trên bảo trì dự báo. Trong "
      "nghiên cứu này, bước cuối cùng của chương trình bảo trì dự báo được chọn "
      "theo cách tiếp cận dữ liệu giám sát tình trạng. Cách tiếp cận này được "
      "chia thành hai nhóm chính: kỹ thuật dự báo dựa trên mô hình và kỹ thuật "
      "dự báo dựa trên dữ liệu. Ở đây, kỹ thuật dựa trên dữ liệu được chọn vì "
      "dữ liệu giám sát tình trạng đã có sẵn. Phương pháp dựa trên mô hình đòi "
      "hỏi một mô hình chính xác của hệ thống, vốn rất phức tạp. Maffezoni đã "
      "trình bày một mô hình vật lý hữu ích của máy nghiền, gọi là mô hình cân "
      "bằng khối lượng với 76 phương trình vi phân thường (ODE), còn được biết "
      "đến như mô hình dựa trên tri thức [21]. Rõ ràng là rất khó xây dựng mô "
      "hình chính xác của hệ thống, vì vậy cách tiếp cận này không được xem "
      "xét. Mặt khác, cách tiếp cận dự báo dựa trên kinh nghiệm không thể dùng "
      "được do thống kê dữ liệu thay đổi và lượng dữ liệu không đủ. Vì tất cả "
      "những lý do trên, cách tiếp cận dựa trên dữ liệu đã được lựa chọn.",
      "The proposed solution to the described problem is based on predictive "
      "maintenance. In this research, the condition-monitoring data approach "
      "was chosen for the last step of the predictive maintenance programme. "
      "This approach can be divided into two main categories: the model-based "
      "prognostic technique and the data-driven prognostic technique. Here, "
      "the data-driven technique was chosen because condition-monitoring data "
      "were available. The model-based method requires an accurate model of "
      "the system, which is highly complex. Maffezoni presents a useful "
      "physical model of the mill, the so-called mass-balance model with 76 "
      "ordinary differential equations (ODE), better known as a knowledge-"
      "based model [21]. It is obvious that it is very hard to make an accurate "
      "model of the system, so this approach was not considered. On the other "
      "hand, the experience-based prognostic approach could not be used "
      "because of the variable data statistics and an insufficient amount of "
      "data. For all these reasons, the data-driven approach was selected.")

    H(b, lang, "Thu thập tín hiệu âm thanh", "Acoustic signal acquisition",
      level=3)
    P(b, lang,
      "Như đã mô tả ở phần trước, bước đầu tiên của chương trình bảo trì dự báo "
      "là thu thập dữ liệu. Trong nghiên cứu này, tín hiệu âm thanh ghi ở vùng "
      "lân cận máy nghiền được dùng để nhận biết tình trạng của máy. Các tín "
      "hiệu âm thanh được thu từ một máy nghiền than tại nhà máy nhiệt điện "
      "'TEKO' trong lúc máy đang vận hành. Tần số quay chính của máy nghiền "
      "khoảng 12,5 Hz và máy nghiền nơi thu tín hiệu có 10 tấm va đập.",
      "As described earlier, the first step in a predictive maintenance "
      "programme is data acquisition. In this research, acoustic signals "
      "recorded in the vicinity of the mill were used to detect the condition "
      "of the mill. The acoustic signals were acquired from a coal mill at the "
      "'TEKO' thermoelectric power plant while it was operational. The main "
      "mill rotation frequency was about 12.5 Hz and the mill from which the "
      "signals were acquired had 10 impact plates.")
    P(b, lang,
      "Trong tài liệu đã ghi nhận rằng thông tin về hư hỏng được ẩn giấu trong "
      "đặc trưng phổ của tín hiệu rung [23], nhưng cũng đã được chứng minh rằng "
      "trong một số trường hợp tín hiệu âm thanh cung cấp thông tin tương "
      "đương. Năm 2001, Baydar đã phân tích song song đặc trưng tần số của tín "
      "hiệu rung và tín hiệu âm thanh để phát hiện các loại hư hỏng khác nhau "
      "của chi tiết quay và kết luận rằng cả hai loại tín hiệu đều có thể dùng "
      "hiệu quả như nhau [24]. Nghiên cứu này dùng tín hiệu âm thanh vì chúng "
      "đơn giản và ít tốn kém hơn khi ghi so với tín hiệu rung. Chúng cũng có "
      "thể được thu mà không can thiệp vào hoạt động của máy nghiền vì được "
      "ghi từ bên ngoài.",
      "The literature reports that failure information is hidden in the "
      "spectral characteristics of vibration signals [23], but it has also "
      "been demonstrated that in some cases acoustic signals are equally "
      "informative. In 2001, Baydar conducted a parallel analysis of the "
      "frequency characteristics of vibration signals and acoustic signals to "
      "detect various types of failure of rotary components, concluding that "
      "both signals can be used equally effectively [24]. The present research "
      "uses acoustic signals because they are simpler and less costly to "
      "record than vibration signals. They can also be acquired without "
      "interfering with mill operation because they are recorded externally.")
    P(b, lang,
      "Tín hiệu âm thanh được thu bằng một micrô định hướng ở khoảng cách vài "
      "milimet trong lúc hệ thống nghiền than vận hành. Việc ghi tín hiệu được "
      "thực hiện ở độ cao thấp trong nhà máy nhiệt điện, nơi nhiễu âm thanh "
      "rất lớn. Vì lý do này, một hệ thống cố định micrô đặc biệt đã được thiết "
      "kế, đặt ở khoảng cách vài milimet từ thành của máy nghiền được phân "
      "tích, sao cho công suất của tín hiệu hữu ích có thể lớn hơn nhiều lần "
      "công suất của các nguồn âm gây nhiễu như các máy nghiền lân cận, bơm cấp "
      "liệu, van xung quanh và các nguồn khác. Tần số lấy mẫu của tín hiệu âm "
      "thanh ghi là 48 kHz. Việc thu dữ liệu được tiến hành trung bình sau mỗi "
      "2 tuần và kéo dài vài phút. Bảng 9.1 cho biết ngày ghi, ngày thay bàn "
      "nghiền và thời lượng của mỗi tín hiệu. Để triển khai thuật toán nhanh "
      "hơn, tần số lấy mẫu được giảm từ 48 xuống 4,8 kHz và thời lượng tín hiệu "
      "phân tích là 1 phút.",
      "The acoustic signals were acquired by means of a directional microphone "
      "at a distance of several millimetres while the coal-grinding subsystem "
      "was operational. Recording was performed at low altitude in the "
      "thermoelectric power plant, where acoustic contamination is highly "
      "pronounced. Because of that, a special microphone fixation system was "
      "designed, positioned at a distance of several millimetres from the walls "
      "of the analysed mill, so that the power of the useful signal could be "
      "many times higher than the power of contaminating acoustic sources such "
      "as neighbouring mills, feed pumps, surrounding valves and so on. The "
      "sampling frequency of the recorded acoustic signals was 48 kHz. Data "
      "acquisition was conducted on average every 2 weeks and lasted for "
      "several minutes. Table 9.1 gives the recording dates, the grinding-table "
      "replacement dates and the duration of each signal. For faster "
      "implementation of the algorithm, the sampling frequency was decimated "
      "from 48 to 4.8 kHz and the duration of the analysed signals was 1 min.")

    TBL(b, lang, _TBL_HEAD_VI, _TBL_HEAD_EN,
        _TBL_VI if lang == "vi" else _TBL_EN,
        caption_vi="Bảng 9.1 · Các tín hiệu âm thanh đã ghi nhận",
        caption_en="Table 9.1 · Recorded acoustic signals")

    P(b, lang,
      "Có thể thấy từ Bảng 9.1 rằng toàn bộ khoảng thời gian từ lúc thay bàn "
      "nghiền đến lúc bàn nghiền bị mòn đã được bao phủ. Sau chu kỳ ghi tín "
      "hiệu âm thanh đầu tiên, ba lần ghi khác được thực hiện sau khi thay bàn "
      "nghiền. Nhờ đó, dựa trên các tín hiệu âm thanh đã ghi, dữ liệu của hệ "
      "thống nghiền than được thu thập ở các trạng thái khác nhau. Một cơ sở "
      "dữ liệu lớn về giám sát tình trạng đã được tạo ra, không làm gián đoạn "
      "hệ thống nghiền than trong khi vận hành, và có thể được xử lý tiếp.",
      "Table 9.1 shows that the whole time period from the moment of grinding "
      "table replacement until the moment when the grinding tables are worn is "
      "covered. After the first cycle of acoustic signal recording, three more "
      "recordings were performed after grinding table replacement. In this way, "
      "based on the recorded acoustic signals, coal-grinding subsystem data "
      "are collected in different states. A large base of condition-monitoring "
      "data is obtained, without disturbing the coal-grinding subsystem while "
      "it is operational, which can be further processed.")

    H(b, lang, "Xử lý dữ liệu và trích xuất đặc trưng",
      "Data processing and feature extraction", level=3)
    P(b, lang,
      "Bước thứ hai trong bảo trì dự báo là xử lý dữ liệu. Vì dữ liệu thu thập "
      "là tín hiệu âm thanh, chúng được xếp vào loại dữ liệu dạng sóng. Để khắc "
      "phục các nhược điểm gặp phải khi phân tích dữ liệu dạng này trong miền "
      "thời gian và miền tần số [25], dữ liệu được phân tích trong miền thời "
      "gian–tần số. Phổ đồ được dùng để đánh giá tín hiệu âm thanh trong miền "
      "thời gian–tần số, vì nó biểu diễn rất rõ các thành phần phổ của tín hiệu "
      "trong ba chiều: thông tin thời gian theo trục ngang, thông tin tần số "
      "theo trục dọc và biên độ được biểu diễn bằng thang màu. Cường độ màu "
      "thể hiện độ mạnh của các thành phần phổ. Hình 9.3 [26] cho thấy phổ đồ "
      "của một tín hiệu âm thanh ghi ngày 30 tháng 3 năm 2012, tức 6 ngày sau "
      "khi thay bàn nghiền.",
      "The second step in predictive maintenance is data processing. Given that "
      "the collected data are acoustic signals, they are classified as "
      "waveform-type data. In order to overcome the disadvantages encountered "
      "when such data are analysed in the time domain and frequency domain "
      "[25], the data are analysed in the time-frequency domain. A spectrogram "
      "was used to assess the acoustic signals in the time-frequency domain, "
      "because it represents the spectral components of the signals in three "
      "dimensions very well: time information along the horizontal axis, "
      "frequency information along the vertical axis and amplitude depicted by "
      "a colour-coded scale. Colour intensity illustrates the strength of the "
      "spectral components. Figure 9.3 [26] shows the spectrogram of an "
      "acoustic signal recorded on 30 March 2012, 6 days after grinding table "
      "replacement.")
    FIG(b, 3, F.fig_f03(), lang)
    P(b, lang,
      "Hình 9.3 cho thấy rõ các tần số chiếm ưu thế và chỉ ra rằng đó là các "
      "họa âm bậc cao của tần số cơ bản của máy nghiền, với f<sub>0</sub> = "
      "12,5 Hz. Ngoài ra, các đỉnh chiếm ưu thế trong phổ xuất hiện ở các tần "
      "số 10f<sub>0</sub>, 20f<sub>0</sub> và cứ thế, phù hợp với việc có 10 "
      "tấm va đập bên trong máy nghiền, sao cho tần số cơ bản của bàn nghiền "
      "đi qua micrô là 10f<sub>0</sub>. Vì micrô được đặt càng gần bàn nghiền "
      "càng tốt, các thành phần phổ này nổi bật hơn nhiều so với các thành "
      "phần khác.",
      "Figure 9.3 clearly shows the dominant frequencies, and indicates that "
      "they are the high harmonics of the basic frequency of mill rotation, "
      "which was f<sub>0</sub> = 12.5 Hz. Also, the dominant peaks in the "
      "spectrum occurred at frequencies 10f<sub>0</sub>, 20f<sub>0</sub> and so "
      "on, according to the fact that there were 10 impact plates inside the "
      "mill, such that the basic frequency of grinding table travelling "
      "alongside the microphone was 10f<sub>0</sub>. Given that the microphone "
      "was positioned so as to be as close as possible to the grinding table, "
      "these spectral components were much more pronounced than the other "
      "components.")
    P(b, lang,
      "Sau khi thu thập dữ liệu, cần trích xuất các đặc trưng phù hợp của tín "
      "hiệu âm thanh đã ghi trong miền tần số, để thu được vectơ quan sát dùng "
      "cho phân tích với biểu đồ kiểm soát T<sup>2</sup>. Như đã đề cập, phổ đồ "
      "được dùng để biểu diễn tín hiệu âm thanh. Nếu tín hiệu âm thanh ghi được "
      "ký hiệu là y[n], thì phổ đồ của tín hiệu, thường được gọi là biến đổi "
      "Fourier nhanh trên cửa sổ ngắn (STFFT) trong tài liệu [27], được tính "
      "bằng biến đổi Fourier nhanh (FFT) trên dữ liệu cửa sổ trượt. Ý tưởng của "
      "STFFT là chia toàn bộ tín hiệu thành các đoạn có cửa sổ thời gian ngắn "
      "và áp dụng biến đổi Fourier cho từng đoạn. Phổ đồ là hàm của thời gian "
      "và tần số, được viết như sau:",
      "After data acquisition, it was necessary to extract proper "
      "characteristics of the recorded acoustic signals in the frequency "
      "domain, in order to obtain a vector of observations for analysis with "
      "T<sup>2</sup> control charts. As mentioned earlier, a spectrogram was "
      "used for acoustic signal representation. If the recorded acoustic "
      "signal is denoted as y[n], the spectrogram of the acoustic signal, often "
      "denoted as short-time fast Fourier transform (STFFT) in the literature "
      "[27], is computed as a fast Fourier transform (FFT) on sliding window "
      "data. The idea of STFFT is to divide the whole signal into segments "
      "with a short time window and apply the Fourier transform to each "
      "segment. The spectrogram represents a function of time and frequency "
      "arguments, which can be written as follows:")
    E(b, lang, _EQ_SP, _EQ_SP, num="1")
    P(b, lang,
      "trong đó f là tần số và n là đối số thời gian của phổ đồ. Các đặc trưng "
      "chất lượng được trích xuất trong miền tần số là các giá trị của "
      "S<sub>p</sub> theo thời gian tại các tần số biểu diễn các giá trị "
      "quanh họa âm bậc cao hoặc chính các họa âm bậc cao đó. Mười bốn tần số "
      "đã chọn được cho trong vectơ f<sub>p</sub>:",
      "where f denotes the frequency and n the time argument of the "
      "spectrogram. The extracted quality characteristics in the frequency "
      "domain are the values of S<sub>p</sub> across time at the frequencies "
      "representing the values around the high harmonics or the high harmonics "
      "themselves. Fourteen selected frequencies are shown in the vector "
      "f<sub>p</sub>:")
    E(b, lang, _EQ_FP, _EQ_FP, num="2")
    P(b, lang,
      "Theo đó, tại mỗi thời điểm một vectơ quan sát 14 chiều được tạo lập:",
      "Accordingly, a 14-dimensional vector of observations is formed at each "
      "time point:")
    E(b, lang, _EQ_X, _EQ_X, num="3")
    P(b, lang,
      "Tọa độ của vectơ X[n] được tính như sau:",
      "The coordinates of the vector X[n] are calculated as follows:")
    E(b, lang, _EQ_XI, _EQ_XI, num="4")
    P(b, lang,
      "trong đó f<sub>i</sub> là tọa độ thứ i của vectơ tần số f<sub>p</sub>, "
      "còn L<sub>w</sub> là độ dài của hàm cửa sổ. Đây là thủ tục tạo vectơ "
      "quan sát ban đầu. Như vậy, bước xử lý dữ liệu và trích xuất đặc trưng "
      "đã hoàn tất.",
      "where f<sub>i</sub> represents the ith coordinate of the frequency "
      "vector f<sub>p</sub>, and L<sub>w</sub> is the length of the window "
      "function. This is the procedure for generating the initial observation "
      "vector. In this way, the data-processing step and feature extraction "
      "are completed.")

    H(b, lang,
      "Ra quyết định bảo trì: biểu đồ kiểm soát Hotelling T² và mô hình Markov ẩn",
      "Maintenance decision-making: the Hotelling T² control chart and the "
      "hidden Markov model", level=3)
    P(b, lang,
      "Bước cuối cùng trong chương trình bảo trì dự báo là ra quyết định bảo "
      "trì. Như đã nêu ở đầu phần này, kỹ thuật dựa trên dữ liệu đã được chọn, "
      "nghĩa là người ta quyết định phân tích chuỗi quan sát đầu vào bằng biểu "
      "đồ kiểm soát T<sup>2</sup>, sau đó đầu ra của biểu đồ kiểm soát lại là "
      "chuỗi đầu vào của mô hình Markov ẩn (HMM). HMM cho biết thông tin về "
      "tình trạng của bàn nghiền, cụ thể là chúng đã mòn đến mức cần thay thế "
      "hay chưa. Đây là cách tiếp cận thứ hai trong dự báo hư hỏng, vì dự đoán "
      "rằng hệ thống sẽ làm việc không có sự cố cho đến một thời điểm tương "
      "lai nào đó, tức là đến khoảng thời gian tiếp theo cần kiểm tra.",
      "The last step in the predictive maintenance programme is maintenance "
      "decision-making. As described at the beginning of this section, the "
      "data-driven technique was chosen, that is, it was decided that the "
      "input sequence of observations be analysed with T<sup>2</sup> control "
      "charts, and then the outputs of the control charts will be the input "
      "sequence for a hidden Markov model (HMM). The HMM should provide "
      "information about the condition of the grinding tables, that is, "
      "whether they are worn so that their replacement is necessary. This "
      "would be the second approach in failure prognostics, because of the "
      "prediction that the system will work without failure until some future "
      "time, that is, until the next interval when inspection is needed.")
    P(b, lang,
      "Sau khi thu được vectơ quan sát, các biểu đồ kiểm soát T<sup>2</sup> "
      "được xây dựng. Nói chung, biểu đồ kiểm soát là công cụ thống kê dùng để "
      "phát hiện hư hỏng. Biểu đồ kiểm soát phân biệt rõ ràng giữa các nguyên "
      "nhân thông thường gây biến thiên trong quá trình và các sự cố của hệ "
      "thống. Với hệ thống chỉ có các nguyên nhân biến thiên thông thường, "
      "người ta nói rằng hệ thống đang ở trạng thái kiểm soát thống kê. Một "
      "biểu đồ kiểm soát thường có đường giữa (CL), giới hạn kiểm soát trên "
      "(UCL) và giới hạn kiểm soát dưới (LCL). Đường giữa biểu diễn giá trị "
      "trung bình của đặc trưng chất lượng đang xét, được xác định khi quá "
      "trình ở trạng thái kiểm soát thống kê. Các giới hạn kiểm soát được chọn "
      "sao cho khi quá trình ở trạng thái kiểm soát thống kê, hầu hết các điểm "
      "trên biểu đồ đều nằm giữa hai đường này.",
      "After obtaining the vector of observations, T<sup>2</sup> control "
      "charts were constructed. Generally speaking, a control chart is a "
      "statistical tool used to detect failure. Control charts make a clear "
      "distinction between common causes of variations in the process and "
      "failures of the system. For a system where only common causes of "
      "variations are present, we say that such a system is under statistical "
      "control. A control chart generally has a centre line (CL), an upper "
      "control limit (UCL) and a lower control limit (LCL). The centre line "
      "represents the mean value of the quality characteristic of interest, "
      "detected while the process is under statistical control. The control "
      "limits are selected such that, while the process is under statistical "
      "control, nearly all the points in the control chart will fall between "
      "these two lines.")
    P(b, lang,
      "Bước đầu tiên trong xây dựng biểu đồ kiểm soát là phân tích dữ liệu sơ "
      "bộ đang ở trạng thái kiểm soát thống kê. Bước này gọi là Giai đoạn I và "
      "dữ liệu dùng trong giai đoạn này được gọi là tập dữ liệu lịch sử. Trong "
      "Giai đoạn II, biểu đồ kiểm soát được dùng để giám sát quá trình bằng "
      "cách so sánh thống kê mẫu của từng mẫu liên tiếp, ngay khi lấy được mẫu "
      "từ quá trình, với các giới hạn kiểm soát đã thiết lập ở Giai đoạn I "
      "[28, 29].",
      "The first step in constructing a control chart requires an analysis of "
      "preliminary data that are under statistical control. This step is "
      "called Phase I, and the data used in this phase are called the "
      "historical data set. In Phase II, the control chart is used to monitor "
      "the process by comparing the sample statistic for each successive "
      "sample, as it is drawn from the process, with the control limits "
      "established in Phase I [28, 29].")
    P(b, lang,
      "Trong nghiên cứu này, phân tích đa biến đã được thực hiện với biểu đồ "
      "kiểm soát Hotelling T<sup>2</sup> [30]. Dựa trên các vectơ quan sát, dãy "
      "giá trị T<sup>2</sup> có thể được tính theo phương trình sau:",
      "A multivariate analysis with Hotelling T<sup>2</sup> control charts was "
      "undertaken in the present research [30]. Based on the observation "
      "vectors, a sequence of T<sup>2</sup> values may be calculated according "
      "to the following equation:")
    E(b, lang, _EQ_T2, _EQ_T2, num="5")
    P(b, lang,
      "trong đó X̄ và S lần lượt là các ước lượng mẫu của vectơ giá trị trung "
      "bình và ma trận hiệp phương sai. Giả sử trong quá trình thu thập dữ "
      "liệu, một dãy gồm N quan sát {X[0], X[1], …, X[N − 1]} được tạo ra, thì "
      "các ước lượng mẫu của vectơ giá trị trung bình và ma trận hiệp phương "
      "sai được viết như sau:",
      "where X̄ and S denote the sample estimators of the mean value vector and "
      "the covariance matrix, respectively. Assuming that during data "
      "acquisition a sequence of N observations {X[0], X[1], …, X[N − 1]} is "
      "generated, the sample estimators of the vector of mean values and the "
      "covariance matrix can be written as follows:")
    E(b, lang, _EQ_MEAN, _EQ_MEAN, num="6")
    E(b, lang, _EQ_COV, _EQ_COV, num="7")
    P(b, lang,
      "Các giới hạn kiểm soát trong Giai đoạn II là:",
      "The control limits in Phase II are:")
    E(b, lang, _EQ_UCL2, _EQ_UCL2, num="8")
    P(b, lang,
      "trong đó χ<sup>2</sup><sub>(α,p)</sub> là điểm phần trăm trên α của phân "
      "phối chi-bình phương với p bậc tự do (p là số biến, trong trường hợp "
      "này là 14). Khi số mẫu sơ bộ n lớn (n > 100), việc dùng giới hạn kiểm "
      "soát chi-bình phương trong Giai đoạn II là một xấp xỉ hợp lý [29]. "
      "Trong Giai đoạn I, các giới hạn dựa trên phân phối beta:",
      "where χ<sup>2</sup><sub>(α,p)</sub> is the upper α percentage point of "
      "the chi-squared distribution with p degrees of freedom (p represents "
      "the number of variables, which is 14 in our case). When the number of "
      "preliminary samples n is large (n > 100), using the chi-squared control "
      "limit in Phase II is a reasonable approximation [29]. In Phase I, the "
      "limits are based on the beta distribution:")
    E(b, lang, _EQ_UCLB, _EQ_UCLB, num="9")
    P(b, lang,
      "trong đó β<sub>(α;p/2,(n−p−1)/2)</sub> là phân vị trên α của phân phối "
      "beta với các thông số p/2 và (n − p − 1)/2.",
      "where β<sub>(α;p/2,(n−p−1)/2)</sub> is the upper α percentile of the "
      "beta distribution with parameters p/2 and (n − p − 1)/2.")
    P(b, lang,
      "Theo quan hệ trên, một dãy giá trị T<sup>2</sup> theo thời gian được "
      "tạo thành, ký hiệu là {T<sup>2</sup>[0], T<sup>2</sup>[1], …, "
      "T<sup>2</sup>[n]}, trong đó n là số thứ tự của dữ liệu cửa sổ trượt. "
      "Để tính đến động lực học của hệ thống, thay vì chỉ dùng mẫu cuối cùng "
      "của biểu đồ kiểm soát, người ta dùng 10 mẫu cuối để đặc trưng hóa trạng "
      "thái thực tế của bàn nghiền. Nói cách khác, vectơ",
      "According to the above relation, a time sequence of T<sup>2</sup> "
      "values is formed, denoted as {T<sup>2</sup>[0], T<sup>2</sup>[1], …, "
      "T<sup>2</sup>[n]}, where n denotes the sequence number of the sliding "
      "window data. In order to account for system dynamics, instead of the "
      "very last control chart sample, the last 10 samples were used for "
      "characterisation of the actual state of the grinding tables. In other "
      "words, the vector")
    E(b, lang, _EQ_O, _EQ_O, num="10")
    P(b, lang,
      "sẽ được dùng để ước tính tiếp trạng thái của hệ thống. Tuy nhiên, nếu "
      "vectơ này được đưa trực tiếp vào HMM làm quan sát, sẽ cần phải ước tính "
      "hàm xác suất đồng thời cho vectơ mười chiều này. Để tránh bài toán tính "
      "toán phức tạp đó, người ta quyết định áp dụng thủ tục lượng tử hóa vectơ "
      "như thường làm trong tài liệu. Với mục đích này, phương pháp phân cụm "
      "k-means được dùng [31]. Kết quả của phân cụm k-means là dãy các tâm cụm. "
      "Trong trường hợp này, dựa trên phương pháp thử và sai, k = 4 cho kết "
      "quả thỏa mãn và các tâm cụm C<sub>i</sub> (i = 1, 2, 3, 4) đã được thu "
      "được. Theo đó, các vectơ quan sát cuối cùng O&#770;[n] được tạo lập và "
      "chuyển tới HMM như sau:",
      "will be used for further estimation of system states. However, if this "
      "vector had been introduced as an observation in the HMM, it would have "
      "been necessary to estimate the joint probability function for this "
      "tenth-dimensional vector. In order to avoid this complex numerical "
      "problem, it was decided, as is usual in the literature, to apply the "
      "procedure of vector quantization. For this purpose, the method of "
      "k-means clustering is used [31]. The result of k-means clustering is a "
      "sequence of k-cluster centres (centroids). In our case, based on a "
      "try-and-error approach, it turned out that k = 4 gives satisfying "
      "results and cluster centres C<sub>i</sub> (i = 1, 2, 3, 4) are "
      "obtained. Accordingly, the final observation vectors O&#770;[n] are "
      "formed and forwarded to the HMM as follows:")
    E(b, lang, _EQ_Q, _EQ_Q, num="11")

    H(b, lang, "Mô hình Markov ẩn", "Hidden Markov model", level=3)
    P(b, lang,
      "Sau khi các mẫu được mã hóa như mô tả ở trên, bước tiếp theo là xây dựng "
      "HMM. HMM là mô hình thống kê dùng để mô tả sự chuyển đổi của hệ thống "
      "giữa các trạng thái. Đây là mở rộng của chuỗi Markov thông thường với "
      "các trạng thái không quan sát được hoặc chỉ quan sát được một phần. "
      "Nói chung, HMM có N trạng thái S = {S<sub>1</sub>, S<sub>2</sub>, …, "
      "S<sub>N</sub>} và M ký hiệu quan sát V = {v<sub>1</sub>, v<sub>2</sub>, "
      "…, v<sub>M</sub>}. HMM với ba trạng thái được cho trong Hình 9.4. Các "
      "trạng thái được nối với nhau sao cho có thể đi từ trạng thái này sang "
      "bất kỳ trạng thái nào khác. Trạng thái ẩn tại thời điểm t được ký hiệu "
      "là q<sub>t</sub> và sự chuyển từ trạng thái này sang trạng thái khác "
      "tuân theo quy tắc Markov (nghĩa là q<sub>t</sub> chỉ phụ thuộc vào "
      "q<sub>t−1</sub>). Bên cạnh số trạng thái N và số ký hiệu quan sát M, "
      "một số đặc trưng khác của HMM cũng cần được xác định.",
      "After the samples were coded as described above, the next step was to "
      "construct the HMM. An HMM is a statistical model used to describe the "
      "transition of a system between states. It is an extension of ordinary "
      "Markov chains with non-observable or partially observable states. "
      "Generally, an HMM has N states S = {S<sub>1</sub>, S<sub>2</sub>, …, "
      "S<sub>N</sub>} and M observation symbols V = {v<sub>1</sub>, "
      "v<sub>2</sub>, …, v<sub>M</sub>}. An HMM with three states is shown in "
      "Figure 9.4. The states are connected in such a way that it is possible "
      "to move from any one to the other. The hidden state at time t is "
      "denoted by q<sub>t</sub>, and the move from one state to the other is "
      "subject to Markov's rule (that state q<sub>t</sub> depends solely on "
      "state q<sub>t−1</sub>). In addition to the number of states N and the "
      "number of observation symbols M, several other HMM characteristics "
      "need to be defined.")
    FIG(b, 4, F.fig_f04(), lang)
    P(b, lang,
      "Ma trận chuyển A = {a<sub>ij</sub>} biểu diễn xác suất chuyển từ trạng "
      "thái i sang trạng thái j. Các hệ số a<sub>ij</sub> nói chung không âm và "
      "bằng 0 nếu không có chuyển trực tiếp giữa hai trạng thái. Tổng các xác "
      "suất trong mỗi ma trận loại A phải bằng 1. Ma trận quan sát (còn gọi là "
      "ma trận phát xạ) B = {b<sub>j</sub>(k)} cho biết xác suất quan sát k "
      "được tạo ra bởi trạng thái thứ j. Dãy trạng thái ban đầu π = {π<sub>i</sub>} "
      "mang thông tin về các xác suất ban đầu, cho biết khả năng một dãy đầu "
      "mới bắt đầu từ một trạng thái nhất định. Cuối cùng, HMM có thể được xác "
      "định bởi bộ ba:",
      "The transition matrix A = {a<sub>ij</sub>} represents the probability "
      "of moving from state i to state j. The coefficients a<sub>ij</sub> are "
      "non-negative in the general case, and equal to zero if there is no "
      "direct switching from one state to another. The sum of probabilities "
      "in each matrix of type A needs to be equal to 1. The observation matrix "
      "(also called the emission matrix) B = {b<sub>j</sub>(k)} shows the "
      "probability that observation k was produced by the jth state. The "
      "sequence of initial states π = {π<sub>i</sub>} carries information "
      "about the initial probabilities, indicating the likelihood that a new "
      "input sequence will move from a given state. Finally, the HMM can be "
      "defined by the triplet:")
    E(b, lang, _EQ_LAM, _EQ_LAM, num="12")
    P(b, lang,
      "Có ba bài toán cơ bản có thể giải bằng HMM. Mô tả chi tiết về HMM và lời "
      "giải của ba bài toán này có trong tài liệu tham khảo [32].",
      "There are three fundamental problems that can be solved by means of "
      "HMMs. A detailed description of HMMs and the solutions to these three "
      "problems is available in Ref. [32].")

    H(b, lang, "Tổ chức thuật toán đề xuất",
      "Organisation of the proposed algorithm", level=3)
    P(b, lang,
      "Hình 9.5 [26] cho thấy thuật toán đề xuất cho bảo trì dự báo được tổ "
      "chức như thế nào. Để triển khai thực tế phương pháp đề xuất, cần làm rõ "
      "rằng một số hoạt động chỉ được thực hiện một lần, như thủ tục ngoại "
      "tuyến, nhằm xác định các thống kê cần thiết và huấn luyện HMM. Mặt khác, "
      "sau khi thủ tục ngoại tuyến kết thúc, thuật toán có thể được triển khai "
      "theo thời gian thực, từ đó cung cấp giám sát trực tuyến trạng thái của "
      "các tấm nghiền của máy.",
      "Figure 9.5 [26] shows how the proposed algorithm for predictive "
      "maintenance is organised. For the purpose of the practical "
      "implementation of the proposed method, it should be clarified that "
      "certain activities are realised only once, as an offline procedure, in "
      "order to determine the necessary statistics and train the HMM. On the "
      "other hand, once the offline procedure is over, the algorithm can be "
      "implemented in real time, thus providing online monitoring of the "
      "state of the mill-grinding plates.")
    FIG(b, 5, F.fig_f05(), lang)
    return b
