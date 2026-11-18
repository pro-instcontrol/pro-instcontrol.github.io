# -*- coding: utf-8 -*-
"""Book 6, Unit 13 — Direct-Loaded Pressure Relief Valves (EN/VI).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 176–212 (PDF pp. 190–226): review of direct loading, safety, safety
relief, liquid and vacuum relief valves, auxiliary actuators, oscillation
dampers, certification, force/lift diagrams, inlet losses, and in-situ
verification (Figures 5-1…5-34).
"""

from vsh_common import fig, h2, h3, p, table, ul
import vshfig10 as F10

PAGES_SRC = 37         # source book pp. 176-212
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Direct-Loaded Pressure Relief Valves"
TITLE_VI = "Van an toàn xả tải trực tiếp"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 13.</b> pressure relief valve — van an "
                "toàn xả · direct-loaded — tải trực tiếp · set pressure — "
                "áp suất cài đặt · overpressure — áp suất vượt · blowdown — "
                "độ giảm áp đóng lại · popping pressure — áp suất mở bật · "
                "reseating pressure — áp suất đóng lại · huddling chamber — "
                "buồng tụ áp · safety valve — van an toàn hơi · safety relief "
                "valve — van an toàn xả đa dụng · bellows-balanced — cân bằng "
                "bằng ống màng · superimposed / built-up back pressure — áp "
                "suất ngược cộng thêm / tích tụ · chatter — rung đĩa chạm béc "
                "· flutter — rung đĩa không chạm béc · simmer — xì nhẹ trước "
                "áp cài đặt · Belleville spring — lò xo đĩa · oscillation "
                "damper — bộ giảm dao động · force/lift diagram — đồ thị "
                "lực/nâng.")
    return ("<b>Key terms.</b> pressure relief valve · direct-loaded · set "
            "pressure · overpressure · blowdown · popping pressure · "
            "reseating pressure · huddling chamber · safety valve · safety "
            "relief valve · bellows-balanced · superimposed / built-up back "
            "pressure · chatter · flutter · simmer · Belleville spring · "
            "oscillation damper · force/lift diagram.")


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

    # ================================================================ review
    H("Tổng quan", "Review")
    P("Van an toàn xả sơ kỳ là van tải trực tiếp bằng trọng lượng, đĩa có "
      "dạng van cầu, thường dạng nón hoặc phẳng. Khi áp suất nâng đĩa khỏi "
      "chỗ kín, dòng thoát không truyền nhiều động năng cho đĩa nên độ nâng "
      "rất nhỏ trong giới hạn áp vượt cho phép. Nhưng Charles Ritchie người "
      "Anh đã có bước tiến quan trọng năm 1848: ông dùng tính giãn nở của "
      "khí để nâng đĩa nhờ vành chuyển dòng và môi quanh chỗ kín, tạo buồng "
      "tụ áp hình vòng với lỗ phụ (Hình 5-1). Khi van bắt đầu mở, khí giãn "
      "trong buồng nhưng không thoát ngay, áp suất tĩnh tăng vọt và tác dụng "
      "trên diện tích lớn hơn phía dưới đĩa làm van mở bật.",
      "Early pressure relief valves were direct-loaded by a weight, with a "
      "globe-shaped tapered or flat disc. Escaping fluid imparted little "
      "kinetic energy, so lift was very small within allowable overpressure. "
      "In 1848 Charles Ritchie exploited gas expansion: a peripheral flow "
      "deflector and lip formed an annular chamber with a secondary orifice "
      "(Figure 5-1). As the valve opened, gas expanded but could not readily "
      "escape, static pressure rose sharply over an enlarged disc area and "
      "the valve popped open.")
    FIG(1, F10.fig_vsh_5_1())
    P("Vì dòng chỉ đổi hướng khoảng 90°, chỉ một phần động năng biến thành "
      "lực nâng và van chỉ mở một phần trong áp vượt thường cho phép. Khi áp "
      "vượt giảm, áp suất trong buồng tụ áp lại tăng làm đĩa còn lơ lửng "
      "trước khi áp làm việc giảm dưới áp cài đặt; hiệu số giữa áp cài đặt "
      "và áp đóng lại gọi là blowdown. Chất lỏng không nén được nên không "
      "tạo được sự tăng áp đột ngột trong buồng, van chỉ mở nhẹ khi áp vượt "
      "tăng.",
      "With only about 90° of deflection, part of the kinetic energy became "
      "lifting force and the valve opened only partially within normal "
      "overpressure. As overpressure receded, chamber pressure rebuilt and "
      "the disc huddled above the seat until operating pressure fell below "
      "set pressure; the difference is blowdown. Liquids cannot develop the "
      "sudden chamber pressure rise, so the valve initially opens only a "
      "little.")
    P("Năm 1863 William Naylor đưa ra van có môi quanh đĩa dẫn dòng quay "
      "180° (Hình 5-2), truyền động lượng cực đại cho đĩa. Tuy độ mở chỉ tỉ "
      "lệ với áp vượt nên lưu lượng và lực nâng ban đầu vẫn quá nhỏ. Thiết "
      "kế hiện đại kết hợp hai nguyên lý: môi tạo buồng tụ áp với lỗ phụ "
      "đồng thời đổi hướng dòng khoảng 180°. Từ đó đã có van xả chất lỏng "
      "mở hoàn toàn trong áp vượt 10%.",
      "In 1863 William Naylor's lip turned discharge through 180° "
      "(Figure 5-2), giving maximum momentum lift, but lift still depended "
      "on rising overpressure. Modern designs combine both principles: a lip "
      "forms the annular chamber and secondary orifice while deflecting flow "
      "about 180°. Liquid relief valves based on this design now open fully "
      "within 10% overpressure.")
    FIG(2, F10.fig_vsh_5_2())
    P("Các van đầu dùng trọng lượng vì lò xo thời đó khó chế tạo và người ta "
      "phản đối đặc tính lò xo làm tăng tải khi đĩa nhấc. Nhưng trọng lượng "
      "nhanh lớn và không thực tế khi cỡ van và áp suất tăng; cần đòn kéo "
      "dài thêm được phạm vi dùng nhưng khó che chắn khỏi tác động trái phép. "
      "Tải lò xo khắc phục các nhược điểm và có thể phối hợp đặc tính lò xo "
      "với đặc tính lực nâng của chất lỏng, nên hầu hết van tải trực tiếp "
      "hiện nay dùng lò xo, trừ một số van áp thấp theo quy phạm.",
      "Early valves used weights because good springs were hard to make and "
      "the rising spring load with lift was objected to. Weights soon became "
      "impractical; lever mounting helped but could not easily be enclosed "
      "against tampering. Spring loading overcame these drawbacks and can be "
      "matched to the fluid lifting-force characteristic, so nearly all "
      "direct-loaded valves are now spring-loaded except some low-pressure "
      "duties.")

    # ---------------------------------------------------------- safety valves
    H("Van an toàn", "Safety valves")
    P("Van an toàn như Hình 5-3 đến 5-6 chủ yếu xả hơi cho lò hơi công "
      "nghiệp và hệ thống hơi khác. Thiết kế nhằm bảo vệ lò xo khỏi nóng quá "
      "mức gây trôi cài đặt và có thể suy giảm lò xo theo thời gian. Vì vậy "
      "nắp thường hở để hơi rò vào nắp thoát thẳng ra khí quyển.",
      "Safety valves such as Figures 5-3 to 5-6 primarily relieve steam in "
      "industrial boiler plants and steam systems. Their design protects the "
      "spring from excessive temperature that could drift the setting or "
      "relax the spring; an open bonnet lets steam leaking into it escape "
      "directly to atmosphere.")
    FIG(3, F10.fig_vsh_5_3())
    FIG(4, F10.fig_vsh_5_4())
    P("Hình 5-4 lắp thêm vòng làm mát giữa thân và nắp để bảo vệ lò xo tốt "
      "hơn. Hình 5-6 có cơ cấu hút (eductor) tạo bởi các kênh quanh đĩa: khi "
      "van mở bật, eductor hút sạch buồng phía trên đĩa, giúp đóng mở sắc "
      "dọn.",
      "Figure 5-4 adds a cooling (lantern) spool between body and bonnet. "
      "Figure 5-6 incorporates an eductor formed by channels around the disc; "
      "when the valve pops, it evacuates the chamber above the disc to assist "
      "sharp opening and closing.")
    FIG(5, F10.fig_vsh_5_5())
    FIG(6, F10.fig_vsh_5_6())
    P("Đĩa van an toàn thường dẫn trong bạc có vòng ren để đổi hướng chuyển "
      "dòng của chất thoát, từ đó đổi lực phản tác dụng dưới đĩa. Hạ vòng dẫn "
      "làm blowdown dài ra; nâng lên làm blowdown ngắn lại. Vòng thứ hai dưới "
      "béc là vòng béc, chủ yếu điều khiển hiệu số giữa áp cài đặt và áp mở "
      "bật: nâng vòng béc thu hẹp lỗ phụ nên mở bật sớm hơn nhưng blowdown "
      "dài thêm một chút; hạ vòng thì ngược lại. Vòng dưới cùng thường được "
      "nhà chế tạo cài sẵn và không cần chỉnh lại; không nên cố xóa hoàn toàn "
      "hiệu số giữa áp cài đặt và áp mở bật. Ở Hình 5-5 không có vòng béc: "
      "chiều rộng lỗ phụ do hình học chỗ kín và đĩa quyết định.",
      "The disc is commonly guided in a sleeve with a screwed ring that "
      "changes flow deflection and reaction force under the disc. Lowering "
      "the guide ring lengthens blowdown; raising it shortens blowdown. The "
      "nozzle ring controls the difference between set and popping pressure: "
      "raising it narrows the secondary orifice, popping earlier but adding "
      "a little blowdown; lowering it has the reverse effect. The lower ring "
      "is factory set and should not be readjusted; the set-to-pop difference "
      "should not be eliminated. Figure 5-5 has no nozzle ring — geometry "
      "of seat and disc fixes the secondary orifice.")
    P("Van an toàn nắp hở được cân bằng một phần nhờ bạc dẫn cần, có thể chịu "
      "áp suất ngược tích tụ khoảng 20% nhưng phải hỏi nhà chế tạo. Chúng "
      "không hợp cho áp suất ngược cộng thêm vì hơi rò quanh cần vào nắp; "
      "vì lý do đó không nên lắp nhiều van an toàn chung một đường xả (manifold).",
      "Open-bonnet safety valves are partially balanced by the stem guide and "
      "may tolerate about 20% built-up back pressure, subject to the maker. "
      "They are unsuitable for superimposed back pressure because of leakage "
      "around the stem into the bonnet; they should not be manifolded.")

    # ------------------------------------------------------ safety relief
    H("Van an toàn xả", "Safety relief valves")
    P("Van an toàn xả là van đa dụng cho khí hoặc chất lỏng trong công "
      "nghiệp quá trình. Vì chất lỏng công nghiệp thường không được phép rò "
      "ra ngoài, nắp van hoặc thông sang đầu ra hoặc được làm kín bằng ống "
      "màng; riêng van hơi quá trình có nắp mở cửa sổ như van an toàn. Với "
      "khí hoặc hơi, van mở bật; với chất lỏng, van mở điều tiết và đạt mở "
      "hoàn toàn ở áp vượt khoảng 25%, hoặc 10% ở thiết kế mới như Hình "
      "5-7 và 5-10.",
      "Safety relief valves are general-purpose valves for gas or liquid in "
      "the process industries. Since process fluids normally cannot be "
      "allowed to escape, the bonnet is vented to the outlet or sealed by "
      "bellows; process-steam types may have windowed bonnets like safety "
      "valves. On gas or vapour they pop open; on liquid they modulate and "
      "reach full lift at about 25% overpressure, or 10% in newer designs "
      "such as Figures 5-7 and 5-10.")
    P("Ngành phân biệt van an toàn xả thông thường và van cân bằng. Loại "
      "thông thường có nắp kín thông sang đầu ra (Hình 5-7, 5-8), để áp "
      "suất ngược tác dụng lên toàn bộ mặt sau đĩa. Trước khi mở, các lực "
      "từ áp ngược trên phần đĩa vượt ra ngoài béc tự cân bằng, nhưng diện "
      "tích phía sau nằm trong béc thì không cân bằng: áp ngược cộng thêm "
      "làm tăng áp cài đặt đúng bằng giá trị đó, nên phải hạ cài đặt trên "
      "bàn thử. Vì lý do này van thông thường không hợp áp ngược cộng thêm "
      "thay đổi và không nên lắp chung đường xả.",
      "The industry distinguishes conventional and balanced safety relief "
      "valves. Conventional types have a closed bonnet vented to the outlet "
      "(Figures 5-7, 5-8), so back pressure acts on the whole back of the "
      "disc. Before opening, back-pressure forces on the overhanging disc "
      "balance, but the area over the nozzle is unbalanced: superimposed "
      "back pressure raises set pressure by its own amount, so the bench "
      "setting must be lowered. They are therefore unsuitable for variable "
      "superimposed back pressure and should not be manifolded.")
    FIG(7, F10.fig_vsh_5_7())
    FIG(8, F10.fig_vsh_5_8())
    P("Khi van mở, áp suất ngược tích tụ tạo lực đóng trên diện tích không "
      "cân bằng, nên thường chỉ dùng khi xả qua đường ngắn giữ áp ngược tích "
      "tụ khoảng 10% áp cài đặt; van có blowdown lớn hoặc chỉnh được có thể "
      "cho phép 15% trở lên (hỏi nhà chế tạo). Nếu áp ngược cộng thêm không "
      "đổi và không đổi theo thời gian, có thể chỉnh lò xo theo chênh áp qua "
      "béc để dùng tới 50% áp cài đặt. Hình 5-9 là van chuyển sang hơi bằng "
      "nắp hở, trở thành van cân bằng một phần, cho phép áp tích tụ khoảng "
      "20% sau khi nhà chế tạo xác nhận. Việc lắp cần nâng kiểu thông thường "
      "cũng gây hiệu ứng tương tự.",
      "On opening, built-up back pressure creates a closing force on the "
      "unbalanced area, limiting conventional valves to short discharge lines "
      "with built-up back pressure around 10% of set pressure; high or "
      "adjustable blowdown designs may allow 15% or more. Constant "
      "superimposed back pressure can be compensated by spring setting for "
      "differential pressure, up to 50%. Figure 5-9 converts a valve to steam "
      "duty with an open bonnet, making it partially balanced for about 20% "
      "built-up back pressure; an ordinary lifting lever has the same effect.")
    FIG(9, F10.fig_vsh_5_9())
    P("Van cân bằng như Hình 5-10 đến 5-12 dùng ống màng cân bằng giữa đĩa "
      "và nắp thông hơi, đưa diện tích không cân bằng về áp khí quyển hằng "
      "định. Khi mở, áp ngược chỉ ép lên phần đĩa vượt ngoài chỗ kín; tuy "
      "áp ngược làm ống màng dãn dài và cứng hơn nên chống nhấc đĩa hơn. Van "
      "cân bằng thường đạt lưu lượng định mức ở áp ngược khoảng 20–40%, tùy "
      "kiểu và cỡ; khi giảm lưu lượng có thể dùng tới khoảng 50%. Có thể thêm "
      "chỗ kín piston phụ (Hình 5-11) phòng hỏng ống màng, và nắp thông hơi "
      "phải dẫn đến nơi an toàn tùy chất lỏng. Không phải van nào gọi là cân "
      "bằng cũng cân bằng hoàn toàn: van theo API 526 cỡ béc D và E có khi "
      "không lắp được ống màng cân bằng nên vẫn chịu áp ngược thay đổi.",
      "Balanced valves (Figures 5-10 to 5-12) use a balancing bellows between "
      "disc and vented bonnet, exposing the unbalanced area to constant "
      "atmosphere. On opening, back pressure only closes the disc overhang; "
      "it also elongates and stiffens the bellows, resisting lift. They are "
      "rated at 20–40% back pressure and offered up to about 50% with reduced "
      "capacity. An auxiliary piston seal (Figure 5-11) guards against "
      "bellows failure and vents must lead to a safe place. Not every "
      "so-called balanced valve is truly balanced: API 526 valves with D and "
      "E orifices may be too small for balancing bellows and remain sensitive "
      "to variable back pressure.")
    FIG(10, F10.fig_vsh_5_10())
    FIG(11, F10.fig_vsh_5_11())
    FIG(12, F10.fig_vsh_5_12())
    P("Chỉnh blowdown van an toàn xả thường bằng vòng béc chỉnh như Hình "
      "5-7: đặt vòng trên béc giúp đĩa được dẫn xa dòng va trực tiếp, bền "
      "hơn với chất có rắn lơ lửng, và cùng ống màng cân bằng có thể cách ly "
      "hoàn toàn bạc dẫn, lò xo khỏi chất lỏng. Nâng vòng béc làm blowdown "
      "dài nhưng áp làm việc giảm và áp mở bật thấp đi; hạ vòng làm blowdown "
      "ngắn nhưng áp mở bật tăng và simmer nhiều hơn. Nhà chế tạo thường đặt "
      "vòng gần giá đĩa để chống ảnh hưởng bất lợi của tổn thất áp đầu vào "
      "đến độ ổn định; Hình 5-12 bỏ hẳn vòng béc. Hình 5-8 chỉnh blowdown "
      "bằng vít bên ngoài làm tiết lưu một lỗ dẫn, thay đổi áp ngược dưới "
      "đĩa mà không đổi áp cài đặt; cùng ghế mềm, van dùng xả nhiệt lượng "
      "nhỏ của LPG, amonia hoặc chất làm lạnh, nơi simmer giữa hai mặt kim "
      "loại có thể gây đóng băng nghiêm trọng.",
      "Blowdown adjustment is commonly by a nozzle ring as in Figure 5-7, "
      "keeping the disc guide out of direct flow impact for solids-bearing "
      "fluids and, with balanced bellows, isolating guide and spring from the "
      "fluid. Raising the ring lengthens blowdown but lowers popping pressure "
      "and operating differential; lowering it shortens blowdown but raises "
      "popping pressure and simmer. Makers usually set the ring near the disc "
      "holder for stability; Figure 5-12 omits it. Figure 5-8 adjusts "
      "blowdown externally by restricting a guide hole, changing back "
      "pressure under the disc without moving set pressure; with soft "
      "seatings it thermally relieves small amounts of LPG, ammonia or "
      "refrigerants where metal-to-metal simmer could cause severe icing.")

    # ---------------------------------------------------------- liquid relief
    H("Van xả chất lỏng", "Liquid relief valves")
    P("Van xả chất lỏng thường chỉ khác van an toàn xả thông thường ở hình "
      "học quanh đĩa nhằm đạt hiệu năng riêng. Hình 5-13 mở hoàn toàn trong "
      "10% áp vượt và làm việc ổn định trên dải rộng, blowdown chỉnh bằng "
      "vòng béc. Hình 5-14 là van cân bằng có hai O-ring trên cần: O-ring "
      "dưới là vòng cản được cấp áp qua lỗ trên đĩa và cần, ma sát khi đóng "
      "mở chống rung không kiểm soát; O-ring trên làm kín cân bằng với áp "
      "ngược, và lỗ trên nắp thông hơi khi rò.",
      "Liquid relief valves usually differ only slightly in disc geometry. "
      "Figure 5-13 opens fully within 10% overpressure, stays stable over a "
      "wide range and has nozzle-ring blowdown adjustment. Figure 5-14 is "
      "balanced with two stem O-rings: the lower drag ring is energized by "
      "inlet pressure through bores in disc and stem and its friction "
      "prevents uncontrolled chatter; the upper ring seals against back "
      "pressure and a bonnet hole vents leakage.")
    FIG(13, F10.fig_vsh_5_13())
    FIG(14, F10.fig_vsh_5_14())
    P("Hình 5-15 là van xả tỉ lệ có đặc tính mở tuyến tính, dùng khi cần xả "
      "trên dải tải rộng. Béc loe ra nên thay đổi lưu lượng chỉ gây dịch đĩa "
      "rất nhỏ; thử nghiệm cho thấy ma sát trong đủ chặn dao động ngay cả khi "
      "lưu lượng khối tăng nhanh. Hình 5-16 trình bày đặc tính mở và đóng "
      "của van. Vì chất lỏng gần như không nén và có mật độ lớn hơn khí, "
      "thay đổi nhỏ về vận tốc vào gây thay đổi áp suất lớn, lập tức biến "
      "thành thay đổi độ nâng rồi lại ảnh hưởng ngược lại áp suất. Van xả "
      "chất lỏng vì thế dễ rung hơn van khí, nhưng bộ giảm ma sát như Hình "
      "5-14 có thể loại bỏ hoàn toàn hiện tượng này.",
      "Figure 5-15 is a proportional valve with a linear opening "
      "characteristic for wide load ranges. Its flared nozzle means flow "
      "changes cause only small disc movements; tests show internal friction "
      "checks oscillation even at rapidly accelerating mass flow. Figure "
      "5-16 shows its opening and closing characteristics. Because liquids "
      "are nearly incompressible and dense, small inlet-velocity changes "
      "produce large pressure changes that immediately change lift, which in "
      "turn affects pressure. Liquid valves are therefore more prone to "
      "chatter than gas valves, though friction dampers such as Figure 5-14 "
      "can avoid it entirely.")
    FIG(15, F10.fig_vsh_5_15())
    FIG(16, F10.fig_vsh_5_16())

    # ----------------------------------------------------------- vacuum valves
    H("Van xả chân không", "Vacuum relief valves")
    P("Hình 5-17 đến 5-19 là ba kiểu van xả chân không tải trực tiếp, có "
      "hoặc có thể ghép với xả áp dương. Hình 5-17 chỉ dùng trọng lượng nhẹ "
      "của đĩa để tải; để kín chặt với tải nhỏ như vậy, chỗ kín dùng cao su "
      "xốp và cần dẫn phủ PTFE cho đĩa dễ dịch. Thân được thiết kế ghép được "
      "với van xả áp dương.",
      "Figures 5-17 to 5-19 show three direct-loaded vacuum relief valves, "
      "combined or combinable with positive overpressure relief. Figure 5-17 "
      "relies solely on the light disc weight; seat tightness comes from a "
      "sponge-rubber seal and a PTFE-coated guide rod. Its body can be "
      "combined with an overpressure valve.")
    FIG(17, F10.fig_vsh_5_17())
    P("Hình 5-18 ghép xả chân không với xả áp dương, thiết kế cho dịch vụ vệ "
      "sinh trong đồ uống, chế biến thực phẩm và dược phẩm. Hình 5-19 là van "
      "thông hơi mang riêng hai van: đĩa mở theo cung quanh bản lề tiếp xúc "
      "điểm, gioăng màng mềm giúp đóng lại gần áp cài đặt, dùng cho bồn chứa "
      "áp thấp.",
      "Figure 5-18 combines vacuum and positive pressure relief for sanitary "
      "beverage, food and pharmaceutical service. Figure 5-19 is a breather "
      "valve carrying separate vacuum and overpressure valves whose discs "
      "swing in arcs on point-contact hinges; soft diaphragm seals let them "
      "reseat close to set pressure. It serves low-pressure storage tanks.")
    FIG(18, F10.fig_vsh_5_18())
    FIG(19, F10.fig_vsh_5_19())

    # ------------------------------------------------------- auxiliary actuation
    H("Van có cơ cấu phụ trợ", "Valves with auxiliary actuator")
    P("Nhu cầu làm kín tốt hơn khi van làm việc gần áp cài đặt và nhu cầu "
      "chống rung trong lắp đặt khó dẫn đến van tải trực tiếp kết hợp cơ cấu "
      "phụ trợ. Nguồn lực thường là khí nén cùng điện; nếu mất nguồn, van vẫn "
      "đóng mở không bị cản như van tải lò xo thông thường. Ba dạng đã phát "
      "triển: van hỗ trợ chống rung; van có tải bổ sung hạn chế chống xì; và "
      "van có tải bổ sung không hạn chế và/hoặc hỗ trợ nâng.",
      "The need for tighter seal near set pressure and for chatter "
      "suppression in difficult installations led to direct-loaded valves "
      "with auxiliary actuators, usually compressed air with electricity. On "
      "power failure the valve still operates unhindered as a spring-loaded "
      "valve. Three types evolved: assisted (anti-chatter), supplementary-"
      "loaded with restricted load (anti-simmer), and unrestricted "
      "supplementary loading and/or lift assistance.")
    P("Van hỗ trợ như Hình 5-20 và sơ đồ điều khiển Hình 5-21: khi làm việc "
      "bình thường cơ cấu hỗ trợ không hoạt động; khi cần mở, nó tạo lực mở "
      "bổ sung không hạn chế; khi áp an toàn phục hồi thì ngắt và van đóng "
      "bình thường. Mất nguồn thì van đóng mở không bị cản trở.",
      "In the assisted valve of Figure 5-20 and its piping (Figure 5-21), the "
      "assist device is inactive in normal operation, introduces unrestricted "
      "supplementary opening force when the valve is called upon to open, "
      "then deactivates. Power failure leaves the valve unhindered.")
    FIG(20, F10.fig_vsh_5_20())
    FIG(21, F10.fig_vsh_5_21())
    P("Van tải bổ sung hạn chế như Hình 5-22 và Hình 5-23 tạo thêm lực đóng "
      "trong giới hạn quy phạm khi vận hành bình thường. Khi cần mở, tải bổ "
      "sung được tháo và van mở như van an toàn xả tải lò xo. Nếu tải không "
      "được tháo, van vẫn mở hoàn toàn chống lại tải đó để đạt lưu lượng "
      "định mức trong áp vượt cho phép. Van còn có cơ cấu an toàn toàn cơ "
      "khí tự ngắt kết nối với cần khi áp vượt tăng, kèm cần tay nhả tải. "
      "Mất nguồn điều khiển thì van đóng mở như van an toàn xả bình thường.",
      "The restricted supplementary-loaded valve (Figures 5-22, 5-23) adds a "
      "permitted closing force in normal operation; when opening is called "
      "for, the load is removed and the valve behaves as a spring-loaded "
      "safety relief valve. If removal fails, the valve still opens fully "
      "against the load to deliver rated capacity within permissible "
      "overpressure. A mechanical fail-safe disconnects the loading device "
      "from the stem as overpressure rises, with a manual release lever. "
      "Control-power failure restores ordinary operation.")
    FIG(22, F10.fig_vsh_5_22())
    FIG(23, F10.fig_vsh_5_23())
    P("Hình 5-24 là van lò xo kết hợp cơ cấu tải và hỗ trợ nâng khí nén, có "
      "ba đường điều khiển giống hệt nhau. Nhờ van liên khóa, từng đường có "
      "thể đưa ra khỏi dịch vụ để thử, sửa hoặc thay mà không làm gián đoạn "
      "van an toàn. Khi vận hành bình thường các van xả điện từ M1 đến M3 "
      "đóng và M4 xả buồng H ra khí quyển; khí nén vào buồng B tạo tải ép. "
      "Khi cần mở, công tắc áp làm M1…M3 mở xả khí và M4 cấp khí vào H: buồng "
      "B giảm áp trong khi khí vào H hỗ trợ nâng đĩa. Hệ thống cho phép "
      "điều khiển chặt chẽ đóng mở và có thể dùng chỉ cho tải bổ sung hoặc "
      "chỉ cho hỗ trợ nâng.",
      "Figure 5-24 combines a spring valve with pneumatic loading and lift "
      "assistance and three identical control lines; interlocked valving lets "
      "one line be removed for test or repair without disturbing relief "
      "operation. Normally solenoid vents M1–M3 are closed and M4 vents "
      "chamber H, while air entering chamber B adds seating load. To open, "
      "pressure switches de-energise M1–M3 to atmosphere and energise M4 to "
      "admit air to H: B depressurises while H assists lift. The system gives "
      "close control and can be arranged for supplementary loading or lift "
      "assistance alone.")
    FIG(24, F10.fig_vsh_5_24())
    P("Hình 5-25 và 5-26 là hai van áp suất cao, lưu lượng lớn dùng bộ lò xo "
      "đĩa Belleville làm cơ cấu tải, kết hợp cơ cấu khí nén phụ và hệ điều "
      "khiển giống hoặc tương tự Hình 5-24; chúng dùng trong nhà máy nhiệt "
      "điện thông thường và nhà máy điện hạt nhân.",
      "Figures 5-25 and 5-26 are high-pressure, high-capacity valves whose "
      "loading device is a Belleville disc spring stack, combined with an "
      "auxiliary pneumatic actuator and a control system like Figure 5-24; "
      "they are used in conventional and nuclear power plants.")
    FIG(25, F10.fig_vsh_5_25())
    FIG(26, F10.fig_vsh_5_26())

    # --------------------------------------------------------------- dampers
    H("Bộ giảm dao động", "Oscillation dampers")
    P("Bộ giảm dao động là thiết bị ma sát tác dụng lên cần mang đĩa. Hình "
      "5-14, 5-27 và 5-28 cho thấy ba cách kết hợp với van tải trực tiếp. "
      "Hình 5-27 dùng ma sát khô với các phần tử hình thấu kính bằng than "
      "chì điện cứng, nén trong buồng bằng lò xo ép vào cần, cho phép chỉnh "
      "lượng ma sát theo ứng dụng. Than chì điện cứng có độ phân tán ma sát "
      "động nhỏ, hiệu số ma sát tĩnh và động cũng nhỏ nên lực gần đều theo "
      "hành trình; ma sát tĩnh thấp nên ảnh hưởng đến áp cài đặt có thể tính "
      "được khi chỉnh van.",
      "Oscillation dampers are friction devices acting on the stem. Figures "
      "5-14, 5-27 and 5-28 show three combinations with direct-loaded valves. "
      "Figure 5-27 uses dry friction from lens-shaped hard electro-graphite "
      "elements packed in a chamber and spring-loaded against the stem, "
      "allowing the friction to be set for the application. The material has "
      "little dynamic friction scatter and a small static-dynamic difference, "
      "so force is fairly uniform over lift; low static friction can be "
      "allowed for when setting the valve.")
    FIG(27, F10.fig_vsh_5_27())
    P("Với biên độ dao động rất nhỏ hoặc tần số thấp, một lượng ma sát khô "
      "nhỏ tương đương với giảm chấn nhớt rất lớn: không có nhiễu động đáng "
      "kể, ma sát khô chặn rung rất hiệu quả. Nhưng nếu nhiễu động vượt giới "
      "hạn thiết kế, bộ giảm có thể không dập được dao động. Hình 5-28 dùng "
      "ma sát nhớt: các trục đồng tâm khít nhau với khe hở nhỏ chứa mỡ nhớt "
      "đặc chủng; khi van đóng mở, các trục trượt tạo lực tỉ lệ vận tốc. Lực "
      "chỉnh được bằng khe hở và diện tích bề mặt, tự thích ứng theo yêu cầu "
      "và chặn rung bất kể mức nhiễu động. Cả hai thiết kế trong Hình 5-27 và "
      "5-28 đã được TÜV Đức thử nghiệm và chứng nhận.",
      "At very small amplitudes or low frequencies, even little dry friction "
      "equals a large viscous damping effect, so it effectively prevents "
      "chatter without significant disturbance; beyond design limits it may "
      "not. Figure 5-28 uses viscous friction: close-fitting concentric "
      "cylinders with a narrow grease-filled gap glide relative to each "
      "other, producing speed-dependent forces. Force is adjusted by gap "
      "width and surface area; viscous damping self-adjusts and can prevent "
      "chatter regardless of disturbance size. Both designs were tested and "
      "certified by TÜV Germany.")
    FIG(28, F10.fig_vsh_5_28())

    # ----------------------------------------------------------- certification
    H("Chứng nhận hiệu năng van", "Certification of valve performance")
    P("Bộ luật ASME Boiler and Pressure Vessel yêu cầu nhà chế tạo chứng minh "
      "hiệu năng và lưu lượng xả bằng thử nghiệm tại cơ sở được ASME chấp "
      "nhận; cơ quan thực hiện là National Board of Boiler and Pressure "
      "Vessel Inspectors. Phương pháp và quy trình nằm trong ASME PTC 25-1994 "
      "(bản cập nhật mới nhất). Áp suất thiết kế tối thiểu theo ASME vào "
      "khoảng 15 psi (1,03 bar), nên quy tắc ASME nói chung không áp dụng cho "
      "van áp thấp hơn. Thử nghiệm thường ở áp vượt 3% hoặc 10%, tối thiểu "
      "3 psi (0,207 bar), tùy phần quy phạm.",
      "The ASME Boiler and Pressure Vessel Code requires manufacturers to "
      "demonstrate performance and capacity by test at an ASME-approved "
      "facility; certification is conducted by the National Board of Boiler "
      "and Pressure Vessel Inspectors. Methods are in ASME PTC 25-1994 "
      "(latest revision). The minimum ASME design pressure is about 15 psi "
      "(1.03 bar), so the rules generally do not cover lower pressures. Tests "
      "are at 3% or 10% overpressure, minimum 3 psi (0.207 bar), as the "
      "applicable code section requires.")
    U([("Phương pháp ba van: chứng nhận lưu lượng cho một kiểu, một cỡ, một "
        "áp cài đặt.",
        "Three-valve method: capacity certification of one model in one size "
        "at one set pressure."),
       ("Phương pháp bốn van hoặc độ dốc: chứng nhận lưu lượng cho một kiểu, "
        "một cỡ, nhiều áp suất.",
        "Four-valve or slope method: capacity of one valve type in one size "
        "at various pressures."),
       ("Phương pháp hệ số: chứng nhận hệ số xả cho một kiểu ở nhiều cỡ và "
        "dải áp.",
        "Coefficient method: discharge coefficient of a type in various "
        "sizes over a pressure range.")])
    P("Mọi giá trị thử phải nằm trong ±5% giá trị trung bình. Giá trị trung "
      "bình nhân 0,90 cho kết quả chứng nhận; với hệ số xả, giá trị thực "
      "trung bình là Kd và giá trị chứng nhận là K. Hệ số giảm 0,90 bù cho "
      "tổn thất áp đầu vào nhỏ, độ lệch âm tới 5%, hao mòn và các yếu tố "
      "không lường trước. Lưu lượng và hệ số được National Board công bố "
      "trong sổ đỏ Pressure Relief Device Certifications. Blowdown của van "
      "không chỉnh được phải được ghi nhận. Trong mọi thử nghiệm van không "
      "được rung (flutter/chatter) và phải đóng lại đúng sau khi áp vượt "
      "giảm. Việc xác định áp ngược cho phép và ảnh hưởng của nó đến lưu "
      "lượng không nằm trong thử nghiệm hiệu năng.",
      "All test values must fall within ±5% of the average; multiply by 0.90 "
      "for the certified value. For discharge coefficient the average actual "
      "value is Kd, the certified value K. The 0.90 derating covers minimal "
      "inlet losses, negative deviations up to 5%, wear and unforeseen "
      "factors. Capacities and coefficients are published by the National "
      "Board in the red book Pressure Relief Device Certifications. Blowdown "
      "of non-adjustable valves is recorded. During tests the valve must not "
      "flutter or chatter and must reseat properly. Determining permissible "
      "back pressure and its effect on flow is outside the performance test.")

    # -------------------------------------------------------- force/lift charts
    H("Đồ thị lực/nâng", "Force/lift diagrams")
    P("Đồ thị lực/nâng như Hình 5-29 đến 5-33 là công cụ quan trọng dự báo "
      "hành vi vận hành của van tải lò xo. Đường đứt thẳng là lực đóng của lò "
      "xo; đường cong chữ S là lực mở ròng của chất lỏng, xác định thực "
      "nghiệm ở áp vào không đổi. Dạng đường thay đổi theo thiết kế van.",
      "Force/lift diagrams such as Figures 5-29 to 5-33 predict the behaviour "
      "of spring-loaded valves. The straight dashed line is spring closing "
      "force; S-shaped curves are net fluid opening forces determined "
      "experimentally at constant inlet pressure. Curve shape varies by valve "
      "design.")
    FIG(29, F10.fig_vsh_5_29())
    P("Hình 5-29 cho thấy tổn thất áp đường vào ngày càng lớn làm lực nâng "
      "suy giảm thế nào ở áp ngược bằng không; ở đây độ nâng bị giới hạn "
      "l/d₀ = 0,22. Dựa trên đồ thị, nhà chế tạo đã chọn đặc tính lò xo để van "
      "mở hoàn toàn trong một nhịp khi tổn thất đầu vào là 3%. Hình 5-30 cho "
      "thấy áp suất ngược tích tụ cũng làm suy giảm lực nâng của van thông "
      "thường không cân bằng ở tổn thất đầu vào bằng không; để xét đồng thời "
      "3% tổn thất và áp ngược, phải chồng hai đường cong lại. Nếu áp ngược "
      "đủ lớn, van mất khả năng mở hoàn toàn trong một nhịp.",
      "Figure 5-29 shows rising inlet line loss decaying lift force at zero "
      "back pressure with lift restricted to l/d₀ = 0.22; the maker chose a "
      "spring characteristic giving full one-stroke opening at 3% inlet loss. "
      "Figure 5-30 shows built-up back pressure decaying lift force for an "
      "unbalanced conventional valve at zero inlet loss; to include 3% inlet "
      "loss the curves must be superimposed. Sufficient back pressure removes "
      "the ability to open fully in one stroke.")
    FIG(30, F10.fig_vsh_5_30())
    P("Hình 5-31 so sánh hai cách chỉnh blowdown. Ở (a), vặn vòng dẫn xuống "
      "kéo dài bạc dẫn, tăng góc đổi hướng dòng, nên lực nâng tăng gần tỉ lệ "
      "với độ nâng và blowdown dài ra nhưng áp mở bật giảm đôi chút. Ở (b), "
      "nâng vòng trên béc về phía đĩa thu hẹp lỗ phụ, làm đĩa lơ lửng lâu hơn "
      "khi áp vượt giảm: blowdown dài hơn nhưng áp mở bật tăng. Vòng béc ở "
      "(a) do nhà chế tạo cài, người dùng không nên chỉnh.",
      "Figure 5-31 compares blowdown devices. In (a), screwing the guide ring "
      "down lengthens the sleeve, raising flow deflection so lift force grows "
      "nearly with lift and blowdown lengthens while popping pressure falls "
      "slightly. In (b), raising the nozzle ring toward the disc narrows the "
      "secondary orifice, making the disc hover longer as overpressure "
      "recedes: longer blowdown but higher popping pressure. The nozzle ring "
      "in (a) is factory set.")
    FIG(31, F10.fig_vsh_5_31())
    P("Hình 5-32 mô tả van mở bật hoàn toàn trong một nhịp (điển hình). Khi "
      "áp hệ thống tới áp cài đặt ở điểm A, van mở điều tiết tới điểm B là "
      "nơi lực nâng và lực đóng cân bằng; thêm áp nhỏ làm lực nâng tăng nhanh "
      "hơn lò xo, van bật mở hoàn toàn tới C, rồi đạt lưu lượng định mức ở D "
      "khi áp tiếp tục tăng. Khi áp giảm, van giữ độ nâng đầy tới S rồi mở "
      "điều tiết đóng về E. Tại E, chênh giữa áp cài đặt và áp đầu van là "
      "tổng tổn thất đường vào và blowdown khi đóng lại; nếu giá trị đó nhỏ "
      "hơn tổn thất đường vào, van không đóng kín được mà mở-đóng liên tục, "
      "tương tác âm thanh với đường ống làm rung dữ dội cho đến khi áp giảm "
      "đủ hoặc van tự phá hủy. Hình bên dưới trong nguyên bản còn cho thấy "
      "đồ thị nâng/áp suất tương ứng.",
      "Figure 5-32 describes a valve that pops fully in one stroke (typical). "
      "At set pressure (A) it modulates open until B, where lifting and "
      "closing forces balance; a further rise makes lift force grow faster "
      "and the valve pops fully to C, reaching rated capacity at D. On "
      "falling pressure it holds full lift to S, then modulates closed to E. "
      "At E, set minus inlet pressure equals inlet-line loss plus reseating "
      "blowdown; if this is less than inlet loss the valve cannot close and "
      "reopens repeatedly, with acoustic interaction aggravating chatter "
      "until pressure drops or the valve destroys itself. The original also "
      "shows the corresponding lift/pressure diagram.")
    FIG(32, F10.fig_vsh_5_32())
    P("Hình 5-33 mô tả van chỉ bật mở một phần rồi tiếp tục mở điều tiết "
      "đến độ nâng đầy, dạng phổ biến với nhiều van tải lò xo; dựa trên quan "
      "hệ nâng/áp suất trong API RP 520 Part I (1993). Hiệu số lực nâng tại D "
      "và lực đóng tại S cho thấy khả năng chịu áp ngược của van. Với cùng "
      "điều kiện, van theo Hình 5-32 chịu áp ngược tốt hơn van theo Hình "
      "5-33. Có thể cải thiện bằng giảm độ dốc đặc tính lò xo hoặc chọn béc "
      "lớn hơn rồi hạn chế độ nâng theo lưu lượng cần; đường ống vào và ra "
      "lớn hơn cũng giảm tổn thất và áp ngược tích tụ.",
      "Figure 5-33 shows valves that pop only partly then modulate to full "
      "lift, a common characteristic based on API RP 520 Part I (1993) Figure "
      "22. The difference between lift force at D and closing force at S "
      "measures back-pressure tolerance; under identical conditions the "
      "Figure 5-32 valve tolerates more back pressure. Tolerance can be "
      "improved by a less steep spring characteristic or a larger orifice "
      "with restricted lift; larger inlet and discharge piping also lower "
      "inlet loss and built-up back pressure.")
    FIG(33, F10.fig_vsh_5_33())

    # ------------------------------------------------- secondary back pressure
    H("Áp suất ngược thứ phát và tổn thất đường vào",
      "Secondary back pressure and inlet loss")
    P("Áp suất ngược thứ phát phát sinh giữa chỗ kín và mặt bích ra; với dòng "
      "đạt vận tốc âm thanh ở nhánh ra, đó là đặc tính nội tại của van. Áp này làm lực "
      "nâng suy giảm như áp ngược trong ống, và nếu đủ lớn van không đạt "
      "lưu lượng định mức. Độ lớn liên quan đến tỉ lệ diện tích giữa cỡ đầu "
      "ra và béc theo API Std 526; tỉ lệ của van 1½D2 lớn gấp khoảng 14 lần "
      "van 8T10. Một van 8T10 dùng hơi được báo cáo không đạt lưu lượng định "
      "mức khi cài đặt trên 50 psig (3,5 barg) dù không có ống xả; ở mức đó "
      "cần cỡ 8T12. Cần thận trọng với van có tỉ lệ diện tích thấp và hỏi "
      "nhà chế tạo khi nghi ngờ.",
      "Secondary back pressure develops between seat and outlet flange and, "
      "for sonic outlet flow, is intrinsic to the valve. It decays lift force "
      "like outlet-pipe back pressure and may prevent rated capacity. It "
      "relates to the outlet-to-nozzle area ratio of API Std 526: the ratio "
      "for a 1½D2 valve is about 14 times that of an 8T10. An 8T10 steam valve "
      "has been reported not to reach capacity above 50 psig (3.5 barg) even "
      "without outlet piping; an 8T12 should be used. Use caution with low "
      "area ratios and consult the maker in doubt.")
    P("Khuyến nghị được chấp nhận rộng rãi: tổn thất áp không hồi phục giữa "
      "thiết bị được bảo vệ và đầu vào van không vượt quá 3% áp cài đặt. Nếu "
      "van lắp trên đường công nghệ, giới hạn 3% áp dụng cho tổn thất trong "
      "đoạn đầu vào vốn không chảy bình thường cộng với tổn thất tăng thêm "
      "trong đường công nghệ do dòng qua van. Tính toán dùng lưu lượng định "
      "mức ở áp vượt 10%. Duy trì dưới 3% khó dần khi tỉ lệ diện tích đầu vào/"
      "béc giảm; với van xả chất lỏng mở toàn phần có AE/AN = 0,9, hệ số "
      "trở kháng cho phép chỉ khoảng 0,5 — bằng hệ số của đầu ống sắc cạnh. "
      "Khi đó cần ống vào lớn hơn hoặc van có bộ giảm dao động, sau khi hỏi "
      "nhà chế tạo.",
      "The accepted recommendation is that non-recoverable pressure loss "
      "between protected equipment and a direct-acting relief valve inlet "
      "should not exceed 3% of set pressure. On a process line the limit "
      "includes loss in the normally non-flowing inlet and the incremental "
      "process-line loss caused by relief flow, calculated at the 10% "
      "overpressure rating. Staying below 3% grows harder as inlet-to-nozzle "
      "area ratio falls; for a full-lift liquid valve with AE/AN = 0.9 the "
      "permitted resistance coefficient is only about 0.5, equal to a "
      "sharp-edged inlet. Use a larger inlet pipe or a valve with an "
      "oscillation damper after consulting the maker.")
    P("Van mở bật bị quá cỡ nghiêm trọng cũng mất ổn định: nếu lưu lượng nhỏ "
      "hơn khoảng 25% lưu lượng van, chất thoát không đủ giữ van ở vị trí mở "
      "nên van đóng mở liên tiếp. Tần số phụ thuộc thể tích hệ thống và cài "
      "đặt blowdown; hạn chế độ nâng sau khi hỏi nhà chế tạo sẽ khắc phục hoàn "
      "toàn.",
      "A grossly oversized pop valve is also unstable: if flow is below about "
      "25% of valve capacity the discharge cannot hold it open and it cycles. "
      "Frequency depends on system volume and blowdown setting; limiting lift "
      "in consultation with the maker eliminates the instability.")

    # -------------------------------------------------------------- verification
    H("Kiểm tra dữ liệu vận hành trước và sau lắp đặt",
      "Verification before and after installation")
    P("Trước khi lắp, kiểm tra thường chỉ là thử áp cài đặt trên bàn theo "
      "hướng dẫn của nhà chế tạo; trong điều kiện bàn thử, áp cài đặt dễ xác "
      "định bằng dòng chảy hoặc độ nâng ổn định đầu tiên. Chỉ thử tại chỗ mới "
      "phản ánh ảnh hưởng riêng của nhà máy. Nhưng tiếng ồn nhà máy cản trở "
      "phát hiện âm thanh, nên áp mở bật thường được lấy làm áp cài đặt. Cách "
      "này ít ảnh hưởng với van áp cao (chênh mở thường chỉ 1–2% áp cài đặt), "
      "nhưng van áp thấp có thể có áp mở bật cao hơn áp cài đặt thực tới 5%. "
      "Phải tính đến sai số này khi đối chiếu với áp làm việc, áp đóng lại và "
      "blowdown; nếu cần đánh giá cả hành vi, phải nâng áp vận hành thêm "
      "khoảng 5% hoặc 10%.",
      "Before installation, verification is commonly only a bench set-pressure "
      "test; on the bench the set point is readily seen as first steady flow "
      "or lift. Only in-situ testing captures plant-specific effects. Plant "
      "noise interferes with audible detection, so popping pressure is often "
      "taken as set pressure. This matters little for high-pressure valves "
      "(opening difference often 1–2%), but low-pressure valves may pop up to "
      "5% above true set pressure. This deviation must be allowed for when "
      "correlating operating, reseating and blowdown pressures; assessing "
      "behaviour may require raising plant pressure by another 5–10%.")
    P("Để khỏi phải quá áp hệ thống, người ta chế tạo thiết bị di động như "
      "Hình 5-34 cho phép thử tại chỗ ban đầu và định kỳ mà không làm gián "
      "đoạn vận hành. Thiết bị mô phỏng áp vượt bằng cách tạo lực nâng đo "
      "được trên cần van, có thể bằng cơ khí, thủy lực hoặc khí nén như hình "
      "vẽ, không cần điều khiển áp hệ thống. Thời gian thử chỉ tính bằng "
      "giây. Các giá trị kiểm tra gồm áp cài đặt, áp mở bật, blowdown khi đã "
      "đóng lại, độ nâng và độ dốc lò xo. Máy tính xách tay kèm phần mềm và "
      "máy in cho ra đồ thị áp suất/nâng để đánh giá đầy đủ hiệu năng. Áp cài "
      "đặt thử được ở mọi áp hệ thống và trên bàn thử; các dữ liệu còn lại "
      "chỉ đánh giá tin cậy khi áp làm việc không dưới 80% áp cài đặt.",
      "Portable devices such as Figure 5-34 avoid overpressurising the plant "
      "by applying a measurable lifting force to the stem mechanically, "
      "hydraulically or pneumatically, without controlling system pressure. "
      "Tests last seconds and verify set pressure, popping pressure, blowdown "
      "after reseating, valve lift and spring rate. A laptop with software and "
      "printer delivers a pressure/lift diagram for full performance "
      "evaluation. Set pressure can be verified at any system pressure and on "
      "the bench; the other data require at least 80% of set pressure.")
    FIG(34, F10.fig_vsh_5_34())

    # -------------------------------------------------------------- table
    H("Bảng tóm tắt các thiết kế trong đơn vị", "Designs in this unit")
    b.append(table(
        ["Hình / chủ đề", "Thiết kế", "Đặc điểm chính"]
        if vi else ["Figure / topic", "Design", "Key feature"],
        [
            ["5-1", "Ritchie, buồng tụ áp" if vi else "Ritchie huddling chamber",
             "Lỗ phụ, đổi hướng ~90°" if vi else "Secondary orifice, ~90° turn"],
            ["5-2", "Naylor, môi đổi hướng" if vi else "Naylor lip",
             "Đổi hướng 180°, lực nâng cực đại"
             if vi else "180° turn, maximum lift"],
            ["5-3…5-6", "Van an toàn hơi" if vi else "Steam safety valves",
             "Nắp hở, vòng làm mát, eductor"
             if vi else "Open bonnet, cooling spool, eductor"],
            ["5-5", "Không có vòng béc" if vi else "No nozzle ring",
             "Lỗ phụ cố định" if vi else "Fixed secondary orifice"],
            ["5-7…5-9",
             "Van an toàn xả thông thường" if vi else "Conventional safety relief valves",
             "Nắp thông ra, áp ngược cộng thêm"
             if vi else "Vented bonnet, additive back pressure"],
            ["5-8", "Vít chỉnh blowdown ngoài" if vi else "External blowdown screw",
             "Ghế mềm cho LPG, amonia" if vi else "Soft seats for LPG, ammonia"],
            ["5-10…5-12", "Cân bằng ống màng" if vi else "Bellows-balanced",
             "Áp ngược 20–40%, tới 50%"
             if vi else "Back pressure 20–40%, up to 50%"],
            ["5-13", "Van xả chất lỏng" if vi else "Liquid relief valve",
             "Mở hẳn ở 10% áp vượt" if vi else "Full lift at 10% overpressure"],
            ["5-14", "Vòng ma sát chống rung" if vi else "Friction ring",
             "Hai O-ring trên cần" if vi else "Two stem O-rings"],
            ["5-15…5-16", "Van tỉ lệ" if vi else "Proportional relief valve",
             "Đặc tính mở tuyến tính" if vi else "Linear opening characteristic"],
            ["5-17…5-19", "Van xả chân không" if vi else "Vacuum relief valves",
             "Tải trọng lượng, ghép áp dương, van thông hơi"
             if vi else "Weight-loaded, combined pressure/vacuum, breather"],
            ["5-20…5-24", "Cơ cấu phụ trợ" if vi else "Auxiliary actuators",
             "Hỗ trợ chống rung, tải bổ sung, hỗ trợ nâng"
             if vi else "Anti-chatter assist, supplementary load, lift assist"],
            ["5-25…5-26",
             "Lò xo Belleville + khí nén" if vi else "Belleville springs + pneumatic",
             "Áp cao, lưu lượng lớn" if vi else "High pressure and capacity"],
            ["5-27", "Giảm dao động ma sát khô" if vi else "Dry-friction damper",
             "Than chì điện cứng" if vi else "Hard electrographite"],
            ["5-28", "Giảm dao động nhớt" if vi else "Viscous damper",
             "Trục đồng tâm, mỡ nhớt"
             if vi else "Concentric cylinders, grease"],
            ["5-29…5-33", "Đồ thị lực/nâng" if vi else "Force/lift diagrams",
             "Tổn thất vào, áp ngược, blowdown, các điểm A–E/S"
             if vi else "Inlet loss, back pressure, blowdown, points A–E/S"],
            ["5-34", "Thiết bị kiểm tra tại chỗ" if vi else "In-situ verifier",
             "Áp cài đặt, mở bật, blowdown, nâng, độ dốc lò xo"
             if vi else "Set pressure, pop, blowdown, lift, spring rate"],
        ],
        caption=("Tóm tắt theo văn bản nguồn, book pp. 176–212, "
                 "Hình 5-1…5-34." if vi else
                 "Summary from source text, book pp. 176–212, "
                 "Figures 5-1…5-34."),
        cls="tbl wide"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
