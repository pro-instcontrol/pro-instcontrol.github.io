# -*- coding: utf-8 -*-
import ipcfig2 as F
from ipc_ch02_lib import H, P, L, E, FIG, TBL, NOTE

def section(lang):
    b = []

    # ---------------------------------------------------------------- 2.3 / 2.3.1
    H(b, lang,
      "2.3 Đo chuyển vị, vận tốc, gia tốc và mô-men xoắn",
      "2.3 Measurement of Displacement, Velocity, Acceleration and Torque")
    H(b, lang, "2.3.1 Chuyển vị", "2.3.1 Displacement", level=3)

    P(b, lang,
      "Chuyển vị là một đại lượng vectơ. Nó biểu diễn vị trí của một vật chuyển động đối với một "
      "điểm quy chiếu tùy ý. Chuyển vị là một biến sơ cấp. Nhiều phép đo thứ cấp hoặc đo suy diễn "
      "được thực hiện dựa trên phép đo chuyển vị. Vận tốc, gia tốc, trọng lượng, áp suất và nhiều "
      "biến tương tự khác có quan hệ toán học hoặc vật lý xác định với chuyển vị có thể được suy "
      "ra từ phép đo chuyển vị.",
      "Displacement is a vector quantity. It represents positions of a moving body with respect "
      "to an arbitrary reference. Displacement is a primary variable. Many secondary or "
      "inferential measurements are carried out on the basis of displacement measurement. "
      "Velocity, acceleration, weight, pressure and similar other variables which bear definite "
      "mathematical or physical relationships with displacement can be inferred from the "
      "measurement of displacement.")

    P(b, lang,
      "Nhiều bộ chuyển đổi chuyển vị đã được thiết kế và chế tạo để đo chuyển vị cũng như các biến "
      "liên quan khác; ở đây chúng ta sẽ thảo luận ba loại bộ chuyển đổi cơ bản và phổ biến nhất.",
      "A number of displacement transducers have been designed and fabricated for measurement of "
      "displacement as well as of other related variables, we shall discuss three most "
      "fundamental as well as popular transducers.")
    L(b, lang,
      ["Loại điện trở biến đổi", "Loại điện cảm biến đổi", "Loại điện dung biến đổi"],
      ["Variable resistance type", "Variable inductance type", "Variable capacitance type."],
      ordered=True)

    # ---------------------------------------------------------------- (i)
    H(b, lang, "(i) Bộ chuyển đổi điện trở biến đổi",
      "(i) Variable resistance transducer", level=4)
    P(b, lang,
      "Bố trí điện trở biến đổi dưới dạng chiết áp tuyến tính hoặc chiết áp góc đã được dùng để chế "
      "tạo loại bộ chuyển đổi này. Tiếp điểm di động (cần gạt) tiếp xúc với phần tử chiết áp nhờ "
      "chính lực lò xo của nó. Chuyển động của điểm tiếp xúc có thể là tuyến tính hoặc góc, tùy "
      "theo loại chuyển động và do đó tùy theo hình dạng của chiết áp.",
      "Variable resistance arrangement in the form of linear or angular potentiometer have been "
      "employed for construction of this type of transducer. The movable contact wiper makes "
      "contacts with the potentiometer element against its own spring action. The motion of the "
      "contact point can be linear or angular depending upon the type of motion and hence the "
      "shape of the potentiometer.")
    P(b, lang,
      "Phần tử điện trở, tức là phần tử chiết áp, là một bộ phận rất quan trọng trong bố trí bộ "
      "chuyển đổi này như thể hiện ở Hình 2.34. Điện trở suất và hệ số nhiệt độ là hai thuộc tính "
      "rất quan trọng cần xem xét khi chọn vật liệu cho cấu trúc này. Phần lớn dùng hợp kim "
      "đồng–niken, niken–crom hoặc bạc–palladi. Điện trở suất của các vật liệu này nằm giữa "
      "0,4 micro ohm-mét và 1,3 micro ohm-mét, còn hệ số nhiệt độ nằm giữa 0,002% mỗi độ Celsius "
      "và 0,01% mỗi độ Celsius. Phần tử là dây được kéo chính xác, phủ men cẩn thận, có đường "
      "kính tới 50 micrô. Cần gạt chạy trên chiết áp được làm bằng vật liệu lò xo, ví dụ đồng "
      "phốt pho (tôi luyện đúng cách) hoặc đồng beri. Đôi khi cũng dùng lò xo lá để giảm thiểu "
      "ảnh hưởng của rung động.",
      "The resistance element, i.e. potentiometer element is a very important part in this "
      "transducer arrangement shown in Figure 2.34. The resistivity and the temperature "
      "coefficient are two very critical properties of the resistance element to be considered "
      "for selecting a material for this scheme. Mostly alloys of copper-nickel, nickel-chromium "
      "or silver-palladium are in use. Resistivity of these materials lies between 0.4 micro "
      "ohmmeter and 1.3 micro ohmmeter and temperature coefficient lies between 0.002% per degree "
      "centigrade and 0.01% per degree centigrade. The element is precision drawn and properly "
      "enameled wire having diameter upto 50 microns. The wiper which runs on the potentiometer "
      "is made of spring material e.g. phosphor bronze (properly tempered) or beryllium copper. "
      "Sometimes leaf springs are also used to minimize the effect of vibration.")
    FIG(b, 34, F.fig_f34(), lang)

    P(b, lang,
      "Trong bố trí bộ chuyển đổi này, sai số do nhiễu là đáng kể. Sai số nhiễu phát sinh do điện "
      "trở tiếp xúc của cần gạt di động và hiệu ứng nhiệt điện. Tuy nhiên, những sai số này được "
      "giảm thiểu bằng cách điều chỉnh áp lực tiếp xúc và cải tiến cấu trúc cần gạt.",
      "In this type of transducer arrangement, error due to noise is considerable. Noise error is "
      "developed due to contact resistance of movable wiper and thermoelectric effect. These are, "
      "however, minimized by adjusting the contact pressure and modifying the wiper structure.")

    H(b, lang, "Ưu điểm", "Advantages", level=4)
    L(b, lang,
      ["Mạch đo đơn giản.",
       "Có thể thực hiện phép đo có độ chính xác cao ngay cả với chuyển vị rất nhỏ."],
      ["Measurement circuit is simple.",
       "High precision measurement is possible for very small displacement as well."])

    H(b, lang, "Nhược điểm", "Disadvantages", level=4)
    L(b, lang,
      ["Rất dễ bị ảnh hưởng bởi rung động cũng như va đập.",
       "Đáp ứng động kém.",
       "Sai số do nhiễu trong trường hợp này rất rõ rệt."],
      ["It is very much susceptible to vibration as well as shock.",
       "It has poor dynamic response.",
       "Noise error in this case is prominent."])

    # ---------------------------------------------------------------- (ii)
    H(b, lang, "(ii) Bộ chuyển đổi điện cảm biến đổi",
      "(ii) Variable inductance transmitter", level=4)
    P(b, lang,
      "Bộ chuyển đổi chuyển vị phổ biến và được dùng rộng rãi nhất hoạt động theo nguyên lý này "
      "được gọi là LVDT (Biến áp vi sai tuyến tính biến đổi). LVDT gồm một cuộn dây nguồn điện áp "
      "xoay chiều sơ cấp và hai cuộn dây thứ cấp "
      "giống hệt nhau (cả về cơ khí lẫn điện) dùng để lấy đầu ra. Một lõi từ tính di động được nối "
      "với một cần, được đặt ở vị trí trung tâm và cho phép chuyển động dọc trục. Chuyển động hay "
      "dịch chuyển của lõi di động sinh ra điện áp tỉ lệ, được đo làm đầu ra. Hệ thống được thể "
      "hiện ở Hình 2.35.",
      "The most popular and widely used displacement transducer working on this principle is "
      "known as LVDT (Linear Variable Differential Transformer). The LVDT consists of a primary "
      "A.C. voltage source coil and two identical (mechanically as well as electrically) "
      "secondary coils for obtaining output. A movable magnetic core connected with an arm is "
      "placed centrally and allowed to move axially. The movement or displacement of movable core "
      "enduces proportional voltage and is measured as output. The system has been shown in "
      "Figure 2.35.")
    FIG(b, 35, F.fig_f35(), lang)

    P(b, lang,
      "Hai cuộn thứ cấp được bố trí đối xứng với nhau và đối xứng với cuộn sơ cấp. Khi lõi ở vị trí "
      "trung tâm, hai cuộn thứ cấp sẽ có dòng điện chạy như thể hiện ở Hình 2.36 trong trường hợp "
      "nửa chu kỳ dương của đầu vào. Đối với nửa chu kỳ âm, các dòng điện này bị chặn hoàn toàn "
      "và đầu ra trở thành không. Hai điện trở bằng nhau và cả hai cuộn thứ cấp đều giống nhau về "
      "điện nên dòng điện chạy qua chúng bằng nhau; nhưng vì cực tính của chúng khác nhau, đầu ra "
      "ròng bằng không.",
      "The secondary coils are placed symmetric to each other and with respect to primary coil. "
      "When the core is at the centre, the two secondary coils shall have the current flow as "
      "shown in Figure 2.36 in the event of positive half cycle of the input. For negative half "
      "cycle, these currents are blocked altogether and output becomes zero. The two resistances "
      "are equal and both the secondary coils are electrically similar the currents through these "
      "are equal but since their polarity is different, net output equals zero.")
    FIG(b, 36, F.fig_f36(), lang)

    P(b, lang,
      "Khi lõi ở gần cuộn thứ cấp 1, điện áp trong cuộn thứ cấp 1 tăng lên và IR1 trở nên lớn hơn "
      "IR2, làm cho eout dương. Tương tự, khi lõi ở gần cuộn thứ cấp 2, eout trở nên âm.",
      "When the core is near to secondary 1, voltage in secondary 1 is increased and IR1 becomes "
      "greater than IR2, eout becomes positive. Similarly, when the core is near to secondary 2, "
      "eout becomes negative.")
    P(b, lang,
      "Độ lớn của eout tỉ lệ với vị trí của lõi so với vị trí trung tâm. Chuyển vị càng lớn thì đầu "
      "ra càng lớn. Cực tính của eout cho biết hướng của chuyển vị. Có thể thu được đầu ra một "
      "chiều bằng chỉnh lưu và lọc. Dạng sóng xoay chiều có thể thu được trực tiếp bằng cách nối "
      "hai cuộn thứ cấp theo cấu trúc mắc nối tiếp ngược cực như thể hiện ở Hình 2.37. Việc sử "
      "dụng bộ phát hiện pha là rất cần thiết.",
      "The magnitude of eout shall be proportional to position of core with respect to central "
      "position. The greater the displacement, the greater shall be the output. Polarity of eout "
      "indicates the direction of displacement. D.C. output can be obtained by rectification and "
      "filtering. A.C. waveform can be obtained directly by connecting the two secondary coils "
      "in series opposition arrangement as shown in Figure 2.37. Use of phase detector shall be "
      "essential.")
    FIG(b, 37, F.fig_f37(), lang)

    P(b, lang,
      "Thiết kế thích hợp các cuộn thứ cấp cho đầu ra tuyến tính trong dải đo chuyển vị đã quy "
      "định.",
      "Proper design of secondary coils gives linear output for specified measurement range of "
      "displacement.")
    P(b, lang,
      "Các cuộn dây được làm từ dây đồng phủ men, quấn trên khung chắc chắn (làm bằng gốm hoặc "
      "nhựa phenol). Toàn bộ cụm được đặt trong vỏ phù hợp để che chắn từ tính và tĩnh điện. Dải "
      "đo thông thường là từ ± 10 micrô đến ± 10 mm.",
      "The coils made of enamelled copper wire are wound on strong former (made of ceramic or "
      "phenolic). The entire unit is enclosed in a suitable case for providing magnetic and "
      "electrostatic shielding. The normal range of measurement is from ± 10 microns to ± 10 mm.")

    H(b, lang, "Ưu điểm của hệ thống", "Advantages of the System", level=4)
    L(b, lang,
      ["Thiết kế lẫn chế tạo đều đơn giản.",
       "Độ phân giải đạt được rất cao.",
       "Cấu trúc chắc chắn.",
       "Đầu ra tuyến tính.",
       "Có thể đạt độ nhạy cao.",
       "Độ ổn định của thiết bị cao hơn."],
      ["Design as well as fabrication are simple.",
       "Resolution obtained is very high.",
       "Constructional feature is rugged.",
       "Output is linear.",
       "High sensitivity is obtainable.",
       "Stability of the instrument is higher."])
    P(b, lang,
      "Nhược điểm duy nhất là thiết bị này đắt tiền. Nhưng trên thực tế, chi phí cao hơn có thể "
      "dễ dàng được bù đắp bằng những ưu điểm thu được.",
      "The only disadvantage is that it is expensive instrument. But practically the higher cost "
      "can be met easily by the advantages obtained.")
    P(b, lang,
      "Theo cách tương tự như LVDT, phép đo chuyển vị góc cũng có thể được thực hiện bằng một bố "
      "trí gọi là RVDT (Biến áp vi sai quay biến đổi). "
      "Nguyên lý hoạt động cơ bản vẫn giữ nguyên như của LVDT. Tuy nhiên, khác biệt chính về cấu "
      "trúc nằm ở lõi; lõi này phải được thiết kế tựa như một cam. Cam được làm bằng vật liệu từ "
      "tính theo yêu cầu. Cả cuộn sơ cấp lẫn cuộn thứ cấp đều được thiết kế có dạng cung vòm. Hình "
      "dạng của cam được chọn sao cho chuyển động góc của nó trong khe hở không khí tạo ra đầu ra "
      "tuyến tính. Bố trí này được thể hiện ở Hình 2.38.",
      "On similar pattern as LVDT, measurement of angular displacement can also be carried out by "
      "employing an arrangement called RVDT (Rotary Variable Differential Transformer). The basic "
      "principle of operation remains same as that of LVDT. The main difference in the "
      "construction however lies in the core which has to be designed just like a cam. The cam is "
      "made of magnetic material as is the requirement. The primary as well as secondary coils are "
      "designed like the shape of an arc. The shape of the cam is selected in such a way that its "
      "angular movement in the air gap produces linear output. The arrangement has been shown in "
      "Figure 2.38.")
    FIG(b, 38, F.fig_f38(), lang)

    # ---------------------------------------------------------------- (iii)
    H(b, lang, "(iii) Bộ chuyển đổi điện dung biến đổi",
      "(iii) Variable capacitance transducer", level=4)
    P(b, lang,
      "Bộ chuyển đổi chuyển vị loại điện dung biến đổi được thiết kế phổ biến nhất dựa trên nguyên "
      "lý cơ bản là sự thay đổi điện dung Cp giữa hai bản cực tụ điện song song theo biểu thức:",
      "The most commonly designed variable capacitance type displacement transducer is based on "
      "the basic principle of change of capacitance Cp between two parallel plates capacitor "
      "according to the relation:")
    E(b, lang, "Cp = ρ A/d0", "Cp = ρ A/d0")
    P(b, lang,
      "trong đó ρ là hằng số điện môi của môi trường; A là diện tích mặt cắt ngang của bản cực tụ "
      "điện và d0 là khoảng cách giữa các bản cực tụ điện.",
      "where ρ is dielectric constant for the medium; A is the cross-sectional area of the "
      "capacitor plate and d0 is the spacing between the capacitor plates.")
    P(b, lang,
      "Như biểu thức trên cho thấy, sự thay đổi điện dung trong bố trí này có thể thực hiện bằng "
      "ba cách: (a) thay đổi d0; (b) thay đổi A hoặc (c) thay đổi ρ. Sự biến thiên kết quả của giá "
      "trị điện dung có thể được chuyển đổi thành tín hiệu điện một chiều 4 đến 20 mAmps bằng cách "
      "thiết kế mạch điện tử phù hợp. Một trong các mạch đó được thể hiện ở Hình 2.39.",
      "As the above relation indicates, the change in the capacitance in such an arrangement can "
      "be brought about by three ways: (a) by changing d0;  (b)  by  changing A or (c) by changing "
      "ρ. The resultant variation in capacitance value can be converted to a 4 to 20 mAmps. D.C. "
      "electrical signal by designing suitable electronic circuit. One of the circuits has been "
      "shown in Figure 2.39.")
    E(b, lang, "eo = [Cp/(C − Cp)] ei", "eo = [Cp/(C − Cp)] ei")
    FIG(b, 39, F.fig_f39(), lang)
    E(b, lang,
      "eo = (ρ A ei)/(C d0). Do đó, e0 ∝ ρ, hoặc A, hoặc 1/d0.",
      "eo = (ρ A ei)/(C d0). Hence, e0 α ρ or A or 1/d0.")

    return "".join(b)
