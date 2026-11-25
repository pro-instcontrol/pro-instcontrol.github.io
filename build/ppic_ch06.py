# -*- coding: utf-8 -*-
"""Book 9, Chapter 6 - Developments of Power System Protection and Control
(EN/VI bilingual).

Source: Z. Q. Bo, X. N. Lin, Q. P. Wang, Y. H. Yi and F. Q. Zhou, in
L. N. Jalali (ed.), *Handbook on Power Plant Instrumentation and Control*
(Bibliotex, 2019), PDF pp. 123-140, printed pp. 107-124. PAGES_SRC = 18
counts the whole source span, including the blank final PDF page.

The chapter has three figures (Figure 6.1 - Figure 6.3), no tables and no
numbered equations, and 17 references. Figures are redrawn as vectors in
`ppicfig6`; all prose is assembled here in source order.
"""
import ppic_common as C          # noqa: F401  (page shell, used by C.build)
import bolton_common as _B       # noqa: F401  (figure-caption language state)
from ppic_common import h2, h3, note, p, fig, refs

# The figure supplier is written in parallel. Use it when available; otherwise
# fall back to a tiny namespace and install non-overwriting 5-tuple stubs below.
try:
    import ppicfig6 as F
except ImportError:                       # supplier not written yet
    class _SupplierNamespace(object):
        pass
    F = _SupplierNamespace()


def _stub_tuple(n):
    """A simple, valid 5-tuple used only while the supplier is unavailable."""
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 60" '
        'role="img"><rect x="1" y="1" width="678" height="58" '
        'fill="#f4f6fa" stroke="#9aa7bd"/>'
        '<text x="340" y="35" text-anchor="middle" '
        'style="font:14px Helvetica,sans-serif;fill:#24364f">'
        'Figure 6.%d</text></svg>' % n
    )
    return (svg,
            "Hình 6.%d · Hình minh họa." % n,
            "Figure 6.%d · Illustration." % n,
            "Hình 6.%d" % n,
            "Figure 6.%d" % n)


# Never replace a real supplier callable: these stubs only fill missing names.
if not hasattr(F, "fig_f61"):
    F.fig_f61 = lambda: _stub_tuple(1)
if not hasattr(F, "fig_f62"):
    F.fig_f62 = lambda: _stub_tuple(2)
if not hasattr(F, "fig_f63"):
    F.fig_f63 = lambda: _stub_tuple(3)


PAGES_SRC = 18
BYLINE = ("Z. Q. Bo · X. N. Lin · Q. P. Wang · Y. H. Yi · F. Q. Zhou · "
          "XUJI Group Corporation, Xuchang, China · "
          "Huazhong University of Science and Technology, Wuhan, China")
TITLE_EN = "Developments of Power System Protection and Control"
TITLE_VI = "Phát triển bảo vệ và điều khiển hệ thống điện"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> bảo vệ hệ thống điện · bảo vệ diện rộng · bảo vệ "
                "và điều khiển tích hợp · nền tảng thông tin · truyền thông đồng bộ tốc độ "
                "cao · hệ thống phân cấp ba cấp · cấp địa phương · cấp trạm biến áp/nhà máy · "
                "cấp diện rộng/khu vực · ba tuyến phòng thủ · rơ-le quá dòng điện cơ · rơ-le "
                "vi sai · rơ-le hướng · rơ-le khoảng cách · bảo vệ thích ứng · trí tuệ nhân "
                "tạo · mạng nơ-ron nhân tạo · bảo vệ dựa trên sóng truyền · đồng bộ GPS · "
                "PMU · RTU · phasor đồng bộ · phối hợp diện rộng · mất ổn định dây chuyền · "
                "thiết bị thông minh đa chức năng · MU · nền tảng thông tin thời gian thực · "
                "điện toán đám mây phân tán · tự phục hồi · IEEE-1588 · PTN · SDH · UFLS · "
                "UVLS · digital computer protection.")
    return ("<b>Key terms.</b> power system protection · wide area protection · integrated "
            "protection and control · information platform · synchronised high-speed "
            "communication · three-level hierarchy · local level · substation/plant level · "
            "wide area/regional level · three lines of defence · electromechanical overcurrent "
            "relay · differential relay · directional relay · distance relay · adaptive "
            "protection · artificial intelligence · artificial neural network · travelling-wave "
            "protection · GPS synchronization · PMU · RTU · synchronized phasor · wide-area "
            "coordination · cascading outages · multiple-function intelligent equipment · MU · "
            "real-time information platform · distributed power cloud · self-healing · "
            "IEEE-1588 · PTN · SDH · UFLS · UVLS · digital computer protection.")


def source_notes(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Lớp văn bản của PDF giữ lại gần như toàn bộ "
                "phần prose và chú thích ba hình, nhưng ba hình trong bản in là ảnh raster; "
                "bản dịch vẽ lại từng hình dạng vector rút gọn với nhãn, mũi tên và chú thích "
                "tương ứng. Trang PDF cuối cùng để trống sau danh mục tài liệu tham khảo, "
                "nhưng vẫn được tính vào PAGES_SRC = 18. Mười bảy tài liệu tham khảo được chép "
                "theo đúng thứ tự in, giữ nguyên tên tác giả, năm, tạp chí và kỳ hiệu; các dấu "
                "và trong danh sách tác giả và tên tạp chí được mã hóa để hiển thị đúng như bản "
                "in. Một số khác biệt nhỏ về dấu câu của nguyên bản (ví dụ mục 8 và mục 15) "
                "được giữ lại. Nguyên bản không có bảng nào và không có phương trình đánh số, "
                "nên bản dịch không thêm vào.")
    return ("<b>Source quirks.</b> The PDF text layer preserves nearly all of the prose and "
            "the captions of the three figures, but the figures themselves are raster images "
            "in the printed book; each is redrawn here as a simplified vector with matching "
            "labels, arrows and captions. The final PDF page is blank after the reference "
            "list, yet it is still counted in PAGES_SRC = 18. All 17 references are transcribed "
            "in printed order with their author initials, years, venues and volume/issue data "
            "unchanged; ampersands in author lists and journal names are encoded so that they "
            "render exactly as printed. A few minor punctuation quirks of the source (for "
            "example in entries 8 and 15) are retained. The source contains no tables and no "
            "numbered equations, so none are added here.")


_REFS = [
    "Rockefeller, G. D. (1969). Fault protection with digital computer. IEEE Transactions "
    "on Power Apparatus and Systems, 88(4), 438–461.",
    "Bo, Z.Q., Jiang, F., Chen, Z., et al. (2000). Transient based protection for power "
    "transmission systems. In: IEEE PES Winter Meeting. Singapore.",
    "Bo, Z.Q., Jayasinge, J.A.S.B., Aggarwal, R.K., et al. (1996). A new scheme for monitoring "
    "and protection of power transmission system based on global positioning system. In: "
    "Technol. Educ. Inst. Iraklio The 31st University Power Engineering Conference "
    "(pp. 21–24). Crete.",
    "Bo, Z. Q., Weller, G., &amp; Lomas, T. (2000). Positional protection of transmission "
    "system using global positioning system. IEEE Transactions on Power Delivery, 15(4), "
    "1163–1168.",
    "Ingelsson, B., Lindstrom, P. O., Karlsson, D., et al. (1997). Wide-area protection "
    "against voltage collapse. IEEE Computer Applications in Power, 10(4), 30–35.",
    "Bo, Z. Q., He, J. H., &amp; Dong, X. Z. (2005). Integrated protection of power network. "
    "Relay, 33(14), 33–41.",
    "Gao, H. L., Liu, Y. Q., Su, J. J., et al. (2012). New type of substation-area backup "
    "protection for intelligent substation. In 2012 China Smart Grid Seminar.",
    "Bo, Z.Q., Wang, L., Zhou, F.Q., et al. (2014). Substation cloud computing for secondary "
    "auxiliary equipment.In: IEEE Powercon2014. Chengdu.",
    "Bo, Z. Q., Zhang, B. H., Dong, X. Z., He, J. H., et al. (2013). The development of "
    "protection intellectuation and smart relay network. Power System Protection and Control, "
    "41(2), 1–12.",
    "Guo, Y., Wu, W. C., Zhang, B. M., et al. (2015). A distributed state estimation method "
    "for power systems incorporated with linear and nonlinear models. International Journal "
    "of Electrical Power &amp; Energy Systems, 64, 608–616.",
    "Chen, R.Z., Wu, W.C., Sun, H.B., Zhang, &amp; B.M. (2013). A two-level online parameter "
    "identification approach. In: IEEE Power &amp; Energy Society General Meeting. Vancouver.",
    "Liu, M.C., Zhang, B.M., Yao, L.Z., et al. (2008). PMU based voltage stability analysis "
    "for the transmission corridor. In: IEEE The 3rd Int. Conf. on Electric Utility "
    "Deregulation and Restructing and Power Technologies. Nanjing.",
    "He, J. B., Lu, C., Wu, X. C., et al. (2007). Design and experiment of heuristic adaptive "
    "HVDC supplementary damping controller based on online Prony analysis. In Proc. IEEE Power "
    "Engineering Society General Meeting.",
    "Wu, W.C., Zhang, B.M., Sun, H.B., et al. (2010). Development and application of on-line "
    "dynamic security early warning and preventive control system in China. In: IEEE Power "
    "&amp; Energy Society General Meeting. Mineapolis.",
    "Wang, B., Dong, X. Z., Xu, F., Cao, R. B., Liu, K., &amp; Bo, Z. Q. (2011). Analysis of "
    "data sharing for protection and control system in smart distribution substation”. In "
    "Proceedings of the CSEE (Vol. 31).",
    "Bo, Z.Q., Ge, S.M., Wang, Q.P., Wang, L., Zhou, F.Q., Liu, X., &amp; Fan, Z.F. (2015). "
    "Integrated wide area protection and control systems based on advanced communication "
    "network. In: ATLANTIS PRESS 2015 International Conference on Mechanical Engineering, "
    "Materials and Energy. Tianjin.",
    "Bo, Z.Q., Wang, Q.P., Wang, L., Zhou, F.Q., Ge, S.M., &amp; Zhang, B.M. \"Architecture "
    "design for integrated wide area protection and control systems\", APPEEC, April 14 2015, "
    "The 7 th Asia-Pacific Power and Energy Engineering Conference (APPEEC 2015).",
]


def _body(lang):
    vi = lang == "vi"
    # Keep figure captions in step with the page even when the body functions
    # are called directly (C.build already sets this, so it is a no-op there).
    _B._CUR_LANG[0] = lang
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H2(v, e):
        b.append(h2(v if vi else e))

    def H3(v, e):
        b.append(h3(v if vi else e))

    def FIG(n, fn):
        b.append(fig(n, fn))

    # ------------------------------------------------------------------ lead
    b.append(C.lead(
        "Chương này xem lại lịch sử phát triển của bảo vệ hệ thống điện, nhấn mạnh các tiến "
        "bộ gần đây về bảo vệ diện rộng và bảo vệ tích hợp, rồi giới thiệu khái niệm bảo vệ "
        "và điều khiển diện rộng tích hợp (IWAPC) với cấu trúc phân cấp ba cấp và nền tảng "
        "thông tin thời gian thực làm chỗ dựa chung."
        if vi else
        "This chapter reviews the development history of power system protection, pays special "
        "attention to recent advances in wide-area and integrated protection, and then "
        "introduces the concept of integrated wide area protection and control (IWAPC), with "
        "a three-level hierarchy and a real-time information platform as its common basis."))

    # -------------------------------------------------------------- ABSTRACT
    H2("TÓM TẮT", "ABSTRACT")
    P(
        "Truyền thông diện rộng đồng bộ đã trở thành một công nghệ chín muồi, làm cho sự tương "
        "tác thời gian thực giữa các trạm biến áp và hệ thống bảo vệ, điều khiển diện rộng trở "
        "thành hiện thực. Tuy nhiên, người ta nhận ra rằng hệ thống bảo vệ và điều khiển hiện "
        "nay còn thiếu sót trong việc xử lý dữ liệu thời gian thực này. Bài viết bắt đầu bằng "
        "việc xem lại lịch sử phát triển của bảo vệ hệ thống điện, đặc biệt chú ý đến những "
        "phát triển gần đây trong lĩnh vực bảo vệ diện rộng và bảo vệ tích hợp, nhằm nhìn vào "
        "tương lai của hệ thống bảo vệ và điều khiển. Tiếp theo, khái niệm bảo vệ và điều khiển "
        "diện rộng tích hợp được giới thiệu: một hệ thống phân cấp cung cấp bảo vệ và điều "
        "khiển cho các trạm biến áp hoặc nhà máy điện diện rộng/khu vực và các mạng lưới điện "
        "liên quan. Hệ thống được chia chủ yếu thành ba cấp: cấp địa phương, cấp trạm biến "
        "áp/nhà máy và cấp diện rộng/khu vực. Chức năng tích hợp ở mỗi cấp được mô tả chi tiết "
        "nhằm xây dựng cơ chế phối hợp tối ưu giữa các cấp. Yếu tố then chốt của hệ thống đề "
        "xuất là nền tảng thông tin bảo vệ và điều khiển diện rộng thời gian thực; nền tảng "
        "này không chỉ cho phép hợp nhất ba tuyến phòng thủ của bảo vệ và điều khiển hệ thống "
        "điện, mà còn cung cấp một công cụ tốt cho việc áp dụng điện toán đám mây trong các "
        "trạm biến áp và mạng lưới điện.",
        "Synchronized wide area communication has become a mature technology, which makes the "
        "real-time interaction between the substations and the wide area protection and "
        "control system possible. However, the present protection and control system for "
        "handling this real-time data has been recognised to be deficient. This chapter begins "
        "by reviewing the development history of power system protection, with special "
        "attention paid to recent developments in the field of wide-area and integrated "
        "protection, in order to look into the future of protection and control systems. The "
        "concept of integrated wide area protection and control is then introduced, where a "
        "hierarchical protection and control system provides protection and control for wide "
        "area or regional substations and plants and their associated power networks. The "
        "system is mainly divided into three levels: the local, the substation/plant and the "
        "wide area/regional levels. The integrated functions at each level are described in "
        "detail with the aim of developing an optimal coordination mechanism between the "
        "levels. The key element in the proposed system is the wide area real-time protection "
        "and control information platform, which not only enables the merger of the three "
        "lines of defence for power system protection and control, but also provides an "
        "excellent tool for the application of cloud computing in substations and power "
        "networks.")

    # ------------------------------------------------------------- KEYWORDS
    H2("TỪ KHÓA", "KEYWORDS")
    P(
        "<b>Từ khóa.</b> Bảo vệ hệ thống điện · Bảo vệ diện rộng · Bảo vệ và điều khiển tích "
        "hợp · Nền tảng thông tin",
        "<b>Keywords.</b> Power system protection · Wide area protection · Integrated "
        "protection and control · Information platform")

    # --------------------------------------------------------- INTRODUCTION
    H2("GIỚI THIỆU", "INTRODUCTION")
    P(
        "Bảo vệ hệ thống điện ra đời vào đầu thế kỷ trước cùng với việc áp dụng rơ-le quá dòng "
        "điện cơ đầu tiên. Hầu hết các nguyên lý bảo vệ hiện vẫn được dùng — quá dòng, hướng, "
        "khoảng cách và vi sai — đã được phát triển trong ba thập kỷ đầu của thế kỷ trước, như "
        "thể hiện trong Hình 1. Sự phát triển của khoa học và công nghệ hiện đại, đặc biệt là "
        "điện tử và máy tính, đã thúc đẩy kỹ thuật rơ-le cả về vật liệu, linh kiện và quy trình "
        "chế tạo cấu trúc phần cứng, đồng thời mang lại tiến bộ lớn về phần mềm và thuật toán "
        "bảo vệ. Từ khi bảo vệ ra đời đến cuối những năm 1990, rơ-le bảo vệ đã đi qua nhiều giai "
        "đoạn, từ cơ khí-điện sang bán dẫn, rồi đến mạch tích hợp và vi xử lý. Ngày nay rơ-le "
        "số và rơ-le kỹ thuật số dựa trên vi xử lý đang thay thế rơ-le truyền thống trong mọi "
        "lĩnh vực của bảo vệ hệ thống điện, dù nhiều nguyên lý bảo vệ cũ vẫn giữ vai trò chủ "
        "đạo.",
        "Power system protection emerged at the beginning of the last century with the "
        "application of the first electromechanical overcurrent relay. The majority of the "
        "protection principles still in use today - overcurrent, directional, distance and "
        "differential protection - were developed within the first three decades of that "
        "century, as shown in Figure 1. Advances in modern science and technology, especially "
        "electronics and computing, promoted relay technology in materials, components and "
        "the manufacturing of hardware structures, while substantial theoretical progress was "
        "made in protection software and algorithms. From the emergence of protection to the "
        "end of the 1990s, relay protection passed through several stages, migrating from "
        "electromechanical to semiconductor, integrated circuit and microprocessor "
        "technologies. Today, microprocessor-based digital and numeric relays are replacing "
        "conventional relays in all areas of power system protection, although many of the "
        "original relaying principles still play a dominant role.")
    P(
        "Cuối những năm 1960, người ta đã đề xuất hệ thống bảo vệ trạm biến áp tập trung dựa "
        "trên máy tính tập trung [1]. Đây là một cột mốc quan trọng trong lịch sử bảo vệ hệ "
        "thống điện. Ý tưởng này khớp tốt với khái niệm bảo vệ tích hợp toàn diện, trong đó "
        "gói bảo vệ không chỉ giám sát các thiết bị riêng lẻ của một nhà máy mà còn cả một "
        "đoạn của mạng lưới. Tuy nhiên, ý tưởng chỉ được áp dụng rộng rãi về sau, vì khi ấy "
        "chưa có phần cứng, phần mềm máy tính hay công nghệ truyền thông phù hợp để hỗ trợ. Từ "
        "đó, kỹ thuật rơ-le phát triển thành công dựa trên công nghệ số. Việc đưa vi xử lý vào "
        "bảo vệ trong thập niên 1980 nói chung vẫn đi theo cách tiếp cận truyền thống, với các "
        "nền tảng xử lý phân tán tập trung vào bảo vệ từng thiết bị riêng lẻ; bảo vệ tích hợp "
        "khi ấy chỉ ở mức hạn chế dưới dạng bảo vệ dự phòng và vì thế vẫn là chức năng phụ.",
        "In the late 1960s, the application of a centralised substation protection system "
        "based on a centralised computer was proposed [1]. This constitutes an important "
        "milestone in the history of power system protection. The idea fits well with the "
        "concept of overall integrated protection, in which the protection package would "
        "oversee not only individual units of a plant but also a section of the network. "
        "However, the idea was not widely applied until recently, because no suitable "
        "computer hardware, software or communication technologies were available to support "
        "it. Since then, relay technology has developed successfully on the basis of digital "
        "techniques. The introduction of microprocessors into protection in the 1980s "
        "generally followed the conventional approach, with distributed processing platforms "
        "concentrating on protecting individual units of the system; only limited integrated "
        "protection was provided in the form of back-up protection, which therefore remained "
        "a secondary function.")
    FIG(1, F.fig_f61())
    P(
        "Những phát triển trong thập niên 1980 và 1990 đã mang lại cách tiếp cận mới cho bảo vệ "
        "hệ thống điện, đặc biệt là bảo vệ thích ứng và bảo vệ dựa trên trí tuệ nhân tạo (AI). "
        "Bảo vệ thích ứng bắt nguồn từ việc áp dụng bảo vệ quá dòng với thời gian nghịch đúng "
        "tối thiểu (IDMT) từ giai đoạn đầu của lịch sử bảo vệ. Khái niệm này đóng vai trò quan "
        "trọng trong thập niên 1980 nhờ tiến bộ của công nghệ máy tính và lý thuyết điều khiển "
        "liên quan. Nó được định nghĩa là một loại rơ-le bảo vệ có thể thay đổi hiệu năng, đặc "
        "tính hoặc giá trị chỉnh định theo chế độ vận hành và tình trạng sự cố của hệ thống "
        "điện. Ý tưởng cơ bản là bảo vệ hệ thống điện tốt nhất có thể nhằm nâng cao hiệu năng "
        "bảo vệ. Bảo vệ thích ứng có ưu điểm cải thiện khả năng đáp ứng của hệ thống, tăng độ "
        "tin cậy và nâng cao hiệu quả kinh tế, với triển vọng ứng dụng rộng rãi trong bảo vệ "
        "khoảng cách, bảo vệ máy biến áp, bảo vệ máy phát, tự động đóng lại và các ứng dụng "
        "khác. Nghiên cứu cũng chỉ ra rằng để bảo vệ thích ứng với chế độ vận hành và trạng "
        "thái sự cố, cần có thông tin chi tiết hơn về vận hành và sự cố của hệ thống thông qua "
        "mạng truyền thông.",
        "Developments in the 1980s and 1990s provided new means to advance power system "
        "protection, especially adaptive protection and protection based on artificial "
        "intelligence (AI). Adaptive protection started with the application of Inverse "
        "Definite Minimum Time Overcurrent (IDMT) protection early in the history of "
        "protection. The concept played an important role in the 1980s with progress in "
        "computing technology and the associated control theory. It can be defined as a new "
        "type of relay protection that can change its performance, characteristics or set "
        "value according to the operating mode and fault condition of the power system. The "
        "basic idea is to protect the power system as fully as possible so as to improve "
        "protection performance. Adaptive protection has the advantages of improving the "
        "response of the system, enhancing reliability and improving economic benefits, with "
        "wide application prospects in distance protection, transformer protection, generator "
        "protection, autoreclosure and other areas. Research has found that, to achieve "
        "protection adaptive to the operating mode and fault status, more detailed system "
        "operation and fault information is required through a communication network.")
    P(
        "Thập niên 1990 chứng kiến sự phát triển nhanh của điện tử và máy tính, cùng với việc "
        "ứng dụng các kỹ thuật trí tuệ nhân tạo như mạng nơ-ron nhân tạo, thuật toán di truyền, "
        "thuật toán tiến hóa, logic mờ và các hướng nghiên cứu khác vào bảo vệ rơ-le. Ví dụ, "
        "mạng nơ-ron nhân tạo (ANN) được dùng để nhận dạng loại sự cố, đo khoảng cách sự cố và "
        "bảo vệ hướng. Mạng nơ-ron có đặc tính lưu trữ phân tán, xử lý song song, tự tổ chức "
        "và tự học. Việc ứng dụng trí tuệ nhân tạo sẽ nâng cao tốc độ và độ chính xác của việc "
        "phát hiện và phân tích sự cố, đại diện cho tương lai của hệ thống chẩn đoán thông "
        "minh. Tuy đã cải thiện đáng kể hiệu năng của rơ-le, những phát triển này chủ yếu hoàn "
        "thiện kỹ thuật bảo vệ truyền thống và chưa sinh ra nguyên lý bảo vệ mới đột phá từ "
        "kỹ thuật thích ứng và trí tuệ nhân tạo.",
        "The 1990s witnessed the rapid development of electronics and computing, together "
        "with the application of artificial intelligence techniques such as artificial neural "
        "networks, genetic algorithms, evolutionary algorithms, fuzzy logic and related "
        "research to the field of relay protection. For example, the artificial neural network "
        "(ANN) is used to achieve fault type identification, fault distance measurement and "
        "directional protection. The ANN has the characteristics of distributed storage, "
        "parallel processing, self-organisation and self-learning. The application of "
        "artificial intelligence improves the speed and accuracy of fault detection and "
        "analysis, and represents the future development of an intelligent diagnosis system. "
        "Although the performance of protection relays has been improved, these developments "
        "have focused on refining conventional relaying techniques, and no significant new "
        "relaying principles have been derived from adaptive and AI techniques.")
    P(
        "Cùng thời kỳ những năm 1990, với việc mạng lưới điện không ngừng mở rộng, nhu cầu dọn "
        "sự cố nhanh để nâng cao độ ổn định hệ thống đã thúc đẩy nghiên cứu các kỹ thuật phát "
        "hiện sự cố ngoài tần số công nghiệp nhằm tăng tốc độ đáp ứng của rơ-le. Điều này dẫn "
        "đến phát triển cái gọi là bảo vệ dựa trên quá trình chuyển tiếp, dựa trên sóng truyền "
        "và các thành phần chồng chất, sử dụng các quá trình chuyển tiếp do sự cố phát sinh để "
        "bảo vệ hệ thống truyền tải. Các nghiên cứu đã chỉ ra rằng những chuyển tiếp tần số cao "
        "do sự cố sinh ra có thể được phát hiện và định lượng, mở ra khả năng xây dựng nguyên "
        "lý và kỹ thuật bảo vệ mới [2]. Hiện đã có nhiều nỗ lực dành cho việc nghiên cứu phát "
        "hiện chuyển tiếp tần số cao. Một cột mốc quan trọng khác là việc dùng global positioning "
        "system (GPS) trong bảo vệ hệ thống điện như thể hiện trong Hình 1, với nhiều kỹ thuật "
        "mới được đề xuất. Đặc biệt, nguyên lý rơ-le bảo vệ mới có khả năng bảo vệ mạng lưới "
        "điện diện rộng [3, 4], và sau đó khái niệm bảo vệ diện rộng tập trung vào khía cạnh "
        "điều khiển cũng được đưa ra [5].",
        "Also in the 1990s, with the continuous expansion of the power network, the demand for "
        "fast fault clearance to improve system stability encouraged research into "
        "non-power-system-frequency fault detection techniques to increase the speed of "
        "relay response. "
        "This led to the development of so-called transient based protection relays, based on "
        "travelling waves and superimposed components, which use fault-generated transients "
        "for transmission system protection. Studies found that the high-frequency transients "
        "generated by a fault can be detected and quantified, creating the possibility of "
        "developing new protection principles and techniques [2]. Considerable effort has now "
        "been devoted to high-frequency transient detection. Another important milestone is "
        "the use of the global positioning system (GPS) in power system protection, as shown "
        "in Figure 1; in this respect a number of new techniques has been proposed. In "
        "particular, the newly proposed protection relay principle is able to provide "
        "protection for a wide area power network [3, 4]. Following this development, the "
        "concept of wide area protection focusing on the control aspect was presented [5].")
    P(
        "Trong những năm gần đây, sự tăng trưởng mạnh về khả năng xử lý tín hiệu của nền tảng "
        "rơ-le và sự sẵn có của các phương án truyền thông phù hợp đã tạo cơ hội xem lại khái "
        "niệm bảo vệ tập trung. Nghiên cứu [6] về khái niệm bảo vệ tích hợp cho thấy thông tin "
        "thu được từ nhiều nhà máy và phần tử điện có thể được dùng để rút ra nguyên lý và sơ "
        "đồ bảo vệ mới, có ưu thế đáng kể so với kỹ thuật bảo vệ dựa trên từng nhà máy hay "
        "thiết bị riêng lẻ. Liền theo đó, bảo vệ khu vực trạm biến áp [7] nhanh chóng trở "
        "thành một hướng phát triển và ứng dụng thực tiễn. Hơn nữa, sự phát triển của công "
        "nghệ thông tin đã khơi dậy sự quan tâm đến việc sử dụng điện toán đám mây [8] và kỹ "
        "thuật dữ liệu lớn như thể hiện trong Hình 1, nhằm nâng cao hiệu năng bảo vệ và điều "
        "khiển hệ thống điện.",
        "In recent years, the dramatic growth in the signal processing capability of relay "
        "platforms and the availability of suitable communication schemes have provided a new "
        "opportunity to revisit the concept of centralised protection. Research [6] on the "
        "concept of integrated protection shows that information obtained from multiple power "
        "plants and components can be used to derive new protection principles and schemes, "
        "which could have significant advantages over existing protection techniques based on "
        "the individual plant or component. In this respect, substation area protection [7] has "
        "quickly become a practical area of development and application. Furthermore, the "
        "development of information technology has led to interest in using cloud computing "
        "[8] and big data techniques, as shown in Figure 1, to improve the performance of "
        "power system protection and control.")
    P(
        "Ở một hướng khác, các phát triển trong công nghệ tự động hóa tích hợp trạm biến áp "
        "tạo nền tảng kỹ thuật cho việc tối ưu hóa sự kết hợp và tích hợp hệ thống của các "
        "thiết bị và hệ thống giám sát, điều khiển, bảo vệ và đo lường. Việc triển khai bảo vệ "
        "rơ-le và tự động hóa tích hợp thể hiện ở tính tích hợp và chia sẻ tài nguyên, điều "
        "khiển từ xa và chia sẻ thông tin. Với rơ-le vi máy tính và thiết bị bảo vệ vi xử lý "
        "làm hạt nhân, các mạch điều khiển, tín hiệu, đo lường, tính toán hóa đơn và các mạch "
        "khác được tích hợp vào hệ thống máy tính để thay thế tủ bảo vệ-điều khiển truyền "
        "thống, giúp giảm diện tích và vốn đầu tư thiết bị đồng thời tăng độ tin cậy của hệ "
        "thống thứ cấp. Nhờ máy tính và mạng truyền thông tiên tiến, thiết bị bảo vệ rơ-le "
        "thực chất là một máy tính đa chức năng, hiệu năng cao, là một terminal thông minh của "
        "toàn bộ mạng máy tính hệ thống điện. Thiết bị có thể lấy từ mạng bất kỳ thông tin nào "
        "về vận hành và sự cố của hệ thống điện, và truyền bất kỳ thông tin nào về thiết bị "
        "được bảo vệ tới trung tâm điều khiển hoặc bất kỳ terminal nào. Vì vậy mỗi thiết bị "
        "bảo vệ vi xử lý không chỉ thực hiện chức năng bảo vệ rơ-le mà còn thực hiện đo lường, "
        "điều khiển, truyền dữ liệu và các chức năng khác trong điều kiện vận hành bình "
        "thường, hiện thực hóa sự tích hợp giữa bảo vệ, điều khiển, đo lường và truyền dữ liệu.",
        "On another front, developments in substation integrated automation technology provide "
        "the technical basis for optimising the combination and system integration of "
        "monitoring, control, protection and measurement devices and systems. The "
        "implementation of relay protection and integrated automation is reflected in "
        "integration and resource sharing, remote control and information sharing. Taking the "
        "remote terminal unit and the microcomputer protection device as the core, the control, "
        "signal, measurement, billing and other circuits are integrated into the computer "
        "system to replace the traditional control and protection cabinet, reducing floor area "
        "and equipment investment while improving the reliability of the secondary system. "
        "With advanced computers and communication networks, the relay protection device is in "
        "fact a high-performance, multi-function computer, an intelligent terminal of the "
        "whole power system computer network. It can obtain from the network any information "
        "about the operation and fault of the power system, and can transmit any information "
        "about the protected components to the network control centre or to any terminal. "
        "Therefore each microcomputer protection device can complete not only the relay "
        "protection function but also measurement, control, data communication and other "
        "functions under normal operating conditions, realising the integration of protection, "
        "control, measurement and data communication.")

    # ------------------------------ RECENT DEVELOPMENT IN PROTECTION AND CONTROL
    H2("PHÁT TRIỂN GẦN ĐÂY TRONG BẢO VỆ VÀ ĐIỀU KHIỂN HỆ THỐNG ĐIỆN",
       "RECENT DEVELOPMENT IN POWER SYSTEM PROTECTION AND CONTROL")
    P(
        "Cùng với sự tiến bộ nhanh của mạng truyền thông tốc độ cao và công nghệ thông tin, đã "
        "có những phát triển đáng kể trong bảo vệ hệ thống điện, điều khiển hệ thống điện và "
        "điều khiển diện rộng trong những năm gần đây, đặc biệt là trong bảo vệ diện rộng và "
        "bảo vệ tích hợp.",
        "With the rapid progress of high-speed communication networks and information "
        "technology, there have been significant developments in power system protection, "
        "power system control and wide area control in recent years, particularly in "
        "wide-area and integrated protection.")

    H3("Bảo vệ diện rộng", "Wide Area Protection")
    P(
        "Trong những năm gần đây, sự phát triển nhanh của công nghệ truyền thông đã làm cho "
        "việc trao đổi thông tin diện rộng trở thành hiện thực. Theo đó, sự xuất hiện của hệ "
        "thống đo lường diện rộng (WAMS) đã mang lại ý tưởng mới cho thiết kế hệ thống bảo vệ "
        "hệ thống điện. Nguyên lý bảo vệ diện rộng đầu tiên bắt nguồn từ bảo vệ dựa trên quá "
        "trình chuyển tiếp năm 1996 [2], trong đó đồng bộ thời gian GPS đóng vai trò chính trong "
        "thiết kế [3]. Ngay sau đó, một bài tổng kết năm 1997 đã phác thảo một cách hệ thống "
        "khái niệm gọi là bảo vệ diện rộng [4], chủ yếu tập trung vào khía cạnh điều khiển của "
        "khu vực. Bảo vệ diện rộng dựa trên các thuật toán mới, rút ra từ phép đo tại nhiều "
        "điểm thông tin, có khả năng dọn sự cố nhanh, tin cậy và chính xác, phân tích ảnh hưởng "
        "đến độ ổn định hệ thống dựa trên phân tích hệ thống sự cố, và thực hiện các biện pháp "
        "điều khiển cần thiết để thực hiện các chức năng bảo vệ rơ-le, an toàn và điều khiển "
        "ổn định nhằm ngăn ngừa sụp đổ điện áp. Bảo vệ rơ-le diện rộng nhanh chóng trở thành "
        "đề tài nghiên cứu sôi động với nhiều kết quả được công bố, đặc biệt trong những năm "
        "gần đây.",
        "In recent years, the rapid development of communication technologies has made "
        "wide-area information exchange possible. In this respect, the emergence of the wide "
        "area measurement system has provided a new idea for the design of power system "
        "protection systems. The first wide-area protection principle was derived from "
        "transient based protection in 1996 [2], in which GPS time synchronisation played a "
        "major role in the design [3]. This was immediately followed by a summary paper in "
        "1997 that systematically outlined the concept of so-called wide area protection [4], "
        "focusing principally on the control aspect of the area. Wide area protection based on "
        "novel algorithms, derived from measurements at multiple information points, is able "
        "to provide fast, reliable and accurate fault clearance, to analyse the effects on "
        "system stability on the basis of fault system analysis, and to take the necessary "
        "control measures to perform the functions of relay protection, security and stability "
        "control in order to prevent voltage collapse. Wide area relay protection has quickly "
        "become a topical research subject, with many results published particularly in recent "
        "years.")

    H3("Bảo vệ tích hợp", "Integrated Protection")
    P(
        "Với sự phát triển của công nghệ số, ngày càng nhiều chức năng bảo vệ cho một thiết bị "
        "nhất định (đường dây, máy biến áp, máy phát, v.v.) được triển khai trong một thiết bị "
        "bảo vệ duy nhất nhằm đạt được một mức độ tích hợp nhất định. Ví dụ, một rơ-le bảo vệ "
        "đường dây kỹ thuật số có thể có chức năng khoảng cách hoặc vi sai dòng điện làm bảo vệ "
        "chính, và các chức năng hướng và quá dòng làm bảo vệ dự phòng. Những phát triển gần "
        "đây về vi xử lý và truyền thông đã mang lại cách thức mới để rút ra nguyên lý và sơ đồ "
        "bảo vệ dựa trên thông tin thu được từ nhiều nhà máy và phần tử điện, có thể có ưu thế "
        "đáng kể so với kỹ thuật bảo vệ dựa trên từng nhà máy hay phần tử riêng lẻ [5]. Khác với "
        "bảo vệ tập trung (hay bảo vệ khu vực trạm biến áp), bảo vệ tích hợp không chỉ đơn "
        "giản tập trung phần cứng và phần mềm rơ-le, mà tập trung vào phát triển các khái niệm "
        "và thuật toán mới dựa trên phép đo tại nhiều điểm; theo cách này, người ta hy vọng "
        "nâng cao đáng kể hiệu năng bảo vệ. Cũng đã có nghiên cứu về bảo vệ diện rộng tích hợp "
        "[9].",
        "With the development of digital technology, more and more protection functions for "
        "any given apparatus (line, transformer, generator, etc.) have been implemented within "
        "one protective device to achieve a certain degree of integration. For example, a "
        "numeric line protection relay may have a distance or current differential function "
        "as the main protection, and directional and overcurrent functions as the back-up "
        "protection. Recent developments in microprocessors and communication techniques have "
        "provided new means to derive protection principles and schemes based on information "
        "obtained from multiple power plants and components, which may have significant "
        "advantages over existing protection techniques based on the individual plant or "
        "component [5]. Unlike centralised protection (or substation area protection), "
        "integrated protection does not simply centralise the relay hardware and software, but "
        "concentrates on developing new concepts and algorithms based on multiple points of "
        "measurement; in this way it is hoped that protection performance can be significantly "
        "improved. There has also been research in the field of integrated wide area "
        "protection [9].")

    H3("Điều khiển diện rộng", "Wide Area Control")
    P(
        "Việc triển khai ngày càng nhiều phép đo diện rộng sẽ nâng cao đáng kể vận hành và "
        "điều khiển hệ thống điện diện rộng. Các phép đo này cung cấp thông tin phasor điện áp "
        "và dòng điện được đồng bộ với độ chính xác cao theo một tham chiếu thời gian chung do "
        "GPS cung cấp. Nhờ đó, có thể triển khai nhiều ứng dụng giám sát và điều khiển hệ thống "
        "điện để cải thiện nhận thức và độ tin cậy của hệ thống, bao gồm ước trạng thái nâng cao "
        "từ phép đo hỗn hợp của Remote Terminal Unit (RTU) và Phasor Measurement Unit (PMU) "
        "[10], ước và kiểm chứng mô hình động trực tuyến [11], quản lý tắc nghẽn thời gian "
        "thực, ước ổn định thời gian thực [12], phát hiện và triệt tiêu dao động liên vùng "
        "[13]. Tuy nhiên, các ứng dụng quan trọng nhất và thách thức nhất là phát hiện và "
        "điều khiển ổn định diện rộng theo thời gian thực nhằm ngăn ngừa mất điện diện rộng "
        "[14]. Cũng có nghiên cứu về bảo vệ và điều khiển tích hợp [15].",
        "The increased deployment of wide-area measurements will significantly enhance "
        "wide-area power system operation and control. These measurements provide voltage and "
        "current phasor information synchronised with high precision to a common time "
        "reference supplied by GPS. Therefore a wide range of power system monitoring and "
        "control applications can be implemented to improve system awareness and reliability, "
        "including enhanced state estimation based on mixed Remote Terminal Unit (RTU) and "
        "Phasor Measurement Unit (PMU) measurements [10], online dynamic model estimation and "
        "validation [11], real-time congestion management, real-time stability estimation [12], "
        "and the detection and damping of inter-area oscillations [13]. However, the most "
        "important and challenging applications are the implementation of wide area real-time "
        "stability detection and control to prevent blackouts [14]. There has also been "
        "research on integrated protection and control [15].")

    H3("Remote Terminal Unit (RTU) và Phasor Measurement Unit (PMU)",
       "Remote Terminal Unit (RTU) and Phasor Measurement Unit (PMU)")
    P(
        "RTU thu thập dữ liệu đo lường tại chỗ từ các thiết bị trong trạm biến áp và thực hiện "
        "các lệnh điều khiển do trung tâm gửi tới; RTU là nền tảng của hệ thống điều khiển và "
        "giám sát (SCADA) truyền thống. PMU thì cung cấp các phasor điện áp và dòng điện được "
        "đóng dấu thời gian theo một tham chiếu chung, cho phép quan sát động trực tiếp các "
        "dao động của hệ thống mà các phép đo SCADA thông thường không thấy được. Sự kết hợp "
        "giữa phép đo RTU và PMU làm nền tảng cho ước trạng thái nâng cao [10], đồng thời mở "
        "đường cho giám sát và điều khiển diện rộng động với độ chi tiết và độ tin cậy cao hơn. "
        "Chính luồng dữ liệu đồng bộ này là nguồn thông tin cho các sơ đồ bảo vệ và điều khiển "
        "diện rộng được mô tả trong chương này.",
        "The RTU gathers local telemetry from devices in the substation and executes the "
        "control commands sent by the control centre; it is the foundation of traditional "
        "supervisory control and data acquisition (SCADA) systems. The PMU, in contrast, "
        "provides voltage and current phasors time-stamped against a common reference, "
        "enabling direct dynamic observation of system oscillations that conventional SCADA "
        "measurements cannot resolve. The combination of RTU and PMU measurements underpins "
        "enhanced state estimation [10] and opens the way to dynamic wide-area monitoring and "
        "control with greater detail and reliability. It is precisely this stream of "
        "synchronised data that feeds the wide-area protection and control schemes described "
        "in this chapter.")

    H3("Khái niệm và phát triển mới", "New Concept and Development")
    P(
        "Dựa trên những phát triển kể trên, một khái niệm mới về bảo vệ và điều khiển diện rộng "
        "tích hợp (IWAPC) đã được đề xuất gần đây. Trọng tâm của khái niệm này [16, 17] là sự "
        "tích hợp giữa bảo vệ và điều khiển, đặc biệt ở cấp diện rộng hoặc khu vực, nhằm mang "
        "lại nhiều lợi ích cho hệ thống bảo vệ và điều khiển tương lai, ví dụ khả năng hợp nhất "
        "hệ thống ba tuyến phòng thủ và ra quyết định tự phục hồi trực tuyến, để ngăn ngừa "
        "việc cắt dây chuyền diện rộng. Khái niệm IWAPC được giới thiệu với một hệ thống phối "
        "hợp phân cấp ba cấp, được hỗ trợ bởi mạng truyền thông diện rộng đồng bộ thời gian "
        "thực được thiết kế riêng, cung cấp bảo vệ và điều khiển cho các trạm biến áp hoặc nhà "
        "máy điện diện rộng/khu vực và mạng lưới điện liên quan. Yếu tố then chốt là nền tảng "
        "thông tin bảo vệ và điều khiển diện rộng tích hợp, nhận dữ liệu đồng bộ thời gian thực "
        "từ mạng truyền thông để hỗ trợ tích hợp bảo vệ và điều khiển ở cấp diện rộng/khu vực.",
        "Based on the developments mentioned above, a new concept of integrated wide area "
        "protection and control (IWAPC) has been proposed recently. The main focus of the "
        "concept [16, 17] is the integration between protection and control, particularly at "
        "the wide-area or regional level, with the aim of bringing a number of benefits to "
        "future protection and control systems, for example the potential to merge the three "
        "lines of defence and to perform online self-healing decision making in order to "
        "prevent cascading tripping of a large area power network. The concept of integrated "
        "wide area protection and control is introduced as a three-level hierarchically "
        "coordinated system supported by a specially designed real-time synchronised wide-area "
        "communication network, providing protection and control for wide area or regional "
        "substations and plants and their associated power network. The key element in the "
        "system is the integrated wide area protection and control information platform, which "
        "receives real-time synchronised data from the communication network to support the "
        "integration of protection and control at the wide area/regional level.")
    P(
        "Nền tảng thông tin cũng hỗ trợ ứng dụng hệ thống điện toán đám mây được thiết kế riêng "
        "để thực hiện một số chức năng thứ cấp cho trạm biến áp và mạng lưới điện. Ngoài các "
        "chức năng cơ bản của bảo vệ rơ-le, nền tảng cần có dung lượng lớn để lưu trữ thông tin "
        "và dữ liệu sự cố, khả năng xử lý dữ liệu nhanh, khả năng truyền thông mạnh và các "
        "chức năng khác; nó cho phép các thiết bị bảo vệ, điều khiển và mạng điều độ cùng chia "
        "sẻ toàn bộ dữ liệu, thông tin và tài nguyên mạng của hệ thống, đồng thời có thể thực "
        " hiện giám sát từ xa với hệ thống máy tính giám sát truyền thông của trạm biến áp. Với "
        "nền tảng đề xuất, cấu trúc của thiết bị trạm biến áp tương lai có thể được định hình "
        "lại, tạo một khung linh hoạt để xây dựng lưới điện tương tác và từ đó nâng cao độ tin "
        "cậy và an toàn của lưới điện.",
        "The information platform also supports the application of a cloud computing system "
        "specially designed to implement a number of secondary functions for substations and "
        "power networks. In addition to the basic functions of relay protection, the platform "
        "should have a large capacity for fault information and data storage, fast data "
        "processing functions, powerful communication functions and other functions; it allows "
        "protection and control devices and the dispatching network to share the whole system "
        "data, information and network resources, and can also carry out remote monitoring "
        "together with the computer monitoring system of substation communication. With the "
        "proposed platform, the architecture of future substation equipment may be reshaped to "
        "provide a flexible framework for building an interactive grid, and subsequently to "
        "improve the reliability and security of power grids.")

    # ---------------------- INTEGRATED WIDE AREA/REGIONAL PROTECTION AND CONTROL
    H2("BẢO VỆ VÀ ĐIỀU KHIỂN DIỆN RỘNG/KHU VỰC TÍCH HỢP",
       "INTEGRATED WIDE AREA/REGIONAL PROTECTION AND CONTROL")

    H3("Kiến trúc bảo vệ và điều khiển diện rộng tích hợp",
       "Architecture of Integrated Wide Area Protection and Control")
    P(
        "Hệ thống bảo vệ và điều khiển diện rộng hoặc khu vực tích hợp (IWAPC) được đề xuất "
        "minh họa trong Hình 2. Đã có những phát triển nhanh trong cả mạng truyền tải và phân "
        "phối, ví dụ bù dọc trên đường dây AC và đường dây DC cao áp trong hệ thống truyền "
        "tải, phát điện phân tán và lưu trữ năng lượng trong hệ thống phân phối. Những phát "
        "triển này tạo ra đặc tính phức tạp hơn nhiều so với hệ thống truyền thống. Hệ quả là "
        "hệ thống bảo vệ và điều khiển hiện có không còn đủ hiệu quả để đối phó với những hệ "
        "thống mới, dẫn đến đề xuất hệ thống IWAPC. Như hình minh họa, hệ thống IWAPC gồm các "
        "thiết bị khác nhau ở các tầng khác nhau: từ dưới lên là thiết bị thông minh tích hợp "
        "đa chức năng ở cấp địa phương; mạng truyền thông trạm biến áp và bảo vệ, điều khiển "
        "trạm biến áp tích hợp ở cấp trạm biến áp; mạng truyền thông diện rộng, nền tảng thông "
        "tin diện rộng tích hợp và bảo vệ, điều khiển diện rộng (khu vực) tích hợp ở cấp diện "
        "rộng. Các phần then chốt của hệ thống là mạng truyền thông diện rộng tốc độ cao và "
        "nền tảng thông tin đồng bộ thời gian thực.",
        "The proposed integrated wide area or regional protection and control system (IWAPC) "
        "is illustrated in Figure 2. There have been rapid developments in both power "
        "transmission and distribution networks, for example series compensation in AC lines "
        "and high-voltage DC lines in transmission systems, and distributed generation and "
        "energy storage in distribution systems. These developments result in far more "
        "complicated characteristics than those of conventional systems. Consequently, the "
        "existing protection and control system is no longer effective in coping with the new "
        "systems, which has led to the proposed IWAPC system. As shown, the IWAPC system "
        "consists of different equipment at different layers: from bottom to top, there is the "
        "integrated multiple-function intelligent equipment at the local level; the substation "
        "communication network and integrated substation protection and control at the "
        "substation level; and the wide area communication network, the integrated wide area "
        "information platform and integrated wide area (regional) protection and control at "
        "the wide area level. The key parts of the system are the high-speed wide area "
        "communication network and the real-time synchronisation information platform.")
    P(
        "IWAPC còn được mở rộng sang công tác điều độ nhằm hiện thực hóa tích hợp tự động hóa "
        "điều độ, bảo vệ và điều khiển lưới điện, và theo kiến trúc điều độ ba cấp (quốc gia, "
        "tỉnh, khu vực) để thực hiện các chức năng bảo vệ, điều khiển và quản lý điều độ khu "
        "vực.",
        "The IWAPC is further extended to dispatching in order to achieve the integration of "
        "dispatching automation, protection and control of the power grid, and, according to "
        "the three-level dispatching architecture (country, province, region), to implement "
        "regional protection, control and dispatching management functions.")
    FIG(2, F.fig_f62())

    H3("Thiết bị thông minh đa chức năng ở cấp địa phương",
       "Multiple-Function Intelligent Equipment at the Local Level")
    P(
        "Như thể hiện trong Hình 2, thiết bị thông minh ở cấp địa phương là thiết bị thứ cấp "
        "tích hợp đa chức năng trong trạm biến áp, chủ yếu gồm MU, terminal thông minh, đo "
        "đếm, PMU và bảo vệ địa phương. Thiết bị này lấy mẫu mọi dữ liệu thời gian thực và gửi "
        "thông tin tới bảo vệ và điều khiển trạm biến áp tích hợp cũng như bảo vệ và điều khiển "
        "diện rộng; đồng thời nó nhận và thực hiện các lệnh điều khiển từ bảo vệ và điều khiển "
        "trạm biến áp tích hợp và từ IWAPC. Thiết bị có thể được tích hợp vào thiết bị điện "
        "sơ cấp và thực hiện bảo vệ địa phương cho khoảng 90% đoạn đường dây liên quan. Nó có "
        "cấu hình dự phòng để bảo đảm độ tin cậy, cùng với các chức năng tích hợp khác như máy "
        "ghi sự cố, lưu trữ dữ liệu và phân tích mạng.",
        "As shown in Figure 2, the intelligent equipment at the local level is an integrated "
        "multiple-function secondary device in the substation, mainly consisting of the MU, "
        "intelligent terminal, metering, PMU and local protection. The equipment is responsible "
        "for sampling all real-time data and sending information to integrated substation "
        "protection and control and to wide area protection and control. It also receives and "
        "carries out the control commands from the integrated substation protection and control "
        "and from the IWAPC. The equipment can be integrated into primary power apparatus and "
        "achieve local protection for about 90% of its associated line sections. It has a "
        "redundant configuration to ensure reliability, together with other integrated "
        "functions such as a fault recorder, data storage and network analysis.")

    H3("Bảo vệ và điều khiển trạm biến áp/nhà máy tích hợp",
       "Integrated Substation/Plant Protection and Control")
    P(
        "Bảo vệ và điều khiển trạm biến áp tích hợp các chức năng bảo vệ đường dây, thanh cái, "
        "máy biến áp, chống hỏng cầu dao, tự động đóng lại, chuyển thanh cái tự động, cắt tải "
        "theo tần số thấp (UFLS), cắt tải theo điện áp thấp (UVLS), cắt liên khóa quá tải và "
        "chức năng điều khiển trạm biến áp. Thiết bị dùng thông tin của toàn trạm biến áp để "
        "thực hiện bảo vệ dự phòng cho trạm và điều khiển an toàn tự động. Các cầu dao (CB) "
        "được dùng làm đơn vị để cấu hình bảo vệ dự phòng thích ứng, và bảo vệ vi sai dòng "
        "được dùng để thay thế bảo vệ quá dòng phân cấp, bảo vệ chống hỏng cầu dao và bảo vệ "
        "vùng chết trong hệ thống bảo vệ truyền thống.",
        "Integrated substation protection and control combines the functions of line, busbar "
        "and transformer protection, breaker failure protection, autoreclosure, automatic bus "
        "transfer, under-frequency load shedding (UFLS), under-voltage load shedding (UVLS), "
        "overload inter-tripping and substation control functions. It uses information from the "
        "whole substation to achieve substation back-up protection and automatic safety "
        "control. The circuit breakers (CBs) are used as units to configure adaptive back-up "
        "protection, and current differential protection is used to replace the staged "
        "overcurrent protection, breaker failure protection and dead zone protection of the "
        "conventional protection system.")

    H3("Bảo vệ và điều khiển diện rộng/khu vực tích hợp",
       "Integrated Wide Area/Regional Protection and Control")
    P(
        "IWAPC được thiết kế riêng cho bảo vệ và điều khiển mạng lưới điện, có khả năng cung "
        "cấp bảo vệ nhanh. Ngoài ra, hệ thống còn tích hợp các chức năng UFLS và UVLS tự động, "
        "điều khiển điện áp và tần số, phát hiện dao động và tách hệ thống khi mất đồng bộ. "
        "IWAPC cũng bao gồm chức năng bảo vệ và điều khiển an toàn mặt cắt truyền tải. Khác "
        "với bảo vệ và điều khiển truyền thống vốn tách biệt cả trong thiết kế lẫn vận hành, "
        "IWAPC tích hợp bảo vệ và điều khiển thành một hệ thống kết hợp tối ưu, phối hợp hiệu "
        "quả bảo vệ và điều khiển diện rộng (khu vực) nhằm đạt được cải thiện đáng kể về bảo vệ "
        "và điều khiển hệ thống điện.",
        "The IWAPC, specially designed for the protection and control of the power network, is "
        "able to offer fast protection. In addition, it integrates the functions of automatic "
        "UFLS and UVLS, voltage and frequency control, oscillation detection and out-of-step "
        "separation. The IWAPC also incorporates the function of transmission cross-section "
        "safety protection and control. Unlike conventional protection and control, which are "
        "separated in both design and operation, the IWAPC integrates protection and control "
        "into one optimally combined system, effectively coordinating wide area (regional) "
        "protection and control in order to achieve significant improvements in power system "
        "protection and control.")

    H3("Mạng truyền thông tốc độ cao đồng bộ",
       "Synchronised High Speed Communication Network")
    P(
        "Mạng truyền thông nhanh là một trong những yếu tố quan trọng nhất của hệ thống IWAPC. "
        "Về vấn đề này, Packet Transport Network (PTN) có thể là lựa chọn tốt cho nhiệm vụ này. "
        "Mạng truyền thông điện hiện nay chủ yếu dùng nền tảng vận chuyển đa dịch vụ dựa trên "
        "Synchronous Digital Hierarchy (SDH). SDH có ưu điểm hiệu quả cao khi chở các dịch vụ "
        "TDM, độ trễ thấp, độ tin cậy cao và khả năng quản lý đầu cuối. Tuy nhiên, với xu hướng "
        "phát triển lưới điện thông minh, công nghệ SDH dần bộc lộ hạn chế như hiệu quả chở "
        "thấp và kém linh hoạt với dịch vụ dữ liệu. Ngược lại, PTN có thể thực hiện ghép kênh "
        "thống kê và truyền tải gói tin hiệu quả nhờ lõi chuyển mạch gói, khắc phục nhược điểm "
        "băng thông cứng của SDH; đồng thời PTN cung cấp chất lượng dịch vụ, vận hành, quản lý "
        "và bảo trì tốt.",
        "The fast communication network is one of the most important elements of the IWAPC "
        "system. In this respect, the Packet Transport Network (PTN) may be a better choice "
        "for implementing such a task. The present power communication network is mainly based "
        "on a multi-service transport platform using the Synchronous Digital Hierarchy (SDH). "
        "Its advantages lie in high efficiency for carrying TDM services, low latency, high "
        "reliability and end management capabilities. However, with new trends in smart grid "
        "development, SDH technology has gradually revealed its limitations, such as low "
        "bearing efficiency and poor flexibility for data services. In contrast, PTN can "
        "realise statistical multiplexing and efficient transfer of packet services by using a "
        "packet-switched core, overcoming the weaknesses of rigid SDH bandwidth. In addition, "
        "it can provide good quality of service, operation, administration and maintenance.")
    P(
        "Mạng cáp quang tự phục hồi được dùng để kết nối nhiều trạm biến áp trong khu vực, bảo "
        "đảm chia sẻ đầy đủ thông tin động và chuyển tiếp của mọi phép đo điện, trạng thái cầu "
        "dao và tác động của bảo vệ; công nghệ IEEE-1588 có độ tin cậy cao được dùng để bảo "
        "đảm đồng bộ thời gian của dữ liệu chia sẻ, cung cấp dữ liệu cho bảo vệ và điều khiển "
        "diện rộng tích hợp. Tuy nhiên, SDH vẫn là một lựa chọn cho nhiệm vụ này vì nó đã được "
        "áp dụng rộng rãi trong mạng điện.",
        "A self-healing fibre optic network is used to connect a number of substations in the "
        "region, ensuring full sharing of dynamic and transient information for all electrical "
        "measurements, breaker status and protection operations; high-reliability IEEE-1588 "
        "technology is used to ensure the synchronisation timing of the shared data, providing "
        "data for integrated wide area protection and control. However, SDH remains an option "
        "for the task because it has been widely applied in power networks.")

    H3("Nền tảng thông tin đồng bộ", "Synchronized Information Platform")
    P(
        "Trạm biến áp được lắp đặt nhiều thiết bị điện với thiết kế phức tạp và khó bảo trì. "
        "Khi mức độ tự động hóa và thông minh của hệ thống điện ngày càng tăng, mạng lưới hệ "
        "thống tiếp tục mở rộng cùng với khối lượng thông tin bảo vệ và điều khiển rất lớn. Vì "
        "mỗi thông tin được thu thập và lưu trữ bởi các thiết bị khác nhau trong các hệ thống "
        "riêng biệt, khả năng tương tác dữ liệu nội bộ giữa các hệ thống kém, trong khi các "
        "giao thức truyền thông phức tạp dễ tạo ra các «ốc đảo thông tin». Hệ quả là dữ liệu "
        "đo lường và cơ chế bảo vệ, điều khiển không được chia sẻ, cản trở tích hợp thông tin. "
        "Bảo vệ và điều khiển lưới điện thông minh cần đáp ứng tình huống ứng dụng mới, nâng "
        "cao hơn nữa năng lực nền tảng thông tin cho các công nghệ trọng điểm trong tương lai "
        "và làm cho hệ thống nền tảng thông tin mở hơn.",
        "A substation is installed with a wide range of electrical equipment with complex "
        "designs that is difficult to maintain. As the level of power system automation and "
        "intelligence continues to improve, the system network keeps expanding along with the "
        "huge amount of protection and control information. Since each piece of information is "
        "collected and stored by different devices in separate systems, the interoperability of "
        "internal power system data between systems is poor, while complex communication "
        "protocols tend to create information islands. Consequently, measurement data and "
        "protection control mechanisms cannot be shared, which restricts information "
        "integration. The protection and control of the smart grid needs to meet the demands "
        "of new application situations, to further improve the capabilities of the information "
        "platform for future key technologies, and to make the information platform system "
        "more open.")
    P(
        "Nền tảng thông tin đồng bộ thời gian thực thu thập chính xác thông tin diện rộng và "
        "khai thác dữ liệu để tìm hiểu mối quan hệ logic giữa các thông tin thời gian thực, nhằm "
        "nâng cao độ nhạy, độ tin cậy và khả năng chịu lỗi. Dữ liệu nhận từ nền tảng gồm phép "
        "đo tĩnh, động, chuyển tiếp và trạng thái của cầu dao. Thông tin có giá trị được trích "
        "xuất từ dữ liệu và phân bổ cho các thuật toán tính toán thiết kế riêng trong nền tảng "
        "để thực hiện chức năng bảo vệ và điều khiển tiên tiến cho mạng lưới điện. Tốc độ "
        "truyền dữ liệu tùy thuộc vào ứng dụng: chậm cho phân tích sự cố, gần thời gian thực "
        "cho giám sát, thời gian thực cho điều khiển và tốc độ cao cho bảo vệ diện rộng, đặc "
        "biệt là đồng bộ thời gian. Thông tin cũng có thể gồm các loại dữ liệu khác như nhiệt "
        "độ dầu và nhiệt độ môi trường của máy biến áp, tốc độ và hướng gió, cường độ ánh sáng "
        "mặt trời. Mặt khác, thông tin được lưu trữ theo cách phân cấp thay vì tập trung, phù "
        "hợp với hệ thống bảo vệ và điều khiển phân cấp. Được trang bị công nghệ truyền thông "
        "đồng bộ tốc độ cao mới nhất, tích hợp kỹ thuật bảo vệ tiên tiến và những phát triển "
        "mới nhất của hệ thống điều khiển, hệ thống không chỉ đưa ra bảo vệ nhanh mà còn điều "
        "khiển trọn vẹn toàn bộ mạng lưới điện.",
        "The real-time synchronised information platform accurately collects wide area "
        "information and conducts data mining to investigate the logical relations between "
        "real-time information, so as to increase sensitivity, reliability and fault tolerance. "
        "The data received from the platform includes static, dynamic and transient "
        "measurements and the states of circuit breakers. Valuable information is extracted "
        "from the data and allocated to specially designed computation algorithms in the "
        "platform to perform advanced protection and control functions for the power network. "
        "The transfer speed depends on the application: slow speed for contingency analysis, "
        "near real-time speed for monitoring, real-time speed for control and high speed for "
        "wide area protection, in particular time synchronization. The information can also "
        "include other types of data, such as the oil and ambient temperature of the "
        "transformer, wind speed and direction, and sun intensity. On the other hand, the "
        "information is stored in a hierarchical rather than a centralised manner, in keeping "
        "with the hierarchical protection and control system. Equipped with the latest "
        "high-speed synchronised communication technology and integrated with advanced "
        "protection techniques and the latest control system developments, the system offers "
        "not only fast protection but also complete control of the entire power network.")
    P(
        "Công nghệ tính toán tiên tiến được đưa vào để xây dựng nền tảng thông tin đồng bộ cho bảo "
        "vệ và điều khiển diện rộng, tạo mạng thu thập dữ liệu vận hành và bảo trì toàn cảnh, "
        "cung cấp giao diện chuẩn cho thiết bị đầu cuối, hình thành nền tảng thông tin chia sẻ "
        "tài nguyên, linh hoạt, tương tác, mở và có trật tự. Tóm lại, công nghệ tính toán tiên "
        "tiến được dùng để xây dựng nền tảng thông tin thông minh phân tán, hợp tác, đơn giản "
        "hóa thiết bị thu thập dữ liệu đầu cuối và phá vỡ rào cản giữa các hệ thống bảo vệ và "
        "điều khiển tại các trạm biến áp khác nhau thông qua nền tảng thông tin đồng bộ được "
        "thiết kế riêng.",
        "Advanced computing technology is introduced to establish a synchronised information "
        "platform for wide area protection and control, to build a panoramic operation and "
        "maintenance data collection network, to provide a standardised interface to terminal "
        "devices, and to form an information platform that is resource-sharing, flexible, "
        "interactive, open and ordered. In summary, advanced computing technologies are used "
        "to build a distributed collaborative intelligent information platform, simplifying "
        "terminal data collection equipment and breaking down the barriers between protection "
        "and control systems at different substations through the specially designed "
        "synchronised information platform.")

    H3("Điện toán đám mây diện rộng", "Wide Area Power Cloud")
    P(
        "Dựa trên nền tảng thông tin kể trên, một hệ thống đám mây phân tán được thiết kế để "
        "thực hiện các chức năng ở cấp trạm biến áp và cấp khu vực, như xác định vị trí sự cố "
        "diện rộng, chọn đường dây sự cố, giám sát chất lượng điện năng, chỉnh định bảo vệ, "
        "v.v. Các chức năng mở rộng còn bao gồm giám sát thiết bị, quản lý vòng đời và quản lý "
        "vận hành, như thể hiện trong Hình 3.",
        "Based on the information platform mentioned above, a distributed cloud system is "
        "designed to implement functions at the substation and regional levels, such as wide "
        "area fault location, fault line selection, power quality monitoring and protection "
        "settings. The extended functions also include equipment monitoring, life cycle and "
        "operation management, as shown in Figure 3.")
    FIG(3, F.fig_f63())
    P(
        "Hiện nay, mỗi trạm biến áp lắp đặt nhiều loại thiết bị thứ cấp thực hiện các chức năng "
        "khác nhau, và số lượng nguồn năng lượng phân tán công suất nhỏ được đấu vào hệ thống "
        "ngày càng nhiều làm tăng mạnh số lượng thiết bị. Việc thực hiện các chức năng phức "
        "tạp của những thiết bị này trong một hệ thống «đám mây» phân tán được phát triển riêng "
        "sẽ giảm đáng kể vốn đầu tư thiết bị. Đám mây ở cấp trạm biến áp nhận dữ liệu từ cấp "
        "quá trình, còn đám mây khu vực nhận dữ liệu từ nền tảng thông tin, gồm phép đo tĩnh, "
        "động, chuyển tiếp và trạng thái của cầu dao; nó trích xuất thông tin có giá trị và "
        "phân bổ cho các thuật toán tính toán thiết kế riêng trong nền tảng để thực hiện chức "
        "năng tiên tiến, xác định đường dây sự cố, vị trí sự cố chính xác và hàm lượng sóng "
        "hài.",
        "Currently, many kinds of secondary equipment implementing different functions are "
        "installed in each substation, and an increasing number of small-capacity distributed "
        "energy resources added to the system greatly increases the number of devices. "
        "Implementing the complex functions of these devices in a specially developed "
        "distributed cloud system will greatly reduce equipment investment. The cloud at the "
        "substation level receives data from the process level, while the regional cloud "
        "receives data from the information platform, including static, dynamic and transient "
        "measurements and the states of circuit breakers; it extracts valuable information and "
        "allocates it to specially designed computation algorithms in the platform to perform "
        "advanced functions, identifying the faulted line, the accurate fault location and the "
        "harmonic content.")
    P(
        "Nền tảng điện toán đám mây có thể tận dụng tối đa «năng lực xử lý của đám mây» để giảm "
        "tải cho thiết bị thứ cấp đầu cuối. Dựa trên kỹ thuật dữ liệu lớn, các đám mây tính "
        "toán có năng lực xử lý mạnh theo yêu cầu. Không cần nâng cấp liên tục để tăng năng lực "
        "xử lý của thiết bị, cũng không cần cập nhật phần mềm để thực hiện nhiều tác vụ khác "
        "nhau. Hệ thống đám mây còn mang lại nhiều ưu điểm khác như chia sẻ thông tin diện rộng, "
        "chuẩn hóa phần mềm và thuật toán, giảm vốn đầu tư thiết bị, diện tích chiếm dụng của "
        "trạm biến áp và khối lượng công việc vận hành, bảo trì.",
        "The cloud computing platform can make full use of the processing ability of the cloud "
        "to reduce the burden on terminal secondary equipment. Based on big data techniques, "
        "the computing clouds enjoy strong on-demand processing power. There is no need for "
        "endless upgrades to improve the processing capacity of the equipment, and no need to "
        "update the software in order to carry out a variety of tasks. The cloud system also "
        "brings many further advantages, such as wide area information sharing, standardisation "
        "of software and algorithms, and reductions in equipment investment, substation floor "
        "area and the workload of operation and maintenance.")

    # ----------------------------------------------------------- CONCLUSIONS
    H2("KẾT LUẬN", "CONCLUSIONS")
    P(
        "Chương này trình bày hệ thống bảo vệ và điều khiển diện rộng tích hợp dựa trên cấu trúc "
        "phân cấp, tích hợp bảo vệ và điều khiển ở cấp địa phương, cấp trạm biến áp và cấp khu "
        "vực. Bao phủ cả mạng truyền tải và phân phối, hệ thống được hỗ trợ bởi mạng truyền "
        "thông đồng bộ tốc độ cao và nền tảng thông tin bảo vệ và điều khiển thời gian thực đề "
        "xuất. Hệ thống tích hợp kỹ thuật bảo vệ tiên tiến và những phát triển mới nhất của "
        "hệ thống điều khiển, không chỉ cho bảo vệ nhanh mà còn cho điều khiển trọn vẹn toàn bộ "
        "mạng lưới điện. Hệ thống mở ra khả năng hợp nhất ba tuyến phòng thủ thành một hệ "
        "thống thống nhất nhằm bảo đảm hiệu quả vận hành tin cậy và an toàn của lưới điện. Dựa "
        "trên nền tảng thông tin của hệ thống, một hệ thống đám mây điện phân tán cũng được "
        "thiết kế để hỗ trợ nhiều ứng dụng tiên tiến cho bảo vệ và điều khiển diện rộng tích "
        "hợp.",
        "This chapter presents an integrated wide area protection and control system based on a "
        "hierarchical structure, integrating protection and control at the local, substation "
        "and regional levels. Covering both transmission and distribution networks, the system "
        "is supported by the proposed high-speed synchronised communication network and the "
        "real-time protection and control information platform. Integrating advanced "
        "protection techniques and the latest developments in control systems, the system "
        "offers not only fast protection but also complete control of the entire power network. "
        "It offers the potential to merge the three lines of defence into a unified system so "
        "as to ensure more effectively the reliable and safe operation of the power grid. Based "
        "on the system information platform, a distributed power cloud system is also designed "
        "to support many advanced applications for integrated wide area protection and "
        "control.")
    P(
        "Với những tiến bộ liên tục của công nghệ đo lường, truyền thông và thông tin, hệ thống "
        "có triển vọng sáng sủa cho ứng dụng thực tiễn; hiệu năng tổng thể của bảo vệ và điều "
        "khiển có thể được kỳ vọng cải thiện. Tuy nhiên, để hệ thống thực sự hữu ích trong ứng "
        "dụng hệ thống điện, việc triển khai thực tế của nó cũng cần dễ quản lý, thân thiện "
        "với người dùng và hiệu quả về chi phí. Tác giả cho rằng, để đạt được những mục tiêu "
        "này, bảo vệ và điều khiển tích hợp ở cấp diện rộng là một hướng đi đầy hứa hẹn.",
        "With the continuous advances in measurement, communication and information "
        "technologies, the system has a bright future for practical application, and an overall "
        "improvement in protection and control performance can be expected. However, for the "
        "system to become useful in power system applications, it is equally important that its "
        "practical implementation be readily manageable, user-friendly and cost-effective. The "
        "authors hold that, to achieve these goals, the proposed integrated protection and "
        "control at the wide area level offers an appealing way forward.")

    # ----------------------------------------------- REFERENCES / SOURCE NOTE
    H2("TÀI LIỆU THAM KHẢO", "REFERENCES")
    b.append(refs(_REFS))

    b.append(h3("Về nguồn tài liệu" if vi else "About the source"))
    P(
        "Chương 6 chiếm PDF tr. 123–140, tương ứng tr. 107–124 của bản in; PAGES_SRC = 18 đếm "
        "toàn bộ phân đoạn nguồn này, kể cả trang PDF cuối để trống. Nguyên bản gồm Tóm tắt, "
        "Từ khóa, Giới thiệu, Phát triển gần đây trong bảo vệ và điều khiển hệ thống điện, Bảo "
        "vệ và điều khiển diện rộng/khu vực tích hợp, Kết luận, Đóng góp của tác giả và 17 tài "
        "liệu tham khảo, cùng ba hình (Hình 6.1 – Hình 6.3). Nguyên bản không có bảng và không "
        "có phương trình đánh số.",
        "Chapter 6 occupies PDF pp. 123–140, corresponding to printed pp. 107–124; PAGES_SRC = "
        "18 counts this whole source span, including the blank final PDF page. The source "
        "contains Abstract, Keywords, Introduction, Recent Development in Power System "
        "Protection and Control, Integrated Wide Area/Regional Protection and Control, "
        "Conclusions, Authors' Contributions and 17 references, together with three figures "
        "(Figure 6.1 - Figure 6.3). The source has no tables and no numbered equations.")
    b.append(note(source_notes(lang)))
    b.append(p(
        "<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2019 "
        "Bibliotex; các chương của sách phát hành theo giấy phép Creative Commons.</i>"
        if vi else
        "<i>This is an unofficial translation for study purposes. Original content © 2019 "
        "Bibliotex; the individual chapters are released under Creative Commons.</i>"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
