# -*- coding: utf-8 -*-
"""Handbook 6.5 — Laser Interferometer Displacement Sensors."""
import hb06fig as F
from hb06_common import eq, fig, h2, h3, nav, note, p, quote, refs, table, ul


def body_vi():
    b = []
    b.append(p(
        "Trong những năm gần đây, người ta đã phát triển được những máy công cụ điều khiển số có độ chính xác rất "
        "cao. Để khai thác được tiềm năng chính xác của những máy ấy, phải thực hiện các phép đo chiều dài và dịch "
        "chuyển có độ phân giải vượt quá chữ số có nghĩa nhỏ nhất của máy. Thiết bị đo như vậy thường không thể dựa "
        "vào thước cơ khí."))
    b.append(p(
        "Giao thoa kế laser so sánh sự thay đổi chiều dài quang trình với bước sóng ánh sáng — đại lượng có thể chọn "
        "từ các hằng số nguyên tử xác định được với rất ít bất định."))
    b.append(p(
        "Năm 1983 đã có một lần định nghĩa lại mét [1], sau lần định nghĩa năm 1960. Định nghĩa cũ dựa trên bước "
        "sóng của một bức xạ nhất định (chuẩn krypton-86) và không thể thực hiện được chính xác hơn 4 phần trong "
        "10⁹. Định nghĩa mới dựa trên tần số nhưng không gắn với bất kỳ bức xạ cụ thể nào, đã mở đường cho những "
        "cải thiện đáng kể về độ chính xác thực hiện mét. Theo khuyến nghị trong nghị quyết 2 về việc thực hiện mét "
        "trong thực tiễn, bước sóng trong chân không λ<sub>v</sub> của một sóng điện từ phẳng tần số f là "
        "λ<sub>v</sub> = c/f, với c là tốc độ ánh sáng trong chân không, c = 299 792 458 m·s⁻¹ đúng chính xác. Như "
        "vậy bước sóng được gắn với tần số và thời gian — những đại lượng có thể đo với độ chính xác cao nhất trong "
        "toàn bộ Hệ đơn vị quốc tế (SI)."))
    b.append(p(
        "Để độc lập với mọi tham số môi trường, mét được định nghĩa bằng tốc độ ánh sáng trong chân không. Tuy vậy, "
        "giao thoa kế thường phải làm việc trong không khí xung quanh. Vì thế các tham số môi trường ảnh hưởng tới "
        "tốc độ ánh sáng trong một môi trường cụ thể (không khí) sẽ tác động và làm suy giảm độ chính xác của phép "
        "đo."))
    b.append(p(
        "Ba yếu tố chính giới hạn độ chính xác tuyệt đối đạt được của giao thoa kế laser làm việc trong không khí: "
        "(1) bất định của bước sóng chân không λ<sub>v</sub> của nguồn laser; (2) bất định của chiết suất không khí "
        "xung quanh; và (3) độ phân giải chia nhỏ nhất của giao thoa kế."))
    b.append(p(
        "Mục này được tổ chức như sau. Trước hết trình bày một số nguyên lý laser cơ bản, gồm cả các cách ổn định "
        "bước sóng chân không của laser. Hiệu ứng thường được dùng nhất để ổn định laser trong các giao thoa kế "
        "thương mại là hiệu ứng Zeeman, cho bất định tương đối 10⁻⁸. Thứ hai, bàn về chiết suất không khí — một yếu "
        "tố chính khác giới hạn độ chính xác đạt được của giao thoa kế làm việc trong không khí; sẽ chỉ ra rằng hiện "
        "nay không thể xác định đại lượng này với bất định tốt hơn 5 × 10⁻⁸. Cuối cùng, mục này mô tả giao thoa kế "
        "Michelson được dùng rộng rãi nhất và hai biến thể của nó cho phép đo chiều dài hành trình dài, kèm độ phân "
        "giải của chúng."))

    # ---------------------------------------------------------------- laser
    b.append(h2("Laser heli–neon", "Helium–neon laser"))
    b.append(p(
        "Để đạt độ chính xác tốt nhất có thể, phải hết sức cẩn thận bảo đảm độ ổn định bước sóng cao nhất của nguồn "
        "sáng. Gần như mọi thước đo kích thước giao thoa đều dùng laser heli–neon, vì nó đã chứng tỏ đáng tin cậy, "
        "bước sóng phát ra nằm trong vùng nhìn thấy ở khoảng 633 nm, và có thể ổn định đủ tốt nhờ hiệu ứng Zeeman, "
        "hoặc tốt hơn nữa nhờ một vạch hấp thụ iốt được xác định rất rõ, cũng ở ≈ 633 nm [1, 2]."))
    b.append(p(
        "Laser heli–neon gồm một ống phóng điện như trên Hình 6-46 [3], nạp các khí đơn đồng vị: heli (He³) ở áp "
        "suất riêng phần ≈ 10⁵ Pa và neon (Ne²⁰) ở áp suất riêng phần ≈ 13 Pa. Ống được bơm điện bằng điện áp cỡ "
        "kilôvôn với dòng vài miliampe để kích thích cả nguyên tử heli lẫn neon. Vì heli là thành phần chiếm đa số, "
        "nó chi phối tính chất phóng điện của ống laser. Các nguyên tử heli trung hoà va chạm với điện tử tự do được "
        "điện áp dọc trục gia tốc, bị kích thích và tồn tại ở hai trạng thái siêu bền có thời gian sống khá dài. "
        "Các trạng thái này đủ gần mức năng lượng của một số trạng thái kích thích của nguyên tử neon để có thể xảy "
        "ra truyền năng lượng do va chạm giữa hai nhóm nguyên tử. Nguyên tử heli bị kích thích có thể rơi về trạng "
        "thái cơ bản, đồng thời nguyên tử neon nhận được gần như đúng lượng năng lượng ấy. Vì vậy heli chỉ có nhiệm "
        "vụ kích thích nguyên tử neon, không đóng góp vào việc phát xạ ánh sáng. Nguyên tử neon bị kích thích tồn "
        "tại ở trạng thái kích thích khá lâu (cỡ 10⁻³ s). Chúng trở về mức năng lượng thấp hơn bằng phát xạ cảm ứng "
        "ánh sáng có tính kết hợp cao. Phát xạ cảm ứng này phát huy tác dụng khi ánh sáng do một số nguyên tử neon "
        "phát ra lại kích thích các nguyên tử khác phát xạ."))
    b.append(fig(46, F.fig_6_46(), "vi"))
    b.append(p(
        "Các gương của hốc cộng hưởng laser, nhờ phản xạ phần lớn ánh sáng tới, khiến ánh sáng đi qua thể tích hoạt "
        "động của laser nhiều lần, do đó khuếch đại mạnh nếu chiều dài hốc L là bội số nguyên m của nửa bước sóng λ:"))
    b.append(eq("L = m · λ/2", "6.70"))
    b.append(p(
        "Ánh sáng phát ra khá đơn sắc, nhưng vẫn có độ rộng vạch phổ hữu hạn xác định bởi các phát xạ ngẫu nhiên của "
        "Ne²⁰. Các cửa sổ đầu ống phóng điện đặt ở góc Brewster [4] truyền ánh sáng có phân cực thẳng thích hợp nếu "
        "muốn. Các gương đầu phải được mài bóng cẩn thận, bán kính cong phải thoả điều kiện ổn định. Chúng có lớp "
        "phủ điện môi chọn lọc bước sóng với hệ số phản xạ rất cao, đôi khi vượt 99 %."))
    b.append(p(
        "Nếu không có biện pháp đặc biệt, laser He–Ne sẽ phát nhiều mode dọc như trên Hình 6-47, tạo ra một tần số "
        "phách giới hạn tính kết hợp thời gian và khiến laser không dùng được cho mục đích giao thoa. Ngoài ra, do "
        "sự giãn nở nhiệt của ống laser, các gương đầu sẽ thay đổi khoảng cách tương đối, do đó thực chất làm chỉnh "
        "bước sóng trong phạm vi độ rộng vạch của đường cong khuếch đại."))
    b.append(fig(47, F.fig_6_47(), "vi"))
    b.append(p(
        "Một tính chất quan trọng khác của laser He–Ne chất lượng cao là biên dạng mặt cắt Gauss, được duy trì dọc "
        "theo sóng lan truyền, tức là mode ngang cơ bản. Đây cũng là điều kiện cần để các mặt sóng giữ được tính gần "
        "phẳng."))

    b.append(h3("Ổn định tần số laser He–Ne", "Frequency stabilization of He–Ne lasers"))
    b.append(p(
        "Tần số cộng hưởng (và bước sóng λ) của laser được quyết định một phần bởi khoảng cách giữa hai gương đầu "
        "và một phần bởi chiết suất n<sub>M</sub> của môi trường hoạt động (hỗn hợp He–Ne). Vì độ rộng vạch của biên "
        "dạng khuếch đại của môi trường hoạt động thường cỡ gigahéc, nhiều mode dọc có thể cùng cộng hưởng trong "
        "hốc, như trên Hình 6-47. Hiệu tần số ∆f giữa hai mode dọc kề nhau là dải phổ tự do (FSR), cho bởi phương "
        "trình 6.71, chỉ phụ thuộc chiều dài hốc L, chiết suất môi trường hoạt động n<sub>M</sub> và tốc độ ánh sáng "
        "trong chân không c:"))
    b.append(eq("∆f = c / (2 n<sub>M</sub> L)", "6.71"))
    b.append(p(
        "Do sự giãn nở nhiệt của hốc laser và/hoặc sự thay đổi chiết suất của môi trường hoạt động do nhiệt, mọi "
        "mode cộng hưởng của laser sẽ dịch chuyển trong đường bao của biên dạng khuếch đại. Nỗ lực ổn định bước "
        "sóng laser, hay tương đương là ổn định tần số của nó, nhằm khoá các mode so với biên dạng khuếch đại và "
        "giảm số mode cùng cộng hưởng đồng thời."))

    b.append(h3("Hiệu ứng Zeeman dọc", "Longitudinal Zeeman effect"))
    b.append(p(
        "Một trong những hiệu ứng thường được dùng nhất để ổn định tần số laser He–Ne cho phép đo khoảng cách là "
        "hiệu ứng Zeeman [3, 5]. Ống của laser cần ổn định tần số được gắn bên trong một nam châm vĩnh cửu dọc trục "
        "như trên Hình 6-48. Nhờ chọn chiều dài hốc ngắn, dải phổ tự do ∆f của laser lớn. Vì thế phát xạ laser xuất "
        "hiện như một mode dọc duy nhất khi chiều dài hốc được điều khiển thích hợp. Một từ trường đặt từ bên ngoài "
        "theo phương dọc làm các tần số chuyển mức của nguyên tử neon tách đối xứng quanh tần số danh định, khoảng "
        "tách tần số tỉ lệ với cường độ từ trường. Hiện tượng này gọi là hiệu ứng Zeeman dọc."))
    b.append(fig(48, F.fig_6_48(), "vi"))
    b.append(p(
        "Với cường độ từ trường đặt vào, mode dọc duy nhất của laser He–Ne tách thành hai mode phân cực tròn phải và "
        "trái với hiệu tần số điển hình 1,5 MHz. Hiệu tần số này phụ thuộc tần số laser và đạt cực trị khi tần số "
        "laser trùng đúng tần số chuyển mức nguyên tử. Việc ổn định tần số được thực hiện bằng điều khiển chiều dài "
        "hốc sao cho tần số được khoá vào giá trị cực trị tương ứng với tần số danh định của laser. Để xác định tần "
        "số laser thực tế nằm ở đâu trong biên dạng khuếch đại, chiều dài hốc được điều biến tuần hoàn bằng một bộ "
        "chấp hành áp điện như trên Hình 6-48. Hiệu tần số được theo dõi liên tục tại điểm giãn nở nhỏ nhất và lớn "
        "nhất của chu kỳ điều biến. Khi hai giá trị cực trị bằng nhau, hiệu tần số sẽ đạt cực đại, nghĩa là đã đạt "
        "tần số danh định của laser. Điều này đạt được bằng cách điều khiển chiều dài hốc laser."))
    b.append(p(
        "Chiều dài hốc được điều khiển cả bằng sự giãn nở nhiệt của ống laser — đặt sát một lò điện trở có dòng làm "
        "việc thay đổi được theo thang ít động — lẫn, trên thang thời gian rất ngắn, bằng một bộ chấp hành áp điện "
        "gắn vào một trong hai mặt đầu của hốc [5]. Bộ chấp hành nhanh này chỉ cho biên độ hạn chế, điển hình dưới "
        "một bước sóng. Vì vậy phải dùng giãn nở nhiệt để đạt biên độ điều biến lớn hơn. Để có độ ổn định tần số "
        "laser cao nhất có thể, các hiệu tần số được đo trong khoảng thời gian rất ngắn, và độ lệch so với giá trị "
        "danh định được đưa trở lại qua một vòng điều khiển kín tới các cơ cấu định vị cơ–điện và nhiệt."))
    b.append(p(
        "Độ ổn định tần số ngắn hạn và dài hạn ∆f/f của một laser ổn định như vậy có thể đạt tới 2 × 10⁻⁸, tuỳ "
        "thuộc cả vào các tham số của vòng hồi tiếp."))
    b.append(p(
        "Một hiện tượng khác vượt xa độ ổn định đạt được bằng hiệu ứng Zeeman dùng một vạch hấp thụ riêng của đồng "
        "vị iốt (¹²⁷I₂, chuyển mức 11-5, R(127), thành phần i) và khoá laser He–Ne [2, 6] vào tần số được xác định "
        "rất rõ ấy. Bước sóng của nó λ<sub>I</sub> = 632,9913981 nm rất gần một trong các bước sóng danh định của "
        "laser He–Ne, nên việc này dễ thực hiện; tuy vậy thiết bị cần thiết, gồm cả phần điện tử tinh vi, khá phức "
        "tạp [2]. Vì lý do ấy, laser He–Ne ổn định bằng iốt chỉ được dùng ở nơi cần độ chính xác rất cao. Bất định "
        "tương đối ước tính tổng cộng của một laser ổn định như vậy là ±10⁻⁹ (suy từ độ lệch chuẩn tương đối ước "
        "tính 3,4 × 10⁻¹⁰ [1]), khiến nó phù hợp cho việc thực hiện thực tiễn các chuẩn sơ cấp và thứ cấp."))

    # ---------------------------------------------------------------- refractive index
    b.append(h2("Chiết suất của không khí", "Refractive index of air"))
    b.append(p(
        "Thang chiều dài của một giao thoa kế dịch chuyển làm việc trong không khí xung quanh được cho bởi "
        "λ<sub>A</sub> = λ<sub>V</sub>/n<sub>A</sub>, trong đó λ<sub>A</sub> là bước sóng của nguồn trong không khí, "
        "λ<sub>V</sub> là bước sóng trong chân không và n<sub>A</sub> là chiết suất của không khí. Bước sóng chân "
        "không λ<sub>V</sub> liên hệ với tốc độ ánh sáng qua λ<sub>V</sub> = c/f₀. Hằng số c — tốc độ ánh sáng trong "
        "chân không — được định nghĩa lại năm 1983 [1]. Nay nó được định nghĩa đúng chính xác là c = 299 792 458 "
        "m·s⁻¹. Do đó, để đo khoảng cách bằng giao thoa, điều thiết yếu là phải biết chiết suất của không khí với độ "
        "chính xác không kém độ ổn định và mức độ xác định của bước sóng chân không của nguồn sáng."))
    b.append(p(
        "Theo Edlén [7, 8] và Owens [9], chiết suất là hàm của áp suất khí quyển P, nhiệt độ T, độ ẩm tương đối H "
        "— hoặc cách khác là áp suất riêng phần của hơi nước trong không khí e<sub>s</sub> — và nồng độ cacbon "
        "đioxit theo thể tích D. Thành phần tiêu chuẩn theo thể tích của không khí khô là 78,03 % N₂, 20,99 % O₂, "
        "0,933 % Ar, 0,035 % CO₂ và một số thành phần vết khác, chủ yếu là khí hiếm [10]. Thành phần duy nhất trong "
        "danh sách trên có thể biến thiên là CO₂, với xu hướng tăng dài hạn, có lẽ gắn với việc đốt nhiên liệu hoá "
        "thạch [11]. Giá trị hiện nay là ≈ 350 ppm theo thể tích và đang tăng ≈ 1,4 ppm mỗi năm. Nồng độ CO₂ trong "
        "không khí cũng có thể thay đổi trong môi trường công nghiệp do các nguồn phát CO₂, và do đó có thể biến "
        "thiên đáng kể theo vị trí."))
    b.append(p(
        "Gần đây hơn, người ta đã công bố sự phụ thuộc của chiết suất vào các hợp chất khí không tự nhiên như "
        "hydrocacbon trong không khí [12], cũng như các hiệu chỉnh cho công thức Edlén [13–15]. Những hiệu chỉnh "
        "chiết suất do các hợp chất ấy gây ra có thể cần thiết cho các phép đo độ chính xác rất cao trong môi trường "
        "công nghiệp nơi có dùng dung môi hoá học hoặc dầu. Bảng 6.9 liệt kê một số hợp chất không tự nhiên, nồng độ "
        "tối đa cho phép tại nơi làm việc và ảnh hưởng của chúng lên chiết suất nếu có mặt tại vị trí đặt giao thoa "
        "kế."))
    b.append(table(
        ["Khí", "(n − 1)·10⁴", "Nồng độ cho ∆n/n = 10⁻⁷ (ppm)", "MWC (mg·m⁻³)", "∆n/n × 10⁷ do MWC"],
        [
            ["Không khí", "2,72", "—", "—", "—"],
            ["Propan", "10,3", "130", "1800", "8"],
            ["Butan", "12,9", "98", "2350", "10"],
            ["Êtanol", "8,1", "190", "1900", "5"],
            ["Êtyl axêtat", "13,0", "97", "1400", "4"],
            ["Đimêtylxêtôn", "10,2", "130", "2400", "9"],
            ["Octan", "23", "50", "2350", "10"],
            ["CFC, ví dụ R12", "10,3", "130", "5000", "7"],
        ],
        caption="Bảng 6.9 — Chiết suất n của một số hợp chất khí, nồng độ tối đa cho phép tại nơi làm việc (MWC) và "
                "độ thay đổi chiết suất do nồng độ ấy gây ra (T = 20 °C, P = 101,315 hPa, λ = 633 nm). Theo VDI, "
                "G. Wilkening."))
    b.append(p(
        "Jones [16] đã kết hợp một phép xác định chính xác khối lượng riêng của không khí ẩm với công thức Edlén để "
        "cho một cách biểu diễn có phần đơn giản hơn. Với một laser He–Ne ổn định bằng iốt điển hình có bước sóng "
        "chân không λ<sub>V</sub> = 632,9913 nm, công thức Jones cho bởi [17]:"))
    b.append(eq("n(P, T, H, D) = 1 + A − B", "6.72"))
    b.append(p("trong đó"))
    b.append(eq("A = 78,603 × 10⁻⁸ · (P/(T Z)) · [1 + 0,540(D − 0,0003)]", "6.73"))
    b.append(eq("B = 0,00042066 × 10⁻⁸ · (f<sub>E</sub> e<sub>s</sub> H)/(T Z)", ""))
    b.append(p(
        "Trong phương trình 6.73, P là áp suất khí quyển tính bằng pascal, T là nhiệt độ tuyệt đối tính bằng kelvin, "
        "H là độ ẩm tương đối tính bằng %, và D là nồng độ CO₂ tính bằng phần trăm thể tích. Có ba hệ số bổ sung "
        "trong công thức Jones tính đến tính không lý tưởng của không khí ẩm so với khí lý tưởng. Đó là Z — hệ số nén "
        "phản ánh tính không lý tưởng của hỗn hợp không khí và hơi nước, với không khí chứa lượng CO₂ hợp lý ở nhiệt "
        "độ từ 15 °C đến 28 °C và áp suất từ 7 × 10⁴ Pa đến 11 × 10⁴ Pa thì nằm trong khoảng 0,99949 đến 0,99979; "
        "f<sub>E</sub> là hệ số tăng cường biểu diễn việc áp suất hơi bão hoà hiệu dụng của nước trong không khí lớn "
        "hơn áp suất hơi bão hoà e<sub>s</sub>, và với các dải áp suất, nhiệt độ trên thì f<sub>E</sub> nằm giữa "
        "1,0030 và 1,0046 [16]; e<sub>s</sub> là áp suất hơi bão hoà trên mặt phẳng của nước lỏng tinh khiết, theo "
        "Jones khoảng 1705 Pa ở 15,0 °C và khoảng 3779 Pa ở 28,0 °C. Các bảng Z, f<sub>E</sub> và e<sub>s</sub> được "
        "đưa vào phần phụ lục bài báo của Jones [16]. Bảng 6.10 cho cái nhìn tổng quan về những thay đổi tham số môi "
        "trường sẽ gây ra thay đổi chiết suất tương đối 10⁻⁷."))
    b.append(table(
        ["Tham số", "Giá trị chuẩn", "Biến thiên để ∆n/n = +1 × 10⁻⁷"],
        [
            ["Áp suất P", "101,3 kPa", "+37,3 Pa"],
            ["Nhiệt độ T", "20,0 °C", "−0,1 °C"],
            ["Độ ẩm H", "40 %", "−10,0 %"],
            ["Nồng độ CO₂", "350 ppm", "+670 ppm"],
        ],
        caption="Bảng 6.10 — Các tham số của không khí chuẩn và độ lệch gây ra ∆n/n = 10⁻⁷. "
                "Theo J. Applied Optics [17]."))
    b.append(p(
        "Edlén [8] và Jones [16] ước tính rằng các biểu thức thực nghiệm của họ về sự phụ thuộc của chiết suất không "
        "khí vào các tham số đã liệt kê có bất định tuyệt đối 5 × 10⁻⁸."))
    b.append(p(
        "Ngoài giới hạn cơ bản này, còn có một số khía cạnh thực tiễn phải tính đến liên quan tới độ chính xác có "
        "thể đo các tham số môi trường. Estler [17] cho rằng áp suất khí quyển P hiện nay có thể xác định với bất "
        "định ≈ 2,7 Pa, và có thể coi là hằng số trên toàn bộ đường quang của giao thoa kế nếu nó được đặt nằm "
        "ngang. Cần lưu ý rằng ở mực nước biển, gradient áp suất là ≈ −13 Pa·m⁻¹, dẫn tới thay đổi chiết suất do áp "
        "suất gây ra là 3,4 × 10⁻⁸ m⁻¹ nếu thiết bị đo không được giữ nằm ngang."))
    b.append(p(
        "Trong một môi trường phòng thí nghiệm được kiểm soát đặc biệt tốt, nơi người ta dành sự chăm sóc đặc biệt "
        "để gradient nhiệt độ không ảnh hưởng tới chiết suất dọc đường quang nhiều nhất có thể, bất định của phép đo "
        "nhiệt độ có thể thấp tới 0,01 °C theo [17]. Độ ẩm đo bằng ẩm kế điểm sương có độ chính xác cao có thể có "
        "bất định xuống tới 0,5 %. Thay đổi nồng độ cacbon đioxit phải rất đáng kể (20 % nồng độ tự nhiên) mới gây "
        "ra ∆n/n bằng 10⁻⁸."))

    # ---------------------------------------------------------------- interferometers
    b.append(h2("Giao thoa kế Michelson", "Michelson interferometer"))
    b.append(p(
        "Cơ sở của phần lớn giao thoa kế dùng trong các thước đo kích thước giao thoa là giao thoa kế Michelson cổ "
        "điển [4], trình bày trên Hình 6-49. Ánh sáng đơn sắc kết hợp của một laser He–Ne đã ổn định bước sóng tới "
        "bộ tách chùm, chia ánh sáng thành hai chùm cường độ bằng nhau (1) và (2)."))
    b.append(fig(49, F.fig_6_49(), "vi"))
    b.append(p(
        "Hai chùm phản xạ trên gương cố định và gương có thể dịch chuyển — gương mà dịch chuyển x của nó cần đo — "
        "rồi hợp lại tại bộ tách, nơi chúng được hướng tới một thấu kính phân kỳ. Nhờ tính kết hợp của ánh sáng "
        "laser, các mặt sóng có quan hệ pha xác định với nhau. Pha này được quyết định bởi hiệu chiều dài quang "
        "trình của hai chùm trong hai nhánh 1 và 2. Nếu hiệu quang trình này thay đổi liên tục bằng cách dịch chuyển "
        "một trong hai gương, có thể quan sát thấy cường độ biến thiên hình sin tại một vị trí cố định trong không "
        "gian phía sau thấu kính dùng để tạo phân kỳ chùm, tạo thành một hệ vân vành. Lỗ nhỏ dùng để xác định chính "
        "xác vị trí quan sát, và bộ tách sóng quang thu cường độ biến thiên để xử lý tiếp."))
    b.append(p(
        "Trong cách bố trí xử lý tín hiệu cơ bản nhất, số chu kỳ sáng và tối được đưa vào một bộ đếm, bộ này đếm "
        "những thay đổi chiều dài quang trình theo bội số nguyên của λ<sub>A</sub>/2. Các cách xử lý tín hiệu tinh "
        "vi hơn không chỉ đếm chu kỳ mà còn xác định thay đổi pha tương đối trong cường độ biến thiên hình sin, nhờ "
        "đó cuối cùng có thể đạt độ phân giải λ<sub>A</sub>/512."))
    b.append(p(
        "Khi dịch chuyển gương, phải bảo đảm chuyển động êm, không có rung giật ngược của bàn trượt gương, để tránh "
        "đếm trùng vân giao thoa. Cần những ổ trượt thẳng chất lượng rất cao (như ổ khí) mới làm được điều ấy."))
    b.append(p(
        "Như thấy trên Hình 6-49, ánh sáng phản xạ từ hai gương về cơ bản đi ngược lại đúng đường của nó và ít nhất "
        "một phần tới thể tích hoạt động của nguồn laser (3), do đó tạo thành một hốc cộng hưởng laser ngoài có thể "
        "làm lệch tần laser, thực chất điều biến công suất ra cũng như bước sóng của nó. Để tránh hiệu ứng này, các "
        "phiên bản thương mại của giao thoa kế Michelson dùng gương góc ba mặt thay cho gương phẳng, cùng các bộ cách "
        "ly quang, như trên Hình 6-50 và 6-51. Tuy vậy, một số tác giả báo cáo việc dùng những bố trí quang học khai "
        "thác chính hiệu ứng này kết hợp với laser điốt để thực hiện cảm biến dịch chuyển giá rẻ, hành trình ngắn "
        "[18, 19]. Các bố trí ấy không được bàn ở đây."))

    b.append(h3("Giao thoa kế dị tần hai tần số", "Two-frequency heterodyne interferometer"))
    b.append(p(
        "Hình 6-50 trình bày giao thoa kế Michelson hai tần số bán trên thị trường, làm việc với nguồn laser He–Ne ổn "
        "định bằng hiệu ứng Zeeman. Laser này phát hai mode dọc có tần số f₁ và f₂, cả hai đều phân cực tròn theo "
        "hai chiều ngược nhau. Khi cho các mode đi qua một bản phần tư bước sóng, hai sóng phân cực thẳng trực giao "
        "được tạo ra. Cả hai được bộ tách chùm không phân cực chia ra. Ở nhánh 1 của bộ tách ấy có một bản phân cực "
        "được quay 45° so với cả hai sóng phân cực tới nó, do đó thực chất cho phép chúng giao thoa phía sau bản ấy, "
        "tạo ra hiệu tần f₂ − f₁ được một bộ tách sóng quang thu và một bộ đếm chuẩn đếm (hiệu tần điển hình "
        "1,5 MHz)."))
    b.append(fig(50, F.fig_6_50(), "vi"))
    b.append(p(
        "Hai sóng phân cực trực giao ở nhánh 2 được bộ tách phân cực chia tiếp. Thành phần phổ f₁ &lt; f₂ được "
        "truyền vào nhánh đo 3, còn thành phần tần số f₂ được phản xạ vào nhánh chuẩn 4 của giao thoa kế. Do vận tốc "
        "v của gương phản xạ ở nhánh 3 gây ra dịch chuyển x, tần số f₁ bị dịch Doppler một lượng f<sub>D</sub> "
        "(phương trình 6.74). Gương chuyển động về phía giao thoa kế cho tần số Doppler dương f<sub>D</sub> &gt; 0. "
        "Sau khi hợp lại cả hai sóng từ nhánh 3 và 4 tại bộ tách chùm, chúng được cho qua một bản phân cực ở nhánh 5 "
        "cũng quay 45° so với phương phân cực của cả hai sóng đã hợp, nhờ đó cho phép chúng giao thoa, tạo ra hiệu "
        "tần f₂ − f₁ − f<sub>D</sub> tại vị trí bộ tách sóng quang, và được một bộ đếm thứ hai đếm. Bằng cách liên "
        "tục lấy hiệu của hai số đếm, đại lượng cần đo (dịch chuyển x theo bội số của λ<sub>A</sub>/2) được tính ra."))
    b.append(p(
        "Với loại giao thoa kế này, chiều chuyển động được cho bởi dấu của số đếm thu được. Một nhược điểm của giao "
        "thoa kế dị tần hai mode là dải động hạn chế đối với vận tốc v của gương chuyển động về phía giao thoa kế, vì "
        "tần số Doppler f<sub>D</sub>, cho bởi:"))
    b.append(eq("f<sub>D</sub> = 2v / λ<sub>A</sub>", "6.74"))
    b.append(p(
        "buộc phải nhỏ hơn hiệu tần số ban đầu giữa f₂ và f₁ khi gương đứng yên. Với hiệu tần số điển hình do hiệu "
        "ứng Zeeman tạo ra f<sub>z</sub> = 1,5 MHz, vận tốc v do đó buộc phải nhỏ hơn:"))
    b.append(eq("v ≤ f<sub>z</sub> λ<sub>A</sub>/2 = 0,474 m·s⁻¹", "6.75"))
    b.append(p(
        "Không có giới hạn như vậy nếu gương chạy ra xa giao thoa kế. Bằng cách nội suy điện tử tín hiệu ra của bộ "
        "tách sóng quang, có thể đạt được độ phân giải dưới bước sóng [22]."))

    b.append(h3("Giao thoa kế đồng tần đơn mode", "Single-mode homodyne interferometer"))
    b.append(p(
        "Một bố trí giao thoa kế không bị giới hạn về vận tốc cực đại theo nghĩa trên là giao thoa kế đồng tần đơn "
        "mode trên Hình 6-51."))
    b.append(fig(51, F.fig_6_51(), "vi"))
    b.append(p(
        "Như ở giao thoa kế dị tần hai tần số, người ta thường dùng nguồn laser ổn định bằng hiệu ứng Zeeman phát hai "
        "mode dọc phân cực tròn lệch tần. Sau khi qua bản phần tư bước sóng, hai sóng phân cực trực giao được tạo "
        "ra, nhưng chỉ một trong hai (f₁) được dùng tiếp. Sóng kia (f₂) bị một bộ tách chùm phân cực định hướng "
        "thích hợp phản xạ ra khỏi đường quang. Mặt phẳng phân cực ở nhánh 1 của giao thoa kế được nghiêng 45° so "
        "với mặt phẳng xác định bởi hai nhánh 2 và 3. Bộ tách chùm phân cực thứ hai sẽ truyền một thành phần định "
        "hướng ngang vào nhánh đo 2 và phản xạ một thành phần định hướng dọc vào nhánh chuẩn 3 của giao thoa kế. Hai "
        "nhánh của giao thoa kế giữ nguyên phân cực trực giao của chúng. Tần số của mặt sóng ở nhánh 2 bị dịch do "
        "hiệu ứng Doppler (phương trình 6.74) vì gương chuyển động. Ánh sáng phản xạ bởi hai gương ba mặt được hợp "
        "lại tại bộ tách chùm phân cực và được một gương đổi hướng."))
    b.append(p(
        "Vì trong bố trí quang học đặc thù này, trạng thái phân cực của hai chùm ở hai nhánh là trực giao, nên sau "
        "gương đổi hướng ở nhánh 4 không có giao thoa như trường hợp giao thoa kế Michelson cơ bản (Hình 6-49). Sau "
        "khi qua một bản phần tư bước sóng đặt ở 45°, hai sóng phân cực tròn ngược chiều (một có tần số f₁, một có "
        "tần số f₁ ± f<sub>D</sub>) được tạo ra và có thể mô tả bằng một phasor quay (đặc trưng bởi Φ(t)) có biên độ "
        "không đổi, với tốc độ quay phụ thuộc tần số Doppler (ở nhánh 5). Có thể quan sát thấy biến thiên biên độ "
        "tại các bộ tách sóng quang A–D sau khi phasor này đi qua các bản phân cực, tức là sau khi được bộ tách chùm "
        "không phân cực chia ra."))
    b.append(p("Đầu ra của một giao thoa kế có dạng tổng quát:"))
    b.append(eq("I(t) = (I<sub>o</sub>(t)/2) · [1 + cos Φ(t)]", "6.76"))
    b.append(p(
        "Ta muốn suy ra Φ(t) từ việc quan sát I(t). Cần lưu ý rằng I<sub>o</sub>(t) — cường độ của laser — cũng có "
        "thể biến thiên theo thời gian. Những vấn đề gặp phải là (1) sự nhoè dấu của Φ(t) và (2) sự phụ thuộc của "
        "pha tính được vào biến thiên cường độ do sự già hoá của laser và các linh kiện quang. Vấn đề thứ nhất nảy "
        "sinh từ chỗ arccos(…) cho hai nghiệm của phương trình 6.76:"))
    b.append(eq("Φ(t) = ± arccos[ 2I(t)/I<sub>o</sub>(t) − 1 ]", "6.77"))
    b.append(p(
        "Có thể khử nhoè dấu bằng cách tạo thêm một tín hiệu sin(Φ(t)), tức là các tín hiệu vuông pha. Để làm vậy, "
        "cần một đầu ra thứ hai của giao thoa kế có dạng:"))
    b.append(eq("I₂(t) = (I<sub>o</sub>(t)/2) · [1 + sin Φ(t)]", "6.78"))
    b.append(p(
        "Hai phương trình 6.76 và 6.78 chỉ xác định Φ(t) một cách không nhập nhằng trong khoảng [0, 2π), nhưng vẫn "
        "còn nhoè modulo 2π. Có thể giải quyết vấn đề thứ hai bằng cách thêm hai đầu ra nữa có dạng:"))
    b.append(eq("I₃(t) = (I<sub>o</sub>(t)/2) · [1 − cos Φ(t)]", "6.79"))
    b.append(eq("I₄(t) = (I<sub>o</sub>(t)/2) · [1 − sin Φ(t)]", "6.80"))
    b.append(p(
        "Kết hợp các phương trình 6.76 tới 6.79 và 6.78 tới 6.80, có thể thu được một điểm qua không tại điểm uốn "
        "tuyến tính nhất và nhạy nhất của vân, nơi ảnh hưởng của biến thiên cường độ lên phép đo pha là nhỏ nhất. "
        "Bố trí trên Hình 6-51 cố gắng thu bốn đầu ra ấy. Tín hiệu A biểu diễn biến thiên cường độ như phương trình "
        "6.76, còn tín hiệu B do bản chất của tác dụng chia chùm bị dịch 180° so với A (phương trình 6.79). Có một "
        "nhánh khác ở bên phải bộ tách chùm không phân cực, gồm bộ tách chùm phân cực II quay 45° so với bộ tách "
        "chùm I, sao cho các bộ tách sóng C và D gắn theo đó tạo ra các tín hiệu xác định bởi phương trình 6.78 và "
        "6.80."))
    b.append(p(
        "Vì tần số Doppler phụ thuộc thời gian theo vận tốc v của gương đo, quãng đường x mà gương đã đi được tính "
        "tới thời điểm T cho bởi phương trình 6.81:"))
    b.append(eq("x = ∫₀<sup>T</sup> v dt = (λ<sub>A</sub>/2) ∫₀<sup>T</sup> f<sub>D</sub> dt = "
                "(λ<sub>A</sub>/4π) ∫₀<sup>T</sup> (∂Φ/∂t) dt", "6.81"))
    b.append(p(
        "Cần lưu ý rằng độ phân giải của giao thoa kế này bị giới hạn ở λ<sub>A</sub>/4 nếu không dùng phần cứng đặc "
        "biệt để nội suy giữa các vân giao thoa. Giao thoa kế này không bị giới hạn về tần số Doppler nhập nhằng cực "
        "đại."))

    b.append(h3("Xử lý tín hiệu giao thoa kế", "Interferometer signal processing"))
    b.append(p(
        "Đường quang của giao thoa kế kết thúc tại các bộ tách sóng quang. Vì các bộ tách sóng chỉ nhạy với giá trị "
        "cường độ ánh sáng, tín hiệu hình sin do gương chuyển động gây ra sẽ chồng lên một tín hiệu nền tỉ lệ với "
        "cường độ trung bình theo thời gian hoặc theo dịch chuyển. Phần điện tử gắn với các bộ tách sóng nhằm phát "
        "hiện một cách tin cậy các điểm qua không của thành phần hình sin trong các tín hiệu (A đến D) ngay cả trong "
        "điều kiện tương phản thấp, bằng cách trừ đi thành phần nền trong các bộ so sánh. Tương phản vân thấp có thể "
        "do gương nghiêng nhẹ và/hoặc rung trong thời gian gương chuyển động, do căn chỉnh giao thoa kế không lý "
        "tưởng, và do khuyết tật của các linh kiện quang như việc chia chùm không đều trong bộ tách chùm. Hình 6-52 "
        "trình bày một khối xử lý tín hiệu đơn giản."))
    b.append(fig(52, F.fig_6_52(), "vi"))
    b.append(p(
        "Mục đích chính của bố trí ấy là tạo ra các tín hiệu số vuông pha (E và F trên Hình 6-52) sao cho có thể dễ "
        "dàng dùng để nội suy tín hiệu bằng kỹ thuật số [20, 21], đồng thời cho phép xác định chiều chuyển động bằng "
        "cách, ví dụ, dùng tín hiệu E làm tín hiệu đếm và F làm chỉ báo lên/xuống."))
    b.append(p(
        "Hai bộ so sánh so sánh các thành phần hình sin có nền một chiều có thể biến thiên chậm, đã được các bộ "
        "khuếch đại đệm khuếch đại. Mọi tín hiệu A đến D của bộ tách sóng đều chịu ảnh hưởng của nền một chiều này, "
        "nên việc lấy hiệu của chúng trong bộ so sánh sẽ cho ra các tín hiệu qua không độc lập với nền. Cần hai khối "
        "so sánh để tạo các tín hiệu vuông pha cho việc phát hiện chiều. Hơn nữa, phần điện tử này cho phép dễ dàng "
        "nội suy vân theo hệ số 4, đưa độ phân giải chia nhỏ nhất của giao thoa kế xuống còn ≈ 160 nm. Có thể thực "
        "hiện nội suy này nếu thay vì đưa tín hiệu E vào lối vào đếm, ta dùng tín hiệu đã XOR là E⊕F. Khi ấy đầu lên/"
        "xuống của mạch đếm cần được nối với tín hiệu E&amp;F. Nếu muốn độ phân giải cao hơn nữa, có thể thực hiện "
        "nội suy số các tín hiệu vuông pha ấy [20–22]."))

    b.append(h2("Kết luận", "Conclusions"))
    b.append(p(
        "Dùng giao thoa kế laser làm việc với nguồn laser ổn định cao, có thể đạt bất định tương đối trong phép đo "
        "chiều dài thấp tới 5 × 10⁻⁸, khiến loại thiết bị này phù hợp để truyền các chuẩn chiều dài sơ cấp và thứ "
        "cấp vào các phòng đo công nghiệp. Vì trong thực tiễn các giao thoa kế này phải làm việc trong không khí "
        "xung quanh, bất định của chiết suất không khí là yếu tố đơn lẻ lớn nhất giới hạn độ chính xác tổng thể. "
        "Muốn giảm bất định từ nguồn ấy, phải xác định các tham số môi trường như độ ẩm tương đối, nhiệt độ dọc "
        "đường quang và áp suất khí quyển với sai số rất nhỏ. Ngược lại, các khúc xạ kế laser có khả năng xác định "
        "trực tiếp chiết suất không khí cho phép đo và bù trực tiếp chiết suất."))
    b.append(p(
        "Nguồn laser ổn định bằng hiệu ứng Zeeman có thể đạt bất định tương đối dưới 10⁻⁸, do đó chỉ đóng góp một "
        "phần nhỏ vào sai số tổng thể. Bản thân giao thoa kế, tuỳ thuộc phần xử lý tín hiệu đi kèm, sẽ có độ phân "
        "giải chia nhỏ nhất ít nhất là λ<sub>A</sub>/4 khi không có nội suy quang hoặc điện tử, và có thể có bất định "
        "nhỏ hơn một bậc nếu dùng các pha kế hiệu năng cao để chia nhỏ bước sóng λ<sub>A</sub>. Cần những ổ khí chất "
        "lượng rất cao và một môi trường đo được kiểm soát rất tốt mới đạt được những mục tiêu ấy."))

    # ---------------------------------------------------------------- glossary
    b.append(h2("Định nghĩa các thuật ngữ", "Defining terms"))
    b.append('<dl class="glossary">')
    for term, body in [
        ("Kỹ thuật dị tần",
         "Việc chồng hai tín hiệu điều hoà tần số f₁ và f₂ trong một linh kiện phi tuyến cho ra một tín hiệu chứa "
         "cả tần số tổng lẫn tần số hiệu. Với mục đích giao thoa, khi mỗi tần số riêng nằm trong dải 10¹⁴ Hz, hiệu "
         "tần số có thể đủ thấp để các bộ tách sóng quang ghi nhận. Các bộ tách sóng ấy cũng đóng vai trò linh kiện "
         "phi tuyến vì đáp ứng của chúng chỉ theo cường độ ánh sáng — đại lượng tỉ lệ với bình phương biên độ."),
        ("Giao thoa",
         "Hiện tượng minh hoạ sinh động bản chất sóng của ánh sáng. Nó xảy ra khi bức xạ đi theo nhiều hơn một "
         "đường từ nguồn tới điểm phát hiện. Có thể mô tả nó như những sai lệch cục bộ của cường độ tổng hợp so với "
         "định luật cộng, khi điểm phát hiện được dịch chuyển, vì cường độ dao động quanh tổng các cường độ riêng."),
        ("Laser",
         "Từ viết tắt của Light Amplification by Stimulated Emission of Radiation (khuếch đại ánh sáng bằng phát xạ "
         "cảm ứng). Ban đầu dùng để mô tả việc khuếch đại ánh sáng, nhưng gần đây mang nghĩa một bộ dao động quang."),
        ("Chiết suất",
         "Một số đặc trưng cho tỉ số giữa tốc độ lan truyền ánh sáng trong chân không c và tốc độ ấy trong một môi "
         "trường. Chiết suất của mọi môi trường luôn lớn hơn 1 một chút. Giá trị của nó phụ thuộc thành phần môi "
         "trường và bước sóng của bức xạ tới."),
        ("Hiệu ứng Zeeman",
         "Hiệu ứng quan sát được khi các nguyên tử bị kích thích phát bức xạ trong một từ trường. Hiệu ứng Zeeman "
         "dọc làm một vạch phát xạ đơn tách đối xứng thành hai vạch phân cực tròn phải và trái."),
    ]:
        b.append("<dt>%s</dt><dd>%s</dd>" % (term, body))
    b.append("</dl>")

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "“Documents concerning the new definition of the metre,” <i>Metrologia</i>, 19, 163–177, 1984.",
        "E. Jaatinen and N. Brown, “A simple external iodine stabilizer applied to 633 nm, 612 nm and 543 nm He–Ne "
        "lasers,” <i>Metrologia</i>, 32, 95–101, 1995.",
        "A. E. Siegman, <i>Lasers</i>, Mill Valley, CA: University Science Books, 1986.",
        "W. R. Steel, <i>Interferometry</i>, 2nd ed. (Cambridge studies in modern optics), Cambridge, U.K.: "
        "Cambridge University Press, 1985.",
        "W. R. C. Rowley, “The performance of a longitudinal Zeeman-stabilized He–Ne laser (633 nm) with thermal "
        "modulation and control,” <i>Meas. Sci. Technol.</i>, 1, 348–351, 1990.",
        "Wolfgang Demtröder, <i>Laser Spectroscopy: Basic Concepts and Instrumentation</i>, 2nd ed., Berlin: "
        "Springer, 1996.",
        "B. Edlén, “The dispersion of standard air,” <i>J. Opt. Soc. Amer.</i>, 43(5), 339–344, 1953.",
        "B. Edlén, “The refractive index of air,” <i>Metrologia</i>, 2(2), 71–80, 1966.",
        "J. C. Owens, “Optical refractive index of air: dependence on pressure, temperature and composition,” "
        "<i>Appl. Optics</i>, 6(1), 51–59, 1967.",
        "H. D. Baehr, <i>Thermodynamik</i>, 6th ed., Berlin: Springer, 1988.",
        "R. Revelle, “Carbon dioxide and world climate,” <i>Sci. Amer.</i>, 247(2), 35, 1982.",
        "K. P. Birch, F. Reinboth, R. W. Ward, and G. Wilkening, “Evaluation of the effect of variations in the "
        "refractive index of air upon the uncertainty of industrial length measurement,” <i>Metrologia</i>, 30(1), "
        "7–14, 1993.",
        "K. P. Birch and M. J. Downs, “An updated Edlén equation for the refractive index of air,” "
        "<i>Metrologia</i>, 30, 155–162, 1993.",
        "K. P. Birch and M. J. Downs, “Corrections to the updated Edlén equation for the refractive index of air,” "
        "<i>Metrologia</i>, 31, 315–316, 1994.",
        "P. E. Ciddor, “Refractive index of air: new equations for the visible and near infrared,” "
        "<i>Appl. Optics</i>, 35(9), 1566–1573, 1996.",
        "F. E. Jones, “The refractivity of air,” <i>J. National Bureau of Standards</i>, 86(1), 27–32, 1981.",
        "W. T. Estler, “High-accuracy displacement interferometry in air,” <i>J. Appl. Optics</i>, 24(6), 808–815, "
        "1985.",
        "J. A. Smith, U. W. Rathe, and C. P. Burger, “Lasers with optical feedback as displacement sensors,” "
        "<i>Opt. Eng.</i>, 34(9), 2802–2810, 1995.",
        "N. Takahashi, S. Kakuma, and R. Ohaba, “Active heterodyne interferometric displacement measurement using "
        "optical feedback effects of laser diodes,” <i>Opt. Eng.</i>, 35, 802–907, 1996.",
        "K. Oka, M. Tsukada, and Y. Ohtsuka, “Real-time phase demodulator for optical heterodyne detection "
        "processes,” <i>Meas. Sci. Technol.</i>, 2, 106–110, 1991.",
        "J. Waller, X. H. Shi, N. C. Altoveros, J. Howard, B. D. Blackwell, and G. B. Warr, “Digital interface for "
        "quadrature demodulation of interferometer signals,” <i>Rev. Sci. Instrum.</i>, 66, 1171–1174, 1995.",
        "J. A. Smith and C. P. Burger, “Digital phase demodulation in heterodyne sensors,” <i>Opt. Eng.</i>, 34, "
        "2793–2801, 1995.",
    ]))

    b.append(h2("Phụ lục mục 6.5 — Nhà sản xuất", "Appendix to Section 6.5 — Manufacturers"))
    b.append(p(
        "Dưới đây liệt kê một số hãng chế tạo hệ giao thoa kế hoàn chỉnh hoặc các thành phần chính của chúng như bộ "
        "tách chùm, gương hồi quang, khúc xạ kế, máy đo bước sóng… Danh sách này hoàn toàn không đầy đủ. Ngoài ra "
        "không nêu thông tin giá vì giá thành hệ thống phụ thuộc quá nhiều vào việc chọn linh kiện cụ thể."))
    b.append(table(
        ["Hãng", "Linh kiện", "Hệ hoàn chỉnh"],
        [
            ["Aerotech Inc., 101 Zeta Drive, Pittsburgh, PA 15238 · Tel: (412) 963-7470", "✓", "✓"],
            ["Burleigh Inc., Burleigh Park, Fishers, NY 14453-0755 · Tel: (716) 924-9355", "—", "✓"],
            ["Hewlett-Packard Inc., Test &amp; Measurement, Englewood, CO 80155-4026 · Tel: (800) 829-4444", "✓", "—"],
            ["Melles Griot Inc., 4665 Nautilus Court South, Boulder, CO 80301 · Tel: (303) 581-0337", "✓", "✓"],
            ["Oriel Instruments Inc., 250 Long Beach Blvd., Stratford, CT 06497-0872 · Tel: (203) 380-4364", "—", "✓"],
            ["Polytec PI Inc., Auburn, MA 01501 · Tel: (508) 832-3456", "✓", "✓"],
            ["Spindler &amp; Hoyer Inc., 459 Fortune Blvd., Milford, MA 01757-1745 · Tel: (508) 478-6200", "✓", "✓"],
            ["Zygo Corporation, Middlefield, CT 06455-0448 · Tel: (860) 347-8506", "✓", "✓"],
        ],
        caption="Danh sách nguyên văn theo bản gốc năm 1999; thông tin liên hệ có thể đã thay đổi."))
    b.append(nav(5, "vi"))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Section 6.5 is the precision-metrology entry, and its argument is narrower than it first looks. A laser "
        "interferometer does not measure length; it counts wavelengths. Everything that follows — the laser, the "
        "stabilisation, the refractometer, the fringe logic — exists because the wavelength in air is not quite "
        "the wavelength in vacuum, and the difference is larger than the precision the instrument is trying to "
        "deliver."))
    b.append(p(
        "The numbers set the scale of the problem. Since 1983 the metre is fixed by c = 299,792,458 m/s exactly, "
        "so the vacuum wavelength is as good as the laser’s frequency stability. A Zeeman-stabilised He–Ne reaches "
        "2 × 10⁻⁸; an iodine-stabilised one reaches 10⁻⁹. But the refractive index of ambient air is only known to "
        "about 5 × 10⁻⁸, and that single term dominates the error budget of any interferometer working in air."))

    b.append(h2("The laser", "Laser"))
    b.append(fig(46, F.fig_6_46(), "en"))
    b.append(fig(47, F.fig_6_47(), "en"))
    b.append(p(
        "The He–Ne discharge is a textbook energy-transfer chain: electrons excite helium into two long-lived "
        "metastable states; those states lie close enough to excited levels of neon that collisions transfer the "
        "energy almost exactly; the neon then emits by stimulated emission. Helium contributes no light at all — "
        "it is there only to pump. The cavity condition L = mλ/2 selects which wavelengths can oscillate, and "
        "because the gain envelope is gigahertz wide, several longitudinal modes usually oscillate at once. Those "
        "modes beat against each other, and the beat destroys the temporal coherence an interferometer needs."))

    b.append(h2("Two ways to stabilise", "Hai cách ổn định"))
    b.append(fig(48, F.fig_6_48(), "en"))
    b.append(p(
        "The Zeeman method is elegant because the error signal is the thing being measured. A longitudinal "
        "magnetic field splits the single oscillating mode into right- and left-circular components about 1.5 MHz "
        "apart, and that splitting peaks exactly when the laser frequency sits on the atomic transition. Lock the "
        "cavity length so the splitting stays at its maximum and the frequency is pinned. The cavity is adjusted "
        "two ways: a heater for the slow, large excursions, and a piezoelectric actuator for the fast, "
        "sub-wavelength corrections."))
    b.append(p(
        "The iodine method is better by an order of magnitude and much harder. A ¹²⁷I₂ absorption line at "
        "632.9913981 nm sits close enough to the He–Ne line to lock onto, and the resulting relative uncertainty "
        "is ±10⁻⁹. It is used only where that last order of magnitude matters."))

    b.append(h2("The refractive index is the real limit",
                "Chiết suất mới là giới hạn thật"))
    b.append(p(
        "Table 6.10 is the most useful table in the section, because it converts a tolerance into an operating "
        "procedure. To hold ∆n/n at 10⁻⁷ you need pressure to 37 Pa, temperature to 0.1 °C, humidity to 10 % RH, "
        "and CO₂ to 670 ppm. Those are achievable in a good laboratory and not achievable on a shop floor, which "
        "is precisely why laser refractometers — instruments that measure n directly rather than inferring it "
        "from four other sensors — matter."))
    b.append(table(
        ["Gas", "(n − 1)·10⁴", "Concentration for ∆n/n = 10⁻⁷ (ppm)", "MWC (mg·m⁻³)", "∆n/n × 10⁷ at MWC"],
        [
            ["Air", "2.72", "—", "—", "—"],
            ["Propane", "10.3", "130", "1800", "8"],
            ["Butane", "12.9", "98", "2350", "10"],
            ["Ethanol", "8.1", "190", "1900", "5"],
            ["Ethyl acetate", "13.0", "97", "1400", "4"],
            ["Dimethylketone", "10.2", "130", "2400", "9"],
            ["Octane", "23", "50", "2350", "10"],
            ["CFC, e.g. R12", "10.3", "130", "5000", "7"],
        ],
        caption="Table 6.9 — Refractive indices of various gases, their maximum workplace concentration (MWC) and "
                "the resulting index change (T = 20 °C, P = 101.315 hPa, λ = 633 nm)."))
    b.append(note(
        "A detail worth noticing: the CO₂ term. Dry air is 0.035 % CO₂, the concentration is rising about 1.4 ppm "
        "per year, and an industrial site can vary it locally by far more than that. Edlén’s 1966 formula assumed "
        "a fixed value; the Birch–Downs and Ciddor updates do not. For work at the 10⁻⁸ level, which formula you "
        "use is itself a decision with metrological consequences."))

    b.append(h2("Three interferometers", "Ba kiểu giao thoa kế"))
    b.append(fig(49, F.fig_6_49(), "en"))
    b.append(p(
        "The Michelson of 6.49 is the reference design and also the one with the obvious flaw: the returning "
        "beams re-enter the laser and form an external cavity that detunes it. Commercial instruments fix this "
        "with corner-cube retroreflectors and optical isolators. The retroreflector has a second virtue — it "
        "returns the beam parallel to itself regardless of small tilts, which is what keeps the fringe contrast "
        "up when the carriage moves."))
    b.append(fig(50, F.fig_6_50(), "en"))
    b.append(p(
        "The heterodyne version of 6.50 turns the measurement into a frequency comparison. Two modes f₁ and f₂ "
        "are separated by polarisation, one sent to the measuring arm and one to the reference arm, and the "
        "detector sees f₂ − f₁ − f_D. Because the carrier is 1.5 MHz rather than dc, the electronics can tell "
        "forward from backward directly from the sign of the count — no quadrature gymnastics required. The price "
        "is equation 6.75: the Doppler shift must stay below the mode spacing, which caps the closing velocity at "
        "0.474 m/s. Moving away has no such limit."))
    b.append(fig(51, F.fig_6_51(), "en"))
    b.append(p(
        "The homodyne version of 6.51 gives up the frequency offset and gets back the velocity range. It pays for "
        "that with the signal-processing problem the rest of the section is about: a single output I(t) ∝ 1 + "
        "cos Φ(t) cannot tell +Φ from −Φ, and its amplitude drifts as the laser ages. Equations 6.78–6.80 answer "
        "both objections by generating sin Φ, −cos Φ and −sin Φ alongside cos Φ. Four signals, four detectors, "
        "and the phase becomes unambiguous over a full 2π and immune to intensity drift at the zero crossing."))

    b.append(h2("Where the resolution actually comes from",
                "Độ phân giải đến từ đâu"))
    b.append(fig(52, F.fig_6_52(), "en"))
    b.append(ul([
        "<b>λ/2</b> — counting fringes, one count per half wavelength of mirror travel. The basic Michelson.",
        "<b>λ/4</b> — quadrature detection with direction sensing, the homodyne instrument as built.",
        "<b>λ/512</b> — electronic phase interpolation of the sinusoidal intensity, the best quoted for a "
        "Michelson with sophisticated processing.",
        "<b>≈160 nm</b> — the ×4 interpolation of the conditioning circuit in Figure 6.52, which is what a "
        "practical counter does before any digital subdivision.",
    ]))
    b.append(p(
        "The last line of the section is the one to remember: none of these numbers mean anything without air "
        "bearings and a controlled environment. A fringe counter that resolves 160 nm is worthless if the air "
        "along the beam changes temperature by 0.1 °C between measurements, because that alone moves the answer "
        "by 10⁻⁷ of the path length."))
    b.append(nav(5, "en"))
    return "".join(b)
