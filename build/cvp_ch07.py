# -*- coding: utf-8 -*-
"""Book 7, Chapter 7 - Sizing and Selection—Let the Computer Do It All! (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
51-54 (PDF pp. 58-61). No figures and no equations; one vendor table
(Table 7-1) and one numbered footnote on valve gain.
"""
from cvp_common import h2, h3, note, ol, p, table, ul

PAGES_SRC = 4
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Sizing and Selection—Let the Computer Do It All!"
TITLE_VI = "Định cỡ và lựa chọn — để máy tính lo hết!"


def note_terms(lang):
    """A one-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 7.</b> phần mềm tính cỡ van (sizing software) · "
                "hệ số lưu lượng C<sub>v</sub> định mức (rated Cv) · hệ số phục hồi áp suất "
                "chất lỏng F<sub>L</sub> · hệ số F<sub>d</sub> · đoạn thu nhỏ (reducer) · độ "
                "nhớt (viscosity) · vòng lặp tính toán (iteration) · xâm thực (cavitation) · "
                "hóa hơi (flashing) · tiếng ồn khí động / thủy động (aerodynamic / "
                "hydrodynamic noise) · tài khoản thứ sáu sau dấu thập phân (sixth decimal "
                "place) · thước loga (slide rule) · kiểu nối đầu (end connections: flanged, "
                "welded, screwed) · cấp rò rỉ (leakage class) I / II / IV / V / VI · chống ăn "
                "mòn (corrosion resistant) · đặc tính lưu lượng (flow characteristic: equal "
                "percentage, linear) · cỡ bộ truyền động và dải hiệu chuẩn bàn (actuator size "
                "and bench range) · đặc tính lưu lượng lắp đặt (installed flow characteristic) · "
                "độ khuếch đại của van (valve gain, dq/ds) · độ ổn định vòng điều khiển (loop "
                "stability) · bộ định vị van (positioner) · dòng chảy bị nghẽn (choked flow) · "
                "số Mach · đế van / bệ van / mặt tựa của van (seat) · ANSI/ISA-75.01.01 · "
                "IEC 60534-8-3 / IEC 60534-8-4 · phương pháp dự báo tiếng ồn ABC.")
    return ("<b>Key terms.</b> sizing software · rated C<sub>v</sub> flow coefficient · "
            "liquid pressure recovery factor F<sub>L</sub> · F<sub>d</sub> factor · reducer · "
            "viscosity · iteration · cavitation · flashing · aerodynamic / hydrodynamic noise · "
            "sixth decimal place · slide rule · end connections (flanged, welded, screwed) · "
            "leakage classes I / II / IV / V / VI · corrosion resistance · flow characteristic "
            "(equal percentage, linear) · actuator size and bench range · installed flow "
            "characteristic · valve gain (dq/ds) · loop stability · positioner · choked flow · "
            "Mach number · seat · ANSI/ISA-75.01.01 · IEC 60534-8-3 / IEC 60534-8-4 · ABC "
            "noise prediction methods.")


def _vendor_rows():
    """The seven Table 7-1 entries, with names and addresses exactly as printed."""
    return [
        ["Engineered Software, Inc.", "PO Box 2514 Olympia, WA 98507"],
        ["Fisher Controls International, Inc.", "Marshalltown, IA 50158"],
        ["Flowserve Incorporated", "PO Box 2200, Springville, UT 84663"],
        ["SAMSON AG", "Frankfurt, Germany"],
        ["International Society of Automation (ISA)",
         "3252 South Miami Blvd, Suite 102 Durham, NC 27703"],
        ["Masoneilan International, Inc.", "GE Energy"],
        ["MESA, Inc.", "PO Box 15004, Worcester, MA 01615"],
    ]


def body_vi():
    b = []
    b.append(h2("Hai loại phần mềm tính cỡ van cơ bản",
                "Two basic types of sizing software"))
    b.append(p("Có hai loại phần mềm tính cỡ van cơ bản. Loại thứ nhất cho phép bạn chọn kiểu "
               "van, rồi cung cấp các thông số cụ thể lấy từ cơ sở dữ liệu, chẳng hạn giá trị "
               "C<sub>v</sub> định mức, F<sub>L</sub> và F<sub>d</sub>, để bạn thực hiện đúng "
               "các phép tính tính cỡ. Loại thứ hai chỉ cho phép bạn nhập điều kiện dòng chảy, "
               "rồi máy tính sẽ tính C<sub>v</sub> và chọn đúng van, thường là lựa chọn kinh tế "
               "nhất."))
    b.append(p("Cả hai phương pháp đều có vấn đề. Trong trường hợp thứ nhất, bạn bị bắt chọn "
               "kiểu van và nhà cung cấp trước khi có cơ hội nhận báo giá của đối thủ cạnh "
               "tranh hoặc đánh giá một kiểu van kinh tế hơn. Trong trường hợp thứ hai, chương "
               "trình tính cỡ phải khởi đầu với một số thông số “giả định”, chẳng hạn giá trị "
               "F<sub>L</sub> và F<sub>d</sub>. Máy tính sau đó chọn kiểu và cỡ van tốt nhất "
               "cho ứng dụng. Tuy nhiên, giá trị F<sub>L</sub> hoặc F<sub>d</sub> được chọn có "
               "thể khác với giá trị giả định, vì thế bạn phải lặp lại các phép tính tính cỡ "
               "— một tình huống không lý tưởng. Dẫu vậy, máy tính có thể tiết kiệm rất nhiều "
               "thời gian, đặc biệt khi tính toán ảnh hưởng của tổn thất ở đoạn thu nhỏ "
               "(reducer) hoặc của độ nhớt. Hai yếu tố này nếu không có máy tính sẽ đòi hỏi "
               "các vòng lặp tốn nhiều công sức (tính lại nhiều lần, trong đó bạn giả định một "
               "cỡ van hoặc giá trị C<sub>v</sub>, thực hiện phép tính, nhận ra cỡ van giả định "
               "là quá nhỏ, chọn cỡ van hoặc giá trị C<sub>v</sub> lớn hơn rồi bắt đầu lại, "
               "và thường phải lặp lại nhiều lần)."))

    b.append(h2("Những gì phần mềm cơ bản tính toán",
                "What basic programs calculate"))
    b.append(p("Phần mềm tính cỡ cơ bản thường có thể tính giá trị C<sub>v</sub> cần thiết cho "
               "các điều kiện lưu lượng lớn nhất, bình thường và nhỏ nhất. Phần mềm cho biết "
               "van có bị xâm thực hay hóa hơi hay không, và có thể tính tiếng ồn của van theo "
               "cơ chế khí động hoặc thủy động."))
    b.append(p("Đừng ấn tượng trước khả năng của máy tính trong việc tính giá trị C<sub>v</sub> "
               "đến tài khoản thứ sáu sau dấu thập phân. Điều đó vô nghĩa. Kết quả đúng phụ "
               "thuộc vào một chương trình không lỗi và việc chọn đúng dữ liệu đầu vào. Tôi "
               "luôn khuyên dùng thước loga (slide rule) hoặc một máy tính cầm tay đơn giản để "
               "kiểm tra lại kết quả của máy tính, đặc biệt khi bạn dùng phần mềm hoàn toàn "
               "mới."))

    b.append(h2("Chương trình tốt hơn: lựa chọn van và tính cỡ bộ truyền động",
                "Better programs: selection and actuator sizing"))
    b.append(p("Các chương trình tốt hơn sẽ tiến xa hơn và chọn đúng cỡ và kiểu van cho điều "
               "kiện dòng chảy của bạn dựa trên các thông số yêu cầu như kiểu nối đầu (mặt "
               "bích, hàn, ren vít, v.v.); yêu cầu rò rỉ (Cấp I, II, IV, V hoặc VI); van có cần "
               "chống ăn mòn hay không (không, mức trung bình, rất cao); đặc tính lưu lượng "
               "(phần trăm bằng nhau, tuyến tính); và có thể còn các yếu tố khác. Dựa trên "
               "những yếu tố này, máy tính sẽ tìm kiếm trong cơ sở dữ liệu và chọn phương án "
               "phù hợp và kinh tế nhất. Một số chương trình thậm chí còn tính cỡ bộ truyền "
               "động cần thiết và dải hiệu chuẩn bàn (bench range). Tuy nhiên, đừng mong "
               "chương trình của Công ty A lại chọn van của Công ty B. Rốt cuộc, lòng tốt cũng "
               "có giới hạn."))

    b.append(h2("Chương trình tiên tiến: đặc tính lắp đặt và độ ổn định vòng điều khiển",
                "Advanced programs: installed characteristic and loop stability"))
    b.append(p("Các chương trình tiên tiến hơn đi thêm một bước: tính độ giảm áp trong hệ thống "
               "đường ống của bạn (bạn phải cung cấp dữ liệu đầu vào), đồng thời tính “đặc tính "
               "lưu lượng lắp đặt” của van và “độ khuếch đại” (dq/ds) của van trong các điều "
               "kiện dòng chảy khác nhau. Nhờ đó bạn xác định được vòng điều khiển có ổn định "
               "hay không.<sup>1</sup>"))
    b.append(note("<b>Chú thích 1.</b> Nhiều người có suy nghĩ sai rằng độ khuếch đại của van "
                  "điều khiển phải bằng ±1. Điều này là không cần thiết và thường cũng không "
                  "thể được (vì bạn không bao giờ dùng toàn bộ dải tín hiệu). Điều quan trọng "
                  "là độ khuếch đại (dù có giá trị nào) phải duy trì tương đối ổn định khi "
                  "điều kiện dòng chảy thay đổi (xem Chương 8)."))

    b.append(h2("Danh mục kiểm tra khi chọn phần mềm",
                "Checklist for choosing a program"))
    b.append(p("Khi chọn một chương trình (hầu hết nhà cung cấp đều có bản miễn phí), hãy kiểm "
               "tra các điểm sau:"))
    b.append(ul([
        "Việc tính cỡ van phải theo tiêu chuẩn hiện hành ANSI/ISA-75.01.01 hoặc các tiêu chuẩn "
        "tương ứng của Ủy ban Kỹ thuật Điện Quốc tế (IEC).",
        "Phương trình tiếng ồn phải theo IEC 60534-8-3 (đối với khí) hoặc IEC 60534-8-4 (đối "
        "với chất lỏng). (Tiếc là bạn sẽ cần các hệ số riêng của nhà cung cấp để dùng các tiêu "
        "chuẩn này.) Tốt hơn nữa, hãy dùng các phương pháp dự báo tiếng ồn ABC đơn giản hơn "
        "(xem Chương 18 và Chương 22), vốn hoạt động tốt cho mọi kiểu và mọi hãng van.",
        "C<sub>v</sub> lớn nhất yêu cầu không được vượt quá 85% C<sub>v</sub> định mức của van "
        "đã chọn.",
        "C<sub>v</sub> nhỏ nhất yêu cầu phải lớn hơn C<sub>v</sub> của van đã chọn được liệt kê "
        "tại 5% hành trình van (nếu dùng bộ định vị van), hoặc 10% nếu ma sát đệm kín có thể "
        "cao và không dùng bộ định vị.",
    ]))

    b.append(h2("Các cảnh báo cần lưu ý", "Warnings to heed"))
    b.append(p("Chương trình cũng sẽ đưa ra các cảnh báo như sau:"))
    b.append(ul([
        "Đừng lo lắng trước cảnh báo đáng sợ “dòng chảy bị nghẽn” (choked flow). Cảnh báo này "
        "không có ý nghĩa gì khác ngoài việc đòi hỏi dùng các phương trình tính cỡ khác.",
        "Bỏ qua các phép tính vận tốc ở đầu vào và đầu ra. Những con số này vô nghĩa, ngoại trừ "
        "trong trường hợp tiếng ồn khí động, nơi bạn nên tránh để vận tốc chất lưu ở cửa ra "
        "của van vượt quá 0,3 Mach.",
        "Hãy chú ý đến các cảnh báo xâm thực hoặc hóa hơi. Chúng có thể báo hiệu rắc rối (xem "
        "Chương 14).",
    ]))

    b.append(h2("Nhà cung cấp phần mềm tính cỡ", "Vendors of sizing programs"))
    b.append(table(["Nhà cung cấp", "Địa chỉ"], _vendor_rows(),
                   caption="Bảng 7-1. Bảng liệt kê một phần các nhà cung cấp phần mềm máy tính "
                           "dùng để tính cỡ và lựa chọn van điều khiển."))

    b.append(note("<b>Ghi chú về nguồn.</b> (1) Lớp văn bản OCR của các trang in có nhiều dấu "
                  "gạch nối khi xuống dòng («maxi-mum», «char-acteristic», «cor-responding», "
                  "«liq-uids», «neces-sary»); bản dịch ghép lại thành từ hoàn chỉnh và cũng sửa "
                  "«C v» bị tách chữ thành «C<sub>v</sub>». (2) Bảng 7-1 trong nguyên bản là "
                  "bảng liệt kê một phần các nhà cung cấp; ở đây được tái hiện đầy đủ như bản "
                  "in, giữ nguyên tên và địa chỉ nhà cung cấp, chỉ dịch tiêu đề cột và chú "
                  "thích bảng. (3) Danh sách cảnh báo viện dẫn «xem Chương 14» cho các cảnh báo "
                  "xâm thực/hóa hơi, dù nội dung xâm thực thực ra được trình bày ở Chương 15. "
                  "Bản dịch giữ nguyên cách viện dẫn của nguồn và ghi rõ sự khác biệt ở đây "
                  "thay vì tự ý sửa. (4) Trang PDF 61 (trang in «55») không chứa nội dung chương, "
                  "chỉ còn một số trang lạc đề."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 7 chiếm các trang in 51-54 của ấn bản in (PDF tr. 58-61). Nguyên bản "
               "không có hình cũng như phương trình; chương chỉ có một bảng nhà cung cấp (Bảng "
               "7-1) và một chú thích đánh số về độ khuếch đại của van, tất cả đều được giữ "
               "lại."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Hai loại phần mềm tính cỡ van cơ bản",
                "Two basic types of sizing software"))
    b.append(p("There are two basic types of sizing software programs. The first lets you pick "
               "the valve type and then gives you the specifics selected from the database, "
               "such as rated C<sub>v</sub>, F<sub>L</sub>, and F<sub>d</sub> values, so you can "
               "do the right sizing calculations. The second type lets you enter only the flow "
               "conditions, and then the computer calculates the C<sub>v</sub> and selects the "
               "right valve, usually the best economical choice."))
    b.append(p("There are problems with both methods. In the first case, you are forced to "
               "select a valve type and vendor before you have a chance to get a competitor's "
               "bid or evaluate a more economical valve type. In the second case, your sizing "
               "program must start with some “assumed” parameters, such as F<sub>L</sub> and "
               "F<sub>d</sub> values. The computer then chooses the best valve type and size to "
               "fit this application. However, the chosen F<sub>L</sub> or F<sub>d</sub> may be "
               "different from the assumed one and, as a result, you have to repeat the sizing "
               "calculations—not an ideal situation. Nevertheless, computers can be great "
               "time-savers, especially when it comes to calculating the effects of reducer "
               "losses or viscosity. Both require otherwise time-consuming iterations (repeat "
               "calculations in which you have to assume a valve size or C<sub>v</sub> value, do "
               "your calculation, realize the assumed valve size was too small, pick a larger "
               "valve size or C<sub>v</sub> value, and then start over, usually several times)."))

    b.append(h2("Những gì phần mềm cơ bản tính toán",
                "What basic programs calculate"))
    b.append(p("Basic computer sizing software usually can calculate the required "
               "C<sub>v</sub> value for maximum, normal, and minimum flow conditions. The "
               "software indicates whether the valve will cavitate or flash and can calculate "
               "the aerodynamic or hydrodynamic valve noise."))
    b.append(p("Do not be impressed by the computer's ability to calculate a C<sub>v</sub> "
               "number to the sixth decimal place. This is meaningless. Correct results depend "
               "on an error-free program and selecting the right input data. I always recommend "
               "using a slide rule or a simple handheld calculator to double-check the "
               "computer's result, especially if you use brand-new software."))

    b.append(h2("Chương trình tốt hơn: lựa chọn van và tính cỡ bộ truyền động",
                "Better programs: selection and actuator sizing"))
    b.append(p("Better programs will go further and select the right valve size and type for "
               "your flow condition based on such required parameters as end connections "
               "(flanged, welded, screwed, etc.); leakage requirements (Class I, II, IV, V, or "
               "VI); whether the valve should be corrosion resistant (no, mild, very); the flow "
               "characteristic (equal percentage, linear); and perhaps others. Based on these "
               "factors, the computer will search the database and select the most suitable and "
               "economical choice. Some will even calculate the required actuator size and "
               "bench range. However, do not expect the program from Company A to select a "
               "valve from Company B. After all, there are limits to benevolence."))

    b.append(h2("Chương trình tiên tiến: đặc tính lắp đặt và độ ổn định vòng điều khiển",
                "Advanced programs: installed characteristic and loop stability"))
    b.append(p("More advanced programs go a step further and calculate the pressure drop in "
               "your piping system (you have to provide the input) and calculate the "
               "“installed” flow characteristic of the valve and the “gain” (dq/ds) of the "
               "valve under various flow conditions. This way you can determine whether the "
               "control loop will be stable.<sup>1</sup>"))
    b.append(note("<b>Footnote 1.</b> Some people have the misconception that the gain of the "
                  "control valve must be ±1. This is not necessary and typically is not "
                  "possible (because you never use the full signal span). It is important for "
                  "the gain (whatever it is) to stay reasonably constant with a change of flow "
                  "conditions (see Chapter 8)."))

    b.append(h2("Danh mục kiểm tra khi chọn phần mềm",
                "Checklist for choosing a program"))
    b.append(p("When selecting a program (most vendors offer free ones), check the following:"))
    b.append(ul([
        "Valve sizing should be per the current ANSI/ISA-75.01.01 standard or the "
        "corresponding International Electrotechnical Commission (IEC) standards.",
        "Noise equations should follow IEC 60534-8-3 (for gas) or IEC 60534-8-4 (for liquids). "
        "(Unfortunately, you will need vendor-specific factors in order to use these "
        "standards.) Or better yet, use the simpler ABC noise prediction methods (see Chapters "
        "18 and 22), which work well for all valve types and makes.",
        "The required maximum C<sub>v</sub> should not be more than 85% of the rated "
        "C<sub>v</sub> of the selected valve.",
        "The minimum required C<sub>v</sub> should be greater than the C<sub>v</sub> of the "
        "selected valve listed at 5% of valve travel (if a positioner is used), or 10% if the "
        "packing friction may be high and no positioner is used.",
    ]))

    b.append(h2("Các cảnh báo cần lưu ý", "Warnings to heed"))
    b.append(p("The program will also contain warnings such as these:"))
    b.append(ul([
        "Do not be scared by the ominous “choked flow” warning. This has no meaning other than "
        "it requires different sizing equations.",
        "Ignore calculations of inlet and outlet velocities. These mean nothing, except on "
        "aerodynamic noise where you should avoid fluid velocities in the valve outlet above "
        "0.3 Mach.",
        "Pay attention to cavitation or flashing warnings. They may spell trouble (see "
        "Chapter 14).",
    ]))

    b.append(h2("Nhà cung cấp phần mềm tính cỡ", "Vendors of sizing programs"))
    b.append(table(["Vendor", "Address"], _vendor_rows(),
                   caption="Table 7-1. Partial tabulation of vendors offering computer "
                           "programs for control valve sizing and selection."))

    b.append(note("<b>Source notes.</b> (1) The OCR text layer of the printed pages contains "
                  "line-break hyphenations («maxi-mum», «char-acteristic», «cor-responding», "
                  "«liq-uids», «neces-sary»); the translation joins them into whole words and "
                  "also repairs the spaced-out «C v» to «C<sub>v</sub>». (2) Table 7-1 is "
                  "printed as a partial tabulation of vendors; it is reproduced here in full "
                  "as printed, with vendor names and addresses unchanged, under localized "
                  "headers and a localized caption. (3) The warning list cites “see Chapter "
                  "14” for cavitation/flashing warnings, although cavitation is actually "
                  "treated in Chapter 15. The translation keeps the source's citation and "
                  "flags the discrepancy here rather than silently correcting it. (4) PDF page "
                  "61 (printed “55”) carries no chapter prose, only a stray page number."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chapter 7 occupies printed pp. 51-54 of the book (PDF pp. 58-61). The source "
               "has no figures and no equations; it contains one vendor table (Table 7-1) and "
               "one numbered footnote on valve gain, all of which are retained."))
    return "".join(b)
