# -*- coding: utf-8 -*-
"""Book 7, Chapter 10, Section B - Valve Positioners (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), the two sections
"What to Look for When Specifying Positioners or Transducers" and "Smart
Positioners—Smart Valves", printed pp. 71-76 (source lines 2236-2423 of
work/cvp_raw.txt). Covers the specifying checks (signal type, hazardous area,
vibration, air quality, weather, frequency response, air capacity, booster
relays, desirable features) and the smart-positioner/smart-valve discussion,
including the two footnotes, Figures 10-2 and 10-3, and the nine-point
digital-versus-analog summary. Figure redrawings live in cvpfig10.py.
"""
from cvp_common import fig, h2, note, ol, p
import cvpfig10 as F


def body_vi():
    b = []
    b.append(h2("Chọn bộ định vị hay bộ chuyển đổi",
                "Choosing a positioner or transducer"))
    b.append(p("Hầu hết các vòng điều khiển dùng tín hiệu tương tự hoặc số 4 đến 20 mA, vì vậy bạn buộc phải chuyển đổi tín hiệu điện tử sang tín hiệu khí nén, hoặc dùng bộ định vị số. Nếu bắt buộc dùng tín hiệu tương tự (4 đến 20 mA), bộ định vị I/P là lựa chọn của bạn; một phương án khác là chỉ định bộ chuyển đổi dòng–áp (I/P) rồi dẫn đầu ra của nó tới một bộ định vị khí nén. Dù bộ định vị khí nén có thể đang dần bị thay thế, chúng vẫn có lợi thế về chi phí và theo thiết kế đã là dạng chống nổ (explosion-proof)."))

    b.append(h2("Kiểm tra điều kiện lắp đặt",
                "Checking the installation conditions"))
    b.append(p("Trước hết, hãy xem xét việc van có được lắp ở khu vực có chất lỏng dễ cháy và có thể có hơi hay không. Bạn có thể cần phiên bản chống nổ (explosion-proof) hoặc an toàn nội tại (intrinsically safe)."))
    b.append(p("Thứ hai, kiểm tra mức rung động tại vị trí lắp van. Ví dụ, nếu van đặt gần một bơm ly tâm, có thể tồn tại rung động đường ống trong dải tần số 60 Hz hoặc các bội số của nó. Bất kỳ bộ định vị hay bộ chuyển đổi I/P tốt nào cũng phải duy trì đầu ra ổn định dưới mức rung ít nhất 3 G ở 30 cps và 1 G ở 100 cps (G = gia tốc trọng trường, 31,1 ft/s²)."))
    b.append(p("Thứ ba, hãy xem xét chất lượng của khí cấp. Bạn dùng khí dụng cụ đã sấy khô và không dầu, hay khí lấy trực tiếp từ máy nén của nhà máy? Trong trường hợp sau, tránh mọi bộ định vị dùng rơ-le khuếch đại tích hợp, vì các khe hở nhỏ bên trong dễ bị tắc."))
    b.append(p("Thứ tư, hãy tính đến ảnh hưởng của thời tiết đối với lắp đặt ngoài trời, hoặc nhiệt độ môi trường cao nếu van đặt gần lò nung, chẳng hạn."))

    b.append(h2("Đáp ứng tần số và dung lượng khí",
                "Frequency response and air capacity"))
    b.append(p("Cuối cùng, ở những nơi bắt buộc phải có đáp ứng tần số tốt (điều khiển lưu lượng, bypass tuốc-bin hoặc máy nén, điều khiển áp suất, v.v.), đừng dùng bộ chuyển đổi I/P lắp trên bảng thiết bị từ xa; thay vào đó hãy lắp bộ chuyển đổi I/P ngay trên bộ truyền động van để tránh độ trễ tín hiệu.<sup>2</sup>"))
    b.append(note("<b>Chú thích 2.</b> Điều này đặc biệt quan trọng đối với các «vòng nhanh» (fast loops) như điều khiển lưu lượng hoặc áp suất, vì độ trễ thời gian do các đường truyền dài giữa bộ chuyển đổi và bộ truyền động van có thể thay đổi từ 0,2 đến 2 giây cho mỗi 10% thay đổi tín hiệu [2]."))
    b.append(p("Hãy đảm bảo dung lượng khí đầu ra của bộ chuyển đổi hoặc bộ định vị đủ để tạo tốc độ hành trình thích hợp. Lưu ý: một số bộ chuyển đổi I/P lắp giá có dung lượng khí từ 1 đến 4 SCFM, điều này giới hạn ứng dụng của chúng ở các tác vụ nhiệt độ và vận hành các van nhỏ hơn (khi không dùng bộ định vị)."))
    b.append(p("Theo quy tắc kinh nghiệm, hãy cho phép ít nhất 1 SCFH ở 20 psi cho mỗi in² diện tích màng (tín hiệu 3 đến 15 psi). Ví dụ, một van có bộ truyền động màng 100 in² cần bộ định vị có dung lượng khí đầu ra ít nhất 100 SCFH."))
    b.append(p("Với các bộ truyền động rất lớn, bạn có thể cần một rơ-le tăng áp (booster relay) giữa bộ định vị và bộ truyền động. Trong trường hợp này, nên dùng bộ tăng thể tích tỷ lệ áp suất 1:1 với chênh áp 1 psi và kim điều tiết bypass có thể chỉnh được. Chênh áp 1 psi đảm bảo bộ tăng chỉ hoạt động khi tín hiệu đầu ra từ, chẳng hạn, bộ định vị nhảy lên hơn 1 psi — thường xảy ra khi van cần mở nhanh trong trường hợp khẩn cấp (điển hình là điều khiển chống dao động máy nén, compressor surge). Kim điều tiết có thể chỉnh được giúp tránh hiện tượng mất ổn định của rơ-le tăng áp."))

    b.append(h2("Các tính năng nên có", "Desirable features"))
    b.append(p("Các tính năng mong muốn khác gồm: mọi liên kết cơ khí bên ngoài làm bằng thép không gỉ loại 18-8; mọi chi tiết nhôm được anod hóa (cả bên trong lẫn bên ngoài) và phủ epoxy; bộ định vị có ít nhất chỉnh độ lợi tích hợp; bộ chuyển đổi I/P có khả năng cho dải áp suất khí đầu ra 1 đến 17 psi (xem Chương 11 về lực nút van mất cân bằng); và nếu là thiết kế «vòng kín» (có cảm biến áp suất phản hồi tích hợp), cần có chỉnh độ lợi hoặc vùng chết để tránh mất ổn định khi lắp gần bộ truyền động màng nhỏ."))

    b.append(h2("Bộ định vị thông minh là gì?",
                "What is a smart positioner?"))
    b.append(p("Cũng như nhiều từ tiếp thị khác, thuật ngữ «bộ định vị van thông minh» (smart positioner) vẫn chưa được định nghĩa rõ ràng. Nhìn chung, nó tương đương với một bộ phát từ xa có thể lập trình, dùng giao thức HART 3 tương đương hoặc tín hiệu số hai chiều từ thiết bị fieldbus.<sup>3</sup> Tuy nhiên, hầu hết vẫn làm việc bên trong với tín hiệu tương tự 4 đến 20 mA."))
    b.append(note("<b>Chú thích 3.</b> HART là viết tắt của Highway Addressable Remote Transducer Protocol (Giao thức bộ chuyển đổi từ xa có địa chỉ trên đường truyền)."))
    b.append(p("Ở phía đầu vào, có mạch điện tử số cho phép lập trình nhiều chức năng, như đặc tính vốn có giữa tín hiệu và hành trình van (lưu ý hằng số thời gian của bộ định vị van trở nên không đồng nhất — xem lại mục trước «Những gì cần tìm khi chỉ định bộ định vị hoặc bộ chuyển đổi»), chỉnh và hiệu chỉnh hành trình van, chia dải tín hiệu (split-ranging), và vùng chết (deadband). Dù vậy, tín hiệu đầu ra cuối cùng tới cơ cấu chuyển đổi khí thường vẫn ở dạng tương tự."))
    b.append(p("Hầu hết các thiết bị này không cần nguồn điện ngoài, do đó chúng an toàn nội tại (chống nổ) khi lắp đúng rào chắn (barriers). Bộ định vị fieldbus có thể thực hiện chức năng của bộ điều khiển tỷ lệ–tích phân–vi phân (PID), tức là đóng vai trò bộ điều khiển phân tán với đầu vào từ các bộ phát số hoặc máy tính. Sự cố của mạch điện tử trong bộ định vị chỉ ảnh hưởng tới vòng điều khiển tại chỗ."))
    b.append(p("Dù các bộ định vị này có giá cao hơn khoảng một phần ba so với loại tương tự, chúng có thể giám sát van điều khiển. Ví dụ, chúng báo cho máy tính biết vị trí hành trình hiện tại, và bằng cách đo mối quan hệ giữa tín hiệu bộ định vị và áp suất khí đầu ra tới bộ truyền động, chúng nhận ra sự khởi phát của vùng chết quá lớn (chẳng hạn nhân viên bảo trì siết quá chặt vật liệu làm kín thân van — stem packing). Mặt khác, hiệu chỉnh từ xa điểm zero và span của bộ định vị sau khi lắp đặt, dù được quảng cáo là tính năng quan trọng, rất hiếm khi thực hiện."))

    b.append(h2("Phần cứng và điều khiển tại chỗ",
                "Hardware and local control"))
    b.append(p("Có lẽ đáng chú ý hơn là phần cứng trong các bộ định vị này. Trong một mẫu, một vi điều khiển ra lệnh mở một van áp điện (piezoelectric) để cấp khí cho bộ truyền động khi tín hiệu tăng, và ra lệnh mở van áp điện thứ hai để xả khí khi tín hiệu giảm. Nếu tín hiệu không thay đổi thì cả hai van áp điện đều đóng, từ đó có tuyên bố về mức tiêu thụ khí thấp. Các thiết bị này cần một vùng chết tối thiểu để tránh hiện tượng «hunt» (dao động qua lại) của hai van đối kháng. Tuy nhiên, đa số bộ định vị thông minh hoặc số dùng bộ chuyển đổi I/P tích hợp để tạo tín hiệu khí nén đầu ra. Tất cả các bộ định vị này đều vận hành từ tín hiệu 4 đến 20 mA hiện có, không cần nguồn điện phụ."))
    b.append(p("Mạch điện tử của bộ định vị số có thể chứa mạch điều khiển PID để thực hiện các chức năng điều khiển chính (máy tính đảm nhận việc ghi đè giám sát và thay đổi giá trị đặt). Các phiên bản tương lai có thể cung cấp chức năng điều khiển tiên tiến hơn như «logic mờ» (fuzzy logic). Hãy lưu ý điều kiện môi trường tại chỗ trước khi dùng bộ định vị làm bộ điều khiển tại chỗ — ví dụ van có thể đặt trong phòng lò hơi nóng và ẩm, hoặc phải chịu độ giảm áp lớn kèm rung động cao, tất cả đều có thể ảnh hưởng đến độ tin cậy của vòng điều khiển. Một số nhà cung cấp đưa ra bộ định vị lắp từ xa dùng thiết bị đo vị trí thân van bằng điện tử để báo cho bộ định vị biết hành trình của van."))

    b.append(h2("Van thông minh với lưu lượng kế tích hợp",
                "Smart valve with a built-in flow meter"))
    b.append(p("Việc dùng van như một hệ thống điều khiển phân tán đã được áp dụng trong một số thiết kế van thông minh (minh họa trên Hình 10-2), với lưu lượng kế tích hợp gồm các phần tử đo áp suất áp điện đặt phía trước và phía sau lỗ tiết lưu của van, cộng thêm một cảm biến nhiệt độ. Khi biết diện tích lỗ tiết lưu (Cv) ở một vị trí hành trình nhất định, độ chênh áp qua nó và mật độ (là hàm của áp suất và nhiệt độ), ta có thể tính toán và điều khiển lưu lượng chảy qua van (xem sơ đồ tương tự trên Hình 10-3)."))
    b.append(fig(2, F.fig_f102()))
    b.append(p("Van thông minh có nhiều ưu điểm. Thứ nhất, chúng cho dải lưu lượng rộng hơn (đến 100:1) so với lưu lượng kế (khoảng 25:1), vì nút van di động đóng vai trò lỗ tiết lưu thay đổi được. Thứ hai, dùng van thông minh loại bỏ các sai số phát sinh khi chuyển đổi từ tín hiệu tương tự sang số. Cuối cùng, chúng đáp ứng nhanh hơn khi vòng điều khiển bị nhiễu loạn."))
    b.append(p("Dù đắt hơn đáng kể so với van thông thường, các van này có thể là yếu tố quan trọng trong sơ đồ điều khiển phức tạp hơn — chẳng hạn khi muốn điều khiển nhiệt độ trong một tháp chưng cất (fractionator) (hệ thống điều khiển nhiệt độ có hằng số thời gian và độ trễ lớn) mà môi trường gia nhiệt là hơi nước. Điều này đòi hỏi hệ thống điều khiển áp suất hoặc lưu lượng tương tác với điều khiển nhiệt độ trong một cấu trúc xếp tầng điển hình. Ở đây, van thông minh là lựa chọn lý tưởng để điều khiển cấp hơi tới bộ trao đổi nhiệt. Dù bộ điều khiển nhiệt độ chịu độ trễ (điển hình cho sự thay đổi nhiệt độ), van thông minh điều khiển hơi có thể phản ứng gần như tức thì trước mọi nhiễu loạn, chẳng hạn ở áp suất hơi tại chỗ."))
    b.append(p("Hãy nhớ rằng ngay cả van thông minh nhất cũng không thay thế được lưu lượng kế. Hình học thay đổi của bộ lõi (trim), hiện tượng bám thành (hiệu ứng Coandă), xâm thực mới phát sinh (incipient cavitation), dòng bị nghẽn (choked flow) và, cuối cùng nhưng không kém phần quan trọng, tiếng ồn do độ nhiễu loạn của van mà cảm biến áp suất thu được khiến phép đo quá không chính xác. Tuy nhiên, điều này không quan trọng đối với điều khiển: ở đây không phải giá trị tuyệt đối của lưu lượng là quyết định, mà là độ lệch của nó cần được điều khiển."))

    b.append(h2("Bộ định vị số nâng cấp van hiện có",
                "Digital positioners enhance existing valves"))
    b.append(p("Nhờ tiến bộ trong lĩnh vực điều khiển tự động, bộ định vị thông minh hay số nâng cao chức năng của mọi van điều khiển hiện có, nhờ đó mang lại mức độ linh hoạt cao hơn. Hình 10-3 cho thấy sơ đồ nguyên lý của một bộ định vị như vậy. Liên lạc từ máy tính giám sát có thể đi trên dây tín hiệu 4 đến 20 mA hiện có hoặc qua dây fieldbus. Chính các dây này cũng trả thông tin phản hồi về trạng thái của van tới máy tính hoặc bảng hiển thị. Thông tin phản hồi có thể được truyền ở dạng số qua giao thức HART chồng trên tín hiệu tương tự 4 đến 20 mA — thậm chí khi van đang vận hành, dù cần phần mềm đặc biệt ở đầu nhận để giải mã thông điệp. Trong các giao thức truyền thông hoàn toàn số như Foundation Fieldbus, cả tín hiệu lẫn thông tin phản hồi đều được truyền ở dạng số."))
    b.append(fig(3, F.fig_f103()))
    b.append(p("Bo mạch in trên Hình 10-3 đóng vai trò bộ điều khiển và bộ xử lý tín hiệu trên bo. Đây thường là phần tử được bọc kín và có thể thay thế tại hiện trường. Mạch so sánh mức tín hiệu này với tín hiệu từ cảm biến vị trí thân van; nếu hai tín hiệu không giống nhau, nó đưa ra tín hiệu hiệu chỉnh tới phần tử chuyển đổi I/P, đầu ra của phần tử này được rơ-le riêng biệt khuếch đại trước khi đưa tới bộ truyền động khí nén của van như «áp suất đầu ra» nhằm hiệu chỉnh sai số vị trí thân van."))
    b.append(p("Một cảm biến áp suất riêng biệt là yếu tố then chốt của mạch chẩn đoán tích hợp. Ví dụ, bằng cách đo áp suất đầu ra cần thiết để đưa thân van tới 50% hành trình, rồi so sánh với áp suất (ở 50% hành trình) đo được khi van còn mới, ta có thể phát hiện mòn, tắc nghẽn hoặc có thể hộp làm kín bị siết quá chặt. Dữ liệu này được phản hồi như đã trình bày để báo cho nhân viên vận hành và có thể khởi động công việc bảo trì van. Việc thử nghiệm bảo trì phòng ngừa này có thể thực hiện sau khi dừng quá trình, hoặc tại hiện trường trong điều kiện vận hành thực tế (in situ). Cách sau có ưu điểm là phản ánh đúng điều kiện làm việc thực tế như nhiệt độ và áp suất tại chỗ; tuy nhiên, thử nghiệm chỉ có thể thực hiện bằng cách dịch chuyển thân van từng bước nhỏ để tránh nhiễu loạn lớn cho biến được điều khiển. Vì vậy, cách này không được áp dụng rộng rãi."))

    b.append(h2("Tóm tắt: thiết bị số so với thiết bị tương tự",
                "Summary: digital versus analog field devices"))
    b.append(p("Dưới đây là bảng tóm tắt các thiết bị số so với thiết bị trường tương tự, trích từ Tài liệu tham khảo 3."))
    b.append(ol([
        "Độ chính xác tăng lên, từ 0,1% đến 1%, so với 0,3% đến 2% của thiết bị tương tự.",
        "Ổn định tốt hơn, khoảng 0,1%, so với 0,1% đến 0,75% của thiết bị tương tự.",
        "Độ phạm vi (rangeability) rộng hơn (không làm giảm độ chính xác), tới 50:1 so với 10:1.",
        "Khả năng đa chức năng, chẳng hạn thích ứng với động học của quá trình.",
        "Khả năng chẩn đoán và tự kiểm tra.",
        "Khả năng thu nhỏ kích thước (miniaturization).",
        "Khả năng hiệu chỉnh và điều chỉnh không cần tiếp cận vật lý tới thiết bị.",
        "Khả năng khai thác các hiệu ứng vật lý mà phương tiện tương tự không đo lường hoặc đánh giá được.",
        "Xử lý số tiêu thụ rất ít năng lượng, cho phép an toàn nội tại theo chính sách «bộ ba» (triad) bao gồm các quy phạm CSA (Hoa Kỳ) · CENELEC (Châu Âu) · CESI (Nhật Bản).",
    ]))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Chọn bộ định vị hay bộ chuyển đổi",
                "Choosing a positioner or transducer"))
    b.append(p("Most control loops use a 4 to 20 mA analog or digital signal, so you are forced to transduce the electronic signal into a pneumatic one or use a digital positioner. If you have to use an analog signal (4 to 20 mA), then an I/P positioner is your choice; an alternative is to specify an I/P transducer and direct its output to a pneumatic positioner. Note: although pneumatic positioners may be on the way out, they still have cost advantages and are, by design, explosion-proof."))

    b.append(h2("Kiểm tra điều kiện lắp đặt",
                "Checking the installation conditions"))
    b.append(p("First, consider whether the valve is installed in an area where flammable liquids are handled and vapors may exist. You may need an explosion-proof (or intrinsically safe) version."))
    b.append(p("Second, check the vibration level at the valve location. For example, if the valve is close to a centrifugal pump, pipe vibrations can exist in the 60 Hz frequency range or multiple modes thereof. Any good I/P positioner or transducer should maintain steady output under vibration levels of at least 3 G at 30 cps and 1 G at 100 cps (G = acceleration of gravity, 31.1 ft/s²)."))
    b.append(p("Third, consider the quality of the air supply. Do you use dehydrated and oil-free instrument air, or air taken directly off the factory compressor? In the latter case, avoid all positioners that utilize built-in amplifying relays, because the small passages may be subject to plugging."))
    b.append(p("Fourth, consider the effects of weather on an outdoor installation, or high ambient temperature if the valve is located near a furnace, for example."))

    b.append(h2("Đáp ứng tần số và dung lượng khí",
                "Frequency response and air capacity"))
    b.append(p("Finally, where good frequency response is a must (flow control, turbine or compressor bypass, pressure control, etc.), do not use an I/P transducer that is rack mounted on a remote instrument panel. Instead, mount the I/P transducer on the valve actuator to avoid signal delays.<sup>2</sup>"))
    b.append(note("<b>Footnote 2.</b> This is especially important for “fast loops” such as flow or pressure control applications because time lags due to long transmission lines between transducers and valve actuators may vary from 0.2 to 2 s per 10% signal change [2]."))
    b.append(p("Make sure the air output capacity of the transducer or positioner is sufficient to give adequate travel speed. Note: some rack-mounted I/P transducers have air capacities of 1 to 4 SCFM, which limits their use to temperature applications and the operation of smaller valves only (if no positioner is used)."))
    b.append(p("As a rule of thumb, allow at least 1 SCFH at 20 psi supply per in² of diaphragm area (3 to 15 psi signal). For example, a valve with a 100 in² diaphragm actuator should need a positioner with at least a 100 SCFH air output capacity."))
    b.append(p("For very large actuators, you may need a booster relay between the positioner and actuator. In this case, a 1:1 pressure-ratio volume booster with a 1 psi differential and an adjustable bypass needle valve is recommended. The 1 psi differential ensures that the booster is activated only when the signal output from, for example, the positioner jumps by more than 1 psi. This is usually the case if the valve should open fast in the event of an emergency (a typical compressor surge control application). The adjustable needle valve can be tuned to avoid the instability of the booster relay."))

    b.append(h2("Các tính năng nên có", "Desirable features"))
    b.append(p("Other desirable features are: all exterior linkages to be type 18-8 stainless steel; all aluminum parts to be anodized (interior and exterior) and epoxy coated; positioners to have at least a built-in gain adjustment; I/P transducers to have the capability for a 1 to 17 psi air output range (see Chapter 11 for information on off-balance plug forces); and, if of “closed-loop” design (with built-in pressure transducer feedback), a gain or deadband adjustment to avoid instability when mounted close to a small diaphragm actuator."))

    b.append(h2("Bộ định vị thông minh là gì?",
                "What is a smart positioner?"))
    b.append(p("As is the case with many marketing catchwords, the term “smart positioner” is not yet well defined. It generally is the equivalent of a remote programmable transmitter using the equivalent HART 3 protocol or a bidirectional digital signal from a fieldbus device.<sup>3</sup> Nevertheless, most still work internally with a 4 to 20 mA analog signal."))
    b.append(note("<b>Footnote 3.</b> HART stands for Highway Addressable Remote Transducer Protocol."))
    b.append(p("On the input side, there are digital electronics that allow for programmable input, such as the inherent characteristic between the signal and valve travel (note the resultant nonuniform valve positioner time constant — refer to the previous section, “What to Look for When Specifying Positioners or Transducers”), the adjustment and calibration of valve travel, split-ranging, and deadband. Nevertheless, the final output signals to the air conversion mechanisms are usually in analog form."))
    b.append(p("Most of these devices do not need external power and are, therefore, intrinsically safe (explosion-proof) when the proper barriers are installed. Fieldbus positioners can perform the functions of a proportional, integral, and derivative (PID) controller, acting as a decentralized controller with inputs from digital transmitters or computers. Failure of the electronic positioner circuit affects only the local loop."))
    b.append(p("While these positioners cost about one-third more than their analog counterparts, they can monitor the control valve. For example, they can tell the computer the current travel position, and by measuring the relationship between the positioner signal and the air output pressure to the actuator, they can identify the onset of too much deadband (e.g., a maintenance person tightens the stem packing too much). On the other hand, remote calibration of the positioner's zero and span setting after installation, while touted as an important feature, will rarely happen."))

    b.append(h2("Phần cứng và điều khiển tại chỗ",
                "Hardware and local control"))
    b.append(p("Perhaps of more interest is the hardware in these positioners. In one model, a microcontroller commands one piezoelectric valve to open to admit air to the actuator on an increase in signal and can command a second piezoelectric valve to open to exhaust the air from the actuator on a decrease in signal. If there is no signal change, then both piezoelectric valves stay closed; hence the claim of low air consumption. These devices require a minimum deadband in order to prevent “hunting” of the opposing valves. However, the majority of smart or digital positioners employ built-in I/P transducers to generate the pneumatic output signal. All these positioners can operate from the current 4 to 20 mA signal. No auxiliary power is required."))
    b.append(p("Digital positioner electronics can include PID control circuitry to perform the primary control functions (the computer will do the supervisory override and the changing of set points). Future versions may offer more advanced control functions such as “fuzzy logic.” Be aware of the local environmental situation at the valve's location before using the positioner as a local controller. For example, the valve may be situated in a boiler room with a hot and humid atmosphere, or it may handle a high-pressure drop with the associated high vibration level, all of which potentially affect the reliability of the control loop. Some vendors offer remotely mounted positioners using electronic stem position measuring devices that tell the positioner the valve's travel position."))

    b.append(h2("Van thông minh với lưu lượng kế tích hợp",
                "Smart valve with a built-in flow meter"))
    b.append(p("Using the valve as a decentralized control system is already done in some smart valve designs (shown schematically in Figure 10-2) that include a built-in flow meter consisting of piezoelectric pressure-measuring elements upstream and downstream of the valve orifice plus a temperature sensor. Knowing the orifice area (Cv) at a given travel position, the differential pressure across it, and the density (a function of pressure and temperature), the flow rate across the valve can be calculated and controlled (for a similar schematic, see Figure 10-3)."))
    b.append(fig(2, F.fig_f102()))
    b.append(p("Smart valves have many advantages. First, they offer a higher range of flow rates (up to 100:1) than flowmeters (about 25:1) because the movable valve plug acts as a variable orifice. Second, the use of smart valves will eliminate the errors produced by converting from analog to digital signals. Finally, they offer a faster response to loop upsets."))
    b.append(p("While they are much more expensive than their conventional counterparts, such valves can be an important element in more complex control schemes; for example, when you want to control the temperature in a fractionator (a temperature control system with long time constants and time lags) in which the heating medium is steam. This needs a pressure or flow control system that interacts with the temperature control in a typical cascade system. Here the smart valve is the ideal choice for controlling the supply of steam to the heat exchanger. Although the temperature controller experiences time lags (typical for temperature changes), the smart valve controlling the steam can react nearly instantly to any upsets in, for example, the local steam pressure."))
    b.append(p("Remember, even the smartest valve is no substitute for a flow meter. The variable geometry of the trim, wall attachment phenomenon (Coandă effect), incipient cavitation, choked flow, and, last but not least, the noise picked up by the pressure transducer due to valve turbulence make it much too inaccurate. Nevertheless, this does not matter for control. Here it is not the absolute value of the flow rate that counts, but the deviation thereof that must be controlled."))

    b.append(h2("Bộ định vị số nâng cấp van hiện có",
                "Digital positioners enhance existing valves"))
    b.append(p("As a result of progress in the automated control field, smart or digital positioners enhance the function of all currently available control valves and, therefore, offer a higher degree of flexibility. Figure 10-3 shows a schematic view of such a positioner. Communication from a supervisory computer can travel over the present 4 to 20 mA signal wires or through fieldbus wiring. These same wires give feedback information regarding the valve's status to a computer or a display panel. This feedback information can be transmitted in digital form via HART protocol over the analog 4 to 20 mA signal. This can be done even while the valve is operating, although special software is required on the receiving end to decode the messages. In fully digital communication protocols such as Foundation Fieldbus, both signal and return information will be transmitted in digital form."))
    b.append(fig(3, F.fig_f103()))
    b.append(p("The printed circuit board in Figure 10-3 acts as the onboard controller and signal processor. This is typically an encapsulated and field-replaceable element. The circuitry compares this signal level to the signal coming from the stem position sensor and, if not identical, puts out a corrective signal to the I/P transducer element whose output is amplified in a separate relay before being fed to the pneumatic valve actuator as “output pressure” to correct the stem position error."))
    b.append(p("A separate pressure sensor is a key element for the integral diagnostic circuit. For example, by measuring the required output pressure to move the valve stem to 50% travel, and then comparing it to the same pressure (at 50% travel) measured when the valve was brand-new, one can detect wear or blockage, or perhaps a too-tight packing box. Such data is fed back, as previously explained, to alert operating personnel and perhaps initiate maintenance work on the valve. Such preventive maintenance testing can be done either after the process has been shut down or in the field under actual operating conditions (in situ). The latter has the advantage of experiencing actual working conditions such as the local temperature and pressure environment. However, such testing can only be done by moving the valve stem in small increments to avoid large upsets in the controlled variable. Understandably, this is not widely practiced."))

    b.append(h2("Tóm tắt: thiết bị số so với thiết bị tương tự",
                "Summary: digital versus analog field devices"))
    b.append(p("Here is a summary of digital devices compared to analog field devices, taken from Reference 3."))
    b.append(ol([
        "Increased accuracy, 0.1% to 1%, compared to analog 0.3% to 2%.",
        "Improved stability, about 0.1%, compared to 0.1% to 0.75% analog.",
        "Wider rangeability (without sacrificing accuracy), up to 50:1 compared to 10:1.",
        "Capable of multifunctioning, such as adapting to process dynamics.",
        "Diagnostics and self-testing.",
        "Ability for miniaturization.",
        "Ability to calibrate and adjust without physical access to the instrument.",
        "Ability to utilize physical effects that cannot be measured or assessed by analog means.",
        "Digital processing can be done with little energy consumption, enabling intrinsic safety under the “triad” policy encompassing the CSA (United States) · CENELEC (European) · CESI (Japanese) codes.",
    ]))
    return "".join(b)
