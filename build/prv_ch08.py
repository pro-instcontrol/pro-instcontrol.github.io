# -*- coding: utf-8 -*-
"""Book 4, Chapter 8 — Appendix: ASME Section VIII, Division 1 excerpts (EN/VI).

Covers the handbook's condensed excerpt of ASME BPVC Section VIII Division 1
(1992 Edition through the 1994 Addenda) for pressure relief devices —
paragraphs UG-125 through UG-136 — plus ASME Appendix 11 (capacity
conversions) and Appendix M (installation and operation).  The four vector
figures and the small data tables are defined here; the source text layer is
jumbled, so the prose is a structured bilingual condensation that keeps every
numeric requirement.
"""

from prv_common import (eq, fig, h2, h3, note, p, table, ul)
import prvfig as F

PAGES_SRC = 24          # source pages A-1 … A-19 + Other Information pages
BYLINE = "Crosby Valve Inc. · Technical Document TP-V300"
TITLE_EN = "Appendix — ASME Section VIII, Division 1 Excerpts"
TITLE_VI = "Phụ lục — Trích dẫn ASME Section VIII, Division 1"


# ---- equation helpers (self-contained, no global CSS dependency) -------------
def _sq(x):
    return '&#8730;<span style="border-top:1px solid currentColor;padding:0 .18rem;">%s</span>' % x


def _fr(num, den):
    return ('<span style="display:inline-block;text-align:center;vertical-align:middle;'
            'margin:0 .3rem;">'
            '<span style="display:block;border-bottom:1px solid currentColor;padding:0 .4rem;">%s</span>'
            '<span style="display:block;padding:0 .4rem;">%s</span></span>' % (num, den))


# ---- small data tables (kept in-module; values as printed in the source) -----
_BREAKPIN = [("30", "150", "5"), ("151", "275", "10"), ("276", "375", "15")]

_CTABLE = [
    ("1.00", "315", "1.26", "343", "1.52", "366"),
    ("1.02", "318", "1.28", "345", "1.54", "368"),
    ("1.04", "320", "1.30", "347", "1.56", "369"),
    ("1.06", "322", "1.32", "349", "1.58", "371"),
    ("1.08", "324", "1.34", "351", "1.60", "372"),
    ("1.10", "327", "1.36", "352", "1.62", "374"),
    ("1.12", "329", "1.38", "354", "1.64", "376"),
    ("1.14", "331", "1.40", "356", "1.66", "377"),
    ("1.16", "333", "1.42", "358", "1.68", "379"),
    ("1.18", "335", "1.44", "359", "1.70", "380"),
    ("1.20", "337", "1.46", "361", "2.00", "400"),
    ("1.22", "339", "1.48", "363", "2.20", "412"),
    ("1.24", "341", "1.50", "364", "", ""),
]

_MW = [
    ("Air", "28.97", "Freon 22", "86.48"),
    ("Acetylene", "26.04", "Freon 114", "170.90"),
    ("Ammonia", "17.03", "Hydrogen", "2.02"),
    ("Butane", "58.12", "Hydrogen Sulfide", "34.08"),
    ("Carbon Dioxide", "44.01", "Methane", "16.04"),
    ("Chlorine", "70.91", "Methyl Chloride", "50.48"),
    ("Ethane", "30.07", "Nitrogen", "28.02"),
    ("Ethylene", "28.05", "Oxygen", "32.00"),
    ("Freon 11", "137.37", "Propane", "44.09"),
    ("Freon 12", "120.9", "Sulfur Dioxide", "64.06"),
]

_M11 = [("≤ 70 psi", "± 2 psi", "5 psi"), ("71 – 1000 psi", "± 3%", "10%"),
        ("> 1000 psi", "± 3%", "7%")]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 8.</b> MAWP — áp suất làm việc cho phép cực đại · "
                "PRV — van xả áp (reclosing) · thiết bị không đóng lại (nonreclosing) — đĩa "
                "nứt (rupture disk), chốt gãy (breaking pin) · MDR — dải thiết kế chế tạo "
                "(manufacturing design range) · K<sub>D</sub>/K — hệ số xả thực nghiệm / hệ "
                "số thiết kế · C — hằng số khí theo k · blowdown — độ hạ áp đóng van · "
                "telltale — thiết bị chỉ thị khe giữa đĩa nứt và van.")
    return ("<b>Key terms.</b> MAWP — maximum allowable working pressure · PRV — "
            "pressure relief valve (reclosing) · nonreclosing devices — rupture disk, "
            "breaking pin · MDR — manufacturing design range · K<sub>D</sub>/K — measured "
            "discharge coefficient / design coefficient · C — gas constant as a function "
            "of k · blowdown — reclosure pressure reduction · telltale — indicator in the "
            "space between a rupture disk and its valve.")


# ---- reusable table builders -------------------------------------------------
def _t_breakpin(lang):
    hdr = ["P định mức (psi) — min", "max", "Dung sai ± (psi)"] if lang == "vi" \
        else ["Rated pressure (psi) — min", "max", "Tolerance ± (psi)"]
    cap = ("Bảng UG-127(b)(3) — dung sai áp lực gãy của chốt gãy, cộng trừ."
           if lang == "vi" else
           "UG-127(b)(3) table — breaking-pin break-pressure tolerance, plus or minus.")
    return table(hdr, _BREAKPIN, caption=cap)


def _t_ctable(lang):
    hdr = ["k", "C", "k", "C", "k", "C"]
    cap = ("Bảng Hình 11-1 — hằng số C của khí/hơi theo tỷ số nhiệt dung riêng "
           "k = c<sub>p</sub>/c<sub>v</sub>." if lang == "vi" else
           "Fig. 11-1 table — gas/vapor constant C versus the ratio of specific "
           "heats k = c<sub>p</sub>/c<sub>v</sub>.")
    rows = [[c.replace(".", ",") if lang == "vi" and i % 2 == 0 else c
             for i, c in enumerate(r)] for r in _CTABLE]
    return table(hdr, rows, caption=cap, cls="tbl wide")


def _t_mw(lang):
    hdr = ["Chất", "M", "Chất", "M"] if lang == "vi" else ["Substance", "M", "Substance", "M"]
    cap = ("Bảng 11-1 — khối lượng phân tử của một số khí và hơi thông dụng."
           if lang == "vi" else
           "Table 11-1 — molecular weights of some common gases and vapors.")
    return table(hdr, _MW, caption=cap, cls="tbl wide")


def _t_m11(lang):
    hdr = (["Áp suất thiết lập", "Dung sai thiết lập", "Chênh lệch tối thiểu tới áp "
            "suất vận hành"] if lang == "vi" else
           ["Set pressure", "Set-pressure tolerance", "Minimum differential to "
            "operating pressure"])
    cap = ("Khuyến nghị M-11(c) — chênh lệch áp suất tối thiểu giữa thiết lập và vận "
           "hành." if lang == "vi" else
           "M-11(c) recommendations — minimum differential between set and operating "
           "pressure.")
    return table(hdr, _M11, caption=cap)


# ---- shared equation groups --------------------------------------------------
def _eq_theoretical(lang):
    dec = "," if lang == "vi" else "."
    out = [
        eq('W<sub>T</sub> = 51,5 A P' if lang == "vi" else 'W<sub>T</sub> = 51.5 A P',
           "UG-131(e)(2) — hơi bão hòa khô"),
        eq('W<sub>T</sub> = 356 A P ' + _sq('M/T'), "UG-131(e)(2) — khí"),
        eq('W<sub>T</sub> = C A P ' + _sq('M/(Z T)'), "UG-131(e)(2) — khí/h"),
        eq('W<sub>T</sub> = 2407 A ' + _sq('(P &#8722; P<sub>d</sub>) w'),
           "UG-131(e)(2) — n"),
    ]
    del dec
    return out


def _eq_kd(lang):
    if lang == "vi":
        return [eq('K<sub>D</sub> = dòng thực tế / dòng lý thuyết', "UG-131(e)(2)"),
                eq('K = 0,90 × K<sub>D,trung bình</sub> &#8804; 0,878', "UG-131(e)(2)")]
    return [eq('K<sub>D</sub> = actual flow / theoretical flow', "UG-131(e)(2)"),
            eq('K = 0.90 × K<sub>D,avg</sub> &#8804; 0.878', "UG-131(e)(2)")]


def _eq_103_110(lang):
    if lang == "vi":
        return [eq(_fr('1,10&#8201;p + 14,7', '1,03&#8201;p + 14,7'),
                   "UG-131(h) — nâng định mức 103% → 110%")]
    return [eq(_fr('1.10&#8201;p + 14.7', '1.03&#8201;p + 14.7'),
               "UG-131(h) — 103% → 110% rating multiplier")]


def _eq_prorate(lang):
    if lang == "vi":
        return [eq(_fr('P + 14,7', '1,10&#8201;p + 14,7'),
                   "UG-133(g) — hệ số quy đổi năng lực")]
    return [eq(_fr('P + 14.7', '1.10&#8201;p + 14.7'),
               "UG-133(g) — capacity prorating multiplier")]


# =====================================================================
def body_vi():
    b = []
    b.append(p("Phụ lục này trích những đoạn thiết yếu của <b>ASME Section VIII, Division 1 "
               "(ấn bản 1992, cập nhật đến Addenda 1994)</b> liên quan đến thiết bị xả áp — "
               "các đoạn UG-125 đến UG-136 — cùng Phụ lục 11 (quy đổi năng lực) và Phụ lục M "
               "(lắp đặt và vận hành). Mục đích là cho người dùng cẩm nang một cái nhìn "
               "trực tiếp về yêu cầu của quy code. ASME sửa code hằng năm và tái ban hành "
               "ba năm một lần; Crosby khuyến nghị luôn áp dụng ấn bản và lần sửa đổi đúng "
               "khi dùng code."))
    b.append(note("<b>Phạm vi.</b> Bản dịch là bản tóm lược kết cấu, giữ nguyên mọi con số "
                  "bắt buộc (tỷ lệ quá áp, dung sai, hệ số) — không thay thế văn bản code gốc."))

    b.append(h2("UG-125 — Quy định chung", "UG-125 — General"))
    b.append(p("(a) Mọi bình chịu áp trong phạm vi Division này, bất kể kích thước hay áp "
               "suất, đều phải có thiết bị bảo vệ theo UG-125–UG-136. Người dùng chịu trách "
               "nhiệm vụ lắp đặt thiết bị xả áp trước khi vận hành lần đầu; thiết bị không "
               "bắt buộc do nhà chế tạo bình cung cấp. Định nghĩa về thiết bị xả áp trong "
               "Phụ lục I của ASME/ANSI PTC 25.3 được áp dụng. (b) Nồi hơi không đốt (theo "
               "U-1(g)) phải có thiết bị xả áp theo Section I."))
    b.append(p("(c) Mọi bình (khác nồi hơi không đốt) phải có thiết bị xả giữ áp suất không "
               "vượt quá mức cho phép dưới đây (xem UG-134 về áp suất thiết lập):"))
    b.append(ul([
        "<b>Một thiết bị:</b> ≤ MAWP + 10% hoặc + 3 psi, chọn giá trị lớn hơn;",
        "<b>Nhiều thiết bị</b> thiết lập theo UG-134(a): ≤ MAWP + 16% hoặc + 4 psi;",
        "<b>Bổ sung cho hỏa hoạn</b> (UG-125(c)(2)): ≤ MAWP + 21%;",
        "<b>Bình chứa khí hóa lỏng</b> không có ống cấp liên tục, nhiệt độ môi trường "
        "(UG-125(c)(3)): thiết bị chỉ chống hỏa hoạn được miễn (c)(1)/(c)(2) nếu giữ áp "
        "≤ MAWP + 20%, áp thiết lập ≤ MAWP, bình có đủ thể tích khí (không đầy lỏng), "
        "MAWP lớn hơn áp suất hơi của khí ở nhiệt độ cao nhất dự kiến (thường ≥ 115°F), "
        "và van tuân thủ UG-129(a)(5), UG-131(c)(2), UG-134(d)(2). (Khí = chất có áp suất "
        "hơi > 40 psia tại 100°F.)",
    ]))
    b.append(p("(d) Thiết bị xả phải đặt ở vị trí dễ tiếp cận để kiểm tra, sửa chữa, không "
               "thể vô hiệu hóa dễ dàng (xem Appendix M) và được chọn theo dịch vụ dự định. "
               "(e) Dùng van xả áp (reclosing) hoặc thiết bị không đóng lại (nonreclosing) — "
               "loại này có thể dùng một mình hoặc phối hợp với van an toàn; đĩa nứt nên cân "
               "nhắc khi áp suất tăng rất nhanh, khi chất trong bình làm van trục trặc, hoặc "
               "khi phải tránh rò rỉ chất quý/độc. (f) Bình vận hành đầy chất lỏng phải có "
               "thiết bị xả dạng lỏng. (g) Khi nguồn áp ngoài được kiểm soát dương sao cho áp "
               "trong bình không thể vượt MAWP, thiết bị bảo vệ chưa phải đặt ngay trên bình "
               "— nhưng van giảm áp và các cơ cấu điều khiển tương tự không được coi là kiểm "
               "soát dương (trừ van pilot theo UG-126(b)). (h) Van cho dịch vụ hơi phải đạt "
               "UG-131(b)."))

    b.append(h2("UG-126 — Van xả áp", "UG-126 — Pressure relief valves"))
    b.append(p("(a) Van an toàn, van an toàn-xả và van xả phải là loại <b>lò xo tải trực "
               "tiếp</b>. (b) Van vận hành bằng pilot được cho phép nếu pilot tự kích và van "
               "chính tự mở ở ≤ áp thiết lập, xả đủ công suất định mức khi bất kỳ bộ phận "
               "thiết yếu của pilot hỏng. (c) Lò xo không được đặt lệch quá ± 5% so với áp "
               "đã ghi trên van, trừ khi nằm trong dải thiết kế lò xo của nhà chế tạo; việc "
               "điều chỉnh ban đầu do nhà chế tạo, đại diện ủy quyền hoặc đơn vị lắp ráp "
               "thực hiện, kèm thẻ dữ liệu (áp thiết lập, công suất, ngày) và niêm phong. "
               "(d) Dung sai áp thiết lập: ≤ 70 psi là ± 2 psi; trên 70 psi là ± 3%."))

    b.append(h2("UG-127 — Thiết bị xả không đóng lại", "UG-127 — Nonreclosing pressure relief devices"))
    b.append(h3("Đĩa nứt (rupture disk)", "Rupture disk devices"))
    b.append(p("Mỗi đĩa có áp nứt đóng dấu, xác định trong <b>dải thiết kế chế tạo (MDR)</b> "
               "ở nhiệt độ đĩa quy định, gắn số lô. Dung sai áp nứt: ≤ 40 psi là + 2 psi; "
               "trên 40 psi là + 5%. Áp đóng dấu xác định bằng: (1) nứt ≥ 2 đĩa mẫu mỗi lô "
               "(≥ 1 đĩa ở nhiệt độ phòng), định mức = trung bình các lần nứt ở nhiệt độ "
               "tương ứng; (2) nứt ≥ 4 đĩa (≥ 5% lô) ở 4 nhiệt độ để lập đường cong áp nứt–"
               "nhiệt độ rồi nội suy; hoặc (3) với đĩa tiền phồng/đĩa đặc/graphite, đường "
               "cong % theo nhiệt độ lập từ 1 cỡ đĩa mỗi lô vật liệu + 2 đĩa mẫu ở nhiệt độ "
               "phòng. Mọi thử nghiệm lô dùng giá đỡ cùng dạng và kích thước với đĩa lắp "
               "thực tế."))
    b.append(p("<b>Định mức công suất:</b> không vượt giá trị lý thuyết (theo UG-131) nhân "
               "với hệ số <b>K = 0,62</b>; diện tích A là diện tích ròng tối thiểu sau khi "
               "đĩa nứt (không vượt diện tích danh nghĩa của cỡ ống). Nhà chế tạo cũng có "
               "thể chứng nhận công suất theo thủ tục UG-131. <b>Áp dụng:</b> đĩa nứt có thể "
               "là thiết bị xả duy nhất; hoặc lắp giữa van và bình nếu (i) tổ hợp đủ công "
               "suất theo UG-133, (ii) công suất van kiểu nozzle bị nhân hệ số <b>0,90</b> "
               "(hoặc tổ hợp được thử theo UG-132), (iii) khe giữa đĩa và van có đồng hồ "
               "áp/try cock/vent/telltale để phát hiện đĩa nứt hoặc rò, (iv) lỗ thông sau "
               "nứt đủ cho dòng bằng công suất van và ≥ diện tích cửa vào van. Khi đĩa nứt "
               "lắp phía xả van: van phải chịu được áp ngược tích tụ (khe được thông/hút "
               "nước), công suất van đủ, áp nứt + áp đường xả không vượt áp thiết kế phần "
               "xả và không vượt MAWP/áp thiết lập của van, chất lưu sạch không đóng cặn, "
               "nắp van được thông khí."))
    b.append(h3("Chốt gãy (breaking pin)", "Breaking pin devices"))
    b.append(p("Chốt gãy <b>chỉ dùng phối hợp</b> với van an toàn/an toàn-xả, không dùng một "
               "mình. Khe giữa chốt và van phải có đồng hồ áp, try cock, vent hoặc telltale. "
               "Mỗi chốt có áp định mức và nhiệt độ gãy, nhận số lô, bảo đảm gãy trong dung "
               "sai sau:"))
    b.append(_t_breakpin("vi"))
    b.append(p("Áp định mức + dung sai không vượt <b>105% MAWP</b> của bình. Áp định mức ở "
               "nhiệt độ vận hành được kiểm chứng bằng cách gãy ≥ 2 chốt mẫu mỗi lô (lô ≤ "
               "25), trong thiết bị cùng dạng và kích thước."))
    b.append(h3("Thiết bị không đóng lại tải lò xo", "Spring-loaded nonreclosing devices"))
    b.append(p("Mở ở áp thiết lập và giữ mở đến khi đặt lại thủ công; nếu cơ cấu kích hỏng, "
               "thiết bị vẫn mở hoàn toàn ở ≤ áp thiết lập. Không phối hợp với thiết bị xả "
               "khác. Dung sai điểm mở ≤ + 5%. Công suất ≤ giá trị lý thuyết nhân K = 0,62 "
               "(A là diện tích dòng qua cửa mở nhỏ nhất) hoặc chứng nhận theo UG-131."))

    b.append(h2("UG-128 & UG-129 — Van xả lỏng; ký hiệu đánh dấu", "UG-128 & UG-129 — Liquid relief valves; marking"))
    b.append(p("<b>UG-128:</b> van xả lỏng dùng cho Division này phải cỡ tối thiểu NPS ½. "
               "<b>UG-129:</b> mỗi van (kể cả van chính của van pilot) từ NPS ½ trở lên "
               "được ghi rõ, không bị xóa trong vận hành: (1) tên nhà chế tạo và đơn vị "
               "lắp ráp; (2) số kiểu thiết kế; (3) cỡ NPS cửa vào; (4) áp thiết lập; (5) "
               "công suất chứng nhận — lb/h hơi bão hòa, hoặc gal/phút nước 70°F, hoặc "
               "SCFM/lb/phút không khí (60°F, 14,7 psia) — tất cả ở quá áp 10% hoặc 3 psi "
               "tùy cái lớn hơn; van chứng nhận theo UG-131(c)(2) ghi “ở quá áp 20%”; "
               "(6) năm sản xuất hoặc mã nhận biết; (7) ký hiệu ASME theo Hình UG-129. Van "
               "nhỏ hơn NPS ½ có thể gắn thẻ kim loại. Van mang dấu Section I dùng cho "
               "Section VIII được theo (b)."))
    b.append(p("<b>Van phối hợp đĩa nứt</b> (c) ghi thêm công suất theo hệ số 0,90 hoặc hệ "
               "số tổ hợp thử nghiệm; <b>phối hợp chốt gãy</b> (d) ghi áp định mức trên chốt "
               "và vỏ. <b>Đĩa nứt</b> (e) ghi trên vành đĩa hoặc thẻ kim loại: tên nhà chế "
               "tạo, số kiểu, số lô, vật liệu, cỡ NPS, áp nứt đóng dấu, nhiệt độ đĩa tương "
               "ứng, công suất (hơi bão hòa lb/h hoặc không khí ft³/phút); các mục (1), (2), "
               "(5) cũng ghi trên giá đỡ đĩa. <b>Thiết bị tải lò xo không đóng lại</b> (f) "
               "đánh dấu theo (a), chỉ đóng dấu Code khi công suất đã chứng nhận theo "
               "UG-127(c)(3)."))

    b.append(h2("UG-130 — Dấu Code", "UG-130 — Use of the Code Symbol Stamp"))
    b.append(p("Mỗi van xả áp mang dấu Code phải do nhà chế tạo hoặc đơn vị lắp ráp giữ "
               "<b>Giấy chứng nhận ủy quyền (UG-117)</b> còn hiệu lực và đã chứng nhận "
               "công suất theo quy định Division này. Dấu chính thức — ký hiệu UV — thể "
               "hiện dưới đây:"))
    b.append(fig(1, F.fig_f81()))

    b.append(h2("UG-131 — Chứng nhận công suất", "UG-131 — Capacity certification"))
    b.append(p("(a)–(c) Trước khi đóng dấu Code, nhà chế tạo phải chứng nhận công suất. "
               "Thử với <b>khí nén</b> trên hơi bão hòa khô (chất lượng ≥ 98%, quá nhiệt ≤ "
               "20°F), không khí hoặc khí tự nhiên; với <b>chất lỏng không nén</b> trên nước "
               "40–125°F. Áp thử không vượt quá áp thiết lập hơn 10% hoặc 3 psi (trừ van "
               "cho UG-125(c)(3): ≤ 120% áp đóng dấu); áp thử tối thiểu hơn thiết lập 3 psi; "
               "ghi lại áp hạ. Van có blowdown chỉnh được phải đặt blowdown ≤ 5% thiết lập "
               "hoặc 3 psi trước khi thử. Van pilot có thể chứng nhận không kèm pilot nếu "
               "thử nghiệm chứng minh pilot mở van chính đầy ở ≤ thiết lập + 10%/3 psi."))
    b.append(p("(d) <b>Thử từng tổ hợp cỡ–thiết kế–áp:</b> mỗi bộ 3 van, chênh lệch trong "
               "± 5% quanh trung bình; công suất đóng dấu ≤ 90% trung bình. Với khí nén tính "
               "độ dốc W/P từng điểm, mọi giá trị trong ± 5% của trung bình (nếu không, "
               "thử thêm tối đa 4 van); đóng dấu ≤ 0,90 × dốc trung bình × áp tích tụ tuyệt "
               "đối [1,10 × thiết lập + 14,7 hoặc thiết lập + 3 + 14,7, chọn lớn hơn; van "
               "theo (c)(2) dùng 1,20]. Với chất lỏng: vẽ công suất theo hiệu áp trên giấy "
               "log–log, đường thẳng qua 4 điểm (điểm lệch > 5% là kém — thử lại tối đa 2 "
               "van/điểm); đóng dấu ≤ 90% giá trị trên đường."))
    b.append(p("(e) <b>Hệ số xả K theo thiết kế:</b> nộp ≥ 9 van (3 cỡ × 3 áp thiết lập); "
               "mỗi lần thử cho K<sub>D</sub> = dòng thực tế đo được / dòng lý thuyết "
               "tính theo công thức:"))
    for e in _eq_theoretical("vi"):
        b.append(e)
    b.append(p("trong đó A — diện tích xả thực tế tại hành trình mở đạt được; P = (thiết "
               "lập × 1,10) + áp khí quyển hoặc thiết lập + 3 psi + khí quyển, chọn lớn "
               "hơn; P<sub>d</sub> — áp phía xả; M — khối lượng phân tử; T — nhiệt độ tuyệt "
               "đối (°F + 460); C — hằng số theo k = c<sub>p</sub>/c<sub>v</sub>; Z — hệ số "
               "nén; w — trọng lực riêng của nước tại điều kiện cửa vào. Hơi trên 1500 psig "
               "đến 3200 psig: W<sub>T</sub> nhân hệ số hiệu chỉnh "
               "(0,1906P − 1000)/(0,2292P − 1061)."))
    for e in _eq_kd("vi"):
        b.append(e)
    b.append(p("Mọi K<sub>D</sub> thực nghiệm phải nằm trong ± 5% của trung bình; nước quy "
               "sang gal/phút nhân 1/500. K áp dụng cho van có tỷ số β (cổ họng/cửa vào) "
               "trong 0,15–0,75 trừ khi thử chứng minh; van dùng lift xác định diện tích "
               "phải cùng tỷ số L/D danh nghĩa."))
    b.append(p("(f)–(g) Thử tại cơ sở đạt ASME/ANSI PTC 25.3, có Người quan sát được ủy "
               "quyền (Authorized Observer); dữ liệu nộp cho ASME để xem xét (công suất các "
               "van được công bố trong “Pressure Relief Device Certifications” của National "
               "Board). Thay đổi thiết kế phải thử lại. (h) Van hơi áp tuyệt đối ≤ 1500 psia "
               "được định mức theo PG-69.1.2 ở 103% áp dòng rồi nâng lên 110% bằng hệ số:"))
    for e in _eq_103_110("vi"):
        b.append(e)
    b.append(p("Hệ số này không dùng để chia ngược; với hơi > 1500 psig không áp dụng. "
               "(i) Van kiểu nozzle định mức nước bão hòa theo 11-2. (j) Mọi thay đổi ảnh "
               "hưởng đường dòng, lift hoặc đặc tính đều phải thử lại."))

    b.append(h2("UG-132 — Chứng nhận tổ hợp với thiết bị không đóng lại",
                "UG-132 — Combination certification"))
    b.append(p("<b>Đĩa nứt phía vào:</b> thử cỡ đĩa nhỏ nhất kèm van cỡ tương đương có cổ "
               "họng lớn nhất của cỡ đó; hơi bão hòa, không khí hoặc khí tự nhiên; áp nứt "
               "đóng dấu giữa 90% và 100% áp thiết lập van. Quy trình: thử một van đơn lẻ ở "
               "quá áp 10%, rồi lắp đĩa phía vào và thử tổ hợp cũng ở quá áp 10%; lặp với "
               "tổng cộng 3 đĩa — kết quả trong ± 10% trung bình, nếu không phải thử lại "
               "tìm nguyên nhân. <b>Hệ số công suất tổ hợp (Combination Capacity Factor)</b> "
               "= công suất tổ hợp trung bình / công suất van đơn; dùng nhân vào công suất "
               "ASME của thiết kế van ở mọi cỡ, giá trị ≤ 1, chỉ áp dụng cho cùng thiết kế "
               "van và đĩa đã thử. Có thể thử thêm 2 cỡ lớn hơn và áp suất cao hơn để mở "
               "rộng hệ số (≤ 1). <b>Chốt gãy phối hợp van</b> chứng nhận theo UG-131(d) "
               "hoặc (e) như một tổ hợp."))

    b.append(h2("UG-133 & UG-134 — Nhu cầu xả và áp suất thiết lập",
                "UG-133 & UG-134 — Relieving requirements; pressure setting"))
    b.append(p("<b>UG-133:</b> tổng công suất thiết bị nối với bình (hoặc hệ bình) phải "
               "xả được lượng tối đa có thể sinh ra/cấp vào mà không để áp tăng quá <b>16%</b> "
               "MAWP khi đang xả; thiết bị bổ sung chống hỏa hoạn giữ mức <b>21%</b>. Bình "
               "nối bằng đường ống không có van cách ly coi như một đơn vị. Trao đổi nhiệt "
               "và tương tự phải có thiết bị đủ công suất cho trường hợp hỏng nội bộ. Công "
               "suất chính thức là công suất đóng dấu. Quy đổi chất lưu khác theo Phụ lục "
               "11. Quy đổi sang áp xả > 1,10p nhân hệ số:"))
    for e in _eq_prorate("vi"):
        b.append(e)
    b.append(p("P — áp xả (psig), p — áp thiết lập (psig); không áp dụng cho hơi trên 1500 "
               "psig. <b>UG-134:</b> một thiết bị: thiết lập ≤ MAWP; nhiều thiết bị: một "
               "thiết bị ≤ MAWP, các thiết bị còn lại ≤ <b>105%</b> MAWP; thiết bị chống "
               "hỏa hoạn ≤ <b>110%</b> MAWP (nếu kiêm vai trò (c) thì ≤ MAWP). Áp thiết lập "
               "tính cả cột áp tĩnh và áp ngược không đổi. Dung sai thiết lập: ± 2 psi "
               "(≤ 70 psi) hoặc ± 3% (trên 70 psi); van theo UG-125(c)(3): −0%, +10%."))

    b.append(h2("UG-135 — Lắp đặt", "UG-135 — Installation"))
    b.append(p("Thiết bị cho dịch vụ hơi/khí nối vào <b>không gian hơi</b> phía trên mặt "
               "chất lỏng; thiết bị cho dịch vụ lỏng nối dưới mức chất lỏng thông thường. "
               "Mọi đường ống và phụ kiện giữa bình và thiết bị phải có tiết diện ≥ cửa vào "
               "thiết bị, dòng vào trực tiếp, không cản trở (Appendix M). Nhiều thiết bị "
               "trên một cổng: tiết diện cổng ≥ tổng tiết diện cửa vào các thiết bị. "
               "<b>Không có van chặn</b> giữa bình và thiết bị bảo vệ hoặc giữa thiết bị và "
               "điểm xả, trừ khi (1) đóng tối đa số van chặn vẫn giữ công suất xả không thấp "
               "hơn yêu cầu, hoặc (2) theo điều kiện Appendix M. Đường xả dẫn đến nơi an "
               "toàn, có thoát nước, kích thước sao cho áp không làm giảm công suất xả hay "
               "gây vận hành bất thường của thiết bị:"))
    b.append(fig(2, F.fig_f84()))

    b.append(h2("UG-136 — Yêu cầu tối thiểu cho van xả áp", "UG-136 — Minimum requirements for pressure relief valves"))
    b.append(h3("(a) Cơ khí", "(a) Mechanical"))
    b.append(ul([
        "(1) Cấu tạo dẫn hướng bảo đảm vận hành nhất quán và kín.",
        "(2) Lò xo: nén đầy hành trình ≤ 80% độ nén chạm khối; biến dạng dư ≤ 0,5% chiều "
        "cao tự do (đo 10 phút sau khi nén chạm khối lần thứ ba).",
        "(3) Van cho không khí, nước > 140°F hoặc hơi phải có bộ nhấc (lifting device) tác "
        "động ở ≥ 75% áp thiết lập; van pilot có bộ nhấc hoặc cổng nạp áp pilot kiểm chứng.",
        "(4) Đệm van gắn vào thân không thể bật ra. (5) Thiết kế thân hạn chế tác động cặn.",
        "(6) Van đầu nối ren có mặt để vặn wrench khi lắp đặt. (7) Mọi điều chỉnh ban đầu "
        "đều niêm phong; tem niêm phong nhận biết đơn vị điều chỉnh (van > NPS ½).",
        "(8) Có van thoát nước tại điểm thấp nhất nơi chất lỏng có thể tích trên phía xả đệm.",
        "(9) Van màng: khoang trên màng phải thông khí; hỏng màng không làm mất khả năng "
        "xả đúng công suất.",
    ]))
    b.append(h3("(b) Vật liệu", "(b) Materials"))
    b.append(p("Không dùng gang cho đệm và đĩa. Các mặt trượt kề nhau (bầu dẫn hướng, đĩa, "
               "giữ đĩa) cùng chống ăn mòn; lò xo chống ăn mòn hoặc có lớp phủ. Vật liệu "
               "thân, nắp, yoke thuộc Section II; với nhiệt độ sử dụng dưới −20°F, thân và "
               "bulong thép cacbon/thép hợp kim thấp phải đạt UCS-66 trừ khi tỷ số tương "
               "ứng theo Hình UCS-66.1 ≤ 0,4 hoặc được miễn thử va đập. Vật liệu cổ họng, "
               "đĩa, phần bên trong thuộc một trong: Section II, tiêu chuẩn ASTM, hoặc do "
               "nhà chế tạo van kiểm soát."))
    b.append(h3("(c)–(f) Thử sản xuất, kiểm tra, thiết kế, hàn", "(c)–(f) Production testing, inspection, design, welding"))
    b.append(p("Mỗi van được thử áp và (cần thiết) thử hơi đủ thời gian; thử độ kín đệm; "
               "phần áp chính của van trên giới hạn được thử theo quy định. Nhà chế tạo/lắp "
               "ráp phải chứng minh mẫu sản xuất ngẫu nhiên đạt như các van đã chứng nhận "
               "công suất; hoạt động chế tạo, lắp ráp, kiểm tra và thử nghiệm chịu thanh "
               "tra của ASME bất cứ lúc nào. <b>Quyền dùng dấu UV</b> cấp theo chu kỳ 5 năm: "
               "mỗi lần gia hạn chọn 2 van sản xuất ngẫu nhiên thử vận hành + công suất tại "
               "phòng thử nghiệm được chấp nhận; blowdown chỉnh ≤ 7% thiết lập hoặc 3 psi; "
               "van thay thế không đạt sẽ thu hồi quyền trong 60 ngày. Van lắp ráp phải dùng "
               "linh kiện gốc không biến đổi; ngoài yêu cầu UG-129 còn ghi tên nhà chế tạo "
               "và đơn vị lắp ráp, dấu Code là dấu của đơn vị lắp ráp. Yêu cầu thiết kế nộp "
               "kèm bản vẽ chi tiết; mọi công việc hàn thực hiện theo Division."))

    b.append(h2("ASME Phụ lục 11 — Quy đổi công suất", "ASME Appendix 11 — Capacity conversions"))
    b.append(p("<b>11-1.</b> Công suất của van an toàn theo chất khác chất định mức xác "
               "định bằng: hơi W<sub>s</sub> = 51,5 KAP; không khí "
               "W<sub>a</sub> = CKAP&#8201;√(M/T) với C = 356, M = 28,97, T = 520; khí/hơi "
               "bất kỳ W = CKAP&#8201;√(M/T). Khi k của hơi hydrocacbon không biết, dùng "
               "giá trị bảo thủ k = 1,001 (C = 315):"))
    b.append(eq('W = 315 K A P ' + _sq('M/T'), "Phụ lục 11 — hydrocacbon, k = 1,001"))
    b.append(p("trong đó K — hệ số xả theo UG-131(d)/(e), A — diện tích xả thực tế "
               "(in²), P = (thiết lập × 1,10) + áp khí quyển (psia). Các công thức cũng "
               "dùng ngược lại khi biết dòng cần xả mà phải tính công suất hơi/không khí."))
    b.append(p("<b>Ví dụ 2.</b> Xả 5000 lb/h propane, T<sub>vào</sub> = 125°F, k không "
               "biết → dùng C = 315: KAP = 5000&#8201;√(44,09/585)/315 = 57,7; hơi tương "
               "đương W<sub>s</sub> = 51,5 × 57,7 = <b>2970 lb/h</b>. <b>Ví dụ 3.</b> Xả "
               "1000 lb/h amoniac ở 150°F, chọn k = 1,33 → C = 350: KAP = 17,10; "
               "W<sub>s</sub> = 51,5 × 17,10 = <b>880 lb/h hơi</b>. <b>Ví dụ 4.</b> Van "
               "định mức 10 000 ft³/phút không khí (60°F, 14,7 psia) = 45 960 lb/h; KAP = "
               "546; W<sub>s</sub> = 51,5 × 546 = <b>28 200 lb/h hơi</b> cùng áp thiết lập "
               "(trước khi quy đổi phải đạt UG-131(b))."))
    b.append(_t_ctable("vi"))
    b.append(fig(3, F.fig_f82()))
    b.append(_t_mw("vi"))
    b.append(p("<b>11-2 — Nước bão hòa.</b> Vì công suất trên nước bão hòa phụ thuộc cấu "
               "tạo, định mức chỉ áp cho van <b>kiểu nozzle</b> (β = 0,25–0,80, chuyển "
               "tiếp nét, K<sub>D</sub> > 0,90). Cách đọc: vào biểu đồ tại áp thiết lập, đi "
               "lên tới đường nước bão hòa, đọc ngang ra công suất xả (giá trị lý thuyết "
               "isentrôpic, giả thiết dòng cân bằng và tỷ số áp tới hạn tính toán). Nếu sau "
               "lần xả đầu lưu chuyển thành hơi khô, van phải định mức theo hơi bão hòa "
               "khô; van trên bình/đường ống hỗn hợp nước–hơi định mức theo hơi khô."))
    b.append(fig(4, F.fig_f83()))

    b.append(h2("ASME Phụ lục M — Lắp đặt và vận hành", "ASME Appendix M — Installation and operation"))
    b.append(p("<b>M-1.</b> Các quy tắc chỉ mang tính thông tin chung: lắp đặt và vận hành "
               "bình chịu áp thuộc thẩm quyền pháp lý của địa phương. <b>M-2.</b> Bình dễ "
               "ăn mòn ngoài phải bố trí đủ chỗ kiểm tra; nắp kiểm tra phải tiếp cận được; "
               "bình đứng dập đáy nên úp lõm về phía áp để thoát nước hoàn toàn. "
               "<b>M-3.</b> Ký hiệu trên bình phải còn nhìn thấy sau lắp đặt, không bị "
               "cách nhiệt che phủ. <b>M-4.</b> Lắp đặt thiết bị xả áp quy định đầy đủ ở "
               "UG-135; dưới đây là chi tiết van chặn và đường ống."))
    b.append(p("<b>M-5 — Van chặn phía vào:</b> chỉ cho mục đích kiểm tra/sửa chữa, phải "
               "khóa hoặc niêm ở vị trí mở, chỉ đóng bởi người được ủy quyền và người đó "
               "phải trực tại chỗ suốt thời gian van đóng, mở lại khóa trước khi rời vị trí. "
               "Bình nhận áp hoàn toàn từ nguồn ngoài có thể đặt van chặn từng bình mà "
               "không cần khóa mở, miễn van chặn đồng thời cắt bình khỏi nguồn áp. "
               "<b>M-6 — Van chặn phía xả:</b> cho phép khi xả vào đường góp chung để ngăn "
               "dòng từ các bình đang vận hành tràn ngược; khóa/niêm ở vị trí mở hoặc đóng "
               "bởi người ủy quyền; khi đóng trong vận hành phải có người trực và van phía "
               "vào phải đóng trước."))
    b.append(p("<b>M-7 — Tổn thất áp phía vào:</b> đường ống, van, phụ kiện và cổng bình "
               "tới van phải ≥ cỡ cửa vào; tổng tổn thất không hồi phục ≤ <b>3%</b> áp "
               "thiết lập, tính theo công suất bảng tên hiệu chỉnh cho lưu chất. Nhiều van "
               "trên một cổng: tiết diện cổng ≥ tổng tiết diện các van. <b>M-8 — Đường "
               "xả:</b> ưu tiên ống ngắn/đứng thẳng qua khuỷu bán kính lớn, xả thẳng ra khí "
               "quyển, cỡ ≥ cửa ra van; đường xả kiểu ống trong ống (telescopic) có khay "
               "hứng nước ngưng được khuyến nghị; đường góp chung cho các van có thể xả "
               "đồng thời thiết kế theo tổng tiết diện ra và tính tổn thất về phía hạ lưu; "
               "áp tĩnh tại mặt bích xả van lò xo thông thường không vượt <b>10%</b> áp "
               "thiết lập khi xả đúng công suất; mọi đường xả phải thoát nước. "
               "<b>M-9.</b> Hệ thống xả của thiết bị không đóng lại phải cỡ sao cho áp bình "
               "không vượt quá áp quá cho phép. <b>M-10.</b> Ảnh hưởng của xả vào đường góp "
               "chung theo từng loại van — tra tài liệu nhà chế tạo."))
    b.append(p("<b>M-11 — Chênh lệch áp:</b> phải xét đủ điều kiện khởi động, dừng, sự cố "
               "quá trình, thời gian đáp ứng thiết bị, xung áp do van đóng nhanh; lưu chất "
               "độc, ăn mòn hoặc quý cần chênh lệch lớn hơn. <b>Blowdown</b> là yếu tố đầu "
               "tiên: van thiết lập 100 psig blowdown 7% đóng ở 93 psig — áp vận hành phải "
               "giữ dưới mốc này; blowdown van lớn khó kiểm chứng chính xác nếu không thử "
               "ngay hiện trường. Van pilot có thể đặt blowdown ngắn tới 2% nhưng van chính "
               "có thể lệch; đường ống nối pilot–van chính không được quá tổn thất. Van "
               "pilot không dùng cho dịch vụ bẩn, mài mòn, đóng cốc/polymer/ăn mòn bộ phận "
               "pilot, hay lưu chất có thể đóng băng/ngưng tụ. Độ kín nên đạt ở áp không "
               "thấp hơn áp vận hành (thủ tục tham chiếu ANSI B146.1) và không coi là vĩnh "
               "viễn. Khuyến nghị chung:"))
    b.append(_t_m11("vi"))
    b.append(p("Van cỡ đệm nhỏ cần bảo dưỡng nhiều hơn khi chênh lệch tiến sát mức khuyến "
               "nghị. <b>M-12.</b> Van lò xo lắp thẳng đứng (trục van thẳng) trừ khi bố trí "
               "không cho phép — khi đó van phải thiết kế phù hợp vị trí nghiêng, lưu chất "
               "không lắng đọng ở cửa vào, thoát nước phía xả đủ. <b>M-13.</b> Lực phản "
               "ứng dòng xả và tải ngoài (giãn nhiệt, ống không đỡ) gây mô men uốn — tính "
               "toán khi thiết kế lắp đặt. <b>M-14.</b> Định cỡ cho hỏa hoạn tham chiếu: API "
               "RP 520 Phần I và API Standard 2000, AAR M-1002, CGA S-1.1/S-1.2/S-1.3, NFPA "
               "30/59/59A, và các nghiên cứu thử đuốc của Phillips Petroleum. <b>M-15.</b> "
               "Đồng hồ áp (nếu có) có dải thước giới hạn trên không thấp hơn 1,25 × áp "
               "thiết lập thiết bị và không quá 2 × MAWP của bình."))

    b.append(h2("Thông tin khác — bảo hành, đặt hàng, dịch vụ", "Other information — warranty, ordering, service"))
    b.append(p("Phần cuối cẩm nang là nội dung thương mại: <b>bảo hành</b> 18 tháng kể từ "
               "giao hàng hoặc 12 tháng kể từ lắp đặt (tùy cái đến trước), loại trừ ăn mòn, "
               "mài mòn, hao mòn tự nhiên và vận hành sai; <b>cảnh báo an toàn</b> — sản "
               "phẩm là linh kiện an toàn, việc áp dụng sai hoặc dùng phụ tùng không chính "
               "hãng có thể gây hỏng thiết bị, mọi lắp đặt/bảo trì/thử nghiệm phải theo "
               "các code và tiêu chuẩn áp dụng; <b>đặt hàng</b> qua Phiếu đặc tả van xả áp "
               "(Pressure Relief Valve Specification Sheet) gồm 53 ô: mục đích chung, đầu "
               "nối, vật liệu, tùy chọn (cap, đòn bẩy, test gag, nút thử, chặn dòng ngược…), "
               "dữ liệu đầu vào (lưu chất, công suất yêu cầu, M, áp thiết lập/vận hành, "
               "nhiệt độ, áp ngược, quá áp cho phép, Z, ẩn nhiệt, k, độ nhớt), kết quả tính "
               "(diện tích tính/chọn, ký hiệu cổ họng); <b>phụ tùng</b> kèm số serial và số "
               "đơn hàng gốc; <b>dịch vụ</b> — trung tâm sửa chữa tại Wrentham (MA), Anh, "
               "Scotland, Singapore, Brazil, Ấn Độ; dịch vụ hiện trường; đào tạo; thử "
               "nghiệm. Crosby đạt chứng nhận ISO 9001 (1992 — nhà chế tạo van xả áp Hoa Kỳ "
               "đầu tiên), ISO 9002 (Anh 1991, Scotland 1992) và tuân thủ Vd TÜV theo "
               "AD-Merkblatt A2/TRD-421 cho các kiểu JOS, JBS, JLT và Series 900 OMNI-TRIM."))

    b.append(note("Tóm tắt: phụ lục trích các đoạn UG-125–UG-136 của ASME Section VIII "
                  "Division 1 — yêu cầu thiết bị xả áp, giới hạn quá áp 10/16/21%, định cỡ "
                  "và chứng nhận công suất (K ≤ 0,878), đánh dấu và dấu Code UV, lắp đặt — "
                  "cùng Phụ lục 11 (quy đổi công suất, ví dụ, bảng C và khối lượng phân "
                  "tử, định mức nước bão hòa) và Phụ lục M (van chặn, tổn thất áp vào ≤ 3%, "
                  "đường xả, chênh lệch áp khuyến nghị, lực phản ứng, định cỡ hỏa hoạn, "
                  "đồng hồ áp)."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc "
               "© 1997 Crosby Valve Inc.; trích dẫn ASME Section VIII Division 1 © ASME "
               "International.</i>"))
    return "".join(b)


# =====================================================================
def body_en():
    b = []
    b.append(p("This appendix excerpts the essential paragraphs of <b>ASME Section VIII, "
               "Division 1 (1992 Edition through the 1994 Addenda)</b> governing pressure "
               "relief devices — paragraphs UG-125 through UG-136 — together with Appendix "
               "11 (capacity conversions) and Appendix M (installation and operation). It "
               "gives the handbook's user direct insight into Code requirements. The ASME "
               "Code is revised annually and reissued every three years; Crosby recommends "
               "that the proper edition and revision be applied whenever the Code is used."))
    b.append(note("<b>Scope.</b> This is a structural condensation that keeps every mandatory "
                  "number (overpressure allowances, tolerances, coefficients) — it does not "
                  "replace the Code text itself."))

    b.append(h2("UG-125 — General", "UG-125 — Quy định chung"))
    b.append(p("(a) All pressure vessels within the scope of this Division, irrespective of "
               "size or pressure, shall be provided with protective devices per UG-125 through "
               "UG-136. The user is responsible for proper installation before initial "
               "operation; the devices need not be supplied by the vessel manufacturer. "
               "Definitions in Appendix I of ASME/ANSI PTC 25.3 apply. (b) An unfired steam "
               "boiler, per U-1(g), shall be equipped with pressure relief devices required "
               "by Section I."))
    b.append(p("(c) All vessels other than unfired steam boilers shall be protected so that "
               "pressure does not rise above the following allowances (see UG-134 for "
               "pressure settings):"))
    b.append(ul([
        "<b>Single device:</b> ≤ MAWP + 10% or + 3 psi, whichever is greater;",
        "<b>Multiple devices</b> set per UG-134(a): ≤ MAWP + 16% or + 4 psi;",
        "<b>Supplemental fire protection</b> (UG-125(c)(2)): ≤ MAWP + 21%;",
        "<b>Nonrefrigerated liquefied compressed gas storage</b> with no permanent supply "
        "connection (UG-125(c)(3)): fire-only devices are exempt from (c)(1)/(c)(2) provided "
        "pressure stays ≤ MAWP + 20%, set pressure ≤ MAWP, the vessel has sufficient ullage "
        "against liquid-full conditions, MAWP exceeds the vapor pressure of the stored gas "
        "at the maximum anticipated temperature (normally not less than 115°F), and the "
        "valves comply with UG-129(a)(5), UG-131(c)(2) and UG-134(d)(2). (Gas = substance "
        "with vapor pressure > 40 psia at 100°F.)",
    ]))
    b.append(p("(d) Devices shall be accessible for inspection and repair, not readily "
               "rendered inoperative (see Appendix M), and selected for the intended "
               "service. (e) Pressure relief valves (reclosing) or nonreclosing devices may "
               "be used — the latter alone or in combination with safety or safety relief "
               "valves; rupture disk devices may be advisable where very rapid rates of "
               "pressure rise may occur, where the medium would render a valve inoperative, "
               "or where loss of valuable or noxious material must be avoided. (f) Vessels "
               "operating completely filled with liquid shall have liquid-service devices. "
               "(g) Where the pressure source is external and under positive control such "
               "that vessel pressure cannot exceed MAWP, the devices need not be mounted on "
               "the vessel — but pressure-reducing valves and similar control instruments "
               "are not considered positive in action (except pilot-operated valves per "
               "UG-126(b)). (h) Steam-service valves shall meet UG-131(b)."))

    b.append(h2("UG-126 — Pressure relief valves", "UG-126 — Van xả áp"))
    b.append(p("(a) Safety, safety relief and relief valves shall be of the <b>direct spring "
               "loaded</b> type. (b) Pilot-operated valves may be used provided the pilot is "
               "self-actuated and the main valve opens automatically at not over the set "
               "pressure and discharges its full rated capacity if any essential part of the "
               "pilot fails. (c) The spring shall not be set more than ± 5% from the marked "
               "pressure unless within the manufacturer's spring design range; initial "
               "adjustment is performed by the manufacturer, its authorized representative "
               "or an assembler, with a data tag (set pressure, capacity, date) and a seal. "
               "(d) Set-pressure tolerance: ± 2 psi up to and including 70 psi, ± 3% above "
               "70 psi."))

    b.append(h2("UG-127 — Nonreclosing pressure relief devices", "UG-127 — Thiết bị xả không đóng lại"))
    b.append(h3("Rupture disk devices", "Đĩa nứt (rupture disk)"))
    b.append(p("Every disk carries a stamped burst pressure established within the "
               "<b>manufacturing design range (MDR)</b> at the specified disk temperature, "
               "and a lot number. Burst tolerance: + 2 psi up to and including 40 psi, "
               "+ 5% above 40 psi. The stamped pressure is established by bursting: (1) at "
               "least two sample disks per lot (one at room temperature), rating = average "
               "burst at coincident temperature; (2) at least four disks (≥ 5% of the lot) "
               "at four temperatures to build a burst-pressure–temperature curve, then "
               "interpolating; or (3) for prebulged solid-metal or graphite disks, a "
               "percent-ratio curve from one size per material lot plus two room-temperature "
               "samples. All lot tests use a holder of the same form and dimensions as the "
               "installed disk."))
    b.append(p("<b>Capacity rating:</b> not more than the applicable theoretical formula "
               "(UG-131) multiplied by <b>K = 0.62</b>; area A is the minimum net area after "
               "complete burst (never exceeding the nominal pipe size area). A manufacturer "
               "may instead have capacity certified per UG-131. <b>Application:</b> a disk "
               "may be the sole relieving device; or installed between the valve and the "
               "vessel provided (i) the combination is ample per UG-133, (ii) the stamped "
               "capacity of a nozzle-type valve is multiplied by a factor of <b>0.90</b> "
               "(or the combination is tested per UG-132), (iii) the space between disk and "
               "valve carries a pressure gage, try cock, free vent or telltale to detect "
               "burst or leakage, and (iv) the post-burst opening passes the valve capacity "
               "and is at least the valve inlet area. On the valve outlet side: the valve "
               "must open at its set pressure regardless of accumulated back pressure (space "
               "vented/drained), the valve capacity is ample, disk burst pressure plus outlet "
               "piping pressure stays within the outlet design pressure and never above the "
               "vessel MAWP or the valve set pressure, contents are clean and free of gumming "
               "matter, and the bonnet is vented."))
    b.append(h3("Breaking pin devices", "Chốt gãy (breaking pin)"))
    b.append(p("Breaking pins are used <b>only in combination</b> with a safety or safety "
               "relief valve, never alone. The space between pin and valve carries a "
               "pressure gage, try cock, free vent or telltale. Each pin has a rated "
               "pressure and temperature, a lot number, and a break guarantee within these "
               "tolerances:"))
    b.append(_t_breakpin("en"))
    b.append(p("Rated pressure plus tolerance must not exceed <b>105% of the vessel MAWP</b>. "
               "The rated pressure at the coincident operating temperature is verified by "
               "breaking at least two sample pins per lot (lot ≤ 25) in a device of the same "
               "form and dimensions."))
    b.append(h3("Spring-loaded nonreclosing devices", "Thiết bị không đóng lại tải lò xo"))
    b.append(p("Opens at the set pressure and remains open until manually reset; if the "
               "actuating means fail, full opening occurs at or below set pressure. It may "
               "not be combined with any other pressure relief device. Opening tolerance "
               "≤ + 5%. Capacity ≤ theoretical value × K = 0.62 (A = flow area through the "
               "minimum opening), or certified per UG-131."))

    b.append(h2("UG-128 & UG-129 — Liquid relief valves; marking", "UG-128 & UG-129 — Van xả lỏng; ký hiệu đánh dấu"))
    b.append(p("<b>UG-128:</b> any liquid relief valve shall be at least NPS ½. <b>UG-129:</b> "
               "each valve (including the main valve of a pilot-operated valve) NPS ½ and "
               "larger is marked so as not to be obliterated in service with: (1) the name "
               "of the manufacturer and the assembler; (2) design or type number; (3) NPS "
               "inlet size; (4) set pressure; (5) certified capacity — lb/hr saturated "
               "steam, or gal/min water at 70°F, or SCFM/lb/min air (60°F, 14.7 psia) — "
               "all at 10% or 3-psi overpressure whichever is greater; valves certified per "
               "UG-131(c)(2) are marked “at 20% overpressure”; (6) year built or a coding; "
               "(7) the ASME symbol of Fig. UG-129. Valves smaller than NPS ½ may carry a "
               "metal tag. Valves bearing the Section I symbol are usable on vessels per (b)."))
    b.append(p("<b>Valves combined with rupture disks</b> (c) additionally carry the 0.90-"
               "factor capacity or the tested combination capacity factor; <b>breaking-pin "
               "combinations</b> (d) mark the rated pressure on the pin and its housing. "
               "<b>Rupture disks</b> (e) are marked on the flange or a metal tab: "
               "manufacturer's name, type number, lot number, disk material, NPS size, "
               "stamped burst pressure, coincident disk temperature, and capacity (lb/hr "
               "saturated steam or ft³/min air); items (1), (2) and (5) also go on the "
               "holder. <b>Spring-loaded nonreclosing devices</b> (f) are marked per (a), "
               "with the Code Symbol applied only when capacity is certified per "
               "UG-127(c)(3)."))

    b.append(h2("UG-130 — Code Symbol Stamp", "UG-130 — Dấu Code"))
    b.append(p("Each pressure relief valve to which the Code Symbol is applied shall have "
               "been fabricated or assembled by a manufacturer or assembler holding a valid "
               "<b>Certificate of Authorization (UG-117)</b> and capacity certified per this "
               "Division. The official symbol — the UV stamp — is shown here:"))
    b.append(fig(1, F.fig_f81()))

    b.append(h2("UG-131 — Capacity certification", "UG-131 — Chứng nhận công suất"))
    b.append(p("(a)–(c) Before the Code Symbol is applied, capacity must be certified. "
               "Compressible-fluid tests use dry saturated steam (98% minimum quality, "
               "20°F maximum superheat), air, or natural gas; incompressible-fluid tests "
               "use water at 40–125°F. Test pressure does not exceed set pressure by more "
               "than 10% or 3 psi (except valves for UG-125(c)(3): up to 120% of stamped "
               "set pressure); the minimum test pressure is 3 psi above set; reseating "
               "pressure is recorded. Valves with adjustable blowdown are adjusted to ≤ 5% "
               "of set pressure or 3 psi before testing. Pilot-operated valves may be "
               "certified without the pilot if testing demonstrates that the pilot opens "
               "the main valve fully at not more than set pressure + 10% or 3 psi."))
    b.append(p("(d) <b>Per size–design–setting:</b> three valves per set, each within "
               "± 5% of the average; stamped capacity ≤ 90% of the average. For "
               "compressible fluids the slope W/P of each test point is averaged; all values "
               "must fall within ± 5% of the average slope (otherwise up to four more "
               "valves are tested); the stamped capacity does not exceed 0.90 × average "
               "slope × absolute accumulation pressure [1.10 × set + 14.7 or set + 3 + "
               "14.7, whichever is greater; valves per (c)(2) use 1.20]. For incompressible "
               "fluids, capacity versus differential pressure is plotted log–log and a "
               "straight line drawn through the four points (a point departing > 5% is "
               "unsatisfactory — two more valves per bad point); stamped capacity ≤ 90% of "
               "the line value."))
    b.append(p("(e) <b>Design coefficient of discharge K:</b> at least nine valves (three "
               "sizes at three set pressures) are submitted; each test run yields "
               "K<sub>D</sub> = measured actual flow / theoretical flow computed from:"))
    for e in _eq_theoretical("en"):
        b.append(e)
    b.append(p("where A is the actual discharge area at developed lift; P = (set × 1.10) "
               "+ atmospheric, or set + 3 psi + atmospheric, whichever is greater; "
               "P<sub>d</sub> is the discharge pressure; M the molecular weight; T the "
               "absolute inlet temperature (°F + 460); C the constant for k = "
               "c<sub>p</sub>/c<sub>v</sub>; Z the compressibility factor; w the specific "
               "weight of water at inlet conditions. For dry saturated steam above 1500 "
               "psig up to 3200 psig, W<sub>T</sub> is corrected by "
               "(0.1906P − 1000)/(0.2292P − 1061)."))
    for e in _eq_kd("en"):
        b.append(e)
    b.append(p("All experimental K<sub>D</sub> values must fall within ± 5% of the average; "
               "water capacity converts to gal/min by × 1/500. K applies to valves with "
               "beta ratio (throat/inlet) 0.15–0.75 unless tests demonstrate otherwise; "
               "lift-determined-area designs share one nominal lift-to-seat ratio (L/D)."))
    b.append(p("(f)–(g) Tests are conducted at facilities meeting ASME/ANSI PTC 25.3 under "
               "an Authorized Observer accepted by ASME; test data reports go to the ASME "
               "designee (valve capacities are published in the National Board's “Pressure "
               "Relief Device Certifications”). Design changes require retesting. (h) "
               "Safety valves at absolute pressures up to 1500 psia may be rated per PG-69.1.2 "
               "at a 103% flow pressure and raised to the 110% permitted flow pressure by "
               "the multiplier:"))
    for e in _eq_103_110("en"):
        b.append(e)
    b.append(p("This multiplier must not be used as a divisor; above 1500 psig it does not "
               "apply. (i) Nozzle-type valves may be rated for saturated water per 11-2. "
               "(j) Any design change affecting flow path, lift or performance requires new "
               "tests."))

    b.append(h2("UG-132 — Certification of combinations with nonreclosing devices",
                "UG-132 — Chứng nhận tổ hợp với thiết bị không đóng lại"))
    b.append(p("<b>Rupture disk at the inlet:</b> test the smallest disk device size with "
               "the equivalent-size valve carrying the largest orifice of that inlet size, "
               "on saturated steam, air or natural gas; the stamped burst pressure is 90% "
               "to 100% of the valve set pressure. Procedure: test one valve alone at 10% "
               "overpressure, then with a disk installed ahead of it and burst, again at "
               "10%; repeat with three disks total — results within ± 10% of the average, "
               "otherwise retest to find the cause. The <b>Combination Capacity Factor</b> "
               "= average combination capacity / individual valve capacity multiplies the "
               "ASME rated capacity of the valve design in all sizes; it shall not exceed "
               "one and applies only to the tested designs of valve and disk. Optional "
               "tests may extend the factor to the next two larger sizes and to higher "
               "pressures (factor ≤ 1). <b>Breaking-pin combinations</b> are capacity "
               "tested per UG-131(d) or (e) as a combination."))

    b.append(h2("UG-133 & UG-134 — Relieving requirements and pressure setting",
                "UG-133 & UG-134 — Nhu cầu xả và áp suất thiết lập"))
    b.append(p("<b>UG-133:</b> the aggregate capacity of the devices on a vessel (or system "
               "of vessels) shall carry off the maximum quantity that can be generated or "
               "supplied without permitting more than a <b>16%</b> rise above MAWP while "
               "blowing; supplemental fire protection holds the rise to <b>21%</b>. Vessels "
               "interconnected by adequate piping without isolating valves count as one "
               "unit. Heat exchangers and similar vessels get devices sized for internal "
               "failure. The official rated capacity is the stamped capacity. Non-steam/air "
               "ratings convert per Appendix 11. To prorate to a relieving pressure above "
               "1.10p, multiply by:"))
    for e in _eq_prorate("en"):
        b.append(e)
    b.append(p("P = relieving pressure (psig), p = set pressure (psig); not applicable to "
               "steam above 1500 psig. <b>UG-134:</b> a single device is set at ≤ MAWP; "
               "with multiple devices only one need be at ≤ MAWP and the others at ≤ "
               "<b>105%</b> of MAWP; fire-protection devices ≤ <b>110%</b> of MAWP (if "
               "serving both roles, ≤ MAWP). Set pressure includes static head and constant "
               "back pressure. Set tolerance: ± 2 psi (≤ 70 psi) or ± 3% (> 70 psi); valves "
               "per UG-125(c)(3): −0%, +10%."))

    b.append(h2("UG-135 — Installation", "UG-135 — Lắp đặt"))
    b.append(p("Vapor-service devices connect to the <b>vapor space</b> above the contained "
               "liquid; liquid-service devices below normal liquid level. All pipe and "
               "fittings between vessel and device have at least the area of the device "
               "inlet, with direct, unobstructed flow (Appendix M). Two or more devices on "
               "one connection: the connection's internal cross-sectional area is at least "
               "the combined inlet areas. <b>No intervening stop valves</b> between vessel "
               "and protective devices or between devices and the point of discharge, "
               "except (1) when closing the maximum number of block valves still leaves "
               "the required relieving capacity, or (2) under Appendix M conditions. "
               "Discharge lines lead to a safe place, drain freely, and are sized so that "
               "any pressure that develops will not reduce relieving capacity or adversely "
               "affect operation:"))
    b.append(fig(2, F.fig_f84()))

    b.append(h2("UG-136 — Minimum requirements for pressure relief valves",
                "UG-136 — Yêu cầu tối thiểu cho van xả áp"))
    b.append(h3("(a) Mechanical", "(a) Cơ khí"))
    b.append(ul([
        "(1) Guiding arrangements ensure consistent operation and tightness.",
        "(2) Spring: full-lift compression ≤ 80% of nominal solid deflection; permanent "
        "set ≤ 0.5% of free height (measured 10 min after the third solid compression).",
        "(3) Valves on air, water over 140°F, or steam carry a substantial lifting device "
        "releasing the seat force at ≥ 75% of set pressure; pilot-operated valves get a "
        "lifting device or pilot pressurization means to verify free movement.",
        "(4) The seat is fastened to the body so it cannot lift. (5) Body design minimizes "
        "deposit effects.",
        "(6) Screwed-connection valves have wrenching surfaces. (7) All initial adjustments "
        "are sealed; the seal identifies the adjuster (valves above NPS ½).",
        "(8) A drain is provided at the lowest point where liquid can collect on the "
        "discharge side of the disk.",
        "(9) Diaphragm-type valves: the space above the diaphragm is vented; diaphragm "
        "failure must not impair rated relieving capacity.",
    ]))
    b.append(h3("(b) Materials", "(b) Vật liệu"))
    b.append(p("Cast iron seats and disks are not permitted. Adjacent sliding surfaces "
               "(guides, disks, disk holders) are corrosion resistant; springs are corrosion "
               "resistant or coated. Body, bonnet and yoke materials are Section II listed; "
               "carbon and low-alloy steel bodies, bonnets, yokes and bolting below −20°F "
               "meet UCS-66 unless the coincident ratio of Fig. UCS-66.1 is ≤ 0.4 or impact "
               "testing is exempted. Nozzle, disk and internal-part materials come from "
               "Section II, ASTM specifications, or controlled by the valve manufacturer."))
    b.append(h3("(c)–(f) Production testing, inspection, design, welding",
                "(c)–(f) Thử sản xuất, kiểm tra, thiết kế, hàn"))
    b.append(p("Each valve is pressure tested (steam valves tested with steam for sufficient "
               "time) and seat-tightness tested. The manufacturer/assembler demonstrates that "
               "random production samples perform like the capacity-certified valves; "
               "manufacturing, assembly, inspection and test operations are subject to ASME "
               "inspection at any time. <b>UV Code Symbol permission</b> runs in 5-year "
               "cycles: two sample production valves are selected and operationally and "
               "capacity tested at an accepted laboratory; adjustable blowdown is set ≤ 7% "
               "of set pressure or 3 psi; failure of replacement valves revokes the "
               "authorization within 60 days. Assemblers use original, unmodified parts; "
               "marking adds the manufacturer and assembler names, with the assembler's "
               "Code Symbol. Design requirements are submitted with detailed drawings; all "
               "welding follows this Division."))

    b.append(h2("ASME Appendix 11 — Capacity conversions", "ASME Phụ lục 11 — Quy đổi công suất"))
    b.append(p("<b>11-1.</b> The capacity of a safety valve in terms of a fluid other than "
               "the officially rated medium follows: steam W<sub>s</sub> = 51.5 KAP; air "
               "W<sub>a</sub> = CKAP&#8201;√(M/T) with C = 356, M = 28.97, T = 520; any gas "
               "or vapor W = CKAP&#8201;√(M/T). Where the k of hydrocarbon vapors is "
               "unknown, the conservative k = 1.001 (C = 315) is commonly used:"))
    b.append(eq('W = 315 K A P ' + _sq('M/T'), "Appendix 11 — hydrocarbons, k = 1.001"))
    b.append(p("where K is the discharge coefficient per UG-131(d)/(e), A the actual "
               "discharge area (sq in), P = (set × 1.10) + atmospheric (psia). The formulas "
               "also work in reverse — from a required flow to the equivalent steam or air "
               "rating."))
    b.append(p("<b>Example 2.</b> Relieve 5000 lb/hr propane at 125°F inlet, k unknown → "
               "use C = 315: KAP = 5000&#8201;√(44.09/585)/315 = 57.7; equivalent steam "
               "W<sub>s</sub> = 51.5 × 57.7 = <b>2970 lb/hr</b>. <b>Example 3.</b> Relieve "
               "1000 lb/hr ammonia at 150°F with k = 1.33 → C = 350: KAP = 17.10; "
               "W<sub>s</sub> = 51.5 × 17.10 = <b>880 lb/hr steam</b>. <b>Example 4.</b> A "
               "valve rated 10,000 cu ft/min air (60°F, 14.7 psia) = 45,960 lb/hr; KAP = "
               "546; W<sub>s</sub> = 51.5 × 546 = <b>28,200 lb/hr steam</b> at the same "
               "setting (UG-131(b) must be met before converting to steam)."))
    b.append(_t_ctable("en"))
    b.append(fig(3, F.fig_f82()))
    b.append(_t_mw("en"))
    b.append(p("<b>11-2 — Saturated water.</b> Because saturated-water capacity is "
               "configuration sensitive, the rating applies only to <b>nozzle-type</b> "
               "valves (throat-to-inlet ratio 0.25–0.80 with continuously contoured change, "
               "K<sub>D</sub> above 0.90). Reading method: enter the chart at the valve set "
               "pressure, move vertically to the saturated water line, and read horizontally "
               "the relieving capacity — a theoretical isentropic value assuming equilibrium "
               "flow and calculated critical pressure ratio. If after initial relief the "
               "medium becomes quality steam, the valve is rated on dry saturated steam; "
               "valves on steam–water mixture service are rated on dry saturated steam."))
    b.append(fig(4, F.fig_f83()))

    b.append(h2("ASME Appendix M — Installation and operation", "ASME Phụ lục M — Lắp đặt và vận hành"))
    b.append(p("<b>M-1.</b> These rules are general information only: installation and "
               "operation are the responsibility of the jurisdictions enforcing Section "
               "VIII. <b>M-2.</b> Vessels subject to external corrosion get inspection "
               "access; manholes and cover plates stay accessible; the dished bottom head of "
               "vertical cylindrical vessels is preferably concave to pressure for complete "
               "drainage. <b>M-3.</b> Vessel markings remain accessible after installation, "
               "not covered by insulation. <b>M-4.</b> Device installation is fully covered "
               "by UG-135; the paragraphs below detail stop valves and piping."))
    b.append(p("<b>M-5 — Inlet stop valves:</b> for inspection and repair only, arranged to "
               "be locked or sealed open, closed only by an authorized person who remains "
               "stationed there while it stays closed and re-locks it open before leaving. "
               "A vessel fed exclusively from an outside source may have a per-vessel stop "
               "valve that need not be locked open, provided it also closes that vessel off "
               "from the pressure source. <b>M-6 — Discharge-side stop valves:</b> "
               "permitted where the discharge joins a common header so closing prevents "
               "backflow from operating vessels; locked or sealed in either position only "
               "by an authorized person; when closed in operation, an authorized person "
               "remains present and the inlet stop valve is closed first."))
    b.append(p("<b>M-7 — Inlet pressure drop:</b> piping, valves, fittings and vessel "
               "components up to the valve are at least the device inlet size; the "
               "cumulative non-recoverable inlet loss must not exceed <b>3%</b> of set "
               "pressure, based on nameplate capacity corrected for the fluid. Multiple "
               "valves on one connection: inlet area ≥ combined areas, verified with all "
               "valves relieving. <b>M-8 — Discharge lines:</b> prefer short pipes or "
               "vertical risers through long-radius elbows blowing to atmosphere, at least "
               "the valve outlet size; telescopic (“broken”) discharge lines with drip pans "
               "are recommended; common headers serving simultaneously-relieving devices "
               "are sized on the total outlet areas with downstream pressure-drop "
               "allowance; static pressure at the discharge flange of a conventional "
               "direct-spring valve must not exceed <b>10%</b> of set pressure at stamped "
               "capacity; provide drainage everywhere. <b>M-9.</b> Nonreclosing relieving "
               "systems are sized so vessel pressure never exceeds allowable overpressure. "
               "<b>M-10.</b> Back-pressure effects of common-header discharge differ per "
               "valve type — consult manufacturer data."))
    b.append(p("<b>M-11 — Pressure differentials:</b> consider start-up/shutdown, upsets, "
               "instrument response, surge from quick-closing valves; toxic, corrosive or "
               "valuable fluids warrant larger differentials. <b>Blowdown</b> is the first "
               "consideration: a valve set at 100 psig with 7% blowdown closes at 93 psig — "
               "operating pressure must stay below that; large spring-valve blowdown cannot "
               "be considered accurate unless verified on the actual installation. "
               "Pilot-operated valves can be set to blowdowns as short as 2%, but the main "
               "valve may lag the pilot; pilot-to-main signal piping must not drop excessive "
               "pressure. Avoid pilot valves in abrasive or dirty service, where coking, "
               "polymerization or corrosion of wetted pilot parts can occur, or where the "
               "lading fluid can freeze or condense. Tightness should be specified to comply "
               "no lower than the normal operating pressure (procedure per ANSI B146.1) and "
               "never treated as permanent. General recommendations:"))
    b.append(_t_m11("en"))
    b.append(p("Small-seat valves need extra maintenance as the differential approaches "
               "these values. <b>M-12.</b> Spring-loaded valves normally install upright "
               "(vertical spindle); other positions are acceptable if the design suits, the "
               "medium will not accumulate at the inlet, and discharge drainage is adequate. "
               "<b>M-13.</b> Reaction thrust and externally applied loads (thermal "
               "expansion, unsupported piping weight) create bending moments — compute them "
               "in installation design. <b>M-14.</b> Fire sizing references: API RP 520 "
               "Part I and API Standard 2000, AAR M-1002, CGA S-1.1/S-1.2/S-1.3, NFPA Codes "
               "30/59/59A, and the Phillips Petroleum fire-test studies. <b>M-15.</b> A "
               "pressure gauge (if provided) spans the set pressure with an upper limit of "
               "not less than 1.25 × device set pressure and not more than 2 × vessel MAWP."))

    b.append(h2("Other information — warranty, ordering, service", "Thông tin khác — bảo hành, đặt hàng, dịch vụ"))
    b.append(p("The handbook closes with commercial content: <b>warranty</b> of 18 months "
               "from shipment or 12 months from installation (whichever is earlier), "
               "excluding corrosion, erosion, normal wear and improper handling; a <b>safety "
               "warning</b> that the product is a safety-related component whose improper "
               "application or the use of non-Crosby parts may cause failure, and that all "
               "installation, maintenance and testing must follow applicable Codes and "
               "Standards; <b>ordering</b> through the Pressure Relief Valve Specification "
               "Sheet — 53 fields covering general data, connections, materials, options "
               "(cap, lever, test gag, test button, back-flow preventer…), input data "
               "(fluid, required capacity, molecular weight, set/operating pressure, "
               "temperatures, back pressure, allowable overpressure, compressibility, "
               "latent heat, k, viscosity) and calculated values (calculated/selected area, "
               "orifice designation); <b>spare parts</b> ordered with nameplate data and "
               "serial number; <b>services</b> — repair centers in Wrentham (MA), England, "
               "Scotland, Singapore, Brazil and India, field service, training and testing. "
               "Crosby earned ISO 9001 in 1992 (the first U.S. pressure-relief-valve "
               "manufacturer to do so), ISO 9002 in England (1991) and Scotland (1992), and "
               "Vd TÜV compliance per AD-Merkblatt A2/TRD-421 for Styles JOS, JBS, JLT and "
               "Series 900 OMNI-TRIM safety valves."))

    b.append(note("Summary: the appendix excerpts ASME Section VIII Division 1 paragraphs "
                  "UG-125–UG-136 — relief-device requirements, the 10/16/21% overpressure "
                  "allowances, capacity certification (K ≤ 0.878), marking and the UV Code "
                  "Symbol, installation — plus Appendix 11 (capacity conversions with "
                  "worked examples, the C table and molecular weights, saturated-water "
                  "rating) and Appendix M (stop valves, ≤ 3% inlet loss, discharge piping, "
                  "recommended differentials, reaction forces, fire sizing, pressure "
                  "gauges)."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 1997 Crosby Valve Inc.; ASME Section VIII Division 1 excerpts © ASME "
               "International.</i>"))
    return "".join(b)
