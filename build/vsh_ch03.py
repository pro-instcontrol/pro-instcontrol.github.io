# -*- coding: utf-8 -*-
"""Book 6, Unit 3 — Fundamentals II: Valve Seatings, Gaskets and Stem Seals
(EN/VI bilingual).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 13–27 (PDF pp. 27–41): valve seatings (metal, sealants, soft — Tables 2-1
and 2-2), gaskets (flat metallic — Equation 2-2, exfoliated graphite, spiral
wound, blowout — Equations 2-3/2-4/2-5) and valve stem seals (compression
packings — Equation 2-6, Figure 2-3, stem corrosion, lip-, squeeze-, thrust-
type, diaphragm seals).
"""

from vsh_common import (eq, fig, h2, h3, note, p, table, ul)
import vshfig as F

PAGES_SRC = 15          # source book pp. 13-27
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Fundamentals II — Seatings, Gaskets and Stem Seals"
TITLE_VI = "Cơ sở II — Chỗ kín seat, gioăng đệm và gioăng trục van"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 3.</b> seating — chỗ kín (cặp bề mặt "
                "seat và phần đóng) · galling — dính ma sát (kết dính bề mặt "
                "trượt) · erosion — xói mòn · gasket — gioăng đệm · exfoliated "
                "graphite — graphit tách lớp · spiral wound gasket — gioăng "
                "xoắn ốc · gasket factor — hệ số gioăng (m) · blowout — bị thổi "
                "bay (gioăng bị đẩy ra) · stuffing box — hộp gioăng (hộp ép "
                "packing) · gland — nắp ép (bích ép packing) · packing — packing "
                "(dây làm kín trục) · Poisson's ratio — hệ số Poisson · "
                "lip-type / squeeze-type / thrust packing — packing môi / kiểu "
                "nén ép / kiểu đỡ trục · durometer — độ cứng Durometer · "
                "back-up ring — vòng đỡ (chống trượt extrusion) · diaphragm — "
                "màng ngăn · bellows — ống lò so.")
    return ("<b>Key terms.</b> seating · galling · erosion · gasket · "
            "exfoliated graphite · spiral wound gasket · gasket factor (m) · "
            "blowout · stuffing box · gland · packing · Poisson's ratio · "
            "lip-type / squeeze-type / thrust packing · durometer · back-up "
            "ring · diaphragm · bellows.")


# ---- Table 2-1: steam-jet erosion resistance of seating materials ----------
_T21 = [
    ("1 — < 0.0127 mm",
     "Stainless AISI 410 (13Cr) rèn tôi · Delhi hard (17Cr) · AISI 304 đúc · "
     "Stellite No. 6"),
    ("2 — 0.0127–0.0254 mm",
     "AISI 304 cán · AISI 316 hàn phủ hồ quang · Stellite No. 6 hàn ngọn lửa"),
    ("3 — 0.0254–0.0508 mm",
     "AISI 410 rèn cứng 444 Bhn · hợp kim nickel–copper–tin · mạ crôm trên "
     "đồng thau No. 4"),
    ("4 — 0.0508–0.1016 mm",
     "Đồng thau thân trục · Nitralloy 212 · Nitralloy Cr–V (770–950 Bhn) · "
     "Nitralloy Cr–Al (758 Bhn) · các biến thể Monel"),
    ("5 — 0.1016–0.2032 mm",
     "Đồng thau No. 4/5/22/24 · Nitralloy Cr–Al 1155 Bhn · Nitralloy Cr–V "
     "739 Bhn · Monel đúc"),
    ("6 — 0.2032–0.4064 mm",
     "Thép hợp kim thấp (C 0.16/Mo 0.27/Si 0.19/Mn 0.96; Cu 0.64/Si 1.37/"
     "Mn 1.42) · Ferro steel"),
    ("7 — 0.4064–0.8128 mm",
     "Đồng thau đỏ cán · gang xám · gang dẻo · thép các-bon 0.40 C"),
]


def _t21(lang):
    hdr = (["Cấp (thâm nhập 100 h)", "Vật liệu chỗ kín"] if lang == "vi"
           else ["Class (100 h penetration)", "Seating materials"])
    rows = _T21 if lang == "vi" else [
        ("1 — < 0.0127 mm (0.0005 in)",
         "Stainless AISI 410 (13Cr) bar forged, heat treated · Delhi hard "
         "(17Cr) · AISI 304 cast · Stellite No. 6"),
        ("2 — 0.0127–0.0254 mm",
         "AISI 304 wrought · AISI 316 arc deposit · Stellite No. 6 torch "
         "deposit"),
        ("3 — 0.0254–0.0508 mm",
         "AISI 410 forged, hardened 444 Bhn · nickel-base copper-tin alloy · "
         "chromium plate on No. 4 brass"),
        ("4 — 0.0508–0.1016 mm",
         "Brass stem stock · Nitralloy 212 · Nitralloy Cr-V (770–950 Bhn) · "
         "Nitralloy Cr-Al (758 Bhn) · Monel modifications"),
        ("5 — 0.1016–0.2032 mm",
         "Brass No. 4/5/22/24 · Nitralloy Cr-Al 1155 Bhn · Nitralloy Cr-V "
         "739 Bhn · Monel metal, cast"),
        ("6 — 0.2032–0.4064 mm",
         "Low-alloy steels (C 0.16/Mo 0.27/Si 0.19/Mn 0.96; Cu 0.64/Si 1.37/"
         "Mn 1.42) · Ferro steel"),
        ("7 — 0.4064–0.8128 mm",
         "Rolled red brass · grey cast iron · malleable iron · carbon steel "
         "0.40 C"),
    ]
    cap = ("Bảng 2-1 · Độ chống xói của vật liệu chỗ kín dưới tia hơi bão "
           "hòa Ø1.59 mm, 2.41 MPa, 100 h, cách mẫu 0.13 mm (Crane Co., tr. 14)."
           if lang == "vi" else
           "Table 2-1 · Erosion resistance of seating materials: 1.59 mm "
           "(1/16 in) jet of saturated steam at 2.41 MPa (350 psi) for 100 h "
           "on a specimen 0.13 mm away (Crane Co., p. 14).")
    return table(hdr, rows, caption=cap, cls="tbl wide")


# ---- Table 2-2: oxygen temperature rise under sudden compression -----------
_T22 = [("25 bar (360 lb/in²)", "375 °C (705 °F)"),
        ("50 bar (725 lb/in²)", "490 °C (915 °F)"),
        ("100 bar (1 450 lb/in²)", "630 °C (1 165 °F)"),
        ("150 bar (2 175 lb/in²)", "730 °C (1 345 °F)"),
        ("200 bar (2 900 lb/in²)", "790 °C (1 455 °F)")]


def _t22(lang):
    hdr = (["Độ tăng áp đột ngột", "Độ tăng nhiệt độ"] if lang == "vi"
           else ["Sudden pressure rise", "Temperature rise"])
    cap = ("Bảng 2-2 · Độ tăng nhiệt độ của oxygen nén đột ngột từ điều kiện "
           "khí quyển và 15 °C (tr. 16)." if lang == "vi" else
           "Table 2-2 · Experimentally determined temperature rise of oxygen "
           "suddenly pressurized from atmospheric pressure and 15 °C (p. 16).")
    return table(hdr, _T22, caption=cap, cls="tbl")


# ---------------------------------------------------------------------------
def body_vi():
    b = []
    b.append(p("Chỗ kín seat (seatings) là phần của seat và phần đóng tiếp xúc "
               "với nhau khi đóng van. Vì chỗ kín chịu <b>mài mòn trong quá trình "
               "tạo kín</b>, khả năng kín của nó giảm dần theo số lần vận hành — "
               "đây là yếu tố rất quan trọng khi chọn van cho một chức năng quá "
               "trình cụ thể."))

    b.append(h2("Chỗ kín kim loại", "Metal seatings"))
    b.append(p("Mài mòn vận hành không chỉ có ở van chỗ kín mềm: van chỗ kín "
               "kim loại cũng bị nếu dòng chất lỏng ăn mòn hoặc chứa hạt. Chỗ "
               "kín kim loại dễ <b>biến dạng do chất lỏng và hạt mài mòn bị kẹt</b>, "
               "bị hủy hoại thêm bởi ăn mòn, xói mòn (erosion) và mài mòn abrasion. "
               "Nếu kích thước hạt mài mòn <b>lớn hơn</b> độ lớn các gờ bất định "
               "bề mặt, độ nhám bề mặt xấu dần khi mài mòn; nếu hạt <b>nhỏ hơn</b>, "
               "bề mặt thô có xu hướng <i>được mài nhẵn dần</i>. Kích thước hạt phụ "
               "thuộc vật liệu, độ bôi trơn của chất lỏng và mức ô nhiễm chỗ kín "
               "bởi sản phẩm ăn mòn — cả hai đều làm hạt nhỏ lại."))
    b.append(p("Vật liệu chỗ kín phải được chọn theo <b>độ chống xói, ăn mòn và "
               "abrasion</b>; hỏng một tiêu chí có thể làm vật liệu vô dụng: ăn "
               "mòn của chất lỏng tăng tốc xói mòn rất mạnh, và vật liệu chống "
               "xói/ăn mòn giỏi vẫn có thể hỏng hoàn toàn do <b>dính ma sát "
               "(galling)</b> kém. Giải pháp tốt nhất đôi khi quá đắt cho hạng "
               "van đang xét — phải đánh đổi."))
    b.append(_t21("vi"))
    b.append(p("Theo Bảng 2-1, <b>AISI 410 (13Cr) tôi</b> gần như miễn nhiễm "
               "xói hơi. Tuy nhiên nếu chất lỏng <b>thiếu độ bôi trơn</b>, cặp "
               "tiếp xúc cùng loại 410 chỉ chống galling khá; hai chi tiết tiếp "
               "xúc nên <b>khác độ cứng</b>. Với hơi và các chất lỏng thiếu bôi "
               "trơn, cặp <b>410 + hợp kim copper-nickel</b> thường được dùng. "
               "<b>Stellite</b> (cobalt-nickel-chromium) thành công nhất chống "
               "xói và galling ở nhiệt độ cao, và chống ăn mòn với phổ chất "
               "ăn mòn rộng. API Std 600 liệt kê các vật liệu chỗ kín và tổ hợp "
               "thường dùng cho van thân thép."))
    b.append(h3("Làm kín bằng sealant", "Sealing with sealants"))
    b.append(p("Một số van có cơ chế <b>bơm định kỳ sealant</b> vào chỗ kín seat "
               "và trục để duy trì chỗ kín lâu dài. Khe rò giữa chỗ kín kim loại "
               "được sealant bơm vào sau khi van đóng bịt kín. Van chỗ kín kim "
               "loại hoàn toàn dựa vào phương pháp này là <b>van phích bôi trơn "
               "(lubricated plug valve)</b>; nhiều kiểu van khác cũng dùng bơm "
               "sealant như <b>chỗ kín khẩn cấp</b> khi chỗ kín gốc đã hỏng."))
    b.append(h3("Chỗ kín mềm", "Soft seatings"))
    b.append(p("Chỗ kín mềm rất hiệu quả nhưng dùng hạn chế ở nhiệt độ/áp suất "
               "cao; nhà sản xuất công bố phạm vi thiết kế tối đa/thiểu của sản "
               "phẩm. Một hoặc cả hai mặt chỗ kín là vật mềm (nhựa, cao su) — "
               "vật liệu dễ biến dạng theo mặt đối diện nên đạt độ kín <b>cực "
               "cao, lặp lại được</b>. Hạn chế: tương thích hóa học với chất lỏng "
               "và nhiệt độ."))
    b.append(p("Một giới hạn ít ngờ tới: khi van <b>đóng kín một hệ thống vừa "
               "được nạp đột ngột bằng khí áp cao</b>, khí nén tác động như "
               "piston lên khối khí trong hệ — <b>nhiệt nén</b> có thể đủ cao để "
               "phân hủy vật liệu chỗ kín mềm. Bảng 2-2 cho thấy mức tăng nhiệt "
               "của oxygen nén đột ngột từ 15 °C."))
    b.append(_t22("vi"))
    b.append(p("Trong van cầu, thiệt hại nhiệt được chống bằng <b>bẫy nhiệt "
               "(heat sink)</b> — nút kim loại diện tích hấp thụ lớn đặt trước "
               "phần tử chỗ kín mềm. Với dịch vụ <b>oxygen</b>, biện pháp này có "
               "thể chưa đủ để tránh phần tử chỗ kín bùng cháy; khi đó đoạn "
               "vào van phải kéo dài quá lỗ seat để tạo một <b>túi</b> chứa khí "
               "nóng xa chỗ kín. Khi thiết kế chỗ kín mềm, mối quan tâm chính là "
               "tránh phần tử mềm bị <b>đẩy dịch chuyển hoặc ép trượt (extrusion)</b> "
               "bởi áp suất chất lỏng."))

    b.append(h2("Gioăng đệm (gaskets)", "Gaskets"))
    b.append(h3("Gioăng kim loại phẳng", "Flat metallic gaskets"))
    b.append(p("Gioăng kim loại phẳng thích nghi với các gờ bất định của mặt "
               "bích bằng biến dạng đàn hồi và dẻo. Để hạn chế biến dạng dẻo của "
               "mặt bích, <b>ứng suất trượt dẻo</b> của vật liệu gioăng phải thấp "
               "hơn đáng kể so với mặt bích. Sự giãn ngang tự do của gioăng bị "
               "<b>độ nhám mặt bích</b> cản trở — lực cản này khiến vùng dẻo xâm "
               "nhập gioăng từ biên ngang, phần còn lại biến dạng đàn hồi trước. "
               "Nếu mặt bích thô đến mức gioăng không trượt được (hệ số ma sát "
               "0.5), gioăng không giãn cho tới khi các vùng dẻo gặp nhau ở tâm. "
               "Với gioăng vật liệu <b>không gia cứng biến dạng</b> đặt giữa hai "
               "mặt bích hoàn toàn thô, áp suất gioăng trung bình theo Lok xấp "
               "xỉ:"))
    b.append(eq("P<sub>m</sub> = 2k·(1 + w/4t)", "2-2"))
    b.append(p("với P<sub>m</sub> áp suất gioăng trung bình, k ứng suất trượt "
               "dẻo của vật liệu gioăng, w bề rộng gioăng, t bề dày. Nếu ma sát "
               "bằng không, áp suất gioăng không vượt quá 2k — <b>ma sát cao "
               "tăng khả năng chịu tải</b>. Lok chỉ ra hệ số ma sát dưới 0.5 "
               "nhưng không dưới 0.2 chỉ giảm nhẹ khả năng chịu tải; mặt bích "
               "gia công tinh có ma sát > 0.2, nhưng <b>nhôm</b> trên mặt bích "
               "mài gương chỉ đạt <b>0.05</b> — mức lấp đầy gờ rất thấp, vì vậy "
               "<i>không khuyến nghị đánh bóng mặt bích</i> dù đôi khi làm cho "
               "các mối nối quan trọng. Lok coi rãnh xoắn góc đỉnh 90°, sâu "
               "0.1 mm (125 rãnh/inch) là tiêu biểu cho cấp hơi và 0.01 mm "
               "(1 250 rãnh/inch) cho cấp nguyên tử; để lấp đầy rãnh mong muốn, "
               "quan hệ kích thước–áp suất: <b>cấp hơi wt &gt; 5 và "
               "P<sub>m</sub>/2k &gt; 2.25</b>; <b>cấp nguyên tử wt &gt; 16 và "
               "P<sub>m</sub>/2k &gt; 5</b>."))
    b.append(h3("Gioăng graphit tách lớp", "Gaskets of exfoliated graphite"))
    b.append(ul([
        "Không thấm khí và chất lỏng ở mức cao, không phụ thuộc nhiệt độ và "
        "thời gian.",
        "Chịu cực nhiệt: −200 °C đến 500 °C trong khí oxy hóa, tới 3 000 °C "
        "trong khí khử hoặc trơ.",
        "Chịu đa số thuốc thử (axit/bazơ vô cơ–hữu cơ, dung môi, dầu và sáp "
        "nóng); ngoại lệ: các chất oxy hóa mạnh (HNO<sub>3</sub> đậm đặc, "
        "H<sub>2</sub>SO<sub>4</sub> siêu đậm đặc, dung dịch Cr(VI)-"
        "permanganate, axit chloric, kim loại kiềm/kiềm thổ nóng chảy).",
        "Gioăng mật độ đầu 1.0 thích nghi dễ dàng với gờ bất định mặt bích "
        "kể cả ở áp bề mặt thấp; nén thêm độ đàn hồi tăng vọt — <b>chỗ kín "
        "hoạt động động</b>, ổn định từ nhiệt độ thấp tới hơn 3 000 °C, hấp "
        "thụ biến động áp suất/nhiệt độ và rung động bích.",
        "Phù hợp bích <i>nhạy cảm</i> — men sứ, thủy tinh, graphit.",
        "Gioăng lớn hoặc hình dạng phức tạp ghép từ các đoạn chồng mép — mối "
        "nối chồng không phải điểm yếu.",
        "Dùng được trong công nghiệp thực phẩm.",
    ]))
    b.append(p("Kiểu cấu tạo phổ biến: graphit phẳng; graphit có tấm thép "
               "chèn; graphit tấm thép chèn + ốp mép trong hoặc trong và ngoài; "
               "gioăng kim loại có rãnh phủ graphit; gioăng xoắn ốc. Do cấu trúc "
               "graphit, <b>gioăng phẳng dễ gãy và trầy xước</b> — thực dụng "
               "thường chọn loại có tấm thép chèn và xoắn ốc; tuy vậy độ mềm "
               "tự do của graphit phẳng thuận lợi cho một số ứng dụng."))
    b.append(h3("Gioăng xoắn ốc", "Spiral wound gaskets"))
    b.append(p("Gồm dải kim loại hình V <b>quấn ốc trên cạnh</b> và lớp phụ "
               "tạo kín mềm giữa các lớp; vài vòng đầu/cuối <b>hàn điểm</b> "
               "chống bung. Dải kim loại cho <b>độ đàn hồi</b> bù dịch chuyển "
               "nhỏ của bích; vật liệu phụ là môi tạo kín, chảy lấp gờ bất định "
               "mặt bích. Nhà sản xuất công bố mức nén lắp đặt để gioăng chịu "
               "đúng ứng suất và độ đàn hồi mong muốn; bề dày vận hành được "
               "khống chế bằng tải bu-lông, hoặc độ sâu recess trên bích, hoặc "
               "<b>vòng nén trong/ngoài</b> — vòng trong thêm nhiệm vụ che gioăng "
               "khỏi xói bởi dòng chất lỏng, vòng ngoài định vị gioăng trong "
               "đường kính bu-lông."))
    b.append(p("Khả năng chịu tải ở bề dày vận hành do <b>số vòng quấn trên "
               "đơn vị bề rộng</b> (mật độ gioăng) quyết định — nhờ đó gioăng "
               "xoắn ốc được <b>may đo</b> cho từng dải áp suất. Khe hở đường "
               "kính cho gioăng <b>không bị kẹp</b> (từ lòng ống tới Ø trong "
               "gioăng, và từ Ø ngoài tới mặt bích nhô) nên ≥ <b>6 mm</b> "
               "(1/4 inch); gioăng <b>bị kẹp</b> khuyến nghị 1.5 mm (1/16 inch). "
               "Lắp sai — gioăng nhô vào lòng ống hoặc vượt mặt bích nhô — "
               "chỗ kín bị suy giảm nghiêm trọng."))
    b.append(p("Vòng quấn kim loại thường là <b>thép không gỉ hoặc hợp kim "
               "nickel</b> (vật liệu tồn kho của đa số nhà sản xuất), có thể "
               "đặc chế: thép các-bon thấp, đồng, thậm chí vàng hoặc bạch kim. "
               "Với chất lỏng ăn mòn/nhiệt cao, xét <b>ăn mòn ứng suất và ăn "
               "mòn liên tinh</b>. Vật liệu phụ chọn theo tương thích chất lỏng "
               "và chịu nhiệt: <b>PTFE, graphit tinh khiết, mica với chất kết "
               "dính cao su hoặc graphit, giấy sợi gốm</b>. Vật liệu phụ cũng "
               "ảnh hưởng khả năng tạo kín: phụ asbestos/giấy gốm cần ứng suất "
               "ngồi cao hơn phụ mềm và kín hơn để đạt độ kín tương đương, và "
               "đòi hỏi kỹ hơn khi chọn độ nhám mặt bích."))
    b.append(p("Trong đa số ứng dụng thực tế, người dùng phải chấp nhận độ nhám "
               "mặt bích thương mại: với cùng hình học, độ nhám dao động phổ "
               "biến <b>3.2–12.5 µm Ra</b> (125–500 µin). <b>Tối ưu: 3.2–6.3 µm "
               "Ra</b> theo mô tả trong ANSI B16.5. Nhám hơn 6.3 µm Ra có thể "
               "cần ứng suất ngồi cao bất thường; nhám mượt hơn nhiều so với "
               "3.2 µm Ra cho hiệu quả kín kém — do ma sát gioăng–bích không đủ "
               "chặn dịch chuyển ngang của gioăng."))
    b.append(h3("Gioăng bị thổi bay", "Gasket blowout"))
    b.append(p("Gioăng <b>không bị kẹp</b> trong mối nối bích có thể bị <b>thổi "
               "bay</b> trước khi kịp rò rỉ cảnh báo nếu thiết kế bất cập. Kiểu "
               "hỏng này không xảy ra nếu lực ma sát tại các mặt gioăng vượt "
               "lực chất lỏng tác động theo hướng bán kính lên gioăng:"))
    b.append(eq("2µF ≥ P·t·πd<sub>m</sub>   ⟺   F ≥ P·t·πd<sub>m</sub>/2µ", "2-3"))
    b.append(eq("F ≥ w·P·m·πd<sub>m</sub>  (ngưỡng bắt đầu rò rỉ)", "2-4"))
    b.append(p("với µ hệ số ma sát, F tải làm việc của gioăng, P áp suất "
               "định mức chất lỏng, t bề dày, d<sub>m</sub> đường kính trung "
               "bình gioăng, w bề rộng, <b>m hệ số gioăng</b> — thước đo khả "
               "năng tạo kín, định nghĩa tỷ số giữa ứng suất dư của gioăng và "
               "áp suất chất lỏng bắt đầu phát sinh rò rỉ; xác định bằng thực "
               "nghiệm. Từ Phương trình 2-3 và 2-4, gioăng an toàn chống thổi "
               "bay <i>không cảnh báo rò rỉ trước</i> nếu:"))
    b.append(eq("w ≥ t/(2µm)", "2-5"))
    b.append(p("Krägeloh coi <b>m = 1.0 và µ = 0.1</b> là an toàn cho đa số "
               "ứng dụng thực tế — suy ra bề rộng gioăng <b>không nhỏ hơn năm "
               "lần bề dày</b> để chống thổi bay không cảnh báo."))

    b.append(h2("Gioăng trục van", "Valve stem seals"))
    b.append(h3("Packing nén", "Compression packings"))
    b.append(p("Packing nén là phần tử tạo kín trong <b>hộp gioăng</b> "
               "(stuffing box; xem Hình 3-17 đến 3-19): vật liệu mềm được nhồi "
               "vào hộp và <b>nén bằng gland</b> tạo chỗ kín quanh trục. Packing "
               "phải chịu cực nhiệt, chống môi trường ăn mòn, hệ số ma sát thấp, "
               "đủ độ bền kết cấu và không thấm chất lỏng. Chất bôi trơn: dầu/"
               "mỡ cho nước và dung dịch nước; xà phòng và chất không tan cho "
               "dầu/xăng. <b>Nhược điểm của chất bôi trơn lỏng</b>: khuếch tán "
               "dưới áp suất, nhất là nhiệt cao, làm packing <b>co và cứng</b> — "
               "phải siết lại định kỳ. Để hạn chế, hàm lượng lỏng trong packing "
               "trục van thường giữ <b>10% trọng lượng</b>. Với <b>PTFE</b>, "
               "chất bôi trơn rắn dùng được trong packing sợi mà không cần phụ "
               "gia lỏng."))
    b.append(p("<b>Asbestos</b> ngày càng được tránh, thay bằng sợi polyme "
               "PTFE và aramid, sợi/foil graphit tinh khiết; vật liệu khác: sợi "
               "thực vật (cotton, flax, ramie — thường bôi trơn PTFE) và dải "
               "kim loại xoắn/gấp. Kiểu cấu tạo sợi theo độ bền cơ học tăng "
               "dần: <b>loose fill, sợi xoắn, braid trên lõi xoắn, braid plait "
               "vuông, interbraid</b>; ba kiểu sau thường có <b>wire kim loại "
               "trong sợi</b> cho áp suất/nhiệt cao."))
    b.append(h3("Tác dụng làm kín của packing nén",
                "Sealing action of compression packings"))
    b.append(p("Tác dụng làm kín do khả năng <b>giãn ngang</b> ép sát thành trục "
               "van và thành hộp khi bị nén bởi gland. Ứng suất ngang của vật "
               "liệu đàn hồi bị giới hạn trong hộp, sinh ra bởi ứng suất trục, "
               "phụ thuộc <b>hệ số Poisson</b>:"))
    b.append(eq("σ<sub>1</sub> = σ<sub>a</sub>·µ/(1 − µ)", "2-6"))
    b.append(p("(bản gốc in phương trình dạng σ₁ = σa · µ/(1−µ); ký hiệu "
               "trình bày theo nghĩa: σ<sub>1</sub> ứng suất ngang, "
               "σ<sub>a</sub> ứng suất trục, µ hệ số Poisson = tỷ số giãn "
               "ngang/nén trục.) Ứng suất ngang "
               "bằng ứng suất trục chỉ khi <b>µ = 0.5</b> — vật liệu không nén "
               "được về khối. <b>Cao su mềm</b> có µ ≈ 0.5 — truyền áp gần như "
               "chất lỏng. <b>PTFE rắn</b>: µ = 0.46 ở 23 °C và 0.36 ở 100 °C — "
               "truyền tương ứng <b>85% và 56%</b> ứng suất trục sang mặt ngang. "
               "Các vật liệu packing khác nén được nhiều hơn nên µ considerably "
               "thấp hơn 0.5."))
    b.append(p("Khi packing như vậy bị nén trong hộp, <b>co trục</b> sinh ma sát "
               "với thành, cản truyền lực gland tới đáy packing — <b>sụt áp "
               "packing theo trục rất nhanh</b> (giá trị lý thuyết tính được, "
               "áp dụng cho điều kiện tĩnh; khi trục chuyển động, phân bố thực "
               "khó phân tích). Phân bố còn phụ thuộc <b>cách lắp</b>: dây vuông "
               "bị bẻ cong quanh trục thành hình thang — áp cạnh trong cao hơn "
               "cạnh ngoài."))
    b.append(p("Khi áp suất chất lỏng dưới đáy packing vượt ứng suất ngang, "
               "<b>khe hở mở ra giữa packing và mặt ngang</b>, chất lỏng tràn "
               "vào; ở áp thấp, gland phải siết lại để duy trì kín. Ở áp suất "
               "đủ cao, tạo kín xảy ra <b>ngay dưới gland</b> — nơi chất lỏng "
               "cố ép packing xuyên qua khe gland; tạo kín trở thành <b>tự "
               "động</b>. Số liệu gradient áp suất dọc hộp gioăng trục quay "
               "(Hình 2-3) xác nhận cơ chế này: áp thấp — gradient gần đều; áp "
               "cao — <b>90% sụt áp qua vòng packing ngay dưới gland</b>. Vì "
               "vậy với áp cao, vòng dưới gland là quan trọng nhất — chọn chống "
               "extrusion và mài mòn, lắp cẩn thận; và <b>hộp gioăng dài thêm "
               "cho áp cao không phục vụ mục đích</b>."))
    b.append(fig(4, F.fig_vsh_2_3()))
    b.append(p("Nếu packing <b>không nén được</b> (cao su mềm), áp trục do gland "
               "sinh ra ứng suất ngang <b>đều trên toàn chiều dài</b>; áp chất "
               "lỏng tăng ứng suất ngang thêm đúng bằng áp chất lỏng — tạo kín "
               "<b>tự động</b> khi đã có can thiệp ban đầu. Nhưng cao su <b>bám "
               "trục</b> cản trở vận hành trừ khi mặt trong trượt trơn — vì vậy "
               "cao su thường dùng dạng <b>O-ring</b>, mặt tiếp xúc hẹp."))
    b.append(h3("Ăn mòn trục van thép không gỉ do packing",
                "Corrosion of stainless steel valve stems by packings"))
    b.append(p("Trục <b>AISI 410 (13Cr)</b> hay bị ăn mòn ngay tại chỗ tiếp "
               "xúc packing — thường trong <b>kho lưu trữ sau thử thủy tĩnh</b> "
               "khi packing thấm nước; đưa vào vận hành ngay sau thử thì không "
               "bị. Nghiên cứu của H. J. Reynolds, Jr.: cơ chế là môi trường "
               "<b>khử khí (deaerated)</b> mà packing ép tạo ra trên bề mặt thép "
               "— nhiều <b>anode nhỏ</b> hình thành tại các điểm thiếu oxygen "
               "nhạy cảm trên màng oxide bảo vệ, trong khi khối kim loại thụ "
               "động còn lại làm <b>cathode</b> — tạo <b>pin galvanic</b> trong "
               "chính vật liệu. <b>Graphite</b> trong packing làm cathode đối "
               "với vùng anode hoạt động, làm nặng thêm tấn công qua mật độ "
               "dòng galvanic tăng. Vì cơ chế này, packing <i>phi ăn mòn</i> bằng "
               "nguyên liệu <i>không ăn mòn</i> là vô dụng — phải <b>pha chất ức "
               "chế</b>: trong các chất ức chế anode, chỉ những chất chứa anion "
               "oxy hóa như <b>sodium nitrite</b> hiệu quả; bảo vệ cathode bằng "
               "kim loại hy sinh như <b>kẽm</b> cũng tốt; bảo vệ tốt nhất với "
               "ảnh hưởng tối thiểu lên tính nén: <b>sodium nitrite phân tán "
               "đồng nhất + lớp kẽm bụi</b>. Thép không gỉ <b>hàm lượng crôm "
               "cao — nhất là có nickel</b> — chống lại tốt hơn rõ rệt với "
               "packing có ức chế."))
    b.append(h3("Packing môi (lip-type)", "Lip-type packings"))
    b.append(p("Packing môi giãn ngang nhờ <b>độ mềm của môi</b>, được áp "
               "chất lỏng đẩy vào mặt tường — cho phép dùng vật liệu cứng hơn "
               "mà packing nén không chịu được. Nhược điểm: tạo kín <b>một "
               "chiều</b>. Đa số packing môi cho trục van là <b>PTFE nguyên "
               "hoặc đổ đầy</b>; cao su gia cường vải và da dùng chủ yếu thủy "
               "lực. Hình dáng phổ biến <b>hình V</b> — tiện cho không gian "
               "packing hẹp. Vòng V bằng PTFE/cao su gia cường <b>tiếp nhau ở "
               "vùng nhỏ gần đầu môi</b>, khe hở vùng lớn để áp chất lỏng tác "
               "động tự do lên môi; vòng V bằng da kém cứng hơn nên <b>đỡ nhau "
               "đầy đủ</b>. Vòng V PTFE/cao su thường có <b>môi loe</b> tự "
               "tải trước mặt tường — chỉ cần siết nhẹ ban đầu; vòng da thành "
               "thẳng cần tải trước trục cao hơn. Khi ma sát thấp quan trọng "
               "(van điều khiển tự động), packing thường được <b>tải từ đáy "
               "bằng lò so</b> cường độ định trước để tránh quá tải bằng tay."))
    b.append(h3("Packing nén ép (squeeze-type)", "Squeeze-type packings"))
    b.append(p("Tên gọi áp cho <b>O-ring và tương tự</b>: lắp với <b>nén "
               "ngang</b>, dựa <b>biến dạng đàn hồi</b> để giữ tải trước ngang. "
               "Khi áp chất lỏng vào đáy, packing <b>trượt về phía khe hở</b> "
               "giữa trục và giá đỡ hậu — <b>bịt lối rò</b>; khi xả áp, packing "
               "trở lại hình ban đầu. Vì cần biến dạng dẻo giới hạn cao, đa số "
               "làm bằng <b>elastomer</b>. Extrusion bị khống chế bởi <b>bề "
               "rộng khe hở</b> và <b>độ cứng elastomer</b> (module đàn hồi — "
               "nhà sản xuất diễn đạt qua <b>độ cứng Durometer</b>, cùng Durometer "
               "có thể ứng module khác nhau giữa các nhóm hợp chất). Khe rất "
               "nhỏ được khống chế bằng <b>vòng đỡ da hoặc nhựa</b> ôm sát trục. "
               "Nhà sản xuất O-ring có bảng liên hệ Durometer – khe hở – áp "
               "suất an toàn chống extrusion."))
    b.append(h3("Packing đỡ trục (thrust)", "Thrust packings"))
    b.append(p("Gồm một <b>vòng hoặc đệm packing</b> đặt giữa hai vai (shoulder) "
               "trên bonnet và trục — trục tự do trục hướng chống lại vòng "
               "packing. Chỗ kín ban đầu do một packing radial bổ sung (kiểu "
               "nén) hoặc một <b>lò so</b> đẩy vai trục vào vòng đỡ; áp chất "
               "lỏng sau đó ép vai trục tiếp xúc sát hơn. Packing đỡ trục gặp "
               "nhiều trong <b>van bi</b> (Hình 3-61 đến 3-63, 3-65, 3-67)."))
    b.append(h3("Gioăng trục kiểu màng", "Diaphragm valve stem seals"))
    b.append(p("Màng là <b>nắp van chứa áp dạng mềm</b> nối trục với phần đóng "
               "— không cho rò rỉ qua trục ra khí quyển, <b>trừ khi màng nứt</b>. "
               "Hình dạng có thể là <b>vòm</b> (như van ở Hình 3-7) hoặc "
               "<b>ống lò so (bellows)</b> (như Hình 3-6 và 3-39), tùy ứng "
               "dụng."))

    b.append(note("Ý chính: chỗ kín kim loại sống chết với <b>galling</b> khi "
                  "chất lỏng thiếu bôi trơn — chọn cặp vật liệu khác độ cứng "
                  "hoặc Stellite; chỗ kín mềm chết bởi <b>nhiệt nén</b> khi "
                  "nạp khí đột ngột (Bảng 2-2). Gioăng phẳng chịu tải nhờ "
                  "<b>ma sát mặt bích</b> (đừng đánh bóng); chống thổi bay "
                  "cần <b>bề rộng ≥ 5×bề dày</b> (P.t. 2-5). Packing nén chỉ "
                  "tự động ở áp cao — 90% sụt áp tại vòng dưới gland (Hình "
                  "2-3) — và hộp dài không giúp gì; trục 13Cr ăn mòn trong "
                  "kho sau thử thủy tĩnh vì pin galvanic, khắc phục bằng "
                  "sodium nitrite + kẽm trong packing."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. "
               "Nội dung gốc © 2004 Elsevier Inc. (Gulf Professional "
               "Publishing).</i>"))
    return "".join(b)


# ---------------------------------------------------------------------------
def body_en():
    b = []
    b.append(p("Valve seatings are the portions of the seat and closure member "
               "that contact each other for closure. Because the seatings are "
               "subject to <b>wear during the making of the seal</b>, the "
               "sealability of the seatings tends to diminish with operation — "
               "a very important factor in selecting a valve for a specific "
               "process function."))

    b.append(h2("Metal seatings", "Chỗ kín kim loại"))
    b.append(p("Operational wear is not limited to soft-seated valves: metal "
               "seatings suffer too if the fluid is corrosive or carries "
               "particles. Metal seatings are prone to <b>deformation by "
               "trapped fluids and wear particles</b>, further damaged by "
               "corrosion, erosion and abrasion. If the wear-particle size is "
               "<b>large</b> compared with the surface irregularities, the "
               "finish deteriorates as the seatings wear in; if particles are "
               "<b>small</b>, a coarse finish tends to improve. Particle size "
               "depends on the material, the lubricity of the fluid and the "
               "contamination of the seatings with corrosion and fluid "
               "products — both reduce it."))
    b.append(p("Seating material must be selected for resistance to <b>erosion, "
               "corrosion and abrasion</b>; failing one requirement can make it "
               "completely unsuitable: corrosive action greatly accelerates "
               "erosion, and a material highly resistant to both may fail "
               "completely through poor <b>galling</b> resistance. The best "
               "material may also be too expensive for the class of valve — a "
               "compromise may have to be made."))
    b.append(_t21("en"))
    b.append(p("Per Table 2-1, heat-treated <b>AISI 410 (13Cr)</b> is "
               "particularly impervious to steam erosion. If, however, the "
               "fluid <b>lacks lubricity</b>, type 410 in like contact offers "
               "only fair galling resistance unless the mating components "
               "differ in hardness. For steam and other non-lubricating "
               "fluids, a combination of <b>410 stainless and copper-nickel "
               "alloy</b> is frequently used. <b>Stellite</b> (cobalt-nickel-"
               "chromium) has proved most successful against erosion and "
               "galling at elevated temperatures, and against corrosion for a "
               "wide range of corrosives. API Std 600 lists seating materials "
               "and combinations frequently used in steel valves."))
    b.append(h3("Sealing with sealants", "Làm kín bằng sealant"))
    b.append(p("Certain valves have the facility to periodically introduce "
               "<b>sealants</b> into the valve seat and stems to maintain an "
               "effective seal over an extended period. The leakage passages "
               "between metal seatings are closed by sealant injected after "
               "the valve is closed. The metal-seated valve relying completely "
               "on this method is the <b>lubricated plug valve</b>; other valve "
               "types also use sealant injection as an <b>emergency seat "
               "seal</b> after the original seal has failed."))
    b.append(h3("Soft seatings", "Chỗ kín mềm"))
    b.append(p("Soft seats are very effective but limited at high temperatures "
               "and pressures; proprietary manufacturers state the maximum and "
               "minimum design pressures and temperatures. One or both seating "
               "faces consist of a soft material (plastic, rubber) that "
               "conforms readily to the mating face — an extremely high degree "
               "of fluid tightness, achieved <b>repeatedly</b>. Limits: "
               "compatibility with the fluid, and temperature."))
    b.append(p("A sometimes unexpected limitation: when the valve shuts off a "
               "system suddenly filled with gas at high pressure, the "
               "high-pressure gas acts like a piston on the gas already in the "
               "system — the <b>heat of compression</b> can disintegrate the "
               "soft seating material. Table 2-2 shows the magnitude of the "
               "rise for oxygen compressed suddenly from 15 °C."))
    b.append(_t22("en"))
    b.append(p("In globe valves, heat damage is combated by a <b>heat sink</b> "
               "— a metallic button with a large heat-absorbing surface ahead "
               "of the soft seating element. In <b>oxygen</b> service this may "
               "not suffice to stop the element bursting into flames; the "
               "inlet passage may have to be extended beyond the seat passage "
               "so its end forms a <b>pocket</b> where the hot gas accumulates "
               "away from the seatings. The main design consideration for soft "
               "seatings is to prevent the element from being <b>displaced or "
               "extruded</b> by the fluid pressure."))

    b.append(h2("Gaskets", "Gioăng đệm (gaskets)"))
    b.append(h3("Flat metallic gaskets", "Gioăng kim loại phẳng"))
    b.append(p("Flat metallic gaskets adapt to the irregularities of the flange "
               "face by elastic and plastic deformation. To inhibit plastic "
               "deformation of the flange face, the <b>yield shear strength</b> "
               "of the gasket material must be considerably lower than that of "
               "the flange. Free lateral expansion of the yielding gasket is "
               "resisted by the <b>roughness of the flange face</b> — the "
               "yield zone enters the gasket from its lateral boundaries while "
               "the remainder deforms elastically. If the face is rough enough "
               "to prevent slippage altogether (friction factor 0.5), the "
               "gasket will not expand until the yield zones meet at its "
               "centre. For gaskets of a non-strain-hardening material between "
               "perfectly rough flange faces, the mean gasket pressure is, "
               "after Lok, approximately:"))
    b.append(eq("P<sub>m</sub> = 2k·(1 + w/4t)", "2-2"))
    b.append(p("where P<sub>m</sub> is the mean gasket pressure, k the yield "
               "shear stress of the gasket material, w the gasket width and t "
               "its thickness. With zero friction the gasket pressure could "
               "not exceed 2k — a <b>high friction factor improves the "
               "load-bearing capacity</b>. Lok showed that a friction factor "
               "below 0.5 but not below 0.2 diminishes the capacity only "
               "slightly; finely machined faces exceed 0.2, but <b>aluminum "
               "gaskets on lapped faces</b> reach only <b>0.05</b> — the "
               "degree of filling of the surface irregularities is then very "
               "low, so <i>polishing the flange face is not recommended</i>, "
               "even as sometimes done for important joints. Lok considered "
               "spiral grooves with a 90° apex angle and 0.1 mm depth (125 "
               "grooves per inch) representative for the steam class, and "
               "0.01 mm (1,250 grooves per inch) for the atom class; the "
               "dimensional and pressure-stress relationships to achieve the "
               "desired filling are: <b>steam class wt &gt; 5 and "
               "P<sub>m</sub>/2k &gt; 2.25</b>; <b>atom class wt &gt; 16 and "
               "P<sub>m</sub>/2k &gt; 5</b>."))
    b.append(h3("Gaskets of exfoliated graphite",
                "Gioăng graphit tách lớp"))
    b.append(ul([
        "Highly impermeable to gases and liquids, irrespective of temperature "
        "and time.",
        "Resists temperature extremes: −200 °C to 500 °C in oxidizing "
        "atmosphere, up to 3,000 °C in reducing or inert atmosphere.",
        "Resists most reagents (inorganic/organic acids and bases, solvents, "
        "hot oils and waxes); exceptions are strongly oxidizing compounds "
        "(concentrated nitric acid, highly concentrated sulfuric acid, "
        "chromium(VI)-permanganate solutions, chloric acid, molten alkali "
        "and alkaline-earth metals).",
        "Gaskets of initial density 1.0 conform readily to flange-face "
        "irregularities even at low surface pressures; further compression "
        "sharply increases resilience — a <b>dynamically behaving seal</b>, "
        "constant from lowest temperatures beyond 3,000 °C, absorbing "
        "pressure/temperature load changes and flange vibrations.",
        "Suitable for sensitive flanges — enamel, glass, graphite.",
        "Large or complicated gaskets can be built from overlapping "
        "segments; the lapped joints are not weak points.",
        "Usable without misgivings in the food industry.",
    ]))
    b.append(p("Common constructions: plain graphite; graphite with steel "
               "sheet inserts; inserts plus inner or inner-and-outer edge "
               "cladding; grooved metal gaskets with graphite facings; spiral "
               "wound. Because of the graphite structure, <b>plain gaskets are "
               "sensitive to breakage and surface damage</b> — steel-insert "
               "and spiral-wound types are commonly preferred, though the "
               "unrestrained flexibility of plain graphite facilitates sealing "
               "in some applications."))
    b.append(h3("Spiral wound gaskets", "Gioăng xoắn ốc"))
    b.append(p("A V-shaped metal strip <b>spirally wound on edge</b> with a "
               "soft filler inlay between the laminations; several turns at "
               "start and finish are <b>spot-welded</b> against unwinding. The "
               "strip provides <b>resiliency</b> compensating minor flange "
               "movements; the filler is the sealing medium flowing into the "
               "imperfections of the flange face. Manufacturers specify the "
               "installed compression for correct stressing and resiliency; "
               "the operating thickness is controlled by bolt loading, by the "
               "depth of a gasket recess, or by <b>inner/outer compression "
               "rings</b> — the inner ring also protects the gasket from "
               "erosion by the fluid, the outer ring locates it within the "
               "bolt diameter."))
    b.append(p("Load capacity at operating thickness is controlled by the "
               "number of windings per unit width — <b>gasket density</b> — so "
               "spiral wound gaskets are <b>tailor-made</b> for their pressure "
               "range. The diametrical clearance for <b>unconfined</b> gaskets "
               "(pipe bore to inner diameter, outer diameter to raised face) "
               "should be at least <b>6 mm</b> (1/4 in); for <b>confined</b> "
               "gaskets 1.5 mm (1/16 in). Wrongly installed — protruding into "
               "the bore or over the raised face — sealing is severely "
               "impaired."))
    b.append(p("Windings are commonly <b>stainless steel or nickel-based "
               "alloys</b> (the inventory materials of most manufacturers), "
               "also special materials: mild steel, copper, even gold or "
               "platinum. For corrosive fluids or high temperatures consider "
               "stress corrosion and intergranular corrosion. Fillers are "
               "selected for fluid compatibility and temperature resistance: "
               "<b>PTFE, pure graphite, mica with rubber or graphite binder, "
               "ceramic fiber paper</b>. The filler also affects sealability: "
               "asbestos and ceramic-paper fillers require higher seating "
               "stresses than softer, more impervious fillers, and more care "
               "in selecting the flange finish."))
    b.append(p("In most practical applications the user must be content with "
               "commercially available finishes: for identical geometry, "
               "roughness typically varies <b>3.2–12.5 µm Ra</b> (125–500 "
               "µin). Optimum sealing has been achieved with the finish "
               "described in ANSI B16.5, limited to <b>3.2–6.3 µm Ra</b>. "
               "Roughness above 6.3 µm Ra may require unusually high seating "
               "stresses; finishes significantly smoother than 3.2 µm Ra may "
               "seal poorly — insufficient friction to prevent lateral "
               "displacement of the gasket."))
    b.append(h3("Gasket blowout", "Gioăng bị thổi bay"))
    b.append(p("<b>Unconfined</b> gaskets may blow out prior to a leakage "
               "warning when inadequately designed. This failure mode cannot "
               "occur if the friction force at the gasket faces exceeds the "
               "radial fluid force acting on the gasket:"))
    b.append(eq("2µF ≥ P·t·πd<sub>m</sub>   ⟺   F ≥ P·t·πd<sub>m</sub>/2µ", "2-3"))
    b.append(eq("F ≥ w·P·m·πd<sub>m</sub>  (leakage begins to develop)", "2-4"))
    b.append(p("where µ is the friction factor, F the gasket working load, P "
               "the fluid gauge pressure, t the gasket thickness, d<sub>m</sub> "
               "the mean gasket diameter, w the width, and <b>m the gasket "
               "factor</b> — a measure of the sealing ability defining the "
               "ratio of residual gasket stress to the fluid pressure at which "
               "leakage begins; found experimentally. From Equations 2-3 and "
               "2-4 the gasket is safe against blowout without prior leakage "
               "warning if:"))
    b.append(eq("w ≥ t/(2µm)", "2-5"))
    b.append(p("Krägeloh regarded a gasket factor of <b>1.0</b> and a friction "
               "factor of <b>0.1</b> safe for most practical applications — "
               "the gasket width should be <b>not less than five times its "
               "thickness</b> to prevent blowout without prior leakage "
               "warning."))

    b.append(h2("Valve stem seals", "Gioăng trục van"))
    b.append(h3("Compression packings", "Packing nén"))
    b.append(p("Compression packings are the sealing elements in <b>stuffing "
               "boxes</b> (see Figures 3-17 to 3-19): a soft material stuffed "
               "into the box and <b>compressed by a gland</b> to seal around "
               "the stem. Packings must withstand temperature extremes, resist "
               "aggressive media, display a low friction factor and adequate "
               "structural strength, and be impervious to the fluid. "
               "Lubricants: oils and greases for water and aqueous solutions; "
               "soaps and insoluble substances for oil or gasoline. <b>Liquid "
               "lubricants migrate under pressure</b>, particularly at higher "
               "temperatures, causing the packing to <b>shrink and harden</b> — "
               "retightening is needed from time to time. To minimize this, "
               "the liquid content of stem packings is normally held to <b>10% "
               "of the packing weight</b>. With <b>PTFE</b>, a solid lubricant "
               "became available for fibrous packings without liquid "
               "lubricant."))
    b.append(p("<b>Asbestos</b> is now avoided where possible, replaced by "
               "polymer filament yarns (PTFE, aramid) and pure graphite fiber "
               "or foil; other materials include vegetable fibers (cotton, "
               "flax, ramie — frequently PTFE-lubricated) and twisted and "
               "folded metal ribbons. Fibrous constructions in order of "
               "mechanical strength: <b>loose fill, twisted yarn, braid-over-"
               "twisted-core, square-plait braid, interbraid</b>; the latter "
               "three often contain <b>metal wire within the strands</b> for "
               "high pressure and temperature."))
    b.append(h3("Sealing action of compression packings",
                "Tác dụng làm kín của packing nén"))
    b.append(p("The sealing action is due to the packing's ability to <b>expand "
               "laterally</b> against the stem and box walls when stressed by "
               "gland tightening. The lateral stress of a confined elastic "
               "solid under an applied axial stress depends on <b>Poisson's "
               "ratio</b>:"))
    b.append(eq("σ<sub>1</sub> = σ<sub>a</sub>·µ/(1 − µ)", "2-6"))
    b.append(p("(the source prints this in the form σ₁ = σa · µ/(1−µ); "
               "σ<sub>1</sub> lateral stress, σ<sub>a</sub> axial stress, µ "
               "Poisson's ratio = lateral expansion / axial compression.) The "
               "lateral stress equals the axial stress only at <b>µ = 0.5</b> "
               "— bulk-incompressible. <b>Soft rubber</b> has µ ≈ 0.5 and "
               "transmits pressure much like a liquid. <b>Solid PTFE</b>: "
               "µ = 0.46 at 23 °C and 0.36 at 100 °C — transmitting <b>85% "
               "and 56%</b> of the axial stress to the lateral faces "
               "respectively. Other packing materials are far more compressible "
               "in bulk, so their Poisson's ratio, where definable, is "
               "considerably below 0.5."))
    b.append(p("When such packing is compressed, axial shrinkage creates "
               "friction with the side walls that prevents full transmission "
               "of the gland force to the bottom — the <b>axial packing "
               "pressure falls off quite rapidly</b> (theoretical value "
               "calculable, applying to static conditions only; with the stem "
               "moving, the actual distribution is difficult to analyze). The "
               "distribution also depends on <b>installation</b>: a square "
               "cord bent around the stem initially assumes a trapezoid shape "
               "— inner-periphery pressure higher than outer."))
    b.append(p("When the fluid pressure at the bottom begins to exceed the "
               "lateral packing pressure, a <b>gap develops</b> between "
               "packing and lateral faces and the fluid enters; at low "
               "pressures the gland must finally be retightened to maintain "
               "the seal. At sufficiently high fluid pressure, sealing takes "
               "place <b>just below the gland</b> — where the fluid attempts "
               "to extrude the packing through the gland clearances — and the "
               "sealing action has become <b>automatic</b>. Fluid-pressure "
               "gradient readings along rotating-shaft stuffing boxes "
               "(Figure 2-3) confirm this: at low fluid pressure the gradient "
               "is near-uniform; at high pressure <b>90% of the pressure drop "
               "occurs across the ring just below the gland</b>. For high "
               "pressures that ring is the most important one — select it for "
               "extrusion and wear resistance and install it carefully — and "
               "<b>extra-long stuffing boxes serve no purpose</b> for "
               "high-pressure duty."))
    b.append(fig(4, F.fig_vsh_2_3()))
    b.append(p("If the packing is bulk-<b>incompressible</b> (soft rubber), "
               "the gland's axial pressure produces a uniform lateral pressure "
               "over the entire length; fluid pressure raises the lateral "
               "pressure by exactly that amount — sealing is <b>automatic</b> "
               "once initial interference exists. But rubber <b>grips the "
               "stem</b> and impedes operation unless the inner face is "
               "slippery — hence rubber packings are normally used as "
               "<b>O-rings</b>, which offer only a narrow contact face."))
    b.append(h3("Corrosion of stainless steel valve stems by packings",
                "Ăn mòn trục van thép không gỉ do packing"))
    b.append(p("<b>AISI 410 (13Cr)</b> stems corrode frequently where the face "
               "contacts the packing — usually during <b>storage after the "
               "hydrostatic test</b>, when the packing is water-saturated; "
               "placed into service immediately after testing, no corrosion "
               "occurs. H. J. Reynolds, Jr.'s investigations: the corrosion "
               "under wet packing results from the <b>deaerated environment</b> "
               "imposed on the steel surface — numerous small <b>anodes</b> at "
               "oxygen-deficient sensitive points of the protective oxide "
               "film, with the large passive masses acting as <b>cathodes</b>, "
               "produce galvanic-cell action within the metal. <b>Graphite</b> "
               "in the packing acts as a cathodic material and aggravates the "
               "attack through increased galvanic current density. Because of "
               "this mechanism, a <i>non-corrosive</i> packing built from "
               "<i>non-corrosive</i> ingredients is impractical — a <b>corrosion "
               "inhibitor</b> is required: of the anodic inhibitors, only "
               "those with an oxidizing anion such as <b>sodium nitrite</b> "
               "are efficient; cathodic protection by sacrificial metals such "
               "as <b>zinc</b> also works well; best protection with minimum "
               "effect on compression characteristics comes from homogeneously "
               "dispersed <b>sodium nitrite plus a zinc-dust interlayer</b>. "
               "High-chromium stainless steels — especially with nickel — "
               "show markedly better resistance to inhibited packing."))
    b.append(h3("Lip-type packings", "Packing môi (lip-type)"))
    b.append(p("Lip-type packings expand laterally through the <b>flexibility "
               "of their lips</b>, forced against the walls by the fluid "
               "pressure — permitting rigid construction materials unsuitable "
               "as compression packings. On the debit side, sealing is <b>one-"
               "directional</b>. Most valve-stem lip packings are <b>virgin or "
               "filled PTFE</b>; fabric-reinforced rubber and leather mainly "
               "for hydraulics. Most are <b>V-shaped</b>, fitting narrow "
               "packing spaces. PTFE/reinforced-rubber V-rings <b>touch only "
               "near the lip tips</b>, gaps letting fluid pressure act freely "
               "on the lips; leather rings lack that rigidity and are designed "
               "to <b>fully support each other</b>. PTFE/rubber V-packings "
               "have <b>flared lips</b> preloading the walls — only slight "
               "initial tightening is needed; leather rings have straight "
               "walls and need a higher axial preload. Where low friction "
               "matters (automatic control valves), the packing is often "
               "<b>loaded from the bottom by a spring</b> of predetermined "
               "strength to prevent manual overloading."))
    b.append(h3("Squeeze-type packings", "Packing nén ép (squeeze-type)"))
    b.append(p("The name applies to <b>O-rings and the like</b>: installed "
               "with <b>lateral squeeze</b>, relying on elastic strain to "
               "maintain the preload. When fluid pressure enters from the "
               "bottom, the packing <b>moves toward the clearance gap</b> "
               "between stem and back-up support and <b>plugs the leakage "
               "path</b>; on depressurizing it regains its configuration. "
               "Because elastomers have the necessary high yield strain, most "
               "squeeze packings are made of them. Extrusion is controlled by "
               "the <b>clearance-gap width</b> and elastomer <b>rigidity</b> "
               "(modulus of elasticity, conventionally expressed as "
               "<b>Durometer hardness</b> — the same durometer value may mean "
               "different moduli for different compound classes). Very small "
               "gaps are controlled by <b>leather or plastic back-up rings</b> "
               "fitted tightly around the stem. O-ring manufacturers supply "
               "tables relating durometer, clearance and the fluid pressure "
               "safe against extrusion."))
    b.append(h3("Thrust packings", "Packing đỡ trục (thrust)"))
    b.append(p("A packing <b>ring or washer</b> mounted between shoulders on "
               "bonnet and stem, the stem free to move axially against it. "
               "The initial seal is provided either by a supplementary radial "
               "packing (compression type) or by a <b>spring</b> forcing the "
               "stem shoulder against the thrust packing; fluid pressure then "
               "forces more intimate contact. Thrust packings are found "
               "frequently in <b>ball valves</b> (Figures 3-61 to 3-63, 3-65, "
               "3-67)."))
    b.append(h3("Diaphragm valve stem seals", "Gioăng trục kiểu màng"))
    b.append(p("Diaphragms are <b>flexible pressure-containing valve covers</b> "
               "linking the stem with the closure member — preventing any "
               "leakage past the stem to atmosphere <b>except on fracture of "
               "the diaphragm</b>. The shape may be a <b>dome</b> (as in "
               "Figure 3-7) or a <b>bellows</b> (as in Figures 3-6 and 3-39), "
               "depending on the application."))

    b.append(note("Central idea: metal seatings live or die by <b>galling</b> "
                  "when the fluid lacks lubricity — pair materials of different "
                  "hardness or use Stellite; soft seatings die by the <b>heat "
                  "of compression</b> on sudden gas fill (Table 2-2). Flat "
                  "gaskets gain capacity from <b>flange-face friction</b> (do "
                  "not polish); blowout protection needs <b>width ≥ 5× "
                  "thickness</b> (Eq. 2-5). Compression packing seals "
                  "automatically only at high pressure — 90% of the drop "
                  "concentrates in the ring below the gland (Figure 2-3) — and "
                  "longer boxes do not help; 13Cr stems corrode in storage "
                  "after hydrostatic testing through galvanic action, cured "
                  "with sodium nitrite + zinc in the packing."))
    b.append(p("<i>This is an unofficial translation for study purposes. "
               "Original content © 2004 Elsevier Inc. (Gulf Professional "
               "Publishing).</i>"))
    return "".join(b)
