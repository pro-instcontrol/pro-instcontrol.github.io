# -*- coding: utf-8 -*-
"""Book 9, Chapter 11 (part E) — simulation results with discussion,
conclusions, acknowledgments and the 24 references (EN/VI bilingual).

Source: ppic_raw.txt lines 7557-7782 (PDF pp. 287-299, printed pp. 271-283).
Figures 3-5 are embedded at their source positions; equation (62) comes from
the shared equation dictionary ppic_ch11_eqd. There are no tables here.
"""
import ppicfig11 as F
from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401
from ppic_ch11_eqd import EQ as ED


# Non-overwriting 5-tuple fallbacks for just the three figures this section
# embeds. The supplier modules are authored in parallel; never replace a real
# callable that may already be registered on the aggregator.
def _fig_fallback(n, title, cap_vi, cap_en):
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 360" '
        'role="img" aria-label="%s"><rect x="1" y="1" width="678" height="358" '
        'fill="#f7f9fc" stroke="#9aa7b8"/><text x="340" y="176" '
        'text-anchor="middle" font-size="18" fill="#1f3555">%s</text>'
        '<text x="340" y="206" text-anchor="middle" font-size="13" '
        'fill="#5a6b80">Figure 11.%d</text></svg>' % (title, title, n)
    )
    return (svg, cap_vi, cap_en, cap_vi, cap_en)


if not hasattr(F, "fig_f03"):
    F.fig_f03 = lambda: _fig_fallback(
        3, "Closed-loop control structure",
        "Hình 11.3 · Sơ đồ cấu trúc vòng lặp điều khiển",
        "Figure 11.3 · Schematic view of the closed-loop structure")
if not hasattr(F, "fig_f04"):
    F.fig_f04 = lambda: _fig_fallback(
        4, "Case A: large power-demand increase",
        "Hình 11.4 · Kết quả mô phỏng trong trường hợp A",
        "Figure 11.4 · Simulation results in case A")
if not hasattr(F, "fig_f05"):
    F.fig_f05 = lambda: _fig_fallback(
        5, "Case B: large power-demand decrease",
        "Hình 11.5 · Kết quả mô phỏng trong trường hợp B",
        "Figure 11.5 · Simulation results in case B")


# Printed reference list, in order 1-24. C.refs() supplies the <ol>, so the
# leading "N. " markers are omitted; every other bibliographic detail and
# printed oddity is kept verbatim. Ampersands are HTML-escaped.
_REFS = [
    "Ingersoll, D.T. Deliberately small reactors and the second nuclear "
    "era. Prog. Nuclear Energy 2009, 51, 589–603.",
    "Vujić, J.; Bergmann, R.M.; Škoda, R.; Miletić, M. Small modular "
    "reactors: simpler, safer, cheaper? Energy 2012, 45, 288–295.",
    "Lohnert, G.H. Technical design features and essential safety-related "
    "properties of the HTR-Module. Nuclear Eng. Des. 1990, 121, 259–275.",
    "Wu, Z.; Lin, D.; Zhong, D. The design features of the HTR-10. "
    "Nuclear Eng. Des.2002, 218, 25–32.",
    "Zhang, Z.; Sun, Y. Economic potential of modular reactor nuclear "
    "power plants based on the Chinese HTR-PM project. Nuclear Eng. "
    "Des. 2007, 237, 2265–2274.",
    "Zhang, Z.; Wu, Z.; Wang, D.; Xu, Y.; Sun, Y.; Li, F.; Dong, Y. Current "
    "status and technical description of Chinese 2 × 250 MWth HTR-PM "
    "demonstration plant. Nuclear Eng. Des. 2009, 239, 265–2274.",
    "Li, W.; Zhang, Y.; Zheng, W. Investigation on three seawater "
    "desalination process coupled with NHR-200. Desalination 2012, "
    "298, 93–98.",
    "Zhang, P.; Chen, S.Z.; Wang, L.J.; Xu, J.M. Overview of nuclear "
    "hydrogen production research through iodine sulfur process at "
    "INET. Int. J. Hydrog. Energy 2010, 35, 2883–2887.",
    "Shtessel, Y.B. Sliding mode control of the space nuclear reactor "
    "system. IEEE Trans. Aerosp. Electron. Syst. 1998, 34, 579–589.",
    "Etchepareborda, A.; Lolich, J. Research reactor power controller "
    "design using an output feedback nonlinear receding horizon control "
    "method. Nuclear Eng. Des.2007, 237, 268–276.",
    "Eliasi, H.; Menhaj, M.B.; Davilu, H. Robust nonlinear model "
    "predictive control for nuclear power plants in load following "
    "operations with bounded xenon oscillations. Nuclear Eng. Des. "
    "2011, 241, 533–543.",
    "Eliasi, H.; Menhaj, M.B.; Davilu, H. Robust nonlinear model "
    "predictive control for a PWR nuclear power plant. Prog. Nuclear "
    "Energy 2012, 54, 177–185.",
    "Dong, Z. Dynamic output feedback power-level control for the "
    "MHTGR based on iterative damping assignment. Energies 2012, 5, "
    "1782–1815.",
    "Kokotović, P. The joy of feedback. IEEE Control Syst. 1992, 12, "
    "7–17.",
    "Dong, Z. Physically-based power-level control for modular high "
    "temperature gas-cooled reactors. IEEE Trans. Nuclear Sci. 2012, "
    "59, 2531–2549.",
    "Park, M.G.; Cho, N.Z. Time-optimal control of nuclear reactor "
    "power with adaptive proportional-integral-feedforward gains. IEEE "
    "Trans. Nuclear Sci. 1993, 40, 266–270.",
    "Arab-Alibeik, H.; Setayeshi, S. Adaptive control of a PWR core "
    "power using neural networks. Ann. Nuclear Energy 2005, 32, 588–"
    "605.",
    "Dong, Z. Artificial neural network compensated output feedback "
    "power-level control for modular high temperature gas-cooled "
    "reactors. Energies 2014, 7, 1149–1170.",
    "Sontag, E.D. Input to state stability: basic concepts and results. In "
    "Nonlinear and Optimal Control Theory; Cachan, J.M., Groningen, "
    "F.T., Paris, B.T., Eds.; Springer: Berlin, Germany, 2008; pp. "
    "163–220.",
    "Dong, Z.; Huang, X.; Zhang, L. A nodal dynamic model for control "
    "system design and simulation of an MHTGR core. Nuclear Eng. "
    "Des. 2010, 240, 1251–1261.",
    "Li, H.; Huang, X.; Zhang, L. A lumped parameter dynamic model "
    "of the helical coiled once-through steam generator with movable "
    "boundaries. Nuclear Eng. Des. 2008, 238, 1657–1663.",
    "Dong, Z.; Huang, X. Real-Time Simulation Platform for the "
    "Design and Verification of the Operation Strategy of the HTR-"
    "PM. In Proceedings of the 21th International Conference on "
    "Nuclear Engineering, Chengdu, China, 29 July–2 August 2013. "
    "ICONE21–16023.",
    "Mazzini, G.; Bomboni, E.; Cerullo, N.; Fridman, E.; Lomonaco, "
    "G.; Shwageraus, E. The use of Th in HTR: state of the art and "
    "implementation in Th/Pu fuel cycles. Sci. Technol. Nuclear Install. "
    "2009.",
    "Cerullo, N.; Bufalino, D.; Forasassi, G.; Lomonaco, G.; Rocchi, "
    "P.; Romanello, V. An additional performance of HTRs: The waste "
    "radiotoxicity minimisation. Radiat. Prot. Dosim. 2005, 115, 122–"
    "125.",
]


def section(lang):
    b = []

    # ------------------------------------------- SIMULATION RESULTS WITH DISCUSSION
    H(b, lang, "KẾT QUẢ MÔ PHỎNG VÀ THẢO LUẬN",
      "SIMULATION RESULTS WITH DISCUSSION", level=2)
    P(b, lang,
      "Để chứng minh tính khả thi của luật điều khiển công suất thích ứng "
      "bão hòa phản hồi đầu ra đề xuất ở các mục trên, mục này áp dụng luật "
      "đó vào điều chỉnh mức công suất cho MHTGR của nhà máy HTR-PM. Các "
      "kết quả mô phỏng số tương ứng với những trường hợp và thông số điều "
      "khiển khác nhau được trình bày, kèm theo một số thảo luận.",
      "In order to show the feasibility of the saturated adaptive "
      "output-feedback control law proposed in the above sections, it is "
      "applied to the power-level regulation for the MHTGR of the HTR-PM "
      "plant in this section. Numerical simulation results corresponding "
      "to different cases and control parameters are shown, and some "
      "discussions are also given.")

    # ------------------------------------------- Description of the Numerical Simulation
    H(b, lang, "Mô tả mô phỏng số", "Description of the Numerical Simulation",
      level=3)
    P(b, lang,
      "Mô hình động lực học của MHTGR dùng trong mô phỏng này là mô hình gồm "
      "cả động học neutron dạng nút và nhiệt thủy lực lò phản ứng dạng nút "
      "nêu trong [20]. Mô hình OTSG chính là mô hình biên di động trình bày "
      "trong [21]. Hơn nữa, mô hình tua-bin hơi và mô hình máy phát điện "
      "cũng được đưa vào mã mô phỏng [22]. Cấu trúc vòng lặp kín tạo bởi "
      "mô hình này và bộ điều khiển công suất thích ứng bão hòa phản hồi "
      "đầu ra đề xuất trong bài báo được thể hiện trong Hình 3.",
      "The dynamic model of the MHTGR utilized in this simulation adopts "
      "that one composed of both nodal neutron kinetics and nodal reactor "
      "thermal-hydraulics given in [20]. The OTSG model is just the moving "
      "boundary model presented in [21]. Furthermore, the model of the "
      "steam turbine and that of the electrical generator are also "
      "included in the simulation code [22]. The structure of the "
      "closed-loop given by this model and the saturated adaptive "
      "output-feedback power-level control proposed in this paper is "
      "shown in Figure 3.")
    P(b, lang,
      "Trong mô phỏng này, chúng tôi chọn các thông số bộ điều khiển là "
      "k<sub>NP</sub> = 2.0, k<sub>NI</sub> = 2.0, q<sub>R</sub> = 0.1G<sub>r</sub>, "
      "γ = η = 0.5, π<sub>1</sub> = 0.001, π<sub>2</sub> = 0.01, "
      "κ<sub>gi</sub> = 0.001 (i = 1, 2), κ<sub>f1</sub> = 0.001, "
      "κ<sub>f3</sub> = 0.1, q<sub>E1</sub> = 0.001 và q<sub>E2</sub> = 3.0. "
      "Hơn nữa, quan hệ sau được áp dụng ở đây:",
      "In this simulation, we choose the controller parameters as "
      "k<sub>NP</sub> = 2.0, k<sub>NI</sub> = 2.0, q<sub>R</sub> = 0.1G<sub>r</sub>, "
      "γ = η = 0.5, π<sub>1</sub> = 0.001, π<sub>2</sub> = 0.01, "
      "κ<sub>gi</sub> = 0.001 (i = 1, 2), κ<sub>f1</sub> = 0.001, "
      "κ<sub>f3</sub> = 0.1, q<sub>E1</sub> = 0.001 and q<sub>E2</sub> = 3.0. "
      "Moreover, the following relation is adopted here:")
    E(b, lang, ED[62], ED[62], num="62")
    P(b, lang,
      "Ở đây u<sub>m</sub> được gán những giá trị khác nhau để xem xét ảnh "
      "hưởng của nó đến hiệu năng điều khiển.",
      "Here u<sub>m</sub> is set to be different values to see its "
      "influence to the control performance.")
    FIG(b, 3, F.fig_f03(), lang)

    # ------------------------------------------- Simulation Results
    H(b, lang, "Kết quả mô phỏng", "Simulation Results", level=3)
    P(b, lang,
      "Hai nghiên cứu trường hợp sau được thực hiện ở đây để chứng minh "
      "tính khả thi của bộ điều khiển mới xây dựng.",
      "The following two case studies are performed here to show the "
      "feasibility of the newly-built control.")

    # ------------------------------------------- Case A
    H(b, lang, "Trường hợp A: Tăng lớn yêu cầu công suất",
      "Case A: Large-Scale Power-Demand Increase", level=4)
    P(b, lang,
      "Tín hiệu yêu cầu công suất của một MHTGR trong nhà máy HTR-PM thay "
      "đổi tuyến tính từ 50% công suất định mức lò phản ứng (RFP) lên 100% "
      "RFP với tốc độ không đổi 10%RFP/phút, tương ứng với một thao tác "
      "vận hành khó khăn đối với MHTGR. Đáp ứng động của công suất neutron "
      "tương đối n<sub>r</sub>, nhiệt độ trung bình của các phần tử nhiên "
      "liệu T<sub>f</sub>, nhiệt độ heli đầu ra T<sub>cout</sub> và tín hiệu "
      "sai số e<sub>ξ</sub> giữa ξ và ξ<sub>d</sub> được cho trong Hình 4; "
      "hơn nữa, tín hiệu tốc độ thanh điều khiển thiết kế u và tín hiệu bù "
      "u<sub>cp</sub> cũng được thể hiện trong hình này.",
      "The power-demand signal of an MHTGR of the HTR-PM plant changes "
      "linearly from 50% reactor full power (RFP) to 100% RFP with a "
      "constant speed of 10%RFP/min, which represents a hard operation of "
      "the MHTGR. The dynamic responses of the relative nuclear power "
      "n<sub>r</sub>, average temperature of the fuel elements "
      "T<sub>f</sub>, outlet helium temperature T<sub>cout</sub>, and error "
      "signal e<sub>ξ</sub> between ξ and ξ<sub>d</sub> are given in Figure "
      "4, and moreover the designed control rod speed signal u and "
      "compensating signal u<sub>cp</sub> are also shown in this figure.")
    P(b, lang,
      "Hình 4 gồm sáu ô tương ứng với bốn giá trị của giới hạn bão hòa "
      "u<sub>m</sub> là 1.0, 1.5, 2.5 và 3.5 cm/s, lần lượt được vẽ bằng "
      "đường đứt nét màu xanh lá, đường chấm đen, đường gạch màu xanh dương "
      "và đường liền màu đỏ. (a) Công suất neutron tương đối n<sub>r</sub> "
      "bắt đầu ở 0.5, bám theo đoạn dốc 10%RFP/phút đến 1.0 với một độ "
      "vọt nhỏ gần cuối đoạn dốc, rồi ổn định ở mức công suất đầy mới; giá "
      "trị u<sub>m</sub> nhỏ nhất cho độ trễ bám lớn nhất và dao động rõ "
      "nhất. (b) Nhiệt độ trung bình nhiên liệu T<sub>f</sub> tăng từ khoảng "
      "603 °C lên khoảng 637 °C, và (c) nhiệt độ heli đầu ra "
      "T<sub>cout</sub> tăng từ khoảng 718 °C lên khoảng 749 °C, cả hai đều "
      "theo sát đoạn dốc công suất với khác biệt nhỏ giữa bốn đường cong. "
      "(d) Sai số vị trí thanh điều khiển e<sub>ξ</sub> (cm) cho thấy quá "
      "trình quá độ sâu và dài nhất ứng với giới hạn nhỏ nhất, trước khi "
      "cuối cùng trở về không. (e) Tốc độ thanh điều khiển thiết kế u "
      "(cm/s) bị cắt tại ±u<sub>m</sub> và dao động trong lúc đoạn dốc được "
      "áp dụng cũng như khi đạt đến điểm đặt mới. (f) Tín hiệu bù "
      "u<sub>cp</sub> (cm/s) mạnh nhất ứng với u<sub>m</sub> nhỏ nhất và "
      "tiêu dần về không khi hệ thống hội tụ.",
      "Figure 4 collects six panels for four values of the saturation "
      "bound u<sub>m</sub> — 1.0, 1.5, 2.5 and 3.5 cm/s — drawn "
      "respectively with green dashed, black dotted, blue dashed and "
      "solid red lines. (a) The relative nuclear power n<sub>r</sub> "
      "starts at 0.5, tracks the 10%RFP/min ramp to 1.0 with a small "
      "overshoot near the end of the ramp, and settles at the new "
      "full-power setpoint; the smallest u<sub>m</sub> gives the largest "
      "tracking lag and the most visible oscillation. (b) The average "
      "fuel temperature T<sub>f</sub> rises from about 603 °C to about 637 "
      "°C, and (c) the outlet helium temperature T<sub>cout</sub> rises "
      "from about 718 °C to about 749 °C, both following the power ramp "
      "with only minor differences among the four curves. (d) The "
      "rod-position error e<sub>ξ</sub> (cm) shows the deepest and longest "
      "transient for the smallest bound, eventually returning to zero. "
      "(e) The designed control-rod speed u (cm/s) is clipped at ±u<sub>m</sub> "
      "and oscillates while the ramp is applied and again when the new "
      "setpoint is reached. (f) The compensating signal u<sub>cp</sub> "
      "(cm/s) is strongest for the smallest u<sub>m</sub> and decays to "
      "zero as the system converges.")
    FIG(b, 4, F.fig_f04(), lang)

    # ------------------------------------------- Case B
    H(b, lang, "Trường hợp B: Giảm lớn yêu cầu công suất",
      "Case B: Large-Scale Power-Demand Decrease", level=4)
    P(b, lang,
      "Tín hiệu yêu cầu công suất của MHTGR giảm tuyến tính từ 100% xuống "
      "50% RFP với tốc độ không đổi 10%RFP/phút, cũng tạo ra một thao tác "
      "vận hành khó khăn đối với MHTGR. Đáp ứng động của công suất neutron "
      "tương đối, nhiệt độ trung bình nhiên liệu, nhiệt độ heli đầu ra, "
      "sai số e<sub>ξ</sub>, cùng với u và u<sub>cp</sub>, được minh họa "
      "trong Hình 5.",
      "The power-demand signal of the MHTGR decreases linearly from 100% "
      "to 50% RFP with a constant speed of 10%RFP/min, which also gives a "
      "hard operation of the MHTGR. The dynamic responses of the relative "
      "nuclear power, average fuel temperature, outlet helium temperature, "
      "and error signal e<sub>ξ</sub> and both u and u<sub>cp</sub> are "
      "illustrated in Figure 5.")
    P(b, lang,
      "Hình 5 dùng cùng sáu ô nhưng với u<sub>m</sub> = 0.8, 1.0, 2.0 và "
      "3.5 cm/s. (a) n<sub>r</sub> giảm từ 1.0 xuống 0.5 với tốc độ "
      "10%RFP/phút; giới hạn nhỏ nhất gây ra độ vọt thấp sâu hơn và quá "
      "trình ổn định dao động dài hơn. (b) T<sub>f</sub> giảm từ khoảng "
      "637 °C xuống khoảng 603 °C và (c) T<sub>cout</sub> giảm từ khoảng "
      "749 °C xuống khoảng 718 °C, với các giới hạn nhỏ hơn một lần nữa "
      "cho độ lệch lớn hơn nhẹ ở cuối đoạn dốc. (d) e<sub>ξ</sub> (cm) đạt "
      "đỉnh vài trăm centimet ứng với u<sub>m</sub> = 0.8 cm/s "
      "trước khi tiêu dần. (e) u (cm/s) bão hòa tại ±u<sub>m</sub>, dao "
      "động mạnh với các giới hạn nhỏ. (f) u<sub>cp</sub> (cm/s) mạnh hơn "
      "rõ rệt với các giới hạn nhỏ hơn, đạt khoảng ±0.2 cm/s, rồi tắt dần "
      "khi lò phản ứng ổn định ở 50% RFP.",
      "Figure 5 uses the same six panels but with u<sub>m</sub> = 0.8, 1.0, "
      "2.0 and 3.5 cm/s. (a) n<sub>r</sub> falls from 1.0 to 0.5 at "
      "10%RFP/min; the smallest bound produces a deeper undershoot and a "
      "longer oscillatory settling. (b) T<sub>f</sub> falls from about 637 "
      "°C to about 603 °C and (c) T<sub>cout</sub> from about 749 °C to "
      "about 718 °C, with the smaller bounds again showing slightly larger "
      "deviations at the end of the ramp. (d) e<sub>ξ</sub> (cm) peaks at "
      "several hundred centimetres for u<sub>m</sub> = 0.8 cm/s before "
      "decaying. (e) u (cm/s) saturates at ±u<sub>m</sub> with pronounced "
      "oscillation for the small bounds. (f) u<sub>cp</sub> (cm/s) is "
      "markedly more active for the smaller bounds, reaching roughly "
      "±0.2 cm/s, and dies away as the reactor settles at 50% RFP.")
    FIG(b, 5, F.fig_f05(), lang)

    # ------------------------------------------- Discussion
    H(b, lang, "Thảo luận", "Discussion", level=3)
    P(b, lang,
      "Yêu cầu công suất xác định các điểm đặt của công suất neutron tương "
      "đối và nhiệt độ trung bình của dòng heli trong vòng sơ cấp. Giả sử "
      "MHTGR vận hành ở trạng thái ổn định trong một khoảng thời gian trước "
      "khi yêu cầu công suất thay đổi. Rõ ràng là sự thay đổi của tín hiệu "
      "yêu cầu công suất làm tăng sai số giữa giá trị thực tế và điểm đặt "
      "của công suất neutron và nhiệt độ heli, tức là các biến trạng thái "
      "đo được x<sub>1</sub> và x<sub>4</sub> được xác định bởi Phương trình "
      "(5). Hơn nữa, từ Phương trình (18), sự thay đổi của x<sub>1</sub> và "
      "x<sub>4</sub> quyết định sự thay đổi của ξ<sub>d</sub>, lần lượt làm "
      "tăng e<sub>ξ</sub> được xác định bởi (22). Sau đó, x<sub>1</sub>, "
      "x<sub>4</sub> và e<sub>ξ</sub> thúc đẩy luật điều khiển thích ứng bão hòa "
      "mới xây dựng cho bởi các Phương trình (17), (19)–(21), (26) và (27) "
      "để tạo ra tín hiệu tốc độ thanh điều khiển bão hòa, giúp MHTGR tiến "
      "đến mức công suất mới được đưa ra.",
      "The power-demand determines the setpoints of the relative nuclear "
      "power and average temperature of the helium flow inside the primary "
      "loop. Suppose that the MHTGR operates at a steady state for a "
      "certain period before the power-demand changes. It is clear that "
      "the variation of the power-demand signal enlarge the errors between "
      "actual values and setpoints of the nuclear power and helium "
      "temperature, i.e., measurable state-variables x<sub>1</sub> and "
      "x<sub>4</sub> defined by Equation (5). Further, from Equation (18), "
      "the variations of x<sub>1</sub> and x<sub>4</sub> determine the "
      "variation of ξ<sub>d</sub>, which in turn enlarge e<sub>ξ</sub> "
      "defined by (22). Then, x<sub>1</sub>, x<sub>4</sub> and e<sub>ξ</sub> "
      "derives the newly-built saturated adaptive control law given by "
      "Equations (17), (19)–(21), (26) and (27) to generate saturated "
      "control rod speed signal so that the MHTGR can come to the newly "
      "given power-level.")
    P(b, lang,
      "Từ các kết quả mô phỏng minh họa bởi Hình 4 và Hình 5, có thể thấy "
      "tính ổn định vòng lặp kín được bảo đảm tốt, mang lại hiệu năng động "
      "thỏa đáng cho MHTGR. Hơn nữa, từ các ô (a), (b) và (c) của Hình 4 và "
      "Hình 5, hiệu năng điều khiển tốt hơn khi giới hạn bão hòa "
      "u<sub>m</sub> lớn hơn. Lý do là khi u<sub>m</sub> tăng, thanh điều "
      "khiển có thể di chuyển nhanh hơn, nghĩa là sai số điều khiển và các "
      "nhiễu loạn bị triệt tiêu nhanh và hiệu quả hơn. Thực tế, đối chiếu "
      "các ô (a), (b), (c) với ô (d) của Hình 4 và Hình 5 cho thấy có một "
      "sự đánh đổi giữa chất lượng đáp ứng và giới hạn bão hòa "
      "u<sub>m</sub>. Hơn nữa, từ ô (d) của Hình 4 và Hình 5, "
      "u<sub>m</sub> càng nhỏ thì độ không khớp giữa ξ và ξ<sub>d</sub>, "
      "tức là e<sub>ξ</sub>, càng lớn, tuy nhiên tính ổn định vòng lặp kín "
      "vẫn được bảo đảm nhờ hiệu ứng bù do thành phần u<sub>cp</sub> xác "
      "định bởi các Phương trình (19)–(21). Như có thể thấy từ ô (f) của "
      "Hình 4 và Hình 5, hiệu ứng bù do u<sub>cp</sub> tạo ra càng mạnh khi "
      "u<sub>m</sub> càng nhỏ, và tiêu tan khi toàn bộ hệ thống hội tụ về "
      "một trạng thái ổn định nhất định.",
      "From the simulation results illustrated by Figure 4 and Figure 5, "
      "we can see that the closed-loop stability is well guaranteed, which "
      "provides a satisfactory dynamic performance for the MHTGR. Moreover, "
      "from parts (a), (b) and (c) of Figure 4 and Figure 5, the control "
      "performance is better if the saturation bound u<sub>m</sub> is "
      "larger. The reason is that as u<sub>m</sub> becomes larger, the "
      "control rods can move faster, which means that the control errors "
      "and disturbances can be suppressed faster and more efficiently. "
      "Actually, through corresponding parts (a), (b) and (c) to part (d) "
      "of Figure 4 and Figure 5, it is clear that there is a trade-off "
      "between the response quality level and saturation bound "
      "u<sub>m</sub>. Furthermore, from part (d) of Figure 4 and Figure 5, "
      "saturation bound u<sub>m</sub> is smaller, the mismatch between ξ "
      "and ξ<sub>d</sub>, i.e., e<sub>ξ</sub> is larger, and however the "
      "closed-loop stability is still guaranteed, which is given by "
      "compensation effect caused by term u<sub>cp</sub> determined by "
      "Equations (19)–(21). As we can see from part (f) of Figure 4 and "
      "Figure 5, the compensating effect generated by u<sub>cp</sub> is "
      "stronger if u<sub>m</sub> is smaller, and is dissipated as the "
      "entire system converges to a given steady state.")
    P(b, lang,
      "Cuối cùng, từ phân tích lý thuyết ở mục trên và mô phỏng số trong "
      "mục này, bộ điều khiển mức công suất thích ứng bão hòa mới xây dựng "
      "cho MHTGR bảo đảm tính ổn định vòng lặp kín thỏa đáng và khả năng "
      "vận hành lò phản ứng. Nhờ việc sử dụng rộng rãi các nền tảng hệ "
      "thống điều khiển số tiên tiến, không có khó khăn nào trong việc "
      "triển khai luật điều khiển mới này. Trong thực tế kỹ thuật, việc "
      "khởi động một SMR thường do các nhân viên vận hành thực hiện. Sau "
      "khi khởi động, hệ thống điều khiển lò phản ứng tự động mới được "
      "phép bật lên. Do đó, bộ điều khiển mức công suất đưa ra trong bài "
      "báo được thiết kế cho vận hành công suất bình thường, và KHÔNG dành "
      "cho việc khởi động lò phản ứng.",
      "Finally, from the theoretical analysis in the above section and the "
      "numerical simulation in this section, the newly-built saturated "
      "adaptive power-level controller of the MHTGR guarantees satisfactory "
      "closed-loop stability and reactor operability. Thanks to the widely "
      "utilization of advanced digital control system platforms, there is "
      "no difficulty in realizing this novel control law. In the practical "
      "engineering, the startup of a SMR is usually performed by the "
      "operators. After the startup, an automatic reactor control system "
      "can be permitted to switch on. Therefore, the power-level controller "
      "given in this paper is designed for normal power operation, and NOT "
      "for reactor startup.")
    NOTE(b, lang,
      "<b>Phạm vi vận hành.</b> Bộ điều khiển công suất này chỉ dành cho "
      "vận hành công suất bình thường sau khi lò phản ứng đã khởi động, "
      "không dành cho khởi động lò phản ứng.",
      "<b>Operational scope.</b> This power-level controller is designed "
      "for normal power operation only, NOT for reactor startup.")

    # ------------------------------------------- CONCLUSIONS
    H(b, lang, "KẾT LUẬN", "CONCLUSIONS", level=2)
    P(b, lang,
      "MHTGR đã được xem là một trong những ứng viên tốt nhất để xây dựng "
      "các nhà máy điện hạt nhân dựa trên SMR với cả đặc tính an toàn vốn "
      "có lẫn tiềm năng cạnh tranh về kinh tế. Điều khiển mức công suất có "
      "vai trò rất quan trọng trong việc cung cấp vận hành an toàn, ổn định "
      "và hiệu quả cho MHTGR. Tuy nhiên, do tồn tại tính phi tuyến, sự bất "
      "định tham số và sự bão hòa đầu vào trong động lực học của nhà máy "
      "điện hạt nhân dựa trên MHTGR, cần phải đưa ra một phương pháp thiết "
      "kế điều khiển mức công suất phi tuyến thích ứng có chức năng bù "
      "bão hòa. Trong bài báo này, một phương pháp điều khiển mức công suất "
      "thích ứng bão hòa phản hồi đầu ra mới cho MHTGR được đề xuất. Người "
      "ta chứng minh về mặt lý thuyết rằng luật điều khiển này có thể cung "
      "cấp tính ổn định nhờ đầu vào (ISS) cho hệ thống vòng lặp kín.",
      "MHTGR has already been seen as one of the best candidates for "
      "building SMR-based nuclear power plants with both inherent safety "
      "features and potential economic competitive power. Power-level "
      "control is very crucial in providing safe, stable and efficient "
      "operation for MHTGRs. However, since there exists nonlinearity, "
      "parameter uncertainty and input saturation in MHTGR-based nuclear "
      "plant dynamics, it is necessary to provide a nonlinear adaptive "
      "power-level control design method with saturation compensating "
      "function. In this paper, a novel saturated adaptive output-feedback "
      "power-level control for MHTGRs is proposed. It is proved "
      "theoretically that this control law can provide input-to-state "
      "stability (ISS) for the closed-loop system.")
    P(b, lang,
      "Những điểm mới trong việc xây dựng bộ điều khiển gồm: (1) xây dựng "
      "hàm Lyapunov dựa trên ectropy dịch chuyển của cả động học neutron và "
      "nhiệt thủy lực lò phản ứng để bộ điều khiển có dạng gọn; (2) đưa ra "
      "một luật thích ứng cho bộ điều khiển này để các thông số của nó có "
      "thể được chỉnh định trực tuyến; và (3) đề xuất một thuật toán bù "
      "bão hòa để tính ổn định ISS của vòng lặp kín có thể đạt được bằng "
      "đầu vào điều khiển bão hòa.",
      "The novelties in developing the control include: (1) constructing "
      "Lyapunov function based upon the shifted-ectropies of both reactor "
      "neutron kinetics and thermal-hydraulics so that this control has a "
      "neat form; (2) giving an adaptation law for this control so that "
      "its parameters can be tuned online; and (3) proposing a saturation "
      "compensating algorithm so that the closed-loop ISS can be realized "
      "by saturated control input.")
    P(b, lang,
      "Hơn nữa, các kết quả mô phỏng số trong các trường hợp tăng và giảm "
      "mức công suất trên phạm vi lớn không chỉ kiểm chứng các kết quả lý "
      "thuyết mà còn minh họa mối quan hệ giữa hiệu năng điều chỉnh và "
      "giới hạn đầu vào điều khiển. Cuối cùng, bộ điều khiển mức công suất "
      "mới xây dựng này có thể dễ dàng triển khai trên các nền tảng hệ "
      "thống điều khiển số tiên tiến cho những ứng dụng kỹ thuật tiềm "
      "năng. Người ta biết rõ rằng các loại nhiên liệu khác nhau cho các "
      "giá trị khác nhau của phần neutron trễ β [23,24], lần lượt ảnh hưởng "
      "sâu sắc đến động lực học lò phản ứng. Trong tương lai, cần nghiên "
      "cứu ảnh hưởng của các β khác nhau đến thiết kế điều khiển mức công "
      "suất, và thiết kế luật điều khiển mức công suất thích ứng tương ứng.",
      "Furthermore, numerical simulation results in the cases of "
      "large-range power-level increase and decrease not only verify the "
      "theoretic results but also illustrate the relationship between "
      "regulating performance and control input bound. Finally, this "
      "newly-built power-level controller can be easily implemented on "
      "advanced digital control system platforms for possible engineering "
      "applications. It is well known that different fuel types induce "
      "different values of the fraction of the delayed neutrons β [23,24], "
      "which in turn influence the reactor dynamics deeply. In the future, "
      "the impact of different β to power-level control design should be "
      "studied, and the corresponding adaptive power-level control law "
      "should be designed.")

    # ------------------------------------------- ACKNOWLEDGMENTS
    H(b, lang, "LỜI CẢM ƠN", "ACKNOWLEDGMENTS", level=2)
    P(b, lang,
      "Công trình trong bài báo này được hỗ trợ chung bởi Quỹ Khoa học "
      "Tự nhiên Trung Quốc (NSFC) (Số hiệu tài trợ 61374045), Chương trình "
      "Nghiên cứu Khoa học Sáng kiến của Đại học Thanh Hoa (Số hiệu tài trợ "
      "20121087992) và Dự án Trọng điểm Khoa học và Công nghệ Quốc gia "
      "(Số hiệu tài trợ ZX06901). Ngoài ra, tác giả muốn gửi lời cảm ơn "
      "sâu sắc tới Huang Xiao-Jin vì sự hỗ trợ liên tục, những thảo luận "
      "giá trị và các góp ý mang tính xây dựng.",
      "The work in this paper is jointly supported by Natural Science "
      "Foundation of China (NSFC) (Grant No. 61374045), Tsinghua University "
      "Initiative Scientific Research Program (Grant No. 20121087992) and "
      "National S&amp;T Major Project (Grant No. ZX06901). Moreover, the "
      "author would like to thank Huang Xiao-Jin deeply for consistent "
      "support, valuable discussions and constructive suggestions.")

    # ------------------------------------------- REFERENCES
    H(b, lang, "TÀI LIỆU THAM KHẢO", "REFERENCES", level=2)
    REFS(b, lang, _REFS)
    return b
