# -*- coding: utf-8 -*-
"""Book 7, Chapter 6 - High-Recovery Valves (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
47-50 (PDF pp. 54-57). Two source figures, one table in two parts, and one
unnumbered acoustic equation.
"""
from cvp_common import eq, fig, h2, h3, note, ol, p, table, ul
import cvpfig6 as F

PAGES_SRC = 4
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "High-Recovery Valves"
TITLE_VI = "Van phục hồi áp suất cao"


def note_terms(lang):
    """A one-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 6.</b> van phục hồi áp suất cao (high-recovery valve) · "
                "van điều khiển thông thường (conventional control valve) · tua-bin khí đốt · "
                "năng lượng thế / năng lượng động (potential / kinetic energy) · dòng chảy bị "
                "nghẽn (choked flow) · điều biến áp suất thượng lưu · hệ số phục hồi áp suất "
                "chất lỏng F<sub>L</sub> · tiết lưu / lỗ tiết lưu (throttling orifice) · "
                "đế van / bệ van / mặt tựa của van (seat) · nén lại đẳng entropy (isentropic "
                "recompression) · đường biên dạng venturi · van bi phân đoạn (segmented ball "
                "valve) · van góc tạo dòng suôn sẻ (streamlined angle valve) · tổn thất cột áp "
                "đầu vào · van cắm quay lệch (eccentric rotary plug valve) · cột áp bơm · "
                "xâm thực (cavitation) · hóa hơi (flashing) · số xâm thực ban đầu fxz · "
                "tiếng ồn nhiễu loạn · âm xâm thực · tỷ lệ áp suất tới hạn Xy.")
    return ("<b>Key terms.</b> high-recovery valve · conventional control valve · fuel-gas "
            "turbine · potential / kinetic energy · choked flow · inlet-pressure modulation · "
            "liquid pressure recovery factor F<sub>L</sub> · throttling / throttling orifice · "
            "seat · isentropic recompression · venturi contour · segmented ball valve · "
            "streamlined angle valve · inlet head loss · eccentric rotary plug valve · pump "
            "head · cavitation · flashing · incipient cavitation number fxz · turbulent noise · "
            "cavitation sound · critical pressure ratio Xy.")


def body_vi():
    b = []
    b.append(h2("Từ năng lượng thế sang điều khiển bằng áp suất thượng lưu",
                "From potential energy to inlet-pressure control"))
    b.append(p("Van phục hồi áp suất cao được dùng để thay thế các van điều khiển thông thường "
               "trong điều khiển quá trình ở nhiều ngành công nghiệp. Ứng dụng chủ yếu là điều "
               "khiển khí đốt tiếp nhiên liệu cho tua-bin máy phát điện, nơi độ giảm áp làm suy "
               "giảm hiệu suất của tua-bin. Mọi van thông thường đều hoạt động theo nguyên lý "
               "chuyển năng lượng thế (áp suất thượng lưu) thành năng lượng động (vận tốc chất "
               "lưu), rồi tùy theo áp suất hạ lưu mong muốn lại chuyển năng lượng động thành sự "
               "nhiễu loạn có cường độ tương ứng với chênh áp qua van. Cách này tuy có hiệu quả "
               "nhưng khá kém hiệu suất, vì làm suy giảm năng lượng thế sẵn có ở hạ lưu van. "
               "Ngược lại, van phục hồi áp suất cao hoạt động như sau: khi dòng chảy đã bị "
               "nghẽn do hạ áp suất hạ lưu xuống dưới 10% áp suất đầu vào, chỉ cần điều biến "
               "áp suất thượng lưu là đã đạt được điều khiển lưu lượng hiệu quả. Điều này cũng "
               "đơn giản hóa thuật toán điều khiển."))
    b.append(p("Các thử nghiệm trên một van tương tự như Hình 6-1 cho thấy có thể đạt dòng nghẽn "
               "chỉ với độ giảm áp 9 psi ở áp suất đầu vào 100 psia và 10% hành trình, và chỉ "
               "giảm 10% so với 100 psia ở 100% hành trình. Trong khi đó, van cầu tiêu chuẩn mở "
               "hoàn toàn với F<sub>L</sub> bằng 0,85 cần tới 36% độ giảm áp so với 100 psia để "
               "đạt được khả năng điều khiển dòng chảy tương tự."))

    b.append(h2("Đường biên dạng venturi và nén lại đẳng entropy",
                "Venturi contours and isentropic recompression"))
    b.append(p("Các kiểu van mới hơn (xem Hình 6-1) giảm tổn thất năng lượng này bằng cách dùng "
               "đường biên dạng dạng venturi ở hạ lưu lỗ tiết lưu. Khi áp suất đầu ra được giảm "
               "đủ, vận tốc trong lỗ tiết lưu đạt tới vận tốc âm thanh đối với chất lưu khí. Khí "
               "sau đó giãn nở dần trong đoạn venturi cho đến khi đạt áp suất hạ lưu mong muốn, "
               "nhờ đó tránh được phần lớn năng lượng bị tiêu hao do nhiễu loạn; quá trình này "
               "được gọi là nén lại đẳng entropy (isentropic recompression). Lượng nhiễu loạn "
               "tránh được tùy thuộc vào mức độ suôn sẻ của đường dòng từ cổng vào tới cửa ra của "
               "van. Điều này đòi hỏi diện tích lưu lượng của mặt cắt ngang giảm đều về phía vùng "
               "tiết lưu tại đế van rồi tăng dần về sau, nhằm tránh những thay đổi đột ngột về "
               "vận tốc."))
    b.append(p("Các kiểu van hiện được dùng cho việc này gồm van bi phân đoạn (segmented ball "
               "valve) và van góc được tạo dòng suôn sẻ (streamlined angle valve). Dù van bi hoạt "
               "động tốt ở lưu lượng cao với số F<sub>L</sub> khoảng 0,4, chúng kém hiệu quả ở "
               "lưu lượng thấp vì số F<sub>L</sub> cao hơn ở hành trình nhỏ. Van góc bị tổn thất "
               "cột áp do cổng vào cong. Tác giả tỏ ra ngạc nhiên khi khái niệm này ít được dùng "
               "cho các ứng dụng công nghiệp khác; theo tác giả, có thể dùng những van này để "
               "nạp khí hoặc hơi vào bình chứa, trong đó tốc độ nạp được điều biến bằng cách thay "
               "đổi áp suất đầu vào của van. Câu hỏi đặt ra là: vì van phục hồi áp suất cao làm "
               "việc tốt với chất lưu khí, tại sao không dùng chúng cho cả chất lỏng?"))

    b.append(h2("Thử nghiệm với nước tại Đại học Bang Utah",
                "Water tests at Utah State University"))
    b.append(p("Quả vậy, chúng có thể mang lại lợi ích tương đương. Các thử nghiệm dòng chảy tại "
               "Phòng thí nghiệm Nghiên cứu Nước, Đại học Bang Utah cho thấy van phục hồi áp suất "
               "cao có hệ số phục hồi áp suất chất lỏng F<sub>L</sub> thấp tới 0,4 và, tốt hơn "
               "nữa, số liệu thấp này duy trì suốt mọi dải hành trình. Điều đó có nghĩa là các van "
               "này bị nghẽn dòng ở độ giảm áp chỉ 19 psi trên 100 psia. Chúng rất phù hợp cho "
               "các ứng dụng yêu cầu lưu lượng không đổi hoặc áp suất hạ lưu không đổi, như liệt "
               "kê trong Bảng 6-1A và Bảng 6-1B."))
    b.append(fig(1, F.fig_f61()))

    b.append(h2("So sánh với van cắm quay lệch",
                "Comparison with eccentric rotary plug valves"))
    b.append(p("Các bảng này cho thấy lợi ích đáng kể của van phục hồi áp suất cao so với van "
               "điều khiển thông thường như van cắm quay lệch (eccentric rotary plug). Lợi ích rõ "
               "rệt của điều khiển lưu lượng không đổi là có thể thay đổi hành trình của van phục "
               "hồi để đổi áp suất hạ lưu mà vẫn giữ áp suất thượng lưu không đổi, tức là giữ cột "
               "áp bơm không đổi. Ngược lại, van cắm lệch bị nghẽn cần thay đổi áp suất thượng "
               "lưu để duy trì lưu lượng không đổi khi áp suất đầu ra thay đổi."))
    b.append(p("Bảng 6-1B cho thấy sự khác biệt tương tự khi duy trì áp suất hạ lưu không đổi "
               "(một ứng dụng giảm áp điển hình) trong khi lưu lượng thay đổi. Ở đây cũng vậy, áp "
               "suất thượng lưu của van thông thường phải được thay đổi khi ta đổi hành trình để "
               "đáp ứng lưu lượng thay đổi."))
    b.append(table(["FL", "Cv", "P1 (psia)", "P2 (psia)", "Q (GPM)", "Kiểu"],
                   [["0.44", "40", "100", "95", "90", "Hi-R"],
                    ["0.44", "20", "100", "80*", "90", "Hi-R"],
                    ["0.7", "40", "100", "88", "140", "Ecc.Pl"],
                    ["0.7", "20", "100", "51*", "140", "Ecc.Pl"]],
                   caption="Bảng 6.1A · Điều khiển lưu lượng không đổi"))
    b.append(table(["FL", "Cv", "P1 (psia)", "P2 (psia)", "Q (GPM)", "Kiểu"],
                   [["0.44", "40", "100", "80", "178", "Hi-R"],
                    ["0.44", "20", "100", "80", "89", "Hi-R"],
                    ["0.7", "40", "100", "51*", "280", "Ecc.Pl"],
                    ["0.7", "20", "100", "51*", "140", "Ecc.Pl"]],
                   caption="Bảng 6.1B · Điều khiển áp suất không đổi"))

    b.append(h2("Xâm thực và tiếng ồn", "Cavitation and noise"))
    b.append(p("Có thể tự hỏi van phục hồi áp suất cao có gây xâm thực quá mức với số xâm thực "
               "ban đầu fxz trung bình chỉ 0,15 hay không. Đáng ngạc nhiên là không, nhờ hai yếu "
               "tố. Thứ nhất, nhờ số F<sub>L</sub> thấp, xâm thực ban đầu phát sinh chỉ dừng ở "
               "mức khiêm tốn, cao hơn tiếng ồn nhiễu loạn từ 3 đến 5 dBA. Tiếng ồn xâm thực đáng "
               "kể hơn chỉ xuất hiện khi độ giảm áp vượt quá khoảng 30% P1, dù vẫn chưa tới mức "
               "gây hư hỏng. Cần nhớ rằng không cần độ giảm áp lớn để điều khiển lưu lượng khi tỷ "
               "lệ áp suất bằng F<sub>L</sub><sup>2</sup> (xem Chương 15). Ở đây, mức nhiễu loạn "
               "cực đại đó chỉ là:"))
    b.append(eq("30 log(10 × FL² / fxz) = 3.3 dB", ""))
    b.append(p("Thứ hai, Xy - điểm xâm thực cực đại trong trường hợp này - là giá trị thấp 0,55. "
               "Ở tỷ lệ áp suất đó, hầu như không có âm nhiễu loạn làm nền để so sánh âm xâm "
               "thực."))
    b.append(p("Đồ thị Hình 6-2 cho thấy mức âm xâm thực cực đại đạt được tại X = 0,55, như đã "
               "dự đoán. Tuy vậy, mức ồn tổng thể vẫn thấp hơn khoảng 5 đến 8 dB so với van thông "
               "thường dùng về cơ bản cùng dữ liệu đầu vào, chỉ khác hệ số F<sub>L</sub> = 0,75."))
    b.append(fig(2, F.fig_f62()))

    b.append(h2("Tiết kiệm năng lượng", "Energy savings"))
    b.append(p("Cuối cùng, không kém quan trọng là khả năng tiết kiệm năng lượng của van phục hồi "
               "áp suất cao. Như Bảng 6-1B cho thấy, van tiêu chuẩn cần độ giảm áp từ 76 đến 120 "
               "psi, trong khi van phục hồi chỉ cần 20 psi. Điều này chuyển hóa trực tiếp thành "
               "tiết kiệm công suất bơm."))

    b.append(note("<b>Ghi chú về nguồn.</b> (1) Lớp văn bản OCR của bản in có nhiều dấu gạch nối "
                  "khi xuống dòng («pro-cess», «tur-bines», «thereaf-ter», «recompres-sion», "
                  "«stream-lined», «pres-sure»); bản dịch ghép lại thành từ hoàn chỉnh. "
                  "(2) Hình 6-1 là bản vẽ bằng sáng chế (US Patent 105 782 15); ở đây được vẽ lại "
                  "dạng sơ đồ vector đơn giản, không phải bản sao facsimile, và chỉ giữ lại một số "
                  "số hiệu gọi ra. (3) Trong Bảng 6-1, các giá trị P2 mang dấu hoa thị (80* và 51*) "
                  "được giữ nguyên như bản in; chương này không giải thích ý nghĩa của dấu hoa "
                  "thị. (4) Chú thích Hình 6-2 ghi đường đen là van thông thường và đường đỏ là van "
                  "phục hồi áp suất cao; bản vẽ lại giữ quy ước đó, nhưng dùng nét đứt cho đường "
                  "đỏ để dễ phân biệt. (5) Phương trình âm thanh trong nguồn bị lỗi OCR "
                  "(«30 log(10 × FL 2/fxz) = 3.3 dB»); ở đây trình bày lại với ký hiệu FL²."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 6 chiếm các trang in 47-50 của ấn bản in (PDF tr. 54-57). Nguyên bản có hai "
               "hình (6-1 và 6-2) và một bảng (6-1, gồm hai phần A và B); tất cả đều được giữ "
               "lại, trong đó hai hình được vẽ lại dạng vector."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("From potential energy to inlet-pressure control",
                "Từ năng lượng thế sang điều khiển bằng áp suất thượng lưu"))
    b.append(p("High-recovery valves are used to replace conventional control valves in process "
               "control across a range of industries. They are used primarily to control fuel gas "
               "to power-plant turbine generators, where pressure drop diminishes the efficiency "
               "of the turbines. All conventional valves operate on the principle of converting "
               "potential energy (upstream pressure) into kinetic energy (fluid velocity), then, "
               "depending on the desired downstream pressure, converting kinetic energy into "
               "turbulence whose magnitude corresponds to the pressure differential across the "
               "valve. Effective though this is, it is relatively inefficient because it reduces "
               "the available potential energy downstream of the valve. High-recovery valves, by "
               "contrast, operate as follows: once choked flow is reached by reducing downstream "
               "pressure below 10% of inlet pressure, effective flow control is achieved simply "
               "by modulating inlet pressure. This also simplifies the control algorithms."))
    b.append(p("Tests on a valve similar to the one in Figure 6-1 showed that choked flow could be "
               "achieved with only a 9 psi pressure drop at 100 psia inlet pressure at 10% travel, "
               "and only a 10% pressure drop out of 100 psia at 100% travel. That compares with a "
               "36% pressure drop out of 100 psia for a fully open standard globe valve with an F"
               "<sub>L</sub> of 0.85 in order to achieve such flow control."))

    b.append(h2("Venturi contours and isentropic recompression",
                "Đường biên dạng venturi và nén lại đẳng entropy"))
    b.append(p("Newer valve types (see Figure 6-1) try to reduce this energy loss by using "
               "venturi-type contours downstream of the valve's throttling orifice. When the "
               "outlet pressure is reduced sufficiently, the velocity within the throttling "
               "orifice reaches sonic velocity for gaseous fluids. The gas gradually expands "
               "within the venturi section until the desired downstream pressure is reached, thus "
               "avoiding most of the energy lost to turbulence. This process is called isentropic "
               "recompression. The amount of avoided turbulence depends on how streamlined the "
               "fluid path is from the inlet port to the outlet of the valve. This requires that "
               "the cross-sectional flow areas evenly decrease toward the throttling area at the "
               "seat and gradually expand thereafter, thus avoiding sudden velocity changes."))
    b.append(p("Valve types currently used for this service include segmented ball valves and "
               "streamlined angle valves. Although ball valves perform well at high flow rates "
               "with F<sub>L</sub> numbers of about 0.4, they lose efficiency at low flow rates "
               "because of higher F<sub>L</sub> numbers at low travel. Angle valves suffer from "
               "head losses due to the curved inlet port. The author is surprised that this "
               "concept is little used in other industrial applications; such valves could, in his "
               "view, be used to fill tanks with gas or steam, with the filling rate modulated by "
               "varying the inlet pressure to the valve. The question arises: because "
               "high-recovery valves work well for gases, why not employ them for liquids as "
               "well?"))

    b.append(h2("Water tests at Utah State University",
                "Thử nghiệm với nước tại Đại học Bang Utah"))
    b.append(p("Indeed, they can offer equal benefits. Flow tests conducted at the Utah State "
               "University Water Research Laboratory found that high-recovery valves have liquid "
               "pressure recovery factors F<sub>L</sub> as low as 0.4 and, even better, that such "
               "low numbers extend through all travel ranges. This means that such valves exhibit "
               "choked flow at pressure drops as low as 19 psi out of 100 psia. This makes them "
               "ideal for applications where either a constant flow or a constant downstream "
               "pressure is demanded, as listed in Tables 6-1A and B."))
    b.append(fig(1, F.fig_f61()))

    b.append(h2("Comparison with eccentric rotary plug valves",
                "So sánh với van cắm quay lệch"))
    b.append(p("These tables show significant benefits of using high-recovery valves compared with "
               "conventional control valves such as an eccentric rotary plug valve. The obvious "
               "benefit of constant flow control is that one can vary the travel of the "
               "high-recovery valve to change the downstream pressure while keeping the inlet "
               "pressure constant. This means a constant pump head. A choked eccentric plug valve, "
               "in contrast, needs variations in inlet pressure to maintain a constant flow when "
               "the outlet pressure varies."))
    b.append(p("Similar differences are shown in Table 6-1B when trying to maintain a constant "
               "downstream pressure (a typical pressure reduction application) with variations in "
               "flow rates. Here too, the inlet pressure of the conventional valve had to be "
               "varied when changing travel to accommodate changing flow rates."))
    b.append(table(["FL", "Cv", "P1 psia", "P2 psia", "Q GPM", "Type"],
                   [["0.44", "40", "100", "95", "90", "Hi-R"],
                    ["0.44", "20", "100", "80*", "90", "Hi-R"],
                    ["0.7", "40", "100", "88", "140", "Ecc.Pl"],
                    ["0.7", "20", "100", "51*", "140", "Ecc.Pl"]],
                   caption="Table 6-1A · Constant flow rate control"))
    b.append(table(["FL", "Cv", "P1 psia", "P2 psia", "Q GPM", "Type"],
                   [["0.44", "40", "100", "80", "178", "Hi-R"],
                    ["0.44", "20", "100", "80", "89", "Hi-R"],
                    ["0.7", "40", "100", "51*", "280", "Ecc.Pl"],
                    ["0.7", "20", "100", "51*", "140", "Ecc.Pl"]],
                   caption="Table 6-1B · Constant pressure control"))

    b.append(h2("Cavitation and noise", "Xâm thực và tiếng ồn"))
    b.append(p("One might wonder whether the high-recovery valve will cavitate excessively with an "
               "average low incipient cavitation number fxz of 0.15. Surprisingly not, due to two "
               "factors. First, because of the low F<sub>L</sub> number, incipient cavitation "
               "generated terminates at a benign level of 3 to 5 dBA above turbulence. More "
               "significant cavitation noise can be expected when the pressure drop exceeds about "
               "30% of P1, even though it does not reach damage level. Keep in mind that high "
               "pressure drops are not needed for flow control when the pressure ratio equals F"
               "<sub>L</sub><sup>2</sup> (see Chapter 15). In this case, the maximum turbulent "
               "noise only terminates at:"))
    b.append(eq("30 log(10 × FL² / fxz) = 3.3 dB", ""))
    b.append(p("Second, Xy, the point of maximum cavitation in this case, is a low 0.55. At this "
               "pressure ratio, there is practically no turbulence sound used to base the "
               "cavitation sound on."))
    b.append(p("The graph in Figure 6-2 shows that a maximum cavitation sound level is reached at "
               "X = 0.55, as predicted. Still, the overall sound level is about 5 to 8 dB below "
               "that of a conventional valve using basically the same input data except for a "
               "0.75 F<sub>L</sub> factor."))
    b.append(fig(2, F.fig_f62()))

    b.append(h2("Energy savings", "Tiết kiệm năng lượng"))
    b.append(p("Finally, also important is the energy savings offered by the high-recovery valve. "
               "As shown in Table 6-1B, the standard valve needs between 76 and 120 psi pressure "
               "drop, compared with only 20 psi for the high-recovery valve. This translates "
               "directly into pump horsepower savings."))

    b.append(note("<b>Source notes.</b> (1) The OCR text layer of the printed pages contains many "
                  "line-break hyphenations («pro-cess», «tur-bines», «thereaf-ter», "
                  "«recompres-sion», «stream-lined», «pres-sure»); the translation joins them into "
                  "whole words. (2) Figure 6-1 is a patent drawing (US Patent 105 782 15); it is "
                  "redrawn here as a simple vector schematic, not a facsimile, and only a few "
                  "callout numbers are retained. (3) In Table 6-1 the asterisked P2 values (80* "
                  "and 51*) are kept exactly as printed; this chapter does not explain what the "
                  "asterisks mean. (4) The Figure 6-2 caption states that the black line is the "
                  "conventional valve and the red line the high-recovery valve; the redraw keeps "
                  "that convention but draws the red line dashed for clarity. (5) The acoustic "
                  "relation is garbled in the source text («30 log(10 × FL 2/fxz) = 3.3 dB»); it "
                  "is presented here with the notation FL²."))
    b.append(h3("About the source", "Về nguồn tài liệu"))
    b.append(p("Chapter 6 occupies printed pp. 47-50 of the book (PDF pp. 54-57). The source has "
               "two figures (6-1 and 6-2) and one table (6-1, in parts A and B); all are retained, "
               "with the two figures redrawn as vectors."))
    return "".join(b)
