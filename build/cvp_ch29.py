# -*- coding: utf-8 -*-
"""Book 7, Chapter 29 - Saving Energy / Tiết kiệm năng lượng (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
171-173 (PDF pp. 166-168; printed = PDF + 5). Three printed pages: the 5%
pressure-drop rule, a worked 120 gpm oil example, Germany/US energy-savings
estimates, five displayed equations (two power calculations plus three
Singleton relations), two references. No figures or tables. The PDF text
layer garbles every equation; the printed forms were read from pypdfium2
renders of the three source pages.
"""
from cvp_common import eq, h2, h3, note, p, refs, ul

PAGES_SRC = 3
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Saving Energy"
TITLE_VI = "Tiết kiệm năng lượng"

_REFS = [
    "H. O. Engel, “Energieökonomiebei der Anwendung von Regelventilen,” RTP "
    "(Germany), no. 4: 188–194 (1991).",
    "E. W. Singleton, “Development of a High-Performance Choke Valve with Reference "
    "to Sizing for Multiphase Flow,” Measurement and Control 24, no. 9 (1991).",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 29.</b> giảm áp cho phép · phần trăm áp suất hệ thống · "
                "đặc tính lưu lượng lắp đặt (installed flow characteristic) · công suất bơm "
                "và máy nén · công suất chuyển hóa tại van · gallon Mỹ mỗi phút (gpm) · độ "
                "giảm áp ΔP · trọng lực riêng Gf · hệ số lưu lượng Cv · hệ số phục hồi áp "
                "suất FL · dòng không bị chokes / dòng bị chokes (nonchoked / choked) · "
                "áp suất tuyệt đối P₁, P₂ · psia · điện năng MWh · MW · bộ lồng chống rung "
                "(trim vibration) · xâm thực · bơm điều chỉnh tốc độ (speed-controlled "
                "pump) · van nghẹt hiệu năng cao (high-performance choke valve) · định cỡ "
                "dòng nhiều pha")
    return ("<b>Key terms.</b> allowed pressure drop · share of total system pressure · "
            "installed flow characteristic · pump and compressor power · power converted "
            "in the valve · US gallons per minute (gpm) · pressure drop ΔP · specific "
            "gravity Gf · flow coefficient Cv · pressure recovery factor FL · nonchoked / "
            "choked flow · absolute pressures P₁, P₂ · psia · electrical energy in MWh · "
            "MW · trim vibration · cavitation · speed-controlled pump · high-performance "
            "choke valve · multiphase-flow sizing")


def body_vi():
    b = []
    b.append(h2("Tiết kiệm năng lượng", "Saving Energy"))
    b.append(p("Như tôi đã chỉ ra ở Chương 5, bạn chỉ nên dùng 5% tổng áp suất hệ thống hoặc "
               "5 đến 10 psi làm độ giảm áp cho phép qua van điều khiển ở lưu lượng cực đại. "
               "Điều đó sẽ tiết kiệm cho công ty bạn rất nhiều điện năng cho bơm và máy nén. "
               "Cách này trái với quy tắc cũ là dùng khoảng 50% cột áp động để có được đặc "
               "tính lưu lượng lắp đặt tuyến tính hơn (xem Chương 8)."))
    b.append(p("Vì công suất chuyển hóa trong van điều khiển tương tự công suất mà bơm dùng "
               "để tạo ra áp suất ngay từ đầu, công suất này có thể tính bằng"))
    b.append(eq("P = 4,2 × 10<sup>−4</sup> × ΔP × q  tính bằng kW"))
    b.append(p("trong đó"))
    b.append(ul([
        "q = lưu lượng chất lỏng tính bằng gallon Mỹ mỗi phút (gpm)",
        "ΔP = độ giảm áp tính bằng psi",
    ]))
    b.append(p("Ví dụ, trong một ứng dụng van với 120 gpm dầu ở G<sub>f</sub> bằng 0,8, cần "
               "thêm công suất bơm (mô tơ lớn hơn) nếu độ giảm áp 50 psi được phân bổ cho "
               "van:"))
    b.append(eq("P = 4,2 × 10<sup>−4</sup> × 50 × 120 = 2,5 kW"))
    b.append(p("Để giảm áp suất, bạn chỉ cần cỡ van 1½ in. C<sub>v</sub> yêu cầu là 15,1."))
    b.append(p("Bằng cách giảm độ giảm áp của van ở lưu lượng cực đại xuống chỉ còn 5 psi "
               "và chọn một bơm khác, năng lượng cần cho van giờ chỉ là 0,25 kW, tức tiết "
               "kiệm được 2,5 − 0,25 = 2,25 kW mỗi giờ. Con số đó tương đương 20.000 kW "
               "mỗi năm! Đúng là cỡ van giờ phải tăng lên 2 in để chứa C<sub>v</sub> cao hơn "
               "(48) theo độ giảm áp 5 psi; tuy nhiên, khoản tiết kiệm chi phí khoảng "
               "$2.000 mỗi năm bù đắp hơn mức chênh lệch giá giữa hai cỡ van. Hơn nữa, cỡ "
               "đường ống cho lưu lượng 120 gpm là 2 in (xem Bảng A-1), nên bạn cũng tiết "
               "kiệm được chi phí đoạn thu nhỏ đường ống."))
    b.append(p("Một lợi ích khác ngoài tiết kiệm năng lượng (chi phí) là ít phải sửa van hơn, "
               "vì không có rung bộ lồng (trim vibration) do độ giảm áp cao gây ra và cũng "
               "không có xâm thực làm mòn bộ lồng."))
    b.append(p("Trong một bài báo, Hans O. Engel [1] chỉ ra rằng ba nhà sản xuất hóa chất "
               "lớn nhất nước Đức dùng khoảng 120.000 bơm, với công suất tiêu thụ trung "
               "bình 3 kW, phối hợp cùng khoảng 200.000 van điều khiển. Nếu tất cả van được "
               "định cỡ hợp lý hơn (nghĩa là như đề xuất ở đây), khoảng một nửa công suất, "
               "tức 180 MW điện năng, có thể được tiết kiệm. Điều đó lại tương đương khoản "
               "tiết kiệm khoảng 1,5 triệu MWh mỗi năm. Có thể hợp lý khi giả định tổng "
               "ngành hóa chất Hoa Kỳ lớn gấp khoảng ba lần quy mô của Đức. Như vậy, mức "
               "tiết kiệm tiềm năng ở Hoa Kỳ là 4 đến 5 triệu MWh mỗi năm."))
    b.append(p("Thật sáng tỏ khi nhận ra một van điều khiển chuyển hóa nhiều điện năng đến "
               "mức nào khi nó tiết lưu, tức là khi nó thực hiện đúng nhiệm vụ giảm áp "
               "của mình. Các phương trình sau của E. W. Singleton [2] giúp bạn tính toán."))
    b.append(h3("Đối với chất lỏng", "For liquids"))
    b.append(p("<b>Không bị chokes (nonchoked):</b>"))
    b.append(eq("kWh = (C<sub>v</sub>/45) (ΔP/G<sub>f</sub>)<sup>0,5</sup>"))
    b.append(p("<b>Bị chokes (choked):</b>"))
    b.append(eq("kWh = C<sub>v</sub>F<sub>L</sub>[(P<sub>1</sub> − P<sub>2</sub>)"
                "(F<sub>L</sub><sup>2</sup>)]<sup>0,5</sup> / "
                "[45(G<sub>f</sub>)<sup>0,5</sup>]"))
    b.append(h3("Đối với chất khí ở dòng chảy tới hạn",
                "For gases at choked flow"))
    b.append(eq("kWh = 0,014 C<sub>v</sub>F<sub>L</sub><sup>3</sup>P<sub>1</sub>"))
    b.append(p("trong đó"))
    b.append(ul([
        "Tất cả áp suất tính bằng psia",
        "C<sub>v</sub> = hệ số lưu lượng ở điều kiện lưu lượng mong muốn",
        "F<sub>L</sub> = hệ số phục hồi áp suất ở hành trình yêu cầu",
        "G<sub>f</sub> = trọng lực riêng ở điều kiện chảy (nước = 1,0)",
    ]))
    b.append(p("Cuộc thảo luận này không nên được xem là sự ủng hộ bơm điều chỉnh tốc độ. "
               "Những bơm đó có vấn đề riêng; xem Chương 2, “Why Not Use a Speed-Controlled "
               "Pump?”"))
    b.append(refs(_REFS))
    b.append(note("<b>Đặc điểm của nguyên bản.</b> Chương gồm ba trang in (171–173; trang in "
                  "= trang PDF + 5). Không có hình hay bảng. Bốn phương trình trong chương "
                  "không được đánh số và bị lỗi trong lớp văn bản của PDF; chúng được đọc "
                  "trực tiếp từ các trang in được render và chuyển sang HTML với dấu thập phân "
                  "Việt hóa thành dấu phẩy. Cụm “kW per hour” và các con số gốc (1½ in, "
                  "C<sub>v</sub> 15,1 và 48, 20.000 kW/năm, $2.000/năm, 180 MW, 1,5 triệu "
                  "và 4 đến 5 triệu MWh/năm) được giữ nguyên."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung "
               "gốc © 2011 Hans D. Baumann, do ISA / John Wiley &amp; Sons xuất bản.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Saving Energy", "Saving Energy"))
    b.append(p("As I pointed out in Chapter 5, you should only use 5% of the total system "
               "pressure or 5 to 10 psi as the allowed pressure drop across the control "
               "valve at the maximum flow rate. It will save your company a lot of "
               "electrical energy for pumps and compressors. This is contrary to the old "
               "rule of using about 50% of the dynamic head pressure to achieve a more "
               "linear installed flow characteristic (see Chapter 8)."))
    b.append(p("Because the power converted in a control valve is similar to that used in a "
               "pump to create the pressure in the first place, it can be calculated as"))
    b.append(eq("P = 4.2 × 10<sup>−4</sup> × ΔP × q  in kW"))
    b.append(p("where"))
    b.append(ul([
        "q = flow in US gallons per minute (gpm) of liquid",
        "ΔP = pressure drop in psi",
    ]))
    b.append(p("For example, in a valve application for 120 gpm oil at a G<sub>f</sub> of "
               "0.8, extra pump horsepower is needed (a bigger motor) if a 50 psi pressure "
               "drop is assigned to the valve:"))
    b.append(eq("P = 4.2 × 10<sup>−4</sup> × 50 × 120 = 2.5 kW"))
    b.append(p("To reduce the pressure, you need a valve size of only 1½ in. The "
               "C<sub>v</sub> required is 15.1."))
    b.append(p("By reducing the valve pressure drop at maximum flow to only 5 psi and "
               "choosing a different pump, the energy required for the valve is now only "
               "0.25 kW, a savings of 2.5 − 0.25 = 2.25 kW per hour. This amounts to "
               "20,000 kW per year! True, the valve size now has to go up to 2 in to "
               "accommodate the higher C<sub>v</sub> (48) based on the 5 psi pressure drop; "
               "however, the cost savings of about $2,000 per year more than pays for the "
               "cost difference between the two valve sizes. Besides, the line size for "
               "120 gpm flow is 2 in (see Table A-1), so you also save the cost of pipe "
               "reducers."))
    b.append(p("Another benefit besides energy (cost) savings is less valve repair because "
               "there is no trim vibration that could be caused by a higher pressure drop "
               "and no cavitation to wear out the trim."))
    b.append(p("In an article, Hans O. Engel [1] pointed out that Germany’s three largest "
               "chemical producers use about 120,000 pumps, with an average power "
               "consumption of 3 kW, cooperating with about 200,000 control valves. If all "
               "valves are sized more rationally (i.e., as proposed herein), then about "
               "half the power, or 180 MW of electric energy, could be saved. This, in "
               "turn, translates to a yearly savings of about 1.5 million MWh. It is fair "
               "to assume that the total US chemical industry is about three times the "
               "size of the German representation. This means a possible savings of 4 to "
               "5 million MWh per year in the United States."))
    b.append(p("It is enlightening to realize how much energy a control valve converts "
               "when it throttles, that is, when it does its assigned job of reducing "
               "pressure. The following equations by E. W. Singleton [2] help you do "
               "this."))
    b.append(h3("For liquids", "For liquids"))
    b.append(p("<b>Nonchoked:</b>"))
    b.append(eq("kWh = (C<sub>v</sub>/45) (ΔP/G<sub>f</sub>)<sup>0.5</sup>"))
    b.append(p("<b>Choked:</b>"))
    b.append(eq("kWh = C<sub>v</sub>F<sub>L</sub>[(P<sub>1</sub> − P<sub>2</sub>)"
                "(F<sub>L</sub><sup>2</sup>)]<sup>0.5</sup> / "
                "[45(G<sub>f</sub>)<sup>0.5</sup>]"))
    b.append(h3("For gases at choked flow", "For gases at choked flow"))
    b.append(eq("kWh = 0.014 C<sub>v</sub>F<sub>L</sub><sup>3</sup>P<sub>1</sub>"))
    b.append(p("where"))
    b.append(ul([
        "All pressures are in psia",
        "C<sub>v</sub> = flow coefficient at desired flow conditions",
        "F<sub>L</sub> = pressure recovery factor at required travel",
        "G<sub>f</sub> = specific gravity at flowing conditions (water = 1.0)",
    ]))
    b.append(p("This discussion should not be taken as an endorsement of speed-controlled "
               "pumps. These have their own problems; see Chapter 2, “Why Not Use a "
               "Speed-Controlled Pump?”"))
    b.append(refs(_REFS))
    b.append(note("<b>Source quirks.</b> The chapter spans three printed pages (171–173; "
                  "printed = PDF + 5), with no figures or tables. The four equations are "
                  "unnumbered and were garbled in the PDF text layer; they were read "
                  "directly from rendered page images and transcribed into HTML. Original "
                  "numbers and wording are retained, including “kW per hour,” 1½ in, "
                  "C<sub>v</sub> 15.1 and 48, 20,000 kW per year, $2,000 per year, 180 MW, "
                  "1.5 million MWh and 4 to 5 million MWh per year."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 2011 Hans D. Baumann, published by ISA / John Wiley &amp; Sons.</i>"))
    return "".join(b)
