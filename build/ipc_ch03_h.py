# -*- coding: utf-8 -*-
"""Chapter 3, section 3.4 "Measurement of Level" (EN/VI bilingual) — part h.

Source: Prasad, Jayaswal & Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 195-202, printed pp. 183-190,
decoded text lines 7428-7719.  The section heading, definition and the first
sight-glass paragraph are in module `ipc_ch03_g`; this module continues with
the industrial method list, reflex/gage glasses, the resistivity boiler
system, float and cable, purge/bubble, displacer/buoyancy (equation 3.44)
and the opening of the differential-pressure method.  Figures 3.54-3.61 are
redrawn in the `ipcfig3` supplier modules.
"""

import ipcfig3 as F
from ipc_ch03_lib import H, P, L, E, FIG, TBL, NOTE


# Stand-ins let this prose module be imported and QA'd while the c/d figure
# suppliers are still being written.  As soon as those suppliers register the
# real drawings these entries are ignored (and never overwrite them).
_FIG_SUBJECTS = {
    54: ("Kính phản xạ và bu lông chữ U", "Reflex gage glass and U-bolt"),
    55: ("Kính đo mức trên buồng cách nhiệt", "Gage glass on insulated chamber"),
    56: ("Cột cân bằng nhiệt và chỉ thị mức từ xa",
         "Temperature equalizing column and remote indicator"),
    57: ("Hệ thống đo mức nồi hơi theo điện trở suất",
         "Resistivity boiler level measurement system"),
    58: ("Cột nước với đầu dò và hộp kết nối",
         "Water column with probes and junction box"),
    59: ("Phao, cáp xích và quả nặng", "Float, chain cable and weight"),
    60: ("Hệ thống thổi khí và rotameter", "Purge system and purge rotameter"),
    61: ("Vật dịch chỗ và cụm ống xoắn", "Displacer and torque tube assembly"),
}

for _n, (_vi, _en) in _FIG_SUBJECTS.items():
    if not hasattr(F, "fig_f%02d" % _n):
        _svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 250">'
                '<rect x="60" y="30" width="560" height="170" rx="8" '
                'fill="none" stroke="#333" stroke-width="2"/>'
                '<text x="340" y="125" text-anchor="middle" font-size="18">'
                'Figure 3.%d</text></svg>' % _n)
        setattr(F, "fig_f%02d" % _n,
                (lambda t=_svg, v=_vi, e=_en, n=_n:
                 (t, "Hình 3.%d %s" % (n, v), "Figure 3.%d %s" % (n, e),
                  "Hình 3.%d %s" % (n, v), "Figure 3.%d %s" % (n, e))))


def section(lang):
    b = []

    # --------------------------------------------------- continuation of 3.4
    P(b, lang,
      "Do đó, mức trở thành một trong bốn biến cơ bản (áp suất, nhiệt độ, lưu "
      "lượng, mức) quan trọng nhất cho bất kỳ hoạt động công đoạn nào trong "
      "nhà máy chế biến. Trong một số trường hợp, hai chất lỏng không trộn lẫn "
      "cũng tạo ra mặt phân cách. Trong nồi hơi sinh hơi, sự có mặt của hơi "
      "bão hòa cùng với nước cấp lò hơi có áp suất trong trống tạo ra mặt phân "
      "cách động giữa hơi và các bọt nước. Việc đo mức chính là đo mặt phân "
      "cách này một cách cẩn thận.",
      "Therefore, the level becomes one of the four basic variables (pressure, "
      "temperature, flow, level) that are most important for any unit operation "
      "activity run in any process plant. In some cases two immiscible liquids "
      "also create an interface. In steam generating boiler, presence of "
      "saturated steam along with pressurized boiler feed water in the drum "
      "makes a dynamic interface of steam and water bubbles. The measurement of "
      "level constitutes the measurement of this interface carefully.")

    P(b, lang,
      "Các phương pháp công nghiệp phổ biến nhất hiện có để đo mức gồm:",
      "The most common industrial methods available for measurement of level "
      "are following:")

    L(b, lang,
      ["(i) Kính nhìn mức/kính đo mức",
       "(ii) Phao và cáp",
       "(iii) Hệ thống thổi/bọt khí",
       "(iv) Vật dịch chỗ/lực đẩy nổi",
       "(v) Kiểu chênh áp",
       "(vi) Kiểu điện dung",
       "(vii) Cột đo mức từ tính",
       "(viii) Kiểu phóng xạ hạt nhân"],
      ["(i) Sight glass/gage glass",
       "(ii) Float and cable",
       "(iii) Purge/bubble system",
       "(iv) Displacer/buoyancy type",
       "(v) Differential pressure type",
       "(vi) Capacitance type",
       "(vii) Magnetic level gage",
       "(viii) Nucleonic type"],
      ordered=True)

    # ------------------------------------------------ (i) sight/gage glass
    P(b, lang,
      "<b>(i) Kính nhìn/kính đo mức (tiếp).</b> Đối với ứng dụng áp suất cao "
      "hơn, đặc biệt trong nồi hơi công nghệ và nồi hơi dịch vụ, người ta dùng "
      "kính phản xạ cho kính chỉ thị mức. Kính phản xạ thường là kính cường "
      "lực, được lồng vào thân kim loại của bộ chỉ thị nhờ đệm làm kín thấm "
      "kim loại và bu lông chữ U, như Hình 3.54. Kính đo mức được thể hiện "
      "trên Hình 3.55.",
      "<b>(i) Sight glass/gage glass (continued).</b> For higher pressure "
      "applications and especially in process boilers as well as service "
      "boilers reflex glasses are used for gage glasses indicator. The reflex "
      "glass which is generally a tempered glass is boxed-up on the metallic "
      "indicator by means of suitable metal impregnated gasket and U-bolt as "
      "shown in Figure 3.54. The gage glass has been shown in Figure 3.55.")

    FIG(b, 54, F.fig_f54(), lang)
    FIG(b, 55, F.fig_f55(), lang)

    P(b, lang,
      "Ngày nay, theo quy định bắt buộc của các quy tắc an toàn, nhà chế tạo "
      "và người sử dụng nồi hơi phải coi kính đo mức là tiêu chuẩn vận hành "
      "để đối chiếu độ chính xác và an toàn của các thiết bị đo mức khác. "
      "Rất tiếc là kính đo mức dạng này không lưu lại bản ghi mức, vì vậy "
      "người ta lắp thêm thiết bị khác để ghi lại mức.",
      "Nowadays, it has become statutory obligation under safety codes that "
      "boiler manufacturers and users consider the gage glass as the operating "
      "standard with respect to which other level measurement instruments "
      "shall be compared for accuracy and safety. It is very unfortunate that "
      "this type of gage glass does not provide record of level and therefore, "
      "additional instruments are installed for obtaining record of level.")

    P(b, lang,
      "Khi chỉ thị mức chất lỏng ở nhiệt độ môi trường, không cần hiệu chỉnh. "
      "Nhưng khi đo mức ở nhiệt độ và áp suất cao (mức nước trong trống nồi "
      "hơi), cần tính đến hiệu chỉnh mật độ tương ứng với điều kiện vận hành. "
      "Để giữ đầu lấy mẫu nước và hơi ở cùng nhiệt độ, người ta dùng cột cân "
      "bằng nhiệt. Cột này được dùng trong lắp đặt điển hình của chỉ thị mức "
      "từ xa như Hình 3.56.",
      "For liquid level indication at ambient temperature application, no "
      "correction is required. But for measurement of level at high temperature "
      "and pressure (boiler water level inside the drum) allowance for density "
      "correction corresponding to operating conditions becomes desirable. For "
      "keeping water and the steam tapping at the same temperature, a "
      "temperature equalizing column is used. Such equalizing column has been "
      "used on a typical installation of remote level indicator as shown in "
      "Figure 3.56.")

    FIG(b, 56, F.fig_f56(), lang)

    P(b, lang,
      "Phần chỉ thị của thiết bị được lắp trên sàn vận hành hoặc sàn phòng "
      "điều khiển của nhà nồi hơi. Để giữ các đầu lấy mẫu của kính đo mức ở "
      "cùng nhiệt độ (Hình 3.56), người ta bọc cách nhiệt bằng len thủy tinh. "
      "Điều này làm giảm khả năng rò rỉ tại van và phụ tùng do đảo ngược "
      "nhiệt độ.",
      "Indicator portion of this unit is installed on the firing floor or the "
      "control room floor of the boiler house. For keeping the gage glass "
      "tappings at the same temperature (Fig. 3.56), the glass-wool insulation "
      "is provided. This reduces the possibility of leakage on the valves and "
      "fittings due to temperature reversals.")

    P(b, lang,
      "Một hệ thống đo mức nồi hơi hiện đại hơn trong dòng thiết bị kính đo "
      "mức dựa trên sự khác biệt về điện trở suất giữa nước cấp lò hơi (BFW) "
      "tinh khiết cao và hơi bão hòa. Các điện cực dẫn điện được cách điện "
      "xuyên qua cột nước vào môi trường chất lỏng. Cột nước tạo thành một tế "
      "bào điện trở, nối với phần tử điện trở chuẩn đặt trong hộp phát hiện "
      "điện tử, tạo thành mạch chia điện trở. Toàn bộ hệ thống gồm ba bộ phận "
      "chính nối nhau bằng cáp điện như Hình 3.57.",
      "Yet another, the most modern boiler level measurement system in the "
      "line of gage glass is based on difference in resistivity between high "
      "purity BFW (Boiler Feed Water) and saturated steam. The conducting "
      "electrodes which are insulated protrude through the water column into "
      "the fluid medium. The water column which forms a resistivity cell is "
      "connected with reference resistor element located inside electronic "
      "detection box and constitutes a resistance divider network. The "
      "complete system which consists of three main units connected with "
      "electric cable as shown in Figure 3.57.")

    FIG(b, 57, F.fig_f57(), lang)

    L(b, lang,
      ["(a) Cột nước với đầu dò",
       "(b) Hộp phát hiện",
       "(c) Bộ hiển thị"],
      ["(a) water column with probe",
       "(b) detection box",
       "(c) display unit"],
      ordered=True)

    H(b, lang, "(a) Cột nước với đầu dò", "(a) Water column with probe", level=4)

    P(b, lang,
      "Bộ phận này nối với trống nồi hơi qua van cô lập ở cả hai đầu lấy mẫu. "
      "Bộ phận chứa tất cả các đầu dò dẫn điện được bố trí đối diện nhau và "
      "cách đều để có độ phân giải tối ưu trong dải vận hành của thiết bị và "
      "tại các điểm báo động đã chọn. Các đầu dò được đấu sẵn dây tới hộp kết "
      "nối lắp trên cột nước như Hình 3.58.",
      "This unit is connected to the boiler drum by means of isolation valves "
      "on both the tappings. This unit holds all the conducting probes which "
      "are fixed one facing to other and are suitably spaced to provide "
      "optimum resolution over the operating range of the equipment and "
      "selected alarm points. The probes are pre-wired to a junction box "
      "installed on the water column as shown in Figure 3.58.")

    FIG(b, 58, F.fig_f58(), lang)

    H(b, lang, "(b) Hộp phát hiện", "(b) Detection box", level=4)

    P(b, lang,
      "Hộp phát hiện được đặt trong tủ, lắp ở mặt sau của phòng điều khiển "
      "trung tâm và nhận tín hiệu điện do các đầu dò dẫn điện tạo ra. Mạch "
      "phát hiện trong hộp hoạt động với hệ xung ± 6 vôn. Mạch này cho phép "
      "phát hiện độ dẫn thấp tới 1 micro mho bằng kỹ thuật một chiều. Đặc "
      "tính nổi bật nhất của toàn hệ thống là có thể tạo ra tín hiệu một "
      "chiều 4 đến 20 mA tỷ lệ thuận với mức trong trống, nhờ đó có bản ghi "
      "mức liên tục. Bộ phận này cũng tạo tín hiệu báo động mức thấp và mức "
      "cao.",
      "The detection box which is cabinet-enclosed is installed on the "
      "backside of the central control room receives the electrical signals "
      "generated by the conducting probes. The detection circuit, located on "
      "the detection box, is operated upon by ± 6 volts pulse system. This "
      "circuit makes possible the detection of low conductivity of 1 micro mho "
      "using D.C. technique. The most fascinating feature of the entire system "
      "is that it can generate 4 to 20 mAmps. D.C. also which will be "
      "proportional to the level of the drum and this way we can have a "
      "continuous record of the level. Low- and high-level alarm signals are "
      "also generated by this unit.")

    H(b, lang, "(c) Bộ hiển thị", "(c) Display unit", level=4)

    P(b, lang,
      "Bộ hiển thị là chỉ thị từ xa lắp trên bảng mặt trước của phòng điều "
      "khiển trung tâm. Bộ này nối với hộp phát hiện bằng cáp nhiều dẫn. Màn "
      "hình được chiếu sáng từ sau bằng loạt đèn LED (Light Emitting Diode) "
      "trạng thái rắn, tuổi thọ cao, hai màu. Các báo động mức thấp và mức "
      "cao cũng được chỉ thị bằng đèn.",
      "The display unit is a remote indicator installed on the front panel of "
      "the central control room. This unit is interconnected to the detection "
      "box by a multi-conductor cable. The display is back-lighted with a "
      "series of two colour solid state long life LED (Light Emitting Diode) "
      "indicators. Low-level, high-level alarms are also indicated by light "
      "indicator.")

    P(b, lang,
      "Điều đáng chú ý là hỏng một hoặc hai đầu dò không làm thiết bị ngừng "
      "hoạt động. Việc bảo trì ít hơn và hệ thống đáp ứng quy tắc nồi hơi "
      "ASME.",
      "Important fact is that failure of one probe or two does not stop "
      "functioning of the instrument. Maintenance is less and the system "
      "complies with ASME boiler code.")

    # -------------------------------------------------- (ii) float and cable
    H(b, lang, "(ii) Phao và cáp", "(ii) Float and cable", level=3)

    P(b, lang,
      "Mức chất lỏng trong bình hở có thể đo bằng cơ cấu cơ khí gồm phao và "
      "cáp. Phao nổi trên mặt chất lỏng và thay đổi vị trí theo sự dâng lên "
      "hay hạ xuống của mức chất lỏng. Cáp về cơ bản là một dạng xích kim "
      "loại, nối với quả nặng ở một đầu và với phao ở đầu kia, như Hình 3.59.",
      "Measurement of liquid level of an open tank can be done by the "
      "mechanical arrangement consisting of float and cable. The float rides "
      "on the surface of the liquid and changes its position according to the "
      "rise and fall of the liquid level. The cable which is essentially a "
      "metallic chain type of article and is connected to a weight of one end "
      "and to the float at the other end as shown in Figure 3.59.")

    FIG(b, 59, F.fig_f59(), lang)

    P(b, lang,
      "Dải ứng dụng của hệ thống đo này tới 50 feet hoặc hơn. Hầu hết chất "
      "lưu công nghệ ổn định trong nhà máy, thậm chí cả bể nước cấp sinh hoạt "
      "trên cao, dùng hệ thống này rất hiệu quả. Đặc tính nổi bật nhất là "
      "sự thay đổi mật độ chất lưu không ảnh hưởng đến phép đo, miễn là phao "
      "còn ở trạng thái nổi. Hệ thống rất đơn giản về kết cấu và rẻ tiền.",
      "The application range at such measurement system is upto 50 feet or "
      "even more. Almost all stable process fluids available in a process "
      "plant or even the sanitary water supply overhead tanks use this system "
      "of level measurement very effectively. The most striking feature of "
      "this system is that change in density of the fluid does not have any "
      "effect on the measurement so long the float is on floating condition "
      "on the fluid. The system is very simple in design and inexpensive.")

    P(b, lang,
      "Hạn chế của hệ thống là chất lưu phải sạch. Khi đo mức dầu nặng (dầu "
      "nhớt), cần duy trì độ lưu động đủ mọi lúc, nếu không dầu có thể bám "
      "vào phao làm phao mất độ nhạy.",
      "Limitations imposed on this system are that the system fluid should be "
      "clean. In case of measurement of level of heavy oil (viscous oil), the "
      "requirement for the system is that sufficient fluidity should be "
      "maintained all the time otherwise the oil may stick to the float making "
      "it insensitive.")

    # ------------------------------------------------ (iii) purge/bubble
    H(b, lang, "(iii) Hệ thống thổi/bọt khí", "(iii) Purge system", level=3)

    P(b, lang,
      "Nguyên lý cơ bản của hệ thống thổi để đo mức dựa trên sự sinh ra áp "
      "suất ngược. Khi chất lưu sạch, thường là không khí khô, được cho sủi "
      "bọt ngược lại cột áp tĩnh, cột áp này gây cản trở dòng khí và sinh ra "
      "áp suất ngược. Áp suất ngược này tỷ lệ chính xác với cột áp, do đó có "
      "thể dùng để đo mức của chất lỏng.",
      "The basic principle behind purge system of level measurement is "
      "dependent on generation of back pressure. When a clean fluid, dry air "
      "invariably is allowed to bubble out against a hydrostatic head, the "
      "head imparts a resistance to the flow of air thereby creating a back "
      "pressure. This back pressure is exactly proportional to the head and "
      "therefore, can be a measure of level of that liquid.")

    P(b, lang,
      "Khí thổi chảy qua rotameter thổi, là rotameter lưu lượng nhỏ được "
      "thiết kế riêng. Có cơ cấu chỉnh lượng khí, thực chất là van kim vận "
      "hành bằng tay, cho phép điều chỉnh lưu lượng rất tinh. Lưu lượng khí "
      "phải được chỉnh sao cho ở mức 100% chỉ có lượng khí tối thiểu sủi ra, "
      "thường là một bọt mỗi giây — một chỉnh định thỏa mãn. Điều này cần "
      "thiết để có độ chính xác cao nhất và sai số nhỏ nhất. Bố trí này được "
      "thể hiện trên Hình 3.60.",
      "The purging air flows through a purge rotameter, especially designed "
      "low flow rotameter. There is an arrangement for adjustment of the "
      "quantity of air flow through the purge rotameter. The knob made for "
      "this purpose is in fact a needle valve which is operated by hand and "
      "in this way the amount of flow can be very minutely adjusted. The "
      "airflow has to be adjusted such that at 100% level minimum possible air "
      "should bubble out. This is normally one bubble per second which is a "
      "satisfactory adjustment. This is required in order to have maximum "
      "accuracy in measurement and hence minimum error. The arrangement has "
      "been shown in Figure 3.60.")

    FIG(b, 60, F.fig_f60(), lang)

    P(b, lang,
      "Ưu điểm nổi bật nhất của phương pháp này là rẻ nhất trong đo mức cho "
      "cả chất lưu ăn mòn lẫn chất lưu bẩn chứa hạt rắn. Nhược điểm duy nhất "
      "có thể thấy là ống sủi bọt phải được thay thế theo thời gian sau khi "
      "bị ăn mòn hoặc mòn hoàn toàn.",
      "The most striking advantage of this measurement system is that it is "
      "the most inexpensive method for level measurement for corrosive as "
      "well as dirty fluid containing solid particles. The only disadvantage "
      "that can be expected of this method is that the bubble pipe has to be "
      "replaced from time-to-time after it gets completely corroded or eroded.")

    # -------------------------------------------- (iv) displacer/buoyancy
    H(b, lang, "(iv) Kiểu vật dịch chỗ/lực đẩy nổi",
      "(iv) Displacer/buoyancy type", level=3)

    P(b, lang,
      "Nguyên lý cơ bản của hệ thống đo mức kiểu lực đẩy nổi là khi một vật "
      "được nhúng vào chất lỏng, lực đẩy lên tác dụng lên vật bằng trọng "
      "lượng chất lỏng bị vật chiếm chỗ. Một vật hình trụ gọi là vật dịch chỗ "
      "hoặc phao được bố trí chìm trong chất lỏng cần đo mức. Vật dịch chỗ "
      "thực chất được treo trong buồng phao đặt ngay ngoài bình chứa chất "
      "lỏng. Buồng phao được nối với bình chính như Hình 3.61.",
      "The basic principle behind the buoyancy type level measurement system "
      "is that when a body is immersed in a liquid, the upthrust acted upon "
      "the body equals the weight of the liquid displaced by it. A cylindrical "
      "body called displacer or float is arranged to be submerged inside the "
      "liquid of which the level is to be measured. The displacer is in fact "
      "suspended in a float chamber located just outside the tank containing "
      "the liquid of which the level is to be measured. The float chamber is "
      "connected to the main tank as shown in Figure 3.61.")

    FIG(b, 61, F.fig_f61(), lang)

    P(b, lang,
      "Lực đẩy sinh ra tỷ lệ trực tiếp với mức mà chất lỏng dâng tới trên phao "
      "trong buồng phao. Như vậy, trọng lượng biểu kiến của phao giảm dần khi "
      "mức chất lỏng tăng và ngược lại. Khi không có chất lỏng gần phao, toàn "
      "bộ trọng lượng phao được đầu tự do của cần phao chịu. Điều này tạo ra "
      "tác động xoay bằng tích của trọng lượng phao và chiều dài cần phao, "
      "truyền tới đầu cụm ống xoắn. Tác động xoay này được cân bằng bằng ứng "
      "suất xoắn sinh ra trong ống xoắn, nên góc xoay của trục tỷ lệ với "
      "trọng lượng biểu kiến của phao. Khi mức chất lỏng tăng gần phao, trọng "
      "lượng biểu kiến giảm làm giảm tác động xoay trên ống xoắn; ứng suất "
      "xoắn trong ống sẽ quay trục tới vị trí góc mới tỷ lệ với trọng lượng "
      "biểu kiến của phao.",
      "The upthrust so created shall be directly proportional to the level on "
      "the float upto which the liquid rises in the float chamber. In this "
      "way, the apparent weight of the float will go on decreasing as the "
      "liquid level will go on rising and vice versa. When the liquid is not "
      "present near the float, the complete weight of the float is taken by "
      "the free end of the float rod. This results in creation of a turning "
      "action given by product of weight of float and length of float rod. "
      "This is applied to the end of torque tube assembly. This turning action "
      "is balanced by the torsional stress created in the torque tube. Hence, "
      "the angle of shaft-turn shall be proportional to apparent weight of the "
      "float. As the liquid level rises near the float, the apparent weight of "
      "the float shall get reduced and hence the turning action on to the "
      "torque tube. The torsional stress set up in the torque tube shall rotate "
      "the shaft to a new angular position which shall be proportional to the "
      "apparent weight of the float.")

    P(b, lang,
      "Phao làm bằng thép không gỉ, hastelloy hoặc k-monel và nối với cần "
      "phao qua khớp cầu. Dải đo được xác định bởi chiều dài phao. Độ lớn "
      "lực đẩy phụ thuộc vào mật độ chất lỏng. Dải biến thiên của lực đẩy hay "
      "lực nổi Fb (newton) được cho bởi phương trình:",
      "The float is made up of stainless steel, hastelloy or k-monel and is "
      "connected to the float rod through ball and socket joint. The range of "
      "measurement is determined by the length of the float. The amount of "
      "upthrust is dependent upon the density of the liquid. Span of the "
      "upthrust or buoyant force Fb (newton) is given by the equation:")

    E(b, lang, "F_b = 9.8 × 10⁻³ ρ V (l/L)",
      "F_b = 9.8 × 10⁻³ ρ V (l/L)", num="3.44")

    P(b, lang,
      "trong đó ρ là trọng lực riêng của chất lỏng; V là thể tích vật dịch "
      "chỗ (cm³); l và L lần lượt là chiều dài làm việc và chiều dài tổng của "
      "vật dịch chỗ (mm).",
      "where ρ is the specific gravity of the liquid; V is the volume of "
      "displacer (cm³); l and L are working and total length of displacer "
      "respectively (mm).")

    P(b, lang,
      "Phương pháp đo mức bằng ống xoắn/vật dịch chỗ có ưu điểm vượt trội. "
      "Phương pháp này dùng rất hiệu quả cho bình chịu áp suất cao. Người ta "
      "nhận thấy chuyển động thẳng đứng thực tế của phao rất nhỏ so với sự "
      "thay đổi của mức. Độ chính xác không bị ảnh hưởng bởi nhiệt độ, và do "
      "đó không bị ảnh hưởng bởi mật độ, vì phao được chọn với kích thước lớn "
      "hơn khi dùng ở nhiệt độ cao.",
      "Torque tube/displacer method of level measurement is superior. It can "
      "be used in case of high pressure vessel application very effectively. "
      "It has been observed that effective vertical motion of the float is "
      "very small with respect to change in level. Accuracy is not affected by "
      "change in temperature and hence density, because increased dimension of "
      "float is selected for use at elevated temperature.")

    P(b, lang,
      "Để đo mức mặt phân cách giữa hai chất lỏng không trộn lẫn có trọng lực "
      "riêng khác nhau, gần như luôn dùng phương pháp vật dịch chỗ. Trong "
      "trường hợp đó, rõ ràng hiệu số trọng lực riêng của hai chất lỏng sẽ "
      "quyết định sự thay đổi lực đẩy khi mức mặt phân cách thay đổi trong "
      "dải chuyển động của phao.",
      "To measure the level (interface) between two immiscible liquids having "
      "different specific gravity, displacer method is almost invariably "
      "employed. In that case, it is obvious that the difference in their "
      "specific gravities shall determine the change in upthrust since the "
      "level of interface changes through the range of float.")

    # ------------------------------------- (v) differential pressure intro
    H(b, lang, "(v) Kiểu chênh áp", "(v) Differential pressure type", level=3)

    P(b, lang,
      "Sự chênh áp do mức chất lỏng tăng lên so với một mốc cố định chính là "
      "thước đo mức. Khi đo mức bình hở, mốc đó là áp suất khí quyển. Ngược "
      "lại, áp suất tĩnh bên trong bình kín trở thành mốc để đo mức của bình "
      "kín. Như vậy, đo mức thực chất trở thành đo áp suất chênh do cột áp "
      "của mức chất lỏng tạo ra.",
      "Differential created by a rising level of a liquid with respect to "
      "fixed reference is the measure of level. In case of an open tank level "
      "measurement, the reference becomes the atmospheric pressure itself. On "
      "the other hand, the static pressure inside a closed tank becomes the "
      "reference for measurement of level of a closed tank. Thus, we observe "
      "that level measurement in fact becomes measurement of differential "
      "pressure created by the level head.")

    return b
