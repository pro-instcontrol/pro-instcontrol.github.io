# -*- coding: utf-8 -*-
"""Book 7, Chapter 20 - Methods of Aerodynamic Valve Noise Reduction (EN/VI).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
125-131 (PDF pp. 126-132). Seven printed pages, five vector redraws of
Figures 20-1 to 20-5, one numbered equation (20-1) and six unnumbered
printed expressions. The OCR text layer garbles the mathematical symbols;
the printed forms were checked against page renders of all seven pages.
"""
from cvp_common import eq, fig, h2, h3, note, p, refs, ul

try:
    import cvpfig20 as F
except ImportError:
    # The figure supplier is authored in parallel; fall back to inert callables.
    class _FallbackFigures(object):
        pass
    F = _FallbackFigures()


def _stub(n, vi, en):
    """Minimal valid five-tuple used only until the real supplier is present."""
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 360" '
           'role="img" aria-label="Figure 20-%d"><rect x="8" y="8" '
           'width="664" height="344" fill="none" stroke="#888" />'
           '<text x="340" y="190" text-anchor="middle" font-size="14">'
           'Figure 20-%d</text></svg>') % (n, n)
    return (svg, vi, en, vi, en)


if not hasattr(F, "fig_f201"):
    F.fig_f201 = lambda: _stub(1, "Hình 20-1. Bộ lót nhiều cấp.",
                               "Figure 20-1. Multistep trim.")
if not hasattr(F, "fig_f202"):
    F.fig_f202 = lambda: _stub(2, "Hình 20-2. Lồng nhiều lỗ.",
                               "Figure 20-2. Multi-orifice cage.")
if not hasattr(F, "fig_f203"):
    F.fig_f203 = lambda: _stub(3, "Hình 20-3. Lồng mê cung.",
                               "Figure 20-3. Labyrinth cage.")
if not hasattr(F, "fig_f204"):
    F.fig_f204 = lambda: _stub(4, "Hình 20-4. Bộ lót hai cấp.",
                               "Figure 20-4. Two-stage trim.")
if not hasattr(F, "fig_f205"):
    F.fig_f205 = lambda: _stub(5, "Hình 20-5. Van bướm và bộ tiết lưu.",
                               "Figure 20-5. Butterfly valve and restrictor.")

PAGES_SRC = 7
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Methods of Aerodynamic Valve Noise Reduction"
TITLE_VI = "Phương pháp giảm tiếng ồn khí động học của van"


def note_terms(lang):
    """A one-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 20.</b> tiếng ồn khí động (aerodynamic "
                "noise) · ô nhiễm tiếng ồn (noise pollution) · vận tốc tia khí "
                "Uvc · tần số ồn đỉnh bên trong fp · tỷ số áp suất lỗ tiết lưu "
                "P₁/P₀, với P₀ là áp suất tĩnh bên trong lỗ · hệ số phục hồi "
                "áp suất F_L · hiệu suất âm thanh hiệu chỉnh ηm · Chế độ I "
                "(dưới âm, P₁/P₀ ≤ 1,9) · Chế độ II và III (tốc độ âm đến Mach "
                "1,4) · bộ lót giảm áp nhiều cấp (multistep resistance trim) · "
                "hệ số kiểu van Fd · số lỗ song song có cùng kích thước n₀ · "
                "đường kính tia khí Dj · tần số vòng của ống fr · suy hao "
                "truyền qua ống (transmission loss) · lồng mê cung (labyrinth "
                "cage) · bộ lót hai cấp đa diện tích · van bướm đĩa có rãnh "
                "(fluted butterfly valve) · bộ tiết lưu đa cấp (multistage "
                "restrictor) · bộ giảm ồn hạ lưu · vật liệu cách âm thành ống · "
                "đồng hồ lưu lượng siêu âm")
    return ("<b>Key terms.</b> aerodynamic noise · noise pollution · jet "
            "velocity Uvc · internal peak noise frequency fp · internal "
            "orifice pressure ratio P₁/P₀, with P₀ the static pressure inside "
            "the orifice · pressure recovery factor F_L · modified acoustical "
            "efficiency ηm · Regime I (subsonic, P₁/P₀ ≤ 1.9) · Regimes II and "
            "III (sonic flow up to Mach 1.4) · multistep resistance trim · "
            "valve style modifier Fd · number of equally sized parallel ports "
            "n₀ · jet diameter Dj · pipe ring frequency fr · transmission "
            "loss · labyrinth cage trim · two-stage multiarea trim · fluted "
            "butterfly valve · multistage fluid restrictor · downstream "
            "silencer · acoustic pipe-wall insulation · ultrasonic flow meter")


def body_vi():
    b = []
    b.append(h2("Các phương pháp giảm ồn khí động cho van",
                "Methods of Aerodynamic Valve Noise Reduction"))

    b.append(p("Giờ ta xét đến trường hợp phổ biến hơn của “ô nhiễm tiếng ồn,” "
               "đó là tiếng ồn khí động. Từ các phương trình trước dùng để "
               "ước tính mức ồn tiết lưu, rõ ràng có hai biến số cơ bản chi "
               "phối mức âm và vì thế có thể được thay đổi để đạt được mức "
               "giảm ồn mong muốn: vận tốc tia khí (Uvc) và tần số ồn đỉnh bên "
               "trong (fp)."))
    b.append(p("Vận tốc tia khí là yếu tố quan trọng nhất trong phát sinh "
               "tiếng ồn, nhưng lại là yếu tố khó xử lý nhất. Vì vận tốc là một "
               "phần của tỷ số áp suất lỗ tiết lưu bên trong P₁/P₀, trong đó P₀ "
               "là áp suất tĩnh bên trong lỗ, việc điều chỉnh tỷ số này là "
               "cách duy nhất để giảm vận tốc. Biểu thức được in là:"))
    b.append(eq("P₁ × F_L²"))

    b.append(h3("Chế độ I dưới âm", "Subsonic Regime I"))
    b.append(p("Trong Chế độ I dưới âm, tức là P₁/P₀ ≤ 1,9, việc chọn bộ lót "
               "van kém suôn sẻ hơn — nghĩa là có số F_L cao (từ 0,9 đến 1,0) "
               "— sẽ cho vận tốc tia khí thấp hơn và do đó mức ồn thấp hơn. Ở "
               "các tỷ số áp suất cao hơn, cách khắc phục duy nhất là dùng các "
               "lỗ tiết lưu hoặc đường dẫn điện trở mắc nối tiếp, sao cho lý "
               "tưởng là mỗi tia khí con đều làm việc trong chế độ dưới âm. "
               "Hình 20-1 cho thấy một van như vậy với bộ lót điện trở nhiều "
               "cấp (đường zig-zag)."))
    b.append(eq("P₁/P₀ ≤ 1.9"))
    b.append(fig(1, F.fig_f201(), lang="vi"))

    b.append(h3("Chế độ II và III", "Regimes II and III"))
    b.append(p("Đối với Chế độ II và III, tức là P₁/P₂ > P₁/P₂ tới hạn, dòng "
               "chảy đạt tốc độ âm đến Mach 1,4:"))
    b.append(eq("ηm = −40 + 37 log[(P₁/P₂)/(P₁/P₂ critical)] + "
                "10 log(F_L²) dB", num="20-1"))

    b.append(h3("Ví dụ tính toán: khí tự nhiên", "Worked example: natural gas"))
    b.append(p("Giả sử cần tiết lưu khí tự nhiên từ áp suất đầu vào 1500 psia "
               "xuống 750 psia, và lấy hệ số phục hồi áp suất của van là 0,9. "
               "Tỷ số áp suất bên trong P₁/P₀ cho lần giảm một cấp sẽ phải là "
               "P₁/P₂ = 2,35:1, cho hiệu suất âm thanh hiệu chỉnh −34,8 dB "
               "theo Phương trình 20-1. Nếu dùng thay vào đó bộ lót mười cấp "
               "của Hình 20-1, tỷ số áp suất qua mỗi lỗ chỉ còn 1,089:1, với "
               "hiệu suất âm thanh hiệu chỉnh −63,1 dB — tiết kiệm được 28,3 "
               "dB (bỏ qua các yếu tố khác). Nếu bỏ qua sự cộng một phần của "
               "mười nguồn âm riêng biệt, mức giảm ồn là khoảng 29 dB; mức "
               "tiết kiệm thực tế khi tính đến các nguồn cộng thêm và sự thay "
               "đổi tần số sẽ vào khoảng 20 dB."))

    b.append(h3("Bộ lót nhiều lỗ và dịch chuyển tần số",
                "Multi-orifice trim and frequency shift"))
    b.append(p("Một cách rẻ hơn để giảm tiếng ồn tiết lưu “nghe được” là tăng "
               "tần số đỉnh bằng bộ lót nhiều lỗ như Hình 20-2. Việc tiết lưu "
               "vẫn là một cấp, nhưng tia khí được chia thành nhiều cổng song "
               "song. Điều này làm giảm hệ số kiểu van Fd vì:"))
    b.append(eq("Fd = 1/(n₀)^0.5"))
    b.append(p("trong đó n₀ là số cổng song song có cùng kích thước. Vì Fd tỷ "
               "lệ thuận với đường kính tia khí Dj, tần số có thể được dịch "
               "lên cao hơn, làm tăng suy hao truyền qua ống. Với n₀ = 16, Fd "
               "bằng 0,25 và tần số đỉnh thu được là 1/0,25, hay gấp bốn lần "
               "so với một lỗ đơn (Fd = 1) có cùng tổng diện tích dòng chảy:"))
    b.append(eq("n₀ = 16 → Fd = 0.25 → f_peak = 1/0.25 = 4×"))
    b.append(p("Nếu tần số đỉnh nằm trong vùng ống chịu điều khiển bởi khối "
               "lượng, điều này rất có thể xảy ra, thì đạt được mức giảm tổng "
               "thể của âm thanh bên ngoài (nghe được):"))
    b.append(eq("ΔT_Lfp = 20 log(f_pl / f^0.25) = 12 dB"))
    b.append(p("(trừ khi dùng ống lớn). Cách này chỉ giới hạn ở tỷ số áp suất "
               "khoảng 3:1 qua thành lồng; ở tỷ số cao hơn, các tia khí có thể "
               "hợp lại ở hạ lưu và triệt tiêu lợi ích của tần số cao. Cần "
               "lưu ý: Phương trình 20-1 chỉ đúng trong vùng mà tần số ồn đỉnh "
               "bên trong fp không vượt quá hai quãng tám (4 lần) trên tần số "
               "vòng của ống fr:"))
    b.append(eq("f_p ≤ 4 f_r"))
    b.append(p("Dưới tỷ số này, âm thanh bên trong chuyển từ 20 dB mỗi quãng "
               "tám xuống chỉ còn 10 dB mỗi quãng tám. Điều này thường xảy ra "
               "khi lắp van có bộ lót thấp ồn (fp cao) vào ống lớn, từ 12 inch "
               "trở lên."))
    b.append(fig(2, F.fig_f202(), lang="vi"))

    b.append(h3("Bộ lót lồng mê cung", "Labyrinth cage trim"))
    b.append(p("Một bố trí phức tạp hơn được cho trong Hình 20-3: ở đây "
               "phương pháp nhiều cấp được kết hợp với phương pháp nhiều "
               "đường dẫn trong các lớp đĩa tựa vòng đệm có kênh dẫn riêng "
               "được đúc hoặc khắc. Thiết kế này vừa mang lại lợi ích của "
               "việc giảm vận tốc, vừa mang lại lợi ích của suy hao truyền "
               "cao hơn nhờ tần số tăng. Mức giảm ồn điển hình lên tới 30 dB."))
    b.append(fig(3, F.fig_f203(), lang="vi"))

    b.append(h3("Bộ lót hai cấp đa diện tích", "Two-stage multiarea trim"))
    b.append(p("Hình 20-4 cho thấy một cải tiến gần đây so với bộ lót mê "
               "cung: nhiều lớp tấm cắt laser giống hệt nhau tạo giữa chúng "
               "một đường dẫn dòng chảy ba chiều, thường là từ một kênh vào "
               "suôn sẻ duy nhất ở mặt trong của mỗi đĩa đến nhiều kênh ra "
               "hình chữ nhật không suôn sẻ ở chu vi ngoài. Tỷ số giữa số "
               "kênh ra và kênh vào do tỷ số áp suất tổng qua van quyết định. "
               "Để giảm ồn tối đa, cấp ra được giữ ở chế độ dưới âm (nơi "
               "đường dẫn kém suôn sẻ có hiệu suất âm thanh thấp hơn), trong "
               "khi cấp đầu chịu dòng siêu âm. Các kênh suôn sẻ đóng vai trò "
               "như bộ khuếch tán siêu âm, chuyển hầu hết năng lượng giảm áp "
               "thành sóng xung kích thay vì thành nhiễu loạn vốn phát tiếng "
               "ồn nhiều hơn. Một phần đáng kể năng lượng âm thanh do cấp đầu "
               "tạo ra cũng được giữ lại trong “khoảng lắng,” tức kênh thẳng "
               "đứng giữa hai cấp. Với tỷ số diện tích kênh ra trên kênh vào "
               "là 6:1, tỷ số áp suất qua cấp đầu thường là 5:1, trong khi tỷ "
               "số áp suất tổng qua cả hai cấp có thể tới 8:1 mà vẫn giữ được "
               "hiệu năng ồn thấp tối ưu. Vì không có đường dẫn dài, ngoằn "
               "nghèo, bộ lót này gọn hơn nhiều so với bộ lót mê cung điển "
               "hình và vì thế có lưu lượng lớn hơn cho cùng kích thước. Nó "
               "cũng ít bị tắc nghẽn hơn khi chất lỏng có chứa hạt bụi — vấn "
               "đề thường gặp ở các bộ lót làm việc với vận tốc khí thấp và "
               "kênh dẫn nhỏ."))
    b.append(fig(4, F.fig_f204(), lang="vi"))

    b.append(h3("Van bướm có rãnh với bộ tiết lưu hạ lưu",
                "Fluted butterfly valve with a downstream restrictor"))
    b.append(p("Một giải pháp kinh tế hơn là ghép một thiết bị giảm áp tĩnh "
               "hạ lưu, chẳng hạn bộ tiết lưu nhiều lỗ, với một van tiết lưu "
               "như van bướm đĩa có rãnh trong Hình 20-5. Đĩa có rãnh tạo ra "
               "nhiều tia khí song song với tần số ồn cao hơn, giống như van "
               "lồng nhiều cổng, nhưng phần lớn năng lượng áp suất được tấm "
               "tĩnh chuyển hóa, cho mức giảm ồn tại lưu lượng cực đại khoảng "
               "20 dB. Ở lưu lượng thiết kế cực đại, van được chọn với tỷ số "
               "áp suất thấp 1,1 hoặc 1,15, phần còn lại của độ giảm áp nằm "
               "ở tấm tĩnh, vốn vốn đã ồn thấp nhờ thiết kế nhiều cấp, nhiều "
               "lỗ. Việc đặt bộ giảm ồn hạ lưu sau van không hiệu quả về chi "
               "phí vì mức giảm chỉ khoảng 10 dB: một phần đáng kể công suất "
               "âm thanh đi ngược lên thượng lưu (đặc biệt ở các van nhìn "
               "thẳng như van bướm và van bi) hoặc bức xạ qua thân van và "
               "bộ truyền động. Lý do tương tự cũng giới hạn vật liệu cách âm "
               "thành ống ở khoảng 15 dB."))
    b.append(fig(5, F.fig_f205(), lang="vi"))

    b.append(h2("Tóm tắt các biện pháp giảm ồn van",
                "Summary of valve noise abatement procedures"))
    b.append(p("Sau đây là tóm tắt các biện pháp giảm ồn van:"))
    b.append(ul([
        "Nếu Cv × F_L × P₁ nhỏ hơn 1000 thì không cần biện pháp giảm ồn "
        "(SL ≤ 90 dBA).",
        "Dùng vật liệu cách âm ống dày 1 inch để giảm 5 đến 10 dB.",
        "Tăng gấp đôi độ dày thành ống để giảm 6 dB.",
        "Đặt bộ giảm ồn hạ lưu để giảm 10 dB.",
        "Đặt bộ giảm ồn cả thượng lưu và hạ lưu để giảm 20 dB.",
        "Đặt tấm điện trở nhiều cổng hạ lưu van để giảm 15 đến 20 dB "
        "(chỉ dùng 5% đến 10% áp suất đầu vào van làm ΔP của van ở lưu "
        "lượng cực đại).",
        "Dùng van chuyên dụng thấp ồn để giảm 15 đến 30 dB.",
        "Có thể phối hợp các biện pháp trên; sự phối hợp đôi khi hiệu quả "
        "hơn về chi phí.",
    ]))

    b.append(p("Một lưu ý thận trọng: các bộ lót thấp ồn làm việc ở tần số "
               "cao, thường giữa 5000 Hz và 20.000 Hz, có thể gây nhiễu cho "
               "đồng hồ lưu lượng siêu âm đặt hạ lưu các van này. Tần số cao "
               "do bộ lót tạo ra có thể làm giảm độ chính xác, thậm chí gây "
               "hỏng các đồng hồ đó [2]."))

    b.append(note("<b>Ghi chú về nguồn.</b> (1) Chương 20 chiếm các trang in "
                  "125–131 (PDF tr. 126–132). (2) Lớp văn bản OCR xáo trộn "
                  "các ký hiệu toán học; các dạng in — gồm P₁ × F_L², "
                  "Phương trình 20-1, Fd = 1/(n₀)^0.5 và biểu thức suy hao "
                  "truyền — đã được đọc lại từ ảnh của cả bảy trang. (3) "
                  "Phương trình 20-1 là phương trình duy nhất được đánh số; "
                  "các biểu thức in khác được trình bày dưới dạng phương "
                  "trình không số. (4) Hai chi tiết in được giữ nguyên: chú "
                  "thích Hình 20-1 mô tả 11 cấp tiết lưu trong khi ví dụ tính "
                  "toán dùng bộ lót mười cấp; và ví dụ van bướm ghi tỷ số áp "
                  "suất thấp 1,1 hoặc 1,15, trong khi một số bản chép lại ghi "
                  "1,1 hoặc 1,5 — bản dịch dùng theo trang in. Năm hình được "
                  "vẽ lại dạng vector từ các hình minh họa trong nguyên bản."))
    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(refs([
        "C. Reed, “Optimizing Valve Jet Size and Spacing Reduces Valve Noise,” "
        "<i>Control Engineering</i> (September 1976): 63–64.",
        "E. W. Singleton, “An Investigation into Control Valve-Generated "
        "Turbulence and Noise,” <i>Measurement &amp; Control</i> 37, no. 6 "
        "(July 2004).",
    ]))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Methods of Aerodynamic Valve Noise Reduction",
                "Methods of Aerodynamic Valve Noise Reduction"))

    b.append(p("Now to the more common occurrence of “noise pollution,” that "
               "is, aerodynamic noise. From the preceding equations for "
               "estimating throttling noise levels it becomes apparent that "
               "two basic variables are mainly responsible for the sound "
               "level and therefore can be varied to achieve a desired noise "
               "reduction: the jet velocity (Uvc) and the internal peak noise "
               "frequency (fp)."))
    b.append(p("Jet velocity is the most important element in noise "
               "generation, yet the most difficult one to deal with. Because "
               "the velocity is a fraction of the internal orifice pressure "
               "ratio P₁/P₀, where P₀ is the static pressure inside the "
               "orifice, manipulating this ratio is the only way to reduce "
               "velocity. The printed relation is:"))
    b.append(eq("P₁ × F_L²"))

    b.append(h3("Subsonic Regime I", "Subsonic Regime I"))
    b.append(p("In subsonic Regime I, that is, P₁/P₀ ≤ 1.9, selecting a valve "
               "trim that is less streamlined — one with a high F_L number "
               "(0.9 to 1.0) — gives a lower jet velocity and therefore a "
               "lower sound level. At higher pressure ratios the only remedy "
               "is to use orifices or resistance paths in series so that, "
               "ideally, each sub-jet operates in the subsonic regime. "
               "Figure 20-1 shows such a valve with a multistep resistance "
               "trim (the zig-zag path)."))
    b.append(eq("P₁/P₀ ≤ 1.9"))
    b.append(fig(1, F.fig_f201(), lang="en"))

    b.append(h3("Regimes II and III", "Regimes II and III"))
    b.append(p("For Regimes II and III, that is, P₁/P₂ > P₁/P₂ critical, flow "
               "is sonic up to Mach 1.4:"))
    b.append(eq("ηm = −40 + 37 log[(P₁/P₂)/(P₁/P₂ critical)] + "
                "10 log(F_L²) dB", num="20-1"))

    b.append(h3("Worked example: natural gas", "Worked example: natural gas"))
    b.append(p("Assume an application in which natural gas at an inlet "
               "pressure of 1500 psia is throttled down to 750 psia, and take "
               "the valve pressure recovery factor as 0.9. The internal "
               "pressure ratio P₁/P₀ for a single-stage reduction would have "
               "to be P₁/P₂ = 2.35:1, yielding a modified acoustical "
               "efficiency of −34.8 dB from Equation 20-1. Using instead the "
               "ten-step trim of Figure 20-1, the pressure ratio across the "
               "orifice at each step is only 1.089:1, with a modified "
               "acoustical efficiency of −63.1 dB — a 28.3 dB noise saving "
               "(ignoring other factors). Ignoring the partial addition of "
               "ten separate sound power sources, this represents about 29 "
               "dB of noise reduction; the actual saving once added sources "
               "and the change in frequency are accounted for would be about "
               "20 dB."))

    b.append(h3("Multi-orifice trim and frequency shift",
                "Multi-orifice trim and frequency shift"))
    b.append(p("A less costly way to reduce “audible” throttling noise is to "
               "increase the peak frequency using a multi-orifice trim as in "
               "Figure 20-2. Throttling is still single-stage, but the jets "
               "are divided into several parallel ports. This lowers the "
               "valve style modifier Fd because:"))
    b.append(eq("Fd = 1/(n₀)^0.5"))
    b.append(p("where n₀ is the number of equally sized parallel ports. "
               "Because Fd is proportional to the jet diameter Dj, the "
               "frequency can be shifted upward, which increases pipe "
               "transmission loss. With n₀ = 16, Fd is 0.25 and the resultant "
               "peak frequency is 1/0.25, or four times that of a single "
               "orifice (Fd = 1) with the same total flow area:"))
    b.append(eq("n₀ = 16 → Fd = 0.25 → f_peak = 1/0.25 = 4×"))
    b.append(p("If the peak frequency falls in the mass-controlled region of "
               "the pipe, which is most likely, an overall reduction in the "
               "external (audible) sound level is achieved:"))
    b.append(eq("ΔT_Lfp = 20 log(f_pl / f^0.25) = 12 dB"))
    b.append(p("(unless a large pipe is involved). This approach is limited "
               "to about a 3:1 pressure ratio across the cage wall; at "
               "higher ratios the jets may combine downstream and negate the "
               "benefits of the high frequencies. One caution: Equation "
               "20-1 works only where the peak internal sound frequency fp "
               "is no more than two octaves (4×) above the pipe ring "
               "frequency fr:"))
    b.append(eq("f_p ≤ 4 f_r"))
    b.append(p("Below this ratio the internal sound shifts from 20 dB per "
               "octave to only 10 dB per octave. This typically occurs when "
               "a valve with low-noise trim (high fp) is installed in a "
               "large pipe, 12 in and larger."))
    b.append(fig(2, F.fig_f202(), lang="en"))

    b.append(h3("Labyrinth cage trim", "Labyrinth cage trim"))
    b.append(p("A more elaborate arrangement is shown in Figure 20-3: the "
               "multistep is combined with the multipath approach in layers "
               "of washer-like disks with individually cast or etched "
               "channels. The design brings both the beneficial effect of "
               "reduced velocity and the benefit of higher transmission loss "
               "from the increased frequency. Typical noise reductions are "
               "up to 30 dB."))
    b.append(fig(3, F.fig_f203(), lang="en"))

    b.append(h3("Two-stage multiarea trim", "Two-stage multiarea trim"))
    b.append(p("Figure 20-4 shows a recent improvement over the labyrinth "
               "trim: multiple identical layers of laser-cut plates that "
               "between them create a three-dimensional flow path, typically "
               "from a single streamlined passage on the inside of each disk "
               "to multiple nonstreamlined rectangular outlet passages at "
               "the outer circumference. The ratio of outlet to inlet "
               "passages is dictated by the overall pressure ratio across "
               "the valve. For maximum noise reduction the outlet stage is "
               "kept subsonic (where a less streamlined path has lower "
               "acoustic efficiency) while the first stage sees supersonic "
               "velocities. The streamlined passages act as supersonic "
               "diffusers, converting most of the pressure-reduction energy "
               "into shock waves rather than into turbulence, which is "
               "generally more sound-producing. A good portion of the sound "
               "energy from the first stage is also retained in the "
               "“settling space,” the vertical passage between the two "
               "stages. With an outlet-to-inlet area ratio of 6:1, the "
               "first-stage pressure ratio is typically 5:1, while the "
               "overall ratio across both stages can be as high as 8:1 with "
               "optimized low-noise performance. Because there is no long, "
               "tortuous path, this trim is much narrower than a typical "
               "labyrinth trim and therefore has more flow capacity for a "
               "given trim size. It is also less likely that the passages "
               "will plug if dust particles are present in the fluid — a "
               "problem typically associated with low gas velocities and "
               "fine flow passages."))
    b.append(fig(4, F.fig_f204(), lang="en"))

    b.append(h3("Fluted butterfly valve with a downstream restrictor",
                "Fluted butterfly valve with a downstream restrictor"))
    b.append(p("A more economical solution couples a static downstream "
               "pressure-reducing device, such as a multiple-hole restrictor, "
               "with a throttling valve such as the fluted-disk butterfly "
               "valve of Figure 20-5. The fluted disk generates multiple "
               "parallel jets with increased noise frequencies, much like a "
               "multiport cage valve, but most of the pressure energy is "
               "converted by the static plate, giving a noise reduction at "
               "maximum flow of about 20 dB. At maximum design flow the "
               "valve is sized for a low pressure ratio of 1.1 or 1.15, with "
               "the rest of the pressure reduction across the static plate, "
               "whose multistage, multihole design is inherently low-noise. "
               "Placing a silencer downstream of a valve is not cost-"
               "effective because its reduction is limited to about 10 dB: "
               "a good portion of the sound power travels upstream "
               "(particularly in line-of-sight valves such as butterfly and "
               "ball valves) or radiates through the valve body and "
               "actuator. Similar concerns limit acoustic pipe-wall "
               "insulation to about 15 dB."))
    b.append(fig(5, F.fig_f205(), lang="en"))

    b.append(h2("Summary of valve noise abatement procedures",
                "Summary of valve noise abatement procedures"))
    b.append(p("The following is a summary of valve noise abatement "
               "procedures:"))
    b.append(ul([
        "If Cv × F_L × P₁ is less than 1000, then no abatement is needed "
        "(SL ≤ 90 dBA).",
        "Use 1-inch-thick pipe insulation for a 5 to 10 dB reduction.",
        "Double the pipe wall thickness for a 6 dB reduction.",
        "Place a silencer downstream for a 10 dB reduction.",
        "Place silencers both upstream and downstream for a 20 dB reduction.",
        "Place a multiport resistance plate downstream of the valve for a 15 "
        "to 20 dB reduction (use only 5% to 10% of valve inlet pressure as "
        "valve ΔP at maximum flow).",
        "Use a special low-noise valve for a 15 to 30 dB reduction.",
        "Combine the above methods where appropriate; a combination can be "
        "more cost-effective.",
    ]))

    b.append(p("A note of caution: low-noise trims operating at high "
               "frequencies, typically between 5000 Hz and 20,000 Hz, can "
               "interfere with ultrasonic flow meters placed downstream of "
               "such valves. The high trim-produced frequencies can reduce "
               "the accuracy, or even cause failure, of such flow meters "
               "[2]."))

    b.append(note("<b>Source note.</b> (1) Chapter 20 occupies printed pp. "
                  "125–131 (PDF pp. 126–132). (2) The OCR text layer garbles "
                  "the mathematical symbols; the printed forms, including "
                  "P₁ × F_L², Equation 20-1, Fd = 1/(n₀)^0.5 and the "
                  "transmission-loss expression, were checked against page "
                  "renders of all seven pages. (3) Equation 20-1 is the only "
                  "numbered equation; the other printed expressions are "
                  "carried as unnumbered equation markup. (4) Two printed "
                  "details are kept as printed: the Figure 20-1 caption "
                  "describes 11 throttling steps while the worked example "
                  "uses a ten-step trim, and the butterfly-valve example "
                  "quotes a low pressure ratio of 1.1 or 1.15, whereas some "
                  "transcriptions give 1.1 or 1.5 — the printed reading is "
                  "used here. The five figures are redrawn as vectors from "
                  "the printed illustrations."))
    b.append(h3("References", "References"))
    b.append(refs([
        "C. Reed, “Optimizing Valve Jet Size and Spacing Reduces Valve Noise,” "
        "<i>Control Engineering</i> (September 1976): 63–64.",
        "E. W. Singleton, “An Investigation into Control Valve-Generated "
        "Turbulence and Noise,” <i>Measurement &amp; Control</i> 37, no. 6 "
        "(July 2004).",
    ]))
    return "".join(b)
