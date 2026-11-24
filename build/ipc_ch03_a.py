# -*- coding: utf-8 -*-
"""Chapter 3, "Transducers - III", section 3.1 "Transducers and Measurement of
Temperature" (EN/VI bilingual).

Source: Prasad, Jayaswal & Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 136-144, printed pp. 124-132,
decoded text lines 4997-5332.  The seven source figures (3.1-3.7) are redrawn
as vectors in the `ipcfig3` supplier modules and placed where the text refers
to them.  Printed equations (3.1)-(3.6) are rendered with standard notation;
garbled minus signs in the decoded text are restored where the physical
meaning is unambiguous.  The English body keeps the source wording quirks,
the Vietnamese body uses the accepted technical meaning.
"""

import ipcfig3 as F
from ipc_ch03_lib import H, P, L, E, FIG, TBL, NOTE


def section(lang):
    b = []

    # --------------------------------------------------------------- 3.1
    H(b, lang,
      "3.1 Bộ chuyển đổi và đo nhiệt độ",
      "3.1 Transducers and Measurement of Temperature")

    # ------------------------------------------------------------- 3.1.1
    H(b, lang, "3.1.1 Mở đầu", "3.1.1 Introduction", level=3)

    P(b, lang,
      "Nhiệt độ có thể được xem là một biến cơ bản như khối lượng, chiều dài hay "
      "thời gian. Gần như mọi quá trình chế biến trong vũ trụ đều phụ thuộc vào "
      "nhiệt độ. Các hệ thống chế biến hóa học, ví dụ dược phẩm, lọc dầu, phân "
      "bón, v.v., đều là những quá trình phụ thuộc nhiệt độ. Ngay cả cơ thể người "
      "cũng có nhiệt độ trong khoảng 96 °F đến 98 °F, được liên tục kiểm soát bên "
      "trong bằng một cơ chế tinh vi. Do đó, đo nhiệt độ là một khía cạnh quan "
      "trọng của hệ thống thiết bị đo lường.",
      "Temperature variable can be considered to be a fundamental variable like "
      "mass, length or time. Almost all the processing of this universe is "
      "temperature-dependent. Chemical processing systems, e.g. pharmaceuticals, "
      "petroleum refinings, Fertilizers, etc. are all temperature dependent "
      "processes. Even our body has temperature ranging in between 96°F to 98F "
      "which is being continuously controlled internally by means of sophisticated "
      "mechanism. Measurement of temperature, therefore, is an important aspect of "
      "instrumentation system.")

    P(b, lang,
      "Cơ sở của phép đo nhiệt độ liên quan tới định luật nhiệt động học thứ zero, "
      "phát biểu rằng nếu hai vật riêng lẻ cùng ở trạng thái cân bằng nhiệt với một "
      "vật thứ ba thì cả ba vật cũng ở trạng thái cân bằng nhiệt với nhau. Các thang "
      "đo dùng để đo nhiệt độ là Celsius (100 °C) và Fahrenheit (180 °F). Hai loại "
      "thang đo này có liên hệ với nhau để chuyển đổi theo biểu thức sau:",
      "The basis of temperature measurement is related to zeroth law of "
      "thermodynamics which states that if two bodies are in thermal equilibrium "
      "with a third body individually than all three together are in thermal "
      "equilibrium amongst one another. The scales used for measurement of "
      "temperature are Celsius (100C) and Fahrenheit (180°F). These two variety of "
      "measurement scales are related with one another for conversion purpose "
      "according to following expression:")

    E(b, lang, "F − 32 = (9/5) C", "F − 32 = (9/5) C", num="3.1")

    P(b, lang,
      "Trong thang nhiệt độ tuyệt đối, đơn vị được gọi là Kelvin, có liên hệ với "
      "Celsius hoặc Fahrenheit theo các biểu thức sau:",
      "In absolute temperature scale, the unit is known as Kelvin which is related "
      "with Celsius or Fahrenheit according to the following expression:")

    L(b, lang,
      ["Nhiệt độ theo Celsius + 273,15 = Nhiệt độ theo Kelvin",
       "Nhiệt độ theo Fahrenheit + 459,69 = Nhiệt độ theo Kelvin"],
      ["Temperature in Celsius + 273.15 = Temperature in Kelvin",
       "Temperature in Fahrenheit + 459.69 = Temperature in Kelvin"],
      ordered=True)

    P(b, lang,
      "Điều này là bởi vì trong đơn vị Celsius, độ không tuyệt đối nằm ở −273,15 °C, "
      "còn trong đơn vị Fahrenheit là ở −459,69 °F. Nhiệt độ không tuyệt đối là "
      "nhiệt độ mà tại đó các phân tử của chất khí đang xét hoàn toàn không "
      "chuyển động.",
      "This is because in Celsius unit, the absolute zero is at 273.15°C and in "
      "Fahrenheit unit this is at 459.69°F. The absolute zero temperature is that "
      "temperature where there in no motion at all in the molecules of the gas "
      "under consideration.")

    # ------------------------------------------------------------- 3.1.2
    H(b, lang, "3.1.2 Phương pháp đo", "3.1.2 Measurement Methods", level=3)

    L(b, lang,
      ["(a) Phương pháp cơ học", "(b) Phương pháp điện", "(c) Phương pháp bức xạ"],
      ["(a) Mechanical methods", "(b) Electrical methods", "(c) Radiation methods."],
      ordered=True)

    H(b, lang, "(a) Phương pháp cơ học", "(a) Mechanical methods", level=4)

    P(b, lang,
      "Trong nhóm này có năm thiết bị đo phổ biến nhất, phụ thuộc vào sự thay đổi "
      "trạng thái hoặc tính chất vật lý của môi trường dùng để đo. Đó là:",
      "Under this category, there are five most popular measurement devices which "
      "depend upon the change in physical state or properties of the medium "
      "employed for the measurement. These are:")

    L(b, lang,
      ["(i) Nhiệt kế chất lỏng trong ống thủy tinh",
       "(ii) Nhiệt kế thủy ngân trong ống thép",
       "(iii) Nhiệt kế song kim loại",
       "(iv) Nhiệt kế áp suất hơi",
       "(v) Nhiệt kế thể tích không đổi"],
      ["(i) Liquid-in-glass thermometer",
       "(ii) Mercury-in-steel thermometer",
       "(iii) Bimetallic thermometer",
       "(iv) Vapour pressure thermometer",
       "(v) Constant volume thermometer"],
      ordered=True)

    P(b, lang,
      "<b>(i) Nhiệt kế chất lỏng trong ống thủy tinh.</b> Nhiệt kế chất lỏng trong "
      "ống thủy tinh về bản chất là hệ thống giãn nở chất lỏng, có đặc điểm là dải "
      "đo hẹp, thang đo đều và tuyến tính, độ chính xác cao và đáp ứng nhanh. Khi "
      "chất lỏng sẽ giãn nở do thay đổi nhiệt độ được đổ vào một ống thủy tinh có "
      "vạch chia, có độ dài mao dẫn (mao dẫn là một đường dẫn hẹp, trông như một "
      "sợi mảnh dưới lớp kính trong suốt) để giãn nở, thì cấu trúc đó được gọi là "
      "nhiệt kế chất lỏng trong ống thủy tinh. Bầu thủy tinh đóng vai trò bình chứa "
      "chất lỏng đo nằm ở đáy của hình dạng như thể hiện trong Hình 3.1. Cơ sở chia "
      "vạch thang đo phụ thuộc vào đặc tính nhiệt của chất lỏng và dải đo tương ứng "
      "có được. Thông thường, điểm đông của chất lỏng dùng là giới hạn dưới của "
      "thang đo và điểm sôi là giới hạn trên. Dải đo thực tế được xác định giữa hai "
      "điểm này, với lưu ý chất lỏng không được đông đặc cũng như không được sôi "
      "bay trong quá trình đo. Nhiệt kế y tế (dùng để đo nhiệt độ cơ thể người) "
      "trong đó thủy ngân thực sự được giữ bên trong bầu thủy tinh và sự giãn nở "
      "xảy ra bên trong mao dẫn thủy tinh cũng thuộc loại này.",
      "<b>(i) Liquid-in-glass thermometer.</b> Liquid-in-glass thermometer is "
      "essentially a liquid-expansion system which is characterized by narrow "
      "spans, uniform and linear scale, high accuracy and fast response. When the "
      "liquid which shall ultimately expand due to temperature changes is filled "
      "in a graduated glass tube having capillary length (capillary is a narrow "
      "passage, looking like a thin line under the transparent glass) for "
      "expansion, the arrangement is called liquid-in-glass thermometer. The glass "
      "bulb working as a reservoir for the measurement liquid is located at the "
      "bottom of the shape as shown in Figure 3.1. The basis for graduation of "
      "measurement scale depends upon the temperature characteristics of the liquid "
      "and corresponding range of measurement available. Normally, the freezing "
      "point of the liquid used is the lower range of the measurement scale and the "
      "boiling point is the upper range. The actual measurement span is fixed in "
      "between these two keeping in mind that the liquid should neither freeze nor "
      "boil out during measurement. Medical thermometer (used to measure the "
      "temperature of human body) in which mercury is actually kept inside the "
      "glass bulb and the expansion takes place inside the glass capillary also "
      "comes under this category.")
    FIG(b, 1, F.fig_f01(), lang)

    TBL(b, lang,
      ["Chất lỏng", "Điểm đông", "Điểm sôi", "Phạm vi đo có sẵn"],
      ["Liquid used", "Freezing point", "Boiling point",
       "Available range of Measurement"],
      [["Thủy ngân", "−39,4 °C", "357 °C", "−25 °C đến 340 °C"],
       ["Cồn", "−62,2 °C", "170 °C", "−46 °C đến 150 °C"],
       ["Pentan", "−200 °C", "300 °C", "−130 °C đến 270 °C"]]
      if lang == "vi" else
      [["Mercury", "39.4C", "357C", "25C to 340C"],
       ["Alcohol", "62.2C", "170C", "46C to 150C"],
       ["Pentane", "200C", "300C", "130C to 270C"]],
      caption_vi="Bảng 3.1", caption_en="Table 3.1")

    P(b, lang,
      "Hoạt động của nhiệt kế phụ thuộc vào hiệu ứng giãn nở nhiệt tổng hợp của cả "
      "chất lỏng lẫn thủy tinh. Thông thường, tốc độ giãn nở của chất lỏng lớn hơn "
      "của thủy tinh. Để đạt được độ giãn nở tuyến tính lớn nhất vì lý do độ chính "
      "xác, diện tích mặt cắt ngang được giảm thiểu, do đó cấu tạo mao dẫn trở nên "
      "rất quan trọng.",
      "The operation depends upon the resultant difference in thermal expansion of "
      "the liquid as well as the glass. Normally, the rate of expansion of liquid "
      "is more than the glass. To obtain maximum linear expansion for accuracy "
      "consideration, the cross-sectional area is minimized and therefore, the "
      "capillary construction becomes very important.")

    P(b, lang,
      "Một yếu tố quan trọng khác ảnh hưởng đến độ chính xác là kỹ thuật ngâm nhiệt "
      "kế. Nhiệt kế càng được ngâm sâu thì kết quả đọc càng chính xác. Ba kỹ thuật "
      "ngâm sau được dùng cho nhiệt kế chất lỏng trong ống thủy tinh:",
      "Another important consideration for accuracy is immersion techniques used. "
      "Deeper the thermometer is immersed, the more accurate the reading shall be. "
      "Three types of immersion techniques are employed for liquid-in-glass "
      "thermometer:")

    L(b, lang,
      ["Ngâm một phần", "Ngâm toàn phần", "Ngâm hoàn toàn"],
      ["Partial immersion", "Total immersion", "Full immersion"],
      ordered=True)

    P(b, lang,
      "Nhiệt kế ngâm một phần được ngâm tới một vạch cố định do một vòng ngâm lắp "
      "trên thân nhiệt kế đánh dấu. Rõ ràng, cách này kém chính xác hơn.",
      "Partial immersion thermometer is immersed upto a fixed mark indicated by an "
      "immersion ring installed on the body of the thermometer. Obviously, this is "
      "less accurate.")

    P(b, lang,
      "Loại ngâm toàn phần được ngâm tới toàn bộ chiều cao của cột chất lỏng, do đó "
      "không cần vạch đánh dấu bằng vòng ngâm cho cách bố trí này.",
      "Total immersion type is immersed upto the full height of the liquid column "
      "and therefore, the immersion ring marking is not required for this "
      "arrangement.")

    P(b, lang,
      "Nhiệt kế ngâm hoàn toàn được nhúng chìm hoàn toàn trong chất lỏng cần đo. "
      "Thang đo được quan sát qua một cửa sổ kính được chế tạo riêng cho mục đích "
      "này. Dải độ chính xác của thiết bị này nằm giữa 0,01 °C và 1 °C. Thông số "
      "ứng dụng của nhiệt kế chất lỏng trong ống thủy tinh thuộc cấp IA và B của "
      "SAMA (Scientific Apparatus Makers Association).",
      "Full immersion thermometer is completely submerged inside the measurement "
      "liquid. The measurement scale is observed through a glass window made "
      "specifically for the purpose. Accuracy range for this instrument is in "
      "between 0.01C and 1°C. Application specification of liquid-in-glass "
      "thermometer comes under SAMA (Scientific Apparatus Makers Association) "
      "class IA and B.")

    P(b, lang,
      "Ưu điểm của loại nhiệt kế này là cấu tạo đơn giản, giá rẻ, dễ mang theo và "
      "chỉ thị trực quan rõ ràng. Nhược điểm là tự thân nó dễ vỡ và việc truyền "
      "tín hiệu từ xa gặp khó khăn.",
      "Advantages of this thermometer are simple in construction, inexpensive, "
      "portability and clear visual indication. Disadvantages are that it is "
      "fragile by nature and remote transmission becomes difficult.")

    P(b, lang,
      "<b>(ii) Nhiệt kế thủy ngân trong ống thép.</b> Khi bầu (bình chứa nhỏ) của "
      "nhiệt kế và mao dẫn dài nơi xảy ra sự giãn nở được làm bằng thép, và chất "
      "lỏng dùng là thủy ngân dưới áp suất, thì cấu trúc đó được gọi là nhiệt kế "
      "thủy ngân trong ống thép. Mao dẫn thường được nối với một phần tử ống "
      "Bourdon, rồi lại nối với hệ thống chỉ thị kim-thang thông thường để chỉ thị "
      "nhiệt độ. Cấu trúc này có thể dùng để truyền nhiệt độ lẫn cho hệ thống ghi "
      "chép, vì có đủ công suất để vận hành hệ thống như thể hiện trong Hình 3.2. "
      "Hệ thống này có thể dùng trong dải thực tế từ 0 đến 500 °C.",
      "<b>(ii) Mercury-in-steel thermometer.</b> When the bulb (small reservoir) of "
      "the thermometer and the long capillary in which the expansion takes place "
      "is made of steel and the fluid used is mercury under pressure, then the "
      "arrangement is called mercury-in-steel thermometer. The capillary is "
      "normally connected to a bourdon tube element which is further connected to "
      "usual pointer-scale system for temperature indication. This arrangement can "
      "be used for temperature transmission as well as recording system since "
      "sufficient power is available for operation of the system as shown in Figure "
      "3.2. This system can be employed over a practical range of 0 to 500°C.")
    FIG(b, 2, F.fig_f02(), lang)

    P(b, lang,
      "Độ chính xác đạt được gần như ± 1 °C.",
      "The accuracy available is almost ± 1°C.")

    P(b, lang,
      "Điểm dễ tổn thương nhất của nhiệt kế thủy ngân trong ống thép là khi chiều "
      "dài mao dẫn tăng dần thì sai số do ảnh hưởng làm nguội của chiều dài kim loại "
      "cũng tăng dần. Tuy nhiên, các kỹ thuật bù trừ được áp dụng để loại bỏ sai số "
      "này. Thông số ứng dụng của nhiệt kế thủy ngân trong ống thép thuộc cấp V của "
      "SAMA.",
      "The most vulnerable point of mercury-in-steel thermometer is that as we go "
      "on increasing the length of the capillary, error introduced due to cooling "
      "effect of metallic length also goes on increasing. However, compensation "
      "techniques are applied to remove the error. Application specification of "
      "mercury-in-steel thermometer comes under SAMA class V.")

    P(b, lang,
      "Ưu điểm của nhiệt kế thủy ngân trong ống thép là dải làm việc rất tốt, trở "
      "nên chính xác hơn sau khi áp dụng kỹ thuật bù trừ, truyền tín hiệu từ xa dễ "
      "dàng và cuối cùng là nếu thiết kế đúng cách thì có thể đo cả nhiệt độ ở thang "
      "thấp, kể cả nhiệt độ âm. Nhược điểm là rất đắt tiền và không chính xác nếu "
      "không dùng biện pháp bù trừ.",
      "Advantages of mercury-in-steel thermometer are that it has very good working "
      "range, becomes more accurate after application of compensation technique, "
      "remote transmission is easily possible and lastly if designed properly "
      "temperature in the lower scale including minus temperature can also be "
      "measured. Disadvantages are that it is very expensive and also inaccurate if "
      "compensation is not employed.")

    P(b, lang,
      "<b>(iii) Nhiệt kế song kim loại.</b> Nhiệt kế song kim loại được chế tạo từ "
      "hai kim loại khác nhau có hệ số giãn nở nhiệt khác nhau. Kim loại có hệ số "
      "giãn nở nhiệt thấp hơn được hàn vào kim loại khác có hệ số giãn nở nhiệt cao "
      "hơn và được cố định thành hệ thống dầm công-xôn (cantilever) như thể hiện "
      "trong Hình 3.3. Khi nhiệt độ môi trường tăng lên, cấu trúc kim loại ghép sẽ "
      "uốn cong như thể hiện trong Hình 3.4. Chuyển động thu được do sự uốn cong "
      "có thể dùng để làm chuyển động hệ thống kim-chỉ thị và có thể được hiệu "
      "chuẩn để chỉ thị nhiệt độ. Hợp kim Invar chứa 35 % niken có hệ số giãn nở "
      "nhiệt rất thấp, vì thế được dùng làm kim loại có hệ số giãn nở thấp trong "
      "một số cấu trúc. Một hợp kim sắt-niken khác chứa 36% niken được dùng làm "
      "kim loại có hệ số giãn nở cao.",
      "<b>(iii) Bimetallic thermometer.</b> Bimetallic thermometers are constructed "
      "using two different metals having different thermal coefficient of "
      "expansion. The metal having lower thermal coefficient of expansion is welded "
      "on to another metal having higher thermal coefficient of expansion and is "
      "fixed as a cantilever system as shown in Figure 3.3. As the temperature of "
      "the surrounding is increased the combined metal structure bends as shown in "
      "Figure 3.4. The movement so obtained due to bending can be utilized to move "
      "a pointer-scale system and can be calibrated to indicate the temperature. "
      "Invar having 35 % of nickel has very low temperature coefficient of "
      "expansion and hence is used as the low expansion coefficient metal in some "
      "of the construction. Another iron-nickel alloy having 36% of nickel is used "
      "for high expansion coefficient metal.")
    FIG(b, 3, F.fig_f03(), lang)
    FIG(b, 4, F.fig_f04(), lang)

    P(b, lang,
      "Nhiệt kế song kim loại công nghiệp dùng dạng xoắn ốc của tổ hợp kim loại "
      "liên kết. Trong một cấu hình, một đầu được cố định và đầu kia tự do chuyển "
      "động, được nối với hệ thống kim-chỉ thị để chỉ thị như thể hiện trong Hình "
      "3.5. Dải đo cũng giống như của nhiệt kế thủy ngân trong ống thép.",
      "Industrial bimetallic thermometer uses helical shape of the bonded metal "
      "combination. In one configuration, one end is fixed and the other is free to "
      "move and is attached to pointer-scale system for indication as shown in "
      "Figure 3.5. The range of measurement is same as that of mercury-in-steel "
      "thermometer.")
    FIG(b, 5, F.fig_f05(), lang)

    P(b, lang,
      "Đây là một phần tử nhiệt độ rất quan trọng, được dùng rất hiệu quả trong "
      "hệ thống kết hợp cần cả cảm nhận lẫn điều khiển. Chẳng hạn, trong điều khiển "
      "nhiệt độ bằng bộ ổn nhiệt, chuyển động nhỏ thu được có khả năng tác động một "
      "công tắc điều khiển. Hoạt động của các công tắc điều khiển này điều khiển lò "
      "nướng gia đình, bàn là điện, đèn báo rẽ của ô tô và tủ lạnh.",
      "This is a very important temperature element which is very effectively used "
      "in combined system where sensing as well as control is required. For "
      "instance, in thermostatic control the small movement obtained is capable of "
      "actuating a control switch. The operation of these control switches control "
      "domestic ovens, electric irons, car winker lamps and refrigerators.")

    P(b, lang,
      "Ưu điểm của loại thiết bị này là giá rẻ, hoàn toàn không cần bảo trì và vận "
      "hành rất ổn định. Đây là thiết bị tự sinh tín hiệu và có thể dễ dàng bổ sung "
      "tính năng ghi chép. Nhược điểm là không đo được nhiệt độ thay đổi nhanh và "
      "hiệu chuẩn bị xáo trộn do xử lý thô bạo.",
      "Advantages of this type of instrument are inexpensive having no maintenance "
      "at all, very stable operation. It is a self-generating type of instrument and "
      "recording feature can be added very easily. Disadvantages are its inability "
      "to measure rapidly changing temperature and disturbances in calibration due "
      "to rough handling.")

    P(b, lang,
      "<b>(iv) Nhiệt kế áp suất hơi.</b> Nhiệt kế áp suất hơi chứa một chất lỏng dễ "
      "bay hơi cùng với hơi của nó bên trong một ranh giới kín. Khi hoạt động, áp "
      "suất của chất lỏng cùng với hơi tăng lên khi nhiệt độ tăng, bất kể sự thay "
      "đổi thể tích. Vì sự thay đổi áp suất do thay đổi nhiệt độ là kết quả kết hợp "
      "của cả hơi lẫn chất lỏng, phép đo bị ảnh hưởng tại bề mặt tiếp xúc giữa hơi "
      "và chất lỏng.",
      "<b>(iv) Vapour pressure thermometer.</b> Vapour pressure thermometer contains "
      "a volatile liquid along with its associated vapour inside a closed boundary. "
      "While in operation, the pressure of the liquid along with its vapour "
      "increases with increase in temperature irrespective of volume change. Since "
      "the pressure change due to change in temperature is the combined result of "
      "vapour as well as liquid, the measurement is affected at the interface "
      "between the vapour and the liquid.")

    P(b, lang,
      "Để bảo đảm đo đúng nhiệt độ tại bề mặt tiếp xúc, bề mặt này phải nằm bên "
      "trong bầu, nhưng trên thực tế không phải lúc nào cũng làm được. Về vấn đề "
      "này, chúng ta có thể hình dung ba điều kiện vận hành khác nhau:",
      "To ascertain proper measurement of the interface temperature, the interface "
      "should remain inside the bulb, but this is not always possible practically. "
      "In this respect, we can envisage three different operating conditions:")

    L(b, lang,
      ["(a) Thứ nhất là khi nhiệt độ bầu cao hơn nhiệt độ của mao dẫn cũng như của "
       "ống Bourdon (điều kiện thông thường). Do đó, nhiệt độ của quá trình sẽ làm "
       "bay hơi chất lỏng dễ bay hơi và hệ quả là chất này sẽ ngưng tụ trong mao dẫn "
       "cũng như trong ống Bourdon.",
       "(b) Thứ hai là khi nhiệt độ bầu thấp hơn nhiệt độ của phần còn lại của hệ "
       "thống (trường hợp này gặp trong các dịch vụ đông lạnh). Do đó, mao dẫn cũng "
       "như ống Bourdon sẽ được lấp đầy hoàn toàn bằng hơi.",
       "(c) Thứ ba là khi hệ thống đo được thiết kế để đo cả nhiệt độ cao lẫn nhiệt "
       "độ thấp của hệ thống. Như vậy, nếu bầu ở nhiệt độ thấp thì bầu sẽ chứa chủ "
       "yếu chất lỏng, còn mao dẫn và ống Bourdon đều chứa hơi. Mặt khác, nếu bầu ở "
       "nhiệt độ cao thì bầu sẽ chứa chủ yếu hơi, còn mao dẫn và ống Bourdon đều "
       "chứa chất lỏng."],
      ["(a) First is when the bulb temperature is higher than the temperature of "
       "capillary as well as the bourdon tube (normal service). Thus, the process "
       "temperature shall vaporize the volatile liquid and consequently shall "
       "condense in capillary as well as bourdon tube.",
       "(b) Second is when the bulb temperature is lower than the temperature of "
       "the rest of the system (this case is observed in cryogenic services). Thus, "
       "the capillary as well as bourdon tube shall be filled completely with "
       "vapour.",
       "(c) Third is when the measurement system is designed to measure higher as "
       "well as lower temperature of the system. Thus, if bulb is at lower "
       "temperature, it will be filled with liquid mostly and the capillary and the "
       "bourdon tube both shall have vapour. On the other hand, if bulb is at higher "
       "temperature, it shall be filled with vapour mostly and the capillary and "
       "the bourdon both shall have liquid."],
      ordered=True)

    P(b, lang,
      "Ba điều kiện vận hành nêu trên lần lượt thuộc thông số ứng dụng SAMA cấp II A, "
      "II B và II C. Nhiệt kế áp suất hơi là thiết bị đa dụng, có sẵn cho gần như "
      "mọi điều kiện đo. Nhưng dải đo của nhiệt kế áp suất hơi rất hẹp, chỉ từ 255 "
      "°C đến 315 °C. Tuy nhiên, các giới hạn này do bản chất của chất lỏng sử dụng "
      "quyết định (phần lớn là hydrocarbon hoặc chất lỏng hữu cơ).",
      "The three operating conditions described above come under application "
      "specification SAMA class II A, II B and II C respectively. Vapour pressure "
      "thermometer is a versatile equipment available for almost all conditions of "
      "measurement. But measurement range of vapour pressure thermometer is "
      "narrowfrom 255°C to 315°C only. However, these limits are decided by the "
      "nature of the fluid employed (being hydrocarbon or organic liquid mostly).")

    P(b, lang,
      "<b>(v) Nhiệt kế thể tích không đổi.</b> Nhiệt kế thể tích không đổi là một "
      "thiết bị đo nhiệt độ quan trọng khác trong hệ thống chất lỏng kín. Về nguyên "
      "tắc, phương pháp này thực chất phụ thuộc vào phép đo áp suất với thể tích "
      "không đổi.",
      "<b>(v) Constant volume thermometer.</b> Constant volume thermometer is yet "
      "another important equipment of temperature measurement in the hierarchy of "
      "liquid filled system. In principle this method is, in fact dependent upon "
      "pressure measurement wherein volume remains constant.")

    P(b, lang,
      "Bầu được đặt trong môi trường cần đo nhiệt độ. Toàn bộ hệ thống, tức là ống "
      "Bourdon, mao dẫn, bầu, v.v., đều được lấp đầy bằng chất lỏng đo. Do sự thay "
      "đổi (tăng hay giảm) của nhiệt độ, chất lỏng đo có xu hướng giãn nở hoặc co "
      "lại. Vì hệ thống được lấp đầy hoàn toàn bằng chất lỏng vốn không nén được, "
      "bất kỳ sự giãn nở hay co lại nào cũng làm áp suất của chất lỏng tăng hoặc "
      "giảm, và đây cuối cùng chính là thước đo nhiệt độ.",
      "The bulb is exposed to the environment in which the temperature is to be "
      "measured. The entire system, i.e. the bourdon tube, capillary, the bulb, "
      "etc. are all filled with the measurement liquid. Due to a change "
      "(increase/decrease) in the temperature, the measurement liquid tends to "
      "expand or contract. Since the system is completely filled with liquid which "
      "is non-compressible by nature, any expansion or contraction causes the "
      "pressure of the liquid to increase or decrease which ultimately is the "
      "measure of temperature.")

    H(b, lang, "(b) Phương pháp điện", "(b) Electrical methods", level=4)

    P(b, lang,
      "Trong nhóm này có ba thiết bị đo phổ biến nhất liên quan đến các đặc tính "
      "điện, ví dụ sự thay đổi điện trở do thay đổi nhiệt độ và sự phát sinh suất "
      "điện động (emf) do chênh lệch nhiệt độ. Các thiết bị này là:",
      "Under this category, there are three most popular measurement devices which "
      "are related to electrical behaviours, e.g. change in resistance due to "
      "change in temperature and generation of emf due to differential temperature. "
      "These devices are:")

    L(b, lang,
      ["(i) Đầu dò nhiệt độ điện trở",
       "(ii) Cặp nhiệt điện",
       "(iii) Nhiệt trở (thermistor)"],
      ["(i) Resistance temperature detector",
       "(ii) Thermocouple and",
       "(iii) Thermistor."],
      ordered=True)

    P(b, lang,
      "<b>(i) Đầu dò nhiệt độ điện trở (RTD).</b> Như đã thảo luận ở phần trước, đặc "
      "tính cơ bản là sự thay đổi điện trở của vật liệu dẫn điện do thay đổi nhiệt "
      "độ đã được ứng dụng trong phát triển RTD. Cấu trúc bên trong của một RTD "
      "công nghiệp được thể hiện trong Hình 3.6, còn dạng lắp ráp hoàn chỉnh (sẵn "
      "sàng lắp đặt) được thể hiện trong Hình 3.7. Bầu của đầu dò nhiệt độ điện trở "
      "gồm một cuộn dây bạch kim nguyên chất. Dây này được quấn trên một khung bằng "
      "mica, steatit hoặc sứ sao cho hoàn toàn không chịu ứng suất. Ứng suất gây ra "
      "tính phi tuyến trong giá trị đo. Sau khi quấn, dây được ủ ở nhiệt độ cao hơn "
      "nhiệt độ tối đa mà nó sẽ gặp trong sử dụng thực tế. Việc ủ này giải tỏa ứng "
      "suất và bảo đảm tăng cường đặc tính tái hiện cho các kết quả đọc điện trở về "
      "sau. Trong lúc ủ phải cẩn thận để tránh dây bị nhiễm bẩn trong quá trình ủ.",
      "<b>(i) Resistance temperature detector (RTD).</b> As we have discussed "
      "earlier, the basic characteristic of change in resistance of a conducting "
      "material due to change in temperature has been utilized in the development "
      "of RTD. The internal view of an industrial RTD has been shown in Figure 3.6 "
      "whereas complete assembled (ready for installation) view has been shown in "
      "Figure 3.7. The resistance temperature detector bulb consists of a coil of "
      "pure platinum wire. This wire is wound on a frame of mica, steatite or "
      "porcelain in such a way that it is completely free from strain. The strain "
      "gives rise to non-linearity in the measured value. After winding, the wire "
      "is annealed at a temperature above the maximum temperature which it would "
      "face during practical use. This annealing relieves the stress and ensures "
      "enhancement in characteristic of reproducibility for later resistance "
      "readings. While annealing care must be taken to prevent the wire becoming "
      "contaminated during process of annealing.")
    FIG(b, 6, F.fig_f06(), lang)
    FIG(b, 7, F.fig_f07(), lang)

    P(b, lang,
      "Để dùng trong công nghiệp, dây được quấn trên một cuộn steatit dài khoảng ba "
      "inch và đường kính 0,25 inch. Dây được quấn không cảm ứng trong rãnh và được "
      "phủ bằng gốm để tránh nhiễm bẩn. Sau đó nó được nhúng vào một ống lót RTD (một "
      "dạng ống bảo vệ). Ống lót dùng oxit magie (MgO) làm bột cách điện được nén "
      "chặt giữa vỏ bọc và phần tử sao cho phần tử không thể dịch chuyển. Ống lót "
      "dẻo, bền và chịu lực cơ học tốt, đồng thời đáp ứng nhiệt của RTD nhanh. Đầu "
      "của cuộn bạch kim được nối với dây dẫn đồng bằng dây vàng.",
      "For industrial use the wire is wound on a steatite spool about three inches "
      "in length and 0.25 inch in diameter. It is wound non-inductively on groove "
      "and is covered by means of ceramic for protection from contamination. It is "
      "then immersed in an RTD inset (a kind of protecting tube). The inset uses "
      "magnesium oxide (MgO) as insulating powder packed tightly between the sheath "
      "and the element so that element cannot move. The inset is flexible, durable "
      "and mechanically strong and the thermal response of the RTD is fast. The ends "
      "of the platinum coil are connected to copper leads by means of gold wire.")

    P(b, lang,
      "Đôi khi một điện trở bổ sung nhỏ (gọi là điện trở cân bằng) cũng được thêm "
      "vào RTD để tổng điện trở của bầu, dây dẫn và điện trở bổ sung đạt một giá "
      "trị tiêu chuẩn nào đó. Điện trở bổ sung làm bằng manganin có hệ số nhiệt độ "
      "điện trở không đáng kể.",
      "Sometimes a small make-up resistance (called ballast) is also added in the "
      "RTD to make the overall resistance of bulb, leads and that of make-up to some "
      "standard value. The make up resistance is made up of manganin which has "
      "negligible temperature coefficient of resistance.")

    P(b, lang,
      "Việc chọn vật liệu ống bảo vệ và chiều dài ngâm phụ thuộc vào nhiệt độ, áp "
      "suất làm việc cũng như vận tốc của chất lỏng cần đo. Với nhiệt độ, áp suất và "
      "vận tốc thấp (100 °C, 10 kg/cm2, 1 mét/giây), thép mềm với chiều dài ngâm tới "
      "500 mm hoặc 700 mm là đủ. Trên mức đó cần dùng thép không gỉ. Từ nhiệt độ "
      "môi trường đến 200 °C và 6 kg/cm2 thì dùng vật liệu nhôm.",
      "Selection of material of protecting tube and choice of immersion length "
      "depend upon service temperature, pressure as well as velocity of the fluid "
      "under measurement. For lower temperature and pressure and velocity (100°C, "
      "10 kg/cm2, 1 metre/sec). Mild steel with immersion length upto 500 mm or 700 "
      "mm are sufficient. Above this stainless steel in required. From ambient to "
      "200°C and 6 kg/cm2 aluminium material is used.")

    P(b, lang,
      "Ngoài những điều trên, RTD có chiều dài ngâm lớn tới 6000 mm (khoảng 20 feet) "
      "cũng được thiết kế cho một số sơ đồ đo đặc biệt. Chẳng hạn, để đo nhiệt độ "
      "trung bình của bình chứa dầu nặng (đường kính khoảng 30 mét), người ta dùng "
      "các phần tử RTD có chiều dài ngâm lớn như vậy. Một RTD đặc biệt khác gọi là "
      "RTD phần tử hình vòng được thiết kế để đo nhiệt độ thay đổi nhanh. Điều này "
      "đòi hỏi đáp ứng nhanh của phần tử RTD dùng. Các phần tử RTD này làm bằng các "
      "phần tử dạng vòng và được lắp khít sát vào bề mặt ngoài của ống chịu nhiệt "
      "(thermowell, một dạng ống bảo vệ khác) để giảm thiểu độ trễ trong sơ đồ đo này.",
      "In addition to the above, long immersion length RTD upto 6000 mm "
      "(approximately 20 feet) are also designed for some specific measurement "
      "scheme. For instance, to measure the average temperature of storage heavy oil "
      "tank (approximately 30 metres in diameter) such long immersion length RTD "
      "elements are employed. One more special RTD called annular element RTD has "
      "been designed to measure fast changing temperature. This necessitates quick "
      "response of RTD element employed. These RTD elements are made of annular "
      "elements and are tightly fitted against the exterior of the thermowell "
      "(another kind of protecting tube) to minimize the lag involved in such "
      "measurement scheme.")

    P(b, lang,
      "Có một ứng dụng khác mà sự suy giảm của phần tử đo nhiệt độ là mối quan tâm "
      "hàng đầu, người ta dùng tổ hợp của hai phần tử đo khác nhau. Đây gọi là phần "
      "tử kết hợp RTD-cặp nhiệt điện. Cả hai phần tử được đặt trong cùng một vỏ bọc, "
      "cho phép hai sơ đồ đo đồng thời cho cùng một nhiệt độ. Trong trường hợp này, "
      "nếu một phần tử suy giảm thì phần tử kia vẫn còn hoạt động.",
      "There is yet another application where degradation of temperature measuring "
      "element is of prime concern, a combination of two different measuring "
      "elements have been employed. This is called RTD-thermocouple combine element. "
      "Both the elements are enclosed in the same sheath enabling two simultaneous "
      "measurement schemes for the same temperature. In such situation if one "
      "element degrades, still another shall be in operation.")

    P(b, lang,
      "Về dải đo, RTD bạch kim được dùng trong khoảng nhiệt độ từ −190 °C đến 630,5 "
      "°C. Thông thường ở 0 °C, RTD bạch kim được chuẩn hóa có giá trị điện trở 100 "
      "ôm. Sự biến đổi điện trở giữa 0 °C và 630,5 °C tuân theo biểu thức:",
      "As far as measurement range is concerned, the platinum RTD is used between "
      "the range of temperature 190°C to 630.5°C. Normally at 0°C, the platinum RTD "
      "is standardized to have a resistance value of 100 ohms. The variation in "
      "resistance between the temperature 0°C and 630.5°C is governed by the "
      "expression:")
    E(b, lang, "Rt = Ro (1 + At + Bt²)", "Rt = Ro (1 + At + Bt²)", num="3.2")

    P(b, lang,
      "Tương tự, sự biến đổi điện trở giữa −190 °C và 0 °C tuân theo biểu thức:",
      "Similarly, the variation in resistance between the temperature 190°C and 0°C "
      "is governed by the expression:")
    E(b, lang, "Rt = Ro [1 + At + Bt² + C (t − 100) t³]",
      "Rt = Ro [1 + At + Bt² + C (t − 100) t³]", num="3.3")

    P(b, lang,
      "Trong hai biểu thức này, Rt và Ro lần lượt là điện trở ở nhiệt độ t °C và 0 "
      "°C. A, B và C là các hằng số. Giá trị của Ro, A, B và C được xác định bằng "
      "cách đo điện trở của RTD tại điểm đá, điểm hơi, điểm lưu huỳnh và điểm oxy.",
      "In these two expressions, Rt and Ro are the resistance at the temperature "
      "t°C and 0°C respectively. A, B and C are constants. The values of Ro, A, B "
      "and C are obtained by measuring the value of resistance of RTD at ice-point, "
      "steam-point, sulphur-point and oxygen-point respectively.")

    L(b, lang,
      ["Điểm đá là điểm nóng chảy của nước đá nguyên chất, bằng 0 °C.",
       "Điểm hơi là điểm sôi của hơi nước nguyên chất, bằng 100 °C.",
       "Điểm lưu huỳnh là điểm sôi của lưu huỳnh lỏng, bằng 444,6 °C.",
       "Điểm oxy là điểm sôi của oxy lỏng, bằng −182,97 °C."],
      ["Ice-point is the melting-point of pure ice which is equal to 0°C.",
       "Steam-point is the boiling-point of pure steam which is equal to 100°C.",
       "Sulphur-point is the boiling-point of liquid sulphur which is equal to "
       "444.6°C.",
       "Oxygen-point is the boiling-point of liquid oxygen which is equal to "
       "182.97°C."],
      ordered=True)

    P(b, lang,
      "Các biểu thức suy ra sau đây cho giá trị của Ro, A, B và C trực tiếp:",
      "The following derived expressions give the value of Ro, A, B and C directly:")

    E(b, lang, "A = (R100 − Ro)/(100 Ro)", "A = (R100 − Ro)/(100 Ro)", num="3.4")

    P(b, lang,
      "trong đó R100 là giá trị điện trở của RTD khi đặt trong hơi ở 100 °C;",
      "where R100 is the value of resistance of RTD when it is kept in steam at "
      "100°C;")

    E(b, lang, "B = (R444.6 − Ro)/(444.6² Ro)",
      "B = (R444.6 − Ro)/(444.6² Ro)", num="3.5")

    P(b, lang,
      "trong đó R444.6 là giá trị điện trở của RTD khi đặt trong lưu huỳnh lỏng sôi "
      "ở 444,6 °C.",
      "where R444.6  is the value of resistance of RTD when it is kept in boiling "
      "liquid sulphur at 444.6°C.")

    E(b, lang,
      "C = (R182.97 − Ro − 182.97 A Ro − 182.97² B Ro)/(182.97³ Ro)",
      "C = (R182.97 − Ro − 182.97 A Ro − 182.97² B Ro)/(182.97³ Ro)", num="3.6")

    P(b, lang,
      "trong đó R182.97 là giá trị điện trở của RTD khi đặt trong oxy lỏng ở "
      "−182,97 °C.",
      "where R182.97  is the value of resistance of RTD when it is kept in liquid "
      "oxygen at 182.97°C.")

    return "".join(b)
