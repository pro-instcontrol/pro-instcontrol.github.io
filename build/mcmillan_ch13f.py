# -*- coding: utf-8 -*-
"""Chapter 13, module F - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 411-426 (PDF pp. 432-447).

Covers the tail of the section 13.12 apparatus-label discussion, section 13.13
"Examples of fault counting in apparatus" (associated apparatus and
intrinsically safe apparatus, the worked 'ib'/'ia' examples and their label
parameter lists), section 13.14 "Intrinsically safe systems" (system fault
counting, the parameter-comparison criteria, simple apparatus, and the
'ia'/'ib' mixture rule), sections 13.14.1 and 13.14.2 (interconnecting cable
systems - separate, multicore and Type 'a' to Type 'd' cables, screen short
circuits, cable capacitance and inductance), Figures 13.36 to 13.45 and the
closing L/R paragraph. The chapter shell owns the chapter h2, the printed
seventeen-item reference list, the glossary, the source-quirk note and the
copyright; this module emits none of those.

The unnumbered comparison list on printed p.416, the fault-count list on
printed p.417 and the fault-count list printed inside Figure 13.40 are rendered
as prose/list markup, never as tables, so the chapter keeps exactly twelve
numbered tables. Printed quirks are kept verbatim in the English text and
flagged in bilingual notes (Exelsior, R_o/L, Associate apparatus, the
truncated Figure 13.39 caption, 'ration', the 0.033/0.035 microfarad
conflict); the Vietnamese follows the intended meaning. This is an unofficial
study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, eq, note, fig, ul, ol
import mcmillanfig13_f as FF


def body_vi():
    b = []

    # Printed p.411. Figure 13.36 heads the page; the paragraph below is the
    # tail of the section 13.12 discussion carried over from printed p.410.
    b.append(fig(36, FF.fig_f1336()))
    b.append(note("<b>Lưu ý về các nhãn trong Hình 13.36.</b> Bản in viết "
                  "'Exelsior Transmitters Ltd.' (không phải 'Excelsior'); "
                  "'Controller type ×R2' và 'Serial No × 2643' dùng dấu nhân "
                  "'×'; nhãn thứ nhất kết thúc bằng 'EEx [ia] IIc' (chữ c "
                  "thường) còn nhãn thứ hai bằng 'EEx ia IIC T6' (chữ C hoa). "
                  "Lớp văn bản OCR đọc nhầm thành 'xR2', 'Serial No x 2643', "
                  "'U,', 'I,', 'P,', 'L,', 'C,', 'Lo/&amp; = 25~H/ohr' và '0.1 pF'; "
                  "trang render cho thấy U_m, U_o, I_o, P_o, L_o, C_o, "
                  "L_o/R_o = 25 μH/ohm và 0.1 μF. Các dạng đúng từ trang render "
                  "được giữ."))
    b.append(p("được quy định trong phạm vi các cực của chúng nối tới phần tử "
               "chính."))
    b.append(note("<b>Lưu ý về ranh giới đoạn đầu.</b> Đoạn đầu tiên trong phạm "
                  "vi này bắt đầu giữa câu, được tiếp nối từ trang in trước "
                  "(nằm ngoài phạm vi module). Đầu đề chạy trên trang in là "
                  "'Protection concept intrinsic safety 'i' 411'; lớp văn bản "
                  "OCR chèn thêm một dấu cách trong số trang thành '41 1'."))
    b.append(p("Các nhãn điển hình cho thiết bị liên kết và thiết bị an toàn "
               "nội tại được thể hiện trong Hình 13.36."))
    b.append(h3("13.13 Ví dụ về đếm hư hỏng trong thiết bị",
                "13.13 Examples of fault counting in apparatus"))
    b.append(p("Việc đếm hư hỏng để tạo ra thông tin ghi trên nhãn thiết bị "
               "phải được thực hiện trong từng thiết bị."))
    b.append(h3("Thiết bị liên kết", "Associated apparatus"))
    b.append(p("Đây là thiết bị cấp nguồn cho thiết bị an toàn nội tại nhưng "
               "bản thân nó không được lắp đặt trong khu vực nguy hiểm. Hình "
               "13.37 cho thấy một nguồn cấp điển hình đưa điện áp tới khu "
               "vực nguy hiểm, gồm một biến áp lưới không hỏng, sau đó là bộ "
               "chỉnh lưu và tụ điện để làm mượt. Tiếp theo là ba"))
    b.append(note("<b>Lưu ý về ranh giới câu giữa các trang in 411 và 412.</b> "
                  "Câu trên kết thúc bằng 'ba' trên trang in 411 và tiếp tục "
                  "bằng 'điện trở' trên trang in 412; không thêm dấu chấm."))

    # Printed p.412. Continuation of the associated-apparatus paragraph, then
    # the worked 'ib' example. Figure 13.37 follows the example on the page.
    b.append(p("điện trở, R1 có giá trị tối thiểu 700 Ω để hạn dòng tới Z1 "
               "trong điều kiện không tải, R2 có giá trị tối thiểu 30 Ω để tạo "
               "sự tách biệt cần thiết cho việc thử từng diode zener riêng lẻ, "
               "và R3 có giá trị tối thiểu 300 Ω để hạn dòng thêm. Tất cả linh "
               "kiện được giả định có công suất định mức thích hợp."))
    b.append(note("<b>Lưu ý về các giá trị điện trở trong ví dụ.</b> Lớp văn "
                  "bản OCR đọc nhầm thành '700 52', '3052', '30052' và "
                  "'R1 (700 Q) R2 (30 Q) R3 (300 a)'; trang render cho thấy "
                  "700 Ω, 30 Ω, 300 Ω và 'R1 (700 Ω)', 'R2 (30 Ω)', "
                  "'R3 (300 Ω)'. Các giá trị đúng từ trang render được giữ."))
    b.append(p("Với thiết bị 'ib' chỉ cần xét một hư hỏng, đó là hỏng một "
               "trong các diode zener. Điều này cho điện áp ra lớn nhất của "
               "mạch hở là 30V bị giới hạn bởi Z1. Nếu các cực ra bị ngắn "
               "mạch, dòng chảy là 38 mA (39/R1 + R2 + R3). Ở dòng này, điện "
               "áp trên Z1 là 12.5V và điện áp trên Z2 là 11.35V. Vì thế các "
               "diode zener bị tắt và không đóng vai trò nào trong việc xác "
               "định dòng ngắn mạch. Tương tự, nếu nối một tải 1030 Ω (tải "
               "phối hợp) qua các cực ra, điện áp trên Z1 là 17.35 V và trên "
               "Z2 là 17V. Một lần nữa, trong điều kiện tải phối hợp cả Z1 và "
               "Z2 đều bị tắt và không ảnh hưởng đến truyền công suất. Công "
               "suất ra lớn nhất vì thế là 0.37W (39²/4× R1 + R2 + R3). Không "
               "có"))
    b.append(note("<b>Lưu ý về khoảng cách và các ký hiệu trong ví dụ in.</b> "
                  "Bản in viết '39/R1 + R2 + R3' với dấu cách sau dấu cộng đầu "
                  "(OCR thiếu dấu cách này), viết 'Z2' ở nơi OCR đọc nhầm "
                  "thành '22', và '1030 Ω', '39²/4×'. Câu công suất in "
                  "'0.37W' (không dấu cách) trong khi các chỗ khác in '0.37 W'; "
                  "cả hai dạng được giữ nguyên."))
    b.append(note("<b>Lưu ý về ranh giới câu giữa các trang in 412 và 413.</b> "
                  "Đoạn trên kết thúc bằng 'Không có' trên trang in 412, câu "
                  "tiếp tục ở đầu trang in 413 sau Hình 13.37."))
    b.append(fig(37, FF.fig_f1337()))
    b.append(note("<b>Lưu ý về Hình 13.37.</b> Bản in ghi 'Z2 (28 V)' (OCR: "
                  "'22(28V)'), tách riêng 'I_o = 39/1030 A' và 'P_o = 0.37 W' "
                  "(OCR gộp thành 'Po = 0.37W = 39/1030A'), và dùng 'L_o' "
                  "cùng '96 μH/ohm' (OCR: 'b', '96pH/ohm'). Ký hiệu ngoặc là "
                  "'[ib]' chữ thường và '[ia]'; cả hai được giữ nguyên theo "
                  "trang render."))

    # Printed p.413. Continuation of the worked example, 'ia' changes, the
    # label parameter list, and the 'Intrinsically safe apparatus' subheading.
    b.append(p("điện dung thực tế trong mạch vì C được đặt qua điện áp ra của "
               "biến áp và bị tách khỏi các cực ra bởi R1, R2 và R3 mắc nối "
               "tiếp. Vì thế nó trông giống như một nguồn áp chứ không giống "
               "một tụ điện."))
    b.append(p("Nếu xét 'ia', thay đổi duy nhất là hỏng Z1, cho phép điện áp "
               "mạch hở ra tăng tới 39 V. Dòng ngắn mạch ra và công suất ra "
               "vẫn giữ nguyên vì các diode zener không được dùng trong công "
               "thức tính, cũng như điện dung và điện cảm. Các thông số trên "
               "nhãn vì thế sẽ là:"))
    b.append(note("<b>Lưu ý về danh sách thông số trên nhãn.</b> Bản in dùng "
                  "dấu gạch ngang dài '[ib] – output open circuit volts (V_o)' "
                  "(OCR dùng dấu gạch ngắn), và ghi mục tỷ số là '(R_o/L)' dù "
                  "giá trị in '96 μH/Ω' có thứ nguyên của L/R; mục điện cảm "
                  "ngoại trích '(from Fig. 13.35)' trong khi Hình 13.37 trích "
                  "'Fig. 13.5' cho cùng đại lượng. Tất cả được giữ nguyên."))
    b.append(ul([
        "[ib] – điện áp mạch hở ra (V_o) — 30 V",
        "dòng ngắn mạch ra (I_o) — 38 mA",
        "công suất ra lớn nhất (P_o) — 0.37 W",
        "điện cảm ngoại lớn nhất (L_o) — 0.22 mH (từ Hình 13.35)",
        "tỷ số điện cảm ngoại/điện trở lớn nhất (R_o/L) (theo công thức) — 96 μH/Ω",
        "điện dung ngoại lớn nhất — 0.067 μF (từ Hình 13.8)",
    ]))
    b.append(p("Với [ia] các con số đều giữ nguyên ngoại trừ điện áp mạch hở "
               "ra (V_o) tăng tới 39 V, làm giảm điện dung ngoại tới 0.035 μF "
               "tối đa. Trong cả hai trường hợp, không có điện cảm hay điện "
               "dung trong thực tế (L_i hoặc C_i) nhưng điều này thường không "
               "được ghi trên nhãn. Tuy nhiên, nếu có bất kỳ điện cảm trong "
               "nào thì cần ghi lại để cho phép tính tỷ số L/R cho cáp nối."))
    b.append(note("<b>Lưu ý về mâu thuẫn 0.033 μF / 0.035 μF.</b> Hình 13.37 "
                  "ghi '[ia] C_o = 0.033 μF (see above)', trong khi đoạn văn "
                  "này ghi điện dung ngoại giảm tới 0.035 μF tối đa. Cả hai "
                  "giá trị được giữ nguyên; lớp văn bản OCR đọc nhầm "
                  "'capacitances' thành 'capaci-tances' (dấu gạch mềm) và "
                  "'0.035 μF' thành '0.035pF'."))
    b.append(h3("Thiết bị an toàn nội tại", "Intrinsically safe apparatus"))
    b.append(p("Đây là thiết bị thực sự đi vào khu vực nguy hiểm và được cấp "
               "nguồn từ thiết bị liên kết, chẳng hạn như thiết bị thể hiện "
               "trong Hình 13.37. Một thiết bị an toàn nội tại điển hình được "
               "thể hiện trong Hình 13.38. Vì thiết bị này tự nó không được "
               "cấp nguồn, điểm quan tâm chính nằm ở các thông số bên trong "
               "của nó để có thể đánh giá mức độ an toàn khi nối vào một nguồn "
               "cấp. Một lần nữa, người ta giả định rằng tất cả linh kiện đều "
               "có công suất định mức thích hợp cho mục đích phân tích. Vấn đề "
               "hơi khác thường ở đây là sự hiện diện của R1. Sẽ thấy rằng "
               "điện trở này mắc nối tiếp với một biến trở và điều này thường "
               "cần thiết vì công suất tiêu thụ có thể tập trung ở một phần "
               "nhỏ của đường biến trở nếu nó được đặt ở giá trị thấp. Người "
               "ta thường giả định chỉ 10 phần trăm đường biến trở hiện diện "
               "cho mục đích phân loại nhiệt độ và, vì nhiều biến trở rất nhỏ, "
               "điều này gây ra mức tăng nhiệt rất cao thường được giảm thiểu "
               "bằng cách chèn một điện trở nối tiếp như thể hiện."))
    b.append(note("<b>Lưu ý về ngắt dòng trong bản in.</b> Lớp văn bản OCR "
                  "chèn dấu gạch ngắt dòng trong 'presence' và 'minimized'; "
                  "trang render cho thấy 'presence' và 'minimized'. Bản dịch "
                  "dùng dạng đúng từ trang render."))
    b.append(p("Nếu giả định rằng thiết bị phù hợp, về mặt công suất tiêu thụ, "
               "để nối vào nguồn cấp 39V có dòng ngắn mạch 38 mA và khả năng "
               "cung cấp công suất 0.37 W, thì không có điều kiện nào của nguồn "
               "cấp thể hiện trong Hình 13.37 có thể quá tải nó."))

    # Printed p.414. Figure 13.38 heads the page; the 'ib' counting paragraph
    # and the start of the ib parameter list follow.
    b.append(fig(38, FF.fig_f1338()))
    b.append(note("<b>Lưu ý về Hình 13.38.</b> Lớp văn bản OCR đọc nhầm nhóm "
                  "'To Sensor { V_o = See text / I_o = See text' và 'V_o = 30 "
                  "V', '0.033 pF'; trang render cho thấy 'To Sensor { V_o = "
                  "See text' cộng 'I_o = See text', 'V_o = 30 V' và '0.033 μF'. "
                  "Mạch in ghi 'Z1 (19 v)' với chữ v thường, còn phần văn bản "
                  "dùng '19V'; cả hai được giữ nguyên."))
    b.append(p("Với các xét đến 'ib', điện áp lớn nhất từ nguồn cấp là 30 V "
               "và có thể dùng để đánh giá thiết bị này ở chế độ 'ib'. Ở chế "
               "độ 'ib' chỉ cần xét một hư hỏng và đó có thể là hỏng D1 hoặc "
               "Z1. Vì D1 hoặc Z1 luôn hiện diện trong những trường hợp này, "
               "không có khả năng nối trực tiếp tụ điện, C, tới các cực vào "
               "của thiết bị khi nó có thể được nạp tới hơn 19V. Nếu C thực "
               "sự nạp tới hơn 19V khi Z1 hỏng thì nó vẫn an toàn nội tại, ngay "
               "cả khi nó có thể nạp và xả vào một tia lửa bên trong thiết bị "
               "an toàn nội tại, vì điện áp lớn nhất của nguồn cấp là 30V như "
               "đã nêu. Vì điện dung không thể đặt qua các cực ra và nạp tới "
               "hơn 19V, và điện dung lớn nhất cho phép là 0.258 μF ở 19V, "
               "không có vấn đề gì vì điện dung cáp lớn nhất, phải được tính ở "
               "30 V. Do đó, tổng điện dung trong trường hợp 19 V là 0.132 μF, "
               "thấp hơn nhiều so với giới hạn 0.258 μF ngay cả khi cộng thêm "
               "điện dung cáp lớn nhất ở 30V. Các thông số của thiết bị là:"))
    b.append(note("<b>Lưu ý về dấu phẩy thừa và các giá trị trong đoạn này.</b> "
                  "Bản in có dấu phẩy thừa sau 'capacitance': 'the maximum "
                  "cable capacitance, must be calculated at 30 V'; dấu phẩy "
                  "được giữ nguyên trong bản tiếng Anh. Lớp văn bản OCR đọc "
                  "nhầm ''ib' mode' thành 'lib’ mode' và '0.258 μF', '0.132 μF' "
                  "thành '0.258pF', '0.132 pF'."))
    b.append(ul([
        "ib – điện áp vào lớn nhất (V_i) — 30 V",
        "dòng vào lớn nhất (I_i) — 38 mA",
        "công suất vào lớn nhất (P_i) — 0.37 W",
    ]))

    # Printed p.415. Continuation of the ib list, then three paragraphs, the
    # 'ia' list, the cable-capacitance paragraph and the heading 13.14.
    b.append(ul([
        "điện cảm đầu cuối thực dụng (L_i) — 0",
        "điện dung đầu cuối thực dụng (C_i) — 0.033 μF",
    ]))
    b.append(p("Giá trị của C_i là do khả năng điện dung cáp có thể cộng thêm "
               "bên trong thiết bị và điều này hạn chế điện dung cáp ở 0.034 "
               "μF. Người ta thường xử lý bằng cách ghi C_i là 0.033 μF dù "
               "đây không phải điện dung đầu cuối thực tế."))
    b.append(note("<b>Lưu ý về các giá trị 0.034 μF / 0.033 μF và OCR.</b> Lớp "
                  "văn bản OCR đọc nhầm '0.034 μF' thành '0.034pF', 'C_i as "
                  "0.033 μF' thành 'C; as 0.033 pF' và 'information' thành "
                  "'mformation'; trang render cho thấy các dạng đúng như trên."))
    b.append(p("Thông tin quan trọng khác duy nhất là điện áp ra tới cảm biến "
               "có thể tới 30V, và dòng cùng công suất tới cảm biến được kiểm "
               "soát bởi các điện trở R1, R2, R3, R4, R5, R6, R7 và R8. Vì cảm "
               "biến thường rất gần thiết bị an toàn nội tại, điện dung của "
               "đường nối rất nhỏ và dòng tới cảm biến thường nhỏ, nên điện "
               "cảm cũng không gây vấn đề. Thường không cần xác định các thông "
               "số này trên nhãn nhưng vẫn nên nhận biết về tình huống tổng "
               "thể."))
    b.append(p("Khi xét thiết bị cho 'ia' mọi thứ rất khác vì 2 hư hỏng được "
               "áp dụng trong mạch 'ia'. Vì thế nếu D1 hỏng ngắn mạch và Z1 "
               "hỏng hở mạch thì tụ điện được đặt qua các cực. Điều này cho "
               "giá trị C_i là 0.033 μF, ở 30 V vẫn cho phép 0.034 μF trong "
               "cáp. Tuy nhiên, để cho phép nối vào nguồn cấp đã mô tả, V_i "
               "bây giờ tăng tới 39V."))
    b.append(ul([
        "ia – điện áp vào lớn nhất (V_i) — 39 V",
        "dòng vào lớn nhất (I_i) — 38 mA",
        "công suất vào lớn nhất (P_i) — 0.37 W",
        "điện cảm đầu cuối thực dụng (L_i) — 0",
        "điện dung đầu cuối thực dụng (C_i) — 0.033 μF",
    ]))
    b.append(note("<b>Lưu ý về OCR trong danh sách 'ia'.</b> Lớp văn bản OCR "
                  "đọc nhầm 'I_i' thành 'I;', '39 V' thành '39 v' và '0.37 W' "
                  "thành '0.37w'; trang render cho thấy các dạng đúng như trên."))
    b.append(p("Điều này có nghĩa là vì nguồn cấp trong Hình 13.37 cung cấp 39 "
               "V trong trường hợp 'ia' nên nó chỉ phù hợp để nối vào thiết bị "
               "an toàn nội tại này trong trường hợp 'ib', vì điện dung cáp cho "
               "phép của ia giảm tới 0.001 μF (một giá trị không chấp nhận được "
               "– &lt;10 m đối với một cáp có màn chắn điển hình). Tình huống "
               "liên quan tới đầu ra tới cảm biến vẫn không đổi so với trường "
               "hợp 'ib'."))
    b.append(note("<b>Lưu ý về giá trị 0.001 μF.</b> Lớp văn bản OCR đọc nhầm "
                  "đoạn này thành '0.001 pF … tlOm'; trang render cho thấy "
                  "'0.001 μF … &lt;10 m'."))
    b.append(h3("13.14 Hệ thống an toàn nội tại",
                "13.14 Intrinsically safe systems"))
    b.append(p("Như đã nêu trước đó, an toàn nội tại là một khái niệm hệ thống "
               "trong đó phải xét toàn bộ lắp đặt. Việc cấu tạo và quy định "
               "thông số thiết bị như đã mô tả trước đó được dùng làm công cụ "
               "để việc đánh giá một hệ thống dễ dàng hơn nhưng không nhằm "
               "giới hạn quá mức. Việc tạo ra các hệ thống an toàn nội tại được "
               "mô tả trong BS 5501, Part 9 (1982)¹¹ (văn bản của Anh của EN "
               "50039). Có hai cách tạo ra một hệ thống an toàn nội tại, cách "
               "thứ nhất là áp dụng số hư hỏng cho từng thiết bị riêng lẻ, và "
               "cách thứ hai là áp dụng thêm số hư hỏng cho toàn hệ thống. "
               "Cách tiếp cận sau cho thấy an toàn nội tại có thể đạt được trong "
               "những tình huống mà không thể nhận ra điều đó từ các thông số "
               "thiết bị đã tạo ra, như đã thảo luận trước đó trong chương này. "
               "Cần nhớ rằng"))
    b.append(note("<b>Lưu ý về đầu đề chạy và chú thích ¹¹.</b> Lớp văn bản OCR "
                  "đọc nhầm đầu đề chạy 'i' thành '7'' ở nhiều trang và "
                  "chú thích sau 'BS 5501, Part 9 (1982)' thành '’l'; trang "
                  "render cho thấy 'i' và ký hiệu chú thích superscript ¹¹. "
                  "Chú thích này tương ứng với tài liệu tham khảo do phần shell "
                  "của chương cung cấp."))

    # Printed p.416. Continuation of 13.14, comparison criteria (T1 as list),
    # then Figure 13.39 with its truncated caption.
    b.append(p("mục tiêu là đạt được an toàn nội tại với không quá hai hư hỏng "
               "được tính, cộng với các hư hỏng không được tính thích hợp áp "
               "dụng cho hệ thống, hoặc ở một trong các thiết bị tạo thành hệ "
               "thống, hoặc phân bổ giữa tất cả chúng."))
    b.append(p("Cách dễ dàng để đảm bảo an toàn nội tại là so sánh các thông số "
               "đầu ra của thiết bị liên kết với các thông số đầu vào của thiết "
               "bị an toàn nội tại và, nếu trường hợp sau đây xảy ra, an toàn "
               "nội tại được đảm bảo một cách rất đơn giản. Việc so sánh các "
               "thông số nên được thực hiện như sau (và xem Hình 13.39):"))
    b.append(note("<b>Lưu ý về bảng so sánh không đánh số.</b> Bản in xếp các "
                  "dòng thành hai cột có dấu quan hệ ở giữa; ở đây được trình "
                  "bày dạng danh sách để không tạo thêm bảng HTML. Hàng thứ hai "
                  "in 'output current (I_i)' bên trái dù theo ngữ cảnh phải là "
                  "I_o; giữ nguyên chỉ số dưới in. Lớp văn bản OCR đọc nhầm "
                  "các dấu ≤, ≤, ≤, ≥, ≤ thành '-', '5', '2', 'z'."))
    b.append(ul([
        "thiết bị liên kết: điện áp ra (V_o) ≤ thiết bị an toàn nội tại: điện áp vào (V_i)",
        "thiết bị liên kết: dòng ra (I_i) ≤ thiết bị an toàn nội tại: dòng vào (I_i)",
        "thiết bị liên kết: công suất ra (P_o) ≤ thiết bị an toàn nội tại: công suất vào (P_i)",
        "thiết bị liên kết: điện cảm ngoại (L_o) ≥ thiết bị an toàn nội tại: điện cảm đầu cuối thực dụng cộng điện cảm cáp (L_i + L_c)",
        "thiết bị liên kết: điện dung ngoại (C_o) ≤ thiết bị an toàn nội tại: điện dung đầu cuối thực dụng cộng điện dung cáp (C_i + C_c)",
    ]))
    b.append(fig(39, FF.fig_f1339()))
    b.append(note("<b>Lưu ý về Hình 13.39 và chú thích bị cụt.</b> Cả hai hộp "
                  "bên trái in 'Associate apparatus' (không phải 'Associated'); "
                  "hộp trái dưới kết thúc bằng 'L_o/R_o  L_2/R_2' không có toán "
                  "tử, không tự thêm dấu '='. Nhóm 'necessary truths' bị OCR "
                  "xáo trộn thành 'Po = Pp', 'WRo LdRz', 'v35v1+vp', "
                  "'G3 + C4 + Cc s'; dạng đọc từ trang render được giữ. Chú "
                  "thích in kết thúc tại 'If L/R requirements are met the "
                  "inductance requirements need not be' và câu không được "
                  "tiếp tục ở đầu trang in 417; phần cụt này được giữ nguyên "
                  "thay vì tự thêm 'considered'."))

    # Printed p.417. Four paragraphs, fault-count list T2 (as list), then the
    # final paragraph which continues onto printed p.418.
    b.append(p("Trường hợp tỷ số điện cảm/điện trở của cáp (L_c/R_c) đã được "
               "tính (xem trước đó trong chương này), có tính đến điện cảm gộp "
               "(L_i) trong mạch, thì không cần cộng điện cảm cáp vào điện cảm "
               "gộp, miễn là cáp có tỷ số L/R bằng hoặc nhỏ hơn L_i/R_i."))
    b.append(p("Như đã nêu trước đó, một thiết bị 'đơn giản' có thể được thêm "
               "vào hệ thống an toàn nội tại miễn là nhiệt độ của nó không vượt "
               "quá nhiệt độ giới hạn của cấp nhiệt độ mà không cần xem xét chi "
               "tiết thêm. Tuy nhiên, phải xác nhận là nhiệt độ đó không vượt "
               "quá. Dù có thể thêm một thiết bị đơn giản, không được chấp nhận "
               "thêm nhiều thiết bị trừ khi đã thực hiện một nghiên cứu chi tiết "
               "về tổng năng lượng cộng thêm vào hệ thống an toàn nội tại, vì "
               "khả năng cộng năng lượng."))
    b.append(p("Các thiết bị an toàn nội tại và thiết bị liên kết có thể toàn "
               "bộ là 'ia' hoặc 'ib', hoặc có thể là hỗn hợp thiết bị 'ia' và "
               "'ib'. Tuy nhiên, hệ thống tạo thành sẽ là 'ib' trừ khi tất cả "
               "thiết bị đều là 'ia'."))
    b.append(note("<b>Lưu ý về OCR của cụm 'ia'.</b> Lớp văn bản OCR đọc nhầm "
                  "'are 'ia'' thành 'may be ?a''; trang render cho thấy dạng "
                  "đúng như trên."))
    b.append(p("Cách tiếp cận trên bao phủ hầu hết các tình huống thực tế nhưng "
               "trong một vài trường hợp nó không cho phép một cấu hình rõ ràng "
               "là an toàn nội tại. Một phương án khác là đếm hư hỏng của hệ "
               "thống (xem Hình 13.40). Ví dụ, nếu lấy hai thiết bị trong Hình "
               "13.37 và 13.38 thì an toàn nội tại sẽ đạt được nếu trường hợp "
               "sau đây xảy ra:"))
    b.append(note("<b>Lưu ý về danh sách tiêu chí đếm hư hỏng không đánh số.</b> "
                  "Bản in dùng chữ F hoa trong 'Faults' và chữ n thường trong "
                  "'no'; danh sách này được trình bày dạng danh sách, không phải "
                  "bảng HTML."))
    b.append(ul([
        "thiết bị liên kết: 2 Faults — thiết bị an toàn nội tại: no Faults",
        "thiết bị liên kết: 1 Fault — thiết bị an toàn nội tại: 1 Fault",
        "thiết bị liên kết: no Faults — thiết bị an toàn nội tại: 2 Faults",
    ]))
    b.append(p("Áp dụng các tiêu chí trên cho các thiết bị thể hiện trong Hình "
               "13.37 và 13.38 cho thấy rõ rằng việc nối hai thiết bị này tạo "
               "thành một hệ thống an toàn nội tại, trong khi so sánh các thông "
               "số đầu ra và đầu vào của hai thiết bị lại cho kết luận ngược "
               "lại. Tuy nhiên, cách đếm hư hỏng của hệ thống này đòi hỏi kiến "
               "thức đáng kể về chi tiết của hai thiết bị và chỉ có thể thực "
               "hiện ở giai đoạn thiết kế thiết bị. Nó cũng có thể gây hạn chế "
               "lớn cho các thiết bị vì nó xác định thiết bị khác mà mỗi thiết "
               "bị có thể nối vào, thay vì chỉ các thông số dễ so sánh. Vì thế "
               "cách này không thường được dùng nhưng có thể hỗ trợ đáng kể "
               "trong các hệ thống phức tạp như hệ thống thông báo công cộng."))
    b.append(p("Một vấn đề khác là khả năng nối các mạch an toàn nội tại riêng "
               "biệt với nhau trong dây dẫn hiện trường. Để hiểu điều này, cần "
               "xác định quy trình lắp đặt thông thường của các hệ thống an "
               "toàn nội tại. Vì về cơ bản đây là các hệ thống đo lường, thường "
               "dùng để truyền tín hiệu hoặc hệ thống vận hành công suất thấp, "
               "nên cáp chúng dùng trong môi trường công nghiệp thông thường "
               "không chắc chắn như cáp dùng cho mạch điện lực. Một trong những "
               "mục tiêu của mạch an toàn nội tại là duy trì tình huống này và, "
               "vì tia lửa sinh ra do ngắt,"))

    # Printed p.418. Figure 13.40 heads the page; the sentence interrupted
    # above resumes below it, followed by the in-figure fault-count list.
    b.append(fig(40, FF.fig_f1340()))
    b.append(note("<b>Lưu ý về bảng 'Fault count' trong Hình 13.40.</b> Bản in "
                  "đặt 'Fault count' căn giữa ở dòng trên, còn 'Apparatus 1', "
                  "'Apparatus 2', 'Apparatus 3' là tiêu đề cột ở dòng dưới; ở "
                  "đây được trình bày dạng danh sách, không phải bảng HTML. Hộp "
                  "trái dưới kết thúc bằng 'L_o / L_2   L_2/R_2' không có toán "
                  "tử. Nhãn cáp in 'Type'C' cable' không có dấu cách quanh 'C'. "
                  "Lớp văn bản OCR đọc nhầm 'L_o = L_1, C_o = C_1' thành 'b = "
                  "Li C4i' và 'L_o/R_o = L_1/R_1' thành 'L&amp; = LiIRi', đồng thời "
                  "xáo trộn các mảnh sơ đồ ở cuối trang. Chú thích không có "
                  "dấu chấm cuối và ghi 'cases 1, 5 and 6'."))
    b.append(ol([
        "Case 1 — Apparatus 1: 2, Apparatus 2: 0, Apparatus 3: 0",
        "Case 2 — Apparatus 1: 1, Apparatus 2: 1, Apparatus 3: 0",
        "Case 3 — Apparatus 1: 1, Apparatus 2: 0, Apparatus 3: 1",
        "Case 4 — Apparatus 1: 0, Apparatus 2: 1, Apparatus 3: 1",
        "Case 5 — Apparatus 1: 0, Apparatus 2: 2, Apparatus 3: 0",
        "Case 6 — Apparatus 1: 0, Apparatus 2: 0, Apparatus 3: 2",
    ]))
    b.append(p("ngắn mạch hoặc lỗi tiếp đất trong các cáp như vậy sẽ không tạo "
               "ra tia lửa có khả năng gây cháy nổ từ công suất của mạch an "
               "toàn nội tại, thì có thể làm được. Vấn đề nằm ở chỗ thông "
               "thường người ta dùng cáp nhiều lõi, mỗi cáp chứa vài mạch đo "
               "lường, ví dụ như trong hệ thống điện thoại. Các cáp này sau đó "
               "được nối đầu cuối tại chỗ đến nơi có cảm biến, v.v., và dùng "
               "cáp riêng cho phần còn lại của đường chạy"))
    b.append(note("<b>Lưu ý về ranh giới câu giữa các trang in 417 và 418.</b> "
                  "Câu trên bắt đầu ở cuối trang in 417 bằng 'vì tia lửa sinh ra "
                  "do ngắt,' và tiếp tục ở đầu trang in 418 sau Hình 13.40."))

    # Printed p.419. Figure 13.41 heads the page; heading 13.14.1 and three
    # italic cable subheadings follow.
    b.append(fig(41, FF.fig_f1341()))
    b.append(note("<b>Lưu ý về Hình 13.41.</b> Lớp văn bản OCR đọc nhầm "
                  "'Individual cables' thành 'individual ca bIei-1'; trang "
                  "render cho thấy nhãn đó, cùng nhãn giữa 'Multicircuit "
                  "multicore cable' và nhãn 'Junction Box' với chữ B hoa."))
    b.append(h4("13.14.1 Hệ thống cáp nối", "13.14.1 Interconnecting cable systems"))
    b.append(h4("Cáp riêng", "Separate cables"))
    b.append(p("Cách dễ nhất để ngăn nối kết là dùng cáp riêng cho từng mạch an "
               "toàn nội tại riêng lẻ. Cách này giải quyết được vấn đề nhưng "
               "vừa tốn kém vừa cồng kềnh. Cần rất nhiều cáp với chi phí tăng "
               "đáng kể và việc nối đầu cuối trở thành vấn đề vì nhiều cáp riêng "
               "có thể cần đi vào một hộp nối, hoặc có thể cần nhiều hộp nối."))
    b.append(h4("Cáp nhiều lõi", "Multicore cables"))
    b.append(p("Để khắc phục điều này có một số cách tiếp cận cho phép dùng cáp "
               "nhiều lõi chứa nhiều hệ thống an toàn nội tại."))
    b.append(h4("Cáp loại 'a'", "Type 'a' cable"))
    b.append(note("<b>Lưu ý về kiểu nháy đơn trong tiêu đề.</b> Bản in dùng nháy "
                  "đơn kiểu cong ở các tiêu đề 'Type ‘a’ cable' đến 'Type ‘d’ "
                  "cable' nhưng một số chỗ html in nháy thẳng; ở đây dùng nháy "
                  "thẳng thống nhất và ghi rõ sự không nhất quán này."))
    b.append(p("Cách đầu tiên trong số đó là cáp loại 'a'. Trong loại cáp này, "
               "các dẫn của mỗi mạch an toàn nội tại được chứa trong một màn "
               "chắn riêng và cáp sẽ chứa nhiều nhóm dẫn được chắn. Đây là một "
               "nguyên tắc cáp khá phổ biến thường dùng cho các hệ thống đo "
               "lường để ngăn nhiễu chéo trong cáp. Sự hiện diện của các màn "
               "chắn này có nghĩa là, dù"))
    b.append(note("<b>Lưu ý về ranh giới câu giữa các trang in 419 và 420.</b> "
                  "Câu trên kết thúc bằng 'dù' trên trang in 419 và tiếp tục "
                  "trên trang in 420."))

    # Printed p.420. Continuation of Type 'a', three more paragraphs, then the
    # Type 'b' heading and two paragraphs (the second continues).
    b.append(p("hư hỏng có thể xảy ra ở màn chắn trong từng mạch an toàn nội tại, "
               "miễn là các màn chắn được tiếp đất thì không có khả năng các "
               "mạch bị nối kết với nhau. Vấn đề của loại cáp này là các màn "
               "chắn thường không được tách rời khỏi nhau và điều này gây vấn "
               "đề cho an toàn nội tại. Nếu các màn chắn được tiếp đất ở những "
               "nơi khác nhau có thể có điện áp giữa chúng khi xảy ra hư hỏng "
               "nguồn trong lắp đặt chung mà hệ thống an toàn nội tại là một "
               "phần. Vì thế, trừ khi tất cả các lắp đặt đều được tiếp đất tại "
               "cùng một điểm, các màn chắn phải được cách điện với nhau để "
               "chịu được điện áp thử 500 V rms. Tương tự, khi các mạch an toàn "
               "nội tại chứa trong đó cũng được tiếp đất, các màn chắn phải "
               "được tiếp đất tại cùng một điểm hiệu dụng với các mạch được "
               "chứa. Điều này là vì người ta giả định các hư hỏng trong mạch "
               "bên trong màn chắn xảy ra và, nếu mạch và màn chắn được tiếp "
               "đất ở những điểm khác nhau, lại có khả năng dòng từ hư hỏng "
               "trong các lắp đặt điện lực liên quan xâm nhập vào mạch an toàn "
               "nội tại."))
    b.append(note("<b>Lưu ý về cụm 'the another'.</b> Bản in viết 'the screens "
                  "are often not isolated from the another'; dạng này được giữ "
                  "nguyên trong bản tiếng Anh, còn bản tiếng Việt dịch theo ý "
                  "định."))
    b.append(p("Bản thân các dẫn được yêu cầu phải được cách điện theo cách "
               "tương tự như các dẫn công nghiệp thông thường và điều này đòi "
               "hỏi độ dày khoảng 0.2 mm của lớp cách điện đối với polyethylene "
               "hoặc PVC, vì dưới độ dày đó người ta cho rằng, trừ khi có biện "
               "pháp đặc biệt, khó đảm bảo được lớp cách điện liên tục tin cậy."))
    b.append(note("<b>Lưu ý về khoảng cách trong các giá trị 0.2 mm.</b> Trang "
                  "in 420 viết 'around 0.2 mm' (có dấu cách) ở đoạn này nhưng "
                  "'0.2mm minimum thickness' (không dấu cách) ở đoạn cáp loại "
                  "'b'; cả hai được giữ nguyên theo bản in. Lớp văn bản OCR đọc "
                  "nhầm '0.2 mm' thành '0.2 nun'."))
    b.append(p("Tất cả cáp đều được yêu cầu có vỏ bọc có chất lượng thường gắn "
               "với các lắp đặt công nghiệp dùng loại cáp này, nhưng không "
               "được yêu cầu có loại vỏ bọc đặc biệt nào tăng cường bảo vệ như "
               "giáp bọc hay polyethylene liên kết chéo, như trong các nguyên "
               "lý bảo vệ khác. Một trong những yêu cầu chính của vỏ bọc này "
               "là đảm bảo vị trí tương đối của các dẫn được cố định, cho phép "
               "nêu điện cảm và điện dung một cách chắc chắn."))
    b.append(p("Các cáp này được coi là phù hợp để lắp đặt trong hệ thống 'ia' "
               "đi vào Khu vực 0, ngay cả khi trộn với hệ thống 'ia' hoặc 'ib' "
               "không đi vào."))
    b.append(h4("Cáp loại 'b'", "Type 'b' cable"))
    b.append(p("Loại cáp thứ hai được dùng là cáp loại 'b', trong đó không lắp "
               "màn chắn riêng cho từng mạch an toàn nội tại. Các lõi của cáp, "
               "như đối với cáp loại 'a', được yêu cầu có cách điện thích hợp "
               "trên các lõi và điều này thường có nghĩa là độ dày tối thiểu "
               "0.2mm đối với polyethylene hoặc PVC. Ngoài ra, vì những lý do "
               "giống như ở cáp loại 'a', chúng được yêu cầu có vỏ bọc tổng "
               "thể phù hợp, dù không cần yêu cầu bổ sung nào cho vỏ bọc này "
               "ngoài những yêu cầu thường áp dụng trong một lắp đặt công "
               "nghiệp."))
    b.append(p("Các cáp này được giả định là chống được hư hỏng giữa các lõi nếu "
               "chúng được lắp đặt theo cách giảm thiểu nguy cơ hư hỏng cơ khí, "
               "ví dụ được đặt trên khay cáp cố định ở cao độ lớn và được bảo "
               "vệ khỏi hư hỏng từ phía trên, hoặc chạy trong bụng dầm đỡ của "
               "nhà máy sao cho khó bị vật mang đi lại trong nhà máy va chạm. "
               "Loại cáp này có lẽ là loại được dùng phổ biến nhất và thường "
               "được dùng để mang một nhóm mạch từ các vị trí như phòng điều "
               "khiển tới"))

    # Printed p.421. Continuation of Type 'b', two paragraphs, Type 'c' heading
    # and two paragraphs.
    b.append(p("các vị trí cụ thể trong nhà máy hoặc trong xưởng. Chúng không "
               "cần được chắn nhưng có thể được chắn, miễn là tất cả mạch trong "
               "cáp đều được tiếp đất tại cùng một điểm (nếu tiếp đất), và màn "
               "chắn cũng được tiếp đất tại điểm đó."))
    b.append(p("Việc lắp cáp có giáp dây thép hoặc bện không được coi là hiệu "
               "quả để bảo vệ chống hư hỏng cơ khí vì nó không ngăn được cáp bị "
               "ép dập, điều có thể dẫn đến nối kết giữa các hệ thống. Tuy "
               "nhiên, vì lý do vận hành, cáp thường được bọc giáp vì nó cho "
               "một sự bảo vệ nhất định chống hư hỏng và do đó, dù sự bảo vệ "
               "đó không được coi là đủ cho mục đích an toàn nội tại, nó vẫn "
               "tăng độ tin cậy khi vận hành và được dùng cho mục đích đó."))
    b.append(p("Tuy nhiên, một điều cần lưu ý là tính chắc chắn của các cáp như "
               "vậy không được coi là đủ để cho phép các mạch an toàn nội tại "
               "đi vào Khu vực 0 đi qua chúng."))
    b.append(h4("Cáp loại 'c'", "Type 'c' cable"))
    b.append(p("Cáp loại 'c' là cáp có cấu tạo hoàn toàn giống cáp loại 'b' "
               "nhưng được lắp đặt theo cách không bảo vệ có hiệu quả nó khỏi "
               "hư hỏng cơ khí. Vì thế phải xét đến hư hỏng nhưng, do cấu tạo "
               "chắc chắn, hư hỏng bị giới hạn ở những trường hợp sau: thứ nhất, "
               "tối đa hai ngắn mạch giữa các lõi của các mạch an toàn nội tại "
               "khác nhau được coi là xảy ra đồng thời; thứ hai, đồng thời với "
               "các ngắn mạch, bất kỳ số hở mạch nào của lõi cũng có thể xảy "
               "ra. Điều này có tác dụng cho phép nhiều cách nối kết khác nhau "
               "trong các mạch an toàn nội tại, với giới hạn là ba nguồn cấp "
               "mắc nối tiếp hoặc song song vào một thiết bị an toàn nội tại "
               "(xem Hình 13.42) hoặc ba thiết bị an toàn nội tại mắc nối tiếp "
               "hoặc song song vào một nguồn cấp của thiết bị liên kết (xem "
               "Hình 13.43). Có nhiều tổ hợp khác có thể giữa các giới hạn này "
               "cũng cần được xét, và điều đó làm cho việc dùng loại cáp này "
               "rất khó khăn trừ khi nó là một phần của một hệ thống được "
               "thiết kế riêng. Một phân tích dựa trên thông số đầu ra và đầu "
               "cuối của thiết bị gần như chắc chắn trong hầu hết trường hợp "
               "sẽ cho kết quả là không an toàn nội tại."))
    b.append(p("Để khắc phục điều này cần có kiến thức chi tiết về tất cả thiết "
               "bị để cho phép đếm hư hỏng của hệ thống và kiến thức này thường "
               "chỉ nhà sản xuất có. Trong một số trường hợp hạn chế thì không "
               "cần như vậy, ví dụ trường hợp ba nguồn cấp cùng cực tính, mỗi "
               "nguồn được tiếp đất như nhau. Dùng các thông số đầu ra của các "
               "nguồn cấp, có thể hình dung một nguồn cấp tổng hợp có điện áp "
               "tương tự nhưng gấp ba dòng ngắn mạch của một nguồn, chứ không "
               "phải ba nguồn mắc nối tiếp. Vì thế, miễn là dòng tổng hợp vẫn "
               "an toàn nội tại và miễn là cáp cùng các điện cảm và tỷ số L/R "
               "khác được giảm thích hợp, an toàn nội tại của tổ hợp có thể "
               "được suy ra một cách đơn giản. Vì khó khăn này, các cáp như vậy "
               "thường không được quy định trừ trường hợp hệ thống an toàn nội "
               "tại đơn lẻ chứa nhiều mạch an toàn nội tại, chẳng hạn hệ thống "
               "thông báo công cộng, trong đó nhà sản xuất có thể đánh giá chi "
               "tiết toàn bộ hệ thống."))

    # Printed p.422. Figure 13.42 heads the page; Type 'd' heading and one
    # paragraph, with stray OCR-only fragments at the foot.
    b.append(fig(42, FF.fig_f1342()))
    b.append(note("<b>Lưu ý về Hình 13.42.</b> Các dòng 18236–18246 và "
                  "18254–18259 của lớp văn bản OCR là mảnh sơ đồ bị gãy; nhãn "
                  "và chú giải đọc từ trang render được giữ. Chú giải chỉ có "
                  "'D = Open circuit fault.' có dấu chấm cuối; các mục A–C "
                  "không có dấu chấm và dòng 'Power supplies 1, 2 and 3 "
                  "connected in parallel to intrinsically safe apparatus' cũng "
                  "không có dấu chấm."))
    b.append(h4("Cáp loại 'd'", "Type 'd' cable"))
    b.append(p("Ở cáp loại 'd', không áp dụng quy định nào về cách điện và vỏ "
               "bọc cho mục đích an toàn nội tại và nó có thể không đáp ứng "
               "bất kỳ yêu cầu nào của cáp loại 'a', 'b' hoặc 'c'. Bất kỳ số "
               "hư hỏng lõi/lõi đồng thời nào với bất kỳ số hư hỏng hở mạch "
               "đồng thời nào đều được coi là có thể xảy ra. Các giới hạn của "
               "cáp loại 'c' áp dụng còn mạnh hơn cho loại cáp này và nó ít "
               "được dùng nói chung."))

    # Printed p.423. Figure 13.43 heads the page; the screen-short-circuit
    # subheading and two paragraphs.
    b.append(fig(43, FF.fig_f1343()))
    b.append(note("<b>Lưu ý về Hình 13.43.</b> Các dòng 18262–18281 của lớp văn "
                  "bản OCR là mảnh sơ đồ bị gãy; nhãn và chú giải đọc từ trang "
                  "render được giữ. Chú giải có các mục A đến F, không mục nào "
                  "có dấu chấm cuối, và các hộp thiết bị bên phải để trống."))
    b.append(h4("Ngắn mạch màn chắn trong cáp nhiều lõi",
                "Screen short circuits in multicore cables"))
    b.append(p("Việc nối dẫn mạch của bất kỳ mạch an toàn nội tại nào vào màn "
               "chắn được coi là hoạt động bình thường trong tất cả các loại "
               "cáp trên nhưng không ảnh hưởng xấu đến an toàn nội tại, miễn "
               "là cả hai màn chắn được tiếp đất tại cùng một điểm đối với cáp "
               "loại 'a' (điều này tạo thành hai nối song song) hoặc, trong "
               "trường hợp cáp loại 'b', dẫn màn chắn có kích thước đủ để không "
               "hỏng (xem trước đó trong chương này) và nối tiếp đất của nó "
               "cũng không hỏng. Nếu không phải vậy trong cáp loại 'b', màn "
               "chắn phải được cách điện với thân các dẫn ở mức giống như các "
               "dẫn được cách điện với nhau, để có thể bỏ qua hư hỏng bên "
               "trong cáp."))
    b.append(p("Điều này không đúng đối với cáp loại 'c' và 'd' và trong những "
               "trường hợp này phải xét nhiều kết nối màn chắn/dẫn dưới góc độ "
               "tác động của nhiều điểm tiếp đất và nối kết. Đây là một lý do "
               "nữa để tránh các loại cáp này nếu có thể."))

    # Printed p.424. Heading 13.14.2, one paragraph, then Cable capacitance
    # and Cable inductance subheadings with four paragraphs.
    b.append(h4("13.14.2 Đo thông số cáp",
                "13.14.2 Cable parameter measurement"))
    b.append(p("Tính toán các thông số điện cảm và điện dung của cáp khá phức "
               "tạp vì cấu hình của cáp không phải là của một cuộn cảm hay một "
               "tụ điện điển hình (với điện cảm, đó là một cuộn dây một vòng "
               "dài và hẹp, và với tụ điện, đó là hai bản cực có kích thước "
               "rất không lý tưởng). Vì lý do này, cách hiệu quả hơn nhiều là "
               "đo các thông số này trên một đoạn cáp cụ thể. Sau đó chúng có "
               "thể được ngoại suy sang chiều dài lớn hơn một cách chắc chắn "
               "nhờ tính đều đặn của cấu tạo cáp. Cần nhớ rằng cả thông số "
               "lõi/lõi và lõi/màn chắn đều quan trọng."))
    b.append(h4("Điện dung cáp", "Cable capacitance"))
    b.append(p("Điện dung cáp trở thành vấn đề khi các mạch nhóm con IIC có "
               "điện áp mạch hở đáng kể. Một cáp đo lường điển hình có thể có "
               "điện dung giữa các lõi, hoặc giữa một lõi và màn chắn, thấp "
               "tới 50 picofarads/metre nhưng con số này có thể tăng tới hơn "
               "100 picofarads/metre ở một số cáp, và giữa một lõi và màn chắn. "
               "Thường cần biết điện dung của một loại cáp cụ thể là bao "
               "nhiêu. Ví dụ, nếu điện dung lõi/lõi hoặc lõi/màn chắn là 200 "
               "pF/m thì đối với mạch IIC có đầu ra mạch hở 30 V, chiều dài "
               "cáp tối đa bị giới hạn ở 330m đối với cáp không chắn, nhưng có "
               "thể nhỏ hơn 115m đối với cáp có màn chắn vì trong trường hợp "
               "sau có hai điện dung song song (xem Hình 13.44). Dù con số này "
               "có vẻ là chiều dài đủ, cần nhớ rằng do phải đi đường vòng "
               "bắt buộc, các khoảng cách này tương đương với những khoảng "
               "cách nhỏ hơn nhiều tính theo đường chim bay."))
    b.append(p("Trong trường hợp nghi ngờ, rất dễ đo điện dung của một đoạn "
               "cáp 10m của một loại cáp cụ thể bằng một cầu đo điện dung "
               "thông thường và ngoại suy, vì điện dung tỷ lệ với chiều dài, "
               "hoặc lấy thông số của nhà sản xuất."))
    b.append(note("<b>Lưu ý về cách viết 'picofarads' và 'manufacturers'.</b> "
                  "Bản in viết '50 pico-farads/metre' chỉ bị ngắt dòng ở "
                  "'pico- / farads/metre', không phải một từ ghép có dấu gạch "
                  "ngang; lớp văn bản OCR đọc nhầm thành '50 pico-farads/metre' "
                  "liền. Bản in cũng viết 'obtain the manufacturers "
                  "specification' không có dấu nháy đơn, và dùng '330m', "
                  "'115m', '10m' không dấu cách."))
    b.append(h4("Điện cảm cáp", "Cable inductance"))
    b.append(p("Điện cảm cáp có thể được đo bằng một cầu đo điện cảm trên một "
               "đoạn cáp ngắn rồi ngoại suy cho chiều dài lớn hơn, vì điện cảm "
               "tỷ lệ với chiều dài. Nếu điện trở của đoạn đó cũng được đo thì "
               "có thể thu được tỷ số L/R của cáp và tỷ số này tất nhiên không "
               "phụ thuộc vào chiều dài. Tuy nhiên cần có phép đo chính xác vì "
               "một cáp đo lường điển hình có điện cảm 1 μH/m và điện trở 0.1 "
               "Ω/m (10 μH/Ω)."))
    b.append(note("<b>Lưu ý về 'ration' và các giá trị điện cảm.</b> Bản in viết "
                  "'the L/R ration of the cable can also be obtained' — "
                  "'ration' (không phải 'ratio') — và dạng này được giữ nguyên "
                  "trong bản tiếng Anh. Lớp văn bản OCR đọc nhầm '1 μH/m and "
                  "0.1 Ω/m (10 μH/Ω)' thành '1 pH/m and O.lQ/m (lOpH/Q)'; "
                  "trang render cho thấy các giá trị đúng."))
    b.append(p("Tình huống với điện cảm tốt hơn một chút so với điện dung vì "
               "năng lượng tích trữ trong điện cảm liên quan đến dòng chứ không "
               "phải điện áp. Đặt các dẫn song song có tác dụng chia dòng (xem "
               "Hình 13.45) và khi mỗi cuộn cảm riêng biệt, làm giảm một nửa "
               "năng lượng tích trữ. Sự giảm này không có khả năng xảy ra trên "
               "thực tế nhưng nó cho thấy tác động của nối kết lõi/lõi hoặc "
               "lõi/màn chắn trong cáp là làm giảm năng lượng tích trữ, chứ "
               "không làm tăng."))

    # Printed p.425. No running prose: Figures 13.44 and 13.45 in printed order.
    b.append(fig(44, FF.fig_f1344()))
    b.append(note("<b>Lưu ý về phép suy diễn trong Hình 13.44.</b> Bản in viết "
                  "'Capacitance between cores at worst' (không phải 'worst "
                  "case') rồi 'C_T = C_1 + C_2 × C_3/C_2 + C_3', 'If C_2 = C_3' "
                  "và 'C_T = C_1 + 1/2C_2'; giữ nguyên đại số bất thường này. "
                  "Lớp văn bản OCR đọc nhầm dòng cuối thành 'CT = c1 + "
                  "1/2c2'."))
    b.append(fig(45, FF.fig_f1345()))
    b.append(note("<b>Lưu ý về phép suy diễn trong Hình 13.45.</b> Dòng đầu in "
                  "'Stored energy = 0.5 L i²'; các dòng tách vòng ghi '= 0.5 L "
                  "× (0.5 i)²', '= 0.125L i²', '= 2 × 0.125 L i²' và '= 0.25 L "
                  "i²' với khoảng cách riêng; giữ nguyên từng khoảng cách. Lớp "
                  "văn bản OCR đọc nhầm '0.5 L i²' thành '0.5 Liz'. Ghi chú "
                  "trong hình nói rằng phép tính không tính đến ghép tương hỗ "
                  "giữa hai vòng nhưng cho thấy tác động của việc chia dòng."))

    # Printed p.426. Closing L/R paragraph only; the shell owns References.
    b.append(note("<b>Lưu ý về danh sách tài liệu tham khảo do phần shell "
                  "cung cấp.</b> Các đặc điểm in trong danh mục gồm: mục 4 "
                  "'BS 5501.' và mục 8 'IEC 79–11.' có dấu chấm cuối ở cột "
                  "trái; mục 2 viết thường 'service'; mục 6 'Physicalisch'; "
                  "mục 9 'Comite' không dấu; mục 10 'Electrical apparatus' "
                  "viết thường 'apparatus'; mục 16 'Under moist Conditions'. "
                  "Lớp văn bản OCR đọc nhầm mục 4 thành 'Intrinsic Safety, 3’.' "
                  "và mục 10 như in. Phần shell của chương giữ các dạng này."))
    b.append(p("L/R thường không gây vấn đề vì đại đa số mạch an toàn nội tại "
               "được thiết kế có giá trị L/R cho phép trên 25 μH/Ω, lớn hơn "
               "nhiều so với cáp đo lường điển hình."))
    return "".join(b)


def body_en():
    b = []

    # Printed p.411. Figure 13.36 heads the page; the paragraph below is the
    # tail of the section 13.12 discussion carried over from printed p.410.
    b.append(fig(36, FF.fig_f1336()))
    b.append(note("<b>Note on the labels in Fig. 13.36.</b> The print reads "
                  "'Exelsior Transmitters Ltd.' (not 'Excelsior'); 'Controller "
                  "type ×R2' and 'Serial No × 2643' use a multiplication sign; "
                  "the first label ends 'EEx [ia] IIc' (lower-case c) while the "
                  "second ends 'EEx ia IIC T6' (upper-case C). The OCR text "
                  "layer reads 'xR2', 'Serial No x 2643', 'U,', 'I,', 'P,', "
                  "'L,', 'C,', 'Lo/&amp; = 25~H/ohr' and '0.1 pF'; the page render "
                  "shows U_m, U_o, I_o, P_o, L_o, C_o, L_o/R_o = 25 μH/ohm and "
                  "0.1 μF. The render readings are kept."))
    b.append(p("to be specified insofar as its terminals connected to their "
               "primary element are concerned."))
    b.append(note("<b>Note on the opening sentence boundary.</b> The first "
                  "paragraph in this span begins mid-sentence, carried over "
                  "from the preceding printed page (outside this module). The "
                  "running header reads 'Protection concept intrinsic safety "
                  "'i' 411'; the OCR text layer inserts a spurious space in "
                  "the page number as '41 1'."))
    b.append(p("Typical labels for associated and intrinsically safe apparatus "
               "are shown in Fig. 13.36."))
    b.append(h3("13.13 Examples of fault counting in apparatus",
                "13.13 Examples of fault counting in apparatus"))
    b.append(p("Fault counting for production of information to be placed on "
               "apparatus labels has to be all within each piece of apparatus."))
    b.append(h3("Associated apparatus", "Associated apparatus"))
    b.append(p("This is apparatus which feeds intrinsically safe apparatus but "
               "which is not itself intended for installation in a hazardous "
               "area. Figure 13.37 shows a typical power source which feeds a "
               "voltage to the hazardous area comprising an infallible mains "
               "transformer, followed by a rectifier and a capacitor for "
               "smoothing purposes. These are then followed by three"))
    b.append(note("<b>Note on the sentence boundary between printed pp. 411 "
                  "and 412.</b> The paragraph above ends with 'three' on "
                  "printed p. 411 and resumes with 'resistors' on printed p. "
                  "412; no full stop is added."))

    # Printed p.412. Continuation of the associated-apparatus paragraph, then
    # the worked 'ib' example. Figure 13.37 follows the example on the page.
    b.append(p("resistors, R1 having a value of 700 Ω minimum in place to limit "
               "the current to Z1 in no load conditions, R2 having a value of "
               "30 Ω minimum in place to provide the necessary separation for "
               "individual zener diode testing, and R3 having a value of 300 Ω "
               "minimum in place to provide further current limiting. All "
               "components are assumed to have adequate ratings."))
    b.append(note("<b>Note on the resistor values in the worked example.</b> "
                  "The OCR text layer reads '700 52', '3052', '30052' and "
                  "'R1 (700 Q) R2 (30 Q) R3 (300 a)'; the page render shows "
                  "700 Ω, 30 Ω, 300 Ω and 'R1 (700 Ω)', 'R2 (30 Ω)', 'R3 (300 "
                  "Ω)'. The render readings are kept."))
    b.append(p("For 'ib' apparatus it is only necessary to consider one fault, "
               "failure of one of the zener diodes. This will give an open "
               "circuit maximum voltage output of 30V limited by Z1. If the "
               "output terminals are short circuited the current which flows "
               "is 38 mA (39/R1 + R2 + R3). At this current the voltage across "
               "Z1 will be 12.5V and the voltage across Z2 will be 11.35V. "
               "Thus the zener diodes will be switched off and not play any "
               "part in short circuit current determination. Likewise, if a "
               "load of 1030 Ω (a matched load) is connected across the output "
               "terminals, the voltage across Z1 will be 17.35 V and across Z2 "
               "will be 17V. Again, at a matched load situation both Z1 and Z2 "
               "will be switched off and not affect the power transfer. Maximum "
               "output power will therefore be 0.37W (39²/4× R1 + R2 + R3). "
               "There is"))
    b.append(note("<b>Note on spacing and symbols in the worked example.</b> "
                  "The print has '39/R1 + R2 + R3' with a space after the first "
                  "plus sign (the OCR omits it), writes 'Z2' where the OCR "
                  "reads '22', and '1030 Ω', '39²/4×'. The power sentence "
                  "prints '0.37W' without a space while other places print "
                  "'0.37 W'; both forms are kept."))
    b.append(note("<b>Note on the sentence boundary between printed pp. 412 "
                  "and 413.</b> The paragraph above ends with 'There is' on "
                  "printed p. 412; the sentence continues at the top of "
                  "printed p. 413 after Figure 13.37."))
    b.append(fig(37, FF.fig_f1337()))
    b.append(note("<b>Note on Fig. 13.37.</b> The print reads 'Z2 (28 V)' (OCR: "
                  "'22(28V)'), separates 'I_o = 39/1030 A' from 'P_o = 0.37 W' "
                  "(OCR merges them as 'Po = 0.37W = 39/1030A'), and uses 'L_o' "
                  "with '96 μH/ohm' (OCR: 'b', '96pH/ohm'). The bracketed "
                  "designators are lower-case '[ib]' and '[ia]'; both are kept "
                  "as printed."))

    # Printed p.413. Continuation of the worked example, 'ia' changes, the
    # label parameter list, and the 'Intrinsically safe apparatus' subheading.
    b.append(p("no effective capacitance in the circuit as C is placed across "
               "the transformer output voltage and separated from the output "
               "terminals by R1, R2 and R3 in series. It thus looks just like a "
               "voltage supply and not like a capacitor."))
    b.append(p("If 'ia' is considered the only change is the failure of Z1, "
               "which allows the output open circuit voltage to rise to 39 V. "
               "Output short circuit current, and output power remain the same "
               "as the zener diodes are not used in their formulation, as do "
               "capacitance and inductance. The parameters on the label will "
               "therefore be:"))
    b.append(note("<b>Note on the label parameter list.</b> The print uses an "
                  "en dash in '[ib] – output open circuit volts (V_o)' (the "
                  "OCR has a hyphen), labels the ratio item '(R_o/L)' even "
                  "though the printed value '96 μH/Ω' has dimensions of L/R, "
                  "and cites '(from Fig. 13.35)' for external inductance while "
                  "Fig. 13.37 cites 'Fig. 13.5' for the same quantity. All are "
                  "kept as printed."))
    b.append(ul([
        "[ib] – output open circuit volts (V_o) — 30 V",
        "output short circuit current (I_o) — 38 mA",
        "maximum output power (P_o) — 0.37 W",
        "maximum external inductance (L_o) — 0.22 mH (from Fig. 13.35)",
        "maximum external inductance/resistance ratio (R_o/L) (from formula) — 96 μH/Ω",
        "maximum external capacitance — 0.067 μF (from Fig. 13.8)",
    ]))
    b.append(p("For [ia] the figures all remain the same with the exception of "
               "the open circuit output voltage (V_o) which rises to 39 V "
               "reducing external capacitances to 0.035 μF maximum. In both "
               "cases, there is no effective internal inductance or capacitance "
               "(L_i or C_i) but this is not normally recorded on the labelling. "
               "Should there be any internal inductance, however, it is "
               "necessary that it be recorded to permit calculation of the "
               "L/R ratio for interconnecting cables."))
    b.append(note("<b>Note on the 0.033 μF / 0.035 μF conflict.</b> Fig. 13.37 "
                  "gives '[ia] C_o = 0.033 μF (see above)' while this paragraph "
                  "gives external capacitances reducing to 0.035 μF maximum. "
                  "Both values are kept; the OCR text layer reads "
                  "'capacitances' as 'capaci-tances' (soft hyphen) and "
                  "'0.035 μF' as '0.035pF'."))
    b.append(h3("Intrinsically safe apparatus", "Intrinsically safe apparatus"))
    b.append(p("This is the apparatus which does go into the hazardous area and "
               "is powered from associated apparatus, such as that shown in "
               "Fig. 13.37. A typical item of intrinsically safe apparatus is "
               "shown in Fig. 13.38. As this apparatus is not powered itself, "
               "the main interest lies in its internal parameters so that an "
               "assessment of its safety when connected to a power source can "
               "be made. Once again a presumption is made that all components "
               "are properly rated for analysis purposes. The only slightly "
               "unusual problem here is the presence of R1. It will be seen "
               "that the resistor is in series with a variable resistor and "
               "this is often necessary as the power dissipation can be in one "
               "small part of the variable resistor track if it is set to a "
               "low value. It is normally assumed that only 10 per cent of the "
               "track is present for temperature classification purposes and, "
               "as many variable resistors are very small, this gives rise to "
               "very high temperature rises which are often minimized by the "
               "insertion of a series resistor as shown."))
    b.append(note("<b>Note on line-break hyphenation.</b> The OCR text layer "
                  "inserts a break in 'presence' and 'minimized'; the page "
                  "render shows 'presence' and 'minimized'. The translation "
                  "follows the render."))
    b.append(p("If one makes the assumption that the apparatus is suitable, "
               "from a power dissipation point of view, for connection to a "
               "supply of 39V with a short circuit current of 38 mA and a "
               "power delivery capability of 0.37 W, then no condition of the "
               "power source shown in Fig. 13.37 can overload it."))

    # Printed p.414. Figure 13.38 heads the page; the 'ib' counting paragraph
    # and the start of the ib parameter list follow.
    b.append(fig(38, FF.fig_f1338()))
    b.append(note("<b>Note on Fig. 13.38.</b> The OCR text layer garbles the "
                  "group 'To Sensor { V_o = See text / I_o = See text' and "
                  "'V_o = 30 V', '0.033 pF'; the page render shows 'To Sensor { "
                  "V_o = See text' plus 'I_o = See text', 'V_o = 30 V' and "
                  "'0.033 μF'. The circuit prints 'Z1 (19 v)' with a lower-case "
                  "v while the prose uses '19V'; both are kept."))
    b.append(p("For 'ib' considerations the maximum voltage from the power "
               "source is 30 V and can be used for evaluation of this apparatus "
               "in the 'ib' mode. In the 'ib' mode only one fault needs to be "
               "considered and that can be the failure of D1 or Z1. As either "
               "D1 or Z1 is always present in these circumstances there is no "
               "possibility of direct connection of the capacitance, C, to the "
               "input terminals of the apparatus when it can be charged to more "
               "than 19V. If C does charge to more than 19V on failure of Z1 "
               "then it is intrinsically safe, even if it can charge and "
               "discharge into a spark within the intrinsically safe apparatus, "
               "because the maximum voltage of the power source is 30V as "
               "already stated. As the capacitance cannot be placed across the "
               "output terminals and charged to more than 19V, and the maximum "
               "permissible capacitance is 0.258 μF at 19V, no problem exists "
               "because the maximum cable capacitance, must be calculated at "
               "30 V. Therefore, the total capacitance in the 19 V situation is "
               "0.132 μF, well below the 0.258 μF limit even with the maximum "
               "30V cable capacitance added. Parameters for the apparatus are:"))
    b.append(note("<b>Note on the stray comma and the values in this "
                  "paragraph.</b> The print has a stray comma after "
                  "'capacitance': 'the maximum cable capacitance, must be "
                  "calculated at 30 V'; it is kept verbatim in English. The "
                  "OCR text layer reads ''ib' mode' as 'lib’ mode' and "
                  "'0.258 μF', '0.132 μF' as '0.258pF', '0.132 pF'."))
    b.append(ul([
        "ib – maximum input voltage (V_i) — 30 V",
        "maximum input current (I_i) — 38 mA",
        "maximum input power (P_i) — 0.37 W",
    ]))

    # Printed p.415. Continuation of the ib list, then three paragraphs, the
    # 'ia' list, the cable-capacitance paragraph and the heading 13.14.
    b.append(ul([
        "effective terminal inductance (L_i) — 0",
        "effective terminal capacitance (C_i) — 0.033 μF",
    ]))
    b.append(p("The value of C_i is because of the possibility that the cable "
               "capacitance can add internally to the apparatus and this "
               "restricts cable capacitance to 0.034 μF. This is normally dealt "
               "with by specifying C_i as 0.033 μF even though this is not the "
               "actual terminal capacitance."))
    b.append(note("<b>Note on the 0.034 μF / 0.033 μF values and OCR.</b> The "
                  "OCR text layer reads '0.034 μF' as '0.034pF', 'C_i as 0.033 "
                  "μF' as 'C; as 0.033 pF' and 'information' as 'mformation'; "
                  "the page render shows the correct forms given above."))
    b.append(p("The only other important information is the voltage out to the "
               "sensor which can be up to 30V, and the current and power to the "
               "sensor which are controlled by resistors R1, R2, R3, R4, R5, "
               "R6, R7 and R8. As the sensor is usually very close to the "
               "intrinsically safe apparatus the capacitance of the connection "
               "is very small and the current to the sensor is usually small, "
               "also making inductance no problem. It is not usually necessary "
               "to identify these parameters on the label but one should be "
               "aware of the total situation nonetheless."))
    b.append(p("When considering the apparatus for 'ia' matters are very "
               "different as 2 faults are applied in 'ia' circuits. Thus if D1 "
               "fails to short circuit and Z1 to open circuit, the capacitor "
               "is across the terminals. This gives a C_i figure of 0.033 μF "
               "which at 30 V still allows for 0.034 μF in the cable. To allow "
               "connection to the described power source, however, V_i is now "
               "increased to 39V."))
    b.append(ul([
        "ia – maximum input voltage (V_i) — 39 V",
        "maximum input current (I_i) — 38 mA",
        "maximum input power (P_i) — 0.37 W",
        "effective terminal inductance (L_i) — 0",
        "effective terminal capacitance (C_i) — 0.033 μF",
    ]))
    b.append(note("<b>Note on OCR in the 'ia' list.</b> The OCR text layer "
                  "reads 'I_i' as 'I;', '39 V' as '39 v' and '0.37 W' as "
                  "'0.37w'; the page render shows the correct forms."))
    b.append(p("This means that as the power supply in Fig. 13.37 supplies 39 V "
               "in the 'ia' situation it is only suitable for connection to "
               "this intrinsically safe apparatus in the 'ib' situation as "
               "permissible cable capacitance for ia is reduced to 0.001 μF (an "
               "unacceptably low figure – &lt;10 m for a typical screened "
               "cable). The situation in respect of the output to the sensor "
               "remains unchanged from the 'ib' situation."))
    b.append(note("<b>Note on the 0.001 μF value.</b> The OCR text layer reads "
                  "this as '0.001 pF … tlOm'; the page render shows '0.001 μF "
                  "… &lt;10 m'."))
    b.append(h3("13.14 Intrinsically safe systems",
                "13.14 Intrinsically safe systems"))
    b.append(p("As previously stated, intrinsic safety is a system concept in "
               "which the total installation has to be considered. The "
               "construction and specification of apparatus as previously "
               "described is used as a tool to make the evaluation of a system "
               "easier but is not intended to be excessively limiting. The "
               "production of intrinsically safe systems is described in BS "
               "5501, Part 9 (1982)¹¹ (the UK text of EN 50039). There are two "
               "ways of producing an intrinsically safe system, the first being "
               "to apply the fault counts to each item of apparatus "
               "individually, and the second to additionally apply the count to "
               "the system as a whole. The latter approach shows intrinsic "
               "safety can be achieved in situations where it is not possible "
               "to identify this from the apparatus parameters produced, as "
               "discussed earlier in this chapter. It must be remembered that"))
    b.append(note("<b>Note on the running header and footnote ¹¹.</b> The OCR "
                  "text layer misreads the running header 'i' as '7'' on "
                  "several pages and the marker after 'BS 5501, Part 9 (1982)' "
                  "as '’l'; the page render shows 'i' and superscript "
                  "footnote ¹¹. The marker resolves to a reference supplied by "
                  "the chapter shell."))

    # Printed p.416. Continuation of 13.14, comparison criteria (T1 as list),
    # then Figure 13.39 with its truncated caption.
    b.append(p("the objective is to achieve intrinsic safety with up to two "
               "countable faults, plus appropriate non-countable faults applied "
               "to the system, either in one of the items of apparatus forming "
               "it or divided among all of them."))
    b.append(p("The easy way to ensure intrinsic safety is to compare the output "
               "parameters of associated apparatus with the input parameters "
               "of intrinsically safe apparatus and, if the following is the "
               "case, intrinsic safety is ensured very simply. The comparison "
               "of parameters should be carried out as follows (and see Fig. "
               "13.39):"))
    b.append(note("<b>Note on the unnumbered comparison list.</b> The print "
                  "sets the lines as two columns with relational signs between "
                  "them; here they are rendered as a list so as not to add an "
                  "HTML table. Row 2 prints 'output current (I_i)' on the left "
                  "although the context requires I_o; the printed subscript is "
                  "kept. The OCR text layer reads the signs ≤, ≤, ≤, ≥, ≤ as "
                  "'-', '5', '2', 'z'."))
    b.append(ul([
        "associated apparatus: output voltage (V_o) ≤ intrinsically safe apparatus: input voltage (V_i)",
        "associated apparatus: output current (I_i) ≤ intrinsically safe apparatus: input current (I_i)",
        "associated apparatus: output power (P_o) ≤ intrinsically safe apparatus: input power (P_i)",
        "associated apparatus: external inductance (L_o) ≥ intrinsically safe apparatus: effective terminal inductance plus cable inductance (L_i + L_c)",
        "associated apparatus: external capacitance (C_o) ≤ intrinsically safe apparatus: effective terminal capacitance plus cable capacitance (C_i + C_c)",
    ]))
    b.append(fig(39, FF.fig_f1339()))
    b.append(note("<b>Note on Fig. 13.39 and the truncated caption.</b> Both "
                  "left-hand boxes read 'Associate apparatus' (not 'Associated'); "
                  "the lower box ends 'L_o/R_o  L_2/R_2' with no operator, and "
                  "no '=' is inserted. The 'necessary truths' group is garbled "
                  "in the OCR layer as 'Po = Pp', 'WRo LdRz', 'v35v1+vp', "
                  "'G3 + C4 + Cc s'; the page-render reading is kept. The "
                  "printed caption ends at 'If L/R requirements are met the "
                  "inductance requirements need not be' and the sentence is "
                  "not continued at the top of printed p. 417; the truncation "
                  "is preserved rather than supplying 'considered'."))

    # Printed p.417. Four paragraphs, fault-count list T2 (as list), then the
    # final paragraph which continues onto printed p.418.
    b.append(p("Where the cable inductance to resistance ratio (L_c/R_c) has "
               "been calculated (see earlier in this chapter), taking account "
               "of the lumped inductance (L_i) in the circuit, it is not "
               "necessary to add the cable inductance to the lumped inductance "
               "provided that the cable has an L/R ratio equal to or less than "
               "L_i/R_i."))
    b.append(p("As previously stated, an item of 'simple apparatus' may be "
               "added into the intrinsically safe system provided that its "
               "temperature does not exceed the limiting temperature of the "
               "temperature class without further detailed consideration. The "
               "temperature must, however, be confirmed as not doing so. While "
               "a single item of simple apparatus may be added it is not "
               "acceptable to add several items unless a detailed study of the "
               "total addition of energy to the intrinsically safe system has "
               "been carried out because of the possibility of energy addition."))
    b.append(p("The items of intrinsically safe apparatus and associated "
               "apparatus may be either all 'ia' or 'ib' or may be a mixture of "
               "'ia' and 'ib' apparatus. The resulting system will, however, be "
               "'ib' unless all items of apparatus are 'ia'."))
    b.append(note("<b>Note on OCR of the 'ia' phrase.</b> The OCR text layer "
                  "reads 'are 'ia'' as 'may be ?a''; the page render shows the "
                  "correct form."))
    b.append(p("The above approach covers most practical situations but in a "
               "few cases it would not permit a configuration which was "
               "manifestly intrinsically safe. An alternative is the system "
               "fault count (see Fig. 13.40). If, for example, we were to take "
               "the two items of apparatus in Fig. 13.37 and 13.38 intrinsic "
               "safety would be achieved if the following were the case:"))
    b.append(note("<b>Note on the unnumbered fault-count criteria list.</b> "
                  "The print uses a capital F in 'Faults' and a lower-case n "
                  "in 'no'; the list is rendered as list markup, not as an "
                  "HTML table."))
    b.append(ul([
        "associated apparatus: 2 Faults — intrinsically safe apparatus: no Faults",
        "associated apparatus: 1 Fault — intrinsically safe apparatus: 1 Fault",
        "associated apparatus: no Faults — intrinsically safe apparatus: 2 Faults",
    ]))
    b.append(p("Application of the above criteria to the apparatus shown in "
               "Figs. 13.37 and 13.38 shows clearly that interconnection of the "
               "two items of apparatus comprises an intrinsically safe system, "
               "whereas comparison of the output and input parameters of the "
               "two items of apparatus indicates the contrary. This system "
               "fault count, however, requires considerable knowledge of the "
               "detail of the two items of apparatus and can only be carried "
               "out at the apparatus design stage. It also can be very "
               "restrictive on the items of apparatus as it will identify the "
               "other apparatus with which each item of apparatus can be "
               "interconnected, rather than the parameters only which are easy "
               "to compare. It is thus not often used but can be of significant "
               "assistance in complex systems such as public address systems."))
    b.append(p("Another problem is the possibility of interconnection of "
               "separate intrinsically safe circuits in field wiring. To "
               "understand this it is necessary to identify the normal "
               "procedure for installation of intrinsically safe systems. "
               "Because these are basically normally instrumentation systems, "
               "usually for intelligence transmission or low power operating "
               "systems, the cables which they use in the normal industrial "
               "context are not as robust as those used for power circuits. It "
               "is one of the objectives of intrinsically safe circuits that "
               "this situation be maintained and, as sparking produced by "
               "breaking,"))

    # Printed p.418. Figure 13.40 heads the page; the sentence interrupted
    # above resumes below it, followed by the in-figure fault-count list.
    b.append(fig(40, FF.fig_f1340()))
    b.append(note("<b>Note on the 'Fault count' list in Fig. 13.40.</b> The "
                  "print centres 'Fault count' over a first line, with "
                  "'Apparatus 1', 'Apparatus 2' and 'Apparatus 3' as the column "
                  "headings on the next line; here they are rendered as a "
                  "list, not as an HTML table. The lower-left box ends 'L_o / "
                  "L_2   L_2/R_2' with no operator. The cable label prints "
                  "'Type'C' cable' with no spaces around 'C'. The OCR text "
                  "layer reads 'L_o = L_1, C_o = C_1' as 'b = Li C4i' and "
                  "'L_o/R_o = L_1/R_1' as 'L&amp; = LiIRi', and scrambles diagram "
                  "fragments at the foot of the page. The caption has no final "
                  "full stop and specifies 'cases 1, 5 and 6'."))
    b.append(ol([
        "Case 1 — Apparatus 1: 2, Apparatus 2: 0, Apparatus 3: 0",
        "Case 2 — Apparatus 1: 1, Apparatus 2: 1, Apparatus 3: 0",
        "Case 3 — Apparatus 1: 1, Apparatus 2: 0, Apparatus 3: 1",
        "Case 4 — Apparatus 1: 0, Apparatus 2: 1, Apparatus 3: 1",
        "Case 5 — Apparatus 1: 0, Apparatus 2: 2, Apparatus 3: 0",
        "Case 6 — Apparatus 1: 0, Apparatus 2: 0, Apparatus 3: 2",
    ]))
    b.append(p("short circuiting, or earth faults in such cables will not "
               "produce ignition capable sparks from the power in intrinsically "
               "safe circuits, it is possible to do so. The problem lies in "
               "the fact that it is normal to use multicore cables each "
               "containing several instrumentation circuits, as, for example, "
               "in telephone systems. These cables are then locally terminated "
               "to the point where sensors, etc., occur and individual cables "
               "used for the latter part of the run"))
    b.append(note("<b>Note on the sentence boundary between printed pp. 417 "
                  "and 418.</b> The sentence begins at the foot of printed p. "
                  "417 with 'as sparking produced by breaking,' and continues "
                  "at the top of printed p. 418 after Figure 13.40."))

    # Printed p.419. Figure 13.41 heads the page; heading 13.14.1 and three
    # italic cable subheadings follow.
    b.append(fig(41, FF.fig_f1341()))
    b.append(note("<b>Note on Fig. 13.41.</b> The OCR text layer reads "
                  "'Individual cables' as 'individual ca bIei-1'; the page "
                  "render shows that label, the centre label 'Multicircuit "
                  "multicore cable' and 'Junction Box' with a capital B."))
    b.append(h4("13.14.1 Interconnecting cable systems",
                "13.14.1 Interconnecting cable systems"))
    b.append(h4("Separate cables", "Separate cables"))
    b.append(p("The easy way to prevent interconnection is to use separate "
               "cables for each individual intrinsically safe circuit. This "
               "solves the problem but is both expensive and cumbersome. Very "
               "large numbers of cables are required at considerable extra "
               "cost and termination becomes a problem in that many individual "
               "cables may need to enter one connection box, or many connection "
               "boxes may be necessary."))
    b.append(h4("Multicore cables", "Multicore cables"))
    b.append(p("To overcome this there are several approaches which will allow "
               "the use of multicore cables containing several intrinsically "
               "safe systems."))
    b.append(h4("Type 'a' cable", "Type 'a' cable"))
    b.append(note("<b>Note on the quote style in the subheadings.</b> The print "
                  "uses curly single quotes in the subheadings 'Type ‘a’ "
                  "cable' through 'Type ‘d’ cable' but some occurrences use "
                  "straight quotes; straight quotes are used consistently here "
                  "and the typographic inconsistency is flagged."))
    b.append(p("The first of these is a Type 'a' cable. In this cable the "
               "conductors of each intrinsically safe circuit are contained in "
               "an individual screen and the cable will contain many screened "
               "groups of conductors. This is a fairly general type of cable "
               "principal often used for instrumentation systems to prevent "
               "crosstalk in the cable. The presence of such screens means "
               "that, although"))
    b.append(note("<b>Note on 'principal'.</b> The print has 'This is a fairly "
                  "general type of cable principal often used for "
                  "instrumentation systems' — 'principal' (not 'principle'); "
                  "the wording is kept verbatim in English while the "
                  "Vietnamese follows the intended meaning."))
    b.append(note("<b>Note on the sentence boundary between printed pp. 419 "
                  "and 420.</b> The paragraph above ends with 'although' on "
                  "printed p. 419 and continues on printed p. 420."))

    # Printed p.420. Continuation of Type 'a', three more paragraphs, then the
    # Type 'b' heading and two paragraphs (the second continues).
    b.append(p("faults to the screen can occur in each intrinsically safe "
               "circuit, provided the screens are earthed there is no likelihood "
               "of circuits becoming interconnected. The problem with this "
               "type of cable is that the screens are often not isolated from "
               "the another and this creates a problem for intrinsic safety. "
               "If the screens are earthed at different places there could be "
               "voltage between them when power faults occur in the general "
               "installation of which the intrinsically safe systems are a "
               "part. Unless, therefore, all of the installations are earthed "
               "at the same point, the screens must be insulated one from "
               "another so that they will withstand a test voltage of 500 V "
               "rms. Likewise, where the intrinsically safe circuits which "
               "they contain are also earthed, the screens must be earthed at "
               "the same effective point as the contained circuits. This is "
               "because faults in the circuit within the screen are assumed to "
               "occur and, if the circuit and screen are earthed at different "
               "points, there is again the possibility of invasion of the "
               "intrinsically safe circuit by currents due to faults in "
               "associated power installations."))
    b.append(note("<b>Note on 'the another'.</b> The print has 'the screens are "
                  "often not isolated from the another'; the wording is kept "
                  "verbatim in English while the Vietnamese follows the "
                  "intended meaning."))
    b.append(p("The conductors themselves are required to be insulated in the "
               "same way as their normal industrial counterparts are and this "
               "requires around 0.2 mm thickness of insulation for polyethylene "
               "or PVC, as below this thickness it is considered that, unless "
               "special precautions are taken, it is difficult to ensure a "
               "reliable continuous insulation cover."))
    b.append(note("<b>Note on the 0.2 mm spacing.</b> Printed p. 420 has "
                  "'around 0.2 mm' (with a space) in this paragraph but '0.2mm "
                  "minimum thickness' (no space) in the Type 'b' paragraph; "
                  "both are kept as printed. The OCR text layer reads '0.2 mm' "
                  "as '0.2 nun'."))
    b.append(p("All cables are required to have a sheath of the quality "
               "normally associated with industrial installations using this "
               "type of cable, but they are not required to have any particular "
               "type of sheath offering increased protection such as armouring "
               "or cross-linked polyethylene, as in other protection concepts. "
               "One of the principal requirements for this sheath is to ensure "
               "that conductor relative positions are fixed enabling inductance "
               "and capacitance to be quoted with confidence."))
    b.append(p("These cables are considered as suitable for installation in "
               "'ia' systems, which enter Zone 0, even when mixed with 'ia' or "
               "'ib' systems which do not."))
    b.append(h4("Type 'b' cable", "Type 'b' cable"))
    b.append(p("The second type of cable used is the Type 'b' cable in which "
               "individual intrinsically safe circuit screens are not fitted. "
               "The cores of the cable are, as for type 'a' cable, required to "
               "have adequate insulation on the cores and this normally means "
               "0.2mm minimum thickness for polyethylene or PVC. In addition, "
               "for the same reasons as in Type 'a' cable they are required to "
               "have a suitable overall sheath, although no additional "
               "requirements for this are necessary other than those which "
               "would normally be applied in an industrial installation."))
    b.append(p("These cables are assumed to be proof against faults between "
               "cores if they are installed in a way which minimizes the risk "
               "of damage by, for example, being led on a cable tray fixed at "
               "high level and protected from damage from above, or being run "
               "in the web of plant support girders so that they are unlikely "
               "to be struck by objects being carried around the plant. This "
               "type of cable is probably the most common type of cable used "
               "and is normally used to carry a group of circuits from "
               "locations such as control rooms to"))

    # Printed p.421. Continuation of Type 'b', two paragraphs, Type 'c' heading
    # and two paragraphs.
    b.append(p("particular locations on a plant or in a factory. They need not "
               "be screened but may be, provided all of the circuits within "
               "the cable are earthed at the same point (if earthed), and the "
               "screen is earthed at that point also."))
    b.append(p("The fitting of cables with a steel wire or braid armouring is "
               "not considered as effective for the purposes of protection "
               "against mechanical damage as it does not prevent the cable "
               "being crushed which could lead to interconnection between "
               "systems. For operational reasons, however, cables are often "
               "armoured as it gives some protection against damage and thus, "
               "although that protection is not considered as enough for "
               "intrinsic safety purposes, it does increase reliability of "
               "operation and is used for that purpose."))
    b.append(p("One consideration which must be borne in mind, however, is "
               "that the security of such cables is not considered as "
               "sufficient to allow intrinsically safe circuits, which enter "
               "Zone 0, to pass through them."))
    b.append(h4("Type 'c' cable", "Type 'c' cable"))
    b.append(p("A Type 'c' cable is one of exactly the same construction as a "
               "Type 'b' cable but installed in a way which does not effectively "
               "protect it from mechanical damage. Thus damage has to be "
               "considered but, because of its robust construction, the damage "
               "is limited to the following: first, up to two short circuits "
               "between cores of different intrinsically safe circuits will be "
               "considered to occur coincidently; second, at the same time as "
               "the short circuits, any number of open circuits of cores may "
               "occur. This has the effect of permitting a variety of "
               "interconnections in intrinsically safe circuits, the limits of "
               "which are three power sources in series, or parallel connected, "
               "to a single item of intrinsically safe apparatus (see Fig. "
               "13.42) or three items of intrinsically safe apparatus in series, "
               "or parallel connected, to a single associated apparatus power "
               "source (see Fig. 13.43). There are many other possible "
               "combinations between these limits which also need consideration, "
               "and this makes the use of this cable very difficult unless it "
               "forms part of a specifically designed system. An analysis based "
               "upon the output and terminal parameters of apparatus would "
               "almost certainly in most cases identify the result as non-"
               "intrinsically safe."))
    b.append(p("To overcome this, detailed knowledge of all apparatus is "
               "necessary to allow a system fault count and this knowledge is "
               "usually only known to the manufacturer. In limited cases this "
               "is not necessary as in the case of three identical polarity "
               "power sources, each identically earthed. Using output "
               "parameters for the power sources, a composite power source of "
               "similar voltage but three times the short circuit current of "
               "one can be envisaged, but not three series power sources. Thus "
               "provided the resultant current remains intrinsically safe and, "
               "provided the cable and other inductances and L/R ratios are "
               "suitably reduced, intrinsic safety of the composite can be "
               "simply deduced. Due to this difficulty such cables are not "
               "normally specified except in the case of single intrinsically "
               "safe systems which contain multiple intrinsically safe circuits, "
               "such as public address systems, in which the manufacturer can "
               "carry out a detailed evaluation of the entire system."))

    # Printed p.422. Figure 13.42 heads the page; Type 'd' heading and one
    # paragraph, with stray OCR-only fragments at the foot.
    b.append(fig(42, FF.fig_f1342()))
    b.append(note("<b>Note on Fig. 13.42.</b> Raw lines 18236–18246 and "
                  "18254–18259 are broken fragments of the diagram in the OCR "
                  "text layer; the render labels and legend are kept. In the "
                  "legend only 'D = Open circuit fault.' has a final full "
                  "stop; items A–C do not, and the line 'Power supplies 1, 2 "
                  "and 3 connected in parallel to intrinsically safe "
                  "apparatus' has no full stop."))
    b.append(h4("Type 'd' cable", "Type 'd' cable"))
    b.append(p("In Type 'd' cable no specification of insulation and sheathing "
               "for the purposes of intrinsic safety are applied and it may not "
               "meet any of the requirements of Type 'a', 'b' or 'c' cables. "
               "Any number of simultaneous core/core faults with any number of "
               "simultaneous open circuit faults are considered as possible. "
               "The limitations of Type 'c' cable apply even more to this type "
               "of cable and it has little general use."))

    # Printed p.423. Figure 13.43 heads the page; the screen-short-circuit
    # subheading and two paragraphs.
    b.append(fig(43, FF.fig_f1343()))
    b.append(note("<b>Note on Fig. 13.43.</b> Raw lines 18262–18281 are broken "
                  "diagram fragments in the OCR text layer; the render labels "
                  "and legend are kept. The legend lists A to F with no final "
                  "full stop on any item, and the right-hand apparatus boxes "
                  "are blank."))
    b.append(h4("Screen short circuits in multicore cables",
                "Screen short circuits in multicore cables"))
    b.append(p("The connection of circuit conductors of any intrinsically safe "
               "circuit to the screen is considered as normal operation in all "
               "of the above types of cable but does not adversely affect "
               "intrinsic safety, provided that both of the screens are earthed "
               "at the same point in Type 'a' cable (this constitutes two "
               "parallel connections) or, in the case of Type 'b' cable, the "
               "screen conductor is a sufficient size to be infallible (see "
               "earlier in this chapter) and its earth connection is also "
               "infallible. If this is not so in Type 'b' cables, the screen "
               "must be insulated from the body of conductors to the same "
               "level as the conductors are insulated from one another so that "
               "faults can be ignored within the cable."))
    b.append(p("This is not true for Type 'c' and 'd' cables and in these cases "
               "multiple screen/conductor connections must be considered from "
               "the standpoint of the effects of multiple earths and "
               "interconnections. This is a further reason for avoiding such "
               "cables if possible."))

    # Printed p.424. Heading 13.14.2, one paragraph, then Cable capacitance
    # and Cable inductance subheadings with four paragraphs.
    b.append(h4("13.14.2 Cable parameter measurement",
                "13.14.2 Cable parameter measurement"))
    b.append(p("Calculation of cable parameters of inductance and capacitance "
               "is somewhat complex due to the fact that the configuration of "
               "a cable is not that of a classic inductor or a classic "
               "capacitor (for inductance it is a long narrow single-turn coil, "
               "and for a capacitor it is two plates of far from ideal "
               "dimension). For this reason it is far more effective to measure "
               "these parameters on a specific length of cable. They can then "
               "be extrapolated on to longer lengths with confidence due to "
               "the regular nature of cable construction. It must be remembered "
               "that the core/core and core/screen parameters are both "
               "important."))
    b.append(h4("Cable capacitance", "Cable capacitance"))
    b.append(p("Cable capacitance becomes a problem where sub-group IIC circuits "
               "have significant open circuit voltages. A typical "
               "instrumentation cable may have a capacitance between cores, or "
               "a core and the screen, of as little as 50 picofarads/metre but "
               "this figure may rise to in excess of 100 picofarads/metre in "
               "some cables, and between a core and the screen. It is usually "
               "necessary to know what the capacitance of a particular type of "
               "cable is. If the core/core or core/screen capacitance were 200 "
               "pF/m, for example, then for IIC circuits at 30 V open circuit "
               "output the maximum cable length would be restricted to 330m "
               "for an unscreened cable, but may be less than 115m for a "
               "screened cable as two parallel capacitances are involved in "
               "this latter case (see Fig. 13.44). While this may appear to be "
               "an adequate length, it must be remembered that because of the "
               "necessary deviation in cable runs these distances are "
               "equivalent to much smaller distances as the crow flies."))
    b.append(p("In any case of doubt it is easy to measure the cable capacity "
               "of a 10m length of a particular cable using a normal capacitance "
               "bridge, and extrapolate as capacitance is proportional to "
               "length, or obtain the manufacturers specification."))
    b.append(note("<b>Note on 'picofarads' and 'manufacturers'.</b> The print "
                  "has '50 pico-farads/metre' split only by line-end "
                  "hyphenation ('pico-' / 'farads/metre'), not a hyphenated "
                  "compound; the OCR text layer reads it as a joined word. The "
                  "print also has 'obtain the manufacturers specification' "
                  "without an apostrophe, and uses '330m', '115m', '10m' "
                  "without a space."))
    b.append(h4("Cable inductance", "Cable inductance"))
    b.append(p("Cable inductance can be measured using an inductance bridge on "
               "a short length of cable and extrapolating for longer lengths, "
               "as inductance is proportional to length. If the resistance of "
               "that length is also measured the L/R ration of the cable can "
               "also be obtained and this is, of course, independent of length. "
               "Accurate measurements are necessary, however, as a standard "
               "instrumentation cable is typically 1 μH/m and 0.1 Ω/m (10 "
               "μH/Ω)."))
    b.append(note("<b>Note on 'ration' and the inductance values.</b> The print "
                  "has 'the L/R ration of the cable can also be obtained' — "
                  "'ration', not 'ratio' — and the wording is kept verbatim in "
                  "English. The OCR text layer reads '1 μH/m and 0.1 Ω/m (10 "
                  "μH/Ω)' as '1 pH/m and O.lQ/m (lOpH/Q)'; the page render shows "
                  "the correct values."))
    b.append(p("The position with inductance is somewhat better than "
               "capacitance as the stored energy in inductance is related to "
               "current and not voltage. Placing conductors in parallel has "
               "the effect of dividing the current (see Fig. 13.45) and where "
               "each inductor is separate, halving the stored energy. This "
               "reduction is not practically likely but it shows that the "
               "effect of core/core or core/screen interconnection in cables is "
               "to reduce stored energy and not increase it."))

    # Printed p.425. No running prose: Figures 13.44 and 13.45 in printed order.
    b.append(fig(44, FF.fig_f1344()))
    b.append(note("<b>Note on the derivation in Fig. 13.44.</b> The print reads "
                  "'Capacitance between cores at worst' (not 'worst case'), then "
                  "'C_T = C_1 + C_2 × C_3/C_2 + C_3', 'If C_2 = C_3' and 'C_T = "
                  "C_1 + 1/2C_2'; the unusual algebra is kept verbatim. The OCR "
                  "text layer reads the last line as 'CT = c1 + 1/2c2'."))
    b.append(fig(45, FF.fig_f1345()))
    b.append(note("<b>Note on the derivation in Fig. 13.45.</b> The first line "
                  "reads 'Stored energy = 0.5 L i²'; the split-loop lines read "
                  "'= 0.5 L × (0.5 i)²', '= 0.125L i²', '= 2 × 0.125 L i²' and "
                  "'= 0.25 L i²' with their own spacing, which is preserved. "
                  "The OCR text layer reads '0.5 L i²' as '0.5 Liz'. The note "
                  "in the figure states that the calculation does not take "
                  "account of mutual coupling between the two loops but does "
                  "indicate the effects of current division."))

    # Printed p.426. Closing L/R paragraph only; the shell owns References.
    b.append(note("<b>Note on the reference list supplied by the shell.</b> "
                  "Printed quirks in the bibliography are: item 4 'BS 5501.' "
                  "and item 8 'IEC 79–11.' carry trailing full stops in the "
                  "left column; item 2 has lower-case 'service'; item 6 "
                  "'Physicalisch'; item 9 'Comite' without accents; item 10 "
                  "'Electrical apparatus' with lower-case 'apparatus'; item 16 "
                  "'Under moist Conditions'. The OCR text layer reads item 4 "
                  "as 'Intrinsic Safety, 3’.' and item 10 as printed. The "
                  "chapter shell keeps these forms."))
    b.append(p("L/R is not usually a problem as the vast majority of "
               "intrinsically safe circuits are designed to have permissible "
               "L/R figures of above 25 μH/Ω, which is much greater than the "
               "typical instrumentation cable."))
    return "".join(b)
