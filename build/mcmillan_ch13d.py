# -*- coding: utf-8 -*-
"""Chapter 13, module D - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 379-394 (PDF pp. 400-415).

The chunk begins mid-paragraph in 13.9.2 (composite spacings, Table 13.8),
continues through 13.9.3 (earth conductors and connections), 13.9.4
(encapsulation), 13.10 (infallible components), 13.10.1 (infallible
transformers and the five unnumbered construction subheadings), 13.10.2
(damping windings) and ends mid-sentence in 13.10.3 (current limiting
resistors). Figures 13.19-13.27 and Tables 13.8-13.12 appear at their printed
positions. The chapter shell owns the chapter h2, the printed references, the
glossary, the source-quirk note and the copyright.

The English follows the authoritative page render verbatim, including the
printed quirks (the unclosed quote in 'a 'Type 2b transformer, the duplicated
'manufacturing tolerances', the digit-one transformer type names, the mixed
current/voltage spacing, the American spellings, the singular 'Detail ... are
shown', the missing terminal full stops in the figure captions and the
mid-sentence page breaks). The Vietnamese translates the intended meaning.
Bilingual note boxes flag every divergence catalogued in survey D section 6.
This is an unofficial study translation; the source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, eq, note, table, fig
import mcmillanfig13_d as FD
import mcmillan_tbl13_5_8 as T2
import mcmillan_tbl13_9_12 as T3


def body_vi():
    b = []

    # ------------------------------------------------------------------
    # BLOCK D-379 / printed 379 / PDF 400: Fig. 13.19 + Table 13.8, no prose.
    # D-379.1, D-379.2, D-379.3, D-379.4, D-379.12, quirk B12.
    b.append(fig(19, FD.fig_f1319()))
    b.append(note("<b>Lưu ý về Hình 13.19 và các lỗi lớp văn bản OCR.</b> Dòng tiêu đề "
                  "chạy trên bản in có 'intrinsic safety ‘i’'; lớp OCR đọc nhầm thành "
                  "'intrinsic safety T’', và trên bản in 385 đọc 'intrinsic safely ?' "
                  "thay vì 'intrinsic safety ‘i’ 385'. Các nhãn trong hình bị OCR đọc là "
                  "'e central metal', 'd. d, , 0; = creepage distance' và gộp 'is not "
                  "electrically connected' vào 'Exposed HT of r,b >d'; trang render cho "
                  "các nhãn đúng là 'The central metal', 'd, d₁, d₂ = creepage distance' "
                  "và 'Exposed HT of r,b > d' (có dấu cách quanh dấu >). Các ký hiệu ≥3, "
                  "<3, ≥1 và chú thích 'Exposed HT of r,b > d' được giữ nguyên dù bản in "
                  "không giải thích chúng."))
    # D-379.10, D-379.14, D-379.15, quirk B2.
    b.append(table(T2.HEAD138_VI, T2.ROWS138_VI, T2.CAPTION138_VI))
    if T2.NOTE138_VI:
        b.append(note(T2.NOTE138_VI))
    b.append(note("<b>Lưu ý về Bảng 13.8.</b> Cột điện áp in '10V' ... '1575V' rồi "
                  "'3.3KV', '4.7KV', '9.5KV', '15.6KV' (chữ K hoa, không dấu cách), "
                  "trong khi lớp OCR đọc '1ov', 'lO0OV', '4.7Kv' và chèn dấu cách trong "
                  "'1 .o' / '1 75'. Các ô CTI in literal là 'Note 1', 'Note 2' và 'N/A'; "
                  "hai tiêu đề danh mục dùng dấu nháy đơn kiểu cong ‘ia’ và ‘ib’ (OCR đọc "
                  "thành dấu nháy thẳng). Chú thích in 'CTG = Coating'. Tất cả được giữ "
                  "theo bản in; bản tiếng Việt dịch nhãn chữ nhưng giữ số liệu và 'N/A'."))

    # ------------------------------------------------------------------
    # BLOCK D-380 / printed 380 / PDF 401: D1, then Figs 13.20 and 13.21.
    # D1 — continuation of the 13.9.2 paragraph from printed 378.
    b.append(p("các dây dẫn sẽ là một lỗi có thể đếm được và Bảng 13.7 cho các giá trị "
               "mà tại đó chúng sẽ không bị hỏng. Nếu những giá trị này không đạt được, "
               "bất kỳ sự hỏng nào như vậy dẫn đến tình trạng kém an toàn hơn sẽ được coi "
               "là lỗi không đếm được, và được áp dụng phù hợp để tạo ra điều kiện xấu "
               "nhất cả trong vận hành bình thường lẫn trong kịch bản lỗi có thể đếm "
               "thích hợp. Nếu khoảng cách giữa hai dây dẫn bao gồm hỗn hợp của khoảng hở "
               "và/hoặc khoảng cách tách, có thể cộng các khoảng cách lại, với điều kiện "
               "tất cả các khoảng cách thành phần cần cộng đều ít nhất bằng một phần ba "
               "mức tối thiểu cho trong Bảng 13.7 và 13.8 cho loại khoảng cách cần thiết "
               "nếu loại khoảng cách đó tồn tại riêng lẻ ở điện áp giữa hai dây dẫn đang "
               "xét. Phép cộng được quy về một trong ba khả năng (khoảng hở, khoảng tách "
               "qua lớp bọc kín, hoặc khoảng tách qua cách điện rắn) bằng cách dùng các "
               "hệ số nhân quy định trong Bảng 13.9 (dựa trên Hình 13.20) cho điện áp giữa "
               "các dây dẫn. Khi một phần của chiều dài đường rò được phủ lớp phủ bảo vệ, "
               "đường rò tổ hợp được tính theo cách rất giống nhau nhưng dùng các hệ số "
               "nhân trong Bảng 13.10, dựa trên Hình 13.21. Trong trường hợp đường rò, "
               "không áp dụng mức tối thiểu cho cả hai thành phần. Các khoảng hở, chiều "
               "dài đường rò và khoảng tách cho trong Bảng 13.8 áp dụng giữa các bộ phận "
               "dẫn điện trong bất kỳ mạch an toàn nội tại nào mà"))
    # D1 quirk: D-379.5, D-379.12, D-379.21, D-379.37 (soft hyphens).
    b.append(note("<b>Lưu ý về các vết gạch nối mềm trong lớp OCR.</b> Lớp văn bản OCR chèn "
                  "ký tự gạch nối mềm cuối dòng trong các từ như 'operation', 'component', "
                  "'separation', 'manufacturing', 'clearances' và 'connection'; trang render "
                  "cho các từ nguyên vẹn. Bản dịch dùng các từ đầy đủ."))
    # D-380.1 / D-380.6 / D-380.7 — Fig. 13.20 and Fig. 13.21 OCR flattening.
    b.append(fig(20, FD.fig_f1320()))
    b.append(note("<b>Lưu ý về Hình 13.20.</b> Lớp OCR dàn phẳng hình vẽ thành một danh "
                  "sách từ và để lại một dấu gạch chéo rời rạc; trang render cho các nhãn "
                  "riêng biệt 'Solid insulation', 'C', 'B', 'A', 'Encapsulant', 'Conductor' "
                  "và chú thích ba dòng A = clearance, B = separation through casting "
                  "compound, C = separation through solid insulation. Không có văn bản nào "
                  "tương ứng với dấu gạch chéo rời rạc đó."))
    b.append(fig(21, FD.fig_f1321()))
    b.append(note("<b>Lưu ý về nhãn Hình 13.21.</b> Lớp OCR đọc nhãn bên phải là 'insulation' "
                  "thường; trang render in 'Insulation' với chữ I hoa. Chú thích hai dòng "
                  "định nghĩa A = creepage under coating và B = creepage in air được giữ "
                  "nguyên."))

    # ------------------------------------------------------------------
    # BLOCK D-381 / printed 381 / PDF 402: Tables 13.9 and 13.10 only.
    # D-381.9, D-381.11, D-381.12, D-381.13, quirk B3.
    b.append(table(T3.HEAD139_VI, T3.ROWS139_VI, T3.CAPTION139_VI))
    if T3.NOTE139_VI:
        b.append(note(T3.NOTE139_VI))
    b.append(table(T3.HEAD1310_VI, T3.ROWS1310_VI, T3.CAPTION1310_VI))
    if T3.NOTE1310_VI:
        b.append(note(T3.NOTE1310_VI))
    b.append(note("<b>Lưu ý về Bảng 13.9 và Bảng 13.10.</b> Lớp OCR đọc sai các dấu bất "
                  "đẳng thức thành 'o< u 510', '10< U 130', '30~ U 51575' và 'O< U 51575', "
                  "đồng thời bỏ dấu hai chấm ở 'Ref Separation Through CC' và 'Ref "
                  "Separation Through SI'; trang render cho '0< U ≤10', '10< U ≤30', "
                  "'30< U ≤1575', '0< U ≤1575' và 'Ref: ...'. Bảng 13.9 dùng từ 'Volts' "
                  "trong tiêu đề còn Bảng 13.10 dùng '(V)'; ghi chú của Bảng 13.9 in "
                  "'1575V' không dấu cách nhưng '15.6 KV' có dấu cách và chữ K hoa. Các "
                  "dạng này được giữ nguyên."))

    # ------------------------------------------------------------------
    # BLOCK D-382 / printed 382 / PDF 403: D2, D3, D4, heading 13.9.3, D6.
    # D2 — continuation of D1.
    b.append(p("cần phải là lỗi có thể đếm được, chẳng hạn như qua các đầu nối của một "
               "diode và giữa bất kỳ hai mạch an toàn nội tại riêng biệt nào mà việc liên "
               "kết ở mức lỗi có thể đếm đã được đánh giá và cho thấy không tạo ra tình "
               "trạng không an toàn. Ngoài ra, các số liệu áp dụng giữa một mạch an toàn nội "
               "tại và một mạch không an toàn nội tại nếu việc thêm mạch không an toàn nội "
               "tại không gây tình trạng không an toàn khi nó trở thành một phần của mạch "
               "an toàn nội tại. Điều này xảy ra, điển hình, trong thiết bị ‘ia’, khi một "
               "lỗi như vậy ở mức lỗi có thể đếm chỉ ngắn mạch một phần của điện trở hạn "
               "dòng, và do đó được chấp nhận vì hệ số an toàn thấp hơn được phép sau lỗi "
               "có thể đếm thứ hai, và giữa một dây dẫn của mạch an toàn nội tại và bất kỳ "
               "kim loại nào được nối đất."))
    # D3 — voltage derivation; quirk B8.
    b.append(p("Các điện áp dùng để áp dụng Bảng 13.7 và 13.8 là các điện áp đỉnh xuất "
               "hiện giữa hai dây dẫn. Chúng được suy ra như sau, thứ nhất, trong các phần "
               "của cùng một mạch, điện áp là điện áp đỉnh cực đại có thể đo giữa hai phần "
               "của mạch nếu cả hai điện áp đều đến từ cùng một nguồn, hoặc là tổng số học "
               "của hai điện áp đỉnh nếu chúng đến từ các nguồn khác nhau, trừ khi một trong "
               "các điện áp này nhỏ hơn 20 phần trăm điện áp kia thì có thể bỏ qua. Đối với "
               "điện áp một chiều, cực tính được tính đến nhưng các khoảng cách cũng được "
               "yêu cầu phải chấp nhận được khi điện áp thấp hơn trong hai điện áp không có "
               "mặt. Trong mạch xoay chiều, người ta chọn các giá trị số để loại bỏ sự cần "
               "thiết phải xác định góc pha. Trong những trường hợp này rõ ràng là tình "
               "huống khi một điện áp không có mặt thì ít khắt khe hơn khi cả hai đều có "
               "mặt. Thứ hai, trong các mạch riêng biệt, điện áp luôn là tổng số học của hai "
               "điện áp, đối với cả xoay chiều và một chiều, trừ khi một điện áp nhỏ hơn 20 "
               "phần trăm điện áp kia vì trong trường hợp này cực tính của nguồn một chiều "
               "không thể được đảm bảo."))
    b.append(note("<b>Lưu ý về câu khó hiểu trong bản in.</b> Bản in viết 'In these cases "
                  "obviously the situation when one voltage is absent it is less onerous "
                  "than when both are present.' — cấu trúc này được giữ nguyên trong bản "
                  "tiếng Anh; bản tiếng Việt dịch theo ý định là tình huống khi một điện áp "
                  "không có mặt thì ít khắt khe hơn. Quy tắc 'less than 20 per cent' và việc "
                  "chọn giá trị số để khỏi xác định góc pha cũng được giữ nguyên."))
    # D4 — voltages, secured conductors; quirk B7, OCR 16.
    b.append(p("Các điện áp dùng là giá trị đỉnh cực đại có thể xảy ra trong một thiết bị ở "
               "điều kiện bình thường hoặc điều kiện lỗi được chấp nhận khi bất kỳ nguồn "
               "cấp điện nào ở giá trị khai báo cực đại của chúng (Uₘ hoặc Uᵢ – xem BS/EN "
               "50020), ngoại trừ việc bất kỳ nguồn lưới điện nào sẽ được xét mà không cộng "
               "thêm dung sai cấp điện của chúng. Các điện áp cao hơn tạm thời (chẳng hạn "
               "như những điện áp xảy ra trong quá trình cầu chì hoạt động và vì vậy là "
               "hiện tượng một lần) được bỏ qua, nhưng nếu một điện áp tạm thời có thể lặp "
               "lại với một mức độ đều đặn nhất định thì phải tính đến nó. Ngoài ra, bất kỳ "
               "dây dẫn nào có trong thiết bị cần được cố định nếu được cách điện, để ngăn "
               "chuyển động gây mòn hoặc cắt lớp cách điện, và phải được dịch chuyển xa nhất "
               "có thể để tạo ra khoảng cách tối thiểu trước khi đo khoảng cách. Người ta "
               "chấp nhận rằng dung sai chế tạo có thể làm giảm thêm các khoảng cách vì dung "
               "sai chế tạo, đặc biệt trong trường hợp bản mạch in. Với điều kiện các dung "
               "sai này nhỏ hơn 10 phần trăm, chúng có thể được bỏ qua và lấy số liệu danh "
               "định của nhà sản xuất."))
    b.append(note("<b>Lưu ý về ký hiệu và cách diễn đạt trong bản in (đoạn điện áp).</b> Lớp "
                  "OCR đọc '(U, or Ui - see BS/EN' nhưng trang render in '(Uₘ or Uᵢ – see "
                  "BS/EN ...)' với chỉ số dưới và dấu gạch ngang kiểu en. Cụm 'manufacturing "
                  "tolerances' bị lặp trong câu 'It is accepted that manufacturing "
                  "tolerances can further reduce spacings because of manufacturing "
                  "tolerances' và được giữ nguyên trong bản tiếng Anh; bản tiếng Việt dịch "
                  "theo ý định."))
    # D5 — heading 13.9.3.
    b.append(h3("13.9.3 Dây dẫn và kết nối đất (bao gồm cả cọc nối)",
                "13.9.3 Earth conductors and connections (including terminals)"))
    # D6 — first part, continues on printed 383.
    b.append(p("Việc nối đất thường được dùng trong an toàn nội tại như một phương pháp "
               "đảm bảo sự tách biệt của các dây dẫn và các bộ phận mà nếu tiếp xúc với "
               "nhau sẽ làm hỏng an toàn nội tại"))

    # ------------------------------------------------------------------
    # BLOCK D-383 / printed 383 / PDF 404: D7-D11.
    # D7 — continuation of D6.
    b.append(p("sẽ tiếp xúc với nhau. Sự cần thiết của việc nối đất bao gồm việc phải nối "
               "đất các dây dẫn, màn chắn, vỏ bọc và các rào an toàn (những thứ này được đề "
               "cập sau trong chương này)."))
    # D8.
    b.append(p("Các dây dẫn bên trong thiết bị nối các bộ phận với đất cần dùng phương pháp "
               "nối không bị hỏng (không thể sai hỏng). Bản thân các dây dẫn cũng phải có "
               "khả năng mang, không bị quá nhiệt hoặc hư hỏng, dòng điện cực đại có thể "
               "chảy qua chúng cả trong vận hành bình thường lẫn trong các điều kiện lỗi có "
               "thể xảy ra."))
    # D9.
    b.append(p("Các đầu nối mang những kết nối nối đất như vậy cần được sắp xếp sao cho "
               "không có khả năng bị tuột ra. Vì các kết nối phích cắm và ổ cắm thông thường "
               "được coi là lỗi có thể đếm được, nên cần có sự dự phòng trong đầu nối. Điều "
               "này dẫn đến yêu cầu hai chân nối cho ‘ib’ và ba chân cho ‘ia’ được nối song "
               "song. Hình 13.14 cho thấy cách đạt được điều đó, bao gồm bố trí cần thiết "
               "trong các thiết bị như đầu nối cạnh, có thể bị tuột ra ở một góc. Các kết "
               "nối vĩnh cửu tới thiết bị cần nối đất để dẫn các kết nối đất đó qua phích "
               "cắm và ổ cắm cần tách biệt nhau vì lý do tương tự, hoặc phải sao cho chúng "
               "được coi là không bị hỏng. Loại kết nối vĩnh cửu sau được đề cập sau trong "
               "chương này."))
    # D10.
    b.append(p("Các cọc nối đặc biệt cần được xem xét kỹ nếu được giả định là không bị hỏng "
               "ở trạng thái hở mạch và cần đáp ứng các yêu cầu sau:"))
    # D11 — numbered list 1-7.
    b.append(p("1. Chúng phải kẹp chặt hiệu quả dây dẫn được nối để ngăn nó trượt khỏi vị trí "
               "dự định, ngay cả với những thay đổi nhiệt độ dự kiến (thường −20 °C đến "
               "+40 °C)."))
    b.append(p("2. Chúng phải duy trì kết nối điện hiệu quả của dây dẫn trong suốt dải nhiệt "
               "độ dự kiến."))
    b.append(p("3. Trong trường hợp dùng dây dẫn nhiều sợi mà không được uốn đầu trước vào "
               "một ống đầu dây, phải có một bản kẹp bổ sung trong cơ cấu kẹp (ví dụ, giữa "
               "vít và dây dẫn) để đảm bảo kẹp chặt đúng cách tất cả các sợi."))
    b.append(p("4. Các cọc nối dự định cho dây dẫn có tiết diện tối đa 4mm² hoặc nhỏ hơn phải "
               "có khả năng kẹp chặt hiệu quả các tiết diện nhỏ hơn mức tối đa mà chúng được "
               "thiết kế. Có lẽ không cần thiết phải bao phủ các tiết diện nhỏ hơn "
               "0.000962mm², đây là mức nhỏ nhất mà tại đó dòng điện tối đa cho phép cho "
               "phân loại nhiệt độ được cho (xem Bảng 13.4)."))
    b.append(p("5. Không được có cạnh sắc trên các cọc nối có thể làm hỏng dây dẫn được nối."))
    b.append(p("6. Các cọc nối không được xoắn hoặc bị biến dạng khi áp mô-men siết vít "
               "bình thường."))
    b.append(p("7. Việc truyền áp lực tới các bộ phận đảm bảo tiếp xúc không được đi qua bất "
               "kỳ vật liệu cách điện nào."))
    # Quirks 18, 19.
    b.append(note("<b>Lưu ý về đơn vị và nhiệt độ trong danh sách cọc nối.</b> Bản in ghi "
                  "'(normally −20 °C to +40 °C)' với dấu trừ và dấu cách trước °C; lớp OCR "
                  "đọc '-20 \"C to +40 \"C'. Bản in ghi '4mm²' và '0.000962mm²' không dấu "
                  "cách, với số 2 dạng mũ; OCR đọc '4mm2' và '0.000962 mm2'. Các dạng in "
                  "được giữ nguyên trong bản tiếng Anh; bản tiếng Việt dùng '−20 °C đến "
                  "+40 °C', '4mm²' và '0.000962mm²'."))

    # ------------------------------------------------------------------
    # BLOCK D-384 / printed 384 / PDF 405: D12, heading 13.9.4, D14-D20.
    # D12.
    b.append(p("Một cách dễ dàng để đáp ứng tất cả các yêu cầu này là chọn cọc nối cho mục "
               "đích này, và cho bất kỳ mục đích nào khác mà cần sự chắc chắn chống tuột "
               "(không thể sai hỏng), từ các dòng sản phẩm đáp ứng yêu cầu của an toàn tăng "
               "cường ‘e’ (BS/EN 50019) (xem Chương 12)."))
    # Quirk 20.
    b.append(note("<b>Lưu ý về dấu nháy đơn kiểu cong trong bản in.</b> Bản in viết "
                  "'increased safety ‘e’ (BS/EN 50019)'; lớp OCR đọc nhầm thành 'increased "
                  "safety 'er (BS/EN 50019)' với chữ r thừa. Dấu nháy cong được giữ nguyên "
                  "trong bản tiếng Anh."))
    # D13 — heading 13.9.4.
    b.append(h3("13.9.4 Bọc kín", "13.9.4 Encapsulation"))
    # D14.
    b.append(p("Bọc kín có thể được dùng vì hai lý do. Có thể cần tăng diện tích bề mặt của "
               "một linh kiện trong thiết bị an toàn nội tại để hạ nhiệt độ bề mặt khi năng "
               "lượng bên trong lớp bọc kín là an toàn nội tại, hoặc có thể dùng nó để loại "
               "trừ bầu khí quyển nổ khỏi một linh kiện từ một mạch an toàn nội tại mà mức "
               "năng lượng lại có khả năng gây cháy (ví dụ, kết nối giữa một cuộn cảm và các "
               "linh kiện triệt tiêu của nó). Yêu cầu tối thiểu cho lớp bọc kín là như nhau "
               "trong cả hai trường hợp nhưng, trong trường hợp hạn chế nhiệt độ, lượng và "
               "độ dày của lớp bọc kín phải đạt được sự hạn chế nhiệt độ cần thiết nếu điều "
               "đó đòi hỏi lớp bọc dày hơn."))
    b.append(note("<b>Lưu ý về chữ 'from' bị lặp trong bản in.</b> Bản in viết 'to exclude an "
                  "explosive atmosphere from a component from an intrinsically safe "
                  "circuit' — chữ 'from' lặp lại trong nguyên bản và được giữ nguyên trong "
                  "bản tiếng Anh; bản tiếng Việt dịch theo ý định."))
    # D15.
    b.append(p("Lớp bọc kín phải đáp ứng các yêu cầu sau trong cả thiết bị an toàn nội tại "
               "lẫn thiết bị liên kết, dù trong trường hợp sau lớp bọc kín chỉ được dùng để "
               "duy trì khoảng cách. Thứ nhất, nó phải bám dính vào các linh kiện và/hoặc mạch "
               "được bọc kín tại vị trí chúng đi ra khỏi lớp bọc. Điều này cần thiết vì chiều "
               "dài đường rò không được đo bên trong lớp bọc kín với giả định rằng chất bẩn "
               "không thể xâm nhập, và nếu lớp bọc kín không bám vào các bộ phận được bọc "
               "trong những trường hợp đó thì chất bẩn có thể xâm nhập, điều này không được "
               "chấp nhận."))
    # D16.
    b.append(p("Thứ hai, khi các dây dẫn trần đi ra khỏi lớp bọc kín, lớp bọc kín phải có CTI "
               "cần thiết để bảo vệ chiều dài đường rò trên bề mặt của nó."))
    # D17.
    b.append(p("Thứ ba, lớp bọc kín cũng phải có quy cách dải nhiệt độ hoạt động đảm bảo nó "
               "không bị hư hỏng bởi nhiệt độ đạt được trong quá trình hoạt động ở cả điều "
               "kiện bình thường và điều kiện lỗi có thể xảy ra, trong dải nhiệt độ mà thiết "
               "bị được thiết kế (thường −20 °C đến +40 °C). Ngoài ra, nếu thử nghiệm cho "
               "thấy lớp bọc kín không bị hư hỏng trong dải nhiệt độ này thì nó vẫn được chấp "
               "nhận, ngay cả khi nó được vận hành ngoài quy cách của nó."))
    # D18.
    b.append(p("Thứ tư, khi bề mặt của lớp bọc kín tạo thành một phần của vỏ bọc ngoài của "
               "thiết bị, nó phải là lớp bọc cứng (cứng rắn), chẳng hạn như nhựa epoxy."))
    # D19.
    b.append(p("Thứ năm, khi lớp bọc kín không có vỏ bọc, độ dày tối thiểu của nó giữa bất kỳ "
               "linh kiện hoặc cụm linh kiện được bọc và bề mặt tự do của nó (xem Hình 13.22) "
               "phải bằng một nửa mức tối thiểu quy định cho điện áp của linh kiện hoặc cụm "
               "đó, với mức tối thiểu là 1 mm."))
    # D20.
    b.append(p("Cuối cùng, khi lớp bọc kín nằm bên trong một vỏ bọc, không có độ dày tối "
               "thiểu của lớp bọc nếu vỏ bọc bằng vật liệu cách điện, nhưng nếu vỏ bọc bằng "
               "vật liệu dẫn điện thì độ dày được xác định bởi mức cần thiết để ngăn bất kỳ "
               "kết nối đất nào có thể làm hỏng an toàn nội tại."))

    # ------------------------------------------------------------------
    # BLOCK D-385 / printed 385 / PDF 406: Fig. 13.22, heading 13.10, D22.
    # D-385.23, quirks B13, B16.
    b.append(fig(22, FD.fig_f1322()))
    b.append(note("<b>Lưu ý về chú thích Hình 13.22.</b> Lớp OCR dàn phẳng hình vẽ thành danh "
                  "sách từ lộn xộn ('penterate', 'EncaDsulant', dấu gạch chéo rời rạc); trang "
                  "render cho bốn mặt cắt với các nhãn riêng 'Free surface', 'Encapsulant "
                  "(Note 1)', 'Enclosure (Note 2)' và 'Encapsulant (no minimum thickness) "
                  "(Note 3)', kèm nhãn ghép 'Enclosure (Note 2 &amp; 3)'. Ghi chú (2) in "
                  "'Metal has no minimum thickness but insulating material must conform to "
                  "the thickness for separation purposes (Table 13.7)' được giữ nguyên dù "
                  "có vẻ đảo ngược kỳ vọng; chú thích kết thúc bằng 'intrinsic safety' không "
                  "có dấu chấm cuối, như bản in."))
    # D21 — heading 13.10.
    b.append(h3("13.10 Linh kiện, cụm và phần tử cấu tạo không thể hỏng",
                "13.10 Infallible components, assemblies and construction elements"))
    # D22 — first part, continues on printed 386.
    b.append(p("Như hiện đã rõ, an toàn nội tại bao gồm trong đánh giá của nó các hỏng hóc "
               "của linh kiện và các phần tử mạch khác theo hai cách, khi những hỏng hóc đó "
               "làm giảm độ an toàn. Những hỏng hóc đạt đến một mức độ hoàn hảo cụ thể về cấu "
               "tạo được coi là chỉ hỏng như một phần của số lỗi hạn chế và những hỏng hóc "
               "không"))

    # ------------------------------------------------------------------
    # BLOCK D-386 / printed 386 / PDF 407: D23-D26, heading 13.10.1, D28,
    # heading "Mains transformer construction", D30.
    # D23 — continuation of D22.
    b.append(p("đạt đến mức đó được coi là hỏng trong mọi trường hợp nếu sự hỏng đó làm cho "
               "mạch có khả năng gây cháy cao hơn. Có một mức thứ ba cần xem xét, đó là mức "
               "mà cấu tạo và định mức có trình độ cao đến mức có thể bỏ qua hỏng hóc. Ở "
               "linh kiện, cụm linh kiện và các phần tử kết nối, mức độ hoàn hảo này xứng "
               "đáng được trao danh hiệu linh kiện, cụm hoặc kết nối không thể hỏng. Những "
               "thứ như khoảng tách cũng có thể đạt đến mức mà không cần xem xét hỏng hóc "
               "(xem Bảng 13.7) nhưng trong trường hợp này chúng được gọi là ‘không chịu sự "
               "cố’ và không dùng thuật ngữ Không thể hỏng. Dù sao đi nữa, kết quả là như "
               "nhau và khi tiến hành bài tập đếm lỗi, không cần xét các chế độ hỏng cụ thể "
               "ở bất kỳ linh kiện, cụm, dây dẫn, kết nối và khoảng tách nào trong số này."))
    # Quirks 24, 25, B10, B11.
    b.append(note("<b>Lưu ý về các thuật ngữ ‘infallible’ và ‘not subject to fault’.</b> Lớp "
                  "OCR đọc các dấu nháy đóng của 'not subject to fault' thành dấu nháy mở; "
                  "trang render in ‘not subject to fault’ và ‘infallible’ với dấu nháy đơn "
                  "kiểu cong. Bản in viết 'Infallible is not used' với chữ I hoa giữa câu, "
                  "và bắt đầu đoạn sau bằng 'Infallible components ...'; các dạng này được "
                  "giữ nguyên trong bản tiếng Anh, bản tiếng Việt dịch theo ý định."))
    # D24.
    b.append(p("Trong mọi trường hợp, tính không thể hỏng của các linh kiện, cụm, dây dẫn, "
               "kết nối và khoảng tách như vậy chỉ giới hạn ở chế độ hỏng cụ thể mà cấu tạo "
               "của chúng cho phép bỏ qua (ví dụ, sự tách biệt của một cặp đường dẫn mạch in "
               "có thể khiến chúng được giả định là không bị nối vào nhau, nhưng điều đó "
               "không ảnh hưởng gì đến việc xem xét sự đứt gãy của chúng)."))
    # D25.
    b.append(p("Dù việc dùng hai thuật ngữ ‘không thể hỏng’ và ‘không chịu sự cố’ cho các chế "
               "độ hỏng cụ thể của linh kiện và các phần tử mạch khác là gây nhầm lẫn, người "
               "ta hiểu rằng việc dùng thuật ngữ nào cũng truyền đạt cùng một thông tin và "
               "không nên phát sinh nguy hiểm."))
    # D26.
    b.append(p("Các linh kiện, cụm và sắp xếp không thể hỏng được coi là không chịu các điều "
               "kiện lỗi cụ thể cần đáp ứng các yêu cầu riêng bổ sung cho các yêu cầu cấu tạo "
               "cơ bản của nguyên lý bảo vệ tạo ra trạng thái lỗi có thể đếm (xem các Mục "
               "13.7 và 13.8)."))
    # D27 — heading 13.10.1.
    b.append(h3("13.10.1 Máy biến áp không thể hỏng", "13.10.1 Infallible transformers"))
    # D28.
    b.append(p("Rõ ràng là máy biến áp lưới điện, được dùng trong thiết bị liên kết để hạ "
               "điện áp xuống mức thấp thông thường dùng trong mạch an toàn nội tại, rất "
               "quan trọng vì hỏng hóc của các cuộn dây liên quan đến mạch đó tới cuộn dây "
               "lưới điện hoặc các cuộn phụ khác trên máy biến áp liên quan đến các mạch an "
               "toàn nội tại khác hoặc các mạch không an toàn nội tại sẽ dẫn đến tình huống "
               "an toàn nội tại bị suy giảm. Một máy biến áp như vậy cần không thể hỏng đối "
               "với các sự nối này cả trong vận hành bình thường lẫn trong điều kiện hỏng. "
               "Ngoài ra, khi hỏng hóc của các cuộn dây liên quan đến mạch an toàn nội tại "
               "tới lõi máy biến áp, vốn thường được nối đất, có thể tạo ra tình trạng có "
               "khả năng gây cháy, máy biến áp cũng phải không thể hỏng đối với hỏng hóc đó. "
               "Các yêu cầu đối với máy biến áp như sau."))
    # D29 — unnumbered heading.
    b.append(h4("Cấu tạo máy biến áp lưới điện", "Mains transformer construction"))
    # D30 — first part, continues on printed 387.
    b.append(p("Một số chế độ cấu tạo được hình dung cho máy biến áp lưới điện trong BS/EN "
               "50020 và được cấp số hiệu. Đơn giản nhất trong số đó là loại"))

    # ------------------------------------------------------------------
    # BLOCK D-387 / printed 387 / PDF 408: Table 13.11, D31, heading Type 2b,
    # D33, items 1 and 2 (first part).
    # D-387.26, quirks B4, B5.
    b.append(table(T3.HEAD1311_VI, T3.ROWS1311_VI, T3.CAPTION1311_VI))
    if T3.NOTE1311_VI:
        b.append(note(T3.NOTE1311_VI))
    b.append(note("<b>Lưu ý về Bảng 13.11.</b> Lớp OCR đọc '1 .o' thay vì 1.0; dòng nguồn in "
                  "'(from BSEN 50020)' không có dấu gạch chéo, khác với 'BS/EN 50020' trong "
                  "văn bản. Ghi chú 1 bị lặp từ trong nguyên bản ('a tolerance of up to 10% "
                  "manufacturing tolerance') và được giữ nguyên từ ngữ trong bản tiếng Anh."))
    # D31 — continuation of D30; quirk B6.
    b.append(p("mà máy biến áp được phép vượt quá định mức cách điện của nó nhưng hỏng hóc "
               "giữa các cuộn dây của mạch không an toàn nội tại và các cuộn dây khác được "
               "ngăn chặn bằng một màn chắn kim loại nối đất có độ dày phù hợp Bảng 13.11. "
               "Điều này được gọi là ‘Máy biến áp Loại 2b và các nguyên lý cấu tạo của nó "
               "được chỉ ra trong Hình 13.23."))
    b.append(note("<b>Lưu ý về dấu nháy chưa đóng trong bản in.</b> Bản in viết 'This is "
                  "termed a ‘Type 2b transformer and its principles of construction are "
                  "shown in Fig. 13.23.' — dấu nháy đơn mở mà không có dấu đóng. Đây là lỗi "
                  "của tài liệu gốc, được giữ nguyên trong bản tiếng Anh; lớp OCR cũng ghi "
                  "như vậy nhưng dùng dấu nháy thẳng."))
    # D32 — unnumbered heading.
    b.append(h4("Máy biến áp Loại 2b", "Type 2b transformer"))
    # D33.
    b.append(p("Máy biến áp Loại 2b thường là máy biến áp ‘kiểu vỏ’ (xem Hình 13.23) với các "
               "cuộn dây chồng lên nhau trên một khung cuộn duy nhất, hoặc không có khung "
               "cuộn, nhưng trong cả hai trường hợp đều được cố kết trên một lõi duy nhất để "
               "mọi khoảng tách đều đáng tin và lặp lại được. Màn chắn phải có toàn bộ chiều "
               "rộng của vùng cuộn dây để đảm bảo không có khả năng nối xuyên qua màn chắn, "
               "trừ ở mép ngoài của các cuộn dây nơi áp dụng Bảng 13.7. Trong cả hai trường "
               "hợp, lớp cách điện hoặc khoảng tách khác giữa các cuộn dây liên quan đến mạch "
               "an toàn nội tại và lõi, màn chắn và các cuộn dây khác phải đảm bảo máy biến "
               "áp đáp ứng ít nhất những điều sau:"))
    # D34 — numbered item 1.
    b.append(p("1. Khoảng tách tổ hợp giữa khối cuộn dây của các cuộn dây riêng biệt quanh "
               "màn chắn phải đáp ứng yêu cầu của Bảng 13.7. (Trong hầu hết trường hợp, điều "
               "này sẽ yêu cầu tính toán tổ hợp khoảng cách tách – xem Hình 13.20 và 13.21)."))
    # D35 — numbered item 2, first part; continues on printed 388.
    b.append(p("2. Màn chắn phải là một lớp lá duy nhất gồm ít nhất một vòng và chồng lên "
               "nhau nhưng được cách điện sao cho các đầu của màn chắn không thể bị nối vào "
               "nhau, hoặc là hai lớp được quấn bằng dây đã cách điện (sơn phủ). Đối với màn "
               "chắn bằng lá, yêu cầu này nhằm tránh các đầu màn chắn trở nên"))

    # ------------------------------------------------------------------
    # BLOCK D-388 / printed 388 / PDF 409: Fig. 13.23, D36, D37.
    # D-388.28, D-388.29, quirks B11, B16, B17.
    b.append(fig(23, FD.fig_f1323()))
    b.append(note("<b>Lưu ý về chú thích Hình 13.23.</b> Lớp OCR trộn chú thích vào văn bản "
                  "hình vẽ; trang render cho chú thích riêng với năm ghi chú. Ghi chú (3) in "
                  "'normal industrial requirements' trong khi Hình 13.24 và 13.25 in 'normal "
                  "industrial standards'; ghi chú (4) in 'withstand 500V test' không dấu "
                  "cách giữa số và V. Chú thích kết thúc bằng 'Windings to be consolidated' "
                  "không có dấu chấm cuối, như bản in."))
    # D36 — continuation of item 2; quirk 30.
    b.append(p("được nối với nhau tạo thành một vòng bị ngắn mạch sẽ làm máy biến áp bị hỏng. "
               "Đối với màn chắn bằng dây, cần cách điện giữa mỗi vòng dây và giữa hai lớp vì "
               "lý do tương tự. Vì vậy, yêu cầu cách điện duy nhất giữa các lớp là lớp cách "
               "điện không bị hỏng khi chịu thử nghiệm cách điện ở điện áp áp dụng 500Vrms "
               "xoay chiều hoặc 700 V một chiều. Điện áp được áp bằng cách tăng dần điện áp "
               "áp dụng sao cho giá trị quy định đạt được sau 10 giây và sau đó duy trì giá "
               "trị đó trong 60 giây. Dòng rò phải nhỏ hơn 5mA và phải ổn định hoặc giảm, vì "
               "bất kỳ sự tăng nào cũng được coi là dấu hiệu báo trước của hỏng cách điện."))
    b.append(note("<b>Lưu ý về điện áp thử trong bản in.</b> Bản in ghi 'an applied voltage of "
                  "500Vrms ac or 700 V dc' — không dấu cách trong '500Vrms' nhưng có dấu cách "
                  "trước '700 V'. Lớp OCR ghi như nhau; dạng này được giữ nguyên trong bản "
                  "tiếng Anh."))
    # D37 — numbered item 3, first part; quirks 31, 32, B22.
    b.append(p("3. Máy biến áp không được tạo ra tình trạng trong đó cuộn dây (các cuộn dây) "
               "liên quan đến một mạch an toàn nội tại cụ thể bị nối vào các cuộn dây khác. "
               "Để chứng minh điều này, một phép thử được áp trong đó một (bất kỳ một) trong "
               "số các cuộn dây đầu ra của máy biến áp bị ngắn mạch, sau đó tất cả các cuộn "
               "dây đầu ra khác được đặt tải tạo ra dòng danh định cực đại từ cuộn đó ở điện "
               "áp danh định. Sau đó máy biến áp chịu tác dụng của điện áp danh định tại cuộn "
               "đầu vào hoặc điện áp nhỏ hơn sao cho tạo ra 1.7Iₙ vào máy biến áp. Điều kiện "
               "này được áp dụng trong 6 giờ hoặc cho đến khi máy biến áp bị hỏng. Tiêu chuẩn "
               "cách điện là khi điện áp gấp đôi điện áp danh định của máy biến áp (Uₙ) cộng "
               "1000 V, với mức tối thiểu 1500 V, được áp giữa các cuộn dây đang xét, dòng "
               "chảy qua không được vượt quá 5mA và phải"))
    b.append(note("<b>Lưu ý về ký hiệu dòng trong bản in.</b> Lớp OCR đọc 'l.71n' nhưng trang "
                  "render in '1.7Iₙ' (chữ I, chỉ số dưới n, không dấu cách); tương tự '(U,)' "
                  "thành '(Uₙ)' và '1OOOV' thành '1000 V'. Bản in dùng '1.7Iₙ' ở đây nhưng "
                  "'1.7 Iₙ' ở các đoạn sau — sự không nhất quán về dấu cách được giữ nguyên "
                  "theo từng chỗ."))

    # ------------------------------------------------------------------
    # BLOCK D-389 / printed 389 / PDF 410: D38, items 4-7, heading Type 1a,
    # D44, D45.
    # D38 — continuation of item 3.
    b.append(p("ổn định hoặc giảm. Máy biến áp có thể bị hỏng trong quá trình thử này nhưng "
               "không được bốc cháy vì cháy có thể gây ra các hỏng hóc tiếp theo."))
    # D39 — numbered item 4.
    b.append(p("4. Khi hỏng hóc tới đất có thể gây vấn đề cho mạch an toàn nội tại, không được "
               "xảy ra hỏng máy biến áp và máy biến áp không được vượt quá định mức nhiệt độ "
               "trong thử nghiệm trên. Điều này có thể đạt được bằng cách dùng các công tắc "
               "nhiệt tích hợp như đã mô tả trước đó hoặc bằng cách đưa vào một điện trở hạn "
               "dòng để hạn chế dòng trong máy biến áp. Khi dùng công tắc tự ngắt rồi tự đặt "
               "lại thay vì công tắc không tự đặt lại, kéo dài thử nghiệm lên 12 giờ để tính "
               "đến các chu kỳ ngắt lặp lại. Khi lắp điện trở, nó được đặt trong mạch đầu vào "
               "của máy biến áp và phải đáp ứng yêu cầu tách của Bảng 13.7, có định mức thích "
               "hợp (xem phần trước trong chương này), và không thể hỏng như mô tả sau này. "
               "Trong trường hợp này, khoảng tách giữa cuộn dây (các cuộn dây) cấp điện cho "
               "mạch an toàn nội tại và các cuộn dây khác và màn chắn phải đáp ứng Bảng 13.7. "
               "Ảnh hưởng có thể có của hỏng hóc tới đất được chỉ ra trong ví dụ ở Hình "
               "13.24."))
    # D40 — numbered item 5.
    b.append(p("5. Khi màn chắn gồm hai lớp dây quấn riêng biệt, mỗi lớp nên được nối đất riêng "
               "và máy biến áp phải có phương tiện cho việc này. Khi màn chắn là lá kim loại, "
               "nó phải có hai dây riêng biệt nối vào để cho phép mức độ chắc chắn nối đất như "
               "nhau, và cần cẩn thận đảm bảo việc nối các dây này không tạo ra một vòng ngắn "
               "mạch cục bộ trên máy biến áp."))
    # D41 — numbered item 6.
    b.append(p("6. Lõi máy biến áp cũng phải được nối đất và cấu tạo của nó phải cho phép "
               "điều này. Thường người ta làm bằng cách xen một dải dẫn điện vào các lá thép "
               "và sau đó bố trí một cọc nối trên đó tại vị trí nó đi ra khỏi các lá thép. Một "
               "số vật liệu máy biến áp, chẳng hạn như ferit, có thể tự chúng là vật cách điện "
               "và trong những trường hợp đó không cần kết nối đất. Tuy nhiên, không được "
               "chấp nhận việc cách điện một lõi dẫn điện mà không nối đất nó, trừ khi độ dày "
               "lớp cách điện đáp ứng Bảng 13.10 và máy biến áp được ngăn không bị quá nhiệt "
               "như đã mô tả trước đó."))
    # D42 — numbered item 7.
    b.append(p("7. Khoảng tách của các phương tiện kết nối cũng phải tuân thủ yêu cầu của "
               "Bảng 13.10 để ngăn các kết nối chéo tại các điểm đầu cuối."))
    # D43 — unnumbered heading; quirks 33, 34, B1.
    b.append(h4("Máy biến áp Loại 1a, 1b và 2a", "Type 1a, 1b and 2a transformers"))
    b.append(note("<b>Lưu ý về số hiệu loại máy biến áp.</b> Bản in dùng chữ số một, không "
                  "phải chữ l: 'Type 1a', 'Type 1b', 'Type 2a', 'Type 2b' và nhan đề 'Type "
                  "1a, 1b and 2a transformers'. Lớp OCR đọc nhầm thành 'Type la', 'Type lb', "
                  "'Type 7b'; dạng chữ số được giữ nguyên trong cả hai ngôn ngữ."))
    # D44.
    b.append(p("Các loại máy biến áp khác được hình dung là máy biến áp Loại 1a, máy biến áp "
               "Loại 1b và máy biến áp Loại 2a. Máy biến áp Loại 1a có các cuộn dây quấn cạnh "
               "nhau trên một chân của máy biến áp và máy biến áp Loại 1b theo cùng cấu tạo "
               "nhưng có các cuộn riêng biệt trên các chân riêng biệt của máy biến áp, nhưng "
               "vẫn là các thực thể riêng biệt (không chồng lên nhau)."))
    # D45; quirk 35, B11.
    b.append(p("Máy biến áp Loại 1b phổ biến hơn vì nó dùng lõi ‘kiểu vỏ’, trong đó một chân "
               "đi xuyên qua cuộn dây và hai chân kia bao quanh nó, thay vì máy biến áp Loại "
               "1a thường có lõi ‘kiểu lõi’ với một chân đi qua mỗi cuộn dây và thường không "
               "có các chân bao quanh."))
    b.append(note("<b>Lưu ý về dấu nháy cong trong tên cấu tạo.</b> Bản in dùng ‘shell type’ "
                  "và ‘core type’ với dấu nháy đơn kiểu cong; lớp OCR đôi khi đọc thành dấu "
                  "nháy đóng ở đầu. Dạng in được giữ nguyên trong bản tiếng Anh; bản tiếng Việt "
                  "dịch là ‘kiểu vỏ’ và ‘kiểu lõi’."))

    # ------------------------------------------------------------------
    # BLOCK D-390 / printed 390 / PDF 411: D46, Fig. 13.24, Fig. 13.25.
    # D46.
    b.append(p("Máy biến áp Loại 2a tương tự máy biến áp Loại 2b, nhưng trong trường hợp này "
               "không có màn chắn, các cuộn dây nằm chồng lên nhau và có lớp cách điện giữa "
               "chúng. Tất nhiên, lớp cách điện phải có toàn bộ chiều rộng của vùng cuộn dây "
               "(xem Hình 13.24) để ngăn sự hiện diện của một đường dẫn xuyên qua nó, trừ việc "
               "đi vòng qua mép ngoài của cuộn dây nơi áp dụng Bảng 13.7."))
    # D-390.36, D-390.37, quirks B14, B17, B18.
    b.append(fig(24, FD.fig_f1324()))
    b.append(fig(25, FD.fig_f1325()))
    b.append(note("<b>Lưu ý về chú thích Hình 13.24 và 13.25.</b> Lớp OCR đọc 'Type la'/'Type "
                  "lb' trong nhan đề và tách từ 'connection' ở cuối dòng; trang render in "
                  "'Type 1a'/'Type 1b' và 'connection'. Ghi chú (2) của cả hai in 'normal "
                  "industrial standards' (số nhiều), khác với 'normal industrial "
                  "requirements' của Hình 13.23. Hình 13.24 trích 'Table 13.10' ở các ghi chú "
                  "(3)/(5), trong khi Hình 13.25 trích 'Table 13.7' ở các ghi chú tương ứng — "
                  "sự khác biệt được giữ nguyên, không đồng nhất hóa. Cả hai chú thích đều "
                  "kết thúc bằng 'Windings to be consolidated' không có dấu chấm cuối."))

    # ------------------------------------------------------------------
    # BLOCK D-391 / printed 391 / PDF 412: Fig. 13.26, D47, D48, heading,
    # D50.
    # D-391.38, D-391.39, quirks B14, B15, B16.
    b.append(fig(26, FD.fig_f1326()))
    b.append(note("<b>Lưu ý về chú thích Hình 13.26.</b> Lớp OCR tách nhan đề 'Fig. 13.26 · "
                  "Type 2a transformer' và đọc 'Types la, lb and 2a'; trang render nối thành "
                  "một dòng và in 'Types 1a, 1b and 2a'. Ghi chú (1) in 'unless material is "
                  "non-conducting', thiếu từ 'core' như trong Hình 13.24 và 13.25; ghi chú "
                  "(4) in 'If necessary to prevent overheating thermal trip embedded in "
                  "primary or secondary winding (as appropriate).' không có dấu phẩy sau "
                  "'overheating' và trong ngoặc. Chú thích không có dấu chấm cuối. Tất cả "
                  "được giữ theo bản in."))
    # D47; quirk B19.
    b.append(p("Trong tất cả các trường hợp này, máy biến áp phải có các cuộn dây được cố kết "
               "và không được hỏng khi chịu các thử nghiệm kiểu mô tả cho máy biến áp Loại 2b, "
               "điều hầu như luôn có nghĩa là cần một công tắc nhiệt hoặc điện trở hạn dòng "
               "như trong trường hợp của hầu hết máy biến áp Loại 2b. Độ dày cách điện giữa "
               "mỗi cuộn dây và các cuộn khác, hoặc lõi nối đất của máy biến áp (nếu việc nối "
               "đất gây vấn đề) phải đáp ứng Bảng 13.7. Chi tiết cấu tạo của các máy biến áp "
               "Loại 1a, 1b và 2a được chỉ ra trong Hình 13.24, 13.25 và 13.26."))
    b.append(note("<b>Lưu ý về câu 'Detail ... are shown'.</b> Bản in viết 'Detail of the "
                  "construction of Types 1a, 1b and 2a transformers are shown in Fig. 13.24, "
                  "13.25 and 13.26.' — danh từ số ít 'Detail' đi với 'are'. Lớp OCR đọc 'Types "
                  "la, lb and 2a'; dạng chữ số một được giữ. Câu được giữ nguyên trong bản "
                  "tiếng Anh; bản tiếng Việt dịch theo ý định."))
    # D48.
    b.append(p("Vì máy biến áp được quấn và nói chung là các linh kiện lắp ráp có mức độ biến "
               "thiên cao hơn các linh kiện được kiểm soát chặt chẽ hơn, cần một thử nghiệm "
               "thường quy và thử nghiệm này được mô tả trong Bảng 13.12."))
    # D49 — unnumbered heading.
    b.append(h4("Cấu tạo của máy biến áp không phải máy biến áp lưới điện",
                "Construction of transformers which are not mains transformers"))
    # D50 — first part, continues on printed 392; quirk B20.
    b.append(p("Trong các mạch an toàn nội tại, thông thường dùng máy biến áp cho các mục "
               "đích khác (ví dụ, tạo cách ly galvanic giữa các phần của mạch). Những máy biến "
               "áp như vậy phải được cấu tạo theo yêu cầu đối với máy biến áp lưới điện, "
               "ngoại trừ việc thử nghiệm 5 giờ chỉ cần thực hiện ở tải danh định của máy biến "
               "áp. Khi những máy biến áp đó được nối giữa"))
    b.append(note("<b>Lưu ý về '5-hour'.</b> Bản in viết 'the 5-hour test need only be done "
                  "at rated transformer load' với dấu gạch nối giữa số và từ; được giữ nguyên "
                  "trong bản tiếng Anh."))

    # ------------------------------------------------------------------
    # BLOCK D-392 / printed 392 / PDF 413: Fig. 13.27, Table 13.12, D51.
    # D-392.40, D-392.41, quirk B16.
    b.append(fig(27, FD.fig_f1327()))
    b.append(note("<b>Lưu ý về chú thích Hình 13.27.</b> Lớp OCR đọc 'windingkore' và "
                  "'secondaty/frame' nhưng trang render in 'winding/core' và 'secondary/frame'; "
                  "các mục 'limiting resistor Ij,' và 'LP' chỉ là nhiễu OCR, không có trong "
                  "hình vẽ. Chú thích kết thúc bằng 'intrinsic safety intact' không có dấu "
                  "chấm cuối, như bản in."))
    # D-392.42, quirks B21, B22.
    b.append(table(T3.HEAD1312_VI, T3.ROWS1312_VI, T3.CAPTION1312_VI))
    if T3.NOTE1312_VI:
        b.append(note(T3.NOTE1312_VI))
    b.append(note("<b>Lưu ý về Bảng 13.12.</b> Lớp OCR đọc '4 U,, or 2000 V rms' và '2 u,, + "
                  "1000 v rms'; trang render in '4 Uₙ or 2000 V rms' và '2 Uₙ + 1000 V rms' "
                  "với U ở dạng chỉ số dưới. Ô thứ ba in 'Intrinsically Safe' với chữ hoa, còn "
                  "văn bản xung quanh viết thường; các ô thứ hai và thứ ba kết thúc bằng dấu "
                  "chấm. Dòng '5mA' được in không có dấu cách trước đơn vị. Tất cả được giữ "
                  "theo bản in."))
    # D51 — continuation of D50, continues on printed 393.
    b.append(p("mạch an toàn nội tại và mạch không an toàn nội tại, tuy nhiên, có một vấn đề "
               "bổ sung là các mạch không an toàn nội tại không được đánh giá và phải giả "
               "định rằng lưới điện có thể xuyên qua tới máy biến áp. Trong những trường hợp "
               "như vậy, cần đưa ra các biện pháp ngăn điều này gây hư hỏng máy biến áp. Những "
               "biện pháp phòng ngừa như vậy có thể là những biện pháp áp dụng cho"))

    # ------------------------------------------------------------------
    # BLOCK D-393 / printed 393 / PDF 414: D52, heading Transformer
    # protection, D54-D59.
    # D52 — continuation of D51.
    b.append(p("máy biến áp lưới điện cùng loại hoặc, thay vào đó, bằng cách đặt một diode "
               "zener song song shunt qua cuộn dây bị ảnh hưởng và sau đó bảo vệ diode bằng "
               "một cầu chì có định mức phù hợp để đảm bảo sự xuyên lưới điện được loại bỏ "
               "trước khi máy biến áp hoặc diode zener bị hư hỏng. Các yêu cầu của Bảng 13.7 "
               "cần được áp dụng cho tổ hợp cầu chì/diode zener này để đảm bảo nó không thể "
               "bị đi tắt qua."))
    # D53 — unnumbered heading.
    b.append(h4("Bảo vệ máy biến áp", "Transformer protection"))
    # D54.
    b.append(p("Để đảm bảo không xảy ra hỏng hóc, điều thiết yếu là không được vận hành máy "
               "biến áp theo cách cho phép những hỏng hóc đó. Điều này đòi hỏi phải bảo vệ máy "
               "biến áp theo cách cho phép xác định các điều kiện xấu nhất của nó. Tất cả máy "
               "biến áp lưới điện phải được cấp cầu chì đầu vào để cắt nguồn lưới nếu hỏng "
               "hóc xảy ra trong chính máy biến áp hoặc trong các mạch được nối."))
    # D55.
    b.append(p("Mức cơ bản của bảo vệ là đặt cầu chì cho mạch đầu vào sao cho không thể vượt "
               "quá các điều kiện vận hành thiết kế tối đa của máy biến áp đã được quy định "
               "trong quá trình thiết kế. Vì máy biến áp có thể chịu được những điều kiện này "
               "mà không gây vấn đề trong mạch an toàn nội tại, nó có thể được coi là không "
               "thể hỏng."))
    # D56; quirk 43, B22.
    b.append(p("Cầu chì phải đáp ứng các yêu cầu đã mô tả trong Mục 13.6.2 đối với cầu chì "
               "lắp trong thiết bị liên kết, nghĩa là dòng điện cực đại mà máy biến áp có thể "
               "rút liên tục, với sự hiện diện của cầu chì như vậy, được coi là 1.7 lần dòng "
               "danh định của cầu chì (Iₙ). Có thể dùng một bộ ngắt mạch có định mức phù hợp "
               "thay cho cầu chì và bộ ngắt mạch chỉ cần tuân thủ một tiêu chuẩn cấu tạo được "
               "công nhận cho loại bộ ngắt đó. Giá trị 1.7 Iₙ được giữ lại và trong trường hợp "
               "này là 1.7 lần dòng danh định mà bộ ngắt sẽ hoạt động. Do đó, máy biến áp phải "
               "có khả năng chịu được dòng này mà không bị hư hỏng, vì hư hỏng có thể ảnh hưởng "
               "xấu đến an toàn nội tại."))
    b.append(note("<b>Lưu ý về cách viết Iₙ.</b> Lớp OCR đọc '(In)', '1.7 I,' và '(1.7 I,)'; "
                  "trang render in '(Iₙ)', '1.7 Iₙ' và '(1.7 Iₙ)'. Cách đặt dấu cách không "
                  "nhất quán giữa '1.7Iₙ' (trước đó), '1.7 Iₙ' và '1.7 times the rated fuse "
                  "current (Iₙ)' ở đây được giữ nguyên theo từng chỗ."))
    # D57; quirk B23.
    b.append(p("Yêu cầu cơ bản của bộ ngắt mạch là chúng tuân thủ một Tiêu chuẩn được công "
               "nhận, thường được hiểu là Tiêu chuẩn Châu Âu, Tiêu chuẩn Quốc tế hài hòa hoặc, "
               "nếu không có cả hai, Tiêu chuẩn Quốc gia."))
    b.append(note("<b>Lưu ý về ngữ pháp và chính tả trong bản in.</b> Bản in viết 'The basic "
                  "requirements of circuit breakers is that they comply ...' — số nhiều "
                  "'requirements' đi với 'is'. Các từ 'recognized', 'harmonized' và "
                  "'minimize' dùng chính tả Mỹ và được giữ nguyên, không đổi sang dạng -ised."))
    # D58.
    b.append(p("Việc dùng cầu chì hoặc bộ ngắt mạch như mô tả ở trên thường đủ đối với máy "
               "biến áp cấu tạo Loại 2b, trừ khi hỏng hóc giữa các cuộn dây với lõi hoặc màn "
               "chắn không được chấp nhận, khi đó, cũng như đối với máy biến áp Loại 1a, 1b và "
               "2a, dòng mà cầu chì cho qua (1.7 Iₙ) không được làm nhiệt độ cuộn dây vượt quá "
               "định mức cách điện của chúng. Trường hợp có thể xảy ra điều đó, cần một công "
               "tắc nhiệt để đảm bảo không xảy ra."))
    # D59 — first part, continues on printed 394; quirk B24.
    b.append(p("Khi công tắc nhiệt như vậy được dùng để ngắt máy biến áp khỏi nguồn trước khi "
               "nhiệt độ cuộn dây vượt quá, nó không được để người truy cập được. Nó phải được "
               "chôn lấp trong các cuộn dây hoặc cố kết cùng chúng để có niềm tin rằng nó sẽ "
               "ngắt tin cậy trước khi bất kỳ cuộn dây hoặc cách điện nào khác bên trong máy "
               "biến áp vượt quá giới hạn định mức của nó. Công tắc có thể không tự đặt lại "
               "hoặc tự đặt lại tự động nhưng không được đặt lại bằng tay vì điều đó ngụ ý "
               "can thiệp từ bên ngoài, điều không được chấp nhận vì nó"))

    # ------------------------------------------------------------------
    # BLOCK D-394 / printed 394 / PDF 415: D60-D63, heading 13.10.2, D65,
    # heading 13.10.3, D67 (partial).
    # D60 — continuation of D59.
    b.append(p("sẽ cho phép đặt lại trước khi máy biến áp kịp nguội và tồn tại khả năng vượt "
               "quá giới hạn nhiệt độ của cấu tạo. Chỉ cần một thiết bị như vậy."))
    b.append(note("<b>Lưu ý về chỗ ngắt giữa trang.</b> Đoạn trên kết thúc giữa câu bằng "
                  "'...which would not be acceptable as it' trên bản in 393 và tiếp tục trên "
                  "bản in 394 bằng 'would permit resetting before the transformer could "
                  "cool ...'. Chỗ ngắt được giữ nguyên theo bản in."))
    # D61; quirk B25.
    b.append(p("Yêu cầu cấu tạo đối với công tắc nhiệt như vậy là nó phải phù hợp với Tiêu "
               "chuẩn được công nhận cho loại thiết bị này. (Tiêu chuẩn được công nhận trong "
               "ngữ cảnh này thường có nghĩa là Tiêu chuẩn Châu Âu nếu có, Tiêu chuẩn Quốc tế "
               "hài hòa hoặc, nếu không có cả hai, tiêu chuẩn quốc gia)."))
    b.append(note("<b>Lưu ý về chữ hoa trong 'national Standard'.</b> Đoạn này viết 'a national "
                  "Standard' với 'national' viết thường, nhưng đoạn trước viết 'a National "
                  "Standard' với chữ N hoa. Sự khác biệt được giữ nguyên trong bản tiếng Anh."))
    # D62; quirk 44, B26.
    b.append(p("Khi máy biến áp có một màn chắn nối đất phù hợp, không nhất thiết phải đảm "
               "bảo không vượt quá giới hạn nhiệt độ cách điện nếu các lỗi tiếp đất bên trong "
               "máy biến áp không gây vấn đề. Cần nhớ rằng, ở Vương quốc Anh, nguồn lưới điện "
               "thông thường được nối đất theo chính sách bảo vệ con người bằng cách nối cực "
               "trung tính của nguồn với đất tại điểm phát nguồn. Điều này có nghĩa là trong "
               "trường hợp hỏng hóc trong máy biến áp, bất kỳ cực nào của nguồn cũng có thể "
               "được nối đất. Để đảm bảo nguồn được cách ly hiệu quả khi xảy ra những hỏng hóc "
               "như vậy, tất cả các dây dẫn cấp điện không nối đất phải có cầu chì hoặc bộ "
               "ngắt mạch đáp ứng các yêu cầu đã nêu ở trên."))
    b.append(note("<b>Lưu ý về từ 'possessed of' và một lỗi OCR.</b> Bản in viết 'Where the "
                  "transformer is possessed of a suitable earthed screen ...'; đây là cách "
                  "diễn đạt của nguyên bản. Lớp OCR đọc 'satisfymg' nhưng trang render in "
                  "'satisfying' trong cụm 'satisfying the already specified requirements'."))
    # D63.
    b.append(p("Trong trường hợp người ta cho rằng không cần đưa lỗi cuộn dây/đất của máy biến "
               "áp vào kịch bản lỗi và nguồn điện không được tham chiếu tới đất (đây là "
               "trường hợp ở một số quốc gia khác), thì chỉ cần một thiết bị bảo vệ trong mạch "
               "đầu vào, vì hỏng hóc tới đất của một dây dẫn nguồn đơn lẻ không gây ra cùng "
               "loại vấn đề như khi nguồn được tham chiếu tới đất. Một đánh giá các kịch bản "
               "lỗi có thể xảy ra cho thấy rằng, ngay cả khi tổ hợp lỗi được hình dung trong "
               "khái niệm an toàn nội tại không bao gồm tình huống đi tắt qua các thiết bị bảo "
               "vệ, khả năng xa hơn của việc này xảy ra vẫn đủ để đưa ra khuyến nghị rằng tất "
               "cả các dây dẫn nguồn không nối đất đều có một thiết bị bảo vệ, bất kể loại máy "
               "biến áp được dùng và nguồn cấp của nó."))
    # D64 — heading 13.10.2.
    b.append(h3("13.10.2 Cuộn dây giảm chấn", "13.10.2 Damping windings"))
    # D65.
    b.append(p("Cuộn dây giảm chấn được dùng để giảm thiểu ảnh hưởng của điện cảm trong những "
               "trường hợp như rơ le. Chúng thực chất là các vòng bị ngắn mạch và làm giảm "
               "điện cảm biểu kiến xuống còn điện cảm rò, giá trị này biểu thị nghịch đảo của "
               "hiệu suất ghép nối giữa chúng và cuộn dây chính. Nếu những cuộn dây như vậy "
               "được dùng để giảm thiểu điện cảm cho mục đích an toàn nội tại, chúng phải tin "
               "cậy để có thể được coi là không thể hỏng đối với hỏng hóc hở mạch. Cách điển "
               "hình để đảm bảo điều này là dùng các ống hoặc dây đồng không cách điện được "
               "ngắn mạch liên tục bằng cách hàn hoặc hàn gió. Bất kỳ cuộn dây nào dùng cho "
               "mục đích này cũng cần đạt được mức độ chắc chắn này chống hở mạch."))
    # D66 — heading 13.10.3; quirk 45.
    b.append(h3("13.10.3 Điện trở hạn dòng", "13.10.3 Current limiting resistors"))
    b.append(note("<b>Lưu ý về số hiệu 13.10.3.</b> Lớp OCR đọc '73.10.3 Current limiting "
                  "resistors'; trang render in '13.10.3 Current limiting resistors'. Số hiệu "
                  "đúng từ bản in được dùng trong cả hai ngôn ngữ."))
    # D67 — partial, continues on printed 395 (outside this module).
    b.append(p("Điện trở hạn dòng thường được dùng để hạn chế dòng ngắn mạch tới một khu vực "
               "nguy hiểm, để hạn chế dòng có thể cấp vào một cuộn cảm, để hạn chế"))
    # Quirk 46, B27.
    b.append(note("<b>Lưu ý về ranh giới module và các dẫn chiếu chưa giải quyết.</b> Module "
                  "này bắt đầu giữa câu của §13.9.2 (từ bản in 378) và kết thúc giữa câu của "
                  "§13.10.3 trên bản in 394; phần tiếp theo nằm ở module E. Các dẫn chiếu "
                  "'Table 13.7', 'Table 13.4', 'Figure 13.14', 'Section 13.6.2', 'Sections "
                  "13.7 and 13.8', 'BS/EN 50020', 'BS/EN 50019' và 'Chapter 12' vẫn không "
                  "được giải quyết trong phạm vi này, đúng như bản in. Dấu === PAGE 416 === "
                  "nằm ở dòng 17208 của văn bản thô (không phải 17254 như ghi trong bản mô tả)."))
    return "".join(b)


def body_en():
    b = []

    # ------------------------------------------------------------------
    # BLOCK D-379 / printed 379 / PDF 400: Fig. 13.19 + Table 13.8, no prose.
    # D-379.1, D-379.2, D-379.3, D-379.4, D-379.12, quirk B12.
    b.append(fig(19, FD.fig_f1319()))
    b.append(note("<b>Note on Fig. 13.19 and OCR text-layer errors.</b> The printed running "
                  "header reads 'intrinsic safety ‘i’'; the OCR layer misreads it as "
                  "'intrinsic safety T’', and on printed p.385 reads 'intrinsic safely ?' "
                  "instead of 'intrinsic safety ‘i’ 385'. The in-figure labels were OCR'd as "
                  "'e central metal', 'd. d, , 0; = creepage distance' and with 'is not "
                  "electrically connected' run into 'Exposed HT of r,b >d'; the render gives "
                  "'The central metal', 'd, d₁, d₂ = creepage distance' and 'Exposed HT of "
                  "r,b > d' (with spaces around >). The markers ≥3, <3, ≥1 and the annotation "
                  "'Exposed HT of r,b > d' are retained although the print does not explain "
                  "them."))
    # D-379.10, D-379.14, D-379.15, quirk B2.
    b.append(table(T2.HEAD138_EN, T2.ROWS138_EN, T2.CAPTION138_EN))
    if T2.NOTE138_EN:
        b.append(note(T2.NOTE138_EN))
    b.append(note("<b>Note on Table 13.8.</b> The first column prints '10V' ... '1575V' and "
                  "then '3.3KV', '4.7KV', '9.5KV', '15.6KV' (capital K, no space), while the "
                  "OCR layer reads '1ov', 'lO0OV', '4.7Kv' and inserts spaces in '1 .o' / "
                  "'1 75'. The CTI cells print the literal words 'Note 1', 'Note 2' and "
                  "'N/A'; the two category heads use curly single quotes ‘ia’ and ‘ib’ (the "
                  "OCR gives straight quotes). The legend prints 'CTG = Coating'. All forms "
                  "are retained as printed."))

    # ------------------------------------------------------------------
    # BLOCK D-380 / printed 380 / PDF 401: D1, then Figs 13.20 and 13.21.
    # D1 — continuation of the 13.9.2 paragraph from printed 378.
    b.append(p("the conductors will be a countable fault and Table 13.7 gives values where "
               "they will not fault. If these are not achieved any such breakdown which "
               "leads to a less secure condition will be considered a non-countable fault, "
               "and applied as appropriate to give the worst condition in both normal "
               "operation and the appropriate countable fault scenario. If the distance "
               "between the two conductors is comprised of a mixture of clearance and/or "
               "separation distance it is possible to add the distances, provided that all "
               "component spacings to be added are at least one third of the minimum given "
               "in Tables 13.7 and 13.8 for the type of spacing required if that type of "
               "spacing existed alone at the voltage between the two conductors in question. "
               "The addition is referred to one of three possibilities (clearance, "
               "separation through encapsulant, or separation through solid insulation) by "
               "the use of the multipliers specified in Table 13.9 (based upon Fig. 13.20) "
               "for the voltage between the conductors. Where part of the creepage distance "
               "is coated with a conformal coating, the composite creepage is calculated in "
               "much the same way but using the multipliers in Table 13.10, based upon Fig. "
               "13.21. In the case of creepage, no minimum is applied to either of the two "
               "constituents. The clearances, creepage distances and separations given in "
               "Table 13.8 apply between conducting parts in any intrinsically safe circuit "
               "where"))
    # D1 quirk: D-379.5, D-379.12, D-379.21, D-379.37 (soft hyphens).
    b.append(note("<b>Note on soft-hyphen artefacts in the OCR layer.</b> The text layer "
                  "inserts soft-hyphen line-break artefacts in such words as 'operation', "
                  "'component', 'separation', 'manufacturing', 'clearances' and 'connection'; "
                  "the page render has ordinary whole words. Whole words are used here."))
    # D-380.1 / D-380.6 / D-380.7 — Fig. 13.20 and Fig. 13.21 OCR flattening.
    b.append(fig(20, FD.fig_f1320()))
    b.append(note("<b>Note on Fig. 13.20.</b> The OCR layer flattens the drawing into a word "
                  "list and leaves a stray backslash; the render has distinct in-figure "
                  "labels 'Solid insulation', 'C', 'B', 'A', 'Encapsulant', 'Conductor' and a "
                  "three-line legend A = clearance, B = separation through casting compound, "
                  "C = separation through solid insulation. No text corresponds to the stray "
                  "backslash."))
    b.append(fig(21, FD.fig_f1321()))
    b.append(note("<b>Note on the label of Fig. 13.21.</b> The OCR layer reads the right-hand "
                  "label as lower-case 'insulation'; the render prints 'Insulation' with a "
                  "capital I. The two-line legend defining A = creepage under coating and B "
                  "= creepage in air is retained."))

    # ------------------------------------------------------------------
    # BLOCK D-381 / printed 381 / PDF 402: Tables 13.9 and 13.10 only.
    # D-381.9, D-381.11, D-381.12, D-381.13, quirk B3.
    b.append(table(T3.HEAD139_EN, T3.ROWS139_EN, T3.CAPTION139_EN))
    if T3.NOTE139_EN:
        b.append(note(T3.NOTE139_EN))
    b.append(table(T3.HEAD1310_EN, T3.ROWS1310_EN, T3.CAPTION1310_EN))
    if T3.NOTE1310_EN:
        b.append(note(T3.NOTE1310_EN))
    b.append(note("<b>Note on Tables 13.9 and 13.10.</b> The OCR layer misreads the "
                  "inequality signs as 'o< u 510', '10< U 130', '30~ U 51575' and 'O< U "
                  "51575', and drops the colon in 'Ref Separation Through CC' and 'Ref "
                  "Separation Through SI'; the render gives '0< U ≤10', '10< U ≤30', '30< U "
                  "≤1575', '0< U ≤1575' and 'Ref: ...'. Table 13.9 uses the unit word "
                  "'Volts' in its header while Table 13.10 uses '(V)'; the Table 13.9 note "
                  "prints '1575V' without a space but '15.6 KV' with a space and capital K. "
                  "All forms are retained."))

    # ------------------------------------------------------------------
    # BLOCK D-382 / printed 382 / PDF 403: D2, D3, D4, heading 13.9.3, D6.
    # D2 — continuation of D1.
    b.append(p("failure is required to be a countable fault, such as across the connections "
               "of a diode and between any two separate intrinsically safe circuits where "
               "interconnections at countable fault level have been evaluated and shown not "
               "to produce an unsafe condition. In addition, the figures apply between an "
               "intrinsically safe circuit and a non-intrinsically safe circuit if the "
               "addition of the non-intrinsically safe circuit does not cause an unsafe "
               "condition when it becomes part of the intrinsically safe circuit. This "
               "occurs, typically, in ‘ia’ apparatus, when such a failure at countable fault "
               "level only short circuits part of the current limiting resistance, and hence "
               "is acceptable because of the lower safety factor permitted after the second "
               "countable fault, and between a conductor of an intrinsically safe circuit "
               "and any earthed metal."))
    # D3 — voltage derivation; quirk B8.
    b.append(p("The voltages used to apply Tables 13.7 and 13.8 are the peak voltages which "
               "occur between the two conductors. These are derived as follows, first, in "
               "parts of the same circuit the voltage is the maximum peak voltage which can "
               "be measured between the two parts of the circuit if both voltages come from "
               "the same source or the numerical addition of the two peak voltages if they "
               "come from different sources, except if one of these voltages is less than 20 "
               "per cent of the other it can be ignored. For dc voltages the polarity is "
               "taken into account but the spacings are also required to be acceptable when "
               "the lower of the two voltages is absent. In ac circuits numerical values are "
               "chosen which removes the necessity of determination of phase angles. In "
               "these cases obviously the situation when one voltage is absent it is less "
               "onerous than when both are present. Second, in separate circuits the voltage "
               "is always the numerical addition of the two voltages, for both ac and dc, "
               "unless one is less than 20 per cent of the other as in this case polarities "
               "of dc supplies cannot be guaranteed."))
    b.append(note("<b>Note on the awkward sentence in the print.</b> The print reads 'In "
                  "these cases obviously the situation when one voltage is absent it is less "
                  "onerous than when both are present.' The wording is retained in English. "
                  "The 'less than 20 per cent' rule and the choice of numerical values to "
                  "avoid determining phase angles are also retained."))
    # D4 — voltages, secured conductors; quirk B7, OCR 16.
    b.append(p("Voltages used are the maximum peak value which can occur in an item of "
               "apparatus in either normal or acceptable fault conditions when any electrical "
               "supplies are at their maximum declared values (Uₘ or Uᵢ – see BS/EN 50020), "
               "except that any mains supplies will be considered without the addition of "
               "their supply tolerance. Transiently higher voltages (such as those which "
               "occur during fuse operation and are thus one-offs) are ignored, but if a "
               "transient can occur repeatedly with some degree of regularity it must be "
               "taken into account. In addition, any conductors which are present in the "
               "apparatus need to be secured if insulated to prevent movement causing "
               "chafing or cutting of insulation, and must be moved as far as they can be to "
               "give minimum spacings before spacing measurement. It is accepted that "
               "manufacturing tolerances can further reduce spacings because of "
               "manufacturing tolerances, particularly in the case of printed circuit boards. "
               "Provided these tolerances are less than 10 per cent they may be ignored and "
               "the manufacturers nominal figures taken."))
    b.append(note("<b>Note on the symbols and wording in the print (voltage paragraph).</b> "
                  "The OCR layer reads '(U, or Ui - see BS/EN' but the render prints '(Uₘ or "
                  "Uᵢ – see BS/EN ...)' with subscripts and an en dash. The phrase "
                  "'manufacturing tolerances' is duplicated in 'It is accepted that "
                  "manufacturing tolerances can further reduce spacings because of "
                  "manufacturing tolerances' and is retained verbatim in English."))
    # D5 — heading 13.9.3.
    b.append(h3("13.9.3 Earth conductors and connections (including terminals)",
                "13.9.3 Earth conductors and connections (including terminals)"))
    # D6 — first part, continues on printed 383.
    b.append(p("Earthing is often used in intrinsic safety as a method of ensuring "
               "separation of conductors and parts which would damage intrinsic safety if "
               "they"))

    # ------------------------------------------------------------------
    # BLOCK D-383 / printed 383 / PDF 404: D7-D11.
    # D7 — continuation of D6.
    b.append(p("came into contact. The need for earthing includes the necessity of earthing "
               "conductors, screens, enclosures and safety barriers (these are dealt with "
               "later in this chapter)."))
    # D8.
    b.append(p("Conductors within the apparatus which connect parts to earth need to use "
               "connection methods which are not subject to fault (infallible). The "
               "conductors themselves must also be capable of carrying, without overheating "
               "or damage, the maximum current which could flow in them in both normal "
               "operation and in possible fault conditions."))
    # D9.
    b.append(p("Connectors which carry such earthed connections need to be arranged so that "
               "they do not have the possibility of a disconnection occurring. As normal "
               "plug and socket connections are considered to be countable faults, then "
               "there needs to be redundancy in the connector. This results in a requirement "
               "for two connecting pins for ‘ib’ and three for ‘ia’ connected in parallel. "
               "Figure 13.14 shows how that can be achieved including the necessary layout "
               "in such devices as edge connectors, which can possibly be removed at an "
               "angle. Permanent connections to the item requiring earthing for conductors "
               "transferring such earth connections through plugs and sockets need to be "
               "separate from one another for the same reason, or must be such that they are "
               "not considered to fail. The latter type of permanent connection is dealt "
               "with later in this chapter."))
    # D10.
    b.append(p("Terminals in particular need special consideration if they are to be assumed "
               "not to fail to open circuit and need to satisfy the following requirements:"))
    # D11 — numbered list 1-7.
    b.append(p("1. They must effectively clamp the conductor being terminated to prevent it "
               "from slipping from its intended location, even with temperature changes "
               "expected (normally −20 °C to +40 °C)."))
    b.append(p("2. They must maintain effective electrical connection of the conductor "
               "throughout the range of temperature expected."))
    b.append(p("3. In cases where multistrand conductors are used without first being "
               "crimped in a ferrule there must be an additional clamping plate in the "
               "clamping mechanism (e.g., between the screw and the conductor) to ensure "
               "proper clamping of all strands."))
    b.append(p("4. Terminals which are intended for conductors of maximum cross sections of "
               "4mm² or less must be capable of effectively clamping cross sections smaller "
               "than the maximum for which they are designed. It is probably not necessary "
               "to cover cross sections less than 0.000962mm², which is the minimum for "
               "which a maximum permissible current for temperature classification is "
               "given (see Table 13.4)."))
    b.append(p("5. There must be no sharp edges on terminals which could damage the "
               "conductors being terminated."))
    b.append(p("6. Terminals must not twist or become deformed when normal screw tightening "
               "torques are applied."))
    b.append(p("7. The transmission of pressure to the parts which ensure contact must not "
               "be via any insulating materials."))
    # Quirks 18, 19.
    b.append(note("<b>Note on units and temperature in the terminal list.</b> The print reads "
                  "'(normally −20 °C to +40 °C)' with a minus sign and spaces before °C; the "
                  "OCR layer reads '-20 \"C to +40 \"C'. The print gives '4mm²' and "
                  "'0.000962mm²' without spaces, with a superscript 2; OCR reads '4mm2' and "
                  "'0.000962 mm2'. The printed forms are retained."))

    # ------------------------------------------------------------------
    # BLOCK D-384 / printed 384 / PDF 405: D12, heading 13.9.4, D14-D20.
    # D12.
    b.append(p("An easy way of complying with all of these requirements is to select "
               "terminals for this use, and for any other use where security from "
               "disconnection is required (infallibility) from ranges complying with the "
               "requirements for increased safety ‘e’ (BS/EN 50019) (see Chapter 12)."))
    # Quirk 20.
    b.append(note("<b>Note on the curly single quote in the print.</b> The print writes "
                  "'increased safety ‘e’ (BS/EN 50019)'; the OCR layer misreads it as "
                  "'increased safety 'er (BS/EN 50019)' with a stray r. The curly quote is "
                  "retained."))
    # D13 — heading 13.9.4.
    b.append(h3("13.9.4 Encapsulation", "13.9.4 Encapsulation"))
    # D14.
    b.append(p("Encapsulation can be used for two reasons. It may be necessary to enlarge "
               "the surface area of a component in intrinsically safe apparatus to lower the "
               "surface temperature where the energy within the encapsulant is intrinsically "
               "safe, or it may be used to exclude an explosive atmosphere from a component "
               "from an intrinsically safe circuit where energy levels are incendive (e.g., "
               "the connection between an inductor and its suppression components). The "
               "minimum requirements for the encapsulant are the same in both cases but, in "
               "the case of temperature limitation, the amount and thickness of the "
               "encapsulant must be such as to achieve the necessary temperature limitation "
               "if this requires thicker encapsulant."))
    b.append(note("<b>Note on the repeated 'from' in the print.</b> The print reads 'to "
                  "exclude an explosive atmosphere from a component from an intrinsically "
                  "safe circuit' — the word 'from' is duplicated in the original and is "
                  "retained verbatim in English."))
    # D15.
    b.append(p("The encapsulant must satisfy the following requirements in both "
               "intrinsically safe apparatus and in associated apparatus, although in this "
               "latter case encapsulant would only be used to maintain spacings. First, it "
               "must adhere to the components and/or circuits being encapsulated where they "
               "exit the encapsulant. This is necessary because creepage distances are not "
               "measured within encapsulant on the basis that contamination cannot enter, "
               "and if the encapsulant did not adhere to the encapsulated parts in such "
               "cases the contamination could enter which is not acceptable."))
    # D16.
    b.append(p("Second, where bare conductors exit the encapsulant the encapsulant must "
               "have the necessary CTI to protect the creepage distances across its surface."))
    # D17.
    b.append(p("Third, the encapsulant must also have an operating temperature range "
               "specification which ensures that it is not damaged by temperatures reached "
               "during operation in both normal and possible fault conditions through the "
               "temperature range for which the apparatus is designed (normally −20 °C to "
               "+40 °C). Alternatively, if the encapsulant is shown not to be damaged within "
               "this temperature range by tests then it will be acceptable, even if it is "
               "operated outside its specification."))
    # D18.
    b.append(p("Fourth, where the surface of the encapsulant forms part of the outer "
               "enclosure of the apparatus it must be a hard (rigid) encapsulant, such as "
               "epoxy resin."))
    # D19.
    b.append(p("Fifth, where the encapsulant has no enclosure, its minimum thickness between "
               "any encapsulated component and assembly and its free surface (see Fig. "
               "13.22) must satisfy half of the minimums specified for the voltage of the "
               "component or assembly with a minimum of 1 mm."))
    # D20.
    b.append(p("Finally, where the encapsulant is within an enclosure there is no minimum "
               "thickness of encapsulant if the enclosure is of insulating material, but if "
               "the enclosure is of conducting material the thickness is determined by that "
               "required to prevent any earth connection which could damage intrinsic "
               "safety."))

    # ------------------------------------------------------------------
    # BLOCK D-385 / printed 385 / PDF 406: Fig. 13.22, heading 13.10, D22.
    # D-385.23, quirks B13, B16.
    b.append(fig(22, FD.fig_f1322()))
    b.append(note("<b>Note on the Fig. 13.22 caption.</b> The OCR layer scrambles the drawing "
                  "into a word list ('penterate', 'EncaDsulant', a stray backslash); the "
                  "render gives four separate cross-sections with the labels 'Free surface', "
                  "'Encapsulant (Note 1)', 'Enclosure (Note 2)' and 'Encapsulant (no minimum "
                  "thickness) (Note 3)', plus the combined label 'Enclosure (Note 2 &amp; 3)'. "
                  "Note (2) prints 'Metal has no minimum thickness but insulating material "
                  "must conform to the thickness for separation purposes (Table 13.7)' and "
                  "is retained even though it appears to invert the usual expectation; the "
                  "caption ends with 'intrinsic safety' and no terminal full stop, as "
                  "printed."))
    # D21 — heading 13.10.
    b.append(h3("13.10 Infallible components, assemblies and construction elements",
                "13.10 Infallible components, assemblies and construction elements"))
    # D22 — first part, continues on printed 386.
    b.append(p("As is by now clear, intrinsic safety includes, in its evaluation, failures "
               "of components and other circuit elements in two ways, where such failures "
               "reduce security. Those which reach a specific level of construction "
               "excellence are considered to fail only as part of a limited fault count and "
               "those which do"))

    # ------------------------------------------------------------------
    # BLOCK D-386 / printed 386 / PDF 407: D23-D26, heading 13.10.1, D28,
    # heading "Mains transformer construction", D30.
    # D23 — continuation of D22.
    b.append(p("not reach this level are considered to fail in any event if such failure "
               "makes the circuits more ignition capable. There is a third level to be "
               "considered which is that level where construction and rating is of such a "
               "high level that failures can be ignored. In components, assemblies of "
               "components, and connection elements this level of excellence warrants the "
               "award of the title of infallible component, assembly or connection. Such "
               "things as separations can also reach a level where failure need not be "
               "considered (see Table 13.7) but in this case they are termed as ‘not subject "
               "to fault’ and Infallible is not used. In any event, the results are the same "
               "and when carrying out a fault-counting exercise specific failure modes in "
               "any of these components, assemblies, wiring, connections and separations "
               "need not be considered."))
    # Quirks 24, 25, B10, B11.
    b.append(note("<b>Note on ‘infallible’ and ‘not subject to fault’.</b> The OCR layer "
                  "misreads the closing quotes of 'not subject to fault' as opening quotes; "
                  "the render prints ‘not subject to fault’ and ‘infallible’ with curly "
                  "single quotes. The print writes 'Infallible is not used' with a capital I "
                  "mid-sentence, and begins the next paragraph with 'Infallible components "
                  "...'; the forms are retained."))
    # D24.
    b.append(p("In all cases the infallibility of such components, assemblies, wiring, "
               "connections and separations is limited to the particular mode of failure "
               "which their construction permits to be ignored (e.g., the separation of a "
               "pair of printed circuit tracks may make them such that connections between "
               "them can be assumed not to occur, but it will not have any effect upon "
               "consideration of their breakage)."))
    # D25.
    b.append(p("While it is confusing to have the two terms ‘infallible’ and ‘not subject to "
               "fault’ applied to particular failure modes of components and other circuit "
               "elements, the use of either term is understood to impart the same "
               "information and no danger should result."))
    # D26.
    b.append(p("Infallible components, assemblies and arrangements which are considered as "
               "not subject to particular fault conditions need to comply with specific "
               "requirements which are additional to the basic constructional requirements "
               "of the protection concept which give countable fault status (see Sections "
               "13.7 and 13.8)."))
    # D27 — heading 13.10.1.
    b.append(h3("13.10.1 Infallible transformers", "13.10.1 Infallible transformers"))
    # D28.
    b.append(p("Clearly, mains transformers, used in associated apparatus to reduce voltage "
               "to the normal low levels used in intrinsically safe circuits, are important "
               "as failure of the windings associated with that circuit to the mains winding "
               "or other auxiliary windings on the transformer associated with other "
               "intrinsically safe circuits or non-intrinsically safe circuits, would lead to "
               "a situation where intrinsic safety was compromised. Such a transformer needs "
               "to be infallible against such interconnections both in normal operation and "
               "in failure conditions. In addition, where failure of windings associated with "
               "the intrinsically safe circuit to the core of the transformer, which is "
               "normally earthed, could produce an ignition-capable condition, the "
               "transformer must be infallible against that failure also. The requirements "
               "for such transformers are as follows."))
    # D29 — unnumbered heading.
    b.append(h4("Mains transformer construction", "Mains transformer construction"))
    # D30 — first part, continues on printed 387.
    b.append(p("Several modes of construction are envisaged for mains transformers in "
               "BS/EN 50020 and are given type numbers. The simplest of these is the"))

    # ------------------------------------------------------------------
    # BLOCK D-387 / printed 387 / PDF 408: Table 13.11, D31, heading Type 2b,
    # D33, items 1 and 2 (first part).
    # D-387.26, quirks B4, B5.
    b.append(table(T3.HEAD1311_EN, T3.ROWS1311_EN, T3.CAPTION1311_EN))
    if T3.NOTE1311_EN:
        b.append(note(T3.NOTE1311_EN))
    b.append(note("<b>Note on Table 13.11.</b> The OCR layer reads '1 .o' instead of 1.0; the "
                  "attribution prints '(from BSEN 50020)' with no slash, unlike the 'BS/EN "
                  "50020' used in the prose. Note 1 is redundant in the original ('a "
                  "tolerance of up to 10% manufacturing tolerance') and its wording is "
                  "retained."))
    # D31 — continuation of D30; quirk B6.
    b.append(p("type where the transformer is permitted to exceed its insulation ratings but "
               "a failure between non-intrinsically safe circuit windings and other windings "
               "is prevented by an earthed metal screen of thickness complying with Table "
               "13.11. This is termed a ‘Type 2b transformer and its principles of "
               "construction are shown in Fig. 13.23."))
    b.append(note("<b>Note on the unclosed quote in the print.</b> The print reads 'This is "
                  "termed a ‘Type 2b transformer and its principles of construction are "
                  "shown in Fig. 13.23.' — an opening curly quote with no closing quote. "
                  "This is a source error and is retained verbatim in English; the OCR layer "
                  "agrees but uses a straight quote."))
    # D32 — unnumbered heading.
    b.append(h4("Type 2b transformer", "Type 2b transformer"))
    # D33.
    b.append(p("The Type 2b transformer is normally a ‘shell type’ transformer (see Fig. "
               "13.23) with its windings over one another on a single bobbin, or without a "
               "bobbin, but consolidated in both cases on a single core so that any "
               "separations are reliable and repeatable. The screen must be the full width "
               "of the winding area to ensure that no possibility exists for interconnection "
               "across the screen except at the outer edge of the windings where Table 13.7 "
               "applies. In either case the insulation or other separation between the "
               "windings associated with intrinsically safe circuits and the core, the screen "
               "and the other windings must ensure that the transformer satisfies the "
               "following as a minimum:"))
    # D34 — numbered item 1.
    b.append(p("1. The composite separation between the winding mass of the separate "
               "windings around the screen must satisfy the requirements of Table 13.7. (In "
               "most cases this will require a composite calculation of separation distance "
               "– see Figs. 13.20 and 13.21)."))
    # D35 — numbered item 2, first part; continues on printed 388.
    b.append(p("2. The screen must be of either a single layer of foil which comprises at "
               "least one turn and overlaps but is insulated so that the ends of the screen "
               "cannot become interconnected, or of two layers wound in insulated (varnished) "
               "wire. For a foil screen this requirement is to avoid the screen ends becoming"))

    # ------------------------------------------------------------------
    # BLOCK D-388 / printed 388 / PDF 409: Fig. 13.23, D36, D37.
    # D-388.28, D-388.29, quirks B11, B16, B17.
    b.append(fig(23, FD.fig_f1323()))
    b.append(note("<b>Note on the Fig. 13.23 caption.</b> The OCR layer mixes the caption "
                  "into the drawing text; the render gives a separate caption with five "
                  "notes. Note (3) prints 'normal industrial requirements' while Figs 13.24 "
                  "and 13.25 print 'normal industrial standards'; note (4) prints 'withstand "
                  "500V test' with no space between the number and V. The caption ends with "
                  "'Windings to be consolidated' and no terminal full stop, as printed."))
    # D36 — continuation of item 2; quirk 30.
    b.append(p("connected to form a short circuited turn which will cause the transformer to "
               "fail. For a wire screen, insulation between each turn of wire and between the "
               "two layers is necessary for the same reason. Because of this, the only "
               "insulation requirement between layers is that the insulation will not fail "
               "when subjected to an insulation test at an applied voltage of 500Vrms ac or "
               "700 V dc. The voltage is applied by raising the applied voltage steadily so "
               "that the specified value is attained after 10 seconds and then maintaining "
               "that value for 60 seconds. The leakage current should be less than 5mA and "
               "must be constant or reducing as any increase will be assumed to be advance "
               "warning of insulation failure."))
    b.append(note("<b>Note on the test voltage in the print.</b> The print reads 'an applied "
                  "voltage of 500Vrms ac or 700 V dc' — no space in '500Vrms' but a space "
                  "before '700 V'. The OCR layer agrees; the form is retained."))
    # D37 — numbered item 3, first part; quirks 31, 32, B22.
    b.append(p("3. The transformer must not create a condition where the winding/s associated "
               "with a particular intrinsically safe circuit become connected to other "
               "windings. To prove this a test is applied where one (any one) of the output "
               "windings of the transformer is short circuited and then all other output "
               "windings are subjected to a load which will produce maximum rated current "
               "from that winding at rated voltage. The transformer then is subjected to "
               "application of its rated voltage at the input winding or such smaller "
               "voltage, as will give 1.7Iₙ into the transformer. This condition is applied "
               "for 6 hours or until the transformer fails. The criteria for insulation is "
               "that when a voltage of twice the transformer rated voltage (Uₙ) plus 1000 V "
               "with a minimum of 1500 V is applied between the windings in question, the "
               "current which flows should not exceed 5mA and should be"))
    b.append(note("<b>Note on the current symbols in the print.</b> The OCR layer reads "
                  "'l.71n' but the render prints '1.7Iₙ' (letter I, subscript n, no internal "
                  "space); likewise '(U,)' becomes '(Uₙ)' and '1OOOV' becomes '1000 V'. The "
                  "print uses '1.7Iₙ' here but '1.7 Iₙ' in later paragraphs — the inconsistent "
                  "spacing is retained at each occurrence."))

    # ------------------------------------------------------------------
    # BLOCK D-389 / printed 389 / PDF 410: D38, items 4-7, heading Type 1a,
    # D44, D45.
    # D38 — continuation of item 3.
    b.append(p("constant or falling. The transformer may fail during this test but must not "
               "burst into flames as burning may introduce further consequent failures."))
    # D39 — numbered item 4.
    b.append(p("4. Where failure to earth may cause problems for the intrinsically safe "
               "circuit, failure of the transformer must not occur and the transformer must "
               "not exceed its temperature rating during the above test. This can be achieved "
               "by the use of in-built thermal trips as already described or by the inclusion "
               "of a limiting resistor to limit current in the transformer. Where "
               "automatically resetting trips are used, rather than non-resetting trips, the "
               "test is extended to 12 hours to allow for repeated trip operations. Where a "
               "resistor is fitted it will be mounted in the input circuit of the transformer "
               "and must satisfy the separation requirements of Table 13.7, be of adequate "
               "rating (see earlier in this chapter), and be infallible as described later. "
               "The separation of the winding/s supplying the intrinsically safe circuit "
               "and other windings and the screen must in this case satisfy Table 13.7. The "
               "possible effect of failures to earth is shown in the example in Fig. 13.24."))
    # D40 — numbered item 5.
    b.append(p("5. Where the screen is of two separate layers of winding each layer should be "
               "individually connected to earth and provision made for this on the "
               "transformer. Where the screen is a foil it must have two separate wires "
               "connected to it to allow the same security of earth connection and care is "
               "necessary to ensure that connection of these wires does not introduce a "
               "partial short circuit turn on the transformer."))
    # D41 — numbered item 6.
    b.append(p("6. The core of the transformer must also be earthed and its construction "
               "should allow for this. This is usually done by interleaving a conducting "
               "strip in the laminations and then providing a terminal on it where it exits "
               "the laminations. Some transformer materials, such as ferrites, may be "
               "insulating in themselves and in such cases the earth connections are not "
               "necessary. It would not be acceptable, however, to insulate a conducting "
               "core and not earth it unless the insulation thickness satisfied Table 13.10 "
               "and the transformer was prevented from overheating as previously described."))
    # D42 — numbered item 7.
    b.append(p("7. The separation of the connection facilities should also comply with the "
               "requirements of Table 13.10 to prevent interconnections at the termination "
               "points."))
    # D43 — unnumbered heading; quirks 33, 34, B1.
    b.append(h4("Type 1a, 1b and 2a transformers", "Type 1a, 1b and 2a transformers"))
    b.append(note("<b>Note on the transformer type numbers.</b> The print uses the digit one, "
                  "not the letter ell: 'Type 1a', 'Type 1b', 'Type 2a', 'Type 2b' and the "
                  "heading 'Type 1a, 1b and 2a transformers'. The OCR layer reads 'Type la', "
                  "'Type lb', 'Type 7b'; the digit forms are retained in both languages."))
    # D44.
    b.append(p("The other types of transformer envisaged are the Type 1a transformer, the "
               "Type 1b transformer, and the Type 2a transformer. The Type 1a transformer has "
               "its windings wound side by side on one limb of the transformer and the Type "
               "1b transformer follows the same construction but has the separate windings "
               "on separate limbs of the transformer, but still as separate entities (not one "
               "over the other)."))
    # D45; quirk 35, B11.
    b.append(p("The Type 1b transformer is more common as it uses a ‘shell type’ core where "
               "one limb goes through the winding and the two other limbs surround it, rather "
               "than the Type 1a transformer which normally has a ‘core type’ core with one "
               "limb through each winding and usually no surrounding limbs."))
    b.append(note("<b>Note on the curly quotes in the construction names.</b> The print uses "
                  "‘shell type’ and ‘core type’ with curly single quotes; the OCR layer "
                  "sometimes reads a closing quote as an opening one. The printed forms are "
                  "retained in English."))

    # ------------------------------------------------------------------
    # BLOCK D-390 / printed 390 / PDF 411: D46, Fig. 13.24, Fig. 13.25.
    # D46.
    b.append(p("The Type 2a transformer is similar to the Type 2b transformer, but in this "
               "case there is no screen with the windings being on top of one another and "
               "having insulation between them. The insulation must, of course, be the full "
               "width of the winding area (see Fig. 13.24) to prevent the presence of a path "
               "through it except around the outside edge of the winding where Table 13.7 "
               "applies."))
    # D-390.36, D-390.37, quirks B14, B17, B18.
    b.append(fig(24, FD.fig_f1324()))
    b.append(fig(25, FD.fig_f1325()))
    b.append(note("<b>Note on the captions of Figs 13.24 and 13.25.</b> The OCR layer reads "
                  "'Type la'/'Type lb' in the captions and splits 'connection' at the line "
                  "end; the render "
                  "prints 'Type 1a'/'Type 1b' and 'connection'. Note (2) of both prints "
                  "'normal industrial standards' (plural), unlike 'normal industrial "
                  "requirements' in Fig. 13.23. Fig. 13.24 cites 'Table 13.10' in notes (3)/(5) "
                  "while Fig. 13.25 cites 'Table 13.7' in the corresponding notes — the "
                  "difference is as printed and is not harmonised. Both captions end with "
                  "'Windings to be consolidated' and no terminal full stop."))

    # ------------------------------------------------------------------
    # BLOCK D-391 / printed 391 / PDF 412: Fig. 13.26, D47, D48, heading,
    # D50.
    # D-391.38, D-391.39, quirks B14, B15, B16.
    b.append(fig(26, FD.fig_f1326()))
    b.append(note("<b>Note on the Fig. 13.26 caption.</b> The OCR layer splits the caption "
                  "'Fig. 13.26 · Type 2a transformer' and reads 'Types la, lb and 2a'; the "
                  "render joins it into one line and prints 'Types 1a, 1b and 2a'. Note 1 "
                  "reads 'unless material is non-conducting', omitting the word 'core' present "
                  "in the parallel notes of Figs 13.24 and 13.25; note 4 reads 'If necessary "
                  "to prevent overheating thermal trip embedded in primary or secondary "
                  "winding (as appropriate).' with no comma after 'overheating' or in the "
                  "parenthesis. The caption has no terminal full stop. All forms are "
                  "retained as printed."))
    # D47; quirk B19.
    b.append(p("In all these cases the transformer must have its windings consolidated and "
               "must not fail when subjected to type tests described for Type 2b transformers, "
               "which almost invariably means that a thermal trip or limiting resistor is "
               "needed as in the case of most Type 2b transformers. The thickness of "
               "insulation between each winding and others, or the earthed core of the "
               "transformer (if earthing causes a problem) must satisfy Table 13.7. Detail of "
               "the construction of Types 1a, 1b and 2a transformers are shown in Fig. 13.24, "
               "13.25 and 13.26."))
    b.append(note("<b>Note on 'Detail ... are shown'.</b> The print reads 'Detail of the "
                  "construction of Types 1a, 1b and 2a transformers are shown in Fig. 13.24, "
                  "13.25 and 13.26.' — the singular 'Detail' is followed by 'are'. The OCR "
                  "layer reads 'Types la, lb and 2a'; the digit-one forms are retained. The "
                  "sentence is retained verbatim in English."))
    # D48.
    b.append(p("As transformers being wound and generally assembled components are subject "
               "to a higher degree of variability than other more critically controlled "
               "components a routine test is necessary and this test is described in Table "
               "13.12."))
    # D49 — unnumbered heading.
    b.append(h4("Construction of transformers which are not mains transformers",
                "Construction of transformers which are not mains transformers"))
    # D50 — first part, continues on printed 392; quirk B20.
    b.append(p("Within intrinsically safe circuits it is common to use transformers for other "
               "purposes (e.g., to produce galvanic isolation between parts of the circuit). "
               "Such transformers must be constructed in accordance with the mains "
               "transformer requirements except that the 5-hour test need only be done at "
               "rated transformer load. Where such transformers are connected between"))
    b.append(note("<b>Note on '5-hour'.</b> The print writes 'the 5-hour test need only be "
                  "done at rated transformer load' with a hyphen between the numeral and the "
                  "word; the form is retained in English."))

    # ------------------------------------------------------------------
    # BLOCK D-392 / printed 392 / PDF 413: Fig. 13.27, Table 13.12, D51.
    # D-392.40, D-392.41, quirk B16.
    b.append(fig(27, FD.fig_f1327()))
    b.append(note("<b>Note on the Fig. 13.27 caption.</b> The OCR layer reads 'windingkore' "
                  "and 'secondaty/frame' but the render prints 'winding/core' and "
                  "'secondary/frame'; the items 'limiting resistor Ij,' and 'LP' are OCR "
                  "artefacts and do not appear in the drawing. The caption ends with "
                  "'intrinsic safety intact' and no terminal full stop, as printed."))
    # D-392.42, quirks B21, B22.
    b.append(table(T3.HEAD1312_EN, T3.ROWS1312_EN, T3.CAPTION1312_EN))
    if T3.NOTE1312_EN:
        b.append(note(T3.NOTE1312_EN))
    b.append(note("<b>Note on Table 13.12.</b> The OCR layer reads '4 U,, or 2000 V rms' and "
                  "'2 u,, + 1000 v rms'; the render prints '4 Uₙ or 2000 V rms' and '2 Uₙ + "
                  "1000 V rms' with a subscript U. The third cell capitalises 'Intrinsically "
                  "Safe' while the surrounding prose uses lower case; the second and third "
                  "cells end with a full stop. The current '5mA' is printed without a space "
                  "before the unit. All forms are retained as printed."))
    # D51 — continuation of D50, continues on printed 393.
    b.append(p("intrinsically safe and non-intrinsically safe circuits there is, however, a "
               "further problem in that the non-intrinsically safe circuits are not evaluated "
               "and it must be assumed that mains can break through to the transformer. In "
               "such cases it is necessary to introduce measures to prevent this causing "
               "damage to the transformer. Such precautions could be those applied to"))

    # ------------------------------------------------------------------
    # BLOCK D-393 / printed 393 / PDF 414: D52, heading Transformer
    # protection, D54-D59.
    # D52 — continuation of D51.
    b.append(p("mains transformers of the same type or, alternatively, by placing a shunt "
               "zener diode across the affected winding and then protecting the diode with a "
               "suitably rated fuse to ensure that the mains breakthrough is removed before "
               "the transformer or zener diode can be damaged. The requirements of Table 13.7 "
               "need to be applied to this fuse/zener combination to ensure it cannot be "
               "by-passed."))
    # D53 — unnumbered heading.
    b.append(h4("Transformer protection", "Transformer protection"))
    # D54.
    b.append(p("To ensure that no failures occur it is essential that the transformer cannot "
               "be operated in such a way as to allow those failures. This necessitates "
               "protection of the transformer in a way which allows its worst case conditions "
               "to be defined. All mains transformers have to be supplied with an input fuse "
               "to remove the mains supplies if failures occur either in the transformers "
               "themselves or the connected circuits."))
    # D55.
    b.append(p("The basic level of protection is to fuse the input circuit so that the "
               "maximum design operating conditions of the transformer specified during its "
               "design cannot be exceeded. As the transformer can handle these without "
               "causing problems in the intrinsically safe circuit, it can be considered as "
               "infallible."))
    # D56; quirk 43, B22.
    b.append(p("The fuse must comply with the requirements already described in Section "
               "13.6.2 for fuses mounted in associated apparatus, which means that the "
               "maximum current which the transformer can continuously draw is, with the "
               "presence of such a fuse, considered as 1.7 times the rated fuse current (Iₙ). "
               "A suitably rated circuit breaker may be used in place of a fuse and the "
               "circuit breaker need only comply with a recognized standard of construction "
               "for such circuit breakers. The 1.7 Iₙ figure is retained and in this case is "
               "1.7 times the rated current at which the breaker will operate. Therefore, the "
               "transformer must be capable of withstanding this current without damage, "
               "which could adversely affect intrinsic safety."))
    b.append(note("<b>Note on the Iₙ symbols.</b> The OCR layer reads '(In)', '1.7 I,' and "
                  "'(1.7 I,)'; the render prints '(Iₙ)', '1.7 Iₙ' and '(1.7 Iₙ)'. The "
                  "inconsistent spacing between '1.7Iₙ' (earlier), '1.7 Iₙ' and '1.7 times "
                  "the rated fuse current (Iₙ)' here is retained at each occurrence."))
    # D57; quirk B23.
    b.append(p("The basic requirements of circuit breakers is that they comply with a "
               "recognized Standard which normally is taken to mean a European Standard, a "
               "harmonized International Standard or, failing the presence of either of "
               "these, a National Standard."))
    b.append(note("<b>Note on grammar and spelling in the print.</b> The print reads 'The "
                  "basic requirements of circuit breakers is that they comply ...' — the "
                  "plural 'requirements' is followed by 'is'. The American spellings "
                  "'recognized', 'harmonized' and 'minimize' are in the original and are not "
                  "converted to -ised."))
    # D58.
    b.append(p("The use of the fuse or circuit breaker described above is usually sufficient "
               "for transformers of Type 2b construction unless winding faults between the "
               "transformer windings and core or screen are not acceptable when, in common "
               "with Types 1a, 1b and 2a transformers, the current which the fuse will pass "
               "(1.7 Iₙ) must not additionally allow the winding temperatures to exceed their "
               "insulation rating. In circumstances where this can occur a thermal trip will "
               "be necessary to ensure this does not occur."))
    # D59 — first part, continues on printed 394; quirk B24.
    b.append(p("Where such a thermal trip is used to disconnect the transformer from its "
               "supplies before winding temperatures are exceeded it must not be accessible. "
               "It must be embedded, in or consolidated with, the windings so that confidence "
               "is present that it will reliably disconnect before any winding or other "
               "insulation within the transformer exceeds its rated limit. The trip may be "
               "non-resettable or automatically self-resetting but not manually reset as this "
               "implies external intervention which would not be acceptable as it"))

    # ------------------------------------------------------------------
    # BLOCK D-394 / printed 394 / PDF 415: D60-D63, heading 13.10.2, D65,
    # heading 13.10.3, D67 (partial).
    # D60 — continuation of D59.
    b.append(p("would permit resetting before the transformer could cool, and the possibility "
               "exists of the temperature limits of the construction being exceeded. Only "
               "one such device is necessary."))
    b.append(note("<b>Note on the page-break continuation.</b> The paragraph above ends "
                  "mid-sentence with '...which would not be acceptable as it' on printed p.393 "
                  "and continues on printed p.394 with 'would permit resetting before the "
                  "transformer could cool ...'. The boundary is kept as printed."))
    # D61; quirk B25.
    b.append(p("The constructional requirements for such a thermal trip are that it should be "
               "to a recognized Standard for such devices. (Recognized Standard in this "
               "context usually means a European Standard where one exists, a harmonized "
               "International Standard or, failing either of these, a national Standard)."))
    b.append(note("<b>Note on capitalisation in 'national Standard'.</b> This paragraph "
                  "writes 'a national Standard' with a lower-case n, whereas the preceding "
                  "paragraph writes 'a National Standard' with a capital N. The difference "
                  "is retained."))
    # D62; quirk 44, B26.
    b.append(p("Where the transformer is possessed of a suitable earthed screen it is not "
               "essential to ensure that insulation temperature limits are not exceeded if "
               "earth faults within the transformer do not cause problems. It must be "
               "remembered that, in the UK, the normal mains supplies are earthed as a matter "
               "of policy for personnel protection by connection of the neutral pole of the "
               "supply to earth at the point of supply origination. This means that in the "
               "case of a fault in the transformer any supply pole could be earthed. To "
               "ensure that the supply is effectively isolated on such failures all "
               "non-earthed electrical supply conductors must have a fuse or circuit breaker "
               "satisfying the already specified requirements."))
    b.append(note("<b>Note on 'possessed of' and one OCR error.</b> The print reads 'Where the "
                  "transformer is possessed of a suitable earthed screen ...'; this is the "
                  "original wording. The OCR layer reads 'satisfymg' but the render prints "
                  "'satisfying' in 'satisfying the already specified requirements'."))
    # D63.
    b.append(p("In cases where it is not considered necessary to include transformer "
               "winding/earth faults in the fault scenario and the power supply is not "
               "referenced to earth (which is the case in some other countries), only one "
               "protection device in the input circuit may be necessary as failure to earth "
               "of a single supply conductor does not cause the same type of problem as it "
               "may where the supply is referenced to earth. An evaluation of the possible "
               "fault scenarios shows that, even if the fault combination envisaged within "
               "the intrinsic safety concept does not include a situation of by-passing "
               "protection devices, the more remote possibility of this occurring is enough "
               "to produce a recommendation that all non-earthed supply conductors have a "
               "protective device, regardless of the type of transformer used and its "
               "supply."))
    # D64 — heading 13.10.2.
    b.append(h3("13.10.2 Damping windings", "13.10.2 Damping windings"))
    # D65.
    b.append(p("Damping windings are used to minimize the effects of inductance in cases such "
               "as relays. They are effectively short circuit turns and reduce the apparent "
               "inductance to the leakage inductance which represents the inverse of the "
               "efficiency of coupling between them and the main winding. If such windings "
               "are used to minimize inductance for the purposes of intrinsic safety, they "
               "must be reliable so that they can be considered as infallible against open "
               "circuit failure. The typical way to ensure this is to use uninsulated copper "
               "tubes or wires which are continuously short circuited by soldering or "
               "welding. Any winding used for this purpose needs to achieve this level of "
               "security against open circuiting."))
    # D66 — heading 13.10.3; quirk 45.
    b.append(h3("13.10.3 Current limiting resistors", "13.10.3 Current limiting resistors"))
    b.append(note("<b>Note on the number 13.10.3.</b> The OCR layer reads '73.10.3 Current "
                  "limiting resistors'; the render prints '13.10.3 Current limiting "
                  "resistors'. The correct printed number is used in both languages."))
    # D67 — partial, continues on printed 395 (outside this module).
    b.append(p("Current limiting resistors are typically used to limit short circuit current "
               "to a hazardous area, to limit the current which can be fed to an inductor, to "
               "limit"))
    # Quirk 46, B27.
    b.append(note("<b>Note on the module boundaries and unresolved cross-references.</b> This "
                  "module begins mid-sentence in 13.9.2 (from printed p.378) and ends "
                  "mid-sentence in 13.10.3 on printed p.394; the continuation is in module E. "
                  "The references 'Table 13.7', 'Table 13.4', 'Figure 13.14', 'Section 13.6.2', "
                  "'Sections 13.7 and 13.8', 'BS/EN 50020', 'BS/EN 50019' and 'Chapter 12' "
                  "remain unresolved here, as printed. The === PAGE 416 === marker is at raw "
                  "line 17208 (not 17254 as stated in the brief)."))
    return "".join(b)
