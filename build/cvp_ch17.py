# -*- coding: utf-8 -*-
"""Book 7, Chapter 17 - Will My Valve Be Too Noisy? (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
111-113 (PDF pp. 114-116). Three printed pages, no figures, no tables;
the chapter covers the three basic noise sources, valve-plug resonant
vibration, the OSHA 90 dBA limit, the energy coefficient EC, the ISA-75.17
and IEC 60534-8-3 prediction methods, Equation (17-1) and the promise of a
simpler ABC method in the next chapter.
"""
from cvp_common import eq, h2, h3, note, ol, p, refs, ul

PAGES_SRC = 3
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Will My Valve Be Too Noisy?"
TITLE_VI = "Van của tôi có quá ồn không?"


def note_terms(lang):
    """A one-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 17.</b> tiếng ồn (noise) · rung cơ khí (mechanical "
                "vibration) · độ rối (turbulence) · xâm thực (cavitation) · hóa hơi "
                "(flashing) · tiếng ồn khí động học (aerodynamic noise) · rung cộng hưởng "
                "(resonant vibration) · khe hở radial (radial clearance) · b dẫn nút van "
                "(plug guide) · bạc dẫn (guide bushing) · váy nút van (plug skirt) · vòng "
                "đế van (seat ring) · đế van / bệ van / mặt tựa của van (valve seat) · tần "
                "số tự nhiên (natural frequency) · độ cứng thân van (stem stiffness) · gãy "
                "do mỏi (fatigue breakage) · thang A-weighted (A-weighted scale) · dBA · "
                "bộ lót giảm ồn (low-noise trim) · hệ số năng lượng EC (energy coefficient) "
                "· Cv · FL · psia · ISA-75.17 · IEC 60534-8-3 · số Mach (Mach number) · "
                "phương pháp ABC")
    return ("<b>Key terms.</b> noise · mechanical vibration · turbulence · cavitation · "
            "flashing · aerodynamic noise · resonant vibration · radial clearance · plug "
            "guide · guide bushing · plug skirt · seat ring · valve seat · natural "
            "frequency · stem stiffness · fatigue breakage · A-weighted scale · dBA · "
            "low-noise trim · energy coefficient EC · Cv · FL · psia · ISA-75.17 · "
            "IEC 60534-8-3 · Mach number · ABC method")


def body_vi():
    b = []
    b.append(h2("Ba nguồn tiếng ồn cơ bản", "The three basic noise sources"))
    b.append(p("Ba loại nguồn tiếng ồn cơ bản trong van là (1) rung cơ khí, (2) độ rối và "
               "xâm thực với chất lỏng, và (3) tiếng ồn khí động học."))

    b.append(h2("Rung cộng hưởng của nút van", "Valve plug resonant vibration"))
    b.append(p("Tiếng ồn do rung cộng hưởng của nút van trong khe hở radial giữa b dẫn nút "
               "van và bạc dẫn, hoặc giữa váy nút van và vòng đế van, thường là kết quả của "
               "độ rối chất lưu dữ dội và có thể dễ dàng vượt quá 90 dB mức ồn ở tần số "
               "giữa 0,5 và 7 kHz. Hiện tượng này dường như không liên quan đến bản thân "
               "sự giảm áp (vận tốc chất lưu), mà liên quan đến dòng chảy không ổn định "
               "như hóa hơi hoặc nước đang xâm thực. May mắn thay, đây là một trường hợp "
               "khá hiếm. Theo kinh nghiệm của tôi, cộng hưởng xảy ra thường xuyên hơn "
               "khi tần số tự nhiên không bị cản của khối lượng m (trọng lượng của nút "
               "van chia cho gia tốc trọng trường) cao tương đối so với độ cứng Kn (tỷ "
               "lệ biến dạng vuông góc) của thân van. Điều này thường xảy ra khi tần số "
               "tự nhiên không bị cản (fn) nằm dưới 5000 Hz (chu kỳ/giây)."))
    b.append(eq("fₙ = 0.16 (Kₙ / m)^(1/2)  chu kỳ/giây"))
    b.append(p("Nút van rỗng làm giảm khối lượng m, trong khi chiều dài thân van không "
               "được đỡ ngắn hơn hoặc đường kính thân van lớn hơn sẽ làm tăng Kn — tất "
               "cả đều là biện pháp khắc phục tích cực. Giảm khe hở dẫn sẽ giảm biên độ, "
               "nhưng đó không phải là cách chữa dứt điểm; nếu không được kiểm soát, vấn "
               "đề có thể dẫn đến gãy do mỏi thân van hoặc b dẫn nút van. May mắn thay, "
               "người ta có thể nghe thấy rung cộng hưởng của nút van chủ yếu ở tần số "
               "giữa 100 và 1500 Hz với mức ồn có thể vượt quá 90 dBA. Điều đó phải được "
               "xem là tín hiệu cần hành động khắc phục."))

    b.append(h2("Giới hạn OSHA và thiệt hại do rung", "The OSHA limit and vibration damage"))
    b.append(p("Giới hạn phơi nhiễm 8 giờ cho người lao động ở mức 90 dB của Cơ quan Quản "
               "lý An toàn và Sức khỏe Nghề nghiệp (OSHA) được đo trên thang A-weighted, "
               "vốn được mô phỏng theo đường cong đáp ứng tần số của tai người; vì vậy, "
               "giới hạn là 90 dBA. Đó là một tiêu chí. Mặt khác, tiếng ồn chẳng qua là "
               "rung động có thể nghe được, và rung động có thể gây hư hỏng cho van, "
               "đường ống và các phụ kiện."))
    b.append(p("Ngay cả khi bạn bỏ qua giới hạn OSHA bằng cách chôn van dưới lòng đất, "
               "đường ống thường vẫn bị vỡ ở mức áp suất âm thanh trên 130 dBA [1], đo tại vị trí "
               "cách thành ống 1 m. Vì vậy, không nên chịu quá 110 dBA nếu không dùng "
               "bộ lót giảm ồn hoặc các biện pháp giảm ồn bên trong khác, ngay cả khi "
               "van được chôn."))

    b.append(h2("Hệ số năng lượng EC", "The energy coefficient EC"))
    b.append(p("Đừng đọc tiếp nếu van của bạn xử lý khí hoặc hơi và có hệ số năng lượng "
               "(EC) nhỏ hơn 1000. Con số này được tính bằng cách lấy áp suất đầu vào "
               "tuyệt đối tính bằng psia nhân với giá trị Cv đã tính của van và hệ số "
               "FL. Ví dụ, bạn giảm áp hơi 150 psia và Cv cần thiết của van bằng 125 ở "
               "hệ số FL = 0,9. Khi đó EC = 150 × 125 × 0,9 = 16,875, tức một van tiêu "
               "chuẩn có khả năng gây ồn. Mặt khác, một van có Cv chỉ bằng 6 sẽ có EC = "
               "6 × 150 × 0,9 = 810 và do đó có mức ồn thấp hơn giới hạn OSHA là 90 dBA, "
               "bất kể sự giảm áp."))

    b.append(h2("Dự đoán tiếng ồn: ISA-75.17 và IEC 60534-8-3",
                "Noise prediction: ISA-75.17 and IEC 60534-8-3"))
    b.append(p("ISA đã công bố một phương pháp dự đoán khá chính xác trong ISA-75.17, "
               "Control Valve Aerodynamic Noise Prediction, dựa trên các lý thuyết tiếng "
               "ồn dòng phun tự do đã được sửa đổi [2]. Tiêu chuẩn này hiện đã được thay "
               "thế bằng một tiêu chuẩn quốc tế, IEC 60534-8-3[3], tiêu chuẩn này chấp "
               "nhận phần lớn phương pháp luận của ISA-75.17. Lưu ý, phương pháp IEC được "
               "suy ra thực nghiệm. Nó chỉ làm việc tốt với các hệ số thuộc quyền sở hữu, "
               "riêng cho từng nhà cung cấp, được suy ra thực nghiệm và phù hợp với các "
               "kiểu van cụ thể, hoặc với một số bảng xấp xỉ; khi đó độ chính xác dự "
               "đoán ±5 dB thường được chấp nhận có thể không đạt được. Vì vậy, phương "
               "pháp IEC không áp dụng được cho mọi trường hợp nếu mong muốn độ chính "
               "xác chấp nhận được."))
    b.append(p("46 phương trình trở lên trong tiêu chuẩn IEC không nên làm bạn e ngại "
               "nếu bạn có một máy tính cỡ lớn; hơn nữa, đại đa số nhà cung cấp đã có sẵn "
               "chương trình máy tính hoặc có thể cung cấp cho bạn. Tuy nhiên, để cuộc "
               "sống dễ dàng hơn, tôi đã rút gọn tài liệu của Ủy ban Kỹ thuật Điện Quốc "
               "tế (IEC) xuống mức tiện lợi hơn, có thể dùng với máy tính cầm tay."))

    b.append(h3("Giới hạn số Mach tại cửa ra", "Limit the outlet Mach number"))
    b.append(p("Lưu ý: Để tránh các vấn đề tiếng ồn phía dưới, hãy giới hạn số Mach (Md) "
               "tại cửa ra của van."))
    b.append(eq("M_d = 0.20 P₁ Cᵥ F_L / (D² P₂ Cᵢ / 343)", num="17-1"))
    b.append(p("Trong đó: Cᵢ = vận tốc âm của khí đang dùng; D = đường kính cửa ra của "
               "van, tính bằng inch; P₁ = áp suất đầu vào tuyệt đối, tính bằng psia; P₂ = "
               "áp suất đầu ra tuyệt đối, tính bằng psia."))
    b.append(p("Nếu bạn thấy IEC 60534-8-3 quá phức tạp, tôi đã phát triển một phương "
               "pháp đơn giản hơn nhiều nhưng vẫn chính xác; đó là phương pháp ABC, được "
               "trình bày trong chương tới."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "V. A. Carucci, and R. T. Mueller, “Acoustically Induced Piping Vibration in High "
        "Capacity Pressure Reducing Systems,” ASME Paper 82-WA/PVP-8, 1982.",
        "H.D. Baumann,  “A Method to Predict Aerodynamic Valve Noise based on Modified "
        "free Jet Noise Theories,”  Proceedings of the ASME Winter Annual Meeting, "
        "December 1987: 13–18.",
        "IEC 60534-8-3 (2010), Control Valve Aerodynamic Noise Prediction Method "
        "(Geneva 20 – Switzerland: IEC [International Electrotechnical Commission]).",
    ]))
    b.append(h3("Đọc thêm", "Additional Reading"))
    b.append(ul([
        "H. D. Baumann, “On the Prediction of Aerodynamically Created Sound Pressure "
        "Level of Control Valves,” ASME paper WA/FE-28 (1970).",
        "C. Reed, “Optimizing Valve Jet Size and Spacing Reduces Valve Noise,” Control "
        "Engineering, (September 1976): 63–64.",
        "E. W. Singleton, “An Investigation into Control Valve-Generated Turbulence and "
        "Noise,” Measurement and Control 37, no. 6 (July 2004).",
        "H. D. Baumann, “Predicting Control Valve Noise at High Exit Velocities,” InTech "
        "(February 1997): 56–59.",
        "George W. Page Jr., “Predict Control Valve Noise,” Chemical Engineering  (July "
        "1997): 137–142.",
    ]))
    b.append(note("<b>Ghi chú về nguồn.</b> (1) Lớp văn bản OCR có các dấu gạch nối khi "
                  "xuống dòng («turbu-lence», «cavita-tion», «pres-sure», «fre-quency», "
                  "«unsup-ported», «expo-sure», «stan-dard»); bản dịch ghép lại thành từ "
                  "hoàn chỉnh. (2) Trong bản dump văn bản, Phương trình (17-1) bị xáo trộn "
                  "thành «M PC F DP d L= 020 1 2 2 . ν C/343i (17-1)»; bản dịch dùng dạng "
                  "đọc được từ trang in: M_d = 0.20 P₁ Cᵥ F_L / (D² P₂ Cᵢ / 343). (3) Các "
                  "nét đặc thù của nguyên bản («inn psia», «undammed natural frequency», "
                  "cụm «standard has now been replaced by an international standard, IEC "
                  "60534-8-3[3]» và «Geneva 20 – Switzerland») được giữ nguyên trong bản "
                  "tiếng Anh; bản tiếng Việt dùng thuật ngữ kỹ thuật đúng. (4) Tên tạp chí "
                  "trong nguyên bản có dấu nối được viết là «Measurement and Control» để "
                  "tránh ký tự trần trong HTML. (5) Chương này không có hình hay bảng nào."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 17 chiếm các trang in 111–113 của ấn bản in (PDF tr. 114–116). "
               "Nguyên bản gồm ba nguồn tiếng ồn cơ bản, đoạn về rung cộng hưởng của nút "
               "van, giới hạn OSHA 90 dBA, hệ số năng lượng EC với hai ví dụ, phương pháp "
               "ISA-75.17 và IEC 60534-8-3, Phương trình (17-1) với định nghĩa các biến, "
               "lời nhắc về số Mach, ba tài liệu tham khảo và năm mục đọc thêm — tất cả "
               "đều được giữ lại."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Ba nguồn tiếng ồn cơ bản", "The three basic noise sources"))
    b.append(p("The three basic types of noise sources in valves are (1) mechanical "
               "vibration, (2) turbulence and cavitation with liquids, and (3) "
               "aerodynamic noise."))

    b.append(h2("Rung cộng hưởng của nút van", "Valve plug resonant vibration"))
    b.append(p("Noise caused by resonant vibration of a valve plug within the radial "
               "clearance between plug guide and guide bushing, or between plug skirt and "
               "seat ring, is usually the result of severe fluid turbulence and can easily "
               "exceed 90 dB of sound level at frequencies between 0.5 and 7 kHz. This "
               "phenomenon seems not to be related to pressure drop (fluid velocity) itself "
               "but rather to unstable fluid flow such as flashing or cavitating water. "
               "Fortunately, this is a rather rare occurrence. Based on my experience, "
               "resonance occurs more often where the undamped natural frequency of the "
               "mass (m, the weight of valve plug divided by the acceleration of gravity) "
               "is high in relationship to the stiffness Kn (the perpendicular deflection "
               "rate) of the valve stem. This typically happens when the undammed natural "
               "frequency (fn) is below 5000 Hz (cycles/s)."))
    b.append(eq("fₙ = 0.16 (Kₙ / m)^(1/2)  cycles/s"))
    b.append(p("A hollow plug will reduce the mass (m), while a shorter unsupported stem "
               "length, or a larger stem diameter, will increase Kn—all positive remedies. "
               "Decreasing the guide clearance will reduce the amplitude, but that is not a "
               "sure cure for the problem, which, when unchecked, can lead to fatigue "
               "breakage of the stem or plug guide. Fortunately, one can hear the resonant "
               "vibrations of a valve plug occurring at frequencies mostly between 100 and "
               "1500 Hz and sound levels that can exceed 90 dBA. This then should be taken "
               "as a call for remedial action."))

    b.append(h2("Giới hạn OSHA và thiệt hại do rung", "The OSHA limit and vibration damage"))
    b.append(p("The Occupational Safety and Health Administration (OSHA) limit of 8 hours "
               "of exposure for workers at 90 dB is measured on the A-weighted scale, "
               "which is patterned after the frequency response curve of the human ear; "
               "therefore, limit = 90 dBA. This is one criterion. On the other hand, noise "
               "is nothing but audible vibration, and vibration can cause damage to "
               "valves, piping, and accessories."))
    b.append(p("Even if you ignore the OSHA limit by putting the valve underground, the "
               "pipe will typically break at a sound pressure above 130 dBA [1] measured "
               "1 m from the pipe wall. Therefore, tolerate no more than 110 dBA without "
               "using “low-noise trim” or other internal noise abatement means even when "
               "the valve is buried!"))

    b.append(h2("Hệ số năng lượng EC", "The energy coefficient EC"))
    b.append(p("Do not read on if your valve is handling gas or steam and has an energy "
               "coefficient (EC) of less than 1000. This number is derived by multiplying "
               "the absolute inlet pressure in psia by the calculated valve Cv and FL "
               "numbers. For example, you reduce 150 psia steam and the required valve "
               "Cv = 125 at an FL factor of 0.9. Here your EC = 150 × 125 × 0.9 = 16,875, "
               "which is potentially a noisy standard valve. On the other hand, a valve "
               "with a Cv of only 6 has an EC of 6 × 150 × 0.9 = 810 and, therefore, a "
               "sound level of less than the OSHA limit of 90 dBA, regardless of the "
               "pressure drop."))

    b.append(h2("Dự đoán tiếng ồn: ISA-75.17 và IEC 60534-8-3",
                "Noise prediction: ISA-75.17 and IEC 60534-8-3"))
    b.append(p("ISA published a reasonably accurate prediction method in ISA-75.17, "
               "Control Valve Aerodynamic Noise Prediction, based on modified free jet "
               "noise theories [2]. This standard has now been replaced by an "
               "international standard, IEC 60534-8-3[3], which adopts most of the "
               "methodology in the ISA-75.17 standard. Note, The IEC method is empirically "
               "derived. It only works well with proprietary, vendor-specific, empirically "
               "derived factors fitting specific valve types, or some tabulated "
               "approximations thereof, where the typically accepted prediction accuracy "
               "of ±5 dB may not be met. Thus, the IEC method is not universally "
               "applicable if acceptable accuracy is desired."))
    b.append(p("The 46 plus equations in the IEC standard should not scare you if you "
               "possess a full-size computer; besides, the vast majority of vendors have "
               "computer programs in place or available to you. However, to make life "
               "easier, I have condensed the International Electrotechnical Commission "
               "(IEC) document to a handier level that can be used with a handheld "
               "calculator."))

    b.append(h3("Giới hạn số Mach tại cửa ra", "Limit the outlet Mach number"))
    b.append(p("Note: To avoid downstream noise problems, limit the Mach number (Md) at "
               "the valve outlet port."))
    b.append(eq("M_d = 0.20 P₁ Cᵥ F_L / (D² P₂ Cᵢ / 343)", num="17-1"))
    b.append(p("where Cᵢ = velocity of sound of the used gas; D = valve outlet diameter in "
               "inches; P₁ = absolute inlet pressure inn psia; P₂ = absolute outlet "
               "pressure in psia."))
    b.append(p("If you think IEC 60534-8-3 is too complicated, I have developed a much "
               "simpler, yet accurate, method; it is called the ABC method and is "
               "addressed in the next chapter."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "V. A. Carucci, and R. T. Mueller, “Acoustically Induced Piping Vibration in High "
        "Capacity Pressure Reducing Systems,” ASME Paper 82-WA/PVP-8, 1982.",
        "H.D. Baumann,  “A Method to Predict Aerodynamic Valve Noise based on Modified "
        "free Jet Noise Theories,”  Proceedings of the ASME Winter Annual Meeting, "
        "December 1987: 13–18.",
        "IEC 60534-8-3 (2010), Control Valve Aerodynamic Noise Prediction Method "
        "(Geneva 20 – Switzerland: IEC [International Electrotechnical Commission]).",
    ]))
    b.append(h3("Đọc thêm", "Additional Reading"))
    b.append(ul([
        "H. D. Baumann, “On the Prediction of Aerodynamically Created Sound Pressure "
        "Level of Control Valves,” ASME paper WA/FE-28 (1970).",
        "C. Reed, “Optimizing Valve Jet Size and Spacing Reduces Valve Noise,” Control "
        "Engineering, (September 1976): 63–64.",
        "E. W. Singleton, “An Investigation into Control Valve-Generated Turbulence and "
        "Noise,” Measurement and Control 37, no. 6 (July 2004).",
        "H. D. Baumann, “Predicting Control Valve Noise at High Exit Velocities,” InTech "
        "(February 1997): 56–59.",
        "George W. Page Jr., “Predict Control Valve Noise,” Chemical Engineering  (July "
        "1997): 137–142.",
    ]))
    b.append(note("<b>Source note.</b> (1) The OCR text layer contains line-break "
                  "hyphenations («turbu-lence», «cavita-tion», «pres-sure», «fre-quency», "
                  "«unsup-ported», «expo-sure», «stan-dard»); the translation rejoins them "
                  "into whole words. (2) In the text dump, Equation (17-1) is garbled as "
                  "«M PC F DP d L= 020 1 2 2 . ν C/343i (17-1)»; the readable form is taken "
                  "from the printed page: M_d = 0.20 P₁ Cᵥ F_L / (D² P₂ Cᵢ / 343). (3) The "
                  "source quirks «inn psia», «undammed natural frequency», «standard has "
                  "now been replaced by an international standard, IEC 60534-8-3[3]», and "
                  "«Geneva 20 – Switzerland» are kept verbatim in this English text; the "
                  "Vietnamese rendering uses the correct technical terms. (4) The journal "
                  "name printed with a joining mark is written «Measurement and Control» "
                  "here to avoid a bare ampersand in the HTML. (5) The chapter contains no "
                  "figures and no tables."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chapter 17 occupies printed pp. 111–113 of the book (PDF pp. 114–116). "
               "The source consists of the three basic noise sources, the passage on "
               "valve plug resonant vibration, the OSHA 90 dBA limit, the energy "
               "coefficient EC with two worked examples, the ISA-75.17 and IEC 60534-8-3 "
               "methods, Equation (17-1) with its variable definitions, the Mach-number "
               "reminder, three references and five additional-reading items, all of "
               "which are retained."))
    return "".join(b)
