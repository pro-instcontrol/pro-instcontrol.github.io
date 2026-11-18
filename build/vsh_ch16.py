# -*- coding: utf-8 -*-
"""Book 6, Unit 16 — Rupture Discs: Selection (EN/VI).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 261–267 (PDF pp. 275–281): selection against operating pressure and
MAWP, combinations with pressure relief valves, reordering, user
responsibility, explosion vent panels and flame-quenching vent systems
(Figures 6-34…6-38).
"""

from vsh_common import fig, h2, p, table, ul
import vshfig13 as F13

PAGES_SRC = 7         # source book pp. 261-267
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Rupture Discs: Selection"
TITLE_VI = "Đĩa vỡ: Lựa chọn"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 16.</b> selection — lựa chọn · "
                "maximum allowable working pressure (MAWP) — áp làm việc "
                "tối đa cho phép · manufacturing range — phạm vi chế tạo · "
                "burst tolerance — sai số áp vỡ · operating ratio — tỉ lệ "
                "vận hành · zero manufacturing range — phạm vi chế tạo bằng "
                "không · telltale indicator — bộ báo rò · combination factor "
                "— hệ số cụm kết hợp · reordering — đặt lại hàng · lot / "
                "batch number — số lô / số mẻ · explosion vent panel — tấm "
                "thông nổ · Pstat — áp mở tấm thông · Pred — áp nổ đã giảm · "
                "Pult — áp bền cuối của bình · Pmax — áp nổ không thông hơi · "
                "flame-quenching vent — cửa thông dập ngọn lửa · KST — hạng "
                "nguy hiểm nổ bụi.")
    return ("<b>Key terms.</b> selection · maximum allowable working pressure "
            "(MAWP) · manufacturing range · burst tolerance · operating "
            "ratio · zero manufacturing range · telltale indicator · "
            "combination factor · reordering · lot / batch number · "
            "explosion vent panel · Pstat · Pred · Pult · Pmax · "
            "flame-quenching vent · KST dust-explosion class.")


def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def U(items):
        b.append(ul([(i[0] if vi else i[1]) for i in items]))

    def FIG(n, fn):
        b.append(fig(n, fn))

    # ============================================================== selection
    H("Lựa chọn đĩa vỡ", "Selecting rupture discs")
    P("Việc chọn đĩa vỡ phụ thuộc vào hiệu áp giữa áp vận hành và áp làm "
      "việc tối đa cho phép (MAWP) của hệ thống. Phạm vi chế tạo, sai số áp "
      "vỡ và tỉ lệ vận hành khuyến nghị đều phải nằm trong hiệu áp đó. Hình "
      "6-34 cho thấy các mức áp khi đĩa vỡ là thiết bị giảm áp duy nhất, "
      "với phạm vi chế tạo +10%/−5% và sai số áp vỡ ±5%.",
      "Rupture-disc selection depends on the pressure differential between "
      "operating pressure and the maximum allowable working pressure (MAWP). "
      "Manufacturing range, burst tolerance and recommended operating ratio "
      "must all fit within that differential. Figure 6-34 shows the levels "
      "for a disc as sole relief device, with +10%/−5% manufacturing range "
      "and ±5% burst tolerance.")
    FIG(34, F13.fig_vsh_6_34())
    P("ASME cho phép áp vỡ định mức không vượt MAWP nhưng cho phép cộng sai "
      "số áp vỡ vượt lên. Trong điều kiện đó áp vỡ nhỏ nhất có thể chỉ bằng "
      "82% MAWP. Với tỉ lệ vận hành 70%, áp vận hành không nên vượt 57% MAWP. "
      "Một số nhà chế tạo với áp trên 2,75 barg (40 psig) bỏ qua sai số −5% "
      "khi đánh giá áp vỡ nhỏ nhất. Khi hiệu áp chỉ 10%, như thường gặp ở "
      "lắp đặt van an toàn xả, lựa chọn duy nhất là đĩa có phạm vi chế tạo "
      "bằng không, tỉ lệ vận hành 90% hoặc 95%, và có thể sai số áp vỡ giảm.",
      "The ASME Code allows rated burst pressure not to exceed MAWP but "
      "permits plus burst tolerance to do so. The minimum possible burst "
      "pressure can then be only 82% of MAWP; at a 70% operating ratio the "
      "operating pressure should not exceed 57% of MAWP. Above 2.75 barg "
      "(40 psig) some makers neglect the minus 5% tolerance when assessing "
      "minimum burst. With only a 10% differential, as is common in relief-"
      "valve installations, the only choice is zero manufacturing range, a "
      "90% or 95% operating ratio and possibly reduced burst tolerance.")
    U([("Nhiệt độ dịch vụ và các lần lệch nhiệt độ có thể xảy ra.",
        "Service temperature and possible temperature excursions."),
       ("Trạng thái lưu chất: khí, hơi hoặc chất lỏng.",
        "Fluid state: gas, vapor or liquid."),
       ("Chu kỳ hoặc dao động áp, tính ăn mòn của môi trường hai mặt đĩa, "
        "chân không hoặc áp ngược, và các điều kiện vận hành khác.",
        "Cyclic or pulsating service, corrosiveness on both sides, vacuum or "
        "back pressure, and other operating conditions."),
       ("Một số loại chỉ có dải áp và cỡ hạn chế, nên khi cần thiết phải "
        "đưa nhà chế tạo vào ngay từ giai đoạn thiết kế sơ bộ.",
        "Some types cover only limited pressure and size ranges, so the "
        "manufacturer may need to be involved at the early design stage.")])

    # ================================================ combinations with valves
    H("Cụm đĩa vỡ kết hợp van an toàn xả",
      "Rupture-disc device combined with a pressure relief valve")
    P("Đĩa vỡ có thể cô lập đầu vào hoặc đầu ra của van an toàn xả khỏi lưu "
      "chất ăn mòn trước khi van mở, nhưng phải bảo đảm van vẫn xả đúng "
      "chức năng. Phần thảo luận dưới đây áp dụng cho dịch vụ khí hoặc hơi.",
      "Rupture discs may isolate valve inlet or outlet from corrosive fluids "
      "before the valve is called upon to open, but must not impair the "
      "relief function. The following discussion is restricted to gas or "
      "vapor service.")
    P("Khi đĩa lắp ở đầu vào van, van phải mở bật đồng thời với đĩa vỡ và "
      "rò qua đĩa bị ăn mòn không được làm tăng áp trong khoảng giữa đĩa và "
      "van. Với hiệu áp 10% thường gặp, có đĩa phạm vi chế tạo bằng không, "
      "sai số ±2% và tỉ lệ vận hành 90% hoặc 95%. Vì van có sai số áp cài đặt "
      "±3% còn đĩa ±2%, áp mở của van có thể cao hơn áp vỡ đĩa 5% trong trường "
      "hợp xấu nhất. Để đĩa mở hoàn toàn, có thể đặt van thấp hơn áp vỡ định "
      "mức 3% nếu không làm blowdown thấp hơn mức cho phép; một số tài liệu "
      "ghi nhận đặt van cao hơn đĩa không quá 5% vẫn mở được đĩa, nhưng đặt "
      "thấp hơn vẫn là lựa chọn ưa dùng.",
      "At the valve inlet, the valve must pop in unison with the disc and "
      "leakage across a corroded disc must not pressurize the space between "
      "them. At the common 10% differential, discs with zero manufacturing "
      "range, ±2% tolerance and 90% or 95% operating ratio are available. "
      "Because valve set-pressure tolerance is ±3% and disc tolerance ±2%, "
      "the worst-case valve opening pressure can exceed disc burst pressure "
      "by 5%. The valve set pressure may need to be 3% below rated burst "
      "pressure if blowdown remains acceptable; setting no more than 5% "
      "above the disc has been reported to open it fully, but a lower valve "
      "setting is preferred.")
    U([("Van trong cụm này nên kiểu mở bật; có thể không cân bằng trừ khi áp "
        "ngược đòi hỏi kiểu cân bằng.",
        "The valve should be pop-acting and may be unbalanced unless back "
        "pressure demands a balanced type."),
       ("ASME yêu cầu bộ báo rò trong khoảng giữa van và đĩa. Áp tăng lên "
        "trong khoảng này sẽ cộng vào áp vỡ của đĩa.",
        "ASME requires a telltale indicator in the space between valve and "
        "disc; pressure build-up there raises the effective burst pressure."),
       ("ASME cho phép lấy lưu lượng cụm bằng 90% lưu lượng định mức của van "
        "hoặc hệ số cụm được chứng nhận bằng thử nghiệm.",
        "ASME permits combination capacity at 90% of valve rated capacity or "
        "at a combination factor certified by test.")])
    P("Khi đĩa lắp ở đầu ra van, mục đích là bảo vệ bên trong van khỏi lưu "
      "chất ăn mòn trong hệ thống xả. Rò qua chỗ kín van có thể vào buồng "
      "giữa chỗ kín và đĩa, nên mặt đầu vào của đĩa cũng cần bộ báo rò. Khi "
      "van mở, áp trong buồng đó tăng tới áp vỡ đĩa; khi đánh giá cần tính "
      "áp định mức cộng sai số và áp ngược cộng thêm. Van và đường ống phía "
      "trước đĩa phải chịu được áp này. Áp tăng như vậy có thể cản van thông "
      "thường mở, nên nên dùng van cân bằng. Nếu lắp cả đầu vào lẫn đầu ra, "
      "chọn van cân bằng kiểu mở bật.",
      "A downstream disc protects valve internals from corrosive discharge "
      "fluid. Leakage past the seatings can enter the chamber between them "
      "and the disc, so its upstream side also needs a telltale. When the "
      "valve opens, chamber pressure rises to disc burst pressure; "
      "assessment must include maximum rated burst pressure plus tolerance "
      "and superimposed back pressure. Valve and piping upstream of the disc "
      "must withstand it. This build-up may impede a conventional valve, so "
      "a balanced valve is suggested; with discs both upstream and "
      "downstream, choose a balanced pop-action valve.")
    P("Cụm đĩa ở đầu vào van cũng dùng được cho dịch vụ lỏng nếu bảo đảm có "
      "thể tích khí đáng kể giữa đĩa và mực chất lỏng để van mở đồng thời với "
      "đĩa vỡ. Khi thiết kế cụm đĩa và van an toàn xả, người thiết kế phải "
      "tuân code thiết kế áp dụng.",
      "An inlet disc combination may also be used in liquid service if a "
      "substantial gas volume between disc and liquid level ensures the "
      "valve opens in unison with disc burst. Designers must follow the "
      "applicable design code.")

    # ================================================ reordering / responsibility
    H("Đặt lại hàng và trách nhiệm người dùng",
      "Reordering and user responsibility")
    U([("Khi đặt lại đĩa vỡ, luôn ghi số lô hoặc số mẻ để nhận đúng đĩa thay "
        "thế. Áp vỡ yêu cầu chỉ cần nằm trong phạm vi chế tạo của đĩa đã đặt; "
        "áp định mức hoặc ghi nhãn vì thế có thể khác giữa các lần đặt cùng "
        "một loại đĩa.",
        "When reordering, always quote the lot or batch number to obtain the "
        "correct replacement. The requested burst pressure need only fall "
        "within the ordered disc's manufacturing range, so rated or marked "
        "burst pressure can vary between orders of the same disc."),
       ("Nhân sự nhà máy phải nắm rõ yêu cầu cầm, cất, lắp và bảo trì đĩa vỡ. "
        "Không giao việc lắp đặt cho người không hiểu yêu cầu và hậu quả của "
        "xử lý sai.",
        "Plant personnel must understand handling, storage, installation and "
        "maintenance requirements. Installation must never be entrusted to "
        "someone unaware of those requirements and their consequences."),
       ("Mỗi nhà máy nên lưu hệ thống hồ sơ vị trí và thông số đĩa đang lắp, ngày "
        "và lịch sử sự cố vỡ, chu kỳ thay thế đã thỏa thuận, cùng hướng dẫn "
        "đặt hàng và cất giữ. Chỉ nhân sự được đào tạo về lựa chọn, lắp đặt "
        "và bảo trì nên chỉ định, mua và lắp đĩa vỡ.",
        "Each plant should keep records of installed disc location and "
        "specification, failure dates and history, agreed replacement "
        "periods, and ordering and storage instructions. Only personnel "
        "trained in selection, installation and maintenance should specify, "
        "procure and install rupture discs.")])

    # =========================================================== explosion venting
    H("Thông hơi nổ", "Explosion venting")
    P("Nhiều bột công nghiệp và khí cháy tạo hỗn hợp nổ khi phân tán trong "
      "không khí. Khi bắt lửa, áp tăng gần như ngay lập tức có thể vỡ bao "
      "bọc yếu nếu không có cửa thông đủ kích thước. Tấm thông nổ thường "
      "hình chữ nhật hoặc tròn, được tính toán để giữ áp trong bình dưới mức "
      "an toàn (Hình 6-35). Hình 6-36 biểu diễn đường áp theo thời gian: "
      "Pstat là áp mở tấm thông, Pred là áp nổ đã giảm, Pult là áp bền cuối "
      "của bình và Pmax là áp của vụ nổ không thông hơi.",
      "Many industrial powders and flammable gases form explosive mixtures "
      "when dispersed in air. On ignition, pressure rises almost instantly "
      "and can rupture weak enclosures without adequate venting. Rectangular "
      "or circular vent panels are sized to keep enclosure pressure below a "
      "safe level (Figure 6-35). Figure 6-36 shows pressure versus time: "
      "Pstat is vent-opening pressure, Pred the reduced explosion pressure, "
      "Pult the enclosure's ultimate sustainable pressure and Pmax the "
      "unvented explosion pressure.")
    FIG(35, F13.fig_vsh_6_35())
    FIG(36, F13.fig_vsh_6_36())
    P("Khi bụi cháy chậm trong thiết bị, lượng bụi thường nhiều hơn oxy cần "
      "để cháy hết. Khi xả, bụi chưa cháy trộn với không khí mới và có thể "
      "tạo quả cầu lửa; một thử nghiệm ghi nhận đám lửa kéo dài ít nhất 4 m "
      "xuống dưới cửa thông và khoảng 15 m theo phương ngang (Hình 6-37). "
      "Người ở trong vùng đó có thể không sống sót. Thiết bị được bảo vệ vì "
      "thế phải bố trí để che chở nhân sự và ngăn nổ thứ phát.",
      "In a dust deflagration, far more dust is present than oxidant needed "
      "to burn it completely. Venting mixes unburned dust with fresh air and "
      "can form a fireball; one test extended at least 4 m below the vent "
      "and about 15 m horizontally (Figure 6-37). Personnel enveloped by "
      "such a fireball might not survive. Protected plant must therefore be "
      "positioned to shield personnel and prevent secondary explosions.")
    FIG(37, F13.fig_vsh_6_37())
    P("Nếu thiết bị thông nổ phải đặt trong nhà, nên đặt gần tường ngoài để "
      "ống dẫn ngắn, tốt nhất không quá 3 m. Với hạng nguy hiểm bụi KST đến "
      "250 bar·m/s, có thể dùng tấm thông kết hợp bẫy lửa dạng ống hoặc hệ "
      "thống thông dập ngọn lửa (Hình 6-38). Khí vào bẫy ở nhiệt độ tới "
      "1500 °C ra ở nhiệt độ dưới 100 °C; độ giảm nhiệt làm thể tích khí "
      "thoát ra nhỏ hơn khoảng 10 lần so với xả không hạn chế. Tấm lọc gốm "
      "tích hợp giữ lại toàn bộ chất rắn. Cấu trúc này cho phép thông nổ "
      "trong phòng kín; lối đi qua bẫy lửa chỉ cần che chắn chống hiệu ứng "
      "bất ngờ.",
      "Where vented equipment must stand inside a building, locate it near "
      "an exterior wall with ducts as short as possible, preferably no more "
      "than 3 m. For dust hazard class KST up to 250 bar·m/s, a vent panel "
      "may be combined with a tubular flame trap or flame-quenching vent "
      "system (Figure 6-38). Gas entering at up to 1500 °C leaves below "
      "100 °C, reducing escaping gas volume by about ten times compared with "
      "unrestrained venting. An integrated ceramic filter mat retains all "
      "solids. This permits venting inside closed rooms; passages past the "
      "trap need only shielding against surprise effect.")
    FIG(38, F13.fig_vsh_6_38())

    # ================================================================== table
    H("Bảng tóm tắt lựa chọn và thông hơi", "Selection and venting summary")
    b.append(table(
        ["Hình / chủ đề", "Quyết định", "Điểm chính"]
        if vi else ["Figure / topic", "Decision", "Key point"],
        [
            ["6-34", "Đĩa là thiết bị duy nhất" if vi else "Disc as sole device",
             "Áp vận hành ≤57% MAWP" if vi else "Operating ≤57% MAWP"],
            ["6-34", "Hiệu áp 10%" if vi else "10% differential",
             "Zero range, 90–95% ratio, ±2%"
             if vi else "Zero range, 90–95% ratio, ±2%"],
            ["đầu vào van" if vi else "Valve inlet",
             "Đĩa trước van" if vi else "Disc upstream of valve",
             "Mở đồng thời, bộ báo rò, 90% lưu lượng"
             if vi else "Unison opening, telltale, 90% capacity"],
            ["đầu ra van" if vi else "Valve outlet",
             "Đĩa sau van" if vi else "Disc downstream of valve",
             "Báo rò, nên dùng van cân bằng"
             if vi else "Telltale, balanced valve suggested"],
            ["cả hai đầu" if vi else "Both ends",
             "Đĩa trước và sau van" if vi else "Discs upstream and downstream",
             "Van cân bằng kiểu mở bật"
             if vi else "Balanced pop-action valve"],
            ["đặt lại hàng" if vi else "Reordering",
             "Ghi số lô" if vi else "Quote lot number",
             "Áp ghi nhãn có thể đổi giữa các lần"
             if vi else "Marked pressure may vary between orders"],
            ["6-35…6-36", "Tấm thông nổ" if vi else "Explosion vent panel",
             "Pstat, Pred, Pult, Pmax" if vi else "Pstat, Pred, Pult, Pmax"],
            ["6-37", "Nguy cơ đám lửa" if vi else "Fireball hazard",
             "~4 m xuống, ~15 m ngang" if vi else "~4 m down, ~15 m across"],
            ["6-38", "Bẫy lửa dạng ống" if vi else "Tubular flame trap",
             "1500 °C → dưới 100 °C; ống ≤3 m"
             if vi else "1500 °C to below 100 °C; duct ≤3 m"],
        ],
        caption=("Tóm tắt theo văn bản nguồn, book pp. 261–267, "
                 "Hình 6-34…6-38." if vi else
                 "Summary from source text, book pp. 261–267, "
                 "Figures 6-34…6-38."),
        cls="tbl wide"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
