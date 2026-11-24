# -*- coding: utf-8 -*-
"""Book 7c, Chapter 12 - Safety Instrumented Systems (EN/VI bilingual).

Source: Emerson, *Control Valve Handbook*, 6th ed. (2020), printed pp. 250-259.
This is a short/mid chapter: safety and layers of protection, safety
instrumented systems and functions, functional safety standards, safety
integrity levels, probability of failure on demand, final elements and proof
testing, partial stroke testing, online testing methods, digital valve
controllers, and high-integrity pressure protection systems (HIPPS).
Five numbered figures are redrawn as legible vectors in `cvh6fig12.py` and
placed in numbered order at their logical prose points.
"""

import cvh6_common as C  # noqa: F401
from cvh6_common import fig, h2, h3, h4, lead, note, p, ul
import cvh6fig12 as F12

PAGES_SRC = 10         # source printed pp. 250-259 inclusive
BYLINE = "Emerson Flow Controls · Control Valve Handbook, 6th ed. (2020)"
TITLE_EN = "Safety Instrumented Systems"
TITLE_VI = "Hệ thống an toàn bằng dụng cụ"


def note_terms(lang):
    """A one-line glossary box of the chapter's key terms."""
    if lang == "vi":
        return (
            "<b>Thuật ngữ chính của chương.</b> an toàn chức năng — functional safety · "
            "hệ thống an toàn bằng dụng cụ (SIS) — safety instrumented system · "
            "hàm an toàn bằng dụng cụ (SIF) — safety instrumented function · "
            "mức toàn vẹn an toàn (SIL) — safety integrity level · "
            "xác suất hỏng khi yêu cầu (PFDavg) — probability of failure on demand · "
            "hệ số giảm rủi ro (RRF) — risk reduction factor · "
            "các lớp bảo vệ — layers of protection · "
            "hệ thống điều khiển quy trình cơ bản (BPCS) — basic process control system · "
            "bộ giải logic — logic solver · phần tử điều khiển cuối — final control element · "
            "lớp bảo vệ độc lập (IPL) — independent protection layer · "
            "kiểm tra chứng minh — proof test · kiểm tra hành trình một phần (PST) — partial "
            "stroke test · kiểm tra hành trình đầy đủ — full stroke test · "
            "thời gian giữa các lần kiểm tra (TI) — test interval · "
            "độ bao phủ chẩn đoán — diagnostic coverage · "
            "an toàn khi mất điện — fail-safe · chịu lỗi — fault-tolerant · "
            "dừng khẩn cấp (ESD) — emergency shutdown · "
            "van xả áp (BDV) — blowdown valve · "
            "bộ điều khiển van số (DVC) — digital valve controller · "
            "hỏng hóc tiềm ẩn — covert or hidden failure · "
            "ngắt giả hoặc ngắt gây phiền nhiễu — nuisance or spurious trip · "
            "phân tích khả năng chịu rủi ro — risk-tolerance analysis · "
            "nghiên cứu mối nguy và khả năng vận hành (HAZOP) — HAZard and OPerability study · "
            "nghiên cứu mối nguy quy trình (PHA) — process hazard study · "
            "hệ thống bảo vệ áp suất toàn vẹn cao (HIPPS) — high-integrity pressure protection "
            "system · bỏ phiếu 2 trên 3 (2oo3) — 2 out of 3 voting · "
            "sắp xếp 1 trên 2 (1oo2) — 1oo2 arrangement · "
            "rào chắn cuối cùng — last line of defense")
    return (
        "<b>Key terms in this chapter.</b> functional safety · safety instrumented system (SIS) · "
        "safety instrumented function (SIF) · safety integrity level (SIL) · probability of "
        "failure on demand (PFDavg) · risk reduction factor (RRF) · layers of protection · "
        "basic process control system (BPCS) · logic solver · final control element · "
        "independent protection layer (IPL) · proof test · partial stroke test (PST) · "
        "full stroke test · test interval (TI) · diagnostic coverage · fail-safe · "
        "fault-tolerant · emergency shutdown (ESD) · blowdown valve (BDV) · "
        "digital valve controller (DVC) · covert or hidden failure · nuisance or spurious trip · "
        "risk-tolerance analysis · HAZard and OPerability study (HAZOP) · "
        "process hazard study (PHA) · high-integrity pressure protection system (HIPPS) · "
        "2 out of 3 voting (2oo3) · 1oo2 arrangement · last line of defense")


def source_notes(lang):
    """Source quirks and translation notes for this chapter."""
    if lang == "vi":
        return (
            "<b>Ghi chú về nguồn.</b> (1) Ký tự bullet OCR lạc «» xuất hiện ở cuối nhiều đoạn và "
            "trước các mục bullet; nó được thay bằng đoạn văn hoặc danh sách bullet bình thường. "
            "(2) Nhiều tiêu đề bị gãy dòng trong bản dump, ví dụ «12.1 Safety and Layers / of "
            "Protection», «12.2 Safety Instrumented / Systems (SIS)», «12.4 Safety Integrity Level / "
            "(SIL)», «12.5 Probability of Failure / Upon Demand», «12.6 Final Elements, Proof / "
            "Testing, and Partial Stroke / Testing Techniques», «12.7 Partial Stroke Testing», "
            "«12.8 Online Testing Methods / for the Final Element», «12.9 Digital Valve Controller / "
            "Use for Partial Stroke Testing», «12.10 High-Integrity / Pressure Protection System / "
            "(HIPPS)», «12.11 Functionality of the / HIPPS»; các dòng được nối lại thành một tiêu đề. "
            "(3) Chú thích Hình 12.2 được chèn giữa câu: «Final control elements implement the action» "
            "trên trang 252 rồi câu tiếp tục «determined by the logic solver...» trên trang 253; câu "
            "được nối lại để dễ đọc và hình được đặt ngay sau mô tả phần tử điều khiển cuối. "
            "(4) Chú thích Hình 12.4 cũng nằm giữa câu ở mục 12.8, tách cụm «a pin, a valve stem» "
            "khỏi «collar, a valve hand jack, etc.»; câu được nối lại. "
            "(5) Chú thích Hình 12.5 nằm ở cuối mục 12.12 trên trang 258, ngay sau dấu «», dù nội "
            "dung thuộc mục 12.10 đến 12.12; thứ tự bản in được giữ nguyên. "
            "(6) Nguồn viết «PFDavg» không có dấu cách và tiêu đề Hình 12.3 gộp «PFDavg and RRF»; bản "
            "tiếng Anh giữ «PFDavg», bản tiếng Việt dùng cùng ký hiệu. "
            "(7) «RRF» được nêu cả trong tiêu đề cột của Hình 12.3 (Risk Reduction Factor) lẫn qua quan "
            "hệ PFDavg bằng 1 chia cho RRF; cả hai cách nêu được giữ. "
            "(8) Một số lỗi chính tả và ngữ pháp được giữ trong tiếng Anh và sửa trong tiếng Việt: "
            "«manufacturing plans» (phải là plants) ở mục 12.3, «All elements of the SIF need to be "
            "capable being used» (thiếu of) ở mục 12.4, và «Logic solvers re often working» (thiếu a) "
            "ở mục 12.12. "
            "(9) Các cụm trong dấu ngoặc kép như «safe state» và «last line of defense» được giữ nguyên. "
            "(10) Bảng Hình 12.3 dùng ký hiệu ^ cho lũy thừa vì bản dump không giữ được chữ số mũ; các "
            "giá trị số được sao chép chính xác. "
            "(11) Hình 12.4 trong bản in chỉ có trục phần trăm 0 đến 50 và ba nhãn cảm biến, bộ giải "
            "logic, phần tử điều khiển cuối, không có giá trị cột cụ thể; chiều cao cột trong bản vẽ "
            "lại chỉ mang tính minh họa và được ghi rõ như vậy. "
            "(12) Các hình trong bản in là sơ đồ, bảng và biểu đồ cột; chúng được vẽ lại dạng vector, "
            "không phải ảnh raster.")
    return (
        "<b>Source notes.</b> (1) A stray OCR bullet glyph «» appears at the end of many paragraphs "
        "and before list entries; it is replaced by ordinary paragraphs or bullet lists. "
        "(2) Many headings are line-wrapped in the dump, for example «12.1 Safety and Layers / of "
        "Protection», «12.2 Safety Instrumented / Systems (SIS)», «12.4 Safety Integrity Level / "
        "(SIL)», «12.5 Probability of Failure / Upon Demand», «12.6 Final Elements, Proof / Testing, "
        "and Partial Stroke / Testing Techniques», «12.7 Partial Stroke Testing», «12.8 Online "
        "Testing Methods / for the Final Element», «12.9 Digital Valve Controller / Use for Partial "
        "Stroke Testing», «12.10 High-Integrity / Pressure Protection System / (HIPPS)», and "
        "«12.11 Functionality of the / HIPPS»; the lines are joined into one heading. "
        "(3) The Figure 12.2 caption interrupts a sentence: «Final control elements implement the "
        "action» on page 252, then «determined by the logic solver...» on page 253; the sentence is "
        "joined for legibility and the figure is placed right after the final-element description. "
        "(4) The Figure 12.4 caption likewise interrupts a sentence in section 12.8, separating "
        "«a pin, a valve stem» from «collar, a valve hand jack, etc.»; the sentence is joined. "
        "(5) The Figure 12.5 caption sits at the end of section 12.12 on page 258, just after a "
        "«» glyph, although its content belongs to sections 12.10 through 12.12; the printed "
        "order is preserved. "
        "(6) The source writes «PFDavg» without a space and the Figure 12.3 heading runs «PFDavg "
        "and RRF» together; the English text keeps «PFDavg», and the Vietnamese text uses the same "
        "notation. "
        "(7) «RRF» is introduced both in the Figure 12.3 column heading (Risk Reduction Factor) and "
        "through the relation PFDavg equals 1 divided by RRF; both mentions are kept. "
        "(8) Several spelling and grammar quirks are retained in English and corrected in "
        "Vietnamese: «manufacturing plans» (should be plants) in section 12.3, «All elements of the "
        "SIF need to be capable being used» (missing of) in section 12.4, and «Logic solvers re "
        "often working» (missing a) in section 12.12. "
        "(9) Quoted phrases such as «safe state» and «last line of defense» are kept as printed. "
        "(10) The Figure 12.3 table uses the caret ^ for powers because the dump does not preserve "
        "superscripts; all numeric values are copied exactly. "
        "(11) The printed Figure 12.4 has only a 0 to 50 percent axis and three category labels, "
        "sensor, logic solver and final control element, with no numeric bar values; the bar heights "
        "in the redrawing are illustrative and are labelled as such. "
        "(12) The printed figures are diagrams, a table and a bar chart; they are redrawn as "
        "vectors rather than raster images.")


def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def B(v, e):
        b.append(ul(v if vi else e))

    def FIG(n, fn):
        b.append(fig(n, fn, lang))

    def N(v, e):
        b.append(note(v if vi else e))

    # ------------------------------------------------------------ lead
    b.append(lead(
        "Chương này trình bày các hệ thống an toàn bằng dụng cụ (SIS): các lớp bảo vệ, thành phần "
        "của SIS và các hàm an toàn bằng dụng cụ (SIF), các tiêu chuẩn an toàn chức năng, mức toàn "
        "vẹn an toàn (SIL), xác suất hỏng khi yêu cầu (PFDavg) và hệ số giảm rủi ro (RRF), kiểm tra "
        "chứng minh và kiểm tra hành trình một phần, bộ điều khiển van số, cũng như hệ thống bảo vệ "
        "áp suất toàn vẹn cao (HIPPS). Năm hình trong bản in được vẽ lại dạng vector và đặt theo "
        "thứ tự số tại vị trí văn bản hợp lý."
        if vi else
        "This chapter presents safety instrumented systems (SIS): layers of protection, the "
        "components of an SIS and safety instrumented functions (SIF), functional safety standards, "
        "safety integrity levels (SIL), probability of failure on demand (PFDavg) and risk reduction "
        "factor (RRF), proof testing and partial stroke testing, digital valve controllers, and "
        "high-integrity pressure protection systems (HIPPS). The five printed figures are redrawn "
        "as vectors and placed in numbered order at their logical prose points."))
    N(note_terms("vi"), note_terms("en"))

    # ------------------------------------------------------------ 12.1
    H("12.1 An toàn và các lớp bảo vệ", "12.1 Safety and Layers of Protection")
    P("An toàn được đảm bảo bằng các lớp bảo vệ. Các lớp bảo vệ này bắt đầu từ việc điều khiển quy "
      "trình hiệu quả, mở rộng đến các lớp phòng ngừa an toàn thủ công và tự động, rồi tiếp tục bằng "
      "các lớp nhằm giảm nhẹ hậu quả của một sự cố.",
      "Safety is provided by layers of protection. These layers of protection start with effective "
      "process control, extend to manual and automatic safety prevention layers, and continue with "
      "layers to mitigate the consequences of an event.")
    P("Lớp đầu tiên là hệ thống điều khiển quy trình cơ bản (BPCS). Bản thân hệ thống điều khiển quy "
      "trình đã mang lại sự an toàn đáng kể thông qua thiết kế đúng đắn của việc điều khiển quy trình.",
      "The first layer is the basic process control system (BPCS). The process control system itself "
      "provides significant safety through proper design of process control.")
    P("Lớp bảo vệ tiếp theo cũng do hệ thống điều khiển và các người vận hành hệ thống đó cung cấp. "
      "Các trình tự dừng máy tự động trong hệ thống điều khiển quy trình, kết hợp với sự can thiệp "
      "của người vận hành để dừng quy trình, là lớp an toàn tiếp theo.",
      "The next layer of protection is also provided by the control system and the control system "
      "operators. Automated shutdown routines in the process control system combined with operator "
      "intervention to shut down the process are the next layer of safety.")
    P("Tiếp theo là hệ thống an toàn bằng dụng cụ. Đây là một hệ thống an toàn độc lập với hệ thống "
      "điều khiển quy trình. Nó có cảm biến, van và bộ giải logic riêng. Vai trò duy nhất của nó là an "
      "toàn. Không có hoạt động điều khiển quy trình nào được thực hiện trong hệ thống này.",
      "Next is the safety instrumented system. It is a safety system independent of the process "
      "control system. It has separate sensors, valves, and a logic solver. Its only role is safety. "
      "No process control is performed in this system.")
    P("Sự can thiệp của người vận hành và các lớp hệ thống an toàn bằng dụng cụ được thiết kế để ngăn "
      "một sự kiện liên quan đến an toàn. Nếu một sự kiện liên quan đến an toàn xảy ra, sẽ có các lớp "
      "bổ sung được thiết kế để giảm nhẹ tác động của sự kiện đó.",
      "Operator intervention and the safety instrumented system layers are designed to prevent a "
      "safety-related event. If a safety-related event occurs, there are additional layers designed "
      "to mitigate the impact of the event.")
    P("Lớp tiếp theo là lớp bảo vệ chủ động. Lớp này có thể có van hoặc đĩa vỡ được thiết kế để tạo "
      "điểm xả, ngăn không cho xảy ra sự thoát không kiểm soát có thể gây cháy hoặc nổ.",
      "The next layer is an active protection layer. This layer may have valves or rupture disks "
      "designed to provide a relief point that prevents an uncontrolled release that can cause an "
      "explosion or fire.")
    P("Lớp tiếp theo là lớp bảo vệ thụ động. Lớp này có thể gồm một con đê hoặc một rào chắn thụ động "
      "khác có tác dụng ngăn chặn đám cháy hoặc dẫn năng lượng của vụ nổ theo hướng giảm thiểu sự lan "
      "truyền của thiệt hại.",
      "The next layer is a passive protection layer. It may consist of a dike or other passive "
      "barrier that serves to contain a fire or channel the energy of an explosion in a direction "
      "that minimizes the spread of damage.")
    FIG(1, F12.fig_f12_01())
    P("Lớp cuối cùng là ứng phó của nhà máy và dịch vụ khẩn cấp. Nếu xảy ra một sự kiện an toàn lớn, "
      "lớp này phản ứng theo cách giảm thiểu thiệt hại, thương tích hoặc mất mạng người đang tiếp "
      "diễn. Nó có thể gồm kế hoạch sơ tán, chữa cháy và các hoạt động tương tự.",
      "The final layer is plant and emergency response. If a large safety event occurs this layer "
      "responds in a way that minimizes ongoing damage, injury, or loss of life. It may include "
      "evacuation plans, firefighting, etc.")
    P("An toàn tổng thể được quyết định bởi cách các lớp này phối hợp với nhau.",
      "Overall safety is determined by how these layers work together.")

    # ------------------------------------------------------------ 12.2
    H("12.2 Hệ thống an toàn bằng dụng cụ (SIS)",
      "12.2 Safety Instrumented Systems (SIS)")
    P("Hệ thống an toàn bằng dụng cụ (SIS) được xem là tách biệt với hệ thống điều khiển quy trình "
      "cơ bản (BPCS) ở chỗ SIS được chuyên dùng để đưa quy trình về «trạng thái an toàn» khi xảy ra "
      "tình huống nguy hiểm.",
      "A safety instrumented system (SIS) is considered separate than the basic process control "
      "system (BPCS) in that the SIS is dedicated to taking the process to a “safe state” should a "
      "critical situation occur.")
    P("SIS gồm nhiều hàm an toàn bằng dụng cụ (SIF). Mỗi hàm an toàn bằng dụng cụ có một mức toàn vẹn "
      "an toàn (SIL) được quy định, cần thiết để đạt được an toàn chức năng. Mỗi SIF là một vòng riêng "
      "biệt hoặc liên kết gồm cảm biến, bộ giải logic (LS) và phần tử điều khiển cuối (FE), như thể "
      "hiện trong Hình 12.2.",
      "The SIS consists of several safety instrumented functions (SIF). Each safety instrumented "
      "function has a specified safety integrity level (SIL), which is necessary to achieve "
      "functional safety. Each SIF is a separate or interlinked loop comprised of sensors, logic "
      "solver (LS), and final control element (FE) as shown in Figure 12.2.")
    P("Cảm biến: Cảm biến hiện trường được dùng để thu thập thông tin cần thiết nhằm xác định có tồn "
      "tại tình huống khẩn cấp hay không. Mục đích của các cảm biến này là đo các thông số quy trình "
      "(như nhiệt độ, áp suất, lưu lượng, mật độ, v.v.) để xác định thiết bị hoặc quy trình có ở trạng "
      "thái an toàn hay không. Loại cảm biến trải từ công tắc khí nén hoặc điện đơn giản đến bộ phát "
      "thông minh có chẩn đoán tích hợp. Các cảm biến này được chuyên dùng cho dịch vụ SIS và có các "
      "điểm lấy mẫu quy trình riêng biệt, khác với các điểm lấy mẫu dùng cho cảm biến thông tin quy "
      "trình thông thường.",
      "Sensors: Field sensors are used to collect information necessary to determine if an emergency "
      "situation exists. The purpose of these sensors is to measure process parameters (i.e. "
      "temperature, pressure, flow, density etc.) to determine if the equipment or process is in a "
      "safe state. Sensor types range from simple pneumatic or electrical switches to smart "
      "transmitters with on-board diagnostics. These sensors are dedicated to SIS service and have "
      "process taps, which are separate and distinct from the process taps used by normal process "
      "information sensors.")
    P("Bộ giải logic: Mục đích của thành phần này của SIS là xác định cần thực hiện hành động gì dựa "
      "trên thông tin đã thu thập. Các bộ giải logic có độ tin cậy cao được dùng, mang lại cả vận hành "
      "an toàn khi mất điện và vận hành chịu lỗi. Thông thường đây là bộ điều khiển đọc tín hiệu từ "
      "cảm biến và thực hiện các hành động được lập trình sẵn để ngăn ngừa mối nguy bằng cách xuất "
      "tín hiệu tới một hoặc nhiều phần tử điều khiển cuối. Bộ giải logic thường là thiết bị có thể "
      "lập trình hoặc không lập trình được, nhưng cũng có thể là cơ khí dưới dạng công tắc được đặt "
      "để kích hoạt chức năng an toàn.",
      "Logic Solver: The purpose of this component of SIS is to determine what action is to be taken "
      "based on the information gathered. Highly reliable logic solvers are used which provide both "
      "fail-safe and fault-tolerant operation. It is typically a controller that reads signals from "
      "the sensors and executes pre-programmed actions to prevent a hazard by providing output to "
      "final control element(s). Logic solvers are very often programmable or non-programmable "
      "devices, but can also be mechanical in form of switched set to trip the safety function.")
    P("Phần tử điều khiển cuối: Các phần tử điều khiển cuối thực hiện hành động do bộ giải logic "
      "quyết định.",
      "Final Control Element: Final control elements implement the action")
    FIG(2, F12.fig_f12_02())
    P("Phần tử điều khiển cuối này thường là van đóng hoặc mở tự động, với chức năng fail-closed "
      "(đóng khi mất nguồn) hoặc fail-open (mở khi mất nguồn).",
      "determined by the logic solver. This final control element is typically an automated on/off "
      "valve, with a valve fail-closed or fail-open function.")
    P("Điều bắt buộc là cả ba phần tử của SIS phải hoạt động đúng như thiết kế để cô lập an toàn "
      "nhà máy quy trình trong trường hợp khẩn cấp.",
      "It is imperative that all three elements of the SIS function as designed in order to safely "
      "isolate the process plant in the event of an emergency.")

    # ------------------------------------------------------------ 12.3
    H("12.3 Tiêu chuẩn an toàn", "12.3 Safety Standards")
    P("Trong một nhà máy quy trình không có khái niệm vận hành không rủi ro hay độ tin cậy 100%. Vì "
      "vậy, một trong những nhiệm vụ đầu tiên của người thiết kế SIS là thực hiện phân tích khả năng "
      "chịu rủi ro để xác định cần mức độ an toàn nào. Tiêu chuẩn IEC 61508 (An toàn chức năng của hệ "
      "thống điện, điện tử và điện tử lập trình được) là tiêu chuẩn chung bao phủ an toàn chức năng "
      "liên quan đến mọi loại nhà máy chế biến và sản xuất. Tiêu chuẩn IEC 61511 và ISA S84.01 "
      "(được thay bằng ISA 84.00.01-2004) là các tiêu chuẩn riêng cho ngành công nghiệp quy trình. "
      "Cả ba tiêu chuẩn đều dùng mô hình vòng đời dựa trên hiệu năng và quy định mức độ an toàn chính "
      "xác, thực hành tốt nhất, cùng bằng chứng định lượng về sự tuân thủ.",
      "In a process plant, there is no such thing as risk-free operation or 100% reliability. "
      "Therefore, one of the first tasks of the SIS designer is to perform a risk-tolerance analysis "
      "to determine what level of safety is needed. IEC Standard 61508 (Functional Safety of "
      "Electric, Electronic and Programmable Electronic Systems) is a general standard that covers "
      "functional safety related to all kinds of processing and manufacturing plans. IEC Standard "
      "61511 and ISA S84.01 (Replaced by ISA 84.00.01-2004) are standards specific to the process "
      "industries. All three standards use a performance-based lifecycle model and specify precise "
      "levels of safety, best practices, and quantifiable proof of compliance.")

    # ------------------------------------------------------------ 12.4
    H("12.4 Mức toàn vẹn an toàn (SIL)",
      "12.4 Safety Integrity Level (SIL)")
    P("Các mức toàn vẹn an toàn (SIL) là thước đo định lượng của rủi ro. Từ khi được đưa vào sử dụng, "
      "các mức toàn vẹn an toàn đã được dùng như cách định lượng để thiết lập mục tiêu hiệu năng an "
      "toàn cho các hệ thống SIS. Tiêu chuẩn IEC quy định bốn mức toàn vẹn an toàn có thể có (SIL 1, "
      "SIL 2, SIL 3, SIL 4) như thể hiện trong Hình 12.3; tuy nhiên, ISA S84.01 chỉ công nhận tối đa "
      "đến SIL 3.",
      "Safety integrity levels (SIL) are quantifiable measurement of risk. Since they were first "
      "introduced, safety integrity levels have been used as a quantifiable way to establish safety "
      "performance targets for SIS systems. IEC standards specify four possible Safety Integrity "
      "Levels (SIL 1, SIL 2, SIL 3, SIL 4) as shown in Figure 12.3; however, ISA S84.01 only "
      "recognizes up to SIL 3.")
    P("Việc xác định mức toàn vẹn an toàn mục tiêu đòi hỏi:",
      "A determination of the target Safety Integrity Level requires:")
    B(["Xác định các mối nguy liên quan.",
       "Đánh giá rủi ro của từng mối nguy đã xác định.",
       "Đánh giá các Lớp bảo vệ độc lập (IPL) khác có thể đã được lắp đặt."],
      ["An identification of the hazards involved.",
       "Assessment of the risk of each of the identified hazards.",
       "An assessment of other Independent Protection Layers (IPLs) that may be in place."])
    P("Các mối nguy có thể được xác định bằng nhiều kỹ thuật khác nhau; một kỹ thuật thường dùng là "
      "nghiên cứu Mối nguy và Khả năng vận hành (HAZard and OPerability study, HAZOP).",
      "Hazards can be identified using a number of different techniques; one common technique is a "
      "HAZard and OPerability study (HAZOP).")
    P("Sau đó, phải xác định hệ số rủi ro cho từng mối nguy đã định nghĩa, trong đó rủi ro được định "
      "nghĩa là hàm của xác suất (khả năng hay tần suất) và hậu quả (mức độ nghiêm trọng) của từng "
      "sự kiện nguy hiểm.",
      "A risk factor must then be determined for each of the defined hazards, where risk is defined "
      "as a function of the probability (likelihood or frequency) and consequences (severity) of "
      "each hazardous event.")
    P("Nghiên cứu HAZOP được dùng để xác định rủi ro cho con người hoặc môi trường và được thực hiện "
      "bởi một nhóm đa ngành (nhóm HAZOP).",
      "The HAZOP study is used to identify the risk to personnel or the environment and is carried "
      "out by a multi-disciplinary team (HAZOP team).")
    P("Sau khi rủi ro đã được xác định, nghiên cứu HAZOP hoặc nghiên cứu mối nguy quy trình (PHA) sẽ "
      "đặt ra yêu cầu giảm rủi ro, từ đó xác định mức SIL cần thiết.",
      "Once the risk is identified, the HAZOP/process hazard study (PHA) will set the requirement for "
      "risk reduction, thus define the required SIL Level.")
    FIG(3, F12.fig_f12_03())
    P("Cần kiểm chứng thêm các tiêu chí khác để đảm bảo SIF đáp ứng SIL yêu cầu, thường được chia "
      "thành các điểm sau:",
      "Additional criteria need to be verified to ensure the SIF meets the required SIL, and they "
      "are often divided into the following points:")
    B(["Toàn vẹn hệ thống: Mọi phần tử của SIF đều cần có khả năng được dùng ở mức SIL đã xác định.",
       "Ràng buộc kiến trúc: Khả năng chịu lỗi phần cứng (HFT) và dự phòng của kiến trúc cần tuân thủ "
       "các tiêu chuẩn an toàn chức năng hiện hành.",
       "Toàn vẹn ngẫu nhiên (PFDavg): Tỷ lệ hỏng của từng thiết bị sẽ được dùng để tính xác suất "
       "trung bình hỏng khi yêu cầu."],
      ["Systematic integrity: All elements of the SIF need to be capable being used for the defined "
       "SIL level.",
       "Architectural constraints: Hardware Fault Tolerance (HFT) and redundancy of the architecture "
       "need to comply with current functional safety standards",
       "Random integrity (PFDavg): The failure rates of the individual devices will be used to "
       "calculate the average probability of failure on demand."])

    # ------------------------------------------------------------ 12.5
    H("12.5 Xác suất hỏng khi yêu cầu",
      "12.5 Probability of Failure Upon Demand")
    P("Bằng cách hiểu các thành phần của hệ thống SIS có thể hỏng như thế nào, ta có thể tính xác "
      "suất hỏng khi yêu cầu (PFD). Có hai cách cơ bản để SIS hỏng. Cách thứ nhất thường được gọi là "
      "ngắt gây phiền nhiễu hoặc ngắt giả, thường dẫn đến việc dừng quy trình ngoài kế hoạch nhưng "
      "tương đối an toàn. Dù kiểu hỏng SIS này ít gây nguy hiểm, chi phí vận hành có thể rất lớn. Kiểu "
      "hỏng thứ hai không gây dừng quy trình hay ngắt gây phiền nhiễu. Thay vào đó, hỏng hóc vẫn "
      "không được phát hiện, cho phép quy trình tiếp tục vận hành một cách không an toàn và nguy "
      "hiểm. Nếu có yêu cầu khẩn cấp, hệ thống SIS sẽ không thể phản ứng đúng. Những hỏng hóc này "
      "được gọi là hỏng hóc tiềm ẩn hoặc ẩn giấu và góp phần vào xác suất (PFD) hệ thống hỏng một "
      "cách nguy hiểm khi có yêu cầu.",
      "By understanding how the components of the SIS system can fail, it is possible to calculate a "
      "probability of failure on demand (PFD). There are two basic ways for the SIS to fail. The "
      "first way is commonly called a nuisance or spurious trip, which usually results in an "
      "unplanned but relatively safe process shutdown. While there is minimal danger associated "
      "with this type of SIS failure, the operational costs can be enormous. The second type of "
      "failure does not cause a process shutdown or nuisance trip. Instead, the failure remains "
      "undetected, permitting continued process operation in an unsafe and dangerous manner. If an "
      "emergency demand occurred, the SIS system would be unable to respond properly. These failures "
      "are known as covert or hidden failures and contribute to the probability (PFD) of the system "
      "failing in a dangerous manner on demand.")
    P("PFD của hệ thống SIS là tổng PFD của từng phần tử trong hệ thống: PFDtotal bằng PFDsensor "
      "cộng PFDlogic solver cộng PFDfinal element.",
      "The PFD for the SIS system is the sum of PFDs for each element of the system: PFDtotal = "
      "PFDsensor + PFDlogic solver + PFDfinal element.")
    P("Để xác định PFD của từng phần tử, người phân tích cần dữ liệu tỷ lệ hỏng được ghi chép cho từng "
      "phần tử. Tỷ lệ hỏng (nguy hiểm) này được dùng cùng với số hạng khoảng cách kiểm tra (TI) để "
      "tính PFD. Chính khoảng cách kiểm tra này phản ánh thời gian trước khi một lỗi tiềm ẩn được "
      "phát hiện qua kiểm tra. Việc tăng khoảng cách kiểm tra tác động trực tiếp đến giá trị PFD theo "
      "cách tuyến tính; nghĩa là nếu bạn nhân đôi khoảng thời gian giữa các lần kiểm tra, bạn sẽ nhân "
      "đôi xác suất hỏng khi yêu cầu và làm cho việc đạt SIL mục tiêu khó gấp đôi.",
      "In order to determine the PFD of each element, the analyst needs documented failure rate data "
      "for each element. This failure rate (dangerous) is used in conjunction with the test interval "
      "(TI) term to calculate the PFD. It is this test interval that accounts for the length of time "
      "before a covert fault is discovered through testing. Increasing the test interval directly "
      "impacts the PFD value in a linear manner; i.e., if you double the interval between tests, you "
      "will double the probability for failure on demand, and make it twice as difficult to meet the "
      "target SIL.")
    P("Các tiêu chuẩn quản lý đối với hệ thống an toàn bằng dụng cụ quy định rằng người vận hành nhà "
      "máy phải xác định và ghi chép rằng thiết bị được thiết kế, bảo trì, kiểm tra, thử nghiệm và "
      "vận hành một cách an toàn. Do đó, điều bắt buộc là các thành phần này của hệ thống an toàn bằng "
      "dụng cụ phải được kiểm tra đủ thường xuyên để giảm PFD và đáp ứng SIL mục tiêu.",
      "The governing standards for safety instrumented systems state that plant operators must "
      "determine and document that equipment is designed, maintained, inspected, tested, and "
      "operated in a safe manner. Thus, it is imperative that these components of safety "
      "instrumented system be tested frequently enough to reduce the PFD and meet the target SIL.")
    FIG(4, F12.fig_f12_04())

    # ------------------------------------------------------------ 12.6
    H("12.6 Phần tử cuối, kiểm tra chứng minh và kỹ thuật kiểm tra hành trình một phần",
      "12.6 Final Elements, Proof Testing, and Partial Stroke Testing Techniques")
    P("Phần tử cuối gồm van, cơ cấu chấp hành và thiết bị đo của van. Tùy theo ứng dụng, van bi, van "
      "bướm hoặc van điều khiển được dùng cho dừng khẩn cấp (ESD), van xả áp (BDV), hoặc các mục đích "
      "khác trong SIS để đưa quy trình về trạng thái an toàn.",
      "Final elements consist of valves, actuators, and valve instrumentation. Depending on the "
      "application ball, butterfly, or control valves are used for emergency shutdown (ESD), "
      "blowdown valves (BDV), or other use in a SIS to take the process to a safe state.")
    P("Vì phần tử cuối chỉ là một phần của SIF, khó có thể xác nhận SIL yêu cầu nếu không xem xét "
      "cả phần khởi tạo và bộ giải logic như một phần của vòng. Dữ liệu thống kê có được từ ngành "
      "công nghiệp quy trình có thể dùng để ước tính mức tuân thủ SIL yêu cầu. Dữ liệu từ OREDA "
      "(Offshore and Onshore Reliability Data) liệt kê rằng nhiều tới 50% hỏng hóc trong một SIF có "
      "thể quy cho phần tử điều khiển cuối, như thể hiện trong Hình 12.4.",
      "As final elements are only part of the SIF, it is difficult to confirm the required SIL "
      "without considering the initiator and logic solver as part of the loop. Statistical data "
      "available from the process industries can be used to provide an estimation of compliance "
      "with the required SIL. Data from OREDA (Offshore and Onshore Reliability Data) lists that as "
      "many as 50% of failures within a SIF can be attributed to the final element, as shown in "
      "Figure 12.4.")
    P("Vì phần tử cuối chiếm 50% số hỏng hóc, điều quan trọng là chọn van đáp ứng điều kiện thiết kế "
      "sản phẩm, đáp ứng mục tiêu SIL yêu cầu và được kiểm tra định kỳ để đảm bảo chức năng. SIS phải "
      "được kiểm tra chức năng bằng các phép kiểm tra chứng minh (proof test) cho từng thiết bị theo "
      "chu kỳ, như xác định là cần thiết trong phân tích kiểm chứng SIL, nhằm duy trì mức SIL yêu cầu "
      "cho SIF trong suốt vòng đời của hệ thống lắp đặt. Một phép kiểm tra chứng minh cho phần tử cuối "
      "gồm kiểm tra bằng mắt và xác minh chức năng an toàn, bao gồm một hành trình van đầy đủ, và cũng "
      "có thể gồm xác minh thời gian an toàn và độ rò của van.",
      "As final elements account for 50% of the failures, it is important that valves are selected "
      "that meet product design conditions, meet the required SIL target, and are tested periodically "
      "to ensure functionality. The SIS must be functionally tested with proof tests of each device "
      "on a periodic basis, as determined necessary during SIL verification analysis to maintain the "
      "required SIL level for the SIF, throughout the lifecycle of the installation. A proof test for "
      "a final element would include a visual inspection and verification of safety function, which "
      "includes a full valve stroke and may also include a verification of safety time and valve "
      "leakage.")

    # ------------------------------------------------------------ 12.7
    H("12.7 Kiểm tra hành trình một phần", "12.7 Partial Stroke Testing")
    P("Đôi khi, khoảng thời gian giữa các lần kiểm tra chứng minh không khớp lý tưởng với các kỳ dừng "
      "máy hoặc bảo trì theo kế hoạch. Để tránh phải dừng quy trình chỉ để kiểm tra, có thể dùng đường "
      "vòng qua phần tử cuối; tuy nhiên, kiểm tra bằng đường vòng có thể để quy trình không được bảo "
      "vệ trong trường hợp có yêu cầu an toàn. Một lựa chọn khác là kéo dài khoảng cách kiểm tra chứng "
      "minh bằng cách dùng kiểm tra hành trình một phần (PST). Kiểm tra hành trình một phần cho van "
      "vận hành một phần trong tổng hành trình của nó để xác minh van không bị kẹt và phát hiện các "
      "chế hỏng nguy hiểm khác vốn không được phát hiện, chẳng hạn kẹt thân van, vấn đề về đệm van, "
      "vấn đề về đường dẫn khí của cơ cấu chấp hành, hoặc các chế hỏng khác có thể ngăn van chuyển "
      "đến vị trí an toàn khi có yêu cầu an toàn.",
      "At times, the duration between proof testing is not ideally aligned with scheduled shutdown "
      "or maintenance periods. To avoid shutting down the process for testing, a bypass around the "
      "final element can be used; however, testing with a bypass potentially leaves the process "
      "unprotected in the case of safety demand. An alternate option is to extend the proof test "
      "intervals by utilizing partial stroke testing (PST). Partial stroke testing exercises the "
      "valve a portion of its total travel to verify that the valve is not stuck and to uncover other "
      "otherwise dangerous undetected failure modes such as valve shaft sticking, valve packing "
      "issues, actuator air line issues, or other modes that could prevent the valve from moving to "
      "its safe position in the case of a safety demand.")
    P("Thời gian có thể kéo dài khoảng cách kiểm tra chứng minh nhờ kiểm tra hành trình một phần thay "
      "đổi tùy theo mục tiêu SIL, tần suất kiểm tra và mức độ bao phủ chẩn đoán (tỷ lệ giữa tỷ lệ hỏng "
      "được phát hiện và tổng tỷ lệ hỏng).",
      "The amount of time a proof test interval can be extended using partial stroke testing varies "
      "depending on SIL target, test frequency, and amount of diagnostic coverage (a ratio between "
      "the failure rates detected to the total failure rate).")

    # ------------------------------------------------------------ 12.8
    H("12.8 Phương pháp kiểm tra trực tuyến cho phần tử cuối",
      "12.8 Online Testing Methods for the Final Element")
    P("Có thể kiểm tra van bằng cách lắp một van vòng qua mỗi van an toàn. Khi đưa đường vòng vào hoạt "
      "động, van an toàn có thể được kiểm tra hành trình đầy đủ mà không phải dừng quy trình.",
      "Valve testing can be done by installing a bypass valve around each safety valve. By placing "
      "the bypass in service, the safety valve can be full stroke tested without shutting down the "
      "process.")
    P("Trong nỗ lực loại bỏ các vấn đề vận hành, kinh tế và quy định liên quan đến kiểm tra bằng đường "
      "vòng, các phương pháp khác đã được phát triển.",
      "In an attempt to eliminate the operational, economic, and regulatory problems associated with "
      "bypass testing, other methods were developed.")
    P("Các phương pháp hạn chế hành trình cơ học dùng một thiết bị cơ khí như chốt, vòng cổ thân van, "
      "kích tay van, v.v., để giới hạn hành trình van ở mức 15% hoặc ít hơn của toàn bộ hành trình.",
      "Mechanical limiting travel methods involve the use of some mechanical device such as a pin, a "
      "valve stem collar, a valve hand jack, etc. that will limit the valve travel to 15% or less of "
      "the valve stroke.")
    P("Phương pháp bảng kiểm tra khí nén cũng dùng một chốt được cài trước khi có thể bắt đầu phép "
      "kiểm tra hành trình một phần.",
      "The pneumatic test panels method also uses a pin to engage before partial travel test could "
      "be initiated.")
    P("Các cách kiểm tra trực tuyến này có nhiều nhược điểm. Một nhược điểm lớn là chức năng dừng an "
      "toàn không sẵn sàng trong thời gian kiểm tra. Thực tế, quy trình hoàn toàn không được bảo vệ "
      "trong khi kiểm tra đang diễn ra, và với một số khu vực và ngành thì loại kiểm tra này sẽ không "
      "được chấp nhận. Cũng đáng lo ngại là khả năng van an toàn bị để lại nhầm ở vị trí vòng sau khi "
      "kiểm tra hoặc chốt khóa cơ học không được tháo ra sau khi kiểm tra kết thúc. Điều này sẽ để quy "
      "trình hoàn toàn không được bảo vệ cho đến khi phát hiện ra sai sót. Thêm vào đó, tất cả các "
      "phương pháp kiểm tra này đều có nguy cơ rõ rệt gây ngắt dừng giả do chính hoạt động kiểm tra. "
      "Một nhược điểm nữa là quá trình kiểm tra phải được khởi tạo thủ công tại hiện trường và bản "
      "thân các phép thử rất tốn nhân công và dễ mắc lỗi.",
      "These online testing approaches have a number of disadvantages. A major drawback to these "
      "methods is that the safety shutdown function is not available during the test period. In "
      "fact, the process is left totally unprotected while the test is in progress, and for some "
      "areas and industries this type of testing will not be accepted. Also of concern is the "
      "possibility of the safety valve being inadvertently left in the bypass position after testing "
      "or the mechanical lock or pin is not removed after testing is complete. This would leave the "
      "process totally unprotected until such time as the error is discovered. In addition, these "
      "test methods all have a definite risk of spurious shutdown trips caused by testing. Another "
      "drawback is that the testing process must be manually initiated in the field and the tests "
      "themselves are extremely manpower intensive and subject to error.")

    # ------------------------------------------------------------ 12.9
    H("12.9 Sử dụng bộ điều khiển van số để kiểm tra hành trình một phần",
      "12.9 Digital Valve Controller Use for Partial Stroke Testing")
    P("Bộ điều khiển van số là thiết bị truyền thông, dựa trên vi xử lý, chuyển đổi tín hiệu dòng "
      "thành tín hiệu khí nén, có khả năng logic nội bộ. Ngoài chức năng truyền thống là chuyển tín "
      "hiệu dòng thành tín hiệu áp suất để vận hành van, các bộ điều khiển van số này dùng giao thức "
      "truyền thông HART để cung cấp quyền truy cập dễ dàng vào thông tin then chốt cho kiểm tra an "
      "toàn. Bộ điều khiển van số nhận phản hồi về vị trí hành trình của van cùng áp suất khí cấp và "
      "áp suất khí của cơ cấu chấp hành. Điều này cho phép bộ điều khiển van số chẩn đoán tình trạng "
      "và hoạt động của chính nó cũng như của van và cơ cấu chấp hành mà nó được lắp vào.",
      "Digital valve controllers are communicating, microprocessor-based current-to-pneumatic "
      "instruments with internal logic capability. In addition to the traditional function of "
      "converting a current signal to a pressure signal to operate the valve, these digital valve "
      "controllers use HART communications protocol to give easy access to information critical to "
      "safety testing. The digital valve controller receives feedback of the valve travel position "
      "plus supply and actuator pneumatic pressures. This allows the digital valve controller to "
      "diagnose the health and operation of itself and the valve and actuator to which it is "
      "mounted.")
    P("Kiểm tra hành trình một phần xác nhận van đang hoạt động mà không làm gián đoạn quy trình. Vì "
      "toàn bộ quy trình kiểm tra có thể được lập trình vào bộ điều khiển van số, kiểm tra hành trình "
      "một phần có thể được thực hiện tự động. Điều này cho phép khoảng cách kiểm tra ngắn tới mức "
      "cần thiết (hàng giờ, hàng ngày, hàng tuần, v.v.) để đáp ứng các giá trị SIL mục tiêu. Người "
      "vận hành có thể khởi tạo kiểm tra thủ công bằng một lần nhấn nút đơn giản, tuy nhiên bản thân "
      "trình tự kiểm tra hoàn toàn tự động, từ đó loại bỏ mọi sai sót và ngắt gây phiền nhiễu có thể "
      "xảy ra, cũng như chi phí nhân công của các sơ đồ kiểm tra thông thường. Nếu có yêu cầu an toàn "
      "trong lúc kiểm tra hành trình một phần, phép kiểm tra sẽ bị hủy và bộ điều khiển van số sẽ "
      "đưa van về trạng thái an toàn.",
      "Partial stroke testing confirms the valve is working without disturbing the process. Since "
      "the entire test procedure can be programmed into the digital valve controller, partial stroke "
      "testing can be performed automatically. This allows the test interval to be as short as "
      "necessary (hourly, daily, weekly, etc.) to meet the target SIL values. The operator can "
      "manually initiate the test by a simple button push, however the testing sequence itself is "
      "completely automatic, thereby eliminating any errors and possible nuisance trips, and the "
      "labor capital cost of conventional testing schemes. If there is a safety demand during the "
      "partial stroke test, the test will be aborted and the digital valve controller will drive the "
      "valve to its safe state.")
    P("Thông thường, phép kiểm tra hành trình một phần dịch chuyển van 10% so với vị trí ban đầu nhưng "
      "có thể tới 30% nếu được phép theo quy định an toàn của nhà máy. Dù kiểm tra hành trình một phần "
      "không loại bỏ nhu cầu kiểm tra hành trình đầy đủ (cần kiểm tra hành trình đầy đủ để kiểm tra "
      "đế van, v.v.), nó làm giảm tần suất kiểm tra hành trình đầy đủ cần thiết đến mức "
      "nhiều khả năng có thể thực hiện trong kỳ đại tu nhà máy.",
      "Typically, the partial stroke test moves the valve 10% from its original position but can be "
      "up to 30% if allowed by plant safety guidelines. Although partial stroke testing does not "
      "eliminate the need for full stroke testing (full stroke testing is required to check valve "
      "seating, etc.) it does reduce the required full stroke testing frequency to the point where "
      "it can most likely be tested during plant turnaround.")
    P("Việc thêm bộ điều khiển van số vào hệ thống an toàn bằng dụng cụ có thể giảm chi phí thiết bị "
      "cơ bản, thời gian kiểm tra và nhu cầu nhân công bằng cách loại bỏ nhu cầu dùng bảng kiểm tra "
      "khí nén đắt tiền và nhân sự có kỹ năng để kiểm tra. Dùng bộ điều khiển van số có thể cung cấp "
      "tài liệu đầy đủ về bất kỳ sự kiện khẩn cấp nào cũng như tài liệu về mọi lần kiểm tra, có thể "
      "được cung cấp cho công ty bảo hiểm làm bằng chứng kiểm tra. Nó cũng cho phép cấu hình kiểm tra "
      "từ xa, giúp tiết kiệm thời gian bằng cách giảm yêu cầu đi lại đến hiện trường để kiểm tra bảo "
      "trì. An toàn của nhân viên nhà máy cũng có thể được tăng lên bằng cách loại bỏ nhu cầu nhân "
      "viên phải đến hiện trường để kiểm tra.",
      "Adding a digital valve controller to a safety instrumented system can reduce base equipment "
      "cost, testing time, and manpower requirements by eliminating the need for expensive pneumatic "
      "test panels and skilled personnel for testing. Using a digital valve controller can provide "
      "complete documentation of any emergency event as well as documentation of all testing, which "
      "could be made available to insurance companies as proof of testing. It also allows for "
      "configuration of remote testing, which can save time by reducing the requirement for "
      "maintenance inspection trips to the field. The safety of plant personnel can also be "
      "increased by eliminating the need for plant personnel to go to the field for testing.")

    # ------------------------------------------------------------ 12.10
    H("12.10 Hệ thống bảo vệ áp suất toàn vẹn cao (HIPPS)",
      "12.10 High-Integrity Pressure Protection System (HIPPS)")
    P("Các hệ thống bảo vệ áp suất toàn vẹn cao (HIPPS) là một phần của hệ thống an toàn bằng dụng cụ "
      "và được thiết kế để ngăn quá áp. So với các hệ thống xả áp thông thường như dùng van xả hoặc "
      "van an toàn cơ khí, HIPPS hoạt động bằng cách ngắt nguồn và giữ áp lực ở phía thượng nguồn của "
      "hệ thống, từ đó tạo rào chắn giữa phía áp suất cao và phía áp suất thấp của một cơ sở sản "
      "xuất. Việc đóng kín sẽ ngăn rò rỉ phía hạ nguồn và loại bỏ phát thải thoát hơi. Theo nghĩa đó, "
      "HIPPS được xem là «rào chắn cuối cùng».",
      "High-integrity pressure protection systems (HIPPS) are part of the safety instrumented "
      "system and designed to prevent overpressure. Compared with conventional systems for pressure "
      "relief like the use of mechanical relief or safety valves, HIPPS work by shutting off the "
      "source and capturing the pressure in the upstream side of the system, thus providing a "
      "barrier between the high-pressure and low-pressure sides of a production facility. The tight "
      "shutoff will prevent downstream leakage and eliminate fugitive emissions. In this regard, "
      "HIPPS are seen as the “last line of defense.”")
    P("HIPPS mang lại giải pháp vừa kinh tế vừa thân thiện với môi trường so với các hệ thống xả áp "
      "thông thường. Hình 12.5 cho thấy một HIPPS điển hình trong cấu hình được thiết lập để đáp ứng "
      "SIL 3.",
      "HIPPS offer an economical as well as environmental friendly solution compared with "
      "conventional relief systems. Figure 12.5 shows a typical HIPPS in a configuration set to "
      "meet SIL 3.")

    # ------------------------------------------------------------ 12.11
    H("12.11 Chức năng của HIPPS", "12.11 Functionality of the HIPPS")
    P("Giống như SIF, một HIPPS thường gồm các thiết bị và chức năng sau:",
      "Like the SIF, a HIPPS typically consists of the following devices and functionality:")
    P("Cảm biến áp suất: Ba cảm biến áp suất riêng biệt ở phía thượng nguồn của HIPPS, được thiết lập "
      "theo cấu trúc bỏ phiếu 2 trên 3 (2oo3), sẽ mang lại cho người vận hành khả năng sẵn có của hệ "
      "thống và độ tin cậy để hỗ trợ SIF.",
      "Pressure Sensors: Three individual pressure sensors on the upstream side of the HIPPS, set in "
      "a voting structure of 2 out of 3 (2oo3), will give the operator availability of the system + "
      "reliability to support the SIF.")
    P("Bộ giải logic: Trong trường hợp hai trong ba cảm biến (2oo3) đo áp suất cao hơn mức quy định "
      "hoặc cho phép, bộ giải logic sẽ dừng hai phần tử cuối và một cảnh báo được gửi về phòng điều "
      "khiển.",
      "Logic Solver: In the case that two out of three (2oo3) sensors measure a pressure higher than "
      "defined/allowed, the logic solver will shut down the two final elements and an alarm is sent "
      "to the control room.")
    P("Phần tử cuối: Hai van cô lập mắc nối tiếp (sắp xếp 1oo2) để cung cấp dự phòng và tăng cường "
      "toàn vẹn an toàn.",
      "Final Elements: Two isolation valves, in series (1oo2 arrangement) to provide redundancy and "
      "enhanced safety integrity.")

    # ------------------------------------------------------------ 12.12
    H("12.12 Yêu cầu kiểm tra", "12.12 Testing Requirements")
    P("Để đảm bảo HIPPS đáp ứng SIL yêu cầu trong suốt vòng đời an toàn của hệ thống lắp đặt, cần "
      "thực hiện kiểm tra trên các phần tử khác nhau:",
      "To ensure the HIPPS will meet the required SIL throughout the safety lifecycle of the "
      "installation, testing will need to be done on the different elements:")
    P("Cảm biến áp suất: Cảm biến áp suất cần được đưa ra khỏi dịch vụ để kiểm tra, nhưng vì cấu hình "
      "là 2oo3, có thể cô lập 1 cảm biến để kiểm tra và vẫn duy trì mức dự phòng như cũ với điều kiện "
      "thay đổi bỏ phiếu trong bộ giải logic từ 2oo3 sang 1oo2. Điều này thường được thực hiện bởi hệ "
      "thống liên khóa, gửi tín hiệu tới bộ giải logic rằng một cảm biến đang được kiểm tra.",
      "Pressure Sensor: Pressure sensors will need to be taken out of service for testing, but as "
      "the configuration is 2oo3, it is possible to isolate 1 sensor for testing and maintain the "
      "same redundancy provided the voting in the logic solver is changed from 2oo3 to 1oo2. This is "
      "often done by an interlock system, providing a signal to the logic solver that a sensor is "
      "out for testing.")
    P("Bộ giải logic: Bộ giải logic thường làm việc với bộ xử lý kép và liên tục chạy tự chẩn đoán. "
      "Nếu phát hiện lỗi, nó có thể được thiết lập để dừng phần tử cuối hoặc chuyển sang bộ giải logic "
      "dự phòng.",
      "Logic Solver: Logic solvers re often working with a dual processor and constantly running "
      "self-diagnostics. Should a failure be detected, it can be set to either shut down the final "
      "element or shift to a redundant logic solver.")
    P("Phần tử điều khiển cuối: Các tiêu chuẩn quản lý đối với hệ thống an toàn bằng dụng cụ quy định "
      "rằng người vận hành nhà máy phải xác định và ghi chép rằng thiết bị được thiết kế, bảo trì, "
      "kiểm tra, thử nghiệm và vận hành một cách an toàn. Do đó, điều bắt buộc là các thành phần này "
      "của hệ thống an toàn bằng dụng cụ phải được kiểm tra đủ thường xuyên để giảm PFD và đáp ứng "
      "SIL mục tiêu: Cần thực hiện kiểm tra hành trình đầy đủ hoặc kiểm tra chứng minh theo một tập "
      "khoảng cách nhất định, nhưng do bản chất của phép thử, việc này cần được thực hiện khi thiết "
      "bị ngừng dịch vụ. Để kéo dài khoảng thời gian giữa các lần kiểm tra chứng minh, có thể dùng "
      "kiểm tra trực tuyến như kiểm tra hành trình một phần để phát hiện một số lượng đáng kể hỏng "
      "hóc, đồng thời cung cấp chẩn đoán dự báo, cho phép người vận hành hành động.",
      "Final Control Element: The governing standards for safety instrumented systems state that "
      "plant operators must determine and document that equipment is designed, maintained, "
      "inspected, tested, and operated in a safe manner. Thus it is imperative that these components "
      "of the safety instrumented system be tested frequently enough to reduce the PFD and meet the "
      "target SIL: A full stroke or proof test will need to be done with a set of intervals, but due "
      "to the nature of the test, this will need to be done out of service. To extend the period "
      "between the proof test, online testing like partial stroke testing can be used to detect a "
      "fair amount of failures plus give predictive diagnostic, allowing an operator to take action.")
    FIG(5, F12.fig_f12_05())

    # ------------------------------------------------------------ source notes
    H("Ghi chú về nguồn", "Source notes", h3)
    N(source_notes("vi"), source_notes("en"))
    P("Chương 12 chiếm tr. 250–259 của bản in (10 trang) trong Emerson, Control Valve Handbook, ấn "
      "bản 6 (2020). Nội dung gồm mười hai mục 12.1–12.12, từ các lớp bảo vệ, thành phần của SIS, "
      "tiêu chuẩn an toàn và mức toàn vẹn an toàn đến PFDavg, thử nghiệm van, bộ điều khiển van số và "
      "HIPPS. Năm hình được vẽ lại dạng vector và đặt theo thứ tự số tại vị trí văn bản hợp lý.",
      "Chapter 12 occupies printed pp. 250-259 (10 pages) of Emerson, Control Valve Handbook, 6th "
      "edition (2020). It contains twelve sections, 12.1-12.12, from layers of protection, SIS "
      "components, safety standards and safety integrity levels to PFDavg, valve testing, digital "
      "valve controllers and HIPPS. The five numbered figures are redrawn as vectors and placed in "
      "numbered order at their logical prose points.")
    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2020 Emerson "
      "Flow Controls.</i>",
      "<i>This is an unofficial translation for study purposes. Original content © 2020 Emerson "
      "Flow Controls.</i>")
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
