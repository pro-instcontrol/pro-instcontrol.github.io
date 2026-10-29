# -*- coding: utf-8 -*-
"""Control & tuning page."""

from framework import Page, section_open, section_close, write, render, page_intro

LOOP_SVG = """
<svg viewBox="0 0 680 250" role="img" aria-label="Block diagram of a feedback control loop">
  <defs>
    <marker id="a2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#0b1725"/>
    </marker>
  </defs>

  <!-- setpoint in -->
  <text x="18" y="124" font-family="'IBM Plex Mono',monospace" font-size="11" fill="#a85a06">SP</text>
  <line x1="42" y1="130" x2="97" y2="130" stroke="#0b1725" stroke-width="1.6" marker-end="url(#a2)"/>

  <!-- summing junction -->
  <circle cx="120" cy="130" r="21" fill="#fff" stroke="#0b1725" stroke-width="1.8"/>
  <text x="105" y="120" font-family="'IBM Plex Mono',monospace" font-size="14" fill="#0b1725">+</text>
  <text x="104" y="154" font-family="'IBM Plex Mono',monospace" font-size="15" fill="#a85a06">&minus;</text>

  <!-- error -->
  <line x1="141" y1="130" x2="172" y2="130" stroke="#0b1725" stroke-width="1.6" marker-end="url(#a2)"/>
  <text x="155" y="120" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="10" fill="#66788d">e</text>

  <!-- controller -->
  <rect x="176" y="108" width="104" height="44" rx="6" fill="#fff" stroke="#0b1725" stroke-width="1.8"/>
  <text x="228" y="127" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="12" font-weight="600" fill="#0b1725">PID</text>
  <text x="228" y="141" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="9" fill="#66788d">controller</text>

  <!-- controller to valve -->
  <line x1="280" y1="130" x2="316" y2="130" stroke="#0b1725" stroke-width="1.6" marker-end="url(#a2)"/>
  <text x="298" y="120" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="10" fill="#0d7a6f">u(t)</text>

  <!-- final element -->
  <rect x="320" y="108" width="100" height="44" rx="6" fill="#fff" stroke="#0b1725" stroke-width="1.8"/>
  <text x="370" y="127" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="12" font-weight="600" fill="#0b1725">Valve</text>
  <text x="370" y="141" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="9" fill="#66788d">final element</text>

  <!-- valve to process -->
  <line x1="420" y1="130" x2="456" y2="130" stroke="#0b1725" stroke-width="1.6" marker-end="url(#a2)"/>

  <!-- process -->
  <rect x="460" y="108" width="110" height="44" rx="6" fill="#f7f9fc" stroke="#0b1725" stroke-width="1.8"/>
  <text x="515" y="127" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="12" font-weight="600" fill="#0b1725">Process</text>
  <text x="515" y="141" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="9" fill="#66788d">T, L, K</text>

  <!-- disturbance -->
  <line x1="515" y1="74" x2="515" y2="104" stroke="#a85a06" stroke-width="1.4" stroke-dasharray="4 3" marker-end="url(#a2)"/>
  <text x="524" y="72" font-family="'IBM Plex Mono',monospace" font-size="10" fill="#a85a06">d(t)</text>

  <!-- output -->
  <line x1="570" y1="130" x2="620" y2="130" stroke="#0b1725" stroke-width="1.6" marker-end="url(#a2)"/>
  <text x="630" y="124" font-family="'IBM Plex Mono',monospace" font-size="11" fill="#0d7a6f">PV</text>

  <!-- feedback -->
  <path d="M515 152 V208 H120 V155" fill="none" stroke="#0d7a6f" stroke-width="1.6" marker-end="url(#a2)"/>
  <text x="320" y="200" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="9.5" fill="#0d7a6f">measurement (feedback)</text>
</svg>
"""


def build():
    pg = Page(
        "control.html",
        "ctl",
        "Control &amp; tuning — PID, dead time, advanced strategies | I&amp;C",
        "Điều khiển &amp; hiệu chỉnh — PID, thời gian trễ, chiến lược nâng cao | I&amp;C",
        "How a control loop decides: PID terms and their effects, tuning methods compared, "
        "why dead time dominates controllability, and where cascade, feedforward and MPC fit.",
        "Cách một vòng điều khiển ra quyết định: các số hạng PID và tác dụng, so sánh phương pháp "
        "hiệu chỉnh, vì sao thời gian trễ chi phối khả năng điều khiển.",
    )

    body = page_intro(
        pg,
        "The loop decides",
        "Vòng điều khiển ra quyết định",
        "A controller is a small piece of arithmetic with a large responsibility: it compares what is "
        "happening with what should be happening and moves something. Everything difficult about "
        "control comes from the gap between those two — and from how long the process takes to notice.",
        "Bộ điều khiển là một phép tính nhỏ với trách nhiệm lớn: so sánh điều đang xảy ra với điều "
        "đáng lẽ phải xảy ra và dịch chuyển một thứ gì đó. Mọi khó khăn của điều khiển đều đến từ "
        "khoảng cách giữa hai điều đó — và từ việc quá trình mất bao lâu mới nhận ra.",
        [
            ("loop", "Anatomy of a loop", "Cấu trúc vòng"),
            ("pid", "Three terms", "Ba số hạng"),
            ("tuning", "Tuning methods", "Phương pháp hiệu chỉnh"),
            ("deadtime", "Dead time", "Thời gian trễ"),
            ("advanced", "Beyond one loop", "Vượt một vòng"),
            ("sim", "Simulator", "Mô phỏng"),
            ("platform", "Platforms &amp; safety", "Nền tảng &amp; an toàn"),
        ],
    )

    # 01 block diagram
    body += section_open("01", "Anatomy", "Cấu trúc", pg, "loop")
    body += """
<div class="figure" style="max-width:780px">
  %s
  <div class="figcap">%s</div>
</div>
<div class="grid c3 mt24">
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
</div>
""" % (
        LOOP_SVG,
        pg.span(
            "Single-input single-output feedback loop. e = SP − PV; u drives the final element.",
            "Vòng phản hồi một vào một ra. e = SP − PV; u điều khiển phần tử chấp hành.",
        ),
        pg.h3("Error is the only input", "Sai lệch là đầu vào duy nhất"),
        pg.p(
            "The controller never sees the process — only the difference between the setpoint and the "
            "measurement. Every tuning problem is a problem of interpreting that difference.",
            "Bộ điều khiển không bao giờ thấy quá trình — chỉ thấy hiệu giữa giá trị đặt và giá trị đo. "
            "Mọi bài toán hiệu chỉnh đều là bài toán diễn giải hiệu số đó.",
        ),
        pg.h3("The valve is part of the loop", "Van là một phần của vòng"),
        pg.p(
            "A sticky valve, an oversized valve or a positioner with a 3&nbsp;% dead band will destroy the "
            "performance of a perfectly tuned controller. Tune the valve first.",
            "Van bị kẹt, van quá lớn hoặc bộ định vị có dải chết 3&nbsp;% sẽ phá hỏng hiệu năng của một "
            "bộ điều khiển được hiệu chỉnh hoàn hảo. Hãy xử lý van trước.",
        ),
        pg.h3("Feedback is always late", "Phản hồi luôn đến muộn"),
        pg.p(
            "The correction arrives after the process has already moved. That delay, not the algorithm, "
            "sets the achievable performance — which is why the next two sections are about time.",
            "Sự hiệu chỉnh đến sau khi quá trình đã thay đổi. Chính độ trễ đó, không phải thuật toán, "
            "quyết định hiệu năng đạt được — vì vậy hai phần tiếp theo nói về thời gian.",
        ),
    )
    body += section_close()

    # 02 PID terms
    body += section_open("02", "Three terms", "Ba số hạng", pg, "pid")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="tbl-wrap">
<table class="tbl">
  <thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead>
  <tbody>
    <tr><td><strong>P</strong> — %s</td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>I</strong> — %s</td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>D</strong> — %s</td><td>%s</td><td>%s</td><td>%s</td></tr>
  </tbody>
</table>
</div>
<div class="note">
  <span class="lbl">%s</span>
  %s
</div>
""" % (
        pg.h2("Proportional, integral, derivative — and what each one costs", "Tỷ lệ, tích phân, vi phân — và cái giá của từng số hạng"),
        pg.p(
            "Ninety percent of industrial loops run PI. Derivative is useful on slow, smooth processes "
            "and actively harmful on noisy ones.",
            "Chín mươi phần trăm vòng công nghiệp chạy PI. Vi phân hữu ích với quá trình chậm, êm và "
            "thực sự có hại với quá trình nhiễu.",
        ),
        pg.th("Term", "Số hạng"),
        pg.th("Action", "Tác động"),
        pg.th("Turn it up", "Tăng lên thì"),
        pg.th("Too much", "Quá mức"),
        pg.span("proportional gain", "hệ số tỷ lệ"),
        pg.span("Output proportional to the current error.", "Đầu ra tỷ lệ với sai lệch hiện tại."),
        pg.span("Faster response, smaller offset, tighter control.", "Đáp ứng nhanh hơn, offset nhỏ hơn, điều khiển sát hơn."),
        pg.span("Overshoot, oscillation, eventual instability.", "Vọt lố, dao động, cuối cùng là mất ổn định."),
        pg.span("integral time", "thời gian tích phân"),
        pg.span("Accumulates error over time until it disappears. Note: lower T<sub>i</sub> means more integral action.", "Tích lũy sai lệch theo thời gian cho đến khi hết. Lưu ý: T<sub>i</sub> nhỏ hơn nghĩa là tác động tích phân mạnh hơn."),
        pg.span("Offset driven to zero at steady state.", "Offset được đưa về zero ở trạng thái xác lập."),
        pg.span("Windup during saturation, slow oscillation, hunting.", "Tích phân bão hòa khi đầu ra bị giới hạn, dao động chậm, dao động săn."),
        pg.span("derivative time", "thời gian vi phân"),
        pg.span("Reacts to the rate of change, anticipating where the error is going.", "Phản ứng với tốc độ thay đổi, dự báo sai lệch sẽ đi đâu."),
        pg.span("Damping, less overshoot, faster settling.", "Tắt dần, ít vọt lố, ổn định nhanh hơn."),
        pg.span("Amplifies sensor noise, wears the valve, hides in the scan time.", "Khuếch đại nhiễu cảm biến, mài mòn van, bị che bởi chu kỳ quét."),
        pg.span("Integral windup", "Tích phân bão hòa"),
        pg.p(
            "When the output saturates — valve fully open — the integral term keeps accumulating error it "
            "cannot act on. When the process finally responds, the controller is still carrying that "
            "history and overshoots badly. Use anti-windup: stop integrating, or back-calculate from the "
            "actual valve position.",
            "Khi đầu ra bão hòa — van mở hoàn toàn — số hạng tích phân vẫn tiếp tục tích lũy sai lệch mà "
            "nó không thể tác động. Khi quá trình cuối cùng đáp ứng, bộ điều khiển vẫn mang theo lịch sử "
            "đó và vọt lố nặng. Hãy dùng chống bão hòa tích phân: ngừng tích phân, hoặc tính ngược từ vị "
            "trí van thực tế.",
        ),
    )
    body += section_close()

    # 03 tuning
    body += section_open("03", "Tuning", "Hiệu chỉnh", pg, "tuning")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="tbl-wrap">
<table class="tbl">
  <thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead>
  <tbody>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
  </tbody>
</table>
</div>

<div class="mt40"></div>
%s
<div class="tbl-wrap mt24">
<table class="tbl">
  <thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead>
  <tbody>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
  </tbody>
</table>
</div>
""" % (
        pg.h2("Six ways to find the numbers", "Sáu cách tìm ra các thông số"),
        pg.p(
            "Every method is a shortcut around the same problem: you do not have a reliable model of the "
            "process, so you perturb it and watch.",
            "Mọi phương pháp đều là đường tắt cho cùng một vấn đề: bạn không có mô hình đáng tin của quá "
            "trình, nên bạn tác động vào nó và quan sát.",
        ),
        pg.th("Method", "Phương pháp"),
        pg.th("Needs", "Cần gì"),
        pg.th("Use when", "Dùng khi"),
        pg.th("Result", "Kết quả"),
        pg.span("Manual / trial", "Thủ công / thử sai"),
        pg.span("Experience, patience, a trend screen.", "Kinh nghiệm, kiên nhẫn, màn hình trend."),
        pg.span("Most loops, most of the time.", "Hầu hết vòng đo, phần lớn thời gian."),
        pg.span("Safe, slow, depends on the person.", "An toàn, chậm, phụ thuộc người làm."),
        pg.span("Ziegler-Nichols, closed loop", "Ziegler-Nichols, vòng kín"),
        pg.span("Raise gain to sustained oscillation → K<sub>u</sub>, P<sub>u</sub>.", "Tăng hệ số đến dao động duy trì → K<sub>u</sub>, P<sub>u</sub>."),
        pg.span("Fast loops that tolerate overshoot; simulation.", "Vòng nhanh chấp nhận vọt lố; mô phỏng."),
        pg.span("Aggressive, typically ~25&nbsp;% overshoot.", "Mạnh, điển hình vọt lố ~25&nbsp;%."),
        pg.span("Ziegler-Nichols, open loop", "Ziegler-Nichols, vòng hở"),
        pg.span("A step test → gain K, dead time L, time constant T.", "Thử bậc thang → hệ số K, trễ L, hằng số thời gian T."),
        pg.span("Dead-time dominant processes.", "Quá trình bị chi phối bởi thời gian trễ."),
        pg.span("Aggressive; can be unstable on lag-dominant loops.", "Mạnh; có thể mất ổn định với vòng chi phối bởi quán tính."),
        pg.span("Cohen-Coon", "Cohen-Coon"),
        pg.span("Same step test data.", "Cùng dữ liệu thử bậc thang."),
        pg.span("L/T between 0.1 and 1.", "L/T trong khoảng 0,1 đến 1."),
        pg.span("Better than ZN for dead time, still fast.", "Tốt hơn ZN với thời gian trễ, vẫn nhanh."),
        pg.span("IMC / lambda tuning", "Hiệu chỉnh IMC / lambda"),
        pg.span("A first-order-plus-dead-time model and a chosen λ.", "Mô hình bậc một có trễ và λ chọn trước."),
        pg.span("Industrial loops that must not overshoot; level and pressure.", "Vòng công nghiệp không được vọt lố; mức và áp suất."),
        pg.span("No overshoot; λ sets the speed. λ ≈ 1–3 × dead time is a good start.", "Không vọt lố; λ quyết định tốc độ. λ ≈ 1–3 × thời gian trễ là khởi điểm tốt."),
        pg.span("Relay auto-tune", "Tự hiệu chỉnh bằng relay"),
        pg.span("Built-in function; a few minutes of valve movement.", "Chức năng có sẵn; vài phút van dịch chuyển."),
        pg.span("Commissioning many loops quickly.", "Chạy thử nhiều vòng một cách nhanh chóng."),
        pg.span("Finds K<sub>u</sub>/P<sub>u</sub> automatically; validate before accepting.", "Tự tìm K<sub>u</sub>/P<sub>u</sub>; kiểm tra lại trước khi chấp nhận."),
        pg.h2("Starting points by loop type", "Điểm khởi đầu theo loại vòng"),
        pg.th("Loop", "Vòng"),
        pg.th("Character", "Đặc tính"),
        pg.th("Start with", "Bắt đầu với"),
        pg.th("Note", "Ghi chú"),
        pg.span("Flow", "Lưu lượng"),
        pg.span("Fast, noisy, self-regulating.", "Nhanh, nhiễu, tự cân bằng."),
        pg.span("P + small I. K<sub>p</sub> 0.5–1.0, T<sub>i</sub> 0.1–0.5 min, no D.", "P + I nhỏ. K<sub>p</sub> 0,5–1,0; T<sub>i</sub> 0,1–0,5 phút; không D."),
        pg.span("Filter the measurement before adding gain.", "Lọc tín hiệu đo trước khi tăng hệ số."),
        pg.span("Level (averaging)", "Mức (san bằng)"),
        pg.span("Integrating — never settles on its own.", "Tích phân — không tự ổn định."),
        pg.span("P only, proportional band 50–200&nbsp;%, or very slow I.", "Chỉ P, dải tỷ lệ 50–200&nbsp;%, hoặc I rất chậm."),
        pg.span("Use the surge volume deliberately; tight level control fights the downstream unit.", "Dùng thể tích đệm có chủ đích; điều khiển mức quá sát sẽ chống lại thiết bị phía sau."),
        pg.span("Pressure (liquid)", "Áp suất (chất lỏng)"),
        pg.span("Fast, hydraulic.", "Nhanh, thủy lực."),
        pg.span("PI, similar to flow.", "PI, tương tự lưu lượng."),
        pg.span("Watch pump interaction and resonance.", "Cẩn thận tương tác bơm và cộng hưởng."),
        pg.span("Temperature", "Nhiệt độ"),
        pg.span("Slow, lag-dominant, often long dead time.", "Chậm, chi phối bởi quán tính, thường trễ dài."),
        pg.span("PID. K<sub>p</sub> 2–6, T<sub>i</sub> 5–20 min, T<sub>d</sub> 1–5 min.", "PID. K<sub>p</sub> 2–6; T<sub>i</sub> 5–20 phút; T<sub>d</sub> 1–5 phút."),
        pg.span("Derivative helps here; tune with the process at load.", "Vi phân hữu ích ở đây; hiệu chỉnh khi quá trình có tải."),
        pg.span("Analyser / composition", "Máy phân tích / thành phần"),
        pg.span("Very slow, large dead time from the sample line.", "Rất chậm, trễ lớn do tuyến lấy mẫu."),
        pg.span("Low-gain PI, or feedforward from a fast upstream measurement.", "PI hệ số thấp, hoặc feedforward từ phép đo nhanh phía trước."),
        pg.span("Minimise the sample transport delay before tuning anything.", "Giảm thiểu trễ vận chuyển mẫu trước khi hiệu chỉnh bất cứ thứ gì."),
    )
    body += section_close()

    # 04 dead time
    body += section_open("04", "Dead time", "Thời gian trễ", pg, "deadtime")
    body += """
<div class="g-2-1">
  <div>
    %s
    %s
    %s
    %s
    <div class="note warn">
      <span class="lbl">%s</span>
      %s
    </div>
  </div>
  <div class="card">
    <span class="n">%s</span>
    <h3>%s</h3>
    <div class="spec" style="margin-top:12px">
      <div><dt>%s</dt><dd>%s</dd></div>
      <div><dt>%s</dt><dd>%s</dd></div>
      <div><dt>%s</dt><dd>%s</dd></div>
      <div><dt>%s</dt><dd>%s</dd></div>
    </div>
  </div>
</div>
""" % (
        pg.h2("The one number that limits everything", "Con số giới hạn mọi thứ"),
        pg.p(
            "Dead time (transport delay) is the interval between moving the valve and seeing any change "
            "at all. It is not lag — lag is the process easing towards a new value; dead time is nothing "
            "happening. A controller cannot distinguish &ldquo;no response yet&rdquo; from &ldquo;no "
            "response&rdquo;, so it keeps pushing.",
            "Thời gian trễ (trễ vận chuyển) là khoảng thời gian từ khi dịch chuyển van đến khi thấy bất "
            "kỳ thay đổi nào. Nó không phải quán tính — quán tính là quá trình từ từ tiến đến giá trị "
            "mới; còn trễ là hoàn toàn không có gì xảy ra. Bộ điều khiển không phân biệt được "
            "&ldquo;chưa có đáp ứng&rdquo; với &ldquo;không có đáp ứng&rdquo;, nên nó tiếp tục đẩy.",
        ),
        pg.p(
            "The controllability ratio <code>L/T</code> — dead time over the dominant time constant — "
            "predicts how well PID can work before you touch a single tuning parameter. Where does dead "
            "time come from? Transport in a pipe, analyser sample lines, a slow-responding sensor in a "
            "thermowell, a scan time that is too coarse, or damping applied to hide noise.",
            "Tỷ số điều khiển được <code>L/T</code> — thời gian trễ chia cho hằng số thời gian trội — dự "
            "báo mức độ PID có thể làm tốt trước khi bạn động đến một tham số nào. Thời gian trễ đến từ "
            "đâu? Vận chuyển trong ống, tuyến lấy mẫu máy phân tích, cảm biến đáp ứng chậm trong ống bảo "
            "vệ, chu kỳ quét quá thô, hoặc hằng số làm mượt dùng để che nhiễu.",
        ),
        pg.p(
            "The engineering response is rarely &ldquo;tune harder&rdquo;. It is to remove the delay: "
            "move the analyser closer, use a faster sensor, cut the damping, shorten the sample line. "
            "Every minute spent on the physical delay is worth an hour of tuning.",
            "Cách xử lý kỹ thuật hiếm khi là &ldquo;hiệu chỉnh mạnh hơn&rdquo;. Đó là loại bỏ độ trễ: "
            "đặt máy phân tích gần hơn, dùng cảm biến nhanh hơn, giảm làm mượt, rút ngắn tuyến lấy mẫu. "
            "Mỗi phút dành cho độ trễ vật lý đáng giá bằng một giờ hiệu chỉnh.",
        ),
        pg.span("Rule", "Quy tắc"),
        pg.p(
            "If the dead time is longer than the time constant, PID is the wrong tool — use feedforward, "
            "dead-time compensation, or change the process.",
            "Nếu thời gian trễ dài hơn hằng số thời gian, PID là công cụ sai — hãy dùng feedforward, "
            "bù thời gian trễ, hoặc thay đổi chính quá trình.",
        ),
        pg.span("L / T ratio", "Tỷ số L / T"),
        pg.h3("Controllability", "Khả năng điều khiển"),
        pg.td("&lt; 0.1", "&lt; 0,1"),
        pg.td("Easy — most of the loop's speed is available.", "Dễ — gần như toàn bộ tốc độ của vòng đều dùng được."),
        pg.td("0.1 – 0.5", "0,1 – 0,5"),
        pg.td("Normal industrial loop; PI or PID works well.", "Vòng công nghiệp bình thường; PI hoặc PID đều tốt."),
        pg.td("0.5 – 1.0", "0,5 – 1,0"),
        pg.td("Difficult; detune for stability, accept slow response.", "Khó; phải giảm hệ số để ổn định, chấp nhận đáp ứng chậm."),
        pg.td("&gt; 1.0", "&gt; 1,0"),
        pg.td("PID inadequate — change the process or the strategy.", "PID không đủ — thay đổi quá trình hoặc chiến lược."),
    )
    body += section_close()

    # 05 advanced
    body += section_open("05", "Beyond the single loop", "Vượt ra ngoài một vòng", pg, "advanced")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="grid c3">
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
</div>
""" % (
        pg.h2("When one loop is not enough", "Khi một vòng là không đủ"),
        pg.p(
            "Most real plants are coupled: the flow loop changes the pressure, which changes the "
            "temperature, which changes the composition. These structures exist to break that coupling "
            "deliberately.",
            "Hầu hết nhà máy thực tế đều có tương tác: vòng lưu lượng thay đổi áp suất, áp suất thay đổi "
            "nhiệt độ, nhiệt độ thay đổi thành phần. Các cấu trúc dưới đây tồn tại để phá vỡ tương tác đó "
            "một cách có chủ đích.",
        ),
        pg.h3("Cascade", "Tầng nối tiếp"),
        pg.p(
            "A slow outer loop (temperature) writes the setpoint of a fast inner loop (flow). The inner "
            "loop absorbs valve and pressure disturbances before the outer loop sees them.",
            "Vòng ngoài chậm (nhiệt độ) đặt giá trị đặt cho vòng trong nhanh (lưu lượng). Vòng trong hấp "
            "thụ nhiễu van và áp suất trước khi vòng ngoài nhìn thấy.",
        ),
        pg.h3("Feedforward", "Feedforward (bù trước)"),
        pg.p(
            "Measure the disturbance and act before the error appears. Requires a measurable disturbance "
            "and a rough model — the classic example is boiler feedwater on steam flow.",
            "Đo nhiễu và tác động trước khi sai lệch xuất hiện. Cần nhiễu đo được và một mô hình gần "
            "đúng — ví dụ kinh điển là nước cấp lò hơi theo lưu lượng hơi.",
        ),
        pg.h3("Ratio", "Tỷ lệ"),
        pg.p(
            "One stream follows another at a fixed ratio — reagent to feed, dilution water to product. "
            "Often the ratio itself is trimmed by a slow composition analyser.",
            "Một dòng đi theo dòng khác với tỷ lệ cố định — hóa chất theo nguyên liệu, nước pha loãng "
            "theo sản phẩm. Thường chính tỷ lệ được hiệu chỉnh bởi một máy phân tích thành phần chậm.",
        ),
        pg.h3("Split range", "Dải chia"),
        pg.p(
            "One controller drives two valves in sequence: the small one for fine control, the large one "
            "for capacity. Common on pressure letdown and compressor anti-surge.",
            "Một bộ điều khiển điều khiển hai van theo trình tự: van nhỏ cho điều chỉnh tinh, van lớn cho "
            "công suất. Phổ biến ở giảm áp và chống surge máy nén.",
        ),
        pg.h3("Override / selective", "Ghi đè / chọn lọc"),
        pg.p(
            "Several controllers share one final element; a selector passes the safest signal. Used for "
            "compressor surge control and fired-heater constraints.",
            "Nhiều bộ điều khiển dùng chung một phần tử chấp hành; bộ chọn truyền tín hiệu an toàn nhất. "
            "Dùng cho chống surge máy nén và giới hạn lò đốt.",
        ),
        pg.h3("MPC", "MPC"),
        pg.p(
            "A model predicts the future over a horizon and optimises the moves, respecting constraints. "
            "Worth it when there are many variables, long dead times and real economic value in pushing "
            "to a limit.",
            "Mô hình dự báo tương lai trên một chân trời và tối ưu các bước dịch chuyển, tôn trọng ràng "
            "buộc. Đáng đầu tư khi có nhiều biến, thời gian trễ dài và giá trị kinh tế thực khi đẩy tới "
            "giới hạn.",
        ),
    )
    body += section_close()

    # 06 simulator
    body += section_open("06", "Try it", "Thử nghiệm", pg, "sim")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="sim">
  <div class="sim-grid">
    <div>
      <canvas id="pid-canvas" width="760" height="380" role="img" aria-label="Simulated closed-loop response"></canvas>
      <div class="sim-read">
        <div><span>%s</span><b id="m-os">–</b></div>
        <div><span>%s</span><b id="m-settle">–</b></div>
        <div><span>%s</span><b id="m-iae">–</b></div>
        <div><span>%s</span><b id="m-mv">–</b></div>
      </div>
    </div>
    <div>
      <div class="ctrl">
        <div class="row"><label for="s-kp">%s</label><output id="o-kp">1.4</output></div>
        <input id="s-kp" type="range" min="0.2" max="8" step="0.1" value="1.4">
      </div>
      <div class="ctrl">
        <div class="row"><label for="s-ti">%s</label><output id="o-ti">9</output></div>
        <input id="s-ti" type="range" min="0" max="30" step="0.5" value="9">
      </div>
      <div class="ctrl">
        <div class="row"><label for="s-td">%s</label><output id="o-td">0</output></div>
        <input id="s-td" type="range" min="0" max="8" step="0.1" value="0">
      </div>
      <div class="ctrl">
        <div class="row"><label for="s-dl">%s</label><output id="o-dl">2</output></div>
        <input id="s-dl" type="range" min="0" max="8" step="0.5" value="2">
      </div>
      <div class="ctrl">
        <div class="row"><label for="s-tc">%s</label><output id="o-tc">6</output></div>
        <input id="s-tc" type="range" min="1" max="20" step="0.5" value="6">
      </div>
      <div class="sim-btns">
        <button type="button" data-preset="p">%s</button>
        <button type="button" data-preset="pi">PI</button>
        <button type="button" data-preset="pid">PID</button>
        <button type="button" data-preset="aggr">%s</button>
      </div>
    </div>
  </div>
</div>
<div class="note mt24">
  <span class="lbl">%s</span>
  %s
</div>
""" % (
        pg.h2("A loop you can break", "Một vòng điều khiển để bạn phá"),
        pg.p(
            "The process below is a first-order lag with dead time. Push the gain until it oscillates, "
            "then add integral action and watch the offset disappear — and the overshoot grow. Raise the "
            "dead time and the same tuning becomes unstable.",
            "Quá trình dưới đây là khâu quán tính bậc một có thời gian trễ. Hãy tăng hệ số đến khi dao "
            "động, rồi thêm tác động tích phân và xem offset biến mất — cùng với vọt lố tăng lên. Tăng "
            "thời gian trễ và chính bộ thông số đó trở nên mất ổn định.",
        ),
        pg.span("Overshoot", "Vọt lố"),
        pg.span("Settling time", "Thời gian ổn định"),
        pg.span("IAE (error area)", "IAE (diện tích sai lệch)"),
        pg.span("Valve output", "Đầu ra van"),
        pg.span("Gain K<sub>p</sub>", "Hệ số K<sub>p</sub>"),
        pg.span("Integral T<sub>i</sub> (s)", "Tích phân T<sub>i</sub> (giây)"),
        pg.span("Derivative T<sub>d</sub> (s)", "Vi phân T<sub>d</sub> (giây)"),
        pg.span("Dead time L (s)", "Thời gian trễ L (giây)"),
        pg.span("Time constant T (s)", "Hằng số thời gian T (giây)"),
        pg.span("P only", "Chỉ P"),
        pg.span("Too aggressive", "Quá mạnh"),
        pg.span("What to watch for", "Điều cần quan sát"),
        pg.p(
            "Set derivative to zero first — most loops do not need it. Then raise gain until the response "
            "is just short of overshooting, and add integral action only until the offset is gone. If the "
            "loop becomes unstable when you raise the dead time, no tuning will fix it: the process is "
            "telling you the delay must be removed.",
            "Trước tiên đặt vi phân bằng không — hầu hết vòng không cần. Sau đó tăng hệ số cho đến khi đáp "
            "ứng vừa chớm vọt lố, và chỉ thêm tích phân cho đến khi hết offset. Nếu vòng mất ổn định khi "
            "tăng thời gian trễ, không bộ thông số nào cứu được: quá trình đang nói rằng phải loại bỏ độ trễ.",
        ),
    )
    body += section_close()

    # 07 architecture
    body += section_open("07", "Platforms &amp; safety", "Nền tảng &amp; an toàn", pg, "platform")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="tbl-wrap">
<table class="tbl">
  <thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead>
  <tbody>
    <tr><td><strong>PLC</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>DCS</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>SCADA + RTU</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>Edge / PAC</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
  </tbody>
</table>
</div>
<div class="note warn mt24">
  <span class="lbl">%s</span>
  %s
</div>
""" % (
        pg.h2("Four platforms, one boundary", "Bốn nền tảng, một ranh giới"),
        pg.p(
            "The choice is about scale, redundancy and engineering workflow — not about which box is more "
            "modern. IEC 61131-3 defines the programming languages that all four implement.",
            "Lựa chọn liên quan đến quy mô, dự phòng và quy trình kỹ thuật — không phải hộp nào hiện đại "
            "hơn. IEC 61131-3 định nghĩa các ngôn ngữ lập trình mà cả bốn đều dùng.",
        ),
        pg.th("Platform", "Nền tảng"),
        pg.th("Scan / scale", "Chu kỳ / quy mô"),
        pg.th("Strength", "Thế mạnh"),
        pg.th("Typical use", "Dùng điển hình"),
        pg.span("1–50 ms; one machine or skid", "1–50 ms; một máy hoặc skid"),
        pg.span("Fast discrete logic, robust, cheap, stand-alone.", "Logic rời rạc nhanh, bền, rẻ, độc lập."),
        pg.span("Packaging lines, compressors, water skids.", "Dây chuyền đóng gói, máy nén, skid nước."),
        pg.span("100–500 ms; plant-wide", "100–500 ms; toàn nhà máy"),
        pg.span("Integrated engineering, history, alarms, redundancy by design.", "Kỹ thuật tích hợp, lịch sử, cảnh báo, dự phòng theo thiết kế."),
        pg.span("Refineries, petrochemical, large continuous plant.", "Nhà máy lọc dầu, hóa dầu, nhà máy liên tục lớn."),
        pg.span("0.1–1 s; hundreds of km", "0,1–1 s; hàng trăm km"),
        pg.span("Geographic distribution, telemetry over WAN or radio.", "Phân tán địa lý, telemetry qua WAN hoặc vô tuyến."),
        pg.span("Water networks, pipelines, power distribution.", "Mạng cấp nước, tuyến ống, phân phối điện."),
        pg.span("1–10 ms + cloud analytics", "1–10 ms + phân tích đám mây"),
        pg.span("Local analytics, protocol translation, ML inference.", "Phân tích tại chỗ, chuyển đổi giao thức, suy luận ML."),
        pg.span("Condition monitoring, advanced control pilots.", "Giám sát tình trạng, thử nghiệm điều khiển nâng cao."),
        pg.span("Keep the SIS separate", "Giữ SIS độc lập"),
        pg.p(
            "IEC 61511 requires the safety instrumented system to be independent of the basic process "
            "control system: separate logic solver, separate wiring, separate final elements where "
            "practicable. Sharing a valve between control and shutdown is one of the most common and most "
            "serious design errors — the controller can drive the valve to the unsafe position just "
            "before the trip needs it.",
            "IEC 61511 yêu cầu hệ thống an toàn độc lập với hệ điều khiển quá trình cơ bản: bộ xử lý logic "
            "riêng, đấu dây riêng, phần tử chấp hành riêng khi có thể. Dùng chung một van giữa điều khiển "
            "và cắt an toàn là một trong những lỗi thiết kế phổ biến và nghiêm trọng nhất — bộ điều khiển "
            "có thể đẩy van đến vị trí không an toàn ngay trước khi cần cắt.",
        ),
    )
    body += section_close()

    body += """
<section class="sec">
  <div class="wrap">
    <div class="nextprev">
      <a href="instruments.html"><span class="k">%s</span>%s</a>
      <a href="comparison.html" style="text-align:right"><span class="k">%s</span>%s</a>
    </div>
  </div>
</section>
""" % (
        pg.span("Back", "Quay lại"),
        pg.span("Instrument reference", "Danh mục thiết bị"),
        pg.span("Next", "Tiếp"),
        pg.span("Process vs geotechnical", "Quá trình vs địa kỹ thuật"),
    )

    write("control.html", render(pg, body, "control.html"))
