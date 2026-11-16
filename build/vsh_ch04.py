# -*- coding: utf-8 -*-
"""Book 6, Unit 4 — Fundamentals III: Flow Through Valves (EN/VI bilingual).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 28–46 (PDF pp. 42–59): resistance coefficient ζ (Equations 2-7/2-8/2-9,
Table 2-3, Figures 2-4…2-8), flow coefficients Cv/Kv/Av (Equations 2-12…2-18),
interrelationships (Equations 2-19…2-24), inherent vs installed flow
characteristics (Figures 2-9/2-10), cavitation (Equation 2-25, Figure 2-11),
waterhammer (Equations 2-26/2-27, Figure 2-12) and attenuation of valve noise.
"""

from vsh_common import (eq, fig, h2, h3, note, p, table, ul)
import vshfig as F

PAGES_SRC = 19          # source book pp. 28-46
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Fundamentals III — Flow Through Valves"
TITLE_VI = "Cơ sở III — Dòng chảy qua van"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 4.</b> resistance coefficient — hệ số "
                "trở lực (ζ) · flow coefficient — hệ số dòng (C<sub>v</sub>, "
                "K<sub>v</sub>, A<sub>v</sub>) · velocity head — cột áp vận "
                "tốc · vena contracta — tiết diện co hẹp nhỏ nhất · pressure "
                "recovery — thu hồi áp suất tĩnh · Borda-Carnot loss — tổn "
                "thất Borda-Carnot · inherent / installed characteristic — "
                "đặc tính dòng tự nhiên / lắp đặt · cavitation — xâm thực · "
                "incipient cavitation — xâm thực bắt đầu · waterhammer — "
                "waterhammer (cú nước va) · surge pressure — áp surge · "
                "Joukowsky — Joukowsky · bulk modulus — mô đun nén · "
                "perforated diffuser — ống khuếch tán khoan lỗ · open area "
                "ratio — tỉ lệ diện tích mở (σ) · Mach number — số Mach.")
    return ("<b>Key terms.</b> resistance coefficient (ζ) · flow coefficient "
            "(C<sub>v</sub>, K<sub>v</sub>, A<sub>v</sub>) · velocity head · "
            "vena contracta · pressure recovery · Borda-Carnot loss · "
            "inherent / installed characteristic · cavitation · incipient "
            "cavitation · waterhammer · surge pressure · Joukowsky · bulk "
            "modulus · perforated diffuser · open area ratio (σ) · Mach "
            "number.")


def _t23(lang):
    hdr = (["Kiểu van (mở hoàn toàn, dòng rối hoàn toàn)",
            "Khoảng ζ"] if lang == "vi" else
           ["Valve type (fully open, fully turbulent flow)", "ζ range"])
    rows = [
        ("Globe kiểu tiêu chuẩn — seat trọn lỗ, đúc",
         "4.0–10.0" if lang == "vi" else "4.0–10.0"),
        ("Globe tiêu chuẩn — seat trọn lỗ, rèn (chỉ cỡ nhỏ)",
         "5.0–13.0"),
        ("Globe kiểu chéo 45° — seat trọn lỗ, đúc", "1.0–3.0"),
        ("Globe kiểu góc — seat trọn lỗ, đúc", "2.0–5.0"),
        ("Globe kiểu góc — seat trọn lỗ, rèn (chỉ cỡ nhỏ)", "1.5–3.0"),
        ("Van cửa (gate) trọn lỗ", "0.1–0.3"),
        ("Van bi trọn lỗ", "0.1"),
        ("Van phích cổng chữ nhật — trọn dòng", "0.3–0.5"),
        ("Van phích cổng chữ nhật — 80% dòng", "0.7–1.2"),
        ("Van phích cổng chữ nhật — 60% dòng", "0.7–2.0"),
        ("Van phích cổng tròn trọn lỗ", "0.2–0.3"),
        ("Van bướm (tùy bề dày tấm)", "0.2–1.5"),
        ("Van màng kiểu đập chắn (weir)", "2.0–3.5"),
        ("Van màng thông suốt (straight-through)", "0.6–0.9"),
        ("Van một chiều kiểu lift (như globe)", "như globe"),
        ("Van một chiều kiểu swing", "1.0"),
        ("Van một chiều đĩa nghiêng (tilting-disc)", "1.0"),
    ] if lang == "vi" else [
        ("Globe valve, standard pattern — full bore seat, cast", "4.0–10.0"),
        ("Globe, standard pattern — full bore seat, forged (small sizes only)",
         "5.0–13.0"),
        ("Globe valve, 45° oblique pattern — full bore seat, cast", "1.0–3.0"),
        ("Globe valve, angle pattern — full bore seat, cast", "2.0–5.0"),
        ("Globe, angle pattern — full bore seat, forged (small sizes only)",
         "1.5–3.0"),
        ("Gate valve, full bore", "0.1–0.3"),
        ("Ball valve, full bore", "0.1"),
        ("Plug valve, rectangular port — full flow area", "0.3–0.5"),
        ("Plug valve, rectangular port — 80% flow area", "0.7–1.2"),
        ("Plug valve, rectangular port — 60% flow area", "0.7–2.0"),
        ("Plug valve, circular port, full bore", "0.2–0.3"),
        ("Butterfly valve, dependent on blade thickness", "0.2–1.5"),
        ("Diaphragm valve — weir type", "2.0–3.5"),
        ("Diaphragm valve — straight-through type", "0.6–0.9"),
        ("Lift check valve (as globe valve)", "as globe"),
        ("Swing check valve", "1.0"),
        ("Tilting-disc check valve", "1.0"),
    ]
    cap = ("Bảng 2-3 · Hệ số trở lực xấp xỉ của van mở hoàn toàn, dòng rối "
           "hoàn toàn (Re ≥ 10⁴) — giá trị điển hình; van cùng kiểu nhưng "
           "khác nhà sản xuất/cỡ thường không đồng dạng hình học (tr. 30)."
           if lang == "vi" else
           "Table 2-3 · Approximate resistance coefficients of fully open "
           "valves under fully turbulent flow (Re ≥ 10⁴) — typical values "
           "only; valves of the same type but different make or size are "
           "normally not geometrically similar (p. 30).")
    return table(hdr, rows, caption=cap, cls="tbl wide")


# ---------------------------------------------------------------------------
def body_vi():
    b = []
    b.append(p("Van có thể xem như một <b>cửa co điều khiển được</b> (control "
               "orifice) với diện tích mở dễ điều chỉnh. Vì vậy tổn thất ma "
               "sát qua van biến thiên theo dòng theo quan hệ tổng quát "
               "v ∝ (Δh)<sup>1/2</sup> và v ∝ (Δp)<sup>1/2</sup> (v vận tốc "
               "dòng, Δh tổn thất cột áp, Δp tổn thất áp suất). Với mỗi vị "
               "trí mở van, đã thiết lập nhiều quan hệ dòng–trở lực dùng các "
               "tham số trở lực/dòng xác định bằng thực nghiệm: <b>hệ số trở "
               "lực ζ</b> và, tùy hệ đơn vị, <b>các hệ số dòng C<sub>v</sub>, "
               "K<sub>v</sub>, A<sub>v</sub></b>. Thực hành chuẩn là quy các "
               "tham số này về cỡ danh nghĩa của van."))

    b.append(h2("Hệ số trở lực ζ", "Resistance coefficient ζ"))
    b.append(p("Hệ số ζ biểu diễn tổn thất ma sát do van gây ra trong đường "
               "ống theo cột áp vận tốc hoặc áp vận tốc:"))
    b.append(eq("Δh = ζ·v²/2g   (SI hoặc imperial liên hợp)", "2-7"))
    b.append(eq("Δp = ζ·v²ρ/2   (SI liên hợp)  ·  Δp = ζ·v²ρ/2g   (imperial "
                "liên hợp)", "2-8"))
    b.append(p("với ρ khối lượng riêng chất lỏng, g gia tốc trọng trường địa "
               "phương. Các phương trình đúng cho <b>dòng một pha của chất "
               "lỏng Newton</b>, cả dòng rối lẫn tầng, và dùng được cho khí ở "
               "<b>số Mach thấp</b>: khi Mach tại cửa vào van tiến về 0.2, "
               "hiệu ứng nén được bắt đầu thấy rõ nhưng thường chưa đáng kể "
               "ngay cả tới Mach 0.5."))
    b.append(_t23("vi"))
    b.append(p("Hệ số ζ của một cỡ/kiểu van cụ thể có thể <b>khác nhau "
               "đáng kể giữa các nhà sản xuất</b> vì thiếu đồng dạng hình học "
               "— Bảng 2-3 chỉ mang tính điển hình, áp dụng cho van mở hoàn "
               "toàn và Re ≥ 10⁴. Hệ số hiệu chỉnh <b>K<sub>1</sub></b> cho "
               "mở một phần lấy từ Hình 2-4 đến 2-7. <b>Engineering Sciences "
               "Data Unit</b> (London) bàn đầy đủ hơn về tổn thất áp suất "
               "trong van, gồm hệ số hiệu chỉnh cho Re &lt; 10⁴ và ảnh hưởng "
               "cỡ van lên ζ và độ tán xạ dữ liệu."))
    b.append(fig(4, F.fig_vsh_2_4()))
    b.append(fig(5, F.fig_vsh_2_5()))
    b.append(fig(6, F.fig_vsh_2_6()))
    b.append(fig(7, F.fig_vsh_2_7()))
    b.append(h3("Thu hồi áp suất trong đoạn co hẹp – phình rộng",
                "Pressure recovery in converging/diverging passages"))
    b.append(p("Với van mở một phần và van có diện tích seat giảm (đoạn dòng "
               "co hẹp–phình rộng), năng lượng dòng tại <b>tiết diện co hẹp "
               "nhỏ nhất (vena contracta)</b> chuyển một phần trở lại thành "
               "năng lượng tĩnh. Hình 2-8 cho thấy ảnh hưởng của thu hồi áp "
               "lên ζ của van cửa venturi mở hoàn toàn (khe giữa hai seat "
               "được nối liền bằng miếng mắt (eye piece)). Mức thu hồi phụ thuộc tỉ số "
               "đường kính đoạn dòng (d²/D²), góc loe (α/2) của đoạn phình, "
               "và chiều dài L đoạn ống thẳng sau họng van tính theo đường "
               "kính ống (d = đường kính họng van, D = đường kính ống)."))
    b.append(fig(8, F.fig_vsh_2_8()))
    b.append(p("Nếu đoạn ống thẳng sau họng van <b>≥ 12D</b>, tổn thất áp "
               "không thể vượt tổn thất <b>Borda-Carnot</b>:"))
    b.append(eq("Δh = (v<sub>d</sub> − v<sub>D</sub>)²/2g", "2-10"))
    b.append(p("với v<sub>d</sub> vận tốc dòng ở họng van, v<sub>D</sub> vận "
               "tốc trong ống. Tổn thất tối đa này xảy ra khi góc loe "
               "<b>α/2 &gt; 30°</b>; góc loe giảm dần thì tổn thất giảm và "
               "đạt giá trị thấp nhất ở <b>α/2 = 4°</b>. Nếu ống thẳng sau "
               "họng <b>&lt; 12D</b>, tổn thất tăng và đạt tối đa khi toàn "
               "bộ năng lượng tĩnh thu hồi được lại chuyển thành động năng "
               "và mất hẳn:"))
    b.append(eq("Δh = (v²<sub>d</sub> − v²<sub>D</sub>)/2g", "2-11"))
    b.append(p("Tổn thất tiến gần giá trị tối đa này khi van có đoạn dòng co "
               "hẹp–phình rộng <b>lắp sát ngay một header</b>."))

    b.append(h2("Các hệ số dòng C<sub>v</sub>, K<sub>v</sub>, A<sub>v</sub>",
                "Flow coefficients Cv, Kv, Av"))
    b.append(p("<b>C<sub>v</sub></b> nói lên lưu lượng của van: số gal (Mỹ)/"
               "phút nước ở 60°F đi qua van với tổn thất 1 lb/in² tại một vị "
               "trí mở cụ thể:"))
    b.append(eq("C<sub>v</sub> = Q·(Δp<sub>0</sub>/Δp × ρ/ρ<sub>0</sub>)"
                "<sup>1/2</sup>", "2-12"))
    b.append(p("với Q gal/phút; Δp<sub>0</sub> = 1 lb/in² (áp tham chiếu); "
               "ρ<sub>0</sub> = 62.4 lb/ft³ (nước). Vì ρ/ρ<sub>0</sub> = tỉ "
               "trọng G và Δp<sub>0</sub> = 1, phương trình thường viết:"))
    b.append(eq("C<sub>v</sub> = Q·(G/Δp)<sup>1/2</sup>", "2-13"))
    b.append(p("Quan hệ này nằm trong các tiêu chuẩn ISA S.39.1–S.39.4 và IEC "
               "Publication 534-1, áp dụng cho dòng một pha rối hoàn toàn của "
               "chất lỏng Newton; điều kiện dòng khác tham chiếu IEC 534-2 "
               "phần 1–2."))
    b.append(p("<b>K<sub>v</sub></b> là phiên bản của C<sub>v</sub> theo SI "
               "kép (mixed SI): số m³/giờ nước ở 5–40 °C đi qua van với tổn "
               "thất 1 bar:"))
    b.append(eq("K<sub>v</sub> = Q·(G/Δp)<sup>1/2</sup>", "2-15"))
    b.append(p("(chứa trong IEC Publication 534-1, cùng phạm vi áp dụng). "
               "<b>A<sub>v</sub></b> là phiên bản của K<sub>v</sub> theo SI "
               "liên hợp: số m³/giây nước ở 5–40 °C đi qua van với tổn thất "
               "1 Pascal:"))
    b.append(eq("A<sub>v</sub> = Q·(ρ/Δp)<sup>1/2</sup>", "2-16"))
    b.append(p("A<sub>v</sub> rút ra từ Phương trình 2-8, viết dưới dạng "
               "Q = A·(2/ζ)<sup>1/2</sup>·(Δp/ρ)<sup>1/2</sup>, với A tiết "
               "diện (m²); biểu thức A·(2/ζ)<sup>1/2</sup> được thay bằng "
               "A<sub>v</sub> (IEC Publication 534-1)."))
    b.append(h3("Quan hệ tương hỗ giữa các hệ số",
                "Interrelationships between coefficients"))
    b.append(p("Các hệ số trở lực/dòng <b>liên hệ được</b>: biết một hệ số, "
               "các hệ số khác tính được (d là ống tham chiếu — inch hoặc "
               "mm):"))
    b.append(eq("ζ = 889·d⁴<sub>in</sub>/C<sub>v</sub>²  ·  "
                "C<sub>v</sub> = 29.8·d²<sub>in</sub>/ζ<sup>1/2</sup>", "2-19"))
    b.append(eq("ζ = 665.2·d⁴<sub>in</sub>/K<sub>v</sub>²  ·  "
                "K<sub>v</sub> = 25.8·d²<sub>in</sub>/ζ<sup>1/2</sup>", "2-20"))
    b.append(eq("ζ = 512·d⁴<sub>in</sub>/(10⁹·A<sub>v</sub>²)  ·  "
                "A<sub>v</sub> = 716·d²<sub>in</sub>/(10⁶·ζ<sup>1/2</sup>)",
                "2-21"))
    b.append(eq("K<sub>v</sub>/C<sub>v</sub> = 865×10⁻³  ·  "
                "A<sub>v</sub>/C<sub>v</sub> = 23.8×10⁻⁶  ·  "
                "A<sub>v</sub>/K<sub>v</sub> = 27.8×10⁻⁶", "2-22"))

    b.append(h2("Đặc tính dòng và vị trí mở van",
                "Flow characteristic and valve opening position"))
    b.append(p("Quan hệ giữa <b>vị trí mở</b> (phân số) và <b>dòng tương "
               "đối</b> qua van gọi là <b>đặc tính dòng</b> (flow "
               "characteristic). Khi dòng tại mọi vị trí mở lấy ở áp suất "
               "đầu vào không đổi, đặc tính thu được gọi là <b>tự nhiên "
               "(inherent)</b> — Hình 2-9. Trong ứng dụng thực tế, tổn thất "
               "áp qua van thay đổi theo vị trí mở: Hình 2-10 minh họa hệ "
               "thống có bơm — phần trên là đường <b>áp bơm</b> (dòng theo "
               "áp bơm) và đường <b>tổn thất đường ống</b>; phần dưới là "
               "lưu lượng theo vị trí mở — gọi là <b>đặc tính dòng lắp đặt "
               "(installed)</b>, riêng cho mỗi installation. Khi mở van thêm "
               "để tăng dòng, áp tại cửa vào van giảm — nên tốc độ mở van "
               "cần thiết cao hơn chỉ dẫn của đặc tính tự nhiên."))
    b.append(fig(9, F.fig_vsh_2_9()))
    b.append(fig(10, F.fig_vsh_2_10()))
    b.append(p("Nếu đặc tính bơm–hệ thống cho thấy van phải hấp thụ <b>sụt áp "
               "cao</b>, nên định cỡ van sao cho sụt áp bắt buộc <b>không "
               "xảy ra gần vị trí đóng</b> — vì điều đó gây hư hại chỗ kín "
               "bởi dòng chảy. Cân nhắc này thường dẫn tới chọn cỡ van "
               "<b>nhỏ hơn</b> đường ống kề bên."))

    b.append(h2("Xâm thực của van", "Cavitation of valves"))
    b.append(p("Khi chất lỏng qua van mở một phần, áp tĩnh ở vùng vận tốc "
               "tăng và phía sau phần đóng <b>giảm và có thể chạm áp suất "
               "hơi</b> của chất lỏng; chất lỏng bốc hơi tạo <b>khối hang "
               "đầy hơi</b> lớn lên quanh các bọt khí nhỏ và tạp chất. Khi "
               "chất lỏng trở lại vùng áp tĩnh cao, các bọt hơi <b>sụp đột "
               "ngột (implode)</b> — đó là <b>xâm thực (cavitation)</b>. Sự "
               "va đập của các phần tử chất lỏng đối diện tạo áp cục bộ cao "
               "nhưng ngắn; nếu sụp xảy ra tại hoặc gần biên thân van/thành "
               "ống, cường độ áp có thể sánh độ bền kéo của các bộ phận này "
               "— đảo ứng suất nhanh trên bề mặt và xung áp trong lỗ rỗng "
               "dẫn tới <b>hỏng mỏi cục bộ</b>, bề mặt nhám dần rồi hình "
               "thành hốc lớn."))
    b.append(p("Hiệu năng xâm thực là đặc trưng của từng kiểu van, thường "
               "định lượng bằng một <b>chỉ số xâm thực</b>. Chỉ số thuận tiện "
               "của <b>United States Bureau of Reclamation</b>:"))
    b.append(eq("C = (P<sub>d</sub> − P<sub>v</sub>)/(P<sub>u</sub> − "
                "P<sub>d</sub>)", "2-25"))
    b.append(p("với P<sub>v</sub> áp suất hơi (so với khí quyển, âm), "
               "P<sub>d</sub> áp trong ống cách seat van 12 lần đường kính "
               "xuống dòng, P<sub>u</sub> áp trong ống cách seat 3 lần đường "
               "kính lên dòng. Hình 2-11 trình bày đặc tính xâm thực bắt đầu "
               "của van bướm, cửa, cầu và bi (nước), do Sydney Metropolitan "
               "Water Sewerage and Drainage Board tổng hợp — chỉ dùng được "
               "như <b>hướng dẫn</b> vì nhiệt độ, không khí lẫn, tạp chất, "
               "dung sai mô hình và phán đoán người quan sát đều ảnh hưởng "
               "kết quả."))
    b.append(fig(11, F.fig_vsh_2_11()))
    b.append(p("Phát triển xâm thực có thể hạn chế bằng cách cho sụt áp xảy "
               "ra <b>theo từng cấp</b>. Bơm khí nén ngay hạ lưu van hạn chế "
               "hình thành bọt hơi bằng cách <b>nâng áp môi trường</b> — "
               "nhưng không khí lẫn sẽ nhiễu phép đọc của mọi thiết bị đo "
               "hạ lưu. Việc <b>phình rộng đột ngột</b> của đoạn dòng ngay "
               "hạ lưu seat có thể bảo vệ biên thân van và ống khỏi hư hại "
               "xâm thực: buồng đường kính 1.5D và dài 8D (gồm cả đoạn loe "
               "ra) đã chứng minh thỏa đáng cho van kim (needle) trong "
               "trạm nước."))

    b.append(h2("Waterhammer từ vận hành van", "Waterhammer from valve "
                "operation"))
    b.append(p("Khi van mở/đóng để thay đổi lưu lượng, biến đổi năng lượng "
               "động của cột chất lỏng gây <b>biến thiên quá độ áp tĩnh</b> "
               "trong ống; với chất lỏng, biến thiên này đôi khi kèm rung "
               "râu ống và tiếng gõ — <b>waterhammer</b>. Biến thiên áp "
               "không xảy ra tức thời dọc toàn ống mà <b>tỏa ra dần</b> từ "
               "nơi khởi phát. Nếu van cuối đường ống đóng tức thời, chỉ các "
               "phần tử chất lỏng tại van cảm nhận ngay: năng động của chúng "
               "<b>nén chất lỏng và giãn thành ống</b>; phần còn lại của cột "
               "chất lỏng tiếp tục chảy với vận tốc cũ tới khi chạm cột đang "
               "đứng yên. Tốc độ tỏa vùng nén về phía cửa vào <b>bằng vận "
               "tốc âm trong chất lỏng trong ống</b>. Khi vùng nén chạm cửa "
               "vào, toàn bộ chất lỏng đứng yên ở áp cao hơn áp tĩnh bình "
               "thường; áp lệch gây dòng ngược, xóa sụt áp tăng và độ giãn "
               "thành; khi sóng giãn về tới van, cột chất lỏng trở về áp "
               "bình thường nhưng vẫn xả về phía cửa vào — tạo <b>sóng áp "
               "thấp</b> đi từ van; khi sóng đi hết lượt khứ hồi, áp bình "
               "thường và chiều dòng gốc được khôi phục — chu kỳ lặp lại tới "
               "khi năng động tiêu tán trong ma sát và các tổn thất khác."))
    b.append(p("<b>Joukowsky</b> chỉ ra rằng đóng van tức thời nâng áp tĩnh "
               "lên:"))
    b.append(eq("ΔP = a·v·ρ/B", "2-26"))
    b.append(eq("a = [K/ρ/B · (1 + K·D·c/(E·e))]^{1/2}", "2-26a"))
    b.append(p("với v vận tốc dòng bị dừng, a vận tốc truyền sóng áp, ρ khối "
               "lượng riêng, K mô đun nén của chất lỏng, E mô đun Young của "
               "vật liệu thành ống, D đường kính trong ống, e bề dày thành, "
               "c hệ số giới hạn ống (c = 1.0 cho ống không giới hạn); "
               "B = 1.0 (SI liên hợp) hoặc g = 32.174 ft/s² (imperial fps). "
               "Với <b>ống thép D/e = 35 chảy nước</b>: sóng truyền ~"
               "<b>1 200 m/s</b> (~4 000 ft/s) và áp tĩnh tăng <b>13.5 bar "
               "cho mỗi 1 m/s</b> (~60 lb/in² cho mỗi 1 ft/s) thay đổi vận "
               "tốc tức thời."))
    b.append(p("Nếu van đóng <b>trong thời gian khứ hồi của sóng áp "
               "2L/a</b> (L chiều dài đường ống), sóng phản hồi đầu tiên "
               "không triệt được sóng phát cuối cùng — sụt áp như đóng tức "
               "thời; gọi là đóng <b>nhanh (rapid)</b>. Đóng lâu hơn 2L/a thì "
               "các sóng phản hồi triệt một phần sóng phát — sụt áp tối đa "
               "giảm; gọi là đóng <b>chậm (slow)</b>. Để hạn chế áp surge cao "
               "bất thường, <b>van chặn nên vận hành chậm và đồng đều</b> về "
               "tốc độ thay đổi vận tốc dòng. <b>Van một chiều</b> được dòng "
               "chảy điều khiển nên tốc độ đóng phụ thuộc thiết kế van và "
               "đặc trưng giảm tốc của cột chất lỏng: nếu khoảng cách tới "
               "điểm phản xạ sóng <b>dài</b> và cao độ/áp tại đó <b>thấp</b> "
               "— hệ thống chấp nhận van một chiều đóng chậm; nếu <b>ngắn</b> "
               "và áp tại đó <b>cao</b> — dòng đảo gần tức thời (ví dụ trạm "
               "đa bơm khi một bơm chết đột ngột) và van phải đóng cực nhanh. "
               "Hướng dẫn chọn van một chiều theo tốc độ đóng xem Chương 4."))
    b.append(p("Nếu surge do <b>bơm dừng</b>, tính toán phải xét đặc trưng "
               "bơm và tốc độ thay đổi tốc độ bơm sau khi mất điện. Tính áp "
               "và vận tốc theo thời gian và vị trí trên ống có thể làm bằng "
               "phương pháp đồ thị/đại số cho trường hợp đơn giản; máy tính "
               "kỹ thuật số cho phép dùng <b>phương pháp số</b> với độ chính "
               "yếu tùy ý (tham chiếu 25)."))
    b.append(p("Khi không thể/thực tế không thể giảm waterhammer bằng điều "
               "chỉnh đặc tính van, hãy thay đổi đặc tính <b>hệ thống đường "
               "ống</b>: lắp một hoặc nhiều <b>thiết bị bảo vệ surge</b> tại "
               "vị trí chiến lược — ống đứng chứa khí tiếp xúc trực tiếp với "
               "chất lỏng hoặc cách ly bằng thành mềm, hoặc van an toàn áp "
               "suất. Waterhammer cũng thay đổi được bằng cách <b>thay đổi "
               "tính chất âm học của chất lỏng</b>: bơm bọt khí không tan "
               "trực tiếp vào dòng để giảm khối lượng riêng và mô đun nén "
               "hiệu dụng — hoặc bọc khí trong ống mềm chạy dọc ống. Khi có "
               "kể chỉ một lượng nhỏ khí, vai trò độ đàn hồi thành ống trở "
               "nên không đáng kể và vận tốc âm hiệu chỉnh:"))
    b.append(eq("a = (B·K/ρ)<sup>1/2</sup>", "2-27"))
    b.append(p("với K mô đun nén hiệu chỉnh = K<sub>l</sub>/[1 + "
               "(V<sub>g</sub>/V<sub>t</sub>)·(K<sub>l</sub>/K<sub>g</sub> "
               "− 1)] và ρ hiệu chỉnh = ρ<sub>g</sub>·V<sub>g</sub>/"
               "V<sub>t</sub> + ρ<sub>l</sub>·V<sub>l</sub>/V<sub>t</sub> "
               "(V<sub>g</sub>, V<sub>l</sub>, V<sub>t</sub>: thể tích khí, "
               "chất lỏng, toàn phần). Hình 2-12 cho thấy tác động của hàm "
               "lượng khí lên vận tốc sóng trong nước: <b>một lượng khí nhỏ "
               "đã làm tốc độ sóng thấp hơn tốc độ âm trong không khí</b> "
               "(khô, 20 °C, áp khí quyển: <b>318 m/s</b>)."))
    b.append(fig(12, F.fig_vsh_2_12()))

    b.append(h2("Giảm tiếng ồn của van", "Attenuation of valve noise"))
    b.append(p("Xả khí từ áp cao xuống áp thấp qua van có thể gây tiếng ồn "
               "phiền, trường hợp cực đoan khó chịu được. Phần lớn tiếng ồn "
               "sinh từ <b>độ loạn lưu do tia vận tốc cao xé môi trường tĩnh "
               "lại phía hạ lưu</b> van. Bộ giảm thanh hiệu quả là <b>ống "
               "khuếch tán khoan lỗ (perforated diffuser)</b> — tấm phẳng, "
               "nón hoặc xô khoan nhiều lỗ nhỏ, buộc khí chảy qua nhiều lỗ "
               "nhỏ. Diffuser giảm tần số thấp và trung của tiếng ồn van, "
               "nhưng tái sinh <b>tiếng ồn tần số cao</b> tại các lỗ — thứ "
               "tiếng này lại dễ giảm hơn khi truyền qua ống và không khí. "
               "Lợi ích thứ hai: phân bố dòng đều hơn trên tiết diện ống."))
    b.append(p("<b>Ingard</b> chỉ ra trở kháng âm quy chuẩn của tấm phẳng "
               "khoan lỗ đặt ngang ống tỉ lệ thuận với <b>số Mach</b> của "
               "dòng qua lỗ và với hệ số ((1 − σ)/σ)², với σ tỉ lệ diện tích "
               "mở của tấm khoan lỗ. Tuy không liên hệ trực tiếp được với "
               "mức giảm ồn, số Mach <b>càng lớn càng tốt và σ càng nhỏ càng "
               "tốt</b>: thực dụng đề nghị <b>Mach tối đa 0.9</b> (nếu sụt áp "
               "khả dụng qua diffuser hạn chế thì chọn Mach thấp hơn) và "
               "<b>σ = 0.1–0.3</b> (thấp hơn 0.1 → diffuser quá lớn; cao hơn "
               "0.3 → mức giảm ồn thấp). Tần số đỉnh của tiếng ồn tia <b>nghịch "
               "với đường kính tia</b> — vì vậy từ góc giảm ồn, đường kính "
               "lỗ nên nhỏ nhất có thể; để tránh bịt lỗ, lỗ <b>đường kính tối "
               "thiểu 5 mm</b> thường được dùng. Nếu vận tốc dòng trong ống "
               "hạ lưu bộ giảm thanh cao, độ loạn lưu lớp biên dọc ống có "
               "thể phát tiếng ồn sánh tiếng ồn van đã giảm — kinh nghiệm "
               "cho thấy giữ <b>Mach trong ống dưới ~0.3</b> sẽ không còn vấn "
               "đề. Dự đoán tiếng ồn van và hiệu năng bộ giảm thanh là việc "
               "phức tạp — xem các tham chiếu 29–35 của nguyên bản."))

    b.append(note("Ý chính: bốn thang đo cùng một tổn thất — ζ (trở lực) và "
                  "C<sub>v</sub>/K<sub>v</sub>/A<sub>v</sub> (dòng) liên hệ "
                  "được qua đường kính tham chiếu (P.t. 2-19…2-22). Bảng 2-3 "
                  "chỉ điển hình: ζ phụ thuộc nhà chế tạo. K<sub>1</sub> tăng "
                  "vọt khi mở nhỏ (Hình 2-4…2-7) — van hấp thụ sụt áp cao "
                  "nên chọn nhỏ hơn ống để không đóng gần seat. Xâm thực đo "
                  "bằng chỉ số C (P.t. 2-25); waterhammer đóng tức thời theo "
                  "Joukowsky ~13.5 bar/(m/s) với ống thép nước — phân biệt "
                  "đóng nhanh/chậm theo 2L/a, và chỉ một ít khí lẫn đã làm "
                  "sóng chậm dưới tốc độ âm không khí (Hình 2-12). Tiếng ồn "
                  "xả khí giảm bằng diffuser khoan lỗ: Mach ≈ 0.9, σ = 0.1–"
                  "0.3, lỗ ≥ 5 mm, Mach ống hạ lưu < 0.3."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học "
               "tập. Nội dung gốc © 2004 Elsevier Inc. (Gulf Professional "
               "Publishing).</i>"))
    return "".join(b)


# ---------------------------------------------------------------------------
def body_en():
    b = []
    b.append(p("Valves may be regarded as analogous to <b>control orifices</b> "
               "in which the area of opening is readily adjustable. As such, "
               "the friction loss across the valve varies with flow as "
               "v ∝ (Δh)<sup>1/2</sup> and v ∝ (Δp)<sup>1/2</sup> (v flow "
               "velocity, Δh headloss, Δp pressure loss). For any valve "
               "position, numerous relationships between flow and flow "
               "resistance have been established, using experimentally "
               "determined resistance or flow parameters: the <b>resistance "
               "coefficient ζ</b> and, depending on the system of units, the "
               "<b>flow coefficients C<sub>v</sub>, K<sub>v</sub> and "
               "A<sub>v</sub></b>. It is standard practice to base these "
               "parameters on the nominal valve size."))

    b.append(h2("Resistance coefficient ζ", "Hệ số trở lực ζ"))
    b.append(p("The resistance coefficient ζ defines the friction loss "
               "attributable to a valve in a pipeline in terms of velocity "
               "head or velocity pressure:"))
    b.append(eq("Δh = ζ·v²/2g   (coherent SI or imperial units)", "2-7"))
    b.append(eq("Δp = ζ·v²ρ/2   (coherent SI units)  ·  Δp = ζ·v²ρ/2g   "
                "(coherent imperial units)", "2-8"))
    b.append(p("where ρ is the fluid density and g the local acceleration "
               "due to gravity. The equations are valid for <b>single-phase "
               "flow of Newtonian liquids</b>, for both turbulent and "
               "laminar flow conditions, and may also be used for gas flow "
               "at <b>low Mach numbers</b>: as the Mach number at the valve "
               "inlet approaches 0.2, the effects of compressibility become "
               "noticeable but are unlikely to be significant even for Mach "
               "numbers up to 0.5."))
    b.append(_t23("en"))
    b.append(p("The resistance coefficient of a particular size and type of "
               "valve can differ <b>considerably between makes</b>, since "
               "valves of the same type but different manufacture or size "
               "are normally not geometrically similar — Table 2-3 can "
               "therefore provide only typical values, applying to fully "
               "open valves at Re ≥ 10⁴. The correction factor "
               "<b>K<sub>1</sub></b> for partial valve opening may be "
               "obtained from Figures 2-4 through 2-7. The <b>Engineering "
               "Sciences Data Unit</b> (London) deals more comprehensively "
               "with pressure losses in valves, covering correction factors "
               "for Re &lt; 10⁴ and the influence of valve size on the ζ "
               "value and scatter of data."))
    b.append(fig(4, F.fig_vsh_2_4()))
    b.append(fig(5, F.fig_vsh_2_5()))
    b.append(fig(6, F.fig_vsh_2_6()))
    b.append(fig(7, F.fig_vsh_2_7()))
    b.append(h3("Pressure recovery in converging/diverging passages",
                "Thu hồi áp suất trong đoạn co hẹp – phình rộng"))
    b.append(p("In partially open valves and valves with reduced seat area "
               "(converging/diverging flow passage), the energy of the flow "
               "stream at the <b>vena contracta</b> converts partially back "
               "into static energy. Figure 2-8 shows the influence of the "
               "pressure recovery on the resistance coefficient of fully "
               "open venturi-type gate valves, in which the gap between the "
               "seats is bridged by an eye piece. The amount of static "
               "energy recovered depends on the ratio of the diameters of "
               "the flow passage (d²/D²), the taper half-angle (α/2) of the "
               "diffuser, and the length L of straight pipe after the valve "
               "throat in terms of pipe diameter (d = valve throat diameter, "
               "D = pipe diameter)."))
    b.append(fig(8, F.fig_vsh_2_8()))
    b.append(p("If the straight length of pipe after the valve throat is "
               "<b>≥ 12D</b>, the pressure loss cannot exceed the "
               "<b>Borda-Carnot loss</b>:"))
    b.append(eq("Δh = (v<sub>d</sub> − v<sub>D</sub>)²/2g", "2-10"))
    b.append(p("with v<sub>d</sub> the flow velocity in the valve throat and "
               "v<sub>D</sub> in the pipeline. This maximum pressure loss "
               "occurs if the taper half-angle <b>α/2 &gt; 30°</b>; with a "
               "decreasing taper angle the pressure loss decreases and "
               "reaches its lowest value at <b>α/2 = 4°</b>. If the straight "
               "pipe after the throat is <b>&lt; 12D</b>, the pressure loss "
               "increases and reaches its maximum when the static energy "
               "converted into kinetic energy gets completely lost:"))
    b.append(eq("Δh = (v²<sub>d</sub> − v²<sub>D</sub>)/2g", "2-11"))
    b.append(p("The friction loss approaches this maximum value if the valve "
               "with a converging/diverging flow passage is <b>mounted "
               "directly against a header</b>."))

    b.append(h2("Flow coefficients Cv, Kv and Av",
                "Các hệ số dòng Cv, Kv, Av"))
    b.append(p("<b>C<sub>v</sub></b> states the flow capacity of a valve: the "
               "number of U.S. gal/min of water at 60 °F that will flow "
               "through the valve with a pressure loss of one pound per "
               "square inch at a specific opening position:"))
    b.append(eq("C<sub>v</sub> = Q·(Δp<sub>0</sub>/Δp × ρ/ρ<sub>0</sub>)"
                "<sup>1/2</sup>", "2-12"))
    b.append(p("where Q is in U.S. gal/min, Δp<sub>0</sub> = 1 lb/in² "
               "(reference differential pressure) and ρ<sub>0</sub> = "
               "62.4 lb/ft³ (reference fluid, water). Because ρ/ρ<sub>0</sub> "
               "= specific gravity G and Δp<sub>0</sub> = 1, the equation is "
               "normally presented as:"))
    b.append(eq("C<sub>v</sub> = Q·(G/Δp)<sup>1/2</sup>", "2-13"))
    b.append(p("This relationship is incorporated in ISA standards S.39.1 to "
               "S.39.4 and IEC Publication 534-1, and applies to single-"
               "phase, fully turbulent flow of Newtonian liquids; for other "
               "flow conditions refer to IEC Publication 534-2, Parts 1 and "
               "2."))
    b.append(p("<b>K<sub>v</sub></b> is a version of C<sub>v</sub> in mixed "
               "SI units: the number of m³/h of water at 5–40 °C that will "
               "flow through the valve with a pressure loss of one bar:"))
    b.append(eq("K<sub>v</sub> = Q·(G/Δp)<sup>1/2</sup>", "2-15"))
    b.append(p("(contained in IEC Publication 534-1, same scope of "
               "application.) <b>A<sub>v</sub></b> is a version of "
               "K<sub>v</sub> in coherent SI units: the number of m³/s of "
               "water at 5–40 °C that will flow through the valve with a "
               "pressure loss of one Pascal:"))
    b.append(eq("A<sub>v</sub> = Q·(ρ/Δp)<sup>1/2</sup>", "2-16"))
    b.append(p("A<sub>v</sub> is derived from Equation 2-8, presented as "
               "Q = A·(2/ζ)<sup>1/2</sup>·(Δp/ρ)<sup>1/2</sup> with A the "
               "cross-sectional area (m²); the expression A·(2/ζ)"
               "<sup>1/2</sup> is replaced by the single expression "
               "A<sub>v</sub> (IEC Publication 534-1)."))
    b.append(h3("Interrelationships between the coefficients",
                "Quan hệ tương hỗ giữa các hệ số"))
    b.append(p("Resistance and flow coefficients are <b>interrelated</b>: if "
               "one coefficient is known, the others can be calculated (d = "
               "reference pipe bore, inches or mm):"))
    b.append(eq("ζ = 889·d⁴<sub>in</sub>/C<sub>v</sub>²  ·  "
                "C<sub>v</sub> = 29.8·d²<sub>in</sub>/ζ<sup>1/2</sup>", "2-19"))
    b.append(eq("ζ = 665.2·d⁴<sub>in</sub>/K<sub>v</sub>²  ·  "
                "K<sub>v</sub> = 25.8·d²<sub>in</sub>/ζ<sup>1/2</sup>", "2-20"))
    b.append(eq("ζ = 512·d⁴<sub>in</sub>/(10⁹·A<sub>v</sub>²)  ·  "
                "A<sub>v</sub> = 716·d²<sub>in</sub>/(10⁶·ζ<sup>1/2</sup>)",
                "2-21"))
    b.append(eq("K<sub>v</sub>/C<sub>v</sub> = 865×10⁻³  ·  "
                "A<sub>v</sub>/C<sub>v</sub> = 23.8×10⁻⁶  ·  "
                "A<sub>v</sub>/K<sub>v</sub> = 27.8×10⁻⁶", "2-22"))

    b.append(h2("Relationship between resistance coefficient and valve "
                "opening position",
                "Đặc tính dòng và vị trí mở van"))
    b.append(p("The relationship between the <b>fractional opening "
               "position</b> and the <b>relative flow</b> through the valve "
               "is denoted as the <b>flow characteristic</b>. When flow at "
               "all valve opening positions is taken at constant inlet "
               "pressure, the characteristic is referred to as "
               "<b>inherent</b> — Figure 2-9. In most practical "
               "applications, however, the pressure loss through the valve "
               "varies with opening position: Figure 2-10 illustrates a flow "
               "system incorporating a pump — the upper portion shows the "
               "<b>pump characteristic</b> (flow against pump pressure) and "
               "the <b>system characteristic</b> (flow against pipeline "
               "pressure loss); the lower portion shows flow rate against "
               "valve opening position — the <b>installed valve flow "
               "characteristic</b>, unique for each valve installation. When "
               "the valve is opened further to increase the flow rate, the "
               "pressure at the valve inlet decreases — so the required rate "
               "of valve opening is higher than indicated by the inherent "
               "characteristic."))
    b.append(fig(9, F.fig_vsh_2_9()))
    b.append(fig(10, F.fig_vsh_2_10()))
    b.append(p("If the pump and system characteristic shows that the valve "
               "has to absorb a <b>high pressure drop</b>, the valve should "
               "be sized so that the required pressure drop does <b>not</b> "
               "occur near the closed position, since this will promote "
               "damage to the seatings from the flowing fluid. This "
               "consideration frequently leads to a valve size <b>smaller "
               "than the adjoining pipe</b>."))

    b.append(h2("Cavitation of valves", "Xâm thực của van"))
    b.append(p("When a liquid passes through a partially closed valve, the "
               "static pressure in the region of increasing velocity and in "
               "the wake of the closure member <b>drops and may reach the "
               "vapor pressure</b> of the liquid; the liquid then vaporizes "
               "and forms <b>vapor-filled cavities</b> growing around minute "
               "gas bubbles and impurities carried by the liquid. When the "
               "liquid again reaches a region of high static pressure, the "
               "vapor bubbles <b>collapse suddenly (implode)</b> — this "
               "process is called <b>cavitation</b>. The impinging of the "
               "opposing liquid particles of the collapsing bubble produces "
               "locally high but short-lived pressures; if the implosions "
               "occur at or near the boundaries of the valve body or pipe "
               "wall, the pressure intensities can match the tensile "
               "strength of these parts — rapid stress reversals on the "
               "surface and pressure shocks in the pores finally lead to "
               "<b>local fatigue failures</b> that roughen the boundary "
               "surface until quite large cavities form."))
    b.append(p("Cavitation performance is typical for a particular valve "
               "type and customarily defined by a <b>cavitation index</b>. "
               "A convenient index used by the <b>United States Bureau of "
               "Reclamation</b>:"))
    b.append(eq("C = (P<sub>d</sub> − P<sub>v</sub>)/(P<sub>u</sub> − "
                "P<sub>d</sub>)", "2-25"))
    b.append(p("where P<sub>v</sub> is the vapor pressure relative to "
               "atmospheric pressure (negative), P<sub>d</sub> the pressure "
               "in the pipe 12 pipe diameters downstream of the valve seat, "
               "and P<sub>u</sub> 3 pipe diameters upstream. Figure 2-11 "
               "displays the incipient cavitation characteristics of "
               "butterfly, gate, globe and ball valves (water), compiled by "
               "the Sydney Metropolitan Water Sewerage and Drainage Board — "
               "they can serve only as a <b>guide</b>, since temperature, "
               "entrained air, impurities, model tolerances and the "
               "observer's judgment influence the test results."))
    b.append(fig(11, F.fig_vsh_2_11()))
    b.append(p("The development of cavitation can be minimized by letting "
               "the pressure drop occur <b>in stages</b>. The injection of "
               "compressed air immediately downstream of the valve minimizes "
               "vapor-bubble formation by <b>raising the ambient "
               "pressure</b> — on the debit side, the entrained air "
               "interferes with the reading of any downstream "
               "instrumentation. A <b>sudden enlargement</b> of the flow "
               "passage just downstream of the valve seat can protect the "
               "boundaries of valve body and pipe: a chamber with a diameter "
               "of 1.5 pipe diameters and a length of 8 pipe diameters "
               "(including the exit taper) has proved satisfactory for "
               "needle valves in waterworks."))

    b.append(h2("Waterhammer from valve operation",
                "Waterhammer từ vận hành van"))
    b.append(p("When a valve is being opened or closed to change the flow "
               "rate, the change in kinetic energy of the flowing fluid "
               "column introduces a <b>transient change in the static "
               "pressure</b> in the pipe; with a liquid this is sometimes "
               "accompanied by a shaking of the pipe and a hammering sound — "
               "<b>waterhammer</b>. The transient pressure change does not "
               "occur instantaneously along the entire pipeline but "
               "<b>progressively</b> from the point at which the change of "
               "flow was initiated. If a valve at the end of a pipeline is "
               "closed instantaneously, only the liquid elements at the "
               "valve feel the closure immediately: their kinetic energy "
               "<b>compresses the liquid and expands the adjoining pipe "
               "walls</b>, while the rest of the column continues to flow at "
               "its original velocity until reaching the column at rest. The "
               "speed at which the compression zone extends towards the "
               "inlet end <b>equals the velocity of sound in the liquid "
               "within the pipe</b>. When the compression zone reaches the "
               "inlet, all liquid is at rest but at a pressure above normal; "
               "the unbalanced pressure creates a flow in the opposite "
               "direction, relieving the pressure rise and the pipe "
               "expansion; when this drop reaches the valve, the whole "
               "column is again at normal static pressure but still "
               "discharging towards the inlet — a wave of <b>subnormal "
               "pressure</b> starts at the valve; after the round trip, "
               "normal pressure and the original flow direction are "
               "restored — and the cycle repeats until the kinetic energy is "
               "dissipated in friction and other losses."))
    b.append(p("<b>Joukowsky</b> showed that instantaneous valve closure "
               "raises the static pressure by:"))
    b.append(eq("ΔP = a·v·ρ/B", "2-26"))
    b.append(eq("a = [K/ρ/B · (1 + K·D·c/(E·e))]^{1/2}", "2-26a"))
    b.append(p("where v is the velocity of arrested flow, a the velocity of "
               "pressure-wave propagation, ρ the liquid density, K the bulk "
               "modulus of the liquid, E Young's modulus of the pipe wall "
               "material, D the inside pipe diameter, e the wall thickness, "
               "c the pipe restriction factor (c = 1.0 for unrestricted "
               "piping); B = 1.0 (coherent SI) or g = 32.174 ft/s² (imperial "
               "fps). For <b>steel piping with D/e = 35 and water flow</b>: "
               "the pressure wave travels at approximately <b>1,200 m/s</b> "
               "(≈4,000 ft/s), and the static pressure increases by <b>13.5 "
               "bar per 1 m/s</b> (≈60 lb/in² per 1 ft/s) of instantaneous "
               "velocity change."))
    b.append(p("If the valve closes <b>within the time of a pressure-wave "
               "round trip 2L/a</b> (L = pipeline length), the first "
               "returning wave cannot cancel the last outgoing wave — the "
               "pressure rise is the same as for instantaneous closure; this "
               "speed of closure is said to be <b>rapid</b>. Closure taking "
               "longer than 2L/a lets returning waves cancel a portion of "
               "the outgoing waves, reducing the maximum pressure rise — "
               "<b>slow</b> closure. To minimize undue surge pressures, "
               "<b>stop valves should be operated slowly and uniformly</b> "
               "with respect to the rate of change of flow velocity. "
               "<b>Check valves</b> are operated by the flowing fluid, so "
               "their closure speed is a function of valve design and the "
               "deceleration characteristic of the retarding fluid column: "
               "if the distance between the check valve and the point of "
               "pressure-wave reflection is <b>long</b> and the elevation "
               "and pressure there are <b>low</b>, the system tolerates a "
               "slow-closing check valve; if the distance is <b>short</b> "
               "and the pressure <b>high</b>, flow reverses almost "
               "instantaneously (e.g. multipump installations where one pump "
               "fails suddenly) and the check valve must close extremely "
               "fast. Guidelines for selecting check valves for speed of "
               "closure are given in Chapter 4."))
    b.append(p("If the surge pressure is due to a <b>pump stopping</b>, the "
               "calculation must account for the pump characteristic and the "
               "rate of change of pump speed after power cut-off. Fluid "
               "pressure and velocity as functions of time and location can "
               "be computed graphically or algebraically for simple cases; "
               "digital computers have made <b>numerical methods</b> "
               "convenient, with solutions to any desired accuracy (see "
               "Reference 25)."))
    b.append(p("Where it is impossible or impractical to reduce waterhammer "
               "by adjusting the valve characteristic, consider changing the "
               "characteristic of the <b>piping system</b>: one or more "
               "<b>surge protection devices</b> at strategic locations — a "
               "standpipe containing gas in direct contact with the liquid, "
               "or separated from it by a flexible wall, or a pressure "
               "relief valve. Waterhammer effects can also be altered by "
               "deliberately changing the <b>acoustic properties of the "
               "fluid</b>: introducing bubbles of a non-dissolvable gas "
               "directly into the stream reduces the effective density and "
               "bulk modulus — a similar effect is achieved with gas "
               "enclosed in a flexible-walled conduit or hose running the "
               "length of the pipe. With even a small amount of gas present, "
               "pipe-wall elasticity becomes insignificant and the modified "
               "acoustic velocity is:"))
    b.append(eq("a = (B·K/ρ)<sup>1/2</sup>", "2-27"))
    b.append(p("with the modified bulk modulus K = K<sub>l</sub>/[1 + "
               "(V<sub>g</sub>/V<sub>t</sub>)·(K<sub>l</sub>/K<sub>g</sub> "
               "− 1)] and modified density ρ = ρ<sub>g</sub>·V<sub>g</sub>/"
               "V<sub>t</sub> + ρ<sub>l</sub>·V<sub>l</sub>/V<sub>t</sub> "
               "(V<sub>g</sub>, V<sub>l</sub>, V<sub>t</sub>: gas, liquid and "
               "total volume). Figure 2-12 shows the effect of air content "
               "on the wave propagation velocity in water: <b>a small amount "
               "of air drives the wave speed below the speed of sound in "
               "air</b> (dry air, 20 °C, atmospheric pressure: <b>318 "
               "m/s</b>)."))
    b.append(fig(12, F.fig_vsh_2_12()))

    b.append(h2("Attenuation of valve noise", "Giảm tiếng ồn của van"))
    b.append(p("Letting down gas by valves from a high to a low pressure can "
               "produce troublesome and, in extreme cases, unbearable noise. "
               "A major portion arises from the <b>turbulence generated by "
               "the high-velocity jet shearing the relatively still medium "
               "downstream</b> of the valve. A successful silencer is the "
               "<b>perforated diffuser</b> — a perforated flat plate, cone or "
               "bucket through which the gas is made to flow via numerous "
               "small orifices. The diffuser attenuates the low and mid "
               "frequencies of the valve noise but also regenerates <b>high "
               "frequency noise</b> in the perforations, which is more "
               "readily attenuated by the passage through the pipe and the "
               "air. A second benefit: the flow is distributed more evenly "
               "over the pipe cross section."))
    b.append(p("<b>Ingard</b> showed that the normalized acoustic resistance "
               "of a perforated flat plate mounted across the pipe is "
               "directly proportional to both the <b>Mach number</b> of the "
               "flow through the perforations and the factor ((1 − σ)/σ)², "
               "with σ the open-area ratio of the plate. Although this "
               "cannot be directly related to noise attenuation, the Mach "
               "number should be <b>as large as possible</b> and σ <b>as "
               "small as possible</b>: for practical purposes a maximum "
               "<b>Mach number of 0.9</b> is suggested (lower if the "
               "available pressure drop across the diffuser is limited), and "
               "practical <b>open-area ratios of 0.1–0.3</b> (below 0.1 → an "
               "excessively large diffuser; above 0.3 → too little "
               "attenuation). The peak frequency of the jet noise is also "
               "<b>inversely proportional to the jet diameter</b> — so from "
               "the noise-attenuation point of view the perforation diameter "
               "should be as small as possible; to avoid blocked nozzles, "
               "orifices with a <b>minimum diameter of 5 mm</b> are "
               "frequently used. If the flow velocity downstream of the "
               "silencer is high, boundary-layer turbulence along the pipe "
               "may generate noise comparable with the attenuated valve "
               "noise — experience suggests this is not a problem if the "
               "Mach number in the pipe is kept <b>below about 0.3</b>. "
               "Predicting valve noise and silencer performance is a complex "
               "matter — see References 29–35 of the source."))

    b.append(note("Central idea: four yardsticks for the same loss — ζ "
                  "(resistance) and C<sub>v</sub>/K<sub>v</sub>/A<sub>v</sub> "
                  "(flow) interconvert through the reference bore "
                  "(Eqs. 2-19…2-22). Table 2-3 is typical only: ζ depends on "
                  "the manufacturer. K<sub>1</sub> rises steeply at small "
                  "opening (Figures 2-4…2-7) — a valve absorbing a high drop "
                  "should be sized smaller than the pipe so the drop is not "
                  "taken near the closed position. Cavitation is measured by "
                  "the index C (Eq. 2-25); instantaneous-closure waterhammer "
                  "follows Joukowsky — ≈13.5 bar per m/s in steel water "
                  "piping — with rapid vs slow closure judged against 2L/a, "
                  "and even a little entrained air slowing the wave below "
                  "the speed of sound in air (Figure 2-12). Gas let-down "
                  "noise is combated with a perforated diffuser: Mach ≈ 0.9, "
                  "σ = 0.1–0.3, orifices ≥ 5 mm, downstream pipe Mach < 0.3."))
    b.append(p("<i>This is an unofficial translation for study purposes. "
               "Original content © 2004 Elsevier Inc. (Gulf Professional "
               "Publishing).</i>"))
    return "".join(b)
