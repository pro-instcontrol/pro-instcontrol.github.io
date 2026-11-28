# -*- coding: utf-8 -*-
"""McMillan Ch.17 prose module A — printed pp. 482-489 (PDF pp. 503-510).

Chapter opening, 17.1, 17.2, 17.3, 17.3.1, the six selection criteria, the
three unnumbered subheadings, the MIC/MESG and T6-T1 display blocks, and the
final paragraph ending exactly at `However,` (the seam with module B).
"""
from mcmillan_common import h3, h4, p, note, eq, fig, ol
import mcmillanfig17 as F


def body_vi():
    b = []

    # ---- printed p.482: chapter opening (A0 title is owned by the shell).
    b.append(h3("Mở đầu chương", "Chapter opening"))
    b.append(p("Sau khi đã xác định mức độ rủi ro và các phương pháp khác nhau "
               "mà thiết bị điện và dụng cụ đo có thể được chế tạo để giải "
               "quyết rủi ro đó, giờ đây cần xem xét đến việc lựa chọn thực tế "
               "thiết bị nhằm giải quyết các rủi ro đó, việc lắp đặt và các "
               "nguồn điện liên quan, cũng như bảo vệ, vì tất cả những yếu tố "
               "này đều ảnh hưởng đến an toàn tổng thể chống cháy nổ và vụ nổ "
               "do đó gây ra. Có ba vấn đề cơ bản cần giải quyết: Thứ nhất, "
               "nguồn điện cơ bản cho mọi thiết bị trong khu vực nguy hiểm và "
               "mọi thiết bị khác có thể ảnh hưởng đến an toàn, bao gồm bảo vệ "
               "điện và các yêu cầu về cân bằng thế (nối liên kết); thứ hai, "
               "các loại thiết bị nên được lựa chọn cho những rủi ro cụ thể; "
               "và thứ ba, các phương pháp liên kết thiết bị với nguồn điện "
               "cũng như mọi kết nối cần thiết khác với các mạch điện bên "
               "ngoài bản thân thiết bị."))

    # ---- 17.1 (A2/A3, printed p.482) then A3 -> B1 across the page break.
    b.append(h3("17.1 Hệ thống cấp điện", "17.1 Electrical supply systems"))
    b.append(p("Đa số thiết bị điện ở Vương quốc Anh được thiết kế để được cấp "
               "từ nguồn điện có điện áp danh định 240 V rms xoay chiều một pha "
               "(tức là pha đến trung tính) ở 50 Hz hoặc, trong trường hợp các "
               "thiết bị như máy quay, 415 V rms ba pha (tức là pha/pha), vì "
               "đây là nguồn điện thường được dùng trên khắp Vương quốc Anh. "
               "(Để phù hợp với các Chỉ thị của EU, điện áp danh định này sẽ "
               "được đổi thành 230V, nhưng sự thay đổi này không được coi là "
               "đáng kể vì nó nằm trong dải dung sai của chuẩn cấp điện hiện "
               "hành.) Nguồn điện này được lấy từ một điện áp cao hơn nhiều "
               "như 3300, 6600, 11000 hoặc 33000V bằng các máy biến áp giảm áp "
               "như trong Hình 17.1. Hệ thống thường dùng chỉ dùng hai dây cho "
               "nguồn một pha (bốn dây cho nguồn ba pha), dẫn trung tính hoặc "
               "dẫn về được kết hợp với dẫn bảo vệ (tiếp đất) (hệ thống "
               "TN-C-S¹ -xem Hình 17.1.) Dẫn này được tin cậy để mang cả dòng "
               "về và mọi dòng sự cố phát sinh, vì nói chung không có kết nối "
               "dẫn trực tiếp nào giữa một lắp đặt và nguồn cấp ngoài dẫn bảo "
               "vệ và trung tính kết hợp (PEN) được nối với"))
    b.append(note("<b>Ghi chú về khoảng trắng trong điện áp và tần số.</b> Bản "
                  "in viết ‘240 V rms’, ‘50 Hz’ và ‘415 V rms’ có khoảng trắng, "
                  "còn ‘230V’ và ‘33000V’ thì không; bản tiếng Anh giữ nguyên. "
                  "Cụm ‘(TN-C-S system¹ -see Fig. 17.1.)’ cũng được giữ nguyên, "
                  "gồm dấu gạch ngang trước ‘see’ và dấu chấm nằm trong ngoặc "
                  "đơn."))
    b.append(fig(1, F.fig_f1701()))
    b.append(p("đất tại nguồn cấp. Để bảo đảm điện áp của các vỏ dẫn điện cục "
               "bộ của thiết bị điện có cùng thế với dẫn PEN và mọi bề mặt "
               "dẫn điện cục bộ khác kể cả mặt đất, dẫn PEN thường được nối đất "
               "tại mỗi địa điểm người dùng. Điều này dẫn đến vấn đề là, nếu "
               "dẫn PEN bị đứt giữa các địa điểm thì mọi dòng trung tính về sẽ "
               "chảy vào đất và xuất hiện lại tại điểm gần nhất mà dẫn PEN vẫn "
               "còn nối với nguồn cấp, thường là kết nối đất tại địa điểm của "
               "người dùng lân cận. Điều này rõ ràng không thể chấp nhận được "
               "đối với các địa điểm có khu vực nguy hiểm, vì nó tạo ra tình "
               "huống mà các lắp đặt điện của họ có thể bị xâm nhập bởi dòng "
               "điện từ các địa điểm khác và nằm ngoài tầm kiểm soát của họ. "
               "Vì lý do này, không nên dùng các loại nguồn cấp như vậy cho "
               "các địa điểm chứa khu vực nguy hiểm; thay vào đó dùng nguồn cấp "
               "sử dụng dẫn bảo vệ riêng (TN-S¹-Hình 17.2) được nối với dẫn "
               "trung tính và nối đất tại nguồn cấp. Dẫn trung tính giờ đây "
               "không còn được nối đất tại mỗi điểm người dùng và sự cố đã "
               "mô tả ở trên thường không thể xảy ra."))
    b.append(note("<b>Ghi chú về chú thích các hình.</b> Chú thích Hình 17.1 "
                  "dùng dấu gạch ngang dài trong ‘T–N–C–S’, trong khi thân bài "
                  "dùng ‘TN-C-S’ với dấu gạch ngang thường. Chú thích Hình 17.2 "
                  "viết ‘TN-S¹-Fig. 17.2’ không có khoảng trắng sau dấu gạch "
                  "ngang. Cả hai được giữ nguyên."))
    b.append(fig(2, F.fig_f1702()))

    # ---- printed p.484: figure 17.3 at the head of the page, then C1/C2.
    b.append(fig(3, F.fig_f1703()))
    b.append(note("<b>Ghi chú về nhãn trong Hình 17.3.</b> Nhãn trong hình in "
                  "là ‘(Either PEN CDR or just N if separate PE CDR exits)’ — "
                  "chữ ‘exits’, không phải ‘exists’. Chú thích có hai Ghi chú "
                  "đánh số (1) và (2) với dấu ngoặc kém kiểu in; bản tiếng Anh "
                  "giữ nguyên."))
    b.append(p("Tuy nhiên, vẫn còn khả năng rằng sự cố tại các địa điểm người "
               "dùng khác, mà không thể kiểm soát được, có thể khiến dòng điện "
               "đi qua đất sang dẫn bảo vệ trong một khu vực nguy hiểm và do "
               "đó, ngoài việc dùng hệ thống phân phối TN-S, nên tách nguồn cấp "
               "đến các địa điểm có khu vực nguy hiểm khỏi mọi nguồn cấp khác, "
               "đặc biệt là những nguồn mà người dùng trong khu vực nguy hiểm "
               "không kiểm soát được (xem Hình 17.3). Ở các địa điểm lớn như "
               "nhà máy lọc dầu hoặc nhà máy hóa chất, việc này dễ thực hiện "
               "vì nguồn cấp thường được đưa đến nhà máy ở điện áp cao và được "
               "biến áp sau khi đến nơi, do đó có sự cách ly galvanic giữa "
               "nhà máy cụ thể và các lắp đặt khác. Tình hình khó khăn hơn đối "
               "với các lắp đặt nhỏ biệt lập, chẳng hạn như các trạm bơm, vì "
               "nguồn cấp của chúng thường ở điện áp nguồn thông thường đã "
               "mô tả ở trên và dùng chung với người dùng khác. Trong trường "
               "hợp này, nên lắp máy biến áp để tạo cách ly galvanic giữa các "
               "nguồn cấp được dùng và nguồn cấp đến, trừ khi có thể bảo đảm "
               "rằng vấn đề xâm nhập không nghiêm trọng. Trong trường hợp "
               "nguồn cấp chỉ dùng chung cho chính người dùng đó, ví dụ cấp "
               "cho các phần khác nhau của cùng một địa điểm, thì phân tích "
               "có thể cho thấy không cần cách ly bổ sung, nhưng đó sẽ là "
               "ngoại lệ chứ không phải quy tắc."))
    b.append(p("Vì vậy, yêu cầu chung cần áp dụng là mọi nguồn cấp cho thiết bị "
               "trong khu vực nguy hiểm đều phải có dẫn về (trung tính) và dẫn "
               "bảo vệ (tiếp đất) riêng biệt, và phải được cách ly bằng máy "
               "biến áp khỏi những người dùng khác của nguồn cấp, trừ khi "
               "những người dùng đó nằm dưới sự kiểm soát của người dùng trong "
               "khu vực nguy hiểm và một đánh giá đã chỉ ra rằng máy biến áp "
               "đó là không cần thiết."))

    # ---- printed p.485: 17.2, paragraphs D1-D5.
    b.append(h3("17.2 Bảo vệ điện", "17.2 Electrical protection"))
    b.append(p("Bảo vệ điện cho mọi nguồn cấp đến thiết bị trong khu vực nguy "
               "hiểm (bầu khí quyển nổ) có tầm quan trọng cơ bản. Thiết bị được "
               "bảo vệ như mô tả trong các Chương 7 đến 16 được chế tạo sao cho "
               "khó có khả năng tạo ra tình huống có khả năng gây cháy nổ trong "
               "vận hành bình thường hoặc do sự cố. Cần nhớ rằng, dù rất hiếm, "
               "vẫn có khả năng thiết bị trở nên có khả năng gây cháy. Khi "
               "điều đó xảy ra, thời gian của nó phải được giới hạn để cơ hội "
               "gây cháy nổ ở mức có thể chấp nhận được, do khả năng trùng hợp "
               "thấp, hoặc do tình huống không phát sinh trước khi kiểm tra và "
               "bảo trì định kỳ phát hiện bất kỳ sự suy giảm nào có thể dẫn "
               "đến cháy nổ và hành động cần thiết được thực hiện."))
    b.append(p("Bảo vệ điện nên được chỉnh với mức tác động càng gần mức vận "
               "hành bình thường càng tốt mà không tạo ra tình huống mà các "
               "sự cắt ngang gây phiền nhiễu trở thành vấn đề, và nên bao gồm "
               "quá tải, ngắn mạch nguồn cấp và sự cố tiếp đất. Bảo vệ điện "
               "phải như nhau bất kể vùng rủi ro, nhưng phải hết sức cẩn trọng "
               "đối với bất kỳ mạch nào đi vào Vùng 0 hoặc 20, do thực tế là "
               "bầu khí quyển nổ được giả định là luôn hiện diện và rằng thời "
               "gian đáng kể của quá tải, sự cố, sự cố ngắn mạch hoặc sự cố "
               "tiếp đất là điều khó chấp nhận nhất trong những hoàn cảnh này."))
    b.append(note("<b>Ghi chú về cụm ‘nuisance rips’.</b> Bản in viết ‘nuisance "
                  "rips become a problem’, không phải ‘trips’; bản tiếng Anh "
                  "giữ nguyên. Đoạn sau đó cũng giữ ‘it is this type of faults "
                  "which is most likely’ (số nhiều ‘faults’ đi với ‘which is’ "
                  "ở số ít)."))
    b.append(p("Ngoài những điều trên, các phương tiện bảo vệ/cách ly điện "
               "cách ly tất cả dẫn pha và dẫn trung tính (nhưng không cách ly "
               "dẫn cân bằng thế hoặc dẫn bảo vệ) phải hiện diện ở các khu vực "
               "không nguy hiểm để cho phép cách ly các mạch đi vào khu vực "
               "nguy hiểm. Việc cách ly trung tính bằng công tắc cách ly các "
               "dẫn pha được khuyến nghị nhưng không thiết yếu trong những "
               "hoàn cảnh này. Yêu cầu tối thiểu là một liên kết riêng trong "
               "dẫn trung tính, có thể cung cấp cách ly thủ công. Tuy nhiên, "
               "khi cần phương tiện cách ly bổ sung trong khu vực nguy hiểm, "
               "thiết bị cách ly phải được bảo vệ bằng một trong các khái "
               "niệm được đề cập trong các Chương 7 đến 16 và thiết bị cách ly "
               "phải cách ly trung tính đồng thời với các dẫn pha. Điều này là "
               "vì trung tính có thể đang mang dòng sự cố từ các nguồn khác "
               "ngay cả khi các dẫn pha đã bị cách ly, và trong những hoàn "
               "cảnh đó, cách ly trung tính bằng một liên kết thủ công có thể "
               "tạo ra tia lửa có khả năng gây cháy nổ."))
    b.append(p("Các mạch điện áp cao, chẳng hạn như mạch dùng để cấp điện cho "
               "máy quay lớn, nên được đối xử như các mạch cấp điện khác nhưng "
               "cách ly ở đây đặc biệt quan trọng và phải nhanh nhất có thể. "
               "Việc cách ly sự cố tiếp đất đặc biệt quan trọng vì chính loại "
               "sự cố này có khả năng gây ra tia lửa không được bảo vệ cao "
               "nhất, và phải cách ly gần như tức thời."))
    b.append(p("Các yêu cầu nêu trên áp dụng cho mọi mạch đi vào khu vực nguy "
               "hiểm, trừ mạch an toàn nội tại (Chương 13) và mạch không gây "
               "cháy (Chương 14), trong đó điện áp và dòng điện trong mạch "
               "được hạn chế đến mức ngăn ngừa tia lửa có khả năng gây cháy "
               "nổ, nhưng trong những trường hợp này, yêu cầu bảo vệ điện nói "
               "chung vẫn áp dụng cho thiết bị ở khu vực không nguy hiểm tạo "
               "ra các mạch đó."))

    # ---- printed p.486: 17.3, lead-in and six numbered criteria.
    b.append(h3("17.3 Lựa chọn thiết bị", "17.3 Selection of apparatus"))
    b.append(p("Khu vực nguy hiểm là một loại địa điểm đặc biệt, nơi mà ngoài "
               "các vấn đề môi trường bình thường còn có thể xuất hiện bầu "
               "khí quyển nổ. Các tiêu chí lựa chọn cơ bản bao gồm những điều "
               "sau."))
    b.append(ol([
        "Vỏ của thiết bị phải đủ để ngăn sự xâm nhập của chất lỏng và chất rắn "
        "ở mức có thể làm suy giảm hoạt động của thiết bị bằng cách gây ngắn "
        "mạch một phần hoặc toàn phần, ăn mòn hoặc bất kỳ sự suy giảm nào khác "
        "làm giảm độ tin cậy của thiết bị hoặc làm hư hỏng các đặc tính an toàn "
        "của nó. Đối với thiết bị lắp ngoài trời, điều này thường có nghĩa là "
        "cấp bảo vệ vỏ IP54.",
        "Vỏ của thiết bị và mọi bộ phận bên trong cần thiết để duy trì hoạt "
        "động tin cậy, cũng như khái niệm bảo vệ, phải chống được sự tấn công "
        "hóa học từ các vật liệu hiện có tại vị trí của nó.",
        "Định mức của thiết bị phải đủ để bao phủ các điều kiện vận hành tại "
        "điểm lắp đặt (các định mức này là các giá trị do khái niệm bảo vệ đưa "
        "ra, có thể bao gồm các hệ số an toàn thay vì các định mức công nghiệp "
        "cơ bản).",
        "Thiết bị và vỏ của nó phải đủ chắc chắn để chịu được mọi va đập cơ "
        "học do va chạm, do rơi rụng nếu là thiết bị di động, hoặc do rung "
        "động. Các yêu cầu về cấu tạo bao gồm rơi rụng hoặc va chạm bình "
        "thường, nhưng không nhất thiết bao gồm rung động và những vị trí mà "
        "va chạm đặc biệt dữ dội.",
        "Phải giải quyết khả năng cụ thể hình thành tĩnh điện trên thiết bị "
        "có vỏ bằng vật liệu nhựa.",
        "Phải tính đến rủi ro tia lửa nhiệt nhôm (thermite) khi dùng kim loại "
        "nhẹ hoặc hợp kim trong vỏ thiết bị. Điều này chỉ được tính đến một "
        "phần trong các yêu cầu về cấu tạo của thiết bị.",
    ]))
    b.append(h4("Vỏ kim loại nhẹ", "Light metal enclosures"))
    b.append(p("Phải đặc biệt cẩn trọng trong trường hợp sau cùng là thiết bị "
               "có vỏ kim loại nhẹ. Các Tiêu chuẩn cấu tạo cho thiết bị có tính "
               "đến hàm lượng magiê nhưng vẫn còn rủi ro dư do khả năng có mặt "
               "của nhôm hoặc titan, và rủi ro này cũng hiện diện khi dùng cáp "
               "bọc nhôm. Rủi ro chủ yếu đến từ khả năng kim loại nhẹ bị kim "
               "loại ferit đã bị oxy hóa (gỉ) đập vào, khi tia lửa tạo ra "
               "thường dữ dội hơn so với trường hợp tiếp xúc giữa hai kim loại "
               "ferit hoặc giữa kim loại ferit với đồng hoặc đồng thau. Điều "
               "này dẫn đến rủi ro đáng kể về tia lửa có khả năng gây cháy nổ."))
    b.append(note("<b>Ghi chú về cách viết ‘oxidized’.</b> Bản in dùng cách "
                  "viết theo tiếng Mỹ ‘oxidized (rusty) ferrous metal’; bản "
                  "tiếng Anh giữ nguyên."))
    b.append(p("Rủi ro là không đáng kể trong Vùng 2 vì khả năng trùng hợp "
               "giữa tia lửa và bầu khí quyển nổ là rất thấp, ở mức có thể "
               "chấp nhận được. Trong trường hợp Vùng 22 về cơ bản cũng đúng, "
               "nhưng ở đây có rủi ro là một cú đập vào vỏ kim loại nhẹ có thể "
               "đồng thời gây lắng đọng bụi trên"))

    # ---- printed p.487: F1 -> F5.
    b.append(p("thiết bị, tạo thành một đám mây, sản sinh sự trùng hợp không "
               "thể chấp nhận được. Vì vậy, trong Vùng 22, không nên dùng "
               "thiết bị có vỏ kim loại nhẹ nếu có thể, nhưng dù sao thì thiết "
               "bị cũng phải được bảo vệ khỏi va đập nhờ vị trí lắp đặt hoặc "
               "che chắn, hoặc phải được chế tạo và lắp đặt sao cho loại trừ "
               "được sự lắng đọng bụi (ví dụ, không có bề mặt phẳng nằm ngang "
               "hoặc có nắp che để ngăn bụi lắng đọng). Thiết bị có vỏ kim "
               "loại nhẹ dự định dùng cho Vùng 1 không bị coi là rủi ro không "
               "thể chấp nhận, trừ khi nó được lắp ở vị trí có rủi ro va đập "
               "cơ học cao, chẳng hạn gần đường giao thông, hoặc nơi công "
               "nhân thường xuyên làm việc với dụng cụ. Trong những trường "
               "hợp đó, nên tránh dùng hoặc phải có tấm che để ngăn va đập "
               "trực tiếp vào vỏ thiết bị. Yêu cầu đối với Vùng 21 cũng giống "
               "như yêu cầu nêu trên về va đập đối với Vùng 22. Trong trường "
               "hợp này, vấn đề bụi chủ yếu là đám mây chứ không phải lớp (như "
               "trường hợp Vùng 22), nhưng rủi ro trùng hợp không lớn hơn. "
               "Trong trường hợp Vùng 0 và 20, bầu khí quyển nổ được coi là "
               "luôn hiện diện và không va đập nào được chấp nhận. Trừ khi có "
               "thể bảo đảm hoàn toàn không có va đập nào, không nên dùng "
               "thiết bị có vỏ kim loại nhẹ trong Vùng 0 hoặc 20."))
    b.append(h3("17.3.1 Lựa chọn theo khí, hơi và sương mù",
                "17.3.1 Selection in respect of gases, vapours and mists"))
    b.append(p("Thiết bị dùng cho rủi ro khí, hơi và sương mù được định nghĩa, "
               "đối với công nghiệp trên mặt đất, là thiết bị Nhóm II (thiết "
               "bị Nhóm I dùng cho việc sử dụng dưới lòng đất trong hầm mỏ than "
               "và các hầm mỏ khác có thể có khí dễ cháy). Nếu thiết bị không "
               "tạo ra tia lửa mà bầu khí quyển nổ có thể tiếp cận được (tức "
               "là được bảo vệ bằng tạo áp ‘p’ (Chương 11), nhồi bột ‘q’ "
               "(Chương 9), ngâm dầu ‘o’ (Chương 9), bọc kín ‘m’ (Chương 9), "
               "an toàn tăng cường ‘e’ (Chương 12) hoặc Kiểu ‘N’ trong ngữ "
               "cảnh không phát tia lửa (Chương 14)), thì việc lựa chọn thiết "
               "bị Nhóm II là đủ, với điều kiện phải xét đến nhiệt độ bề mặt."))
    b.append(note("<b>Ghi chú về ‘Group II apparatus’ và dấu ngoặc đơn không "
                  "được đóng.</b> Bản in viết ‘Group II apparatus’ và ‘Group I "
                  "apparatus’ bằng chữ số La Mã (không phải chữ số 1), và đoạn "
                  "kết thúc bằng ‘… surface temperature considerations.’ mà "
                  "không đóng dấu ngoặc đơn mở trước ‘i.e.’; bản tiếng Anh giữ "
                  "nguyên cả hai."))
    b.append(h4("Gây cháy bằng tia lửa và hồ quang",
                "Ignition by sparks and arcs"))
    b.append(p("Khi phát sinh tia lửa mà bầu khí quyển nổ thực sự có thể tiếp "
               "cận được, chúng sẽ được làm cho không có khả năng gây cháy bằng "
               "an toàn nội tại ‘i’ (Chương 13) hoặc khái niệm hạn chế năng "
               "lượng trong Kiểu ‘N’ (Chương 14), hoặc chúng sẽ bị ngăn không "
               "gây nổ dù vẫn có khả năng gây cháy nhờ dùng khái niệm vỏ chống "
               "cháy ‘d’ (Chương 10) hoặc khái niệm linh kiện không gây cháy "
               "trong Kiểu ‘N’ (Chương 14). Trong những trường hợp này, mức độ "
               "gây cháy thay đổi theo khả năng gây cháy của hỗn hợp khí, hơi, "
               "sương mù và không khí, và điều này cho phép thay đổi mức độ "
               "nghiêm ngặt của việc hạn chế cấu tạo thiết bị, và thiết bị như "
               "vậy được chia thành ba Nhóm phụ IIA, IIB và IIC, tùy theo khả "
               "năng gây cháy của chúng. Các khí và hơi được liên kết với các "
               "phân nhóm này để cho phép lựa chọn loại phù hợp nhất theo đặc "
               "tính gây cháy của chúng. Cần nhớ rằng việc hạn chế năng lượng, "
               "chẳng hạn"))

    # ---- printed p.488: G1 -> G8 and the MIC/MESG display.
    b.append(p("như được dùng trong an toàn nội tại và khái niệm Kiểu ‘N’, dựa "
               "trên việc sử dụng thiết bị thử nghiệm như trong Hình 13.2 tại "
               "Chương 13, còn kỹ thuật phòng nổ dùng trong vỏ chống cháy và "
               "khái niệm Kiểu ‘N’ dựa trên thiết bị thử nghiệm như trong Hình "
               "8.1 tại Chương 8. Bất kỳ khí hoặc hơi cụ thể nào cũng có thể "
               "được đo trong các thiết bị thử nghiệm này để xác định Dòng "
               "điện gây cháy tối thiểu (MIC), liên quan đến khả năng gây cháy "
               "của tia lửa, và Khe hở an toàn thử nghiệm tối đa (MESG), liên "
               "quan đến hiệu quả của vỏ tia lửa trong việc ngăn sự truyền của "
               "sự cháy do tia lửa gây ra ra khỏi vỏ. May mắn thay, hai khía "
               "cạnh này của đặc tính của khí hoặc hơi có liên quan với nhau, "
               "nên có thể dùng một cách tiếp cận chung. Như vậy, khí, hơi và "
               "sương mù được liên kết với nhóm phụ của thiết bị dựa trên MIC "
               "của chúng (thường được nêu như một phần của MIC của metan) và "
               "MESG của chúng (thường được nêu bằng mm) như sau:"))
    b.append(eq("Nhóm phụ IIA&#160;&#160;&#160;MIC &gt; 0.8<br>"
                "&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;"
                "&#160;&#160;&#160;MESG &gt; 0.9 mm<br>"
                "Nhóm phụ IIB&#160;&#160;&#160;MIC ≤ 0.45 và ≥ 0.8<br>"
                "&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;"
                "&#160;&#160;&#160;MESG ≤ 0.5 mm và ≥ 0.9 mm<br>"
                "Nhóm phụ IIC&#160;&#160;&#160;MIC ≥ 0.45<br>"
                "&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;"
                "&#160;&#160;&#160;MESG ≥ 0.5 mm"))
    b.append(note("<b>Ghi chú về giới hạn Nhóm phụ IIB.</b> Bản in cho ‘MIC ≤ "
                  "0.45 và ≥ 0.8’ và ‘MESG ≤ 0.5 mm và ≥ 0.9 mm’. Các giới "
                  "hạn có vẻ bị đảo ngược nhưng được sao chép đúng như bản in."))
    b.append(p("Thông thường chỉ cần đo một trong hai thông số này để xác định "
               "nhóm phụ mà khí hoặc hơi được liên kết, trừ khi thông số được "
               "đo cho thấy khí đó nằm gần giới hạn như sau:"))
    b.append(p("Nếu MIC đo được nằm giữa 0.8 và 0.9 thì nhóm phụ được xác định "
               "bởi MESG và không nhất thiết là IIA."))
    b.append(p("Nếu MIC đo được nằm giữa 0.45 và 0.5 thì nhóm phụ được xác "
               "định bởi MESG và không nhất thiết là IIB."))
    b.append(p("Nếu MESG đo được nằm giữa 0.5 và 0.55 thì nhóm phụ được xác "
               "định bởi MIC và không nhất thiết là IIB."))
    b.append(p("Các tình huống trên dựa trên kiến thức về đặc tính của khí và "
               "hơi đã được đo cho đến nay, và số lượng của chúng lớn đến mức "
               "người ta tin rằng đây là những tình huống duy nhất cần đo thêm "
               "thông số kia."))
    b.append(p("Nhiều khí và hơi đã được xác định, cả ở cấp quốc gia lẫn quốc "
               "tế, là liên kết với các nhóm phụ cụ thể bằng phép đo hoặc bằng "
               "đánh giá dựa trên sự tương đồng về cấu trúc hóa học của chúng "
               "với các khí và hơi khác mà nhóm phụ tương ứng đã được xác định "
               "bằng phép đo. Chúng được cho trong Bảng 4.3 tại Chương 4. Chưa "
               "có công trình nào được ghi nhận về sương mù hình thành từ "
               "chất lỏng ở dưới nhiệt độ sôi của chúng, và có thể hợp lý cho "
               "rằng, do kích thước hạt lớn hơn, chúng sẽ khó gây cháy hơn hơi "
               "hình thành từ cùng một chất lỏng nếu chất đó được đưa lên trên "
               "nhiệt độ sôi của nó. Vì vậy, nhóm phụ chọn cho một đám sương "
               "mù nên giống như nhóm phụ của hơi sẽ hình thành nếu"))
    b.append(note("<b>Ghi chú về ‘particular subgroups’ và ‘other, gases and "
                  "vapours’.</b> Bản in dùng ‘subgroups’ viết liền ở đây (nơi "
                  "khác là ‘sub-group’) và đặt dấu phẩy sau ‘other’; bản tiếng "
                  "Anh giữ nguyên cả hai."))

    # ---- printed p.489: H1 -> H6, T-class display, final paragraph.
    b.append(p("chất lỏng tạo sương mù được đưa lên trên nhiệt độ sôi của nó. "
               "Dù điều này có thể là nặng nề, không thể nới lỏng trừ khi có "
               "thể chứng minh là hợp lệ bằng cách đo nhiệt độ gây cháy của một "
               "đám sương mù cụ thể với kích thước hạt nhỏ nhất có thể trong "
               "trường hợp đó, và rất khó có thể làm được điều này một cách "
               "đáng tin cậy."))
    b.append(p("Hệ thống phân nhóm ở Hoa Kỳ, vốn tìm cách thực hiện chức năng "
               "giống như phân nhóm ở châu Âu, được cho trong Bảng 8.1 tại "
               "Chương 8. Nó khác với hệ thống dùng ở châu Âu ở chỗ dùng một "
               "chữ cái duy nhất, hydro và axetilen được tách riêng và carbon "
               "disulphide không được đề cập. Nếu thiết bị của Hoa Kỳ được cho "
               "là phù hợp về mặt khác, nên dùng hệ thống phân nhóm của Hoa Kỳ "
               "để lựa chọn nó nhưng, vì có thể gây nhầm lẫn, không nên dùng "
               "thiết bị đó trừ khi mọi người tham gia vào việc lựa chọn, lắp "
               "đặt và bảo trì thiết bị đều nắm rõ hệ thống này và mối liên hệ "
               "của nó với hệ thống châu Âu. Dù sao đi nữa, việc thực hiện "
               "Chỉ thị mới của EU 94/9/EC² có khả năng khiến việc sử dụng "
               "thiết bị như vậy bị loại dần, trừ khi nó đáp ứng các yêu cầu "
               "của Tiêu chuẩn châu Âu, dùng hệ thống phân nhóm châu Âu."))
    b.append(note("<b>Ghi chú về các cụm in trong đoạn về Hoa Kỳ.</b> Bản in "
                  "viết ‘carbon disulphide in not addressed’ (chữ ‘in’, không "
                  "phải ‘is’), ‘It is different to that used in Europe’ và ‘EU "
                  "Directive 94/9/EC²’ kèm chỉ số tham chiếu ²; bản tiếng Anh "
                  "giữ nguyên cả ba."))
    b.append(h4("Gây cháy bằng bề mặt nóng", "Ignition by hot surfaces"))
    b.append(p("Thiết bị được chế tạo theo mọi khái niệm bảo vệ được mô tả "
               "trong các Chương 7 đến 14 được phân loại theo nhiệt độ tối đa "
               "đạt được của bất kỳ bề mặt nào mà bầu khí quyển nổ có thể tiếp "
               "cận, và bất kỳ sự gây cháy nào gây ra cũng sẽ dẫn đến một vụ nổ "
               "không được thiết bị chứa giữ. Hệ thống phân loại nhiệt độ bề "
               "mặt được mô tả trong Chương 8 và thiết bị được cấp một cấp "
               "nhiệt độ từ T1 đến T6 ở châu Âu tùy theo nhiệt độ bề mặt tối "
               "đa của nó. Bảng 4.3 tại Chương 4 quy định cấp nhiệt độ bề mặt "
               "tối đa yêu cầu đối với thiết bị dự định dùng trong các khí và "
               "hơi cụ thể, dựa trên nhiệt độ gây cháy tối đa đã đo được của "
               "khí hoặc hơi. Một đám sương mù sẽ mang cùng cấp nhiệt độ tối "
               "đa như hơi sẽ hình thành bằng cách nâng nhiệt độ của chất lỏng "
               "tạo sương mù lên trên nhiệt độ sôi của nó. Có thể dùng thiết bị "
               "có cấp nhiệt độ hạn chế hơn trong các khí, hơi và sương mù cụ "
               "thể như sau:"))
    b.append(eq("T6 – chỉ thiết bị có phân loại T6 mới được dùng<br>"
                "T5 – thiết bị có phân loại T5 và T6 được dùng<br>"
                "T4 – thiết bị có phân loại T4, T5 và T6 được dùng<br>"
                "T3 – thiết bị có phân loại T6, T5, T4 và T3 được dùng<br>"
                "T2 – thiết bị có phân loại T6, T5, T4, T3 và T2 được dùng<br>"
                "T1 – thiết bị có phân loại T6, T5, T4, T3, T2 và T1 được dùng"))
    b.append(note("<b>Ghi chú về thứ tự các cấp nhiệt độ.</b> Ở mỗi dòng, bản "
                  "in liệt kê các cấp theo thứ tự giảm dần T6, T5, T4, T3, T2, "
                  "T1, kể cả các dòng T3–T1; bản tiếng Anh giữ nguyên thứ tự "
                  "này."))
    b.append(p("Trong một số hoàn cảnh, có thể chứng minh rằng thiết bị đáp ứng "
               "yêu cầu của một khái niệm bảo vệ cụ thể ở nhiệt độ môi trường "
               "cao hơn nhiều so với 40 °C thường dùng để phân loại nhiệt độ "
               "(ví dụ, điện trở nhiệt, cặp nhiệt điện). Trong những trường "
               "hợp như vậy, phân loại nhiệt độ đôi khi dựa trên nhiệt độ môi "
               "trường tối đa có thể và điều này sẽ do nhà cung cấp thiết bị "
               "xác định. Tuy nhiên,"))
    b.append(note("<b>Ghi chú về ‘40 °C’ và điểm nối giữa các phần.</b> Bản in "
                  "có khoảng trắng trong ‘40 °C’; bản tiếng Anh giữ nguyên. "
                  "Đoạn cuối cùng kết thúc đúng tại ‘However,’; phần tiếp theo "
                  "bắt đầu bằng ‘a surface temperature classification may be "
                  "given…’."))
    return "".join(b)


def body_en():
    b = []

    # ---- printed p.482: chapter opening (A0 title is owned by the shell).
    b.append(h3("Chapter opening", "Chapter opening"))
    b.append(p("Having identified the degree of risk and the various methods "
               "by which electrical apparatus and instrumentation may be "
               "constructed to address the risk it is now necessary to consider "
               "the actual selection of apparatus to address those risks, its "
               "installation and associated electrical supplies, and "
               "protection, as all of these have an effect on overall security "
               "against ignition and resultant explosion. There are three "
               "basic matters which need addressing: First, the basic "
               "electrical supply to all apparatus in the hazardous area and "
               "any other apparatus which may have an influence on security "
               "including electrical protection and potential equalization "
               "(bonding) requirements; second, the types of apparatus which "
               "should be selected for particular risks; and third, the "
               "methods of interconnection of apparatus with power sources and "
               "any other necessary interconnections with electrical circuits "
               "external to the apparatus itself."))

    # ---- 17.1 (A2/A3, printed p.482) then A3 -> B1 across the page break.
    b.append(h3("17.1 Electrical supply systems", "17.1 Electrical supply systems"))
    b.append(p("The majority of electrical apparatus in the UK is designed to "
               "be fed from a supply whose rated voltage is 240 V rms ac single "
               "phase (i.e., phase to neutral) at 50 Hz or, in the case of such "
               "things as rotating machines, 415 V rms three phase (i.e., "
               "phase/phase) as this is the supply which is normally used "
               "throughout the UK. (To come into line with EU Directives this "
               "rated voltage is set to change to 230V but this change is not "
               "considered as significant as it is within the tolerance band "
               "of the current supply norm.) This supply is derived from a "
               "much higher voltage such as 3300, 6600, 11000 or 33000V by "
               "step-down transformers as shown in Fig. 17.1. The normally "
               "used system uses only two wires for a single-phase supply "
               "(four for a three-phase supply) the neutral or return "
               "conductor being combined with the protective (earth) conductor "
               "(TN-C-S system¹ -see Fig. 17.1.) This conductor is relied upon "
               "to carry both the return current and any fault currents which "
               "occur as there is usually no direct conductive connection "
               "between any installation and the supply source other than the "
               "combined protective and neutral (PEN) conductor which is "
               "connected to"))
    b.append(note("<b>Source quirks: voltage and frequency spacing.</b> The "
                  "print reads ‘240 V rms’, ‘50 Hz’ and ‘415 V rms’ with "
                  "spaces, but ‘230V’ and ‘33000V’ without; all are kept as "
                  "printed. The phrase ‘(TN-C-S system¹ -see Fig. 17.1.)’ is "
                  "also retained verbatim, with the hyphen before ‘see’ and "
                  "the full stop inside the closing parenthesis."))
    b.append(fig(1, F.fig_f1701()))
    b.append(p("earth at the source of supply. To ensure that voltages of "
               "local conducting enclosures of electrical equipment are at "
               "the same potential as the PEN conductor and any other local "
               "conducting surfaces including the ground, the PEN conductor "
               "is normally earthed at each user site. This leads to problems "
               "in that, if the PEN conductor breaks between sites then any "
               "neutral return current will flow into the ground and reappear "
               "at the nearest point where the PEN conductor remains connected "
               "to the supply source, which is usually the earth connection at "
               "a neighbouring user site. This is clearly not acceptable as "
               "far as sites with hazardous areas are concerned as it produces "
               "a situation where their electrical installations could be "
               "invaded by currents from other sites and over which they have "
               "no control. For this reason such types of supply should not be "
               "used for sites containing hazardous areas and instead a supply "
               "using a separate protective conductor (TN-S¹-Fig. 17.2) "
               "connected to the neutral conductor and earthed at the source "
               "of supply. The neutral conductor is now no longer earthed at "
               "each user point and the failure described previously cannot "
               "normally occur."))
    b.append(note("<b>Source quirks: figure captions.</b> The Fig. 17.1 caption "
                  "uses en dashes in ‘T–N–C–S’, whereas the body uses "
                  "‘TN-C-S’ with ordinary hyphens. The Fig. 17.2 caption reads "
                  "‘TN-S¹-Fig. 17.2’ with no space after the hyphen. Both are "
                  "retained as printed."))
    b.append(fig(2, F.fig_f1702()))

    # ---- printed p.484: figure 17.3 at the head of the page, then C1/C2.
    b.append(fig(3, F.fig_f1703()))
    b.append(note("<b>Source quirk: Fig. 17.3.</b> The in-figure label prints "
                  "‘(Either PEN CDR or just N if separate PE CDR exits)’ — "
                  "‘exits’, not ‘exists’. The caption has two numbered Notes, "
                  "(1) and (2), with curly quotes around ‘B’. Retained as "
                  "printed."))
    b.append(p("There is still, however, the possibility that failure at other "
               "user sites, over which no control can be exercised, could "
               "result in current being passed through the ground on to the "
               "protective conductor in a hazardous area and thus, in addition "
               "to using the TN-S distribution system, it is recommended that "
               "supplies to locations where hazardous areas exist are "
               "separated from any other supplies, particularly those over "
               "which the user in the hazardous area has no control (see Fig. "
               "17.3). On large sites, such as oil refineries or chemical "
               "plants, this is easy to achieve as the supply is normally fed "
               "to the plant at high voltage and transformed after it arrives, "
               "so that galvanic isolation exists between the particular plant "
               "and other installations. It is not so easy in the case of "
               "small isolated installations, such as pumping stations, as "
               "their feed is usually at the normal supply voltage described "
               "earlier and is common with other users. In this case it is "
               "recommended that a transformer still be fitted to provide "
               "galvanic isolation between the supplies used and the incoming "
               "supply unless it can be assured that the problem of invasion "
               "is not critical. In cases where the supply is only common to "
               "the individual user, for example, feeding different parts of "
               "the same site, then an analysis may show that additional "
               "isolation is not necessary but this will be the exception "
               "rather than the rule."))
    b.append(p("The general requirement which should be applied therefore is "
               "that all supplies to apparatus in hazardous areas should have "
               "separate return (neutral) and protective (earth) conductors "
               "and should be isolated by a transformer from other users of "
               "the supply unless those users are under the control of the "
               "user in the hazardous area and an evaluation has shown that "
               "such a transformer is not necessary."))

    # ---- printed p.485: 17.2, paragraphs D1-D5.
    b.append(h3("17.2 Electrical protection", "17.2 Electrical protection"))
    b.append(p("The electrical protection of all supplies to apparatus in "
               "hazardous areas (explosive atmospheres) is of fundamental "
               "importance. Apparatus protected as described in Chapters 7 to "
               "16 is constructed so as to be unlikely to produce an "
               "ignition-capable situation in normal operation or due to "
               "fault. It has to be remembered, however, that it is possible "
               "that in very rare circumstances it may become ignition "
               "capable. When this occurs its duration must be limited so "
               "that the chance of an ignition is acceptably low, because of "
               "the low likelihood of coincidence, or of the situation arising "
               "before routine inspection and maintenance has identified any "
               "deterioration which could lead to ignition, and the necessary "
               "action taken."))
    b.append(p("Electrical protection should be set with its operating level "
               "as close to the normal operating levels as possible without "
               "producing a situation in which nuisance rips become a problem, "
               "and should cover overload, short circuit of the supply and "
               "earth faults. The electrical protection should be the same "
               "whatever the zone of risk but extreme care must be taken in "
               "respect of any circuits which enter Zone 0 or 20, due to the "
               "fact that the explosive atmosphere is assumed always to be "
               "present, and that significant duration of overloads, faults, "
               "short circuit faults or earth faults is least acceptable in "
               "these circumstances."))
    b.append(note("<b>Source quirk: ‘nuisance rips’.</b> The print reads "
                  "‘nuisance rips become a problem’, not ‘trips’; retained. "
                  "The following paragraph also keeps ‘it is this type of "
                  "faults which is most likely’ (plural ‘faults’ with singular "
                  "‘which is’)."))
    b.append(p("In addition to the above, electrical protection/isolation "
               "facilities which isolate all phase conductors and the neutral "
               "conductor (but not the potential equalization or protective "
               "conductor) should be present in non-hazardous areas to permit "
               "isolation of circuits entering hazardous areas. The neutral "
               "isolation by the switch isolating the phase conductors is "
               "recommended but not essential in these circumstances. The "
               "minimum requirement is for a separate link in the neutral "
               "conductor which may provide manual isolation. Where, however, "
               "additional isolation facilities in the hazardous area are "
               "required, the isolator must be protected by one of the "
               "concepts dealt with in Chapters 7 to 16 and the isolator must "
               "isolate the neutral at the same time as the phase conductors. "
               "This is because the neutral may be carrying fault current from "
               "other sources even when the phase conductors are isolated, and "
               "in these circumstances isolating the neutral with a manual "
               "link could produce an ignition-capable spark."))
    b.append(p("High voltage circuits, such as those used for supply of large "
               "rotating machines, should be treated in the same way as other "
               "supply circuits but isolation is particularly critical here "
               "and must be as rapid as possible. Isolation of earth faults is "
               "particularly important as it is this type of faults which is "
               "most likely to cause unprotected sparking and this isolation "
               "must be as near instantaneous as possible."))
    b.append(p("The foregoing requirements apply to all circuits entering the "
               "hazardous area except intrinsically safe circuits (Chapter 13) "
               "and non-incendive circuits (Chapter 14) where voltage and "
               "current in the circuit is so limited as to prevent "
               "ignition-capable sparking, but in these cases the electrical "
               "protection requirements generally apply to the apparatus in "
               "the non-hazardous area generating those circuits."))

    # ---- printed p.486: 17.3, lead-in and six numbered criteria.
    b.append(h3("17.3 Selection of apparatus", "17.3 Selection of apparatus"))
    b.append(p("Hazardous areas are a special type of location where, in "
               "addition to there being the normal environmental problems, "
               "explosive atmospheres can also occur. The basic selection "
               "criteria include the following."))
    b.append(ol([
        "The enclosure of apparatus must be sufficient to prevent the ingress "
        "of liquids and solids to an extent which could impair the operation "
        "of the apparatus by causing partial or full short circuits, corrosion "
        "or any other deterioration which would decrease the reliability of "
        "the apparatus or damage its safety features. For apparatus mounted "
        "outdoors this normally means an IP54 enclosure rating.",
        "The enclosure of the apparatus and any interior parts necessary to "
        "maintain reliable operation, and the protection concept must be "
        "proof against chemical attack from the materials present at its "
        "location.",
        "The rating of the apparatus must be sufficient to cover the operating "
        "conditions at its installation point (these ratings are those given "
        "by the protection concept which may include safety factors rather "
        "than the basic industrial ratings).",
        "The apparatus and its enclosure must be sufficiently robust to "
        "withstand any mechanical shock from impact, being dropped if portable "
        "apparatus, or vibration. The construction requirements cover normal "
        "dropping or impact, but not necessarily vibration, and locations "
        "where impact is particularly severe.",
        "The particular possibility of static formation on apparatus with "
        "plastics enclosures must be addressed.",
        "The thermite sparking risk must be taken into account when light "
        "metals or alloys are used in enclosure of the apparatus. This is "
        "only partially taken into account in construction requirements for "
        "the apparatus.",
    ]))
    b.append(h4("Light metal enclosures", "Light metal enclosures"))
    b.append(p("Particular care must be taken in the latter case of apparatus "
               "with light metal enclosure. The construction Standards for "
               "apparatus take account of magnesium content but there is still "
               "a residual risk due to the possible presence of aluminium or "
               "titanium and this is also present when aluminium sheathed "
               "cables are used. The risk principally comes from the "
               "possibility of the light metal being struck by oxidized "
               "(rusty) ferrous metal, when the resulting spark is often more "
               "intense than is the case when such contact is between two "
               "ferrous metals or ferrous metal and copper or brass. This "
               "results in a significant risk of ignition-capable sparking."))
    b.append(note("<b>Source quirk: ‘oxidized’.</b> The print uses the American "
                  "spelling ‘oxidized (rusty) ferrous metal’; retained as "
                  "printed."))
    b.append(p("The risk is negligible in Zone 2 as the likelihood of "
               "coincidence of spark and explosive atmosphere is so low as to "
               "be acceptable. In the case of Zone 22 the same is basically "
               "true but here there is the risk that a blow on the light metal "
               "enclosure may at the same time cause deposits of dust on the"))

    # ---- printed p.487: F1 -> F5.
    b.append(p("apparatus to form a cloud, producing a coincidence which is "
               "not acceptable. In Zone 22, therefore, apparatus with light "
               "metal enclosures should not be used if possible but in any "
               "event it should be either protected from impact by location or "
               "guarding or it should be constructed and mounted in such a way "
               "as to preclude dust deposits (e.g., by having no horizontal "
               "flat surfaces or by having a cover to prevent dust deposition). "
               "Apparatus with light metal enclosures intended for Zone 1 is "
               "not considered to be an unacceptable risk unless it is mounted "
               "in a location where the risk of mechanical impact is high, "
               "such as near roadways, or where operatives work with tools "
               "regularly. In these cases it should be avoided or provided "
               "with a guard to prevent impact directly on its enclosure. The "
               "requirement for Zone 21 is the same as that above for Zone 22 "
               "impact. In this case the dust problem is principally one of "
               "clouds rather than layers (as in the case of Zone 22) but the "
               "risk of coincidence is no greater. In the case of Zone 0 and "
               "20 the explosive atmosphere is considered to always be present "
               "and no impact is acceptable. Unless freedom from any impact "
               "can be guaranteed apparatus with light metal enclosures should "
               "not be used in Zone 0 or 20."))
    b.append(h3("17.3.1 Selection in respect of gases, vapours and mists",
                "17.3.1 Selection in respect of gases, vapours and mists"))
    b.append(p("Apparatus for gas, vapour and mist risks is defined for surface "
               "industry as Group II apparatus (Group I apparatus being for "
               "underground use in coal mines and other mines where flammable "
               "gas may be present). If the apparatus does not produce sparks "
               "to which the explosive atmosphere has access (i.e., is "
               "protected by pressurization ‘p’ (Chapter 11), powder filling "
               "‘q’ (Chapter 9), oil immersion ‘o’ (Chapter 9), encapsulation "
               "‘m’ (Chapter 9), increased safety ‘e’ (Chapter 12) or Type ‘N’ "
               "in its non-sparking context (Chapter 14), selection of Group II "
               "apparatus is sufficient, subject to surface temperature "
               "considerations."))
    b.append(note("<b>Source quirks: ‘Group II apparatus’ and the unclosed "
                  "parenthesis.</b> The print reads ‘Group II apparatus’ and "
                  "‘Group I apparatus’ with Roman numerals (not the digit 1), "
                  "and the paragraph ends ‘… surface temperature "
                  "considerations.’ without ever closing the parenthesis "
                  "opened before ‘i.e.’; both retained."))
    b.append(h4("Ignition by sparks and arcs", "Ignition by sparks and arcs"))
    b.append(p("Where sparks occur to which the explosive atmosphere does have "
               "access they will either be rendered as non-ignition capable "
               "using intrinsic safety ‘i’ (Chapter 13) or the energy limited "
               "concept in Type ‘N’ (Chapter 14) or they will be prevented from "
               "causing an explosion even though they are capable of causing "
               "an ignition by utilization of the flameproof enclosure concept "
               "‘d’ (Chapter 10) or non-incendive component concept in Type ‘N’ "
               "(Chapter 14). In these cases the degree of incendivity varies "
               "as the ignition capability of gas, vapour, mist and air "
               "mixtures varies and this allows variation in the severity of "
               "the limitation on apparatus construction and such apparatus is "
               "divided into three Sub-Groups IIA, IIB, and IIC, depending "
               "upon their ignition capability. Gases and vapours are "
               "associated with these sub-divisions to permit choice of the "
               "most appropriate according to their ignition performance. It "
               "will be remembered that energy limitation, such"))

    # ---- printed p.488: G1 -> G8 and the MIC/MESG display.
    b.append(p("as used in intrinsic safety and the Type ‘N’ concept is based "
               "upon the use of a test apparatus as shown in Fig. 13.2 in "
               "Chapter 13 and the explosion prevention technique used in "
               "flameproof enclosure and the Type ‘N’ concept upon a test "
               "apparatus as shown in Fig. 8.1 in Chapter 8. Any particular "
               "gas or vapour can be measured in these test devices to "
               "determine its Minimum Ignition Current (MIC) which is relevant "
               "to ignition capability of the spark and its Maximum "
               "Experimental Safe Gap (MESG) which is relevant to the "
               "performance of the spark enclosure in preventing transmission "
               "of the ignition caused by the spark out of the enclosure. "
               "Fortunately these two facets of the performance of a gas or "
               "vapour are related and so a common approach is possible. Thus "
               "gases, vapours and mists are related to the apparatus sub-group "
               "on the following basis of their MIC (normally quoted as a "
               "fraction of the MIC of methane) and their MESG (normally "
               "quoted in mm) as follows:"))
    b.append(eq("Sub-group IIA&#160;&#160;&#160;MIC > 0.8<br>"
                "&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;"
                "&#160;&#160;&#160;MESG > 0.9 mm<br>"
                "Sub-group IIB&#160;&#160;&#160;MIC ≤ 0.45 and ≥ 0.8<br>"
                "&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;"
                "&#160;&#160;&#160;MESG ≤ 0.5 mm and ≥ 0.9 mm<br>"
                "Sub-group IIC&#160;&#160;&#160;MIC ≥ 0.45<br>"
                "&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;"
                "&#160;&#160;&#160;MESG ≥ 0.5 mm"))
    b.append(note("<b>Source quirk: inverted Sub-group IIB bounds.</b> The "
                  "print shows ‘MIC ≤ 0.45 and ≥ 0.8’ and ‘MESG ≤ 0.5 mm and ≥ "
                  "0.9 mm’. The bounds appear inverted but are reproduced "
                  "exactly as printed."))
    b.append(p("It is normally only necessary to measure one or other of these "
               "parameters to define the sub-group with which the gas or "
               "vapour is associated unless the parameter measured identifies "
               "the gas as being near to the limit as follows:"))
    b.append(p("If the MIC measures between 0.8 and 0.9 then the sub-group is "
               "determined by the MESG and is not necessarily IIA."))
    b.append(p("If the MIC measures between 0.45 and 0.5 then the sub-group is "
               "determined by the MESG and is not necessarily IIB."))
    b.append(p("If the MESG measures between 0.5 and 0.55 then the sub-group is "
               "determined by the MIC and is not necessarily IIB."))
    b.append(p("The above situations are based upon the knowledge of the "
               "performance of gases and vapours measured to date and so large "
               "is that number that there is confidence that these are the "
               "only situations where additional measurements of the other "
               "parameter are necessary."))
    b.append(p("Many gases and vapours have been identified both nationally "
               "and internationally to be associated with particular subgroups "
               "by measurement or by assessment on the basis of the similarity "
               "of their chemical structures to other, gases and vapours whose "
               "associated sub-group has been determined by measurement. These "
               "are given in Table 4.3 in Chapter 4. No work on mists formed by "
               "liquids below their boiling points has been recorded and it is "
               "fair to assume that, because of their greater particle size, "
               "they will be less ignitable than vapours formed by the same "
               "liquid if it is raised to above its boiling point. The "
               "sub-grouping chosen for a mist should therefore be the same as "
               "that for the vapour which would be formed if"))
    b.append(note("<b>Source quirks: ‘particular subgroups’ and ‘other, gases "
                  "and vapours’.</b> The print uses the one-word ‘subgroups’ "
                  "here (elsewhere ‘sub-group’) and puts a comma after "
                  "‘other’; both retained."))

    # ---- printed p.489: H1 -> H6, T-class display, final paragraph.
    b.append(p("the mist-producing liquid were raised to above its boiling "
               "point. While this is probably onerous no relaxation can be "
               "made unless it can be shown to be valid by measurement of the "
               "ignition temperature of a particular mist with the smallest "
               "particle size possible in the particular case, and it is "
               "unlikely that this can be reliably done."))
    b.append(p("The grouping system in the USA which seeks to perform the same "
               "function as sub-grouping in Europe is shown in Table 8.1 in "
               "Chapter 8. It is different to that used in Europe in that a "
               "single letter is used, hydrogen and acetylene are separated "
               "and carbon disulphide in not addressed. If USA apparatus is "
               "otherwise acceptable the USA grouping system should be used "
               "for its selection but, as confusion might result, it is not "
               "recommended that such apparatus is used unless all involved in "
               "the selection, installation and maintenance of apparatus are "
               "fully aware of the system and its relationship with the "
               "European system. In any event, the implementation of the new "
               "EU Directive 94/9/EC² is likely to cause the use of such "
               "equipment to be phased out unless it complies with the "
               "requirements of European Standards, using the European "
               "sub-grouping system."))
    b.append(note("<b>Source quirks in the USA-grouping paragraph.</b> The "
                  "print reads ‘carbon disulphide in not addressed’ (‘in’, not "
                  "‘is’), ‘It is different to that used in Europe’, and ‘EU "
                  "Directive 94/9/EC²’ with its superscript reference marker; "
                  "all three retained."))
    b.append(h4("Ignition by hot surfaces", "Ignition by hot surfaces"))
    b.append(p("Apparatus constructed in accordance with all of the protection "
               "concepts described in Chapters 7 to 14 is classified as to the "
               "maximum temperature reached by any surface to which an "
               "explosive atmosphere has access and any resulting ignition "
               "would result in an explosion which was not contained by the "
               "apparatus. The surface temperature classification system is "
               "described in Chapter 8 and apparatus is awarded a temperature "
               "class of T1 to T6 in Europe depending upon its maximum surface "
               "temperature. Table 4.3 in Chapter 4 specifies the maximum "
               "surface temperature class required for apparatus which is "
               "intended for use in particular gases and vapours based upon "
               "the measured maximum ignition temperature of the gas or vapour. "
               "A mist will adopt the same maximum temperature class, as would "
               "a vapour formed by raising the temperature of the liquid "
               "forming the mist to above its boiling point. Apparatus of a "
               "more limiting temperature class may be used in particular "
               "gases, vapours and mists as follows:"))
    b.append(eq("T6 – only apparatus of T6 classification may be used<br>"
                "T5 – apparatus of T5 and T6 classifications may be used<br>"
                "T4 – apparatus of T4, T5 and T6 classifications may be used<br>"
                "T3 – apparatus of T6, T5, T4 and T3 classifications may be used<br>"
                "T2 – apparatus of T6, T5, T4, T3 and T2 classifications may be used<br>"
                "T1 – apparatus of T6, T5, T4, T3, T2 and T1 classifications may be used"))
    b.append(note("<b>Source quirk: descending temperature-class order.</b> In "
                  "every line the print enumerates the classes in descending "
                  "T-number order T6, T5, T4, T3, T2, T1, including the T3–T1 "
                  "lines; retained."))
    b.append(p("In some circumstances apparatus can be shown to satisfy the "
               "requirements of a particular protection concept at ambient "
               "temperatures well in excess of the 40 °C ambient normally used "
               "for temperature classification (e.g., resistance thermometers, "
               "thermocouples). In such cases the temperature classification "
               "is sometimes based upon the maximum ambient which is possible "
               "and this will be identified by the apparatus supplier. "
               "However,"))
    b.append(note("<b>Source quirk: ‘40 °C’ and the module seam.</b> The print "
                  "has a space in ‘40 °C’; retained. This final paragraph ends "
                  "exactly at ‘However,’; its continuation, ‘a surface "
                  "temperature classification may be given…’, opens the next "
                  "module."))
    return "".join(b)
