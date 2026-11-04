# -*- coding: utf-8 -*-
"""Handbook Chapter 37 — Voltage (Điện áp).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch37.py
"""
import os

from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch37-voltage"
TITLE_EN = "Voltage"
TITLE_VI = "Điện áp"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


# ----------------------------------------------------------------- inline art
def _svg_loading():
    return ('<svg viewBox="0 0 520 220" role="img" aria-label="Von ke noi song song">'
            '<style>.w{stroke:#2a2a2a;stroke-width:2;fill:none}'
            '.t{font:12px Inter,Helvetica,sans-serif;fill:#111}'
            '.d{stroke:#b45309;stroke-width:2;fill:none}</style>'
            '<circle cx="70" cy="110" r="28" class="w"/><text x="70" y="115" text-anchor="middle" class="t">E</text>'
            '<line x1="98" y1="110" x2="200" y2="110" class="w"/>'
            '<line x1="200" y1="40" x2="200" y2="180" class="w"/>'
            '<line x1="320" y1="40" x2="320" y2="180" class="w"/>'
            '<line x1="200" y1="110" x2="320" y2="110" class="w"/>'
            '<line x1="98" y1="110" x2="70" y2="110" class="w"/>'
            '<line x1="320" y1="110" x2="450" y2="110" class="w"/>'
            '<circle cx="450" cy="110" r="28" class="w"/><text x="450" y="115" text-anchor="middle" class="t">−</text>'
            '<line x1="200" y1="40" x2="320" y2="40" class="d"/>'
            '<text x="260" y="32" text-anchor="middle" class="t">Rₛ (nguồn)</text>'
            '<line x1="200" y1="180" x2="320" y2="180" class="d"/>'
            '<text x="260" y="200" text-anchor="middle" class="t">Rʟ (tải) // Rᵥ (von kế)</text>'
            '<text x="260" y="130" text-anchor="middle" class="t">V = I·Rʟ</text>'
            '</svg>')


FIGS = {
    1: (_svg_loading(),
         "Hình 37.1 · Vôn kế nối song song với tải làm thay đổi phân bố điện trở của mạch.",
         "Figure 37.1 · A voltmeter in parallel with the load alters the circuit resistance.",
         "Sơ đồ vôn kế song song", "Voltmeter parallel diagram"),
}


def fig(n, lang="vi"):
    if n not in FIGS:
        return ""
    svg, cap_vi, cap_en, _av, _ae = FIGS[n]
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-37-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
            % (n, svg, cap))


def p(t):
    return "<p>%s</p>" % t


def h2(t, en=""):
    return '<h2>%s%s</h2>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h3(t, en=""):
    return '<h3>%s%s</h3>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def eq(body, num=""):
    if not num:
        return '<div class="eq">%s</div>' % body
    return '<div class="eq"><span class="n">(%s)</span>%s</div>' % (num, body)


def table(head, rows, cap):
    th = "".join("<th>%s</th>" % c for c in head)
    tr = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table class="tbl"><thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>' % (th, tr, cap))


# ---------------------------------------------------------------- Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Điện áp (voltage), hay hiệu điện thế (potential difference), là công cần thiết để dịch chuyển "
        "một đơn vị điện tích giữa hai điểm trong một trường điện. Nó là một trong những đại lượng điện "
        "từ cơ bản nhất và được đo trong hầu hết mọi hệ thống điện và điện tử. Đơn vị SI là vôn (V); "
        "các bội và ước thường gặp là kilôvôn (kV = 10³ V), milivôn (mV = 10⁻³ V), micrôvôn (µV = 10⁻⁶ V) "
        "và nanôvôn (nV = 10⁻⁹ V). Dải đo thực tế trải rộng mười mấy bậc — từ vài nanôvôn trong đo tín "
        "hiệu sinh học đến hàng trăm kilôvôn trong truyền tải điện năng."))
    b.append(p(
        "Một vôn kế (voltmeter) đo điện áp bằng cách nối hai đầu vào của nó song song với hai điểm cần "
        "đo. Vì nối song song, bất kỳ thiết bị đo nào cũng rút một dòng điện nhỏ từ mạch — điều này dẫn "
        "đến <b>hiệu ứng tải</b> (loading effect), sai số hệ thống đặc trưng của phép đo điện áp."))

    b.append(h2("37.1 Hiệu ứng tải của vôn kế", "Voltmeter Loading"))
    b.append(p(
        "Xét một nguồn có điện trở trong Rₛ cấp cho tải Rʟ (Hình 37.1). Không có vôn kế, điện áp trên "
        "tải là V₀ = E·Rʟ/(Rₛ+Rʟ). Khi nối vôn kế có trở kháng vào Rᵥ song song với Rʟ, điện trở tương "
        "đương của nhánh tải trở thành R′ʟ = Rʟ∥Rᵥ, và điện áp đo được là:"))
    b.append(eq("V = E · R′ʟ / (Rₛ + R′ʟ) ,  với  R′ʟ = (Rʟ·Rᵥ)/(Rʟ + Rᵥ)"))
    b.append(p(
        "Sai số tương đối do tải gây ra xấp xỉ −Rʟ/(Rᵥ+Rʟ) khi Rₛ ≪ Rʟ, và nói chung tỉ lệ nghịch với "
        "Rᵥ. Để sai số dưới 1%, trở kháng vào của vôn kế phải lớn hơn khoảng 100 lần trở kháng tải; để "
        "sai số dưới 0,1% thì phải lớn hơn 1000 lần. Đây là lý do vôn kế điện tử (input impedance 1–10 MΩ, "
        "thậm chí 1 GΩ trở lên) thay thế hầu hết vôn kế kiểu động cơ (moving-coil) có trở kháng vài kΩ/V."))
    b.append(fig(1))

    b.append(h2("37.2 Vôn kế tương tự và vôn kế điện tử", "Analog and Electronic Voltmeters"))
    b.append(p(
        "Vôn kế kiểu động cơ (D'Arsonval) là một ampe kế dòng điện một chiều nối qua trở chia (multiplier "
        "resistor) Rₘ sao cho dòng full-scale I_g sinh ra điện áp full-scale V_g = I_g(R_g+Rₘ). Độ nhạy "
        "thường được cho bằng Ω/V; một đồng hồ 20 kΩ/V đọc 10 V sẽ có trở kháng 200 kΩ. Hạn chế lớn là "
        "trở kháng vào thay đổi theo thang đo và khá thấp so với mạch hiện đại."))
    b.append(p(
        "Vôn kế điện tử dùng bộ khuếch đại thuật toán (op-amp) có trở kháng vào rất cao (FET input, "
        "10⁶–10⁹ Ω) và dòng rút cực nhỏ (pA–nA). Bộ khuếch đại theo cấu hình đệm (voltage follower) cách "
        "ly vôn kế khỏi mạch đo, giảm hiệu ứng tải đến mức không đáng kể. Đầu ra khuếch đại được chỉ thị "
        "bằng đồng hồ tương tự hoặc — phổ biến nhất hiện nay — đưa vào bộ chuyển đổi tương tự–số (ADC) "
        "để hiển thị số."))

    b.append(h2("37.3 Vôn kế số (DMM)", "Digital Voltmeters"))
    b.append(p(
        "Vôn kế số (digital multimeter, DMM) đo điện áp một chiều bằng bộ chuyển đổi slope kép (dual-slope) "
        "hoặc sigma-delta. Nguyên lý slope kép: trong khoảng thời gian cố định T₁, tụ tích điện với dòng "
        "tỉ lệ với V_in; sau đó được xả với dòng chuẩn I_ref và đếm thời gian xả T₂. Vì V_in = V_ref·T₂/T₁, "
        "phép đo chỉ phụ thuộc vào tỉ số thời gian nên loại bỏ sai số của tụ và đồng hồ, cho độ chính xác "
        "cao và triệt tiêu nhiễu mode chung tần số điện lưới. Độ phân giải điển hình 3½–6½ chữ số (0,1% "
        "đến vài ppm), trở kháng vào 10 MΩ, băng thông vài trăm kHz."))
    b.append(p(
        "DMM tự động đổi thang (autoranging) chọn thang đo tối ưu, và dùng đầu vào vi sai (differential) "
        "kết hợp tỉ số triệt mode chung (CMRR) cao để đo điện áp nhỏ giữa hai điểm không cùng điện thế (potential) "
        "với đất."))

    b.append(h2("37.4 Đo điện áp xoay chiều", "AC Voltage Measurement"))
    b.append(p(
        "Điện áp xoay chiều (AC) được đặc trưng bởi biên độ đỉnh (V_peak), giá trị hiệu dụng (RMS, "
        "V_rms = V_peak/√2 với sóng sine), và giá trị trung bình chỉnh lưu. Vôn kế đáp ứng trung bình "
        "(average-responding) chỉ thị chính xác giá trị RMS <i>chỉ với sóng sine</i>; với sóng méo (hình "
        "thang, tam giác, bậc) chúng đọc sai đáng kể. Vôn kế RMS thực (true-RMS) dùng bộ hiệu chỉnh RMS "
        "hay chuyển đổi nhiệt/ích phân số bình phương để đo đúng công suất nhiệt tương đương của mọi dạng "
        "sóng. Công thức RMS tổng quát:"))
    b.append(eq("V_rms = √( (1/T) ∫₀ᵀ v²(t) dt )"))
    b.append(p(
        "Đo AC ở tần số cao cần đầu vào trở kháng cao và băng thông rộng; các đầu dò (probe) bù tần (compensated "
        "10× probe) mở rộng dải đến hàng chục MHz với tải thấp lên mạch. Đo AC ở tần số thấp hoặc gần một chiều "
        "(VLF) dùng khóa đồng bộ (chopper/lock-in) để tách tín hiệu khỏi nhiễu 1/f."))

    b.append(h2("37.5 Phương pháp so sánh không (null method)", "Null (Potentiometer) Method"))
    b.append(p(
        "Để đạt độ chính xác cao nhất, người ta dùng phương pháp so sánh không với một điện áp chuẩn đã "
        "hiệu chuẩn. Một cầu cân bằng (potentiometer) so sánh điện áp cần đo với điện áp rơi trên một trở "
        "chuẩn được cấp bởi nguồn ổn định. Khi vôn kế chỉ thị không (null), không dòng chảy qua mạch đo, "
        "nghĩa là không có hiệu ứng tải — độ chính xác chỉ giới hạn bởi trở chuẩn và nguồn tham chiếu "
        "(thường là điện trở chuẩn và nguồn tham chiếu bandgap/zener). Đây là cơ sở của hiệu chuẩn vôn kế "
        "cấp phòng thí nghiệm."))

    b.append(h2("37.6 Đo điện áp cao và điện áp thấp", "High- and Low-Voltage Measurement"))
    b.append(p(
        "<b>Điện áp cao (HV, kV–MV):</b> không nối vôn kế trực tiếp; dùng bộ chia điện áp (voltage divider) "
        "kiểu trở hoặc tụ để hạ tỉ lệ xuống dải vôn kế an toàn. Bộ chia trở (high-megohm series resistor) "
        "dùng cho DC và tần thấp; bộ chia tụ (capacitive divider) cho xung và cao tần. Đầu vào phải cách "
        "điện đủ bậc và có bảo vệ quá áp."))
    b.append(p(
        "<b>Điện áp thấp (µV–mV):</b> nhiễu và trôi nhiệt (thermal EMF) thống trị. Kỹ thuật gồm: che chắn "
        "(shielding) vỏ kín nối đất, <b>giữ (guarding)</b> để triệt dòng rò qua trở cách điện, che chắn kép "
        "(double shielding), bù offset, và lấy trung bình nhiều lần (averaging) kết hợp lọc thông thấp. "
        "Đầu nối phải là loại bù nhiệt (copper–constantan) và hàn lạnh để triệt sức điện động nhiệt."))

    b.append(h2("37.7 Các thông số của vôn kế", "Voltmeter Specifications"))
    b.append(table(
        ["Thông số", "Ý nghĩa", "Điển hình"],
        [["Trở kháng vào (input Z)", "Mức cách ly mạch đo; cao → ít tải", "10 MΩ (DC), 1–10 MΩ (AC)"],
         ["Độ phân giải (resolution)", "Bước đọc nhỏ nhất", "1 µV – 100 µV"],
         ["Độ chính xác (accuracy)", "Sai số so với giá trị thực", "0,01% – 0,1% full-scale"],
         ["Dải đo (range)", "Từ mV đến kV (qua đầu dò)", "100 mV – 1 kV"],
         ["Băng thông (bandwidth)", "Giới hạn tần số đo AC", "DC – vài trăm kHz (DC), MHz (đầu dò)"],
         ["CMRR", "Triệt nhiễu mode chung", "> 80 dB"],
         ["Loại đáp ứng", "Average hay true-RMS", "True-RMS cho mọi dạng sóng"]],
        "Bảng 37.1 · Các thông số chính của vôn kế số và điện tử."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Đo điện áp là đo hiệu điện thế giữa hai điểm bằng vôn kế nối song song. Sai số chủ yếu là hiệu "
        "ứng tải, giảm bằng trở kháng vào cao (vôn kế điện tử/DMM). DMM dùng ADC slope kép cho độ chính "
        "xác cao; true-RMS cần thiết cho sóng méo. Điện áp cao dùng bộ chia, điện áp thấp dùng che chắn, "
        "giữ và bù nhiệt. Phương pháp null cho độ chính xác chuẩn phòng thí nghiệm."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (BASE_VI, BASE_VI))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "This is the companion to the Vietnamese translation of Chapter 37. The figures and tables of the "
        "source are reproduced below; the translation prose is not repeated here."))
    b.append(p(
        "Voltage (potential difference) is the work per unit charge to move between two points in an "
        "electric field — one of the most measured electromagnetic quantities. The SI unit is the volt "
        "(V); practical ranges span nV (bio-signals) to hundreds of kV (power transmission). A voltmeter "
        "connects in parallel with the points of interest, so it always draws some current — the "
        "<i>loading effect</i>."))
    b.append(p(
        "Loading: with source resistance Rₛ feeding load Rʟ, the no-meter voltage is V₀ = E·Rʟ/(Rₛ+Rʟ). "
        "Adding a meter of input resistance Rᵥ in parallel gives R′ʟ = Rʟ∥Rᵥ and V = E·R′ʟ/(Rₛ+R′ʟ). The "
        "relative error is roughly −Rʟ/(Rᵥ+Rʟ); keeping error under 1% needs Rᵥ ≳ 100·Rʟ, under 0.1% needs "
        "Rᵥ ≳ 1000·Rʟ. This is why electronic voltmeters (1–10 MΩ, up to GΩ) replaced moving-coil meters "
        "(kΩ/V sensitivity)."))
    b.append(fig(1, "en"))
    b.append(p(
        "Analog meters scale a moving-coil movement with a series multiplier resistor (sensitivity in "
        "Ω/V). Electronic voltmeters use an op-amp voltage follower for very high input impedance (10⁶–10⁹ Ω) "
        "and pA–nA input current, isolating the meter from the circuit. Digital voltmeters (DMMs) use a "
        "dual-slope or sigma-delta ADC: V_in = V_ref·T₂/T₁ makes the reading depend only on a time ratio, "
        "rejecting capacitor and clock errors and line-frequency common-mode noise. Resolution is 3½–6½ "
        "digits, input Z ≈ 10 MΩ."))
    b.append(p(
        "AC voltage is characterized by peak, RMS (V_rms = V_peak/√2 for sine) and rectified-average. "
        "Average-responding meters read RMS correctly only for sine; true-RMS meters measure the thermal "
        "equivalent of any waveform via V_rms = √(1/T ∫ v²(t)dt). High-voltage measurement uses resistive "
        "or capacitive voltage dividers; low-voltage (µV–mV) measurement needs shielding, guarding, "
        "thermal-EMF compensation, and averaging. The null/potentiometer method gives laboratory accuracy "
        "by balancing against a calibrated reference with zero current drawn."))
    b.append(table(
        ["Parameter", "Meaning", "Typical"],
        [["Input impedance", "Circuit isolation; high = less loading", "10 MΩ (DC)"],
         ["Resolution", "Smallest readable step", "1–100 µV"],
         ["Accuracy", "Error vs. true value", "0.01%–0.1% FS"],
         ["Range", "mV to kV (via probes)", "100 mV – 1 kV"],
         ["Bandwidth", "AC frequency limit", "DC – hundreds of kHz"],
         ["CMRR", "Common-mode rejection", "> 80 dB"],
         ["Response", "Average or true-RMS", "True-RMS preferred"]],
        "Table 37.1 · Key voltmeter specifications."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Contents</span>Handbook</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Contents →</span>Handbook</a></div>'
             % (BASE_EN, BASE_EN))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 37 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 37 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 37 “Điện áp” — hiệu ứng tải vôn kế, vôn kế điện tử/DMM, slope "
            "kép, true-RMS, phương pháp null, đo điện áp cao/thấp, Bảng 37.1." if vi else
            "Companion to Chapter 37 of the CRC Measurement Handbook — voltage measurement: loading, "
            "electronic/DMM voltmeters, dual-slope ADC, true-RMS, null method, HV/LV, Table 37.1.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 37' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 37' % BASE_EN)
    meta = ("Chương 37 · điện áp · hiệu ứng tải · DMM slope kép · true-RMS · 1 hình, 1 bảng" if vi
            else "Chapter 37 · voltage · loading · dual-slope DMM · true-RMS · 1 figure, 1 table")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div></article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE, meta,
               body_vi() if vi else body_en()))
    return head(lang, title, desc) + header(lang, switch) + body + footer(lang)


def main():
    pairs = [("en", os.path.join(ROOT, "books", "read", SLUG, CSLUG, "index.html")),
             ("vi", os.path.join(ROOT, "vi", "books", "read", SLUG, CSLUG, "index.html"))]
    for lang, path in pairs:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        page = build(lang)
        open(path, "w", encoding="utf-8").write(page)
        print("wrote %s  %d kB" % (path, len(page) // 1024))


if __name__ == "__main__":
    main()
