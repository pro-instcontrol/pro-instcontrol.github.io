# -*- coding: utf-8 -*-
"""ANSI/ISA-5.1 — Chapter 7: Drawings, worked examples (§§6.9–6.12).

This chapter closes the book.  It carries the last 17 vector sheets of the
standard (pages 48–64): eight sheets of function examples, five of
miscellaneous combinations, one complex-combination drawing and the three
simplified / conceptual / detailed diagrams of the degree-of-detail example.
"""
import isa51fig as F
from isa51_common import (T, fig, h2, h3, lead, note, ol, p, quote, refs,
                          table, ul)

PAGES_SRC = 17
BYLINE = "ANSI/ISA-5.1-1984 (R1992) · §§6.9–6.12"

# (clause, heading_vi, heading_en, prose_vi, prose_en, standard pages)
GROUPS = [
    ("6.9", "Ví dụ — các chức năng", "Examples — functions",
     "Tám tờ đầu của phần ví dụ áp dụng <em>từng chức năng riêng lẻ</em> vào một vòng lặp "
     "điển hình: chỉ thị, ghi, điều khiển, trạm điều khiển tay–tự động, báo động cao / thấp, "
     "công tắc và rơ-le interlock, đèn báo, bộ tính toán (cộng, tỷ lệ, tích phân / tổng, "
     "quét, giới hạn), bộ truyền, điểm thử, kính quan sát, thao tác bằng tay, cơ cấu chấp "
     "hành và các tổ hợp đa chức năng. Đây là nơi Bảng 1 (chương 4) và Bảng 2 (chương 5) "
     "«lên hình»: mỗi tổ hợp chữ cái được đặt vào một vòng tròn, trên một đường tín hiệu, "
     "nối tới một phần tử sơ cấp và một van. Đọc mỗi ví dụ bằng cách đi từ số thẻ, qua "
     "ký hiệu vòng tròn, tới đường tín hiệu và phần tử cuối — trình tự đó chính là trình tự "
     "thông tin của vòng lặp.",
     "The first eight example sheets apply <em>one function at a time</em> to a typical "
     "loop: indicating, recording, controlling, auto–manual control stations, high/low "
     "alarms, switches and interlock relays, pilot lights, computing devices (sum, ratio, "
     "integrate/totalize, scan, limiters), transmitters, test points, viewing glasses, "
     "hand operation, drivers and multifunction combinations. This is where Table 1 "
     "(Chapter 4) and Table 2 (Chapter 5) become pictures: each letter combination sits "
     "in a bubble, on a signal line, connected to a primary element and a valve. Read "
     "each example by walking from the tag number through the bubble, along the signal "
     "line and out to the final element — that order is the information flow of the "
     "loop.", list(range(48, 56))),
    ("6.10", "Ví dụ — các tổ hợp khác", "Examples — miscellaneous combinations",
     "Năm tờ tiếp theo xếp cạnh nhau những tổ hợp không thuộc gọn vào một lớp chức năng: "
     "bộ điều khiển logic khả trình (PLC), xả khí / làm sạch bằng khí (purge) và xả khí an "
     "toàn (safety purging), liên kết dữ liệu, các thiết bị dùng chung hiển thị / điều "
     "khiển, và những cách thêm thông tin bằng chú thích cạnh ký hiệu. Điểm đáng chú ý là "
     "hình thoi trong hình vuông (chức năng logic khả trình) được nối trực tiếp với các "
     "tín hiệu nhị phân, trong khi các vòng tròn vẫn giữ quy ước của điều 6.3. Các ví dụ "
     "này cũng minh họa điều 4.4.11: phần cứng interlock trung gian (rơ-le phụ, biến dòng) "
     "có thể được lược bỏ trên sơ đồ luồng kỹ thuật và thể hiện ở tài liệu khác.",
     "Five more sheets place side by side the combinations that do not fit neatly into one "
     "function class: programmable logic controllers (PLC), purge and safety-purging "
     "arrangements, data links, shared display / shared control devices, and the ways of "
     "adding information by notes adjacent to a symbol. Note how the diamond-in-a-square "
     "(programmable logic function) connects directly to binary signals while the bubbles "
     "still follow the clause 6.3 convention. These examples also illustrate clause 4.4.11: "
     "intermediate interlock hardware (auxiliary relays, current transformers) may be "
     "omitted from engineering flow diagrams and shown on another document.",
     list(range(56, 61))),
    ("6.11", "Ví dụ — tổ hợp phức tạp", "Example — complex combinations",
     "Một tờ duy nhất, nhưng là tờ cô đọng nhất của điều 6: một sơ đồ ghép cùng lúc phần "
     "tử sơ cấp, bộ truyền, chức năng tính toán, hiển thị / điều khiển dùng chung, logic "
     "khả trình, interlock nhị phân, cơ cấu chấp hành và trạng thái khi mất nguồn. Nó là "
     "phép thử thực tế cho toàn bộ hệ thống ký hiệu: nếu đọc được tờ này thì đã nắm được "
     "cách các quy tắc ở các chương trước phối hợp với nhau. Tiêu chuẩn khuyến nghị thêm "
     "mũi tên hướng trên các đường tín hiệu ở những bản vẽ phức tạp như thế này (điều "
     "4.4.6) để làm rõ chiều thông tin mà không phụ thuộc vào kiểu đấu dây thật.",
     "A single sheet, but the densest in clause 6: one diagram combining a primary "
     "element, transmitter, computing function, shared display / shared control, "
     "programmable logic, binary interlocks, an actuator and its power-failure state. "
     "It is the practical test of the whole symbol system — if you can read this sheet, "
     "you have seen how the rules of the earlier chapters work together. The standard "
     "recommends directional arrowheads on signal lines in drawings this complex "
     "(clause 4.4.6), to make information flow clear independently of the actual "
     "wiring.", [61]),
    ("6.12", "Ví dụ — mức độ chi tiết", "Example — degree of detail",
     "Ba tờ cuối vẽ <em>cùng một quy trình</em> ở ba mức chi tiết: đơn giản hóa "
     "(simplified), khái niệm (conceptual) và chi tiết (detailed). Đây không phải ba loại "
     "tài liệu khác nhau, mà là một mặt cắt cho thấy cùng một hệ thống ký hiệu có thể co "
     "lại hay mở rộng tùy mục đích — đúng như điều 4.4.10: mức độ chi tiết hoàn toàn do "
     "người dùng quyết định, và điều bắt buộc chỉ là <b>nhất quán trong từng ứng dụng</b>. "
     "Bản đơn giản có thể chỉ còn vài vòng tròn; bản chi tiết lộ ra các thành phần trong "
     "đường ống, điểm thử, chú thích dải tín hiệu và ký hiệu mất nguồn. Khép lại điều 6, "
     "đây cũng là lời nhắc quan trọng nhất: ký hiệu là ngôn ngữ, còn câu văn dài hay ngắn "
     "do người viết chọn.",
     "The final three sheets draw <em>the same process</em> at three levels of detail: "
     "simplified, conceptual and detailed. These are not three different document types "
     "but a cross-section showing that one symbol system can contract or expand to suit "
     "the purpose — exactly as clause 4.4.10 states: the degree of detail is entirely at "
     "the user's discretion, and the only requirement is <b>consistency within each "
     "application</b>. The simplified version may be a handful of bubbles; the detailed "
     "one exposes in-line components, test points, split-range notations and failure "
     "symbols. Closing clause 6, this is also its most important reminder: symbols are "
     "the language, and the writer chooses how long the sentence is.",
     list(range(62, 65))),
]

# The three named diagrams of clause 6.12, for the comparison table.
DETAIL_LEVELS = [
    ("Simplified",
     ("Đơn giản hóa", "Simplified"),
     ("Vài vòng tròn và đường tín hiệu; bỏ hầu hết chi tiết ngoài đường ống.",
      "A few bubbles and signal lines; most off-line detail omitted."),
     ("Phác thảo thiết kế, bài báo kỹ thuật, tài liệu giảng dạy.",
      "Design sketches, technical papers, teaching examples.")),
    ("Conceptual",
     ("Khái niệm", "Conceptual"),
     ("Thể hiện rõ quan hệ chức năng giữa các vòng lặp nhưng chưa liệt kê từng phần tử.",
      "Shows the functional relationships between loops without enumerating every element."),
     ("Sơ đồ luồng quá trình, mô tả chức năng, thuyết minh hệ thống.",
      "Process flow diagrams, functional descriptions, system overviews.")),
    ("Detailed",
     ("Chi tiết", "Detailed"),
     ("Đầy đủ thành phần trong đường ống, điểm thử, chú thích dải tín hiệu, trạng thái mất nguồn.",
      "Full in-line components, test points, split-range notes and power-failure states."),
     ("Sơ đồ luồng kỹ thuật / P&ID, tài liệu xây lắp và đấu nối.",
      "Engineering flow diagrams / P&IDs, construction and loop wiring documents.")),
]


def note_terms(lang):
    return note(T(
        "<b>Thuật ngữ chính của chương.</b> <em>Ví dụ chức năng</em> — một tổ hợp chữ cái "
        "được đặt vào một vòng lặp điển hình. · <em>Tổ hợp phức tạp</em> — sơ đồ ghép "
        "nhiều họ ký hiệu trên cùng một quy trình. · <em>PLC</em> — bộ điều khiển logic "
        "khả trình, ký hiệu hình thoi trong hình vuông. · <em>Purge / safety purging</em> "
        "— xả khí làm sạch / xả khí an toàn. · <em>Mức độ chi tiết</em> — simplified / "
        "conceptual / detailed, do người dùng chọn nhưng phải nhất quán.",
        "<b>Key terms.</b> <em>Function example</em> — one letter combination placed in a "
        "typical loop. · <em>Complex combination</em> — a diagram combining several symbol "
        "families on one process. · <em>PLC</em> — programmable logic controller, the "
        "diamond-in-a-square symbol. · <em>Purge / safety purging</em> — instrument purging "
        "for protection or for safe operation. · <em>Degree of detail</em> — simplified / "
        "conceptual / detailed, user-chosen but required to stay consistent.", lang))


def _build(lang):
    b = []
    A = lambda vi, en: T(vi, en, lang)  # noqa: E731

    # ------------------------------------------------------------------ lead
    b.append(lead(A(
        "Sáu chương trước xây dựng <em>từ vựng</em>: định nghĩa, số thẻ, bảng chữ cái nhận "
        "dạng và 20 tờ ký hiệu. Chương cuối này là phần <em>ngữ pháp</em> — 17 tờ ví dụ "
        "từ trang 48 đến trang 64, nơi các ký hiệu được ghép thành những vòng lặp, sơ đồ "
        "interlock và bản vẽ hoàn chỉnh. Đây cũng là chương được dùng nhiều nhất trong thực "
        "hành: khi cần biết một <code>FRC</code> hay một hình thoi PLC phải vẽ thế nào, "
        "người ta mở điều 6.9–6.12.",
        "The first six chapters built the <em>vocabulary</em>: definitions, tag numbers, "
        "identification letters and 20 symbol sheets. This final chapter is the "
        "<em>grammar</em> — 17 example sheets from page 48 to page 64, where those symbols "
        "are assembled into loops, interlock schemes and complete drawings. It is also the "
        "most-used chapter in practice: when you need to know how an <code>FRC</code> or a "
        "PLC diamond should be drawn, you turn to clauses 6.9–6.12.")))

    # ------------------------------------------------------- how to read them
    b.append(h2(A("Cách đọc các ví dụ", "How to read the examples"),
                A("Những điều tiêu chuẩn dặn trước", "What the standard warns first")))
    b.append(quote(A(
        "«Việc dùng một sơ đồ minh họa nào đó không có nghĩa là ứng dụng hay cách định danh "
        "của thiết bị hoặc chức năng bị giới hạn theo bất kỳ cách nào. Không được suy ra "
        "rằng việc chọn một phương án minh họa là một khuyến nghị cho phương pháp đo hoặc "
        "điều khiển được minh họa.»",
        "«This usage does not imply, however, that the applications or designations of the "
        "instruments or functions are restricted in any way. No inference should be drawn "
        "that the choice of any of the schemes for illustration constitutes a "
        "recommendation for the illustrated methods of measurement or control.»"),
        A("ANSI/ISA-5.1-1984 (R1992), điều 4.4.1",
          "ANSI/ISA-5.1-1984 (R1992), clause 4.4.1")))
    b.append(ol([
        A("<b>Ví dụ không phải khuyến nghị.</b> Nhiều phương án ký hiệu được đưa ra cạnh "
          "nhau mà không nói phương án nào hơn; thứ tự xuất hiện <b>không</b> ngầm định "
          "sự ưu tiên (4.4.1).",
          "<b>Examples are not recommendations.</b> Alternative symbols are shown side by "
          "side without a stated preference; their relative order does <b>not</b> imply "
          "one (4.4.1)."),
        A("<b>Vòng tròn có hai vai trò.</b> Nó có thể đại diện chính thiết bị, hoặc chỉ "
          "làm «nhãn» gắn cạnh một ký hiệu đặc trưng như van điều khiển — khi đó đường "
          "nối vẽ sát nhưng không chạm vào ký hiệu (4.4.2).",
          "<b>The bubble has two roles.</b> It either represents the instrument itself or "
          "acts as a tag attached to a distinctive symbol such as a control valve — in "
          "that case the connecting line is drawn close to, but not touching, the "
          "symbol (4.4.2)."),
        A("<b>Không phải phần tử nào cũng cần số thẻ.</b> Mặt bích lỗ tiết lưu hay van "
          "điều khiển có thể bỏ số thẻ nếu quan hệ của nó với vòng lặp đã rõ trên sơ đồ; "
          "ký hiệu phần tử sơ cấp cũng là tùy chọn (4.4.3).",
          "<b>Not every element needs a tag.</b> An orifice flange or a control valve may "
          "be left untagged when its relationship to the loop is obvious; showing a "
          "primary-element symbol is likewise optional (4.4.3)."),
        A("<b>Chú thích ngắn gỡ bỏ sự mơ hồ.</b> Hai chú thích <em>3–9 psig</em> và "
          "<em>9–15 psig</em> cạnh đường tín hiệu, kết hợp với ký hiệu trạng thái mất "
          "nguồn, làm rõ hoàn toàn ý đồ của cặp van chia dải (4.4.4).",
          "<b>Short notes remove ambiguity.</b> The notations <em>3–9 psig</em> and "
          "<em>9–15 psig</em> beside signal lines, combined with the failure-mode "
          "symbols, fully define a split-range valve pair (4.4.4)."),
        A("<b>Hướng ký hiệu tự do, nhưng chữ phải nằm ngang.</b> Ký hiệu có thể xoay, "
          "đường tín hiệu có thể đi vào / ra ở mọi góc; riêng ký tự khối chức năng Bảng 3 "
          "và số thẻ luôn viết ngang. Nên thêm mũi tên hướng trên bản vẽ phức tạp (4.4.6).",
          "<b>Symbol orientation is free, lettering is not.</b> Symbols may be rotated "
          "and signal lines may enter or leave at any angle; only Table 3 function-block "
          "designators and tag numbers stay horizontal. Directional arrowheads are "
          "recommended on complex drawings (4.4.6)."),
        A("<b>Sơ đồ vẽ logic, không vẽ dây.</b> Thứ tự nối các thiết bị phải phản ánh "
          "luồng thông tin, dù thực tế mạch điện áp đấu song song còn mạch dòng đấu nối "
          "tiếp; cả hai đều vẽ như đấu song song để giữ sơ đồ độc lập với loại thiết bị "
          "sẽ lắp (4.4.9).",
          "<b>Diagrams show logic, not wiring.</b> The connection order must reflect "
          "information flow even though voltage loops are wired in parallel and current "
          "loops in series; both are drawn as parallel so the diagram stays independent "
          "of the installed hardware (4.4.9)."),
        A("<b>Mức độ chi tiết do người dùng chọn.</b> Bản phác thảo thường rất đơn giản, "
          "sơ đồ luồng quá trình ít chi tiết hơn sơ đồ luồng kỹ thuật; điều bắt buộc là "
          "thiết lập sự nhất quán cho từng ứng dụng (4.4.10).",
          "<b>Degree of detail is the user's choice.</b> Sketches are usually highly "
          "simplified and process flow diagrams less detailed than engineering flow "
          "diagrams; what is mandatory is consistency for each application (4.4.10)."),
    ]))

    # ----------------------------------------------------------- clause map
    b.append(table(
        [A("Điều", "Clause"), A("Nội dung", "Subject"),
         A("Trang gốc", "Source pages"), A("Số tờ", "Sheets")],
        [[g[0], g[1] if lang == "vi" else g[2],
          "%d–%d" % (g[5][0], g[5][-1]), str(len(g[5]))] for g in GROUPS],
        A("Bản đồ 17 tờ ví dụ khép lại điều 6.",
          "Map of the 17 example sheets that close clause 6.")))

    # ------------------------------------------------- a worked tag walkthrough
    b.append(h2(A("Đọc một vòng lặp từ số thẻ", "Reading a loop from its tag number"),
                A("Ví dụ có hướng dẫn", "A guided example")))
    b.append(p(A(
        "Trước khi xem các tờ ví dụ, hãy đi qua một vòng lặp điều khiển lưu lượng điển "
        "hình. Bảng dưới lấy lại đúng quy tắc của các chương 3–5: chữ cái đầu là biến đo, "
        "chữ tiếp theo là chức năng, phần số là số vòng lặp, và vị trí của vòng tròn trên "
        "bản vẽ nói lên nơi thiết bị được lắp.",
        "Before the sheets, walk through one typical flow-control loop. The table below "
        "reuses exactly the rules of Chapters 3–5: the first letter is the measured "
        "variable, succeeding letters are the functions, the numeric part is the loop "
        "number, and the position of the bubble on the drawing tells you where the "
        "device is mounted.")))
    b.append(table(
        [A("Số thẻ", "Tag"), A("Đọc là", "Read as"), A("Ký hiệu trên bản vẽ", "Symbol on drawing")],
        [
            ["FE-1",
             A("E = phần tử sơ cấp, F = lưu lượng", "E = primary element, F = flow"),
             A("Lỗ tiết lưu trên đường ống; có thể không cần vòng tròn riêng (4.4.3).",
               "Orifice plate in the process line; a separate bubble is optional (4.4.3).")],
            ["FT-1",
             A("T = bộ truyền, F = lưu lượng", "T = transmitter, F = flow"),
             A("Vòng tròn đơn tại hiện trường (không có vạch ngang), nối bằng đường tín hiệu mảnh.",
               "Plain field-mounted circle (no horizontal bar), joined by a fine signal line.")],
            ["FRC-1",
             A("R = ghi, C = điều khiển, F = lưu lượng", "R = record, C = control, F = flow"),
             A("Vòng tròn có vạch ngang tại vị trí chính, người vận hành truy cập được (6.3).",
               "Circle with a horizontal bar at the primary location, accessible to the operator (6.3).")],
            ["FAL-1 / FAH-1",
             A("A = báo động, L / H = thấp / cao", "A = alarm, L / H = low / high"),
             A("Chữ L / H viết cạnh vòng tròn; đèn báo dùng ký hiệu riêng của điều 6.3.",
               "L / H written beside the bubble; the pilot light uses its own clause 6.3 symbol.")],
            ["FV-1",
             A("V = van, F = lưu lượng", "V = valve, F = flow"),
             A("Thân van (6.4) + cơ cấu chấp hành (6.5) + ký hiệu FC / FO khi mất nguồn (6.7).",
               "Valve body (6.4) + actuator (6.5) + an FC / FO failure symbol (6.7).")],
        ],
        A("Một vòng lặp FRC-1 đọc theo trình tự thông tin, không theo trình tự đấu dây.",
          "An FRC-1 loop read in information-flow order rather than wiring order.")))
    b.append(note(A(
        "<b>Mẹo đọc tờ ví dụ.</b> Đi từ trái sang phải theo chiều mũi tên: phần tử sơ cấp "
        "→ bộ truyền → chức năng (vòng tròn) → cơ cấu chấp hành. Khi thấy một vòng tròn "
        "trong hình vuông, một hình lục giác hay một hình thoi, hãy quay lại bảng 3×4 của "
        "chương 6 để xác định đó là chức năng máy tính, điều khiển dùng chung hay logic "
        "khả trình.",
        "<b>Reading tip.</b> Follow the arrowheads left to right: primary element → "
        "transmitter → function (bubble) → final actuator. Whenever you meet a circle "
        "inside a square, a hexagon or a diamond, go back to the 3×4 matrix in Chapter 6 "
        "to decide whether it is a computer function, shared control or programmable "
        "logic.")))

    # ------------------------------------------------------------ all 17 sheets
    n = 0
    for clause, h_vi, h_en, s_vi, s_en, pages in GROUPS:
        b.append(h2(A("%s · %s" % (clause, h_vi), "%s · %s" % (clause, h_en)),
                    A("Tờ ví dụ của tiêu chuẩn", "The standard's example sheets")))
        b.append(p(A(s_vi, s_en)))
        for pg in pages:
            n += 1
            b.append(h3(A("Tờ %d · trang %d của tiêu chuẩn" % (n, pg),
                          "Sheet %d · standard page %d" % (n, pg))))
            b.append(fig(n, F.sheet(pg)))

    # ------------------------------------------------------ degree of detail
    b.append(h2(A("6.12 · Ba mức độ chi tiết", "6.12 · Three levels of detail"),
                A("Cùng một quy trình, ba cách viết", "One process, three renderings")))
    b.append(table(
        [A("Tên trong tiêu chuẩn", "Standard term"), A("Mức chi tiết", "Level of detail"),
         A("Dùng cho", "Typical use")],
        [[d[1][0] if lang == "vi" else d[1][1],
          d[2][0] if lang == "vi" else d[2][1],
          d[3][0] if lang == "vi" else d[3][1]] for d in DETAIL_LEVELS],
        A("Theo điều 4.4.10 và các tờ 62–64; ba tên này chỉ là một mặt cắt cách dùng ký hiệu, "
          "không phải ba loại tài liệu bắt buộc.",
          "From clause 4.4.10 and sheets 62–64; these three names represent a cross-section "
          "of symbol usage, not three mandatory document types.")))
    b.append(ul([
        A("Ba tờ 62–64 vẽ cùng một quy trình, nên sự khác biệt giữa chúng <b>chỉ là mức "
          "độ chi tiết</b>, không phải khác biệt về thiết bị hay sơ đồ công nghệ.",
          "Sheets 62–64 depict the same process, so the difference between them is "
          "<b>only the level of detail</b>, not a difference in equipment or process "
          "scheme."),
        A("Tiêu chuẩn không quy định bản vẽ nào «phải» chi tiết đến đâu; mỗi người dùng "
          "tự thiết lập mức phù hợp với mục đích tài liệu, rồi giữ nguyên mức đó trong "
          "suốt bộ tài liệu.",
          "The standard does not prescribe how detailed any particular drawing must be; "
          "each user sets the level suited to the document's purpose and then holds it "
          "steady across the document set."),
        A("Đây là lý do các tờ ví dụ của điều 6.9–6.11 nên được đọc như <em>cách dùng</em> "
          "ký hiệu, không phải như mẫu bản vẽ bắt buộc phải sao chép.",
          "This is why the example sheets of 6.9–6.11 should be read as <em>usage</em> "
          "demonstrations rather than templates that must be copied."),
    ]))

    # ------------------------------------------------------------- wrap-up
    b.append(h2(A("Khép lại bộ tiêu chuẩn", "Closing the standard"),
                A("Từ chữ cái đến bản vẽ hoàn chỉnh", "From letters to a complete drawing")))
    b.append(p(A(
        "Bảy chương của cuốn sách đi theo một đường thẳng: mục đích và phạm vi (chương 1) "
        "→ định nghĩa (chương 2) → cấu trúc số thẻ (chương 3) → bảng chữ cái nhận dạng "
        "(chương 4) → tổ hợp chữ cái và khối chức năng (chương 5) → 20 tờ ký hiệu "
        "(chương 6) → 17 tờ ví dụ (chương này). Cộng thêm 4 tờ khối chức năng Bảng 3 ở "
        "chương 5, toàn bộ <b>41 tờ vector</b> của phần 5.4 và điều 6 đã được tái tạo "
        "nguyên vẹn, cùng 2 hình vẽ lại cho Hình 1 và sáu khối SAMA cơ bản.",
        "The book's seven chapters follow one line: purpose and scope (Chapter 1) → "
        "definitions (Chapter 2) → tag-number structure (Chapter 3) → identification "
        "letters (Chapter 4) → letter combinations and function blocks (Chapter 5) → "
        "20 symbol sheets (Chapter 6) → the 17 example sheets here. With the four "
        "Table 3 function-block sheets in Chapter 5, all <b>41 vector sheets</b> of "
        "clauses 5.4 and 6 are reproduced in full, plus two redrawn figures for Figure 1 "
        "and the six core SAMA blocks.")))
    b.append(refs([
        A("Điều 3 — Định nghĩa: xem <a href=\"../ch02-definitions/\">chương 2</a>.",
          "Clause 3 — Definitions: see <a href=\"../ch02-definitions/\">Chapter 2</a>."),
        A("Điều 4 — Hệ thống nhận dạng và Hình 1: xem <a href=\"../ch03-identification-system/\">chương 3</a>.",
          "Clause 4 — Identification system and Figure 1: see <a href=\"../ch03-identification-system/\">Chapter 3</a>."),
        A("Điều 5.1 — Bảng 1 chữ cái nhận dạng và 22 chú thích: xem <a href=\"../ch04-identification-letters/\">chương 4</a>.",
          "Clause 5.1 — Table 1 identification letters and its 22 notes: see <a href=\"../ch04-identification-letters/\">Chapter 4</a>."),
        A("Điều 5.2–5.4 — Bảng 2, Bảng 3 và khối chức năng SAMA: xem <a href=\"../ch05-letter-combinations-function-blocks/\">chương 5</a>.",
          "Clauses 5.2–5.4 — Tables 2 and 3 and SAMA function blocks: see <a href=\"../ch05-letter-combinations-function-blocks/\">Chapter 5</a>."),
        A("Điều 6.1–6.8 — 20 tờ ký hiệu đường, vòng tròn, van, cơ cấu chấp hành và phần "
          "tử sơ cấp: xem <a href=\"../ch06-instrument-symbols/\">chương 6</a>.",
          "Clauses 6.1–6.8 — 20 sheets of line, bubble, valve, actuator and primary-element "
          "symbols: see <a href=\"../ch06-instrument-symbols/\">Chapter 6</a>."),
    ]))
    b.append(note(A(
        "<b>Về bản tái tạo.</b> Các tờ ví dụ trong bản PDF gốc không có lớp văn bản — mọi "
        "đường nét và nhãn đều là lệnh vẽ vector. Mỗi tờ ở đây được phát lại trực tiếp "
        "thành <code>&lt;path&gt;</code> SVG, giữ nguyên bố cục và nhãn tiếng Anh gốc của "
        "tiêu chuẩn; chú thích tiếng Việt đi kèm giải thích nội dung. Bản dịch tiếng Việt "
        "trình bày toàn bộ văn bản quy phạm, còn nhãn trên hình được giữ nguyên để người "
        "đọc đối chiếu được với bản gốc ANSI/ISA-5.1-1984 (R1992).",
        "<b>About this reproduction.</b> The example sheets in the source PDF have no "
        "text layer — every line and label is a vector drawing operator. Each sheet here "
        "is replayed directly as SVG <code>&lt;path&gt;</code> elements, preserving the "
        "standard's layout and its original English labels; the paired Vietnamese "
        "caption explains the content. The Vietnamese translation renders the full "
        "normative prose, while labels inside the figures are kept verbatim so readers "
        "can check them against ANSI/ISA-5.1-1984 (R1992).")))
    return "".join(b)


def body_vi():
    return _build("vi")


def body_en():
    return _build("en")
