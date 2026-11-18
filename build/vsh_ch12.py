# -*- coding: utf-8 -*-
"""Book 6, Unit 12 — Check Valves (EN/VI).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 153–168 (PDF pp. 167–182): function and grouping of check valves,
operation and fast-closing assessment, lift / swing / tilting-disc /
diaphragm designs, dashpots, and selection for incompressible and
compressible fluids (Figures 4-1…4-15).
"""

from vsh_common import fig, h2, h3, p, table, ul
import vshfig9 as F9

PAGES_SRC = 16          # source book pp. 153-168
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Check Valves"
TITLE_VI = "Van một chiều"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 12.</b> check valve — van một chiều · "
                "flow reversal — dòng chảy ngược · lift check — van một chiều "
                "kiểu nâng · swing check — van một chiều kiểu đĩa quay bản lề "
                "· tilting-disc — đĩa nghiêng · diaphragm check — van một "
                "chiều màng · dashpot — bộ giảm chấn · surge pressure — áp "
                "suất dội · closure member — cơ cấu đóng · ring-shaped seat "
                "orifice — lỗ chỗ kín dạng vòng · flutter — rung đĩa · "
                "stalling position — vị trí kẹt đĩa · tide gate — cửa triều "
                "· multi-disc — nhiều đĩa · positive displacement — thể tích "
                "dương.")
    return ("<b>Key terms.</b> check valve · flow reversal · lift check · "
            "swing check · tilting-disc · diaphragm check · dashpot · surge "
            "pressure · closure member · ring-shaped seat orifice · flutter "
            "· stalling position · tide gate · multi-disc · positive "
            "displacement.")


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

    # ============================================================== function
    H("Chức năng của van một chiều", "Function of check valves")
    P("Chức năng chính của van một chiều là bảo vệ thiết bị cơ khí trong hệ "
      "thống đường ống bằng cách ngăn chất lỏng chảy ngược. Điều này đặc "
      "biệt quan trọng với bơm và máy nén: dòng ngược có thể làm hỏng chi "
      "tiết bên trong, gây dừng hệ thống không cần thiết và trong trường hợp "
      "nặng có thể dừng toàn nhà máy.",
      "The prime function of a check valve is to protect mechanical equipment "
      "in a piping system by preventing reversal of flow. This is especially "
      "important for pumps and compressors, where backflow can damage "
      "internals, cause an unnecessary system shutdown, and in severe cases "
      "shutdown of the whole plant.")
    P("Nhìn chung van một chiều không cần người vận hành: van tự làm việc "
      "khi dòng đảo chiều, dù trong trường hợp rất đặc biệt phải bỏ qua tính "
      "năng một chiều đó. Có thể lắp cơ cấu khóa các đĩa đóng ở vị trí mở, "
      "hoặc tháo các đĩa đó — cách sau phải tháo van, lấy đĩa ra rồi lắp lại.",
      "Check valves generally need no operator: the valve is operated "
      "automatically by flow reversal, although in very special circumstances "
      "this one-way facility has to be overridden. A device may lock the "
      "closure plate(s) open, or the plates may be removed; the latter "
      "requires dismantling the valve, removing the plates and reinstalling "
      "it. Check valves are automatic valves that open with forward flow and "
      "close against reverse flow.")
    P("Cần van một chiều để ngăn dòng trở lại, giữ mồi sau khi bơm dừng, cho "
      "bơm và máy nén kiểu piston hoạt động, và ngăn bơm hoặc máy nén kiểu "
      "quay làm quay ngược máy dự phòng. Van cũng có thể cần trên đường ống "
      "cấp hệ thống phụ, nơi áp suất có thể vượt hệ thống chính.",
      "Check valves are needed to prevent return flow, maintain prime after "
      "the pump stops, enable reciprocating pumps and compressors to "
      "function, and prevent rotary pumps and compressors from driving "
      "standby units in reverse. They may also be needed in lines feeding a "
      "secondary system where pressure can rise above that of the primary "
      "system.")

    H("Phân loại van một chiều", "Grouping of check valves")
    P("Van một chiều được chia thành bốn nhóm theo cách cơ cấu đóng đi vào "
      "chỗ kín:",
      "Check valves are grouped according to the way the closure member moves "
      "onto the seat:")
    U([("Van một chiều kiểu nâng: cơ cấu đóng đi theo phương vuông góc với "
        "mặt chỗ kín (Hình 4-1 đến 4-7).",
        "Lift check valves: the closure member travels normal to the plane of "
        "the seat (Figures 4-1 to 4-7)."),
       ("Van kiểu đĩa quay bản lề: cơ cấu đóng xoay quanh bản lề đặt ngoài "
        "chỗ kín (Hình 4-8 đến 4-10).",
        "Swing check valves: the closure member swings about a hinge mounted "
        "outside the seat (Figures 4-8 to 4-10)."),
       ("Van đĩa nghiêng: cơ cấu đóng xoay quanh trục gần nhưng nằm trên tâm "
        "chỗ kín (Hình 4-11).",
        "Tilting-disc check valves: the closure member tilts about a hinge "
        "near but above the centre of the seat (Figure 4-11)."),
       ("Van một chiều màng: cơ cấu đóng là màng uốn ra khỏi hoặc ép vào chỗ "
        "kín (Hình 4-12 đến 4-14).",
        "Diaphragm check valves: the closure member is a diaphragm that "
        "deflects from or against the seat (Figures 4-12 to 4-14).")])

    # ============================================================= operation
    H("Vận hành van một chiều", "Operation of check valves")
    P("Van một chiều phải vận hành sao cho tránh được áp suất dội quá cao "
      "khi đóng và chuyển động dao động nhanh của cơ cấu đóng. Để tránh áp "
      "suất dội, van phải đóng đủ nhanh để không hình thành vận tốc dòng "
      "ngược đáng kể trước khi đóng hẳn — chính vận tốc này gây dội khi "
      "chảy ngược bị chặn đột ngột.",
      "Check valves operate in a way that avoids excessively high surge "
      "pressure on closing and rapid fluctuating movements of the closure "
      "member. To avoid surge, the valve must close fast enough to prevent a "
      "significant reverse-flow velocity from developing before sudden "
      "shut-off; that velocity is the source of the surge pressure.")
    P("Tốc độ giảm của dòng xuôi khác nhau rất nhiều giữa các hệ thống. Nếu "
      "nhiều bơm chạy song song và một bơm hỏng đột ngột, van ở đầu ra của "
      "bơm đó phải đóng gần như tức thì. Ngược lại, nếu chỉ có một bơm dừng "
      "đột ngột, đường ống dài và áp suất ngược cùng độ cao bơm thấp, van "
      "đóng chậm là đủ.",
      "The rate at which forward flow retards varies widely. If several pumps "
      "run in parallel and one fails suddenly, its outlet check valve must "
      "close almost instantaneously. If a single pump fails and the delivery "
      "line is long with low outlet back pressure and pumping elevation, a "
      "slow-closing valve is satisfactory.")
    P("Chuyển động dao động nhanh làm mòn chi tiết chuyển động và có thể hỏng "
      "van sớm. Có thể tránh bằng cách chọn cỡ van theo vận tốc dòng ép chắc "
      "cơ cấu đóng vào điểm dừng. Nếu dòng nhấp nhô, nên lắp van xa nguồn "
      "tạo xung nhất có thể; nhiễu loạn dòng mạnh cũng gây dao động, nên đặt "
      "van ở nơi nhiễu loạn nhỏ nhất. Bước đầu tiên khi chọn van một chiều "
      "là nhận rõ điều kiện vận hành của nó.",
      "Rapid fluctuating movement causes excessive wear and early failure. "
      "Size the valve for a flow velocity that holds the closure member "
      "firmly against a stop; mount pulsating-flow valves as far as practical "
      "from the pulsation source and locate them where flow disturbance is "
      "minimal. The first step in selection is to recognise the operating "
      "conditions.")

    H("Đánh giá khả năng đóng nhanh", "Assessment for fast closing")
    P("Trong hầu hết trường hợp thực tế chỉ đánh giá định tính được tốc độ "
      "đóng. Ba tiêu chí sau làm kim chỉ nam:",
      "In most practical applications fast closing can be assessed only "
      "qualitatively. Three criteria serve as a guide:")
    U([("Hành trình từ mở hoàn toàn đến đóng càng ngắn càng tốt; vì vậy van "
        "nhỏ có thể đóng nhanh hơn van lớn cùng kiểu thiết kế.",
        "Travel from fully open to closed should be as short as possible; a "
        "smaller valve is potentially faster than a larger one of the same "
        "design."),
       ("Quán tính của cơ cấu đóng càng thấp càng tốt, nhưng lực đóng phải "
        "đủ lớn để đáp ứng ngay khi dòng xuôi suy giảm. Cấu trúc nhẹ có thể "
        "cần lò xo bổ sung lực đóng từ trọng lượng.",
        "Inertia should be as low as possible while closing force is high "
        "enough to respond to declining forward flow; light construction may "
        "need a spring to augment the weight closing force."),
       ("Tránh mọi cản trở quanh cơ cấu đóng làm chậm chuyển động đóng tự do.",
        "Avoid restrictions around the moving closure member that retard "
        "free closing movement.")])
    P("Việc dùng toán học cho van một chiều là tương đối mới. Pool, Porwit và "
      "Carlton mô tả cách tính cho van có đĩa bản lề bằng phương trình "
      "chuyển động của đĩa kết hợp đặc tính giảm tốc của chất lỏng trong "
      "hệ thống; cần biết một số hằng số vật lý của van. Phép tính xác định "
      "vận tốc dòng ngược tại thời điểm đóng hẳn, từ đó tính áp suất dội như "
      "đã trình bày ở Chương 2. Nhà chế tạo có thể dùng toán học để thiết kế "
      "van cho ứng dụng tới hạn và dự báo áp suất dội.",
      "Mathematics in check valve operation is of recent origin. Pool, "
      "Porwit and Carlton describe a calculation for hinged-disc valves that "
      "sets up the disc equation of motion with the fluid deceleration "
      "characteristic of the system; certain physical constants of the valve "
      "must be known. It determines reverse-flow velocity at sudden "
      "shut-off, from which surge pressure is calculated as in Chapter 2. "
      "Manufacturers can use mathematics to design valves for critical "
      "applications and predict surge pressure.")

    # ============================================================ design
    H("Thiết kế van một chiều", "Design of check valves")
    H("Van một chiều kiểu nâng", "Lift check valves", h3)
    P("Các van Hình 4-1 đến 4-7 là một lát cắt của họ van một chiều kiểu "
      "nâng. Chúng chỉ cần hành trình nâng ngắn để mở hoàn toàn; ngắn nhất "
      "khi lối dòng tại chỗ kín có dạng vòng như Hình 4-4 và 4-6, nên kiểu "
      "nâng có khả năng đóng nhanh.",
      "Figures 4-1 to 4-7 represent a cross section of the lift check family. "
      "They need only a short lift for full opening, minimal where the seat "
      "passage is ring-shaped as in Figures 4-4 and 4-6, so lift checks are "
      "potentially fast closing.")
    FIG(1, F9.fig_vsh_4_1())
    P("Đa số van kiểu nâng dẫn hướng cơ cấu đóng để hai mặt kín khít khi "
      "đóng. Tuy nhiên bụi bẩn lọt vào bộ dẫn hướng có thể làm kẹt cơ cấu, "
      "và chất lỏng nhớt gây đóng chậm hoặc kẹt hẳn. Vì vậy các kiểu này chỉ "
      "phù hợp chất lỏng độ nhớt thấp và về cơ bản không có rắn. Một số "
      "thiết kế khắc phục như Hình 4-5: cơ cấu dạng bi không được dẫn hướng "
      "sát và lăn vào chỗ kín khi đóng để tự chỉnh.",
      "Most lift checks guide the closure member so the seatings mate. Dirt "
      "in the guide can hang up the member, and viscous liquids cause lazy "
      "operation or hanging, so these types suit only low-viscosity fluids "
      "essentially free of solids. Figure 4-5 overcomes this with a ball that "
      "travels without close guidance and rolls into the seat for alignment.")
    FIG(2, F9.fig_vsh_4_2())
    FIG(3, F9.fig_vsh_4_3())
    FIG(4, F9.fig_vsh_4_4())
    FIG(5, F9.fig_vsh_4_5())
    P("Van Hình 4-2 được thiết kế riêng cho nơi áp suất dội thấp là yêu cầu "
      "quan trọng: một phần đuôi hình nón tiết lưu dần dòng khi van đóng, "
      "phần khác là bộ giảm chấn chỉ tác dụng trong những khoảnh khắc cuối "
      "của hành trình đóng. Lò xo hỗ trợ đóng được cố ý bỏ vì gãy lò xo được "
      "coi là nguy hiểm cho dịch vụ dự kiến.",
      "Figure 4-2 is designed where low surge pressure is critical. A conical "
      "extension progressively throttles flow as the valve closes, and a "
      "dashpot acts in the final closing moments. A closing spring is "
      "deliberately omitted because spring breakage was considered a hazard "
      "for the intended service.")
    FIG(6, F9.fig_vsh_4_6())
    P("Van Hình 4-6 chỉ dùng cho khí. Tùy điều kiện dòng, nó làm việc như van "
      "lưu lượng không đổi — luôn mở hoàn toàn dù dòng dao động nhẹ — hoặc "
      "như van dòng xung, mở và đóng theo từng xung khí. Loại lưu lượng "
      "không đổi dùng sau máy nén ly tâm, kiểu bánh răng cưa hoặc vít, và "
      "sau máy nén piston khi xung đủ nhỏ không gây rung đĩa. Loại dòng xung "
      "dùng sau máy nén piston khi xung làm van đóng mở theo từng nhịp; van "
      "được thiết kế theo nguyên lý van máy nén nên chịu được va đập lặp "
      "giữa các mặt kín. Nhà chế tạo sẽ tư vấn loại phù hợp. Đặc tính của "
      "van đến từ hành trình nâng tối thiểu kết hợp nhiều lỗ chỗ kín dạng "
      "vòng, quán tính thấp của đĩa mỏng, dẫn hướng không ma sát và lò xo "
      "chọn đúng chế độ.",
      "Figure 4-6 is for gas service only. Depending on flow it acts as a "
      "constant-flow valve, staying fully open despite minor fluctuations, "
      "or as a pulsating-flow valve opening and closing with each pulse. "
      "Constant-flow types follow centrifugal, lobe and screw compressors, "
      "or reciprocating compressors with low enough pulsation to avoid disc "
      "flutter. Pulsating-flow types follow reciprocating compressors whose "
      "pulses open and close the valve each cycle; built on compressor-valve "
      "principles, they withstand repeated seating impacts. The maker advises "
      "which type to use. Their behaviour comes from minimum lift with "
      "multiple ring-shaped seat orifices, low plate inertia, frictionless "
      "guidance and a spring matched to the duty.")
    FIG(7, F9.fig_vsh_4_7())
    P("Van Hình 4-7 là kết hợp một chiều kiểu nâng và van chặn, giống van "
      "cầu xiên nhưng cơ cấu đóng tách rời cần van. Nâng cần thì van làm việc "
      "như van một chiều; hạ cần ép chặt vào cơ cấu đóng thì van làm việc "
      "như van chặn.",
      "Figure 4-7 combines a lift check and a stop valve. It resembles an "
      "oblique globe valve with the closure member disconnected from the "
      "stem: raise the stem and it acts as a lift check; lower and press it "
      "firmly onto the closure member and it acts as a stop valve.")
    P("Van kiểu nâng phải lắp sao cho trọng lượng của cơ cấu đóng hướng theo "
      "chiều đóng; ngoại lệ là một số van nâng thấp có lò xo là lực đóng "
      "chủ đạo. Vì vậy Hình 4-1 và 4-5 chỉ lắp ngang; Hình 4-2 chỉ lắp "
      "thẳng đứng chiều lên; Hình 4-3, 4-4 và 4-7 lắp được ngang hoặc thẳng "
      "đứng chiều lên; riêng Hình 4-6 lắp được mọi vị trí, kể cả thẳng đứng "
      "chiều xuống.",
      "Lift checks must be mounted so the closure member's weight acts in "
      "the closing direction, except some spring-loaded low-lift types where "
      "the spring dominates. Figures 4-1 and 4-5 mount horizontally only; "
      "4-2 vertically upflow only; 4-3, 4-4 and 4-7 horizontally or vertically "
      "upflow; and 4-6 in any position, including vertical downflow.")

    H("Van một chiều kiểu đĩa quay bản lề", "Swing check valves", h3)
    P("Van kiểu đĩa quay thông thường có đĩa xoay quanh bản lề đặt ngoài chỗ "
      "kín như Hình 4-8 và 4-9. Hành trình từ mở hoàn toàn đến đóng dài hơn "
      "đa số van kiểu nâng, nhưng bụi bẩn và chất lỏng nhớt không dễ cản "
      "chuyển động quay của đĩa. Ở Hình 4-9, cơ cấu đóng là một phần của "
      "gioăng cao su giữa hai nửa thân, được gia cố thép, và mở/đóng bằng "
      "cách uốn một dải cao su nối đĩa với gioăng.",
      "Conventional swing checks have a disc-like closure member swinging "
      "about a hinge outside the seat, as in Figures 4-8 and 4-9. Disc travel "
      "is longer than in most lift checks, but dirt and viscous fluids do "
      "not easily hinder rotation. In Figure 4-9 the closure member is an "
      "integral part of the rubber body gasket, steel-reinforced, opening and "
      "closing by bending a rubber strip connecting it to the gasket.")
    FIG(8, F9.fig_vsh_4_8())
    FIG(9, F9.fig_vsh_4_9())
    P("Khi cỡ van kiểu đĩa quay tăng, trọng lượng và hành trình của đĩa cuối "
      "cùng trở nên quá lớn; van lớn hơn khoảng DN 600 (NPS 24) thường làm "
      "kiểu nhiều đĩa, với nhiều đĩa quay thông thường đặt trên một màng "
      "nhiều chỗ kín ngang qua đường dòng.",
      "As swing check size grows, disc weight and travel eventually become "
      "excessive. Above about DN 600 (NPS 24) they are often multi-disc "
      "designs, with several conventional discs on a multi-seat diaphragm "
      "across the flow passage.")
    P("Nên lắp van kiểu đĩa quay ở vị trí nằm ngang; lắp thẳng đứng cũng "
      "được nếu không để đĩa tới vị trí kẹt. Tuy nhiên khi mở hoàn toàn ở "
      "tư thế thẳng đứng, momen đóng do trọng lượng đĩa rất nhỏ nên van có "
      "xu hướng đóng muộn. Để khắc phục đáp ứng chậm với dòng suy giảm, có "
      "thể lắp đối trọng cần đòn hoặc dùng lò xo.",
      "Swing checks should be mounted horizontally; vertical mounting is "
      "possible if the disc is prevented from reaching the stalling position. "
      "Fully open in that position, the disc's weight closing moment is very "
      "small, so the valve tends to close late. A lever-mounted weight or "
      "spring loading overcomes the slow response.")
    FIG(10, F9.fig_vsh_4_10())
    P("Van Hình 4-10 là kiểu đĩa quay kép với hai đĩa chữ D nén lò xo lắp "
      "trên một gân ngang lòng van. Thiết kế này rút ngắn đường đi của trọng "
      "tâm đĩa và giảm khoảng 50% trọng lượng so với van một đĩa cùng cỡ; "
      "cộng với nén lò xo, van đáp ứng rất nhanh với dòng suy giảm.",
      "Figure 4-10 is a double-disc swing check with two spring-loaded "
      "D-shaped discs on a rib across the bore. It shortens the path travelled "
      "by the disc centre of gravity and cuts weight by about 50% against a "
      "single-disc valve of the same size; with spring loading, response to "
      "retarding flow is very fast.")

    H("Van một chiều đĩa nghiêng", "Tilting-disc check valves", h3)
    P("Van đĩa nghiêng như Hình 4-11 có đĩa quay quanh trục nằm giữa tâm và "
      "mép đĩa, lệch khỏi mặt chỗ kín. Khi đóng đĩa rơi vào chỗ kín, khi mở "
      "đĩa nhấc ra. Trọng tâm của hai nửa đĩa đi một đoạn ngắn giữa hai vị "
      "trí, nên van có khả năng đóng nhanh; riêng van này còn nén lò xo để "
      "đáp ứng nhanh với dòng xuôi suy giảm.",
      "A tilting-disc check such as Figure 4-11 has a disc rotating about a "
      "pivot between its centre and edge, offset from the seat plane. It drops "
      "into the seat on closing and lifts out on opening. The centre of "
      "gravity of the disc halves travels only a short path, so the valve is "
      "potentially fast closing; this one is also spring-loaded for quick "
      "response to retarding forward flow.")
    P("Có thể tham chiếu van Hình 3-77: tùy thiết kế cơ cấu dẫn động, nó làm "
      "van bướm, van một chiều đĩa nghiêng hoặc van kết hợp đĩa nghiêng một "
      "chiều và van chặn. Van đĩa nghiêng đắt hơn và khó sửa hơn van đĩa quay "
      "bản lề, nên thường chỉ dùng cho ứng dụng mà van kiểu đĩa quay không "
      "đáp ứng được.",
      "Figure 3-77 may serve as a butterfly valve, a tilting-disc check valve "
      "or a combined tilting-disc check and stop valve depending on the drive. "
      "Tilting discs cost more and are harder to repair than swing checks, so "
      "their use is normally restricted to duties swing checks cannot meet.")
    FIG(11, F9.fig_vsh_4_11())

    H("Van một chiều màng", "Diaphragm check valves", h3)
    P("Các van Hình 4-12 đến 4-15 ít phổ biến hơn nhưng đáng lưu ý. Hình "
      "4-12 gồm rổ hình nón đục lỗ đỡ một màng cùng hình dạng; cụm này kẹp "
      "giữa hai bích hoặc giữa hai đầu nối ống. Dòng chảy qua nón nâng màng "
      "khỏi chỗ kín; khi dòng xuôi dừng, màng hồi hình dạng cũ và đóng rất "
      "nhanh. Một ứng dụng đáng chú ý là đường khí thổi rửa dẫn vào đường "
      "chứa hỗn dịch hoặc chất dẻo: ở đây van màng làm việc rất tin cậy trong "
      "khi van khác nhanh bị kẹt.",
      "The diaphragm checks in Figures 4-12 to 4-15 are less well known but "
      "deserve attention. Figure 4-12 has a perforated cone-shaped basket "
      "supporting a matching diaphragm, clamped between flanges or pipe "
      "unions. Flow through the cone lifts the diaphragm off its seat; when "
      "forward flow stops the diaphragm regains its shape and closes fast. A "
      "notable use is purge-gas lines feeding slurry or gluey service, where "
      "diaphragm valves remain reliable while other valves hang up quickly.")
    FIG(12, F9.fig_vsh_4_12())
    P("Hình 4-13 dùng màng cao su dạng vòng xếp nếp. Khi đóng, một môi của "
      "màng tựa lên lõi trong đường dòng với các nếp ép lại; dòng xuôi mở "
      "các nếp và co môi ra khỏi chỗ kín. Vì màng biến dạng đàn hồi khi mở và "
      "đường đi của môi rất ngắn, van đóng cực nhanh và hợp với dòng thay đổi "
      "trong phạm vi rộng. Tuy nhiên áp suất chênh chỉ tới 10 bar (145 lb/in²) "
      "và nhiệt độ làm việc khoảng 74 °C (158 °F).",
      "Figure 4-13 uses a pleated annular rubber diaphragm. When closed, a "
      "lip rests with pleats closed against a core in the passage; forward "
      "flow opens the pleats and retracts the lip. Elastically strained in the "
      "open position with short lip travel, it closes extremely fast and "
      "suits widely varying flow. Its differential pressure is limited to "
      "10 bar (145 lb/in²) and operating temperature to about 74 °C (158 °F).")
    FIG(13, F9.fig_vsh_4_13())
    P("Cơ cấu đóng của Hình 4-14 là ống mềm ép dẹt ở một đầu. Đầu ép dẹt mở "
      "khi có dòng xuôi và đóng lại khi dòng ngược. Ống làm từ nhiều "
      "ê-lô-me, gia cố bên ngoài bằng các lớp vải nylon cấu trúc như lốp xe; "
      "mặt trong mềm có thể chôn vùi hạt rắn bị kẹt, nên van đặc biệt hợp "
      "dịch vụ có rắn lơ lửng hoặc hỗn dịch. Cỡ van từ DN 3 (NPS 1/8) tới "
      "DN 3000 (NPS 120) cho cửa triều.",
      "The closure member of Figure 4-14 is a flexible sleeve flattened at "
      "one end; that end opens on forward flow and recloses against reverse "
      "flow. The sleeve comes in many elastomers, externally reinforced with "
      "nylon plies like a car tyre. Its soft bore can embed trapped solids, "
      "making it especially suitable for suspended solids or slurry. Sizes "
      "range from DN 3 (NPS 1/8) to DN 3000 (NPS 120) for tidal gates.")
    FIG(14, F9.fig_vsh_4_14())
    P("Hình 4-15 là ứng dụng của chính van này làm cửa triều: khi mực nước "
      "ngoài cao hơn, đầu ống ép dẹt ngăn nước biển chảy ngược vào cống xả.",
      "Figure 4-15 applies the same valve as a tidal gate: when the outside "
      "tide is higher, the flattened sleeve prevents seawater flowing back "
      "into the outfall.")
    FIG(15, F9.fig_vsh_4_15())

    H("Bộ giảm chấn", "Dashpots", h3)
    P("Mục đích của bộ giảm chấn là giảm chuyển động của cơ cấu đóng. Ứng "
      "dụng quan trọng nhất là hệ thống có dòng đảo chiều rất nhanh: nếu van "
      "không đóng kịp để ngăn dòng ngược tích tụ đáng kể trước khi đóng hẳn, "
      "bộ giảm chấn tác dụng trong các cử động đóng cuối có thể giảm đáng kể "
      "áp suất dội.",
      "Dashpots damp movement of the closure member. Their most important "
      "use is where flow reverses very fast: if the valve cannot close fast "
      "enough to prevent substantial reverse-flow buildup before sudden "
      "closure, a dashpot acting in the final closing movements can "
      "considerably reduce surge pressure.")

    # ============================================================= selection
    H("Lựa chọn van một chiều", "Selection of check valves")
    P("Đa số van một chiều được chọn định tính bằng cách so sánh tốc độ đóng "
      "cần thiết với đặc tính đóng của van; cách này cho kết quả tốt trong "
      "đa số ứng dụng. Kích thước cũng là yếu tố quyết định. Nếu ứng dụng "
      "tới hạn, nên hỏi nhà chế tạo có uy tín.",
      "Most check valves are selected qualitatively by comparing required "
      "closing speed with the valve's closing characteristic; this works well "
      "in most applications. Sizing is also critical. For a critical "
      "application, consult a reputable manufacturer.")
    H("Chất lỏng không nén được", "Check valves for incompressible fluids", h3)
    P("Với chất lỏng không nén được, tiêu chí chính là đóng mà không gây áp "
      "suất dội không chấp nhận được khi dòng ngược bị chặn đột ngột; chọn "
      "van có áp suất giảm thấp thường chỉ là tiêu chí phụ. Bước một là đánh "
      "giá định tính tốc độ đóng cần thiết (xem Chương 2, trang 41); bước hai "
      "là chọn kiểu van có khả năng đáp ứng tốc độ đó như đã thảo luận ở "
      "phần vận hành.",
      "For incompressible fluids, valves are chosen primarily for closing "
      "without unacceptably high surge pressure when reverse flow is suddenly "
      "stopped; low pressure drop is normally secondary. First assess "
      "qualitatively the required closing speed (Chapter 2, page 41); then "
      "select the valve type likely to meet it, as discussed in the operation "
      "section.")
    H("Chất lỏng nén được", "Check valves for compressible fluids", h3)
    P("Có thể chọn van cho chất lỏng nén được theo cách tương tự. Tuy nhiên "
      "rung đĩa có thể là vấn đề với van kiểu nâng hành trình lớn trong dịch "
      "vụ khí, và có thể cần lắp bộ giảm chấn. Khi dòng khí dao động nhanh, "
      "van kiểu máy nén như Hình 4-6 là lựa chọn tốt.",
      "Compressible-fluid valves may be selected on a similar basis. Valve "
      "flutter can be a problem for high-lift checks in gas service, and a "
      "dashpot may be needed. Where gas flow fluctuates rapidly, compressor-"
      "type check valves such as Figure 4-6 are a good choice.")
    P("Phụ lục C liệt kê tiêu chuẩn Hoa Kỳ và Anh áp dụng cho van một chiều.",
      "Appendix C lists U.S. and British standards pertaining to check "
      "valves.")

    # -------------------------------------------------------------- table
    H("Bảng tóm tắt các thiết kế trong đơn vị", "Designs in this unit")
    b.append(table(
        ["Hình", "Thiết kế", "Nguyên lý đóng", "Đặc điểm chính"]
        if vi else
        ["Figure", "Design", "Closing principle", "Key feature"],
        [
            ["4-1", "Nâng, đĩa piston, kiểu tiêu chuẩn / Piston lift, standard",
             "Nâng thẳng đứng / Vertical lift", "Chỉ lắp ngang / Horizontal only"],
            ["4-2", "Nâng dạng góc, giảm chấn / Angle lift with dashpot",
             "Nón tiết lưu + dashpot / Cone + dashpot",
             "Áp dội thấp / Low surge"],
            ["4-3", "Nâng, kiểu xiên / Oblique piston lift",
             "Nâng thẳng đứng / Vertical lift",
             "Ngang hoặc thẳng lên / Horizontal or upflow"],
            ["4-4", "Nâng, đĩa vòng nén lò xo / Spring ring lift",
             "Lò xo + vòng / Spring + ring", "Lỗ vòng, đóng nhanh / Ring orifice"],
            ["4-5", "Nâng, đĩa bi / Ball lift",
             "Bi lăn vào chỗ kín / Ball rolls to seat",
             "Không dẫn hướng sát / No close guide"],
            ["4-6", "Nâng cho khí xung / Gas pulsating lift",
             "Nhiều lỗ vòng, lò xo / Ring orifices, spring",
             "Mọi vị trí, chống rung đĩa / Any position"],
            ["4-7", "Kết hợp nâng và chặn / Lift-check plus stop",
             "Cần tách rời đĩa / Detached stem",
             "Nâng: một chiều; hạ: chặn / Check or stop"],
            ["4-8", "Đĩa quay bản lề / Swing check",
             "Xoay quanh bản lề / Hinge swing", "Hành trình dài / Long travel"],
            ["4-9", "Đĩa quay gia cố, một khối với gioăng / Reinforced disc",
             "Uốn dải cao su / Bending rubber strip",
             "Ít bị bụi và chất nhớt / Tolerant of dirt"],
            ["4-10", "Đĩa quay kép chữ D / Double D-disc swing",
             "Hai đĩa nén lò xo / Two spring discs",
             "Nhẹ hơn 50%, đáp ứng nhanh / 50% lighter"],
            ["4-11", "Đĩa nghiêng / Tilting disc",
             "Trục lệch mặt chỗ kín / Offset pivot",
             "Đường trọng tâm ngắn / Short CG path"],
            ["4-12", "Màng nón trên rổ / Cone diaphragm",
             "Dòng nâng màng / Flow lifts diaphragm",
             "Tin cậy cho khí thổi rửa / Purge-gas reliability"],
            ["4-13", "Màng xếp nếp dạng vòng / Pleated annular diaphragm",
             "Mở nếp, co môi / Pleats open, lip retracts",
             "≤10 bar, ~74 °C"],
            ["4-14", "Ống cao su ép dẹt / Flattened sleeve",
             "Đầu dẹt mở theo dòng xuôi / Flattened end opens",
             "Chịu rắn, DN 3…DN 3000 / Handles solids"],
            ["4-15", "Cửa triều / Tide gate",
             "Ống dẹt ngăn dòng ngược / Sleeve blocks backflow",
             "Ngăn nước biển / Blocks seawater"],
        ],
        caption=("Tóm tắt theo văn bản nguồn, book pp. 153–168, "
                 "Hình 4-1…4-15." if vi else
                 "Summary from source text, book pp. 153–168, "
                 "Figures 4-1…4-15."),
        cls="tbl wide"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
