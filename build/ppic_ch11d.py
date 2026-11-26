# -*- coding: utf-8 -*-
"""Book 9, Chapter 11, section d: proof of Theorem 1 (shifted-ectropy
Lyapunov functions, virtual control, adaptation, saturation compensation,
Remarks 4-5). Equations (34)-(61).
"""
from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS
from ppic_ch11_eqc import EQ as EC
from ppic_ch11_eqd import EQ as ED


def section(lang):
    b = []
    H(b, lang, "CHỨNG MINH ĐỊNH LÝ 1", "PROOF OF THEOREM 1", level=2)

    P(b, lang,
      "Ở đây, Định lý 1 sẽ được chứng minh qua hai bước. Bước thứ nhất là thiết kế "
      "một điều khiển phản hồi đầu ra thích ứng ảo ξ<sub>d</sub> cho hệ con",
      "Here, Theorem 1 will be proved in two steps. The first step is to design a "
      "virtual adaptive output feedback control ξ<sub>d</sub> for the subsystem")
    E(b, lang, EC[34], EC[34], num="34")
    P(b, lang,
      "trong đó ξ<sub>d</sub> là giá trị đặt của biến trạng thái ξ. Bước thứ hai là "
      "thiết kế đầu vào điều khiển phản hồi đầu ra thích ứng u sao cho hệ vòng kín "
      "ổn định tiệm cận toàn cục và bất đẳng thức (16) được thỏa mãn.",
      "where ξ<sub>d</sub> is the setpoint of state-variable ξ. The second step is "
      "to design the adaptive output feedback control input u so that the "
      "closed-loop system is globally asymptotically stable and inequality (16) "
      "is satisfied.")

    # ----- Step 1: virtual adaptive output-feedback control -----
    H(b, lang,
      "Bước 1: Thiết kế điều khiển phản hồi đầu ra thích ứng ảo",
      "Step 1: Design of the virtual adaptive output-feedback control", level=3)

    P(b, lang,
      "Trước hết, điều khiển phản hồi đầu ra thích ứng ảo ξ<sub>d</sub> được thiết "
      "kế cho hệ con (34). Vì ectropy dịch chuyển của động lực học neutron có thể "
      "được viết là [16]:",
      "First, the virtual adaptive output feedback control ξ<sub>d</sub> is "
      "designed for subsystem (34). Since the shifted-ectropy of the neutron "
      "kinetics can be written as [16]:")
    E(b, lang, EC[35], EC[35], num="35")

    P(b, lang,
      "nên hàm Lyapunov tương ứng với động lực học neutron có thể được chọn là",
      "the Lyapunov function corresponding to the neutron kinetics can be "
      "chosen as")
    E(b, lang, EC[36], EC[36], num="36")

    P(b, lang,
      "trong đó số hạng thứ hai của V<sub>N</sub> biểu diễn sự biến đổi của năng "
      "lượng phân hạch được giải phóng. Bằng cách lấy đạo hàm của (35) dọc theo "
      "quỹ đạo do động lực học neutron cho, ta thu được:",
      "where the second term of V<sub>N</sub> denotes the variation of the "
      "released fission energy. By differentiating (35) along the trajectory "
      "given by the neutron kinetics, we can obtain that:")
    E(b, lang, EC[37], EC[37], num="37")

    P(b, lang,
      "Hơn nữa, rõ ràng rằng ectropy dịch chuyển của vòng nhiệt–thủy lực là [16]:",
      "Moreover, it is clear that the shifted-ectropy of the thermal-hydraulic "
      "loop is [16]:")
    E(b, lang, EC[38], EC[38], num="38")

    P(b, lang,
      "và sau đó chọn hàm Lyapunov tương ứng là:",
      "and then choose the corresponding Lyapunov function as:")
    E(b, lang, EC[39], EC[39], num="39")

    P(b, lang,
      "trong đó 0 &lt; γ &lt; 1, và:",
      "where 0 &lt; γ &lt; 1, and:")
    E(b, lang, EC[40], EC[40], num="40")

    P(b, lang,
      "biểu diễn sự biến đổi năng lượng của vòng nhiệt–thủy lực của MHTGR. Lấy "
      "đạo hàm của (39):",
      "denotes the energy variation of the MHTGR thermal-hydraulic loop. "
      "Differentiate (39):")
    E(b, lang, EC[41], EC[41], num="41")

    P(b, lang,
      "trong đó 0 &lt; η &lt; 1.",
      "where 0 &lt; η &lt; 1.")

    P(b, lang,
      "Dựa trên các suy luận trên, chọn hàm Lyapunov cho hệ con (34) là",
      "Based on the above derivation, choose the Lyapunov function for "
      "subsystem (34) as")
    E(b, lang, EC[42], EC[42], num="42")

    P(b, lang,
      "và lấy đạo hàm của V<sub>1</sub> dọc theo quỹ đạo do (34) cho,",
      "and differentiate V<sub>1</sub> along the trajectory given by (34),")
    E(b, lang, EC[43], EC[43], num="43")

    P(b, lang, "trong đó:", "where:")
    E(b, lang, EC[44], EC[44], num="44")
    E(b, lang, EC[45], EC[45], num="45")

    P(b, lang, "và:", "and:")
    E(b, lang, EC[46], EC[46], num="46")

    P(b, lang,
      "Ở đây, các vô hướng θ<sub>i</sub> (i = 1, 2) có liên hệ chặt chẽ với các "
      "thông số vật lý và nhiệt của MHTGR và không thể xác định chính xác. Bằng "
      "cách định nghĩa θ̂<sub>i</sub> là ước lượng của θ<sub>i</sub> (i = 1, 2), "
      "chọn đầu vào điều khiển ảo ξ<sub>d</sub> như Phương trình (18), trong đó "
      "k<sub>NP</sub> thỏa mãn bất đẳng thức (28). Sau đó, thay Phương trình (18) "
      "vào (43),",
      "Here, the scalars θ<sub>i</sub> (i = 1, 2) are tightly related to the "
      "physical and thermal parameters of the MHTGR, which cannot be obtained "
      "accurately. By defining θ̂<sub>i</sub> as the estimation of θ<sub>i</sub> "
      "(i = 1, 2), choose virtual control input ξ<sub>d</sub> as Equation (18) "
      "where k<sub>NP</sub> satisfies inequality (28). Then, substitute "
      "Equations (18) to (43),")
    E(b, lang, EC[47], EC[47], num="47")

    P(b, lang, "trong đó:", "where:")
    E(b, lang, EC[48], EC[48], num="48")

    P(b, lang,
      "là các sai số ước lượng tương ứng với θ<sub>i</sub> (i = 1, 2).",
      "are estimation error corresponding to θ<sub>i</sub> (i = 1, 2).")

    P(b, lang,
      "Để bảo đảm tính ổn định của vòng kín tạo bởi hệ con (34) và (18), cần "
      "thiết kế một luật thích ứng trực tuyến thích hợp cho θ̂<sub>i</sub> "
      "(i = 1, 2). Vì vậy, định nghĩa hàm Lyapunov mở rộng là",
      "To guarantee the stability of the closed-loop formed by subsystem (34) "
      "and (18), it is necessary to design a proper online adaptation law of "
      "θ̂<sub>i</sub> (i = 1, 2). Thus, define the expanded Lyapunov function as")
    E(b, lang, EC[49], EC[49], num="49")

    P(b, lang, "trong đó:", "where:")
    E(b, lang, EC[50], EC[50], num="50")

    P(b, lang, "và:", "and:")
    E(b, lang, EC[51], EC[51], num="51")

    P(b, lang,
      "Bằng cách lấy đạo hàm của V<sub>2</sub>, ta thu được:",
      "By differentiating V<sub>2</sub>, we can obtain that:")
    E(b, lang, EC[52], EC[52], num="52")

    P(b, lang,
      "Từ bất đẳng thức (52), rõ ràng rằng nếu các luật thích ứng tương ứng với "
      "θ̂<sub>i</sub> (i = 1, 2) được chọn là (26) và (27), thì ta có:",
      "From inequality (52), it is clear that if the adaptation laws "
      "corresponding to θ̂<sub>i</sub> (i = 1, 2) are chosen as (26) and (27), "
      "then we have:")
    E(b, lang, EC[53], EC[53], num="53")

    P(b, lang,
      "nghĩa là x→O khi t→∞. Điều khiển ảo thích ứng của hệ con (18) có thể được "
      "tóm tắt là",
      "which means that x→O as t→∞. The adaptive virtual control of subsystem "
      "(18) can be summarized as")
    E(b, lang, EC[54], EC[54], num="54")

    # ----- Step 2: saturated control input for the entire system -----
    H(b, lang,
      "Bước 2: Thiết kế đầu vào điều khiển bão hòa cho toàn hệ thống",
      "Step 2: Design of the saturated control input for the entire system",
      level=3)

    P(b, lang,
      "Thứ hai, dựa trên điều khiển ảo (54), đầu vào điều khiển bão hòa u của toàn "
      "hệ thống (9) được thiết kế. Để bù cho sự bão hòa của đầu vào điều khiển, "
      "một biến trạng thái mở rộng e<sub>f</sub> được đưa vào, biến này thỏa mãn "
      "Phương trình vi phân (21) và trong đó vô hướng e<sub>g</sub> được cho bởi "
      "Phương trình (20). Hơn nữa, đặt:",
      "Second, based on virtual control (54), the saturated control input u of "
      "the entire system (9) is designed. For compensating control input "
      "saturation, an expanded state-variable e<sub>f</sub> is introduced, which "
      "satisfies differential Equation (21) and where the scalar e<sub>g</sub> "
      "is given by Equation (20). Moreover, set:")
    E(b, lang, ED[55], ED[55], num="55")

    P(b, lang,
      "là một hàm xác định dương, trong đó q<sub>Ei</sub> (i = 1, 2) là các hằng "
      "số dương cho trước. Lấy đạo hàm của V<sub>ex</sub> dọc theo quỹ đạo do (21) "
      "và (20) cho và dựa trên Phương trình (29):",
      "which is positive-definite and where q<sub>Ei</sub> (i = 1, 2) are given "
      "positive constants. Differentiate V<sub>ex</sub> along the trajectory "
      "given by (21) and (20) and based on Equation (29):")
    E(b, lang, ED[56], ED[56], num="56")

    P(b, lang,
      "Sau đó, để thiết kế đầu vào điều khiển u, chọn hàm Lyapunov cho toàn hệ "
      "thống (9) là:",
      "Then, for designing control input u, choose the Lyapunov function for "
      "the entire system (9) as:")
    E(b, lang, ED[57], ED[57], num="57")

    P(b, lang,
      "Thiết kế đầu vào điều khiển u sao cho các Phương trình (17) và (19) được "
      "thỏa mãn. Sau đó, lấy đạo hàm của V<sub>3</sub> dọc theo quỹ đạo do (9) và "
      "(17) cho:",
      "Design control input u so that Equations (17) and (19) are satisfied. "
      "Then, differentiate V<sub>3</sub> along the trajectory given by (9) and "
      "(17):")
    E(b, lang, ED[58], ED[58], num="58")

    P(b, lang, "trong đó:", "where:")
    E(b, lang, ED[59], ED[59], num="59")

    P(b, lang,
      "và hàm sat(·) được xác định bởi (23).",
      "and function sat(·) is determined by (23).")

    P(b, lang,
      "Từ bất đẳng thức (58), và bằng cách coi w là nhiễu, rõ ràng rằng hệ vòng "
      "kín ổn định nhờ đầu vào nếu các bất đẳng thức (31), (32) và (33) đều được "
      "thỏa mãn, điều đó hoàn tất chứng minh của định lý này.",
      "From inequality (58), and by regarding w as the disturbance, it is clear "
      "that the closed-loop system is input-to-state stable if inequalities "
      "(31), (32) and (33) are all satisfied, which completes the proof of this "
      "theorem.")

    P(b, lang,
      "<b>Nhận xét 4.</b> Từ bất đẳng thức (58), rất rõ ràng rằng hằng số dương "
      "γ<sub>w</sub> càng lớn thì ảnh hưởng của w càng yếu, dẫn đến tính bền vững "
      "mạnh hơn của tính ổn định vòng kín đối với nhiễu w.",
      "<b>Remark 4.</b> From inequality (58), it is very clear that the larger "
      "the positive constant γ<sub>w</sub> is, the weaker the influence of w is, "
      "which then leads to stronger robustness of the closed-loop stability to "
      "the disturbance w.")

    P(b, lang,
      "<b>Nhận xét 5.</b> Nếu w = 0, tức là:",
      "<b>Remark 5.</b> If w = 0, i.e.:")
    E(b, lang, ED[60], ED[60], num="60")

    P(b, lang,
      "thì từ bất đẳng thức (58), ta có:",
      "then from inequality (58), we have:")
    E(b, lang, ED[61], ED[61], num="61")

    P(b, lang,
      "nghĩa là x→O, e<sub>g</sub>→0, e<sub>f</sub>→0 và e<sub>ξ</sub>→0 khi t→∞.",
      "which means that x→O, e<sub>g</sub>→0, e<sub>f</sub>→0 and e<sub>ξ</sub>→0 "
      "as t→∞.")

    return b
