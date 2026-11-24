# -*- coding: utf-8 -*-
"""Book 7, Chapter 18 - The ABC Method for Gases (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
115-120 (PDF pp. 117-122). Six printed pages, one vector figure, one gas-constant
table, six numbered equations, two references and four additional-reading
items. The OCR text layer garbles every equation; the printed forms were read
from pypdfium2 renders of the six source pages.
"""
from cvp_common import eq, fig, h2, h3, note, ol, p, refs, table, ul
import cvpfig18 as F

PAGES_SRC = 6
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "The ABC Method for Gases"
TITLE_VI = "Phương pháp ABC cho chất khí"


def note_terms(lang):
    """A one-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 18.</b> phương pháp ABC (ABC method) · tiếng ồn "
                "khí động học (aerodynamic noise) · ISA-75.17 · IEC 60534-8-3 · mức áp "
                "suất âm thanh (sound pressure level) · dBA · logarit thập phân · hệ số "
                "lưu lượng Cv · đường kính ngoài ống D · áp suất đầu vào tuyệt đối P₁ · "
                "áp suất đầu ra tuyệt đối P₂ · tỷ số áp suất X = (P1 − P2)/P1 · hệ số "
                "đường kính tia khí Fd · hằng số khí G · hệ số FL · ΔFL · hệ số "
                "trở kháng công suất âm rw · bộ lót giảm ồn (sound-reducing trim) · "
                "lỗ / khe tiết lưu · đường kính thủy lực dh · đường kính lỗ tròn tương "
                "đương do · tỷ số diện tích AR · dịch vụ nhiều cấp (multistage) · "
                "nhiều bước / nhiều đường dẫn · số Reynolds · van một cổng (single-ported "
                "valve) · van bi phân đoạn (segmented ball valve)")
    return ("<b>Key terms.</b> ABC method · aerodynamic noise · ISA-75.17 · "
            "IEC 60534-8-3 · sound pressure level · dBA · base-10 logarithm · flow "
            "coefficient Cv · outside pipe diameter D · absolute inlet pressure P₁ · "
            "absolute outlet pressure P₂ · pressure ratio X = (P1 − P2)/P1 · gas jet "
            "diameter factor Fd · gas constant G · FL · ΔFL · sound power resistance "
            "factor rw · sound-reducing trim · drilled holes / rectangular passages · "
            "hydraulic diameter dh · equivalent circular orifice do · area ratio AR · "
            "multistage trim · multistep and multipath trims · Reynolds number · "
            "single-ported valve · segmented ball valve")


def body_vi():
    b = []
    b.append(h2("Phần 1: Ước tính mức ồn cho van có bộ lót tiêu chuẩn",
                "Part 1: Sound Level Estimate for Valves Having a Standard Trim"))

    b.append(p("Khác với tiêu chuẩn IEC 834-8-3 do nhà cung cấp chi phối và mang tính "
               "thực nghiệm, phương pháp ABC và tiêu chuẩn ISA 75.17 thân thiện với "
               "người dùng [1] đều mở và chỉ dựa trên các định luật khoa học. Thêm vào "
               "đó, hai phương pháp này dễ lập trình [2]."))
    b.append(p("Chương này gồm hai phần. Phần 1 có ba mục A, B và C. Khi cộng các phần "
               "lại với nhau, rồi cộng thêm một số hệ số hiệu chỉnh được thảo luận ở "
               "dưới đây, ta có thể xác định mức ồn khí động học của một van điều khiển "
               "có ống ra schedule 40 và cổng ra thẳng. Xem Phụ lục C «Phương pháp ABC "
               "hoạt động như thế nào?» để hiểu các thuật toán của phương pháp này."))
    b.append(p("Lưu ý rằng tôi không quy định một kiểu van cụ thể nào. Trên thực tế, "
               "phương pháp này áp dụng cho mọi kiểu van tác động qua lại hoặc quay "
               "hiện có, thậm chí cả các thiết kế chưa được phát minh, miễn là van có "
               "ống ra schedule 40 và cổng ra thẳng. Các hệ số hiệu chỉnh được cung "
               "cấp để điều chỉnh phép tính khi ống dày hơn schedule 40 và khi dùng "
               "chất lưu khác không khí."))
    b.append(note("<b>Tuyên bố miễn trừ.</b> Phương pháp đề xuất chỉ hợp lệ với van "
                  "điều khiển một cổng, chẳng hạn van cầu hoặc van có đường chảy thẳng, "
                  "và với chất lưu rối (Rev > 10.000)."))

    b.append(h3("Mục A", "Section A"))
    b.append(eq("A = 25 log(D) − 10 + 20 log(Cᵥ/D²)  dBA", num="18-1"))
    b.append(p("Trong đó Cᵥ là hệ số lưu lượng của van trong điều kiện dòng chảy và thử "
               "nghiệm thực tế; D là đường kính ngoài của ống tại cửa ra của van, tính "
               "bằng inch."))

    b.append(h3("Mục B", "Section B"))
    b.append(p("Với mục B, ta đơn giản có:"))
    b.append(eq("B = 35 log(P₁) − 35  dBA", num="18-2"))

    b.append(h3("Mục C", "Section C"))
    b.append(eq("C = 27 + 30 + 30 log(X) + 20 log(F_d)  dBA", num="18-3"))
    b.append(p("Như đã giải thích trước đây, F_d là hệ số về bản chất xác định đường "
               "kính của tia khí. Hãy nhớ rằng tia càng nhỏ thì tần số fp và tổn hao "
               "truyền âm càng cao. Đó là lý do ta trừ F_d. Lưu ý, 20 log(F_d) là âm "
               "vì mọi giá trị F_d đều nhỏ hơn 1 (xem Bảng 5-4 để biết giá trị F_d "
               "điển hình)."))
    b.append(eq("A + B + C + G", num="18-4"))
    b.append(p("Lưu ý: G được tra trong Bảng 18-1."))

    b.append(table(
        ["Khí", "G"],
        [["Không khí", "0"],
         ["Hơi bão hòa", "−3"],
         ["Hơi quá nhiệt", "−3"],
         ["Heli", "−4"],
         ["Oxy", "0,34"],
         ["Nitơ", "−0,3"],
         ["Mêtan", "−1,2"],
         ["Khí tự nhiên", "−2,9"],
         ["Argon", "0,67"]],
        "Bảng 18-1. Hằng số khí vật lý."))
    b.append(p("Trong đó G là hệ số hiệu chỉnh cho các loại khí khác không khí."))

    b.append(h2("Cộng các thành phần và các hệ số hiệu chỉnh",
                "Adding the parts and modifiers"))
    b.append(p("Việc còn lại là cộng tất cả kết quả A + B + C rồi cộng hai hệ số "
               "hiệu chỉnh: ΔF_L và hệ số trở kháng công suất âm r_w. Khi đó ta có "
               "mức áp suất âm thanh ở khoảng cách 1 m, tính bằng dBA, cho thành ống "
               "schedule 40. Lưu ý: G là hệ số hiệu chỉnh cho các loại khí khác không "
               "khí (xem bên dưới); với không khí thì G = 0. Ta có:"))
    b.append(eq("A + B + C + ΔF_L − r_w + G + các hệ số hiệu chỉnh khác", num="18-5"))
    b.append(p("Hệ số hiệu chỉnh thứ nhất là ΔF_L, xét đến trường hợp F_L thực tế "
               "khác với giá trị giả định 0,7 (F_L trung bình). Để hiệu chỉnh ΔF_L, dùng:"))
    b.append(eq("ΔF_L = 30 log(F_L thực tế / 0,7)", num="18-6"))
    b.append(p("r_w = 3 dB chỉ đối với van cầu; đây là hệ số trở kháng xét đến đường "
               "dẫn chảy ngoằn ngoèo trong thân van cầu."))

    b.append(h3("Ví dụ", "Example"))
    b.append(p("Một van bi phân đoạn 8 inch, Cv = 134, F_L = 0,6, F_d = 0,40, "
               "P₁ = 37,5 psia, P₂ = 14,5 psia. Ống ra có D = 16 in. Khi đó X = 0,6 "
               "và Cv/D² = 2,1."))
    b.append(p("Theo các phương trình trên: A = 17,5; B = 20; C = 48,7 và "
               "ΔF_L = −2. Tổng = 17,5 + 20 + 48,7 − 2 = 84,7 dBA. Kết quả này phù hợp "
               "với số liệu thử nghiệm 85 dBA trong Hình 18-1 tại 10X = 0,6."))
    b.append(fig(1, F.fig_f181()))

    b.append(p("Các hệ số hiệu chỉnh khác: với khí khác không khí, cộng thêm vào "
               "tiểu mục PLa: ps = 20 log(Ci khí/1126) + 15 log(M khí dùng/28,97), "
               "trong đó Ci là tốc độ âm của khí đang dùng, tính bằng ft/giây."))
    b.append(p("Về độ dày ống: schedule 40 = 0; schedule 80 = −4 dB; "
               "schedule 160 = −8 dB."))

    b.append(h2("Phần 2: Phương pháp ước tính mức ồn cho bộ lót giảm ồn",
                "Part 2: Method for Estimating Sound Levels for Sound-Reducing Valve Trims"))

    b.append(h3("2.1 Bộ lót một cấp, nhiều lưu thông",
                "2.1 Single-Stage, Multipassage Trim"))
    b.append(p("Ví dụ: các lỗ khoan trên nút van hoặc lồng van."))
    b.append(p("Phương pháp: dùng các phương trình ở Phần 1 với giá trị F_d sau: "
               "với các lỗ kích thước bằng nhau, F_d = 1/(n_o^0,5), trong đó n_o là "
               "số lưu thông kích thước bằng nhau tiếp xúc với dòng chảy trong điều "
               "kiện thực tế."))
    b.append(p("Lưu ý: phương pháp này chỉ hợp lệ nếu khoảng cách giữa các lỗ không "
               "nhỏ hơn một đường kính lỗ."))
    b.append(p("Với các lưu thông chữ nhật, dùng F_d = (d_h/d_o) × (1/n_o^0,5), "
               "với d_h = 4 a_p / 2 l_p và d_o = (a_p × 4 / 3,14)^0,5 n_os^0,5."))
    b.append(p("Trong đó d_o là lỗ tròn tương đương; d_h là đường kính thủy lực của "
               "một khe; l_p là chiều dài của một khe; n_os là số khe chữ nhật; a_p "
               "là diện tích dòng chảy của một lưu thông. Mọi kích thước đều tính "
               "bằng inch."))

    b.append(h3("2.2 Bộ lót van nhiều cấp, một lưu thông",
                "2.2 Multistage, Single-Passage Valve Trim"))
    b.append(p("Ví dụ: nút van dạng nón có các gờ tròn cách đều, cắt ngang các rãnh "
               "lõm tương ứng trong chi tiết ghép cặp."))
    b.append(p("Phương pháp: dùng kết quả từ Phương trình 18-1 ở Phần 1 rồi trừ "
               "ΔAR, với ΔAR = 10 log(AR). AR là tỷ số giữa diện tích dòng chảy của "
               "lưu thông ra và lưu thông vào."))
    b.append(p("Ví dụ: một van cầu có một đường chảy với bộ lót nhiều cấp, Cv = 10 "
               "và đường kính ống 2 in, giảm áp từ 200 psia xuống 14,5 psia. Bộ lót có "
               "8 cấp, tỷ số diện tích 7, F_L = 0,8 và F_d = 0,9. Khi đó X = 0,93."))
    b.append(p("Dùng các phương trình ở Phần 1, kết quả là 104,9 dBA − 10 log(7) "
               "= 96,4 dBA."))

    b.append(h3("2.3 Bộ lót nhiều bước và nhiều đường dẫn",
                "2.3 Multistep and Multipath Trims"))
    b.append(p("Phương pháp: làm theo quy trình ở Mục 2.2 rồi trừ thêm "
               "20 log(n_op^0,5), trong đó n_op là số đường dẫn nhiều bước có kích "
               "thước bằng nhau trong điều kiện dòng chảy đã cho."))
    b.append(p("Ví dụ: dùng ví dụ ở Mục 2.2 và giả sử bộ lót có 12 đường dẫn bằng "
               "nhau (n_op), kết quả là 96,4 dBA − 20 log(12^0,5) = 85,6 dBA."))
    b.append(p("Để giải thích cách một phương pháp đơn giản như vậy hoạt động, "
               "xem Phụ lục C. Nếu điều đó vẫn còn quá phức tạp, hãy xem Chương 19, "
               "«Phương pháp ABC dạng đồ thị cho chất khí»."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "ISA-75.17-1989, Control Valve Aerodynamic Noise Prediction (Research Triangle "
        "Park, NC: ISA [International Society for Automation]).",
        "J. Monsen, “SimpleExcel Based Predicts Control Valve Aerodynamic Noise,” "
        "Valve World Magazine (October 2022).",
    ]))
    b.append(h3("Đọc thêm", "Additional Reading"))
    b.append(ul([
        "H. D. Baumann, “Control Valve Noise Estimating Method Made Easy,” InTech 65, "
        "no 4. (July/August 2018): 42–43.",
        "IEC 60534-8-4: 2015 Ed 3.0, Industrial-Process Control Valves – Part 8-4: "
        "Noise Considerations – Prediction of Noise Generated by Hydrodynamic Flow "
        "(Geneva 20 – Switzerland: IEC [International Electrotechnical Commission]).",
        "H. D. Baumann, “A Simple Aerodynamic Sound Estimating Method—Why Not?” "
        "Valve World magazine, no. 10 (November 2018): 111–117.",
        "IEC 60534-8-3: 2010 Ed 3.0, Industrial-Process Control Valves – Part 8-3: "
        "Noise Considerations – Control Valve Aerodynamic Noise Prediction Method "
        "(Geneva 20 – Switzerland: IEC [International Electrotechnical Commission]).",
    ]))

    b.append(note("<b>Ghi chú về nguồn.</b> (1) Lớp văn bản OCR xáo trộn toàn bộ "
                  "phương trình; các dạng in trên trang 116–119 đã được đọc lại từ "
                  "ảnh trang nguồn, kể cả hệ số 25 log(D) − 10 của (18-1), 35 log(P₁) "
                  "− 35 của (18-2), 27 + 30 + 30 log(X) + 20 log(F_d) của (18-3), "
                  "và 30 log(F_L thực tế/0,7) của (18-6). (2) Nguyên bản ghi "
                  "«IEC standard 834-8-3» và «in psia» ở chương trước; bản Anh giữ "
                  "cách viết đó, bản Việt dùng thuật ngữ chuẩn. (3) Hình 18-1 là ảnh "
                  "trong PDF; bản dịch vẽ lại dạng vector với các điểm số liệu đọc "
                  "từ trục in. (4) Chương này có một bảng, một hình và sáu phương "
                  "trình đánh số (18-1)–(18-6)."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 18 chiếm các trang in 115–120 của ấn bản in (PDF tr. 117–122). "
               "Nguyên bản gồm phần mở đầu về hai tiêu chuẩn mở ISA-75.17 và ABC, "
               "tuyên bố miễn trừ, ba mục A–B–C với bảng hằng số khí, phần cộng các "
               "hệ số hiệu chỉnh và ví dụ van bi 8 inch, ba dạng bộ lót giảm ồn ở "
               "Phần 2, Hình 18-1, hai tài liệu tham khảo và ba mục đọc thêm — tất "
               "cả đều được giữ lại."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Part 1: Sound Level Estimate for Valves Having a Standard Trim",
                "Part 1: Sound Level Estimate for Valves Having a Standard Trim"))

    b.append(p("In contrast to vendor-dominated, empirical IEC standard 834-8-3, "
               "the ABC method and user-friendly ISA standard 75.17 [1] are open "
               "and based only on scientific laws. In addition, they are easily "
               "programmable [2]."))
    b.append(p("This chapter consists of two parts. Part 1 has three sections: A, B, "
               "and C. When the parts are combined, and after adding a few discussed "
               "modifiers, one can determine an aerodynamic sound level for a control "
               "valve with a schedule 40 outlet pipe and a straight valve outlet "
               "port. Please consult Appendix C, “How Does the ABC Method Work?” to "
               "understand the algorithms used in this method."))
    b.append(p("Note that I did not specify a particular valve type. As a matter of "
               "fact, this method accommodates all available reciprocating or rotary "
               "valve types, or even designs not invented yet, as long as the valve "
               "has a schedule 40 outlet pipe and a straight valve outlet port. "
               "Modifiers are provided for adjusting the calculations when the pipes "
               "are thicker than schedule 40 and fluids other than air are used."))
    b.append(note("<b>Disclaimer.</b> The proposed method is valid only for "
                  "single-ported control valves, such as globe or line-of-sight "
                  "valves, and for turbulent fluids (Rev > 10,000)."))

    b.append(h3("Section A", "Section A"))
    b.append(eq("A = 25 log(D) − 10 + 20 log(Cᵥ/D²)  dBA", num="18-1"))
    b.append(p("where Cᵥ = flow coefficient of the valve under actual flow and test "
               "conditions; D = outside diameter of the pipe at the valve’s outlet "
               "(inches)."))

    b.append(h3("Section B", "Section B"))
    b.append(p("In the B section, we simply have:"))
    b.append(eq("B = 35 log(P₁) − 35  dBA", num="18-2"))

    b.append(h3("Section C", "Section C"))
    b.append(eq("C = 27 + 30 + 30 log(X) + 20 log(F_d)  dBA", num="18-3"))
    b.append(p("As I explained previously, F_d is a factor that essentially "
               "determines the diameter of a gas jet. Remember, the smaller the jet, "
               "the higher the fp and the transmission loss. This is why we have to "
               "subtract F_d. Note, 20 log(F_d) is negative because all F_d numbers "
               "are below 1 (for typical Fd values, see Table 5-4)."))
    b.append(eq("A + B + C + G", num="18-4"))
    b.append(p("Note: G is tabulated in Table 18-1."))

    b.append(table(
        ["Gas", "G"],
        [["Air", "0"],
         ["Sat. Steam", "−3"],
         ["Super Heated Steam", "−3"],
         ["Helium", "−4"],
         ["Oxygen", "0.34"],
         ["Nitrogen", "−0.3"],
         ["Methane", "−1.2"],
         ["Natural Gas", "−2.9"],
         ["Argon", "0.67"]],
        "Table 18-1. Physical gas constants."))
    b.append(p("where G = a correction actor for gases other than air."))

    b.append(h2("Adding the Parts and Modifiers", "Adding the Parts and Modifiers"))
    b.append(p("All we have to do now is add all the results of A + B + C and then "
               "add two modifiers: ΔF_L and the sound power resistance factor (r_w). "
               "Now we have the 1m distance sound pressure level in dBA for a "
               "schedule 40 pipe wall. Note: G is a modifier to account for gases "
               "other than air (see below). G for air = 0. This gives:"))
    b.append(eq("A + B + C + ΔF_L − r_w + G plus other modifiers", num="18-5"))
    b.append(p("The first modifier is ΔF_L, which accounts for the case where the "
               "actual F_L differs from an assumed 0.7 (average F_L). To correct "
               "for ΔF_L, use:"))
    b.append(eq("ΔF_L = 30 log(actual F_L / 0.7)", num="18-6"))
    b.append(p("Rw = 3 dB for globe valves only. A resistance factor accounting for "
               "the torturous flow path in a globe valve housing."))

    b.append(h3("Example", "Example"))
    b.append(p("An 8-inch segmented ball valve, Cv = 134, F_L = 0.6, F_d = 0.40, "
               "P₁ = 37.5 psia, P₂ = 14.5 psia. The outlet pipe (D) = 16 in. "
               "This makes X = 0.6 and Cv/D² = 2.1."))
    b.append(p("From the above equations, A = 17.5, B = 20, C = 48.7, and "
               "ΔF_L = −2. The total = 17.5 + 20 + 48.7 − 2 = 84.7 dBA. This "
               "agrees with the test data of 85 dBA in Figure 18-1 for 10X = .6."))
    b.append(fig(1, F.fig_f181()))

    b.append(p("Other Modifiers: For gases other than air, add the following: "
               "ps = 20 log(Ci gas/1126) + 15 log(M gas use/28.97) from the PLa "
               "subtotal, where Ci is the sonic speed of the gas used, in ft/sec."))
    b.append(p("For pipe thickness: Schedule 40 = 0, Schedule 80 = −4, dB "
               "Schedule 160 = −8 dB."))

    b.append(h2("Part 2: Method for Estimating Sound Levels for Sound-Reducing "
                "Valve Trims",
                "Part 2: Method for Estimating Sound Levels for Sound-Reducing "
                "Valve Trims"))

    b.append(h3("2.1 Single-Stage, Multipassage Trim",
                "2.1 Single-Stage, Multipassage Trim"))
    b.append(p("Example: Drilled holes in valve plugs or cages."))
    b.append(p("Method: Use the equations from Part 1 with the following values "
               "for F_d: F_d for equally sized holes = 1/(n_o^0.5), where n_o is "
               "the number of equally sized passages exposed under actual flow "
               "conditions."))
    b.append(p("Note: This method is only valid if the distance between holes is "
               "no less than one hole diameter."))
    b.append(p("For rectangular passages, utilize F_d = (d_h / d_o) × (1 / n_o^0.5), "
               "where d_h = 4 a_p / 2 l_p, and d_o = (a_p × 4 / 3.14)^0.5 n_os^0.5."))
    b.append(p("where d_o = the equivalent circular orifice; d_h = the hydraulic "
               "diameter of one slot; l_p = the length of a slot; n_os = number of "
               "rectangular slots; a_p = the flow area if a single passage. Note: "
               "All dimensions are in inches."))

    b.append(h3("2.2 Multistage, Single-Passage Valve Trim",
                "2.2 Multistage, Single-Passage Valve Trim"))
    b.append(p("Example: Cone-shaped plugs having equally spaced circular rims "
               "intersecting with similar concave recessions in mating elements."))
    b.append(p("Method: Use the results from Part 1 Equation 18-1 and subtract "
               "ΔAR, where ΔAR = 10 log(AR). AR is the ratio between the flow area "
               "of the exit flow passage and the flow passage at the entrance."))
    b.append(p("Example: A globe valve having a single flow page with multistage "
               "trim has a Cv of 10 and a pipe diameter of 2 in, reducing 200 psia "
               "to 14.5 psia. The trim has 8 stages, an area ratio of 7, an F_L of "
               "0.8, and an F_d of 0.9. X = 0.93."))
    b.append(p("Using the equations from Part 1, the result is 104.9 dBA − "
               "10 log(7) = 96.4 dBA."))

    b.append(h3("2.3 Multistep and Multipath Trims",
                "2.3 Multistep and Multipath Trims"))
    b.append(p("Method: Use the procedure from Part 2.2 and subtract "
               "20 log(n_op^0.5), where n_op = the number of equally sized "
               "multistep flow paths for given flow conditions."))
    b.append(p("Example: Using the example from Part 2.2 and assuming the trim "
               "has 12 equally sized paths (n_op), the result is 96.4 dBA (from "
               "above) −20 log(12^0.5) = 85.6 dBA."))
    b.append(p("For an explanation of how such a simple method works, see "
               "Appendix C. If this is still too complicated, consult Chapter 19, "
               "“The Graphical ABC Method for Gases.”"))

    b.append(h2("References", "References"))
    b.append(refs([
        "ISA-75.17-1989, Control Valve Aerodynamic Noise Prediction (Research Triangle "
        "Park, NC: ISA [International Society for Automation]).",
        "J. Monsen, “SimpleExcel Based Predicts Control Valve Aerodynamic Noise,” "
        "Valve World Magazine (October 2022).",
    ]))
    b.append(h3("Additional Reading", "Additional Reading"))
    b.append(ul([
        "H. D. Baumann, “Control Valve Noise Estimating Method Made Easy,” InTech "
        "65, no 4. (July/August 2018): 42–43.",
        "IEC 60534-8-4: 2015 Ed 3.0, Industrial-Process Control Valves – Part 8-4: "
        "Noise Considerations – Prediction of Noise Generated by Hydrodynamic Flow "
        "(Geneva 20 – Switzerland: IEC [International Electrotechnical Commission]).",
        "H. D. Baumann, “A Simple Aerodynamic Sound Estimating Method—Why Not?” "
        "Valve World magazine, no. 10 (November 2018): 111–117.",
        "IEC 60534-8-3: 2010 Ed 3.0, Industrial-Process Control Valves – Part 8-3: "
        "Noise Considerations – Control Valve Aerodynamic Noise Prediction Method "
        "(Geneva 20 – Switzerland: IEC [International Electrotechnical Commission]).",
    ]))

    b.append(note("<b>Source note.</b> (1) The OCR text layer garbles every "
                  "equation; the printed forms on pp. 116–119 were read from page "
                  "renders, including the 25 log(D) − 10 coefficient in (18-1), "
                  "35 log(P₁) − 35 in (18-2), 27 + 30 + 30 log(X) + 20 log(F_d) in "
                  "(18-3), and 30 log(actual F_L/0.7) in (18-6). (2) The source "
                  "quirk «IEC standard 834-8-3» is retained here; the Vietnamese "
                  "uses the intended standard name. (3) Figure 18-1 is an image in "
                  "the PDF; it is redrawn as a vector with data points read from "
                  "the printed axes. (4) The chapter contains one table, one figure "
                  "and six numbered equations (18-1)–(18-6)."))
    b.append(h3("About the source", "About the source"))
    b.append(p("Chapter 18 occupies printed pp. 115–120 of the book (PDF pp. "
               "117–122). The source consists of the introduction to the two open "
               "standards ISA-75.17 and ABC, the disclaimer, sections A–B–C with "
               "the gas-constant table, the modifier section and the 8-inch ball "
               "valve example, the three sound-reducing trim types in Part 2, "
               "Figure 18-1, two references and four additional-reading items, "
               "all of which are retained."))
    return "".join(b)
