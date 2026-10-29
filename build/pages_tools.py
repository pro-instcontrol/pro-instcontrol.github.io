# -*- coding: utf-8 -*-
"""Tools page - live engineering calculators."""

from framework import Page, section_open, section_close, write, render, page_intro


def field(pg, label_en, label_vi, inp_id, value, unit, step="any", hint=None):
    hint_html = ""
    if hint:
        hint_html = '<span class="hint">%s</span>' % pg.span(hint[0], hint[1])
    return (
        '<div class="field"><label for="%s">%s</label>'
        '<div class="inwrap"><input id="%s" type="number" step="%s" value="%s">'
        '<span class="unit">%s</span></div>%s</div>'
        % (inp_id, pg.span(label_en, label_vi), inp_id, step, value, unit, hint_html)
    )


def verdict(pg, vid, items):
    """A block of mutually exclusive verdict lines, toggled by data-v."""
    spans = "".join(
        '<span class="v %s" data-v="%s">%s</span>' % (cls, key, pg.span(en, vi))
        for key, cls, en, vi in items
    )
    return '<div class="verdict" id="%s">%s</div>' % (vid, spans)


def build():
    pg = Page(
        "tools.html",
        "tol",
        "Tools — signal scaling, DP flow, valve Cv, error budget | I&amp;C",
        "Công cụ — quy đổi tín hiệu, lưu lượng chênh áp, Cv van, ngân sách sai số",
        "Four working calculators for process instrumentation: 4–20 mA scaling with the NAMUR "
        "fault band, differential-pressure flow scaling, liquid control valve sizing with a choked "
        "flow check, hydrostatic level, and a loop error budget.",
        "Bốn công cụ tính toán cho thiết bị đo quá trình: quy đổi 4–20 mA với dải báo lỗi NAMUR, "
        "quy đổi lưu lượng theo chênh áp, tính Cv van điều khiển cho chất lỏng có kiểm tra xâm thực, "
        "mức thủy tĩnh, và ngân sách sai số của vòng đo.",
    )

    body = page_intro(
        pg,
        "Five calculators you actually use on a Monday",
        "Năm công cụ bạn thực sự dùng vào sáng thứ Hai",
        "Every number below updates as you type. These are the calculations that get done on site with "
        "a phone and a coffee — signal scaling, square-root flow, valve sizing, hydrostatic level and "
        "the error budget nobody writes down.",
        "Mọi con số dưới đây cập nhật ngay khi bạn nhập. Đây là những phép tính được làm tại hiện "
        "trường bằng điện thoại và một ly cà phê — quy đổi tín hiệu, lưu lượng căn bậc hai, tính van, "
        "mức thủy tĩnh và ngân sách sai số mà không ai ghi lại.",
        [
            ("signal", "Signal scaling", "Quy đổi tín hiệu"),
            ("dpflow", "DP flow", "Lưu lượng chênh áp"),
            ("valve", "Valve sizing", "Tính van"),
            ("level", "Hydrostatic level", "Mức thủy tĩnh"),
            ("error", "Error budget", "Ngân sách sai số"),
            ("limits", "Limits &amp; caveats", "Giới hạn &amp; lưu ý"),
        ],
    )

    # ---------------- 01 signal scaling ----------------
    body += section_open("01", "Signal scaling", "Quy đổi tín hiệu", pg, "signal")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="tool" data-tool="ma">
  <div class="tool-body">
    <div class="fields">
      %s
      %s
      %s
      %s
    </div>
    <div class="result">
      <div class="big"><b id="ma-out">—</b><span>mA</span></div>
      <div class="rline"><span>%s</span><b id="ma-pct">—</b></div>
      <div class="rline"><span>%s</span><b id="ma-eu">—</b></div>
      <div class="band" id="ma-band"><i></i></div>
      <div class="zones"><span>0</span><span>3.6</span><span>4</span><span>20</span><span>21</span><span>24</span></div>
      %s
    </div>
  </div>
</div>
<div class="note">
  <span class="lbl">%s</span>
  %s
</div>
""" % (
        pg.h2("Where the value sits on the loop", "Giá trị nằm ở đâu trên vòng đo"),
        pg.p(
            "Type a process value and read the current, or type a measured current and read the value. "
            "The bar shows the NAMUR NE&nbsp;43 fault bands — anything outside 3.6–21.0&nbsp;mA is a "
            "diagnostic, not a measurement.",
            "Nhập giá trị quá trình để đọc dòng điện, hoặc nhập dòng đo được để đọc giá trị. Thanh bên "
            "phải hiển thị dải báo lỗi NAMUR NE&nbsp;43 — bất cứ giá trị ngoài 3,6–21,0&nbsp;mA là chẩn "
            "đoán, không phải phép đo.",
        ),
        field(pg, "Lower range value (LRV)", "Giá trị dải dưới (LRV)", "ma-lrv", "0", "EU"),
        field(pg, "Upper range value (URV)", "Giá trị dải trên (URV)", "ma-urv", "100", "EU"),
        field(pg, "Process value", "Giá trị quá trình", "ma-pv", "60", "EU"),
        field(pg, "Loop current", "Dòng vòng đo", "ma-ma", "13.6", "mA", "0.01"),
        pg.span("Span position", "Vị trí dải"),
        pg.span("From current", "Từ dòng điện"),
        verdict(
            pg,
            "ma-verdict",
            [
                ("ok", "ok", "Valid measurement — inside the 4–20 mA range.",
                 "Phép đo hợp lệ — trong dải 4–20 mA."),
                ("under", "warn", "Below 4 mA but above 3.6 mA — value under range, loop still alive.",
                 "Dưới 4 mA nhưng trên 3,6 mA — giá trị dưới dải, vòng vẫn còn sống."),
                ("over", "warn", "Above 20 mA but below 21 mA — value over range, loop still alive.",
                 "Trên 20 mA nhưng dưới 21 mA — giá trị vượt dải, vòng vẫn còn sống."),
                ("faultlow", "bad", "Below 3.6 mA — broken wire, dead transmitter or lost supply.",
                 "Dưới 3,6 mA — dây đứt, bộ truyền hỏng hoặc mất nguồn."),
                ("faulthigh", "bad", "Above 21.0 mA — transmitter fault or saturation.",
                 "Trên 21,0 mA — bộ truyền lỗi hoặc bão hòa."),
            ],
        ),
        pg.span("Why 4 mA is not zero", "Vì sao 4 mA không phải zero"),
        pg.p(
            "A live zero means a genuine zero reading still draws 4&nbsp;mA, so 0&nbsp;mA can only be a "
            "broken wire. Below 3.6&nbsp;mA and above 21.0&nbsp;mA the transmitter is allowed to report "
            "a failure instead of a value — which is why the two bands are coloured differently here.",
            "Điểm không sống nghĩa là giá trị không thật vẫn tiêu thụ 4&nbsp;mA, nên 0&nbsp;mA chỉ có "
            "thể là dây đứt. Dưới 3,6&nbsp;mA và trên 21,0&nbsp;mA bộ truyền được phép báo lỗi thay vì "
            "báo giá trị — vì vậy hai dải này được tô màu khác ở đây.",
        ),
    )
    body += section_close()

    # ---------------- 02 DP flow ----------------
    body += section_open("02", "Differential-pressure flow", "Lưu lượng theo chênh áp", pg, "dpflow")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="tool" data-tool="dp">
  <div class="tool-body">
    <div class="fields">
      %s
      %s
      %s
      %s
    </div>
    <div class="result">
      <div class="big"><b id="dp-out">—</b><span>flow</span></div>
      <div class="rline"><span>%s</span><b id="dp-dp">—</b></div>
      <div class="rline"><span>%s</span><b id="dp-pct">—</b></div>
      <div class="rline"><span>%s</span><b id="dp-td">—</b></div>
    </div>
  </div>
</div>
<div class="note warn">
  <span class="lbl">%s</span>
  %s
</div>
""" % (
        pg.h2("Square root, and why turndown hurts", "Căn bậc hai, và vì sao dải đo bị thu hẹp"),
        pg.p(
            "Across an orifice, nozzle or venturi the differential pressure rises with the square of the "
            "flow (ISO 5167). Scaling from a known design point needs no discharge coefficient — but it "
            "does need an honest design point.",
            "Qua lỗ khoan, nozzle hay venturi, chênh áp tăng theo bình phương lưu lượng (ISO 5167). Quy "
            "đổi từ một điểm thiết kế đã biết không cần hệ số lưu lượng — nhưng cần một điểm thiết kế "
            "trung thực.",
        ),
        field(pg, "Design flow", "Lưu lượng thiết kế", "dp-qd", "100", "m³/h"),
        field(pg, "Design differential", "Chênh áp thiết kế", "dp-dpd", "250", "mbar"),
        field(pg, "Measured differential", "Chênh áp đo được", "dp-dpm", "100", "mbar"),
        field(pg, "Accuracy at design", "Độ chính xác tại điểm thiết kế", "dp-acc", "1", "% span", "0.05"),
        pg.span("Flow at this differential", "Lưu lượng tại chênh áp này"),
        pg.span("DP as % of span", "Chênh áp theo % dải"),
        pg.span("Error at this flow", "Sai số tại lưu lượng này"),
        pg.span("The trap", "Cái bẫy"),
        pg.p(
            "At 50&nbsp;% of design flow the differential is only 25&nbsp;% of span, so a ±1&nbsp;% span "
            "error becomes ±2&nbsp;% of reading. At 25&nbsp;% flow the differential is 6.25&nbsp;% of "
            "span and the same error becomes ±4&nbsp;% of reading. This is why a DP meter is a poor "
            "choice for wide turndown, however good the transmitter.",
            "Tại 50&nbsp;% lưu lượng thiết kế, chênh áp chỉ còn 25&nbsp;% dải, nên sai số ±1&nbsp;% dải "
            "trở thành ±2&nbsp;% giá trị đọc. Tại 25&nbsp;% lưu lượng, chênh áp là 6,25&nbsp;% dải và "
            "cùng sai số đó thành ±4&nbsp;% giá trị đọc. Đó là lý do đồng hồ chênh áp là lựa chọn kém "
            "cho dải đo rộng, dù bộ truyền có tốt đến đâu.",
        ),
    )
    body += section_close()

    # ---------------- 03 valve sizing ----------------
    body += section_open("03", "Liquid valve sizing", "Tính van cho chất lỏng", pg, "valve")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="tool" data-tool="cv">
  <div class="tool-body">
    <div class="fields">
      %s
      %s
      %s
      %s
      %s
      %s
      %s
      %s
    </div>
    <div class="result">
      <div class="big"><b id="cv-out">—</b><span>Kv</span></div>
      <div class="rline"><span>%s</span><b id="cv-cv">—</b></div>
      <div class="rline"><span>%s</span><b id="cv-dp">—</b></div>
      <div class="rline"><span>%s</span><b id="cv-open">—</b></div>
      %s
    </div>
  </div>
</div>
<div class="note">
  <span class="lbl">%s</span>
  %s
</div>
""" % (
        pg.h2("Kv from flow, and the choked-flow limit", "Kv từ lưu lượng, và giới hạn xâm thực"),
        pg.p(
            "Kv is the flow of water in m³/h at 1&nbsp;bar drop. Once the pressure drop exceeds the "
            "choked limit the extra drop buys nothing — the valve is already at critical flow and the "
            "sizing must use the limited ΔP, not the actual one.",
            "Kv là lưu lượng nước tính bằng m³/h khi chênh áp 1&nbsp;bar. Khi chênh áp vượt giới hạn tới "
            "hạn, phần chênh áp thêm không mang lại gì — van đã ở trạng thái dòng tới hạn và phải tính "
            "theo ΔP giới hạn, không phải ΔP thực tế.",
        ),
        field(pg, "Flow", "Lưu lượng", "cv-q", "40", "m³/h"),
        field(pg, "Specific gravity", "Khối lượng riêng tương đối", "cv-sg", "1", "–", "0.01"),
        field(pg, "Inlet pressure (abs)", "Áp vào (tuyệt đối)", "cv-p1", "6", "bar a"),
        field(pg, "Outlet pressure (abs)", "Áp ra (tuyệt đối)", "cv-p2", "4", "bar a"),
        field(pg, "Vapour pressure (abs)", "Áp hơi (tuyệt đối)", "cv-pv", "0.02", "bar a", "0.001"),
        field(pg, "Liquid critical pressure", "Áp tới hạn của chất lỏng", "cv-pc", "220.6", "bar a", "0.1"),
        field(pg, "Pressure recovery factor F<sub>L</sub>", "Hệ số thu hồi áp F<sub>L</sub>", "cv-fl", "0.9", "–", "0.01"),
        field(pg, "Rated Cv of the valve", "Cv định mức của van", "cv-rated", "60", "Cv", "1"),
        pg.span("Required Cv", "Cv yêu cầu"),
        pg.span("ΔP used in sizing", "ΔP dùng để tính"),
        pg.span("Opening at rated Cv (approx.)", "Độ mở theo Cv định mức (xấp xỉ)"),
        verdict(
            pg,
            "cv-verdict",
            [
                ("ok", "ok", "Sizing looks reasonable — the valve works in the controllable part of its range.",
                 "Cỡ van hợp lý — van làm việc trong vùng điều khiển được."),
                ("low", "warn", "Under 10 % opening — the valve is oversized and control will be poor. Consider a smaller trim.",
                 "Dưới 10 % độ mở — van quá lớn và điều khiển sẽ kém. Cân nhắc trim nhỏ hơn."),
                ("high", "warn", "Over 90 % opening — no margin left for a higher demand.",
                 "Trên 90 % độ mở — không còn dự phòng cho nhu cầu cao hơn."),
                ("choked", "bad", "Choked flow — the sizing used the limited ΔP, not the actual one. Expect cavitation or flashing.",
                 "Dòng tới hạn — phép tính dùng ΔP giới hạn, không phải ΔP thực. Dự kiến có xâm thực hoặc hóa hơi."),
            ],
        ),
        pg.span("Sizing rules of thumb", "Quy tắc chọn cỡ"),
        pg.p(
            "Aim for 20–80&nbsp;% opening at normal flow, with the maximum at about 90&nbsp;%. Below "
            "10&nbsp;% the plug is off its seat and control is poor; above 90&nbsp;% there is no margin "
            "for a higher demand. Choked flow also means cavitation or flashing — check the trim "
            "material and consider an anti-cavitation cage.",
            "Nhắm tới độ mở 20–80&nbsp;% tại lưu lượng bình thường, cực đại khoảng 90&nbsp;%. Dưới "
            "10&nbsp;% nút van vừa rời đế và điều khiển kém; trên 90&nbsp;% không còn dự phòng cho nhu "
            "cầu cao hơn. Dòng tới hạn cũng có nghĩa là xâm thực hoặc hóa hơi — hãy kiểm tra vật liệu "
            "trim và cân nhắc lồng chống xâm thực.",
        ),
    )
    body += section_close()

    # ---------------- 04 level ----------------
    body += section_open("04", "Hydrostatic level", "Mức thủy tĩnh", pg, "level")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="tool" data-tool="lvl">
  <div class="tool-body">
    <div class="fields">
      %s
      %s
      %s
    </div>
    <div class="result">
      <div class="big"><b id="lvl-out">—</b><span>m</span></div>
      <div class="rline"><span>%s</span><b id="lvl-dp">—</b></div>
      <div class="rline"><span>%s</span><b id="lvl-err">—</b></div>
    </div>
  </div>
</div>
<div class="note warn">
  <span class="lbl">%s</span>
  %s
</div>
""" % (
        pg.h2("ρgh, and the error you inherit from ρ", "ρgh, và sai số thừa hưởng từ ρ"),
        pg.p(
            "A DP transmitter does not measure level — it measures pressure and divides by a density "
            "you typed in once, years ago. Change the temperature, the product or the concentration, "
            "and the level reading moves without anything moving.",
            "Bộ truyền áp vi sai không đo mức — nó đo áp suất rồi chia cho một khối lượng riêng bạn đã "
            "nhập một lần, nhiều năm trước. Thay đổi nhiệt độ, sản phẩm hoặc nồng độ, và kết quả đo mức "
            "sẽ dịch chuyển dù không có gì dịch chuyển.",
        ),
        field(pg, "Differential pressure", "Chênh áp", "lvl-dp-in", "500", "mbar"),
        field(pg, "Density", "Khối lượng riêng", "lvl-rho", "1000", "kg/m³", "1"),
        field(pg, "Density uncertainty", "Độ bất định khối lượng riêng", "lvl-dr", "1", "%", "0.1"),
        pg.span("Equivalent pressure", "Áp suất tương đương"),
        pg.span("Level error from ρ", "Sai số mức do ρ"),
        pg.span("The dominant term", "Số hạng chi phối"),
        pg.p(
            "A 1&nbsp;% density error is a 1&nbsp;% level error — 50&nbsp;mm on a 5&nbsp;m tank, straight "
            "onto the operator's screen. If the product temperature swings, either compensate with a "
            "measured density or accept that the level is nominal.",
            "Sai số khối lượng riêng 1&nbsp;% là sai số mức 1&nbsp;% — 50&nbsp;mm trên bồn 5&nbsp;m, đi "
            "thẳng lên màn hình người vận hành. Nếu nhiệt độ sản phẩm dao động, hãy bù bằng khối lượng "
            "riêng đo được hoặc chấp nhận rằng mức chỉ là danh nghĩa.",
        ),
    )
    body += section_close()

    # ---------------- 05 error budget ----------------
    body += section_open("05", "Loop error budget", "Ngân sách sai số vòng đo", pg, "error")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="tool" data-tool="err">
  <div class="tool-body">
    <div class="fields">
      %s
      %s
      %s
      %s
      %s
    </div>
    <div class="result">
      <div class="big"><b id="err-out">—</b><span>&#37;&nbsp;span</span></div>
      <div class="rline"><span>%s</span><b id="err-rss">—</b></div>
      <div class="rline"><span>%s</span><b id="err-eu">—</b></div>
      <div class="rline"><span>%s</span><b id="err-worst">—</b></div>
    </div>
  </div>
</div>
<div class="note">
  <span class="lbl">%s</span>
  %s
</div>
""" % (
        pg.h2("Four errors, one number", "Bốn sai số, một con số"),
        pg.p(
            "The datasheet accuracy is only the first term. Installation, ambient temperature and the "
            "input card each add their own. Independent random errors combine as the root of the sum of "
            "squares; systematic ones add directly.",
            "Độ chính xác trên datasheet chỉ là số hạng đầu tiên. Lắp đặt, nhiệt độ môi trường và card "
            "đầu vào mỗi thứ thêm sai số riêng. Sai số ngẫu nhiên độc lập cộng theo căn bậc hai tổng "
            "bình phương; sai số hệ thống cộng trực tiếp.",
        ),
        field(pg, "Transmitter accuracy", "Độ chính xác bộ truyền", "err-a", "0.1", "% span", "0.01"),
        field(pg, "Installation error", "Sai số lắp đặt", "err-b", "0.5", "% span", "0.01"),
        field(pg, "Ambient / EMC effect", "Ảnh hưởng môi trường / EMC", "err-c", "0.2", "% span", "0.01"),
        field(pg, "Input card resolution", "Độ phân giải card đầu vào", "err-d", "0.05", "% span", "0.01"),
        field(pg, "Span in engineering units", "Dải đo theo đơn vị kỹ thuật", "err-span", "250", "EU"),
        pg.span("Root sum square", "Căn tổng bình phương"),
        pg.span("In engineering units", "Theo đơn vị kỹ thuật"),
        pg.span("Arithmetic worst case", "Tổng hợp xấu nhất"),
        pg.span("Which one to quote", "Nên trích dẫn con số nào"),
        pg.p(
            "Quote the RSS figure when the errors are genuinely independent and you are reporting a "
            "typical uncertainty. Quote the arithmetic sum when you must guarantee a limit, because it "
            "assumes every error lines up in the same direction — which is what a customer's auditor "
            "will assume if the number is challenged.",
            "Trích dẫn con số RSS khi các sai số thực sự độc lập và bạn đang báo cáo độ bất định điển "
            "hình. Trích dẫn tổng số học khi phải đảm bảo một giới hạn, vì nó giả định mọi sai số cùng "
            "chiều — điều mà kiểm toán viên của khách hàng sẽ giả định nếu con số bị chất vấn.",
        ),
    )
    body += section_close()

    # ---------------- 06 limits ----------------
    body += section_open("06", "Limits &amp; caveats", "Giới hạn &amp; lưu ý", pg, "limits")
    body += """
<div class="grid c2">
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
</div>
<div class="nextprev">
  <a href="control.html"><span class="k">%s</span>%s</a>
  <a href="instruments.html" style="text-align:right"><span class="k">%s</span>%s</a>
</div>
""" % (
        pg.h3("Valve sizing is not a spreadsheet exercise", "Tính van không phải bài tập bảng tính"),
        pg.p(
            "Kv from a formula gives you a number to compare against a catalogue. The final choice still "
            "depends on the trim characteristic, noise, cavitation, actuator thrust and what the "
            "purchasing department can actually deliver.",
            "Kv từ công thức cho bạn một con số để so với catalogue. Lựa chọn cuối cùng vẫn phụ thuộc "
            "đặc tính trim, độ ồn, xâm thực, lực cơ cấu chấp hành và thứ mà bộ phận mua hàng thực sự "
            "giao được.",
        ),
        pg.h3("DP flow needs a real design point", "Lưu lượng chênh áp cần điểm thiết kế thật"),
        pg.p(
            "The square-root scaling assumes the same fluid, the same density and the same orifice. "
            "Change the gas composition or the temperature and the relationship quietly stops being true.",
            "Quy đổi căn bậc hai giả định cùng chất lỏng, cùng khối lượng riêng và cùng tấm lỗ khoan. "
            "Thay đổi thành phần khí hoặc nhiệt độ và mối quan hệ âm thầm không còn đúng.",
        ),
        pg.h3("Level is a density measurement in disguise", "Mức thực chất là phép đo khối lượng riêng"),
        pg.p(
            "The uncertainty from ρ usually dominates the transmitter's own accuracy. If density is not "
            "measured, level is not measured — it is estimated.",
            "Độ bất định từ ρ thường chi phối độ chính xác của chính bộ truyền. Nếu không đo khối lượng "
            "riêng thì không đo được mức — đó là ước lượng.",
        ),
        pg.h3("Every number here is a starting point", "Mọi con số ở đây chỉ là khởi điểm"),
        pg.p(
            "These tools exist to catch mistakes early — a choked valve, a turndown that cannot work, a "
            "loop error larger than the tolerance. They do not replace the standard, the vendor's sizing "
            "software or a second engineer's check.",
            "Các công cụ này để phát hiện sai sót sớm — van bị tới hạn, dải đo không khả thi, sai số "
            "vòng lớn hơn dung sai. Chúng không thay thế tiêu chuẩn, phần mềm tính toán của nhà sản "
            "xuất hay bước kiểm tra của kỹ sư thứ hai.",
        ),
        pg.span("Back", "Quay lại"),
        pg.span("Control &amp; tuning", "Điều khiển &amp; hiệu chỉnh"),
        pg.span("Also", "Xem thêm"),
        pg.span("Instrument reference", "Danh mục thiết bị"),
    )
    body += section_close()

    write("tools.html", render(pg, body, "tools.html"))
