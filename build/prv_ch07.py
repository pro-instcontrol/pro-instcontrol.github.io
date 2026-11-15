# -*- coding: utf-8 -*-
"""Book 4, Chapter 7 — Engineering Support Information (EN/VI bilingual).

Redrawn vector figures (build/prvfig.py) and parsed reference tables
(build/prv_ch07_tbl.py) are embedded here alongside the handbook's
explanatory notes, so the companion reader reproduces Crosby Technical
Publication TP-V300, Chapter 7 (pages 7-2 through 7-31) with both
Vietnamese and English prose.
"""

from prv_common import (eq, fig, h2, h3, note, p, table, ul)
import prv_ch07_tbl as D
import prvfig as F

PAGES_SRC = 30          # source pages 7-2 … 7-31
BYLINE = "Crosby Valve Inc. · Technical Document TP-V300"
TITLE_EN = "Engineering Support Information"
TITLE_VI = "Thông tin hỗ trợ kỹ thuật"


# ---- equation helpers (self-contained, no global CSS dependency) -------------
def _sq(x):
    return '&#8730;<span style="border-top:1px solid currentColor;padding:0 .18rem;">%s</span>' % x


def _fr(num, den):
    return ('<span style="display:inline-block;text-align:center;vertical-align:middle;'
            'margin:0 .3rem;">'
            '<span style="display:block;border-bottom:1px solid currentColor;padding:0 .4rem;">%s</span>'
            '<span style="display:block;padding:0 .4rem;">%s</span></span>' % (num, den))


def _sub(x):
    return '<sub>%s</sub>' % x


def _hdr(vi, en, lang):
    """Pick the Vietnamese or English column header set."""
    return vi if lang == "vi" else en


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 7.</b> Z — hệ số nén · K<sub>b</sub> — hệ số hiệu "
                "chỉnh áp suất ngược cho khí/hơi · K<sub>w</sub> — hệ số hiệu chỉnh áp suất "
                "ngược cho chất lỏng · K<sub>n</sub> — hệ số hiệu chỉnh hơi nước áp suất cao · "
                "K<sub>v</sub> — hệ số hiệu chỉnh độ nhớt · K<sub>sh</sub> — hệ số hiệu chỉnh "
                "quá nhiệt · k — tỷ số nhiệt dung riêng · C — hệ số định cỡ · K<sub>r</sub> — "
                "hệ số hiệu chỉnh tỷ số nhiệt dung riêng cho lực phản ứng · diện tích xả hiệu dụng.")
    return ("<b>Key terms.</b> Z — compressibility factor · K<sub>b</sub> — back-pressure "
            "correction factor (gas/vapor) · K<sub>w</sub> — back-pressure correction factor "
            "(liquid) · K<sub>n</sub> — high-pressure steam factor · K<sub>v</sub> — viscosity "
            "correction factor · K<sub>sh</sub> — superheat correction factor · k — ratio of "
            "specific heats · C — sizing coefficient · K<sub>r</sub> — specific-heat correction "
            "for reaction force · effective discharge area.")


# ---- reusable table builders (bilingual headers) ----------------------------
def _t71(lang):
    hdr = _hdr(["Tỷ số áp suất ngược Pb/P1 (%)", "Hệ số Kb"],
               ["Back-pressure ratio Pb/P1 (%)", "Factor Kb"], lang)
    cap = ("Bảng T7-1 — Hệ số hiệu chỉnh năng lực Kb cho van thường (áp suất ngược không đổi), "
           "khí và hơi." if lang == "vi" else
           "Table T7-1 — Capacity correction factor Kb for conventional valves (constant back "
           "pressure), gas and vapor.")
    return table(hdr, D.T71, caption=cap)


def _t72(lang):
    temps = ["400°F", "450°F", "500°F", "550°F", "600°F", "650°F", "700°F", "750°F",
             "800°F", "850°F", "900°F", "950°F", "1000°F", "1050°F"]
    lead = (_hdr(["Áp suất xả (psia)", "bara", "kPaa"],
                 ["Relieving pressure (psia)", "bara", "kPaa"], lang))
    hdr = lead + temps
    cap = ("Bảng T7-2 — Hệ số hiệu chỉnh quá nhiệt Ksh (áp suất xả × nhiệt độ hơi tổng cộng). "
           "Để trống nghĩa là không áp dụng." if lang == "vi" else
           "Table T7-2 — Superheat correction factor Ksh (relieving pressure × total steam "
           "temperature). Blank = not applicable.")
    return table(hdr, D.T72, caption=cap, cls="tbl wide")


def _t73(lang):
    hdr = _hdr(["Tỷ số nhiệt dung riêng k", "Hệ số C"],
               ["Ratio of specific heats k", "Coefficient C"], lang)
    cap = ("Bảng T7-3 — Tỷ số nhiệt dung riêng k và hệ số C tương ứng." if lang == "vi" else
           "Table T7-3 — Ratio of specific heats k and the corresponding coefficient C.")
    return table(hdr, D.T73, caption=cap)


def _t74(lang):
    hdr = _hdr(["Mức tiếng ồn (dB)", "Tham chiếu"],
               ["Sound level (dB)", "Reference"], lang)
    cap = ("Bảng T7-4 — Mức tiếng ồn tương đối để tham khảo." if lang == "vi" else
           "Table T7-4 — Relative noise levels for reference.")
    return table(hdr, D.T74, caption=cap)


def _t75(lang):
    hdr = _hdr(["Tỷ số nhiệt dung riêng k", "Hệ số Kr"],
               ["Ratio of specific heats k", "Factor Kr"], lang)
    cap = ("Bảng T7-5 — Hệ số hiệu chỉnh K<sub>r</sub> cho tỷ số nhiệt dung riêng khác 1,4 "
           "(dùng cho công thức lực phản ứng khí/hơi)." if lang == "vi" else
           "Table T7-5 — Specific-heat correction factor K<sub>r</sub> for k ≠ 1.4 (gas/vapor "
           "reaction-force formula only).")
    return table(hdr, D.T75, caption=cap)


def _t76(lang):
    hdr = _hdr(["Loại thiết bị", "Cách nhiệt (BTU/h·ft²·°F)", "Hệ số F"],
               ["Equipment type", "Insulation (BTU/hr·ft²·°F)", "Factor F"], lang)
    cap = ("Bảng T7-6 — Hệ số môi trường F (API RP 520, mục D.5.1)." if lang == "vi" else
           "Table T7-6 — Environmental factor F (API RP 520, Par. D.5.1).")
    return table(hdr, D.T76, caption=cap)


def _t77(lang):
    hdr = _hdr(["Khí hoặc hơi", "KLPT", "k", "C*", "Tỷ trọng", "Áp suất tới hạn (psia)",
                "Nhiệt độ tới hạn (°R)"],
               ["Gas or vapor", "Mol. wt", "k", "C*", "Sp. gr.", "Crit. press. (psia)",
                "Crit. temp (°R)"], lang)
    cap = ("Bảng T7-7 — Tính chất điển hình của các khí (nếu không biết C, dùng C = 315; nếu biết "
           "k, xem trang 7-9 để tính C)." if lang == "vi" else
           "Table T7-7 — Typical properties of gases (* use C = 315 if unknown; if k is known, "
           "see page 7-9 to find C).")
    return table(hdr, D.T77, caption=cap, cls="tbl wide")


def _t78(lang):
    hdr = _hdr(["Áp suất (psia)", "kPaa", "bara", "Nhiệt độ °F", "Nhiệt độ °C"],
               ["Pressure (psia)", "kPaa", "bara", "Temp °F", "Temp °C"], lang)
    cap = ("Bảng T7-8 — Áp suất/temperature bão hòa của nước." if lang == "vi" else
           "Table T7-8 — Water saturation pressure / temperature.")
    return table(hdr, D.T78, caption=cap, cls="tbl wide")


def _t79(lang):
    blocks = []
    props_vi = ["Đường kính mặt bích", "Đường kính mặt lồi", "Chiều dày mặt bích (tối thiểu)",
                "Đường kính vành bu lông", "Số lượng bu lông", "Đường kính lỗ bu lông"]
    props_en = ["Flange diameter", "Raised face diameter", "Flange thickness, min.",
                "Bolt circle diameter", "Number of bolts", "Bolt hole diameter"]
    for cls, d in D.T79.items():
        hdr = (_hdr(["Thông số"], ["Property"], lang) + d["sizes"])
        props = props_vi if lang == "vi" else props_en
        rows = [[props[i]] + r for i, r in enumerate(d["rows"])]
        cap = ("Bảng T7-9 — Kích thước mặt bích ANSI %s (đơn vị inch)." % cls
               if lang == "vi" else
               "Table T7-9 — ANSI %s flange dimensions (inches)." % cls)
        blocks.append(table(hdr, rows, caption=cap, cls="tbl wide"))
    return "".join(blocks)


def _t710(lang):
    hdr = _hdr(["Nhân A", "với B", "thu được C"],
               ["Multiply A", "by B", "to obtain C"], lang)
    cap = ("Bảng T7-10 — Hệ số tương đương và chuyển đổi đơn vị. Nhân cột A với cột B được cột C; "
           "chia cột C cho cột B được cột A." if lang == "vi" else
           "Table T7-10 — Equivalents and conversion factors. Multiply column A by B to get C; "
           "divide C by B to get A.")
    return table(hdr, D.T710, caption=cap, cls="tbl wide")


def _orifice(lang, rows, title_vi, title_en):
    hdr = _hdr(["Ký hiệu", "Diện tích (in²)", "Diện tích (mm²)"],
               ["Orifice", "Area (in²)", "Area (mm²)"], lang)
    cap = (title_vi if lang == "vi" else title_en)
    return table(hdr, [list(r[:3]) for r in rows], caption=cap, cls="tbl")


# ============================================================================
#  VIETNAMESE BODY
# ============================================================================
def body_vi():
    b = []
    b.append(p("Chương này tập hợp các số liệu, biểu đồ và bảng dùng để hỗ trợ tính toán và tra "
               "cứu trong quá trình định cỡ van xả áp Crosby. Nội dung bao gồm các hệ số hiệu "
               "chỉnh (Z, K<sub>b</sub>, K<sub>w</sub>, K<sub>n</sub>, K<sub>v</sub>, K<sub>sh</sub>), "
               "tỷ số nhiệt dung riêng k và hệ số C, tính toán mức tiếng ồn và lực phản ứng, định "
               "cỡ cho điều kiện hỏa hoạn, các bảng tính chất khí, bảng bão hòa nước, kích thước "
               "mặt bích ANSI, hệ số chuyển đổi đơn vị và diện tích lỗ xả hiệu dụng của van."))
    b.append(h3("Mục lục dữ liệu chương 7", "Chapter 7 data listing"))
    b.append(ul([
        "Hệ số nén Z (trang 7-2)",
        "Hệ số hiệu chỉnh áp suất ngược (trang 7-3 đến 7-5)",
        "Hệ số hiệu chỉnh hơi nước áp suất cao K<sub>n</sub> (trang 7-6)",
        "Hệ số hiệu chỉnh độ nhớt K<sub>v</sub> (trang 7-7)",
        "Hệ số hiệu chỉnh quá nhiệt K<sub>sh</sub> (trang 7-8)",
        "Tỷ số nhiệt dung riêng k và hệ số C (trang 7-9)",
        "Tính toán mức tiếng ồn (trang 7-10, 7-11)",
        "Lực phản ứng (trang 7-12 đến 7-16)",
        "Điều kiện hỏa hoạn — định cỡ chất lỏng bay hơi (trang 7-17 đến 7-23)",
        "Điều kiện hỏa hoạn — định cỡ bồn chứa khí/hơi (trang 7-24)",
        "Dòng hai pha và dòng sôi (trang 7-25)",
        "Tính chất điển hình của khí (trang 7-26)",
        "Áp suất/temperature bão hòa của nước (trang 7-27)",
        "Kích thước mặt bích ANSI (trang 7-28)",
        "Hệ số tương đương và chuyển đổi (trang 7-29)",
        "Diện tích lỗ xả — van lò xo Crosby (trang 7-30)",
        "Diện tích lỗ xả — van vận hành pilot Crosby (trang 7-31)",
    ]))

    # ---- Z --------------------------------------------------------------------
    b.append(h2("Hệ số nén Z", "Compressibility Factor, Z"))
    b.append(p("Hệ số nén Z dùng để hiệu chỉnh phương trình trạng thái khí lý tưởng khi tính lưu "
               "lượng khối lượng hoặc thể tích ở điều kiện xả. Đối với khí thực, mật độ tại đầu "
               "vào van phụ thuộc vào tỷ số áp suất suy giảm P<sub>r</sub> = P/P<sub>c</sub> và "
               "nhiệt độ quy giản T<sub>r</sub> = T/T<sub>c</sub> (P<sub>c</sub>, T<sub>c</sub> "
               "lấy từ Bảng T7-7). Nếu không biết Z, dùng Z = 1,0."))
    b.append(fig(1, F.fig_f71()))

    # ---- Back pressure --------------------------------------------------------
    b.append(h2("Hệ số hiệu chỉnh áp suất ngược", "Capacity Correction Factors for Back Pressure"))
    b.append(p("Áp suất ngược là áp suất tại cửa xả của van xả áp do áp suất trong hệ thống xả "
               "hoặc do sự sôi (flashing) trong thân van. Nếu không xem xét đúng ảnh hưởng của áp "
               "suất ngược, van có thể bị: (1) thay đổi áp suất mở, (2) thay đổi áp suất đóng, "
               "(3) giảm năng lực xả, và (4) mất ổn định động."))
    b.append(h3("Áp suất ngược trong công nghệ", "Back pressure in process service"))
    b.append(ul([
        "<b>Áp suất ngược tạo ra (built-up):</b> áp suất cộng thêm tại cửa xả do trở lực của hệ "
        "thống xả và đường ống, hoặc do sự sôi trong thân van.",
        "<b>Áp suất ngược chép lên (superimposed):</b> áp suất tĩnh có sẵn tại cửa xả khi van cần "
        "hoạt động, do áp suất từ các nguồn khác trong hệ thống xả.",
    ]))
    b.append(p("Ảnh hưởng của áp suất ngược phụ thuộc vào sự kết hợp của nhiều điều kiện: áp suất "
               "ngược không đổi hay biến thiên; van đóng hay đang xả; pha chất lưu (khí/hơi hay "
               "chất lỏng); và kết cấu van (bellows/cân bằng piston hay van thường)."))
    b.append(h3("Van thường (Style JOS, Series 800/900)", "Conventional Valves"))
    b.append(p("<b>Van đóng:</b> áp suất ngược chép lên không đổi làm tăng áp suất mở của van một "
               "lượng bằng áp suất ngược, nên thiết lập lò xo (áp suất thử chênh lệch nguội, CDTP) "
               "được tính bằng áp suất thiết lập trừ đi áp suất ngược. Áp suất ngược chép lên biến "
               "thiên làm áp suất mở dao động — thường nên dùng van cân bằng. <b>Van mở và xả:</b> "
               "áp suất ngược tạo ra làm giảm lực nâng giữ van mở; phải giới hạn không quá 10% áp "
               "suất thiết lập. Nếu vượt, phải dùng van cân bằng."))
    b.append(p("Đối với khí và hơi (kể cả hơi nước), năng lực không bị ảnh hưởng nếu áp suất ngược "
               "nhỏ hơn áp suất tới hạn của chất lưu (thường lấy bằng 55% áp suất xả tuyệt đối). "
               "Khi áp suất ngược vượt áp suất tới hạn, phải áp dụng hệ số hiệu chỉnh dòng K<sub>b</sub> "
               "(Bảng T7-1). Nếu nhỏ hơn, K<sub>b</sub> = 1,00. Đối với chất lỏng, van thường ở "
               "dịch vụ áp suất ngược không cần hệ số hiệu chỉnh: K<sub>w</sub> = 1."))
    b.append(_t71("vi"))
    b.append(h3("Van cân bằng (Style JBS, Series BP)", "Balanced Valves"))
    b.append(p("Vì diện tích hiệu dụng của màng (bellows) hoặc piston tương đương diện tích ghế, "
               "áp suất thiết lập của van cân bằng không bị ảnh hưởng bởi áp suất ngược — van luôn "
               "mở trong dung sai áp suất thiết lập của ASME. Tuy nhiên, khi van mở và xả, áp suất "
               "ngược từ từ làm giảm lực nâng, nên phải dùng hệ số hiệu chỉnh dòng cho áp suất ngược "
               "kỳ vọng lớn nhất khi tính diện tích yêu cầu."))
    b.append(p("Khí và hơi: dùng hệ số K<sub>b</sub> từ Hình F7-2 để bù ảnh hưởng áp suất ngược "
               "với van Style JBS hoặc Series BP. Chất lỏng: dùng hệ số K<sub>w</sub> từ Hình F7-3. "
               "Khi điều kiện áp suất ngược không áp dụng, K<sub>b</sub> = K<sub>w</sub> = 1,00. "
               "Với áp suất ngược vượt giới hạn Hình F7-2/F7-3, hãy liên hệ đại diện Crosby."))
    b.append(fig(2, F.fig_f72()))
    b.append(fig(3, F.fig_f73()))
    b.append(h3("Van vận hành pilot", "Pilot Operated Valves"))
    b.append(p("<b>Style JPV (tác động nhanh):</b> áp suất ngược không ảnh hưởng đến áp suất thiết "
               "lập hay năng lực xả, trừ khi dòng ở chế độ dưới tới hạn (tỷ số áp suất ngược tuyệt "
               "đối / áp suất xả tuyệt đối vượt 55%); khi đó phải áp dụng K<sub>b</sub> (Bảng T7-1). "
               "Nếu tỷ số dưới 55%, K<sub>b</sub> = 1,00. <b>Style JPVM (điều biến):</b> áp suất "
               "thiết lập và khả năng vận hành không bị ảnh hưởng bởi áp suất ngược đến 70% áp suất "
               "thiết lập (cần van chống chảy ngược ngược nếu áp suất ngược có thể vượt áp suất đầu "
               "vào). Năng lực bị ảnh hưởng khi dòng dưới tới hạn (tỷ số vượt 55%); khi đó áp dụng "
               "K<sub>b</sub> (Bảng T7-1), còn dưới 55% thì K<sub>b</sub> = 1,00."))

    # ---- Kn -------------------------------------------------------------------
    b.append(h2("Hệ số hiệu chỉnh hơi nước áp suất cao K<sub>n</sub>",
                "Capacity Correction Factor for High Pressure Steam, Kn"))
    b.append(p("Khi áp suất xả của hơi nước vượt 10.340 kPaa (1.500 psig), ASME yêu cầu một hệ số "
               "hiệu chỉnh bổ sung K<sub>n</sub> cho hơi bão hòa khô. Hình F7-4 cho giá trị K<sub>n</sub> "
               "theo áp suất xả. Xem Chương 6 để biết cách dùng K<sub>n</sub> trong công thức định "
               "cỡ hơi nước."))
    b.append(fig(4, F.fig_f74()))

    # ---- Kv -------------------------------------------------------------------
    b.append(h2("Hệ số hiệu chỉnh độ nhớt K<sub>v</sub>",
                "Capacity Correction Factor for Viscosity, Kv"))
    b.append(p("Khi định cỡ van cho dịch vụ chất lỏng nhớt, trước tiên hãy định cỡ như ứng dụng "
               "không nhớt để có diện tích xả hiệu dụng sơ bộ A. Từ các cỡ lỗ chuẩn của Crosby, "
               "chọn cỡ lỗ lớn hơn kế tiếp và tính số Reynolds R theo công thức dưới, sau đó lấy "
               "hệ số K<sub>v</sub> từ đồ thị (Hình F7-5) để hiệu chỉnh diện tích sơ bộ. Nếu diện "
               "tích đã hiệu chỉnh vượt diện tích lỗ đã chọn, lặp lại với cỡ lỗ lớn hơn."))
    b.append(p("Đơn vị USCS: &nbsp; R = 12.700 · GPM · G / &#8730;A&nbsp;&nbsp; (GPM = lưu lượng "
               "tại nhiệt độ chảy, galông/phút; G = tỷ trọng chất lỏng so với nước = 1,00 ở 70°F; "
               "A = diện tích xả hiệu dụng, in²; U = độ nhớt ở nhiệt độ chảy, giây Saybolt "
               "phổ thông SSU)."))
    b.append(p("Đơn vị mét: &nbsp; R = 85.225 · Q · G / &#8730;A′&nbsp;&nbsp; (Q = lưu lượng, "
               "lít/phút; A′ = diện tích xả hiệu dụng, mm²; µ = độ nhớt tuyệt đối, centipoise)."))
    b.append(fig(5, F.fig_f75()))

    # ---- Ksh ------------------------------------------------------------------
    b.append(h2("Hệ số hiệu chỉnh quá nhiệt K<sub>sh</sub>",
                "Capacity Correction Factor for Superheat, Ksh"))
    b.append(p("Các công thức định cỡ hơi nước (trang 5-6 và 6-6) dựa trên dòng hơi bão hòa khô. "
               "Để định cỡ hơi quá nhiệt, dùng hệ số hiệu chỉnh quá nhiệt K<sub>sh</sub> để hiệu "
               "chỉnh lưu lượng hơi bão hòa tính toán sang hơi quá nhiệt. Với hơi bão hòa, "
               "K<sub>sh</sub> = 1,0. Với hơi quá nhiệt, tra Bảng T7-2 tại áp suất xả yêu cầu và "
               "đọc hệ số dưới cột nhiệt độ hơi tổng cộng."))
    b.append(_t72("vi"))

    # ---- k / C ----------------------------------------------------------------
    b.append(h2("Tỷ số nhiệt dung riêng k và hệ số C",
                "Ratio of Specific Heats, k, and Coefficient, C"))
    b.append(p("Công thức sau đây liên hệ tỷ số nhiệt dung riêng k với hệ số C dùng trong các "
               "phương pháp định cỡ khí và hơi. Hình F7-6 và Bảng T7-3 cung cấp nghiệm tính toán "
               "của công thức này."))
    b.append(eq('C = 520 ' + _fr('&#8730;(k) [2/(k+1)]<sup>(k+1)/(k-1)</sup>', ''), ""))
    b.append(fig(6, F.fig_f76()))
    b.append(_t73("vi"))

    # ---- Noise ----------------------------------------------------------------
    b.append(h2("Tính toán mức tiếng ồn", "Noise Level Calculations"))
    b.append(p("Các công thức sau dùng để tính mức tiếng ồn của khí, hơi và hơi nước do van xả áp "
               "thải ra, bắt nguồn từ API RP 521. Bảng T7-4 liệt kê các mức tiếng ồn tương đối."))
    b.append(eq('L<sub>100</sub> = L + 10&#8201;log<sub>10</sub> (0,29354&#8201;W&#8201;k&#8201;T/M)', ""))
    b.append(ul([
        "L<sub>100</sub> — mức âm tại 100 ft từ điểm xả, đơn vị decibel (dB).",
        "L — cường độ tiếng ồn (mức áp suất âm) tại 100 ft, lấy từ Hình F7-7.",
        "W — năng lực xả cực đại, lb/hr (xem Bảng T7-7 để lấy k, M của chất lưu; với hơi nước "
        "k = 1,3, M = 18 nếu không biết).",
        "T — nhiệt độ tuyệt đối của chất lưu tại đầu vào van, độ Rankine (°F + 460).",
        "M — khối lượng phân tử (Bảng T7-7; với hơi nước M = 18).",
    ]))
    b.append(p("Khi cần mức tiếng ồn ở khoảng cách khác 100 ft, dùng:"))
    b.append(eq('L<sub>p</sub> = L<sub>100</sub> &#8722; 20&#8201;log<sub>10</sub> (r/100)', ""))
    b.append(p("với r là khoảng cách từ điểm xả, ft. Tỷ số áp suất PR = áp suất xả tuyệt đối / "
               "áp suất ngược tuyệt đối, dùng để tra L trong Hình F7-7."))
    b.append(fig(7, F.fig_f77()))
    b.append(_t74("vi"))
    b.append(h3("Ví dụ 1 — Khí/hơi, lưu lượng khối lượng (lb/hr)",
                "Example 1 — Gas/Vapor Mass Flow (lb/hr)"))
    b.append(p("Chất lưu: Khí tự nhiên; áp suất thiết lập: 210 psig; quá áp: 10%; áp suất ngược: "
               "50 psig; nhiệt độ đầu vào: 120°F; khối lượng phân tử: 19,0; hệ số nén: 1; diện "
               "tích chọn: 0,503 in²; tính tại 500 ft. P₁ = 210 + 21 + 14,7 = 245,7 psia; K<sub>b</sub> "
               "= 1,0; C = 344 (Bảng T7-7); K = 0,975. Tính lưu lượng định mức W = 7.502 lb/hr, "
               "T = 580°R, PR = 245,7/(50 + 14,7) = 3,8 → L = 54,5 (Hình F7-7). "
               "L<sub>100</sub> = 103,8 dB; tại 500 ft: L<sub>p</sub> = 89,9 dB."))

    # ---- Reaction forces ------------------------------------------------------
    b.append(h2("Lực phản ứng", "Reaction Forces"))
    b.append(p("Các công thức sau dùng để tính lực phản ứng của van xả áp thải khí, hơi hoặc hơi "
               "nước trực tiếp ra khí quyển không qua đường ống xả. Kết quả phù hợp với API RP 520 "
               "(khí/hơi) và ANSI/ASME B31.1 (hơi nước). Việc xác định lực phản ứng tại cửa xả là "
               "trách nhiệm của người thiết kế bồn và/hoặc đường ống."))
    b.append(h3("Khí và hơi", "Gas/Vapor"))
    b.append(eq('F = C&#8201;K&#8201;A&#8201;P<sub>1</sub> ' + _sq('k/(k+1)') + ' + F<sub>g</sub>', ""))
    b.append(eq('F<sub>g</sub> = ' + _fr('(K&#8201;A&#8201;P<sub>1</sub>&#8201;K<sub>r</sub> &#8722; P<sub>a</sub>)&#8201;A<sub>o</sub>',
                                                              '1,383&#8201;A<sub>o</sub>'), ""))
    b.append(p("Nếu F<sub>g</sub> ≤ 0, lấy F<sub>g</sub> = 0."))
    b.append(h3("Hơi nước", "Steam"))
    b.append(eq('F = ' + _fr('A&#8201;P<sub>1</sub> + F<sub>s</sub>', '1,335'), ""))
    b.append(eq('F<sub>s</sub> = ' + _fr('(A&#8201;P<sub>1</sub> &#8722; P<sub>a</sub>)&#8201;A<sub>o</sub>&#8201;K<sub>n</sub>',
                                                              '1,886&#8201;A<sub>o</sub>'), ""))
    b.append(p("Nếu F<sub>s</sub> ≤ 0, lấy F<sub>s</sub> = 0. Các ký hiệu: F — tổng lực phản ứng tại "
               "điểm xả ra khí quyển (lbf); F<sub>g</sub>, F<sub>s</sub> — thành phần lực tĩnh tại "
               "cửa xả (khí/hơi, hơi nước); C — hệ số từ tỷ số nhiệt dung riêng (Bảng T7-7); K = "
               "0,975; A — diện tích xả hiệu dụng (in²); A<sub>o</sub> — diện tích mặt cắt cửa xả "
               "(in²); P<sub>1</sub> — áp suất xả tuyệt đối (psia); P<sub>a</sub> — áp suất khí "
               "quyển; k — tỷ số nhiệt dung riêng (Bảng T7-7); K<sub>n</sub> — hệ số hơi nước áp "
               "suất cao; K<sub>r</sub> — hiệu chỉnh tỷ số nhiệt dung riêng khác 1,4 (Bảng T7-5)."))
    b.append(_t75("vi"))
    b.append(h3("Ví dụ 1 — Khí/hơi, lưu lượng khối lượng (lb/hr)",
                "Example 1 — Gas/Vapor Mass Flow (lb/hr)"))
    b.append(p("Khí tự nhiên; năng lực yêu cầu: 5.900 lb/hr; áp suất thiết lập: 210 psig; quá áp: "
               "10%; áp suất xả: 245,7 psia; k = 1,27; C = 344; diện tích tính: 0,397 in²; van "
               "chọn: 1-1/2G2-1/2, diện tích 0,503 in². P₁ = 245,7 psia; K<sub>r</sub> = 1,04 "
               "(Bảng T7-5); P<sub>a</sub> = 14,7 psia; A<sub>o</sub> = (2-1/2)²(π/4) = 4,909 in². "
               "F<sub>g</sub> = 18,5 lbf; F = 111,6 lbf."))

    # ---- Fire, wetted ---------------------------------------------------------
    b.append(h2("Điều kiện hỏa hoạn — định cỡ chất lỏng bay hơi (bồn ướt)",
                "Fire Conditions — Sizing for Vaporizing Liquids (Wetted Vessels)"))
    b.append(p("Phương pháp sau (tham chiếu API RP 520) dùng để tính diện tích lỗ yêu cầu cho van "
               "xả áp trên bồn chứa chất lỏng tiếp xúc với hỏa hoạn."))
    b.append(h3("Bước 1 — Tổng diện tích bề mặt ướt", "Step 1. Total wetted surface area"))
    b.append(p("Dùng sơ đồ chọn bồn (Hình F7-13) và sơ đồ logic mức chất lỏng hiệu dụng (Hình F7-12) "
               "để xác định diện tích bề mặt ướt A<sub>wet</sub> (ft²)."))
    b.append(h3("Bước 2 — Tổng nhiệt hấp thụ", "Step 2. Total heat absorption"))
    b.append(p("Khi có nỗ lực chữa cháy kịp thời và thoát nước tốt: &nbsp; Q = 21.000 · F · "
               "A<sub>wet</sub><sup>0,82</sup>. Khi không có: &nbsp; Q = 34.500 · F · "
               "A<sub>wet</sub><sup>0,82</sup>. Với Q (BTU/h) và F là hệ số môi trường (Bảng T7-6)."))
    b.append(_t76("vi"))
    b.append(h3("Bước 3 — Tốc độ bay hơi", "Step 3. Vaporization rate"))
    b.append(eq('W = Q / H<sub>vap</sub>', ""))
    b.append(p("W — lưu lượng khối lượng (lb/hr); H<sub>vap</sub> — nhiệt bay hơi (BTU/lb)."))
    b.append(h3("Bước 4 — Diện tích xả tối thiểu", "Step 4. Minimum required relieving area"))
    b.append(p("Dùng các công thức định cỡ khí/hơi (trang 5-3) với quá áp 21% nếu van là thiết bị "
               "bổ sung cho hỏa hoạn (quá áp cho phép tuân theo quy định địa phương)."))
    b.append(fig(8, F.fig_f712()))
    b.append(fig(9, F.fig_f713()))
    b.append(h3("Ví dụ 1 — Benzene (bồn nằm ngang, hai đáy cầu)",
                "Example 1 — Benzene (horizontal cylinder, spherical ends)"))
    b.append(p("Chất lưu: Benzene; năng lực yêu cầu: 5.000 lb/hr; áp suất thiết lập: 200 psig; áp "
               "suất ngược: khí quyển; nhiệt độ: 100°F; khối lượng phân tử: 78,11; nhiệt bay hơi: "
               "172 BTU/lb. Bồn: đường kính D = 15 ft; chiều dài L = 30 ft; cao trình H = 15 ft; "
               "mức chất lỏng tối đa F = 12,25 ft; nằm ngang; không cách nhiệt. Bước 1: "
               "K₁ = H + F = 27,25 &gt; 25 → K = 25; E₁ = K − H = 10 &gt; 0 → E = 10; "
               "β = cos⁻¹[1 − 2E/D] = 109,5°; A<sub>wet</sub> = 901 ft². Bước 2: F = 1,0 → "
               "Q = 5.560.000 BTU/h. Bước 3: W = 32.330 lb/hr. Bước 4: A = 1,051 in²."))

    # ---- Fire, unwetted -------------------------------------------------------
    b.append(h2("Điều kiện hỏa hoạn — định cỡ bồn chứa khí/hơi (bồn khô)",
                "Fire Conditions — Sizing for Vessels Containing Gases and Vapors Only"))
    b.append(p("Phương pháp sau (API RP 520, bản 5) tính diện tích lỗ hiệu dụng yêu cầu cho van xả "
               "áp trên bồn chứa khí tiếp xúc hỏa hoạn."))
    b.append(eq('A = F&#8242; A&#8242; / ' + _sq('P<sub>1</sub>'), ""))
    b.append(eq('F&#8242; = 0,1406 (T<sub>w</sub> &#8722; T<sub>1</sub>)<sup>1,25</sup> / '
                '(C&#8201;K&#8201;T<sub>1</sub><sup>0,6506</sup>)', ""))
    b.append(ul([
        "A — diện tích xả hiệu dụng tối thiểu (in²); A′ — diện tích bề mặt bồn tiếp xúc (ft²).",
        "P<sub>1</sub> — áp suất xả tuyệt đối (psia).",
        "T<sub>w</sub> — nhiệt độ vách bồn (°R); API khuyến nghị tối đa 1100°F cho thép các-bon.",
        "T<sub>1</sub> = P<sub>1</sub>·T<sub>n</sub>/P<sub>n</sub> (T<sub>n</sub> — nhiệt độ khí vận "
        "hành bình thường, °R; P<sub>n</sub> — áp suất vận hành bình thường tuyệt đối).",
        "C — hệ số từ trang 7-9 hoặc 7-26; K = 0,975. Giá trị F′ nhỏ nhất khuyến nghị là 0,01; "
        "nếu không biết, dùng F′ = 0,045.",
    ]))
    b.append(h3("Ví dụ 1 — Không khí (bồn khô)", "Example 1 — Air (unwetted vessel)"))
    b.append(p("Không khí; áp suất thiết lập: 100 psig; diện tích bề mặt A′ = 200 ft²; nhiệt độ khí "
               "vận hành: 125°F; áp suất vận hành: 80 psig; nhiệt độ vách: 1100°F. Bước 1: P₁ = "
               "(100)(1,1) + 14,7 = 124,7 psia; T<sub>n</sub> = 585°R; P<sub>n</sub> = 94,7 psia → "
               "T<sub>1</sub> = 770,3°R. Bước 2: T<sub>w</sub> = 1560°R; C = 356; K = 0,975 → "
               "F′ = 0,022. Bước 3: A = (0,022)(200)/√124,7 = 0,402 in² → cần van lỗ \"G\" "
               "(0,503 in²)."))

    # ---- Two-phase ------------------------------------------------------------
    b.append(h2("Dòng hai pha và dòng sôi", "Two-Phase and Flashing Flow"))
    b.append(p("Dòng hai pha xảy ra khi dòng chứa cả pha lỏng và pha khí/hơi. Dòng sôi xảy ra khi "
               "áp suất giảm làm một phần hoặc toàn bộ chất lỏng hóa hơi. Cả hai có thể xảy ra đồng "
               "thời. Các công thức định cỡ khí, hơi, chất lỏng và hơi nước trong sách này có thể "
               "không phù hợp cho dòng hai pha và sôi."))
    b.append(p("Công trình của DIERS và các nghiên cứu khác cho thấy chủ đề này rất phức tạp và "
               "không có phương pháp duy nhất áp dụng cho mọi trường hợp. Khi định cỡ dòng hai pha "
               "và sôi, hãy lưu ý:"))
    b.append(ul([
        "Ước tính và xem xét áp suất tăng trong thân van do sôi, cùng với áp suất ngược tạo ra dự "
        "kiến.",
        "Có thể cần van cân bằng (Style JBS) hoặc van pilot (Style JPVM) khi áp suất thân van do "
        "sôi quá lớn hoặc không thể dự đoán chắc chắn.",
        "Nếu hỗn hợp hai pha tại đầu vào van có ≥ 50% khối lượng là lỏng, dùng van kết cấu dịch vụ "
        "lỏng; nếu pha hơi &gt; 50% khối lượng, dùng van cho chất lưu nén được.",
    ]))

    # ---- Reference tables -----------------------------------------------------
    b.append(h2("Tính chất điển hình của khí", "Typical Properties of Gases"))
    b.append(_t77("vi"))
    b.append(h2("Áp suất/temperature bão hòa của nước", "Water Saturation Pressure/Temperature"))
    b.append(_t78("vi"))
    b.append(h2("Kích thước mặt bích ANSI", "ANSI Flange Dimensions"))
    b.append(_t79("vi"))
    b.append(h2("Hệ số tương đương và chuyển đổi", "Equivalents and Conversion Factors"))
    b.append(_t710("vi"))
    b.append(h2("Diện tích lỗ xả — van lò xo Crosby",
                "Orifice Areas — Crosby Spring Loaded Pressure Relief Valves"))
    b.append(_orifice("vi", D.T711,
                      "Bảng T7-11 — Diện tích lỗ xả van lò xo Crosby (* lỗ có sẵn).",
                      "Table T7-11 — Crosby spring loaded PRV orifice areas (* available orifice)."))
    b.append(h2("Diện tích lỗ xả — van vận hành pilot Crosby",
                "Orifice Areas — Crosby Pilot Operated Pressure Relief Valves"))
    b.append(_orifice("vi", D.T712,
                      "Bảng T7-12 — Diện tích lỗ xả van vận hành pilot Crosby (* lỗ có sẵn).",
                      "Table T7-12 — Crosby pilot operated PRV orifice areas (* available orifice)."))
    return "".join(b)


# ============================================================================
#  ENGLISH BODY
# ============================================================================
def body_en():
    b = []
    b.append(p("This chapter assembles the charts, tables and supporting data used to assist in "
               "sizing and selecting Crosby pressure relief valves. It covers the correction factors "
               "(Z, K<sub>b</sub>, K<sub>w</sub>, K<sub>n</sub>, K<sub>v</sub>, K<sub>sh</sub>), the "
               "ratio of specific heats k and coefficient C, noise and reaction-force calculations, "
               "fire sizing, gas-property and water-saturation tables, ANSI flange dimensions, unit "
               "conversion factors, and the effective orifice areas of the valves."))
    b.append(h3("Chapter 7 data listing", "Mục lục dữ liệu chương 7"))
    b.append(ul([
        "Compressibility factor, Z (page 7-2)",
        "Capacity correction factors for back pressure (pages 7-3 through 7-5)",
        "Capacity correction factor for high pressure steam, K<sub>n</sub> (page 7-6)",
        "Capacity correction factor for viscosity, K<sub>v</sub> (page 7-7)",
        "Capacity correction factor for superheat, K<sub>sh</sub> (page 7-8)",
        "Ratio of specific heats, k, and coefficient, C (page 7-9)",
        "Noise level calculations (pages 7-10, 7-11)",
        "Reaction forces (pages 7-12 through 7-16)",
        "Fire conditions — sizing for vaporizing liquids (pages 7-17 through 7-23)",
        "Fire conditions — sizing for vessels containing gases and vapors only (page 7-24)",
        "Two-phase and flashing flow (page 7-25)",
        "Typical properties of gases (page 7-26)",
        "Water saturation pressure/temperature (page 7-27)",
        "ANSI flange dimensions (page 7-28)",
        "Equivalents and conversion factors (page 7-29)",
        "Orifice areas — Crosby spring loaded PRVs (page 7-30)",
        "Orifice areas — Crosby pilot operated PRVs (page 7-31)",
    ]))

    # ---- Z --------------------------------------------------------------------
    b.append(h2("Compressibility Factor, Z", "Hệ số nén Z"))
    b.append(p("The compressibility factor Z corrects the ideal gas law when calculating mass or "
               "volumetric flow at relieving conditions. For a real gas the inlet density depends on "
               "the reduced pressure P<sub>r</sub> = P/P<sub>c</sub> and reduced temperature "
               "T<sub>r</sub> = T/T<sub>c</sub> (P<sub>c</sub>, T<sub>c</sub> from Table T7-7). If Z "
               "is unknown, use Z = 1.0."))
    b.append(fig(1, F.fig_f71()))

    # ---- Back pressure --------------------------------------------------------
    b.append(h2("Capacity Correction Factors for Back Pressure",
                "Hệ số hiệu chỉnh áp suất ngược"))
    b.append(p("Back pressure is the pressure at the outlet of a relief valve caused by pressure in "
               "the discharge system or by flashing in the valve body. Without proper consideration "
               "of back pressure the valve may experience (1) a change in set pressure, (2) a change "
               "in closing pressure, (3) a decrease in relieving capacity, and (4) dynamic "
               "instability."))
    b.append(h3("Back pressure in process service", "Áp suất ngược trong công nghệ"))
    b.append(ul([
        "<b>Built-up back pressure</b> is the additional pressure at the valve outlet resulting from "
        "discharge-system resistance or flashing in the valve body.",
        "<b>Superimposed back pressure</b> is the static pressure already present at the valve "
        "outlet when the valve is required to operate, from other sources in the discharge system.",
    ]))
    b.append(p("The effect of back pressure depends on several coexisting conditions: constant vs. "
               "variable back pressure; valve closed vs. open and relieving; gas/vapor vs. liquid "
               "phase; and conventional vs. balanced valve construction."))
    b.append(h3("Conventional Valves (Style JOS, Series 800/900)", "Van thường (Style JOS, Series 800/900)"))
    b.append(p("<b>Valve closed:</b> constant superimposed back pressure raises the opening "
               "pressure by the amount of the back pressure, so the spring setting (cold differential "
               "test pressure) is based on set pressure minus back pressure. Variable superimposed "
               "back pressure shifts the opening pressure as it varies — a balanced valve is usually "
               "recommended. <b>Valve open and relieving:</b> built-up back pressure rapidly reduces "
               "the lifting forces; it must be limited to no greater than 10% of the set pressure. "
               "Excess requires a balanced valve."))
    b.append(p("For gases and vapors including steam, capacity is unaffected if back pressure is "
               "below the critical pressure (generally 55% of absolute relieving pressure). Above "
               "critical pressure the flow correction factor K<sub>b</sub> (Table T7-1) must be "
               "applied; below it, K<sub>b</sub> = 1.00. For liquids, conventional valves need no "
               "correction: K<sub>w</sub> = 1."))
    b.append(_t71("en"))
    b.append(h3("Balanced Valves (Style JBS, Series BP)", "Van cân bằng (Style JBS, Series BP)"))
    b.append(p("Because the effective area of the bellows or piston equals the seat area, the set "
               "pressure of a balanced valve is unaffected by back pressure and it opens within the "
               "ASME set-pressure tolerances. However, while open and relieving, back pressure "
               "gradually reduces the lifting force, so a flow correction factor for the maximum "
               "expected back pressure must be used in sizing."))
    b.append(p("For gases and vapors use the K<sub>b</sub> factor from Figure F7-2 for Style JBS or "
               "Series BP valves. For liquids use the K<sub>w</sub> factor from Figure F7-3. When "
               "back pressure conditions do not apply, K<sub>b</sub> = K<sub>w</sub> = 1.00. For back "
               "pressures beyond the Figure F7-2/F7-3 limits, consult your local Crosby "
               "representative."))
    b.append(fig(2, F.fig_f72()))
    b.append(fig(3, F.fig_f73()))
    b.append(h3("Pilot Operated Valves", "Van vận hành pilot"))
    b.append(p("<b>Style JPV (snap-acting):</b> back pressure does not affect set pressure or flow "
               "capacity except when flow is subcritical (ratio of absolute back pressure to absolute "
               "relieving pressure exceeds 55%); then K<sub>b</sub> (Table T7-1) must be applied. "
               "Below 55%, K<sub>b</sub> = 1.00. <b>Style JPVM (modulating):</b> set pressure and "
               "operability are unaffected by back pressure up to 70% of set pressure (use a backflow "
               "preventer if back pressure may exceed inlet pressure). Capacity is affected only when "
               "flow is subcritical (ratio exceeds 55%); then K<sub>b</sub> (Table T7-1) applies, "
               "otherwise K<sub>b</sub> = 1.00."))

    # ---- Kn -------------------------------------------------------------------
    b.append(h2("Capacity Correction Factor for High Pressure Steam, Kn",
                "Hệ số hiệu chỉnh hơi nước áp suất cao K<sub>n</sub>"))
    b.append(p("When the relieving pressure of steam exceeds 10,340 kPaa (1,500 psig), ASME "
               "requires an additional factor K<sub>n</sub> for dry saturated steam. Figure F7-4 "
               "gives K<sub>n</sub> versus relieving pressure. See Chapter 6 for its use in the "
               "steam sizing formula."))
    b.append(fig(4, F.fig_f74()))

    # ---- Kv -------------------------------------------------------------------
    b.append(h2("Capacity Correction Factor for Viscosity, Kv",
                "Hệ số hiệu chỉnh độ nhớt K<sub>v</sub>"))
    b.append(p("When sizing a valve for viscous liquid service, first size it as for nonviscous "
               "service to obtain a preliminary required effective area A. Select the next larger "
               "standard orifice and calculate the Reynolds number R from the formulas below, then "
               "obtain K<sub>v</sub> from the graph (Figure F7-5) to correct the preliminary area. If "
               "the corrected area exceeds the chosen orifice area, repeat with the next larger "
               "orifice."))
    b.append(p("U.S.C.S. units: &nbsp; R = 12,700 · GPM · G / &#8730;A&nbsp;&nbsp; (GPM = flow at "
               "flowing temperature, gal/min; G = specific gravity referred to water = 1.00 at 70°F; "
               "A = effective discharge area, in²; U = viscosity at flowing temperature, Saybolt "
               "Universal Seconds, SSU)."))
    b.append(p("Metric units: &nbsp; R = 85,225 · Q · G / &#8730;A′&nbsp;&nbsp; (Q = flow, L/min; "
               "A′ = effective discharge area, mm²; µ = absolute viscosity, centipoise)."))
    b.append(fig(5, F.fig_f75()))

    # ---- Ksh ------------------------------------------------------------------
    b.append(h2("Capacity Correction Factor for Superheat, Ksh",
                "Hệ số hiệu chỉnh quá nhiệt K<sub>sh</sub>"))
    b.append(p("The steam sizing formulas (pages 5-6 and 6-6) are based on dry saturated steam. To "
               "size for superheated steam, the superheat correction factor K<sub>sh</sub> corrects "
               "the calculated saturated-steam flow to superheated flow. For saturated steam "
               "K<sub>sh</sub> = 1.0. For superheated steam, enter Table T7-2 at the required "
               "relieving pressure and read the factor under the total steam temperature column."))
    b.append(_t72("en"))

    # ---- k / C ----------------------------------------------------------------
    b.append(h2("Ratio of Specific Heats, k, and Coefficient, C",
                "Tỷ số nhiệt dung riêng k và hệ số C"))
    b.append(p("The following formula equates the ratio of specific heats k to the coefficient C "
               "used in gas and vapor sizing. Figure F7-6 and Table T7-3 give the calculated "
               "solution."))
    b.append(eq('C = 520 ' + _fr('&#8730;(k) [2/(k+1)]<sup>(k+1)/(k-1)</sup>', ''), ""))
    b.append(fig(6, F.fig_f76()))
    b.append(_t73("en"))

    # ---- Noise ----------------------------------------------------------------
    b.append(h2("Noise Level Calculations", "Tính toán mức tiếng ồn"))
    b.append(p("The following formulas calculate the noise level of gases, vapors and steam "
               "discharged from a relief valve, derived from API Recommended Practice 521. Table T7-4 "
               "lists relative noise levels."))
    b.append(eq('L<sub>100</sub> = L + 10&#8201;log<sub>10</sub> (0.29354&#8201;W&#8201;k&#8201;T/M)', ""))
    b.append(ul([
        "L<sub>100</sub> — sound level at 100 feet from the point of discharge, decibels.",
        "L — noise intensity (sound pressure level) at 100 ft, from Figure F7-7.",
        "W — maximum relieving capacity, lb/hr (k and M from Table T7-7; for steam k = 1.3, M = 18 "
        "if unknown).",
        "T — absolute temperature at the valve inlet, degrees Rankine (°F + 460).",
        "M — molecular weight (Table T7-7; for steam M = 18).",
    ]))
    b.append(p("When the noise level is required at a distance other than 100 feet, use:"))
    b.append(eq('L<sub>p</sub> = L<sub>100</sub> &#8722; 20&#8201;log<sub>10</sub> (r/100)', ""))
    b.append(p("where r is the distance from the point of discharge, feet. The pressure ratio "
               "PR = absolute relieving pressure / absolute back pressure is used to obtain L from "
               "Figure F7-7."))
    b.append(fig(7, F.fig_f77()))
    b.append(_t74("en"))
    b.append(h3("Example 1 — Gas/Vapor Mass Flow (lb/hr)",
                "Ví dụ 1 — Khí/hơi, lưu lượng khối lượng (lb/hr)"))
    b.append(p("Fluid: Natural Gas; set pressure: 210 psig; overpressure: 10%; back pressure: 50 "
               "psig; inlet relieving temperature: 120°F; molecular weight: 19.0; compressibility: "
               "1; selected area: 0.503 in²; noise at 500 feet. P₁ = 210 + 21 + 14.7 = 245.7 psia; "
               "K<sub>b</sub> = 1.0; C = 344 (Table T7-7); K = 0.975. Rated flow W = 7,502 lb/hr, "
               "T = 580°R, PR = 245.7/(50 + 14.7) = 3.8 → L = 54.5 (Figure F7-7). "
               "L<sub>100</sub> = 103.8 dB; at 500 ft: L<sub>p</sub> = 89.9 dB."))

    # ---- Reaction forces ------------------------------------------------------
    b.append(h2("Reaction Forces", "Lực phản ứng"))
    b.append(p("The following formulas calculate the reaction force of a relief valve discharging "
               "gas, vapor or steam directly to atmosphere without discharge piping, consistent with "
               "API Recommended Practice 520 (gas/vapor) and ANSI/ASME B31.1 (steam). Determining "
               "the outlet reaction force is the responsibility of the vessel and/or piping "
               "designer."))
    b.append(h3("Gas/Vapor", "Khí và hơi"))
    b.append(eq('F = C&#8201;K&#8201;A&#8201;P<sub>1</sub> ' + _sq('k/(k+1)') + ' + F<sub>g</sub>', ""))
    b.append(eq('F<sub>g</sub> = ' + _fr('(K&#8201;A&#8201;P<sub>1</sub>&#8201;K<sub>r</sub> &#8722; P<sub>a</sub>)&#8201;A<sub>o</sub>',
                                                              '1.383&#8201;A<sub>o</sub>'), ""))
    b.append(p("If F<sub>g</sub> is less than or equal to 0.0, use F<sub>g</sub> = 0.0."))
    b.append(h3("Steam", "Hơi nước"))
    b.append(eq('F = ' + _fr('A&#8201;P<sub>1</sub> + F<sub>s</sub>', '1.335'), ""))
    b.append(eq('F<sub>s</sub> = ' + _fr('(A&#8201;P<sub>1</sub> &#8722; P<sub>a</sub>)&#8201;A<sub>o</sub>&#8201;K<sub>n</sub>',
                                                              '1.886&#8201;A<sub>o</sub>'), ""))
    b.append(p("If F<sub>s</sub> is less than or equal to 0.0, use F<sub>s</sub> = 0.0. Symbols: F "
               "— total reaction force at the point of discharge to atmosphere, lbf; F<sub>g</sub>, "
               "F<sub>s</sub> — static-pressure reaction force component at the outlet (gas/vapor, "
               "steam); C — coefficient from ratio of specific heats (Table T7-7); K = 0.975; A — "
               "effective discharge area, in²; A<sub>o</sub> — outlet cross-sectional area, in²; "
               "P<sub>1</sub> — relieving pressure, psia; P<sub>a</sub> — atmospheric pressure; k — "
               "ratio of specific heats (Table T7-7); K<sub>n</sub> — high-pressure steam factor; "
               "K<sub>r</sub> — specific-heat correction for k ≠ 1.4 (Table T7-5)."))
    b.append(_t75("en"))
    b.append(h3("Example 1 — Gas/Vapor Mass Flow (lb/hr)",
                "Ví dụ 1 — Khí/hơi, lưu lượng khối lượng (lb/hr)"))
    b.append(p("Natural Gas; required capacity: 5,900 lb/hr; set pressure: 210 psig; overpressure: "
               "10%; relieving pressure: 245.7 psia; k = 1.27; C = 344; calculated area: 0.397 in²; "
               "valve selected: 1-1/2G2-1/2, area 0.503 in². P₁ = 245.7 psia; K<sub>r</sub> = 1.04 "
               "(Table T7-5); P<sub>a</sub> = 14.7 psia; A<sub>o</sub> = (2-1/2)²(π/4) = 4.909 in². "
               "F<sub>g</sub> = 18.5 lbf; F = 111.6 lbf."))

    # ---- Fire, wetted ---------------------------------------------------------
    b.append(h2("Fire Conditions — Sizing for Vaporizing Liquids (Wetted Vessels)",
                "Điều kiện hỏa hoạn — định cỡ chất lỏng bay hơi (bồn ướt)"))
    b.append(p("The following method (reference API Recommended Practice 520) calculates the "
               "required orifice area for relief valves on vessels containing liquids exposed to "
               "fire."))
    b.append(h3("Step 1. Total wetted surface area", "Bước 1 — Tổng diện tích bề mặt ướt"))
    b.append(p("Use the vessel selection diagram (Figure F7-13) and the effective-liquid-level "
               "logic diagram (Figure F7-12) to determine the wetted surface area A<sub>wet</sub> "
               "(ft²)."))
    b.append(h3("Step 2. Total heat absorption", "Bước 2 — Tổng nhiệt hấp thụ"))
    b.append(p("When prompt fire-fighting efforts and adequate drainage exist: &nbsp; Q = 21,000 · "
               "F · A<sub>wet</sub><sup>0.82</sup>. When they do not exist: &nbsp; Q = 34,500 · F · "
               "A<sub>wet</sub><sup>0.82</sup>. Q is total heat absorption (BTU/hr); F is the "
               "environmental factor (Table T7-6)."))
    b.append(_t76("en"))
    b.append(h3("Step 3. Vaporization rate", "Bước 3 — Tốc độ bay hơi"))
    b.append(eq('W = Q / H<sub>vap</sub>', ""))
    b.append(p("W — mass flow, lb/hr; H<sub>vap</sub> — latent heat of vaporization, BTU/lb."))
    b.append(h3("Step 4. Minimum required relieving area", "Bước 4 — Diện tích xả tối thiểu"))
    b.append(p("Use the gas/vapor sizing equations (page 5-3). An overpressure of 21% may be used "
               "for a supplemental fire device (allowable overpressure varies by local regulation)."))
    b.append(fig(8, F.fig_f712()))
    b.append(fig(9, F.fig_f713()))
    b.append(h3("Example 1 — Benzene (horizontal cylinder, spherical ends)",
                "Ví dụ 1 — Benzene (bồn nằm ngang, hai đáy cầu)"))
    b.append(p("Fluid: Benzene; required capacity: 5,000 lb/hr; set pressure: 200 psig; back "
               "pressure: atmospheric; inlet temperature: 100°F; molecular weight: 78.11; latent "
               "heat: 172 BTU/lb. Vessel: diameter D = 15 ft; length L = 30 ft; elevation H = 15 ft; "
               "max fluid level F = 12.25 ft; horizontal; no insulation. Step 1: K₁ = H + F = 27.25 "
               "&gt; 25 → K = 25; E₁ = K − H = 10 &gt; 0 → E = 10; β = cos⁻¹[1 − 2E/D] = 109.5°; "
               "A<sub>wet</sub> = 901 ft². Step 2: F = 1.0 → Q = 5,560,000 BTU/hr. Step 3: "
               "W = 32,330 lb/hr. Step 4: A = 1.051 in²."))

    # ---- Fire, unwetted -------------------------------------------------------
    b.append(h2("Fire Conditions — Sizing for Vessels Containing Gases and Vapors Only",
                "Điều kiện hỏa hoạn — định cỡ bồn chứa khí/hơi (bồn khô)"))
    b.append(p("The following method (API Recommended Practice 520, Fifth Edition) calculates the "
               "required effective discharge area for relief valves on vessels containing gases "
               "exposed to fire."))
    b.append(eq('A = F&#8242; A&#8242; / ' + _sq('P<sub>1</sub>'), ""))
    b.append(eq('F&#8242; = 0.1406 (T<sub>w</sub> &#8722; T<sub>1</sub>)<sup>1.25</sup> / '
                '(C&#8201;K&#8201;T<sub>1</sub><sup>0.6506</sup>)', ""))
    b.append(ul([
        "A — minimum required effective discharge area, in²; A′ — exposed surface area of the vessel, ft².",
        "P<sub>1</sub> — relieving pressure, psia.",
        "T<sub>w</sub> — vessel wall temperature, °R; API recommended maximum is 1100°F for carbon steel.",
        "T<sub>1</sub> = P<sub>1</sub>·T<sub>n</sub>/P<sub>n</sub> (T<sub>n</sub> — normal operating "
        "gas temperature, °R; P<sub>n</sub> — normal operating gas pressure absolute).",
        "C — coefficient from page 7-9 or 7-26; K = 0.975. Recommended minimum F′ = 0.01; if unknown, "
        "use F′ = 0.045.",
    ]))
    b.append(h3("Example 1 — Air (unwetted vessel)", "Ví dụ 1 — Không khí (bồn khô)"))
    b.append(p("Air; set pressure: 100 psig; exposed surface area A′ = 200 ft²; normal operating "
               "gas temperature: 125°F; normal operating gas pressure: 80 psig; wall temperature: "
               "1100°F. Step 1: P₁ = (100)(1.1) + 14.7 = 124.7 psia; T<sub>n</sub> = 585°R; "
               "P<sub>n</sub> = 94.7 psia → T<sub>1</sub> = 770.3°R. Step 2: T<sub>w</sub> = 1560°R; "
               "C = 356; K = 0.975 → F′ = 0.022. Step 3: A = (0.022)(200)/√124.7 = 0.402 in² → a "
               "\"G\" orifice valve (0.503 in²) is required."))

    # ---- Two-phase ------------------------------------------------------------
    b.append(h2("Two-Phase and Flashing Flow", "Dòng hai pha và dòng sôi"))
    b.append(p("Two-phase flow describes a stream containing both liquid and gas/vapor phases. "
               "Flashing flow occurs when, due to a pressure decrease, all or part of a liquid flow "
               "changes to vapor. Both conditions can occur simultaneously. The formulas provided for "
               "liquid, gas, vapor and steam may not be suitable for two-phase and flashing flow."))
    b.append(p("Work by DIERS (Design Institute for Emergency Relief Systems) and others has shown "
               "this subject is complex and no single universally accepted method handles all "
               "applications. When sizing for two-phase and flashing flow:"))
    b.append(ul([
        "Estimate the increase in body-bowl pressure due to flashing, together with expected "
        "built-up back pressure.",
        "A balanced valve (Crosby Style JBS bellows or Style JPVM pilot) may be necessary when the "
        "flashing-induced body-bowl pressure increase is excessive or unpredictable.",
        "If the two-phase mixture at the valve inlet is 50% liquid or more by mass, use a liquid "
        "service valve construction; if the vapor content exceeds 50% by mass, use a valve designed "
        "for compressible fluid service.",
    ]))

    # ---- Reference tables -----------------------------------------------------
    b.append(h2("Typical Properties of Gases", "Tính chất điển hình của khí"))
    b.append(_t77("en"))
    b.append(h2("Water Saturation Pressure/Temperature",
                "Áp suất/temperature bão hòa của nước"))
    b.append(_t78("en"))
    b.append(h2("ANSI Flange Dimensions", "Kích thước mặt bích ANSI"))
    b.append(_t79("en"))
    b.append(h2("Equivalents and Conversion Factors", "Hệ số tương đương và chuyển đổi"))
    b.append(_t710("en"))
    b.append(h2("Orifice Areas — Crosby Spring Loaded Pressure Relief Valves",
                "Diện tích lỗ xả — van lò xo Crosby"))
    b.append(_orifice("en", D.T711,
                      "Table T7-11 — Crosby spring loaded PRV orifice areas (* available orifice).",
                      "Bảng T7-11 — Diện tích lỗ xả van lò xo Crosby (* lỗ có sẵn)."))
    b.append(h2("Orifice Areas — Crosby Pilot Operated Pressure Relief Valves",
                "Diện tích lỗ xả — van vận hành pilot Crosby"))
    b.append(_orifice("en", D.T712,
                      "Table T7-12 — Crosby pilot operated PRV orifice areas (* available orifice).",
                      "Bảng T7-12 — Diện tích lỗ xả van vận hành pilot Crosby (* lỗ có sẵn)."))
    return "".join(b)
