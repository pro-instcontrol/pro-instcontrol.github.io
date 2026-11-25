# -*- coding: utf-8 -*-
"""Book 9, Chapter 5 (part E) — effective enrichment and initial inventory of
U-235, initial effective multiplication factor and average conversion ratio,
and the further discussion that introduces the four control groups (EN/VI).

Source: decoded lines 2875-2989 of ``work/ppic_raw.txt`` (PDF pp. 109-114,
printed pp. 93-98). Part D ends after the caption of Figure 10, so this module
resumes with the heading "Effective Enrichment and Initial Inventory of
U-235" at line 2875 and does not split its first paragraph. It contains
Figures 11-14, Table 5.4 (printed as Table 4) and equations (1) and (2).
Every printed number in Table 5.4 is transcribed from p114.png / p115.png;
equations (1) and (2) are transcribed from p110.png. Equation (3), which the
printed text places after Table 5.4, belongs to part F together with Table 5.5.
Figures 11-14 are supplied by ``ppicfig5_b`` and ``ppicfig5_c``; neutral
bilingual stubs keep section() callable in a partial build without overwriting
any callable the real suppliers have registered.
"""
import ppicfig5 as F
from ppic_ch05_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401

# ------------------------------------------------------- figure stubs
# Short subject-only captions; _mk() prefixes "Hinh 5.N / Figure 5.N" and
# appends the bilingual bottom strip.
_STUBS = {
    11: ("Độ làm giàu hiệu dụng ban đầu của U-235 theo hàm lượng thori cho các mức tách khác nhau",
         "Initial effective enrichment of U-235 as a function of thorium content for different separation levels",
         "Đồ thị đường ε_eff ban đầu theo hàm lượng thori từ 0 đến 100% cho Th/U MOX, SBT, SBU và WASB.",
         "Plot of initial ε_eff versus thorium content from 0 to 100% for Th/U MOX, SBT, SBU and WASB."),
    12: ("Tồn kho ban đầu của kim loại nặng theo hàm lượng thori cho các mức tách khác nhau",
         "Initial inventory of heavy metal as a function of thorium content for different separation levels",
         "Đồ thị tồn kho ban đầu của urani làm giàu và của kim loại nặng theo hàm lượng thori cho bốn mức tách.",
         "Plot of initial enriched-uranium and heavy-metal inventories versus thorium content for four separation levels."),
    13: ("Tồn kho ban đầu của U-235 theo hàm lượng thori cho các mức tách khác nhau",
         "Initial inventory of U-235 as a function of thorium content for different separation levels",
         "Đồ thị tồn kho U-235 ban đầu theo hàm lượng thori cho Th/U MOX, SBT, SBU và WASB.",
         "Plot of initial U-235 inventory versus thorium content for Th/U MOX, SBT, SBU and WASB."),
    14: ("k_eff ban đầu và tỷ lệ chuyển đổi trung bình của các mức tách không gian khác nhau",
         "Initial k_eff and average conversion ratio of different spatial separation levels",
         "Hai đồ thị: k_eff ban đầu và tỷ lệ chuyển đổi trung bình theo hàm lượng thori cho bốn mức tách không gian.",
         "Two plots: initial k_eff and average conversion ratio versus thorium content for four spatial separation levels."),
}

for _n, (_cvi, _cen, _avi, _aen) in _STUBS.items():
    _name = "fig_f%02d" % _n
    if not hasattr(F, _name):
        from ppicfig5_common import _mk
        _tuple = _mk(_n, [], "Figure 5.%d" % _n, _cvi, _cen, _avi, _aen)
        setattr(F, _name, (lambda _t=_tuple: _t))

# ------------------------------------------------------------- Table 5.4
# Printed Table 4: five factors and initial k_eff of the four control-group
# cores. Numeric rows are language-neutral; only the heads are localized.
_T54_HEAD_VI = ["Lò phản ứng", "ηf", "ε", "p", "P_NL", "k_eff"]
_T54_HEAD_EN = ["Reactor core", "ηf", "ε", "p", "P_NL", "k_eff"]
_T54_ROWS = [
    ["Th/U MOX-0%Th",  "1.7257", "1.0804", "0.6994", "0.9550", "1.24531"],
    ["Th/U MOX-30%Th", "1.6891", "1.0861", "0.6852", "0.9551", "1.20058"],
    ["Th/U MOX-80%Th", "1.5540", "1.0701", "0.7379", "0.9570", "1.17436"],
    ["Th/U MOX-50%Th", "1.6491", "1.0830", "0.6935", "0.9556", "1.18358"],
    ["SBU-50%Th",      "1.5690", "1.0687", "0.7508", "0.9567", "1.20442"],
    ["WASB-50%Th",     "1.5182", "1.0734", "0.7567", "0.9615", "1.18567"],
]


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 5."""
    b = []

    # ------------------------ effective enrichment and U-235 inventory
    H(b, lang, "Độ làm giàu hiệu dụng và tồn kho ban đầu của U-235",
      "Effective Enrichment and Initial Inventory of U-235", level=3)

    P(b, lang,
      "Như đã đề cập trong Phần 3.1, có thể phải sử dụng U-235 làm giàu cao "
      "khi hàm lượng thori tăng. So với lò chạy nhiên liệu thori/urani, lò "
      "chạy nhiên liệu urani chỉ chứa một đồng vị phân hạch, đó là U-235, "
      "và một đồng vị sinh sản, đó là U-238, trong nhiên liệu. Phần khối "
      "lượng của đồng vị phân hạch, tức là U-235, được gọi là độ làm giàu "
      "của U-235, như được định nghĩa trong Phương trình (1).",
      "As mentioned in Section 3.1, the highly enriched U-235 possibly has "
      "to be used when the thorium content increases. Compared with a "
      "thorium/uranium-fueled reactor, a uranium-fueled reactor only contains "
      "one fissile isotope, that is, U-235, and one fertile isotope, that is, "
      "U-238, in the fuel. The mass fraction of fissile isotopes, that is, "
      "U-235, is the so-called enrichment of U-235, as defined in Eq. (1).")

    E(b, lang, "ε = m_U5 / (m_U5 + m_U8)", "ε = m_U5 / (m_U5 + m_U8)", num="1")

    P(b, lang,
      "Khi một đồng vị sinh sản khác, đó là Th-232, xuất hiện trong nhiên "
      "liệu lò thì phần khối lượng của các đồng vị phân hạch, như được định "
      "nghĩa trong Phương trình (2), khác với độ làm giàu truyền thống của "
      "U-235 và được gọi là độ làm giàu hiệu dụng của U-235 [19].",
      "When another fertile isotope, that is, Th-232, appears in the reactor "
      "fuel, the mass fraction of fissile isotopes, as defined in Eq. (2), is "
      "different from the traditional enrichment of U-235, which is called "
      "the effective enrichment of U-235 [19].")

    E(b, lang, "ε_eff = m_U5 / (m_U5 + m_U8 + m_Th2)",
      "ε_eff = m_U5 / (m_U5 + m_U8 + m_Th2)", num="2")

    P(b, lang,
      "Nếu áp dụng khái niệm độ làm giàu hiệu dụng của U-235 thì phần khối "
      "lượng danh nghĩa của các đồng vị phân hạch đối với lò HTR chạy nhiên "
      "liệu thori thấp hơn nhiều so với 20%, như thể hiện trong Hình 11; đây "
      "là giới hạn làm giàu của U-235 đối với nhiên liệu làm giàu thấp. Vì "
      "trong lò có nạp thori, độ làm giàu của U-235 không còn bằng độ làm "
      "giàu hiệu dụng của U-235 và ý nghĩa vật lý của cái sau rõ ràng hơn, "
      "nên cái sau được phân tích thay vì cái trước.",
      "If the concept of the effective enrichment of U-235 is adopted, the "
      "nominal mass fraction of fissile isotopes is far less than 20% for the "
      "thorium-fueled HTRs, as shown in Figure 11, which is the limit "
      "enrichment of U-235 for low-enriched fuel. Since the enrichment of "
      "U-235 is no longer equal to the effective enrichment of U-235 in a "
      "thorium-loaded reactor, and the physical meaning of the latter is "
      "clearer, the latter is analyzed instead of the former.")

    FIG(b, 11, F.fig_f11(), lang)

    P(b, lang,
      "Như thể hiện trong Hình 11, đối với cùng chiều dài chu kỳ nạp nhiên "
      "liệu 2 năm, độ làm giàu hiệu dụng ban đầu cần thiết của U-235 giảm rõ "
      "rệt khi mức tách tăng từ Th/U MOX đến SBU và WASB, khi hàm lượng thori "
      "thay đổi từ 10% đến 80%. Khi hàm lượng thori nhỏ hơn 10% hoặc lớn hơn "
      "80%, ảnh hưởng của mức tách không gian đến ε_eff ban đầu là yếu vì "
      "nhiên liệu gần như là urani hoặc thori, do đó không có sự khác biệt "
      "rõ ràng. Hơn nữa, ε_eff ban đầu của SBU gần như giống với của WASB khi "
      "hàm lượng thori nằm trong khoảng 20-70%. Đối với nhiên liệu Th/U MOX, "
      "ε_eff ban đầu tăng khi hàm lượng thori tăng từ 0 đến 30% và giảm khi "
      "thori tiếp tục tăng. Đối với SBT, SBU và WASB, ε_eff ban đầu giảm khi "
      "hàm lượng thori tăng.",
      "As shown in Figure 11, the required initial effective enrichment of "
      "U-235 obviously decreases with the increase of separation level from "
      "Th/U MOX to SBU and WASB for the same 2-year refueling cycle length, "
      "when the thorium content changes from 10 to 80%. When the thorium "
      "content is less than 10% or larger than 80%, the influence of spatial "
      "separation level on the initial ε_eff is weak because the fuel is "
      "nearly uranium or thorium and thus there is no obvious difference. "
      "Moreover, the initial ε_eff of SBU is nearly the same as that of WASB "
      "when the thorium content is in the range of 20-70%. For the Th/U MOX "
      "fuel, the initial ε_eff increases when the thorium content increases "
      "from 0 to 30% and decreases with the further increase of thorium. For "
      "the SBT, SBU, and WASB, the initial ε_eff decreases with the increase "
      "of the thorium content.")

    P(b, lang,
      "Mặc dù tồn kho ban đầu tổng của kim loại nặng giảm nhẹ do sự khác biệt "
      "về mật độ giữa ThO2 (9,4 g/cm³) và UO2 (10,4 g/cm³), như thể hiện "
      "trong Hình 12, nhưng tồn kho ban đầu cần thiết của U-235, như thể hiện "
      "trong Hình 13, có xu hướng gần như giống với độ làm giàu hiệu dụng ban "
      "đầu của U-235 theo Phương trình (2). Hơn nữa, tồn kho ban đầu của "
      "urani làm giàu cũng giảm khi hàm lượng thori tăng, như thể hiện trong "
      "Hình 12, vì ngày càng nhiều U-238 bị thay thế bằng Th-232 trong lõi "
      "lò. Sự thay đổi của tồn kho ban đầu của U-235 hoặc của độ làm giàu "
      "hiệu dụng ban đầu của U-235 là kết quả của sự khác biệt về hiệu năng "
      "hạt nhân (ví dụ hệ số nhân hiệu dụng ban đầu và tỷ lệ chuyển đổi "
      "trung bình) do các mức tách không gian gây ra, như được thảo luận thêm "
      "trong Phần 3.3.",
      "Although the total initial inventory of heavy metal slightly decreases "
      "because of the density difference between ThO2 (9.4 g/cm3) and UO2 "
      "(10.4 g/cm3), as shown in Figure 12, the required initial inventory of "
      "U-235, as shown in Figure 13, nearly has the same trend as the initial "
      "effective enrichment of U-235, according to Eq. (2). Furthermore, the "
      "initial inventory of the enriched uranium also decreases with the "
      "increase of the thorium content, as shown in Figure 12, because more "
      "and more U-238 is replaced by Th-232 in the reactor core. The change "
      "of the initial inventory of U-235 or the initial effective enrichment "
      "of U-235 is a result of the difference of nuclear performance (e.g., "
      "initial effective multiplication factor and average conversion ratio) "
      "caused by the spatial separation levels, as further discussed in "
      "Section 3.3.")

    FIG(b, 12, F.fig_f12(), lang)
    FIG(b, 13, F.fig_f13(), lang)

    # --------------- initial effective multiplication factor and ACR
    H(b, lang, "Hệ số nhân hiệu dụng ban đầu và tỷ lệ chuyển đổi trung bình",
      "Initial Effective Multiplication Factor and Average Conversion Ratio",
      level=3)

    P(b, lang,
      "Hình 14 trình bày hệ số nhân hiệu dụng ban đầu (k_eff) và tỷ lệ "
      "chuyển đổi trung bình (ACR) của bốn mức tách không gian theo hàm lượng "
      "thori. Đối với mỗi mức tách không gian, k_eff gần như giảm khi hàm "
      "lượng thori tăng. Ở cùng hàm lượng thori, k_eff ban đầu thường tăng "
      "khi mức tách không gian tăng từ Th/U MOX đến SBU. Khi hàm lượng thori "
      "lớn hơn 80%, sự khác biệt giữa các mức trở nên nhỏ. Quy luật đáng chú "
      "ý hơn là xu hướng của ACR luôn ngược với k_eff ban đầu, tức là khi "
      "ACR cao hơn thì k_eff ban đầu thấp hơn, ngay cả đối với mức WASB.",
      "Figure 14 presents the initial effective multiplication factors "
      "(k_eff) and average conversion ratios (ACRs) of four spatial "
      "separation levels as a function of thorium content. For each spatial "
      "separation level, the k_eff nearly decreases with the increase of "
      "thorium content. For the same thorium content, the initial k_eff "
      "usually increases when the spatial separation level increases from "
      "Th/U MOX to SBU. When the thorium content is larger than 80%, the "
      "difference among them becomes small. The more interesting rule is "
      "that the trend of ACR is always opposite to the initial k_eff, that "
      "is, when the ACR is higher, initial k_eff is smaller, even for the "
      "WASB level.")

    FIG(b, 14, F.fig_f14(), lang)

    P(b, lang,
      "Nếu so sánh Hình 14 với Hình 11 hoặc Hình 13, có thể thấy thú vị là "
      "khi mức tách không gian của nhiên liệu thori/urani thay đổi từ SBU "
      "sang Th/U MOX, tồn kho ban đầu cần thiết của U-235 là lớn nhất đối "
      "với Th/U MOX để đạt được cùng thời gian vận hành, nhưng k_eff ban đầu "
      "lại nhỏ nhất và lợi ích chính là lượng Th-232 chuyển hóa thành U-233 "
      "lớn nhất. Khi mức tách không gian của nhiên liệu thori/urani thay đổi "
      "từ SBU sang WASB, tồn kho ban đầu cần thiết của U-235 giảm. Hơn nữa, "
      "ACR tăng khi hàm lượng thori tăng, k_eff ban đầu giảm, do đó độ giảm "
      "hoặc độ dao động của độ phản ứng trong chiều dài chu kỳ nạp nhiên "
      "liệu cũng giảm.",
      "If Figure 14 is compared with Figure 11 or Figure 13, it is "
      "interesting to find that when the spatial separation level of "
      "thorium/uranium fuels changes from SBU to Th/U MOX, the required "
      "initial inventory of U-235 is the most for the Th/U MOX in order to "
      "achieve the same operation time, but the initial k_eff is smallest "
      "and the main benefit is the most amount of Th-232 transmuted into "
      "U-233. Once the spatial separation of thorium/uranium fuels changes "
      "from SBU to WASB, the required initial inventory of U-235 decreases. "
      "Moreover, the ACR increases with increase of thorium content, the "
      "initial k_eff decreases, and thus the reactivity drop or swing "
      "decreases in the refueling length.")

    # --------------------------- further discussion / four control groups
    H(b, lang, "Thảo luận thêm về hệ số nhân hiệu dụng ban đầu",
      "Further Discussion of Initial Effective Multiplication Factor", level=3)

    P(b, lang,
      "Để phân tích ảnh hưởng của các mức tách không gian và hàm lượng thori "
      "đến k_eff ban đầu và do đó đến tồn kho ban đầu của U-235, bốn nhóm đối "
      "chứng gồm các lõi lò điển hình với các mức tách không gian và hàm "
      "lượng thori khác nhau đã được tính toán và thảo luận. Nhóm 1 so sánh "
      "Th/U MOX với SBU ở hàm lượng thori 50% nhằm giải thích lý do tồn kho "
      "ban đầu của U-235 giảm. Nhóm 2 so sánh SBU với WASB ở hàm lượng thori "
      "50% nhằm giải thích sự khác biệt giữa chúng. Các nhóm 3 và 4 thảo "
      "luận về Th/U MOX với hàm lượng thori 0%, 30% và 80%, tương ứng, nhằm "
      "giải thích ảnh hưởng của hàm lượng thori.",
      "In order to analyze the influence of spatial separation levels and "
      "thorium content on the initial k_eff and thus the initial inventory of "
      "U-235, four control groups of typical reactor cores including spatial "
      "separation levels and thorium content are calculated and discussed. "
      "The group 1 is to compare the Th/U MOX with SBU with 50% thorium "
      "content, in order to explain the reason of the decrease of the initial "
      "inventory of U-235. The group 2 is to compare the SBU and WASB with "
      "50% thorium content, in order to explain the difference between them. "
      "The groups 3 and 4 are to discuss the Th/U MOX with 0, 30, and 80% "
      "thorium content, respectively, in order to explain the influence of "
      "the thorium content.")

    P(b, lang,
      "Bảng 5.4 trình bày năm hệ số và k_eff ban đầu của các lõi lò thuộc "
      "bốn nhóm đối chứng, được tính toán theo phương pháp đã được kiểm "
      "chứng [10].",
      "Table 5.4 presents the five factors and initial k_eff of the reactor "
      "cores involved in the four control groups, which are calculated "
      "according to the validated method [10].")

    TBL(b, lang, _T54_HEAD_VI, _T54_HEAD_EN, _T54_ROWS,
        caption_vi="Bảng 5.4 — Năm hệ số và k_eff ban đầu của các lõi lò khác nhau trong bốn nhóm đối chứng",
        caption_en="Table 5.4 — Five factors and initial k_eff of different reactor cores involved in four control groups")

    return b
