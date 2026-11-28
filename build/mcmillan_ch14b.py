# -*- coding: utf-8 -*-
"""Chapter 14, module B - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 437-446 (PDF pp. 458-467).

Covers the continuation of the test-voltage paragraph from printed p. 436,
sections 14.4-14.4.5 (non-sparking apparatus, luminaires, low-power
apparatus) and 14.5-14.5.2 (arcing/sparking apparatus, enclosed break
devices, non-incendive components, hermetically sealed devices). Figures
14.1-14.4 and Tables 14.4-14.5 are embedded in printed order. The chapter
shell owns the chapter h2, the printed references, the glossary, the
source-quirk note and the copyright.

Printed quirks are kept in the English text (premiss, machmes, tₑ, the
unclosed quotes, 'where have access is needed', '60Vrms', the conditioning
values, 'as it normally operated at low voltage and power', '660V', '15A',
'In Type ‘N, however', 'a single large production of bubbles', and the
OCR-vs-render fixes for 14.5.1 and 14.5.2) with bilingual notes; the
Vietnamese follows the intended meaning. This is an unofficial study
translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, table, fig, ul, ol
import mcmillanfig14 as F
import mcmillan_tbl14_4_5 as T2


def body_vi():
    b = []

    # Survey quirk 0 - the assignment's original line anchor.
    b.append(note("<b>Lưu ý về mốc dòng được giao.</b> Đề bài ban đầu đặt "
                  "'=== PAGE 458 ===' ở dòng thô 18939; thực tế dòng 18939 là "
                  "'=== PAGE 459 ==='. Điểm bắt đầu đúng của PDF trang 458 "
                  "(trang in 437) là dòng thô 18896 và phạm vi được giao "
                  "kết thúc ở dòng 19275, với '=== PAGE 468 ===' ở dòng "
                  "19276. Mô-đun này theo phạm vi đã hiệu chỉnh 18896–19275."))

    # B1 (raw 18898-18900; continuation of a paragraph from printed 436).
    b.append(p("Tất cả các điện áp thử nghiệm nêu trên đều là giá trị tối "
               "thiểu và không cần thiết phải kiểm soát điện áp nhiều hơn "
               "là chỉ bảo đảm rằng nó không vượt quá +5 phần trăm của con "
               "số này."))
    b.append(note("<b>Lưu ý về đoạn mở đầu.</b> Đoạn 'Tất cả các điện áp "
                  "thử nghiệm nêu trên...' bắt đầu ở trang in 437 như phần "
                  "tiếp nối của văn bản từ trang in 436 nằm ngoài phạm vi "
                  "mô-đun này. Đoạn được giữ ở dạng chưa trọn vẹn ở đầu như "
                  "bản in."))

    # Heading 14.4 (printed 437).
    b.append(h3("14.4 Yêu cầu bổ sung cho một số loại thiết bị không phát "
                "tia lửa",
                "14.4 Additional requirements for certain types of "
                "non-sparking apparatus"))
    # B3 (raw 18903-18906).
    b.append(p("Tiếp nối chủ đề rằng các yêu cầu cơ bản đối với thiết bị "
               "Kiểu ‘N’ là các yêu cầu công nghiệp bình thường sẽ tạo ra "
               "một thiết bị đáng tin cậy, chỉ có một tập hợp hạn chế các "
               "yêu cầu bổ sung được áp dụng cho các thiết bị cụ thể."))

    # Heading 14.4.1 (printed 437).
    b.append(h3("14.4.1 Máy điện quay", "14.4.1 Rotating electrical machines"))
    # B5 (raw 18908-18926, continues on printed 438).
    b.append(p("Cả BS 6941⁸ và IEC 79-15¹¹ đều đặt tiền đề ban đầu rằng các "
               "máy phải đáp ứng các Tiêu chuẩn công nghiệp cơ bản, tiêu "
               "chuẩn liên quan ở Vương quốc Anh là BS 5000, Phần 16⁹, trong "
               "đó nêu chi tiết các máy Kiểu ‘N’, còn Tiêu chuẩn quốc tế là "
               "IEC 34¹⁷, một tiêu chuẩn tổng quát hơn cho các máy điện quay. "
               "Tài liệu IEC là tài liệu tổng quát hơn, để dành các bổ sung "
               "đặc biệt cho Kiểu ‘n’ trong IEC 79-15¹¹. Những vấn đề cơ bản "
               "cần xem xét là chẳng hạn như độ an toàn khi lắp các thanh "
               "rôto, vỏ bọc, v.v. Cũng như các máy Kiểu ‘e’, các thanh rôto "
               "được yêu cầu phải được cố định trong các rãnh sao cho giảm "
               "thiểu khả năng dịch chuyển của chúng và do đó sinh tia lửa. "
               "Các phương pháp cố định tương tự như đối với máy Kiểu ‘e’ "
               "(ví dụ, nhôm đúc, v.v.) được đề xuất là phù hợp và tia lửa "
               "có thể phát sinh cần được giải quyết, như đối với Kiểu ‘e’, "
               "trong cả khi khởi động và khi chạy. Mũ che quạt phải được "
               "chế tạo sao cho giảm nguy cơ hư hỏng gây tiếp xúc với quạt "
               "và, ngoài việc chịu được các thử nghiệm va đập cho Kiểu ‘N "
               "như đã mô tả ở trên, khe hở khi chạy giữa chúng và quạt được "
               "bao bọc phải có giá trị cơ bản ít nhất là 1 phần trăm đường "
               "kính quạt. Có giới hạn cho việc này ở chỗ khe hở cũng phải "
               "ít nhất 1 mm nhưng không cần vượt quá 5 mm."))
    b.append(note("<b>Lưu ý về 'premiss', 'machmes' và các chi tiết liên "
                  "quan.</b> Bản in viết 'initial premiss' (không phải "
                  "'premise'), 'Type ‘N’ machmes' (không phải 'machines'), "
                  "'so as to minimize, the possibility' (dấu phẩy thừa) và "
                  "để dấu nháy chưa đóng trong 'impact tests for Type ‘N "
                  "described earlier'. Tất cả được giữ nguyên trong bản "
                  "tiếng Anh; bản tiếng Việt theo nghĩa đúng."))
    # B6 (raw 18927-18932).
    b.append(p("Máy Kiểu ‘N’ phải đáp ứng các yêu cầu về vỏ bọc đã nêu ở "
               "phần trước của chương này nhưng trong trường hợp này "
               "BS 4999¹⁴ là Tiêu chuẩn phù hợp được dùng. Nếu máy được "
               "lắp một hộp đấu dây thì hộp đó phải đạt IP54 đối với môi "
               "trường bên ngoài nhưng chỉ cần đạt IP44 đối với bên trong "
               "máy, vì bên trong máy đã được bảo vệ bằng vỏ bọc riêng của "
               "nó và bằng sự bảo vệ bên ngoài của hộp đấu dây."))
    # B7 (raw 18933-18938, continues on printed 438).
    b.append(p("Cuối cùng, do nguy cơ thấp về môi trường nổ trong Khu vực 2, "
               "việc phân loại nhiệt độ bề mặt của máy có thể chỉ xét đến "
               "tình trạng chạy dưới tải tối đa được công nhận và loại trừ "
               "các điều kiện khởi động, vì những điều kiện này khó có thể "
               "trùng với sự hiện diện của môi trường nổ bên trong máy, nơi "
               "thường xảy ra nhiệt độ cao nhất. Nếu máy dùng cho chu trình "
               "làm việc liên tục khởi động và"))

    # B8 (raw 18941-18944; continuation of B7).
    b.append(p("dừng, như trường hợp xảy ra trong một quy trình theo mẻ hoặc "
               "khi máy được dùng để bổ sung vào một bể chứa hoặc bình tương "
               "tự, thì lập luận loại trừ các điều kiện khởi động khỏi việc "
               "phân loại nhiệt độ không còn hợp lệ và các điều kiện đó sẽ "
               "phải được tính đến."))
    b.append(note("<b>Lưu ý về cụm 'where it is regularly started and "
                  "stopped'.</b> Bản in tách cụm này qua ranh giới trang in "
                  "437 sang 438; hai nửa được giữ thành hai đoạn riêng như "
                  "bản in."))
    # B9 (raw 18945-18946).
    b.append(p("Không có yêu cầu đặc biệt nào cho thời gian tₑ liên quan đến "
               "các sự cố, vì các sự cố đó không được xem xét đối với máy "
               "Kiểu ‘n’."))
    b.append(note("<b>Lưu ý về 'tₑ'.</b> Bản in viết chỉ số dưới e trong "
                  "'tₑ' và bỏ mạo từ trong câu 'There is not special "
                  "requirement for tₑ time...'. Cả hai được giữ trong bản "
                  "tiếng Anh; bản tiếng Việt theo nghĩa đúng."))

    # Heading 14.4.2 (printed 438).
    b.append(h3("14.4.2 Cầu chảy và giá đỡ cầu chảy",
                "14.4.2 Fuse links and fuseholders"))
    # B11 (raw 18948-18952).
    b.append(p("Nhìn chung, sự đứt của cầu chảy, miễn là phần tử được bao "
               "bọc, không được coi là một sự kiện có khả năng đánh lửa. Vì "
               "vậy, miễn các phần tử cầu chảy là loại hộp không chỉ thị, "
               "thường chứa cát khi dùng cho điện áp trên 60 V, hồ quang do "
               "phần tử tạo ra trong lúc đứt có thể được bỏ qua như một "
               "nguồn đánh lửa, miễn là phần tử cầu chảy đáp ứng các yêu cầu "
               "lắp đặt cần thiết."))
    # B12 (raw 18953-18959).
    b.append(p("Hiện nay, các cầu chảy ngắt điện áp dưới 60 V có thể được "
               "lắp trong giá đỡ hở giữ bằng kẹp đầu lò xo hoặc hàn thiếc "
               "tại chỗ, trong khi những cầu chảy làm việc ở điện áp trên "
               "60 V cần có giá đỡ kín bên trong thiết bị, dù giá đỡ đó có "
               "thể tiếp cận được từ bên ngoài thiết bị. Rõ ràng cầu chảy "
               "dưới 60 V cũng có thể lắp trong những giá đỡ như vậy, nhưng "
               "đó là lựa chọn và có lẽ chỉ cần thiết khi cần tiếp cận cầu "
               "chảy từ bên ngoài vỏ bọc. Khi các giá đỡ cầu chảy có thể "
               "tiếp cận như vậy thì các cảnh báo thông thường được áp dụng "
               "và các vỏ bọc phải đạt IP54."))
    b.append(note("<b>Lưu ý về 'where have access is needed'.</b> Bản in "
                  "viết 'where have access is needed to the fuse from the "
                  "outside of the enclosure'. Cụm được giữ nguyên trong bản "
                  "tiếng Anh."))
    # B13 (raw 18960-18970).
    b.append(p("Khi một số cầu chảy được lắp trong một vỏ bọc cầu chảy (vỏ "
               "bọc dành riêng cho cầu chảy) thì các quy tắc này có thể không "
               "áp dụng, nhưng bản thân vỏ bọc cần phải cung cấp sự bảo vệ "
               "IP và điều khiển cần thiết để ngăn việc rút cầu chảy khi "
               "đang có điện (tức là, liên kết cơ khí hoặc bắt chặt kèm nhãn "
               "cảnh báo). Trong những trường hợp như vậy, có thể áp dụng hệ "
               "số đa dạng khi xác định nhiệt độ tối đa. Nhiệt độ này thường "
               "được xác định khi cầu chảy mang dòng định mức, vì dòng cao "
               "hơn được coi là hoạt động bất thường, nhưng khi có nhiều "
               "cầu chảy thì nhiệt độ có thể tăng thêm do nhiều cầu chảy "
               "cùng mang dòng đó đồng thời. Trong các trường hợp không có "
               "khả năng đó, có thể áp dụng hệ số đa dạng (ví dụ, giả định "
               "rằng không phải tất cả cầu chảy đều mang dòng đó cùng một "
               "lúc), miễn là người sử dụng thiết bị biết cơ sở áp dụng hệ "
               "số đa dạng đó để thiết bị có thể được dùng an toàn."))

    # Heading 14.4.3 (printed 438).
    b.append(h3("14.4.3 Đèn cố định", "14.4.3 Fixed luminaires"))
    # B15 (raw 18972-18978, continues on printed 439).
    b.append(p("Đèn cố định (bộ đèn chiếu sáng) phải tuân theo các yêu cầu "
               "bổ sung nhằm giảm nguy cơ phát tia lửa và không cho phép "
               "dùng đèn natri áp suất thấp, như trường hợp của bảo vệ Kiểu "
               "‘e’. Tiêu chuẩn Anh BS 4533¹⁰ được viện dẫn cho một số đèn "
               "trong BS 6941⁸, cũng như BS 5042¹⁸ cho giá đỡ đèn kiểu "
               "bayonet, BS 6766¹⁹ cho giá đỡ đèn kiểu vặn, BS 6702²⁰ cho "
               "giá đỡ đèn hai chân và giá đỡ bộ khởi động, BS 3772²¹ cho "
               "bộ khởi động, và BS 2818²² cùng 4782²³ cho ballast. Tất cả "
               "các tiêu chuẩn này đều bao phủ thiết bị thông thường, một "
               "lần"))

    # B16 (raw 18981-18986; continuation of B15).
    b.append(p("nữa, lại nhấn mạnh việc dùng thiết bị công nghiệp chất lượng "
               "tốt trong Khu vực 2. IEC 79-15¹¹ cũng giải quyết vấn đề này "
               "tương tự bằng cách viện dẫn IEC 61²⁴, IEC 238²⁵ và IEC 400²⁶ "
               "cho giá đỡ đèn, cùng IEC 262²⁷ và IEC 598-1²⁸ cho thiết bị "
               "phụ trợ. Cả hai tiêu chuẩn cũng đề cập đến các yêu cầu an "
               "toàn tối thiểu có thể không xuất hiện trong một số tiêu "
               "chuẩn công nghiệp này và bao phủ các đặc điểm quan trọng "
               "của các thiết bị đó như sau."))

    # Unnumbered subheading "Lampholders" (printed 439).
    b.append(h4("Giá đỡ đèn", "Lampholders"))
    # B18 (raw 18988-18991).
    b.append(p("Các giá đỡ đèn cần phải thực sự không phát tia lửa trong "
               "hoạt động bình thường, không bao gồm việc thay đèn. Điều "
               "này dẫn đến các yêu cầu cụ thể mà giá đỡ đèn phải đáp ứng "
               "nhưng có thể không phải là yêu cầu trong Tiêu chuẩn công "
               "nghiệp liên quan. Các yêu cầu cơ bản như sau."))
    # B19 - numbered item 1 (raw 18992-19001).
    b.append(p("1. Giá đỡ đèn kiểu vặn phải được chứng minh là đủ chắc "
               "chống lại sự lỏng ra để có thể bỏ qua khả năng nó là nguồn "
               "phát tia lửa gây cháy. Vì mục đích này, các yêu cầu như "
               "trong Bảng 12.5 (Chương 12) quy định rằng đèn phải được vặn "
               "chặt trong giá đỡ với một mô-men xác định, sau đó nới lỏng "
               "đi 15°, sau đó mô-men tháo ra phải ít nhất là một giá trị "
               "xác định. Các giá trị siết và nhả được lặp lại trong Bảng "
               "14.4. Bảng này áp dụng cho ba kích cỡ Tiêu chuẩn E14, E27 "
               "và E40 nhưng không áp dụng cho kích cỡ nhỏ nhất là E10, ở "
               "đó thử nghiệm mô-men được coi là không cần thiết và chỉ "
               "yêu cầu đèn được lắp chặt. Điều này là vì các đèn dùng E10 "
               "thường rất nhỏ, chẳng hạn như loại dùng trong đèn pin, và "
               "vấn đề lỏng do rung động thông thường được coi là nhỏ hơn."))
    b.append(note("<b>Lưu ý về lỗi dẫn đến Bảng 12.5.</b> Mục 1 dẫn đến "
                  "'Bảng 12.5 (Chương 12)', bảng này không được in trong "
                  "phần này; không tạo bảng mới ở đây."))
    # B20 - numbered item 2 (raw 19002-19009, continues on printed 440).
    b.append(p("2. Giá đỡ đèn kiểu bayonet gây ra một vấn đề đặc biệt ở chỗ "
               "mỗi tiếp điểm thường gồm hai phần đồng tâm với một lò xo "
               "xoắn bên trong để bảo đảm phần dưới duỗi ra hoàn toàn (xem "
               "Hình 14.1). Dòng điện tới đèn thường đi qua sự kết hợp giữa "
               "tiếp điểm ma sát giữa hai phần đồng tâm và lò xo xoắn. Điều "
               "này làm cho kiểu kết nối này rất dễ bị bẩn giữa hai phần "
               "hoặc bị yếu lò xo. Một cách có thể làm lò xo yếu đi là sự "
               "nóng lên do dòng điện chạy qua và vì mục đích này phải có "
               "một phương pháp chính khác"))

    # Table 14.4 (printed 439).
    b.append(table(T2.HEAD144_VI, T2.ROWS144_VI, T2.CAPTION144_VI))
    if T2.NOTE144_VI:
        b.append(note(T2.NOTE144_VI))

    # B23 (raw 19042-19046; continuation of item 2, printed 440).
    b.append(p("để dẫn dòng điện ngoài lò xo, và sự tiếp xúc tình cờ giữa "
               "hai phần của đầu bayonet là không đủ. Có nhiều cách để làm "
               "điều này, ví dụ, bổ sung các tiếp điểm trượt lò xo không "
               "đóng vai trò trong việc duỗi đầu bayonet, và các kết nối "
               "mềm bổ sung giữa điểm nối và phần dưới của đầu bayonet. "
               "Nhìn chung, tuy nhiên, giá đỡ đèn kiểu vặn được ưu tiên hơn "
               "nhờ kết nối chắc chắn đạt được."))
    # Fig. 14.1 (printed 440), after the item-2 continuation.
    b.append(fig(1, F.fig_f1401()))
    b.append(note("<b>Lưu ý về nhan đề Hình 14.1.</b> Nhan đề in viết "
                  "'In addition of the spring' (không phải 'to the spring'), "
                  "dùng 'e.g.:' và các phương án đánh số '(1)', '(2)', đồng "
                  "thời có nhãn 'Fortuitous frictional contact (Note 1)'. "
                  "Việc dẫn 'Note 1' không được giải thích bằng một chú giải "
                  "nào trong phần này. Tất cả được giữ nguyên như bản in."))
    # B24 - numbered item 3 (raw 19047-19052).
    b.append(p("3. Đối với ống huỳnh quang và các đèn tương tự, các phương "
               "pháp nối hai chân thông thường được cho phép, cho phép hoạt "
               "động với catốt nóng. Trong trường hợp này dòng điện tới đèn "
               "có thể được dẫn qua lò xo ngang dùng để ép vào các chân khi "
               "lắp ống, nhưng phải có cách bảo đảm là các chân ống không "
               "bị cong vào trong dưới áp lực đó, điều có thể xảy ra với "
               "nhiều giá đỡ tiêu chuẩn. Để bảo đảm điều này chỉ cần có một "
               "chốt cách điện ở giữa làm điểm tựa cho các tiếp điểm (xem "
               "Hình 14.2)."))

    # Unnumbered subheading "Lamp control gear" (printed 440).
    b.append(h4("Thiết bị điều khiển đèn", "Lamp control gear"))
    # B26 (raw 19054-19063, continues on printed 441).
    b.append(p("Thiết bị điều khiển đèn như loại dùng cho bộ đèn huỳnh quang "
               "cũng phải không phát tia lửa. Trong trường hợp Kiểu ‘N, bộ "
               "khởi động kiểu công tắc được chấp nhận miễn là các tiếp "
               "điểm công tắc, thường là một ống phóng điện, được chứa trong "
               "một vỏ bọc bịt kín kín khí (xem phần sau trong chương này) "
               "được bảo vệ cơ học bổ sung (ví dụ, một vỏ bọc kín khí bên "
               "trong một hộp kim loại hoặc nhựa bổ sung tuân thủ BS 3772). "
               "Vì là các thiết bị được biết là có chu kỳ hỏng hóc định kỳ, "
               "các bộ khởi động thường là loại cắm vào, và các tiếp điểm ở "
               "đáy bộ khởi động và trong ổ cắm của nó phải có độ tin cậy "
               "tương tự như các tiếp điểm dùng cho ống. Ngoài ra, thông "
               "thường không được chấp nhận là bộ khởi động dựa vào các "
               "tiếp điểm này để"))
    b.append(note("<b>Lưu ý về dấu nháy chưa đóng trong 'In the case of Type "
                  "‘N, switch starters'.</b> Bản in bỏ dấu nháy đóng sau "
                  "chữ N. Bản tiếng Anh giữ nguyên; bản tiếng Việt theo "
                  "nghĩa đúng."))

    # Fig. 14.2 (printed 441), in Lamp control gear.
    b.append(fig(2, F.fig_f1402()))
    # B28 (raw 19075-19077; continuation of B26).
    b.append(p("đỡ nó, và cần có giá đỡ bổ sung để ngăn sự dịch chuyển "
               "không mong muốn của bộ khởi động tại chỗ. Vòng đỡ thông "
               "thường thường là đủ cho mục đích này."))
    # B29 (raw 19078-19088).
    b.append(p("Ballast (cuộn cảm) và các thiết bị tương tự trong trường hợp "
               "này có cấu tạo công nghiệp bình thường vì hỏng hóc là điều "
               "bất thường. Khác với cuộn cảm Kiểu ‘e’, tuy nhiên, không có "
               "yêu cầu ngăn quá nhiệt hoặc hỏng hóc trong trường hợp ống "
               "bị hỏng, vì khả năng điều này xảy ra đồng thời với sự hiện "
               "diện của môi trường nổ trong Khu vực 2 là rất nhỏ. Tuy "
               "nhiên, không thể chấp nhận tình huống cuộn cảm trở nên rất "
               "nóng mà không bị hỏng theo cách làm các phần tử bảo vệ "
               "hoạt động, cô lập bộ đèn. Vì vậy, nếu cuộn cảm vượt quá "
               "phân loại nhiệt độ hoặc giới hạn hoạt động của lớp cách "
               "điện khi đèn hỏng, nó phải hỏng theo cách làm thiết bị an "
               "toàn (chẳng hạn như cầu chảy mạch) hoạt động trong một thời "
               "gian ngắn. Không đưa ra thời gian cụ thể nhưng bất kỳ thời "
               "gian nào vượt quá khoảng 30 phút khó có thể được chấp nhận."))
    b.append(note("<b>Lưu ý về 'say 30 minutes'.</b> Bản in không nêu thời "
                  "gian cố định cho hoạt động của cầu chảy; giá trị được "
                  "diễn đạt như một ước lượng và được giữ như bản in."))

    # Heading 14.4.4 (printed 441).
    b.append(h3("14.4.4 Đèn di động và các nguồn sáng khác",
                "14.4.4 Portable luminaires and other light sources"))
    # B31 (raw 19090-19096, continues on printed 442).
    b.append(p("Đèn di động và các nguồn sáng khác, chẳng hạn như những "
               "nguồn là bộ phận của thiết bị khác thay vì là đèn, phải "
               "đáp ứng các yêu cầu giống như đã nêu ở trên trừ khi có thể "
               "chứng minh là chúng không phù hợp (ví dụ, trong trường hợp "
               "đèn báo hàn chết thì yêu cầu về giá đỡ đèn rõ ràng là "
               "không phù hợp). Ngoài ra, trong trường hợp đèn di động, đèn "
               "phải có khả năng bị rơi bốn lần từ độ cao 1 m xuống sàn bê "
               "tông nhẵn mà không bị gì khác ngoài"))
    b.append(note("<b>Lưu ý về 'eg.,'.</b> Bản in viết 'eg.,' (thay vì "
                  "'e.g.,') trong đoạn về đèn di động. Hình thức này được "
                  "giữ nguyên."))

    # B32 (raw 19099-19101; continuation of B31).
    b.append(p("hư hỏng bề mặt và đặc biệt là vỏ đèn không bị vỡ. Điều kiện "
               "tiến hành thử nghiệm rơi này được nêu trong Chương 8 và "
               "giống như đối với các khái niệm bảo vệ khác."))

    # Heading 14.4.5 (printed 442).
    b.append(h3("14.4.5 Thiết bị điện tử và công suất thấp",
                "14.4.5 Electronic and low power apparatus"))
    # B34 (raw 19103-19110).
    b.append(p("Loại thiết bị này được xác định riêng vì nó thường hoạt động "
               "ở điện áp và công suất thấp, thường gồm thiết bị đo lường "
               "và thiết bị truyền tín hiệu thông minh. Loại thiết bị này "
               "được miễn yêu cầu phải đạt mức tách biệt các phần dẫn điện, "
               "hoặc bằng cách đáp ứng các yêu cầu về chiều dài đường rò "
               "hoặc khoảng hở của Bảng 14.3, hoặc bằng các thử nghiệm cách "
               "điện giữa các phần dẫn điện được đưa ra như giải pháp thay "
               "thế việc tuân thủ Bảng đó (xem ở phần trước của chương "
               "này), nhưng không được miễn các yêu cầu cách điện giữa mạch "
               "và đất hoặc khung, miễn là nó đáp ứng tất cả ba yêu cầu sau."))
    b.append(note("<b>Lưu ý về 'as it normally operated at low voltage and "
                  "power'.</b> Bản in bỏ từ 'is' trong mệnh đề này. Cách "
                  "viết được giữ trong bản tiếng Anh; bản tiếng Việt theo "
                  "nghĩa đúng."))
    # B35 - numbered item 1 (raw 19111-19116).
    b.append(p("1. Vỏ bọc thiết bị phải ít nhất là IP54 khi được thử nghiệm, "
               "như đã mô tả ở phần trước của chương này, hoặc phải được "
               "dự định lắp đặt ở một vị trí mà bản thân vị trí đó cung "
               "cấp mức bảo vệ này. Nếu là trường hợp sau thì người sử dụng "
               "thiết bị cần được thông báo về các yêu cầu lắp đặt và "
               "không được kỳ vọng là vỏ bọc thiết bị sẽ được phép giảm "
               "xuống dưới IP20 trong những trường hợp như vậy."))
    # B36 - numbered item 2 (raw 19117-19119).
    b.append(p("2. Điện áp định mức của loại thiết bị này (hoặc các phần "
               "thiết bị đang xét) không được vượt quá 60 Vrms xoay chiều "
               "hoặc 75 V một chiều. Theo đó, không nên sinh điện áp cao "
               "hơn bên trong thiết bị."))
    b.append(note("<b>Lưu ý về '60Vrms ac or 75V dc'.</b> Bản in viết các "
                  "giá trị này không có dấu cách quanh đơn vị. Hình thức "
                  "được giữ nguyên trong bản tiếng Anh."))
    # B37 - numbered item 3 (raw 19120-19125).
    b.append(p("3. Cần có biện pháp bên trong thiết bị hoặc theo quy định "
               "lắp đặt để ngăn nguồn cấp cho thiết bị vượt quá đáng kể các "
               "giá trị định mức trong bất kỳ khoảng thời gian nào. Khi "
               "biện pháp đó nằm ngoài thiết bị, yêu cầu của nó phải được "
               "làm rõ cho người lắp đặt bằng thông tin đi kèm thiết bị và "
               "bằng ký hiệu trên thiết bị (thường là ký hiệu ‘X’ để thu "
               "hút sự chú ý đến các yêu cầu lắp đặt bất thường)."))
    # B38 (raw 19126-19138).
    b.append(p("Vì thiết bị thường không phát tia lửa, nên những sự tăng "
               "điện áp tạm thời nhỏ không được kỳ vọng gây phát tia lửa "
               "hoặc quá nhiệt và vì lý do này thiết bị được đánh giá ở "
               "điện áp nguồn tối đa bình thường của nó. Phương pháp ngăn "
               "cấp điện áp quá mức thường là một thiết bị như diode zener, "
               "hoặc tổ hợp các diode zener mắc song song với nguồn có cầu "
               "chảy mắc nối tiếp giữa nguồn và các diode. Các diode cần có "
               "giá trị dẫn tối thiểu, có lẽ cao hơn 10 phần trăm so với "
               "điện áp nguồn tối đa và với dung sai bình thường sẽ cho "
               "phép, tạm thời, mức tăng khoảng 30 phần trăm trong thời "
               "gian cầu chảy đứt. Năng lượng truyền vào thiết bị trong "
               "thời gian này, tính bằng mili giây, thường không được kỳ "
               "vọng gây vấn đề vì trong trường hợp hiếm hoi có tia lửa "
               "phát sinh trong thời gian đó thì khả năng môi trường nổ "
               "hiện diện đồng thời trong tình huống Khu vực 2 được coi là "
               "khó xảy ra."))

    # Heading 14.5 (printed 443).
    b.append(h3("14.5 Thiết bị phát sinh hồ quang, tia lửa và/hoặc bề mặt "
                "nóng có khả năng đánh lửa",
                "14.5 Apparatus producing arcs, sparks and/or "
                "ignition-capable hot surfaces"))
    # B40 (raw 19143-19150).
    b.append(p("Như đã thảo luận ở phần trước của chương này, sự xuất hiện "
               "của loại bảo vệ ‘N’ không chỉ nhằm xác định rõ hơn các yêu "
               "cầu lựa chọn đối với thiết bị không phát tia lửa vốn theo "
               "truyền thống được dùng để lựa chọn cho Khu vực 2 mà còn "
               "nhằm đưa vào các phương pháp bảo vệ đơn giản hóa đối với "
               "tia lửa và bề mặt nóng có khả năng đánh lửa do thiết bị tạo "
               "ra trong hoạt động bình thường, để loại bỏ sự cần thiết "
               "phải dùng các khái niệm bảo vệ Khu vực 1. Các kỹ thuật dùng "
               "cho những phương pháp đơn giản hóa này tương tự về mặt "
               "khái niệm với các phương pháp cổ điển hơn được phát triển "
               "cho Khu vực 1, với việc bổ sung khả năng được thừa nhận là "
               "môi trường nổ có thể được loại trừ với mức độ tin cậy đủ "
               "cho Khu vực 2, một cách tiếp cận không được coi là phù hợp "
               "cho Khu vực 0 và 1."))

    # Heading 14.5.1 (printed 443).
    b.append(h3("14.5.1 Thiết bị ngắt kín và linh kiện không gây cháy",
                "14.5.1 Enclosed break devices and non-incendive "
                "components"))
    b.append(note("<b>Lưu ý về số mục 14.5.1.</b> Lớp OCR đọc '74.5.7'; ảnh "
                  "trang in cho thấy rõ '14.5.1'. Cách đọc theo ảnh trang "
                  "được dùng."))
    # B42 (raw 19152-19160).
    b.append(p("Các phương pháp ngăn ngừa nói chung sự đánh lửa do tiếp "
               "điểm phát tia lửa (hoặc, dù tiêu đề của thiết bị có nói gì, "
               "do bề mặt nóng) thực chất là một dạng cấu tạo chống cháy nổ "
               "được đơn giản hóa. Giữa chúng có rất ít khác biệt về cấu "
               "tạo nhưng, trong thiết bị ngắt kín, người ta bảo đảm là "
               "bất kỳ môi trường nổ nào đi vào thiết bị đều bị đánh lửa "
               "và sự bảo vệ nằm ở việc ngăn truyền ngọn lửa ra môi trường "
               "nổ xung quanh. Trong linh kiện không gây cháy, người ta "
               "không cố gắng bảo đảm đánh lửa bên trong và sự bảo vệ có "
               "thể giống như đối với thiết bị ngắt kín nhưng, cũng có thể "
               "là cấu hình tiếp điểm hoặc cấu hình bề mặt bên trong linh "
               "kiện làm dập tắt ngọn lửa mới hình thành và ngăn đánh lửa "
               "bên trong có hiệu quả."))

    # Unnumbered subheading "Construction" (printed 443, first occurrence).
    b.append(h4("Cấu tạo", "Construction"))
    b.append(note("<b>Lưu ý về các tiêu đề phụ không đánh số.</b> 'Cấu tạo' "
                  "xuất hiện hai lần, dưới 14.5.1 và lại dưới 14.5.2, trong "
                  "khi 'Thử nghiệm kiểu' và 'Việc thử nghiệm kiểu' là hai "
                  "cụm in khác nhau. Cả ba được giữ phân biệt."))
    # B44 (raw 19162-19174).
    b.append(p("Cả hai loại vỏ bọc đều có thể được mở trong khi sử dụng và "
               "có thể chứa các gioăng nhiệt dẻo hoặc cao su đàn hồi. Nhìn "
               "chung các gioăng này phải chống được sự xuống cấp và điều "
               "đó đòi hỏi bất kỳ gioăng nào chứa vật liệu nhiệt dẻo hoặc "
               "cao su đàn hồi phải được tiền xử lý trước khi tiến hành "
               "bất kỳ thử nghiệm nào. Đối với gioăng chứa vật liệu nhiệt "
               "dẻo, việc đó gồm đặt các gioăng vào lò ở 80±2°C trong 168 "
               "giờ (7 ngày), còn đối với gioăng chứa vật liệu cao su đàn "
               "hồi, việc đó gồm đặt các gioăng vào buồng chứa oxy nguyên "
               "chất ở 70±2°C với áp suất đo 2 × 10⁶ N/m² trong 96 giờ "
               "(4 ngày). Ngoài ra, bất kỳ gioăng nào dùng để bịt nắp được "
               "mở trong lúc sử dụng hoặc không được bảo vệ chống lại hoặc "
               "không chịu được các điều kiện cơ học hoặc điều kiện môi "
               "trường khác (ví dụ, tiếp xúc với ánh sáng) phải được tháo "
               "bỏ hoàn toàn hoặc một phần – tùy theo trường hợp nào xấu "
               "hơn. Tháo bỏ một phần có thể tệ hơn vì nó có thể gây ra sự "
               "phun tia, làm cho việc truyền ngọn lửa dễ xảy ra hơn và "
               "có thể cần thử nghiệm cả trong trường hợp tháo bỏ hoàn "
               "toàn lẫn tháo bỏ một phần (khoảng 1 phần trăm gioăng)."))
    b.append(note("<b>Lưu ý về các giá trị tiền xử lý.</b> Bản in viết "
                  "'80±2°C for 168 hours (7 days)', '70±2°C' và "
                  "'2 × 10⁶ N/m² for 96 Hours (4 days)' với chữ H viết hoa "
                  "trong 'Hours', cùng dấu gạch ngang trong 'removed – "
                  "whichever is considered worst' và 'say 1 per cent of "
                  "the gasket'. Tất cả được giữ như bản in."))

    # B45 (raw 19177-19180; continuation of Construction, printed 444).
    b.append(p("Các gioăng đúc dùng làm gioăng vĩnh viễn và không bị tách "
               "ra trong hoạt động bình thường phải có điểm nóng chảy ít "
               "nhất cao hơn 20°C so với nhiệt độ tối đa mà thiết bị dự "
               "kiến đạt được khi hoạt động ở nhiệt độ môi trường tối đa."))
    # B46 (raw 19181).
    b.append(p("Thể tích tự do bên trong của cả thiết bị ngắt kín và linh "
               "kiện không gây cháy không được vượt quá 20 cm³."))
    b.append(note("<b>Lưu ý về 'at least 20°C higher' và '20 cm³'.</b> Bản "
                  "in viết '20°C' không có dấu cách ở đây và thể tích với "
                  "chỉ số trên 3. Cả hai được giữ như bản in."))

    # Unnumbered subheading "Ratings" (printed 444).
    b.append(h4("Định mức", "Ratings"))
    # B48 (raw 19183).
    b.append(p("Cũng có các giới hạn về định mức của các thiết bị này như "
               "sau."))
    # B49 (raw 19184-19185).
    b.append(p("Thứ nhất, thiết bị ngắt kín không được có định mức điện áp "
               "vượt quá 660V và có định mức dòng vượt quá 15A."))
    b.append(note("<b>Lưu ý về các giá trị định mức.</b> Bản in viết "
                  "'660V' và '15A' không có dấu cách, nhưng '250 V' và "
                  "'15 A' có dấu cách trong đoạn ngay sau đó. Sự không "
                  "nhất quán được giữ nguyên."))
    # B50 (raw 19186-19194).
    b.append(p("Thứ hai, linh kiện không gây cháy có các giới hạn tuyệt đối "
               "tương tự nhưng thấp hơn là 250 V và 15 A. Trong trường hợp "
               "này, do bản chất của thiết bị, mạch cấp cho bất kỳ tiếp "
               "điểm nào phát tia lửa rất quan trọng vì sự dập tắt ngọn "
               "lửa là phương tiện bảo vệ có thể có. Chúng chỉ dùng được "
               "trong các mạch cụ thể và thử nghiệm đánh lửa phải được "
               "thực hiện trong các mạch điển hình như mạch mà linh kiện "
               "dự định được sử dụng. Vì lý do này, linh kiện không gây "
               "cháy thường chỉ xuất hiện như bộ phận của thiết bị khác và "
               "không phải là thiết bị tự thân – khác với thiết bị ngắt "
               "kín có thể đứng riêng dễ dàng hơn."))

    # Unnumbered subheading "Type tests" (printed 444).
    b.append(h4("Thử nghiệm kiểu", "Type tests"))
    # B52 (raw 19196-19197).
    b.append(p("Để thực hiện các thử nghiệm kiểu cần thiết, các thiết bị "
               "được đổ đầy và bao quanh bằng môi trường nổ quy định trong "
               "Bảng 14.5."))
    # B53 (raw 19198-19202).
    b.append(p("Trong trường hợp thiết bị ngắt kín, môi trường bên trong "
               "vỏ bọc sẽ bị đánh lửa bởi các tiếp điểm bên trong nó hoặc "
               "bởi bề mặt nóng bên trong, và sự đánh lửa được kiểm chứng "
               "bằng một phương tiện nào đó (ví dụ, cặp nhiệt điện hoặc "
               "phát hiện ion hóa). Môi trường bên ngoài không được bị "
               "đánh lửa. Thử nghiệm sẽ được lặp lại ba lần, mỗi lần dùng "
               "môi trường nổ mới, và sự đánh lửa sẽ do các tiếp điểm làm "
               "việc ở định mức tối đa của chúng hoặc bề mặt nóng ở nhiệt "
               "độ tối đa của nó."))
    # B54 (raw 19203-19204, continues on printed 445).
    b.append(p("Trong trường hợp linh kiện không gây cháy, không cần xác "
               "nhận đánh lửa bên trong. Vỏ bọc được đổ đầy và bao quanh "
               "bằng môi trường nổ"))

    # Table 14.5 (printed 444, between the two halves of B54/B56).
    b.append(table(T2.HEAD145_VI, T2.ROWS145_VI, T2.CAPTION145_VI))
    if T2.NOTE145_VI:
        b.append(note(T2.NOTE145_VI))

    # B56 (raw 19218-19227; continuation of B54, printed 445).
    b.append(p("như trước và bề mặt nóng hoặc các tiếp điểm bên trong được "
               "cho hoạt động trong điều kiện khắc nghiệt nhất trong mạch "
               "mà chúng được dùng. Trong trường hợp tiếp điểm, chúng được "
               "tiền xử lý bằng cách cho hoạt động 6000 lần với tốc độ "
               "khoảng 6 lần thao tác mỗi phút ở tải định mức của chúng "
               "(không phải tải của mạch). Sau đó các tiếp điểm được cho "
               "hoạt động ở tải mạch tối đa 50 lần với tốc độ đại loại như "
               "vậy khi có môi trường nổ hiện diện và không được xảy ra "
               "đánh lửa môi trường nổ bên ngoài. Không nêu tiêu chí thời "
               "gian nào cho bề mặt nóng nhưng cho phép thử nghiệm tiến "
               "hành trong 10 phút là được. Các thử nghiệm này cũng phải "
               "được lặp lại ba lần, mỗi lần dùng môi trường nổ mới."))
    # B57 (raw 19228-19232).
    b.append(p("Thiết bị trong trường hợp này được phân nhóm con IIA, IIB "
               "hoặc IIC tùy theo hỗn hợp thử nghiệm được dùng. Một cách "
               "dùng điển hình của thiết bị ngắt kín được thể hiện trong "
               "Hình 14.3, ở đó nó được dùng như một thiết bị cô lập tự "
               "động cho giá đỡ đèn kiểu vặn. Một công tắc vi mô là linh "
               "kiện không gây cháy điển hình được thể hiện trong Hình "
               "14.4."))

    # Heading 14.5.2 (printed 445).
    b.append(h3("14.5.2 Thiết bị được bịt kín kín khí",
                "14.5.2 Hermetically sealed devices"))
    b.append(note("<b>Lưu ý về số mục 14.5.2.</b> Lớp OCR đọc '74.5.2'; ảnh "
                  "trang in cho thấy rõ '14.5.2'. Cách đọc theo ảnh trang "
                  "được dùng."))
    # B59 (raw 19234-19238).
    b.append(p("Thiết bị bịt kín kín khí là thiết bị được bịt kín vĩnh viễn "
               "bằng các phương thức như hàn chảy. Loại gioăng này được "
               "dùng trong thiết bị thông thường cho các thứ như tiếp điểm "
               "và rơ le để tạo ra một môi trường được kiểm soát quanh các "
               "tiếp điểm nhằm đạt hiệu quả và tuổi thọ tối đa. Trong Kiểu "
               "‘N, tuy nhiên, chúng có thể được dùng để loại trừ môi "
               "trường nổ."))
    b.append(note("<b>Lưu ý về dấu nháy chưa đóng trong 'In Type ‘N, "
                  "however'.</b> Bản in bỏ dấu nháy đóng sau chữ N. Bản "
                  "tiếng Anh giữ nguyên; bản tiếng Việt theo nghĩa đúng."))

    # Fig. 14.3 (printed 445), under 14.5.2.
    b.append(fig(3, F.fig_f1403()))
    b.append(note("<b>Lưu ý về nhan đề Hình 14.3.</b> Nhan đề in xuống "
                  "dòng sau 'non-' trong 'enclosed break/non-incendive "
                  "component technique'; lớp OCR đọc sai dấu gạch chéo "
                  "thành 'breawnon'. Cách đọc theo ảnh trang được dùng "
                  "trong hình vẽ lại."))

    # Fig. 14.4 (printed 446), at the start of the page.
    b.append(fig(4, F.fig_f1404()))
    b.append(note("<b>Lưu ý về nhan đề và Lưu ý của Hình 14.4.</b> Nhan đề "
                  "kết thúc bằng dấu chấm và theo sau là 'Note: The shroud "
                  "is removed for testing'; nhãn trong hình ghi 'Protection "
                  "shroud (Note 1)'. Việc dẫn 'Note 1' không được giải "
                  "thích bằng chú giải nào trong phần này. Tất cả được "
                  "giữ như bản in."))

    # Unnumbered subheading "Construction" (printed 446, second occurrence).
    b.append(h4("Cấu tạo", "Construction"))
    # B63 (raw 19254-19258).
    b.append(p("Gioăng được tạo bằng các cách như hàn chảy kính/kim loại, "
               "hàn, hàn đồng hoặc hàn thiếc. Gioăng làm bằng các miếng "
               "đệm không thể được gọi là gioăng kín khí. Khi dùng bịt kín "
               "kín khí, gioăng không được bị hư hỏng khi lắp thiết bị này "
               "vào thiết bị khác và không được bị hư hỏng bởi các thử "
               "nghiệm va đập và, nếu phù hợp, thử nghiệm rơi được áp dụng "
               "bình thường."))

    # Unnumbered subheading "Type testing" (printed 446).
    b.append(h4("Việc thử nghiệm kiểu", "Type testing"))
    # B65 (raw 19260-19268).
    b.append(p("Sau khi gioăng đã được tạo thì không thể thực hiện bất kỳ "
               "phép đo nào bên trong vỏ bọc và thử nghiệm duy nhất có thể "
               "thực hiện là thử nghiệm rò rỉ. Có thể thực hiện thử nghiệm "
               "này bằng cách đặt thiết bị vào nước nóng để giãn nở khí "
               "bên trong (dùng nước ở 75 °C đến 85 °C và nhiệt độ ban đầu "
               "của thiết bị là giữa 15 °C và 35 °C), hoặc bằng cách hút "
               "chân không không khí phía trên mặt nước mà thiết bị được "
               "nhúng vào để khuyến khích sự rò rỉ (trong trường hợp này "
               "nhiệt độ của cả vật thử và nước đều nằm giữa 15 °C và "
               "35 °C và áp suất trên mặt nước được giảm đến giá trị tuyệt "
               "đối là 5 × 10³ N/m² tuyệt đối)."))
    # B66 (raw 19269-19275; last complete sentence on printed 446).
    b.append(p("Thử nghiệm chênh nhiệt độ thường kéo dài 2 phút và sự rò "
               "rỉ được quan sát bằng cách ghi nhận một đám bọt khí lớn "
               "duy nhất trên bề mặt thiết bị, hoặc một chuỗi bọt khí "
               "trong ít nhất 20 giây. Sự thoát khí thông thường từ bề mặt "
               "khi mới nhúng lần đầu phải được bỏ qua dù nó cho các dấu "
               "hiệu tương tự trong một thời gian ngắn. Trong trường hợp "
               "giảm áp suất, một chuỗi bọt khí liên tục sẽ được ghi nhận "
               "cho đến khi vỏ bọc đạt đến áp suất của không khí phía trên "
               "chất lỏng."))
    b.append(note("<b>Lưu ý về 'a single large production of bubbles'.</b> "
                  "Bản in dùng chính cụm từ này (thay vì, ví dụ, 'a single "
                  "large bubble') trong mô tả thử nghiệm rò rỉ. Cụm được "
                  "giữ nguyên."))
    b.append(note("<b>Lưu ý về điểm kết thúc phạm vi của mô-đun này.</b> "
                  "Đoạn cuối kết thúc ở trang in 446; trang in 447 mở "
                  "§14.5.3 thuộc về mô-đun tiếp theo."))

    return "".join(b)


def body_en():
    b = []

    # Survey quirk 0 - the assignment's original line anchor.
    b.append(note("<b>Note on the assigned line anchor.</b> The task brief "
                  "originally placed '=== PAGE 458 ===' at raw line 18939; "
                  "line 18939 is in fact '=== PAGE 459 ==='. The true start "
                  "of PDF p. 458 (printed p. 437) is raw line 18896 and the "
                  "owned range ends at line 19275, with '=== PAGE 468 ===' "
                  "at 19276. This module follows the corrected range "
                  "18896–19275."))

    # B1 (raw 18898-18900; continuation of a paragraph from printed 436).
    b.append(p("All of the above test voltages are minima and it is not "
               "necessary to control the voltage any more than to ensure "
               "that it does not exceed +5 per cent of this figure."))
    b.append(note("<b>Note on the opening paragraph.</b> The paragraph "
                  "'All of the above test voltages are minima...' begins on "
                  "printed p. 437 as a continuation of text from printed "
                  "p. 436, which lies outside this module's span. It is "
                  "kept incomplete at the start as printed."))

    # Heading 14.4 (printed 437).
    b.append(h3("14.4 Additional requirements for certain types of "
                "non-sparking apparatus",
                "14.4 Additional requirements for certain types of "
                "non-sparking apparatus"))
    # B3 (raw 18903-18906).
    b.append(p("Continuing the theme that the basic requirements for Type "
               "‘N’ apparatus are normal industrial requirements which "
               "would produce a reliable item of equipment, there are only "
               "a limited set of additional requirements applied to "
               "specific items of apparatus."))

    # Heading 14.4.1 (printed 437).
    b.append(h3("14.4.1 Rotating electrical machines",
                "14.4.1 Rotating electrical machines"))
    # B5 (raw 18908-18926, continues on printed 438).
    b.append(p("Both BS 6941⁸ and IEC 79-15¹¹ make the initial premiss that "
               "the machines must meet basic industrial Standards, the "
               "standard in question in the UK being BS 5000, Part 16⁹ which "
               "details Type ‘N’ machmes and the international Standard "
               "being IEC 34¹⁷ which is a more general standard for rotating "
               "electrical machines. The IEC document is the more general "
               "document leaving the Type ‘n’ special additions for IEC "
               "79-15¹¹. The basic matters which require consideration are "
               "such things as the security of fitting of rotor bars, "
               "enclosure, etc. In common with Type ‘e’ machines, the rotor "
               "bars are required to be secured in the slots so as to "
               "minimize, the possibility of their movement and hence "
               "sparking. Similar methods of securing as for Type ‘e’ "
               "machines (e.g., die-cast aluminium, etc.) are proposed as "
               "appropriate and the sparking which would be otherwise "
               "produced needs, as for Type ‘e’, to be addressed during "
               "both starting and running. Fanhoods are expected to be "
               "constructed so as to reduce the risk of damage causing "
               "contact with the fans and, in addition to withstanding the "
               "impact tests for Type ‘N described earlier, the running "
               "clearance between them and the enclosed fan must have a "
               "basic value of at least 1 per cent of the fan diameter. "
               "There are limits to this in that the clearance must also "
               "be at least 1 mm but need not exceed 5 mm."))
    b.append(note("<b>Note on 'premiss', 'machmes' and related quirks.</b> "
                  "The print reads 'initial premiss' (not 'premise'), 'Type "
                  "‘N’ machmes' (not 'machines'), 'so as to minimize, the "
                  "possibility' (stray comma), and leaves the quote unclosed "
                  "in 'impact tests for Type ‘N described earlier'. All are "
                  "retained verbatim in the English text; the Vietnamese "
                  "follows the intended meaning."))
    # B6 (raw 18927-18932).
    b.append(p("Type ‘N’ machines must satisfy the enclosure requirements "
               "stated earlier in this chapter but in this case BS 4999¹⁴ is "
               "the appropriate Standard used. If the machine is fitted "
               "with a terminal box that box must achieve IP54 to the "
               "outside world but need only provide IP44 to the interior of "
               "the machine as that is already protected by its own "
               "enclosure and the outer protection of the terminal box."))
    # B7 (raw 18933-18938, continues on printed 438).
    b.append(p("Finally, because of the low risk of an explosive atmosphere "
               "in Zone 2 the surface temperature classification of the "
               "machine may consider running under recognized maximum load "
               "only and exclude starting conditions as these are unlikely "
               "to coincide with the presence of an explosive atmosphere "
               "within the machine which is usually where the maximum "
               "temperature occurs. If the machine is for duty cycling "
               "where it is regularly started and"))

    # B8 (raw 18941-18944; continuation of B7).
    b.append(p("stopped, such as would occur in a batch process or where it "
               "is used for topping up a tank or similar vessel, the "
               "argument for excluding the starting conditions for "
               "temperature classification is not valid and these "
               "conditions will have to be included."))
    b.append(note("<b>Note on 'where it is regularly started and "
                  "stopped'.</b> The print splits this phrase across the "
                  "page turn from printed p. 437 to 438; the two halves are "
                  "kept as separate paragraphs as printed."))
    # B9 (raw 18945-18946).
    b.append(p("There is not special requirement for tₑ time in respect of "
               "faults as these are not considered for Type ‘n’ machines."))
    b.append(note("<b>Note on 'tₑ'.</b> The print writes the subscript e in "
                  "'tₑ' and omits the article in 'There is not special "
                  "requirement for tₑ time...'. Both are retained in the "
                  "English text; the Vietnamese follows the intended "
                  "meaning."))

    # Heading 14.4.2 (printed 438).
    b.append(h3("14.4.2 Fuse links and fuseholders",
                "14.4.2 Fuse links and fuseholders"))
    # B11 (raw 18948-18952).
    b.append(p("In general, rupture of a fuse, provided the element is "
               "enclosed, is not considered as an ignition-capable "
               "occurrence. Thus provided fuse elements are non-indicating "
               "cartridge types, usually sand filled for voltages over "
               "60 V, the arc produced by the element during rupturing can "
               "be ignored as a source of ignition as long as the fuse "
               "element satisfies the necessary mounting requirements."))
    # B12 (raw 18953-18959).
    b.append(p("Currently, fuse links interrupting voltages below 60 V may "
               "be installed in open holders retained by spring end clamps "
               "or soldered in position, whereas those operating at more "
               "than 60 V need an enclosed holder within the apparatus "
               "although it may be accessible from the outside of the "
               "apparatus. Obviously fuses below 60 V may be installed in "
               "such holders also but this is by choice and is probably "
               "only necessary where have access is needed to the fuse from "
               "the outside of the enclosure. Where fuse holders are so "
               "accessible the normal warnings apply and the enclosures "
               "must achieve IP54."))
    b.append(note("<b>Note on 'where have access is needed'.</b> The print "
                  "reads 'where have access is needed to the fuse from the "
                  "outside of the enclosure'. The phrase is retained "
                  "verbatim in the English text."))
    # B13 (raw 18960-18970).
    b.append(p("Where several fuses are mounted within a fuse enclosure (an "
               "enclosure dedicated to fuses) these rules may not apply but "
               "the enclosure itself needs to provide the necessary IP "
               "protection and control to prevent fuse extraction live "
               "(i.e., interlocking or fastening with a warning label). In "
               "such cases diversity may be applied in determination of "
               "maximum temperature. This is normally determined with the "
               "fuse carrying its rated current as higher currents are "
               "considered as abnormal operation but, where several fuses "
               "exist the temperature could be further elevated by several "
               "fuses carrying this current simultaneously. In cases where "
               "this is not likely diversity (e.g., the assumption that not "
               "all fuses will carry such current at once) may be applied "
               "as long as the user of the apparatus knows on what basis "
               "that diversity has been applied so that the apparatus can "
               "be used safely."))

    # Heading 14.4.3 (printed 438).
    b.append(h3("14.4.3 Fixed luminaires", "14.4.3 Fixed luminaires"))
    # B15 (raw 18972-18978, continues on printed 439).
    b.append(p("Fixed luminaires (lighting fittings) are, subject to "
               "additional requirements to reduce the risk of sparking and, "
               "low pressure sodium lamps are not permitted, as is the case "
               "with Type ‘e’ protection. British Standard BS 4533¹⁰ is "
               "called up for certain luminaires in BS 6941⁸, as are "
               "BS 5042¹⁸ for bayonet lamp holders, BS 6766¹⁹ for screw "
               "lampholders, BS 6702²⁰ for bi-pin lampholders and starter "
               "holders, BS 3772²¹ for starters and BS 2818²² and 4782²³ for "
               "ballasts. All of these standards cover normal equipment, "
               "once"))

    # B16 (raw 18981-18986; continuation of B15).
    b.append(p("again reinforcing the use of good quality industrial "
               "equipment in Zone 2. IEC 79-15¹¹ similarly addresses this by "
               "referring to IEC 61²⁴, IEC 238²⁵ and IEC 400²⁶ for "
               "lampholders, and IEC 262²⁷ and IEC 598-1²⁸ for auxiliary "
               "gear. Both standards also address the minimum requirements "
               "for safety which may not appear in some of these industrial "
               "Standards and cover the important features of these devices "
               "which are as follows."))

    # Unnumbered subheading "Lampholders" (printed 439).
    b.append(h4("Lampholders", "Lampholders"))
    # B18 (raw 18988-18991).
    b.append(p("The lampholders need to be effectively non-sparking in "
               "normal operation which does not include lamp changing. This "
               "leads to specific requirements with which the lampholders "
               "need to comply but which may not be requirements in the "
               "industrial Standard concerned. The basic requirements are "
               "as follows."))
    # B19 - numbered item 1 (raw 18992-19001).
    b.append(p("1. Screw lampholders must be shown to be sufficiently secure "
               "against loosening so that it can be ignored as a possible "
               "source of incendive sparking. To this end the requirements "
               "are as in Table 12.5 (Chapter 12) which require the lamp to "
               "be tightened in the holder with a specific torque, then "
               "loosened by 15° after which the removal torque must be at "
               "least a specific figure. The tightening and release figures "
               "are repeated in Table 14.4. This table applies to the three "
               "Standard sizes E14, E27 and E40 but not to the smallest "
               "size, E10, where the torque test is not considered necessary "
               "and all that is required is that the lamp is tightly fitted. "
               "This is because lamps using E10 are normally very small, "
               "such as those used in torches, and the problem of loosening "
               "by normal vibration is considered less."))
    b.append(note("<b>Note on the cross-reference to Table 12.5.</b> Item 1 "
                  "refers to 'Table 12.5 (Chapter 12)', which is not printed "
                  "in this chunk; no table is invented here."))
    # B20 - numbered item 2 (raw 19002-19009, continues on printed 440).
    b.append(p("2. Bayonet lampholders produce a particular problem in that "
               "each contact normally comprises two concentric parts with "
               "an internal coil spring to ensure full extension of the "
               "lower part (see Fig. 14.1). Current to the lamp is normally "
               "passed down a combination of the friction contact between "
               "the two concentric parts and the coil spring. This makes "
               "the type of connection very vulnerable to dirt in between "
               "the two parts or weakening of the spring. One possible "
               "method of spring weakening is heating due to the passage of "
               "current and to this end there must be some other principal "
               "method"))

    # Table 14.4 (printed 439).
    b.append(table(T2.HEAD144_EN, T2.ROWS144, T2.CAPTION144_EN))
    if T2.NOTE144_EN:
        b.append(note(T2.NOTE144_EN))

    # B23 (raw 19042-19046; continuation of item 2, printed 440).
    b.append(p("of carrying current in addition to the spring and the "
               "fortuitous contact between the two parts of the bayonet is "
               "not sufficient. There are many ways of doing this, for "
               "example, the addition of spring sliding contacts which play "
               "no part in extension of the bayonet, and additional flexible "
               "connections between the connection facility and the lower "
               "part of the bayonet. In general, however, screw lampholders "
               "are to be preferred due to the positive connection "
               "achieved."))
    # Fig. 14.1 (printed 440), after the item-2 continuation.
    b.append(fig(1, F.fig_f1401()))
    b.append(note("<b>Note on the Fig. 14.1 caption.</b> The printed caption "
                  "reads 'In addition of the spring' (not 'to the spring'), "
                  "uses 'e.g.:' and the numbered alternatives '(1)' and "
                  "'(2)', and carries the label 'Fortuitous frictional "
                  "contact (Note 1)'. The Note 1 reference is not resolved "
                  "by a legend within this chunk. All are retained as "
                  "printed."))
    # B24 - numbered item 3 (raw 19047-19052).
    b.append(p("3. For fluorescent tubes and similar lamps the normal bi-pin "
               "connection methods are permitted, allowing hot cathode "
               "operation. In this case the current to the lamp may be "
               "carried by the lateral spring used to apply pressure to the "
               "pins when the tube is fitted, but there must be some method "
               "of ensuring that the tube pins cannot distort inwards under "
               "such pressure, as is possible with many standard holders. "
               "To ensure this it is only necessary to have a central "
               "insulating boss against which the contacts rest (see Fig. "
               "14.2)."))

    # Unnumbered subheading "Lamp control gear" (printed 440).
    b.append(h4("Lamp control gear", "Lamp control gear"))
    # B26 (raw 19054-19063, continues on printed 441).
    b.append(p("Lamp control gear such as that used for fluorescent fittings "
               "must also be non-sparking. In the case of Type ‘N, switch "
               "starters are acceptable provided the switch contacts, "
               "normally a discharge tube, are contained in a hermetically "
               "sealed enclosure (see later in this chapter) which is "
               "afforded additional mechanical protection (e.g., a "
               "hermetically sealed envelope in an additional metal or "
               "plastic canister complying with BS 3772). As devices which "
               "are known to have a regular failure pattern the starters "
               "are normally plug in, and the contacts on the base of the "
               "starter and in its receptacle must have similar reliability "
               "to those used for the tubes. In addition it is not normally "
               "acceptable to have the starter rely upon these contacts "
               "for"))
    b.append(note("<b>Note on the unclosed quote in 'In the case of Type "
                  "‘N, switch starters'.</b> The print omits the closing "
                  "quotation mark after N. The English text retains it; the "
                  "Vietnamese follows the intended meaning."))

    # Fig. 14.2 (printed 441), in Lamp control gear.
    b.append(fig(2, F.fig_f1402()))
    # B28 (raw 19075-19077; continuation of B26).
    b.append(p("its support, and additional support to prevent untoward "
               "movement of the starter in situ is necessary. The normal "
               "holder ring is usually sufficient for this."))
    # B29 (raw 19078-19088).
    b.append(p("Ballasts (chokes) and similar devices are in this case of "
               "normal industrial construction as failure is abnormal. "
               "Unlike Type ‘e’ chokes, however, there is no requirement "
               "for prevention of overheating or failure in case of tube "
               "failure as the likelihood of this occurring at the same "
               "time as an explosive atmosphere is present in Zone 2 is "
               "remote. A situation where the choke becomes very hot and is "
               "not subject to a failure which causes protection elements "
               "to operate, isolating the fitting is not, however, "
               "acceptable. Thus if the choke does exceed the temperature "
               "classification or the operating limit of its insulation on "
               "lamp failure, it must fail in a way which causes safety "
               "devices (such as circuit fuses) to operate within a short "
               "time. No time is given but any time in excess of say 30 "
               "minutes is unlikely to be acceptable."))
    b.append(note("<b>Note on 'say 30 minutes'.</b> The print gives no fixed "
                  "time for fuse operation; the value is expressed as an "
                  "approximation and is retained as printed."))

    # Heading 14.4.4 (printed 441).
    b.append(h3("14.4.4 Portable luminaires and other light sources",
                "14.4.4 Portable luminaires and other light sources"))
    # B31 (raw 19090-19096, continues on printed 442).
    b.append(p("Portable luminaires and other light sources, such as those "
               "forming parts of other apparatus rather than luminaires, "
               "need to comply with the same requirements as those "
               "specified above unless they can be shown to be "
               "inappropriate (eg., in the case of a soldered-in indicator "
               "lamp lampholder requirements are clearly not appropriate). "
               "In addition, in the case of portable luminaires the "
               "luminaire must be capable of being dropped four times from "
               "a height of 1 m on to a smooth concrete floor without other "
               "than"))
    b.append(note("<b>Note on 'eg.,'.</b> The print writes 'eg.,' (rather "
                  "than 'e.g.,') in the portable-luminaires paragraph. The "
                  "form is retained verbatim."))

    # B32 (raw 19099-19101; continuation of B31).
    b.append(p("superficial damage and, in particular, without the lamp "
               "envelope breaking. The conditions under which this drop "
               "test is carried out are given in Chapter 8 and are the same "
               "as for other protection concepts."))

    # Heading 14.4.5 (printed 442).
    b.append(h3("14.4.5 Electronic and low power apparatus",
                "14.4.5 Electronic and low power apparatus"))
    # B34 (raw 19103-19110).
    b.append(p("This type of apparatus is specifically identified separately "
               "as it normally operated at low voltage and power, "
               "comprising typically instrumentation and intelligence "
               "transmitting equipment. This type of apparatus is absolved "
               "from the necessity to achieve the level of separation of "
               "conductive parts either by meeting the creepage or clearance "
               "requirements of Table 14.3, or the electrical insulation "
               "tests between conducting parts given as alternatives to "
               "compliance with that Table (see earlier in this chapter) "
               "but not the insulation requirements between circuits and "
               "earth or frame provided that it satisfies all of the "
               "following three requirements."))
    b.append(note("<b>Note on 'as it normally operated at low voltage and "
                  "power'.</b> The print omits 'is' in this clause. The "
                  "wording is retained in the English text; the Vietnamese "
                  "follows the intended meaning."))
    # B35 - numbered item 1 (raw 19111-19116).
    b.append(p("1. The apparatus enclosure must be at least IP54 when "
               "tested, as described earlier in this chapter, or must be "
               "intended for installation in a location which itself "
               "provides that protection. If the latter is the case the "
               "user of the apparatus needs to be informed of the "
               "installation needs and it is not expected that the "
               "apparatus enclosure will ever be permitted to reduce to "
               "below IP20 in such circumstances."))
    # B36 - numbered item 2 (raw 19117-19119).
    b.append(p("2. The rated voltage of such apparatus (or the parts of "
               "apparatus in question) must not exceed 60Vrms ac or 75V dc. "
               "It follows that higher voltages should not be generated "
               "within the apparatus."))
    b.append(note("<b>Note on '60Vrms ac or 75V dc'.</b> The print writes "
                  "these values without spaces around the units. The form "
                  "is retained verbatim in the English text."))
    # B37 - numbered item 3 (raw 19120-19125).
    b.append(p("3. Provision needs to be made either within the apparatus or "
               "by installation specification to prevent the supplies to "
               "the apparatus from exceeding the rated values significantly "
               "and for any length of time. Where the provision is outside "
               "the apparatus its requirements must be made known to the "
               "installer by information provided with the apparatus and "
               "marking upon it (usually the ‘X’ mark to draw attention to "
               "unusual installation requirements)."))
    # B38 (raw 19126-19138).
    b.append(p("As the apparatus is normally non-sparking then transient "
               "supply elevations of a minor nature are not expected to "
               "cause sparking or overheating and for this reason the "
               "apparatus is assessed at its normal maximum supply voltage. "
               "The method of preventing excess voltage supply is normally "
               "a device such as a zener diode, or combination of zener "
               "diodes across the supply with series fusing between the "
               "supply and the diodes. The diodes need to have a minimum "
               "conduction value, probably 10 per cent higher than the "
               "maximum supply voltage and with normal tolerances will "
               "allow, transiently, an elevation of around 30 per cent "
               "during the rupturing period of the fuse. The energy "
               "transmitted into the apparatus during this period, which is "
               "milliseconds, is not normally expected to cause problems as "
               "in the unlikely event that a spark occurs during this time "
               "the possibility of the presence of an explosive atmosphere "
               "being coincident in a Zone 2 situation is considered as "
               "unlikely."))

    # Heading 14.5 (printed 443).
    b.append(h3("14.5 Apparatus producing arcs, sparks and/or "
                "ignition-capable hot surfaces",
                "14.5 Apparatus producing arcs, sparks and/or "
                "ignition-capable hot surfaces"))
    # B40 (raw 19143-19150).
    b.append(p("As discussed earlier in this chapter the advent of type of "
               "protection ‘N’ was not only to precise the selection "
               "requirements for non-sparking apparatus which were "
               "historically used for selection for Zone 2 but, in addition, "
               "to introduce simplified methods of protection of "
               "ignition-capable sparks and hot surfaces produced by "
               "apparatus in its normal operation to remove the necessity "
               "to use the Zone 1 protection concepts. The techniques used "
               "for these simplified methods are similar in concept to the "
               "more classic methods developed for Zone 1 with the addition "
               "of the possibility being recognized that the explosive "
               "atmosphere can be excluded to a sufficient level of "
               "confidence for Zone 2, an approach not considered as "
               "suitable for Zone 0 and 1."))

    # Heading 14.5.1 (printed 443).
    b.append(h3("14.5.1 Enclosed break devices and non-incendive "
                "components",
                "14.5.1 Enclosed break devices and non-incendive "
                "components"))
    b.append(note("<b>Note on the section number 14.5.1.</b> The OCR layer "
                  "reads '74.5.7'; the page render clearly shows '14.5.1'. "
                  "The render reading is used."))
    # B42 (raw 19152-19160).
    b.append(p("These methods of prevention of general ignition by sparking "
               "contacts (or for that matter hot surfaces despite the "
               "title of the device) are effectively a sort of simplified "
               "flameproof construction. There is little difference between "
               "their construction but, in the enclosed break device, it is "
               "ensured that any explosive atmosphere entering the device "
               "is ignited and the protection is in prevention of flame "
               "transmission into the surrounding explosive atmosphere. In "
               "the non-incendive component no attempt is made to ensure "
               "internal ignition and protection may be as for the enclosed "
               "break device but, equally, it may be that the contact "
               "configuration or surface configuration within the component "
               "may quench any incipient flame and prevent effective "
               "internal ignition."))

    # Unnumbered subheading "Construction" (printed 443, first occurrence).
    b.append(h4("Construction", "Construction"))
    b.append(note("<b>Note on the unnumbered subheadings.</b> 'Construction' "
                  "occurs twice, under 14.5.1 and again under 14.5.2, while "
                  "'Type tests' and 'Type testing' are distinct printed "
                  "strings. All three are kept distinct."))
    # B44 (raw 19162-19174).
    b.append(p("Both types of enclosure may be opened in service and may "
               "contain thermoplastic or elastomeric seals. In general these "
               "seals must be proof against deterioration and this requires "
               "any gaskets containing thermoplastic or elastomeric "
               "materials to be preconditioned before any testing is "
               "carried out. In the case of gaskets containing thermoplastic "
               "materials, this comprises of the placing of the gaskets in "
               "an oven at 80±2°C for 168 hours (7 days), and in the case of "
               "gaskets containing elastomeric materials the placing of the "
               "gaskets in a chamber containing pure oxygen at 70±2°C at a "
               "gauge pressure of 2 × 10⁶ N/m² for 96 Hours (4 days). In "
               "addition, any gaskets which are used to seal covers which "
               "are opened in service or which are not protected against or "
               "proof against mechanical or other environmental conditions "
               "(e.g., exposure to light) must be wholly or partly removed "
               "– whichever is considered worst. Partial removal may be "
               "worse because it can result in jetting, which will make the "
               "transmission of flame more likely and testing is likely to "
               "be necessary in both total removal and partial removal (say "
               "1 per cent of the gasket)."))
    b.append(note("<b>Note on the preconditioning values.</b> The print "
                  "reads '80±2°C for 168 hours (7 days)', '70±2°C', and "
                  "'2 × 10⁶ N/m² for 96 Hours (4 days)' with a capital H in "
                  "'Hours', plus the en dash in 'removed – whichever is "
                  "considered worst' and 'say 1 per cent of the gasket'. "
                  "All are retained as printed."))

    # B45 (raw 19177-19180; continuation of Construction, printed 444).
    b.append(p("Poured seals which are used as permanent seals and not "
               "subject to separation in normal service must have a melting "
               "point which is at least 20°C higher than the maximum "
               "temperature which the device is expected to reach in "
               "service at maximum ambient temperature."))
    # B46 (raw 19181).
    b.append(p("The internal free volume of both enclosed break devices and "
               "non-incendive components must not exceed 20 cm³."))
    b.append(note("<b>Note on 'at least 20°C higher' and '20 cm³'.</b> The "
                  "print has no space in '20°C' here and writes the volume "
                  "with superscript 3. Both are retained as printed."))

    # Unnumbered subheading "Ratings" (printed 444).
    b.append(h4("Ratings", "Ratings"))
    # B48 (raw 19183).
    b.append(p("There are also limits on the rating of these devices and "
               "these are as follows."))
    # B49 (raw 19184-19185).
    b.append(p("First, enclosed break devices shall not be rated at "
               "voltages exceeding 660V and which are rated for currents in "
               "excess of 15A."))
    b.append(note("<b>Note on the rating values.</b> The print writes "
                  "'660V' and '15A' without spaces, but '250 V' and '15 A' "
                  "with spaces in the following paragraph. The "
                  "inconsistency is retained."))
    # B50 (raw 19186-19194).
    b.append(p("Second, non-incendive components have similar but lower "
               "absolute limits which are 250 V and 15 A. In this case, "
               "because of the nature of the device, the circuit feeding "
               "any sparking contacts is important as flame quenching is "
               "the possible means of protection. They are usable only in "
               "particular circuits and testing for ignition must be in "
               "circuits typical of those in which the component is "
               "intended to be used. For this reason non-incendive "
               "components normally appear only as parts of other apparatus "
               "and not as apparatus in themselves – unlike enclosed break "
               "devices which can more readily stand alone."))

    # Unnumbered subheading "Type tests" (printed 444).
    b.append(h4("Type tests", "Type tests"))
    # B52 (raw 19196-19197).
    b.append(p("To execute the necessary type tests the devices are filled "
               "and surrounded with the explosive atmosphere specified in "
               "Table 14.5."))
    # B53 (raw 19198-19202).
    b.append(p("In the case of enclosed break devices the atmosphere within "
               "the enclosure will be ignited by the contacts within it or "
               "by the internal hot surface and ignition verified by some "
               "means (e.g., thermocouples or ionization detection). The "
               "external atmosphere must not be ignited. The test will be "
               "repeated three times using renewed explosive atmospheres in "
               "each case and the ignition will be by the contacts operating "
               "at their maximum rating or the hot surface at its maximum "
               "temperature."))
    # B54 (raw 19203-19204, continues on printed 445).
    b.append(p("In the case of non-incendive components there is no need to "
               "confirm internal ignition. The enclosure is filled and "
               "surrounded with the explosive"))

    # Table 14.5 (printed 444, between the two halves of B54/B56).
    b.append(table(T2.HEAD145_EN, T2.ROWS145, T2.CAPTION145_EN))
    if T2.NOTE145_EN:
        b.append(note(T2.NOTE145_EN))

    # B56 (raw 19218-19227; continuation of B54, printed 445).
    b.append(p("atmosphere as before and the contained hot surface or "
               "contacts operated in the most onerous condition in the "
               "circuit in which they are used. In the case of contacts they "
               "will be preconditioned by being operated 6000 times at a "
               "rate of around 6 operations per minute at their rated load "
               "(not the circuit load). The contacts are then operated at "
               "their maximum circuit load 50 times at around the same rate "
               "when the explosive atmosphere is present and ignition of "
               "the external explosive atmosphere must not take place. No "
               "time criterion is given for hot surfaces but allowing the "
               "test to proceed for 10 minutes is acceptable. These tests "
               "also must be repeated three times with new explosive "
               "atmospheres each time."))
    # B57 (raw 19228-19232).
    b.append(p("The apparatus is, in this case, sub-grouped IIA, IIB or IIC "
               "depending upon the test mixture used. A typical use for an "
               "enclosed break device is shown in Fig. 14.3 where it is used "
               "as an automatic isolator for a screw lampholder. A "
               "microswitch which is a typical non-incendive component is "
               "shown in Fig. 14.4."))

    # Heading 14.5.2 (printed 445).
    b.append(h3("14.5.2 Hermetically sealed devices",
                "14.5.2 Hermetically sealed devices"))
    b.append(note("<b>Note on the section number 14.5.2.</b> The OCR layer "
                  "reads '74.5.2'; the page render clearly shows '14.5.2'. "
                  "The render reading is used."))
    # B59 (raw 19234-19238).
    b.append(p("Hermetically sealed devices are devices which are "
               "permanently sealed by means such as fusion. This type of "
               "seal is used in normal equipment for such things as contacts "
               "and relays to allow for the production of a controlled "
               "atmosphere around contacts to give maximum efficiency and "
               "longevity. In Type ‘N, however, they can be used to exclude "
               "an explosive atmosphere."))
    b.append(note("<b>Note on the unclosed quote in 'In Type ‘N, "
                  "however'.</b> The print omits the closing quotation mark "
                  "after N. The English text retains it; the Vietnamese "
                  "follows the intended meaning."))

    # Fig. 14.3 (printed 445), under 14.5.2.
    b.append(fig(3, F.fig_f1403()))
    b.append(note("<b>Note on the Fig. 14.3 caption.</b> The printed caption "
                  "wraps after 'non-' in 'enclosed break/non-incendive "
                  "component technique'; the OCR layer garbles the slash as "
                  "'breawnon'. The render reading is used in the redraw."))

    # Fig. 14.4 (printed 446), at the start of the page.
    b.append(fig(4, F.fig_f1404()))
    b.append(note("<b>Note on the Fig. 14.4 caption and Note.</b> The "
                  "caption ends with a full stop and is followed by 'Note: "
                  "The shroud is removed for testing'; the in-figure label "
                  "reads 'Protection shroud (Note 1)'. The Note 1 reference "
                  "is not resolved by a legend within this chunk. All are "
                  "retained as printed."))

    # Unnumbered subheading "Construction" (printed 446, second occurrence).
    b.append(h4("Construction", "Construction"))
    # B63 (raw 19254-19258).
    b.append(p("Seals are made by such arrangements as glass/metal fusion, "
               "welding, brazing or soldering. Seals made using gaskets "
               "cannot be termed as hermetic seals. Where hermetic sealing "
               "is used the seal must not be damaged in installation of the "
               "device in apparatus and must not be damaged by the normally "
               "applied impact and, if appropriate, drop tests."))

    # Unnumbered subheading "Type testing" (printed 446).
    b.append(h4("Type testing", "Type testing"))
    # B65 (raw 19260-19268).
    b.append(p("Once the seal is made it is not possible to carry out any "
               "measurements inside the enclosure and the only test which "
               "can be carried out is a leakage test. This can be carried "
               "out by placing the device in hot water to expand the "
               "internal gas (water at 75 °C to 85 °C is used and the "
               "initial apparatus temperature is between 15 °C and 35 °C), "
               "or by evacuating the air above the water in which the "
               "device is immersed to encourage leaking (in this case the "
               "temperature of both test item and water are between 15 °C "
               "and 35 °C and the pressure over the water is reduced to an "
               "absolute value of 5 × 10³ N/m² absolute)."))
    # B66 (raw 19269-19275; last complete sentence on printed 446).
    b.append(p("The differential temperature test is normally for 2 minutes "
               "and leakage is observed by noting a single large production "
               "of bubbles at the device surface, or a train of bubbles for "
               "at least 20 seconds. Normal air release from the surface on "
               "initial immersion should be ignored even though it gives "
               "similar indications for a short time. In the case of "
               "reduced pressure a continuous train of bubbles will be "
               "noted until the enclosure reaches the pressure of the air "
               "over the liquid."))
    b.append(note("<b>Note on 'a single large production of bubbles'.</b> "
                  "The print uses this exact wording (rather than, say, 'a "
                  "single large bubble') in the leakage-test description. "
                  "It is retained verbatim."))
    b.append(note("<b>Note on the end of this module's span.</b> The last "
                  "paragraph ends on printed p. 446; printed p. 447 opens "
                  "§14.5.3, which belongs to the next module."))

    return "".join(b)
