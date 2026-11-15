# -*- coding: utf-8 -*-
"""Book 5, Chapter 1 — Introduction (EN/VI bilingual).

Source: Heikkilä, *Inherent Safety in Process Plant Design — An Index-Based
Approach*, VTT Publications 384 (1999), pp. 11–13, with front matter (Abstract
pp. 3–4, Preface p. 5, List of symbols pp. 9–10) condensed into the chapter's
orientation material.  One editorial vector schematic is drawn in `isdfig.py`.
"""

from isd_common import (eq, fig, h2, h3, note, p, table, ul)
import isdfig as F

PAGES_SRC = 3           # source pages 11–13
BYLINE = "Anna-Mari Heikkilä · VTT Publications 384 (1999)"
TITLE_EN = "Introduction"
TITLE_VI = "Giới thiệu"


# ---- List of symbols (front matter, pp. 9–10) -------------------------------
_SYMBOLS = [
    ("CCA", "Cause-Consequence Analysis", "Phân tích nguyên nhân – hệ quả"),
    ("FMEA", "Failure Modes and Effects Analysis", "Phân tích dạng hỏng và ảnh hưởng"),
    ("ΔHf", "heat of formation", "nhiệt tạo thành"),
    ("ΔHr", "heat of reaction", "nhiệt phản ứng"),
    ("HE", "Hazard Evaluation", "Đánh giá mối nguy"),
    ("HRA", "Human Reliability Analysis", "Phân tích độ tin cậy con người"),
    ("ICI", "Chemical Inherent Safety Index", "Chỉ số an toàn nội tại hóa học"),
    ("ICOR", "Corrosiveness Subindex", "Chỉ số thành phần ăn mòn"),
    ("IEQ", "Equipment Safety Subindex", "Chỉ số thành phần an toàn thiết bị"),
    ("IEX", "Explosiveness Subindex", "Chỉ số thành phần nổ"),
    ("IFL", "Flammability Subindex", "Chỉ số thành phần dễ cháy"),
    ("II", "Inventory Subindex", "Chỉ số thành phần tồn lượng"),
    ("IINT", "Chemical Interaction Subindex", "Chỉ số thành phần tương tác hóa học"),
    ("Ip", "Process Pressure Subindex", "Chỉ số thành phần áp suất quá trình"),
    ("IPI", "Process Inherent Safety Index", "Chỉ số an toàn nội tại quá trình"),
    ("IRM", "Reaction Heat Subindex (main reaction)", "Chỉ số nhiệt phản ứng chính"),
    ("IRS", "Reaction Heat Subindex (side reactions)", "Chỉ số nhiệt phản ứng phụ"),
    ("IST", "Safe Process Structure Subindex", "Chỉ số cấu trúc quá trình an toàn"),
    ("IT", "Process Temperature Subindex", "Chỉ số nhiệt độ quá trình"),
    ("ITI", "Total Inherent Safety Subindex", "Chỉ số an toàn nội tại tổng"),
    ("ITOX", "Toxic Exposure Subindex", "Chỉ số phơi nhiễm độc"),
    ("ISBL", "Inside Battery Limit Area", "Khu vực trong ranh giới pin (ISBL)"),
    ("ISI", "Inherent Safety Index", "Chỉ số An toàn Nội tại"),
    ("LC50", "Lethal Concentration 50%", "Nồng độ gây chết 50%"),
    ("LD50", "Lethal Dose 50%", "Liều gây chết 50%"),
    ("LEL", "Lower Explosion Limit", "Giới hạn nổ dưới"),
    ("OSBL", "Offsite Battery Limit Area", "Khu vực ngoài ranh giới pin (OSBL)"),
    ("PHA", "Preliminary Hazard Analysis", "Phân tích mối nguy sơ bộ"),
    ("PIIS", "Prototype Index of Inherent Safety", "Chỉ số An toàn Nội tại nguyên mẫu"),
    ("TLV", "Threshold Limit Value", "Giá trị giới hạn ngưỡng"),
    ("UEL", "Upper Explosion Limit", "Giới hạn nổ trên"),
    ("ΔUf", "formation energies of reactants and products",
     "năng lượng tạo thành của chất phản ứng và sản phẩm"),
    ("ΔUr", "energy change during the reaction", "độ biến thiên năng lượng trong phản ứng"),
]


def _t_symbols(lang):
    hdr = ["Ký hiệu", "Tiếng Anh", "Nghĩa tiếng Việt"] if lang == "vi" \
        else ["Symbol", "English", "Vietnamese gloss"]
    cap = ("Bảng ký hiệu (tr. 9–10 của nguyên bản) — giữ nguyên ký hiệu gốc, "
           "kèm nghĩa tiếng Việt." if lang == "vi" else
           "List of symbols (source pp. 9–10) — original notation kept, with a "
           "Vietnamese gloss.")
    return table(hdr, _SYMBOLS, caption=cap, cls="tbl wide")


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 1.</b> inherent safety — an toàn nội tại / an toàn "
                "tự thân · external (add-on) safety — an toàn bên ngoài (hệ thống bổ sung) · "
                "hazard — mối nguy · risk — rủi ro · SHE — an toàn, sức khỏe, môi trường · "
                "ISI — Chỉ số An toàn Nội tại · ISBL/OSBL — trong/ngoài ranh giới pin · "
                "conceptual process design — thiết kế quá trình sơ bộ.")
    return ("<b>Key terms.</b> inherent safety — avoiding hazards by the intrinsic "
            "properties of the process · external (add-on) safety — controlling hazards "
            "with protective systems · hazard / risk · SHE — safety, health, environment · "
            "ISI — Inherent Safety Index · ISBL / OSBL — inside / offsite battery limits · "
            "conceptual process design.")


# ---------------------------------------------------------------------------
def body_vi():
    b = []
    b.append(p("Thiết kế quá trình nhằm tạo ra một quá trình có lợi nhuận, kinh tế, "
               "an toàn, thân thiện môi trường và dễ dùng cho người vận hành. Điều đó đạt "
               "được bằng cách tối ưu các phương án quá trình theo tiêu chí kinh tế và "
               "chức năng. An toàn của nhà máy phải đạt một mức bắt buộc nhất định — do yêu "
               "cầu pháp luật, hình ảnh công ty, và cả lý do kinh tế: một nhà máy không an "
               "toàn không thể có lợi nhuận vì mất sản xuất và mất vốn."))

    b.append(h2("An toàn nội tại và an toàn bên ngoài",
                "Inherent safety and external safety"))
    b.append(p("An toàn của một quá trình hóa chất đạt được bằng phương tiện <b>bên trong "
               "(nội tại)</b> và <b>bên ngoài</b>. An toàn nội tại (Kletz, 1984) gắn với các "
               "thuộc tính tự thân của quá trình — ví dụ dùng hóa chất và thao tác an toàn "
               "hơn. Bản chất của an toàn nội tại là <b>tránh và loại bỏ mối nguy</b> thay "
               "vì khống chế chúng bằng các hệ thống bảo vệ lắp thêm, vốn là nguyên lý của "
               "an toàn bên ngoài. Lợi ích lớn nhất có được khi xác nhận rằng an toàn nội "
               "tại đã được xét đến sớm và thường xuyên trong thiết kế quá trình và thiết "
               "kế kỹ thuật (Lutz, 1997)."))
    b.append(p("Khái niệm nhà máy an toàn nội tại hơn đã có từ nhiều năm, nhưng dù tiềm "
               "năng lợi ích rõ ràng về an toàn, sức khỏe, môi trường (SHE) lẫn chi phí, "
               "nó vẫn ít được áp dụng trong thiết kế nhà máy hóa chất. Kletz (1996) chỉ ra "
               "các rào cản: thiết kế an toàn nội tại hơn đòi hỏi một <b>thay đổi cơ bản "
               "trong cách tiếp cận</b> — thay vì giả định rằng ta có thể kiểm soát được "
               "lượng lớn vật liệu nguy hiểm, ta phải tìm cách loại bỏ chúng. Thay đổi niềm "
               "tin và hành động tương ứng không đến dễ dàng."))

    b.append(h2("Thói quen dựa vào hệ thống bổ sung", "The add-on habit"))
    b.append(p("Thái độ truyền thống trong thiết kế nhà máy là dựa nhiều vào các hệ thống "
               "an toàn lắp thêm. Phản ứng của ngành công nghiệp có thể tóm thành hai câu "
               "hỏi (Gowland, 1996): <i>“Làm sao biết quá trình của tôi được thiết kế "
               "theo nguyên lý an toàn nội tại?”</i> và <i>“Có thể đo được ảnh hưởng của "
               "một thay đổi quá trình lên mức an toàn nội tại của nhà máy không?”</i>. "
               "Nhà máy được thiết kế trong tiến độ chặt chẽ, dùng tiêu chuẩn và cái gọi là "
               "thực hành kỹ thuật hợp lý. Lutz (1997) nhận thấy các phương án an toàn nội "
               "tại đã trở thành yêu cầu tại những công ty hiểu rằng nhà máy an toàn nội tại "
               "hơn có chi phí vòng đời thấp hơn, vì vậy có lợi nhuận hơn."))
    b.append(p("Ngành hóa chất nói chung bỏ qua sự giản đơn của việc thiết kế để loại bỏ "
               "mối nguy ngay từ cơ hội đầu tiên. Hệ quả là các biện pháp khống chế được "
               "đưa vào gần <b>điểm cuối</b> của quá trình thiết kế và đầu tư — khi ấy hệ "
               "thống lắp thêm trở thành cơ hội duy nhất cho an toàn quá trình và kiểm soát "
               "ô nhiễm. Những hệ thống thêm muộn này cần nhân sự vận hành và bảo trì liên "
               "tục suốt vòng đời nhà máy, làm tăng đáng kể chi phí vòng đời, cộng thêm đào "
               "tạo lặp đi lặp lại và cập nhật hồ sơ tài liệu."))

    b.append(h2("Các mối nguy liên kết chặt với nhau", "Hazards are inextricably linked"))
    b.append(p("Không có câu trả lời chung cho câu hỏi quá trình nào an toàn nội tại hơn. "
               "Một vấn đề là làm sao giảm thiểu <b>đồng thời</b> rủi ro của mọi mối nguy: "
               "trong thực tế các mối nguy không độc lập mà gắn bó chặt chẽ với nhau "
               "(Hendershot, 1995). Một sửa đổi làm giảm mối nguy này luôn có tác động — "
               "tốt hoặc xấu — lên rủi ro từ mối nguy khác. Ưu và nhược điểm của từng "
               "phương án phải được so sánh cho từng trường hợp cụ thể, dựa trên chi tiết "
               "riêng của quá trình và vật liệu."))
    b.append(p("Ví dụ của Hendershot (1995) là mối lo ngại về tác hại môi trường của "
               "chlorofluorocarbon (CFC). Dễ quên rằng các chất này ban đầu được đưa vào "
               "như những <b>chất thay thế an toàn nội tại hơn</b> cho các môi chất lạnh "
               "nguy hiểm hơn lúc bấy giờ. Dù an toàn nội tại hơn về thiệt hại môi trường "
               "dài hạn, chúng thường nguy hiểm hơn về tính dễ cháy và độc tính cấp."))

    b.append(h2("Thống kê tai nạn: xu hướng tăng", "Accident statistics: a rising trend"))
    b.append(p("Một cách đánh giá hiệu quả của chính sách an toàn hiện hành là nhìn vào "
               "thống kê tai nạn ngành. Theo Anon. (1997), tại Hoa Kỳ đã xảy ra khoảng "
               "<b>23 000</b> tai nạn liên quan hóa chất độc trong giai đoạn 1993–1995 — "
               "trung bình <b>7 700</b> vụ/năm, gây khoảng <b>60</b> ca tử vong và phải "
               "sơ tán <b>41 000</b> người. Giai đoạn 1988–1992 mức trung bình là "
               "<b>6 900</b> vụ/năm: xu hướng đang tăng. Cách tiếp cận truyền thống là "
               "giảm rủi ro dường như chưa đủ, cần những hành động mang tính phòng ngừa "
               "mới như thiết kế nhà máy an toàn nội tại."))
    b.append(table(["Giai đoạn", "Số tai nạn", "Trung bình/năm", "Hệ quả"],
                   [["1988–1992", "—", "6 900", "—"],
                    ["1993–1995", "≈ 23 000", "7 700", "≈ 60 tử vong · 41 000 người sơ tán"]],
                   caption="Tai nạn hóa chất độc tại Hoa Kỳ (Anon., 1997) — số liệu trích "
                           "trực tiếp từ nguyên bản, tr. 12.",
                   cls="tbl"))

    b.append(h2("Mục tiêu của luận văn", "Aim of the thesis"))
    b.append(p("Để đưa an toàn nội tại vào thực hành, cần một phương pháp <b>ước lượng "
               "mức an toàn nội tại</b> của các phương án thiết kế khác nhau. Các chỉ số "
               "Dow và Mond được dùng phổ biến trong công nghiệp hóa chất, nhưng trọng tâm "
               "của chúng chủ yếu là nguy cơ cháy nổ, và thường cần thông tin chi tiết về "
               "quá trình — trong khi ở giai đoạn đầu thiết kế chỉ có rất ít tri thức. "
               "Luận văn này trình bày một <b>Chỉ số An toàn Nội tại</b> (Inherent Safety "
               "Index) để giải quyết bài toán đánh giá an toàn trong giai đoạn thiết kế kỹ "
               "thuật sơ bộ, khi các quyết định lớn về quá trình hóa học còn đang được đưa "
               "ra và chỉ số phải dựa trên tri thức sẵn có ở giai đoạn thiết kế sơ bộ."))
    b.append(p("Theo Tóm tắt (tr. 3–4), chỉ số tổng được chia thành <b>Chỉ số An toàn "
               "Nội tại Hóa học</b> (nhiệt phản ứng, dễ cháy, nổ, độc tính, ăn mòn, tương "
               "tác hóa học) và <b>Chỉ số An toàn Nội tại Quá trình</b> (tồn lượng, nhiệt "
               "độ, áp suất, an toàn thiết bị, cấu trúc quá trình). Chỉ số an toàn thiết "
               "bị được xây dựng từ thống kê tai nạn và dữ liệu bố trí mặt bằng, tách riêng "
               "cho khu vực ISBL và OSBL. Chỉ số cấu trúc quá trình mô tả an toàn theo góc "
               "nhìn kỹ thuật hệ thống, đánh giá bằng suy luận dựa trên tình huống trên cơ "
               "sở dữ liệu các trường hợp thiết kế tốt và xấu — tức kinh nghiệm về cấu hình "
               "quá trình được khuyến nghị và dữ liệu tai nạn — nhờ đó tái sử dụng kinh "
               "nghiệm thiết kế vốn thường bị bỏ qua. Cuối cùng, chỉ số còn được dùng làm "
               "<b>hàm thích nghi</b> trong tối ưu cấu trúc quá trình bằng thuật toán kết "
               "hợp giải thuật di truyền và suy luận dựa trên tình huống, với hai nghiên "
               "cứu tình huống tổng hợp quá trình an toàn hơn."))
    b.append(fig(1, F.fig_isd_intro()))

    b.append(h2("Bảng ký hiệu", "List of symbols"))
    b.append(p("Các ký hiệu dùng xuyên suốt luận văn (tr. 9–10). Ký hiệu gốc được giữ "
               "nguyên để tra cứu chéo với nguyên bản; cột tiếng Việt là giải thích, không "
               "phải thay thế thuật ngữ chuẩn."))
    b.append(_t_symbols("vi"))

    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Công trình được thực hiện tại Phòng thí nghiệm Kỹ thuật Hóa học và Thiết kế "
               "Nhà máy, Đại học Công nghệ Helsinki, từ tháng 4/1993 đến tháng 7/1998 "
               "(Lời tựa, tr. 5); tác giả Anna-Mari Heikkilä, Tampere, tháng 3/1999. "
               "Xuất bản trong loạt VTT Publications 384 của Trung tâm Nghiên cứu Kỹ thuật "
               "Phần Lan, 129 trang, một tệp PDF; từ khóa: an toàn nội tại, thiết kế nhà "
               "máy quá trình, phân tích an toàn, suy luận dựa trên tình huống, giải thuật "
               "di truyền."))
    b.append(note("Ý chính: an toàn nội tại <i>loại bỏ</i> mối nguy bằng lựa chọn hóa chất, "
                  "tồn lượng và cấu trúc quá trình ngay từ thiết kế sơ bộ, thay vì khống chế "
                  "mối nguy bằng hệ thống bảo vệ lắp thêm muộn. Chương này đặt vấn đề và "
                  "mục tiêu của Chỉ số An toàn Nội tại; các chương sau lần lượt rà soát "
                  "phương pháp đánh giá hiện có, xây dựng chỉ số và các chỉ số thành phần, "
                  "rồi áp dụng vào nghiên cứu tình huống và tổng hợp quá trình bằng máy tính."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc "
               "© 1999 Anna-Mari Heikkilä / VTT (VTT Publications 384).</i>"))
    return "".join(b)


# ---------------------------------------------------------------------------
def body_en():
    b = []
    b.append(p("The aim of process design is to create a process which is profitable, "
               "economic, safe, environmentally benign and user friendly. This is achieved "
               "by the optimization of process alternatives according to economic and "
               "functional criteria. It is required that the safety of a process plant "
               "fulfills a certain required level — because of general legal requirements, "
               "company image, and also for economic reasons, since an unsafe plant cannot "
               "be profitable due to losses of production and capital."))

    b.append(h2("Inherent safety and external safety",
                "An toàn nội tại và an toàn bên ngoài"))
    b.append(p("The safety of a chemical process can be achieved through internal "
               "(<b>inherent</b>) and external means. Inherent safety (Kletz, 1984) is "
               "related to the intrinsic properties of the process — e.g. the use of safer "
               "chemicals and operations. The essence of inherent safety is to <b>avoid and "
               "remove hazards</b> rather than to control them by added-on protective "
               "systems, which is the principle of external safety. The largest payoffs are "
               "achieved by verifying that inherent safety has been considered early and "
               "often in the process and engineering design (Lutz, 1997)."))
    b.append(p("The concept of the inherently safer plant has been with us for many years. "
               "But in spite of its clear potential benefits related to safety, health and "
               "the environment (SHE), as well as costs, there have been few applications "
               "in chemical plant design. As Kletz (1996) has written, there are hurdles "
               "to overcome: inherently safer design requires a <b>basic change in "
               "approach</b>. Instead of assuming that we can keep large quantities of "
               "hazardous materials under control, we have to try and remove them. Changes "
               "in belief and the corresponding actions do not come easily."))

    b.append(h2("The add-on habit", "Thói quen dựa vào hệ thống bổ sung"))
    b.append(p("The traditional attitude in plant design is to rely much on added-on "
               "safety systems. Reactions from industry can be expressed by two questions "
               "(Gowland, 1996): <i>“How do I know if my process is designed according to "
               "inherently safe principles?”</i> and <i>“Can the influence of a process "
               "change on the inherent safety of a plant be measured?”</i>. Plants are "
               "designed on a tight time schedule using standards and so-called sound "
               "engineering practice. Lutz (1997) realized that inherent safety "
               "alternatives have become a requirement in companies that understand that "
               "inherently safer plants have lower lifetime costs and therefore are more "
               "profitable."))
    b.append(p("The chemical process industry in general overlooks the simplicity of "
               "designing to eliminate the hazard at the earliest opportunity. The result "
               "is controls being engineered near the <b>end-point</b> of the design and "
               "capitalization process: with this approach add-on systems become the only "
               "opportunities for process safety and pollution control. Systems added late "
               "in design require continual staffing and maintenance throughout the life "
               "of the plant, greatly adding to lifetime costs as well as repetitive "
               "training and documentation upkeep."))

    b.append(h2("Hazards are inextricably linked", "Các mối nguy liên kết chặt với nhau"))
    b.append(p("There is no general answer to the question of which process is inherently "
               "safer. One problem is how to minimize <b>simultaneously</b> the risk "
               "associated with all of the process hazards: in the real world the various "
               "hazards are not independent of each other but are inextricably linked "
               "together (Hendershot, 1995). A process modification which reduces one "
               "hazard will always have some impact, positive or negative, on the risk "
               "resulting from another hazard. The advantages and disadvantages of each "
               "option must be compared for a particular case and the choice made based on "
               "the specific details of the process and materials."))
    b.append(p("Hendershot (1995) points to current concerns about the adverse "
               "environmental effects of chlorofluorocarbons (CFCs). It is easy to forget "
               "that these materials were originally introduced as <b>inherently safer "
               "replacements</b> for the more hazardous refrigerants then in use. While the "
               "alternative materials are inherently safer with respect to long-term "
               "environmental damage, they are often more hazardous with respect to "
               "flammability and acute toxicity."))

    b.append(h2("Accident statistics: a rising trend", "Thống kê tai nạn: xu hướng tăng"))
    b.append(p("One way of assessing the efficiency of existing safety policies is to look "
               "at accident statistics in industry. They show (Anon., 1997) that in the USA "
               "about <b>23,000</b> accidents involving toxic chemicals took place in the "
               "period 1993–1995 — an average of <b>7,700</b> accidents per year — resulting "
               "in about <b>60</b> deaths and the evacuation of <b>41,000</b> people. In "
               "1988–1992 the yearly average was <b>6,900</b> accidents: the trend is "
               "increasing. It seems that the traditional approach of reducing risks is not "
               "enough and new types of actions are needed. This calls for more "
               "preventative strategies such as inherent-safety plant design."))
    b.append(table(["Period", "Accidents", "Yearly average", "Consequences"],
                   [["1988–1992", "—", "6,900", "—"],
                    ["1993–1995", "≈ 23,000", "7,700",
                     "≈ 60 deaths · 41,000 people evacuated"]],
                   caption="Toxic-chemical accidents in the USA (Anon., 1997) — figures as "
                           "quoted in the source, p. 12.",
                   cls="tbl"))

    b.append(h2("Aim of the thesis", "Mục tiêu của luận văn"))
    b.append(p("To implement inherent safety in practice, a method to estimate the "
               "inherent safety of different design alternatives is needed. Methods such "
               "as the Dow and Mond Indices are commonly used in the chemical industry, but "
               "their point is mostly fire and explosion hazards, and they often need "
               "detailed information on the process while at the beginning of design only "
               "scarce knowledge is available. This study presents an <b>Inherent Safety "
               "Index</b> to solve the safety evaluation problems of the conceptual "
               "engineering phase — when the major decisions on the chemical process are "
               "made — built on the knowledge available at the preliminary design stage."))
    b.append(p("Per the Abstract (pp. 3–4), the total index is divided into the "
               "<b>Chemical Inherent Safety Index</b> (reaction heats, flammability, "
               "explosiveness, toxicity, corrosiveness, chemical interaction) and the "
               "<b>Process Inherent Safety Index</b> (inventory, process temperature, "
               "pressure, equipment safety, process structure). The equipment safety "
               "subindex was developed from accident statistics and layout data separately "
               "for ISBL and OSBL areas. The process structure subindex describes safety "
               "from the system engineering point of view, evaluated by case-based "
               "reasoning on a database of good and bad design cases — experience-based "
               "information on recommended process configurations and accident data — "
               "allowing the reuse of existing design experience, which is often "
               "neglected. Finally the index is used as a <b>fitness function</b> in the "
               "optimization of the process structure by an algorithm combining a genetic "
               "algorithm and case-based reasoning, with two case studies on the synthesis "
               "of inherently safer processes."))
    b.append(fig(1, F.fig_isd_intro()))

    b.append(h2("List of symbols", "Bảng ký hiệu"))
    b.append(p("Notation used throughout the thesis (pp. 9–10). The original symbols are "
               "kept verbatim for cross-reference with the source; the Vietnamese column "
               "is a gloss, not a replacement for the standard term."))
    b.append(_t_symbols("en"))

    b.append(h3("About the source", "Về nguồn tài liệu"))
    b.append(p("The work was carried out at the Helsinki University of Technology, "
               "Laboratory of Chemical Engineering and Plant Design, from April 1993 to "
               "July 1998 (Preface, p. 5); the author is Anna-Mari Heikkilä, Tampere, "
               "March 1999. Published as VTT Publications 384 of the Technical Research "
               "Centre of Finland, 129 pages, one PDF file; keywords: inherent safety, "
               "process plant design, safety analysis, case-based reasoning, genetic "
               "algorithm."))
    b.append(note("Central idea: inherent safety <i>removes</i> hazards through the choice "
                  "of chemicals, inventory and process structure at the earliest design "
                  "stage, instead of controlling them with protective systems added late. "
                  "This chapter sets the problem and the aim of the Inherent Safety Index; "
                  "later chapters review existing evaluation methods, build the index and "
                  "its subindices, and apply them to a case study and to computerized "
                  "process synthesis."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 1999 Anna-Mari Heikkilä / VTT (VTT Publications 384).</i>"))
    return "".join(b)
