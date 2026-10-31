# -*- coding: utf-8 -*-
"""Safety Instrumented Systems — Chapter 8, Initial System Evaluation
(Gruhn & Cheddie, ISA 2006)."""
from pcsis_common import (eq, fig, h2, h3, lead, note, ol, p, quote, refs,
                          table, ul)

import sis08fig as F

PAGES_SRC = 35
BYLINE = "Paul Gruhn & Harry Cheddie · ISA (2006)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>λ (lambda)</em> — suất hỏng, số hư hỏng mỗi đơn vị thời gian; λ = 1/MTBF. · "
            "<em>MTBF</em> — thời gian trung bình giữa hai lần hỏng; không phải “tuổi thọ”. · "
            "<em>MTTF<sub>spurious</sub></em> — thời gian trung bình tới một lần cắt nhầm. · "
            "<em>PFD<sub>avg</sub></em> — xác suất hỏng trung bình khi có yêu cầu. · "
            "<em>RRF</em> — hệ số giảm rủi ro, bằng nghịch đảo của PFD. · "
            "<em>SA</em> — độ khả dụng an toàn, bằng 1 − PFD. · "
            "<em>Hệ số phủ chẩn đoán (DC)</em> — phần trăm hư hỏng mà hệ tự phát hiện được. · "
            "<em>Hệ số Beta</em> — phần trăm hư hỏng của một kênh hoá ra đánh vào toàn hệ (nguyên nhân "
            "chung). · "
            "<em>TI / TD</em> — chu kỳ thử và thời gian thử. · "
            "<em>SFF</em> — tỷ lệ hư hỏng an toàn, dùng để tra bảng yêu cầu dự phòng.")
    return note(
        "<b>Key terms.</b> <em>Lambda</em> — failure rate, failures per unit time; λ = 1/MTBF. · "
        "<em>MTBF</em> — mean time between failures; not the same thing as life. · "
        "<em>MTTF<sub>spurious</sub></em> — mean time to a nuisance trip. · <em>PFD<sub>avg</sub></em> — "
        "average probability of failure on demand. · <em>RRF</em> — risk reduction factor, the reciprocal "
        "of PFD. · <em>SA</em> — safety availability, 1 − PFD. · <em>Diagnostic coverage</em> — the "
        "fraction of failures the system finds by itself. · <em>Beta factor</em> — the fraction of one "
        "channel's failures that take out the whole system. · <em>TI / TD</em> — test interval and test "
        "duration. · <em>SFF</em> — safe failure fraction, the number you look up in the fault tolerance "
        "tables.")


# ===================================================================== VI
def body_vi():
    b = []
    b.append(lead(
        "Nếu chỉ nhìn qua đã thấy ngay hệ nào phù hợp với ứng dụng nào thì đã không cần cuốn sách này, "
        "cũng không cần các tiêu chuẩn thiết kế. Vấn đề là ở chỗ mọi thứ không hiển nhiên như vẻ ngoài của "
        "chúng. Hai kênh không phải lúc nào cũng tốt hơn một, và ba kênh không phải lúc nào cũng tốt hơn "
        "hai. Chương này dựng bộ công cụ để trả lời câu hỏi đó bằng số, và — quan trọng không kém — chỉ ra "
        "những chỗ mà con số ấy không đáng tin."))

    b.append(note_terms("vi"))

    b.append(quote("Với mọi vấn đề của con người, bao giờ cũng có một lời giải dễ: gọn gàng, nghe hợp "
                   "lý… và sai.", "H. L. Mencken"))

    # ------------------------------------------------------------------ 8.1
    b.append(h2("8.1 Mọi thứ không hiển nhiên như vẻ ngoài", "Things Are Not as Obvious as They May Seem"))
    b.append(p("Giả sử, ở thời điểm này, cả chín trường hợp trong bảng dưới đây đều dùng hệ logic dựa trên "
               "phần mềm (hệ điện tử khả trình — PES). Tạm gác hệ rơ-le và hệ bán dẫn rắn sang một bên."))
    b.append(table(
        ["Cảm biến", "Logic PES", "Độ phủ chẩn đoán", "Nguyên nhân chung", "Đầu ra", "Chu kỳ thử"],
        [
            ["Đơn", "Đơn", "99,9 %", "không áp dụng", "Đơn", "hằng tháng"],
            ["Đôi", "Đơn", "99 %", "không áp dụng", "Đôi", "hằng quý"],
            ["Ba", "Đơn", "90 %", "không áp dụng", "Đôi", "hằng năm"],
            ["Đơn", "Đôi", "99 %", "0,1 %", "Đơn", "hằng tháng"],
            ["Đôi", "Đôi", "90 %", "1 %", "Đôi", "hằng quý"],
            ["Ba", "Đôi", "80 %", "10 %", "Đôi", "hằng năm"],
            ["Đơn", "Ba", "99 %", "0,1 %", "Đơn", "hằng tháng"],
            ["Đôi", "Ba", "90 %", "1 %", "Đơn", "hằng quý"],
            ["Ba", "Ba", "80 %", "10 %", "Đơn", "hằng năm"],
        ],
        caption="Bảng 8-1. Hệ nào “tốt nhất”? Hệ nào ít cắt nhầm nhất? Hệ nào cho hiệu năng an toàn tốt "
                "nhất? Ba câu hỏi, và không có hàng nào đứng đầu cả ba."))
    b.append(p("Trước hết, hãy nhớ rằng hệ thống đo lường an toàn có hai cách hỏng. Chúng có thể cắt nhầm, "
               "dừng nhà máy khi thực tế chẳng có gì sai. Chúng cũng có thể không hành động khi thật sự "
               "cần. Liệu có hệ nào tốt nhất ở cả hai chế độ? Và nếu một hệ tốt ở chế độ này thì có nhất "
               "thiết phải dở ở chế độ kia?"))
    b.append(p("Chuỗi chỉ bền bằng mắt yếu nhất. Vậy cảm biến có nên dự phòng? Thiết bị dự phòng đôi có "
               "ít nhất hai cách đấu. Bỏ phiếu một-trong-hai (1oo2) sẽ cắt khi <em>một</em> cảm biến vào "
               "báo động. Bỏ phiếu hai-trong-hai (2oo2) chỉ cắt khi <em>cả hai</em> cùng vào báo động."))
    b.append(p("Bộ xử lý logic có nên dự phòng? Có ít nhất bốn cách đấu hai bộ xử lý logic (1oo2, 2oo2, "
               "1oo2D, hoặc dự phòng nóng). Còn ba bộ thì sao?"))
    b.append(p("Độ phủ chẩn đoán là tỷ lệ hư hỏng mà hệ tự phát hiện được. Không thiết bị nào đạt 100 %. "
               "Vậy một hệ không dự phòng với độ phủ 99,9 % có tốt hơn một hệ ba kênh với độ phủ 80 %?"))
    b.append(p("Nguyên nhân chung là một tác nhân căng thẳng hay một lỗi duy nhất đánh vào cả hệ dự phòng. "
               "Ví dụ điển hình là các tác nhân môi trường bên ngoài: nhiệt, rung, quá áp… Một cách lượng "
               "hoá nguyên nhân chung gọi là <b>hệ số Beta</b>. Nó biểu thị phần trăm hư hỏng ghi nhận "
               "trong một “nhánh” của hệ mà có thể đánh vào nhiều kênh cùng lúc. Ví dụ, nếu một hệ dự "
               "phòng có hệ số Beta 1 %, nghĩa là trong toàn bộ số hư hỏng ghi nhận được, 1 % có thể đánh "
               "vào nhiều kênh cùng lúc và làm hỏng cả hệ. 1 % đã đáng lo chưa? Còn 10 % thì sao?"))
    b.append(p("Phần tử cuối — thường là van — có nên dự phòng? Song song hay nối tiếp? Van dự phòng, "
               "nhất là van lớn, rõ ràng rất tốn kém, nhưng chúng có quan trọng không? Đầu ra ba kênh "
               "không có trong bảng. Ba kênh thường — tuy không phải luôn luôn — nghĩa là bỏ phiếu hai "
               "trong ba. Không thể nối ba chiếc van để được phép bỏ phiếu hai-trong-ba. Tuy vậy, người ta "
               "đã từng lắp ba chiếc van nối tiếp nhau."))
    b.append(p("Bao lâu phải thử toàn hệ một lần bằng tay? Phải thử vì không hệ nào có chẩn đoán 100 % và "
               "tự phát hiện được mọi lỗi. Nên thử mọi thứ cùng một chu kỳ, hay thử từng phần với chu kỳ "
               "khác nhau? Hệ dự phòng cần thử thường xuyên hơn hay ít hơn hệ không dự phòng?"))
    b.append(p("Quay lại Bảng 8-1. Thêm một cột bên trái ghi “cắt nhầm”. Thêm một cột bên phải ghi “an "
               "toàn”. Xếp hạng từng hàng từ 1 đến 9, tốt nhất đến tệ nhất. Cứ làm đi!"))
    b.append(p("Bạn tự tin đến mức nào về câu trả lời của mình? Bạn có tin rằng trực giác, cảm nhận hay "
               "kinh nghiệm của bạn sẽ cho cùng đáp án với người khác?"))
    b.append(p("Nhiều nhóm soạn tiêu chuẩn đã họp hàng năm trời để giải quyết những câu hỏi này. Nếu tất "
               "cả đều dễ thì họ đã xong từ lâu rồi. Chỉ riêng uỷ ban ISA SP84: danh sách thư có hơn 300 "
               "thành viên, đại diện gần như mọi nhóm lợi ích có thể hình dung (nhà cung cấp bán dẫn rắn, "
               "PLC, PLC an toàn, DCS; người dùng cuối; nhà thầu; đơn vị tích hợp; tư vấn; tổ chức chứng "
               "nhận…). Một nhóm đa dạng như thế làm sao đồng thuận được về một chủ đề phức tạp và gây "
               "tranh cãi đến vậy? Làm sao nhìn xuyên qua lớp quảng cáo?"))
    b.append(p("Trực giác có thể đủ cho vài việc, nhưng không đủ cho nhiều việc khác. Máy bay phản lực "
               "không được chế tạo bằng cảm tính. Cầu không được làm bằng thử-sai, ít nhất là không còn "
               "như thế nữa. Nhà máy điện hạt nhân không được xây bằng linh cảm. Nếu bạn hỏi kỹ sư "
               "trưởng của Boeing 777 vì sao họ chọn cỡ động cơ ấy, bạn sẽ thấy yên tâm đến đâu nếu câu "
               "trả lời là: “À, chúng tôi cũng không chắc… nhưng nhà cung cấp khuyên thế.”"))

    # ------------------------------------------------------------------ 8.2
    b.append(h2("8.2 Vì sao phải phân tích hệ trước khi xây", "Why Systems Should be Analyzed Before They’re Built"))
    b.append(p("Lý tưởng thì bạn muốn thực hiện một nghiên cứu nguy cơ và khả năng vận hành (HAZOP) cho "
               "nhà máy trước khi xây hay sau khi xây? Câu trả lời hiển nhiên là trước, nhưng không phải "
               "ai được hỏi cũng nhận ra lý do thật sự. Thiết kế lại nhà máy trên giấy thì rẻ hơn. Cách "
               "còn lại là đập đi xây lại. Hệ an toàn cũng vậy."))
    b.append(p("Như đã nói ở mục 8.1, mọi thứ không hiển nhiên như ta mong. Quyết định hệ nào phù hợp cho "
               "một ứng dụng cụ thể không phải chuyện đơn giản. Vì thế điều quan trọng là phải phân tích "
               "hệ một cách định lượng. Phân tích định lượng có thể không chính xác — điều sẽ được nhấn "
               "mạnh ngay sau đây — nhưng vẫn là một việc đáng làm, vì những lý do sau:"))
    b.append(ul([
        "Cho biết sớm liệu hệ có khả năng đáp ứng yêu cầu thiết kế hay không.",
        "Cho phép so sánh chi phí vòng đời.",
        "Cho phép xác định mắt yếu của hệ (và sửa nếu cần).",
        "Cho phép so sánh “táo với táo” giữa các phương án chào hàng khác nhau.",
    ]))

    b.append(h3("8.2.1 Những lưu ý", "Caveats"))
    b.append(quote("Có những lời nói dối, có những lời nói dối trắng trợn, và rồi có thống kê.",
                   "M. Twain"))
    b.append(p("Mô hình đơn giản có thể tính và giải bằng tay. Nhưng khi càng nhiều yếu tố được tính đến, "
               "phương pháp thủ công càng trở nên khó dùng. Có thể lập bảng tính hoặc viết chương trình để "
               "tự động hoá. Nhược điểm lớn của một số mô hình thường không phải ở chỗ chúng bao gồm những "
               "gì, mà ở chỗ chúng <em>không</em> bao gồm những gì. Có thể mô hình hoá một hệ ba kênh theo "
               "các giả định lạc quan của một nhà cung cấp, rồi mô hình hoá lại với một bộ giả định thực "
               "tế hơn — và kết quả thay đổi bốn bậc độ lớn! Không phải độ chính xác của mô hình quyết "
               "định, mà thường là các giả định đưa vào mô hình. Máy tính nổi tiếng vì tốc độ, không phải "
               "vì trí tuệ."))
    b.append(quote("Mô hình máy tính có thể dự báo hiệu năng với tốc độ và độ chính xác cao, nhưng cũng "
                   "có thể hoàn toàn sai!", "Khuyết danh"))
    b.append(p("Khi thiết kế Boeing 777, có hai phe về việc mô hình hoá và thử nghiệm động cơ. Một nhóm "
               "cho rằng mô hình máy tính của họ tốt đến mức không cần thử động cơ thật. Nhóm kia cho rằng "
               "phải thử thật. Nhóm sau thắng. Hai động cơ ở một bên chiếc 747 được tháo ra và thay bằng "
               "một động cơ mới dành cho 777, mạnh gấp đôi động cơ cũ. Lần đầu máy bay cất cánh, động cơ "
               "mới tắt ngóm. Lỗi đó không hề xuất hiện trong mô hình máy tính. Hãy luôn nhớ: mô hình chỉ "
               "là mô hình — không phải thực tế!"))
    b.append(quote("Dù máy tính có trung lập đến đâu, nó cũng không bao giờ cho ra một đáp án khách quan "
                   "từ dữ liệu hết sức chủ quan.", "Imperato & Mitchell"))
    b.append(p("Cần một chút ý thức thường thức trong mọi việc mô hình hoá. Ví dụ, nếu hai biến cố mỗi "
               "biến cố có xác suất 10⁻⁶, cách làm đơn giản là nói rằng xác suất hai biến cố xảy ra đồng "
               "thời là 10⁻¹². Những con số nhỏ như thế chỉ có nghĩa rằng hệ sẽ hỏng theo một cách mà "
               "chính người thiết kế ban đầu cũng không nghĩ tới. Những ước lượng rủi ro vô lý đến mức "
               "ngớ ngẩn, tính từ số liệu suất hỏng, không phải chuyện hiếm. [Ref. 2] Kỷ lục hiện nay là "
               "một ước lượng cho một hệ vũ khí hạt nhân với xác suất biến cố 2,8 × 10⁻³⁹⁷. Xét rằng xác "
               "suất bị một chiếc máy bay rơi trúng chỉ vào khoảng 10⁻⁸, mức vô lý của một số phép tính "
               "trở nên hiển nhiên. Kletz nói gọn và thẳng: “Người ta tự hỏi làm sao những người được đào "
               "tạo khoa học lại có thể chấp nhận thứ rác rưởi như vậy.” [Ref. 1]"))
    b.append(quote("Mô hình độ tin cậy giống như điệp viên bị bắt: tra tấn đủ lâu, chúng sẽ khai bất cứ "
                   "điều gì.", "P. Gruhn"))
    b.append(p("Kletz cũng chỉ ra rằng “thời gian thường được dùng tốt hơn nếu đem đi tìm mọi nguồn nguy "
               "hiểm, thay vì định lượng ngày càng chính xác những nguồn đã tìm ra.” Ví dụ, trong chương "
               "trình không gian — nơi phân tích cây lỗi định lượng và phân tích chế độ hỏng được dùng rất "
               "rộng rãi — gần 35 % số hỏng hóc thực tế trên chuyến bay đã không được nhận diện trước. "
               "[Ref. 2]"))

    # ------------------------------------------------------------------ 8.3
    b.append(h2("8.3 Lấy số liệu suất hỏng ở đâu", "Where to Get Failure Rate Information"))
    b.append(p("Muốn phân tích và dự báo hiệu năng của một hệ, cần số liệu hiệu năng (tức suất hỏng) của "
               "mọi thành phần. Lấy những số liệu ấy ở đâu?"))

    b.append(h3("8.3.1 Sổ sách bảo trì", "Maintenance Records"))
    b.append(p("May thay, mỗi cơ sở thường có sổ bảo trì ghi suất hỏng của các thiết bị liên quan an toàn. "
               "Quy định về quản lý an toàn quá trình (29 CFR 1910.119, Phụ lục C, Phần 9) yêu cầu người "
               "dùng phải lưu loại số liệu này. Nhiều nhà máy thật sự có thông tin, dù ban đầu nó có thể "
               "chưa được tập hợp theo cách dùng được. Những kỹ thuật viên có kinh nghiệm thường biết rất "
               "rõ thiết bị nào phải sửa hoặc thay bao lâu một lần."))
    b.append(p("Sổ bảo trì của nhà máy là nguồn số liệu tiềm năng tốt nhất. Nó đại diện nhất cho môi "
               "trường ứng dụng, cho cách bảo trì và cho đúng nhà cung cấp đang xét — miễn là mẫu thu được "
               "đủ lớn để có ý nghĩa thống kê."))
    b.append(p("Nhưng nếu không có sổ sách ấy thì sao?"))

    b.append(h3("8.3.2 Số liệu của nhà cung cấp", "Vendor Records"))
    b.append(p("Có thể hỏi nhà cung cấp, nhưng phản hồi từ những người đã thử thì không mấy khả quan. Bản "
               "ANSI/ISA-84.01 năm 1996 từng nói rằng nhà cung cấp bộ xử lý logic phải cung cấp số liệu "
               "này. Kể cả khi nhà cung cấp có đưa số liệu, vẫn phải hỏi họ lấy nó ở đâu. Từ hàng trả về "
               "hay từ thí nghiệm trong phòng? Có bao nhiêu người dùng một thiết bị đã mười năm tuổi (ví "
               "dụ một bộ chuyển đổi hay một van điện từ) thật sự gửi thiết bị hỏng về nhà máy?"))
    b.append(p("Một nhà cung cấp PLC cho biết số liệu suất hỏng của họ giả định khoảng 25 % số thiết bị "
               "xuất xưởng đang nằm trong kho (tức không hoạt động) và số còn lại chạy hai ca một ngày, "
               "năm ngày một tuần. Không nhiều hệ an toàn trong công nghiệp chế biến vận hành theo giả "
               "định đó."))
    b.append(p("Hàng trả về là nguồn số liệu tiềm năng tệ nhất. Ít người dùng gửi trả thiết bị đã hết bảo "
               "hành; vì thế số liệu thu được thường không có ý nghĩa thống kê."))
    b.append(p("Số liệu suất hỏng của nhà cung cấp, nhất là với thiết bị trường, thường không tính đến "
               "yếu tố công nghệ và môi trường. Một thiết bị trong môi trường bẩn và ăn mòn sẽ hỏng sớm "
               "hơn trong môi trường sạch. Những kiểu hỏng như tắc đường ống xung áp thường không được "
               "tính trong số liệu nhà cung cấp (vì họ coi đó là ngoài phạm vi thiết bị của mình)."))

    b.append(h3("8.3.3 Cơ sở dữ liệu của bên thứ ba", "Third-party Databases"))
    b.append(p("Có sẵn các cơ sở dữ liệu thương mại của ngành dầu khí ngoài khơi, hoá chất và hạt nhân, "
               "cùng các bộ số liệu chung. Thông tin này đã được tập hợp và cung cấp cho mọi người dưới "
               "dạng sách và cơ sở dữ liệu điện tử. [Ref. 5 đến 10] Những cơ sở dữ liệu này dễ tiếp cận, "
               "tuy không phải lúc nào cũng rẻ. Chúng là nguồn tiềm năng tốt thứ hai. Chúng dựa trên kinh "
               "nghiệm thực địa của nhiều người dùng khác nhau, nhưng mang tính chung. Chúng không phân "
               "biệt nhà cung cấp và không tính đến môi trường ứng dụng khác nhau. Các chương trình mô "
               "hình hoá hệ an toàn chuyên dụng cũng có sẵn cơ sở dữ liệu suất hỏng bên trong. [Ref. 16 và "
               "17]"))
    b.append(p("Nhưng còn những thiết bị hoàn toàn mới, hoặc chưa được chế tạo, chưa có lịch sử hoạt động "
               "thực địa thì sao?"))

    b.append(h3("8.3.4 Tính toán kiểu quân sự", "Military Style Calculations"))
    b.append(p("Quân đội đã gặp bài toán này từ nhiều thập kỷ trước. Khi một tàu ngầm hạt nhân nhận mã "
               "phóng, người ta muốn biết khả năng hệ thông tin hoạt động đúng — bằng một thước đo nào đó "
               "khác chữ “cao”. Quân đội đã xây dựng một kỹ thuật dự báo suất hỏng cho linh kiện điện tử "
               "(MIL-HDBK 217). Cuốn sổ tay này đã qua nhiều lần sửa đổi và từ lâu là đề tài tranh cãi. "
               "Ai dùng cũng biết nó có xu hướng cho đáp án bi quan, đôi khi lệch cả bậc độ lớn. Điều đó "
               "không có nghĩa là không nên dùng, mà là phải dùng thận trọng. Nó vẫn là một cái thước rất "
               "tốt để so sánh các hệ, kể cả khi đáp án tuyệt đối đáng ngờ. Nhà phát hành tài liệu biết "
               "điều này và viết rõ:"))
    b.append(quote("… không bao giờ được coi một dự báo độ tin cậy là đại diện cho độ tin cậy thực địa "
                   "mà người dùng đo được…", "MIL-HDBK 217F, đoạn 3.3"))
    b.append(p("Nhiều nhà cung cấp hiện cung cấp số liệu suất hỏng theo cách tính kiểu quân sự. Với một "
               "số chứng nhận an toàn, việc thực hiện các phép tính này thậm chí là yêu cầu bắt buộc. Tuy "
               "vậy, phép tính có thể không bao gồm mọi yếu tố hay mọi kiểu hỏng mà người dùng gặp ngoài "
               "thực tế. Ví dụ, một nhà cung cấp cảm biến công bố MTBF 450 năm. Số liệu do người dùng "
               "tổng hợp thường thấp hơn một bậc độ lớn (khoảng 45 năm). Khác biệt có thể đơn giản là do "
               "nhà cung cấp không tính hết mọi điều kiện ứng dụng và mọi chế độ hỏng trong phân tích của "
               "họ (tắc đường ống xung áp, vấn đề lắp đặt…), trong khi cơ sở dữ liệu người dùng thì có. "
               "Cần thận trọng và cần ý thức thường thức. Nhà cung cấp đưa cho bạn một con số không có "
               "nghĩa là con số ấy đúng hay thực tế."))

    # ------------------------------------------------------------------ 8.4
    b.append(h2("8.4 Chế độ hỏng", "Failure Modes"))
    b.append(p("Rất nhiều người đã thay hệ rơ-le bằng bộ điều khiển logic khả trình (PLC). Lý do họ "
               "thường nêu là: “PLC sinh ra để làm việc đó — thay rơ-le.” Cách hệ vận hành đương nhiên là "
               "quan trọng. Rõ ràng PLC làm được mọi thứ rơ-le làm được, và nhiều hơn thế (bộ định thời, "
               "hàm toán học…). Nhưng điều đáng quan tâm nhất với một hệ an toàn không phải là hệ vận hành "
               "thế nào, mà là hệ <em>hỏng</em> thế nào. Khái niệm này đơn giản đến mức thường bị bỏ qua. "
               "Đây chính là lý do sâu xa khiến hệ an toàn tĩnh tại khác hệ điều khiển chủ động, và khiến "
               "hệ thống đo lường an toàn có những yêu cầu thiết kế riêng."))

    b.append(h3("8.4.1 Hư hỏng an toàn và hư hỏng nguy hiểm", "Safe/Dangerous Failures"))
    b.append(p("Có thể hơi đơn giản hoá, nhưng hệ an toàn được coi là hỏng theo hai cách. Thứ nhất, hệ có "
               "thể gây cắt nhầm. Nó dừng nhà máy khi thật ra chẳng có gì sai. Ví dụ: một tiếp điểm rơ-le "
               "đang đóng và có điện bỗng bật ra. Người ta đặt nhiều tên cho kiểu hỏng này: hỏng lộ, hỏng "
               "khởi phát, hỏng theo hướng an toàn (fail-safe)… Thuật ngữ dùng trong tiêu chuẩn là “hư "
               "hỏng an toàn”. Phải thừa nhận rằng chẳng có gì “an toàn” trong một lần cắt nhầm, nên "
               "nhiều người không thích thuật ngữ này. Hư hỏng an toàn dẫn đến dừng nhà máy; vì thế chúng "
               "thường tốn kém vì mất sản lượng. Người ta tránh hư hỏng an toàn chủ yếu vì lý do kinh tế. "
               "Khi hệ hỏng an toàn quá nhiều, người ta mất niềm tin vào nó, và hệ có thể bị đặt bypass. "
               "Đừng bao giờ quên: độ khả dụng của một hệ đang bị bypass bằng không. Tai nạn đã xảy ra vì "
               "cảm biến hoặc hệ bị đặt bypass trong khi quá trình vẫn được phép chạy. Một người quản lý "
               "khách sạn đã phải vào tù vì tội ngộ sát sau khi vô hiệu hoá hệ phát hiện cháy, khiến một "
               "tá khách thiệt mạng. Hàm ý của quy định quản lý an toàn quá trình OSHA năm 1992 là cá "
               "nhân có thể phải chịu trách nhiệm hình sự cho những hành vi như vậy."))
    b.append(p("Tuy nhiên cũng không được quên rằng hệ an toàn còn có thể hỏng theo cách khiến nó không "
               "phản ứng được với một yêu cầu thật. Có thể hình dung đó là kiểu “tôi kẹt rồi, tôi sẽ "
               "không làm việc khi anh cần”. Có người gọi đây là hỏng ngầm, hỏng ẩn, hỏng ức chế, hay "
               "hỏng theo hướng nguy hiểm. Tiêu chuẩn nay gọi là “hư hỏng nguy hiểm”. Nếu hệ hỏng theo "
               "cách này (ví dụ tiếp điểm rơ-le bị hàn dính) thì đó là mối nguy tiềm ẩn. Một tiếp điểm "
               "đang đóng mà hỏng ở trạng thái đóng có thể không gây ra biến cố nguy hiểm ngay. Nhưng nếu "
               "có yêu cầu đúng lúc đang có hư hỏng ấy, hệ sẽ không phản ứng. Cách duy nhất để tìm ra "
               "những hư hỏng này — trước khi quá muộn — là thử. Nhiều người đơn giản là không hiểu nhu "
               "cầu đó."))
    b.append(p("Nhưng hãy nhớ: hệ thống đo lường an toàn là tĩnh tại, thụ động. Không phải mọi hư hỏng đều "
               "tự bộc lộ. Van thường mở bị kẹt ở vị trí mở không cho thấy dấu hiệu bất thường. Mạch "
               "thường có điện bị ngắn mạch không cho thấy dấu hiệu bất thường. PLC tĩnh tại kẹt trong "
               "vòng lặp vô hạn không cho thấy dấu hiệu bất thường. Cảm biến có đường xung áp bị tắc "
               "không phải lúc nào cũng cho thấy dấu hiệu bất thường. Đáng tiếc là nhiều hệ đa dụng không "
               "có chẩn đoán hiệu quả để phát hiện những hư hỏng đó. Nhà cung cấp hiếm khi nói về những "
               "điểm yếu tiềm ẩn như vậy."))
    b.append(p("Ví dụ về hư hỏng nguy hiểm, ẩn thì hơi khó nói và vì thế thường bị “chôn”. Một ví dụ: một "
               "nhà sản xuất vệ tinh dùng cần cẩu để nâng một vệ tinh trị giá 200.000 USD vào thùng vận "
               "chuyển. Khi nâng lên, cần cẩu không dừng được chuyển động đi lên. Vệ tinh chạm đỉnh cần "
               "cẩu, cáp đứt, và vệ tinh rơi xuống sàn. Rơ-le điều khiển chuyển động đi lên đã được thay "
               "trước đó bằng một rơ-le chỉ chịu 10 % tải thực, nên tiếp điểm bị hàn dính. Cần cẩu là hàng "
               "thuê và chưa được thử trước khi dùng."))

    b.append(h3("8.4.2 Hư hỏng phát hiện được và không phát hiện được", "Detected/Undetected Failures"))
    b.append(p("Hư hỏng không chỉ được phân loại theo an toàn và nguy hiểm, mà còn theo phát hiện được và "
               "không phát hiện được (xem Hình 8-1). Hư hỏng an toàn ở nửa trên của biểu đồ. Hư hỏng "
               "nguy hiểm ở nửa dưới. Hư hỏng phát hiện được ở nửa trái. Hư hỏng không phát hiện được ở "
               "nửa phải. Các phần của biểu đồ tròn được vẽ bằng nhau chỉ để đơn giản. Hư hỏng phát hiện "
               "được gắn với chẩn đoán tự động — tức là hệ có tự phát hiện được khi hư hỏng xảy ra hay "
               "không. Một thước đo mức chẩn đoán gọi là “hệ số phủ”. Hình 8-1 vẽ trường hợp tỷ lệ chế độ "
               "hư hỏng an toàn là 50 % và hệ số phủ chẩn đoán là 50 %. Chữ Hy Lạp λ dùng để biểu thị suất "
               "hỏng, tức số hư hỏng mỗi đơn vị thời gian. Thuật ngữ này sẽ được bàn kỹ ngay sau đây."))
    b.append(fig(1, F.fig_8_1(), "vi"))

    # ------------------------------------------------------------------ 8.5
    b.append(h2("8.5 Các thước đo", "Metrics"))
    b.append(p("Muốn đo và so sánh hiệu năng của các hệ khác nhau, cần một hệ quy chiếu chung, một bộ "
               "thuật ngữ chung dễ hiểu. Nhiều thuật ngữ hiệu năng đã được dùng qua năm tháng, như độ khả "
               "dụng và độ tin cậy. Đáng tiếc là những thuật ngữ tưởng như tầm thường ấy lại gây rắc "
               "rối. Hỏi bốn người cùng một câu, bạn sẽ nhận được bốn câu trả lời khác nhau. Nguyên nhân "
               "chính nằm ở hai chế độ hỏng đã bàn ở trên. Nếu có hai chế độ hỏng thì phải có hai thuật "
               "ngữ hiệu năng khác nhau, mỗi chế độ một thuật ngữ. Làm sao dùng một thuật ngữ như độ khả "
               "dụng để mô tả hiệu năng của hai chế độ hỏng khác nhau? Nếu ai đó nói một chiếc van hỏng "
               "một lần mỗi 10 năm, điều đó thật sự nghĩa là gì? Nếu 10 % số hỏng là “an toàn” (ví dụ "
               "đóng kín) và 90 % là “nguy hiểm” (ví dụ kẹt) thì sao? Nếu tỷ lệ đó đảo lại thì sao? Nếu "
               "hai bên bằng nhau thì sao? Một con số tổng hợp đơn giản là không nói đủ."))
    b.append(p("Một lý do nữa khiến thuật ngữ độ khả dụng gây nhầm lẫn là dải số thường gặp. Con số nào "
               "trên 99 % cũng nghe ấn tượng. Mỗi khi nhà cung cấp PLC đưa ra số liệu hiệu năng, nó luôn "
               "là một chuỗi số 9 dài gần như vô tận. Hãy dừng lại và tự hỏi 99 % và 99,99 % khác nhau có "
               "đáng kể không. Chênh chưa tới 1 %, đúng không? Đúng — nhưng hai con số cũng khác nhau hai "
               "bậc độ lớn! Thật dễ nhầm."))
    b.append(p("Về mặt an toàn, có người thích dùng phần bù của độ khả dụng — độ bất khả dụng — còn gọi là "
               "xác suất hỏng khi có yêu cầu (PFD). Đáng tiếc là những con số này thường nhỏ đến mức phải "
               "dùng ký hiệu khoa học, khiến nhiều người khó hình dung. Mục đích của cả việc này là cung "
               "cấp cho lãnh đạo thông tin có nghĩa để họ ra quyết định sáng suốt. Nói với sếp rằng “thưa "
               "sếp, hệ an toàn của chúng ta có PFD là 2,3 × 10⁻⁴!” liệu có nghĩa hay có ích không? Chắc "
               "chắn câu đầu tiên của vị ấy sẽ là: “Ừ, thế là tốt hay xấu?”"))
    b.append(p("Hãy xét biểu đồ tròn ở Hình 8-2. Phần một phần ba phía trên bên phải là chỗ hệ an toàn "
               "đang làm việc đúng và nhà máy đang chạy, đang sản xuất. Trong trường hợp này cả SIS và nhà "
               "máy đều khả dụng. Dùng chữ “độ khả dụng” ở đây có vẻ hợp lý."))
    b.append(p("Ở phần dưới, SIS bị cắt nhầm và dừng nhà máy. Trong trường hợp này cả hai đều không khả "
               "dụng. (Phải thừa nhận rằng bạn còn phải khởi động lại SIS trước khi khởi động được nhà "
               "máy, nên hai thứ không hoàn toàn giống nhau — nhưng như thế là bắt bẻ.) Dùng chữ “độ khả "
               "dụng” (hay “độ bất khả dụng”) vẫn có vẻ hợp lý."))
    b.append(p("Tuy nhiên, trường hợp mà hầu hết mọi người không hề biết là phần trên bên trái: SIS không "
               "hoạt động (ví dụ PLC kẹt trong vòng lặp vô hạn, đầu ra còn điện và kẹt ở trạng thái bật…) "
               "nên SIS không khả dụng, nhưng nhà máy vẫn đang chạy. Kiểu hỏng này không dừng nhà máy. Nhà "
               "máy vẫn khả dụng, vẫn sản xuất, và hoàn toàn không biết rằng SIS sẽ không hoạt động khi "
               "cần. Trong trường hợp này, “độ khả dụng” của hai hệ (SIS và nhà máy) rõ ràng không giống "
               "nhau."))
    b.append(p("Điều này cũng cho thấy không nên gộp hai thước đo hiệu năng khác nhau vào một thuật ngữ "
               "(như một độ khả dụng tổng hợp), vì tác động của mỗi kiểu hỏng hoàn toàn khác nhau. Lấy "
               "trung bình của 99,999 % ở chế độ an toàn và 94,6 % ở chế độ nguy hiểm thì gần như vô "
               "nghĩa. Đáp án cuối cùng sẽ nói với bạn điều gì? Không gì cả."))
    b.append(p("Thuật ngữ chung “độ khả dụng” chỉ đơn giản là thời gian hoạt động chia cho tổng thời "
               "gian. Vậy độ khả dụng 99,99 % thật sự có thể nghĩa là gì? Hệ có thể cắt nhầm mỗi tháng "
               "một lần và chỉ dừng 4,3 phút. Hệ có thể cắt mỗi năm một lần và dừng 53 phút. Hệ có thể "
               "cắt mười năm một lần và dừng 8,8 giờ. Cả ba đều cho ra 99,99 %. Đây không phải loại thông "
               "tin mà hầu hết người dùng thật sự muốn biết."))
    b.append(p("Một thuật ngữ tốt hơn cho hiệu năng chống cắt nhầm là <b>thời gian trung bình tới lần cắt "
               "nhầm</b> (MTTF<sub>spurious</sub>). Thuật ngữ này được đưa ra trong một báo cáo kỹ thuật "
               "của ISA SP84. [Ref. 11] Nói cách khác: trung bình bao lâu hệ gây một lần cắt nhầm — 5 "
               "năm, 50 năm hay 500 năm một lần? Người dùng biết quá trình của họ sẽ dừng bao lâu khi bị "
               "cắt nhầm. Họ chỉ muốn biết nó xảy ra thường đến mức nào."))
    b.append(p("Một thuật ngữ tốt hơn cho hiệu năng ở chế độ nguy hiểm là <b>hệ số giảm rủi ro</b> (RRF), "
               "là nghịch đảo của xác suất hỏng khi có yêu cầu (PFD). Khác biệt giữa 0,1 và 0,001 rất khó "
               "hình dung hay cảm nhận. Nhưng khác biệt giữa 10 và 1.000 thì rõ ràng."))
    b.append(fig(2, F.fig_8_2(), "vi"))

    b.append(h3("8.5.1 Suất hỏng, MTBF và tuổi thọ", "Failure Rate, MTBF, and Life"))
    b.append(p("Suất hỏng được định nghĩa là số hư hỏng mỗi đơn vị thời gian. Chữ Hy Lạp λ thường dùng để "
               "biểu thị suất hỏng. Đường cong bồn tắm (Hình 8-3) cho thấy suất hỏng không cố định suốt "
               "đời thiết bị. Đường cong này được chấp nhận rộng rãi cho thiết bị điện tử. Phần mềm và "
               "thiết bị cơ khí có đường cong hơi khác."))
    b.append(p("Phần bên trái của đường cong thể hiện ảnh hưởng của hư hỏng “mồi tử”: linh kiện khuyết "
               "tật chết sớm. Phần bên phải thể hiện hư hỏng do “mòn”. Với hầu hết thiết bị, người ta giả "
               "định suất hỏng không đổi, thể hiện bằng đoạn phẳng ở giữa. Giả định đơn giản này vẫn là đề "
               "tài tranh luận sôi nổi trong giới độ tin cậy. Ít nhất nó cũng làm phép toán đơn giản đi. "
               "Có ý kiến cho rằng những thiết bị như van không tuân theo đường cong ấy: van để càng lâu ở "
               "một vị trí càng dễ kẹt. Có thể đúng, nhưng cho đến khi ngành có mô hình và số liệu chính "
               "xác hơn thì đành chấp nhận đơn giản hoá. Vì hầu hết các đánh giá chỉ cần độ chính xác cỡ "
               "bậc độ lớn, điều này thường không thành vấn đề."))
    b.append(p("Các cơ sở dữ liệu thường liệt kê suất hỏng theo đơn vị số hư hỏng mỗi triệu giờ. Một kỹ sư "
               "độ tin cậy có thể thấy thoải mái với 1,5 hư hỏng mỗi triệu giờ, nhưng ít người khác thì "
               "không. Phần lớn thích nghịch đảo của suất hỏng — thời gian trung bình giữa hai lần hỏng "
               "(MTBF) — với đơn vị là năm. Biết rằng hai thuật ngữ chỉ là nghịch đảo của nhau và một năm "
               "có 8.760 giờ, suất hỏng 1,5 × 10⁻⁶ cho ra MTBF 76 năm."))
    b.append(p("Có người tranh luận về khác biệt giữa thời gian trung bình tới lần hỏng (MTTF) và thời "
               "gian trung bình giữa hai lần hỏng (MTBF). Theo truyền thống, MTTF dùng cho linh kiện thay "
               "thế được (ví dụ điện trở), còn MTBF dùng cho hệ sửa chữa được (ví dụ máy bay). MTBF cũng "
               "có thể coi là tổng hợp của MTTF và thời gian sửa chữa trung bình (MTTR). Xét rằng MTBF "
               "thường tính bằng năm còn MTTR thường tính bằng giờ, có thể thấy khác biệt giữa MTTF và "
               "MTBF thường không đáng tranh cãi. Để nhất quán, chương này dùng MTBF."))
    b.append(p("Nhiều người coi MTBF và “tuổi thọ” là một. Ví dụ, nếu một thiết bị có MTBF 30 năm, nhiều "
               "người nghĩ thiết bị ấy sống trung bình 30 năm rồi hỏng. Không đúng. MTBF 3.000 năm có thể "
               "là con số hoàn toàn hợp lý cho một thiết bị, dù không ai mong thiết bị ấy sống 3.000 năm. "
               "Con số chỉ có nghĩa rằng trong tổng số 3.000 thiết bị, có một chiếc hỏng trong vòng một "
               "năm. Nó chỉ là một trung bình thống kê. Không thể dự đoán chiếc nào hỏng, và hỏng lúc nào "
               "trong khoảng thời gian đó. Một ví dụ kinh điển cho thấy MTBF và tuổi thọ không giống nhau "
               "là que diêm. Với diêm khô và thao tác đúng, hầu như không có lần nào hỏng. Vì thế suất "
               "hỏng (số lần hỏng mỗi đơn vị thời gian) sẽ thấp. Suất hỏng thấp thì nghịch đảo của nó — "
               "MTBF — sẽ lớn, có thể tới vài phút với một que diêm. Nhưng que diêm chỉ cháy, tức chỉ "
               "sống, được vài giây."))
    b.append(fig(3, F.fig_8_3(), "vi"))

    # ------------------------------------------------------------------ 8.6
    b.append(h2("8.6 Mức độ chính xác của mô hình", "Degree of Modeling Accuracy"))
    b.append(p("Mọi phân tích độ tin cậy đều dựa trên số liệu suất hỏng. Phải nhận rằng loại số liệu này "
               "rất biến động. Giả định rằng những linh kiện được cho là giống hệt nhau, hoạt động trong "
               "điều kiện môi trường và vận hành được cho là giống hệt nhau, là giả định không thực tế. "
               "Với một mức chi tiết cho trước, độ chính xác bề ngoài mà một số phương pháp mô hình hoá "
               "đem lại không tương xứng với độ chính xác của số liệu suất hỏng. Từ đó có thể kết luận "
               "rằng những đánh giá đơn giản hoá và những mô hình tương đối đơn giản là đủ."))
    b.append(p("Những dự báo chính xác hơn có thể vừa gây nhầm lẫn, vừa là sự lãng phí thời gian, tiền bạc "
               "và công sức. Trong bất kỳ ngành kỹ thuật nào, khả năng nhận ra mức chính xác cần thiết là "
               "điều cốt yếu. Vì các thông số độ tin cậy có dung sai rộng, phải đưa ra phán đoán ở độ "
               "chính xác một, cùng lắm là hai, con số có nghĩa. Lợi ích đến từ phán đoán và hành động "
               "tiếp theo, không đến từ việc làm mịn phép tính. [Ref. 4]"))
    b.append(p("Đơn giản hoá và xấp xỉ có ích khi chúng làm giảm độ phức tạp và giúp mô hình trở nên hiểu "
               "được. [Ref. 14] Ví dụ, nếu một mô hình đơn giản cho biết hệ số giảm rủi ro của một hệ là "
               "55, thì gần như chẳng có lý do gì để bỏ thêm một bậc độ lớn thời gian và công sức, hoặc "
               "thuê tư vấn ngoài, để dựng một mô hình cho ra hệ số giảm rủi ro là 60. Cả hai đáp án đều "
               "nằm giữa dải SIL 1 (hệ số giảm rủi ro từ 10 đến 100)."))

    # ------------------------------------------------------------------ 8.7
    b.append(h2("8.7 Các phương pháp mô hình hoá", "Modeling Methods"))
    b.append(quote("Quản lý nhiều dữ liệu bắt đầu bằng một dạng đơn giản hoá nào đó.", "Megill"))
    b.append(quote("Càng ít hiểu một hiện tượng, ta càng cần nhiều biến để giải thích nó.",
                   "L. Branscomb"))
    b.append(p("Có nhiều phương pháp ước lượng hiệu năng của hệ. Một số phương pháp phổ biến hơn là sơ đồ "
               "khối độ tin cậy, cây lỗi và mô hình Markov."))

    b.append(h3("8.7.1 Sơ đồ khối độ tin cậy", "Reliability Block Diagrams"))
    b.append(p("Sơ đồ khối độ tin cậy (RBD) đúng nghĩa là sơ đồ. Công dụng của nó là giúp làm rõ cấu hình "
               "và cách vận hành của hệ. Hình 8-4 là một ví dụ. Trong trường hợp này, hệ sẽ hỏng nếu A, B "
               "hoặc G hỏng. Các mục C và D, cũng như E và F, là dự phòng. Hệ chỉ hỏng nếu cả C và D, "
               "hoặc cả E và F, cùng hỏng một lúc. Các công thức thường gắn với sơ đồ khối độ tin cậy chỉ "
               "đơn giản là cộng hoặc nhân xác suất của các khối. Với giả định xác suất nhỏ, ta cộng xác "
               "suất các mục nối tiếp (A, B và G) và nhân xác suất các mục song song (C với D, E với F). "
               "Nói chung, sơ đồ khối và phép toán kèm theo không xử lý được các biến phụ thuộc thời gian "
               "như thời gian sửa chữa, chu kỳ thử, chẩn đoán, và những hệ dự phòng phức tạp hơn. Tuy "
               "vậy, có thể dùng công thức phức tạp hơn để tính xác suất hỏng của từng khối."))
    b.append(fig(4, F.fig_8_4(), "vi"))

    b.append(h3("8.7.2 Cây lỗi", "Fault Trees"))
    b.append(p("Cây lỗi dựa trên tổ hợp các cổng VÀ và HOẶC. Hình 8-5 là một ví dụ với cổng HOẶC. Tương tự "
               "sơ đồ khối độ tin cậy, xác suất của các biến cố cơ bản được cộng hoặc nhân qua các cổng: "
               "cộng qua cổng HOẶC, nhân qua cổng VÀ. Vòng tròn biểu thị biến cố cơ bản, hình chữ nhật "
               "dùng cho phần mô tả. Cây lỗi rất tốt để mô hình hoá toàn bộ hệ an toàn, kể cả thiết bị "
               "trường. Ví dụ ở Hình 8-5 cho thấy nếu cảm biến cháy, tủ báo cháy hoặc bơm chữa cháy không "
               "hoạt động khi cần thì hệ sẽ hỏng. Tuy nhiên cây lỗi chỉ có giá trị hạn chế khi mô hình "
               "hoá hệ logic, vì — giống sơ đồ khối — chúng không tính đến các yếu tố phụ thuộc thời "
               "gian. Như với sơ đồ khối, có thể dùng công thức phức tạp hơn để tính xác suất của các "
               "biến cố cơ bản. Ngoài ra, cây lỗi — như mọi mô hình — chỉ tính đến những biến cố đã "
               "biết. Nói cách khác, nếu bạn còn không biết có một kiểu hỏng nào đó thì dĩ nhiên không thể "
               "đưa nó vào cây lỗi."))
    b.append(fig(5, F.fig_8_5(), "vi"))

    b.append(h3("8.7.3 Mô hình Markov", "Markov Models"))
    b.append(p("Nhiều người làm độ tin cậy đã chọn mô hình Markov. Mô hình hoá Markov dùng sơ đồ chuyển "
               "trạng và đại số ma trận. Hình 8-6 là một ví dụ tương đối đơn giản. Mô hình Markov khá linh "
               "hoạt. Đáng tiếc là ít người dùng được kỹ thuật này, và những người dùng được thường có "
               "bằng cấp cao."))
    b.append(p("Các phép đơn giản hoá đại số cho mô hình Markov đã có từ nhiều thập kỷ (được phát triển "
               "trong Tài liệu 5 và liệt kê trong Tài liệu 11 và 12). Những “công thức đơn giản hoá” này "
               "thường được gắn với sơ đồ khối độ tin cậy, nhưng hoàn toàn có thể đưa vào cây lỗi dễ như "
               "nhau."))
    b.append(fig(6, F.fig_8_6(), "vi"))

    # ------------------------------------------------------------------ 8.8
    b.append(h2("8.8 Ảnh hưởng thật của dự phòng", "The Real Impact of Redundancy"))
    b.append(p("Hai kênh không phải lúc nào cũng tốt hơn một, và ba kênh không phải lúc nào cũng tốt hơn "
               "hai. Lạ nhưng đúng. Hãy xem Hình 8-7 trong phần thảo luận dưới đây."))
    b.append(p("Bắt đầu với trường hợp gốc: một hệ đơn (không dự phòng), có thể gọi là 1oo1 "
               "(một-trong-một). Một ví dụ về hư hỏng an toàn là tiếp điểm rơ-le mở ra, ngắt điện hệ và "
               "gây cắt nhầm. Giả sử xác suất hỏng ở chế độ này là 0,04. Nghĩa là trong một khoảng thời "
               "gian cho trước (ví dụ 1 năm), hệ có 4 % xác suất bị cắt nhầm. Có thể hình dung là 4 hệ "
               "trong 100 bị cắt nhầm trong một năm, hay 1 hệ trong 25, hay MTTF(an toàn) là 25 năm. Ở "
               "giai đoạn này, các con số chỉ để so sánh."))
    b.append(p("Một ví dụ về hư hỏng nguy hiểm là tiếp điểm rơ-le bị hàn dính và không hoạt động khi cần. "
               "Giả sử xác suất hỏng ở chế độ này là 0,02. Nghĩa là trong một khoảng thời gian cho trước "
               "(ví dụ 1 năm), hệ có 2 % xác suất không hoạt động đúng khi có yêu cầu (tức khi có tình "
               "trạng nguy hiểm mà hệ phải phản ứng). Có thể hình dung là 2 hệ trong 100 không phản ứng "
               "trong một năm, hay 1 trong 50, hay MTTF(nguy hiểm) là 50 năm. Có thể cho hai số an toàn "
               "và nguy hiểm bằng nhau, đổi chỗ cho nhau, hoặc đổi bậc độ lớn — thật sự không quan trọng. "
               "Mục đích chỉ là minh hoạ ảnh hưởng của dự phòng."))
    b.append(p("Một hệ đôi 1oo2 (một-trong-hai) có đầu ra đấu nối tiếp (giả định tiếp điểm đóng và có "
               "điện). Một-trong-hai nghĩa là hệ chỉ cần một kênh để thực hiện việc dừng, nên mới có tên "
               "ấy. Nếu kênh nào cũng có thể dừng hệ, và lượng phần cứng gấp đôi, thì số lần cắt nhầm "
               "cũng gấp đôi. Vì thế 0,04 thành 0,08. Có thể hình dung là 8 hệ trong 100 bị cắt nhầm "
               "trong một năm, hay 1 hệ trong 12,5, hay MTTF(an toàn) là 12,5 năm."))
    b.append(p("Ở chế độ nguy hiểm, hệ này chỉ không hoạt động nếu cả hai kênh cùng hỏng nguy hiểm một "
               "lúc. Nếu một kênh kẹt, kênh kia vẫn ngắt điện và dừng được hệ. Xác suất hai hư hỏng đồng "
               "thời là bao nhiêu? Thật ra rất đơn giản. Xác suất một đồng xu ra mặt ngửa là bao nhiêu? "
               "50 %. Xác suất hai đồng xu cùng ra ngửa? 25 %. Đó chính là xác suất của một biến cố đem "
               "bình phương (0,5 × 0,5 = 0,25). Vậy xác suất hai kênh hỏng cùng lúc là rất nhỏ (0,02 × "
               "0,02 = 0,0004). Có thể hình dung là 4 hệ trong 10.000 không phản ứng trong một năm, hay 1 "
               "trong 2.500, hay MTTF(nguy hiểm) là 2.500 năm."))
    b.append(p("Nói cách khác, hệ 1oo2 rất an toàn (xác suất hỏng nguy hiểm rất nhỏ), nhưng hệ bị cắt "
               "nhầm gấp đôi so với hệ đơn — điều không mong muốn vì mất sản lượng."))
    b.append(p("Một hệ đôi 2oo2 (hai-trong-hai) có đầu ra đấu song song. Ở đây cả hai kênh đều phải ngắt "
               "điện thì mới dừng được hệ. Hệ này sẽ không hoạt động nếu một kênh hỏng nguy hiểm. Vì hệ "
               "có lượng phần cứng gấp đôi hệ đơn, nó có số hư hỏng nguy hiểm gấp đôi. Vì thế 0,02 thành "
               "0,04. Có thể hình dung là 4 hệ trong 100 không phản ứng trong một năm, hay 1 trong 25, "
               "hay MTTF(nguy hiểm) là 25 năm."))
    b.append(p("Để hệ này bị cắt nhầm, cả hai kênh phải cùng hỏng an toàn một lúc. Như trước, xác suất "
               "hai hư hỏng đồng thời là xác suất một biến cố đem bình phương. Vì thế cắt nhầm ở hệ này "
               "khó xảy ra (0,04 × 0,04 = 0,0016). Có thể hình dung là 16 hệ trong 10.000 bị cắt nhầm "
               "trong một năm, hay 1 hệ trong 625, hay MTTF(an toàn) là 625 năm."))
    b.append(p("Vậy hệ 2oo2 chống cắt nhầm tốt (xác suất hư hỏng an toàn rất nhỏ), nhưng hệ kém an toàn "
               "hơn hệ đơn — điều không mong muốn vì lý do an toàn. Điều này không có nghĩa hệ 2oo2 là "
               "“xấu” hay không nên thiết kế. Nếu PFD (con số ta quan tâm vì lý do an toàn) đáp ứng yêu "
               "cầu an toàn tổng thể thì thiết kế ấy chấp nhận được."))
    b.append(p("Hệ ba kênh dự phòng (TMR) được phát triển từ những năm 1970 và ra thị trường vào đầu và "
               "giữa những năm 1980. Lý do của việc làm ba kênh hồi đó rất đơn giản: những hệ dựa trên "
               "máy tính thời đầu có chẩn đoán hạn chế. Ví dụ, nếu chỉ có hai tín hiệu và chúng không "
               "khớp nhau, không phải lúc nào cũng xác định được tín hiệu nào đúng. Thêm kênh thứ ba giải "
               "quyết vấn đề: có thể giả định kênh không khớp là kênh sai, và nó bị hai kênh kia bỏ phiếu "
               "áp đảo."))
    b.append(p("Hệ 2oo3 (hai-trong-ba) là hệ bỏ phiếu theo đa số. Hai kênh trở lên nói gì thì hệ làm "
               "theo. Điều khiến người ta ngạc nhiên lúc đầu là hệ 2oo3 có tỷ lệ cắt nhầm cao hơn hệ "
               "2oo2, và xác suất không hoạt động lớn hơn hệ 1oo2. Có người thoạt đầu nói: “Khoan đã, "
               "không thể thế được!” Thật ra nó hiển nhiên, chỉ cần nghĩ một chút. Hệ 1oo2 cần bao nhiêu "
               "hư hỏng đồng thời để hỏng nguy hiểm? Hai. Hệ 2oo3 cần bao nhiêu hư hỏng đồng thời để hỏng "
               "nguy hiểm? Hai. À há! Hệ ba kênh có nhiều phần cứng hơn, nên có gấp ba tổ hợp hỏng kép! "
               "(A+B, A+C, B+C) Hệ 2oo2 cần bao nhiêu hư hỏng đồng thời để bị cắt nhầm? Hai. Hệ 2oo3 cần "
               "bao nhiêu hư hỏng đồng thời để bị cắt nhầm? Hai. Cũng vậy: hệ ba kênh có gấp ba tổ hợp "
               "hỏng kép. Hệ ba kênh thật ra là một sự đánh đổi. Nhìn tổng thể, nó tốt ở cả hai chế độ, "
               "nhưng không tốt bằng hai hệ đôi chuyên biệt. Trong khi đó, một hệ đôi truyền thống chỉ "
               "tốt ở chế độ này hoặc chế độ kia, không tốt cả hai."))
    b.append(p("Nhìn kỹ các con số ở Hình 8-7, có thể thấy hệ 1oo2 an toàn hơn 2oo3, và hệ 2oo2 chống "
               "cắt nhầm tốt hơn 2oo3. Về lý thuyết, nếu một hệ đôi được thiết kế để đạt hiệu năng tốt "
               "nhất của cả hai hệ đôi thì hệ ấy thật ra có thể vượt cả hệ ba kênh."))
    b.append(p("Những tiến bộ về phần cứng và phần mềm từ đầu thập niên 1980 nghĩa là hư hỏng trong hệ "
               "dựa trên máy tính hai kênh nay có thể được chẩn đoán đủ tốt để biết kênh nào đúng khi hai "
               "kênh không khớp. Điều này có nghĩa không còn cần làm ba kênh nữa. Ngành gọi thiết kế đôi "
               "mới hơn này là 1oo2D. [Ref. 15] Có lẽ lợi ích đáng kể nhất với các nhà cung cấp hệ 1oo2D "
               "là việc hệ của họ được các tổ chức độc lập (như TÜV và FM) chứng nhận đạt cùng mức hiệu "
               "năng với hệ TMR. Đáng tiếc là chứng nhận an toàn không bao gồm hiệu năng chống cắt nhầm. "
               "Vì thế các nhà cung cấp TMR tấn công đối thủ đôi ở đúng điểm ấy."))
    b.append(fig(7, F.fig_8_7(), "vi"))

    # ------------------------------------------------------------------ 8.9
    b.append(h2("8.9 Các công thức cơ bản", "Basic Formulas"))
    b.append(p("Các phép đơn giản hoá đại số cho mô hình Markov đã có từ nhiều thập kỷ. Lý thuyết đằng sau "
               "những công thức dưới đây được trình bày trong Tài liệu 5. Công thức tương tự cũng có trong "
               "Tài liệu 11 và 12. Chúng thường được gọi là “công thức đơn giản hoá” và thường được gắn "
               "với sơ đồ khối độ tin cậy. Điều đó thật ra không đúng, vì các công thức này cũng có thể "
               "đưa vào cây lỗi dễ như nhau."))
    b.append(p("Bộ công thức thứ nhất dùng để tính thời gian trung bình tới lần cắt nhầm "
               "(MTTF<sub>spurious</sub>):"))
    b.append(eq("MTTF<sub>spurious</sub> — 1oo1: 1 / λ<sub>s</sub>", "8.1"))
    b.append(eq("1oo2: 1 / (2 · λ<sub>s</sub>)", "8.2"))
    b.append(eq("2oo2: 1 / (2 · (λ<sub>s</sub>)² · MTTR)", "8.3"))
    b.append(eq("2oo3: 1 / (6 · (λ<sub>s</sub>)² · MTTR)", "8.4"))
    b.append(p("trong đó: MTTR là thời gian sửa chữa trung bình; λ là suất hỏng (1/MTBF); chỉ số s là hư "
               "hỏng an toàn. 1oo1 nghĩa là 1 trong 1, 2oo3 nghĩa là 2 trong 3…"))
    b.append(p("Các công thức trên đúng khi tốc độ sửa chữa lớn hơn nhiều so với suất hỏng (1/MTTR ≫ λ), "
               "hay nói cách khác khi MTBF lớn hơn nhiều so với MTTR. Chúng dựa trên giả định rằng hư hỏng "
               "an toàn đều bộc lộ trong mọi hệ, kể cả từng kênh riêng của cấu hình 2oo2 và 2oo3 (ví dụ "
               "qua một dạng báo động sai lệch). Nói cách khác, không có hư hỏng an toàn nào bị ẩn."))
    b.append(p("Xác suất hỏng trung bình khi có yêu cầu (PFD<sub>avg</sub>) được tính từ suất hỏng nguy "
               "hiểm, ẩn và chu kỳ thử bằng tay. Cũng có thể tính PFD của hư hỏng nguy hiểm phát hiện được "
               "(bằng công thức hơi khác), nhưng ảnh hưởng của chúng lên đáp án cuối cùng là không đáng "
               "kể, thường nhỏ hơn một bậc độ lớn. Vì thế có thể bỏ qua ảnh hưởng của hư hỏng nguy hiểm "
               "phát hiện được trong tính toán."))
    b.append(eq("PFD<sub>avg</sub> — 1oo1: λ<sub>du</sub> · (TI / 2)", "8.5"))
    b.append(eq("1oo2: ((λ<sub>du</sub>)² · (TI)²) / 3", "8.6"))
    b.append(eq("2oo2: λ<sub>du</sub> · TI", "8.7"))
    b.append(eq("2oo3: (λ<sub>du</sub>)² · (TI)²", "8.8"))
    b.append(p("trong đó: TI là chu kỳ thử bằng tay; λ<sub>du</sub> là suất hỏng nguy hiểm, ẩn. Các công "
               "thức trên đúng khi MTBF (1/λ<sub>du</sub>) lớn hơn nhiều so với TI."))

    b.append(h3("8.9.1 Ảnh hưởng của thời gian thử bằng tay", "Impact Due to Manual Test Duration"))
    b.append(p("Nếu thử một hệ an toàn khi đang vận hành (tức là khi quá trình vẫn đang chạy), phải đặt "
               "một phần hệ an toàn vào bypass để tránh dừng nhà máy. Độ dài thời gian thử bằng tay có thể "
               "ảnh hưởng đáng kể đến hiệu năng tổng thể của hệ an toàn. Trong lúc thử, hệ đơn (không dự "
               "phòng) buộc phải ngừng hoạt động: độ khả dụng của nó trong thời gian thử bằng không. Hệ dự "
               "phòng thì không phải đặt toàn bộ vào bypass khi thử. Có thể đặt từng nhánh của hệ đôi vào "
               "bypass một lúc. Thực chất, hệ đôi bị giảm xuống thành hệ đơn trong lúc thử, và hệ ba kênh "
               "bị giảm xuống thành hệ đôi. Các công thức sau (cho PFD<sub>avg</sub>) được phát triển trong "
               "Tài liệu 4 để tính đến việc thử khi đang vận hành. PFD từ các công thức này chỉ việc cộng "
               "vào PFD tính từ các công thức phía trên."))
    b.append(eq("1oo1: TD / TI", "8.9"))
    b.append(eq("1oo2: 2 · TD · λ<sub>d</sub> · (((TI / 2) + MTTR) / TI)", "8.10"))
    b.append(eq("2oo2: 2 · (TD / TI)", "8.11"))
    b.append(eq("2oo3: 6 · TD · λ<sub>d</sub> · (((TI / 2) + MTTR) / TI)", "8.12"))
    b.append(p("trong đó: TD là thời gian thử; TI là chu kỳ thử."))

    # ------------------------------------------------------------------ 8.10
    b.append(h2("8.10 Phân tích một hệ rơ-le", "Analysis of a Relay System"))
    b.append(p("Trước hết phải giả định suất hỏng (hay MTBF) của rơ-le. Các sổ tay số liệu cho thấy một "
               "dải rất rộng cho các loại rơ-le khác nhau. Ta có thể giả định MTBF 100 năm cho một rơ-le "
               "công nghiệp."))
    b.append(p("Tiếp theo phải xét xem đưa bao nhiêu rơ-le vào phép tính. Giả sử mỗi đầu vào và mỗi đầu "
               "ra của hệ có một rơ-le. Giả sử đây là một nhóm khoá liên động tương đối nhỏ: chỉ tám đầu "
               "vào (ví dụ công tắc cao và thấp cho áp suất, nhiệt độ, mức và lưu lượng) và hai đầu ra (ví "
               "dụ hai van). Hệ sẽ bị cắt nhầm nếu bất kỳ rơ-le nào trong mười chiếc hỏng ở trạng thái hở "
               "mạch. Vì thế ta chỉ việc cộng suất hỏng an toàn của mười rơ-le. Nhớ rằng MTBF = 1/λ. Giả "
               "sử rơ-le có 98 % hư hỏng theo hướng an toàn:"))
    b.append(eq("MTTF<sub>spurious</sub> = 1 / λ<sub>s</sub> = 1 / ((1/100 năm) · 0,98 · 10) = 10,2 năm",
                "8.13"))
    b.append(p("(0,98 là tỷ lệ chế độ hỏng an toàn, 10 là số lượng rơ-le.) Chỉ nên lấy hai con số có "
               "nghĩa: 10 năm."))
    b.append(p("Với phép tính PFD<sub>avg</sub>, cần chia nhỏ đầu vào/ra hơn nữa. Khi có yêu cầu dừng đặt "
               "lên hệ, yêu cầu ấy chỉ đến từ <em>một</em> đầu vào. Ví dụ chỉ có khoá dừng do áp suất cao "
               "vào báo động, chứ không phải cả tám đầu vào cùng lúc. Ngoài ra, SIL được xác định cho từng "
               "chức năng riêng, nên chỉ nên mô hình PFD của một chức năng duy nhất. Vì thế trong mô hình "
               "này chỉ nên tính một đầu vào và cả hai đầu ra — tổng cộng ba rơ-le. Lưu ý rằng vì rơ-le "
               "không có chẩn đoán tự động, mọi hư hỏng nguy hiểm đều là nguy hiểm, ẩn."))
    b.append(eq("PFD<sub>avg</sub> = λ<sub>du</sub> · (TI / 2) = (1/100 năm) · 0,02 · 3 · (1 năm / 2) = "
                "3,00 × 10⁻⁴", "8.14"))
    b.append(p("(0,02 là tỷ lệ chế độ hỏng nguy hiểm, 3 là số lượng rơ-le.) Từ đó:"))
    b.append(eq("RRF = 1 / 3,00 × 10⁻⁴ = 3.300", "8.15"))
    b.append(eq("SA = 1 − 3,00 × 10⁻⁴ = 0,9997 = 99,97 %", "8.16"))

    # ------------------------------------------------------------------ 8.11
    b.append(h2("8.11 Phân tích một hệ PLC không dự phòng", "Analysis of a Non-redundant PLC System"))
    b.append(p("Nếu thay hệ rơ-le bằng một PLC đa dụng thì sao? Để nhất quán với số điểm vào/ra của ví dụ "
               "rơ-le, có thể xét một PLC với một mô-đun vào và một mô-đun ra. Đừng cố chia phép tính "
               "xuống từng kênh của một mô-đun, vì trên một bo mạch thường có những linh kiện dùng chung "
               "có thể làm hỏng cả mô-đun."))
    b.append(p("Giả sử: MTBF của CPU = 10 năm; MTBF của mô-đun vào/ra = 50 năm; tỷ lệ chế độ hỏng an toàn "
               "của CPU = 60 %; tỷ lệ chế độ hỏng an toàn của mô-đun vào/ra = 75 %."))
    b.append(p("Cũng có thể giả định bộ nguồn dự phòng đôi. Xác suất hai bộ nguồn hỏng đồng thời thấp hơn "
               "các thành phần đơn cả bậc độ lớn, nên thực chất có thể bỏ qua trong mô hình."))
    b.append(eq("MTTF<sub>spurious</sub> = 1 / λ<sub>s</sub> = 1 / (((1/10) · 0,6) + ((1/50) · 0,75 · 2)) "
                "= 11 năm", "8.17"))
    b.append(p("(0,6 và 0,75 là tỷ lệ chế độ hỏng an toàn, 2 là số mô-đun vào/ra.)"))
    b.append(p("Bây giờ giả sử độ phủ chẩn đoán của CPU là 90 % và của mô-đun vào/ra là 50 %. Phép tính "
               "sau giả định PLC thật sự được thử bằng tay hằng năm."))
    b.append(eq("PFD<sub>avg</sub> = [((1/10) · 0,4 · 0,1) + ((1/50) · 2 · 0,25 · 0,5)] · (1 năm / 2) = "
                "4,5 × 10⁻³", "8.18"))
    b.append(p("(suất hỏng CPU, tỷ lệ chế độ hỏng nguy hiểm, phần ẩn) + (suất hỏng mô-đun vào/ra, số "
               "lượng, tỷ lệ chế độ hỏng, phần ẩn). Từ đó:"))
    b.append(eq("RRF = 1 / (4,5 × 10⁻³) = 220", "8.19"))
    b.append(eq("SA = 1 − 4,5 × 10⁻³ = 0,9955 = 99,55 %", "8.20"))
    b.append(p("Vậy hiệu năng chống cắt nhầm xấp xỉ như rơ-le, nhưng PLC kém an toàn hơn rơ-le một bậc độ "
               "lớn! Điều này thường làm nhiều người ngạc nhiên. Hãy nhớ rằng ta đang giả định PLC thật sự "
               "được thử toàn bộ bằng tay mỗi năm một lần — một giả định lạc quan quá mức với nhiều hệ. Độ "
               "phủ chẩn đoán 50 % cho mô-đun vào/ra cũng là giả định lạc quan với nhiều hệ đa dụng."))
    b.append(p("Điều này không nói xấu gì PLC. PLC đa dụng tốt cho đúng việc chúng được thiết kế để làm: "
               "điều khiển. Đơn giản là chúng không được thiết kế cho an toàn. Người dùng nên lấy số liệu "
               "phù hợp từ nhà cung cấp để mô hình hoá hệ. Tiêu chuẩn quy định nhà cung cấp <em>phải</em> "
               "cung cấp thông tin đó."))

    # ------------------------------------------------------------------ 8.12
    b.append(h2("8.12 Phân tích một hệ TMR", "Analysis of a TMR System"))
    b.append(p("Các MTBF và tỷ lệ chế độ hỏng giả định cho PLC vẫn hợp lý để dùng cho hệ ba kênh dự phòng "
               "bỏ phiếu 2oo3 (TMR). Phần cứng về cơ bản giống nhau, chỉ nhiều hơn, và có khả năng chẩn "
               "đoán tốt hơn. Như PLC, hệ TMR có bộ nguồn dự phòng, ban đầu có thể bỏ qua trong mô hình."))
    b.append(p("Với hệ TMR, có thể gộp mô-đun vào, CPU và mô-đun ra thành một kênh của hệ ba kênh. Điều "
               "này có nghĩa: nếu mô-đun vào số 1 và CPU số 2 cùng hỏng thì hệ hỏng. Một số hệ TMR thật sự "
               "hoạt động như vậy."))
    b.append(eq("MTTF<sub>spurious</sub> = 1 / (6 · (λ<sub>s</sub>)² · MTTR) = 1 / (6 · (0,09)² · "
                "(4 / 8.760)) = 45.000 năm", "8.21"))
    b.append(p("(0,09 là tổng suất hỏng an toàn của một kênh, tính từ 0,6 và 0,75 ở trên; MTTR là 4 giờ "
               "quy ra năm.)"))
    b.append(p("Bây giờ giả sử độ phủ chẩn đoán của cả CPU và mô-đun vào/ra là 99 %. Phép tính sau giả "
               "định hệ TMR thật sự được thử bằng tay hằng năm — điều cũng có thể không bao giờ xảy ra với "
               "một số hệ."))
    b.append(eq("PFD<sub>avg</sub> = (λ<sub>du</sub>)² · (TI)² = 6,25 × 10⁻⁸", "8.22"))
    b.append(eq("RRF = 1 / (6,25 × 10⁻⁸) = 16.000.000", "8.23"))
    b.append(eq("SA = 1 − 6,25 × 10⁻⁸ = 0,9999999375 = 99,99999375 %", "8.24"))
    b.append(p("Các phép tính cho thấy hệ TMR có thời gian trung bình giữa hai lần cắt nhầm là 45.000 năm "
               "và hệ số giảm rủi ro vượt mười triệu! Có thứ gọi là SIL 7 không?! Đáng chú ý là hệ TMR "
               "thậm chí không được chứng nhận để dùng ở SIL 4. Tiêu chuẩn IEC 61508 có một ghi chú cảnh "
               "báo, thực chất đặt trần cho mức hiệu năng có thể tuyên bố. Những con số giảm rủi ro vượt "
               "100.000 thật ra không tồn tại, nhất là với hệ khả trình phức tạp. Vậy phép tính có sai "
               "không? Không hẳn. Chỉ là còn những yếu tố ta chưa tính đến."))

    b.append(h3("8.12.1 Nguyên nhân chung", "Common Cause"))
    b.append(p("Trên thế giới có rất nhiều hệ dự phòng. Đáng tiếc là kinh nghiệm cho thấy chúng không hoạt "
               "động tốt như phép tính ngụ ý. Vấn đề không nằm ở phép tính, mà ở các giả định và ở những "
               "gì được (hoặc không được) đưa vào phép tính."))
    b.append(p("Ai cũng đã nghe câu “rác vào, rác ra”. Như mọi kỹ thuật mô hình hoá, cái gì không đưa vào "
               "mô hình thì sẽ không xuất hiện trong kết quả."))
    b.append(p("Các giả định trong ví dụ TMR ở trên có thể coi là hơi đơn giản. Không có yếu tố nguyên "
               "nhân chung. Nguyên nhân chung có thể định nghĩa là một tác nhân căng thẳng duy nhất đánh "
               "vào nhiều thành phần. Như Hình 8-8, A, B và C là một hệ ba kênh. Tuy nhiên nếu mục D hỏng "
               "thì cả hệ hỏng. Khối D có thể là sai thiết kế, sai lập trình, sai bảo trì, nhiễu điện từ, "
               "hay vấn đề môi trường… Một cách gọi nguyên nhân chung là hệ số Beta. Nó biểu thị phần trăm "
               "hư hỏng ghi nhận trong một nhánh của hệ mà sẽ đánh vào toàn hệ. Hệ số Beta được rút ra từ "
               "các nghiên cứu thực nghiệm. Kỹ thuật ước lượng dải giá trị Beta được mô tả trong Tài liệu "
               "5 và 12. Tài liệu 5 nêu dải Beta điển hình là 20 % khi dùng các thành phần giống hệt nhau "
               "dự phòng (như phần lớn các hệ làm)."))
    b.append(p("Có thể đưa nguyên nhân chung vào mô hình một cách dễ dàng. Chỉ việc lấy một tỷ lệ phần "
               "trăm của suất hỏng tổng của một nhánh trong mỗi chế độ hỏng và mô hình hoá phần đó bằng "
               "công thức 1oo1. Bạn nghĩ chỉ thêm hệ số Beta 1 % vào phép tính thì ảnh hưởng đến đáp án "
               "TMR ở trên là bao nhiêu? Làm với MTTF<sub>spurious</sub>:"))
    b.append(eq("MTTF<sub>spurious</sub> = 1 / (λ<sub>s</sub> · 0,01) = 1 / (0,09 · 0,01) = 1.100 năm",
                "8.25"))
    b.append(p("Nói cách khác, ước lượng 45.000 năm ban đầu là quá lạc quan. Chỉ thêm một hệ số nguyên "
               "nhân chung Beta 1 % đã làm hiệu năng tổng của hệ giảm hơn một bậc độ lớn. Dùng hệ số Beta "
               "10 % thực tế hơn thì đáp án tụt xuống 110 năm. Rõ ràng nguyên nhân chung có thể chi phối "
               "toàn bộ hiệu năng của hệ. Người đọc nên tự làm phép tính PFD<sub>avg</sub> có kể đến "
               "nguyên nhân chung."))
    b.append(p("Một cách khác để tính nguyên nhân chung là quy về hư hỏng hệ thống hay hư hỏng chức năng. "
               "Thay vì thêm một tỷ lệ phần trăm, người ta cộng thẳng một con số suất hỏng vào phần 1oo1 "
               "của công thức. Tuy đã có kỹ thuật được ghi chép để ước lượng hệ số Beta, việc biện minh "
               "cho một suất hỏng hệ thống lại khó hơn."))
    b.append(fig(8, F.fig_8_8(), "vi"))

    # ------------------------------------------------------------------ 8.13
    b.append(h2("8.13 Thiết bị trường", "Field Devices"))
    b.append(p("Mọi ví dụ mô hình hoá ở trên chỉ tính hộp logic. Nhưng yêu cầu hiệu năng nêu trong tiêu "
               "chuẩn lại bao gồm cả thiết bị trường (tức cảm biến và phần tử cuối). Điều đó ảnh hưởng "
               "thế nào?"))
    b.append(p("Hãy xét cùng hệ logic như trước, nhưng lần này có tám đầu vào (cảm biến) và hai đầu ra "
               "(van). Hình dung một bình áp suất có đường vào và đường ra. Tám cảm biến có thể là công "
               "tắc đo giá trị cao và thấp của áp suất, nhiệt độ và mức trong bình, cùng lưu lượng vào "
               "bình. Hai van có thể là van vào và van ra của bình. Logic có thể là: bất kỳ cảm biến nào "
               "vào báo động đều yêu cầu đóng cả hai van. Đây là tám chức năng an toàn (áp suất cao, áp "
               "suất thấp, nhiệt độ cao, nhiệt độ thấp…). Việc các van dùng chung cho mọi chức năng không "
               "thành vấn đề. Mỗi chức năng được thiết kế để chống một mối nguy riêng (ví dụ bình nổ do "
               "áp suất cao, bình bị hút chân không và bẹp do áp suất thấp, một mẻ bị hỏng do nhiệt độ "
               "cao…). Mỗi biến cố nguy hiểm có tần suất, hậu quả và các lớp bảo vệ độc lập riêng (nếu "
               "có). Vì thế mỗi chức năng có mục tiêu SIL riêng (dù có thể tất cả đều là SIL 1)."))
    b.append(p("Giả sử một cảm biến có MTBF an toàn và nguy hiểm là 50 năm, một van có MTBF an toàn và "
               "nguy hiểm là 40 năm. Với cảm biến, điều này có nghĩa trong 50 thiết bị, trong một năm, có "
               "một chiếc gây cắt nhầm, và khi thử hằng năm, có một chiếc được phát hiện là không hoạt "
               "động đúng. Đây là những con số thực tế và có ở nhiều nguồn khác nhau. Giả sử bất kỳ cảm "
               "biến nào cũng có thể gây cắt nhầm (như mô tả ở trên), cả tám đều phải đưa vào mô hình cắt "
               "nhầm. Đóng bất kỳ van nào cũng dừng sản xuất, nên cả hai van đều phải đưa vào mô hình cắt "
               "nhầm. Tổng cộng ví dụ này có mười thiết bị trường."))
    b.append(p("Phần lớn thiết bị trường đang lắp đặt là không dự phòng, kể cả khi dùng với hệ logic TMR. "
               "Để tính MTTF<sub>spurious</sub> tổng của hệ, cần cộng suất hỏng an toàn của mọi thành phần "
               "trong hệ (cảm biến, hộp logic và phần tử cuối). Cây lỗi cho trường hợp này trông giống "
               "Hình 8-5."))
    b.append(eq("MTTF<sub>spurious</sub> = 1 / ((1/50) · 8 + (1/1.100) + (1/40) · 2) = 4,7 năm", "8.26"))
    b.append(p("Nói cách khác, xét về cắt nhầm thì hộp logic TMR không phải là vấn đề — thiết bị trường mới "
               "là. Còn hiệu năng an toàn thì sao? Nhiều thiết bị trường là loại “câm”, không có dạng tự "
               "chẩn đoán nào. Ví dụ công tắc áp suất và van điện từ tiêu chuẩn không cho biết gì khi bị "
               "kẹt. Cây lỗi cho trường hợp này cũng trông giống Hình 8-5. Tuy nhiên, như đã nói, bình "
               "thật ra chứa tám chức năng an toàn. SIL được xác định cho từng chức năng. Vì thế chỉ nên "
               "mô hình một chức năng, trong ví dụ này gồm một cảm biến, hộp logic TMR và cả hai van. Giả "
               "sử thử hằng năm, có thể xác định PFD của hệ bằng cách cộng PFD của ba thành phần."))
    b.append(eq("PFD<sub>avg</sub> của cảm biến = (1/50) · (1 năm / 2) = 0,01", "8.27"))
    b.append(eq("PFD<sub>avg</sub> của hộp logic = 6,25 × 10⁻⁸ (tính ở trên, chưa kể nguyên nhân chung)",
                "8.28"))
    b.append(eq("PFD<sub>avg</sub> của hai van = (1/40) · 2 · (1 năm / 2) = 0,025", "8.29"))
    b.append(eq("PFD<sub>avg</sub> tổng = 3,50 × 10⁻² → RRF = 29 → SA = 96,5 %", "8.30"))
    b.append(p("Đau thật! Nói cách khác, hộp logic TMR của ta — tự nó có thể đáp ứng yêu cầu SIL 3 — khi "
               "ghép với vài thiết bị trường không dự phòng thì chỉ đạt SIL 1 (hệ số giảm rủi ro từ 10 đến "
               "100)!"))
    b.append(p("Một lần nữa, hộp logic TMR không phải nguồn của vấn đề; thiết bị trường mới là. Một hộp "
               "logic không làm nên một hệ thống."))
    b.append(p("Có người sẽ kết luận rằng không cần hệ logic TMR, mà phải tập trung vào thiết bị trường. "
               "Điều đó không hoàn toàn đúng. Đừng đổ cả chậu nước cùng đứa trẻ. Nó chỉ có nghĩa: chuỗi chỉ "
               "bền bằng mắt yếu nhất. Để đáp ứng yêu cầu của những mức toàn vẹn an toàn cao hơn, cần một "
               "trong các yếu tố sau: a) thiết bị trường có tự chẩn đoán; b) thiết bị trường dự phòng; c) "
               "thiết bị có suất hỏng thấp hơn; d) thử thường xuyên hơn… Mọi yếu tố này đều có thể mô hình "
               "hoá bằng các công thức trên. Mục 8.13.1 trình bày một ví dụ như vậy."))
    b.append(p("Cũng có người sẽ kết luận rằng không cần hệ logic đôi hay ba kênh cho ứng dụng SIL 1 hoặc "
               "SIL 2. Điều này cũng không hoàn toàn đúng. Dự báo độ tin cậy là công cụ hữu ích, nhưng "
               "không nên là yếu tố quyết định duy nhất. Không phải mọi thứ đều lượng hoá được. Nếu bạn "
               "đang tìm mua một chiếc ô tô mới, liệu bạn có mua mà không xem, chỉ dựa vào một tờ thông số "
               "một trang, không có cả ảnh hay một lần chạy thử? Có những yếu tố vô hình không diễn đạt "
               "được bằng con số. Tương tự, có những lợi ích của một số hệ an toàn khiến chúng rất phù hợp "
               "cho an toàn, kể cả trong ứng dụng SIL 1."))

    b.append(h3("8.13.1 Thử hành trình một phần cho van", "Partial Stroking of Valves"))
    b.append(p("Như đã nêu ở mục trước, thiết bị trường — nhất là van — thường là mắt yếu nhất trong hệ. "
               "Những lựa chọn truyền thống để cải thiện hiệu năng là dự phòng và/hoặc thử bằng tay thường "
               "xuyên hơn. Với van, cả hai lựa chọn thường không hấp dẫn về mặt tài chính lẫn vận hành. "
               "Van dự phòng, nhất là van lớn, có thể làm tăng mạnh tổng chi phí. Không gian cho van phụ "
               "cũng có thể không có trong một cơ sở đã xây. Thử hành trình toàn phần thường xuyên (ví dụ "
               "hằng quý) thường không khả thi trong quá trình liên tục phải chạy nhiều năm giữa hai lần "
               "bảo dưỡng lớn. Một giải pháp ngày càng phổ biến từ cuối thập niên 1990 là thử hành trình "
               "một phần cho van. Thật vậy, nhiều nhà cung cấp nay chào bán giải pháp đóng gói sẵn."))
    b.append(p("Có thể sửa các công thức trên để tính đến việc thử hành trình một phần. Trước hết xét "
               "trường hợp một van đơn có MTTF nguy hiểm 40 năm và thử hành trình toàn phần hằng năm."))
    b.append(eq("PFD<sub>avg</sub> = λ<sub>du</sub> · TI/2 = (1/40) · (1/2) = 1,25 × 10⁻² → RRF = 80",
                "8.31"))
    b.append(p("Công thức trên giả định van không có chẩn đoán tự động (tức mọi hư hỏng nguy hiểm đều ẩn) "
               "và phép thử có hiệu quả 100 % (tức thử sẽ phát hiện mọi hư hỏng). Kết quả rơi vào dải "
               "SIL 1 (dù đó chỉ là một chiếc van, không phải cả hệ). Tăng chu kỳ thử (tức thử ít hơn) chỉ "
               "làm con số tệ hơn."))
    b.append(p("Một chế độ hỏng của van thường mở là kẹt ở vị trí mở. Thử hành trình một phần sẽ phát hiện "
               "được hỏng hóc đó mà không ảnh hưởng vận hành (tức không đóng van và dừng sản xuất). Có thể "
               "sửa công thức PFD để tính đến việc thử hành trình một phần thường xuyên hơn, dù không hoàn "
               "hảo."))
    b.append(eq("PFD<sub>avg</sub> = (C · λ<sub>d</sub> · TI<sub>1</sub> / 2) + ((1 − C) · λ<sub>d</sub> · "
                "TI<sub>2</sub> / 2)", "8.32"))
    b.append(p("trong đó C là hệ số phủ chẩn đoán; T1 là chu kỳ thử hành trình một phần; T2 là chu kỳ thử "
               "hành trình toàn phần."))
    b.append(p("C — hệ số phủ chẩn đoán — biểu thị phần trăm hư hỏng mà thử hành trình một phần có thể "
               "phát hiện. Con số này gây nhiều tranh cãi. Người ta đã tuyên bố những giá trị từ 60 đến "
               "90 %. Nếu chọn 80 % theo Nguyên lý Pareto (còn gọi là quy tắc 80/20), cùng với thử hành "
               "trình một phần hằng tháng và thử toàn phần hằng năm:"))
    b.append(eq("PFD<sub>avg</sub> = (0,8 · (1/40) · 0,083/2) + (0,2 · (1/40) · 1/2) = 8,3 × 10⁻⁴ + "
                "2,5 × 10⁻³ = 3,3 × 10⁻³", "8.33"))
    b.append(eq("RRF = 1 / PFD = 300", "8.34"))
    b.append(p("Các con số này nay rơi vào dải SIL 2 (RRF = 100 – 1.000). Tuy nhiên, nếu tăng chu kỳ thử "
               "toàn phần lên năm năm thì RRF còn 75, tức trở lại dải SIL 1 (RRF = 10 – 100)."))

    # ------------------------------------------------------------------ 8.14
    b.append(h2("8.14 Yêu cầu về khả năng chịu lỗi", "Fault Tolerance Requirements"))
    b.append(p("Một hệ quả của định luật Murphy có thể phát biểu là: “Cái gì bị lạm dụng được thì sẽ bị "
               "lạm dụng.” Mô hình độ tin cậy giống như điệp viên bị bắt — tra tấn đủ lâu, chúng sẽ khai "
               "bất cứ điều gì. Đã có trường hợp người ta tuyên bố đạt mức toàn vẹn an toàn cao bằng những "
               "hệ không dự phòng. Nếu chọn suất hỏng đủ thấp và chu kỳ thử đủ dày, có thể đạt con số SIL 3 "
               "với một hệ không dự phòng. Nhưng con số có thể nói dối."))
    b.append(p("Các thành viên uỷ ban IEC 61508 và 61511 thấy cần đưa bảng yêu cầu chịu lỗi vào tiêu chuẩn, "
               "với hy vọng hạn chế việc lạm dụng phép toán và mô hình hoá. Hai bảng dưới đây lấy từ tiêu "
               "chuẩn IEC 61511 (dành cho người dùng cuối trong công nghiệp chế biến). Mức độ tranh luận, "
               "cãi vã và viết lại hai bảng này là rất lớn. Trước hết cần định nghĩa hai thuật ngữ."))
    b.append(p("<b>Khả năng chịu lỗi phần cứng</b> nói về mức dự phòng yêu cầu. Ví dụ, khả năng chịu lỗi "
               "phần cứng bằng 1 nghĩa là có ít nhất hai thiết bị, và kiến trúc sao cho hư hỏng nguy hiểm "
               "của một trong hai thành phần không ngăn được hành động an toàn. Đó là cấu hình 1oo2, không "
               "phải 2oo2. Khả năng chịu lỗi bằng 2 đòi hỏi cấu hình 1oo3."))
    b.append(p("<b>Tỷ lệ hư hỏng an toàn</b> (SFF) là một cách biểu thị mức hư hỏng nguy hiểm, ẩn của một "
               "thiết bị. Nhìn lại Hình 8-1 sẽ giúp ích ở đây. Tỷ lệ hư hỏng an toàn được định nghĩa là số "
               "hư hỏng an toàn cộng số hư hỏng nguy hiểm phát hiện được, chia cho tổng. Biểu diễn bằng "
               "công thức:"))
    b.append(eq("SFF = (λ<sub>SD</sub> + λ<sub>SU</sub> + λ<sub>DD</sub>) / λ<sub>TỔNG</sub>", "8.35"))
    b.append(p("Điều này đơn giản có nghĩa: mức chẩn đoán càng cao thì càng cần ít dự phòng để đạt một SIL "
               "cho trước."))
    b.append(table(
        ["SIL", "SFF &lt; 60 %", "SFF 60 % – 90 %", "SFF &gt; 90 %"],
        [
            ["1", "0", "0", "0"],
            ["2", "1", "0", "0"],
            ["3", "2", "1", "0"],
            ["4", "xem IEC 61508", "xem IEC 61508", "xem IEC 61508"],
        ],
        caption="Bảng 8-2. Khả năng chịu lỗi phần cứng tối thiểu cho bộ xử lý logic khả trình (theo IEC "
                "61511). Số trong ô là số kênh dự phòng tối thiểu phải có thêm."))
    b.append(p("Bảng 8-2 dành cho bộ xử lý logic khả trình (dựa trên phần mềm). Bảng 8-3 dành cho bộ xử lý "
               "logic không khả trình và thiết bị trường. Xét sự đa dạng của thiết bị trường — có loại "
               "không chẩn đoán gì, có loại chẩn đoán rất rộng — những hạn chế gắn với Bảng 8-3 là hiển "
               "nhiên. Còn rắc rối hơn nữa: có những trường hợp yêu cầu chịu lỗi ở Bảng 8-3 phải tăng "
               "thêm một (ví dụ khi chế độ hỏng chủ đạo không đưa về trạng thái an toàn, hoặc khi hư hỏng "
               "nguy hiểm không được phát hiện), và những trường hợp có thể giảm một (ví dụ các vấn đề "
               "“đã qua sử dụng”). Dù thế nào, Bảng 8-3 cho thấy rõ: để đạt các SIL cao hơn thì phải có "
               "thiết bị trường dự phòng. Nếu có số liệu SFF chi tiết hơn cho thiết bị trường, có thể dùng "
               "những bảng chi tiết hơn trong IEC 61508."))
    b.append(table(
        ["SIL", "Khả năng chịu lỗi phần cứng tối thiểu"],
        [
            ["1", "0"],
            ["2", "1"],
            ["3", "2"],
            ["4", "xem IEC 61508"],
        ],
        caption="Bảng 8-3. Khả năng chịu lỗi phần cứng tối thiểu cho thiết bị trường và bộ xử lý logic "
                "không khả trình (theo IEC 61511)."))

    # ------------------------------------------------------------------ 8.15
    b.append(h2("8.15 Một “sách dạy nấu ăn” thiết kế SIS mẫu", "Sample SIS Design Cookbook"))
    b.append(p("Dùng các công thức trên cùng số liệu suất hỏng hợp lệ cho những thiết bị đang xét, có thể "
               "xây một “sách dạy nấu ăn” cho thiết kế SIS. Một ví dụ ở Bảng 8-4. Như mọi sách dạy nấu ăn, "
               "nó có giới hạn sử dụng. Ví dụ, một công thức làm bánh cho bốn người không nhất thiết nhân "
               "lên được để phục vụ tiệc cưới bốn trăm khách. Chừng nào thiết kế của bạn còn nằm trong các "
               "giả định đã dùng khi xây cuốn sách ấy (số lượng thiết bị, suất hỏng, chu kỳ thử…), thì "
               "không cần phân tích định lượng chi tiết cho từng hệ."))
    b.append(table(
        ["SIL", "Cảm biến", "Logic", "Phần tử cuối"],
        [
            ["1", "Công tắc hoặc bộ chuyển đổi",
             "Rơ-le; bán dẫn rắn an toàn; PLC đa dụng; PLC an toàn",
             "Van tiêu chuẩn"],
            ["2", "Bộ chuyển đổi có so sánh<sup>1</sup>; bộ chuyển đổi an toàn<sup>2</sup>",
             "Rơ-le; bán dẫn rắn an toàn; PLC an toàn",
             "Van dự phòng; van đơn có thử hành trình một phần<sup>3</sup>"],
            ["3", "Bộ chuyển đổi dự phòng",
             "Rơ-le; bán dẫn rắn an toàn; PLC an toàn dự phòng",
             "Van dự phòng có thử hành trình một phần"],
            ["4", "xem IEC 61508", "xem IEC 61508", "xem IEC 61508"],
        ],
        caption="Bảng 8-4. Sách dạy nấu ăn thiết kế SIS mẫu. Giả định: 1 cảm biến, 2 van, thử hằng năm. "
                "<br><sup>1</sup> Bộ chuyển đổi có so sánh nghĩa là dùng một bộ chuyển đổi an toàn và một "
                "bộ chuyển đổi của BPCS rồi so sánh hai tín hiệu. Việc này làm tăng đáng kể mức phủ chẩn "
                "đoán. <br><sup>2</sup> Bộ chuyển đổi an toàn có bán từ nhiều nhà cung cấp, với hệ số phủ "
                "chẩn đoán vượt 95 %. <br><sup>3</sup> Thử hành trình một phần nghĩa là thử van một phần "
                "khi đang vận hành, không đi hết hành trình. Có nhiều cách thực hiện, thủ công và tự động. "
                "Phải thử ít nhất hằng tháng mới có lợi ích đáng kể."))

    # ------------------------------------------------------------------ 8.16
    b.append(h2("8.16 Công cụ kỹ thuật để phân tích hiệu năng hệ", "Engineering Tools Available for Analyzing System Performance"))
    b.append(p("Trước hết nên mô hình hoá hệ bằng tay để nhận ra rằng a) không có phép thuật nào ở đây, và "
               "b) không cần bằng tiến sĩ toán mới làm được. Tuy vậy, tính tay nhanh chóng trở nên tẻ nhạt "
               "và buồn chán. May thay, có những công cụ kỹ thuật để tự động hoá việc mô hình hoá."))
    b.append(p("Có thể chỉ việc lấy các công thức trình bày ở trên và đưa vào một bảng tính. Ngoài việc "
               "tính hiệu năng của hệ, còn có thể vẽ biểu đồ thể hiện ảnh hưởng của chu kỳ thử, của chẩn "
               "đoán… Cách tự động hoá này giúp rất nhiều trong việc hiểu yếu tố nào ảnh hưởng đáng kể đến "
               "hiệu năng của hệ và yếu tố nào không."))
    b.append(p("Có một số chương trình thương mại để lập sơ đồ khối độ tin cậy, cây lỗi và mô hình Markov. "
               "[Ref. 13] Tuy nhiên những chương trình này là loại chung, không dành riêng cho tính chất và "
               "cách thiết kế đặc thù của phần lớn hệ an toàn đang dùng."))
    b.append(p("Các nhà cung cấp hệ điều khiển và hệ an toàn đã tự phát triển chương trình mô hình hoá "
               "riêng. Những chương trình này có thể được cung cấp cho người dùng, có thể không. Ngoài ra "
               "còn có những chương trình thương mại được thiết kế riêng để mô hình hoá hiệu năng của hệ "
               "điều khiển và hệ an toàn. [Ref. 14, 16 và 17]"))

    # ------------------------------------------------------------------ Summary
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p("Mọi thứ không hiển nhiên như vẻ ngoài. Hai kênh không phải lúc nào cũng tốt hơn một, và ba "
               "kênh không phải lúc nào cũng tốt hơn hai. Dùng công nghệ nào, mức dự phòng bao nhiêu, chu "
               "kỳ thử bằng tay bao lâu, còn thiết bị trường thì sao? Nếu trả lời được những câu hỏi này "
               "một cách dễ dàng thì các nhóm soạn tiêu chuẩn đã không mất 10 năm viết tài liệu, và đã "
               "không cần đến cuốn sách này."))
    b.append(p("Chúng ta không thiết kế nhà máy điện hạt nhân hay máy bay bằng cảm tính hay linh cảm. Là kỹ "
               "sư, phải dựa vào đánh giá định lượng làm cơ sở cho phán đoán. Phân tích định lượng có thể "
               "không chính xác và không hoàn hảo, nhưng vẫn là việc đáng làm, vì:"))
    b.append(ol([
        "Nó cho biết sớm liệu hệ có khả năng đáp ứng yêu cầu thiết kế hay không.",
        "Nó cho phép xác định mắt yếu của hệ (và sửa nếu cần).",
    ]))
    b.append(p("Để dự báo hiệu năng của một hệ, cần số liệu hiệu năng của mọi thành phần. Thông tin có thể "
               "lấy từ sổ sách người dùng, sổ sách nhà cung cấp, dự báo kiểu quân sự, và các cơ sở dữ liệu "
               "thương mại của nhiều ngành khác nhau."))
    b.append(p("Khi mô hình hoá hiệu năng của một SIS, cần xét hai chế độ hỏng. Hư hỏng an toàn dẫn đến "
               "cắt nhầm và mất sản lượng. Thuật ngữ nên dùng cho chế độ này là thời gian trung bình tới "
               "lần cắt nhầm (MTTF<sub>spurious</sub>), thường tính bằng năm. Hư hỏng nguy hiểm là khi hệ "
               "không phản ứng đúng lúc cần. Các thuật ngữ thường dùng để định lượng hiệu năng ở chế độ "
               "này là xác suất hỏng khi có yêu cầu (PFD), hệ số giảm rủi ro (RRF) và độ khả dụng an toàn "
               "(SA)."))
    b.append(p("Có nhiều phương pháp mô hình hoá để dự báo hiệu năng của hệ an toàn. Báo cáo kỹ thuật "
               "ISA-TR84.00.02-2002, Phần 1–5, trình bày tổng quan về việc dùng công thức đơn giản hoá (tới "
               "mô hình Markov), cây lỗi, và mô hình Markov đầy đủ. Mỗi phương pháp có ưu nhược điểm. Không "
               "phương pháp nào đúng hay sai hơn phương pháp khác. Tất cả đều dùng đơn giản hoá và đều "
               "tính đến những yếu tố khác nhau. (Đáng chú ý là khi mô hình hoá cùng một hệ trong "
               "ISA-TR84.00.02 bằng cả ba phương pháp, kết quả thu được giống nhau.) Dùng những kỹ thuật "
               "ấy, có thể mô hình hoá các công nghệ khác nhau, các mức dự phòng, các chu kỳ thử và các "
               "cấu hình thiết bị trường khác nhau. Có thể mô hình hoá bằng máy tính tay, hoặc lập bảng "
               "tính hay chương trình riêng để tự động hoá và đơn giản hoá công việc."))

    b.append(note(
        "<b>Ba điểm cần lưu ý khi đọc chương này.</b><br>"
        "<b>(1) Con số PFD của hệ TMR không tái lập được.</b> Với λ<sub>du</sub> một kênh = 1,4 × 10⁻⁴/năm "
        "và TI = 1 năm, công thức (8.22) cho (1,4 × 10⁻⁴)² × (1/2)² ≈ 4,9 × 10⁻⁹, không phải 6,25 × 10⁻⁸ "
        "như sách in. Dòng ngay sau đó còn chia cho 6,25 × 10⁻⁷ trong khi đang trích 6,25 × 10⁻⁸. Bản dịch "
        "giữ nguyên hai con số của bản gốc và sửa lại số chia cho khớp (8,23), vì chính lập luận của "
        "chương là những con số này chỉ có giá trị cỡ bậc độ lớn — và ví dụ TMR là chỗ chứng minh điều đó "
        "rõ nhất.<br>"
        "<b>(2) Bảng 8-2 và 8-3 được phục dựng.</b> Bản scan làm chữ số SIL dính vào ô đầu tiên (“11 0 "
        "0”, “22 1 0”, “32 2 1”). Bản dịch khôi phục theo đúng IEC 61511: SIL 1 → 0/0/0, SIL 2 → 1/0/0, "
        "SIL 3 → 2/1/0, SIL 4 → xem IEC 61508; và Bảng 8-3: 0, 1, 2.<br>"
        "<b>(3) Một nhãn sai trong ví dụ thiết bị trường.</b> Ở mục 8.13, dòng “Sensor PFD<sub>avg</sub> = "
        "(1/40) · 2 · (1/2) = 0,025” thực ra là PFD của <em>hai chiếc van</em>, không phải của cảm biến — "
        "cảm biến đã được tính ở dòng ngay trên. Bản dịch sửa nhãn thành “hai van”. Ngoài ra tên H. L. "
        "Mencken được viết đúng chính tả (bản gốc in “Menken”)."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "Kletz, Trevor A. <em>Computer Control and Human Error</em>. Gulf Publishing, 1995.",
        "Leveson, Nancy G. <em>Safeware — System Safety and Computers</em>. Addison-Wesley, 1995.",
        "Neumann, Peter G. <em>Computer Related Risks</em>. Addison-Wesley, 1995.",
        "Duke, Geoff R. “Calculation of Optimum Proof Test Intervals for Maximum Availability.” "
        "<em>Quality &amp; Reliability Engineering International</em> (Volume 2), 1986. tr. 153–158.",
        "Smith, David J. <em>Reliability, Maintainability, and Risk: Practical Methods for Engineers</em>. "
        "Ấn bản 4. Butterworth-Heinemann, 1993. (Ấn bản 5 [1997] và 6 [2001] cũng có.)",
        "ISA-TR84.00.02-2002, Phần 1–5. <em>Safety Instrumented Functions (SIF) – Safety Integrity Level "
        "(SIL) Evaluation Techniques</em>.",
        "OREDA-92. <em>Offshore Reliability Data</em>. DNV Technica, 1992. (Các bản 1997 và 2002 cũng đã "
        "phát hành.)",
        "<em>Guidelines For Process Equipment Reliability Data, with Data Tables</em>. American Institute "
        "of Chemical Engineers – Center for Chemical Process Safety, 1989.",
        "IEEE 500-1984. <em>Equipment Reliability Data for Nuclear-Power Generating Stations</em>.",
        "<em>Safety Equipment Reliability Handbook</em>. exida.com, 2003.",
        "ISA-TR84.00.02-2002, Phần 1–5. <em>Safety Instrumented Functions (SIF) – Safety Integrity Level "
        "(SIL) Evaluation Techniques</em>.",
        "IEC 61508-1998. <em>Functional Safety of Electrical/Electronic/Programmable Electronic "
        "Safety-Related Systems</em>.",
        "ITEM Software (Irvine, CA), 1998. Website: www.itemsoft.com (truy cập 28/6/2005).",
        "CaSSPack (Control and Safety System Modeling Package). L&amp;M Engineering (Kingwood, TX). "
        "Website: www.landmengineering.com (truy cập 28/6/2005).",
        "Goble, W. M. <em>Control Systems Safety Evaluation and Reliability</em>. Ấn bản 2. ISA, 1998.",
        "SILver™ (SIL Verification). exida.com (Sellersville, PA). Website: www.exida.com (truy cập "
        "28/6/2005).",
        "SIL Solver™. SIS-TECH (Houston, TX). Website: www.sis-tech.com (truy cập 28/6/2005).",
    ]))
    return "".join(b)


# ===================================================================== EN
def body_en():
    b = []
    b.append(lead(
        "This is the chapter that tells you the arithmetic is unreliable, and then makes you do the "
        "arithmetic anyway. Both halves matter. The formulas are how you find out which component is "
        "killing your safety performance; the caveats are why you must never quote the answer to three "
        "significant figures in a meeting."))

    b.append(h2("The four numbers that decide everything"))
    b.append(p("Strip away the vendor literature and a safety instrumented function is four numbers: the "
               "failure rate of the sensor, the failure rate of the logic solver, the failure rate of the "
               "final element, and how often somebody actually tests all three. Everything else — "
               "architecture, diagnostics, certification, the glossy brochure — is a way of moving those "
               "four numbers around."))
    b.append(p("Section 8.10 to 8.13 does this four times in a row, and the sequence is worth reading as a "
               "single argument rather than as four worked examples. A relay panel of ten relays lands at "
               "RRF 3,300. Replace it with a general-purpose PLC and the number falls to 220 — a full order "
               "of magnitude worse, with the same nuisance-trip performance. Replace that with a TMR system "
               "and the number becomes 16,000,000, which is nonsense. Add a 1 % common-cause factor and the "
               "nuisance-trip figure collapses from 45,000 years to 1,100. Then bolt on eight non-redundant "
               "field devices and the whole thing comes back down to RRF 29."))

    b.append(h2("Why the field devices always win"))
    b.append(p("The last step is the one people skip. A logic solver is one box; a loop has a sensor, a "
               "cable, a solenoid, a valve body, a stem, a seat and a spring. The valve is the only part of "
               "the loop that is asked to move after sitting still for a year in a dirty process. It is "
               "unsurprising that it dominates, and yet the purchasing conversation is almost always about "
               "the logic solver, because that is where the specification sheet is."))
    b.append(p("Partial stroke testing is the interesting compromise in section 8.13.1, and the arithmetic "
               "explains why it spread so fast in the late 1990s. A monthly partial stroke at 80 % coverage "
               "takes a single valve from RRF 80 to RRF 300 — from the bottom of SIL 1 to the middle of SIL "
               "2 — without ever stopping the process. Nothing else in this book buys that much for so "
               "little. The catch is the coverage factor: nobody can measure it, the claims run from 60 % to "
               "90 %, and the whole benefit rests on it."))

    b.append(h2("MTBF is not life"))
    b.append(p("The match analogy in section 8.5.1 is the clearest explanation of this in the literature. A "
               "match has a very low failure rate per hour of storage and therefore an enormous MTBF — "
               "minutes or hours — while its actual life is a few seconds. The two numbers answer different "
               "questions. MTBF answers how often one unit in a population fails per unit time; life "
               "answers how long one unit lasts. Confusing them produces the classic maintenance plan that "
               "replaces every device at the MTBF, which throws away 63 % of the good ones."))
    b.append(p("The same confusion sits behind the nines argument. Ninety-nine percent availability "
               "sounds excellent and can mean a nuisance trip every month with four minutes of downtime "
               "each. Ninety-nine point nine nine percent sounds barely different and can mean one trip "
               "every ten years. Both are true statements about different plants."))

    b.append(h2("The models disagree with reality for a reason"))
    b.append(p("Section 8.12 is the honest heart of the chapter. The TMR calculation produces a risk "
               "reduction factor of sixteen million, and the authors immediately ask whether SIL 7 exists. "
               "It does not, and the reason is that the model contains only the failures somebody thought "
               "of. Common cause is the largest of the missing terms, and a Beta factor of 1 % — one failure "
               "in a hundred taking out all three channels — removes a factor of forty from the answer."))
    b.append(p("This is why IEC 61511 put the fault tolerance tables in. If the arithmetic alone decided "
               "the architecture, a clever engineer with optimistic failure rates could justify a simplex "
               "logic solver at SIL 3 and be technically correct. The tables say: no. At SIL 3 you need two "
               "channels regardless of what your spreadsheet says, because the spreadsheet cannot see the "
               "failure mode that takes out both."))

    b.append(h2("Reading the tables in section 8.14"))
    b.append(p("The two fault tolerance tables look bureaucratic and are actually the most useful pages in "
               "the chapter. Read them as a floor, not a target. Table 8-2 tells you the minimum redundancy "
               "for a programmable logic solver at each SIL and each band of safe failure fraction; Table "
               "8-3 does the same for field devices and non-programmable solvers, and is stricter because "
               "field devices have far less diagnostics."))
    b.append(p("The trap is that SFF is a property of the device, not of your installation. A transmitter "
               "with 95 % diagnostic coverage installed with its impulse line plugged has the diagnostic "
               "coverage of a brick. The standard knows this, which is why section 8.14 mentions the "
               "conditions that raise the requirement by one — dominant failure mode not to the safe state, "
               "dangerous failures undetected — and the ones that lower it."))

    b.append(h2("What to do on Monday"))
    b.append(p("Build the spreadsheet. Not because the answer will be right, but because building it forces "
               "you to write down the four numbers, and writing them down is where the arguments happen. "
               "Most disagreements about SIL are not disagreements about mathematics; they are disagreements "
               "about whether a thirty-year-old valve really has a forty-year MTBF."))
    b.append(p("Then sanity-check the output against the tables in section 8.14 and against the cookbook in "
               "section 8.15. If your model says a simplex system meets SIL 3, one of the two is wrong, and "
               "it is not the table."))
    return "".join(b)
