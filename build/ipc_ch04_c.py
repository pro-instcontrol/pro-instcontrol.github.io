# -*- coding: utf-8 -*-
"""Chapter 4, "Telemetry", section 4.2 "Cable Telemetry" continued (EN/VI bilingual).

Source: Janardan Prasad, M. N. Jayaswal and Vishnu Priye, *Instrumentation and
Process Control* (I.K. International, 2019), PDF pp. 225-230, printed pp.
213-218, decoded text lines 8515-8757.  Covered here are coaxial cable types
and joining, fibre-optic principles and index profiles, fibre strength and
connection, complete fibre cable structure, opto-electric telemetry and
composite cabling.  The nine source figures (4.6-4.14) are redrawn as vectors
in the `ipcfig4_a` supplier module and placed where the text refers to them.
Units use literal Unicode; the English body follows the source wording, the
Vietnamese body uses the accepted technical reading.
"""

import ipcfig4 as F
from ipc_ch04_lib import H, P, L, E, FIG, TBL, NOTE


def section(lang):
    b = []

    # ------------------------------------------------------------ 4.2 (iii)
    H(b, lang, "(iii) Cáp đồng trục", "(iii) Coaxial cable", level=3)

    P(b, lang,
      "Trong khi cáp xoắn đôi đã che chắn đủ tốt khỏi nhiễu và các tạp nhiễu từ "
      "bên ngoài, cáp đồng trục có chất lượng che chắn cao hơn hẳn. Các tín "
      "hiệu mức cực thấp (tín hiệu truyền hình, tín hiệu máy tính, tín hiệu pH "
      "hoặc các phép đo chất lượng khác) rất dễ bị ảnh hưởng ngay cả bởi nhiễu "
      "có cường độ nhỏ nhất, vì vậy hầu như luôn dùng cáp đồng trục để truyền "
      "tín hiệu. Hình 4.6 cho thấy cấu trúc hoàn chỉnh của cáp đồng trục, gồm "
      "một dẫn điện đồng đơn ở giữa, lớp cách điện Teflon, lớp bện lưới đồng "
      "và vỏ PVC dày.",
      "While the twisted pair provides sufficient shielding from outside "
      "interference due to noise, the coaxial cable possesses high quality of "
      "shielding property. The extremely low level signals (television signal, "
      "computer signal, pH or other quality measurement signals), which are very "
      "much susceptible to even smaller intensity of noise signal, use coaxial "
      "cable almost invariably for signal transmission. A diagram showing "
      "complete structure of coaxial cable has been shown in Figure 4.6: a "
      "single copper conductor, Teflon insulation, braiding made of copper mesh "
      "and a thick PVC cover.")
    FIG(b, 6, F.fig_f06(), lang)

    P(b, lang,
      "Cấu trúc này giải thích việc loại cáp này có thể dùng ở băng thông cao "
      "hơn và đạt hệ số tín hiệu trên nhiễu lớn. Có bốn loại cáp đồng trục:",
      "The constructional feature explains that this variety of cable can be "
      "used for higher bandwidth and can achieve high signal-to-noise ratio "
      "factor. There are altogether four different varieties of coaxial cable:")
    L(b, lang,
      ["Cáp 50 ôm (cáp Ethernet)",
       "Cáp 75 ôm",
       "Cáp 93 ôm",
       "Cáp đồng trục đôi"],
      ["50 ohms cable (Ethernet cable)",
       "75 ohms cable",
       "93 ohms cable",
       "Twin axial cable"],
      ordered=True)

    P(b, lang,
      "Cáp đồng trục 50 ôm, còn gọi là cáp Ethernet, cũng được dùng cho các "
      "mạng thời gian thực. Trong một kiểu thiết kế cáp 50 ôm, người ta dùng "
      "dây dày có che chắn kép; loại này được dùng rất thành công trong hệ "
      "thống thiết bị đo của các ngành công nghiệp chế biến. Với kiểu thiết "
      "kế khác dùng dây mảnh và che chắn đơn, cáp dễ bị nhiễu nhưng lại dễ "
      "thao tác khi làm đầu nối và các công việc tương tự. Ngược lại, cáp dây "
      "dày tuy khó thao tác nhưng có khả năng loại nhiễu rất tốt.",
      "The 50 ohms coaxial cables (called Ethernet cable) also are used for "
      "real-time networks. In one design of 50 ohms cable, thick wire with "
      "double shield are provided. These are very successfully used in process "
      "industries instrumentation system. In another design where a thin wire "
      "with single shield is selected is susceptible to noise interference but "
      "is easier to work upon for termination and others. The thick wire cable "
      "on the other hand is not easy to work upon but provides excellent noise "
      "rejection capability.")

    P(b, lang,
      "Cáp đồng trục 75 ôm thường không dùng trong hệ thống thiết bị đo; hầu "
      "như chỉ dùng cho mạng truyền hình cáp (CATV). Lý do là cáp 75 ôm làm "
      "suy giảm tín hiệu mà mắt người thường không nhận ra trong trường hợp "
      "tín hiệu hình ảnh. Nhưng sự suy giảm của tín hiệu đo lại có thể gây sai "
      "số đo được và làm hỏng điều khiển quá trình.",
      "75 ohms coaxial cables are normally not in use for instrumentation "
      "system. These are used almost invariably for CATV (Cable Television) "
      "network. The fact is that the 75 ohms cable provides degradation in "
      "signal which goes normally, unnoticed by human eyes (in case of video "
      "signal). But degradation in instrumentation signal can bring measurable "
      "error and failure of process control.")

    P(b, lang,
      "Cáp đồng trục 93 ôm là loại đặc biệt, dùng trong liên lạc mạng độc "
      "quyền cho máy tính lớn IBM và cũng dùng trong mạng ARCnet.",
      "The 93 ohms coaxial cable is a special class cable and is used in "
      "proprietary networks communication for IBM mainframe computers and also "
      "in ARC net networks.")

    P(b, lang,
      "Cáp đồng trục đôi cũng là loại đặc biệt, gồm hai dẫn điện đồng được "
      "che chắn chung như Hình 4.7. Ngoài ứng dụng trong mạng độc quyền, cáp "
      "còn được dùng trong bộ điều khiển logic lập trình (PLC) để nối các "
      "mô-đun vào/ra (I/O) từ xa. Tốc độ thường gặp của các mô-đun I/O từ xa "
      "rất phù hợp với hiệu năng của cáp đồng trục đôi, và khả năng loại nhiễu "
      "của loại cáp này cũng vượt trội.",
      "The twin-axial cable is also a special cable, which has two copper "
      "conductors with overall shielding as shown in Figure 4.7. In addition "
      "to its use in proprietary network applications, these are used in "
      "programmable logic controller (PLC) for connecting remote I/O module "
      "(input/output module). The speeds, which are typically encountered with "
      "remote I/O modules are excellently matched with the performance of the "
      "twin-axial cable. Performance in noise rejection is also superior.")
    FIG(b, 7, F.fig_f07(), lang)

    P(b, lang,
      "Bất cứ khi nào cần nối hai cáp đồng trục, cả hai thành phần của cáp đều "
      "phải được nối riêng. Dẫn điện đồng này được nối với dẫn điện đồng kia, "
      "còn lớp bện lưới đồng phải được vặn xoắn thật kỹ để nối với nhau. Cuối "
      "cùng, toàn bộ mối nối được quấn riêng bằng băng cách điện dân dụng.",
      "Whenever there is a requirement of joining two coaxial cables, both the "
      "components of the cable have to be joined together separately. The "
      "copper conductor is to be joined to the other copper conductor and the "
      "braiding (made of copper mesh) has to be joined to each other by "
      "twisting properly. Finally, the combination should be wrapped separately "
      "by domestic insulation tapes.")

    # ------------------------------------------------------------ 4.2 (iv)
    H(b, lang, "(iv) Cáp sợi quang", "(iv) Fibre optic cable", level=3)

    P(b, lang,
      "Cáp sợi quang là phần trung gian, tức là môi trường truyền dẫn của toàn "
      "bộ hệ thống truyền quang. Hệ thống này nhìn chung gồm nguồn sáng tạo "
      "tín hiệu, môi trường truyền và cuối cùng là một hệ thống dò nhận phù "
      "hợp. Nguyên lý cơ bản của hệ thống sợi quang dựa trên tính chất phản xạ "
      "toàn phần trong quang học. Tia sáng tới ở góc bằng hoặc lớn hơn góc tới "
      "hạn sẽ bị phản xạ hoàn toàn trở lại và bị giữ bên trong sợi. Nhờ đó, "
      "ánh sáng bị giữ lại có thể truyền liên tục trong nhiều dặm với tổn hao "
      "nhỏ nhất. Hình 4.8 minh họa một tia sáng như vậy bị giữ bên trong sợi.",
      "Fibre optic cable constitutes the intermediate part, i.e. the medium for "
      "transmission of an entire optical transmission system. This is consisting "
      "of, in general, a light-generating source for signal, the medium and "
      "finally a suitable detection system. The basic principles behind the "
      "fibre optic system lie in the property of total internal reflection "
      "described in optical physics. The ray of light incident at (and/or above) "
      "critical angle gets totally reflected back and is trapped inside the "
      "fibre enclosure. In this way the trapped light can be propagated "
      "uninterruptedly for many miles altogether with minimum loss. Figure 4.8 "
      "indicates one such ray of light trapped inside the fibre enclosure.")
    FIG(b, 8, F.fig_f08(), lang)

    P(b, lang,
      "Nếu kích thước của sợi được thu nhỏ tới mức tương đương bước sóng ánh "
      "sáng (tính bằng micron), sợi hoạt động như một ống dẫn sóng, trong đó "
      "tia sáng đi thẳng hoàn toàn mà không bị phản xạ. Cấu trúc này gọi là sợi "
      "chế độ đơn. Ở chiều ngược lại, nếu lõi sợi được phóng to, nhiều tia sáng "
      "sẽ phản xạ ở các góc khác nhau, tối đa bằng góc tới hạn của phản xạ toàn "
      "phần, và thu được sợi đa chế độ. Rõ ràng sợi chế độ đơn đắt hơn sợi đa "
      "chế độ. Sợi chế độ đơn dùng cho truyền dẫn tốc độ cao và khoảng cách xa, "
      "trong khi sợi đa chế độ dùng cho tốc độ và khoảng cách trung bình. Có "
      "thể truyền tới 100 kilômét mà không cần khuếch đại.",
      "If the dimension of the fibre enclosure is reduced and made equivalent "
      "to the wavelength (in microns) of light, the fibre enclosure works like "
      "a waveguide through which the ray of light propagates in perfect "
      "straight line without any bounce. This arrangement is known as "
      "single-mode fibre. If, on the other hand, the core of the fibre "
      "enclosure is increased, more than one ray of light bounces around at "
      "different angles (up to the maximum angle of total internal reflection), "
      "a multimode fibre arrangement results. Obviously the single-mode fibre "
      "shall be more expensive in effect than the multimode. Single-mode fibre "
      "is applicable to higher speed and longer distance transmission system "
      "whereas a multimode fibre is applied to medium range of speed and "
      "distance. Transmission upto 100 kilometre can be realized without the "
      "need for amplification.")

    P(b, lang,
      "Hình 4.9 cho thấy một sợi đơn. Toàn bộ tinh chỉnh thiết kế tập trung "
      "vào chế tạo lõi thủy tinh mà tia sáng đi qua. Kích thước của sợi được "
      "xác định bằng đường kính lõi và lớp vỏ bọc, ghi là lõi/vỏ.",
      "A single fibre has been shown in Figure 4.9. The entire design "
      "refinement is centred at manufacturing of glass core through which the "
      "ray of light shall propagate. The diameter of the core and cladding "
      "(expressed as core/clad) determines the size of the optical fibre.")
    FIG(b, 9, F.fig_f09(), lang)

    P(b, lang,
      "Thường có ba kích thước được dùng trong thực tế: loại 9/125, loại "
      "62,5/125 và loại 200/230. Chữ số đầu cho biết kích thước lõi, chữ số "
      "còn lại cho biết kích thước lớp vỏ, tính bằng micron (1 micron = 10⁻⁶ "
      "m). Loại 9/125 với lõi 9 micron và vỏ 125 micron dùng trong điện thoại. "
      "Loại 62,5/125 dùng cho hệ thống truyền dữ liệu doanh nghiệp. Loại lõi "
      "lớn 200/230 dùng cho hệ thống điều khiển quá trình và thiết bị đo. Ba "
      "loại này được thể hiện ở Hình 4.10.",
      "In general, three different dimensions are in practical use. They are "
      "type 9/125 type 62.5/125, and type 200/230. The first digit indicates "
      "the size of core and the other one shows size of the cladding in micron "
      "units (1 micron = 10⁻⁶ metres). Type 9/125 where core is 9 micron and "
      "cladding is 125 micron are used for telephony applications. The next "
      "one, i.e. 62.5/125 type are used for enterprise data transmission system. "
      "The large-core fibre, i.e. type 200/230 are used for process control and "
      "instrumentation system. These three types have been shown in Figure 4.10.")
    FIG(b, 10, F.fig_f10(), lang)

    P(b, lang,
      "Lõi của sợi quang thường được coi là đồng nhất, nhưng tại ranh giới "
      "giữa lõi và lớp vỏ, tính đồng nhất không còn nữa. Chiết suất vì thế "
      "thay đổi tại ranh giới này; đó gọi là sợi chiết suất bậc thang. Đặc điểm "
      "của loại sợi này là không bị ảnh hưởng bởi chiết suất không đổi hay sự "
      "thay đổi đột ngột tại ranh giới. Tuy nhiên, với sợi đa chế độ lại có sự "
      "khác biệt giữa tia đi theo góc tới hạn và tia đi dọc trục. Dù tốc độ "
      "ánh sáng không đổi, độ dài đường đi của hai tia này không giống nhau, "
      "nên thời gian tới đầu kia cũng không như nhau. Hiện tượng này gọi là mở "
      "rộng xung hay tán sắc chế độ. Có thể giảm tán sắc bằng cách bố trí lõi "
      "có chiết suất cao nhất dọc trục và giảm dần chiết suất về phía ranh "
      "giới; khi đó tạo ra sự phân bố chiết suất dần dần và loại sợi này gọi là "
      "sợi chiết suất thay đổi dần. Hai loại này được thể hiện ở Hình 4.11 và "
      "Hình 4.12.",
      "The core of an optical fibre is generally considered to be homogeneous "
      "but at the junction of the core and the cladding, the theory of "
      "homogeneity ceases to exist. The refractive index thus gets changed at "
      "the boundary of the two. This is called step index fibre. The speciality "
      "of this type of fibre is that it does not get affected by either constant "
      "refractive index or step change in it at the junction. But with multimode "
      "fibre there is a difference between the ray at the critical angle and "
      "the ray along the axis. Even then the speed of light remains constant, "
      "the length of the path of these two rays not being the same, the time to "
      "reach the other end does not remain same. This phenomenon is called "
      "broadening of pulse or modal dispersion. The dispersion can be minimized "
      "by arranging the core of the fibre of highest refractive index along the "
      "axis and decreasing the refractive index gradually upto the boundary. "
      "This way a gradation of refractive index is created and this type of "
      "fibre is known as graded index fibre. These have been shown in Figures "
      "4.11 and 4.12.")
    FIG(b, 11, F.fig_f11(), lang)
    FIG(b, 12, F.fig_f12(), lang)

    P(b, lang,
      "Việc xử lý sợi thủy tinh là yếu tố quan trọng trong toàn bộ công việc. "
      "Nguy cơ gãy do bốn nguyên nhân sau:",
      "Handling of fibre glass is an important factor in whole of the affairs. "
      "Risk of breakage is due to four reasons:")
    L(b, lang,
      ["Ứng suất kéo",
       "Nhiệt",
       "Nước hoặc độ ẩm",
       "Yếu tố thời gian"],
      ["Tensile strain",
       "Heat",
       "Water/moisture",
       "Time factor"],
      ordered=True)

    P(b, lang,
      "Quá trình chế tạo đúng cách giúp giảm ứng suất kéo, vốn cuối cùng tạo "
      "ra vết nứt. Lớp phủ nhựa trên sợi tạo ra một rào cản nhân tạo chống nước "
      "hoặc độ ẩm; lớp vỏ bọc cũng bảo vệ như vậy. Lớp vỏ thường làm bằng "
      "polyme fluoro cứng, có khả năng chống thấm nước rất tốt. Thực ra thủy "
      "tinh không dễ gãy vì độ bền gãy của nó gần gấp năm lần thép, nhưng thủy "
      "tinh trở nên yếu do các khuyết tất hi vi có sẵn trên bề mặt. Những "
      "khuyết tất này phát triển thành vết nứt rất nhanh khi có nhiệt và độ ẩm. "
      "Vì vậy, độ bền của sợi là yếu tố quan trọng và cần hết sức cẩn trọng khi "
      "lắp đặt và xử lý.",
      "Proper manufacturing process minimizes the tensile strain, which "
      "ultimately develops cracks. Plastic coating on the fibre creates an "
      "artificial barrier for water or humidity. The cladding also provides "
      "same protection. Cladding is generally made of hard fluoro-polymer which "
      "is an excellent water repellent. In fact, glass is not easily broken "
      "because its breaking strength is nearly five times more than the steel "
      "but the glass becomes weak due to microscopic defect found on the glass "
      "surface by nature. These microscopic defects develop cracks rapidly in "
      "the presence of heat and moisture. Therefore, the strength of the fibre "
      "is an important factor and great care has to be taken for installation "
      "and other handling activities.")

    P(b, lang,
      "Việc nối hai sợi thủy tinh đòi hỏi sự cẩn trọng đặc biệt trong quá trình "
      "thực hiện. Người ta nối hai sợi bằng nhiều cách. Theo một cách, hai sợi "
      "được kết thúc trong một đầu nối đặc biệt và cắm chắc vào một ổ cắm sợi "
      "thiết kế riêng. Cách này làm mất gần 20% tín hiệu ánh sáng truyền đi "
      "nhưng rất dễ thao tác. Theo cách khác, hai đoạn sợi được đặt trong một "
      "ống bọc đặc biệt, úp mặt nhau và kẹp chặt. Ở cách này, người ta kiểm tra "
      "sự căn chỉnh bằng cách chiếu một tia sáng và điều chỉnh vị trí nhẹ nhàng "
      "sang hai bên; cách nối này cũng làm mất gần 10% tín hiệu sáng. Cách thứ "
      "ba là hàn hai đoạn bằng cách nung chảy trong điều kiện kiểm soát để được "
      "một sợi liền mạch. Đây là phương pháp nối tốt nhất, tổn hao ánh sáng "
      "nhỏ nhất.",
      "As far as connection of the two fibre glasses is concerned, great care "
      "is observed during the process. Two fibres are connected in many ways. "
      "In one way of connection, the two fibres can be terminated in a special "
      "connector and can be plugged securely to an especially designed fibre "
      "socket. In this arrangement, nearly 20% of the transmitted light signal "
      "is lost but is very easy to handle. In another arrangement, the two "
      "pieces are put in a special sleeve facing each other and clamped "
      "properly. In this particular arrangement, provision for alignment "
      "checking is thereby sending a ray of light and adjusting the position "
      "slightly this way or that way. With this connection also almost 10% of "
      "the light signal is lost. In the third arrangement, the two pieces can "
      "be fused by melting under controlled condition and a one-piece fibre "
      "can be obtained. This is the best possible method of connection, which "
      "has minimum loss of light.")

    P(b, lang,
      "Các thảo luận trên cho thấy hệ thống sợi quang rất khó và tốn kém khi "
      "xử lý, lắp đặt, nối và bảo trì. Dù vậy, hệ thống này vẫn ngày càng phổ "
      "biến trong đo từ xa và các môi trường truyền tín hiệu khác, nhờ băng "
      "thông lớn vượt trội. Băng thông cho biết khả năng chở tín hiệu của sợi "
      "quang hay của bất kỳ kênh nào. Yêu cầu băng thông cho thoại là 3 kilôhertz "
      "(kHz) và cho truyền hình là 6 megahertz (MHz), nhưng băng thông sẵn có "
      "của hệ thống sợi quang là gigahertz (GHz), cao hơn rất nhiều so với hai "
      "yêu cầu thực tế nói trên.",
      "Discussions till now indicate that it is very difficult and expensive "
      "to handle, install, connect and maintain an optical fibre system. Even "
      "then the optical fibre system is gaining popularity in the world of "
      "telemetry and other signal transmission environments. The reason lies in "
      "its tremendous bandwidth availability. Bandwidth indicates signal-carrying "
      "capacity in an optical fibre system or in any channel. Requirement of "
      "bandwidth for voice is 3 kilohertz (KHz) and for television is 6 "
      "megahertz (MHz), but the available bandwidth with an optical fibre system "
      "is in gigahertz (GHz) which is much higher than the above two practical "
      "requirements.")

    NOTE(b, lang,
      "Tán sắc màu là sự thay đổi vận tốc ánh sáng trên toàn bộ dải bước sóng do "
      "nguồn sáng phát ra. Đây là nguồn hạn chế băng thông duy nhất của hệ "
      "thống sợi quang; trong chế tạo, người ta thiết kế sợi để tán sắc màu ở "
      "mức nhỏ nhất khi sử dụng.",
      "Chromatic dispersion is the variation in the velocity of light over the "
      "entire range of wavelength produced by the light source. It is the only "
      "limitation on bandwidth in an optical fibre system; during manufacturing "
      "the fibre is developed in such a way that minimum chromatic dispersion "
      "should result while in use.")

    P(b, lang,
      "Sợi chế độ đơn có băng thông lớn hơn sợi đa chế độ chiết suất bậc "
      "thang; sợi đa chế độ chiết suất thay đổi dần có băng thông nằm giữa hai "
      "loại này. Với khoảng cách truyền tới 10 kilômét và tốc độ 10 Mbps "
      "(megabit trên giây), dùng sợi đa chế độ chiết suất bậc thang. Với 500 "
      "MHz-km (tích của băng thông và khoảng cách), dùng sợi đa chế độ chiết "
      "suất thay đổi dần. Cuối cùng, với 10 GHz-km, dùng sợi chế độ đơn.",
      "Single-mode fibre has more bandwidth than the step index multimode "
      "fibre. Graded index multimode fibre has the bandwidth in between these "
      "two. For transmission distance upto 10 kilometer and 10 Mbps (Megabits "
      "per second) speed, step index multimode fibre is used. For 500 MHz-km "
      "(product of bandwidth and distance) graded index multimode fibre is "
      "used. And finally for 10 GHz-km single-mode fibre is used.")

    P(b, lang,
      "Một điểm cần xét đến khác là cấu trúc tổng thể của sợi quang. Cáp là "
      "cấu trúc đặt bao quanh sợi thủy tinh để bảo vệ sợi mỏng manh về mặt "
      "vật lý. Thiết kế cấu trúc được tính toán phù hợp với nhu cầu riêng của "
      "sợi. Vì sợi không dẻo như đồng, bất kỳ sự kéo dãn quá mức nào cũng có "
      "thể làm hỏng hoàn toàn sợi. Các yêu cầu quan trọng của một cáp sợi quang "
      "tốt là:",
      "Another consideration in this regard is the overall structure of the "
      "optical fibre. The cable is the overall structure placed on top of the "
      "fibre glass in order to provide physical protection to the delicate "
      "fibre. Structural provision is designed properly to meet the specific "
      "need of the fibre. Since the fibre is not at all ductile like copper, "
      "any undue stretching can damage the fibre completely. Important "
      "requirements of a perfect fibre optic cable are:")
    L(b, lang,
      ["Khả năng chống ép dập",
       "Khả năng chống mọi dạng lực kéo",
       "Độ giãn nở do nhiệt nhỏ nhất",
       "Khả năng chịu uốn trong quá trình lắp đặt",
       "Tổn hao uốn vi mô nhỏ nhất (một lượng nhỏ ánh sáng có thể bị mất do "
       "uốn vi mô tự nhiên, thường không nhận thấy bằng mắt, làm suy giảm "
       "chính tín hiệu)"],
      ["Resistance to crushing effect",
       "Resistance to all forms of tensile forces",
       "Minimum expansion due to heat",
       "Sustenance to bending during installation",
       "Minimum microbending loss (Small amount of light can be lost due to "
       "natural microbending which goes normally unnoticed physically, resulting "
       "in loss in the main signal itself)"],
      ordered=True)

    P(b, lang,
      "Hình 4.13 cho thấy mặt cắt ngang của một cáp sợi quang hoàn chỉnh được "
      "dùng trong hệ thống điều khiển và mạng của một nhà máy phân bón.",
      "Figure 4.13 shows the cross-section of a complete fibre optic cable that "
      "has been used in one of the fertilizer plants control as well as "
      "networking systems.")
    FIG(b, 13, F.fig_f13(), lang)

    P(b, lang,
      "Lõi và lớp vỏ bọc của sợi giữ vai trò như thường lệ. Lớp tiếp theo là "
      "ống bảo vệ, thực chất bảo vệ lớp vỏ khỏi hư hỏng. Thanh Kelvar được bố "
      "trí cạnh ống bảo vệ để tăng độ bền cơ học, giúp việc xử lý an toàn và "
      "dễ dàng hơn. Bó thanh Kelvar được phủ nhựa và cuối cùng bọc hai lớp vỏ, "
      "một lớp Kelvar và một lớp PVC hoặc Teflon, để bảo vệ các phần bên trong "
      "khỏi tác động cơ học và môi trường.",
      "The fibre core and the cladding serve the usual purpose. Next layer is "
      "the protection tube, which in fact protects the cladding from damage. "
      "Kelvar rod has been provided next to the protection tube for mechanical "
      "strength making the handling safer and easier. The Kelvar rod bunch is "
      "covered with resin and finally two-layer jacketing (one of Kelvar and "
      "the other one of PVC or Teflon) is done to protect the interior parts of "
      "the assembly from physical as well as environmental abuses.")

    P(b, lang,
      "Hình 4.14 cho thấy toàn bộ một hệ thống đo từ xa kiểu quang-điện.",
      "Figure 4.14 shows an entire telemetry system of opto-electric type.")
    FIG(b, 14, F.fig_f14(), lang)

    P(b, lang,
      "Sự xuất hiện của hệ thống đo từ xa quang-điện thiết kế mới cũng mang "
      "lại kỹ thuật đi dây mới, gọi là hệ thống cáp ghép. Hệ thống này gồm dây "
      "UTP/STP, cáp đồng trục và cáp sợi quang gộp chung trong một vỏ bọc "
      "thống nhất. Các mối nối được thực hiện theo yêu cầu của từng ứng dụng "
      "cụ thể tại vị trí thích hợp. Loại cáp này được chọn khi hệ thống truyền "
      "dẫn phức tạp và có nhiều dạng tín hiệu khác nhau. Nếu hệ thống không "
      "yêu cầu thì việc dùng cáp ghép là không kinh tế. Thường thì các loại cáp "
      "này được chế tạo theo yêu cầu và do nhà cung cấp làm cho các dự án trọn "
      "gói trong hệ thống thiết bị đo công nghiệp và các hệ thống mạng khác.",
      "The advent of newly designed opto-electric telemetry system has brought "
      "about new wiring techniques as well. This is known as composite cabling "
      "system. This cabling system contains UTP/STP wiring, co-axial cabling and "
      "also fibre cables all put together in a unified jacket. The connections "
      "are made as per the requirement for specific application at appropriate "
      "place. This cable is selected when the transmission system is complicated "
      "and many forms of signals are encountered with. If the system does not "
      "call for, use of composite cable is uneconomical. Normally these cables "
      "are custom-built and vendor-supplied for turn-key projects in process "
      "instrumentation system and other networking systems.")

    return b
