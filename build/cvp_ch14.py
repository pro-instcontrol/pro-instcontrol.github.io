# -*- coding: utf-8 -*-
"""Book 7, Chapter 14 - When Do I Need to “Hard Face” the Valve Trim and Other
Questions Concerning Valve Material (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
99-102 (PDF pp. 102-105). No figures, no tables; one Rockwell-hardness
footnote, three references and several material-grade callouts.
"""
from cvp_common import h2, h3, note, p, refs

PAGES_SRC = 4
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "When Do I Need to “Hard Face” the Valve Trim and Other Questions Concerning Valve Material"
TITLE_VI = "Khi nào cần “phủ cứng” bộ lót van và các câu hỏi khác về vật liệu van"


def note_terms(lang):
    """A one-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 14.</b> ăn mòn (corrosion) · xói mòn (erosion) · vật liệu "
                "phần ướt (wetted parts) · chất lưu chứa hạt rắn · bùn than (coal slurry) · "
                "van kẹp (pinch valve) · van bướm lót cao su · lót elastomer · cao su tự nhiên "
                "/ GRS (Buna-S) · chênh áp (pressure drop) · giữ hạt lơ lửng (particles in "
                "suspension) · van góc (angle valve) · dòng chảy làm đóng nút van (flow "
                "tending-to-close the plug) · phủ cứng (hard facing) · bề mặt đế van / vòng "
                "đế van (seating surfaces / seat ring) · độ cứng Rockwell C (RC) · gầm van "
                "(plug guide) · bạc dẫn hướng (guide bushing) · gốm ceramic · cacbua vonfram "
                "(tungsten carbide) · thu hẹp dòng (vena contracta) · xâm thực (cavitation) · "
                "thép không gỉ 316 / 440C / 17-4 pH · Stellite · hợp kim chrome-moly · đồng "
                "thau (bronze) · hơi ngưng tụ (water condensate) · hơi quá nhiệt (superheated "
                "steam) · giãn nở đẳng entropy (isentropic throttling) · ăn mòn ứng suất (stress "
                "corrosion) · khí «chua» chứa lưu huỳnh (sour gas) · vận tốc âm (sonic velocity) "
                "· bạc ổ trục (guide bushing / bearing) · TFE / PTFE (Teflon) · sợi thủy tinh "
                "· Nitronic 60 · than chì rắn (solid graphite) · van bi / van quay (rotary valve) "
                "· van cầu (globe valve) · bùn bô-xít (bauxite slurry) · đế van / bệ van / mặt "
                "tựa của van (seat).")
    return ("<b>Key terms.</b> corrosion · erosion · wetted parts · solid particles in the fluid · "
            "coal slurry · pinch valve · rubber-lined butterfly valve · elastomer liner · natural "
            "rubber / GRS (Buna-S) · pressure drop · particles in suspension · angle valve · flow "
            "tending-to-close the plug · hard facing · seating surfaces / seat ring · Rockwell C "
            "hardness (RC) · plug guide · guide bushing · ceramic · tungsten carbide · vena "
            "contracta · cavitation · 316 / 440C / 17-4 pH stainless steel · Stellite · "
            "chrome-moly alloy · bronze · water condensate · superheated steam · isentropic "
            "throttling · stress corrosion · sour (sulfur-containing) gas · sonic velocity · "
            "bearing material · TFE / PTFE (Teflon) · glass fiber · Nitronic 60 · solid graphite "
            "· rotary valve · globe valve · bauxite slurry · seat.")


def body_vi():
    b = []
    b.append(h2("Xói mòn — nguyên nhân chính gây hỏng van",
                "Erosion — the main cause of valve failure"))
    b.append(p("Ngoài ăn mòn (corrosion) — vốn có thể xử lý bằng cách tra cứu một sổ tay tốt "
               "khi chọn vật liệu cho các phần tiếp xúc chất lưu — thì xói mòn (erosion) là "
               "nguyên nhân của hầu hết các hỏng hóc van. Chúng ta phải phân biệt rõ nguyên "
               "nhân của xói mòn thì mới có thể đưa ra giải pháp bền lâu."))

    b.append(h2("Xói mòn do hạt rắn trong dòng chất lưu hoặc vật liệu dạng hạt như bùn than",
                "Erosion caused by solid particles in the fluid stream or granular materials such as coal slurry"))
    b.append(p("Nếu vận tốc của chất lưu gây xói mòn đủ thấp (ví dụ, thấp hơn vận tốc tương ứng "
               "với chênh áp van 10 psi), thì lớp lót elastomer làm việc rất tốt, đặc biệt là "
               "cao su tự nhiên hoặc các loại elastomer GRS (Buna-S); khi đó nên cân nhắc van "
               "kẹp (pinch valve) hoặc van bướm lót cao su."))
    b.append(p("Hãy nhớ rằng phải có chênh áp tối thiểu 1 psi qua van để giữ các hạt lơ lửng "
               "(vận tốc 3 đến 7 ft/s). Với chênh áp cao hơn hoặc nhiệt độ tăng, hãy cân nhắc "
               "van góc theo chiều «dòng chảy có xu hướng làm đóng nút van». Hãy cố gắng xả "
               "dòng vào một đoạn ống phía dưới có đường kính ít nhất bằng bốn lần kích thước "
               "lỗ tiết lưu, để tránh cắt thủng thành ống. Việc phủ cứng (hard facing) các bề "
               "mặt đế van, lỗ vòng đế van và đường viền ngoài của nút van là cách tốt để kéo "
               "dài tuổi thọ làm việc. Để đóng kín chặt, tốt nhất là tạo sự chênh lệch độ cứng giữa "
               "nút van (40 đến 46 RC)<sup>1</sup> và vòng đế van (56 đến 62 RC). Điều tương tự "
               "có thể nói về sự chênh lệch độ cứng giữa bề mặt dẫn hướng của nút van và bạc "
               "dẫn hướng. Với nút van cỡ nhỏ, gốm đặc (ALO2) hoặc cacbua [1] (chẳng hạn cacbua "
               "vonfram) có hiệu quả. Tuy nhiên, chìa khóa là làm cho dòng chảy được suôn sẻ "
               "ở mọi vùng tiến về phía chỗ thu hẹp nút van/đế van (vena contracta), và tránh "
               "bất cứ thứ gì gây va đập trực tiếp của chất lưu vào các bề mặt vỏ van lân cận. "
               "Lý tưởng nhất là chỉ có lỗ tiết lưu của van làm tăng tốc chất lưu."))
    b.append(note("<b>Chú thích 1.</b> Độ cứng theo thang Rockwell C."))
    b.append(p("Sự giảm tốc thực tế (chênh áp) cùng độ nhiễu loạn phá hủy sinh ra sau đó phải "
               "xảy ra bên trong một ống hoặc bình lớn ở phía dưới — chứ không phải gần nút "
               "van."))
    b.append(p("Để có ví dụ về tuổi thọ ngắn ngủi của nút van và vòng đế van, xem Tài liệu tham "
               "khảo 2: ở đó, một vòng đế van 6 in làm bằng thép không gỉ 316 đã bị phá hủy "
               "hoàn toàn trong vài tuần khi xử lý đất sét mịn lơ lửng trong dầu nóng với chênh "
               "áp chỉ 50 psi. (Tôi nghi ngờ van cũng chịu xâm thực, và điều đó đương nhiên đã "
               "làm tăng tốc sự phá hủy.) Trong một ví dụ khác, một nút van đường kính 1½ in "
               "được phủ hoàn toàn Stellite số 1 đã bị mòn sạch trong 2 tuần bởi bùn quặng "
               "uranium, dù chênh áp chỉ là 100 psi."))
    b.append(p("Hãy nhớ rằng bộ lót đã được tôi cứng và đắt tiền chỉ làm chậm sự phá hủy, chứ "
               "không ngăn được nó. Trong một số trường hợp, mua van rẻ nhất có thể và thay "
               "thế định kỳ lại kinh tế hơn. Đó là cách làm đã được áp dụng trong điều khiển "
               "bùn bô-xít, nơi dùng một van bướm thép carbon đơn giản và thay thế nó theo "
               "chu kỳ."))

    b.append(h2("Xói mòn do hơi ướt", "Erosion by wet steam"))
    b.append(p("Ở một đầu của thang nhiệt độ là nước ngưng tụ, thứ tấn công thép carbon. Vì "
               "vậy chỉ dùng hợp kim chrome-moly, đồng thau hoặc thép không gỉ làm vật liệu "
               "thân van, hoặc đảm bảo có một gioăng đặt dưới vòng đế van bằng thép không gỉ "
               "nếu dùng thân van bằng thép carbon. Ở đầu kia là hơi quá nhiệt, có thể phóng "
               "các giọt nước trong quá trình tiết lưu đẳng entropy trong van. Ở đây nên dùng "
               "bộ lót thép không gỉ martensitic chứa crôm, đặc biệt là loại AISI 440C, có thể "
               "tôi cứng tới khoảng 58 RC. Ở nhiệt độ thấp hơn (<750°F), thép không gỉ 17-4 pH "
               "cũng hữu ích nếu được xử lý nhiệt, thường ở 1075°F, cho độ cứng khoảng 38 RC. "
               "Hãy theo dõi mức pH của hơi. Điều kiện kiềm (>7 pH) có thể gây ăn mòn ứng suất "
               "trên các chi tiết cứng hơn 35 RC [2]. Tiện thể, điều này cũng đúng với khí "
               "thiên nhiên «chua» (chứa lưu huỳnh)."))
    b.append(p("Không có quy tắc cứng nhắc về thời điểm hoặc điều kiện áp suất nào thì nên phủ "
               "cứng bộ lót. Hãy nhớ rằng chất lưu khí đạt vận tốc âm trong lỗ tiết lưu (thường "
               "là 1350 ft/s đối với hơi), bất kể chênh áp là từ 3000 psi xuống 500 psi hay chỉ "
               "từ 15 psi đo (gauge) tới áp suất khí quyển."))

    b.append(h2("Vật liệu dẫn hướng và vật liệu ổ trục",
                "Guide material and bearing material"))
    b.append(p("Về vật liệu dẫn hướng thân van hoặc trục van: khí thiên nhiên từ giếng có chứa "
               "cát không? Đó là một trong những câu hỏi cần được đặt ra khi quy định vật liệu "
               "van. Nếu không, vật liệu bộ lót dùng cho mục đích chung — tức thép không gỉ AISI "
               "loại 316 — sẽ làm việc rất tốt với chất lỏng hoặc khí sạch, ngay cả khi chênh "
               "áp vượt quá 1000 psi, dù hầu hết các sổ tay giới hạn ΔP cho phép của bộ lót thép "
               "không gỉ ở mức 150 đến 200 psi [3]."))
    b.append(p("Một lời cuối về vật liệu dẫn hướng: đối với van cầu và dịch vụ áp suất thấp "
               "(ΔP <500 psi), cả bạc dẫn hướng của nút van lẫn của thân van đều có thể làm bằng "
               "thép không gỉ 316, miễn là bề mặt nút van bằng thép không gỉ 316 hoặc bề mặt "
               "thân van bằng thép không gỉ 316 được làm cứng chắc đôi chút bằng gia công phù "
               "hợp hoặc kỹ thuật lăn ép (roller burnishing)."))
    b.append(p("Lý do gây mòn bộ lót tinh tế hơn. Hơi do van xử lý có khá ướt vì van đặt xa lò "
               "hơi không? Chất lưu có chứa chất xúc tác rắn không? Chất lưu có xu hướng kết "
               "tinh trong một số điều kiện không? Có thể tồn tại dòng chảy hai pha (chất lỏng "
               "cộng khí) không? Khí thiên nhiên từ giếng có chứa cát không? Những câu hỏi này "
               "được giải đáp ở chương sau."))
    b.append(p("Các loại van nặng hơn dùng bạc dẫn hướng bằng thép không gỉ loại 440C hoặc, cho "
               "dịch vụ ăn mòn, bạc làm bằng hoặc phủ hợp kim coban–crôm–vonfram như Stellite. "
               "Đối với van quay, bạc bằng sợi thủy tinh phân tán TFE làm việc tốt đến 350°F và "
               "bạc bằng đồng thau phân tán TFE đến 450°F. Các vật liệu ổ trục phù hợp khác là "
               "Nitronic 60 — hợp kim thép không gỉ dùng được tới 800°F — hoặc, nếu được giữ "
               "chặt đúng cách, bạc than chì rắn. Với nhiệt độ cao hơn (tới 1250°F) và/hoặc "
               "dịch vụ ăn mòn, hãy dùng hợp kim coban–crôm–vonfram hoặc than chì."))
    b.append(p("Không thể đưa ra khuyến nghị vật liệu cho vô số hóa chất ăn mòn. Tuy nhiên, "
               "khi còn nghi ngờ, van lót polytetrafluoroethylene (PTFE; Teflon) thường là lựa "
               "chọn tốt nhất. Bạn có thể chọn giữa van cầu với dải Cv từ 0,001 đến 100, hoặc "
               "van quay cho khả năng lưu lượng lớn hơn."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "W. L. Kennicott, “Use of Hard Carbide Components” In Petrochemical Processing, "
        "ASME Paper 61-SA-51 (1962).",
        "Kenneth M. Pruett, Compass Corrosion Guide II: A Guide to Chemical Resistance of "
        "Metals and Engineering Plastics (La Mesa, CA: Compass Publications, 1983).",
        "Paul Wing, “Selecting Control Valve Trim for High Pressure Drop and Erosive Service,” "
        "ISA Journal 2 (September 1955): 332–337.",
    ]))
    b.append(note("<b>Ghi chú về nguồn.</b> (1) Lớp văn bản OCR có nhiều dấu gạch nối khi xuống "
                  "dòng («select-», «butter-», «parti-», «adjoin-», «chro-», «mate-», «ser-»); "
                  "bản dịch ghép lại thành từ hoàn chỉnh. (2) Nguồn in «chrome-molly alloys» "
                  "(thường viết là chrome-moly); bản dịch giữ nguyên dạng in. (3) Công thức gốm "
                  "được in là «ALO2»; bản dịch giữ nguyên dạng in. (4) Câu hỏi «Does natural gas "
                  "coming from a well contain sand?» xuất hiện hai lần trong bản in — một lần "
                  "ở đoạn về vật liệu dẫn hướng và một lần trong danh sách lý do gây mòn; cả "
                  "hai đều được giữ lại. (5) Một cụm từ trong bản dịch bị lặp nhầm trong quá "
                  "trình soạn thảo đã được loại bỏ; nội dung giữ nguyên ý định của nguyên bản."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 14 chiếm các trang in 99–102 của ấn bản in (PDF tr. 102–105). Nguyên "
               "bản không có hình và không có bảng; chương gồm phần mở đầu, các mục về xói "
               "mòn do hạt rắn và do hơi ướt, các đoạn về vật liệu dẫn hướng và ổ trục, một "
               "chú thích về độ cứng Rockwell C và ba tài liệu tham khảo — tất cả đều được giữ "
               "lại. Các tiêu đề phụ trong bản dịch được biên tập thêm vì nguyên bản chỉ có một "
               "số tiểu mục không đánh số."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Xói mòn — nguyên nhân chính gây hỏng van",
                "Erosion — the main cause of valve failure"))
    b.append(p("Besides corrosion, which can be handled by consulting a good handbook when "
               "selecting a suitable material for wetted parts, erosion is the cause of most "
               "valve failures. We must distinguish the causes of erosion to affect a durable "
               "solution."))

    b.append(h2("Erosion caused by solid particles in the fluid stream or granular materials such as coal slurry",
                "Erosion caused by solid particles in the fluid stream or granular materials such as coal slurry"))
    b.append(p("If the velocity of the erosive fluid is low enough (e.g., less than "
               "corresponding to a 10 psi valve pressure drop), then elastomer lining works "
               "well, particularly with natural rubber or GRS (Buna-S) types of elastomers, and "
               "a pinch valve or rubber-lined butterfly valve should be considered."))
    b.append(p("Remember, there must be a pressure drop across the valve of at least 1 psi to "
               "keep particles in suspension (3 to 7 ft/s velocity). For higher pressure drop "
               "or where temperature is elevated, consider angle valves in the “flow "
               "tending-to-close the plug” direction. Try to discharge the flow into a "
               "downstream pipe that has a diameter of at least four times the orifice size to "
               "avoid cutting through the pipe wall. Hard facing of the seating surfaces, the "
               "seat ring bore, and the outer contour of the plug is a good practice to prolong "
               "service life. For tight shutoff, it is best if there is a difference in hardness "
               "between the plug (40 to 46 RC)<sup>1</sup> and seat ring (56 to 62 RC). The same "
               "can be said for the hardness difference between the plug guide and the guide "
               "bushing. For smaller size plugs, solid ceramic (ALO2) or carbides [1] (such as "
               "tungsten carbide) are effective. However, the key is to streamline the fluid "
               "flow in all areas that approach the plug/seat restriction (vena contracta) and "
               "to avoid anything that would cause direct fluid impact on adjoining valve "
               "housing surfaces. Ideally, only the valve orifice should accelerate the fluid."))
    b.append(note("<b>Footnote 1.</b> Rockwell C-Scale hardness."))
    b.append(p("The actual deceleration (pressure drop) with the resulting destructive high "
               "turbulence should take place inside a large pipe or vessel downstream—but not "
               "close to the valve plug."))
    b.append(p("For an example of how brief the service life of valve plugs and seat rings can "
               "be, see Reference 2, in which a 6-inch seat ring made from 316 stainless steel "
               "was completely destroyed within a few weeks while handling fine clay in "
               "suspension in hot oil at a pressure drop of only 50 psi. (I suspect that the "
               "valve also underwent cavitation, which, of course, accelerated the "
               "destruction.) In another example, a fully Stellite No. 1–coated, 1½-inch-"
               "diameter valve plug was completely worn away by uranium ore slurry within 2 "
               "weeks, even though the pressure drop was only 100 psi."))
    b.append(p("Remember, the hardened and expensive valve trim will only delay the "
               "destruction, not prevent it. In some cases, it is more cost-effective to buy "
               "the cheapest valve possible and to replace it on a regular basis. This has been "
               "the practice with the control of bauxite slurry where a simple carbon steel "
               "butterfly valve was used and periodically replaced."))

    b.append(h2("Erosion by wet steam", "Erosion by wet steam"))
    b.append(p("On one side of the temperature scale is water condensate, which attacks carbon "
               "steel. Therefore, only use chrome-molly alloys, bronze, or stainless steel as "
               "valve body material, or make sure a gasket is placed under the stainless-steel "
               "seat ring in case a carbon steel body is employed. On the other side is "
               "superheated steam, which can discharge water droplets during isentropic "
               "throttling in a valve. Here the use of martensitic, chromium stainless steel "
               "trim is recommended, especially AISI type 440C, which can be hardened to about "
               "58 RC. For lower temperatures (<750°F), 17-4 pH stainless steel is also useful "
               "if heat treated, usually at 1075°F, yielding a hardness of about 38 RC. Watch "
               "the pH level of the steam. A caustic condition (>7 pH) can cause stress "
               "corrosion on parts harder than 35 RC [2]. Incidentally, this also applies to "
               "“sour” (sulfur-containing) natural gas."))
    b.append(p("There is no hard-and-fast rule for when or under what pressure conditions a "
               "trim should be hard-faced. Remember, gaseous fluid undergoes sonic velocity in "
               "the orifice (typically 1350 ft/s for steam) regardless of whether the pressure "
               "drop is from 3000 psi to 500 psi or only from 15 psi gauge to atmosphere."))

    b.append(h2("Guide material and bearing material",
                "Guide material and bearing material"))
    b.append(p("Regarding stem or shaft guide material, does natural gas coming from a well "
               "contain sand? These are all questions that should be asked when specifying the "
               "valve material. Otherwise, the general-purpose trim material, that is, AISI type "
               "316 stainless steel, will do just fine with clean liquid or gases even if the "
               "pressure drop exceeds 1000 psi, even though most handbooks limit the allowable "
               "ΔP for stainless steel trim to between 150 and 200 psi [3]."))
    b.append(p("A final word regarding guide material: For globe valves and low-pressure service "
               "(<500 psi ΔP), both plug or stem guide bushing can be 316 stainless steel, as "
               "long as the 316 stainless steel plug surface or the 316 stainless steel stem "
               "surface is somewhat work hardened by suitable machining or roller burnishing "
               "techniques."))
    b.append(p("The reasons for trim wear are more subtle. Is the steam handled by the valve "
               "fairly wet because the valve is far removed from the boiler? Does the fluid "
               "contain a solid catalyst? Does the fluid tend to crystallize under certain "
               "conditions? Can two-phase flow (liquid plus gas) exist? Does natural gas coming "
               "from a well contain sand? These questions are addressed in the next chapter."))
    b.append(p("Heavier valve types use type 440C stainless-steel guide bushings or, for "
               "corrosive service, bushings made of or faced with a cobalt-chromium-tungsten "
               "alloy such as Stellite. For rotary valves, tetrafluoroethylene (TFE)-dispersed "
               "glass fiber bushings work well up to 350°F and TFE-dispersed bronze bushings to "
               "450°F. Other suitable bearing materials are Nitronic 60, a stainless-steel alloy "
               "suitable to 800°F or, if properly retained, a solid graphite bushing. For higher "
               "temperature (to 1250°F) and/or corrosive service, use cobalt-chromium-tungsten "
               "alloy or graphite."))
    b.append(p("Recommending suitable materials for the infinite variety of corrosive "
               "chemicals is not possible. However, when in doubt, a "
               "polytetrafluorethylene (PTFE; Teflon)-lined valve is usually the best bet. Your "
               "choice is between globe valves with Cv ranges from 0.001 to 100 or rotary valves "
               "for larger capacities."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "W. L. Kennicott, “Use of Hard Carbide Components” In Petrochemical Processing, "
        "ASME Paper 61-SA-51 (1962).",
        "Kenneth M. Pruett, Compass Corrosion Guide II: A Guide to Chemical Resistance of "
        "Metals and Engineering Plastics (La Mesa, CA: Compass Publications, 1983).",
        "Paul Wing, “Selecting Control Valve Trim for High Pressure Drop and Erosive Service,” "
        "ISA Journal 2 (September 1955): 332–337.",
    ]))
    b.append(note("<b>Source notes.</b> (1) The OCR text layer contains many line-break "
                  "hyphenations («select-», «butter-», «parti-», «adjoin-», «chro-», «mate-», "
                  "«ser-»); the translation rejoins them into whole words. (2) The source prints "
                  "«chrome-molly alloys» (usually written chrome-moly); the printed form is "
                  "retained. (3) The ceramic formula is printed as «ALO2»; the printed form is "
                  "retained. (4) The question «Does natural gas coming from a well contain "
                  "sand?» occurs twice in the source — once in the guide-material passage and "
                  "once in the list of trim-wear reasons; both occurrences are retained. (5) One "
                  "duplicated editorial phrase introduced during drafting was removed without "
                  "changing the intended content."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chapter 14 occupies printed pp. 99-102 of the book (PDF pp. 102-105). The source "
               "has no figures and no tables; it consists of an opening passage, sections on "
               "erosion by solid particles and by wet steam, passages on guide and bearing "
               "materials, a Rockwell-hardness footnote and three references, all of which are "
               "retained. The editorial subheadings in the translation were added because the "
               "source has only a few unnumbered subsection headings."))
    return "".join(b)
