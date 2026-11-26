# -*- coding: utf-8 -*-
"""Book 9, Chapter 9 (part A) — ABSTRACT, KEYWORDS and INTRODUCTION (EN/VI).

Source: Emilija Kisić, Željko Đurović and Vera Petrović, in L. N. Jalali (ed.),
*Handbook on Power Plant Instrumentation and Control* (Bibliotex, 2019), PDF
pp. 215-217, printed pp. 199-201 (absolute lines 5485-5564 of work/ppic_raw.txt).
The printed title, chapter number, authors and affiliations are rendered by the
page shell in `ppic_ch09.py` (TITLE_EN/TITLE_VI and BYLINE); this module therefore
starts with the ABSTRACT heading, as the other chapter parts do. Printed
bracketed citations [1] and [2] are retained inline; no reference list is emitted
here. There are no figures, tables or equations in this module.
"""
try:
    import ppicfig9 as F  # noqa: F401  (shared supplier import style)
except ImportError:                       # supplier not written yet
    class _SupplierNamespace(object):
        pass
    F = _SupplierNamespace()

from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS, LEAD  # noqa: F401


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 9."""
    b = []

    # ---------------------------------------------------------------- ABSTRACT
    H(b, lang, "TÓM TẮT", "ABSTRACT", level=2)
    P(b, lang,
      "Trong chương này, một kỹ thuật bảo trì dự báo đổi mới được mô tả nhằm "
      "làm nổi bật những lợi ích của bảo trì dự báo so với bảo trì theo thời "
      "gian. Kỹ thuật đề xuất được áp dụng cho một bài toán cụ thể phát sinh "
      "khi bảo trì theo thời gian được áp dụng cho các bàn nghiền của máy "
      "nghiền than, trong hệ thống nghiền than tại nhà máy nhiệt điện "
      "'TEKO', Kostolac, Serbia. Bảo trì theo thời gian quy định thay thế các "
      "bàn nghiền sau một số giờ làm việc nhất định, nhưng tùy thuộc vào chất "
      "lượng than và bản thân bàn nghiền, việc thay thế này đôi khi cần được "
      "thực hiện sớm hơn hoặc muộn hơn thời điểm đã định. Hậu quả của cách "
      "bảo trì này là những tổn thất vật chất lớn phát sinh do phải tắt "
      "thường xuyên toàn bộ hệ thống nghiền than, cũng như khả năng hỏng hóc "
      "xảy ra trước khi thay thế. Kỹ thuật bảo trì dự báo đổi mới được mô tả "
      "trong chương này được dùng để giải quyết bài toán đó.",
      "In this chapter, innovative predictive maintenance technique is "
      "described with the aim of highlighting the benefits of predictive "
      "maintenance compared to time-based maintenance. The proposed technique "
      "is applied to a specific problem that occurs when time-based "
      "maintenance is applied on grinding tables of the coal mill, in "
      "coal-grinding subsystem at the thermoelectric power plant 'TEKO', "
      "Kostolac, Serbia. Time-based maintenance provides replacement of "
      "grinding tables after certain number of working hours, but depending "
      "on the quality of the coal and grinding table itself, this replacement "
      "sometimes needs to be made before or after planned replacement. The "
      "consequences of such maintenance are great material losses incurred "
      "because of frequent shutdowns of the entire coal-grinding subsystem, "
      "as well as the possibility that the failure occurs before replacement. "
      "Innovative predictive maintenance technique described in the chapter "
      "is used for solution of this problem.")

    # ---------------------------------------------------------------- KEYWORDS
    P(b, lang,
      "<b>Từ khóa:</b> bảo trì dự báo, biểu đồ kiểm soát T², mô hình Markov ẩn, "
      "nhà máy nhiệt điện, kiểm soát quá trình thống kê",
      "<b>Keywords:</b> predictive maintenance, T² control chart, hidden Markov "
      "model, thermoelectric power plant, statistical process control")

    # ------------------------------------------------------------ INTRODUCTION
    H(b, lang, "GIỚI THIỆU", "INTRODUCTION", level=2)
    P(b, lang,
      "Trong công nghiệp hiện nay, việc áp dụng các chiến lược bảo trì tốt "
      "nhất là một nhiệm vụ rất quan trọng để bảo đảm tính ổn định và độ tin "
      "cậy của các hệ thống kỹ thuật. Có thể tìm thấy trong tài liệu nhiều bài "
      "báo và sách về các chiến lược bảo trì khác nhau, và gần như ở đâu người "
      "ta cũng nhấn mạnh ưu điểm của bảo trì dự báo so với bảo trì theo thời "
      "gian [1]. Bảo trì dự báo kéo dài thời gian hệ thống hoạt động tốt, giảm "
      "các lần tắt máy không cần thiết, giảm tổn thất vật chất và ngăn ngừa "
      "các sự cố thảm khốc. Mặc dù lĩnh vực nghiên cứu này đã phát triển rất "
      "mạnh cùng với sự phát triển của các công nghệ tinh vi, vẫn còn nhiều "
      "dư địa để cải tiến các kỹ thuật hiện có và phát triển những kỹ thuật "
      "mới.",
      "In today's industry, application of the best maintenance strategies is "
      "a very important task in ensuring stability and reliability of "
      "technical systems. Numerous papers and books about different "
      "maintenance strategies can be found in literature, and almost "
      "everywhere the merits of predictive maintenance in regard to "
      "time-based maintenance are emphasized [1]. Predictive maintenance "
      "extends the period of time during which the system functions well, "
      "decreases unnecessary shutdowns, reduces material losses and prevents "
      "catastrophic failures. Although this field of research is very much "
      "advanced with the development of highly sophisticated technologies, "
      "there is still a lot of room for improvement of the existing "
      "techniques and the development of new ones.")

    P(b, lang,
      "Trong nghiên cứu này, một kỹ thuật bảo trì dự báo đổi mới được đề xuất "
      "và áp dụng cho một bài toán cụ thể phát sinh tại nhà máy nhiệt điện "
      "'TEKO', Kostolac, Serbia. Cụ thể, một trong những thành phần then chốt "
      "của nhà máy nhiệt điện là hệ thống nghiền than. Khi áp dụng bảo trì theo "
      "thời gian cho các bàn nghiền của máy nghiền than, các bàn nghiền được "
      "thay thế sau một số giờ làm việc nhất định. Tùy thuộc vào chất lượng "
      "than và bản thân bàn nghiền, việc thay thế này đôi khi cần được thực "
      "hiện trước hoặc sau thời điểm thay thế đã định. Cách duy nhất để xác "
      "định tình trạng của bàn nghiền là kiểm tra bằng mắt, việc này đòi hỏi "
      "phải tắt toàn bộ hệ thống. Hậu quả của việc thay thế bàn nghiền sau các "
      "khoảng thời gian cố định là những tổn thất vật chất lớn do phải tắt "
      "thường xuyên toàn bộ hệ thống nghiền than. Ngoài ra, vẫn có khả năng sự "
      "cố xảy ra trước khi thay thế.",
      "In this research, an innovative technique of predictive maintenance is "
      "proposed and applied to a specific problem that occurs at the "
      "thermoelectric power plant 'TEKO', Kostolac, Serbia. Namely, one of the "
      "key thermoelectric power plant components is the coal-grinding "
      "subsystem. When time-based maintenance is applied on grinding tables "
      "of the coal mill, grinding tables are replaced after certain number of "
      "working hours. Depending on the quality of the coal and grinding table "
      "itself, this replacement sometimes needs to be made before or after "
      "planned replacement. The only way to determine the condition of the "
      "grinding table is visual inspection, which implies the shutting down "
      "of the whole subsystem. Consequences of grinding table replacement "
      "after fixed time intervals are great material losses incurred because "
      "of frequent shutdowns of the entire coal-grinding subsystem. Also, "
      "there is a possibility that the failure will occur before replacement.")

    P(b, lang,
      "Có một 'truyền thuyết đô thị' cho rằng các công nhân vận hành giàu kinh "
      "nghiệm trong các nhà máy công nghiệp, chẳng hạn như nhà máy nhiệt điện, "
      "có thể 'nghe' được âm thanh từ nội dung tiếng động của các cơ cấu vận "
      "hành. Dựa trên những âm thanh này, họ có thể nhận biết sự hao mòn của "
      "các bộ phận cụ thể có thể bị mòn, chẳng hạn như bàn nghiền của máy "
      "nghiền. Ngoài ra, trong tài liệu người ta cũng đề cập rằng 99% sự cố "
      "cơ khí có các dấu hiệu rất dễ nhận biết đi trước [2]. Từ những thực tế "
      "này, ý tưởng ghi lại các tín hiệu âm thanh trong khi hệ thống nghiền "
      "than đang vận hành đã ra đời. Bằng cách này, có thể dễ dàng thu thập dữ "
      "liệu giám sát tình trạng phục vụ bảo trì dự báo, và không cần phải tắt "
      "toàn bộ hệ thống để lấy thông tin về tình trạng ổn định của bàn nghiền.",
      "There is an 'urban legend' that experienced operators in industrial "
      "plants, such as thermoelectric power plants, can 'hear' the sounds in "
      "sound content from operational drives. Based on these sounds, they can "
      "recognize the detritions of specific elements that can wear out, such "
      "as mill-grinding tables. Also, in literature one can find that 99% of "
      "mechanical failures are foregone by some very noticeable indicators "
      "[2]. Because of these facts, the idea came up for the recording of "
      "acoustic signals while coal-grinding subsystem is operational. In this "
      "way, it is easy to obtain condition-monitoring data which can be "
      "applied for predictive maintenance, and there is no need for shutting "
      "down the whole subsystem for obtaining the information about grinding "
      "stable condition.")

    P(b, lang,
      "Phương pháp đề xuất là một sự thỏa hiệp giữa các giải pháp đã được đưa "
      "ra trong tài liệu, và tính mới của thuật toán đề xuất dựa trên việc "
      "lựa chọn kỹ thuật dự báo hỏng hóc. Mục tiêu chính của thuật toán đề "
      "xuất là tăng hiệu năng sử dụng năng lượng tại nhà máy nhiệt điện.",
      "The proposed method is a trade-off between solutions already offered "
      "in the literature, and originality of the proposed algorithm is based "
      "on the selection of failure prognostic technique. The main goal of the "
      "proposed algorithm is the increase of energy efficiency at the "
      "thermoelectric power plant.")

    P(b, lang,
      "Chương này được tổ chức như sau: Ở phần tiếp theo, chúng tôi mô tả chi "
      "tiết khái niệm bảo trì dự báo. Phần 3 trình bày mô tả về hệ thống "
      "nghiền than trong nhà máy nhiệt điện. Phần 4 giới thiệu một kỹ thuật "
      "bảo trì dự báo mới. Phần 5 chứa các kết quả. Phần cuối là phần kết "
      "luận, với thảo luận về các kết quả đạt được.",
      "This chapter is organized as follows: In the next section, we describe "
      "the concept of predictive maintenance in detail. In Section 3, a "
      "description of the coal-grinding subsystem in thermoelectric power "
      "plant will be given. In Section 4, we present a new predictive "
      "maintenance technique. Section 5 contains the results. The last "
      "section is the conclusion, with the discussion about gain results.")

    return b
