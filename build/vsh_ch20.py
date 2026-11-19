# -*- coding: utf-8 -*-
"""Book 6, Unit 20 — Mechanical Locking Devices for Valves (EN/VI).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 314–326 (PDF pp. 329–340): car sealed open/closed, locked open and
locked closed, mechanical interlocking, PRV change-out sequence, pig
launcher/receiver interlocking (Figures 10-1…10-8).
"""

from vsh_common import fig, h2, h3, ol, p, table, ul
import vshfig17 as F17

PAGES_SRC = 13         # source book pp. 314-326
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Mechanical Locking Devices for Valves"
TITLE_VI = "Thiết bị khóa cơ khí cho van"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 20.</b> car sealed open / closed "
                "(CSO/CSC) — niêm phong mở / đóng · locked open / closed "
                "(LO/LC) — khóa mở / khóa đóng · padlock — khóa padlock · "
                "key cabinet — tủ chìa khóa · mechanical interlock — khóa "
                "liên động cơ khí · key path — đường đi chìa · pressure "
                "safety valve (PSV) — van an toàn áp suất · switchover — "
                "chuyển đổi van dự phòng · pig — búp bê làm sạch ống · "
                "launcher / receiver — bệ phóng / bệ thu pig · special "
                "piping (SP) — bố trí đường ống đặc biệt.")
    return ("<b>Key terms.</b> car sealed open / closed (CSO/CSC) · locked "
            "open / closed (LO/LC) · padlock · key cabinet · mechanical "
            "interlock · key path · pressure safety valve (PSV) · "
            "switchover · pig · launcher / receiver · special piping (SP).")


def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def U(items):
        b.append(ul([(i[0] if vi else i[1]) for i in items]))

    def O(items):
        b.append(ol([(i[0] if vi else i[1]) for i in items]))

    def FIG(n, fn):
        b.append(fig(n, fn))

    # ============================================================= introduction
    H("Giới thiệu", "Introduction")
    P("Trong những năm gần đây, sự an toàn của hệ thống đường ống cần được "
      "quan tâm nhiều hơn do các thảm họa quy mô lớn và môi trường ngoài "
      "khơi khắc nghiệt hơn, nơi các cơ sở dầu khí hiện nay được xây dựng. "
      "Môi trường vận hành an toàn hơn được yêu cầu không chỉ để bảo vệ lợi "
      "nhuận, mà quan trọng hơn là bảo vệ nhân viên nhà máy, không có họ thì "
      "lợi nhuận ấy cũng không thể có.",
      "During recent years more attention has had to be given to the safety "
      "of piping systems because of large-scale disasters and the harsher "
      "offshore environments where oil and gas facilities are now "
      "constructed. Safer operating environments are required not only to "
      "protect profits, but more importantly to protect plant personnel, "
      "without whom the former would not be achievable.")
    P("Mọi van, kể cả van xả nhỏ nhất, đều có vai trò trong vận hành an toàn "
      "và hiệu quả của nhà máy quá trình. Ở dạng đơn giản nhất, một van có "
      "thể mở, đóng hoặc ở vị trí nào đó ở giữa để điều khiển dòng quá "
      "trình. Tất cả các van đều quan trọng, tuy nhiên có những van quan "
      "trọng hơn những van khác, đặc biệt ở các dòng quá trình chính và "
      "trong hệ thống đường ống giải áp.",
      "Every valve, even the very smallest drain valve, has a role to play "
      "in the safe and efficient operation of a process plant. Put in its "
      "simplest form a valve can be open, closed, or in a position somewhere "
      "in between to control the process flow. All valves are important, "
      "however, some valves are naturally more important than others, "
      "especially in main process flows and in piping relief systems.")

    # ============================================================= CSO / CSC
    H("Niêm phong mở và niêm phong đóng (CSO / CSC)",
      "Car sealed open and car sealed closed")
    P("Trong giai đoạn thiết kế nhà máy quá trình, kỹ sư quá trình sẽ xác "
      "định một số van tới hạn phải được niêm phong mở hoặc niêm phong đóng "
      "chắc chắn. Những van được chọn này được đánh dấu trên sơ đồ đường ống "
      "và thiết bị đo (P&ID) là CSO hoặc CSC — Car Sealed Opened và Car "
      "Sealed Closed.",
      "During the design stage of a process plant, the Process Engineer "
      "will identify some critical valves that must be securely sealed open "
      "or sealed closed. These chosen valves are marked on the piping and "
      "instrument diagram (P&ID) as CSO or CSC. This stands for Car Sealed "
      "Opened and Car Sealed Closed.")
    P("Thuật ngữ này có từ những ngày đầu của ngành dầu mỏ và bắt nguồn từ "
      "đường sắt. Số lượng lớn ngũ cốc và nông sản khác luôn được đường sắt "
      "vận chuyển khắp nước Mỹ, và cần một phương pháp khóa hàng rẻ và hiệu "
      "quả để chống trộm hoặc người không phép lên toa. Hàng hóa phần lớn "
      "không quá giá trị nên không đáng bỏ nhiều tiền để bảo vệ; hệ thống "
      "bảo vệ còn phải không cần chìa để có thể mở từ nhiều vị trí dọc đường "
      "và khi mở rồi phải đóng lại dễ dàng.",
      "This terminology dates back to the very early days of the petroleum "
      "industry and it originates from the railroads. Huge quantities of "
      "grain and other produce have always been freighted by the railroads "
      "all over the United States and there had to be a cheap and efficient "
      "method of securing this cargo from theft or illegal passengers "
      "boarding the train. The cargo, in most cases, was not particularly "
      "valuable and so it was not worth investing vast sums of money to "
      "protect it. Also the security system had to be keyless to allow "
      "access from various locations along the route of the train and once "
      "opened it had to be easily closed again.")
    P("Phương pháp được phát triển là lấy một đầu sợi dây thép dày, luồn "
      "qua then cửa toa và qua một mắt lưới trên khung cửa, rồi xoắn hai "
      "đầu lại với nhau bằng kìm. Kết quả vừa rẻ vừa sơ sài nhưng hiệu quả: "
      "cửa được đóng chắc chắn và chỉ có thể mở bằng tay với rất nhiều khó "
      "khăn. Nhân viên đường sắt có thể mở cửa toa bằng dụng cụ rồi đóng lại "
      "nhanh chóng. Để tăng cường bảo vệ, người ta thêm các khối chì nóng "
      "chảy vào hai đầu dây để bảo đảm hệ thống niêm phong không thể bị mở "
      "bởi tay người lười biếng, và cách duy nhất để phá niêm phong là dùng "
      "kìm cắt dây cường lực.",
      "The method that was developed was to take one end of a heavy gauge "
      "wire, pass it through the car door bolt lock and then through an "
      "eyelet on the door frame, and finally twist the two ends together "
      "with pliers. The result was cheap and primitive, but it was "
      "effective and doors were securely closed and could only be opened by "
      "hand with very great difficulty. Railway personnel could open the "
      "car doors with the aid of a tool and then close them again quickly. "
      "For added security blobs of molten lead were added to the ends to "
      "guarantee that the sealing system could not be opened by idle hands "
      "and that the only method of breaking the seal was with a pair of "
      "heavy-duty wire cutters.")
    P("Vì đường sắt được dùng để vận chuyển sản phẩm từ các nhà máy quá "
      "trình từ sớm, phương pháp tạm thời cố định này được các chủ nhà máy "
      "hưởng ứng. Đến nay nó vẫn là phương pháp cơ bản nhất để tạm thời đóng "
      "hoặc mở van.",
      "Because the railways were used to transport product from the early "
      "process plants, this method of temporary securing was adopted by the "
      "plant owners. It is still used to this day as the very most basic "
      "method for temporarily closing or opening valves.")

    # ============================================================= LO / LC
    H("Khóa mở và khóa đóng (LO / LC)", "Locked open and locked closed")
    P("Vì vật thể phải đóng là một van ở một vị trí cố định, lý do cần mở "
      "không cần chìa không còn, nên dây được thay bằng xích và khóa bằng "
      "padlock (Hình 10-1 và 10-2). Việc đổi trạng thái van từ mở sang đóng "
      "hoặc ngược lại chỉ có thể thực hiện bởi nhân viên vận hành được phép, "
      "tức là những người có chìa. Đến nay đây vẫn là phương pháp ưa thích "
      "để khóa mở hoặc khóa đóng các van. Phương pháp này ngăn thao tác "
      "vô ý trên các van quan trọng. Thật vậy, trong nhiều dự án ngày nay, "
      "van thường được chỉ định có sẵn bố trí để gắn thiết bị khóa trong "
      "phạm vi cung cấp: có thể là miếng kẹp trên thân van để luồn xích hoặc "
      "khóa chữ D, hoặc tấm có lỗ khoan trên van bi hoặc van cắm. Trên bản "
      "vẽ P&ID và tài liệu nhà máy, phương pháp này được ký hiệu LC (khóa "
      "đóng) hoặc LO (khóa mở).",
      "As the item that had to be closed is a valve in one location, the "
      "reason for having a keyless method of opening was not necessary and "
      "the wire was changed to a chain and closed with a padlock (see "
      "Figure 10-1 and Figure 10-2). To change the function of a valve from "
      "open to closed or vice versa, can only be done by authorized "
      "operators, hence the terminology key personnel. To this day this is "
      "the preferred method of securing valves to be locked open or locked "
      "closed. This method prevents the unintentional operation of "
      "important valves. Indeed on many of today's projects, valves are "
      "often specified with a facility to add a locking device as part of "
      "the scope of supply. This could be either a cleat located on the "
      "body of the valve, through which a chain or a D-lock can be placed, "
      "or a plate with a drilled hole on a ball or plug valve. This method "
      "is identified on P&ID drawings and associated plant documentation as "
      "LC (locked closed) or LO (locked open).")
    FIG(1, F17.fig_vsh_10_1())
    FIG(2, F17.fig_vsh_10_2())

    # ============================================================= interlocking
    H("Khóa liên động cơ khí", "Mechanical interlocking")
    P("Khi nhà máy lớn lên và quá trình ngày càng phức tạp, vận hành ở nhiệt "
      "độ và áp suất cao hơn trong môi trường khắc nghiệt hơn, nhu cầu về "
      "một phương pháp khóa tinh vi hơn trở nên quan trọng. Khả năng phá "
      "hoại cũng phải được tính đến. Những mối quan tâm này dẫn tới sự ra "
      "đời của hệ thống khóa liên động cơ khí — một thiết bị được chế tạo "
      "sẵn có thể lắp cho mọi van tay và van có cơ cấu chấp hành, và chỉ "
      "cho phép thao tác theo một trình tự nhất định với các van khác.",
      "As plants grew in size and processes became more complex, operating "
      "at higher temperatures and pressures in harsher environments, the "
      "need for a more sophisticated method of locking became more "
      "important. The possibility of sabotage also had to be considered. "
      "These concerns led to the development of the mechanical "
      "interlocking system, an engineered piece of equipment that can be "
      "fitted to all manual and actuated valves and only allows operation "
      "to be carried out in a sequence with other valves.")
    P("Thiết bị khóa cơ khí về cơ bản gồm hai bộ phận: trước hết là vỏ kim "
      "loại có khóa liền, được bắt vít vào phần trên của van cùng cơ cấu "
      "vận hành, có thể là tay quay hoặc cần mở. Thứ hai là hai chìa riêng "
      "cho các khóa cụ thể này dùng để mở hoặc đóng van. Một chìa dùng để "
      "khóa mở van, chìa kia dùng để khóa đóng van. Chìa rỗi — chìa không "
      "nằm trên van — luôn được giữ trong tủ chìa (Hình 10-3a và 10-3b) "
      "đặt ở phòng điều khiển, hoặc được dùng để mở/đóng một van khác. Chỉ "
      "nhân viên có chìa được phép mới tiếp cận được tủ này.",
      "The mechanical locking device is essentially two components: first a "
      "metal housing with integral locks that is attached by bolts to the "
      "top works of the valve with the operator, either a handwheel or a "
      "wrench. Secondly there are two keys dedicated to these specific "
      "locks for opening or closure. One key is used to lock open the valve "
      "and the other key is used to lock closed the valve. The loose key, "
      "the one not in the valve, is always retained in a key cabinet (see "
      "Figures 10-3a and 10-3b) that is located in the control room, or "
      "used to open or close another valve. Only authorized key personnel "
      "will have access to this cabinet.")
    FIG(3, F17.fig_vsh_10_3())
    P("Khóa cơ khí là phương pháp tương đối rẻ để hỗ trợ điều khiển quá "
      "trình và góp phần vận hành an toàn cho nhân viên nhà máy và chủ đầu "
      "tư. Các thiết bị này có thể lắp trong giai đoạn xây dựng nhà máy hoặc "
      "lắp bổ sung khi nhà máy đang chạy. Hiện nay thiết bị khóa cơ khí là "
      "giải pháp tốt nhất để tạo môi trường vận hành an toàn.",
      "Mechanical locking is a relatively inexpensive method of aiding "
      "process control and adding to the safe operation of a plant for the "
      "benefit of the plant personnel and the owner. These mechanical "
      "devices can be either installed during the construction phase of the "
      "plant or retrofitted while the plant is operating. At the moment "
      "mechanical locking devices are the best solution to creating a safe "
      "operating environment.")
    P("Các thiết bị khóa này có kết cấu bền và được chế tạo từ kết hợp vật "
      "liệu vừa có độ bền cơ học vừa phù hợp điều kiện môi trường. Thông "
      "thường vỏ được làm từ kết hợp thép các-bon và thép không gỉ, còn "
      "chìa gần như chắc chắn làm từ tấm thép không gỉ (Hình 10-4, 10-5 và "
      "10-6). Van bị khóa mở hoặc khóa đóng thường được ký hiệu LO hoặc LC; "
      "ngoài ra còn gọi thêm SP (Special Piping) cho biết cần một thiết bị "
      "đặc biệt — khóa liên động cơ khí — tại vị trí cụ thể.",
      "These locking devices are of a robust design and constructed of a "
      "combination of materials that both have mechanical strength and are "
      "also suitable for the environmental conditions. Typically the "
      "housing will be constructed of a combination of carbon steel and "
      "stainless steel, however the key is most likely to be made of "
      "stainless-steel plate (see Figure 10-4, Figure 10-5, and Figure "
      "10-6). Valves that are locked open or locked closed are usually "
      "identified as LO (locked open) or LC (locked closed); in addition to "
      "this an SP (Special Piping) is called up indicating that a special "
      "piece of equipment, that is mechanical interlocking, is required at "
      "a specific location.")
    FIG(4, F17.fig_vsh_10_4())
    FIG(5, F17.fig_vsh_10_5())
    FIG(6, F17.fig_vsh_10_6())

    # ============================================================= PRVs
    H("Khóa liên động cho van an toàn áp suất",
      "The mechanical interlocking of pressure safety valves")
    P("Nhà máy quá trình có hệ thống đường ống chịu áp phải có hệ thống giải "
      "áp tích hợp để tránh nổ do quá áp và có thể làm việc đứt ống khi đang "
      "chạy. Van an toàn áp suất (PSV) là rào chắn giữa hệ thống chịu áp ở "
      "phía thượng lưu và xả ra khí quyển phía hạ lưu qua đường ống xả không "
      "có van. Một PSV chứa lò xo được chỉnh để bật mở khi quá trình quá "
      "áp, và lưu chất phải xả ra khí quyển để tránh hỏng thiết bị. Để bảo "
      "trì PSV đang trực, cần có một PSV dự phòng cùng đặc tả để chuyển đổi. "
      "Việc chuyển đổi có thể diễn ra khi nhà máy đang hoạt động nếu bố trí "
      "đường ống đúng. Khi bảo trì, luôn có rủi ro hệ thống đường ống hoặc "
      "bình bị bỏ không được bảo vệ — một mối đe dọa an toàn khi quá áp. Để "
      "tránh rủi ro này, khóa liên động cơ khí có thể lắp trên các van cách "
      "ly thượng lưu và hạ lưu của PRV. Với các khóa liên động này, người "
      "vận hành chỉ có thể mở hoặc đóng van theo một trình tự cụ thể, nghĩa "
      "là hệ thống đường ống hoặc bình luôn được bảo vệ bởi ít nhất một PSV.",
      "Process plants that have pressurized piping systems must also have "
      "an integrated pressure relief system to avoid explosions caused by "
      "overpressurization and possible in-service pipe failure. Pressure "
      "safety valves (PSVs) are the barrier between on the upstream the "
      "pressurized system and on the downstream relief to the atmosphere "
      "via an unvalved header. A PSV contains a spring that is set to pop "
      "when overpressurization of the process piping system occurs and "
      "fluid must be released to the atmosphere to avoid component failure. "
      "In order to execute maintenance to the in-service live PSV, a spare "
      "PSV of the same specification must be available for switchover. This "
      "change-over can take place while the plant is live, if the correct "
      "piping configuration is laid out. When this maintenance activity "
      "takes place, there is always a risk that the piping system or the "
      "vessel is left unprotected, which is a safety threat in the event of "
      "overpressurization. To avoid this risk, mechanical interlocks can be "
      "installed on the upstream and downstream isolating valves associated "
      "with the PRV. With these interlocks installed the operators will "
      "only be able to open or close valves in a specific sequence, which "
      "means that the piping system or the vessel is always protected by a "
      "minimum of one PSV.")
    FIG(7, F17.fig_vsh_10_7())
    P("Quy trình thay PRV 1 (Hình 10-7) như sau:",
      "Procedure to change out PRV 1 (see Figure 10-7):")
    O([
        ("Bước xuất phát: PRV 1 trực, PRV 2 dự phòng; V1, V3, V4 khóa mở; "
         "V2 khóa đóng; chìa B ở phòng điều khiển.",
         "Starting scenario: PRV 1 in service, PRV 2 spare; V1, V3, V4 "
         "locked open; V2 locked closed; Key B in the control room."),
        ("Bước 1 — Lấy chìa B từ phòng điều khiển, cắm vào khe trống trên "
         "V2. Van này giờ có thể mở và khóa, và nhả chìa C.",
         "Step 1 — Key B is collected from the control room and inserted "
         "into the empty slot on V2. This valve can now be opened and "
         "locked, and releases Key C."),
        ("Bước 2 — Chìa C cắm vào khe của V3, nhả chìa D và cho phép van "
         "khóa đóng.",
         "Step 2 — Key C can be inserted into the slot of V3, releasing "
         "Key D and allowing the valve to be locked closed."),
        ("Bước 3 — Chìa D dùng để khóa đóng V4 và nhả chìa E.",
         "Step 3 — Key D is used to lock closed V4 and release Key E."),
        ("Bước 4 — Trả chìa E về phòng điều khiển.",
         "Step 4 — Return Key E to the control room."),
    ])
    P("Kịch bản trung gian: PRV 1 ngừng hoạt động để tháo sửa, PRV 2 trực; "
      "V1, V2 khóa mở; V3, V4 khóa đóng; chìa E ở phòng điều khiển. PRV 1 "
      "có thể được sửa và lắp lại; chìa E lấy từ phòng điều khiển dùng để "
      "khóa mở V4, nhả chìa D trả lại phòng điều khiển.",
      "Intermediate scenario: PRV 1 out of service to be removed for "
      "repair, PRV 2 in service; V1, V2 locked open; V3, V4 locked closed; "
      "Key E in the control room. PRV 1 can be repaired and re-installed, "
      "and Key E can be taken from the control room and used to lock open "
      "V4. This releases Key D, which is returned to the control room.")
    P("Kịch bản cuối: PRV 1 dự phòng, PRV 2 trực; V1, V2, V4 khóa mở; V3 "
      "khóa đóng; chìa D ở phòng điều khiển.",
      "Final scenario: PRV 1 spare, PRV 2 in service; V1, V2, V4 locked "
      "open; V3 locked closed; Key D in the control room.")

    # ============================================================= pigging
    H("Khóa liên động cho bệ phóng và bệ thu pig",
      "The mechanical interlocking of pipeline launchers and receivers")
    P("Đường ống vận chuyển sản phẩm cần làm sạch định kỳ bằng các phần tử "
      "làm sạch gọi là pig, được đẩy qua đường ống bằng nước hoặc lưu chất "
      "phục vụ. Pig được đưa vào đường ống qua bệ phóng — một thiết bị gồm "
      "thân ống, cửa kín và các cổ nối.",
      "Pipelines carrying product require periodic cleaning and this is "
      "achieved by cleaning elements called pigs, which are propelled "
      "through the pipeline by water or the service fluid. These pigs are "
      "introduced into the pipeline via a launcher, which is a piece of "
      "equipment comprising a pipe barrel, a closure door, and various "
      "nozzles.")
    P("Khi đưa pig vào đường ống, điều bắt buộc là hệ thống đường ống phải "
      "đã xả áp hoàn toàn, tránh tai nạn khi cửa kín bị mở trong khi hệ "
      "thống còn áp. Đã có nhiều vụ tử vong và thương tích khi điều này "
      "xảy ra, và việc đưa quy trình khóa liên động cơ khí vào có thể giải "
      "quyết vấn đề này.",
      "When the pig is introduced into the pipeline it is essential that "
      "full depressurization of the piping system has taken place, thus "
      "avoiding any accidents when the closure door has been opened while "
      "the system has been live. There have been numerous fatalities and "
      "injuries when this has happened and by introducing a mechanical "
      "interlocking procedure this problem can be solved.")
    P("Trong điều kiện vận hành bình thường, bệ phóng pig được cách ly và "
      "tất cả các van khóa đóng (Hình 10-8): van thông V4 khóa đóng; van "
      "cách ly V3 khóa đóng; van đường ống V2 khóa mở; van cách ly V1 khóa "
      "đóng; cửa kín bệ phóng khóa đóng; chìa A ở phòng điều khiển.",
      "Under normal operating conditions the pipeline pig launcher is "
      "isolated and all valves are locked closed (Figure 10-8): vent valve "
      "V4 locked closed; isolating valve V3 locked closed; pipeline valve "
      "V2 locked open; isolating valve V1 locked closed; launcher closure "
      "door locked closed; Key A in the control room.")
    FIG(8, F17.fig_vsh_10_8())
    P("Trình tự nạp pig:",
      "Loading the pig:")
    O([
        ("Bước 1 — Lấy chìa A từ phòng điều khiển dùng để mở van thông V4; "
         "hành động này nhả chìa B.",
         "Step 1 — Key A is removed from the control room and used to open "
         "the vent valve V4. This releases Key B."),
        ("Bước 2 — Chìa B dùng để mở cửa kín ở cuối thân bệ phóng.",
         "Step 2 — Key B is now used to open the closure door at the end "
         "of the launcher barrel."),
        ("Trạng thái khi nạp: V4 khóa mở; V3 khóa đóng; V2 khóa mở; V1 khóa "
         "mở; cửa kín khóa mở; không có chìa ở phòng điều khiển. Pig có thể "
         "đặt vào thân ống và chuẩn bị phóng.",
         "Loading state: V4 locked open; V3 locked closed; V2 locked open; "
         "V1 locked open; closure door locked open; no key in the control "
         "room. The pig can be placed in the barrel and prepared for "
         "launching."),
    ])
    P("Phóng pig — để khôi phục bệ phóng, trước hết phải thực hiện trình tự "
      "chìa ngược lại:",
      "Launching the pig — to re-instate the launcher, first a reverse key "
      "sequence has to take place:")
    O([
        ("Bước 3 — Cửa bệ phóng khóa đóng, nhả chìa B; chìa B dùng để khóa "
         "đóng van thông V4, nhả chìa A.",
         "Step 3 — The launcher door is locked closed, releasing Key B, "
         "which is used to lock closed vent V4. This releases Key A."),
        ("Bước 4 — Chìa A dùng để khóa mở van cách ly V3, nhả chìa C.",
         "Step 4 — Key A is used to lock open the isolating valve V3, "
         "which releases Key C."),
        ("Bước 5 — Chìa C dùng để khóa mở van V1, nhả chìa D. Lúc này bệ "
         "phóng pig chịu toàn áp đường ống.",
         "Step 5 — Key C is used to lock open valve V1, which releases Key "
         "D. At this point the pig launcher is under full line pressure."),
        ("Bước 6 — Chìa D dùng để khóa đóng van đường ống chính V2.",
         "Step 6 — Key D is used to lock closed the main pipeline valve "
         "V2."),
    ])
    P("Van tiết lưu V2 sau đó được dùng để thu hẹp dòng chảy qua bệ phóng, "
      "gây tích áp phía sau pig cho tới khi ma sát được thắng và pig bắt "
      "đầu hành trình dọc đường ống. Áp lực đẩy pig được duy trì cho tới "
      "khi pig hoàn thành hành trình và tới bình thu. Bệ thu cũng được bảo "
      "vệ bằng một bộ van khóa liên động tương tự, và một trình tự mở/đóng "
      "van phải được thực hiện trước khi bệ thu xả áp, cửa có thể mở và pig "
      "được lấy ra khỏi thân ống.",
      "The throttle valve, V2, is then used to restrict the flow through "
      "the launcher, which causes a pressure build-up behind the pig, until "
      "friction is overcome causing the pig to start its travel along the "
      "pipeline. Pressure to drive the pig will be sustained until the pig "
      "has completed its journey and arrived at the receiver vessel. The "
      "receiver will also be protected by a similar mechanically "
      "interlocked set of valves and a sequence of opening and closing "
      "valves will have to be carried out before the receiver is "
      "depressurized, the door can be opened, and the pig retrieved from "
      "the barrel.")
    P("Nội dung trên là quy trình cơ bản để phóng và thu pig; hoạt động này "
      "có thể phức tạp hơn với áp suất cao hơn, bố trí đường ống khác nhau "
      "và việc thêm PSV. Nhưng mục tiêu là như nhau — bệ phóng hoặc bệ thu "
      "chỉ có thể được mở khi đã xả áp an toàn và xả hết lưu chất dư.",
      "What has been described above is the basic procedure to launch and "
      "receive a pig, and this activity can be more complex with higher "
      "pressures, different piping configurations, and the addition of "
      "PSVs. But the objective is the same — that the launcher or a "
      "receiver can only be opened when they have been safely "
      "depressurized and drained of excess fluid.")

    # ============================================================= conclusion
    H("Kết luận", "Conclusion")
    P("Việc dùng van khóa liên động cơ khí đã vận hành rất thành công trong "
      "những năm gần đây và nhờ mức độ an toàn tăng lên, chúng đã trở thành "
      "bổ sung có giá trị cho thiết bị nhà máy hóa dầu. Đã có nhiều sự cố "
      "nhà máy trong quá khứ có thể tránh được nếu có hệ thống khóa liên "
      "động. Khóa liên động cơ khí không nên bị xem là phụ kiện, mà là bộ "
      "phận hợp nhất của hệ thống giải áp an toàn đường ống, thiết yếu để "
      "bảo đảm vận hành nhà máy an toàn.",
      "The use of mechanically interlocked valves has worked very "
      "successfully in recent years and because of the increase in safety, "
      "they have become a valuable addition to petrochemical plant "
      "equipment. There have been numerous plant accidents in the past that "
      "could have been avoided if an interlock system had been in place. "
      "Mechanical interlocks should not be looked upon as an accessory, but "
      "as an integral part of a piping safety relief system, which is "
      "essential to guarantee safe plant operation.")

    # ============================================================= summary
    H("Tóm tắt đơn vị 20", "Unit 20 summary")
    b.append(table(
        ["Hạng mục", "Loại", "Điểm chính"]
        if vi else ["Aspect", "Type", "Key point"],
        [
            ["CSO / CSC" if vi else "CSO / CSC",
             "niêm phong dây chì" if vi else "lead-wire seals",
             "ký hiệu P&ID cho van tới hạn" if vi else
             "P&ID marks for critical valves"],
            ["LO / LC" if vi else "LO / LC",
             "xích + padlock" if vi else "chain + padlock",
             "chỉ người có chìa đổi trạng thái" if vi else
             "only key personnel change state"],
            ["10-1, 10-2" if vi else "10-1, 10-2",
             "dây + padlock độc lập" if vi else "wire + independent padlock",
             "hộp số, tay quay van cầu" if vi else
             "gearbox, globe handwheel"],
            ["10-3" if vi else "10-3",
             "tủ chìa khóa" if vi else "key cabinet",
             "chìa rỗi giữ ở phòng điều khiển" if vi else
             "spare key retained in control room"],
            ["10-4…10-6" if vi else "10-4…10-6",
             "hộp khóa trên van" if vi else "locking housings on valves",
             "gate, bi, bướm; hai chìa riêng" if vi else
             "gate, ball, butterfly; two dedicated keys"],
            ["10-7" if vi else "10-7",
             "khóa hai PRV" if vi else "dual-PRV interlock",
             "luôn có ít nhất một PSV trực" if vi else
             "at least one PSV always in service"],
            ["10-8" if vi else "10-8",
             "khóa bệ phóng pig" if vi else "pig launcher interlock",
             "chỉ mở cửa khi đã xả áp" if vi else
             "door opens only when depressurized"],
            ["SP" if vi else "SP",
             "bố trí đường ống đặc biệt" if vi else "special piping",
             "gọi kèm LO/LC trên tài liệu" if vi else
             "called up with LO/LC in documentation"],
        ],
        caption=("Tóm tắt theo văn bản nguồn, book pp. 314–326, "
                 "Hình 10-1…10-8." if vi else
                 "Summary from source text, book pp. 314–326, "
                 "Figures 10-1…10-8."),
        cls="tbl wide"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
