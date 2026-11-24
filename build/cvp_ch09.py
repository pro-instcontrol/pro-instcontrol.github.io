# -*- coding: utf-8 -*-
"""Book 7, Chapter 9 - Why Most People Choose "Equal Percentage" as a Flow
Characteristic (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
57-65 (PDF pp. 63-71). Four figures, four unnumbered numeric tabulations,
five unnumbered equations, two footnotes, and three references.
"""
from cvp_common import eq, fig, h2, h3, note, ol, p, refs, table, ul
import cvpfig9 as F

PAGES_SRC = 9
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Why Most People Choose “Equal Percentage” as a Flow Characteristic"
TITLE_VI = "Vì sao hầu hết chọn đặc tính lưu lượng “phần trăm bằng nhau”"


def note_terms(lang):
    """A one-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 9.</b> đặc tính lưu lượng vốn có (inherent flow "
                "characteristic) · đặc tính lưu lượng lắp đặt (installed flow characteristic) "
                "· hệ số lưu lượng Cv · hành trình van (valve travel) · tuyến tính (linear) · "
                "phần trăm bằng nhau (equal percentage) · mở nhanh (quick-opening) · dòng "
                "chảy hở (clearance flow) · nút van (plug) · đế van / bệ van / mặt tựa của "
                "van (seat, seat ring) · lỗ tiết lưu (orifice) · tiết lưu (throttling) · "
                "độ giảm áp (ΔP) · hóa hơi (flashing) · xâm thực (cavitation) · dòng âm tốc "
                "(sonic flow) · hệ số phục hồi áp suất chất lỏng F<sub>L</sub> · dòng bị "
                "nghẽn (choked flow) · đoạn thu nhỏ (reducers) · tổn thất cột áp (head loss) "
                "· độ lợi van (valve gain) · bộ điều khiển PID · dải tỷ lệ (proportional "
                "band) · độ phạm vi / độ giảm tải (rangeability / turndown) · van chọn quá "
                "lớn (oversized) · vùng chết (deadband) · vùng nguy hiểm (danger zone) · "
                "bộ điều khiển tự chỉnh (self-tuning controller) · van điều khiển quay "
                "(rotary control valve) · cam định tính (characterized cam) · bộ định vị "
                "van (positioner) · hằng số thời gian (time constant) · bồn chứa · bơm ly "
                "tâm · cột áp tĩnh (static head) · áp suất ngược (backpressure) · trọng "
                "riêng (specific gravity) · van bướm góc (angle-seating butterfly valve) "
                "· van lồng (cage valve) · bộ lót phần trăm bằng nhau (equal-percentage "
                "trim) · bộ chuyển đổi số–tương tự (D/A converter) · tín hiệu đầu ra.")
    return ("<b>Key terms.</b> inherent flow characteristic · installed flow characteristic "
            "· flow coefficient Cv · valve travel · linear · equal percentage · quick-opening "
            "· clearance flow · plug · seat · seat ring · throttling / throttling orifice · "
            "pressure drop (ΔP) · flashing · cavitation · sonic flow · liquid pressure "
            "recovery factor F<sub>L</sub> · choked flow · reducers · head loss · valve gain "
            "· PID controller · proportional band · rangeability / turndown · oversized "
            "valve · deadband · danger zone · self-tuning controller · rotary control valve "
            "· characterized cam · valve positioner · time constant · storage tank · "
            "centrifugal pump · static head · backpressure · specific gravity · angle-seating "
            "butterfly valve · cage valve · equal-percentage trim · digital-to-analog "
            "converter · output signal.")


def body_vi():
    b = []
    b.append(h2("Đặc tính vốn có: Cv theo hành trình",
                "The inherent characteristic: Cv versus travel"))
    b.append(p("Một trong những câu hỏi khó nhất là: van của tôi nên có đặc tính lưu lượng "
               "vốn có nào? Trước hết, cần định nghĩa: đặc tính lưu lượng vốn có là mối quan "
               "hệ giữa hệ số lưu lượng Cv và hành trình van. Nếu đặc tính tuyến tính "
               "(linear), thì về mặt lý thuyết bạn nhận được cùng một lượng tăng Cv cho một "
               "lượng tăng hành trình bằng nhau. Giá trị điển hình là tăng 9,8% Cv cho mỗi "
               "10% tăng hành trình. Ồ! Bạn có thể thắc mắc: sao không phải 10% Cv? Nguyên "
               "nhân là ở, chẳng hạn, 1% hành trình, lưu lượng đã chiếm 2% lưu lượng cực "
               "đại do dòng chảy hở (clearance flow) giữa nút van và bệ van (seat ring). Vì "
               "vậy, mức tăng chỉ là 9,8% cho mỗi bước 10% (xem Hình 9-1)."))
    b.append(p("Đối với đặc tính phần trăm bằng nhau (equal percentage), mức tăng Cv điển "
               "hình là khoảng 43% cao hơn số liệu trước đó cho mỗi 10% hành trình; ví dụ, ở "
               "20% hành trình, số Cv bằng 143% số Cv ở 10% hành trình. Giả sử Cv ở 40% "
               "hành trình là 10, thì ở 50% hành trình là 14,3 và ở 60% hành trình là 20,5, "
               "v.v. Điều này có nghĩa là lưu lượng tăng theo hàm mũ thay vì tuyến tính. "
               "Đặc tính này thường được biểu diễn bằng một đường thẳng trên giấy log-bán "
               "log (semi-logarithmic)."))
    b.append(p("Cuối cùng là đặc tính mở nhanh (quick-opening), trong đó nút van không còn "
               "được tạo hình mà thường là một đĩa phẳng. Ở đây, mức tăng Cv xấp xỉ tuyến "
               "tính cho đến hành trình tương đương một phần tư đường kính lỗ tiết lưu "
               "(orifice). Sau đó, về mặt thực tế, lưu lượng không còn tăng nữa. Bạn có thể "
               "hoàn toàn bỏ qua đặc tính này đối với các van điều khiển tiết lưu."))
    b.append(fig(1, F.fig_f91()))

    b.append(h2("Cảnh báo: đường cong vốn có chỉ đúng khi ΔP không đổi",
                "Caution: inherent curves apply only at constant ΔP"))
    b.append(p("Sau khi van được lắp vào một hệ thống ống dẫn, các đặc tính lưu lượng nêu "
               "trên chỉ áp dụng được khi:"))
    b.append(ul([
        "độ giảm áp không đổi khi lưu lượng thay đổi;",
        "không có sự khởi phát của hóa hơi (flashing), xâm thực (cavitation) hoặc dòng âm "
        "tốc (sonic flow) ở một số điều kiện lưu lượng nhất định (rất có thể do sự thay đổi "
        "hệ số F<sub>L</sub> của van khi hành trình thay đổi);",
        "van không được lắp giữa hai đoạn thu nhỏ (reducers).",
    ]))
    b.append(p("Điều kiện lý tưởng ngăn không cho các tình huống đó xảy ra chỉ có trong "
               "phòng thí nghiệm dòng chảy của nhà sản xuất. Để xử lý thực tế, ta phải làm "
               "việc với đặc tính lưu lượng lắp đặt (installed flow characteristic). Đây là "
               "mối quan hệ giữa lưu lượng chảy và hành trình van, có tính đến sự khác biệt "
               "về độ giảm áp giữa lưu lượng cực đại và cực tiểu [1]; khả năng bị nghẽn "
               "dòng (choked flow) dọc theo đường ống; và sự méo mó mà tổn thất cột áp ở "
               "đoạn thu nhỏ gây ra cho đặc tính lưu lượng vốn có của van. Chính đặc tính "
               "lắp đặt này cuối cùng mới ảnh hưởng đến độ ổn định của bộ điều khiển."))

    b.append(h2("Điều khiển PID và độ lợi không đổi",
                "PID control and constant gain"))
    b.append(p("Cài đặt lý tưởng của bộ điều khiển tỷ lệ – tích phân – vi phân (PID) đòi "
               "hỏi một «độ lợi» (gain) không đổi từ phần tử điều khiển cuối. Độ lợi này là "
               "tốc độ thay đổi của lưu lượng (q) ứng với một sự thay đổi nhất định của tín "
               "hiệu. Thường thì hành trình van (h) tỷ lệ với tín hiệu (s). Điều đó làm cho "
               "δ(q)/δ(s) = hằng số đối với van lý tưởng."))
    b.append(p("Lý tưởng nhất, chúng ta muốn một đặc tính lưu lượng lắp đặt «tuyến tính» — "
               "tức là tăng khoảng 10% lưu lượng (không phải Cv) cho mỗi 10% tăng hành "
               "trình (điều này cho độ lợi lắp đặt của van bằng 1). Tuy nhiên, không có gì "
               "là lý tưởng, nên chúng ta phải thỏa hiệp. Theo quy tắc kinh nghiệm, độ lợi "
               "của van có thể thay đổi ±50% so với giá trị độ lợi không đổi trung bình "
               "(không nhất thiết phải bằng 1,0) mà không cần chỉnh lại cài đặt PID của bộ "
               "điều khiển. Nghĩa là, ví dụ, ta có thể chấp nhận một đặc tính lắp đặt mà ở "
               "một đầu lưu lượng thay đổi 5% cho mỗi 10% hành trình và ở đầu kia là 15% cho "
               "mỗi 10% hành trình. Điều này quả thực giúp cuộc sống dễ dàng hơn. Hình 9-2 "
               "cho thấy một ví dụ về đặc tính lưu lượng lắp đặt điển hình của van."))
    b.append(p("Ở đây, bộ điều khiển được chỉnh tại 20% lưu lượng hay 28% tín hiệu. Độ dốc "
               "của đường cong tại điểm đó (15% lưu lượng cho 20% tín hiệu) đóng vai trò là "
               "mốc tham chiếu. Trong trường hợp này, độ lợi thay đổi theo cả hai hướng. Do "
               "đó, các độ dốc «độ lợi không đổi» ở mức ±50% (tức 1,5 và 0,5) xác định các "
               "giới hạn, chồng lên những thay đổi độ lợi của van là ±50% so với cài đặt "
               "ban đầu của bộ điều khiển, cho thấy giới hạn của hiệu suất điều khiển ổn "
               "định dự kiến. Có thể cần chỉnh lại bộ điều khiển nếu dải lưu lượng vượt quá "
               "các giới hạn đã cho.<sup>1</sup> Chú thích của Hình 9-2 mô tả van có độ lợi "
               "không đổi 0,75 với độ ổn định điều khiển tốt; hai mốc đã nêu là 10% lưu "
               "lượng (8% tín hiệu) và 57% lưu lượng (78% tín hiệu)."))
    b.append(note("<b>Chú thích 1.</b> Chuyển dải tỷ lệ (proportional band) của bộ điều "
                  "khiển về 50% nếu độ lợi trung bình vào khoảng 2, chẳng hạn."))
    b.append(fig(2, F.fig_f92()))

    b.append(h2("Quy tắc chọn đặc tính", "Rules for choosing the characteristic"))
    b.append(p("Dựa trên thông tin trong Hình 9-2, ta có thể rút ra các quy tắc sau."))
    b.append(ol([
        "Trước hết, hãy kiểm tra quá trình và xác định ΔP qua van ở lưu lượng tối thiểu yêu "
        "cầu và ΔP ở lưu lượng cực đại. Thiết lập tỷ lệ giữa hai giá trị này.",
        "Thứ hai, nếu tỷ lệ nhỏ hơn 2:1, hãy chọn đặc tính vốn có tuyến tính. Nếu tỷ lệ lớn "
        "hơn 2:1, hãy chọn nút van phần trăm bằng nhau.",
    ]))
    b.append(p("Đến đây là hết phần khoa học. Giờ hãy nhìn vào khía cạnh đời thường hơn của "
               "vấn đề. Như tôi đã nói, hầu hết các van đều được chọn quá lớn, chủ yếu do "
               "ước tính quá cao tổn thất áp suất đường ống — vốn làm giảm ΔP dùng để tính "
               "kích cỡ — và do dự phòng cho việc tăng sản lượng trong tương lai. Thường thì "
               "bạn chỉ dùng tới 40% Cv định mức của van ở lưu lượng cực đại. Một van tuyến "
               "tính sẽ mở khoảng 40% (chỉ dùng 40% dải tín hiệu của bộ điều khiển). Một van "
               "phần trăm bằng nhau thì lại ở khoảng 75% hành trình. Đâu sẽ gây ấn tượng "
               "thị giác tốt hơn với sếp của bạn? Đừng bận tâm rằng vùng chết (deadband) của "
               "van giờ được trải ra trên 75% dải tín hiệu thay vì chỉ 40%. Bạn đã đoán ra "
               "rồi: đó là van có nút phần trăm bằng nhau!"))

    b.append(h2("Ví dụ bộ trao đổi nhiệt", "Heat-exchanger example"))
    b.append(p("Hãy xét một lập luận khác. Giả sử lưu lượng chất lỏng qua bộ trao đổi nhiệt "
               "có thể thay đổi 3:1 và ΔP tương ứng qua van thường tỷ lệ với bình phương "
               "lưu lượng, tức là gấp chín lần ΔP ở một phần ba lưu lượng. Độ phạm vi "
               "(rangeability), hay độ giảm tải (turndown) — tỷ lệ giữa Cv cực đại và Cv cực "
               "tiểu — khi đó là [1/(1)<sup>1/2</sup>]/[0,333/(9)<sup>1/2</sup>] = 1/0,111 "
               "hay 9:1. Chia 40% Cv định mức ở lưu lượng cực đại (xem ở trên) cho 9, ta "
               "được 4,4% Cv định mức ở lưu lượng cực tiểu."))
    b.append(eq("[1/(1)<sup>1/2</sup>] / [0,333/(9)<sup>1/2</sup>] = 1 / 0,111 = 9:1", ""))
    b.append(p("Đối với van có đặc tính tuyến tính, điều này xảy ra ở khoảng 3% hành trình, "
               "tức là trong «vùng nguy hiểm» (dưới 5% hành trình), nơi nút van có thể va "
               "vào đế van (seat) sau một dao động nhỏ của bộ điều khiển. Ngược lại, van "
               "phần trăm bằng nhau có khoảng 14% hành trình ở lưu lượng cực tiểu! Đây là "
               "những lập luận bạn nên ghi nhớ."))

    b.append(h2("Bộ điều khiển tự chỉnh và đường cong tín hiệu lập trình được",
                "Self-tuning controllers and programmable output curves"))
    b.append(p("Với sự có mặt của các bộ điều khiển tự chỉnh (self-tuning) và các chip máy "
               "tính có thể thay đổi hình dạng của đường cong tín hiệu đầu ra gửi tới van, "
               "câu hỏi chọn đặc tính lưu lượng vốn có nào trở nên ít quan trọng hơn. Hãy "
               "nhớ rằng hầu hết các van điều khiển quay (rotary) có đặc tính vốn có «tự "
               "nhiên» không thể xếp vào một trong hai định nghĩa kinh điển nào, thế nhưng "
               "tất cả chúng dường như đều làm việc tốt."))
    b.append(p("Điều đó chứng minh mức độ «dễ tính» của hầu hết các vòng điều khiển. Hãy nhớ "
               "rằng bất kỳ đặc tính lưu lượng nào cũng là tuyến tính khi nhìn qua kính lúp. "
               "Đối với các quá trình liên tục mà lưu lượng không thay đổi quá 20%, sự thay "
               "đổi độ lợi là dưới 2:1 bất kể loại đặc tính vốn có, nên bạn cũng đành chọn "
               "phần trăm bằng nhau vì những ưu điểm đã nêu ở trên."))

    b.append(h2("Cam định tính trong bộ định vị", "Characterized cams in positioners"))
    b.append(p("Một lời cuối cùng về việc dùng cam định tính (characterized cams) trong các "
               "bộ định vị (positioner) gắn với van điều khiển quay. Chúng chỉ có ích hạn "
               "chế. Thứ nhất, nếu van có đặc tính vốn có gần tuyến tính, thì 4% Cv vẫn chỉ "
               "là 3% hành trình, bất chấp tín hiệu đầu vào 14% mà cam phần trăm bằng nhau "
               "yêu cầu. Thứ hai, mối quan hệ đã chỉnh sửa giữa hành trình và tín hiệu chỉ "
               "đúng trong điều kiện tĩnh; nghĩa là nó chỉ làm việc với các quá trình có "
               "hằng số thời gian lớn như điều khiển nhiệt độ. Cuối cùng, cam định tính "
               "không chính xác và khó chỉnh."))
    b.append(p("Nếu quá trình nhanh, bạn sẽ có một van điều khiển với hằng số thời gian "
               "thay đổi theo hành trình, và điều đó có thể gây rối loạn nghiêm trọng cho độ "
               "ổn định của vòng điều khiển. Tại sao? Vì nếu bạn dùng cam phần trăm bằng nhau "
               "để chuyển đổi (chẳng hạn) đặc tính vốn có tuyến tính của van, bộ truyền động "
               "phải dịch chuyển khoảng 21% hành trình định mức khi tín hiệu đổi từ 90% xuống "
               "80%, nhưng chỉ 1,6% hành trình khi tín hiệu đổi từ 20% xuống 10%. Nói cách "
               "khác, van mất nhiều thời gian gấp 13 lần để di chuyển ở đầu trên của dải tín "
               "hiệu so với ở đầu dưới! Điều này có thể làm sai lệch đáng kể hằng số thời "
               "gian của vòng quá trình. Vì vậy, tránh dùng cam cho điều khiển áp suất hoặc "
               "lưu lượng (các vòng nhanh)."))

    b.append(h2("Cách tính đặc tính lưu lượng «lắp đặt»",
                "How to Calculate the “Installed” Flow Characteristic"))
    b.append(p("Trước khi ký phiếu mua hàng cho một van điều khiển cụ thể, bạn có thể muốn "
               "biết liệu bộ điều khiển của mình có giữ ổn định trong một vòng mà lưu lượng "
               "có thể thay đổi trên dải rộng, với tiêu chí chỉ cho phép thay đổi độ lợi van "
               "tối đa ±50% như đã nêu ở trên hay không. Tuy nhiên, điều này không thể làm "
               "được nếu chưa tính toán hoặc vẽ đặc tính lưu lượng lắp đặt của tổ hợp van và "
               "hệ thống đường ống; khi hoàn thành, nó phải trông giống như đường cong trong "
               "Hình 9-2."))
    b.append(p("Giả sử ta có một hệ thống dòng chảy chất lỏng gồm bồn chứa, bơm ly tâm, van "
               "điều khiển, hơn 20 feet ống 6 inch, bốn cút (elbows) và một bình công nghệ, "
               "như ví dụ trong Hình 9-3 [2] (hình do Jon Monsen cung cấp)."))
    b.append(fig(3, F.fig_f93()))
    b.append(p("Để thực hiện công việc, ta cần các thông tin sau."))
    b.append(ul([
        "Lưu lượng cực đại và cực tiểu, lần lượt là 1250 và 250 gpm.",
        "Đặc tính bơm (đã đổi từ feet sang psi), do nhà sản xuất cung cấp (xem bảng dưới "
        "đây).",
        "Tổn thất ma sát trong ống và các cút, tính là 28 psi ở lưu lượng 1250 gpm. Nếu "
        "không có vấn đề về độ nhớt hoặc hóa hơi (flashing), ta có thể giả định tổn thất ma "
        "sát tỷ lệ với bình phương lưu lượng, tức là ΔP<sub>ống</sub> = 28 psi/(gpm/1250 "
        "gpm)²; như trong bảng dưới đây.",
        "Thay đổi cột áp tĩnh (chênh lệch độ cao) từ đầu hút bơm đến bình công nghệ (đã đổi "
        "từ feet sang psi), cho là 23 psi (không đổi).",
        "Áp suất ngược (backpressure) trong bình công nghệ, cho là 52 psig (không đổi).",
    ]))
    b.append(table(["gpm", "1250", "1050", "850", "650", "450", "250"],
                   [["ΔP<sub>ống</sub> (psi)", "28", "19,8", "12,9", "7,6", "3,6", "1,1"],
                    ["Cột áp bơm (psi)", "110", "121", "131", "140", "146", "150"]],
                   caption="Đặc tính bơm và tổn thất ma sát theo lưu lượng (theo bản in)."))
    b.append(p("Trước hết, tính độ giảm áp sẵn có qua van điều khiển ở lưu lượng cực đại "
               "(1250 gpm):"))
    b.append(eq("ΔP<sub>van</sub> = cột áp bơm − ΔP<sub>ống</sub> − cột áp tĩnh − áp suất "
                "ngược = 110 − 28 − 23 − 52 = 7 psi", ""))
    b.append(p("Theo số liệu công nghệ, trọng riêng (specific gravity) bằng 1,1. Giờ ta có "
               "thể tính Cv lớn nhất cần dùng theo Phương trình 5-1:"))
    b.append(eq("C<sub>v</sub> = 1250 / (7 / 1,1)<sup>0,5</sup> ≈ 496", ""))
    b.append(p("Vì không yêu cầu đóng kín (tight shutoff), và dựa trên các cân nhắc về độ "
               "phạm vi và chi phí, ta có thể chọn van bướm góc (angle-seating butterfly) "
               "6 inch có Cv định mức 825. Từ catalog của nhà sản xuất, ta có đặc tính lưu "
               "lượng vốn có như sau:"))
    b.append(table(["% Hành trình", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100"],
                   [["Cv", "32", "80", "130", "190", "265", "345", "440", "535", "680", "825"]],
                   caption="Đặc tính lưu lượng vốn có của van bướm góc 6 inch, Cv định mức "
                           "825 (theo catalog)."))
    b.append(p("Điều này cho biết van sẽ mở khoảng 75% ở lưu lượng cực đại — gần như hoàn "
               "hảo. Giờ ta tính phần trăm hành trình cho các lưu lượng khác, tức là phần "
               "trăm tín hiệu của bộ điều khiển, vì (do không quy định cam cho bộ định vị) "
               "nó xấp xỉ bằng hành trình van. Tại 1050 gpm, ta lại tính độ giảm áp qua van "
               "như trên: 121 psi (cột áp bơm) − 19,8 psi (ΔP<sub>ống</sub>) − 23 psi − 52 "
               "psi = 26,2 psi, và Cv = 1050/(26,2/1,1)<sup>0,5</sup> = 215. Ngoại suy từ "
               "bảng Cv của van, ta xác định được hành trình 43,3%."))
    b.append(eq("121 − 19,8 − 23 − 52 = 26,2 psi;   C<sub>v</sub> = "
                "1050/(26,2/1,1)<sup>0,5</sup> = 215", ""))
    b.append(p("Lặp lại quy trình trên cho tất cả các lưu lượng khác, ta thu được bảng sau:"))
    b.append(table(["Lưu lượng (gpm)", "1250", "1050", "850", "650", "450", "250"],
                   [["% Tín hiệu = % Hành trình", "75", "43", "31", "22", "15", "9"],
                    ["Cv của van", "496", "215", "136", "90", "57", "29"]],
                   caption="Đặc tính lắp đặt tính được: lưu lượng theo phần trăm tín hiệu và "
                           "Cv tương ứng."))
    b.append(p("Lưu lượng theo % tín hiệu giờ chính là đặc tính lưu lượng lắp đặt của ta, "
               "như Hình 9-4, đường A; nó hóa ra phi tuyến mạnh với sự thay đổi độ lợi khoảng "
               "6,7:1 giữa lưu lượng thấp và cao. Điều này rõ ràng sẽ dẫn đến tình trạng bộ "
               "điều khiển không ổn định. Tiếc thay, ta bị kẹt với đặc tính vốn có của van "
               "bướm. Nhưng ngay cả van cầu phần trăm bằng nhau cũng chẳng tốt hơn là mấy,"))
    b.append(fig(4, F.fig_f94()))
    b.append(p("vì độ giảm áp qua van thay đổi theo tỷ lệ 74 psi / 7 psi = 10,5:1. Tiện thể, "
               "nếu cỡ ống là 8 in, các đoạn thu nhỏ cần thiết sẽ làm méo đặc tính lắp đặt "
               "còn hơn nữa. Một lập luận nữa ủng hộ van bướm cùng cỡ với đường ống!"))
    b.append(p("Vậy ta làm gì đây? Một kiểm tra nhanh trong catalog của một nhà sản xuất van "
               "điều khiển phổ biến cho thấy Cv cực đại của van lồng (cage valve) 6 inch với "
               "bộ lót phần trăm bằng nhau (equal-percentage trim) là 357 — quá thấp. Cỡ 8 "
               "inch có sẵn với Cv định mức 570. Cái này thì đáp ứng được, nhưng chi phí cao "
               "và lắp một van lớn hơn cả đường ống thì rất bất tiện. Hơn nữa, đặc tính cũng "
               "không cải thiện được bao nhiêu [3]."))
    b.append(p("Một bộ định vị có cam chỉnh sửa đặc tính cũng vô dụng với mọi thứ ngoại trừ "
               "hệ thống điều khiển nhiệt độ chậm (nguồn in «xem Chương 9», nhưng thực tế nội "
               "dung về cam nằm ngay trong chương này). Vì vậy, ta phải dựa vào phép màu hiện "
               "đại của điện tử. Giả sử ta chỉnh sửa tín hiệu đầu ra S<sub>i</sub> từ máy tính "
               "thay vì gửi trực tiếp (qua bộ chuyển đổi số–tương tự) tới van trong dải 4 đến "
               "20 mA chuẩn. Nếu S<sub>i</sub> là tín hiệu do logic điều khiển bên trong tạo "
               "ra và S<sub>o</sub> là tín hiệu đầu ra cuối cùng tới van, ta có thể lập trình "
               "phép chỉnh sửa sau trong trường hợp này:"))
    b.append(eq("S<sub>o</sub> = 0,9 (S<sub>i</sub>)²", ""))
    b.append(note("<b>Lưu ý.</b> Bộ định vị số (digital positioners) không cần chuyển đổi "
                  "sang tín hiệu tương tự."))
    b.append(p("Ở đây, tôi dùng 0,9 để đưa hành trình van gần hơn tới tín hiệu cực đại, và "
               "dùng hàm bình phương để tuyến tính hóa hình dạng của đặc tính lưu lượng lắp "
               "đặt. Điều này cho mối quan hệ sau:"))
    b.append(table(["S<sub>i</sub> (%)", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100"],
                   [["S<sub>o</sub> (%)", "1", "4", "8", "14", "23", "32", "44", "58", "73", "90"]],
                   caption="Tín hiệu máy tính S<sub>i</sub> và tín hiệu đầu ra đã chỉnh sửa "
                           "S<sub>o</sub> (theo bản in)."))
    b.append(p("Giờ ta có thể vẽ lại đặc tính thu được, ví dụ lấy lưu lượng tại 32% hành "
               "trình (S<sub>o</sub>) từ đường A (880 gpm) và chuyển nó tới điểm 60% tín hiệu "
               "máy tính (S<sub>i</sub>) tương ứng. Sau khi chuyển tất cả các điểm, ta có mối "
               "quan hệ giữa lưu lượng và tín hiệu logic bộ điều khiển (S<sub>i</sub>) ở dạng "
               "đường B. Dù độ dốc vẫn còn thay đổi dần, sự thay đổi độ lợi kết quả từ 1,92 "
               "xuống 0,72 (240 gpm/10% xuống 90 gpm/10%) đều nằm trong giới hạn ±50% đã "
               "nêu. Nếu bộ điều khiển được đặt ở độ lợi van 1,35, thì giới hạn trên = 1,35 "
               "+ 50% = 2,025 và giới hạn dưới = 1,35 − 50% = 0,68, cả hai đều nằm trên và "
               "dưới sự thay đổi độ lợi thực tế."))
    b.append(note("<b>Chú thích 2.</b> Độ lợi của van điều khiển là phần trăm thay đổi lưu "
                  "lượng chia cho phần trăm thay đổi tín hiệu."))
    b.append(p("Như vậy, độ lợi 1,35 trong trường hợp này sẽ cho mức tăng lưu lượng 13,5% "
               "(125 gpm) cho mỗi 10% tăng tín hiệu."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "H. D. Baumann, “How to Assign Pressure Drop Across Control Valves for Liquid "
        "Pumping Systems,” Proceedings of the 29th Annual Symposium on Instrumentation for "
        "the Process Industries, Dept. of Chemical Engineering, Texas A&amp;M University, "
        "January 16, 17, and 18 (1974).",
        "Jon Monsen, “Calculating the Installed Flow and Gain of a Control Valve,” Process "
        "Instrumentation (March 2021): 26–30.",
        "H. W. Boger, “Flow Characteristic for Control Valve Installations,” ISA Journal "
        "(November 1966): 50–54.",
    ]))

    b.append(note("<b>Ghi chú về nguồn.</b> (1) Lớp văn bản OCR của các trang in có nhiều "
                  "dấu gạch nối khi xuống dòng («incre-ments», «con-ditions», «manufac-turer», "
                  "«back-pressure», «throt-tling», «over-sized») và các phương trình bị lỗi "
                  "(«Cv ==1250 711 49605//(.) .»); bản dịch ghép từ lại thành từ hoàn chỉnh "
                  "và trình bày lại phương trình bằng ký hiệu toán học. (2) Bốn hình (9-1 đến "
                  "9-4) là bản vẽ lại dạng vector đã đơn giản hóa, không phải bản sao "
                  "facsimile. (3) Trên Hình 9-3, đồng hồ áp suất đầu ra của bơm được in là "
                  "«Pp»; bản vẽ lại giữ nguyên nhãn đó. (4) Trên Hình 9-4, nhãn độ lợi được "
                  "in là «GAIN = 300 GPM/10% SIGNAL»; bản dịch giữ nguyên nhãn này (đã dịch "
                  "theo đúng bản in), dù văn bản chương có chỗ nêu 240 gpm/10%. (5) Nguồn có "
                  "lỗi chép ở câu về cam: «A cam-modified positioner characteristic is of no "
                  "use for anything other than a slow temperature control system (see "
                  "Chapter 9)» — thực tế nội dung về cam nằm ngay trong chương 9 này. (6) Ở "
                  "phần chỉnh sửa tín hiệu ra, nguồn in «lower limit = 1.35 + 50% = 0.68»; "
                  "bản dịch trình bày là 1,35 − 50% = 0,68 cho đúng ý."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 9 chiếm các trang in 57–65 của ấn bản in (PDF tr. 63–71). Nguyên bản "
               "có bốn hình (9-1 đến 9-4), một số bảng số liệu không đánh số và ba tài liệu "
               "tham khảo; tất cả đều được giữ lại. Bốn hình được vẽ lại dạng vector; các "
               "phương trình bị lỗi OCR được trình bày lại bằng ký hiệu toán học."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Đặc tính vốn có: Cv theo hành trình",
                "The inherent characteristic: Cv versus travel"))
    b.append(p("One of the most vexing questions is, what inherent flow characteristic should "
               "my valve have? First, a definition: the inherent flow characteristic is the "
               "relationship between the flow coefficient Cv and valve travel. If it is "
               "linear, then you get (theoretically) the same amount of Cv increase for an "
               "equal increase in travel. Typical values are a 9.8% increase in Cv for every "
               "10% increase in travel. Aha! You might wonder, why not 10% Cv? At, for "
               "example, 1% travel, the flow is already 2% of maximum Cv due to clearance "
               "flow between the plug and the seat ring. Therefore, the change is only 9.8% "
               "per 10% increments (see Figure 9-1)."))
    b.append(p("For the equal percentage characteristic, the typical Cv increase is about "
               "43% above the previous number for each 10% of travel; for example, at 20% "
               "travel the Cv number is 143% of that at 10% travel; assuming the Cv at 40% "
               "travel is 10, then at 50% travel it is 14.3 and at 60% travel, 20.5, and so "
               "on. This means that the flow increases exponentially instead of linearly. "
               "This characteristic is typically represented by a straight line on "
               "semi-logarithmic paper."))
    b.append(p("Finally, there is the quick-opening characteristic, which means the valve "
               "plug is no longer contoured but is usually a flat disk. Here, the Cv increase "
               "is approximately linear, up to a travel equivalent to one-quarter of the "
               "orifice diameter. After that, the flow stops increasing for all practical "
               "purposes. You may safely ignore this characteristic for throttling control "
               "valves."))
    b.append(fig(1, F.fig_f91()))

    b.append(h2("Cảnh báo: đường cong vốn có chỉ đúng khi ΔP không đổi",
                "Caution: inherent curves apply only at constant ΔP"))
    b.append(p("Now a word of caution: after the valve is installed in a piping system, the "
               "above-mentioned flow characteristics are only applicable when:"))
    b.append(ul([
        "the pressure drop remains constant with flow changes;",
        "there will be no onset of flashing, cavitation, or sonic flow at certain flow "
        "conditions (quite possibly due to changes in the F<sub>L</sub> factor of the valve, "
        "with changes in valve travel);",
        "the valve is not installed between reducers.",
    ]))
    b.append(p("Ideal conditions that prevent any of these situations from occurring will "
               "prevail only in the manufacturer's flow lab. To account for the real world, "
               "we have to deal with the installed flow characteristic. This is the "
               "relationship of the flowing quantity to valve travel, accounting for the "
               "difference in pressure drop between the maximum and minimum flow [1]; the "
               "possibility of choked flow along the line; and the distortion that reducer "
               "head losses create in the inherent valve flow characteristic. This installed "
               "characteristic is what finally affects controller stability."))

    b.append(h2("Điều khiển PID và độ lợi không đổi", "PID control and constant gain"))
    b.append(p("An ideal controller proportional, integral, and derivative (PID) action "
               "setting will demand a constant “gain” of the final control element. This "
               "gain is the rate of change in flow (q) for a given change of signal. Usually, "
               "the valve travel (h) is proportional to the signal (s). This makes δ(q)/δ(s) "
               "= constant, for the ideal valve."))
    b.append(p("Ideally, we want a “linear” installed flow characteristic, which is about a "
               "10% increase in flow (not Cv) for every 10% increase in travel (this would "
               "result in an installed “gain” of the valve of 1). However, nothing in life is "
               "ideal, therefore we have to compromise. As a rule of thumb, the valve gain "
               "can vary ±50% from the average constant gain value (it does not need to be "
               "1.0) without requiring an adjustment in the controller's PID settings. This "
               "means, for example, that one can accept an installed characteristic where "
               "the flow can vary 5% per 10% travel at one end and 15% per 10% travel on the "
               "other. This certainly makes life easier. Figure 9-2 shows an example of a "
               "typical installed valve flow characteristic."))
    b.append(p("Here, the controller was tuned at 20% flow or 28% of signal. The slope of "
               "the curve at that point (15% flow per 20% signal) serves as a reference. In "
               "this case, it just so happens that the gain changes in either direction. "
               "Therefore, the ±50% (i.e., 1.5 and 0.5) “constant gain” slopes determine "
               "the limits' superimposed 50% control valve gain variations from the original "
               "controller setting, indicating limits of expected stable controller "
               "performance. Retuning the controller may be necessary if the flow range "
               "exceeds the shown limits.<sup>1</sup> The figure caption describes a valve "
               "having a constant gain of 0.75 with good controller stability; the two "
               "quoted characteristics are 10% flow (8% signal) and 57% flow (78% signal)."))
    b.append(note("<b>Footnote 1.</b> Change the proportional band of the controller to 50% "
                  "if the average gain is around 2, for example."))
    b.append(fig(2, F.fig_f92()))

    b.append(h2("Quy tắc chọn đặc tính", "Rules for choosing the characteristic"))
    b.append(p("Based on the information in Figure 9-2, we can make the following rules."))
    b.append(ol([
        "First, check your process and identify the ΔP across the valve at the minimum "
        "required flow rate and the ΔP at the maximum flow rate. Establish a ratio between "
        "the two.",
        "Second, if the ratio is less than 2:1, choose a linear inherent valve "
        "characteristic. If the ratio is above 2:1, choose an equal percentage plug.",
    ]))
    b.append(p("So much for science. Now let us look at the more mundane aspects of the "
               "subject. As I have already stated, most valves are oversized, primarily due "
               "to overestimating pipe pressure losses that tend to lower the sizing ΔP and "
               "allowing for future increases in throughput. Typically, you wind up using "
               "only 40% of the valve's rated Cv at maximum flow. A linear valve will be about "
               "40% open (using only 40% of the controller's signal span). An equal "
               "percentage valve, on the other hand, will be at about 75% travel. Which will "
               "make the better optical impression on your supervisor? Never mind that the "
               "valve's deadband is now spread over 75% of the signal span instead of only "
               "over 40%. You guessed it: the answer is the valve with the equal percentage "
               "plug!"))

    b.append(h2("Ví dụ bộ trao đổi nhiệt", "Heat-exchanger example"))
    b.append(p("Consider another argument. Assume the liquid flow through a heat exchanger "
               "may vary 3:1 and the corresponding ΔP across the valve, typically to the "
               "square of the flow rate, that is, nine times the ΔP at one-third of the flow. "
               "Our rangeability, or turndown, that is, the ratio of maximum to minimum Cv, is "
               "now [1/(1)^1/2]/[0.333/(9)^1/2] = 1/0.111 or 9:1. Dividing the 40% of rated "
               "Cv at maximum flow (see above) by 9 now yields 4.4% of rated Cv at minimum "
               "flow."))
    b.append(eq("[1/(1)<sup>1/2</sup>] / [0.333/(9)<sup>1/2</sup>] = 1 / 0.111 = 9:1", ""))
    b.append(p("For a valve with a linear characteristic, this occurs at about 3% travel or "
               "in the “danger” zone (below 5% travel) where the plug may bump against the "
               "seat following a slight controller instability. The equal percentage valve, "
               "on the other hand, has about 14% travel at the minimum flow! These are "
               "arguments you should keep in mind."))

    b.append(h2("Bộ điều khiển tự chỉnh và đường cong tín hiệu lập trình được",
                "Self-tuning controllers and programmable output curves"))
    b.append(p("With the availability of self-tuning controllers and computer chips that can "
               "vary the shape of the output signal curve to your valve, the question of what "
               "to choose as an inherent valve flow characteristic becomes more irrelevant. "
               "Keep in mind that most rotary control valves have “natural” inherent "
               "characteristics that cannot be defined in either of the classic definitions, "
               "yet they all seem to work well."))
    b.append(p("This proves how forgiving most control loops are. Remember, any flow "
               "characteristic is linear when viewed under a magnifying glass. For continual "
               "processes where the flow rate does not vary by more than 20%, the gain change "
               "is less than 2:1 regardless of the type of inherent characteristic, so you "
               "might as well choose equal percentage because of the advantages outlined "
               "earlier."))

    b.append(h2("Cam định tính trong bộ định vị", "Characterized cams in positioners"))
    b.append(p("Here is a final word regarding the use of characterized cams in positioners "
               "attached to rotary control valves. These are of limited use. First, if the "
               "valve has a nearly linear inherent characteristic, then 4% Cv is still only "
               "3% travel, regardless of the 14% signal input required by the equal "
               "percentage cam. Second, the modified relationship of travel to signal is "
               "correct only under static conditions; that is, it only works with large "
               "process time constants such as temperature control. Finally, characterized "
               "cams are inaccurate and difficult to adjust."))
    b.append(p("If the process is fast, you have a control valve that has a variable time "
               "constant with travel, which can raise cane with the stability of the loop. "
               "Why? Because if you have an equal percentage cam to convert (e.g., a linear "
               "inherent valve characteristic), it requires the valve actuator to move about "
               "21% of its rated travel for a signal change from 90% to 80% but only 1.6% of "
               "travel for a signal change from 20% to 10%. Expressed differently, it takes "
               "13 times longer for the valve to move at the top of the signal change than "
               "near the bottom of the signal span! This can drastically interfere with the "
               "time constant of the process loop. Therefore, avoid cams for pressure or flow "
               "control (fast loops)."))

    b.append(h2("Cách tính đặc tính lưu lượng «lắp đặt»",
                "How to Calculate the “Installed” Flow Characteristic"))
    b.append(p("Before you sign a purchase requisition for a given control valve, you may "
               "want to know if your controller remains stable in a control loop where the "
               "flow rate can vary over a wide range, allowing only the maximum control valve "
               "gain change of ±50% mentioned earlier as a criterion. However, this cannot be "
               "done without calculating or plotting the installed flow characteristic of "
               "the valve and piping system combination, which, when completed, should look "
               "similar to the curve in Figure 9-2."))
    b.append(p("Assume we have a liquid flow system that consists of a storage tank, a "
               "centrifugal pump, the control valve, more than 20 feet of 6-inch pipe, four "
               "elbows, and a process vessel like the example shown in Figure 9-3 [2]; the "
               "figure is courtesy of Jon Monsen."))
    b.append(fig(3, F.fig_f93()))
    b.append(p("To do the job, we need the following information."))
    b.append(ul([
        "The maximum and minimum flow rates, given as 1250 and 250 gpm, respectively.",
        "The pump characteristic (converted from feet to psi), given by the manufacturer "
        "(see the table below).",
        "The friction loss in the pipe and elbows, calculated as 28 psi at a flow rate of "
        "1250 gpm. If there is no problem with viscosity or flashing, we can assume that the "
        "friction loss is proportional to the square of the flow rate, that is, ΔP pipe = 28 "
        "psi/(gpm/1250 gpm)²; as in the table below.",
        "The static head change (elevation difference) from the pump intake to the process "
        "vessel (converted from feet to psi), given as 23 psi (remains constant).",
        "The back pressure in the process vessel, given as 52 psig (remains constant).",
    ]))
    b.append(table(["gpm", "1250", "1050", "850", "650", "450", "250"],
                   [["ΔP pipe (psi)", "28", "19.8", "12.9", "7.6", "3.6", "1.1"],
                    ["Pump head (psi)", "110", "121", "131", "140", "146", "150"]],
                   caption="Pump characteristic and pipe friction loss versus flow (as "
                           "printed)."))
    b.append(p("First, we calculate the available pressure drop across the control valve at "
               "maximum flow (1250 gpm):"))
    b.append(eq("ΔP<sub>valve</sub> = pump head − ΔP<sub>pipe</sub> − static head − "
                "backpressure = 110 − 28 − 23 − 52 = 7 psi", ""))
    b.append(p("From the process data, we know the specific gravity equals 1.1. We now can "
               "calculate the maximum required valve Cv using Equation 5-1:"))
    b.append(eq("C<sub>v</sub> = 1250 / (7 / 1.1)<sup>0.5</sup> ≈ 496", ""))
    b.append(p("Because no tight shutoff is required, and based on rangeability and cost "
               "considerations, we might consider a 6-inch, angle-seating butterfly valve "
               "with a rated Cv of 825. From the manufacturer's catalog, we get the inherent "
               "flow characteristic, which is:"))
    b.append(table(["% Travel", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100"],
                   [["Cv", "32", "80", "130", "190", "265", "345", "440", "535", "680", "825"]],
                   caption="Inherent flow characteristic of the 6 in angle-seating butterfly "
                           "valve, rated Cv 825 (catalog)."))
    b.append(p("This tells us that the valve will be about 75% open at maximum flow—almost "
               "perfect. Now we will calculate the percentage of valve travel for our other "
               "flow rates, that is, the percentage of controller signal, which (because we "
               "did not specify a positioner cam) is about identical to the valve travel. "
               "Going to 1050 gpm, we again calculate the valve pressure drop as above. This "
               "is 121 psi (pump head) – 19.8 psi (ΔP pipe) – 23 psi – 52 psi = 26.2 psi, and "
               "the Cv = 1050/(26.2/1.1)<sup>0.5</sup> = 215. Extrapolating from the Cv table "
               "of the valve, we identify the travel at 43.3%."))
    b.append(eq("121 − 19.8 − 23 − 52 = 26.2 psi;   C<sub>v</sub> = "
                "1050/(26.2/1.1)<sup>0.5</sup> = 215", ""))
    b.append(p("Repeating the same process for all other flow rates, we determine the "
               "following:"))
    b.append(table(["Flow (gpm)", "1250", "1050", "850", "650", "450", "250"],
                   [["% Signal = % Travel", "75", "43", "31", "22", "15", "9"],
                    ["Valve Cv", "496", "215", "136", "90", "57", "29"]],
                   caption="Calculated installed characteristic: flow versus percent signal "
                           "and corresponding valve Cv."))
    b.append(p("The flow versus % signal is now our installed flow characteristic as shown "
               "in Figure 9-4, curve A, which turns out to be highly nonlinear with a gain "
               "variation of about 6.7:1 between low flow and high flow. This obviously will "
               "result in an unstable controller situation. Unfortunately, we are stuck with "
               "the inherent characteristic of the butterfly valve. But even an equal "
               "percentage globe valve would not have been much better,"))
    b.append(fig(4, F.fig_f94()))
    b.append(p("with the pressure drop across the valve varying over a ratio of 74 psi / 7 "
               "psi = 10.5:1. Incidentally, if the line size would have been 8 in, the "
               "required reducers would have distorted the installed characteristic even "
               "more. Another argument for line-size butterfly valves!"))
    b.append(p("So, what can we do? A quick check in a popular control valve manufacturer's "
               "catalog shows the maximum Cv of a 6-inch cage valve with equal percentage "
               "trim is 357, which is too low. An 8-inch size valve is available with a rated "
               "Cv of 570. This would fit the bill, but the cost is high, and it would be "
               "awkward to install a valve larger than the pipe size. Besides, the "
               "characteristic would not have made that much of an improvement [3]."))
    b.append(p("A cam-modified positioner characteristic is of no use for anything other than "
               "a slow temperature control system (printed as “see Chapter 9,” although the "
               "cam discussion is in this very chapter), so we have to rely on the modern "
               "miracle of electronics. Assume we modify the output signal S<sub>i</sub> from "
               "a computer instead of sending it directly (via a digital-to-analog converter) "
               "to the valve in the standard 4 to 20 mA range. If S<sub>i</sub> is the signal "
               "generated by the internal controller logic and S<sub>o</sub> is the final "
               "output signal to the valve, we can program the following modification in "
               "this case:"))
    b.append(eq("S<sub>o</sub> = 0.9 (S<sub>i</sub>)²", ""))
    b.append(note("<b>Note.</b> Digital positioners need no conversion to analog."))
    b.append(p("In this case, I use 0.9 to bring the valve travel closer to the maximum "
               "signal and use the square function to linearize the shape of the installed "
               "flow characteristic. This yields the following relationship:"))
    b.append(table(["S<sub>i</sub> (%)", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100"],
                   [["S<sub>o</sub> (%)", "1", "4", "8", "14", "23", "32", "44", "58", "73", "90"]],
                   caption="Computer signal S<sub>i</sub> and modified output signal "
                           "S<sub>o</sub> (as printed)."))
    b.append(p("We can now replot the resultant characteristic, for example, by taking the "
               "flow at 32% travel (S<sub>o</sub>) from curve A (880 gpm) and moving it to the "
               "corresponding 60% computer signal (S<sub>i</sub>) point. After transferring "
               "all points, we now have the relationship between flow and controller logic "
               "signal (S<sub>i</sub>) in the form of curve B. While we still have some "
               "gradual change in slope, the resultant gain variations from 1.92 to 0.72 (240 "
               "gpm/10% to 90 gpm/10%) are all within the stated limitation of ±50%. If the "
               "controller is set to a valve gain of 1.35, then the upper limit = 1.35 + 50% "
               "= 2.025, and a lower limit = 1.35 − 50% = 0.68, both above and below the "
               "actual gain variations."))
    b.append(note("<b>Footnote 2.</b> The control valve gain is the percentage of flow change "
                  "divided by a percentage of signal change."))
    b.append(p("Thus, a gain of 1.35, in this case, will yield 13.5% of flow (125 gpm) "
               "increase per each 10% of signal increase."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "H. D. Baumann, “How to Assign Pressure Drop Across Control Valves for Liquid "
        "Pumping Systems,” Proceedings of the 29th Annual Symposium on Instrumentation for "
        "the Process Industries, Dept. of Chemical Engineering, Texas A&amp;M University, "
        "January 16, 17, and 18 (1974).",
        "Jon Monsen, “Calculating the Installed Flow and Gain of a Control Valve,” Process "
        "Instrumentation (March 2021): 26–30.",
        "H. W. Boger, “Flow Characteristic for Control Valve Installations,” ISA Journal "
        "(November 1966): 50–54.",
    ]))

    b.append(note("<b>Source notes.</b> (1) The OCR text layer of the printed pages contains "
                  "many line-break hyphenations («incre-ments», «con-ditions», "
                  "«manufac-turer», «back-pressure», «throt-tling», «over-sized») and garbled "
                  "equations («Cv ==1250 711 49605//(.) .»); the translation joins the words "
                  "into whole words and re-presents the equations with mathematical notation. "
                  "(2) All four figures (9-1 to 9-4) are simplified vector redrawings, not "
                  "facsimiles. (3) In Figure 9-3 the pump discharge gauge is printed as "
                  "«Pp»; the redrawing keeps that label. (4) In Figure 9-4 the gain label is "
                  "printed as «GAIN = 300 GPM/10% SIGNAL»; the label is retained and "
                  "translated exactly as printed, even though the chapter text elsewhere "
                  "states 240 gpm/10%. (5) The source contains a cross-reference error in "
                  "the cam sentence: «A cam-modified positioner characteristic is of no use "
                  "for anything other than a slow temperature control system (see Chapter "
                  "9)» — in fact the cam discussion is in this very chapter. (6) In the "
                  "output-signal section the source prints «lower limit = 1.35 + 50% = "
                  "0.68»; the translation gives 1.35 − 50% = 0.68, as intended."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chapter 9 occupies printed pp. 57-65 of the book (PDF pp. 63-71). The source "
               "has four figures (9-1 to 9-4), several unnumbered numeric tabulations and "
               "three references; all are retained. The figures are redrawn as vectors and "
               "the OCR-garbled equations are re-presented with mathematical notation."))
    return "".join(b)
