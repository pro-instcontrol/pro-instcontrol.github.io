# -*- coding: utf-8 -*-
"""Handbook 6.6 — Bore Gaging Displacement Sensors."""
import hb06fig as F
from hb06_common import eq, fig, h2, h3, nav, note, p, quote, refs, table, ul

# Flexbar plug-gage price list: (range text, handle, [(class, q1, q2-4, q5-10), ...])
_FLEX = [
    ("0,01–0,030 in · 0,25–0,762 mm", "1W", [("XX", "35,45", "28,65", "22,26"), ("X", "31,15", "23,35", "17,00"),
                                            ("Y", "28,35", "22,15", "15,05"), ("Z", "25,65", "20,70", "12,55")]),
    ("0,03–0,075 in · 0,762–1,91 mm", "1W", [("XX", "19,25", "15,30", "13,63"), ("X", "15,05", "11,70", "10,60"),
                                            ("Y", "13,90", "10,80", "9,40"), ("Z", "11,40", "9,35", "8,15")]),
    ("0,075–0,180 in · 1,91–4,57 mm", "2W", [("XX", "21,15", "17,00", "14,80"), ("X", "18,15", "14,45", "12,85"),
                                            ("Y", "17,00", "13,90", "11,25"), ("Z", "14,00", "11,10", "9,65")]),
    ("0,180–0,281 in · 4,57–7,14 mm", "3W", [("XX", "22,00", "17,80", "15,30"), ("X", "18,90", "15,30", "13,10"),
                                            ("Y", "17,85", "13,55", "11,95"), ("Z", "14,30", "11,40", "9,90")]),
    ("0,281–0,406 in · 7,17–10,31 mm", "4W", [("XX", "24,20", "19,50", "17,80"), ("X", "21,15", "17,00", "14,80"),
                                             ("Y", "19,30", "15,65", "13,80"), ("Z", "14,90", "12,00", "10,50")]),
    ("0,406–0,510 in · 10,31–12,95 mm", "5W", [("XX", "25,35", "20,35", "17,80"), ("X", "22,25", "17,80", "15,80"),
                                              ("Y", "20,45", "16,50", "14,55"), ("Z", "16,30", "13,15", "11,30")]),
    ("0,510–0,635 in · 12,95–16,13 mm", "6W", [("XX", "26,70", "21,45", "18,50"), ("X", "23,70", "19,25", "16,30"),
                                              ("Y", "21,85", "17,60", "15,50"), ("Z", "17,50", "14,30", "12,55")]),
    ("0,635–0,760 in · 16,13–19,30 mm", "7W", [("XX", "28,15", "22,60", "19,85"), ("X", "25,35", "20,05", "17,50"),
                                              ("Y", "23,25", "18,45", "16,40"), ("Z", "18,65", "15,15", "13,45")]),
    ("0,780–1,010 in · 19,30–25,65 mm", "8W", [("XX", "44,25", "34,25", "32,80"), ("X", "39,56", "29,80", "27,30"),
                                              ("Y", "36,30", "27,25", "24,90"), ("Z", "32,40", "25,65", "24,20")]),
]

# Intrimic internal micrometers: (range, tool no, price)
_INTRIMIC = [
    ("0,275–0,350 in (6–8 mm)", "599-290-35", "745,40"),
    ("0,350–0,425 in (8–10 mm)", "599-290-42", "745,40"),
    ("0,425–0,500 in (10–12 mm)", "599-290-50", "745,40"),
    ("0,500–0,600 in (12–14 mm)", "599-290-60", "826,70"),
    ("0,600–0,700 in (14–17 mm)", "599-290-70", "826,70"),
    ("0,700–0,800 in (17–20 mm)", "599-290-80", "826,70"),
    ("0,800–1,000 in (20–25 mm)", "599-290-100", "843,60"),
    ("1,000–1,200 in (25–30 mm)", "599-290-120", "843,60"),
    ("1,200–1,400 in (30–35 mm)", "599-290-140", "854,30"),
    ("1,400–1,600 in (35–40 mm)", "599-290-160", "854,30"),
    ("1,600–2,000 in (40–50 mm)", "599-290-200", "933,10"),
    ("2,000–2,400 in (50–60 mm)", "599-290-240", "933,10"),
    ("2,400–2,800 in (60–70 mm)", "599-290-280", "933,10"),
    ("2,800–3,200 in (70–80 mm)", "599-290-320", "950,20"),
    ("3,200–3,600 in (80–90 mm)", "599-290-360", "950,20"),
    ("3,600–4,000 in (90–100 mm)", "599-290-400", "950,20"),
    ("Bộ đầy đủ Intrimik Plus #5", "599-290-5", "3 374,60"),
]

# TRIOMATIC electronic bore gages
_TRIO = [
    ("0,600–0,800 in (12–15 mm)", "62-32005", "1 492,60"),
    ("0,800–1,000 in (20–25 mm)", "62-32006", "1 501,20"),
    ("1,000–1,200 in (25–30 mm)", "62-32007", "1 515,40"),
    ("1,200–1,600 in (30–40 mm)", "62-32008", "1 578,10"),
    ("1,600–2,000 in (40–50 mm)", "62-32009", "1 612,40"),
    ("2,000–2,400 in (50–60 mm)", "62-32010", "1 639,70"),
    ("2,400–2,800 in (60–70 mm)", "62-32011", "1 697,10"),
    ("2,800–3,200 in (70–80 mm)", "62-32012", "1 695,90"),
    ("3,200–3,600 in (80–90 mm)", "62-32013", "1 702,10"),
    ("3,600–4,000 in (90–100 mm)", "62-32014", "1 759,60"),
    ("4,000–4,400 in (100–110 mm)", "62-32015", "1 759,60"),
    ("4,400–4,800 in (110–120 mm)", "62-32016", "1 759,60"),
]


def body_vi():
    b = []
    b.append(p(
        "Kích thước là một phần trong toàn bộ đặc tả mà kỹ thuật giao cho chi tiết. Thế nhưng người kỹ sư trong "
        "công nghiệp luôn phải đối diện với một sự thật: không có hai vật thể nào trong thế giới vật chất được chế "
        "tạo giống hệt nhau. Những dao động nhỏ xuất hiện trong sản xuất lặp lại phải được tính đến ngay từ khâu "
        "thiết kế. Để cho người thợ biết được phép lệch bao nhiêu so với kích thước chính xác, nhà thiết kế dùng "
        "kỹ thuật dung sai hay kích thước giới hạn. Dung sai được định nghĩa là toàn bộ lượng biến thiên cho phép "
        "của kích thước, tức hiệu giữa hai giới hạn kích thước. Kích thước giới hạn là những kích thước lớn nhất và "
        "nhỏ nhất cho phép. Thực hành ghi dung sai đúng đắn bảo đảm sản phẩm hoàn thiện hoạt động đúng như chủ định "
        "và tồn tại được trong suốt tuổi thọ dự kiến."))

    # ---------------------------------------------------------------- tolerance
    b.append(h2("Dung sai lỗ", "Bore tolerancing"))
    b.append(p(
        "Mọi kích thước lỗ ghi trên bản vẽ — trừ những kích thước được ghi rõ là kích thước cơ bản, kích thước "
        "kiểm, kích thước tham chiếu, kích thước lớn nhất hay nhỏ nhất — đều phải có dung sai xác định, hoặc ghi "
        "trực tiếp ngay sau kích thước, hoặc chỉ định bằng các ghi chú dung sai chung. Với một kích thước thập phân "
        "được ghi dung sai trực tiếp, dung sai có cùng số chữ số thập phân với phần thập phân của kích thước."))
    b.append(p(
        "Dung sai kỹ thuật có thể chia thành ba nhóm lớn: (1) dung sai kích thước gán cho các kích thước như chiều "
        "dài, đường kính và góc; (2) dung sai hình học dùng để khống chế hình dạng của lỗ theo phương dọc trục và "
        "phương ngang; và (3) dung sai vị trí dùng để khống chế vị trí tương đối của các bề mặt lắp ghép. Bạn đọc "
        "quan tâm có thể tham khảo [1, 2]."))
    b.append(p(
        "Hệ giới hạn và lắp ghép ISO (Khuyến nghị ISO R 286) bao gồm dung sai và sai lệch tiêu chuẩn cho các kích "
        "thước tới 3150 mm. Hệ này dựa trên một dãy dung sai được phân cấp để phù hợp với mọi loại công việc, từ "
        "tinh xảo nhất đến thô nhất, cùng với các kiểu lắp khác nhau, từ lắp hở nhiều đến lắp chặt nặng. Ở đây "
        "<i>lắp</i> là thuật ngữ chung để chỉ khoảng độ chặt có thể phát sinh khi áp dụng một tổ hợp dung sai cụ "
        "thể trong thiết kế các chi tiết lắp ghép với nhau."))
    b.append(p(
        "Có 18 cấp dung sai nhằm đáp ứng yêu cầu của các loại chi tiết khác nhau. Các cấp này được gọi là IT, từ "
        "IT 01, IT 02 (dành cho tương lai) và IT 1 đến IT 16 (dùng ngày nay). Trong mỗi cấp, trị số dung sai tăng "
        "theo kích thước theo một công thức liên hệ một hằng số cho trước với đường kính trung bình của dải kích "
        "thước tương ứng. Hệ thống đưa ra 27 sai lệch cơ bản cho các kích thước tới 500 mm và 14 sai lệch cho các "
        "kích thước lớn hơn, tạo ra các kiểu lắp từ hở nhiều đến chặt nặng. Bạn đọc quan tâm có thể tham khảo [3]."))

    # ---------------------------------------------------------------- classification
    b.append(h2("Phân loại và đặc tả căn lỗ", "Bore gage classification and specification"))
    b.append(p(
        "Để đo được những dung sai kể trên, nền sản xuất hiện đại cần dùng đến căn. <i>Căn</i> được định nghĩa là "
        "một thiết bị dùng để khảo sát mức phù hợp về kích thước của một chi tiết đối với chức năng cụ thể của nó. "
        "<i>Kiểm bằng căn</i> được ANSI định nghĩa là quá trình đo vật liệu đã chế tạo nhằm bảo đảm độ đồng đều về "
        "kích thước và đường bao mà các ngành công nghiệp yêu cầu. Nhờ đó việc kiểm bằng căn bảo đảm chi tiết hoạt "
        "động đúng và lắp lẫn được; nghĩa là một chi tiết sẽ lắp vừa đúng chỗ như bất kỳ chi tiết tương tự nào và "
        "thực hiện đúng chức năng, dù là cho lần lắp ráp ban đầu hay cho lần thay thế trong sử dụng."))
    b.append(p("Căn lỗ có thể được phân loại như sau:"))
    b.append(ul([
        "Căn chuẩn (master gages)",
        "Căn kiểm tra (inspection gages)",
        "Căn của nhà chế tạo (manufacturer’s gages)",
        "Căn khống chế kích thước",
        "Căn khống chế các tham số hình học của lỗ",
        "Căn làm việc giới hạn cố định",
        "Căn chỉ thị biến thiên (variable indicating)",
        "Căn kiểm sau gia công (post-process)",
        "Căn kiểm trong gia công (in-process)",
    ]))
    b.append(p(
        "Căn chuẩn được chế tạo theo kích thước cơ bản của chúng một cách chính xác nhất có thể và được dùng làm "
        "chuẩn tham chiếu, chẳng hạn để kiểm tra hay đặt zero cho căn kiểm tra hoặc căn của nhà chế tạo. Căn kiểm "
        "tra do nhân viên kiểm tra dùng để kiểm sản phẩm đã chế tạo. Căn của nhà chế tạo dùng để kiểm chi tiết "
        "ngay trong quá trình sản xuất."))
    b.append(p(
        "Căn kiểm sau gia công dùng để kiểm chi tiết sau khi đã chế tạo xong. Về cơ bản loại căn này làm hai việc: "
        "(1) khống chế kích thước sản phẩm trong giới hạn quy định, và (2) phân loại hay loại bỏ những sản phẩm "
        "nằm ngoài giới hạn ấy. Kiểm sau gia công có hồi tiếp là một kỹ thuật nâng cao độ chính xác chi tiết bằng "
        "cách dùng kết quả kiểm chi tiết để bù những sai số lặp lại trên đường chạy của máy công cụ. Quá trình này "
        "thường được áp dụng cho máy điều khiển số (CNC), dùng số liệu kiểm để sửa chương trình gia công, và cho "
        "máy chép hình, dùng chính số liệu ấy để sửa mẫu chép."))
    b.append(p(
        "Căn kiểm trong gia công dùng để kiểm chi tiết ngay trong chu trình gia công. Trong chiến lược sản xuất "
        "hiện nay, căn kiểm trong gia công cùng phần mềm thu thập số liệu cho phản hồi về chất lượng nhanh hơn. "
        "Thật vậy, khía cạnh thu thập và phân phối số liệu của việc kiểm tra 100% đã trở nên quan trọng ngang với "
        "chính công nghệ kiểm. Phần mềm được thiết kế riêng để thu thập thông tin từ nhiều căn, đo hàng chục loại "
        "và cỡ sản phẩm, rồi cung cấp cho cả nhân viên kiểm tra lưu động lẫn cán bộ giám sát chất lượng khi cần, "
        "đang nhanh chóng trở thành một phần của chiến lược kiểm soát chất lượng. Kết hợp với các đơn vị điều khiển "
        "số (CNC), kiểm trong gia công có thể tự động bù độ lệch gá đặt của phôi, biến thiên chiều dài dao và sai "
        "số do mòn dao."))

    # ---------------------------------------------------------------- dimensions
    b.append(h2("Căn khống chế kích thước", "Gages that control dimensions"))
    b.append(p(
        "Căn khống chế kích thước dùng để khống chế đường kính lỗ. Những căn này có thể là căn kiểm sau gia công "
        "hoặc kiểm trong gia công. Hơn nữa, chúng có thể là căn giới hạn cố định hoặc căn chỉ thị biến thiên."))
    b.append(p(
        "Căn nút (plug gage) là một căn làm việc giới hạn cố định dùng cho lỗ. Những căn rẻ tiền này không thực sự "
        "đo kích thước hay hình học; chúng chỉ cho người vận hành biết lỗ to quá hay nhỏ quá. Thiết kế thực tế của "
        "phần lớn căn nút là tiêu chuẩn, được quy định trong các chuẩn Thiết kế Căn Hoa Kỳ (AGD). Tuy vậy, có nhiều "
        "trường hợp phải thiết kế căn nút đặc biệt."))
    b.append(p(
        "Căn nút thường gồm hai chi tiết. Một chi tiết gọi là đầu “qua” (go), chi tiết kia là đầu “không qua” "
        "(no-go hay not-go). Căn thường có hai phần: phần thân đo và một tay cầm có ghi dấu “qua” hoặc “không qua” "
        "cùng dung sai chế tạo căn. Nói chung có ba kiểu căn nút tiêu chuẩn AGD. Thứ nhất là căn nút một đầu "
        "(Hình 6-53a); thứ hai là căn hai đầu (Hình 6-53b); và thứ ba là căn lũy tiến (Hình 6-53c). Bạn đọc quan "
        "tâm có thể tham khảo [4]."))
    b.append(fig(53, F.fig_6_53()))
    b.append(p(
        "Dung sai của căn giới hạn cố định thường được xác định từ lượng dung sai của chi tiết. Quy tắc 10% thường "
        "được dùng để xác định lượng dung sai căn cho các căn giới hạn cố định. Ủy ban Thiết kế Căn Hoa Kỳ đã lập "
        "ra bốn cấp dung sai chế tạo căn và bốn cấp này được dùng phổ biến [4]. Bốn cấp ấy quy định mức biến thiên "
        "lớn nhất cho mọi cỡ căn được thiết kế. Độ chính xác cần thiết quyết định cấp căn sẽ dùng. Bảng 6-11 trình "
        "bày bốn cấp dung sai chế tạo căn này. Căn cấp XX chủ yếu dùng làm căn chuẩn và để kiểm tra tinh cuối cùng. "
        "Căn cấp X dùng cho một số công việc căn chuẩn, đồng thời làm căn kiểm tra và căn làm việc có dung sai chặt. "
        "Căn cấp Y dùng làm căn kiểm tra và căn làm việc. Căn cấp Z dùng làm căn làm việc ở nơi dung sai chi tiết "
        "lớn. Bảng 6-12 cho các dải đường kính và giá của căn nút do Flexbar Machine Corp. chế tạo."))
    b.append(table(
        ["Tới (mm)", "Bao gồm (mm)", "Cấp XX", "Cấp X", "Cấp Y", "Cấp Z"],
        [["0,254", "20,95", "0,00051", "0,00102", "0,00178", "0,00254"],
         ["20,95", "38,35", "0,00076", "0,00152", "0,00229", "0,00305"],
         ["38,35", "63,75", "0,00102", "0,00203", "0,00305", "0,00406"],
         ["63,75", "114,55", "0,00127", "0,00254", "0,00381", "0,00508"]],
        "Bảng 6-11 · Dung sai chế tạo căn tiêu chuẩn (mm). Tương ứng theo inch: 0,010–0,825 in; 0,825–1,510 in; "
        "1,510–2,510 in; 2,510–4,510 in."))
    _rows = []
    for rng, handle, items in _FLEX:
        for cls, q1, q24, q510 in items:
            _rows.append([rng if cls == "XX" else "", handle if cls == "XX" else "", cls, q1, q24, q510])
    b.append(table(
        ["Dải kích thước", "Tay cầm", "Cấp", "SL 1", "SL 2–4", "SL 5–10"],
        _rows,
        "Bảng 6-12 · Căn nút GO/NO GO bằng thép tôi chất lượng cao của Flexbar Machine Corp., giá tính bằng USD "
        "theo số lượng đặt hàng. Tay cầm bán riêng."))
    b.append(p(
        "Căn chỉ thị biến thiên cho phép người dùng kiểm một số tham số của lỗ và nhận được con số để vẽ biểu đồ "
        "cũng như để kiểm soát quá trình bằng thống kê (viết tắt là SPC). Những căn này có một ưu điểm chính so với "
        "căn cố định: chúng cho biết lỗ to hay nhỏ hơn bao nhiêu. Khi dùng căn chỉ thị biến thiên, phải dùng một "
        "vòng chuẩn đúng bằng đường kính danh nghĩa cần kiểm để đặt căn về zero. Sau đó, khi áp căn vào lỗ, lượng "
        "lệch so với zero được đọc trên mặt số. Hình 6-54 minh hoạ đồng hồ đo lỗ hai điểm tiếp xúc — loại dụng cụ "
        "đo lỗ phổ biến nhất trong công nghiệp — và Hình 6-55 giới thiệu một bộ đồng hồ đo lỗ cho dải 35 mm đến "
        "150 mm."))
    b.append(fig(54, F.fig_6_54()))
    b.append(fig(55, F.fig_6_55()))
    b.append(p(
        "Hình 6-56 giới thiệu panme đo trong Intrimic® plus (Brown &amp; Sharpe). Intrimic® plus cho khả năng đo "
        "trong đơn giản và chính xác. Panme có chức năng tự tắt, chế độ ghi nhớ điện tử, chuyển đổi tức thời giữa "
        "hệ inch và hệ mét, cùng đầu ra trực tiếp tiêu chuẩn cho các ứng dụng SPC. Việc phân loại dung sai chỉ trong "
        "một cái nhìn cho phép phân loại nhanh và hiệu quả trong khi kiểm. Màn hình hiển thị cho nhân viên kiểm tra, "
        "bằng màu, biết kích thước nào nằm trong dung sai (xanh), ngoài dung sai (đỏ) hay còn sửa được (vàng). "
        "Bảng 6-13 trình bày các dải cơ bản và giá của những panme này."))
    b.append(fig(56, F.fig_6_56()))
    b.append(table(
        ["Dải đo", "Mã hiệu B&amp;S", "Giá (USD)"],
        [[r, t, g] for r, t, g in _INTRIMIC],
        "Bảng 6-13 · Panme đo trong Intrimik® Plus của Brown &amp; Sharpe."))

    # ---------------------------------------------------------------- geometry
    b.append(h2("Căn khống chế hình dạng", "Gages that control geometry"))
    b.append(p(
        "Căn khống chế các tham số hình học của lỗ dùng để so sánh phức hợp giữa hình dạng chi tiết và hình dạng lý "
        "tưởng. Tất cả những căn này đều là căn kiểm sau gia công. Có hai nhóm lớn đang được dùng: căn dùng hệ đầu "
        "đo thủ công và máy đo hình dạng."))

    b.append(h3("Căn dùng hệ đầu đo thủ công", "Gages with manual probe head systems"))
    b.append(p(
        "Căn hình dạng dùng hệ đầu đo thủ công đang nhanh chóng trở nên phổ biến trong nhiều ứng dụng gia công kim "
        "loại chính xác cao. Dạng đơn giản nhất của hệ đầu đo thủ công đang được dùng rộng rãi là đầu đo lỗ bằng "
        "khí, hay trục khí (Hình 6-57). Khí nén từ bộ chỉ thị của căn khí được dẫn vào đầu đo và thoát ra từ hai "
        "vòi phun trở lên trên chu vi. Khi đầu đo khí được đưa vào lỗ, dòng khí thoát ra bị hạn chế bởi khe hở giữa "
        "mặt vòi phun và thành lỗ. Những thay đổi nhỏ của khe hở khi đưa đầu đo vào những lỗ có kích thước khác "
        "nhau tạo ra thay đổi về lưu lượng hay áp suất ngược trong mạch. Việc phóng đại và đặt chuẩn cho các hệ có "
        "lỗ điều chỉnh biến thiên và nhánh xả zero được thực hiện bằng các lỗ chuẩn."))
    b.append(fig(57, F.fig_6_57()))
    b.append(p(
        "Một số dạng sai lệch hình dạng có thể phát hiện được bằng đầu đo khí là: (1) độ côn, (2) miệng loe, "
        "(3) phình giữa, (4) ô van và (5) múi. Hình 6-58b minh hoạ năm dạng ấy. Các trục khí lỗ hở kiểu Dearborn "
        "(Dearborn Gage Company, MI) có sẵn theo tiêu chuẩn để đo lỗ thông, lỗ kín và lỗ có khoét, với đường kính "
        "từ 0,070 in (2 mm) đến 6,000 in (154 mm)."))
    b.append(p(
        "Một loại căn hình dạng khác dùng hệ đầu đo thủ công là căn lỗ điện tử. Những căn này đo lỗ ở nhiều độ sâu "
        "khác nhau để xác định các trạng thái như miệng loe, độ côn, lồi hay lõm. Chúng cũng xác định được trạng "
        "thái không tròn khi được trang bị hệ đo ba điểm. Hình 6-58a minh hoạ đầu đo ba điểm tiếp xúc cách nhau "
        "120°, và Bảng 6-14 trình bày các dải cơ bản cùng giá của căn lỗ điện tử TRIOMATIC® (Brown &amp; Sharpe)."))
    b.append(fig(58, F.fig_6_58()))
    b.append(p(
        "Căn lỗ điện tử TRIOMATIC® có chức năng tự tắt, chế độ ghi nhớ điện tử, chuyển đổi tức thời giữa inch và "
        "mét, cùng đầu ra trực tiếp tiêu chuẩn tới hệ xử lý số liệu phục vụ SPC và kiểm soát chất lượng bằng thống "
        "kê. Về mặt cơ khí, chúng dùng các đầu thay thế ba điểm tiếp xúc đã được kiểm chứng qua thời gian. Các điểm "
        "tiếp xúc cách nhau 120°, bảo đảm định tâm và căn thẳng đúng — đặc biệt thiết yếu với lỗ sâu. Đầu của các "
        "điểm tiếp xúc làm bằng cacbit vonfram để chống mòn và vươn tới bề mặt của đầu đo, nhờ đó đo được ở đáy lỗ "
        "kín hay trên mặt các bậc bên trong lỗ. Vì các đầu này nối với một hệ đo điện tử dẫn động bằng côn, người "
        "ta gọi chúng là căn điện tử."))
    b.append(table(
        ["Dải đo", "Mã hiệu B&amp;S", "Giá (USD)"],
        [[r, t, g] for r, t, g in _TRIO],
        "Bảng 6-14 · Căn lỗ điện tử TRIOMATIC® của Brown &amp; Sharpe. Bộ TRIOMATIC II gồm các dải 12–30 mm "
        "(62-32001), 30–60 mm (62-32002), 60–90 mm (62-32003) và 90–120 mm (62-32004)."))

    b.append(h3("Máy đo hình dạng", "Form measuring instruments"))
    b.append(p(
        "Hầu hết các máy đo hình dạng hiện đại gá chi tiết trên một bàn quay và tạo phương tiện định vị đầu đo áp "
        "vào chi tiết (Hình 6-59). Khi bàn quay, đầu đo ghi độ lệch so với đường tròn thật. Những máy mà đầu đo "
        "được đỡ bằng một giá đỡ đơn giản, cứng vững, quay tay hoặc chạy motor, không có điều khiển định vị chính "
        "xác, có khả năng thực hiện các phép đo sau: độ tròn, độ đồng tâm, độ đảo hướng kính, độ phẳng theo vòng, "
        "độ vuông góc, độ đảo mặt phẳng, độ đảo mặt trên và mặt dưới, độ song song theo vòng và độ đồng trục."))
    b.append(fig(59, F.fig_6_59()))
    b.append(p(
        "Những máy tự động hoàn toàn hiện đại là loại thiết bị đo tinh vi nhất. Thông thường chúng được trang bị "
        "giao diện đồ hoạ thân thiện với PC, chạy trên Windows™, để thu thập và xử lý số liệu theo thời gian thực. "
        "Mitutoyo/MTI Corp. sản xuất nhiều loại máy như vậy (Bảng 6-15). Dòng RA-600 (Hình 6-60) có phương pháp tự "
        "động hoàn toàn và rất mới, cho phép máy tự định tâm và tự cân bằng nếu phát hiện độ lệch trong lần đo sơ "
        "bộ. Ngoài ra, những máy này còn đo được độ dày, độ vuông góc, độ trụ, độ trụ xoắn, độ thẳng, độ đảo toàn "
        "phần, độ thẳng đứng và độ song song thẳng đứng. Máy được cung cấp kèm phần mềm thu thập số liệu "
        "MeasurLink® cho Windows™, cho phép phân tích số liệu đo ngay lập tức và phản hồi cho các lần kiểm biến "
        "thiên, kiểm thuộc tính và kiểm ngắn. Phần mềm cho phép cán bộ quản lý chất lượng và sản xuất lập các danh "
        "sách truy xuất không giới hạn độ dài. Những thông tin như trung tâm gia công, người vận hành, vật liệu sử "
        "dụng, nguyên nhân được quy trách nhiệm và các dữ liệu liên quan khác có thể được lưu và gắn kèm theo từng "
        "giá trị đo."))
    b.append(fig(60, F.fig_6_60()))
    b.append(table(
        ["Thông số", "RA-112", "RA-334", "RA-434", "RA-661"],
        [["Đường kính đo lớn nhất", "11 in (280 mm)", "11,8 in (300 mm)", "11,8 in (300 mm)", "—"],
         ["Chiều cao đo lớn nhất", "8,6 in (220 mm)", "27,6 in (700 mm)", "13,8 in (350 mm)", "—"],
         ["Đường kính tải lớn nhất", "—", "21,7 in (550 mm)", "20,4 in (520 mm)", "—"],
         ["Khả năng tải", "22 lb (10 kg)", "66,1 lb (30 kg)", "132 lb (60 kg)", "—"],
         ["Dải đầu đo", "±0,01 in (±250 µm)", "±0,012 in (±300 µm)", "±0,012 in (±300 µm)", "—"],
         ["Lực đo", "7–10 gf", "7–10 gf", "—", "—"],
         ["Độ chính xác quay của bàn", "(1,6 + 0,3H) µin<br>(0,04 + 0,3H) µm", "(1,6 + 0,6H) µin<br>(0,04 + 0,6H) µm",
          "(1,6 + 0,6H) µin<br>(0,04 + 0,6H) µm", "—"],
         ["Dải điều chỉnh định tâm", "±0,08 in (±2 mm)", "±0,2 in (±5 mm)", "±0,2 in (±5 mm)", "—"],
         ["Dải điều chỉnh cân bằng", "±1°", "±1°", "—", "—"],
         ["Tốc độ quay", "6 vòng/phút", "2, 4, 6 vòng/phút", "—", "—"],
         ["Độ phóng đại đo", "100–20 000×", "100–50 000×", "100–100 000×", "—"],
         ["Khối lượng bộ đo", "61,7 lb (28 kg)", "276 lb (125 kg)", "298 lb (135 kg)", "770 lb (350 kg)"],
         ["Giá cơ bản (USD)", "17 000", "45 000", "60 000", "60 000"]],
        "Bảng 6-15 · Máy đo độ tròn Rountest của Mitutoyo/MTI Corp. H là chiều cao đo tính bằng inch (hoặc mm) "
        "tuỳ hệ đơn vị."))

    # ---------------------------------------------------------------- GRR
    b.append(h2("Tiêu chuẩn năng lực GAGE R&amp;R", "GAGE R and R standards"))
    b.append(p(
        "Các tiêu chuẩn năng lực về độ lặp lại và độ tái lập của dụng cụ đo (GAGE R AND R) có ảnh hưởng trực tiếp "
        "tới cả nhà chế tạo chi tiết lẫn nhà chế tạo căn. <i>Độ lặp lại</i> là khả năng của một người vận hành dùng "
        "một căn duy nhất thu được những kết quả đo giống nhau trong một loạt lần thử. <i>Độ tái lập</i> là khả "
        "năng của những người vận hành khác nhau thu được kết quả tương tự nhau với cùng một căn. GAGE R AND R hoà "
        "hai yếu tố này lại để xác định độ tin cậy của một hệ đo và mức phù hợp của nó với một ứng dụng đo cụ thể. "
        "Chẳng hạn, một thiết kế căn đáp ứng tiêu chuẩn GAGE R AND R cho lỗ 50 mm (2 in) có thể không đạt yêu cầu "
        "trên lỗ 250 mm (10 in). Một căn đáp ứng dung sai 2 µm có thể không đạt yêu cầu ở dung sai 1 µm. Các tiêu "
        "chuẩn GAGE R AND R giúp nhà chế tạo chi tiết xác định được căn tốt nhất cho từng ứng dụng và ở từng mức "
        "dung sai."))
    b.append(p(
        "Việc ISO 9004 ngày càng được chấp nhận như một triết lý chất lượng quốc tế đang tạo ra những thay đổi đáng "
        "kể cho các nhà sản xuất. Thay đổi quan trọng nhất mà ISO 9004 sẽ tạo ra là nhu cầu về các tiêu chuẩn năng "
        "lực GAGE R AND R mang tính quốc tế và sự bảo đảm về một sân chơi bình đẳng. Trước đây, nhà chế tạo căn và "
        "nhà chế tạo chi tiết có nhiều bộ tiêu chí đo khác nhau. Nay, khi thiết lập các tiêu chuẩn năng lực GAGE R "
        "AND R song hành cùng các tiêu chuẩn ISO 9004, sẽ có một bộ tiêu chuẩn quốc tế áp dụng cho mọi người. Một "
        "bộ số liệu đo từ châu Âu sẽ có cùng ý nghĩa như một bộ từ Bắc Mỹ hay từ châu Á."))
    b.append(p("Các yếu tố ảnh hưởng tới năng lực GAGE R AND R khi kiểm một lỗ bao gồm:"))
    b.append(ul([
        "<b>Biến thiên do căn lỗ:</b> gồm độ tuyến tính, độ lặp lại, độ ổn định và việc hiệu chuẩn.",
        "<b>Biến thiên do thao tác với căn lỗ:</b> gồm độ lặp lại của một người vận hành dùng căn và độ tái lập "
        "của những người vận hành khác nhau dùng cùng một căn.",
        "<b>Biến thiên do dây chuyền sản xuất:</b> do độ nhẵn bề mặt chi tiết, sai số gá đặt khi áp dụng và thay "
        "đổi nhiệt độ.",
    ]))
    b.append(p(
        "Hãng Dyer (Dyer, Lancaster, PA 17604) công bố các dải biến thiên sau cho dòng căn lỗ 830 và 230 của mình: "
        "độ tuyến tính ±0,001 mm (±0,000040 in); độ lặp lại nhỏ hơn ±0,00025 mm (±0,000010 in); độ ổn định — căn lỗ "
        "được chế tạo từ một loại thép hợp kim đặc biệt chống lại thay đổi nhiệt độ hay “nhiệt từ tay”, kết cấu "
        "kín bảo đảm độ tin cậy của tính năng ngay cả trong điều kiện ẩm hay dính dầu; độ lặp lại của một người "
        "vận hành — căn không bị nghiêng và tự định tâm theo cả phương dọc trục lẫn phương hướng kính của lỗ, người "
        "vận hành có thể đặt tay lên hoặc rời khỏi căn mà không ảnh hưởng gì tới phép đo; nhờ tự căn chỉnh, kết quả "
        "đọc có độ tái lập cao."))

    # ---------------------------------------------------------------- suppliers
    b.append(h2("Các hãng chế tạo căn lỗ", "Companies that make bore gages"))
    b.append(table(
        ["Hãng", "Sản phẩm"],
        [["Brown &amp; Sharpe Manufacturing Company<br>Precision Park, 200 Frenchtown Road, North Kingstown, "
          "RI 02852-1700",
          "Mọi loại căn lỗ, từ thước cặp đến máy đo toạ độ"],
         ["MITUTOYO/MTI Corporation<br>965 Corporate Blvd., Aurora, IL 60504",
          "Hãng chế tạo dụng cụ đo chính xác lớn nhất thế giới; mọi loại căn lỗ"],
         ["Dearborn Gage Company<br>32300 Ford Road, Garden City, MI 48135",
          "Trục khí, hệ kiểm, dụng cụ đo chính xác mô đun điện tử và khí–điện tử"],
         ["The Dyer Company<br>1500 McGovernville Road, Box 4966, Lancaster, PA 17604",
          "Căn lỗ cơ khí và điện tử dùng tại xưởng"],
         ["The L.S. Starrett Co.<br>121 Crescent Street, Athol, MA 01331-1915",
          "Căn lỗ cơ khí và điện tử, máy đo toạ độ, thiết bị so sánh quang học"],
         ["Flexbar Machine Corporation<br>250 Gibbs Road, Islandia, NY 11722-2697",
          "Mọi loại căn lỗ, kể cả căn lỗ sâu và thiết bị so sánh"],
         ["Federal Products Co.<br>1144 Eddy Street, P.O. Box 9400, Providence, RI 02940",
          "Mọi loại căn lỗ: căn chỉ thị, căn khí, thiết bị đo điện tử, chuẩn kích thước, đo hình học, căn phòng "
          "thí nghiệm"],
         ["Comtorgage Corporation<br>58 N.S. Industrial Drive, Slatersville, RI 02876",
          "Đồng hồ chỉ thị — hệ nút giãn chuyên dùng cho một cỡ; căn lỗ đặt riêng"],
         ["Marposs Corporation<br>Auburn Hills, MI 48326-2954",
          "Kiểm trong và sau gia công cho máy mài và máy tiện, hệ kiểm tự động và máy kiểm chuyên dụng"],
         ["Rank Taylor Hobson Inc.<br>2100 Golf Road, Suite 350, Rolling Meadows, IL 60008",
          "Hệ đo lường cho gia công kim loại chính xác và sản phẩm cơ khí dung sai chặt"],
         ["Sterling Mfg. &amp; Engineering Inc.<br>7539 19th Mile Road, Sterling Heights, MI 48314",
          "Căn kích thước đặt riêng, gồm hệ khí, thủ công, điện tử và máy tính hoá"]],
        "Bảng 6-16 · Các hãng chế tạo căn lỗ (địa chỉ và số điện thoại theo nguyên bản năm 1999)."))

    # ---------------------------------------------------------------- glossary
    b.append(h2("Định nghĩa các thuật ngữ", "Defining terms"))
    b.append('<dl class="glossary">')
    for term, body in [
        ("Kích thước",
         "Giá trị số biểu thị bằng đơn vị đo thích hợp và được ghi trên bản vẽ bằng đường, ký hiệu và ghi chú để "
         "xác định các đặc trưng hình học của một vật thể."),
        ("Dung sai",
         "Toàn bộ lượng biến thiên cho phép của kích thước, hình dạng hay vị trí."),
        ("Lắp",
         "Thuật ngữ chung để chỉ khoảng độ chặt có thể phát sinh khi áp dụng một tổ hợp dung sai và khe hở cho "
         "trước trong thiết kế các chi tiết lắp ghép."),
        ("Hệ giới hạn và lắp ghép ISO",
         "Một hệ giới hạn và lắp ghép được tiêu chuẩn hoá, tức một nhóm dung sai được coi là tương ứng với cùng "
         "một mức chính xác cho mọi kích thước cơ bản."),
        ("Căn",
         "Thiết bị dùng để khảo sát mức phù hợp về kích thước của một chi tiết đối với chức năng xác định."),
        ("Kiểm bằng căn",
         "Quá trình đo vật liệu đã chế tạo nhằm bảo đảm độ đồng đều về kích thước và đường bao mà các ngành công "
         "nghiệp yêu cầu."),
    ]:
        b.append("<dt>%s</dt><dd>%s</dd>" % (term, body))
    b.append("</dl>")

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "J. W. Greve (ed.), <i>Handbook of Industrial Metrology</i>, ASTM Publications Committee, Englewood Cliffs, "
        "NJ: Prentice-Hall, 1967.",
        "M. F. Spotts, <i>Dimensioning and Tolerancing for Quantity Production</i>, Englewood Cliffs, NJ: "
        "Prentice-Hall, 1983.",
        "E. R. Friesth, <i>Metrication for Manufacturing</i>, New York: Industrial Press Inc., 1978.",
        "J. G. Nee, <i>Fundamentals of Tool Design</i>, 4th ed., Dearborn, MI: Society of Manufacturing Engineers, "
        "1998.",
    ]))
    b.append(h2("Đọc thêm", "Further information"))
    b.append(ul([
        "F. T. Farago, <i>Handbook of Dimensional Measurement</i>, 3rd ed., New York: Industrial Press Inc., 1994 — "
        "trình bày rất đầy đủ các định nghĩa thuật ngữ, phương pháp và cách bố trí phép đo.",
        "J. Dally, <i>Instrumentation for Engineering Measurements</i>, 2nd ed., New York: Wiley, 1993 — mô tả chi "
        "tiết đặc tính của các dụng cụ và máy đo.",
        "R. S. Sirohi, <i>Mechanical Measurements</i>, 3rd ed., New York: Wiley, 1991 — giáo trình lý thuyết về đo "
        "lường cơ khí.",
        "J. D. Meadows, <i>Geometric Dimensioning and Tolerancing: Applications and Techniques for Use in Design, "
        "Manufacturing, and Inspection</i>, New York: M. Dekker, 1995 — các quy tắc và thủ tục cơ bản của thực hành "
        "ghi dung sai tốt, tạo nền tảng giúp giải quyết các bài toán dung sai nảy sinh trong công việc hằng ngày.",
    ]))
    b.append(nav(6, "vi"))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "The section that follows is the odd one out in this chapter. Every other section measures a displacement "
        "with some physical effect; this one measures a hole, and the displacement is the small motion of a "
        "spring-loaded contact as it follows the wall. The engineering problem is not the transducer — it is the "
        "tolerance budget that decides how precisely the hole has to be made in the first place, and how much of "
        "that budget the gage itself is allowed to consume."))
    b.append(p(
        "Viktor Astakhov opens with the tolerance argument, and it is worth keeping in view: a gage is only ever as "
        "good as the tolerance it has to police. The 10% rule — gage tolerance no larger than a tenth of the "
        "workpiece tolerance — is the whole design brief in one line."))

    b.append(h2("The tolerance chain", "Chuỗi dung sai"))
    b.append(p(
        "ISO R 286 grades tolerances from IT 01 to IT 16, with the value in each grade rising with size according "
        "to a formula tied to the geometric mean diameter of the size band. Eighteen grades, 27 fundamental "
        "deviations below 500 mm and 14 above it, and every fit from loose clearance to heavy interference is "
        "built from those two choices. Nothing about the measurement is decided until those are fixed."))
    b.append(p(
        "The nine classes of bore gage then sort themselves by when in the production cycle they act: master gages "
        "for reference, inspection gages for the inspector, manufacturer’s gages during production, post-process "
        "gages after the part is finished, and in-process gages inside the machining cycle. Post-process gaging "
        "with feedback is the interesting one — inspection data flows back into the part program of a CNC machine "
        "or the template of a tracer, and repeatable path errors are compensated rather than merely detected."))

    b.append(h2("Fixed limit versus variable indicating", "Giới hạn cố định và chỉ thị biến thiên"))
    b.append(fig(53, F.fig_6_53(), "en"))
    b.append(p(
        "A plug gage answers one question: is the bore between the limits? The go end must enter, the no-go end "
        "must not. Figure 6.53 shows the three AGD arrangements — two separate members, two members on one handle, "
        "and the progressive gage where the go portion leads the no-go portion on a single body. None of them "
        "produces a number."))
    b.append(p(
        "Table 6.11 is the reason they can be trusted. Four gagemaker’s tolerance classes, XX through Z, cap the "
        "permissible error of the gage itself; class XX is roughly 0.5 µm on a 20 mm bore, class Z about five times "
        "that. Which class you buy is decided by how much of the part tolerance you are willing to spend on the "
        "gage."))
    b.append(fig(54, F.fig_6_54(), "en"))
    b.append(p(
        "A dial bore gage gives a number, and the number is a deviation from a master ring rather than an absolute "
        "diameter. That is the point of zeroing on the ring: the instrument never has to be accurate in absolute "
        "terms, only repeatable and linear over the narrow band around nominal. It is a comparative instrument "
        "wearing an absolute instrument’s clothes."))
    b.append(fig(56, F.fig_6_56(), "en"))
    b.append(p(
        "The three-point internal micrometer in Figure 6.56 solves a different problem. Two contacts can only "
        "define a chord; three contacts at 120° define a circle, so the instrument centres itself in the bore and "
        "stays aligned with the axis however deep the hole runs. That is why the same head works at the bottom of a "
        "blind hole, where a two-point gage would rock."))

    b.append(h2("Where the air gage wins", "Đầu đo khí mạnh ở đâu"))
    b.append(fig(57, F.fig_6_57(), "en"))
    b.append(p(
        "The air plug gage measures nothing directly. It measures the back pressure of a circuit whose restriction "
        "is the clearance between two jets and the bore wall. The non-linearity in Figure 6.57 is not a defect to "
        "be corrected — it is why the instrument is so sensitive: near zero clearance, a micrometre of extra "
        "diameter changes the pressure by far more than the same micrometre would change a dial reading. The price "
        "is a short working range and a hard dependence on supply pressure."))
    b.append(fig(58, F.fig_6_58(), "en"))
    b.append(p(
        "Five form errors follow directly from having more than one jet: taper, bell mouthing, barrelling, "
        "ovality and lobing. A single-jet plug sees only the diameter at its own plane and is blind to all five. "
        "Two jets at different axial positions separate taper from barrelling; two jets in the same plane separate "
        "ovality from lobing only if you rotate the plug, which is why three-point electronic heads exist."))

    b.append(h2("Form, and the limits of a number", "Hình dạng, và giới hạn của một con số"))
    b.append(fig(59, F.fig_6_59(), "en"))
    b.append(p(
        "A roundness machine abandons the diameter entirely. The part turns, the head stays still, and what is "
        "recorded is the radial deviation from a least-squares reference circle, magnified by a factor chosen to "
        "make the trace legible. The polar plot in Figure 6.59 is the result: a three-lobed shape that no single "
        "diameter measurement could have revealed, because every diameter across it is very nearly the same."))
    b.append(fig(60, F.fig_6_60(), "en"))
    b.append(p(
        "The fully automatic machines add the one thing manual staging cannot guarantee — that the part axis and "
        "the table axis coincide. The RA-600 centres and levels itself from a preliminary scan, then measures "
        "roundness, cylindricity, squareness and total runout without an operator touching a knob. The measurement "
        "is only as good as that alignment, which is why the machine spends its first seconds doing nothing but "
        "alignment."))

    b.append(h2("GAGE R and R", "GAGE R and R"))
    b.append(p(
        "Repeatability is one operator, one gage, many trials. Reproducibility is many operators, one gage. The "
        "two together decide whether a measuring system is fit for a particular tolerance — and the answer is "
        "tolerance-dependent. A gage that passes at 50 mm may fail at 250 mm, because the same absolute error is a "
        "larger fraction of a tighter budget at the bigger size. Dyer’s published figures for its 830 and 230 "
        "series — linearity ±1 µm, repeatability better than ±0.25 µm — are worth remembering as the order of "
        "magnitude a good mechanical bore gage reaches before any electronics are involved."))
    b.append(p(
        "The three sources of variation are worth separating because only one of them is the gage’s fault. The "
        "gage contributes linearity, repeatability, stability and calibration. The operator contributes "
        "repeatability and reproducibility. The production line contributes surface finish, setup error and "
        "temperature. Buying a better gage fixes the first group and does nothing for the other two."))
    b.append(nav(6, "en"))
    return "".join(b)
