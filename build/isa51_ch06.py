# -*- coding: utf-8 -*-
"""ANSI/ISA-5.1 — Chapter 6: Drawings, instrument and function symbols (§§6.1–6.8)."""
import isa51fig as F
from isa51_common import T, fig, h2, h3, lead, note, ol, p, table, ul

PAGES_SRC = 21
BYLINE = "ANSI/ISA-5.1-1984 (R1992) · §6.1–6.8"

# (section, Vietnamese heading, English heading, Vietnamese prose, English prose, pages)
GROUPS = [
    ("6.2", "Ký hiệu đường tín hiệu", "Instrument line symbols",
     "Điều 6.2 định nghĩa mười hai kiểu đường nối, phân biệt nguồn cấp, tín hiệu khí nén, "
     "thủy lực, điện, mao dẫn, sóng điện từ/âm (dẫn hướng và không dẫn hướng), liên kết nội "
     "bộ hệ thống (phần mềm / liên kết dữ liệu), liên kết cơ khí, và hai kiểu tín hiệu nhị "
     "phân. Mọi đường tín hiệu phải vẽ <b>mảnh hơn đường ống công nghệ</b>. Người dùng được "
     "chọn giữa đường đứt nét và ký hiệu gạch chéo ba cho tín hiệu điện, nhưng phải dùng "
     "nhất quán trong một bộ tài liệu; dấu gạch chéo ngược trên đường tín hiệu nhị phân là "
     "tùy chọn và có thể bỏ nếu không cần phân biệt tương tự / nhị phân. Các chữ viết tắt "
     "AS, IA, PA, ES, GS, HS, NS, SS, WS chỉ rõ loại nguồn cấp.",
     "Clause 6.2 defines twelve line types distinguishing instrument supply, pneumatic, "
     "hydraulic, electric, capillary, electromagnetic/sonic (guided and unguided), internal "
     "system link (software/data link), mechanical link and two binary signal forms. All "
     "instrument lines are to be <b>fine in relation to process piping lines</b>. The user "
     "may choose either the dashed line or the triple cross-hatch for the electrical symbol, "
     "but must apply it consistently across a document set; the reverse slash on binary "
     "(on-off) signal lines is optional and may be omitted where analog/binary "
     "differentiation is unnecessary. Abbreviations AS, IA, PA, ES, GS, HS, NS, SS and WS "
     "identify the supply type.", [28]),
    ("6.3", "Ký hiệu chung cho thiết bị hoặc chức năng", "General instrument or function symbols",
     "Bảng 3×4 nổi tiếng nhất của tiêu chuẩn: bốn họ thiết bị (thiết bị rời rạc; hiển thị / "
     "điều khiển dùng chung; chức năng máy tính; điều khiển logic khả trình) × ba vị trí lắp "
     "đặt (vị trí chính, người vận hành thường truy cập được; lắp tại hiện trường; vị trí "
     "phụ, thường không truy cập được). Vòng tròn trơn, vòng tròn có một hoặc hai vạch ngang, "
     "vòng tròn trong hình vuông, hình lục giác, hình thoi trong hình vuông — mỗi biến thể "
     "mang một ý nghĩa riêng. Trang tiếp theo của điều 6.3 liệt kê các biến thể và ký hiệu "
     "bổ sung. Kích thước vòng tròn có thể thay đổi theo nhu cầu nhưng nên giữ nhất quán; "
     "thiết bị không truy cập được thường xuyên có thể vẽ bằng cùng ký hiệu với vạch ngang "
     "đứt nét.",
     "The standard's best-known 3×4 matrix: four device families (discrete instruments; "
     "shared display / shared control; computer function; programmable logic control) × "
     "three locations (primary, normally accessible to the operator; field mounted; "
     "auxiliary, normally not accessible). Plain circle, circle with one or two horizontal "
     "bars, circle inside a square, hexagon, diamond inside a square — each variant carries "
     "its own meaning. The continuation sheet lists further variants and additional symbols. "
     "Symbol size may vary with the document but should stay consistent; normally "
     "inaccessible or behind-panel devices may use the same symbol with dashed horizontal "
     "bars.", [29, 30]),
    ("6.4", "Ký hiệu thân van điều khiển và cánh chắn", "Control valve body symbols, damper symbols",
     "Mười hai ô mô tả thân van: ký hiệu chung (hai tam giác đối nhau), van góc, van bướm, "
     "van quay, van ba ngả, van bốn ngả, van cầu (globe), van màng, và ba kiểu cánh chắn / "
     "cánh gió (damper, louver). Thông tin bổ sung có thể ghi cạnh ký hiệu thân van bằng chú "
     "thích hoặc số hiệu ghi chú, chứ không nhồi vào bản thân ký hiệu.",
     "Twelve cells describe valve bodies: the general symbol (two opposed triangles), angle, "
     "butterfly, rotary valve, three-way, four-way, globe, diaphragm and three damper/louver "
     "forms. Further information may be added adjacent to the body symbol by note or note "
     "number rather than packed into the symbol itself.", [31]),
    ("6.5", "Ký hiệu cơ cấu chấp hành", "Actuator symbols",
     "Hai tờ ký hiệu cho cơ cấu chấp hành: màng ngăn (diaphragm), piston, xi lanh, động cơ "
     "điện, cơ cấu quay, cơ cấu tự lực, bộ định vị, công tắc hành trình, van điện từ và các "
     "tổ hợp của chúng. Ký hiệu cơ cấu chấp hành được vẽ nối với ký hiệu thân van ở điều "
     "6.4; khi cần, ghi rõ kiểu tác động bằng ký hiệu ở điều 6.7.",
     "Two sheets cover actuators: diaphragm, piston, cylinder, electric motor, rotary "
     "actuator, self-actuated device, positioner, limit switch, solenoid valve and their "
     "combinations. Actuator symbols attach to the valve-body symbols of clause 6.4; where "
     "needed, the failure action is stated with the clause 6.7 symbols.", [32, 33]),
    ("6.6", "Bộ điều chỉnh tự lực, van và thiết bị khác", "Self-actuated regulators, valves and other devices",
     "Ba tờ ký hiệu cho các thiết bị không cần tín hiệu điều khiển từ bên ngoài: van giảm áp, "
     "van chống áp ngược, bẫy hơi, van một chiều, van xả an toàn / đĩa vỡ, bộ điều chỉnh "
     "lưu lượng tự lực, ống Venturi, ejector và các phần tử tương tự. Đây cũng là nơi phân "
     "biệt <b>PCV</b> (van điều khiển tự lực, chú thích 8 của Bảng 1) với <b>PSV</b> (van "
     "bảo vệ khẩn cấp).",
     "Three sheets cover devices needing no external control signal: pressure-reducing and "
     "back-pressure regulators, steam traps, check valves, safety/relief valves and rupture "
     "discs, self-actuated flow regulators, venturis, ejectors and similar elements. This is "
     "also where <b>PCV</b> (a self-actuated control valve, Table 1 note 8) is distinguished "
     "from <b>PSV</b> (emergency protective valve).", [34, 35, 36]),
    ("6.7", "Trạng thái khi mất nguồn cơ cấu chấp hành", "Actuator action on power failure",
     "Một tờ ký hiệu (vẽ điển hình cho van điều khiển màng ngăn) biểu diễn ba khả năng: "
     "<b>FO</b> mở khi mất nguồn (fail open), <b>FC</b> đóng khi mất nguồn (fail closed), "
     "và <b>FL</b> giữ nguyên vị trí cuối (fail last / lock in place). Các ký hiệu này kết "
     "hợp với chú thích dải tín hiệu ở điều 4.4.4 (3–9 psig / 9–15 psig) để làm rõ hoàn "
     "toàn ý đồ của van chia dải.",
     "One sheet (drawn typically for a diaphragm-actuated control valve) shows the three "
     "possibilities: <b>FO</b> fail open, <b>FC</b> fail closed and <b>FL</b> fail last / "
     "lock in place. Combined with the split-range notations of clause 4.4.4 (3–9 psig / "
     "9–15 psig), these symbols make the valve intent completely unambiguous.", [37]),
    ("6.8", "Ký hiệu phần tử sơ cấp", "Primary element symbols",
     "Mười tờ liên tiếp — phần lớn nhất của điều 6 — liệt kê ký hiệu phần tử sơ cấp theo "
     "từng phép đo: lỗ tiết lưu, ống Venturi, vòi phun, ống Pitot, cánh khuấy, đồng hồ tuabin, "
     "đo từ, đo siêu âm, đo Coriolis; cảm biến nhiệt độ (cặp nhiệt điện, RTD, ống bảo vệ), "
     "áp suất (màng, ống Bourdon), mức (phao, radar, điện dung, trọng lực), phân tích (điện "
     "cực pH, dẫn suất, sắc ký), tốc độ / dao động, và các điểm thử. Mỗi tờ được tái tạo "
     "nguyên vẹn ở đây dưới dạng vector.",
     "Ten consecutive sheets — the largest block of clause 6 — list primary-element symbols "
     "by measurement: orifice plate, venturi, flow nozzle, Pitot tube, target/turbine meters, "
     "magnetic, ultrasonic and Coriolis flowmeters; temperature (thermocouple, RTD, "
     "thermowell), pressure (diaphragm, Bourdon), level (float, radar, capacitance, "
     "displacement), analysis (pH electrode, conductivity, chromatograph), speed/vibration "
     "and test points. Every sheet is reproduced in full here as a vector.", list(range(38, 48))),
]


def note_terms(lang):
    return note(T(
        "<b>Thuật ngữ chính của chương.</b> <em>Đường tín hiệu</em> — nối các thiết bị trong "
        "vòng lặp, luôn mảnh hơn đường ống công nghệ. · <em>Bubble</em> — vòng tròn ký hiệu "
        "thiết bị / chức năng. · <em>FO / FC / FL</em> — trạng thái van khi mất nguồn: mở, "
        "đóng, giữ nguyên. · <em>Phần tử sơ cấp</em> — cảm biến đầu tiên cảm nhận biến quá "
        "trình. · <em>Damper / louver</em> — cánh chắn, cánh gió.",
        "<b>Key terms.</b> <em>Signal line</em> — links instruments in a loop, always fine "
        "relative to process piping. · <em>Bubble</em> — the circular instrument/function "
        "symbol. · <em>FO / FC / FL</em> — valve state on power failure: open, closed, last "
        "position. · <em>Primary element</em> — the first sensor to sense the process "
        "variable. · <em>Damper / louver</em> — flow-control plates in ducts.", lang))


def _build(lang):
    b = []
    A = lambda vi, en: T(vi, en, lang)  # noqa: E731

    b.append(lead(A(
        "Điều 6 là <em>phần nhìn thấy được</em> của tiêu chuẩn: 37 tờ ký hiệu trải dài từ "
        "trang 28 đến trang 64. Chương này tái tạo 20 tờ đầu (các điều 6.2–6.8) — ký hiệu "
        "đường, vòng tròn thiết bị, thân van, cơ cấu chấp hành, thiết bị tự lực và phần tử "
        "sơ cấp. Chương 7 sẽ đưa 17 tờ ví dụ còn lại.",
        "Clause 6 is the <em>visible part</em> of the standard: 37 symbol sheets spanning "
        "pages 28 to 64. This chapter reproduces the first 20 (clauses 6.2–6.8) — line "
        "symbols, instrument bubbles, valve bodies, actuators, self-actuated devices and "
        "primary elements. Chapter 7 carries the remaining 17 example sheets.")))

    b.append(h2(A("6.1 · Lưu ý trước khi dùng ký hiệu", "6.1 · Cautionary notes"),
                A("Ba cảnh báo của tiêu chuẩn", "Three warnings from the standard")))
    b.append(ol([
        A("Nếu một bản vẽ (hay bộ bản vẽ) dùng các ký hiệu giống hệt hoặc gần giống nhau "
          "nhưng <em>khác nghĩa</em> vì lấy từ những tiêu chuẩn khác nhau, phải có biện pháp "
          "tránh hiểu nhầm: ghi chú cảnh báo, chú thích tham chiếu, bảng so sánh định nghĩa "
          "các ký hiệu xung đột, hoặc cách phù hợp khác. Yêu cầu này đặc biệt quan trọng khi "
          "ký hiệu của nhiều chuyên ngành trộn lẫn mà hiểu nhầm có thể gây nguy hiểm cho "
          "người hoặc hư hỏng thiết bị.",
          "If a drawing or set of drawings uses graphic symbols that are similar or identical "
          "in shape but have <em>different meanings</em> because they come from different "
          "standards, adequate steps must be taken to avoid misinterpretation: caution "
          "notes, reference notes, comparison charts defining the conflicting symbols, or "
          "other suitable means. This is especially critical where symbols from different "
          "disciplines are intermixed and misinterpretation might endanger personnel or "
          "damage equipment."),
        A("Các tên <em>Simplified Diagrams</em>, <em>Conceptual Diagrams</em> và "
          "<em>Detailed Diagrams</em> ở điều 6.12 được chọn để đại diện cho một mặt cắt cách "
          "dùng ký hiệu, <b>không</b> đại diện cho một loại tài liệu cụ thể nào (xem thêm "
          "điều 4.4.10).",
          "The titles Simplified Diagrams, Conceptual Diagrams and Detailed Diagrams in "
          "clause 6.12 were chosen to represent a cross-section of symbol usage, <b>not</b> "
          "any particular generic document (see also clause 4.4.10)."),
        A("Các ký hiệu đường ở điều 6.2 có phương án điện «tùy chọn người dùng» và ký hiệu "
          "nhị phân tùy chọn. Các ví dụ về sau dùng <em>một bộ nhất quán</em> và áp dụng "
          "tùy chọn nhị phân để đồng nhất hình thức của tiêu chuẩn. Người dùng nên chọn hoặc "
          "đường đứt nét hoặc gạch chéo ba, rồi dùng nhất quán; dấu gạch chéo ngược có thể "
          "bỏ nếu không cần phân biệt tương tự / nhị phân.",
          "The clause 6.2 line symbols offer «user's choice» electrical alternatives and "
          "optional binary symbols. The examples that follow use <em>one consistent set</em> "
          "and apply the binary options for consistency of appearance. The user should "
          "choose either the dashed line or the triple cross-hatch and apply it "
          "consistently; the reverse slash may be omitted where analog/binary "
          "differentiation is not required."),
    ]))

    b.append(table(
        [A("Điều", "Clause"), A("Nội dung", "Subject"), A("Trang gốc", "Source pages"),
         A("Số tờ", "Sheets")],
        [[g[0], g[1] if lang == "vi" else g[2],
          "%d–%d" % (g[5][0], g[5][-1]), str(len(g[5]))] for g in GROUPS],
        A("Bản đồ 20 tờ ký hiệu trong chương này.",
          "Map of the 20 symbol sheets in this chapter.")))

    n = 0
    for clause, h_vi, h_en, s_vi, s_en, pages in GROUPS:
        b.append(h2(A("%s · %s" % (clause, h_vi), "%s · %s" % (clause, h_en)),
                    A("Tờ ký hiệu của tiêu chuẩn", "The standard's sheets")))
        b.append(p(A(s_vi, s_en)))
        for pg in pages:
            n += 1
            b.append(fig(n, F.sheet(pg)))

    b.append(h2(A("Cách các tờ ký hiệu được tái tạo", "How these sheets were reproduced"),
                A("Vector, không phải ảnh chụp", "Vectors, not screenshots")))
    b.append(p(A(
        "Các tờ ký hiệu trong bản PDF gốc <b>không có lớp văn bản</b>: mọi đường nét lẫn chữ "
        "đều là lệnh vẽ vector. Vì vậy mỗi tờ ở đây được tạo bằng cách đọc trực tiếp các lệnh "
        "vẽ của PDF và phát lại dưới dạng <code>&lt;path&gt;</code> SVG — giữ nguyên bố cục, "
        "nét vẽ và nhãn tiếng Anh gốc của tiêu chuẩn, nhưng phóng to hay thu nhỏ đều không "
        "bị vỡ hạt. Chú thích tiếng Việt đi kèm từng hình giải thích nội dung tờ ký hiệu.",
        "The source PDF's drawing sheets have <b>no text layer</b>: every line and every "
        "label is a vector path. Each sheet here is therefore produced by reading the PDF's "
        "drawing operators directly and replaying them as SVG <code>&lt;path&gt;</code> "
        "elements — preserving the standard's layout, linework and original English labels, "
        "while staying sharp at any zoom. The accompanying Vietnamese caption explains what "
        "each sheet contains.")))
    return "".join(b)


def body_vi():
    return _build("vi")


def body_en():
    return _build("en")
