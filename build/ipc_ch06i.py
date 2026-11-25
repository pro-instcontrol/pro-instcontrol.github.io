# -*- coding: utf-8 -*-
"""Chapter 6, examples and exercise (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), decoded text lines 12418-12747, PDF pp. 319-328,
printed pp. 307-316.  Covers the thirteen worked Examples 6.1-6.13 with their
printed solutions and the fourteen-question exercise with its two printed
answers.  The formulas were rewritten with standard mathematical notation
after checking the page renders; the printed numbers and results are retained
even where the arithmetic looks odd.  The small unnumbered control-line
diagrams that accompany some examples are described in prose only, so no
figure call appears in this module.
"""

from ipc_ch06_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401


def section(lang):
    b = []

    H(b, lang, "Các ví dụ", "EXAMPLES")

    # -------------------------------------------------------- Example 6.1
    H(b, lang, "Ví dụ 6.1", "Example 6.1", level=3)
    P(b, lang,
      "Một bộ điều khiển chỉ thị áp suất (PIC) loại chỉ tỷ lệ có dải điều khiển "
      "từ 0 đến 160 kg/cm². Nếu kim chỉ biến quá trình chỉ 50 kg/cm² thì đầu ra "
      "bộ điều khiển là 0.2 kg/cm². Hãy tính giá trị cài đặt của bộ điều khiển "
      "và phần trăm sai số. Giả sử độ lợi của bộ điều khiển bằng 2.",
      "A pressure indicator controller (PIC) of proportional only type has a "
      "range of control between 0 and 160 kg/cm². If the process variable "
      "pointer indicates 50 kg/cm², then the controller output is 0.2 kg/cm². "
      "Calculate the set value of the controller and also percentage error. "
      "Assume gain of the controller to be 2.")
    H(b, lang, "Lời giải", "Solution", level=4)
    E(b, lang, "E₀ = đầu ra bộ điều khiển = 0.2 kg/cm² = 0%",
      "E₀ = controller output = 0.2 kg/cm² = 0%", num="")
    P(b, lang,
      "[Vì dải đầu ra là từ 0.2 đến 1.0 kg/cm²] Đầu ra bộ điều khiển bình "
      "thường Eₙ = 50% ≈ 0.6 kg/cm². Độ lợi Pg = 2.",
      "[Since the range of output is from 0.2 to 1.0 kg/cm²] Normal controller "
      "output Eₙ = 50% ≈ 0.6 kg/cm². Gain Pg = 2.")
    E(b, lang, "Eₛ = (E₀ − Eₙ)/Pg = (0 − 50)/2 = −25%",
      "Eₛ = (E₀ − Eₙ)/Pg = (0 − 50)/2 = −25%", num="")
    E(b, lang, "Eₛ = (Cpv − Csv)/(Crmax − Crmin) × 100    ...(i)",
      "Eₛ = (Cpv − Csv)/(Crmax − Crmin) × 100    ...(i)", num="")
    P(b, lang,
      "trong đó Cpv và Csv lần lượt là giá trị kim chỉ biến quá trình và giá "
      "trị cài đặt của bộ điều khiển; Crmax và Crmin là giới hạn lớn nhất và "
      "nhỏ nhất của dải bộ điều khiển. Ở đây Cpv = 50; Crmax = 160; Crmin = 0; "
      "Eₛ = −25. Thay các giá trị này vào phương trình (i), ta được",
      "where Cpv and Csv are the controller process pointer value and set value "
      "respectively, and Crmax and Crmin are the controller maximum and minimum "
      "range respectively. Here Cpv = 50; Crmax = 160; Crmin = 0; Eₛ = −25. "
      "Putting these values in equation (i), we get")
    E(b, lang, "−25 = (50 − Csv)/(160 − 0) × 100    hay    Csv = 90 kg/cm²",
      "−25 = (50 − Csv)/(160 − 0) × 100    or    Csv = 90 kg/cm²", num="")
    E(b, lang, "Ở độ lợi 2, dải tỷ lệ Pb = 50%",
      "At gain 2, proportional band Pb = 50%", num="")
    E(b, lang, "= (160 × 50)/100 = 80 kg/cm²",
      "= (160 × 50)/100 = 80 kg/cm²", num="")
    P(b, lang,
      "Sơ đồ đường điều khiển kèm theo mô tả hoạt động điều khiển: thang biến "
      "quá trình chạy từ 0 đến 160, thang đầu ra bộ điều khiển từ 0.2 đến 1.0, "
      "các vạch ở 0.2, 0.6 và 1.0; giá trị cài đặt nằm tại 90 và dải tỷ lệ "
      "80 kg/cm² trải từ 50 đến 130.",
      "The accompanying control line diagram describes the control activity: "
      "the process variable scale runs from 0 to 160, the controller output "
      "scale from 0.2 to 1.0, with marks at 0.2, 0.6 and 1.0; the set value "
      "sits at 90 and the 80 kg/cm² proportional band spans from 50 to 130.",
      )

    # -------------------------------------------------------- Example 6.2
    H(b, lang, "Ví dụ 6.2", "Example 6.2", level=3)
    P(b, lang,
      "Một bộ điều khiển chỉ thị nhiệt độ (TIC) loại chỉ tỷ lệ có dải từ 50°C "
      "đến 450°C. Khi các kim chỉ biến quá trình chỉ 75°C và 225°C thì đầu ra "
      "bộ điều khiển lần lượt là 0.3 kg/cm² và 0.9 kg/cm². Hãy tính giá trị độ "
      "lợi và giá trị cài đặt của bộ điều khiển.",
      "A temperature indicator controller (TIC) of proportional only type has "
      "range between 50°C and 450°C. When the process variable pointers "
      "indicate 75°C and 225°C, the controller output is 0.3 kg/cm² and "
      "0.9 kg/cm² respectively. Calculate the gain value and set value of the "
      "controller.")
    H(b, lang, "Lời giải", "Solution", level=4)
    E(b, lang, "Eₛ = (E₀ − Eₙ)/Pg    và    Eₛ = (Cpv − Csv)/(Crmax − Crmin) × 100",
      "Eₛ = (E₀ − Eₙ)/Pg    and also    Eₛ = (Cpv − Csv)/(Crmax − Crmin) × 100",
      num="")
    P(b, lang, "Biểu thức trên có thể viết thành",
      "which can be written as")
    E(b, lang, "Csv = Cpv − [(Crmax − Crmin)/100] × [(E₀ − Eₙ)/Pg]    ...(i)",
      "Csv = Cpv − [(Crmax − Crmin)/100] × [(E₀ − Eₙ)/Pg]    ...(i)", num="")
    P(b, lang,
      "Ở đây Crmax = 450°C; Crmin = 50°C; Eₙ = 0.6 kg/cm². Thay các giá trị này "
      "vào phương trình (i) cho biến quá trình 75°C:",
      "Here Crmax = 450°C; Crmin = 50°C; Eₙ = 0.6 kg/cm²; putting these values "
      "in equation (i) gives for 75°C process variable:")
    E(b, lang, "Csv = 75 − [(450 − 50)/100] × [(0.3 − 0.6)/(0.8 Pg)] × 100",
      "Csv = 75 − [(450 − 50)/100] × [(0.3 − 0.6)/(0.8 Pg)] × 100", num="")
    P(b, lang,
      "[trong đó 0.8 lấy từ dải của môi trường đầu ra, tức là "
      "(1.0 − 0.2) = 0.8 kg/cm²]",
      "[where 0.8 comes from the range of output medium, i.e. "
      "(1.0 − 0.2) = 0.8 kg/cm²]")
    E(b, lang, "= 75 + 150/Pg    ...(ii)", "= 75 + 150/Pg    ...(ii)", num="")
    P(b, lang, "Tương tự, với biến quá trình 225°C:",
      "Similarly, for 225°C process variable:")
    E(b, lang, "Csv = 225 − [(450 − 50)/100] × [(0.9 − 0.6)/(0.8 Pg)] × 100",
      "Csv = 225 − [(450 − 50)/100] × [(0.9 − 0.6)/(0.8 Pg)] × 100", num="")
    E(b, lang, "= 225 + 150/Pg    ...(iii)", "= 225 + 150/Pg    ...(iii)", num="")
    P(b, lang, "Vì hai giá trị Csv phải bằng nhau, nên",
      "Now since both Csv have to be equal, hence,")
    E(b, lang, "75 + 150/Pg = 225 − 150/Pg, suy ra Pg = 2",
      "75 + 150/Pg = 225 − 150/Pg, which gives Pg = 2", num="")
    E(b, lang, "Do đó Csv = 75 + 150/2 = 150°C",
      "Hence, Csv = 75 + 150/2 = 150°C", num="")
    P(b, lang,
      "Sơ đồ đường điều khiển kèm theo cho thấy các vạch 50, 75, 150, 225 và "
      "450 trên thang biến quá trình, còn 0.3, 0.6 và 0.9 trên thang đầu ra; "
      "giá trị cài đặt nằm tại 150. Vì 0.6 kg/cm² nằm đúng giữa 0.3 và 0.9 "
      "kg/cm² (các giá trị đã cho), giá trị cài đặt phải nằm giữa 75°C và 225°C.",
      "The control line diagram shows marks at 50, 75, 150, 225 and 450 on the "
      "process variable scale and at 0.3, 0.6 and 0.9 on the controller output "
      "scale; the set value sits at 150. Since the value 0.6 kg/cm² is halfway "
      "between 0.3 kg/cm² and 0.9 kg/cm² (given values), the set value must be "
      "halfway between 75°C and 225°C.")

    # -------------------------------------------------------- Example 6.3
    H(b, lang, "Ví dụ 6.3", "Example 6.3", level=3)
    P(b, lang,
      "Hình vẽ cho thấy một vòng điều khiển mức, trong đó mức của bình được "
      "điều khiển bằng cách đưa nước qua van điều khiển (CV) có lưu lượng "
      "1000 m³/hr ở vị trí mở hoàn toàn. Đặc tính van là cho qua 10 m³/hr cho "
      "mỗi phần trăm thay đổi của tín hiệu đầu ra bộ điều khiển. Ban đầu mức "
      "được duy trì ở tải 500 m³/hr. Nếu cài đặt dải tỷ lệ (PB) của bộ điều "
      "khiển chỉ thị mức (LIC) loại chỉ tỷ lệ là 10%, hãy tính đầu ra bộ điều "
      "khiển và sai số offset khi tải thay đổi thành 600 m³/hr.",
      "The diagram shows a level control loop where the level of the tank is "
      "being controlled by putting water through a control valve (CV) which "
      "delivers 1000 m³/hr in full open position. The control valve "
      "characteristic is such that it passes 10 m³/hr per percentage change in "
      "controller output signal. The level has been maintained originally for "
      "a load of 500 m³/hr. If the PB setting of the level indicator controller "
      "(LIC) of proportional only type is 10%, calculate the controller output "
      "and offset error when the load is changed to 600 m³/hr.")
    H(b, lang, "Lời giải", "Solution", level=4)
    E(b, lang, "Đầu ra bộ điều khiển cần thiết = (600 m³/hr)/(10 m³/hr cho mỗi "
      "phần trăm thay đổi đầu ra) = 60%",
      "The required controller output = (600 m³/hr)/(10 m³/hr per cent change "
      "in controller output) = 60%", num="")
    E(b, lang, "Sai số offset = (E₀ − Eₙ)/Pg    ...(i)",
      "Therefore, the offset error = (E₀ − Eₙ)/Pg    ...(i)", num="")
    E(b, lang, "Ở đây PB = 10% = 0.1, suy ra Pg = 1/0.1 = 10",
      "Here PB = 10% = 0.1, hence Pg = 1/0.1 = 10", num="")
    E(b, lang, "Sai số offset = (60 − 50)/10 = 1%",
      "Putting the value of Pg in equation (i) gives the offset error, which "
      "is equal to (60 − 50)/10 = 1%", num="")
    P(b, lang,
      "Sơ đồ vòng điều khiển kèm theo gồm bình chứa, van điều khiển (CV) trên "
      "đường vào, bộ phát hiện mức (LT), bộ điều khiển chỉ thị mức (LIC) với "
      "giá trị cài đặt và đường ra có dòng chảy ra ngoài.",
      "The accompanying level control loop shows the tank, the control valve "
      "(CV) on the inlet, the level transmitter (LT), the level indicator "
      "controller (LIC) with its set value, and the outlet flow.")

    # -------------------------------------------------------- Example 6.4
    H(b, lang, "Ví dụ 6.4", "Example 6.4", level=3)
    P(b, lang,
      "Một bộ điều khiển chỉ thị mức (LIC) có dải từ 10 đến 15 mét, loại tích "
      "phân, có giá trị cài đặt 12 mét với đầu ra bộ điều khiển ban đầu là "
      "21%. Nếu mức giảm xuống 13.5 mét, hãy tính đầu ra bộ điều khiển sau "
      "2 giây. Giả sử tốc độ tích phân được cài đặt ở 9 lần lặp mỗi phút và sai "
      "số không đổi.",
      "A level indicator controller (LIC) of range 10 to 15 metres and of "
      "integral type has a set value of 12 metres with the original controller "
      "output at 21%. If the level goes down to 13.5 metres, calculate the "
      "controller output after 2 seconds. Assume the integral rate of the "
      "controller to be set at 9 repeats per minute. Also assume the error to "
      "remain constant.")
    H(b, lang, "Lời giải", "Solution", level=4)
    E(b, lang, "Cpv = 13.5 mét; Csv = 12 mét; Crmax = 15 mét; Crmin = 10 mét",
      "Cpv = 13.5 metres; Csv = 12 metres; Crmax = 15 metres; Crmin = 10 metres",
      num="")
    E(b, lang, "Eₛ = (Cpv − Csv)/(Crmax − Crmin) × 100 = "
      "[(13.5 − 12)/(15 − 10)] × 100 = 30%",
      "Eₛ = (Cpv − Csv)/(Crmax − Crmin) × 100 = "
      "[(13.5 − 12)/(15 − 10)] × 100 = 30%", num="")
    E(b, lang, "Ti = 9 lần lặp/phút = 0.15 lần lặp/giây = "
      "0.15% đầu ra/giây/% sai số",
      "Ti = 9 repeats/minute = 0.15 repeats/second = "
      "0.15% output/second/% error", num="")
    E(b, lang, "dE₀/dt = Ti Eₛ = 0.15 × 30 = 4.5% mỗi giây",
      "dE₀/dt = Ti Eₛ = 0.15 × 30 = 4.5% per second", num="")
    E(b, lang, "E₀ = Ti∫₀ᵗ Eₛ dt + Eₙ = Ti Eₛ t + Eₙ = 4.5 × 2 + 21 = 30%",
      "E₀ = Ti∫₀ᵗ Eₛ dt + Eₙ = Ti Eₛ t + Eₙ = 4.5 × 2 + 21 = 30%", num="")

    # -------------------------------------------------------- Example 6.5
    H(b, lang, "Ví dụ 6.5", "Example 6.5", level=3)
    P(b, lang,
      "Một bộ điều khiển chỉ thị mức (LIC) loại tỷ lệ có dải tỷ lệ (P.B.) cài "
      "đặt ở 75%. Dải của bộ điều khiển từ 0 đến 10 mét và giá trị cài đặt ở "
      "6.5 mét. Đặc tính của phần tử điều khiển cuối dùng để duy trì mức là "
      "tuyến tính. Nguồn nước được cấp từ một bình được bơm với lưu lượng "
      "7 m³/hr. Hãy ước tính mức được duy trì nếu phần tử điều khiển cuối cùng "
      "cấp 10 m³/hr ở độ mở lớn nhất.",
      "A level indicating controller (LIC) of proportional type has "
      "proportional band (P.B.) set at 75%. The range of the controller is from "
      "0 to 10 metres and the set value is at 6.5 metres. The characteristic of "
      "the final control element through which the level is being maintained "
      "is linear. The supply of water is from a tank which is fed by a pump at "
      "7 m³/hr rate. Estimate the level maintained if the final control element "
      "delivers 10 m³/hr at maximum opening.")
    H(b, lang, "Lời giải", "Solution", level=4)
    E(b, lang, "Tải = 7 m³/hr (năng suất bơm); tải lớn nhất = 10 m³/hr "
      "(năng suất phần tử điều khiển cuối)",
      "Load = 7 m³/hr (pump capacity); maximum load = 10 m³/hr (capacity of "
      "final control element)", num="")
    E(b, lang, "% tải = (7/10) × 100 = 70%",
      "% load = (7/10) × 100 = 70%", num="")
    P(b, lang,
      "Giả sử áp suất vi sai không đổi qua phần tử điều khiển cuối, ở trạng "
      "thái cân bằng lưu lượng vào bằng lưu lượng ra, do đó đầu ra bộ điều "
      "khiển E₀ = 70%, vì Eₙ = 50% và Pg = 100/75.",
      "Assuming constant differential pressure across the final control "
      "element, for balanced conditions flow in must equal flow out, so the "
      "controller output is E₀ = 70%, since Eₙ = 50% and Pg = 100/75.")
    E(b, lang, "Eₛ = [(70 − 50)/100] × 75 = 15%",
      "Eₛ = [(70 − 50)/100] × 75 = 15%", num="")
    E(b, lang, "% giá trị cài đặt = (6.5 × 100)/Dải = (6.5 × 100)/10 = 65%",
      "% set value = (6.5 × 100)/Range = (6.5 × 100)/10 = 65%", num="")
    E(b, lang, "% mức = 65 + Eₛ = 65 + 15 = 80%",
      "and % Level = 65 + Eₛ = 65 + 15 = 80%", num="")
    E(b, lang, "Vậy mức = 8 mét", "Hence, Level = 8 metres", num="")

    # -------------------------------------------------------- Example 6.6
    H(b, lang, "Ví dụ 6.6", "Example 6.6", level=3)
    P(b, lang,
      "Một bộ điều khiển chỉ thị nhiệt độ (TIC) loại PID (tỷ lệ + tích phân + "
      "vi phân) có dải từ 0 đến 100°C. Nhiệt độ đo được và giá trị cài đặt lần "
      "lượt là 35°C và 45°C. Với độ lợi 2 và thời gian tích phân cùng thời gian "
      "vi phân đều bằng 4 phút, hãy tìm thời gian bộ điều khiển để thay đổi đầu "
      "ra 5% nếu nhiệt độ được giữ không đổi.",
      "A temperature indicator controller (TIC) of PID type (proportional + "
      "integral + derivative) has a range of 0 to 100°C. The value of "
      "temperature measured and the set value are 35°C and 45°C respectively. "
      "For a gain of 2 and integral and derivative times of 4 minutes each, "
      "find the time taken by the controller to change its output by 5%, if "
      "the temperature is held constant.")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang,
      "Vì nhiệt độ được giữ không đổi, sẽ không có thay đổi do hành động tỷ lệ "
      "hay vi phân. Tuy nhiên hành động tích phân chắc chắn ảnh hưởng đến sự "
      "thay đổi, và dải tỷ lệ cũng ảnh hưởng đến đáp ứng tích phân.",
      "Since the temperature is held constant, there shall not be any change "
      "due to either proportional or derivative action. However, the integral "
      "action certainly shall affect the change, but the proportional band "
      "will affect the integral response as well.")
    E(b, lang, "Sai số = 45 − 35 = 10°C = (10/100) × 100 = 10%",
      "error = 45 − 35 = 10°C = (10/100) × 100 = 10%", num="")
    E(b, lang, "Đầu ra do hành động tỷ lệ = Sai số × Độ lợi = 10 × 2 = 20%",
      "Output due to proportional action = Error × Gain = 10 × 2 = 20%", num="")
    P(b, lang,
      "Vì hành động tích phân lặp lại đầu ra của hành động tỷ lệ, sự thay đổi "
      "20% này xảy ra trong toàn bộ thời gian 4 phút. Do đó sự thay đổi 5% xảy "
      "ra trong một phút.",
      "Since integral action repeats the output of the proportional action, "
      "this 20% change will take place over the entire period of 4 minutes. "
      "Hence, a 5% change shall take place in one minute.")

    # -------------------------------------------------------- Example 6.7
    H(b, lang, "Ví dụ 6.7", "Example 6.7", level=3)
    P(b, lang,
      "Độ lệch quan sát được ở bộ điều khiển sau một nhiễu loạn bước là 4.8% "
      "(sai số) trên biến quá trình. Hãy tính sai số sau hai chu kỳ, giả sử "
      "đáp ứng của bộ điều khiển có suy giảm biên độ một phần tư.",
      "Deviation observed in a controller following a step disturbance is 4.8% "
      "(error) in the process variable. Calculate the error after elapsing two "
      "periods, assuming quarter amplitude decay in the response of the "
      "controller.")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang,
      "Đường cong dao động tắt dần kèm theo có các đỉnh liên tiếp A, B và C "
      "cách nhau một chu kỳ; ở đây B/A = C/B = 1/4.",
      "The damped oscillating curve shown has successive peaks A, B and C one "
      "period apart; here B/A = C/B = 1/4.")
    E(b, lang, "Sai số sau một chu kỳ = 4.8/4 = 1.2%",
      "Error after one period with quarter amplitude decay = 4.8/4 = 1.2%",
      num="")
    E(b, lang, "Sai số sau chu kỳ thứ hai = 1.2/4 = 0.3%",
      "Error after the second period with quarter amplitude decay = "
      "1.2/4 = 0.3%", num="")

    # -------------------------------------------------------- Example 6.8
    H(b, lang, "Ví dụ 6.8", "Example 6.8", level=3)
    P(b, lang,
      "Một bộ điều khiển chỉ thị nhiệt độ (TIC) loại PID có dải từ 0 đến 100°C. "
      "Bằng cách điều chỉnh tay tín hiệu điều khiển 0.6 kg/cm² tới phần tử "
      "điều khiển cuối lắp trên đường cấp hơi gia nhiệt, nhiệt độ được duy trì "
      "ở 50°C. Khi tăng tín hiệu điều khiển lên 0.8 kg/cm², một đường cong phản "
      "ứng quá trình được vẽ cho thấy nhiệt độ tăng lên 80°C trong thời gian "
      "3 phút. Nếu độ trễ của quá trình là 2 phút, hãy xác định loại bộ điều "
      "khiển phù hợp nhất và ước tính các cài đặt tối ưu.",
      "A temperature-indicating controller (TIC) of PID type has a range of 0 "
      "to 100°C. By manual adjustment of a 0.6 kg/cm² control signal to the "
      "final control element installed in a heating steam supply line, the "
      "temperature could be maintained at 50°C. By increasing the control "
      "signal to 0.8 kg/cm², a process reaction curve is plotted which shows a "
      "rise in temperature to 80°C within a period of 3 minutes. If the lag in "
      "the process is 2 minutes, find what type of controller is best suited "
      "and estimate the optimum controller settings as well.")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang,
      "Đường cong phản ứng quá trình kèm theo cho thấy nhiệt độ tăng từ 50°C "
      "lên 80°C (thay đổi 30°C ≈ 30%) sau độ trễ 2 phút và khoảng thời gian "
      "3 phút.",
      "The accompanying process reaction curve shows the temperature rising "
      "from 50°C to 80°C (a change of 30°C ≈ 30%) after a 2-minute lag and over "
      "a 3-minute interval.")
    E(b, lang, "Thay đổi phần trăm của phần tử điều khiển cuối: "
      "ΔC = (0.8 − 0.6)/0.8 × 100 = 25%",
      "Percentage change in final control element: "
      "ΔC = (0.8 − 0.6)/0.8 × 100 = 25%", num="")
    E(b, lang, "Thay đổi phần trăm của nhiệt độ: "
      "Δt = (80 − 50)/(100 − 0) × 100 = 30%",
      "Percentage change in temperature: "
      "Δt = (80 − 50)/(100 − 0) × 100 = 30%", num="")
    E(b, lang, "Lg = 2 phút; T = 3 phút; vì Lg < T, bộ điều khiển PID là phù "
      "hợp nhất",
      "Lag Lg = 2 minutes; duration T = 3 minutes; since Lg < T, a PID "
      "controller is most suitable for the control purpose", num="")
    E(b, lang, "Tốc độ phản ứng quá trình PRR = Δt/T = 30/3 = 10% mỗi phút",
      "Process reaction rate PRR = Δt/T = 30/3 = 10% per minute", num="")
    E(b, lang, "PB = [(80 + 3) + PRR × Lg]/ΔC = (83 × 10 × 2)/25 = 66.4%",
      "PB = [(80 + 3) + PRR × Lg]/ΔC = (83 × 10 × 2)/25 = 66.4%", num="")
    E(b, lang, "Tốc độ tích phân = 0.5/Lg = 0.5/2 = 0.25 lần lặp/phút",
      "Integral rate = 0.5/Lg = 0.5/2 = 0.25 repeats/minute", num="")
    E(b, lang, "Thời gian vi phân = 0.5 Lg = 0.5 × 2 = 1 phút",
      "Derivative time = 0.5 Lg = 0.5 × 2 = 1 minute", num="")

    # -------------------------------------------------------- Example 6.9
    H(b, lang, "Ví dụ 6.9", "Example 6.9", level=3)
    P(b, lang, "Tại sao một bộ điều khiển cần được chỉnh?",
      "Why is a controller adjusted?")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang,
      "Một bộ điều khiển được chỉnh để phối hợp độ lợi và các hàm thời gian "
      "của nó với độ lợi và các hàm thời gian của quá trình đang được điều "
      "khiển.",
      "A controller is adjusted to match the gain and time functions of the "
      "controller to those of the process which is being controlled.")

    # ------------------------------------------------------- Example 6.10
    H(b, lang, "Ví dụ 6.10", "Example 6.10", level=3)
    P(b, lang,
      "Mối quan hệ giữa thời gian tích phân và thời gian vi phân của một bộ "
      "điều khiển PID được chỉnh đúng cách lắp trong vòng điều khiển quá trình "
      "là gì?",
      "What is the relation between the integral time and the derivative time "
      "of a properly adjusted PID controller installed in a process control "
      "loop?")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang, "Trong bộ điều khiển như vậy, thời gian tích phân bằng đúng "
      "thời gian vi phân.",
      "In such a controller, integral time is just equivalent to derivative "
      "time.")

    # ------------------------------------------------------- Example 6.11
    H(b, lang, "Ví dụ 6.11", "Example 6.11", level=3)
    P(b, lang,
      "Trong một tình huống điều khiển xếp tầng điển hình, trong đó hằng số thời gian "
      "của vòng điều khiển phụ lớn hơn hằng số thời gian của vòng điều khiển "
      "chính, lợi ích của việc chọn vòng xếp tầng là gì?",
      "In a typical cascade control situation where the time constant of the "
      "secondary control loop happens to be more than the time constant of the "
      "primary control loop, what is the benefit of selecting a cascade loop?")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang, "Không có lợi ích gì.", "No benefit.")

    # ------------------------------------------------------- Example 6.12
    H(b, lang, "Ví dụ 6.12", "Example 6.12", level=3)
    P(b, lang,
      "Hãy nêu hai tình huống điều khiển quan trọng nhất mà hệ thống điều "
      "khiển đón đầu đã được áp dụng thành công.",
      "Name two of the most important control situations in which feed forward "
      "control systems have been successfully applied.")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang,
      "Chúng là: (i) điều khiển mức trống nồi hơi và (ii) điều khiển đón đầu "
      "cột chưng cất.",
      "They are: (i) boiler drum level control and (ii) feed forward control "
      "of a distillation column.")

    # ------------------------------------------------------- Example 6.13
    H(b, lang, "Ví dụ 6.13", "Example 6.13", level=3)
    P(b, lang,
      "Một bộ điều khiển chỉ thị mức (LIC) loại tỷ lệ có dải từ 0 đến 90 inch. "
      "PB được cài đặt ở 70%, độ lệch (bias) 50% và giá trị cài đặt ở 45 inch. "
      "Mức ở trạng thái điều khiển ổn định là bao nhiêu nếu tải cố định ở "
      "3.6 gpm? Phần tử điều khiển cuối có đặc tính tuyến tính và có thể cấp "
      "6 gpm ở 100% hành trình.",
      "A level-indicating controller (LIC) of proportional type has a range of "
      "0 to 90 inches. PB is set at 70%, bias at 50% and the set value is at "
      "45 inches. What is the level at steady state control if the load is "
      "fixed at 3.6 gpm? The final control element has a linear characteristic "
      "and can supply 6 gpm at 100% stroke.")
    H(b, lang, "Lời giải", "Solution", level=4)
    E(b, lang, "Lưu lượng vào = (3.6 gpm/6 gpm) × 100 = 60%",
      "Flow in = (3.6 gpm/6 gpm) × 100 = 60%", num="")
    P(b, lang,
      "Ở trạng thái ổn định, lưu lượng vào bằng lưu lượng ra. Vì vậy đầu ra bộ "
      "điều khiển bằng phần trăm lưu lượng vào, tức là 60% = E₀.",
      "At steady state condition, flow in shall equal flow out. The controller "
      "output should therefore equal the percentage flow in, i.e. 60% = E₀.")
    E(b, lang, "% giá trị cài đặt = 45 inch/90 inch = 50% = Csv",
      "Percentage set value = 45 inches/90 inches = 50% = Csv", num="")
    E(b, lang, "E₀ = [100/(%PB)](Csv − Cpv) + 50%",
      "E₀ = [100/(%PB)](Csv − Cpv) + 50%", num="")
    E(b, lang, "60 = (100/70)(50 − Cpv) + 50",
      "60 = (100/70)(50 − Cpv) + 50", num="")
    E(b, lang, "Cpv = 50 − [(60 − 50) × 70]/100 = 43%",
      "Cpv = 50 − [(60 − 50) × 70]/100 = 43%", num="")
    E(b, lang, "= 0.43 × 90 = 38.7 inch", "= 0.43 × 90 = 38.7 inches", num="")

    # ---------------------------------------------------------- exercise
    H(b, lang, "Bài tập", "Exercise")
    L(b, lang,
      ["Những yếu tố nào cần được xem xét khi chọn một hành động điều khiển cụ "
       "thể cho một quá trình? Giải thích kèm ví dụ.",
       "Điều khiển ON-OFF có thể được thực hiện như thế nào bằng cách dùng "
       "phần tử nhiệt độ thermistor? Giả sử điều khiển nhiệt độ của một ấm đun "
       "nước điện.",
       "Tại sao điều khiển PID được xem là hành động điều khiển phù hợp nhất "
       "cho vòng điều khiển nhiệt độ trong công nghiệp? Có thể gặp hạn chế gì "
       "nếu dùng điều khiển PI?",
       "Hạn chế của hành động điều khiển tỷ lệ là gì? Hành động tích phân loại "
       "bỏ hạn chế đó như thế nào? Mô tả chi tiết.",
       "Mô tả cách các hành động PID được thực hiện bằng khí nén cũng như bằng "
       "điện tử.",
       "So sánh chi tiết bộ điều khiển khí nén và bộ điều khiển điện tử.",
       "Vẽ sơ đồ khối hoàn chỉnh cho thấy tất cả các thành phần cần thiết của "
       "một vòng điều khiển quá trình tự động. Nêu ngắn gọn chức năng của từng "
       "thành phần.",
       "Hệ thống điều khiển đón đầu là gì? Chức năng của các hành động điều "
       "khiển phản hồi trong vòng điều khiển xếp tầng là gì?",
       "Mô tả sơ đồ điều khiển đón đầu dùng trong hệ thống điều khiển mức trống "
       "nồi hơi.",
       "Trong một tình huống điều khiển PID nhất định, PB được cài đặt ở 50%, "
       "thời gian tích phân và vi phân đều bằng 3 phút, giá trị cài đặt và giá "
       "trị quá trình lần lượt là 45% và 35%. Nếu giá trị quá trình không đổi, "
       "thời gian để đầu ra thay đổi 5% là bao nhiêu? <b>Đáp số: 45 giây.</b>",
       "Trong một lần vận hành bộ điều khiển PID nhất định, quá trình bắt đầu "
       "dao động với dải tỷ lệ 25% ở chu kỳ 8 phút. Hãy xác định các cài đặt "
       "tối ưu của bộ điều khiển. <b>Đáp số: Độ lợi 2.4, thời gian tích phân "
       "4 phút, thời gian vi phân 1 phút.</b>",
       "Điều khiển quá trình là gì? Mô tả các thành phần khác nhau của một hệ "
       "thống điều khiển tự động thực tế bằng sơ đồ khối.",
       "Thảo luận ngắn gọn các chế độ điều khiển khác nhau. Tại sao điều khiển "
       "PI lại tốt hơn điều khiển P?",
       "Đặc điểm đặc biệt của điều khiển PID là gì? Tại sao nó có lợi cho vòng "
       "điều khiển nhiệt độ? Tại sao hành động vi phân được thực hiện qua tín "
       "hiệu đầu vào?"],
      ["What are the different factors to be considered when selecting a "
       "particular control action for a process? Explain with examples.",
       "How can ON-OFF control be implemented by use of a thermistor "
       "temperature element? Assume temperature control of an electric kettle.",
       "Why is PID control supposed to be the most suitable control action for "
       "a temperature control loop in industry? What limitation can be "
       "expected if a PI control is used?",
       "What is the limitation of a proportional control action? How does an "
       "integral action eliminate the limitation of the proportional control "
       "action? Describe in detail.",
       "Describe how PID actions are implemented pneumatically as well as "
       "electronically.",
       "Make a detailed comparison between a pneumatic and an electronic "
       "controller.",
       "Draw a complete block diagram indicating all the required components "
       "of an automatic process control loop. Mention the function of the "
       "components in brief.",
       "What is a feedforward control system? What is the function of feedback "
       "control actions in a cascade control loop?",
       "Describe the feedforward control scheme used in a boiler drum level "
       "control system.",
       "In a particular PID control situation, the PB is set at 50%, the "
       "integral and derivative times are each equal to 3 minutes, and the set "
       "value and the process value are 45% and 35% respectively. If the "
       "process value remains unchanged, what time would be taken for the "
       "output to change by 5%? <b>Ans: 45 seconds.</b>",
       "In a certain PID controller operation, the process starts to oscillate "
       "with a 25% proportional band at a period of 8 minutes. Find out the "
       "optimum settings of the controller. <b>Ans: Gain 2.4, integral time "
       "4 min, derivative time 1 min.</b>",
       "What is process control? Describe the different components of a "
       "practical automatic control system with the help of a block diagram.",
       "Discuss the different modes of control in brief. Why is PI control "
       "superior to P-control?",
       "What are the specialities of a PID control? Why is it beneficial for a "
       "temperature control loop? Why is derivative action implemented through "
       "the input signal?"],
      ordered=True)

    return b
