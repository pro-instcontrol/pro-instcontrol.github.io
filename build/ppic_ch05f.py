# -*- coding: utf-8 -*-
"""Book 9, Chapter 5 (part F) — further discussion of the initial effective
multiplication factor, five-factor contribution analysis, and fuel cycle cost
results (EN/VI).

Source: decoded lines 2990-3115 of ``work/ppic_raw.txt`` (PDF pp. 115-119,
printed pp. 99-103). This module resumes after Table 5.4 of part E with the
lead-in to Eq. (3), carries the four control-group discussion and Table 5.5,
and closes with the fuel cycle cost analysis. Equations (3)-(5) and every
number and percentage in Table 5.5 are transcribed from p115.png / p116.png;
Figures 16 and 17 are read from p118.png and Figure 15 from p113.png.
Figures 15-17 are supplied by ``ppicfig5_c``; neutral bilingual stubs keep
section() callable in a partial build without overwriting any callable the
real supplier has registered.
"""
import ppicfig5 as F
from ppic_ch05_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401

# ------------------------------------------------------- figure stubs
# Short subject-only captions; _mk() prefixes "Figure 5.N" / "Hinh 5.N" and
# appends the bilingual bottom strip.
_STUBS = {
    15: ("k_eff theo EFPD cho các tỷ lệ chuyển đổi trung bình khác nhau",
         "k_eff versus EFPD for different average conversion ratios",
         "Đồ thị k_eff theo EFPD cho ACR 0.582 và 0.535 với điểm cuối chu kỳ B (657, 1.005).",
         "Plot of k_eff versus EFPD for ACR 0.582 and 0.535 with end-of-cycle point B (657, 1.005)."),
    16: ("Chi phí chu kỳ nhiên liệu của các mức tách không gian khác nhau",
         "Fuel cycle cost of different spatial separation levels",
         "Đồ thị chi phí chu kỳ nhiên liệu theo hàm lượng thori cho Th/U MOX, SBT, SBU và WASB.",
         "Plot of fuel cycle cost versus thorium content for Th/U MOX, SBT, SBU and WASB."),
    17: ("Thành phần chi phí chu kỳ nhiên liệu của một số lõi lò điển hình",
         "Composition of fuel cycle cost for some typical reactor cores",
         "Ba biểu đồ tròn về thành phần chi phí cho Th/U MOX 50% thori, SBT 90% thori và WASB 90% thori.",
         "Three pie charts of cost composition for Th/U MOX with 50% thorium, SBT with 90% thorium and WASB with 90% thorium."),
}

for _n, (_cvi, _cen, _avi, _aen) in _STUBS.items():
    _name = "fig_f%02d" % _n
    if not hasattr(F, _name):
        from ppicfig5_common import _mk
        _tuple = _mk(_n, [], "Figure 5.%d" % _n, _cvi, _cen, _avi, _aen)
        setattr(F, _name, (lambda _t=_tuple: _t))

# ------------------------------------------------------------- Table 5.5
# Printed Table 5: factor contributions in pcm and the printed percentages
# in parentheses. Numeric rows are language-neutral; only heads are localized.
_T55_HEAD_VI = ["Số nhóm", "Nhóm", "Δηf [pcm]", "Δε [pcm]", "Δp [pcm]",
                "ΔP_NL [pcm]", "Δk_eff [pcm]"]
_T55_HEAD_EN = ["Group number", "Group", "Δηf [pcm]", "Δε [pcm]", "Δp [pcm]",
                "ΔP_NL [pcm]", "Δk_eff [pcm]"]
_T55_ROWS = [
    ["1", "Th/U MOX-50%Th", "−4167", "−1112", "+6649", "+96", "+1460"],
    ["", "SBU-50%Th", "(−285%)", "(−76%)", "(+455%)", "(+6%)", "(+100%)"],
    ["2", "SBU-50%Th", "−2754", "+367", "+655", "+419", "−1313"],
    ["", "WASB-50%Th", "(−210%)", "(+28%)", "(+50%)", "(+32%)", "(−100%)"],
    ["3", "MOX-0%Th", "−1753", "+430", "−1677", "+9", "−2992"],
    ["", "MOX-30%Th", "(−59%)", "(+14%)", "(−56%)", "(+1%)", "(−100%)"],
    ["4", "MOX-30%Th", "−7017", "−1250", "+6236", "+171", "−1857"],
    ["", "MOX-80%Th", "(−378%)", "(−67%)", "(+336%)", "(+9%)", "(−100%)"],
]


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 5."""
    b = []

    # --------------------------- continuation of the initial k_eff discussion
    P(b, lang,
      "Hình 15 trình bày k_eff như một hàm của thời gian vận hành trong một "
      "chu kỳ nạp nhiên liệu đối với hai tỷ lệ chuyển đổi trung bình (ACR) "
      "khác nhau. Trong các phép tính này, chiều dài chu kỳ nạp nhiên liệu là "
      "657 ngày công suất đầy đủ hiệu dụng (EFPD), nghĩa là tọa độ điểm cuối "
      "chu kỳ (EOC) được cố định, tại điểm B (657, 1.005) trong Hình 15. Mặt "
      "khác, k_eff là hàm gần tuyến tính của độ cháy đối với lò HTR chạy "
      "nhiên liệu thori như thể hiện trong Hình 15. Do đó, nếu ACR của chu kỳ "
      "nạp nhiên liệu nhỏ hơn thì độ giảm của độ phản ứng lớn hơn, và vì thế "
      "k_eff ban đầu phải cao hơn để đảm bảo lò đạt tới hạn tại EOC.",
      "Figure 15 presents the k_eff as a function of operation time for two "
      "different ACRs in one refueling cycle. In these calculations, the "
      "refueling cycle length is 657 effective full power days (EFPDs), which "
      "means the coordinate of end of cycle (EOC) is fixed, as the point B "
      "(657, 1.005) in Figure 15. On the other hand, the k_eff is a nearly "
      "linear function of burnup for the thorium-fueled HTR as shown in "
      "Figure 15. Therefore, if the average conversion ratio of the refueling "
      "cycle is smaller, the reactivity drop is larger and thus the initial "
      "k_eff must be higher to guarantee a critical reactor at EOC.")

    FIG(b, 15, F.fig_f15(), lang)

    P(b, lang,
      "Công thức năm hệ số [20] có thể được viết như sau:",
      "The five-factor formula [20] can be written as:")

    E(b, lang, "k_eff = η f p ε P_NL", "k_eff = η f p ε P_NL", num="3")

    P(b, lang,
      "Trong đó η, f, p, ε và P_NL lần lượt là hệ số sinh sản, hệ số sử dụng "
      "nhiên liệu, xác suất thoát cộng hưởng, hệ số phân hạch nhanh và xác "
      "suất không rò rỉ. Tuy nhiên, trong phép tính vật lý lõi được mô tả "
      "trong Phần 2.2.1, sự đồng nhất hóa bảng nhiên liệu sẽ trộn nhiên liệu, "
      "chất làm chậm và chất làm mát thành một hỗn hợp, làm cho η và f không "
      "thể tách rời. Vì vậy, tích của η và f được xem là hệ số sinh sản của "
      "lõi. Thông tin thêm về công thức năm hệ số có thể tìm thấy trong Tài "
      "liệu tham khảo [10].",
      "where η, f, p, ε, P_NL are, respectively, the reproduction factor, "
      "fuel utilization factor, resonance escape probability, fast fission "
      "factor, and nonleakage probability. However, in the core physics "
      "calculation described in Section 2.2.1, the homogenization of fuel "
      "block will mix the fuel, moderator, and coolant into a mixture, making "
      "the η and f inseparable. Thus, the production of η and f is regarded "
      "as the reproduction factor of the core. More information about the "
      "five-factor formula can be found in Ref. [10].")

    P(b, lang,
      "Để mô tả định lượng đóng góp của từng hệ số vào sự thay đổi của hệ số "
      "nhân hiệu dụng ban đầu, đóng góp [21] được định nghĩa dựa trên các "
      "thành phần của công thức năm hệ số:",
      "To quantitatively describe the contribution of each factor to the "
      "variation of the initial effective multiplication factor, its "
      "contribution [21] is defined in terms of the components of five-factor "
      "formula")

    E(b, lang,
      "Δr = (1/(r̄₁/k̄₁) − 1/(r̄₂/k̄₂)) · 10⁵,  r = η_f, ε, p, P_NL",
      "Δr = (1/(r̄₁/k̄₁) − 1/(r̄₂/k̄₂)) · 10⁵,  r = η_f, ε, p, P_NL", num="4")

    P(b, lang, "Trong đó", "where")

    E(b, lang, "r̄ = 0.5(r₁ + r₂), k̄ = η̄_f ε̄ p̄ P̄_NL",
      "r̄ = 0.5(r₁ + r₂), k̄ = η̄_f ε̄ p̄ P̄_NL", num="5")

    P(b, lang,
      "Các chỉ số 1 và 2 lần lượt biểu thị hai trường hợp khác nhau. Bảng 5.5 "
      "trình bày đóng góp của từng hệ số cho bốn nhóm đối chứng.",
      "The subscripts 1 and 2 represent two different cases, respectively. "
      "Table 5 presents the contribution of each factor for the four control "
      "groups.")

    TBL(b, lang, _T55_HEAD_VI, _T55_HEAD_EN, _T55_ROWS,
        caption_vi="Bảng 5.5 — Đóng góp của từng hệ số vào sự thay đổi của k_eff ban đầu",
        caption_en="Table 5.5 — Contribution of each factor to variation of initial k_eff")

    P(b, lang,
      "Đối với nhóm 1, khi hàm lượng thori là 50% và mức tách không gian thay "
      "đổi từ mức Th/U MOX sang mức SBU, xác suất không rò rỉ tăng thêm 96 pcm "
      "và đóng góp +6% vào k_eff ban đầu, vì mức tách không gian tăng cường sự "
      "hấp thụ thori và tiết diện hấp thụ vi mô của Th-232 (7.4 barns) lớn gấp "
      "ba lần của U-238 (2.7 barns). Theo lý do tương tự, nhiều neutron nhiệt "
      "hơn bị Th-232 hấp thụ nhưng không gây được phản ứng phân hạch, dẫn đến "
      "hệ số sinh sản của lõi (ηf) giảm 4167 pcm và đóng góp −285% vào k_eff "
      "ban đầu. Tiết diện phân hạch nhanh của Th-232 (0.01 barns) nhỏ hơn của "
      "U-238 (0.04 barns), làm cho hệ số phân hạch nhanh (ε) giảm 1112 pcm và "
      "đóng góp −76%. Tuy nhiên, vì nhiên liệu thori được gom trong các bảng "
      "thori đối với SBU-50%Th và tích phân cộng hưởng (RI) của Th-232 (85) "
      "nhỏ hơn của U-238 (275), xác suất thoát cộng hưởng (p) của SBU-50%Th "
      "tăng thêm 6649 pcm và đóng góp +455%. Kết quả của tất cả các hiệu ứng, "
      "đặc biệt là đóng góp của sự tăng p, k_eff ban đầu của SBU-50%Th lớn hơn "
      "1460 pcm so với Th/U MOX-50%Th. Hiệu ứng tự che chắn không gian được "
      "tăng cường bởi Th-232 và các mức tách không gian, do đó sự tăng xác "
      "suất thoát cộng hưởng dẫn đến sự giảm 188 kg tồn kho ban đầu của U-235.",
      "For the group 1, when the thorium content is 50% and spatial separation "
      "level changes from Th/U MOX level to SBU level, the nonleakage "
      "probability increases by 96 pcm and contributes +6% to the initial "
      "k_eff, because the spatial separation level strengthens thorium "
      "absorption, and the microscopic absorption cross section of Th-232 "
      "(7.4 barns) is three times of U-238 (2.7 barns). Based on the same "
      "reason, more thermal neutrons are absorbed by Th-232 but cannot induce "
      "fission reactions, which leads to the reproduction factor of core (ηf) "
      "to decrease by 4167 pcm and contributes −285% to the initial k_eff. "
      "The fast fission cross-section of Th-232 (0.01 barns) is smaller than "
      "that of U-238 (0.04 barns), which causes the fast fission factor (ε) "
      "to decrease by 1112 pcm and contribute −76%. However, because the "
      "thorium fuel is lumped in the thorium compacts for the SBU-50%Th and a "
      "smaller resonance integral (RI) of Th-232 (85) compared to U-238's "
      "(275), the resonance escape probability (p) of the SBU-50%Th increases "
      "by 6649 pcm and contributes +455%. As a result of all effects, "
      "especially the contribution of the increase of p, the initial k_eff of "
      "the SBU-50%Th is 1460 pcm larger than that of the Th/U MOX-50%Th. The "
      "spatial self-shielding effect is strengthened by Th-232 and spatial "
      "separation levels, and thus the increase of resonance escape "
      "probability leads to the decrease of 188 kg initial inventory of "
      "U-235.")

    P(b, lang,
      "Đối với nhóm 2, khi mức tách không gian tăng từ mức SBU sang mức WASB, "
      "mặc dù xác suất thoát cộng hưởng tăng thêm 655 pcm, hệ số sinh sản lại "
      "giảm 2754 pcm do sự gom nhóm nhiên liệu thori xa hơn. Kết quả là k_eff "
      "ban đầu giảm 1313 pcm, gây ra độ dao động độ phản ứng nhỏ hơn trong "
      "chu kỳ nạp nhiên liệu. Hơn nữa, tồn kho ban đầu của U-235 giảm 6 kg vì "
      "ACR lớn hơn.",
      "For the group 2, when the spatial separation increases from SBU level "
      "to WASB level, although the resonance escape probability further "
      "increases by 655 pcm, the reproduction factor decreases by 2754 pcm "
      "because of the further lumping of the thorium fuel. As a result, the "
      "initial k_eff decreases by 1313 pcm causing a smaller reactivity swing "
      "in the refueling period. Moreover, the initial inventory of U-235 "
      "decreases 6 kg because of a larger ACR.")

    P(b, lang,
      "Đối với nhóm 3, ở cùng một mức tách không gian, ví dụ mức Th/U MOX, khi "
      "hàm lượng thori tăng từ 0 đến 30%, nhiều neutron nhiệt hơn do phân "
      "hạch sinh ra bị Th-232 sinh sản hấp thụ vì tiết diện hấp thụ vi mô của "
      "Th-232 lớn gấp ba lần, dẫn đến hệ số sinh sản giảm 1753 pcm. Hơn nữa, "
      "do phổ neutron cứng hơn, xác suất thoát cộng hưởng giảm 1677 pcm. Kết "
      "quả là k_eff ban đầu giảm 2992 pcm và tồn kho ban đầu cần thiết của "
      "U-235 tăng thêm 77.8 kg. Nếu hàm lượng thori tiếp tục tăng từ 30 đến "
      "80%, như trong nhóm 4, một lượng lớn U-238 bị thay thế bằng Th-232 "
      "trong lõi lò. Vì tích phân cộng hưởng của Th-232 (85) nhỏ hơn của U-238 "
      "(275), xác suất thoát cộng hưởng (p) tăng 6236 pcm và đóng góp +336%, "
      "nhưng hệ số sinh sản giảm 7017 pcm và đóng góp −378%. Kết quả là k_eff "
      "ban đầu giảm 1857 pcm. Hơn nữa, tồn kho ban đầu cần thiết của U-235 "
      "giảm 206 kg vì ACR lớn hơn.",
      "For the group 3, for a fixed spatial separation level, for example, "
      "Th/U MOX level, when the thorium content increases from 0 to 30%, more "
      "thermal neutrons generated by fission are absorbed by fertile Th-232 "
      "because of three-time microscopic absorption cross section of Th-232, "
      "which leads to the decrease of the reproduction factor by 1753 pcm. "
      "Moreover, because of harder neutron spectrum, the resonance escape "
      "probability decreases by 1677 pcm. As a result, the initial k_eff "
      "decreases by 2992 pcm and the required initial inventory of U-235 "
      "increases by 77.8 kg. If the thorium content further increases from 30 "
      "to 80%, as shown in the group 4, a large amount of U-238 is replaced by "
      "Th-232 in the reactor core. Because of a smaller resonance integral of "
      "Th-232 (85) compared to U-238's (275), the resonance escape probability "
      "(p) increases by 6236 pcm and contributes +336% but the reproduction "
      "factor decreases by 7017 pcm and contributes −378%. As a result, the "
      "initial k_eff decreases by 1857 pcm. Moreover, the required initial "
      "inventory of U-235 decreases by 206 kg because of a larger ACR.")

    # ------------------------------------------- fuel cycle cost analysis
    H(b, lang, "Phân tích chi phí chu kỳ nhiên liệu",
      "Fuel Cycle Cost Analysis", level=3)

    P(b, lang,
      "Sử dụng phương pháp chi phí vòng đời san bằng mô tả trong Phần 2.2.2, "
      "chi phí chu kỳ nhiên liệu của bốn loại lõi lò (Th/U MOX, SBT, SBU và "
      "WASB) được phân tích trong các Phần 3.2 và 3.3 theo hàm lượng thori "
      "được thể hiện trong Hình 16. So với Hình 11 hoặc Hình 13, chi phí chu "
      "kỳ nhiên liệu thay đổi theo xu hướng giống như độ làm giàu hiệu dụng "
      "của U-235 hoặc tồn kho ban đầu của U-235 trong lõi lò. Khi hàm lượng "
      "thori không đổi, chi phí chu kỳ nhiên liệu giảm khi mức tách không gian "
      "tăng. Tuy nhiên, sự khác biệt giữa mức SBU và mức WASB là nhỏ. Chi phí "
      "chu kỳ nhiên liệu giảm khi hàm lượng thori tăng đối với các mức SBT, "
      "SBU và WASB. Tuy nhiên, chi phí tăng trong khoảng hàm lượng thori từ 0 "
      "đến 40% và giảm khi hàm lượng thori lớn hơn 40%.",
      "Using the levelized lifetime cost methodology described in Section "
      "2.2.2, the fuel cycle cost of the four types of reactor cores (Th/U "
      "MOX, SBT, SBU, and WASB) analyzed in Sections 3.2 and 3.3 as a function "
      "of thorium content is shown in Figure 16. Compared with Figures 11 or "
      "13, the fuel cycle cost changes with the same trend as the effective "
      "enrichment of U-235 or the initial inventory of U-235 in the reactor "
      "cores. When the thorium content is constant, the fuel cycle cost "
      "decreases with the increase of the spatial separation level. However, "
      "the difference of the SBU level and WASB level is small. The fuel "
      "cycle cost decreases with the increase of the thorium content for the "
      "SBT, SBU, and WASB levels. However, it increases in the range of "
      "thorium content from 0 to 40% and decreases when the thorium content "
      "is larger than 40%.")

    FIG(b, 16, F.fig_f16(), lang)

    P(b, lang,
      "Mối liên hệ chặt chẽ giữa chi phí chu kỳ nhiên liệu và tồn kho ban đầu "
      "của U-235 chủ yếu bắt nguồn từ thành phần của chi phí. Hình 17 trình "
      "bày thành phần chi phí chu kỳ nhiên liệu cho ba lõi lò khác nhau, gồm "
      "mua urani tự nhiên, mua thori, chuyển đổi urani, làm giàu urani, chế "
      "tạo các bảng nhiên liệu, và lưu trữ cùng xử lý nhiên liệu đã qua sử "
      "dụng.",
      "The tight relationship between fuel cycle cost and initial inventory "
      "of U-235 mainly results from the composition of the cost. Figure 17 "
      "presents the composition of fuel cycle cost for three different "
      "reactor cores, including natural uranium purchase, thorium purchase, "
      "uranium conversion, uranium enrichment, the fabrication of fuel "
      "blocks, and storage and the deposal of spent fuels.")

    FIG(b, 17, F.fig_f17(), lang)

    P(b, lang,
      "Vì lượng urani tự nhiên cần thiết lớn gấp 13 lần tồn kho kim loại nặng "
      "trong lõi lò do U-235 chiếm 0.7% trong urani tự nhiên, mua urani tự "
      "nhiên và làm giàu urani đều chiếm 70% tổng chi phí chu kỳ nhiên liệu. "
      "Mua thori chỉ chiếm 2.5% vì thori không cần làm giàu và lượng thori "
      "cần dùng ít hơn rất nhiều so với lượng urani tự nhiên. Chi phí chế tạo "
      "có đơn giá cao nhất (777 $/kg HM) và quá trình chế tạo liên quan đến "
      "tất cả kim loại nặng, nên chi phí này chiếm khoảng 20% tổng chi phí. "
      "Dù đơn giá xử lý nhiên liệu đã qua sử dụng cũng cao (610 $/kg HM), "
      "chi phí xử lý chỉ chiếm khoảng 0.5% vì cái gọi là giá trị thời gian.",
      "Because the required amount of natural uranium is 13 times of the "
      "inventory of heavy metal in the reactor core due to 0.7% U-235 in "
      "natural uranium, both the natural uranium purchase and uranium "
      "enrichment are 70% of total fuel cycle cost. The thorium purchase is "
      "only 2.5% because the thorium need not be enriched, and the required "
      "amount of thorium is by far less than the amount of the natural "
      "uranium. The fabrication cost is the highest unit price (777 $/kg HM) "
      "and the fabrication involves all heavy metals, so it is about 20% of "
      "the total cost. Although the unit price of the disposal of spent fuel "
      "is also high (610 $/kg HM), the disposal cost is only about 0.5% "
      "because of so-called time value.")

    P(b, lang,
      "Chi phí chu kỳ nhiên liệu chủ yếu được quyết định bởi mua urani tự "
      "nhiên (35–40%), làm giàu urani (32–35%) và chế tạo các bảng nhiên liệu "
      "(18–21%). Tổng của ba khoản này chiếm 85–96% chi phí nhiên liệu. Chi "
      "phí chế tạo như nhau đối với mọi lõi lò vì tồn kho kim loại nặng trong "
      "lõi lò là như nhau. Mua urani tự nhiên và làm giàu urani liên quan trực "
      "tiếp đến tồn kho ban đầu của U-235. Tồn kho U-235 càng lớn thì lượng "
      "urani tự nhiên cần dùng và công đoạn làm giàu urani càng nhiều. Kết "
      "quả là chi phí chu kỳ nhiên liệu có xu hướng giống như tồn kho ban đầu "
      "của U-235 hoặc độ làm giàu hiệu dụng ban đầu.",
      "The fuel cycle cost is mainly determined by natural uranium purchase "
      "(35–40%), uranium enrichment (32–35%), and the fabrication of fuel "
      "blocks (18–21%). The total of three items is 85–96% fuel cost. The "
      "fabrication cost is the same for all reactor cores because the "
      "inventory of heavy metal in the reactor core is the same. The natural "
      "uranium purchase and uranium enrichment are directly related to the "
      "initial inventory of U-235. The more is the inventory of U-235, the "
      "more are the required natural uranium and the uranium enrichment. As "
      "a result, the fuel cycle cost is the same trend as the initial "
      "inventory of U-235 or the initial effective enrichment.")

    return b
