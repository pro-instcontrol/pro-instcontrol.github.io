# -*- coding: utf-8 -*-
"""Book 7, Chapter 16 - Concern for the Environment (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
109-110 (PDF pp. 112-113). Two printed pages, zero figures, no references;
the chapter covers fugitive emissions, gasket and bonnet sealing, extended
bonnets, packing friction and rotary stem packing.
"""
from cvp_common import eq, h2, h3, note, ol, p

PAGES_SRC = 2
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Concern for the Environment"
TITLE_VI = "Quan tâm đến môi trường"


def note_terms(lang):
    """A one-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 16.</b> khí thải thoát hưu (fugitive emissions) · rò rỉ "
                "· gioăng (gasket) · thân van (valve housing/body) · nắp van bắt bulông "
                "(bolted bonnet) · nắp ren (threaded closure) · gioăng vòng mềm nhiều vòng kim "
                "loại xen kẽ nhựa biến dạng · Teflon · tải trọng bulông tối thiểu · bộ lót "
                "dạng lồng (cage trim) · hệ số giãn nở nhiệt · rò rỉ tại mặt ghép · nắp van kéo "
                "dài (extended bonnet) · đệm chèn (packing) · thân van trượt / thân van quay · "
                "ma sát đệm chèn · lực ma sát thân van · vùng chết (deadband) · dải đo (span) · "
                "đệm chèn V-ring Teflon có lò xo · than chì (graphite) · bệ ép đệm (packing "
                "follower) · mô-men xoắn (torque) · mòn thân do hạt rắn · van chuyển động tịnh "
                "tiến (reciprocating valve) · thay đổi tín hiệu · Chương 24.")
    return ("<b>Key terms.</b> fugitive emissions · leakage · gasket · valve housing/body · "
            "bolted bonnet · threaded closure · flexible ring gasket with metal rings and "
            "deformable plastic · Teflon · minimum bolting load · cage trim · coefficient of "
            "thermal expansion · seal leakage · extended bonnet · packing · sliding or rotary "
            "valve stem · packing friction · stem friction force · deadband · span · "
            "spring-loaded Teflon V-ring packing · graphite · packing follower · torque · stem "
            "abrasion by particles · reciprocating valve · signal change · Chapter 24.")


def body_vi():
    b = []
    b.append(h2("Khí thải thoát hưu", "Fugitive emissions"))
    b.append(p("Sự quan tâm ngày càng lớn đối với môi trường không khí sạch đã làm cho mức phát "
               "thải chất lỏng hoặc khí từ van điều khiển trở nên nghiêm ngặt hơn đáng kể."))
    b.append(p("Van điều khiển thường có hai vị trí có thể rò rỉ:"))
    b.append(ol([
        "Gioăng giữa thân van và nắp van bắt bulông, hoặc các nắp ren, để tạo thành một lớp "
        "bịt kín áp suất.",
        "Đệm chèn trên thân van trượt hoặc thân van quay (xem Chương 24).",
    ]))

    b.append(h3("Mặt ghép thân–nắp van và bộ lót dạng lồng",
                "Body–bonnet joints and cage trim"))
    b.append(p("Có thể giải quyết dễ dàng hơn nhóm vấn đề thứ nhất bằng cách dùng gioăng phù "
               "hợp. Gioăng vòng mềm có nhiều vòng kim loại xen kẽ các vật liệu nhựa biến dạng "
               "như Teflon là loại được ưa dùng. Các bulông ép gioăng đó phải đủ bền không chỉ "
               "để duy trì áp suất chất lưu cực đại mà còn để biến dạng gioăng đủ mức, loại bỏ "
               "các khe hở nhỏ. Tải trọng bulông tối thiểu phải bằng 2,5 lần lực cần thiết chỉ "
               "để chịu áp suất."))
    b.append(p("Cần chú ý khi mặt bích nắp van đồng thời giữ bộ lót dạng lồng. Khi vật liệu lồng "
               "có hệ số giãn nở nhiệt lớn hơn thân van và có chất lưu nóng, đã có trường hợp "
               "vành lồng cố nâng nắp van ra khỏi thân van và gây rò rỉ tại mặt ghép."))

    b.append(h3("Nắp van kéo dài", "Extended bonnet"))
    b.append(p("Nắp van kéo dài luôn có ích. Đối với chất lỏng, nắp dài làm giảm nhiệt độ của "
               "chất lỏng tại vị trí đệm chèn; nhờ đó độ nhớt tăng và rò rỉ giảm. Đối với hơi, "
               "nắp dài hơn sẽ ngưng tụ hơi thành nước, cũng làm giảm rò rỉ qua đệm chèn. Tuy "
               "nhiên, cách này chỉ có tác dụng khi van được lắp úp ngược; nếu không, chất lỏng "
               "ngưng tụ sẽ chảy ngược về thân van."))

    b.append(h3("Ma sát đệm chèn và ổn định vòng điều khiển",
                "Packing friction and loop stability"))
    b.append(p("Ma sát đệm chèn có thể ảnh hưởng đến độ ổn định của vòng điều khiển. Theo quy "
               "tắc kinh nghiệm, lực ma sát thân van do đệm chèn gây ra có thể ước tính bằng "
               "diện tích mặt cắt ngang của thân nhân với áp suất đầu vào."))
    b.append(eq("F_friction ≈ A_stem × P1"))
    b.append(p("Ví dụ, với thân van đường kính 1/2 in và áp suất đầu vào 100 psi, lực ma sát có "
               "thể là 19,5 lb. Dùng cơ cấu chấp hành màng có diện tích 500 in², lực đó có thể "
               "tạo vùng chết ±0,04 psi, tức 0,6% dải đo — hoàn toàn chấp nhận được khi có bộ "
               "định vị van. Các giá trị này dựa trên kiểu đệm chèn V-ring Teflon có lò xo."))
    b.append(eq("A_stem = π(0.5 in)² / 4 ≈ 0.196 in²"))
    b.append(eq("F_friction ≈ 0.196 in² × 100 psi ≈ 19.5 lb"))
    b.append(eq("Deadband ≈ ±19.5 lb / 500 in² = ±0.04 psi ≈ 0.6% of span"))
    b.append(p("Dùng than chì làm vật liệu đệm chèn sẽ cho các giá trị cao hơn nhiều lần. Người "
               "ta thường dùng lò xo ép bệ đệm để duy trì ma sát không đổi và bù cho giãn nở "
               "nhiệt cũng như hao mòn về sau."))

    b.append(h3("Đệm chèn thân quay", "Rotary stem packing"))
    b.append(p("Đệm chèn thân quay có ưu điểm. Sự mòn thân do các hạt rắn trong chất lưu — vốn "
               "có thể gây rò rỉ kéo dài ở thân van chuyển động tịnh tiến — được tránh. Thay vì "
               "một lực, ma sát đệm chèn quay tạo ra mô-men xoắn bổ sung."))
    b.append(p("Ví dụ, thân van 1 in có thể có 80 lb ma sát thân. Điều này tương đương 40 in-lb "
               "mô-men xoắn. Giả sử cơ cấu chấp hành quay tạo 100 in-lb mô-men xoắn cho mỗi psi, "
               "sẽ cần 0,4 psi thay đổi tín hiệu."))
    b.append(eq("T = F × r = 80 lb × 0.5 in = 40 in-lb"))
    b.append(eq("Δsignal = 40 in-lb / (100 in-lb/psi) = 0.4 psi"))

    b.append(note("<b>Ghi chú về nguồn.</b> (1) Lớp văn bản OCR có các dấu gạch nối khi xuống "
                  "dòng («hous-ing», «fric-tion»); bản dịch ghép lại thành từ hoàn chỉnh. "
                  "(2) Nguyên bản viết «The first problems can more easily be solved»; bản dịch "
                  "giữ nguyên cấu trúc này và hiểu là nhóm vấn đề thứ nhất, tức mặt ghép thân–"
                  "nắp van. (3) Cụm «longtime leakage problems» và cách viết «spring load "
                  "packing followers» được giữ nguyên trong bản tiếng Anh; bản tiếng Việt dùng "
                  "«rò rỉ kéo dài» và «dùng lò xo ép bệ đệm». (4) Các phép tính lực và mô-men "
                  "được trình bày lại dạng phương trình để làm rõ các giá trị in trong văn bản, "
                  "không thêm dữ liệu mới. (5) Chương này không có hình, bảng hay tài liệu "
                  "tham khảo in trong nguồn."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 16 chiếm các trang in 109–110 của ấn bản in (PDF tr. 112–113). Nguyên bản "
               "gồm một mục duy nhất, «Fugitive Emissions», với hai đoạn mở đầu, hai vị trí rò "
               "rỉ, lời khuyên về gioăng và bulông, lưu ý về bộ lót dạng lồng, nắp van kéo dài, "
               "ma sát đệm chèn và đệm chèn thân quay — tất cả đều được giữ lại."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Khí thải thoát hưu", "Fugitive emissions"))
    b.append(p("Our enhanced concern for a clean air environment has significantly toughened "
               "the allowable amount of emissions of fluids or gases from control valves."))
    b.append(p("Control valves typically have two places of possible leakage:"))
    b.append(ol([
        "The gasket between a valve housing and bolted bonnet or threaded closures to define "
        "a pressure-tight seal",
        "Packing on sliding or rotary valve stems (see Chapter 24)",
    ]))

    b.append(h3("Mặt ghép thân–nắp van và bộ lót dạng lồng",
                "Body–bonnet joints and cage trim"))
    b.append(p("The first problems can more easily be solved by using proper gaskets (flexible "
               "ring gaskets with multiple metal rings interspaced by deformable plastics such "
               "as Teflon are popular). The bolts depressing those gaskets must be strong "
               "enough not only to maintain the maximum fluid pressure but also to deform the "
               "gasket sufficiently to eliminate tiny voids. The minimum bolting load should "
               "be 2.5 times what is required to contain the pressure."))
    b.append(p("Attention must be paid when bonnet flanges simultaneously retain a cage trim. "
               "When the cage material has a higher coefficient of thermal expansion than that "
               "of the housing and hot fluid is encountered, there have been instances where "
               "the cage tried to lift the bonnet from the housing and caused seal leakage."))

    b.append(h3("Nắp van kéo dài", "Extended bonnet"))
    b.append(p("An extended bonnet is always helpful. In the case of liquids, it cools the "
               "temperature of the liquid at the packing. This increases the viscosity and "
               "thus reduces leakage. In the case of steam, a longer bonnet will condense the "
               "steam into water, which again reduces packing leakage. However, this method "
               "only works when a valve is installed upside down; otherwise, the condensed "
               "liquid drains back into the valve housing."))

    b.append(h3("Ma sát đệm chèn và ổn định vòng điều khiển",
                "Packing friction and loop stability"))
    b.append(p("Packing friction can affect the loop stability. Here is a rule of thumb: "
               "Typical stem friction forces due to packing friction can be estimated as the "
               "cross-sectional area of the stem times the inlet pressure."))
    b.append(eq("F_friction ≈ A_stem × P1"))
    b.append(p("For example, a 1/2-inch stem diameter and 100 psi inlet pressure may have a "
               "friction force of 19.5 lb. Using a 500-square-inch diaphragm actuator, this "
               "force could create a deadband of ±0.04 psi, or 0.6% of span, quite tolerable "
               "with a valve positioner. These values are based on a spring-loaded Teflon "
               "V-ring packing."))
    b.append(eq("A_stem = π(0.5 in)² / 4 ≈ 0.196 in²"))
    b.append(eq("F_friction ≈ 0.196 in² × 100 psi ≈ 19.5 lb"))
    b.append(eq("Deadband ≈ ±19.5 lb / 500 in² = ±0.04 psi ≈ 0.6% of span"))
    b.append(p("Using graphite as packing material will produce several times higher values. "
               "It is common to spring load packing followers to achieve constant friction and "
               "to compensate for thermal expansion and future wear."))

    b.append(h3("Đệm chèn thân quay", "Rotary stem packing"))
    b.append(p("Rotary stem packing has advantages. Stem abrasions due to particles in the "
               "fluid, which can lead to longtime leakage problems with reciprocating stems, "
               "are avoided. Instead, for a force, rotary packing friction produces extra "
               "torque."))
    b.append(p("For example, a 1-inch stem may have 80 lb of stem friction. This would "
               "translate into 40 in-lb of torque. Assuming a rotary actuator producing 100 "
               "in-lb of torque per psi, it would require 0.4 psi of signal change."))
    b.append(eq("T = F × r = 80 lb × 0.5 in = 40 in-lb"))
    b.append(eq("Δsignal = 40 in-lb / (100 in-lb/psi) = 0.4 psi"))

    b.append(note("<b>Source note.</b> (1) The OCR text contains line-break hyphenations "
                  "(«hous-ing», «fric-tion»); these have been rejoined. (2) The printed phrase "
                  "«The first problems can more easily be solved» is retained; it refers to the "
                  "first of the two leakage places, the body–bonnet joint. (3) The printed "
                  "«longtime leakage problems» and «spring load packing followers» are kept "
                  "verbatim in this English text. (4) The force and torque arithmetic is "
                  "presented as equations to make the printed numbers explicit; no new source "
                  "data was added. (5) The source chapter has no figures, tables or references."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chapter 16 occupies printed pp. 109–110 of the book (PDF pp. 112–113). The "
               "source has a single section, «Fugitive Emissions», with two opening paragraphs, "
               "two leakage places, advice on gaskets and bolting, a cage-trim caution, "
               "extended bonnets, packing friction and rotary stem packing — all retained."))
    return "".join(b)
