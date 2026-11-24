# -*- coding: utf-8 -*-
"""Book 7, Chapter 5, Section C — Small Flow / Metric Units / What Size Valve
(EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), PDF pp. 47-53,
printed pp. 40-46. Covers the small-flow Reynolds/FR method (equations
5-14 through 5-17), the revised FR explanation, metric units (5-18), the
valve-size choice, Table 5-5, the 8 chapter references and the additional
reading. Equations 5-1 through 5-13 belong to sections A and B.
"""
from cvp_common import eq, h2, h3, h4, ol, p, refs, table, ul

PAGES_SRC = 7
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Valve Sizing Made Easy"
TITLE_VI = "Định cỡ van dễ dàng"

def body_vi():
    b = []
    b.append(h2("Định cỡ van lưu lượng nhỏ", "Small Flow Valve Sizing"))
    b.append(p("Đối với van lưu lượng nhỏ (C<sub>v</sub> ≤ 0.1), F<sub>L</sub> ≈ 1.0, "
               "chúng ta tính số Reynolds của van Re<sub>v</sub> như trước, nhưng dùng các "
               "hệ số F<sub>d</sub> khác,<sup>10</sup> cụ thể là:"))
    b.append(ul([
        "0.7 cho nút van có rãnh then (splined plugs)",
        "0.3 cho van màng hành trình ngắn có bề mặt tựa phẳng",
        "F<sub>d</sub> = 0.09 √(C<sub>v</sub>)/(đường kính nút van), cho nút van "
        "hình nón có khe hở nhỏ",
    ]))
    b.append(p("Ví dụ: Với một nút van có khe hở nhỏ đường kính 1/8 inch và C<sub>v</sub> = "
               "0.05: F<sub>d</sub> = 0.09 √0.05/0.125 = 0.16."))
    b.append(p("Đối với chất lỏng:"))
    b.append(eq("Re<sub>v</sub> = 17300 F<sub>q</sub> q / "
                "[ν d (C<sub>vR</sub> F<sub>L</sub>/d<sup>2</sup>)<sup>0.5</sup>]", "5-14"))
    b.append(p("Đối với khí:"))
    b.append(eq("Re<sub>v</sub> = 2153 F<sub>q</sub> q / "
                "[ν d (C<sub>vR</sub> F<sub>L</sub>/d<sup>2</sup>)<sup>0.5</sup>]", "5-15"))
    b.append(p("trong đó q = lưu lượng tính bằng SCFH ở 14.7 psia và 60°F. Bây giờ hãy "
               "tính F<sub>R</sub>:"))
    b.append(eq("F<sub>R</sub> = (Re<sub>v</sub>/10000)<sup>1/n</sup> ≤ 1 (max.)", "5-16"))
    b.append(eq("n = 1 + K + log(Re<sub>v</sub>)", "5-17"))
    b.append(p("và vì K = 1 đối với van lưu lượng nhỏ, n = 2 + log(Re<sub>v</sub>). Ví dụ:"))
    b.append(p("Chất lưu: khí CO<sub>2</sub> ở 85°F (T = 545°R); P<sub>1</sub> = "
               "36.3 psia; P<sub>2</sub> = 24.7 psia; ν = độ nhớt động học = 8.65 cSt ở "
               "85°F và 14.7 psia (Lưu ý: dùng ν ở áp suất khí quyển nếu bạn dùng q "
               "tính bằng SCFH); G<sub>g</sub> = trọng lực riêng = 1.516; C<sub>v</sub> = hệ "
               "số định cỡ van rối (đã chọn) = 0.025; F<sub>L</sub> = hệ số phục hồi áp suất "
               "chất lỏng = 1 (theo catalog của nhà sản xuất); F<sub>d</sub> = hệ số điều "
               "chỉnh kiểu van = 0.16 (theo catalog của nhà sản xuất); q = lưu lượng lớn nhất "
               "mong muốn = 15 SCFH ở 85°F và 14.7 psia; T = 460 + 85 = 545°R."))
    b.append(p("Theo Phương trình 5-15, Re<sub>v</sub> = 2153(0.16)(15)/[8.65 "
               "√(0.025)] = 3778."))
    b.append(p("và theo Phương trình 5-16, n = 2 + log(3778) = 5.58, nên F<sub>R</sub> = "
               "(3778/10000)<sup>1/5.58</sup> = 0.84."))
    b.append(p("Bây giờ hãy xác định xem C<sub>v</sub> = 0.025 đã chọn có đủ để xử lý lưu "
               "lượng 15 SCFH hay không. Tính C<sub>v</sub> rối từ phương trình khí rối cho "
               "dòng dưới tới hạn<sup>5</sup> và hiệu chỉnh theo F<sub>R</sub>: C<sub>v</sub> "
               "= q √(G<sub>g</sub>T) F<sub>R</sub> √(P<sub>1</sub>/ΔP)/"
               "(963 P<sub>1</sub> Y). Với P<sub>1</sub> − P<sub>2</sub> = 11.6 psi, "
               "kết quả là C<sub>v</sub> = 0.0193."))
    b.append(p("C<sub>v</sub> = 0.025 của van đã chọn là đạt."))

    b.append(h3("Định cỡ van điều khiển cho chất lưu nhớt: một giải thích",
                "Sizing Control Valves for Viscous Fluids: An Explanation"))
    b.append(p("Tôi luôn tự hỏi làm thế nào một van bi gần như không có vật cản lại cho qua "
               "cùng một lượng hắc ín<sup>6</sup> với một sụt áp và hệ số lưu lượng "
               "(C<sub>v</sub>) nhất định như một van lồng, chẳng hạn van lồng có 100 lỗ "
               "khoan nhỏ, dù van lồng có cùng C<sub>v</sub> với van bi. Trực giác mách bảo "
               "điều đó không thể đúng, dù tiêu chuẩn ISA trước đó nói như vậy. Không tin "
               "vào điều đó, tôi quyết định tìm hiểu và đã đưa ra phương pháp hiệu chỉnh "
               "trình bày trong mục này."))
    b.append(p("<sup>6</sup> Bỏ qua hệ số F<sub>L</sub>, vốn ảnh hưởng đến số Reynolds."))
    b.append(p("Các giá trị F<sub>R</sub> cho van lưu lượng nhỏ suy ra từ các phương trình mới "
               "của tôi không khớp với các giá trị cho trong Hình 1 của ISA-75.01.01 cũ, "
               "<i>Flow Equations for Sizing Control Valves</i> (nay đã sửa đổi), và chúng "
               "cho kết quả chính xác hơn — thường làm tăng C<sub>v</sub> cần thiết cho van "
               "lưu lượng nhỏ lên gấp bốn hoặc hơn so với phương pháp hiện hành ở số "
               "Reynolds dưới 100.<sup>5</sup> Đường cong F<sub>R</sub> đơn của ISA trước đây "
               "dựa trên số lượng thử nghiệm hạn chế với van cầu cỡ đầy đủ, trong khi các giá "
               "trị mới dựa trên các thử nghiệm với không khí và nước trên van lưu lượng nhỏ "
               "hoặc các kiểu van quay, bổ sung cho van cầu."))
    b.append(p("<sup>5</sup> Hãy nhớ rằng không có vận tốc âm thanh nếu dòng chảy không phải "
               "rối; do đó, các phương trình dòng chảy tới hạn không áp dụng được."))
    b.append(p("Từ dữ liệu công bố trong <i>Perry's Chemical Engineers Handbook</i>, ấn bản "
               "thứ sáu, Bảng 5-15, có vẻ như các van có đường dòng êm hơn (ví dụ van góc và "
               "van cổng) có hệ số F<sub>R</sub> gần với các đường cong Hình 5-2, trong khi "
               "van cầu kiểu đĩa và kiểu nút (do kiểu dòng chảy đột ngột hơn) có xu hướng "
               "nghiêng về các giá trị F<sub>R</sub> của ISA trước đây khi được hiệu chỉnh "
               "bằng các giá trị F<sub>d</sub> phù hợp."))
    b.append(p("Từ dữ liệu này, có vẻ như “C<sub>v</sub> giả”, tức “C<sub>v</sub> dòng tầng”, "
               "hay C<sub>v</sub>F<sub>R</sub>F<sub>L</sub>, là như nhau cho mọi kiểu van có "
               "trim cỡ đầy đủ và ở số Reynolds thấp (Re<sub>v</sub> &lt; 100)."))
    b.append(p("Từ đó, C<sub>v</sub> cần thiết (năng lực van cần để cho dòng nhớt qua ở một số "
               "Reynolds nhất định) là C<sub>v</sub> = q R<sub>e</sub>/(0.026 K A<sub>p</sub>), "
               "trong đó 0.026 là diện tích tính bằng inch vuông trên mỗi 1 C<sub>v</sub> khi "
               "hệ số tổn thất cột áp K = 1. A<sub>p</sub> là diện tích mặt cắt ngang của cỡ "
               "ống đã cho tính bằng inch vuông (cùng với cỡ van!)."))
    b.append(ul([
        "K = hệ số tổn thất cột áp tốc độ của trim van, với K = (38 × "
        "A/C<sub>v</sub>)<sup>2</sup>",
        "A = diện tích dòng chảy của trim tính bằng in<sup>2</sup>",
    ]))
    b.append(p("Hơn nữa, theo phương trình ISA, C<sub>v,Req</sub> = C<sub>i</sub>/F<sub>R</sub>, "
               "trong đó C<sub>i</sub> là C<sub>v</sub> tính với giả thiết kiểu dòng chảy "
               "hoàn toàn rối; từ đó C<sub>v</sub> = R<sub>e</sub>/(A<sub>p</sub>F<sub>L</sub>). "
               "Vì số Reynolds của van đối với chất lỏng là R<sub>e</sub> = 17300 F<sub>q</sub> "
               "q/[ν d (C<sub>vR</sub>F<sub>L</sub>/d<sup>2</sup>)<sup>0.5</sup>], phương "
               "trình đã gắn nhãn (5-13) ở trên cho C<sub>v,req</sub> = 0.194 q "
               "(G<sub>f</sub>/ΔP)<sup>0.5</sup> [ν/(F<sub>L</sub><sup>2</sup>"
               "F<sub>d</sub> K d<sup>2</sup>)]<sup>2/3</sup>."))
    b.append(p("Vì F<sub>L</sub> xấp xỉ tỷ lệ với năng lực tương đối của van "
               "(C<sub>v</sub>/d<sup>2</sup>), ta có thể — chỉ để ước tính — thay F<sub>L</sub> "
               "≅ 0.96[1 − 0.0025(C<sub>v</sub>/d<sup>2</sup>)]<sup>2/15</sup> "
               "trong Phương trình 5-13."))
    b.append(p("Hơn nữa, F<sub>d</sub> có liên hệ nhất định với F<sub>L</sub> (ví dụ, một van "
               "lớn như van bi có F<sub>L</sub> thấp nhưng F<sub>d</sub> cao). Vì vậy ta có "
               "thể ước tính tiếp rằng F<sub>L</sub> = F<sub>d</sub> = 0.4/0.89 = 0.42 và, "
               "cuối cùng, là √K/d."))
    b.append(p("Khi đó Phương trình 5-13 trở thành: C<sub>v</sub> = 0.00386 q "
               "√(G<sub>f</sub>/ΔP) [0.96 − 0.0025(C<sub>v</sub>/d<sup>2"
               "</sup>)]<sup>2/15</sup> (ΔP/d<sup>4</sup>)<sup>2/3</sup>."))
    b.append(p("Lưu ý: C<sub>v</sub> đã chọn không được nhỏ hơn 10 d<sup>2</sup> và không được "
               "lớn hơn 30 d<sup>2</sup>."))
    b.append(p("Tôi gợi ý bạn nhập cỡ ống của khách hàng cho d. Phương trình trên sẽ cho bạn "
               "một con số C<sub>v</sub> ước tính sơ bộ, giúp ích trong việc chọn kiểu van. "
               "Dùng các hệ số thực của van (C<sub>v</sub> định mức, F<sub>L</sub> và "
               "F<sub>d</sub>), hãy tính lại C<sub>v</sub> cần thiết theo Phương trình 5-9."))

    b.append(h2("Đơn vị mét", "Metric Units"))
    b.append(p("Việc phần còn lại của thế giới dùng đơn vị mét có thể không làm bạn bận tâm. "
               "Tuy nhiên, có thể có lúc bạn phải làm một dự án cho một nhà máy ở nước ngoài, "
               "và bạn sẽ đối mặt với lưu lượng chất lỏng tính bằng mét khối trên giờ thay vì "
               "gpm. May thay, các số C<sub>v</sub> vẫn dùng được như vậy ở châu Âu. Ví dụ:"))
    b.append(eq("C<sub>v</sub> = 1.17 q √(G<sub>f</sub>/ΔP)", "5-18"))
    b.append(ul([
        "q = m<sup>3</sup>/h chất lỏng",
        "ΔP = sụt áp qua van tính bằng bar",
        "G<sub>f</sub> = trọng lực riêng (nước ở 60°F = 1)",
    ]))
    b.append(p("Ở Đức, người ta đi xa đến mức bỏ hẳn hằng số 1.17 và gọi hệ số lưu lượng là "
               "K<sub>v</sub>; do đó K<sub>v</sub> = 0.85 C<sub>v</sub>, hay C<sub>v</sub> = "
               "1.17 K<sub>v</sub>."))
    b.append(p("Chỉ phát sinh phức tạp khi bạn gặp đơn vị newton trên mét vuông, còn gọi là "
               "pascal hay Pa. Để trở về đơn vị bar quen thuộc hơn, hãy chia Pa cho 100.000, "
               "tức một bar = 100.000 Pa, và một bar = 14.5 psi. Một kilopascal (kPa) = 0.145 "
               "psi. Cũng có đơn vị ít dùng hơn là kg/cm<sup>2</sup>, bằng 0.98 bar hay 14.2 "
               "psi."))
    b.append(p("Cũng hãy nhớ rằng ở nước ngoài người ta dùng độ Celsius, với °F = "
               "(°C × 9/5) + 32, và theo giá trị tuyệt đối, °K = 273 + °C. "
               "Đổi các đơn vị lưu lượng:"))
    b.append(ul([
        "1 m<sup>3</sup>/h chất lỏng = 4.4 gpm",
        "1 m<sup>3</sup>/h khí = 35.3 ft<sup>3</sup>/h",
        "kg/h = 2.2 lb/h",
    ]))
    b.append(p("Giờ bạn đã được trang bị đầy đủ để làm việc ở nước ngoài."))

    b.append(h2("Chọn cỡ van nào", "What Size Valve to Choose"))
    b.append(p("Sau khi bạn đã vất vả chọn C<sub>v</sub> cuối cùng của van phù hợp với yêu cầu "
               "lưu lượng lớn nhất, và đã xem xét các hệ số F (F<sub>L</sub>, F<sub>p</sub>, "
               "F<sub>R</sub>), giờ bạn đối mặt với lựa chọn cuối cùng — cỡ van."))
    b.append(p("Nếu sụt áp thấp, chẳng hạn 5 đến 15 psi, luôn an toàn khi bắt đầu với van có "
               "cỡ bằng cỡ đường ống. Hãy nhớ rằng người trong bộ phận thiết kế đường ống đã "
               "chọn cỡ ống hạ lưu hoặc thượng lưu để cho dòng thiết kế chảy với vận tốc hợp "
               "lý. Nhân tiện, vận tốc tại đầu ra van không nên làm bạn bận tâm, trừ khi có "
               "thể phát sinh vấn đề tiếng ồn khi giảm áp khí hoặc hơi áp suất cao (Chương "
               "20, “Methods of Aerodynamic Valve Noise Reduction,” thảo luận về tiếng ồn "
               "khí động), hoặc khi có chất lỏng hóa hơi (nếu ống hạ lưu quá dài, van của "
               "bạn sẽ bị xâm thực do áp suất hạ lưu tăng lên vì vận tốc hỗn hợp hai pha "
               "cao). Như vậy chỉ còn lại cấp C<sub>v</sub> của van. Trong trường hợp bạn "
               "chưa chọn nhãn hiệu nào vì bạn thiên về màu của van — xanh hoặc đỏ — hãy xem "
               "Bảng 5-5 để gợi ý."))
    b.append(p("Các giá trị C<sub>v</sub> tính theo bình phương đường kính van (inch). Các "
               "giá trị C<sub>v</sub> trong ngoặc đơn tính theo bình phương đường kính ống "
               "(inch). Ví dụ, một van cắm quay lệch tâm 6 inch có hệ số lưu lượng "
               "C<sub>v</sub> khi mở hoàn toàn là 6<sup>2</sup> × 12 = 432. Tuy nhiên, "
               "khi lắp giữa các đoạn thu nhỏ trong ống 12 inch, hệ số lưu lượng sẵn có chỉ "
               "là 6<sup>2</sup> × 11.3 = 407 (xem cột C<sub>v</sub>/d<sup>2</sup> với "
               "D/d = 2), hoặc 12<sup>2</sup> × 2.8 = 403 nếu dùng các số trong ngoặc "
               "đơn."))
    b.append(p("Các giá trị trên là bảo thủ và thay đổi đôi chút theo từng cỡ. Bạn có thể "
               "nhận thấy rằng khi các van công suất cao được dùng trong điều kiện dòng chảy "
               "nghẽn (chẳng hạn giảm áp hơi), tất cả chúng đều có xu hướng mất lợi thế "
               "C<sub>v</sub> cao, như bạn thấy ở cột C<sub>v</sub>F<sub>L</sub>/d<sup>2</sup>"
               "! Hãy giải thích điều này với nhà cung cấp van của bạn."))
    b.append(p("Bắt đầu với van có cỡ bằng cỡ ống, trước tiên hãy chia giá trị C<sub>v</sub> "
               "tối đa mong muốn. Cách này cho bạn hệ số an toàn 10% và phòng tránh sai số "
               "±10% trong cấp C<sub>v</sub> do nhà sản xuất công bố. Bây giờ hãy chia "
               "số C<sub>v</sub> mới này cho bình phương cỡ ống. Ví dụ, theo dữ liệu lưu "
               "lượng, bạn cần C<sub>v</sub> tối đa = 123. Cỡ ống của bạn là 4 in. Trước tiên "
               "chia 123 cho 0.8 được 154. Rồi chia số này cho (4 in)<sup>2</sup>. "
               "154/4<sup>2</sup> = 9.6 C<sub>v</sub>/d<sup>2</sup>."))
    b.append(p("Từ dữ liệu cho trong Bảng 5-4, bạn có các lựa chọn sau:"))
    b.append(ul([
        "Van cầu một đế 4 inch, C<sub>v</sub>/d<sup>2</sup> = 10; C<sub>v</sub> định mức = "
        "10 × 4<sup>2</sup> = 160.",
        "Van bướm mở 70° (nếu các yếu tố khác như rò rỉ, tiếng ồn v.v. cho phép). Ở đây, "
        "van bướm 3 inch lắp trong ống 4 inch có năng lực lưu lượng cao hơn 10.2 × "
        "D<sup>2</sup> (xem các số trong ngoặc đơn), tức hơn 4<sup>2</sup> × 10.2 = "
        "163 C<sub>v</sub>.",
    ]))
    b.append(p("Sau khi đã xác định cỡ (và kiểu) van, giờ bạn nên kiểm tra xem có đáp ứng được "
               "hệ số lưu lượng tối thiểu mà quá trình yêu cầu hay không. Hãy xem bảng "
               "C<sub>v</sub> của nhà sản xuất (thường in theo bước 10% hành trình) và tra "
               "hành trình gần đúng của van khi van vận hành ở C<sub>v</sub> tối thiểu của "
               "bạn. Hành trình này không được nhỏ hơn 5% tổng hành trình van, cũng như không "
               "nhỏ hơn phần trăm vùng chết của van (với đệm kín chặt). Thường là 5% với đệm "
               "kín tetrafluoroethylene (TFE), tới 15% với đệm kín graphite nhiều lớp nếu "
               "không dùng bộ định vị. Đối với van điển hình đệm TFE và không có bộ định vị, "
               "điều này giới hạn hành trình van ở 10% kể từ vị trí đóng kín. Ngoại lệ duy "
               "nhất là một số nút van có đế mềm “nhúng” qua"))
    b.append(table(
        ["Kiểu van", "C<sub>v</sub>/d<sup>2</sup>", "F<sub>L</sub>",
         "C<sub>v</sub>F<sub>L</sub>/d<sup>2</sup>",
         "C<sub>v</sub>F<sub>p</sub>/d<sup>2</sup><br>D/d = 1.5",
         "C<sub>v</sub>/d<sup>2</sup> với D/d = 2"],
        [
            "Van cầu một đế",
            ("Nút parabol, dòng chảy làm mở van", "10", "0.9", "9", "9.8 (4.3)", "9.6 (2.4)"),
            ("Van cầu hai đế", "12.5", "0.9", "11.3", "12 (5.3)", "11.7 (2.9)"),
            ("Van lồng công suất cao, chỉ đến cỡ 3 in", "14", "0.9", "12.5", "13.5 (6.0)", "12.9 (3.2)"),
            ("Van cắm quay lệch tâm", "12.0", "85", "10", "11.6 (5.1)", "11.3 (2.8)"),
            ("Van bướm mở 60°", "17", "0.68", "11.5", "15.8 (7.0)", "15 (3.8)"),
            ("Van bướm mở 70°", "27", "0.57", "15.5", "23 (10.2)", "20.8 (5.2)"),
            ("Van bướm có rãnh @ 70°", "25", "0.7", "17.5", "21.8 (9.7)", "19.8 (5.0)"),
            ("Van bi định hình @ 90°", "25", "0.6", "15", "21.8 (9.7)", "19.8 (5.0)"),
            ("Van góc kiểu venturi, dòng chảy làm đóng van", "22", "0.5", "11", "19.8 (8.8)", "18.3 (4.6)"),
            "D = inch",
        ],
        "Bảng 5-5. Hệ số lưu lượng điển hình tại hành trình định mức."))
    b.append(p("vòng làm kín của chúng, van bi, van bướm lót elastomer có cánh tựa góc, và một "
               "số van màng hoặc van kẹp không có tác dụng tựa “cứng”. Nếu một van tiêu "
               "chuẩn bắt bạn tiết lưu dưới 5% hành trình, lựa chọn duy nhất là dùng một van "
               "lớn và một van nhỏ song song, chia dải tín hiệu cơ cấu chấp hành, hoặc tốt "
               "hơn là dùng hai tín hiệu riêng từ máy tính của bạn để van nhỏ mở trước, rồi "
               "van lớn bắt đầu khi van nhỏ mở khoảng 80%."))
    b.append(p("Tóm lại:"))
    b.append(ul([
        "Chọn van có C<sub>v</sub> định mức lớn hơn ít nhất 20% so với yêu cầu lớn nhất của bạn.",
        "Đảm bảo C<sub>v</sub> tối thiểu cần thiết xuất hiện ở mức cao hơn ít nhất 5% hành "
        "trình van (kiểm tra catalog của nhà cung cấp).<sup>7</sup>",
    ]))
    b.append(p("<sup>7</sup> Bạn có thể phải dùng 10% nếu không biết C<sub>v</sub> ở hành "
               "trình 5%."))

    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(refs([
        "L. R. Driskell, “New Approach to Control Valve Sizing,” <i>Hydrocarbon "
        "Processing</i> (July 1969): 111–114.",
        "Bulletin No. SM-6, “Control Valve Sizing.” Portsmouth, NH: H. D. Baumann "
        "Assoc., Ltd., (1991).",
        "H. D. Baumann, “A Case for Butterfly Valves in Throttling Applications,” "
        "<i>Instruments and Control Systems</i> (May 1979): 35–38.",
        "H. D. Baumann, “Effect of Pipe Reducers on Control Valve Capacity,” "
        "<i>Instrument &amp; Control Systems</i> (December 1968): 99–102.",
        "E. B. McCutcheon, “A Reynolds Number for Control Valves,” in <i>Flow: "
        "Its Measurement and Control in Science and Industry</i>, Volume 1, "
        "Part 3, proceedings of the first symposium on Pittsburgh, "
        "Pennsylvania, on May 9 to 14, 1971, Instrument Society of America, 1974.",
        "H. D. Baumann, “A Unifying Method for Sizing Throttling Valves Under "
        "Laminar or Transitional Flow Conditions,” <i>Transactions of the "
        "ASME, Journal of Fluids Engineering</i> (March1993): 166–169.",
        "H. D. Baumann, “Viscosity Flow Correction for Small Control Valve "
        "Trim,” <i>Transactions of the ASME, Journal of Fluids Engineering</i> "
        "113 (March 1991): 86–89.",
        "ANSI/ISA-75.01.01-2012 (60534-2-1 MOD), Industrial-Process Control "
        "Valves – Part 1-1: Flow Capacity – Sizing Equations for Fluid Flow "
        "under Installed Conditions (Research Triangle Park, NC: ISA "
        "[International Society of Automation]).",
    ]))
    b.append(p("<b>Đọc thêm.</b> J. A. George, “Evolution and Status of Non-Turbulent Flow "
               "Sizing for Control Valves,” monograph, ISA 2001."))
    b.append(p("<b>Ghi chú về nguồn.</b> OCR làm méo các ký tự phương trình ở khắp nơi: "
               "(5-14) và (5-15) được viết theo ký hiệu chuẩn giống Phương trình 5-10; trong "
               "ví dụ CO<sub>2</sub>, giá trị 0.16 (F<sub>d</sub>) được thay vào vị trí mà "
               "phương trình in ghi F<sub>q</sub>, cho Re<sub>v</sub> ≈ 3778 (bản in ghi "
               "“377805”), n = 5.58 và F<sub>R</sub> = 0.84. Dòng tính C<sub>v</sub> khí kết "
               "thúc ở 0.0193 và các phương trình ẩn C<sub>v</sub> sau phần trích "
               "<i>Perry's Handbook</i> được biểu diễn dạng ký hiệu; các số mũ như 2/15 và 2/3 "
               "không chắc chắn trong bản quét. Một số nét đặc thù của bản in được giữ nguyên: "
               "F<sub>L</sub> = 0.4/0.89 = 0.42; “Bảng 5-4” trong khi dữ liệu lại là Bảng "
               "5-5; “March1993” ở tài liệu tham khảo 6; mã trích dẫn dấu mũ “10” sau các hệ "
               "số F<sub>d</sub>; và “85” (rõ ràng là 0.85) ở hàng van cắm quay lệch tâm "
               "trong Bảng 5-5. Phương trình 5-13 chỉ được nhắc trong lời văn; nó thuộc mục "
               "trước và không được đóng khung ở đây."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Định cỡ van lưu lượng nhỏ", "Small Flow Valve Sizing"))
    b.append(p("Now for small flow valves (C<sub>v</sub> ≤ 0.1) F<sub>L</sub> ≈ 1.0, "
               "we calculate the valve Reynolds number Re<sub>v</sub> as before, except we use "
               "different F<sub>d</sub> factors,<sup>10</sup> namely"))
    b.append(ul([
        "0.7 for splined plugs",
        "0.3 for short travel diaphragm valves with a flat seating surface",
        "F<sub>d</sub> = 0.09 √(C<sub>v</sub>)/(plug diameter), for close clearance "
        "tapered plugs",
    ]))
    b.append(p("Example: For a 1/8-inch-diameter close clearance plug with a C<sub>v</sub> = "
               "0.05: F<sub>d</sub> = 0.09 √0.05/0.125 = 0.16."))
    b.append(p("For liquids:"))
    b.append(eq("Re<sub>v</sub> = 17300 F<sub>q</sub> q / "
                "[ν d (C<sub>vR</sub> F<sub>L</sub>/d<sup>2</sup>)<sup>0.5</sup>]", "5-14"))
    b.append(p("For gases:"))
    b.append(eq("Re<sub>v</sub> = 2153 F<sub>q</sub> q / "
                "[ν d (C<sub>vR</sub> F<sub>L</sub>/d<sup>2</sup>)<sup>0.5</sup>]", "5-15"))
    b.append(p("where q = flow in SCFH at 14.7 psia and 60°F. Now calculate F<sub>R</sub>:"))
    b.append(eq("F<sub>R</sub> = (Re<sub>v</sub>/10000)<sup>1/n</sup> ≤ 1 (max.)", "5-16"))
    b.append(eq("n = 1 + K + log(Re<sub>v</sub>)", "5-17"))
    b.append(p("and because K for small flow valves = 1, n = 2 + log(Re<sub>v</sub>). For "
               "example:"))
    b.append(p("Fluid: CO<sub>2</sub> gas at 85°F (T = 545°R); P<sub>1</sub> = "
               "36.3 psia; P<sub>2</sub> = 24.7 psia; ν = kinematic viscosity = 8.65 cSt "
               "at 85°F and 14.7 psia (Note: use ν at atmospheric pressure if you use "
               "q in SCFH); G<sub>g</sub> = specific gravity = 1.516; C<sub>v</sub> = "
               "turbulent valve sizing coefficient (selected) = 0.025; F<sub>L</sub> = "
               "liquid pressure recovery factor = 1 (from manufacturer's catalog); "
               "F<sub>d</sub> = valve style modifier = 0.16 (from manufacturer's catalog); "
               "q = desired maximum flow rate = 15 SCFH at 85°F and 14.7 psi absolute; "
               "T = 460 + 85 = 545°R."))
    b.append(p("From Equation 5-15, Re<sub>v</sub> = 2153(0.16)(15)/[8.65 "
               "√(0.025)] = 3778."))
    b.append(p("and from Equation 5-16, n = 2 + log(3778) = 5.58, so F<sub>R</sub> = "
               "(3778/10000)<sup>1/5.58</sup> = 0.84."))
    b.append(p("Now, determine if the selected valve C<sub>v</sub> of 0.025 is sufficient to "
               "handle the flow of 15 SCFH. Measure turbulent C<sub>v</sub> from the "
               "turbulent gas equation for subcritical flow<sup>5</sup> and modified by "
               "F<sub>R</sub>: C<sub>v</sub> = q √(G<sub>g</sub>T) F<sub>R</sub> "
               "√(P<sub>1</sub>/ΔP)/(963 P<sub>1</sub> Y). With P<sub>1</sub> "
               "− P<sub>2</sub> = 11.6 psi, this gives C<sub>v</sub> = 0.0193."))
    b.append(p("The selected valve C<sub>v</sub> of 0.025 is OK."))

    b.append(h3("Định cỡ van điều khiển cho chất lưu nhớt: một giải thích",
                "Sizing Control Valves for Viscous Fluids: An Explanation"))
    b.append(p("I always wondered how a ball valve with hardly any obstruction can pass the "
               "same amount of tar<sup>6</sup> for a given pressure drop and flow coefficient "
               "(C<sub>v</sub>) as a cage valve with, for example, 100 small, drilled holes "
               "even though it has the same C<sub>v</sub> as the ball valve. Instinct tells "
               "us this could not be so despite the fact the previous ISA standard told us "
               "so. Not believing it, I decided to do something about it and came up with "
               "the revised method presented in this section."))
    b.append(p("<sup>6</sup> Ignoring the F<sub>L</sub> factor, which affects the Reynolds "
               "number."))
    b.append(p("The F<sub>R</sub> values for small flow valves derived from my new equations "
               "did not agree with values given in Figure 1 of the former ISA-75.01.01, "
               "<i>Flow Equations for Sizing Control Valves</i> (now revised) and they yield "
               "more accurate results typically increasing the required C<sub>v</sub> for "
               "small flow valves by a factor of four or more over the current method in "
               "Reynolds numbers below 100.<sup>5</sup> The former ISA (single) F<sub>R</sub> "
               "curve was based on a limited number of tests with full-sized globe valves, "
               "whereas the new values are based on air and water tests with small flow "
               "valves, or rotary valve types in addition to globe valves."))
    b.append(p("<sup>5</sup> Remember, there is no sonic velocity if flow is nonturbulent; "
               "therefore, critical flow equations do not apply."))
    b.append(p("From data published in <i>Perry's Chemical Engineers Handbook</i>, sixth "
               "edition, Table 5-15, it appears that more streamlined valves (e.g., angle "
               "valves and gate valves) exhibit F<sub>R</sub> factors close to the Figure 5-2 "
               "curves, while disk and plug-style globe valves (due to their more abrupt "
               "flow pattern) tend to favor the former ISA F<sub>R</sub> values when "
               "corrected with the proper F<sub>d</sub> values."))
    b.append(p("From this data, it appears that the “pseudo C<sub>v</sub>,” that is, the "
               "“laminar flow C<sub>v</sub>,” or C<sub>v</sub>F<sub>R</sub>F<sub>L</sub>, is "
               "identical for all valve types with full-size trim and at low Reynolds "
               "numbers (Re<sub>v</sub> &lt; 100)."))
    b.append(p("From this, the required C<sub>v</sub> (valve capacity needed to pass viscous "
               "flow for a given Reynolds number) is C<sub>v</sub> = q R<sub>e</sub>/(0.026 "
               "K A<sub>p</sub>), where 0.026 is the area in square inch per 1 C<sub>v</sub> "
               "when the head loss coefficient K = 1. A<sub>p</sub> is the cross-sectional "
               "area of the given pipe size in inches squared (same as the valve size!)."))
    b.append(ul([
        "K = velocity head loss coefficient of valve trim where K = (38 × "
        "A/C<sub>v</sub>)<sup>2</sup>",
        "A = flow area of trim in in<sup>2</sup>",
    ]))
    b.append(p("Furthermore, from the ISA equation, C<sub>v,Req</sub> = C<sub>i</sub>/"
               "F<sub>R</sub>, where C<sub>i</sub> is the C<sub>v</sub> calculated assuming "
               "the flow pattern is completely turbulent; this makes C<sub>v</sub> = "
               "R<sub>e</sub>/(A<sub>p</sub>F<sub>L</sub>). Because the valve Reynolds number "
               "for liquids is R<sub>e</sub> = 17300 F<sub>q</sub> q/[ν d "
               "(C<sub>vR</sub>F<sub>L</sub>/d<sup>2</sup>)<sup>0.5</sup>], the equation "
               "labelled (5-13) above gives C<sub>v,req</sub> = 0.194 q "
               "(G<sub>f</sub>/ΔP)<sup>0.5</sup> [ν/(F<sub>L</sub><sup>2</sup>"
               "F<sub>d</sub> K d<sup>2</sup>)]<sup>2/3</sup>."))
    b.append(p("Because F<sub>L</sub> is approximately proportional to the relative valve "
               "capacity (C<sub>v</sub>/d<sup>2</sup>), we may, for estimating purposes only, "
               "substitute F<sub>L</sub> ≅ 0.96[1 − 0.0025(C<sub>v</sub>/d<sup>2"
               "</sup>)]<sup>2/15</sup> in Equation 5-13."))
    b.append(p("Furthermore, F<sub>d</sub> is somewhat related to F<sub>L</sub> (e.g., a "
               "large valve, such as a ball valve, has a low F<sub>L</sub> but a high "
               "F<sub>d</sub>). We can thus further estimate that F<sub>L</sub> = F<sub>d</sub> "
               "= 0.4/0.89 = 0.42 and, finally, that √K/d is involved."))
    b.append(p("This then makes Equation 5-13: C<sub>v</sub> = 0.00386 q "
               "√(G<sub>f</sub>/ΔP) [0.96 − 0.0025(C<sub>v</sub>/d<sup>2"
               "</sup>)]<sup>2/15</sup> (ΔP/d<sup>4</sup>)<sup>2/3</sup>."))
    b.append(p("Note: The selected C<sub>v</sub> should not be less than 10 d<sup>2</sup> "
               "and no more than 30 d<sup>2</sup>."))
    b.append(p("I suggest you input the customer's pipe size for d. The previous equation "
               "will give you a ballpark C<sub>v</sub> number, which can aid in selecting a "
               "valve type. Using the actual valve coefficients (rated C<sub>v</sub>, "
               "F<sub>L</sub>, and F<sub>d</sub>), recalculate the required C<sub>v</sub> "
               "using Equation 5-9."))

    b.append(h2("Đơn vị mét", "Metric Units"))
    b.append(p("It might not bother you that the rest of the world thinks in metric terms. "
               "However, an occasion may arise when you will have to do a project for an "
               "overseas plant, and you will be confronted with liquid flow rates of cubic "
               "meters per hour instead of gpm. Luckily, the C<sub>v</sub> numbers work "
               "equally as well in Europe. For example:"))
    b.append(eq("C<sub>v</sub> = 1.17 q √(G<sub>f</sub>/ΔP)", "5-18"))
    b.append(ul([
        "q = m<sup>3</sup>/h of liquid",
        "ΔP = valve pressure drop in bar",
        "G<sub>f</sub> = specific gravity (water at 60°F = 1)",
    ]))
    b.append(p("In Germany, they go so far as to eliminate the 1.17 constant and then call "
               "the flow coefficient K<sub>v</sub>; therefore, K<sub>v</sub> = 0.85 "
               "C<sub>v</sub>, or C<sub>v</sub> = 1.17 K<sub>v</sub>."))
    b.append(p("Complications arise only if you are confronted by Newton per square meter, "
               "also called pascal or Pa. To get back to the more familiar bar, divide Pa "
               "by 100,000 or one bar = 100,000 Pa, and one bar = 14.5 psi. One kilopascal "
               "(kPa) = 0.145 psi. There is also the less often used kg/cm<sup>2</sup>, which "
               "is 0.98 bar or 14.2 psi."))
    b.append(p("Remember also that degrees Celsius is used abroad where °F = "
               "(°C × 9/5) + 32, and in absolute terms, °K = 273 + °C. "
               "Converting flowing units:"))
    b.append(ul([
        "1 m<sup>3</sup>/h liquid = 4.4 gpm",
        "1 m<sup>3</sup>/h gas = 35.3 ft<sup>3</sup>/h",
        "kg/h = 2.2 lb/h",
    ]))
    b.append(p("You are now fully equipped to work abroad."))

    b.append(h2("Chọn cỡ van nào", "What Size Valve to Choose"))
    b.append(p("After you have labored hard to select the final required valve C<sub>v</sub> "
               "suitable for maximum flow requirements, and having considered the F effects "
               "(F<sub>L</sub>, F<sub>p</sub>, F<sub>R</sub>), you are now confronted with the "
               "final choice—the valve size."))
    b.append(p("If the pressure drop is low, say, 5 to 15 psi, it is always safe to start "
               "with a line-size valve. Keep in mind that the person in the piping design "
               "department already sized the downstream or upstream pipe to pass the design "
               "flow rate at a reasonable velocity. Incidentally, valve outlet velocity "
               "should not bother you unless there could be a noise problem with high-"
               "pressure gas or steam reduction (Chapter 20, “Methods of Aerodynamic Valve "
               "Noise Reduction,” discusses aerodynamic noise), or where you have flashing "
               "liquids (if the downstream pipe is too long, your valve will cavitate "
               "because of downstream pressure buildup caused by high mixed-phase velocity). "
               "This then leaves only the C<sub>v</sub> rating of the valve. In case you "
               "have not yet selected a certain brand because you are partial to the color "
               "of the valve, that is, green or red, see Table 5-5 for a hint."))
    b.append(p("The C<sub>v</sub> values are per valve diameter (inch) squared. The "
               "C<sub>v</sub> values in parentheses are per pipe diameter (inch) squared. "
               "For example, a 6-inch eccentric rotary plug valve has a wide open "
               "C<sub>v</sub> flow coefficient of 6<sup>2</sup> × 12 = 432. However, "
               "when installed between reducers in a 12-inch pipe, the available flow "
               "coefficient is only 6<sup>2</sup> × 11.3 = 407 (see column "
               "C<sub>v</sub>/d<sup>2</sup> for D/d = 2), or 12<sup>2</sup> × 2.8 = "
               "403 using the figures in parentheses."))
    b.append(p("The above values are conservative and vary somewhat from size to size. You "
               "may notice that when high-capacity valves are used under choked flow "
               "conditions (such as steam pressure reduction), they all tend to lose their "
               "high C<sub>v</sub> advantage, as you can see from the C<sub>v</sub>F<sub>L"
               "</sub>/d<sup>2</sup> column! Explain this to your valve vendor."))
    b.append(p("Starting out with a line-size valve, divide your desired maximum "
               "C<sub>v</sub> value first. This will give you a 10% safety factor, and it "
               "will guard against the ±10% tolerance in the C<sub>v</sub> rating of "
               "the valve given by the manufacturer. Now divide this new C<sub>v</sub> "
               "number by the pipe size squared. For example, from the flow data, you "
               "require a maximum C<sub>v</sub> = 123. Your line size is 4 in. First divide "
               "123 by 0.8 to obtain 154. Now divide this by (4 in)<sup>2</sup>. "
               "154/4<sup>2</sup> = 9.6 C<sub>v</sub>/d<sup>2</sup>."))
    b.append(p("From the data given in Table 5-4, you have the following choices:"))
    b.append(ul([
        "A 4-inch single-seated globe valve, C<sub>v</sub>/d<sup>2</sup> = 10; "
        "C<sub>v</sub> rated = 10 × 4<sup>2</sup> = 160.",
        "A butterfly valve at 70° opening (if other considerations such as leakage, "
        "noise, etc., permit). Here a 3-inch butterfly valve installed in a 4-inch pipe has "
        "a flow capacity higher than 10.2 × D<sup>2</sup> (see the figures in "
        "parentheses), that is, more than 4<sup>2</sup> × 10.2 = 163 C<sub>v</sub>.",
    ]))
    b.append(p("Having thus determined the size (and type) of valve, you now should verify "
               "that you can meet the minimum required flow coefficient that your process "
               "requires. Go to the manufacturer's C<sub>v</sub> tables (usually printed in "
               "increments of 10% travel) and look up the approximate valve travel when the "
               "valve is operating at your minimum C<sub>v</sub>. This travel should not be "
               "less than 5% of the total valve travel or less than the percentage of the "
               "valve deadband (with tight packing). This is usually 5% with "
               "tetrafluoroethylene (TFE) packing to 15% for laminated graphite packing if "
               "no positioner is used. For a typical TFE-packed valve and no positioner, "
               "this limits the valve travel to 10% from the shutoff position. The only "
               "exceptions are certain soft seat plugs that “dip” through their"))
    b.append(table(
        ["Type", "C<sub>v</sub>/d<sup>2</sup>", "F<sub>L</sub>",
         "C<sub>v</sub>F<sub>L</sub>/d<sup>2</sup>",
         "C<sub>v</sub>F<sub>p</sub>/d<sup>2</sup><br>D/d = 1.5",
         "C<sub>v</sub>/d<sup>2</sup> for D/d = 2"],
        [
            "Single-seated globe valves",
            ("Parabolic plug, flow-to-open", "10", "0.9", "9", "9.8 (4.3)", "9.6 (2.4)"),
            ("Double-seated globe valve", "12.5", "0.9", "11.3", "12 (5.3)", "11.7 (2.9)"),
            ("High-capacity cage valve to size 3 in only", "14", "0.9", "12.5", "13.5 (6.0)", "12.9 (3.2)"),
            ("Eccentric rotary plug valve", "12.0", "85", "10", "11.6 (5.1)", "11.3 (2.8)"),
            ("Butterfly valve 60° open", "17", "0.68", "11.5", "15.8 (7.0)", "15 (3.8)"),
            ("Butterfly valve 70° open", "27", "0.57", "15.5", "23 (10.2)", "20.8 (5.2)"),
            ("Fluted butterfly valve @ 70°", "25", "0.7", "17.5", "21.8 (9.7)", "19.8 (5.0)"),
            ("Contoured ball valve @ 90°", "25", "0.6", "15", "21.8 (9.7)", "19.8 (5.0)"),
            ("Angle, venturi type, flow-to-close", "22", "0.5", "11", "19.8 (8.8)", "18.3 (4.6)"),
            "D = inches",
        ],
        "Table 5-5. Typical flow coefficients at rated travel."))
    b.append(p("seal ring, ball valves, elastomer-lined butterfly valves with angle-seated "
               "vanes, and certain diaphragm valves or pinch valves where there is no "
               "“hard” seating action. If a standard valve forces you to throttle below "
               "5% travel, then your only choice is to use a larger and a smaller valve in "
               "parallel and split-range the actuator signal, or better yet, use two "
               "separate signals from your computer so that the small valve will open "
               "first, and then the larger valve starts when the small valve is about 80% "
               "open."))
    b.append(p("In summary:"))
    b.append(ul([
        "Choose a valve that has a rated C<sub>v</sub> at least 20% larger than your maximum "
        "requirements.",
        "See that the minimum required C<sub>v</sub> occurs at least above 5% of the valve "
        "travel (check the vendor's catalog).<sup>7</sup>",
    ]))
    b.append(p("<sup>7</sup> You may have to use 10% if the 5% travel C<sub>v</sub> is not "
               "known."))

    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(refs([
        "L. R. Driskell, “New Approach to Control Valve Sizing,” <i>Hydrocarbon "
        "Processing</i> (July 1969): 111–114.",
        "Bulletin No. SM-6, “Control Valve Sizing.” Portsmouth, NH: H. D. Baumann "
        "Assoc., Ltd., (1991).",
        "H. D. Baumann, “A Case for Butterfly Valves in Throttling Applications,” "
        "<i>Instruments and Control Systems</i> (May 1979): 35–38.",
        "H. D. Baumann, “Effect of Pipe Reducers on Control Valve Capacity,” "
        "<i>Instrument &amp; Control Systems</i> (December 1968): 99–102.",
        "E. B. McCutcheon, “A Reynolds Number for Control Valves,” in <i>Flow: "
        "Its Measurement and Control in Science and Industry</i>, Volume 1, "
        "Part 3, proceedings of the first symposium on Pittsburgh, "
        "Pennsylvania, on May 9 to 14, 1971, Instrument Society of America, 1974.",
        "H. D. Baumann, “A Unifying Method for Sizing Throttling Valves Under "
        "Laminar or Transitional Flow Conditions,” <i>Transactions of the "
        "ASME, Journal of Fluids Engineering</i> (March1993): 166–169.",
        "H. D. Baumann, “Viscosity Flow Correction for Small Control Valve "
        "Trim,” <i>Transactions of the ASME, Journal of Fluids Engineering</i> "
        "113 (March 1991): 86–89.",
        "ANSI/ISA-75.01.01-2012 (60534-2-1 MOD), Industrial-Process Control "
        "Valves – Part 1-1: Flow Capacity – Sizing Equations for Fluid Flow "
        "under Installed Conditions (Research Triangle Park, NC: ISA "
        "[International Society of Automation]).",
    ]))
    b.append(p("<b>Additional Reading.</b> J. A. George, “Evolution and Status of Non-"
               "Turbulent Flow Sizing for Control Valves,” monograph, ISA 2001."))
    b.append(p("<b>Source note.</b> The OCR mangles the equation glyphs throughout: (5-14) "
               "and (5-15) are given in the same standard notation as Equation 5-10; in the "
               "worked CO<sub>2</sub> example the value 0.16 (F<sub>d</sub>) is substituted "
               "where the printed equation shows F<sub>q</sub>, giving Re<sub>v</sub> "
               "≈ 3778 (printed “377805”), n = 5.58 and F<sub>R</sub> = 0.84. The "
               "gas-sizing line ending at C<sub>v</sub> = 0.0193 and the implicit "
               "C<sub>v</sub> equations after the <i>Perry's Handbook</i> discussion are "
               "rendered symbolically; exponents such as 2/15 and 2/3 are uncertain in the "
               "scan. Printed quirks retained: F<sub>L</sub> = 0.4/0.89 = 0.42; “Table "
               "5-4” where the surrounding data are Table 5-5; “March1993” in reference "
               "6; the superscript citation “10” on the F<sub>d</sub> factors; and “85” "
               "(evidently 0.85) in the eccentric rotary plug row of Table 5-5. Equation "
               "5-13 is cited in passing only; it belongs to the preceding section and is "
               "not boxed here."))
    return "".join(b)
