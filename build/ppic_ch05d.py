# -*- coding: utf-8 -*-
"""Book 9, Chapter 5 (part D) — Results and Discussion introduction, the five
typical uranium/thorium configurations and the channel-level and block-level
separation studies (EN/VI bilingual).

Source: decoded lines 2787-2874 of ``work/ppic_raw.txt`` (PDF pp. 105-109,
printed pp. 89-93). The next section, "Effective Enrichment and Initial
Inventory of U-235" (line 2875 onward, equations (1) and (2)), belongs to
part E, so this module resumes exactly at the boundary used by its sibling
modules: it ends after the caption of Figure 10 and does not split the first
paragraph of that following section. Contains Figures 6-10; table-free and
equation-free. Figures 6-10 are supplied by ``ppicfig5_a`` and
``ppicfig5_b``; neutral bilingual stubs keep section() callable in a partial
build without overwriting any callable the real suppliers have registered.
"""
import ppicfig5 as F
from ppic_ch05_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401

# ------------------------------------------------------- figure stubs
# Short subject-only captions; _mk() prefixes "Hinh 5.N / Figure 5.N" and
# appends the bilingual bottom strip.
_STUBS = {
    6: ("Năm cấu hình điển hình của nhiên liệu urani/thori ở hàm lượng thori 46%",
        "Five typical configurations of uranium/thorium fuels at 46% thorium content",
        "Năm cấu hình khối nhiên liệu dạng lục giác với các compact urani (đỏ) và "
        "thori (xanh) phân bố khác nhau (SBU 1#-SBU 5#).",
        "Five hexagonal fuel-block configurations with uranium (red) and thorium "
        "(blue) compacts arranged differently (SBU 1#-SBU 5#)."),
    7: ("k_eff của năm cấu hình ở hàm lượng thori 46%",
        "k_eff of five configurations at 46% thorium content",
        "Đồ thị k_eff theo EFPD cho năm cấu hình ở độ làm giàu U-235 20% và 80%, "
        "hàm lượng thori 46%.",
        "Plots of k_eff versus EFPD for five configurations at 20% and 80% "
        "U-235 enrichment, 46% thorium content."),
    8: ("k_eff của năm cấu hình ở hàm lượng thori 91%",
        "k_eff of five configurations at 91% thorium content",
        "Đồ thị k_eff theo EFPD cho năm cấu hình ở độ làm giàu U-235 20% và 80%, "
        "hàm lượng thori 91%.",
        "Plots of k_eff versus EFPD for five configurations at 20% and 80% "
        "U-235 enrichment, 91% thorium content."),
    9: ("Cấu hình compact thori/urani cho tách ở cấp kênh",
        "Configurations of thorium/uranium compacts for channel-level separation",
        "Bảy cấu hình khối nhiên liệu dạng lục giác với compact urani (đỏ) và thori "
        "(xanh) ở hàm lượng thori từ 16% đến 91%.",
        "Seven hexagonal fuel-block configurations with uranium (red) and thorium "
        "(blue) compacts at thorium contents from 16% to 91%."),
    10: ("Cấu hình khối nhiên liệu thori/urani cho tách ở cấp khối",
         "Configurations of thorium/uranium fuel blocks for block-level separation",
         "Năm cấu hình tam giác gồm các khối nhiên liệu urani (đỏ), thori (xanh) và "
         "grafite (xám) ở hàm lượng thori từ 20% đến 67%.",
         "Five triangular configurations of uranium (red), thorium (blue) and "
         "graphite (grey) fuel blocks at thorium contents from 20% to 67%."),
}

for _n, (_cvi, _cen, _avi, _aen) in _STUBS.items():
    _name = "fig_f%02d" % _n
    if not hasattr(F, _name):
        from ppicfig5_common import _mk
        _tuple = _mk(_n, [], "Figure 5.%d" % _n, _cvi, _cen, _avi, _aen)
        setattr(F, _name, (lambda _t=_tuple: _t))


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 5."""
    b = []

    # ------------------------------------------------Results and Discussion
    H(b, lang, "KẾT QUẢ VÀ THẢO LUẬN", "RESULTS AND DISCUSSION", level=2)

    P(b, lang,
      "Đối với các lò HTR thực tế với việc nạp nhiên liệu nhiều lô và nhiều "
      "khối, cả các mức tách không gian được định nghĩa trong Phần 2 và kiểu "
      "nạp nhiên liệu đều ảnh hưởng đến hiệu năng của nhiên liệu trong lõi lò, "
      "vì vậy yếu tố sau được loại trừ bằng cách áp dụng lý tưởng chế độ nạp "
      "nhiên liệu một lô theo kiểu cố định, nhằm tập trung vào ảnh hưởng của "
      "sự tách không gian đối với nhiên liệu thori/urani. Dựa trên chế độ nạp "
      "nhiên liệu một lô theo kiểu cố định, như thể hiện trong Hình 3, thori "
      "và urani ở các mức tách không gian khác nhau với cùng khối lượng được "
      "nạp vào cùng một lõi lò về mặt hình học và được thải ra khi k_eff đạt "
      "cùng một giá trị quy định. Sự khác biệt về hiệu năng của lõi lò là do "
      "các mức tách không gian.",
      "For real HTRs with multi-batch refueling and multi-block, both the "
      "spatial separation levels defined in Section 2 and refueling patterns "
      "influence the performance of fuel in the reactor core, so the latter "
      "is excluded by ideally adopting one-batch fixed-pattern refueling mode "
      "in order to focus on the spatial separation effect of the "
      "thorium/uranium fuel. Based on the one-batch fixed-pattern refueling "
      "mode, as shown in Figure 3, thorium and uranium in the different "
      "spatial separation levels with the same mass are loaded into the "
      "geometrically same reactor core and are discharged when the k_eff "
      "reaches the same specified value. The core performance difference is "
      "due to the spatial separation levels.")

    # --------------------------------------------- one separation level
    H(b, lang, "Ảnh hưởng của cấu hình trong một mức tách không gian",
      "Configuration Effects in One Spatial Separation Level", level=3)

    P(b, lang,
      "Để so sánh bốn mức tách không gian khác nhau ở quy mô lõi, chương này "
      "phân tích đơn giản các cấu hình hoặc kiểu bố trí của nhiên liệu "
      "thori/urani trong tách ở cấp kênh và tách ở cấp khối, bởi vì cái trước "
      "có các cấu hình hoặc kiểu bố trí khác nhau ở quy mô khối và cái sau có "
      "ở quy mô lõi, như thể hiện trong Hình 2, và các cấu hình này ảnh hưởng "
      "đến hiệu năng của lõi lò. Đối với hai mức tách còn lại, tức là không "
      "tách và tách ở cấp TRISO, các khối nhiên liệu giống hệt nhau tồn tại "
      "trong toàn bộ lõi lò.",
      "In order to compare four different spatial separation levels in the "
      "core scale, the configurations or patterns of the thorium/uranium "
      "fuels in the channel-level separation and block-level separation are "
      "simply analyzed in this section because the former meets different "
      "configurations or patterns in block scale and the latter does in core "
      "scale, as shown in Figure 2, and the configurations influence the "
      "performance of the reactor core. For the other two separation levels, "
      "that is no separation level and TRISO-level separation, the same fuel "
      "blocks exist in the whole reactor core.")

    # ---------------------------------------------- channel-level separation
    H(b, lang, "Ảnh hưởng của cấu hình không gian trong tách ở cấp kênh",
      "Spatial Configuration Effects in the Channel-Level Separation", level=4)

    P(b, lang,
      "Đối với tách ở cấp kênh, các cấu hình không gian của các compact "
      "thori/urani trong khối nhiên liệu là khác nhau ngay cả khi cùng hàm "
      "lượng thori, bởi vì các compact urani và thori được đặt ở các kênh "
      "khác nhau, tức là về mặt lý thuyết có 2²¹⁰ cấu hình. Gần như không thể "
      "nghiên cứu tất cả chúng, nhưng cũng không cần thiết phải làm vậy vì "
      "hiệu năng có thể tương tự đối với một số cấu hình tương tự, và phép "
      "so sánh ở quy mô lõi lò là mối quan tâm chính. Năm cấu hình điển hình "
      "(SBU 1#-SBU 5#) được chọn và nghiên cứu cho hàm lượng thori 46%, như "
      "thể hiện trong Hình 6. Các compact nhiên liệu urani được đặt lần lượt "
      "ở vùng trung tâm, vùng giữa và vùng ngoài của khối nhiên liệu đối với "
      "SBU 1#-SBU 3#, và được bố trí đều khắp trong khối nhiên liệu đối với "
      "SBU 4# và SBU 5#. Các compact urani tương đối tập trung trong nhóm "
      "cấu hình trước và tương đối phân tán trong nhóm cấu hình sau. Đối với "
      "các hàm lượng thori khác, sự tách không gian của các compact "
      "urani/thori được bố trí theo cách tương tự.",
      "For the channel-level separation, the spatial configurations of "
      "thorium/uranium compacts in the fuel block are different even for the "
      "same thorium content because uranium and thorium compacts are located "
      "in different channels, that is, there are 2²¹⁰ configurations "
      "theoretically. It is almost impossible to investigate all of them, but "
      "it is not necessary to do it because the performance is possibly "
      "similar for some similar configurations, and the comparison in the "
      "reactor core scale is of the main concern. Five typical configurations "
      "(SBU 1#-SBU 5#) are chosen and investigated for 46% of thorium content, "
      "as shown in Figure 6. The uranium fuel compacts are located in the "
      "central, middle, and outer regions of the fuel block, respectively, "
      "for the SBU 1#-SBU 3#, and are evenly located in the fuel block for the "
      "SBU 4# and SBU 5#. The uranium compacts are relatively concentrated in "
      "the former group of configurations and are relatively dispersed in the "
      "latter group of configurations. For other thorium content, the spatial "
      "separation of uranium/thorium compacts are located in the similar mode.")

    FIG(b, 6, F.fig_f06(), lang)

    P(b, lang,
      "Hình 7 và Hình 8 cho thấy k_eff của lõi lò đối với hàm lượng thori 46% "
      "và 91%, được tính toán dựa trên mô hình mô tả trong Phần 2.2. Khi hàm "
      "lượng thori tăng, số lượng compact thori sẽ tăng và số lượng compact "
      "urani sẽ giảm. Để duy trì cùng khối lượng U-235 trong khối nhiên liệu "
      "hoặc trong lõi lò, độ làm giàu của U-235 phải được tăng lên. Đối với "
      "các hàm lượng thori khác nhau, khi độ làm giàu của U-235 nhỏ hơn 20%, "
      "năm cấu hình không gian khác nhau của nhiên liệu thori/urani cho k_eff "
      "tương tự nhau. Tuy nhiên, khi độ làm giàu cao hơn 20%, ví dụ 80%, k_eff "
      "của năm cấu hình khác nhau rõ rệt. Hơn nữa, k_eff của SBU 4# và SBU 5# "
      "luôn cao hơn ba cấu hình còn lại, và ảnh hưởng của các cấu hình không "
      "gian trở nên quan trọng. Trong tách ở cấp kênh, các compact urani phân "
      "tán có lợi cho việc chuyển hóa Th-232 thành U-233 khi hàm lượng thori "
      "và, do đó, độ làm giàu của U-235 cao. Dựa trên các phép tính và phân "
      "tích, các cấu hình không gian được đề xuất của các compact "
      "thori/urani trong khối nhiên liệu đối với tách ở cấp kênh được thể "
      "hiện trong Hình 9. Các compact urani được tập trung ở vùng trung tâm "
      "của khối nhiên liệu đối với hàm lượng thori thấp và được phân tán đối "
      "với hàm lượng thori cao.",
      "Figures 7 and 8 show the k_eff of the reactor core for 46 and 91% "
      "thorium contents, which are calculated based on the model described in "
      "Section 2.2. When the thorium content increases, the number of thorium "
      "compacts will increase and the number of uranium compacts will "
      "decrease. In order to maintain the same mass of U-235 in the fuel block "
      "or in the reactor core, the enrichment of U-235 has to be increased. "
      "For different thorium contents, when the enrichment of U-235 is less "
      "than 20%, the five different spatial configurations of thorium/uranium "
      "fuels achieve the similar k_eff. However, when the enrichment is higher "
      "than 20%, for example 80%, the k_eff of the five configurations is "
      "different obviously. Moreover, the k_eff of the SBU 4# and SBU 5# is "
      "always higher than the other three configurations, and the influence "
      "of the spatial configurations becomes important. In the channel-level "
      "separation, the dispersed uranium compacts are advantageous to "
      "transmute Th-232 to U-233 when the thorium content and, thus, the "
      "enrichment of U-235 are high. Based on the calculations and analysis, "
      "the suggested spatial configurations of thorium/uranium compacts in "
      "the fuel block are shown in Figure 9 for the channel-level separation. "
      "The uranium compacts are concentrated in the central region of the "
      "fuel block for low thorium content and are dispersed for high thorium "
      "content.")

    FIG(b, 7, F.fig_f07(), lang)
    FIG(b, 8, F.fig_f08(), lang)
    FIG(b, 9, F.fig_f09(), lang)

    # ----------------------------------------------- block-level separation
    H(b, lang, "Ảnh hưởng của cấu hình không gian trong tách ở cấp khối",
      "Spatial Configuration Effects in Block-Level Separation", level=4)

    P(b, lang,
      "Đối với tách ở cấp khối, các cấu hình không gian của các khối nhiên "
      "liệu thori/urani trong lõi lò gặp phải vấn đề tương tự như tách ở cấp "
      "kênh. Các khối nhiên liệu urani và thori được đặt ở những vị trí khác "
      "nhau trong lõi lò dẫn đến các cấu hình khác nhau, tức là về mặt lý "
      "thuyết có 2¹⁹⁸ cấu hình của các khối nhiên liệu. Dựa trên phương pháp "
      "phân tích tương tự như trình bày trong Phần 3.1.1, năm cấu hình điển "
      "hình (WASB 1#-WASB 5#) đã được chọn và nghiên cứu cho các hàm lượng "
      "thori khác nhau. Kết quả cho thấy các khối nhiên liệu thori phân tán "
      "có lợi cho việc chuyển hóa Th-232 thành U-233 trong tách ở cấp khối. "
      "Dựa trên kết quả, các cấu hình không gian được đề xuất của các khối "
      "nhiên liệu thori/urani trong lõi lò đối với tách ở cấp khối được thể "
      "hiện trong Hình 10, được chọn để so sánh với ba mức tách còn lại.",
      "For the block-level separation, the spatial configurations of "
      "thorium/uranium fuel blocks in the reactor core meet the same problem "
      "as the channel-level separation. The uranium and thorium fuel blocks "
      "located in different positions in the reactor core lead to different "
      "configurations, that is, there are 2¹⁹⁸ configurations of the fuel "
      "blocks theoretically. Based on the same analysis method as presented "
      "in Section 3.1.1, every five typical configurations (WASB 1#-WASB 5#) "
      "were chosen and investigated for different thorium content. The "
      "results show that the dispersed thorium fuel blocks are advantageous "
      "to transmute Th-232 to U-233 in the block-level separation. Based on "
      "the results, the suggested spatial configurations of thorium/uranium "
      "fuel blocks in the reactor core are shown in Figure 10 for the "
      "block-level separation, which is chosen to be compared with other "
      "three separation levels.")

    FIG(b, 10, F.fig_f10(), lang)

    return b
