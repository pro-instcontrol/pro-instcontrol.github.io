# -*- coding: utf-8 -*-
"""ANSI/ISA-5.1 — Chapter 3: Outline of the identification system (§4).

Carries the standard's only numbered illustration, Figure 1 — Tag numbers,
redrawn here as a bilingual vector diagram.
"""
import isa51fig as F
from isa51_common import T, fig, h2, h3, lead, note, ol, p, table, ul

PAGES_SRC = 4
BYLINE = "ANSI/ISA-5.1-1984 (R1992) · §4"


def note_terms(lang):
    return note(T(
        "<b>Thuật ngữ chính của chương.</b> <em>Số thẻ (tag number)</em> — mã chữ-số nhận "
        "dạng một thiết bị. · <em>Nhận dạng chức năng</em> — phần chữ cái, gồm một chữ đầu và "
        "các chữ tiếp theo. · <em>Nhận dạng vòng lặp</em> — chữ cái đầu kèm số vòng lặp. · "
        "<em>Chữ bổ nghĩa</em> — D (vi phân), F (tỷ lệ), Q (tích phân), K (tốc độ thay đổi), "
        "H/L/M (cao/thấp/trung gian).",
        "<b>Key terms.</b> <em>Tag number</em> — the alphanumeric code identifying one "
        "instrument. · <em>Functional identification</em> — the letter group, one first-letter "
        "plus succeeding-letters. · <em>Loop identification</em> — a first-letter plus a loop "
        "number. · <em>Modifying letters</em> — D (differential), F (ratio), Q (integrate), "
        "K (rate of change), H/L/M (high/low/middle).", lang))


def _build(lang):
    b = []
    A = lambda vi, en: T(vi, en, lang)  # noqa: E731

    b.append(lead(A(
        "Điều 4 là <em>xương sống</em> của toàn bộ tiêu chuẩn: nó giải thích số thẻ được ghép "
        "như thế nào, chữ cái nhận dạng chọn theo nguyên tắc gì, vòng lặp được đánh số ra sao "
        "và ký hiệu được dùng trên bản vẽ như thế nào.",
        "Clause 4 is the <em>backbone</em> of the whole standard: it explains how a tag number "
        "is assembled, how identification letters are chosen, how loops are numbered and how "
        "symbols are used on drawings.")))

    b.append(h2(A("4.1 · Khái quát", "4.1 · General"),
                A("Số thẻ và cấu trúc của nó", "The tag number and its parts")))
    b.append(p(A(
        "Mỗi thiết bị hoặc chức năng cần nhận dạng được chỉ định bằng một <b>mã chữ-số</b> hay "
        "<b>số thẻ</b> như Hình 1. Phần nhận dạng vòng lặp của số thẻ thường dùng chung cho "
        "mọi thiết bị/chức năng trong cùng vòng lặp. Có thể thêm <em>tiền tố</em> hoặc "
        "<em>hậu tố</em> để hoàn chỉnh nhận dạng.",
        "Each instrument or function to be identified is designated by an <b>alphanumeric code "
        "or tag number</b> as shown in Figure 1. The loop-identification part of the tag number "
        "is generally common to all instruments or functions of the loop. A <em>prefix</em> or "
        "<em>suffix</em> may be added to complete the identification.")))
    b.append(fig(1, F.fig_tag_numbers()))
    b.append(p(A(
        "<b>TIC 103</b> đọc được thành: <b>T</b> = biến đo (nhiệt độ), <b>IC</b> = chỉ thị và "
        "điều khiển, <b>103</b> = số vòng lặp. Ở dạng mở rộng, <b>10-PAH-5A</b> có tiền tố "
        "<b>10</b> (mã khu vực/chủng loại), nhận dạng chức năng <b>PAH</b> (báo động áp suất "
        "cao), số vòng lặp <b>5</b> và hậu tố tùy chọn <b>A</b>. Dấu gạch nối chỉ là dấu "
        "phân cách, không bắt buộc.",
        "<b>TIC 103</b> parses as: <b>T</b> = measured variable (temperature), <b>IC</b> = "
        "indicating and control, <b>103</b> = loop number. In expanded form, <b>10-PAH-5A</b> "
        "has prefix <b>10</b> (area/type code), functional identification <b>PAH</b> (high "
        "pressure alarm), loop number <b>5</b> and optional suffix <b>A</b>. Hyphens are "
        "optional separators.")))
    b.append(ul([
        A("<b>4.1.2</b> · Số vòng lặp có thể mang thông tin mã hóa, ví dụ ký hiệu khu vực "
          "nhà máy. Cũng có thể dành riêng một dãy số cho chức năng đặc biệt — chẳng hạn dãy "
          "<b>900–999</b> cho các vòng lặp có chức năng chính liên quan an toàn.",
          "<b>4.1.2</b> · The loop number may include coded information such as a plant-area "
          "designation. Specific number series may also be set aside for special functions — "
          "for instance <b>900–999</b> for loops whose primary function is safety-related."),
        A("<b>4.1.3</b> · Mỗi thiết bị có thể được biểu diễn trên sơ đồ bằng một ký hiệu, và "
          "ký hiệu đó có thể đi kèm số thẻ.",
          "<b>4.1.3</b> · Each instrument may be represented on diagrams by a symbol, and the "
          "symbol may be accompanied by a tag number."),
    ]))

    b.append(h2(A("4.2 · Nhận dạng chức năng", "4.2 · Functional identification"),
                A("Quy tắc chọn chữ cái", "Rules for choosing letters")))
    b.append(p(A(
        "Nhận dạng chức năng gồm các chữ cái lấy từ <b>Bảng 1</b>: đúng <em>một chữ cái đầu</em> "
        "chỉ biến đo hoặc biến khởi tạo, và <em>một hay nhiều chữ cái tiếp theo</em> chỉ chức "
        "năng thực hiện (4.2.1). Nguyên tắc nền tảng là nhận dạng theo <b>chức năng</b>, không "
        "phải theo cấu tạo (4.2.2).",
        "Functional identification consists of letters from <b>Table 1</b>: exactly one "
        "<em>first-letter</em> designating the measured or initiating variable, plus one or "
        "more <em>succeeding-letters</em> identifying the functions performed (4.2.1). The "
        "foundation rule is that identification follows <b>function</b>, not construction "
        "(4.2.2).")))
    b.append(table(
        [A("Trường hợp", "Case"), A("Nhận dạng đúng", "Correct designation"),
         A("Vì sao", "Why")],
        [
            [A("Máy ghi chênh áp dùng để đo lưu lượng", "A differential-pressure recorder used for flow measurement"),
             A("FR", "FR"), A("Chức năng là đo lưu lượng, dù cấu tạo là chênh áp.",
                              "Its function is flow measurement, whatever its construction.")],
            [A("Đồng hồ chỉ áp nối với đầu ra của bộ truyền mức khí nén", "A pressure indicator on the output of a pneumatic level transmitter"),
             A("LI", "LI"), A("Biến được đo là mức, không phải áp suất tín hiệu.",
                              "The measured variable is level, not the signal pressure.")],
            [A("Công tắc áp suất tác động bởi cùng bộ truyền mức", "A pressure-actuated switch on that same transmitter output"),
             A("LS", "LS"), A("Vẫn lấy chữ đầu theo biến mức.", "The first-letter still follows the level variable.")],
            [A("Van thay đổi lưu lượng theo lệnh của bộ điều khiển mức", "A valve varying flow on the command of a level controller"),
             A("LV, không phải FV", "LV, not FV"),
             A("Chữ đầu theo biến <em>đo</em> (mức), không theo biến <em>bị tác động</em> (lưu lượng).",
               "The first-letter follows the <em>measured</em> variable (level), not the <em>manipulated</em> one (flow).")],
        ],
        A("Bốn ví dụ kinh điển của điều 4.2.2–4.2.3 về nhận dạng theo chức năng.",
          "Four classic examples from clauses 4.2.2–4.2.3 of identification by function.")))
    b.append(p(A(
        "<b>4.2.4 · Chữ bổ nghĩa.</b> Các chữ tiếp theo chỉ chức năng đọc/chức năng thụ động "
        "và/hoặc chức năng ra. Một chữ bổ nghĩa có thể được thêm và có thể bổ nghĩa cho cả "
        "chữ đầu lẫn chữ tiếp theo. Ví dụ <b>TDAL</b> có hai chữ bổ nghĩa: <b>D</b> biến đổi "
        "biến đo <b>T</b> thành một biến mới «nhiệt độ vi phân», còn <b>L</b> giới hạn chức "
        "năng đọc <b>A</b> (báo động) thành chỉ báo động thấp.",
        "<b>4.2.4 · Modifying letters.</b> Succeeding-letters designate readout or passive "
        "functions and/or output functions. A modifying-letter may be added, and may modify "
        "either a first-letter or succeeding-letters. Thus <b>TDAL</b> contains two modifiers: "
        "<b>D</b> turns the measured variable <b>T</b> into a new variable, «differential "
        "temperature», while <b>L</b> restricts the readout function <b>A</b> (alarm) to a low "
        "alarm only.")))
    b.append(p(A(
        "<b>4.2.5 · Thứ tự chữ.</b> Chuỗi bắt đầu bằng chữ đầu theo Bảng 1; các chữ đọc/thụ "
        "động theo sau (thứ tự tùy ý), rồi đến các chữ chức năng ra (cũng tùy ý), <em>ngoại "
        "trừ</em> chữ ra <b>C</b> (control) phải đứng trước chữ ra <b>V</b> (valve) — ví dụ "
        "<b>PCV</b>, van điều khiển tự lực. Chữ bổ nghĩa luôn đặt ngay sau chữ mà nó bổ "
        "nghĩa.",
        "<b>4.2.5 · Letter order.</b> The sequence starts with a first-letter from Table 1; "
        "readout/passive letters follow in any order, then output letters in any sequence — "
        "<em>except</em> that output letter <b>C</b> (control) precedes output letter <b>V</b> "
        "(valve), e.g. <b>PCV</b>, a self-actuated control valve. Modifying letters are always "
        "placed immediately after the letters they modify.")))
    b.append(ul([
        A("<b>4.2.6</b> · Thiết bị đa chức năng có thể vẽ bằng nhiều vòng tròn tiếp xúc nhau "
          "bằng số lượng biến đo, tín hiệu ra và chức năng. Bộ điều khiển nhiệt độ có công tắc "
          "có thể là hai vòng tròn <b>TIC-3</b> và <b>TSH-3</b>, viết gộp là "
          "<b>TIC/TSH-3</b>.",
          "<b>4.2.6</b> · A multiple-function device may be drawn with as many bubbles as it "
          "has measured variables, outputs and functions. A temperature controller with a "
          "switch may be two tangent bubbles <b>TIC-3</b> and <b>TSH-3</b>, written jointly as "
          "<b>TIC/TSH-3</b>."),
        A("<b>4.2.7</b> · Giữ số chữ chức năng ở mức tối thiểu, <b>không quá bốn chữ</b> "
          "trong một nhóm. Có thể tách nhóm con, hoặc bỏ chữ <b>I</b> (chỉ thị) nếu thiết bị "
          "vừa chỉ thị vừa ghi cùng một biến.",
          "<b>4.2.7</b> · Keep the number of functional letters to a minimum: <b>no more than "
          "four</b> letters in one group. Use subgroups, or omit <b>I</b> (indicate) when an "
          "instrument both indicates and records the same variable."),
        A("<b>4.2.8</b> · Mọi chữ cái trong nhận dạng chức năng đều viết <b>HOA</b>.",
          "<b>4.2.8</b> · All letters of the functional identification are <b>uppercase</b>."),
    ]))

    b.append(h2(A("4.3 · Nhận dạng vòng lặp", "4.3 · Loop identification"),
                A("Đánh số song song và nối tiếp", "Parallel and serial numbering")))
    b.append(p(A(
        "Nhận dạng vòng lặp gồm một chữ cái đầu và một con số. Mọi thiết bị trong cùng vòng "
        "lặp dùng chung số vòng lặp — và trong cách đánh số song song, dùng chung cả chữ cái "
        "đầu. Mỗi vòng lặp có một nhận dạng duy nhất. Thiết bị dùng chung cho hai hay nhiều "
        "vòng lặp mang nhận dạng của vòng lặp được coi là chính (4.3.1).",
        "Loop identification consists of a first-letter and a number. Every instrument in a "
        "loop carries the same loop number — and, with parallel numbering, the same "
        "first-letter. Each loop has a unique identification. An instrument common to two or "
        "more loops carries the identification of the loop considered predominant (4.3.1).")))
    b.append(table(
        [A("Cách đánh số", "Scheme"), A("Ví dụ", "Example"), A("Đặc điểm", "Characteristic")],
        [
            [A("Song song / Parallel", "Parallel"), A("TIC-100, FRC-100, LIC-100, AI-100",
                                                     "TIC-100, FRC-100, LIC-100, AI-100"),
             A("Mỗi chữ cái đầu mở một dãy số mới.", "A new numerical sequence starts for each first-letter.")],
            [A("Nối tiếp / Serial", "Serial"), A("TIC-100, FRC-101, LIC-102, AI-103",
                                                 "TIC-100, FRC-101, LIC-102, AI-103"),
             A("Một dãy số duy nhất cho cả dự án, không phụ thuộc chữ đầu.",
               "One sequence for the project regardless of the first-letter.")],
        ],
        A("4.3.2 · Dãy số có thể bắt đầu từ 1 hoặc một con số tiện lợi khác như 001, 301, 1201; "
          "có thể mang mã hóa, nhưng nên giữ đơn giản.",
          "4.3.2 · Numbering may begin at 1 or any convenient number such as 001, 301 or 1201; "
          "coded information is allowed but simplicity is recommended.")))
    b.append(ol([
        A("<b>4.3.3 · Hậu tố.</b> Khi một vòng lặp có nhiều thiết bị cùng nhận dạng chức năng, "
          "thêm hậu tố vào số vòng lặp: <b>FV-2A, FV-2B, FV-2C</b> hoặc <b>TE-25-1, "
          "TE-25-2</b>. Dùng chữ HOA; với máy ghi nhiệt độ đa điểm, đánh số cảm biến theo số "
          "điểm đo; có thể luân phiên chữ và số để chia nhỏ tiếp.",
          "<b>4.3.3 · Suffixes.</b> When a loop contains more than one instrument with the "
          "same functional identification, append a suffix: <b>FV-2A, FV-2B, FV-2C</b> or "
          "<b>TE-25-1, TE-25-2</b>. Use uppercase letters; for a multipoint temperature "
          "recorder, number primary elements after the point identification; subdivisions may "
          "alternate letters and numbers."),
        A("<b>4.3.4 · Đa chức năng.</b> Một thiết bị làm hai hay nhiều chức năng có thể ghi "
          "đủ: máy ghi lưu lượng FR-2 có thêm bút áp suất PR-4 thành <b>FR-2/PR-4</b>; máy "
          "ghi áp suất hai bút là <b>PR-7/8</b>; cửa sổ báo động chung cho báo động nhiệt độ "
          "cao và thấp là <b>TAHL-21</b>. Dấu gạch chéo không cần khi không có thiết bị tách "
          "biệt.",
          "<b>4.3.4 · Multiple functions.</b> A device performing two or more functions may "
          "be designated by all of them: flow recorder FR-2 with a pressure pen PR-4 becomes "
          "<b>FR-2/PR-4</b>; a two-pen pressure recorder is <b>PR-7/8</b>; a common annunciator "
          "window for high and low temperature alarms is <b>TAHL-21</b>. The slash is "
          "unnecessary when no distinct separate devices exist."),
        A("<b>4.3.5 · Phụ kiện.</b> Đồng hồ xả khí, bộ lọc khí, bình ngăn cách… dù không vẽ "
          "trên sơ đồ vẫn được gắn thẻ theo chức năng, dùng cùng nhận dạng vòng lặp với thiết "
          "bị mà chúng phục vụ: mặt bích lỗ tiết lưu đi với <b>FE-7</b> là <b>FX-7</b> (hoặc "
          "«FE-7 FLANGES»), ống bảo vệ nhiệt kế đi với <b>TI-9</b> là <b>TW-9</b>. Quy tắc "
          "này có thể bỏ qua với vật tư mua số lượng lớn.",
          "<b>4.3.5 · Accessories.</b> Purge meters, air sets and seal pots not shown on the "
          "diagram are still tagged by function, using the same loop identification as the "
          "instrument they serve: an orifice flange union with <b>FE-7</b> is <b>FX-7</b> (or "
          "«FE-7 FLANGES»); a thermowell with <b>TI-9</b> is <b>TW-9</b>. The rule need not "
          "apply to bulk-purchased items."),
    ], 3))

    b.append(h2(A("4.4 · Dùng ký hiệu trên bản vẽ", "4.4 · Using symbols on drawings"),
                A("Mười hai quy tắc thực hành", "Twelve practical rules")))
    b.append(p(A(
        "Các ví dụ của tiêu chuẩn minh họa cách ký hiệu được dùng điển hình; chúng <b>không "
        "giới hạn</b> ứng dụng hay cách gọi tên, và thứ tự các phương án ký hiệu không hàm ý "
        "ưu tiên gì (4.4.1).",
        "The standard's examples illustrate typical usage; they <b>do not restrict</b> the "
        "applications or designations, and the order in which alternative symbols appear "
        "implies no preference (4.4.1).")))
    b.append(ul([
        A("<b>4.4.2</b> · Vòng tròn ký hiệu có thể dùng để gắn thẻ cho ký hiệu đặc thù (vd. "
          "van điều khiển); khi đó đường nối vòng tròn tới ký hiệu được vẽ gần nhưng "
          "<em>không chạm</em>. Trong trường hợp khác, chính vòng tròn đại diện cho thiết bị.",
          "<b>4.4.2</b> · A bubble may tag a distinctive symbol such as a control valve; the "
          "connecting line is then drawn close to, but <em>not touching</em>, the symbol. "
          "Elsewhere the bubble itself represents the instrument."),
        A("<b>4.4.3</b> · Ký hiệu đặc thù có quan hệ dễ thấy với phần còn lại của vòng lặp "
          "không cần gắn thẻ riêng (mặt bích lỗ tiết lưu, van điều khiển). Ký hiệu phần tử sơ "
          "cấp nối với thiết bị khác là tùy chọn.",
          "<b>4.4.3</b> · A distinctive symbol whose relationship to the loop is obvious need "
          "not be individually tagged (an orifice flange, a control valve). Showing a primary "
          "element symbol connected to another instrument is optional."),
        A("<b>4.4.4</b> · Có thể thêm chú thích ngắn cạnh ký hiệu hoặc đường tín hiệu. Ví dụ "
          "<b>3–9 psig</b> và <b>9–15 psig</b> cạnh hai van chia dải, cùng ký hiệu trạng thái "
          "khi mất nguồn, làm rõ hoàn toàn ý đồ.",
          "<b>4.4.4</b> · A brief notation may be added adjacent to a symbol or line: "
          "<b>3–9 psig</b> and <b>9–15 psig</b> beside two split-range valves, together with "
          "failure-mode symbols, make the intent completely clear."),
        A("<b>4.4.5–4.4.6</b> · Kích thước vòng tròn chỉ là khuyến nghị, tùy thuộc tỷ lệ thu "
          "nhỏ của bản vẽ và số ký tự trong số thẻ. Ký hiệu được phép vẽ ở <em>mọi hướng</em>, "
          "đường tín hiệu có thể đi vào/ra ở mọi góc; nhưng ký hiệu khối chức năng của Bảng 3 "
          "và số thẻ <b>luôn nằm ngang</b>. Thêm mũi tên khi cần làm rõ chiều thông tin.",
          "<b>4.4.5–4.4.6</b> · Bubble sizes are recommendations only, depending on drawing "
          "reduction and tag length. Symbols may be drawn in <em>any orientation</em> and "
          "signal lines may enter or leave at any angle; but Table 3 function-block designators "
          "and tag numbers are <b>always horizontal</b>. Add arrowheads where information "
          "flow needs clarifying."),
        A("<b>4.4.7–4.4.8</b> · Nguồn điện, khí nén hay nguồn khác thường không vẽ trừ khi "
          "cần để hiểu hoạt động. Nhìn chung <em>một</em> đường tín hiệu là đủ để biểu diễn "
          "liên kết giữa hai thiết bị, dù thực tế có nhiều dây.",
          "<b>4.4.7–4.4.8</b> · Electrical, pneumatic or other power supplies are not shown "
          "unless essential to understanding. In general <em>one</em> signal line suffices "
          "between two instruments even if physically connected by several."),
        A("<b>4.4.9</b> · Thứ tự nối các thiết bị trên sơ đồ phải phản ánh <em>logic chức "
          "năng / dòng thông tin</em>, không nhất thiết đúng trình tự đấu dây. Vòng tín hiệu "
          "áp cần đấu song song, vòng tín hiệu dòng cần đấu nối tiếp, nhưng cả hai đều nên vẽ "
          "như thể đi dây song song để thể hiện rõ quan hệ chức năng.",
          "<b>4.4.9</b> · The connection sequence on a diagram should reflect <em>functional "
          "logic / information flow</em>, not necessarily the wiring order. Analog voltage "
          "loops need parallel wiring and current loops series wiring, yet both should be drawn "
          "as if all wiring were parallel so the functional relationships stay clear."),
        A("<b>4.4.10</b> · Mức độ chi tiết hoàn toàn do người dùng quyết định. Phác thảo và "
          "bài báo thường rất đơn giản; sơ đồ dòng công nghệ ít chi tiết hơn sơ đồ dòng kỹ "
          "thuật; sơ đồ kỹ thuật có thể hiện mọi phần tử trên đường ống. Điều quan trọng là "
          "<b>nhất quán</b> trong từng ứng dụng. Ba tên gọi <em>simplified / conceptual / "
          "detailed</em> ở điều 6.12 chỉ là mặt cắt của cách dùng điển hình.",
          "<b>4.4.10</b> · The degree of detail is entirely at the user's discretion. Sketches "
          "and papers are usually highly simplified; process flow diagrams are less detailed "
          "than engineering flow diagrams, which may show all in-line components. What matters "
          "is <b>consistency</b> within each application. The terms simplified / conceptual / "
          "detailed in clause 6.12 merely sample typical usage."),
        A("<b>4.4.11</b> · Sơ đồ dòng kỹ thuật thường bỏ qua phần cứng liên khóa thật sự cần "
          "cho hệ thống chạy được (relay phụ, biến dòng…), đặc biệt với liên khóa điện. Chi "
          "tiết đó được thể hiện ở tài liệu khác.",
          "<b>4.4.11</b> · Engineering flow diagrams commonly omit interlock hardware that a "
          "working system actually needs (auxiliary relays, current transformers…), especially "
          "for electrical interlocks; such detail belongs in other documents."),
        A("<b>4.4.12</b> · Ranh giới giữa hiển thị/điều khiển dùng chung và chức năng máy tính "
          "đôi khi mờ; khi chọn ký hiệu, người dùng phải dựa vào định nghĩa của nhà sản xuất, "
          "tập quán ngành và phán đoán của mình.",
          "<b>4.4.12</b> · The distinction between shared display/shared control and computer "
          "functions is sometimes blurred; the choice of symbol must rely on manufacturers' "
          "definitions, industry usage and personal judgement."),
    ]))
    b.append(note(A(
        "<b>Chuyển sang Bảng 1.</b> Điều 4 dùng Bảng 1 làm nguồn chữ cái, và dùng các tờ ký "
        "hiệu của điều 6 để minh họa. Chương 4 giải mã Bảng 1 cùng 22 chú thích đi kèm; "
        "Chương 6–7 tái tạo toàn bộ các tờ ký hiệu đó.",
        "<b>On to Table 1.</b> Clause 4 draws its letters from Table 1 and its illustrations "
        "from the clause 6 sheets. Chapter 4 decodes Table 1 with its 22 notes; Chapters 6–7 "
        "reproduce every one of those sheets.")))
    return "".join(b)


def body_vi():
    return _build("vi")


def body_en():
    return _build("en")
