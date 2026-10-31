# -*- coding: utf-8 -*-
"""Safety Instrumented Systems — Chapter 4, Protection Layers
(Gruhn & Cheddie, ISA 2006)."""
import sisfig as F
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul)

PAGES_SRC = 13
BYLINE = "Paul Gruhn & Harry Cheddie · ISA (2006)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Lớp ngăn ngừa (prevention layer)</em> — làm giảm xác suất sự kiện xảy ra. · "
            "<em>Lớp giảm nhẹ (mitigation layer)</em> — làm giảm hậu quả khi sự kiện đã xảy ra. · "
            "<em>Phòng vệ theo chiều sâu (defense in depth)</em> — nhiều lớp độc lập, đa dạng. · "
            "<em>LOPA</em> — phân tích lớp bảo vệ, phương pháp bán định lượng gán hệ số giảm rủi ro cho "
            "từng lớp. · "
            "<em>Hệ số giảm rủi ro (RRF)</em> — nghịch đảo của xác suất lớp đó không làm việc. · "
            "<em>Đa dạng hóa (diversification)</em> — dùng công nghệ khác nhau cho các lớp khác nhau. · "
            "<em>F&G</em> — hệ phát hiện cháy và khí. · "
            "<em>An toàn vốn có (inherently safe)</em> — an toàn nhờ chính thiết kế, không cần thêm thiết bị.")
    return note(
        "<b>Key terms.</b> <em>Prevention layer</em> — reduces the probability of the event. · "
        "<em>Mitigation layer</em> — reduces the consequences after it has happened. · "
        "<em>Defense in depth</em> — several independent, diverse layers. · "
        "<em>LOPA</em> — layer of protection analysis, the semi-quantitative method that assigns a risk "
        "reduction factor to each layer. · "
        "<em>Risk reduction factor (RRF)</em> — the inverse of that layer's probability of failing on "
        "demand. · <em>Diversification</em> — using different technologies in different layers. · "
        "<em>F&amp;G</em> — fire and gas detection. · "
        "<em>Inherently safe</em> — safe by virtue of the design itself, with no added devices.")


# ===================================================================== VI
def body_vi():
    b = []
    b.append(lead(
        "Tai nạn hiếm khi có một nguyên nhân duy nhất. Chương này kể lại vụ Bhopal — không phải để nhắc lại "
        "con số thương vong, mà để cho thấy một chuỗi mười mấy quyết định riêng lẻ, mỗi quyết định đều có "
        "lý do riêng và đều nhỏ, đã xếp thẳng hàng như thế nào. Sau đó chương phân loại các lớp bảo vệ "
        "thành hai nhóm — ngăn ngừa và giảm nhẹ — và giải thích vì sao gộp quá nhiều chức năng vào một lớp "
        "lại làm an toàn tổng thể giảm đi."))

    # ---------------------------------------------------------------- 4.0
    b.append(h2("Vì sao phải có nhiều lớp", "Why Layers at All"))
    b.append(p("Tai nạn hiếm khi có một nguyên nhân duy nhất. Tai nạn thường là tổ hợp của những sự kiện "
               "hiếm mà ban đầu người ta cho là độc lập và sẽ không xảy ra cùng lúc. Lấy ví dụ vụ tai nạn "
               "hóa chất tồi tệ nhất tới nay — Bhopal, Ấn Độ, nơi ước tính 3.000 người chết và 200.000 "
               "người bị thương."))
    b.append(p("Chất thoát ra ở Bhopal là MIC (methyl isocyanate). Vụ phát tán xảy ra từ một bồn chứa nhiều "
               "hơn mức cho phép của yêu cầu an toàn công ty. Quy trình vận hành quy định dùng hệ làm lạnh "
               "của bồn để giữ nhiệt độ vật liệu dưới 5 °C; cảnh báo nhiệt độ sẽ kêu ở 11 °C. Hệ làm lạnh "
               "đã bị tắt vì lý do tài chính, và vật liệu thường được lưu ở gần 20 °C. Ngưỡng cảnh báo "
               "nhiệt độ được đổi từ 11 °C lên 20 °C."))
    b.append(p("Một công nhân được giao nhiệm vụ rửa một số đường ống và bộ lọc bị tắc. Mặt bích mù không "
               "được lắp như quy định. Nước rò qua van vào bồn chứa MIC. Các đồng hồ nhiệt độ và áp suất "
               "chỉ điều kiện bất thường bị bỏ qua vì bị coi là không chính xác. Một tháp rửa khí "
               "(scrubber) — thứ có thể trung hòa được lượng khí thoát — không được giữ ở trạng thái làm "
               "việc vì người ta cho rằng không cần khi sản xuất đang tạm dừng (đúng là lúc đó đang dừng). "
               "Dù sao thì tháp rửa khí đó cũng không đủ công suất cho quy mô phát tán này. Tháp đốt (flare) "
               "— thứ có thể đốt bớt một phần vật liệu — đang ngừng để bảo dưỡng, và cũng không được thiết "
               "kế cho quy mô phát tán đó. Vật liệu lẽ ra có thể được xả sang các bồn bên cạnh, nhưng đồng "
               "hồ hiển thị sai rằng các bồn đó đang đầy một phần. Một màn nước có sẵn để trung hòa khí "
               "thoát, nhưng MIC được xả qua một ống khói cao 108 feet — quá cao so với tầm với của màn "
               "nước. Công nhân chỉ biết có phát tán khi mắt và cổ họng bị kích ứng; những phản ánh của họ "
               "với quản lý lúc đó bị bỏ qua."))
    b.append(p("Công nhân hoảng loạn bỏ chạy, phớt lờ bốn chiếc xe buýt vốn được dùng để sơ tán nhân viên và "
               "cư dân gần đó. Giám sát viên khu MIC không tìm thấy mặt nạ oxy của mình và bị gãy chân khi "
               "trèo qua hàng rào. Khi được thông báo về tai nạn, giám đốc nhà máy nói trong sự hoài nghi: "
               "“Không thể nào khí lại rò từ nhà máy của tôi. Nhà máy đang dừng. Công nghệ của chúng tôi "
               "không thể sai được, chúng tôi không thể có rò rỉ.”"))
    b.append(note(
        "<b>Đọc lại danh sách trên và đếm số lớp.</b> Giới hạn tồn chứa, hệ làm lạnh, cảnh báo nhiệt độ, "
        "mặt bích mù, đồng hồ đo, tháp rửa khí, tháp đốt, bồn chứa dự phòng, màn nước, xe buýt sơ tán — "
        "mười lớp. Không lớp nào hỏng vì một lý do kỹ thuật bí ẩn. Mỗi lớp bị vô hiệu hóa vì một quyết "
        "định riêng, hợp lý trong hoàn cảnh riêng của nó."))
    b.append(p("Các cuộc điều tra tai nạn công nghiệp cho thấy một tỉ lệ lớn xảy ra trong lúc sản xuất bị "
               "gián đoạn, khi người vận hành đang cố duy trì hoặc khởi động lại sản xuất. Trong mỗi trường "
               "hợp, tình huống nguy hiểm được tạo ra bởi mong muốn tiết kiệm thời gian và làm vận hành dễ "
               "hơn. Và trong mỗi trường hợp, nội quy an toàn của công ty đã bị vi phạm."))
    b.append(p("Những lớp an toàn tốt nhất và dư thừa nhất vẫn có thể bị đánh bại bởi thực hành quản lý tồi "
               "hoặc mâu thuẫn. Nhiều ví dụ đã được ghi chép trong ngành hóa chất. Một tai nạn ở nhà máy "
               "chế biến polymer xảy ra sau khi bộ phận vận hành đặt tất cả cảnh báo và liên động vào "
               "bypass để tăng sản lượng 5 %. Ở một vụ khác, liên động và cảnh báo hỏng — với tốc độ bình "
               "thường — nhưng không ai biết, vì ban quản lý đã quyết định bỏ các đợt kiểm tra bảo dưỡng "
               "định kỳ cho thiết bị đo an toàn."))
    b.append(p("James Reason đã mô tả cách tai nạn tổ chức xảy ra khi nhiều lớp an toàn cùng hỏng. "
               "<b>Hình 4-1a</b> cho thấy ý đồ thiết kế của nhiều lớp: nếu mọi lớp đều hiệu quả (đặc và "
               "chắc) thì lỗi không lan qua được. Nhưng trong thực tế, các lớp không đặc. Chúng giống lát "
               "phô mai Thụy Sĩ hơn. Các lỗ do khiếm khuyết từ quản lý, kỹ thuật, vận hành, bảo dưỡng và "
               "các lỗi khác tạo ra. Không chỉ mỗi lớp có lỗ, mà các lỗ còn liên tục di chuyển, lớn lên, "
               "co lại, xuất hiện và biến mất. Khi đó dễ hình dung rằng nếu các lỗ xếp thẳng hàng "
               "(<b>Hình 4-1b</b>), lỗi có thể lan qua tất cả."))
    b.append(fig(1, F.fig_4_1(), "vi"))
    b.append(p("<b>Hình 4-2</b>, thường được gọi là “sơ đồ củ hành”, xuất hiện dưới nhiều dạng khác nhau "
               "trong hầu hết tài liệu an toàn. Nó cho thấy có nhiều lớp an toàn khác nhau, một số là lớp "
               "ngăn ngừa, số khác là lớp giảm nhẹ. Khái niệm cơ bản rất đơn giản: “đừng bỏ tất cả trứng "
               "vào một giỏ”. Có người gọi đó là “phòng vệ theo chiều sâu”."))
    b.append(p("Rủi ro là một hàm của xác suất (hay tần suất, hay khả năng xảy ra) của một sự kiện và mức "
               "nghiêm trọng (hay hậu quả) của nó. Nhiều lớp an toàn trong một cơ sở được thiết kế để làm "
               "giảm một trong hai đại lượng đó. Lớp ngăn ngừa được thực hiện để giảm xác suất sự kiện nguy "
               "hiểm xảy ra. Lớp giảm nhẹ được thực hiện để giảm hậu quả khi sự kiện đã xảy ra."))
    b.append(note(
        "Phần bàn về lớp ngăn ngừa và lớp giảm nhẹ dưới đây chỉ là <b>ví dụ</b>. Danh sách này không nhằm "
        "được coi là toàn bộ các lớp có thể thực hiện, cũng không phải là những lớp bắt buộc phải dùng cho "
        "một cơ sở cụ thể nào."))
    b.append(fig(2, F.fig_4_2(), "vi"))

    # ---------------------------------------------------------------- 4.1
    b.append(h2("4.1 Các lớp ngăn ngừa", "Prevention Layers"))
    b.append(p("Lớp ngăn ngừa được thực hiện để giảm xác suất hay khả năng xảy ra của một sự kiện nguy hiểm. "
               "Người ta thường dùng nhiều lớp đa dạng."))

    b.append(h3("4.1.1 Thiết kế nhà máy", "Process Plant Design"))
    b.append(p("Bản thân nhà máy phải được thiết kế với an toàn trong đầu. Đó là lý do phải thực hiện HAZOP "
               "(nghiên cứu mối nguy và khả năng vận hành) và các soát xét an toàn khác như cây lỗi, danh "
               "mục kiểm tra, phân tích “nếu – thì”…"))
    b.append(p("Một mục tiêu chính trong ngành chế biến là thiết kế nhà máy <b>an toàn vốn có</b>. Đừng "
               "thiết kế một nhà máy nguy hiểm rồi dán lên đó thật nhiều băng cá nhân với hy vọng chúng sẽ "
               "che lấp vấn đề. Hãy thiết kế sao cho không cần tới băng cá nhân. Làm việc với thiết kế áp "
               "suất thấp, tồn chứa thấp, vật liệu không nguy hiểm… Như Trevor Kletz nói: “Cái bạn không có "
               "thì không thể rò.”"))
    b.append(p("Đáng ngạc nhiên là mức phản đối với cách làm này — cũng như với hầu hết các thay đổi khác — "
               "lại rất lớn. Lời phàn nàn điển hình là: “Nhưng chúng tôi không đủ tiền để làm hết những thứ "
               "đó!” Thông tin mà một trong hai tác giả thu thập được ở nhiều ngành cho thấy hệ an toàn vốn "
               "có thể có chi phí ban đầu cao hơn (tuy không phải lúc nào cũng vậy), nhưng chi phí sở hữu "
               "trong suốt vòng đời dự án lại thấp hơn. Điều tương tự cũng đúng với quản lý chất lượng: "
               "hãy nghĩ xem bao nhiêu công ty từng nói họ không đủ tiền làm việc đó; giờ thì bạn không thể "
               "không có nó."))
    b.append(p("Loại bỏ hoặc giảm mối nguy thường dẫn tới thiết kế đơn giản hơn, và chính điều đó có thể "
               "làm giảm rủi ro. Phương án thay thế là thêm thiết bị bảo vệ để kiểm soát mối nguy — cách "
               "này thường làm tăng độ phức tạp."))
    b.append(p("Một ví dụ về sự phản đối thiết kế an toàn vốn có nằm ngay trong đời sống. Đạo luật An toàn "
               "Tủ lạnh ra đời vì trẻ em bị kẹt và ngạt khi chơi trong những tủ lạnh bỏ không. Các nhà sản "
               "xuất khẳng định họ không đủ tiền để thiết kế chốt cửa an toàn hơn. Khi bị buộc phải làm, họ "
               "đưa ra loại chốt nam châm đơn giản: cho phép mở cửa từ bên trong, và thế là loại bỏ được "
               "mối nguy. Thiết kế mới còn <em>rẻ hơn</em> thiết kế cũ."))

    b.append(h3("4.1.2 Hệ điều khiển quá trình", "Process Control System"))
    b.append(p("Hệ điều khiển quá trình là lớp an toàn tiếp theo. Nó điều khiển nhà máy để tối ưu hóa việc "
               "dùng nhiên liệu, chất lượng sản phẩm… Nó cố giữ mọi biến (áp suất, nhiệt độ, mức, lưu "
               "lượng…) trong giới hạn an toàn, nên có thể coi nó là một lớp an toàn. Tuy nhiên, lỗi của "
               "hệ điều khiển cũng có thể khởi phát một sự kiện nguy hiểm."))
    b.append(p("Tự động hóa thường không loại bỏ con người khỏi hệ. Thực tế, tự động hóa thường đẩy nhiệm vụ "
               "của con người lên mức phức tạp mới. Nếu máy tính đang được dùng để ngày càng nhiều quyết "
               "định vì phán đoán và trực giác của con người không thỏa đáng, thì để con người làm trọng "
               "tài cuối cùng có thể là một sai lầm. Kinh nghiệm cho thấy con người giám sát hệ tự động rất "
               "kém. Những nhiệm vụ đòi hỏi ít hành động tích cực có thể làm giảm độ tỉnh táo và cảnh giác, "
               "dẫn tới tự mãn và phụ thuộc quá mức vào hệ tự động. Những khoảng giám sát thụ động dài có "
               "thể khiến người vận hành không sẵn sàng hành động khi có sự cố. Có người đã nói rằng “điều "
               "khiển bằng máy tính biến người vận hành thành kẻ ngốc”."))
    b.append(p("Một cách giải quyết là đưa người vận hành tham gia vào phân tích an toàn và các quyết định "
               "thiết kế ngay từ đầu và trong suốt quá trình phát triển — tham gia nhiều hơn, chứ không "
               "phải ít hơn."))

    b.append(h3("4.1.3 Hệ cảnh báo", "Alarm Systems"))
    b.append(p("Nếu hệ điều khiển quá trình không thực hiện được chức năng của nó (vì bất kỳ lý do nào, như "
               "lỗi bên trong hay một vòng bị đặt bypass), cảnh báo có thể được dùng để báo cho người vận "
               "hành rằng cần có can thiệp."))
    b.append(p("Hệ cảnh báo và giám sát phải:"))
    b.append(ol([
        "Phát hiện vấn đề càng sớm càng tốt, ở mức đủ thấp để bảo đảm có thể hành động trước khi tới điều "
        "kiện nguy hiểm.",
        "Độc lập với các thiết bị mà chúng giám sát (nghĩa là chúng không được hỏng khi hệ được giám sát "
        "hỏng).",
        "Thêm vào càng ít độ phức tạp càng tốt.",
        "Dễ bảo dưỡng, dễ kiểm tra và dễ hiệu chuẩn.",
    ]))
    b.append(p("Hệ cảnh báo và giám sát được coi là lớp an toàn mà ở đó con người tham gia tích cực. Người "
               "vận hành nói chung vẫn cần trong nhà máy vì lý do đơn giản: không phải mọi thứ đều tự động "
               "hóa được. Về bản chất, người thiết kế không thể lường trước mọi tổ hợp điều kiện có thể xảy "
               "ra. Người vận hành có thể cần được tính đến vì chỉ họ mới đủ linh hoạt và thích nghi trong "
               "một số tình huống."))
    b.append(p("Nhưng đó là con dao hai lưỡi: những sự kiện không được tính tới ở giai đoạn thiết kế chắc "
               "chắn cũng không nằm trong chương trình đào tạo người vận hành. Mặt khác, việc mù quáng tuân "
               "theo quy trình cũng đã gây ra tai nạn. Việc đi lệch khỏi quy tắc là dấu hiệu của người có "
               "kinh nghiệm, nhưng nó chắc chắn dẫn tới những lỗi con người thỉnh thoảng xảy ra — và những "
               "lời đổ lỗi sau đó."))

    b.append(h3("4.1.3.1 Độ tin cậy của con người", "Human Reliability"))
    b.append(p("Một trong hai tác giả từng nghe có người nói họ không muốn hệ tự động điều khiển an toàn "
               "trong nhà máy của mình. Họ muốn dựa vào những người được đào tạo và huấn luyện về vận hành "
               "và động học của quá trình. Điều đó có thể chấp nhận cho vận hành thường lệ (dù vẫn có người "
               "phản đối), nhưng không phải là phương án được khuyến nghị cho các tình huống khẩn cấp "
               "tới hạn."))
    b.append(p("Ví dụ, tai nạn đã xảy ra vì:"))
    b.append(ol([
        "Người vận hành không tin rằng sự kiện hiếm là có thật;",
        "Người vận hành bị quá tải thông tin và không hành động được.",
    ]))
    b.append(p("Con người đã và sẽ còn trực tiếp chịu trách nhiệm cho một số tai nạn. Một số người trong "
               "ngành — đáng chú ý là Trevor Kletz — đã ghi chép rất tốt những trường hợp này. Hy vọng phần "
               "còn lại của ngành sẽ học từ đó và không lặp lại. Nhưng chính Kletz cũng nói: “Tai nạn không "
               "phải do thiếu hiểu biết, mà do không dùng cái hiểu biết mình đã có.” Đáng tiếc, lịch sử cho "
               "thấy nhiều tai nạn vẫn tái diễn."))
    b.append(p("Ví dụ, đã có trường hợp người vận hành thấy cảnh báo, hiểu nó nghĩa là gì, và vẫn không hành "
               "động. Hoặc cảnh báo bị coi là phiền nhiễu (“Ôi, cái đó ngày nào chả có” — đây là một trong "
               "nhiều vấn đề ở Bhopal), hoặc họ chờ xem có gì khác xảy ra không (đôi khi với hậu quả thảm "
               "khốc)."))
    b.append(p("Khi mọi thứ đi sai, chúng thường dồn dập và leo thang. Một trong hai tác giả biết một nhà "
               "máy nơi khi có sự cố dừng, DCS in ra <b>17.000</b> thông báo cảnh báo. Nhấn chìm người vận "
               "hành trong ngần ấy thông tin rõ ràng là có hại. Quá nhiều thông tin không phải là điều tốt."))
    b.append(p("Khi đối mặt với tình huống đe dọa tính mạng và phải quyết định trong vòng một phút, con "
               "người có xu hướng quyết định sai tới 99 % số lần. Kết luận này đến từ các nghiên cứu thực "
               "tế của quân đội. Nói cách khác, trong tình huống khẩn cấp, con người là một trong những thứ "
               "tồi tệ nhất để dựa vào, dù được huấn luyện tốt tới đâu."))

    b.append(h3("4.1.4 Quy trình", "Procedures"))
    b.append(p("Có người coi quy trình vận hành và bảo dưỡng là một lớp bảo vệ. Đây là chủ đề khá tranh "
               "cãi. Việc kiểm tra để phát hiện ăn mòn và suy giảm thành thiết bị có thể giúp ngăn tai nạn. "
               "Quy trình giới hạn vận hành thiết bị dưới giới hạn an toàn có thể giúp ngăn tai nạn. Bảo "
               "dưỡng phòng ngừa — thay chi tiết trước khi hỏng — cũng có thể giúp tránh tai nạn. Nhưng "
               "<em>mọi</em> quy trình sẽ có lúc bị vi phạm (cố ý hoặc không). Và với sức ép cắt giảm chi "
               "phí và nhân lực, những quy trình từng khả thi trong quá khứ có thể không còn khả thi hôm "
               "nay hoặc ngày mai."))
    b.append(p("Nếu muốn tính quy trình như một lớp bảo vệ thì quy trình phải được ghi chép, con người phải "
               "được đào tạo để tuân theo, và việc sử dụng phải được kiểm toán. Những kỹ sư và quản lý cho "
               "rằng một số quy trình đang được tuân thủ có thể sẽ sững sờ khi người vận hành và kỹ thuật "
               "viên kể cho họ nghe thực tế diễn ra trong nhà máy. Mà ngược lại, người vận hành và kỹ thuật "
               "viên cũng có thể ngần ngại không muốn báo cáo, vì biết rõ rằng báo cáo chỉ làm công việc "
               "của họ khó hơn."))

    b.append(h3("4.1.5 Hệ dừng / liên động / đo lường an toàn (SIS)",
                "Shutdown/Interlock/Instrumented Systems (SIS)"))
    b.append(p("Nếu hệ điều khiển và người vận hành không hành động, hệ dừng tự động sẽ hành động. Các hệ "
               "này thường hoàn toàn tách rời, có cảm biến, hệ logic và phần tử cuối riêng (xem lại "
               "chương 3 về vấn đề tách rời). Chúng được thiết kế để:"))
    b.append(ol([
        "Cho phép quá trình tiến lên một cách an toàn khi các điều kiện quy định cho phép; hoặc",
        "Tự động đưa quá trình về trạng thái an toàn khi các điều kiện quy định bị vi phạm; hoặc",
        "Hành động để giảm nhẹ hậu quả của một mối nguy công nghiệp.",
    ]))
    b.append(p("Vì vậy một hệ an toàn có thể cung cấp chức năng cho phép (permissive), chức năng ngăn ngừa "
               "và/hoặc chức năng giảm nhẹ. Cần phân biệt <b>SIF</b> (chức năng an toàn đo lường) và "
               "<b>SIS</b> (hệ thống đo lường an toàn). SIF là một chức năng đơn lẻ (ví dụ cắt do áp suất "
               "cao, cắt do mức thấp…), còn SIS là toàn bộ các chức năng kết hợp lại thành hệ tổng thể. "
               "Phần lớn SIF gồm một cảm biến đầu vào và một (hoặc vài) phần tử cuối. Một SIS thì có thể "
               "gồm hàng chục, hàng trăm, thậm chí hàng nghìn đầu vào và đầu ra."))
    b.append(p("Các hệ này đòi hỏi mức bảo mật cao hơn để ngăn thay đổi vô ý và can thiệp trái phép, cũng "
               "như mức chẩn đoán lỗi cao hơn. Cuốn sách này tập trung vào các hệ đó."))

    b.append(h3("4.1.6 Bảo vệ vật lý", "Physical Protection"))
    b.append(p("Van an toàn và đĩa vỡ là một phương tiện bảo vệ vật lý có thể dùng để ngăn điều kiện quá áp. "
               "Dù việc này có thể ngăn một bình áp suất nổ, việc xả vật liệu có thể tạo ra một sự kiện nguy "
               "hiểm thứ cấp (ví dụ phát tán chất độc) hoặc bị phạt vì vi phạm môi trường."))

    # ---------------------------------------------------------------- 4.2
    b.append(h2("4.2 Các lớp giảm nhẹ", "Mitigation Layers"))
    b.append(p("Lớp giảm nhẹ được thực hiện để làm giảm mức nghiêm trọng hay hậu quả của một sự kiện nguy "
               "hiểm khi nó đã xảy ra. Chúng có thể giữ lại, phân tán hoặc trung hòa lượng phát tán."))

    b.append(h3("4.2.1 Hệ chứa giữ", "Containment Systems"))
    b.append(p("Nếu một bồn chứa áp suất khí quyển bị vỡ, bờ bao có thể được dùng để giữ lượng chất thoát ra. "
               "Tuy vậy, giữ chất lỏng quá trình trong bờ bao có thể tạo ra mối nguy thứ cấp. Lò phản ứng "
               "trong nhà máy điện hạt nhân thường được đặt trong tòa nhà chứa để ngăn phát tán ngoài ý "
               "muốn. Lò phản ứng Xô Viết ở Chernobyl không có tòa nhà chứa, còn lò của Hoa Kỳ ở Three Mile "
               "Island thì có."))

    b.append(h3("4.2.2 Tháp rửa khí và tháp đốt", "Scrubbers and Flares"))
    b.append(p("Tháp rửa khí được thiết kế để trung hòa lượng phát tán. Tháp đốt được thiết kế để đốt bỏ "
               "lượng vật liệu dư. Lưu ý rằng Bhopal có cả hai hệ, nhưng cả hai đều không hoạt động trong "
               "giai đoạn bảo dưỡng mà nhà máy đang trải qua lúc đó."))

    b.append(h3("4.2.3 Hệ phát hiện cháy và khí (F&G)", "Fire and Gas (F&amp;G) Systems"))
    b.append(p("Hệ phát hiện cháy và khí gồm cảm biến, bộ giải logic và phần tử cuối, được thiết kế để phát "
               "hiện khí cháy, khí độc hoặc cháy, và sau đó a) cảnh báo tình trạng, b) đưa quá trình về "
               "trạng thái an toàn, hoặc c) hành động để giảm nhẹ hậu quả của sự kiện nguy hiểm. Cảm biến "
               "có thể là đầu báo nhiệt, khói, lửa và/hoặc khí, cùng với hộp gọi tay. Hệ logic có thể là "
               "PLC thông thường, DCS, PLC an toàn, PLC chuyên dụng cho F&G, hoặc bộ điều khiển F&G đa vòng "
               "chuyên dụng. Phần tử cuối có thể là đèn nháy/đèn chớp, còi báo, hệ thông báo qua điện "
               "thoại, kíp nổ, hệ phun nước dập, hệ chữa cháy và/hoặc lệnh dừng quá trình."))
    b.append(p("Một hệ phát hiện khí <em>không</em> ngăn được việc rò khí; nó chỉ chỉ ra việc rò đã xảy ra khi "
               "nào và ở đâu. Tương tự, hệ phát hiện cháy không ngăn được cháy; nó chỉ chỉ ra cháy đã xảy ra "
               "khi nào và ở đâu. Đây là những lớp giảm nhẹ truyền thống, dùng để làm giảm hậu quả của một "
               "sự kiện đã xảy ra. Ở Hoa Kỳ, đây thường là hệ “chỉ cảnh báo” — chúng không thực hiện hành "
               "động điều khiển tự động nào, và đội cứu hỏa phải tới tận nơi dập lửa bằng tay. Ngoài Hoa Kỳ, "
               "các hệ này thường thực hiện một số hành động tự động hoặc được tích hợp với hệ dừng."))
    b.append(p("Một khác biệt lớn giữa hệ dừng và hệ cháy – khí là: hệ dừng bình thường ở trạng thái có điện "
               "(nghĩa là mất điện thì dừng), còn hệ cháy – khí bình thường ở trạng thái không có điện "
               "(nghĩa là có điện thì hành động). Lý do thực ra khá đơn giản. Hệ dừng được thiết kế để đưa "
               "nhà máy về trạng thái an toàn, thường nghĩa là ngừng sản xuất. Việc dừng nhầm (dừng nhà máy "
               "khi thực sự không có gì sai) gây thiệt hại kinh tế do mất thời gian sản xuất, nhưng dừng "
               "nhầm nói chung không thảm khốc về mặt an toàn. Thực tế, các nghiên cứu cho thấy dù hoạt động "
               "dừng/khởi động chỉ chiếm khoảng 4 % tổng thời gian vận hành, khoảng 25 % số tai nạn xảy ra "
               "trong 4 % thời gian đó. Hệ cháy – khí được thiết kế để bảo vệ thiết bị và con người; hoạt "
               "động nhầm của chúng có thể làm hỏng một số thiết bị và thậm chí gây chết người (ví dụ một "
               "lần xả Halon hoặc CO₂ không báo trước trong phòng điều khiển). Nếu hệ bình thường ở trạng "
               "thái không có điện thì lỗi dừng nhầm rất khó xảy ra."))
    b.append(p("Cuộc tranh luận vẫn tiếp tục về việc hệ cháy – khí có phải là hệ thống đo lường an toàn hay "
               "không. Câu trả lời không nên được đưa ra nhẹ nhàng, vì nó ảnh hưởng tới chi phí, phần cứng, "
               "tiêu chuẩn áp dụng, trách nhiệm, tiêu chí thiết kế, vận hành và bảo dưỡng của hệ."))

    b.append(h3("4.2.4 Quy trình sơ tán", "Evacuation Procedures"))
    b.append(p("Trong trường hợp phát tán thảm khốc, quy trình sơ tán có thể được dùng để đưa nhân viên nhà "
               "máy và/hoặc cộng đồng bên ngoài ra khỏi khu vực. Dù đây chỉ là quy trình chứ không phải một "
               "hệ vật lý (ngoài còi báo), nó vẫn có thể được coi là một trong các lớp an toàn tổng thể."))
    b.append(p("Ở Bhopal có một còi báo dùng để cảnh báo người dân xung quanh. Tuy nhiên nó lại có tác dụng "
               "ngoài ý muốn: hút cư dân xung quanh <em>lại gần</em> (giống như con thiêu thân lao vào ánh "
               "sáng) thay vì đẩy họ ra xa."))

    # ---------------------------------------------------------------- 4.3
    b.append(h2("4.3 Đa dạng hóa", "Diversification"))
    b.append(p("Các nhà đầu tư hiểu sự cần thiết của đa dạng hóa. Nếu một nhà đầu tư đặt toàn bộ tiền tiết "
               "kiệm cả đời vào một tài khoản chứng khoán và tài khoản đó phá sản, anh ta mất tất cả. An "
               "toàn hơn là phân tán rủi ro sang nhiều tài khoản: nếu một tài khoản thất bại, các tài khoản "
               "khác hy vọng sẽ bảo vệ khỏi mất toàn bộ. Điều tương tự đúng với các lớp an toàn trong nhà "
               "máy. Đừng bỏ tất cả trứng vào một giỏ, dù cái giỏ tốt tới đâu. Mọi thứ đều hỏng, chỉ là vấn "
               "đề thời điểm. Nói chung, càng nhiều lớp và càng đa dạng thì càng tốt. Ngoài ra, mỗi lớp nên "
               "càng đơn giản càng tốt. Lỗi của một lớp không được ngăn lớp khác thực hiện chức năng của nó."))
    b.append(p("Lợi ích của nhiều lớp đa dạng được thể hiện trên <b>Hình 4-3</b>. Hình này cũng hữu ích để "
               "hiểu khái niệm phân tích lớp bảo vệ (LOPA) sẽ được trình bày ở chương 6. Hãy hình dung tần "
               "suất một sự kiện nguy hiểm có thể gây nhiều người chết cùng lúc, tính theo lần mỗi năm, do "
               "chính thiết kế quá trình cơ bản gây ra. Trên sơ đồ, đó là đường thẳng đứng bên phải, ghi "
               "“rủi ro vốn có của quá trình”. Không ai coi việc mỗi nhà máy có một sự kiện thảm khốc mỗi "
               "năm gây nhiều người chết là “chấp nhận được”. Một mục tiêu mong muốn hơn có thể là khoảng "
               "1/100.000 mỗi năm — đường thẳng đứng bên trái, ghi “mức rủi ro chấp nhận được”."))
    b.append(p("Mỗi lớp an toàn có tác dụng giảm rủi ro. Nhưng không lớp nào hoàn hảo, như <b>Hình 4-1b</b> "
               "cho thấy. Mức hiệu quả (hay độ mạnh) của mỗi lớp có thể biểu diễn bằng độ dài (hay độ rộng) "
               "của mũi tên tương ứng — tức là “hệ số giảm rủi ro” của lớp đó. Mức giảm rủi ro càng lớn thì "
               "mũi tên càng dài. Không lớp nào một mình giảm được rủi ro 100.000 lần; nhưng năm lớp độc "
               "lập, mỗi lớp giảm 10 lần, thì làm được."))
    b.append(fig(3, F.fig_4_3(), "vi"))
    b.append(p("Trong lịch sử, các lớp khác nhau này được thực hiện trong những hệ hoàn toàn tách rời do các "
               "nhà cung cấp khác nhau cung cấp, thường dùng công nghệ rất khác nhau. Mức đa dạng đó làm cho "
               "lỗi do nguyên nhân chung (một lỗi duy nhất tác động nhiều thành phần) trở nên cực kỳ khó "
               "xảy ra. Nhưng ngày nay nhiều hệ trong số đó dùng máy tính và phần mềm. Điều gì sẽ xảy ra "
               "nếu gộp chức năng phát hiện cháy – khí, chức năng dừng và chức năng cảnh báo vào chung hệ "
               "điều khiển quá trình?"))
    b.append(p("Làm nhiều việc hơn trong một hộp không làm nó chạy tốt hơn. Chạy nhiều chương trình hơn "
               "trong một máy tính không làm nó chạy tốt hơn hay nhanh hơn; thực tế thường ngược lại. Một "
               "chiếc Volkswagen Beetle được thiết kế để chở một số người nhất định, đi một quãng đường "
               "nhất định, với một tốc độ nhất định. Nhồi mười anh sinh viên vào đó không làm nó chạy nhanh "
               "hơn. Tương tự, làm nhiều việc hơn trong hệ điều khiển không làm nó chạy tốt hơn. Nói cách "
               "khác, độ dài mũi tên BPCS trên <b>Hình 4-3</b> sẽ không thay đổi chút nào; các tiêu chuẩn "
               "IEC đặt giới hạn tuyên bố cho BPCS ở hệ số giảm rủi ro bằng 10."))
    b.append(p("Từ đó có thể thấy rõ rằng gộp quá nhiều chức năng vào hệ điều khiển có thể làm <em>giảm</em> "
               "an toàn tổng thể của cơ sở, chứ không phải cải thiện nó nhờ công nghệ mới."))

    # ---------------------------------------------------------------- summary
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p("Tai nạn thường là tổ hợp của những sự kiện hiếm mà ban đầu người ta cho là độc lập và sẽ "
               "không xảy ra cùng lúc. Một cách bảo vệ chống lại những trường hợp như vậy là thực hiện nhiều "
               "lớp an toàn đa dạng. Điều đó khiến một sự kiện khởi phát khó lan qua tất cả các lớp để tới "
               "sự kiện nguy hiểm."))
    b.append(p("Nên thực hiện nhiều lớp an toàn độc lập và đa dạng. Một số lớp có mặt để ngăn tai nạn xảy ra "
               "(lớp ngăn ngừa); số khác có mặt để làm giảm hậu quả khi sự kiện đã xảy ra (lớp giảm nhẹ)."))
    b.append(p("Nói chung, càng nhiều lớp an toàn càng tốt. Gộp quá nhiều chức năng vào một lớp duy nhất có "
               "thể có tác dụng ngược là làm giảm an toàn chứ không cải thiện. Tuy vậy, cách phòng thủ tốt "
               "nhất là loại bỏ mối nguy ngay từ giai đoạn thiết kế ban đầu: “Cái bạn không có thì không "
               "thể rò.” Thiết kế an toàn vốn có có thể dẫn tới thiết kế đơn giản hơn với tổng chi phí thấp "
               "hơn."))
    return "\n".join(b)


# ===================================================================== EN
def body_en():
    b = []
    b.append(lead(
        "Accidents rarely have a single cause. This chapter retells Bhopal — not for the casualty figures, "
        "but because the sequence shows a dozen separate decisions, each reasonable in its own context and "
        "each small, lining up. It then sorts the protection layers into prevention and mitigation, and "
        "explains why cramming more functions into one layer makes the whole plant less safe rather than "
        "more."))

    b.append(h2("Every layer was removed for a good reason"))
    b.append(p("Read the Bhopal sequence as a list of engineering decisions rather than as a tragedy. The "
               "refrigeration was switched off to save money. The alarm threshold was raised to match the "
               "new storage temperature, which is a perfectly logical thing to do once the refrigeration "
               "is off. The scrubber was left idle because the plant was not producing. The flare was down "
               "for maintenance, which is when flares are normally maintained. The slip blinds were not "
               "fitted because the job was a wash-out, not a vessel entry. The gauges were disbelieved "
               "because they were known to be unreliable."))
    b.append(p("Not one of those decisions was made by someone trying to cause an accident. Each was made "
               "by someone optimising the thing in front of them — cost, schedule, production, nuisance "
               "alarms. The layers failed not because they were badly designed but because each was "
               "individually negotiable, and the negotiation was always won by whoever was closest to the "
               "immediate problem. That is the argument for independence in one sentence: a layer that can "
               "be switched off by the person it inconveniences is not a layer."))

    b.append(h2("Prevention and mitigation are different businesses"))
    b.append(p("The distinction sounds academic until you try to buy one. A prevention layer competes with "
               "production for the same equipment, the same instrument, the same maintenance window; its "
               "value is invisible because the accidents it prevents do not appear in any report. A "
               "mitigation layer sits outside the production path and is easier to justify, but by "
               "definition it only pays out after the plant has already failed."))
    b.append(p("This is why the onion diagram is drawn as concentric rings rather than as a list. The "
               "innermost rings are the ones the operating team touches every day, and they are therefore "
               "the ones most exposed to the pressure to keep running. The outermost rings — the dikes, the "
               "flare, the evacuation plan — are touched by almost nobody, and they are the ones that still "
               "work when everything inside has been compromised. A plant with excellent inner layers and "
               "no outer ones is a plant that has never had a bad day."))

    b.append(h2("Alarms are the weakest layer, and the most used"))
    b.append(p("Alarms occupy a strange position: they are cheap, they are easy to add, and they are the "
               "layer most often counted on in a hazard study. They are also the layer with the worst "
               "record, for a reason that has nothing to do with the instruments. An alarm transfers the "
               "problem to a human being under time pressure, and the human being is the component whose "
               "behaviour is least predictable and least testable."))
    b.append(p("The 17,000-message DCS printout is the extreme case of a general rule: an alarm system's "
               "value collapses as its count rises. A single high-pressure alarm at three in the morning "
               "gets a response. The same alarm among two hundred others in the same hour gets a shrug, "
               "because the operator has learned — correctly, from experience — that almost all of them "
               "are noise. Alarm rationalisation is therefore not housekeeping; it is the only thing that "
               "keeps the layer alive."))
    b.append(p("The finding that people make the wrong decision 99 % of the time when given under a minute "
               "to choose is worth sitting with. It does not mean operators are incompetent. It means that "
               "a layer whose success depends on a fast, correct decision under stress has a performance "
               "that cannot be claimed with any confidence, and should not be assigned a serious risk "
               "reduction factor in a LOPA study."))

    b.append(h2("Why more functions in one box makes the plant less safe"))
    b.append(p("The Volkswagen Beetle analogy in the source is worth keeping because it is quantitative "
               "rather than rhetorical. A protection layer's claimed risk reduction factor is a property "
               "of the layer, not of the processor it runs on. Moving the fire and gas logic into the BPCS "
               "does not add a factor of ten to the BPCS; it subtracts one, because the combined system now "
               "shares a failure mode that neither had alone, and because the IEC standards cap the BPCS "
               "claim at ten precisely to reflect that."))
    b.append(p("The same logic explains why the standards are so insistent about field devices. A shared "
               "transmitter is a shared failure, and a shared impulse line is a shared failure that no "
               "amount of logic redundancy can see. Diversification is not a preference for old "
               "technology; it is the recognition that the cheapest way to avoid a common cause failure is "
               "to make the two paths physically incapable of sharing one."))
    return "\n".join(b)
