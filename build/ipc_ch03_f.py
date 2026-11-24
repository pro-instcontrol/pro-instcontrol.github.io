# -*- coding: utf-8 -*-
"""Chapter 3, "Transducers - III", first half of section 3.3.3
"Different Types of Primary Elements" (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 174-190, printed pp. 162-178,
decoded text lines 6685-7284.  The figures (3.33-3.47) are redrawn as
vectors in the `ipcfig3` supplier modules.  Printed equations (3.20)-(3.38)
are rendered with standard notation; the glyph-decoded symbols are restored
from the page renders.  The English body keeps the source wording quirks,
the Vietnamese body uses the accepted technical meaning.
"""

import ipcfig3 as F
from ipc_ch03_lib import H, P, L, E, FIG, TBL, NOTE


def section(lang):
    b = []

    # ----------------------------------------------------------- 3.3.3
    H(b, lang,
      "3.3.3 Các loại phần tử sơ cấp khác nhau",
      "3.3.3 Different Types of Primary Elements", level=3)

    # ------------------------------------------------------- 1. Orifice Plate
    H(b, lang, "1. Tấm lỗ", "1. Orifice Plate", level=4)

    P(b, lang,
      "Khi cần đo chất lỏng ở trạng thái hai pha, ví dụ hơi bão hòa và các chất "
      "lỏng tương tự có chứa hơi của chính nó, tấm lỗ hiện có phải được cải "
      "tiến. Một lỗ nhỏ được khoan bên dưới lỗ chính. Lỗ này gọi là lỗ rỉ "
      "(weep hole), cho phép chất lỏng chảy liên tục và không để hơi tụ lại ở "
      "phía thượng lưu. Hình 3.33 cho thấy ba dạng tấm lỗ: đồng tâm, lệch tâm "
      "và dạng đoạn cung.",
      "When the measurement has to be carried out on mixed phase fluid, e.g. "
      "saturated steam and similar other fluid containing its vapour as well, "
      "the existing orifice plate has to be modified. A small hole is made "
      "below the main orifice. This hole which is known as weep hole, shall "
      "allow the liquid to continuously flow and will not allow the vapour to "
      "collect on the upstream side. Figure 3.33 shows three types of orifice "
      "plates: concentric, eccentric and segmental.")
    FIG(b, 33, F.fig_f33(), lang)

    P(b, lang,
      "Chúng ta biết rằng tấm lỗ hay bất kỳ phần tử sơ cấp tương tự nào cũng tạo "
      "ra một chênh áp trong đường ống chính, và chênh áp này là thước đo lưu "
      "lượng. Chênh áp đó phải được đo trước thì mới suy ra được lưu lượng. Vị "
      "trí lấy áp để đo chênh áp là một vấn đề quan trọng. Ở phía hạ lưu của "
      "tấm lỗ, điểm mà vận tốc chất lỏng lớn nhất (do đó áp suất nhỏ nhất) "
      "được gọi là chỗ co thắt (vena contracta). Lấy áp thấp gần chỗ co thắt "
      "là lý tưởng nhưng khó thực hiện, vì điểm này luôn thay đổi do nhiều "
      "nguyên nhân. Vị trí chỗ co thắt phụ thuộc chủ yếu vào vận tốc chất lỏng "
      "qua lỗ và tỷ số d/D, gọi là tỷ số β. Trong thực tế vận tốc chất lỏng "
      "luôn thay đổi, ngay cả tỷ số d/D cũng thay đổi chỉ vì một ít cặn bẩn "
      "bám trên bề mặt tấm lỗ hay đường ống chính. Tuy nhiên, có thể tìm được "
      "vị trí lấy áp lý tưởng cho một bộ giá trị xác định của vận tốc, kích "
      "thước lỗ và kích thước đường ống.",
      "We know that the orifice plate or any other similar primary element "
      "creates a differential pressure in the main pipe which is a measure of "
      "the flow rate. This differential pressure has to be measured first so "
      "that the flow rate can be inferred. Location of tapping to measure the "
      "differential pressure constitutes an important consideration. In this "
      "respect, a point in the downstream side of the orifice where velocity "
      "of the fluid is maximum (consequently minimum pressure) is called vena "
      "contracta. Low pressure tapping location near vena contracta is ideal "
      "but is difficult to realize. Because this point gets always changed "
      "due to various reasons. This location of vena contracta depends mainly "
      "upon fluid velocity through the orifice and the ratio d/D (which is "
      "called β ratio). Practically, the velocity of the fluid goes on "
      "changing every time. Even d/D ratio goes on changing due to even "
      "slight accumulation of foreign particles on the internals of the "
      "orifice or the main pipes. However, an ideal location for vena "
      "contracta tapping can be found out for a particular set of values of "
      "velocity, orifice size and the main pipe size.")

    P(b, lang,
      "Trong ứng dụng thực tế, điểm lấy áp cao ở thượng lưu cách 1 đường kính "
      "ống (1D) và điểm lấy áp thấp ở hạ lưu cách nửa đường kính ống (0.5D) "
      "được coi là vị trí gần nhất tương đương với điểm co thắt lý tưởng. "
      "Điểm lấy áp này gọi là lấy áp bán kính (radius tap). Ưu điểm lớn nhất "
      "của cách lấy áp tiêu chuẩn này là tấm lỗ có thể được lắp cùng với mặt "
      "bích đi kèm đã chế sẵn kiểu lấy áp này trên bích. Nhờ vậy việc lắp đặt "
      "tấm lỗ trở nên dễ dàng. Đây là điểm rất quan trọng trong thực hành lắp "
      "đặt, vì yêu cầu về vị trí chính xác của các điểm lấy áp và việc chế tạo "
      "chúng để đạt độ chính xác đo rất nghiêm ngặt, nên việc chuẩn bị sẵn tại "
      "xưởng trước khi lắp đặt là rất có lợi.",
      "In practical application, one pipe diameter (1D) upstream "
      "(high-pressure tap) and one half-pipe diameter (0.5D) downstream "
      "(low-pressure tap) has been considered the nearest tapping point "
      "equivalent to the ideal vena contracta point. This tap is called "
      "radius tap. The biggest advantage of this standard tapping is that the "
      "orifice plate can be combined along with companion flanges having this "
      "type of tapping already fabricated on the flanges. Due to this "
      "availability, installation of orifice plate becomes easier. This is a "
      "very important point in installation practices because requirement of "
      "exact tap location and also their fabrication for accuracy of "
      "measurement are so stringent that preparations at shop floor itself "
      "for installation is very much advantageous.")

    H(b, lang, "Các kiểu lấy áp trong kỹ thuật đồng hồ lưu lượng",
      "Types of tapping used in flowmeter engineering", level=4)
    L(b, lang,
      ["Lấy áp bích (flange taps): 1 inch ở phía thượng lưu và 1 inch ở phía "
       "hạ lưu của vị trí tấm lỗ.",
       "Lấy áp góc (corner taps): 0.02D ở thượng lưu và 0.02D ở hạ lưu.",
       "Lấy áp bán kính (D và D/2): 1D ở thượng lưu và D/2 ở hạ lưu của vị trí "
       "tấm lỗ.",
       "Lấy áp toàn dòng (2.5D và 8D): đầu áp suất cao đặt ở 2.5D thượng lưu, "
       "đầu áp suất thấp ở 8D hạ lưu của tấm lỗ."],
      ["Flange taps: 1 inch on the upstream side and 1 inch on the downstream "
       "side of the orifice location.",
       "Corner taps: 0.02D at the upstream and also 0.02D on the downstream "
       "is called corner tap.",
       "Radius taps (D and D/2 tap): This is 1D upstream and D/2 downstream "
       "of the orifice location.",
       "Full Flow tap (2.5D and 8D): In this tapping the high pressure end "
       "shall be located at 2.5D upstream and low pressure end will be at 8D "
       "downstream of the orifice."], ordered=True)
    P(b, lang,
      "Cả ba kiểu lấy áp kể trên đều có thể được cung cấp cùng với cụm tấm lỗ "
      "chế tạo sẵn nếu đặt hàng. Ưu điểm của tấm lỗ là chi phí thấp, độ chính "
      "xác cao, lắp đặt và tháo dỡ dễ dàng và khả năng lặp lại cao. Nhược điểm "
      "là đáp ứng không ổn định khi dùng với chất lỏng nhớt, không phù hợp với "
      "chất bẩn và hiệu năng giảm khi đo chất lưu hỗn hợp pha.",
      "All the three tappings can be provided along with the manufactured "
      "orifice assembly if ordered. Advantages of orifice plate are low cost, "
      "high accuracy, installation and removal easy and reproducibility high. "
      "Disadvantages include erratic response when used on viscous fluids, "
      "unsuitability for dirty fluids and reduced performance on mixed phase "
      "fluids.")

    # -------------------------------------------------------- 2. Pitot Tube
    H(b, lang, "2. Ống Pitot", "2. Pitot Tube", level=4)

    P(b, lang,
      "Nếu một ống được đặt trong dòng chất lỏng đang chảy với một đầu mở hướng "
      "thẳng vào dòng chảy, chất lỏng sẽ đột ngột dừng lại và năng lượng động "
      "của nó chuyển thành năng lượng áp suất. Áp suất tăng lên bên trong ống "
      "sẽ lớn hơn áp suất của phần dòng chảy không bị xáo trộn. Chênh áp này "
      "có thể biểu diễn bằng toán học như sau:",
      "If a tube is put inside the stream of a flowing fluid with one of its "
      "open end directly facing the stream, then the fluid abruptly comes to "
      "rest and results in conversion of its kinetic energy into pressure "
      "energy. This pressure build-up inside the tube shall have a greater "
      "value than that of the undisturbed portion of the stream. The "
      "difference in pressure can be represented mathematically by:")
    E(b, lang, "h = V₂²/(2g) − V₁²/(2g)", "h = V₂²/(2g) − V₁²/(2g)", num="3.20")
    P(b, lang,
      "Trong đó h là chênh áp, V₁ và V₂ là hai vận tốc và g là gia tốc trọng "
      "trường.",
      "where h is the difference in pressure, V₁ and V₂ are the two velocities "
      "and g is the acceleration due to gravity.")
    P(b, lang,
      "Vì V₂ = 0 nên h = V₁²/(2g), hay:",
      "Since V₂ = 0, h = V₁²/(2g), or")
    E(b, lang, "V₁ = √(2gh)", "V₁ = √(2gh)", num="3.21")
    P(b, lang,
      "Trong thực tế không thể làm V₂ bằng đúng không, vì một phần dòng chảy "
      "có thể bị lệch qua cạnh của ống và do đó ảnh hưởng đến giá trị của V₁. "
      "Tuy nhiên có thể đưa vào một hằng số C gọi là hằng số ống Pitot để tính "
      "đến sai số do nguyên nhân trên. Giá trị của C do các yếu tố thiết kế của "
      "ống Pitot quyết định. Phương trình trên trở thành:",
      "Practically it is not possible to bring the value of V₂ equal to zero "
      "because some part of the flow stream may get deflected across the edge "
      "also and therefore, it will affect the value of V₁. A constant C can "
      "however, be introduced as Pitot tube constant which shall look after "
      "the inaccuracy brought about by the above consideration. The value of "
      "C shall be decided by the design factors at the pitot tube. The above "
      "equation takes the form,")
    E(b, lang, "V₁ = C√(2gh)", "V₁ = C√(2gh)", num="3.22")
    P(b, lang,
      "Phương trình này có thể áp dụng trực tiếp cả cho khí ở vận tốc thấp, "
      "nhưng ở vận tốc cao cần có hệ số hiệu chỉnh thích hợp (hệ số hiệu "
      "chỉnh đoạn nhiệt).",
      "This equation can be directly applied to gas of low velocity also, but "
      "at higher velocity a suitable correction factor (adiabatic correction "
      "factor) shall be needed.")
    P(b, lang,
      "Ống Pitot shown trong Hình 3.34 là một thiết bị va chạm. Nó thực tế "
      "không gây trở lực cho dòng chảy. Đây là thiết bị đo chênh áp trong đó "
      "lối vào chính hứng lấy cả áp suất lẫn năng lượng dòng chảy, còn lối vào "
      "phụ hay tĩnh chỉ đo áp suất. Vì vậy không có tổn thất áp suất và thiết "
      "bị cho output chênh áp lớn nhất so với mọi phần tử lưu lượng khác. "
      "Tiếc là đây không phải hệ thống đo chính xác, vì nó đo tại một điểm "
      "(spot measurement), trong khi các phần tử khác cho lưu lượng trung "
      "bình của chất lỏng; ống Pitot chỉ đo lưu lượng tại một điểm bên trong "
      "dòng chảy.",
      "The pitot tube which has been shown in Figure 3.34 is an impact device. "
      "It does not offer any resistance to the flow of stream practically. It "
      "is differential pressure measuring device of which the main entrance "
      "faces the pressure as well as flowing energy. The auxiliary or the "
      "static entrance measures pressure only and therefore, the arrangement "
      "does not have any loss of pressure and produces greatest differential "
      "output with respect to any other flow element. But, unfortunately it "
      "is not so accurate measuring system since it is a spot measurement "
      "device, whereas other flow elements present average flow rate of the "
      "fluid, a pitot tube can measure the flow rate at a point only inside "
      "the stream.")
    FIG(b, 34, F.fig_f34(), lang)
    P(b, lang,
      "Chức năng chính của ống Pitot là tìm phân bố vận tốc của dòng chảy; "
      "chức năng này đòi hỏi dòng chảy phải được chỉnh lưu. Chi phí của hệ "
      "thống đo này rất thấp.",
      "Main function of a pitot tube is to find the velocity distribution of "
      "the flow stream. Such function needs to have the flow stream to be "
      "streamlined. The cost of this measurement system is very low.")

    # -------------------------------------------------------- 3. Venturi Tube
    H(b, lang, "3. Ống Venturi", "3. Venturi Tube", level=4)

    P(b, lang,
      "Ống Venturi được thiết kế cho những trường hợp không thể dùng tấm lỗ "
      "một cách dễ dàng và phát huy đầy đủ ưu điểm. Vấn đề khó chịu nhất của "
      "tấm lỗ là tổn thất áp suất lớn. Tấm lỗ tạo ra nhiều nhiễu loạn ở phía "
      "hạ lưu của phần tử và tổn thất áp suất do đó không bao giờ phục hồi "
      "được. Như Hình 3.35, cấu tạo của ống Venturi có đoạn vào được chỉnh "
      "lưu, đoạn ra không đột ngột mà loe dần và đủ dài để phục hồi tổn thất. "
      "Nhờ vậy dòng chảy đạt vận tốc lớn mà không gây nhiễu loạn. Đoạn thượng "
      "lưu gọi là đoạn tiếp cận (approach section), đoạn hạ lưu là đoạn phục "
      "hồi (recovery section) và phần nằm giữa là đoạn cổ hẹp (throat section). "
      "Bán kính đoạn vào là D/2, bán kính cổ hẹp là d/2, với D là đường kính "
      "ống và d là đường kính cổ hẹp; góc vào α ≈ 21°, góc loe ra ≈ 5° đến 8°.",
      "Venturi tube has been designed for the services where orifice plate "
      "cannot be used easily and with full advangates. The most annoying "
      "problem with orifice plate is its large pressure loss. Orifice creates "
      "great turbulence in the downstream part of the flow element and the "
      "loss of pressure due to this can never be recovered. Since the "
      "construction of the venturi tube as shown in Figure 3.35 is such that "
      "the inlet section is streamlined, outlet section is not abrupt but "
      "gradually expanding and long enough to recover the loss. In this way, "
      "the flow can achieve greater velocity without experiencing turbulence. "
      "The upstream section is called approach section, the downstream "
      "section is called recovery section and the portion lying in between is "
      "called throat section. The inlet radius is D/2, the throat radius is "
      "d/2, with D the pipe diameter and d the throat diameter; the inlet "
      "angle α ≈ 21° and the outlet angle ≈ 5° to 8°.")
    FIG(b, 35, F.fig_f35(), lang)
    P(b, lang,
      "Vì có đặc tính tổn thất áp suất thấp, ống Venturi dùng được thành công "
      "trong các ứng dụng mà chênh áp sẵn có rất nhỏ. Nó đặc biệt hữu ích để đo "
      "lưu lượng của bùn và hỗn dịch chất rắn trong chất lỏng. Đây là thiết bị "
      "đắt tiền. Nó được cung cấp cùng với chính đường ống, nghĩa là sau khi "
      "lắp đặt không thể thay đổi phạm vi ứng dụng. Nó cũng khó lắp đặt trên "
      "đường ống hiện có.",
      "Since this has low pressure loss characteristics, this can be "
      "successfully used in applications where the available differential is "
      "low. This is very useful for measurement of flow of slurries as well as "
      "suspensions of solids in liquids. This is an expensive instrument. It "
      "is supplied along with pipeline itself, that means once installed, the "
      "range of application cannot be changed. Also it is difficult to install "
      "it on existing pipeline.")
    P(b, lang,
      "Ống Venturi áp suất thấp có kích thước nhỏ hơn 50 mm được làm bằng đồng "
      "thau và đồng đúc. Kích thước lớn hơn với áp suất làm việc tới 15 "
      "kg/cm² được làm bằng gang. Ở các ứng dụng áp suất cao hơn, nó được làm "
      "bằng thép đúc có lớp lót bằng đồng gun metal để giảm thiểu xói mòn. Để "
      "dễ lắp đặt, đoạn vào được thiết kế có cùng kích thước với đường ống.",
      "Low pressure venturi tubes of dimension less than 50 mm are made of "
      "brass and bronze. Larger dimensions having operating pressure upto 15 "
      "kg/cm2 are made of cast iron. For higher pressure applications it is "
      "made of cast steel with a liner of gun metal to minimize the erosion. "
      "For making ease of installation the entry portion of it is designed to "
      "have the same dimension as the pipeline.")

    # ------------------------------------------------------- 4. Flow Nozzle
    H(b, lang, "4. Vòi phun lưu lượng", "4. Flow Nozzle", level=4)

    P(b, lang,
      "Vòi phun lưu lượng là dạng cải tiến của ống Venturi và cũng rất giống "
      "tấm lỗ. Phần vào của vòi phun được uốn cong nhẹ nhàng sao cho tiếp "
      "xúc với một đoạn song song ngắn như Hình 3.36. Hầu hết đặc tính của nó "
      "nằm giữa ống Venturi và tấm lỗ. Sự phục hồi áp suất giống như ống "
      "Venturi, trong khi chi phí chế tạo và lắp đặt cao hơn một chút so với "
      "tấm lỗ nhưng vẫn chấp nhận được. Nó thường được làm bằng kim loại chắc "
      "chắn vì lắp đặt chủ yếu cho dịch vụ áp suất cao. Các kích thước ghi trên "
      "hình gồm d, 1.5d, D, 0.6d và 0.1D.",
      "A flow nozzle is a modified version of a venturi tube and also very "
      "much similar to an orifice plate. The entry part of the flow nozzle is "
      "gently curved in such a way that it is tangent to a short parallel "
      "section as shown in Figure 3.36. Almost all of its characteristics lie "
      "in between venturi tube and orifice plate. The pressure recovery is "
      "just like venturi tube where as the expenses of fabrication and "
      "installation are slightly more than orifice plate but bearable "
      "comparatively. It is generally made of strong metal since this is "
      "installed on normally higher pressure services. The dimensions shown "
      "in the figure are d, 1.5d, D, 0.6d and 0.1D.")
    FIG(b, 36, F.fig_f36(), lang)
    P(b, lang,
      "Đồng gun metal, thép không gỉ (các loại AISI 304, 316 hoặc 316 L) và "
      "hợp kim monel là một số vật liệu chế tạo vòi phun lưu lượng. Trong đo "
      "lưu lượng hơi, đây là phần tử sơ cấp duy nhất được dùng không thể thay "
      "thế. Hệ số lưu lượng của nó áp dụng cho phạm vi rộng của tỷ số áp suất. "
      "Nó rẻ hơn ống Venturi. Việc lắp lại trên đường ống hiện có không khó. "
      "Tổn thất áp suất của nó nhỏ hơn tấm lỗ.",
      "Gun metal, stainless steel (AISI 304, 316 or 316 L varieties) or monel "
      "metal are some of the materials that a flow nozzles are made of. For "
      "steam flow measurement services, this is the only primary flow element "
      "which is used invariably. Its discharge coefficient applies over a "
      "wide range of pressure ratio. This is less expensive than a venturi "
      "tube. The reinstallation on existing pipeline is not difficult. The "
      "pressure loss is less than an orifice plate.")

    # ----------------------------------------- 5. Variable Areameter / Rotameter
    H(b, lang, "5. Đồng hồ diện tích thay đổi / Rotameter",
      "5. Variable Areameters or Rotameter", level=4)

    P(b, lang,
      "Rotameter được phát minh bởi ROTA, người đi đầu trong nguyên lý đo "
      "lưu lượng này. Rotameter là thiết bị đo lưu lượng nhỏ, đơn giản. Độ chính "
      "xác tuy kém nhưng nó rất hữu ích làm đồng hồ đo lượng khí thổi "
      "(purgemeter), nơi độ chính xác không phải là yếu tố quyết định.",
      "Rotameter was invented by ROTA who was the main person behind this "
      "principle of flow measurement. Rotameter is a simple, low flow "
      "measurement equipment. The accuracy is however poor but very useful "
      "for purgemeter where accuracy is not a deciding factor.")
    H(b, lang, "Lý thuyết rotameter", "Theory of Rotameter", level=4)
    L(b, lang,
      ["Q = lưu lượng chất lỏng qua rotameter (m³/h)",
       "C = hệ số lưu lượng (phụ thuộc hình dạng phao và Rd)",
       "A = diện tích tiết diện giữa ống và phao (m²)",
       "A_f = diện tích ép của phao (m²)",
       "g = gia tốc trọng trường (m/h²)",
       "r_f và r₀ = trọng lượng riêng của phao và của chất lỏng (kg/m³)",
       "p₁ và p₂ = áp suất thượng lưu và hạ lưu (kg/m²)",
       "V = vận tốc trung bình của chất lỏng (m/h)",
       "h = chênh áp qua phao",
       "L_f = chiều dài phao hình trụ (m)",
       "μ = độ nhớt của chất lỏng (Poise)",
       "R_d = số Reynolds",
       "D_eq = đường kính tương đương của khe hình khuyên phía trên phao ở "
       "lưu lượng cực đại (m)",
       "D = đường kính ống tại vạch lưu lượng cực đại (m)",
       "d_f = đường kính phao = đường kính ống tại vạch lưu lượng bằng không (0)"],
      ["Q = Flow rate of fluid through rotameter (m3/hr)",
       "C = Discharge of coefficient (depends upon float shape and Rd)",
       "A = Sectional area between tube and float (m2)",
       "A_f = Pressed area of float (m2)",
       "g = Acceleration due to gravity (m/hr2)",
       "r_f and r₀ = sp. wt. of float and fluid respectively (kg/m3)",
       "p₁ and p₂ = Upstream and downstream pressure (kg/m2)",
       "V = Average fluid velocity (m/hr)",
       "h = Pressure differential across float",
       "L_f = Length of cylindrical float (m)",
       "μ = Viscosity of fluid (Poise)",
       "R_d = Reynolds number",
       "D_eq = Equivalent diameter of the annular space on top of the float "
       "for maximum flow (m)",
       "D = Diameter of tube at maximum flow mark (m)",
       "d_f = Diameter of float = Diameter of tube at zero (0) flow mark"])
    FIG(b, 37, F.fig_f37(), lang)
    L(b, lang,
      ["Trọng lượng của phao = V_f r_f",
       "Lực đẩy lên do trọng lượng chất lỏng bị phao chiếm chỗ = V_f r₀",
       "Lực chênh áp tác dụng lên bề mặt phao (mặt trên và mặt dưới) = "
       "(p₁ − p₂) A_f"],
      ["Weight of the float = V_f r_f",
       "Upward thrust due to the weight of fluid displaced by the float = V_f r₀",
       "Differential force acting on the surface of the float (upper side and "
       "lower side) = (p₁ − p₂) A_f"])
    P(b, lang,
      "Như Hình 3.37, phao treo ở trạng thái cân bằng dưới tác dụng của các lực "
      "kể trên. Tại điểm cân bằng: V_f r_f = (p₁ − p₂) A_f + V_f r₀, hay:",
      "Refer to Figure 3.37 where the float hangs in equilibrium under the "
      "actions of above forces. At equilibrium, V_f r_f = (p₁ − p₂) A_f + "
      "V_f r₀, or")
    E(b, lang, "(p₁ − p₂) = (V_f/A_f)(r_f − r₀)",
      "(p₁ − p₂) = (V_f/A_f)(r_f − r₀)", num="3.23")
    E(b, lang, "v² = 2gh", "v² = 2gh", num="3.24")
    E(b, lang, "h = (p₁ − p₂)/r₀", "h = (p₁ − p₂)/r₀", num="3.25")
    P(b, lang, "Do đó:", "Hence,")
    E(b, lang, "V = √[2g(V_f/A_f)((r_f/r₀) − 1)]",
      "V = √[2g(V_f/A_f)((r_f/r₀) − 1)]", num="3.26")
    P(b, lang, "Dựa vào kết quả trên, lưu lượng Q là:",
      "Based on above, the flow rate Q shall be given by:")
    E(b, lang, "Q = C A √[2g(V_f/A_f)((r_f/r₀) − 1)]",
      "Q = C A √[2g(V_f/A_f)((r_f/r₀) − 1)]", num="3.27")
    P(b, lang, "Biểu thức này cho các quan hệ tỷ lệ:",
      "This expression gives the proportionality relations:")
    E(b, lang, "Q ∝ [(r_f − r₀)/r₀]^(1/2)  hoặc  W ∝ [r₀(r_f − r₀)]^(1/2)",
      "Q ∝ [(r_f − r₀)/r₀]^(1/2)  or  W ∝ [r₀(r_f − r₀)]^(1/2)", num="3.28")
    P(b, lang,
      "Nếu giả thiết phao hình trụ thì L_f = V_f/A_f. Số Reynolds R_d được cho "
      "bởi:",
      "If we assume the float to be cylindrical, L_f = V_f/A_f. The Reynolds "
      "number R_d shall be given by:")
    E(b, lang, "R_d = (D_eq × V × r₀)/μ = 3.54 W/(μ D_eq)",
      "R_d = (D_eq × V × r₀)/μ = 3.54 W/(μ D_eq)", num="3.29")
    NOTE(b, lang, "Ở đây D_eq tính bằng mm và W tính bằng kg/hr.",
         "Here D_eq is in mm and W is in kg/hr.")
    E(b, lang, "R_d = (3.54 × Q × r₀)/(μ D_eq)",
      "R_d = (3.54 × Q × r₀)/(μ D_eq)", num="3.30")
    P(b, lang,
      "Hằng số lưu lượng C của đồng hồ dạng areameter thay đổi trong khoảng "
      "0.6 đến 0.8. Một điểm quan trọng nữa là với lưu lượng khối không đổi "
      "thì r_f = 2r₀; điều này có được bằng cách lấy đạo hàm biểu thức 3.28 "
      "theo r₀ rồi cho bằng không: dW/dr₀ = (r_f − 2r₀) = 0 (vì W không đổi), "
      "suy ra:",
      "The discharge constant C for an areameter instrument varies in between "
      "0.6 and 0.8. Another important point is that for constant mass flow "
      "rate, r_f = 2r₀, which can be obtained by differentiating expression "
      "3.28 with respect to r₀ and equating the same to zero as follows: "
      "dW/dr₀ = (r_f − 2r₀) = 0 (Since W is constant), or")
    E(b, lang, "r_f = 2r₀", "r_f = 2r₀", num="3.31")
    P(b, lang,
      "Rotameter thường được hiệu chuẩn và sử dụng cho một chất lỏng cụ thể. "
      "Nếu đổi chất lỏng thì áp dụng hệ số hiệu chỉnh sau:",
      "A rotameter is generally calibrated and applied for a particular "
      "fluid. If the fluid changes, a correction factor shall apply which is "
      "given below:")
    E(b, lang, "Q₂/Q₁ = √(r₁/r₂)", "Q₂/Q₁ = √(r₁/r₂)", num="3.32")
    P(b, lang,
      "Trong đó Q₁ và Q₂ là lưu lượng của chất lỏng ban đầu và chất lỏng mới; "
      "tương tự r₁ và r₂ là trọng lượng riêng của chất lỏng ban đầu và chất "
      "lỏng mới. Để đổi năng suất của rotameter chỉ cần đổi phao: giữ nguyên "
      "hình dạng phao gốc và chỉ đổi vật liệu chế tạo (vật liệu có trọng lượng "
      "riêng cao hơn hoặc thấp hơn). Năng suất của rotameter thực tế dao động "
      "từ mức thấp 2 đến 20 lít/giờ đối với dòng nước đến 1.500 lít/giờ đối "
      "với dòng khí. Kích thước ống danh nghĩa từ 3 mm đến 150 mm.",
      "where Q₁ and Q₂ are flow rates of original fluid and the new fluid "
      "respectively. Similarly, r₁ and r₂ are the specific weights of original "
      "fluid and the new fluid respectively. For changing capacity of "
      "rotameter, the float has to be changed only. The shape of the original "
      "float is kept same, the material of construction is changed (material "
      "of higher or lower specific weight) only. The capacity of practical "
      "rotameter ranges from a low value of 2 to 20 litres per hour of "
      "waterflow upto 1500 litres per hour of airflow. The nominal pipe size "
      "is from 3 mm to 150 mm.")

    # ------------------------------------------- 6. Magnetic Flowmeter
    H(b, lang, "6. Đồng hồ lưu lượng từ tính", "6. Magnetic Flowmeter", level=4)

    P(b, lang,
      "Đồng hồ lưu lượng từ tính hoạt động theo định luật cảm ứng Faraday. "
      "Chuyển động tương đối của vật dẫn so với từ trường nằm vuông góc với "
      "nó sẽ sinh ra một suất điện động (emf). Suất điện động này có thể thu "
      "nhận bằng cách bố trí thích hợp như Hình 3.38.",
      "Magnetic flowmeter works on the principle of Faradays law of induction. "
      "The relative motion of conductor with respect to the magnetic field "
      "located at right angle to one another induces an emf. The induced emf "
      "can be collected by means of suitable arrangement as shown in Figure "
      "3.38.")
    FIG(b, 38, F.fig_f38(), lang)
    P(b, lang,
      "Thiết bị thực tế gồm một đoạn ống cách điện cùng với một cặp điện cực "
      "đặt ở hai đầu đối diện của ống. Các điện cực được lắp bằng phẳng với "
      "thành trong của ống. Các cuộn dây chính được quấn quanh ống sao cho từ "
      "trường được tạo ra trên một mặt phẳng vuông góc với trục thiết bị và "
      "với các điện cực. Chất lỏng chảy được xem như một bó dẫn song song "
      "chuyển động dưới tác dụng của từ trường với các vận tốc khác nhau trên "
      "toàn bộ tiết diện ống. Suất điện động do các dẫn giả định chuyển động "
      "này sinh ra thực chất là suất điện động trung bình, và điện áp tức thời "
      "toàn phần tỷ lệ trực tiếp với vận tốc trung bình của chất lỏng. Điều "
      "này phản ánh đúng lưu lượng thể tích.",
      "The actual instrument consists of a portion of an insulating pipe "
      "along with a pair of electrodes placed at the opposite end of the "
      "pipe. The electrodes are mounted flush with respect to the inner wall "
      "of the pipe. The main coils are wound arround the pipe so that the "
      "magnetic field is produced on a plane which is mutually perpendicular "
      "to the axis of the instrument and the electrodes. The flowing fluid is "
      "considered here a bundle of parallel conductors moving under the "
      "influence of magnetic field with different velocities that change "
      "across the entire cross-section of the pipe. The emf induced by the "
      "moving imaginary conductors is in fact the average emf and the total "
      "instantaneous voltage thus produced is directly proportional to the "
      "average velocity of the flowing fluid. This represents a true picture "
      "of volume flow rate.")
    E(b, lang, "e = d v B", "e = d v B", num="3.33")
    P(b, lang,
      "Trong đó V là vận tốc trung bình của chất lỏng cắt qua điện cực; B là "
      "mật độ thông lượng từ và d là đường kính trong của ống đo.",
      "where V is the average velocity of the fluid crossing the electrode; B "
      "is the magnetic flux density and d is internal diameter of measuring "
      "tube.")
    P(b, lang,
      "Vì tín hiệu đầu ra tỷ lệ với vận tốc trung bình, chế độ chảy tầng hay "
      "rối không ảnh hưởng gì. Phép đo không phụ thuộc vào độ nhớt, mật độ, "
      "nhiệt độ và áp suất. Nó cũng không phụ thuộc vào độ dẫn của chất lỏng "
      "một khi đã đạt đến một giá trị dẫn tối thiểu. Giá trị nhỏ nhất này thay "
      "đổi từ 20 micro mho xu tới 0.1 micro mho, tùy theo khả năng xử lý các "
      "cường độ tín hiệu khác nhau của thiết bị giao tiếp.",
      "Since the output signal is proportional to the average velocity, it "
      "does not matter whether the flow is laminar or turbulent. The "
      "measurement is independent of viscosity, density, temperature and "
      "pressure. It is also independent of the conductivity of the fluid once "
      "a minimum conductivity value has been reached. The minimum value "
      "varies from 20 micro mho down to 0.1 micro mho, depending upon the "
      "capacity of the interfacing equipment to handle various signal "
      "strength.")
    P(b, lang,
      "Ống đo được lót gốm để có khả năng chống ăn mòn và độ bền cơ học cao. "
      "Các điện cực dạng tiếp xúc (wetted type) không rò rỉ nhờ khe hở nhỏ "
      "nhất giữa điện cực và thành ống. Các điện cực điện dung dạng không tiếp "
      "xúc được lắp bên ngoài ống đo gốm. Kích cỡ có sẵn của đồng hồ lưu lượng "
      "từ tính từ 0.1 inch đến 100 inch đường kính với nhiều lựa chọn vật liệu "
      "chế tạo. Độ chính xác đạt được từ ± 0.5 đến ± 2% và phạm vi đo từ 20:1 "
      "đến 30:1.",
      "The measurement tube is given ceramic lining to have superior "
      "corrosion resistance and mechanical strength. Electrodes (wetted "
      "type) become leak-free due to minimum clearance between electrode and "
      "the tube-wall. The non-wetted type capacitance electrodes are installed "
      "outside the ceramic measurement tube. The available sizes of magnetic "
      "flowmeters are from 0.1 inch to 100 inches diameter with wide choice "
      "of material of construction. Obtainable accuracy is from ± 0.5 to ± 2% "
      "and rangeability from 20 : 1 to 30 : 1.")
    P(b, lang,
      "Trên góc độ ứng dụng công nghiệp, các đặc điểm nổi bật của đồng hồ lưu "
      "lượng từ tính là:",
      "On industrial application point of view, following are the salient "
      "features of magnetic flowmeter:")
    L(b, lang,
      ["Hoàn toàn không có vật cản đối với dòng chảy của chất lỏng.",
       "Tổn thất áp suất qua thiết bị là nhỏ nhất có thể.",
       "Đo dễ dàng các chất lỏng khó như bùn, chất ăn mòn, chất mài mòn và các "
       "chất khác.",
       "Vì phép đo dựa trên khái niệm vận tốc trung bình, hình học đường ống "
       "không ảnh hưởng lớn.",
       "Có thể đo dòng chảy theo cả hai hướng chỉ bằng cách đảo mối nối.",
       "Độ nhớt, mật độ, nhiệt độ, áp suất và cả độ rối hoàn toàn không ảnh "
       "hưởng đến độ chính xác."],
      ["There is absolutely no obstruction to the flow of fluid.",
       "There has been minimum possible loss of pressure across the instrument.",
       "Measurement of difficult fluids like slurries, corrosives, abrasives "
       "and others is easy.",
       "Since the measurement is based upon average velocity concept, piping "
       "geometry is not critical.",
       "Measurement of flow in both the directions is possible by reversing "
       "the connections only.",
       "Viscosity, density, temperature, pressure and also turbulence have "
       "absolutely no effect on the accuracy."], ordered=True)
    P(b, lang, "Tuy nhiên cũng phải tuân theo một số biện pháp phòng ngừa:",
      "However, certain precautions also have to be followed:")
    L(b, lang,
      ["Độ dẫn của chất lỏng chảy phải nằm trong khoảng 0.1 đến 20 μ (micromho).",
       "Thiết bị phải được đầy hoàn toàn trong lúc đo.",
       "Không được có bọt khí cuốn theo, nếu không sẽ gây sai số đo.",
       "Phải vệ sinh các điện cực định kỳ."],
      ["Conductivity of the flowing fluid must be between 0.1 and 20 μ "
       "(micromho).",
       "The instrument must be completely filled during the metering.",
       "There must not be any gas bubble entrained otherwise error in "
       "measurement will result.",
       "Electrodes must be cleaned periodically."], ordered=True)

    # ------------------------------------------- 7. Turbine Flowmeter
    H(b, lang, "7. Đồng hồ lưu lượng tuabin", "7. Turbine Flowmeter", level=4)

    P(b, lang,
      "Đồng hồ lưu lượng tuabin gồm các cánh tuabin gắn trên chu vi của một "
      "bánh xe, và cụm này quay tự do bên trong ống dẫn quanh đường tâm như "
      "Hình 3.39. Vận tốc của chất lỏng chảy trong ống tạo lực tiếp tuyến tác "
      "dụng lên các cánh, gây chuyển động quay. Tốc độ của cánh tỷ lệ trực "
      "tiếp với lưu lượng. Một cuộn dây cảm nhận từ tính được bố trí trên ống "
      "sao cho mỗi lần cánh đi qua cuộn sẽ sinh ra một xung điện áp xoay chiều "
      "đại diện cho một lượng chất lỏng xác định đi qua. Bộ đếm thích hợp có "
      "thể đếm các xung này và thể hiện lưu lượng tích lũy rất dễ dàng.",
      "Turbine flowmeter consists of turbine blades fixed on the periphery of "
      "a wheel and this assembly is free to rotate inside a flow tube about "
      "its centreline as shown in Figure 3.39. The velocity of the fluid "
      "flowing inside the flow tube creates tangential force and acts on to "
      "the blades resulting in a rotatory motion. The speed of the blade is "
      "directly proportional to the rate of flow. A magnetic pick-up coil is "
      "arranged on the flow tube in such a way that as the blade crosses the "
      "pick-up coil, one pulse of A.C. voltage is induced which represents a "
      "fixed/known quantity of the fluid crossing through. A suitable counter "
      "can count these flow pulses and a totalized flow can be presented very "
      "easily.")
    FIG(b, 39, F.fig_f39(), lang)
    P(b, lang,
      "Độ chính xác của thiết bị phụ thuộc vào mối quan hệ giữa cấu tạo cánh "
      "và kiểu dòng chảy. Số xung sinh ra trên mỗi gallon lưu lượng là yếu tố "
      "mô tả năng suất và đặc tính lưu lượng của đồng hồ tuabin, gọi là hệ số "
      "K. Các đường cong hệ số K liên quan được thể hiện trong Hình 3.40. "
      "Các đường cong này cho thấy mối quan hệ thỏa đáng giữa lưu lượng và "
      "các biến khác như trên sơ đồ. Độ chính xác từ ± 0.25% đến ± 0.5%.",
      "Accuracy of such instrument depends upon the relationship between the "
      "construction of the blade and the flow pattern. The number of pulses "
      "generated per gallon of flow is a factor which describes the capacity "
      "and the flow characteristics of a turbine meter. This is called "
      "K-factor and the related curves which is called K-factor curve has been "
      "shown in Figure 3.40. The curves indicate satisfactory relationship "
      "between flow and other variables as shown in the diagram. The accuracy "
      "is from ± 0.25% to ± 0.5%.")
    FIG(b, 40, F.fig_f40(), lang)
    P(b, lang,
      "Phạm vi đo trong các ứng dụng công nghiệp thông thường nằm giữa 10:1 và "
      "20:1; với ứng dụng quân sự có thể tới 100:1. Độ lặp lại trung bình là "
      "± 0.25% nhưng có thể đạt giá trị cao hơn tới ± 0.02% cho các thiết kế "
      "đặc biệt nếu yêu cầu.",
      "Rangeability of measurement is in between 10 : 1 and 20 : 1 for average "
      "flow ranges in industrial application. For military application it can "
      "go upto 100 : 1. The average repeatability happens to be ± 0.25% but "
      "can attain higher value upto ± 0.02% as well for special designs if "
      "required.")
    P(b, lang,
      "Trong thực tế kỹ sư gặp nhiều khó khăn trong bảo trì đồng hồ lưu lượng "
      "tuabin. Việc đưa thiết bị đo quay vào trong đường ống gây ra những vấn "
      "đề bảo trì rõ ràng. Toàn bộ cơ cấu quay phải chịu tác động của bẩn, "
      "tác dụng xói mòn và ăn mòn của chất lỏng cùng các hạt rắn cuốn theo. "
      "Một điểm quan trọng nữa là ổ bi của cánh tuabin được bôi trơn nhờ đặc "
      "tính bôi trơn của chính chất lỏng. Không phải chất lỏng nào cũng có đủ "
      "đặc tính đó, nên với các chất này người ta dùng bề mặt đánh bóng cao. "
      "Một số vật liệu phi kim được dùng chế tạo ổ bi không bôi trơn, như "
      "Teflon, than chì và gốm. Thực tế hầu hết các công việc bảo trì áp dụng "
      "cho bơm ly tâm và bơm piston cũng được áp dụng cho đồng hồ tuabin. "
      "Không nên dùng đồng hồ lưu lượng tuabin cho chất lỏng bẩn để tránh các "
      "vấn đề bảo trì.",
      "In practice, engineers face a lot of problems in maintaining the "
      "turbine flowmeters. The entry of a rotating measurement equipment into "
      "the pipeline presents some obvious maintenance problems. The complete "
      "rotating mechanism faces the attack of dirts, erosive and corrosive "
      "actions of the fluids, solid particles entrained in the fluid. Another "
      "important point is that the bearing of the rotor blade gets lubrication "
      "from the lubricating property of the fluid. All fluids may not have "
      "that much lubricating property and therefore, for those fluids, highly "
      "polished surfaces are used. Some non-metallic materials are used for "
      "fabricating the non-lubricating bearings. These are Teflon, carbon "
      "graphite, ceramics, etc. In fact, almost all the maintenance practices "
      "that are followed for maintenance of centrifugal and reciprocating "
      "pumps also are followed for the maintenance of turbine flowmeter. It "
      "is advised that turbine flow meters should not be used for dirty "
      "liquids to avert the maintenance problems.")

    # ------------------------------------------- 8. Target Flowmeter
    H(b, lang, "8. Đồng hồ lưu lượng dạng mục tiêu",
      "8. Target Flowmeter", level=4)

    P(b, lang,
      "Đồng hồ lưu lượng dạng mục tiêu gồm một phần tử sơ cấp và một bộ phát "
      "cân bằng lực. Phần tử sơ cấp là một cấu trúc dạng đĩa gọi là mục tiêu "
      "đặt giữa dòng chất lỏng. Mục tiêu tạo thành một lỗ hình khuyên ở vị trí "
      "đường tâm của ống. Phương trình lưu lượng qua đồng hồ dạng mục tiêu "
      "là:",
      "The target flowmeter consists of a primary flow element and a "
      "force-balance transmitter. The primary element in this arrangement is "
      "a disc-shaped structure called target located in the middle of the "
      "fluid stream. The target forms an annular orifice at the centreline "
      "position of the pipe. The equation of flow through the target meter is "
      "given by:")
    E(b, lang, "Q = K√F", "Q = K√F", num="3.34")
    P(b, lang,
      "Trong đó Q là lưu lượng, F là lực tác dụng lên mục tiêu trong khoảng 2 "
      "đến 6 pound và K là hằng số tỷ lệ.",
      "where Q is the rate of flow, F is the force acting on the target ranging "
      "from 2 to 6 pounds and K is proportionality constant.")
    P(b, lang,
      "Bộ phát cân bằng lực tích hợp biến đổi lực này thành tín hiệu khí nén "
      "hoặc điện dùng cho cả ghi chép lẫn điều khiển.",
      "The integral force-balance transmitter converts this force into "
      "pneumatic or electrical output which is used for recording as well as "
      "control purposes.")
    P(b, lang,
      "Việc lắp đặt đồng hồ dạng mục tiêu trở nên đơn giản vì phần tử cảm biến "
      "sơ cấp và bộ phát được kết hợp thành một cụm. Phần tử cảm biến sơ cấp "
      "nằm trong một tấm mỏng (wafer) được lắp giữa hai mặt bích đi kèm trên "
      "đường ống. Với cách lắp này không cần cụm van 3 chiều. Vì loại đồng hồ "
      "này dùng để đo chất lỏng nhớt (dầu nặng), cần kiểm tra và vệ sinh thường "
      "xuyên theo lịch bảo trì. Việc tháo đồng hồ dạng mục tiêu ra khỏi đường "
      "ống để kiểm tra và vệ sinh trở nên dễ dàng nhờ các mặt bích đi kèm.",
      "The installation of target type flowmeter becomes simpler because "
      "primary sensing element and the transmitter are combined in a single "
      "unit. The primary sensing element is contained in a wafer to be mounted "
      "between companion flanges on the pipeline. In this installation 3-way "
      "valve manifold is not required. Since this type of flowmeter is used "
      "for viscous (heavy oil) flow measurement, frequent inspection and "
      "cleaning is required to be done under maintenance schedule. The removal "
      "of the target flowmeter from the pipeline for such inspection and "
      "cleaning become easier from the companion flanges.")
    P(b, lang,
      "Nguyên lý làm việc của bộ phát cân bằng lực tích hợp được chỉ ra trong "
      "Hình 3.41. Lực do chất lỏng chảy tác dụng lên mục tiêu, rồi truyền qua "
      "thanh lực (force bar). Lực này được truyền qua bộ uốn (flexure) tới "
      "thanh tầm (range bar) được bản lề trên bánh xe tầm. Chuyển động của "
      "thanh tầm vận hành hệ thống vòi–cánh (flapper-nozzle) tiêu chuẩn, tạo "
      "tín hiệu khí nén tỷ lệ. Ống đếm phản hồi (feedback bellows) thực hiện "
      "việc cân bằng để giữ thanh lực ở trạng thái cân bằng.",
      "The principle of operation of the integral force-balance transmitter "
      "has been shown in Figure 3.41. The force is exerted on the target by "
      "the flowing fluid and this force acts on the force bar. This force is "
      "transmitted through the flexure to the range bar pivoted on the range "
      "wheel. Movement of the range bar operates the standard flapper-nozzle "
      "system resulting in proportional output pneumatic signal. The feedback "
      "bellows does the balancing work for keeping the force bar under "
      "equilibrium.")
    FIG(b, 41, F.fig_f41(), lang)
    P(b, lang,
      "Độ chính xác của thiết bị tới ± 0.5%. Thiết bị có các kích cỡ ống 2, 3 "
      "và 4 inch. Tỷ số giữa đường kính mục tiêu và đường kính ống từ 0.5 đến "
      "0.8. Nó chịu được áp suất 1500 psig và nhiệt độ 750°C.",
      "The accuracy of this instrument is upto ± 0.5%. This is available in "
      "sizes of 2, 3 and 4 inches pipeline. The ratio of target to pipeline "
      "diameters is from 0.5 to 0.8. It can handle a pressure and temperature "
      "of 1500 psig and 750°C respectively.")
    P(b, lang,
      "Một dạng đồng hồ khác cũng gọi là đồng hồ lưu lượng kiểu cản (drag type "
      "flowmeter) hoạt động theo nguyên lý giống đồng hồ dạng mục tiêu. Trong "
      "thiết kế này lực va chạm tác dụng lên mục tiêu được cảm nhận bằng mạch "
      "cầu đo strain gage. Cách bố trí được chỉ ra trong Hình 3.42. Thiết kế và "
      "lắp đặt sao cho cụm phát có thể lấy ra khỏi đường ống để kiểm tra và vệ "
      "sinh định kỳ.",
      "Another type of flowmeter which is also called drag type flowmeter, "
      "works on the same principle as target flowmeter. In this design the "
      "impact force acting on the target is sensed by a strain gage-bridge "
      "circuitry. The arrangement has been shown in Figure 3.42. The design "
      "and installation are such that the transmitter unit can be taken out "
      "from the pipeline for periodic inspection and cleaning.")
    FIG(b, 42, F.fig_f42(), lang)
    P(b, lang, "Lực cản F của thiết kế này được cho bởi:",
      "The drag force F of this design is given by:")
    E(b, lang, "F = C A ρ (V²/(2g))", "F = C A ρ (V²/(2g))", num="3.35")
    P(b, lang,
      "Trong đó C là hệ số cản; A là diện tích phần cảm biến; ρ là mật độ chất "
      "lỏng và V²/(2g) là cột động áp (velocity head).",
      "where C is the drag coefficient; A is area of the sensing part; ρ is "
      "the fluid density and V²/(2g) is the velocity head.")
    P(b, lang,
      "Độ chính xác của thiết kế này nằm giữa ± 0.5% và ± 3%. Loại dạng ống có "
      "kích cỡ từ 0.5 inch đến 2 inch, dạng lắp bích từ 4 inch đến 60 inch. "
      "Thiết bị chịu được áp suất 5000 psig và nhiệt độ 600°C.",
      "The accuracy obtainable of this design is between ± 0.5% and ± 3%. "
      "These are available in the sizes from 0.5 inch to 2 inches in tube "
      "design and from 4 inches to 60 inches for flange mounting design. It "
      "can handle a pressure and temperature of 5000 psig and 600°C "
      "respectively.")

    # ----------------------------------------------------------- 9. Annubar
    H(b, lang, "9. Annubar", "9. Annubar", level=4)

    P(b, lang,
      "Annubar là cảm biến lưu lượng sơ cấp tiên tiến nhất dùng để đo lưu lượng "
      "chất lỏng, khí và hơi. Nó được thiết kế để tạo ra chênh áp tỷ lệ với "
      "lưu lượng. Có sẵn với kích thước từ 1 inch đến 360 inch, annubar cho độ "
      "chính xác cao và ổn định lâu dài, tổn thất áp suất vĩnh viễn thấp, chi "
      "phí lắp đặt và vận hành thấp.",
      "Annubar is the most advanced primary flow sensor used for liquid, gas "
      "and steam flow measurement. It is designed to produce a differential "
      "pressure which is proportional to flow. Available in size ranging from "
      "1 inch to 360 inches, the annubar provides high as well as long-term "
      "accuracy, low permanent pressure loss, low installed and operating "
      "cost.")
    FIG(b, 43, F.fig_f43(), lang)
    P(b, lang,
      "Annubar làm bằng thép không gỉ AISI 316 gồm chủ yếu bốn phần: (i) cảm "
      "biến, (ii) ống, (iii) cổng sau và (iv) đầu thiết bị (xem Hình 3.43).",
      "Annubar, made of AISI 316 stainless steel consists of mainly four "
      "parts: (i) Sensor, (ii) Tube, (iii) Rear Port, and (iv) Instrument head "
      "(Refer Figure 3.43).")
    P(b, lang,
      "Cảm biến với bốn cổng va chạm áp suất cao hướng về phía thượng lưu của "
      "dòng chảy và cảm nhận áp suất va chạm do vận tốc dòng chảy tạo ra. Bốn "
      "cổng áp suất cao có tiết diện bằng nhau lấy trung bình áp suất va chạm "
      "trên dòng chảy. Ống chịu áp suất va chạm này và sau khi nội suy truyền "
      "áp suất trung bình tới hệ thống đo. Cổng sau nằm ở phía hạ lưu cảm "
      "nhận áp suất thấp. Hiệu của hai áp suất này tỷ lệ với lưu lượng. Đầu "
      "thiết bị, phần trên cùng của cụm, truyền chênh áp tới bộ phát, máy ghi "
      "hoặc bộ điều khiển để xử lý tiếp. Thiết kế cảm biến tạo ra kiểu dòng "
      "chảy đồng đều quanh cảm biến, nhờ vậy có độ chính xác và độ lặp lại "
      "cao.",
      "The sensor with four high pressure impact ports faces the upstream side "
      "of the flow and senses the impact pressure created by the flow "
      "velocity. The four high pressure and equal cross-sectional areas of "
      "the flow stream averages the impact pressure. The tube is acted upon "
      "by this impact pressure and after interpolation transmits the average "
      "pressure to the measuring system. The rear port which is located on "
      "the downstream side of the flow medium, senses the low pressure. The "
      "difference between these two pressures is proportional to flow rate. "
      "The instrument head which is the top portion of the arrangement "
      "transmits their differential pressure to a transmitter, recorder or "
      "controller for further processing. The sensor design is such that it "
      "produces a uniform flow pattern around the sensor resulting in high "
      "accuracy and repeatability.")
    P(b, lang, "Phương trình lưu lượng thủy lực cho cảm biến annubar là:",
      "Hydraulic equation of flow for annubar sensors is given by:")
    E(b, lang, "Q_l = K A √(2g·(d.p.)/ρ)", "Q_l = K A √(2g·(d.p.)/ρ)", num="3.36")
    P(b, lang, "và", "and")
    E(b, lang, "Q_g = K A y √(2g·(d.p.)/ρ)",
      "Q_g = K A y √(2g·(d.p.)/ρ)", num="3.37")
    P(b, lang,
      "Trong đó Q_l và Q_g là lưu lượng thể tích thực tế của chất lỏng và khí "
      "tương ứng, tính bằng ft³/sec; A là diện tích tiết diện ống tính bằng "
      "sq. ft; g là gia tốc trọng trường tính bằng ft/sec²; K là hệ số lưu "
      "lượng; d.p. là chênh áp tính bằng lbf/ft²; ρ là mật độ chất lỏng, tính "
      "bằng lbm/ft³ và y là hệ số giãn nở của khí.",
      "where Q_l and Q_g are actual volume flow rates for liquid and gas "
      "respectively in ft3/sec; A is the cross-sectional area of the pipe in "
      "sq. ft; g is gravitational acceleration in ft/sec2; K is discharge "
      "coefficient; d.p. is differential pressure lbf/ft2; ρ is the density "
      "of the fluid, lbm/ft3 and y is the expansion factor of the gas.")
    P(b, lang,
      "Độ chính xác đo của Annubar, kể cả độ trễ, là ± 1%. Khác với tấm lỗ, "
      "sự mòn bề mặt, vết khía và gờ trên cổng cảm biến có ảnh hưởng không "
      "đáng kể đến độ chính xác của Annubar. Điều này giúp duy trì mức độ cao "
      "và độ ổn định lâu dài của độ chính xác. Độ lặp lại của phép đo Annubar "
      "đã được thử nghiệm ở mức ± 0.1%.",
      "Accuracy of measurement by Annubar which includes hysteresis as well is "
      "± 1%. Unlike orifice plates, surface wear, nicks and burrs on sensor "
      "ports have negligible effects on the accuracy of Annubar. This results "
      "in maintenance of high degree and long-term stability on accuracy. "
      "Repeatability of Annubar measurement have been tested to be ± 0.1%.")

    # ---------------------------------------------- 10. Vortex Flowmeter
    H(b, lang, "10. Đồng hồ lưu lượng xoáy", "10. Vortex Flowmeter", level=4)

    P(b, lang,
      "Đồng hồ lưu lượng xoáy đo lưu lượng theo nguyên lý xoáy KARMAN do vật "
      "tạo xoáy (vortex shredder) sinh ra. Vật tạo xoáy là một vật thể không "
      "đối xứng dạng khối (bluff body) có hình dạng đặc biệt (giống hình thang) "
      "được nhúng hoàn toàn vào dòng chất lỏng như Hình 3.44.",
      "Vortex flowmeter measures flow rate on the principle of KARMAN vortices "
      "produced by vortex shredder. The vortex shredder is an especially "
      "shaped (trapezoidal-like) non-streamlined bluff body submerged "
      "completely in the fluid flow path as shown in Figure 3.44.")
    FIG(b, 44, F.fig_f44(), lang)
    P(b, lang,
      "Có thể hình dung xoáy Karman như chuyển động dao động của một lá cờ "
      "phất trong gió. Đây là quá trình tự nhiên luôn thấy được trong dòng "
      "chảy khi đặt một vật thể dạng khối vào dòng. Tần số của các xoáy này "
      "có quan hệ tỷ lệ xác định với lưu lượng. Nếu vận tốc dòng chảy là v và "
      "bề rộng của vật thể dạng khối hướng trực tiếp vào dòng là D thì tần số "
      "xoáy F được cho bởi:",
      "Karman vortices can be conceived as oscillating motion created by a "
      "flag fluttering in a clear wind. This is a natural process which can "
      "always be seen in a flowing stream whenever a bluff body is put inside "
      "the stream. The frequency of these vortices bear a definite "
      "proportionality relation with flow rate. If the flow velocity is v and "
      "the width of bluff body directly facing the flow stream is D, then the "
      "frequency F of the vortex is given by the expression:")
    E(b, lang, "F = St·v/D", "F = St·v/D", num="3.38")
    P(b, lang,
      "Trong đó St là số Strouhal. Số Strouhal phụ thuộc vào hình dạng của vật "
      "thể dạng khối. Về mặt số học nó bằng tỷ số giữa khoảng cách sinh xoáy "
      "(L) và bề rộng vật thể (D) như Hình 3.45.",
      "where St is Strouhal number. Strouhal number depends upon the shape of "
      "the bluff body. It is numerically equal to ratio between the vortex "
      "produced interval (L) and width of bluff body (D) as shown in Figure "
      "3.45.")
    FIG(b, 45, F.fig_f45(), lang)
    P(b, lang,
      "Nếu số Strouhal không đổi thì có thể dễ dàng tìm vận tốc dòng chảy v "
      "chỉ bằng cách đếm số xoáy. Số Strouhal chỉ được xem là không đổi khi số "
      "Reynolds (R_d) nằm trong một phạm vi xác định. Như Hình 3.46 cho thấy, "
      "phạm vi của R_d rất rộng, nên có thể coi số Strouhal là không đổi. "
      "Lưu lượng đo bằng phương trình 3.38 không phụ thuộc vào áp suất, nhiệt "
      "độ, mật độ và độ nhớt của chất lỏng. Trong một số trường hợp có thể cần "
      "bù áp suất và nhiệt độ khi lưu lượng được đo theo một chuẩn tham chiếu.",
      "If the Strouhal number is constant, then the velocity of flow v, can be "
      "found out easily by counting the number of vortices only. The Strouhal "
      "number can be considered constant only when the Reynolds number (R_d) "
      "is within a specified range. As is indicated in Figure 3.46, the "
      "specified range of R_d is wide and hence the Strouhal number can be "
      "taken as constant. The flow rate measured by the equation 3.38 is "
      "independent of fluid pressure, temperature, density and viscosity. In "
      "some cases compensation for pressure and temperature may be required "
      "when the flow rate is measured with reference to some standard.")
    FIG(b, 46, F.fig_f46(), lang)
    P(b, lang,
      "Trên Hình 3.46, trục St có các vạch 0.1, 0.2 và 0.3; phạm vi đo được "
      "của R_d là từ 5 × 10³ đến 7 × 10⁶, trong khi dải làm việc bình thường "
      "là từ 2 × 10⁴ đến 7 × 10⁶.",
      "In Figure 3.46 the St axis is marked 0.1, 0.2 and 0.3; the measurable "
      "range of R_d is from 5 × 10³ to 7 × 10⁶, while the normal operating "
      "range is from 2 × 10⁴ to 7 × 10⁶.")
    P(b, lang,
      "Vật thể dạng khối làm bằng thép không gỉ AISI 316. Nó bị nâng lên mỗi "
      "khi xoáy được sinh ra. Các lần nâng này tạo ra ứng suất đo được, được "
      "cảm nhận bởi phần tử chuyển đổi áp điện đặt bên trong vật thể. Tín hiệu "
      "điện sinh ra được gửi tới bộ phát, nơi tính toán lưu lượng.",
      "The bluff body is made of AISI 316 stainless steel material. This is "
      "lifted each time the vortices are produced. These lifts create "
      "measurable stress which is detected by piezoelectric transducer element "
      "located inside the bluff body. The electric signals produced is sent to "
      "the transmitter where the flow rate is calculated.")
    P(b, lang,
      "Độ chính xác của đồng hồ lưu lượng xoáy là ± 1% giá trị chỉ thị, tốt hơn "
      "đồng hồ lưu lượng dạng tấm lỗ. Vì đầu ra của đồng hồ xoáy tỷ lệ trực "
      "tiếp với lưu lượng nên thang đo là tuyến tính, trái ngược với thang căn "
      "bậc hai của đồng hồ tấm lỗ. Không có tổn thất áp suất như ở đồng hồ tấm "
      "lỗ.",
      "Accuracy of vortex flowmeter is ± 1% of indicated value which is "
      "superior to orifice flow meters. Since the output of vortex flowmeter "
      "is directly proportional to flow rate, scale is linear which is in "
      "contrast with the square root scale of orifice flowmeter. There is no "
      "pressure loss as is found with orifice flowmeter.")
    P(b, lang,
      "Trong một thiết kế khác, tần số thoát xoáy được cảm nhận bằng một cặp "
      "thermistor nhúng trên mặt thượng lưu. Chúng được đốt nóng bằng điện để "
      "có nhiệt độ cao hơn chất lỏng chảy và cảm nhận hiệu ứng làm nguội của "
      "xoáy thoát ra bằng cách thay đổi nhiệt độ/điện trở ở tần số thoát xoáy "
      "tỷ lệ với lưu lượng.",
      "In another design, the vortex shedding frequency is sensed by a pair "
      "of thermistors embedded in the upstream face. They are heated "
      "electrically to a temperature above that of the flowing fluid and "
      "sense the cooling effect of the vortex shedding by changing "
      "temperature/resistance at the vortex shedding frequency which is "
      "proportional to flow rate.")

    # --------------------------------------------- 11. Mass Flowmeter intro
    H(b, lang, "11. Đồng hồ lưu lượng khối lượng",
      "11. Mass Flowmeter", level=4)

    P(b, lang,
      "Các loại đồng hồ lưu lượng thông thường trong công nghiệp được gọi phổ "
      "biến là đồng hồ lưu lượng thể tích. Nhưng thực tế điều khiển quá trình, "
      "và vì thế cả việc đo các biến của quá trình, liên quan nhiều hơn đến "
      "phương trình cân bằng khối lượng. Do đó đo theo khối lượng có vẻ logic "
      "hơn đo theo thể tích trong điều khiển quá trình. Để điều khiển đúng "
      "quá trình, khối lượng được suy từ lưu lượng thể tích theo áp suất và "
      "nhiệt độ. Công việc này trở nên phức tạp hơn với hệ chất khí so với hệ "
      "chất lỏng.",
      "General type of engineering flowmeters are popularly known as "
      "volumetric flowmeters in the process industries. But the fact is that "
      "the control of processes and therefore, measurement of process variables "
      "as well are more related to mass balance equations. Due to this reason, "
      "mass measurement seems to be more logical for process control than "
      "volume measurement. For proper control of the processes, the mass is "
      "inferred from the volume flow rate with respect to pressure and "
      "temperature. The work becomes more tedious in case of gas flow system "
      "than with the liquid flow system.")
    P(b, lang,
      "Đo khối lượng được thực hiện trực tiếp vì đây là chuẩn cơ bản và lý "
      "tưởng, hoàn toàn không bị ảnh hưởng bởi thay đổi của nhiệt độ, áp suất, "
      "mật độ, độ nhớt và độ dẫn. Đặc điểm thiết kế của đồng hồ lưu lượng khối "
      "lượng dựa trên một hiện tượng tự nhiên gọi là hiệu ứng Coriolis. Chính "
      "hiệu ứng Coriolis giải thích sự cong của quỹ đạo của một vật chuyển "
      "động tự do trên bề mặt trái đất. Thiết bị chế tạo theo nguyên lý này "
      "gọi là đồng hồ lưu lượng khối lượng hiệu ứng Coriolis/Con quay.",
      "Mass measurement is done directly because this is the basic and ideal "
      "standard which is not affected at all by changes in temperature, "
      "pressure, density, viscosity and conductivity. Design features of mass "
      "flowmeter are based upon a natural phenomenon called coriolis effect. "
      "It is the coriolis effect that the curvature appearance of a freely "
      "moving object on the surface of the earth can be attributed to. The "
      "instrument so designed is called coriolis/Gyroscopic Effect Mass "
      "Flowmeter.")
    FIG(b, 47, F.fig_f47(), lang)
    P(b, lang,
      "Việc xác định chính xác lượng khối lượng chảy qua đồng hồ được thực "
      "hiện theo định luật II Newton về chuyển động. Hình 3.47 cho thấy một cụm "
      "ống dẫn bên trong bộ cảm biến.",
      "Determination of exact amount of mass flowing through the meter is done "
      "by Newtons second law of motion. Figure 3.47 shows a flow tube "
      "assembly.")

    return b
