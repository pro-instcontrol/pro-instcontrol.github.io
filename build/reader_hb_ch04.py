# -*- coding: utf-8 -*-
"""Handbook Chapter 4 — Measurement Accuracy (Ronald H. Dieck).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch04.py
"""
import os

import hbfig
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch04-measurement-accuracy"
TITLE_EN = "Measurement Accuracy"
TITLE_VI = "Độ chính xác của phép đo"
BYLINE = "Ronald H. Dieck · Pratt &amp; Whitney"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-4-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
            % (num, svg, cap))


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


T95 = [(1, "12,706"), (2, "4,303"), (3, "3,182"), (4, "2,776"), (5, "2,571"), (6, "2,447"),
       (7, "2,365"), (8, "2,306"), (9, "2,262"), (10, "2,228"), (11, "2,201"), (12, "2,179"),
       (13, "2,160"), (14, "2,145"), (15, "2,131"), (16, "2,120"), (17, "2,110"), (18, "2,101"),
       (19, "2,093"), (20, "2,086"), (21, "2,080"), (22, "2,074"), (23, "2,069"), (24, "2,064"),
       (25, "2,060"), (26, "2,056"), (27, "2,052"), (28, "2,048"), (29, "2,045"), (30, "2,000")]


def table_t95(lang="vi"):
    head_txt = ("Bậc tự do", "t₉₅") if lang == "vi" else ("Degrees of freedom", "t95")
    cols = []
    # three blocks of ten rows, like the printed table
    for start in (0, 10, 20):
        rows = []
        for v, t in T95[start:start + 10]:
            lab = ("≥30" if v == 30 else str(v))
            rows.append("<tr><td>%s</td><td>%s</td></tr>" % (lab, t))
        cols.append('<div class="table-wrap" style="flex:1"><table class="tbl"><thead><tr>'
                    '<th>%s</th><th>%s</th></tr></thead><tbody>%s</tbody></table></div>'
                    % (head_txt[0], head_txt[1], "".join(rows)))
    cap = ("Bảng 4-1 · Giá trị thống kê t của Student ở độ tin cậy 95 %, ký hiệu t₉₅,ᵥ theo bậc tự do v. "
           "Với v ≥ 30 dùng t₉₅ = 2,000." if lang == "vi" else
           "Table 4.1 · Student’s t at 95 % confidence, written t95,v, for v degrees of freedom. "
           "For v ≥ 30 use t95 = 2.000.")
    return ('<div style="display:flex;gap:14px;flex-wrap:wrap">%s</div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>' % ("".join(cols), cap))


def table_data(lang="vi"):
    if lang == "vi":
        hd = ("Quá trình đo đã xác định", "Độ không đảm bảo hệ thống Bᵢ", "bậc tự do của Bᵢ",
              "Độ lệch chuẩn S̄<sub>X,i</sub>", "Số điểm dữ liệu Nᵢ",
              "Độ không đảm bảo ngẫu nhiên S̄<sub>X,i</sub>", "bậc tự do νᵢ")
        rows = [("Hiệu chuẩn cặp nhiệt điện (tc)", "0,06<sup>B</sup>", "∞", "0,3<sup>A</sup>", "10", "0,095<sup>A</sup>", "9"),
                ("Mối nối so sánh (reference junction)", "0,07<sup>A</sup>", "12", "0,1<sup>A</sup>", "5", "0,045<sup>A</sup>", "4"),
                ("Thu thập dữ liệu", "0,10<sup>B</sup>", "∞", "0,6<sup>A</sup>", "12", "0,173<sup>A</sup>", "11")]
        cap = ("Bảng 4-2 · Độ không đảm bảo của một phép đo nhiệt độ, đơn vị °F. Chỉ số A nghĩa là có dữ liệu "
               "để tính độ lệch chuẩn; chỉ số B nghĩa là không có dữ liệu, phải ước lượng.")
    else:
        hd = ("Defined measurement process", "Systematic uncertainty, Bi", "d.f. for Bi",
              "Standard deviation, S̄<sub>X,i</sub>", "Number of data points, Ni",
              "Random uncertainty, S̄<sub>X,i</sub>", "Degrees of freedom, νi")
        rows = [("Calibration of tc", "0.06<sup>B</sup>", "∞", "0.3<sup>A</sup>", "10", "0.095<sup>A</sup>", "9"),
                ("Reference junction", "0.07<sup>A</sup>", "12", "0.1<sup>A</sup>", "5", "0.045<sup>A</sup>", "4"),
                ("Data acquisition", "0.10<sup>B</sup>", "∞", "0.6<sup>A</sup>", "12", "0.173<sup>A</sup>", "11")]
        cap = ("Table 4.2 · Temperature measurement uncertainties, °F. The superscript A means data exist to "
               "calculate a standard deviation; B means there are none and it must be estimated.")
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table class="tbl"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % ("".join("<th>%s</th>" % h for h in hd), body, cap))


# ------------------------------------------------------------------ VI body
def body_vi():
    b = []
    b.append('<div class="note"><b>Thuật ngữ chính.</b> '
             '<em>Sai số (error)</em> · <em>Độ không đảm bảo đo (measurement uncertainty)</em> · '
             '<em>Độ tin cậy (confidence)</em> · <em>Độ lệch chuẩn của trị trung bình</em> · '
             '<em>Bậc tự do (degrees of freedom)</em> · <em>Hệ số ảnh hưởng / độ nhạy (θᵢ)</em> · '
             '<em>Truyền độ không đảm bảo (propagation)</em> · <em>Loại A / loại B (ISO)</em> · '
             '<em>Ngẫu nhiên / hệ thống (random / systematic)</em> · '
             '<em>Hiệp phương sai (covariance)</em> · <em>Welch–Satterthwaite</em>. '
             'Tiêu đề mỗi mục giữ kèm tên tiếng Anh để đối chiếu với bản gốc.</div>')

    b.append('<p class="lead">Chương này là phần tính toán của phép đo: từ một tập dữ liệu, làm sao nói được '
             '“kết quả là 45,2 °F ± 0,45 °F ở độ tin cậy 95 %” và nói đúng. Nó trình bày phân bố chuẩn và phân bố '
             'đều, mô hình độ không đảm bảo đo với hai cách phân loại (ISO loại A/B và phân loại kỹ thuật ngẫu '
             'nhiên/hệ thống), công thức tổng hợp bình phương, xấp xỉ Welch–Satterthwaite cho bậc tự do, và một ví dụ '
             'tính đầy đủ cho thấy hai mô hình cho cùng một kết quả.</p>')

    b.append(p("Tất cả các phép đo thử nghiệm được thực hiện để thu dữ liệu hữu ích cho việc ra quyết định. Không ai "
               "chạy thử nghiệm hay đo đạc khi đã biết “đáp án”. Để dữ liệu hữu ích, sai số đo của chúng phải nhỏ so "
               "với thay đổi hay hiệu ứng đang được đánh giá. Sai số đo là không biết và không thể biết. Chương này "
               "trình bày các kỹ thuật dùng để ước lượng, với một mức tin cậy nào đó, các giới hạn mong đợi của sai "
               "số đo."))

    # ---------------------------------------------------------------- 4.1
    b.append(h2("4.1 Sai số: phân bố chuẩn và phân bố đều",
                "Error: The Normal Distribution and the Uniform Distribution"))
    b.append(p("<b>Sai số</b> được định nghĩa là hiệu giữa giá trị đo được và giá trị thật của đại lượng đo [1]. "
               "Nghĩa là:"))
    b.append(eq("E = (giá trị đo) − (giá trị thật)", "4.1"))
    b.append(p("trong đó <i>E</i> là sai số đo, (giá trị đo) là giá trị nhận được từ một phép đo, và (giá trị thật) "
               "là giá trị thật của đại lượng đo."))
    b.append(p("Chỉ có thể ước lượng, với một mức tin cậy nào đó, các giới hạn mong đợi của sai số. Phương pháp phổ "
               "biến nhất để ước lượng các giới hạn đó là dùng <b>phân bố chuẩn</b> [2]:"))
    b.append(eq("Y = [1/(σ√(2π))] · e<sup>−(X−µ)²/(2σ²)</sup>", "4.2"))
    b.append(p("trong đó <i>X</i> là biến vào, ở đây là giá trị nhận được từ một phép đo; µ là trung bình của tổng "
               "thể biến <i>X</i>; và σ là độ lệch chuẩn của tổng thể, biểu diễn bằng:"))
    b.append(eq("σ = √[ Σ<sub>i=1..n</sub> (X<sub>i</sub> − µ)² / n ]", "4.3"))
    b.append(p("trong đó X<sub>i</sub> là phép đo <i>X</i> thứ <i>i</i>, và <i>n</i> là số điểm dữ liệu đo được từ "
               "tổng thể. Thông thường cả <i>n</i>, µ lẫn σ đều không biết."))
    b.append(p("Hình 4-1 minh hoạ phân bố này. Ở đây, với một tổng thể vô hạn (<i>N</i> = ∞), độ lệch chuẩn σ được "
               "dùng để ước lượng các giới hạn mong đợi của một sai số cụ thể với một mức tin cậy nào đó. Nghĩa là "
               "trung bình, cộng trừ 2σ chia cho căn bậc hai của số điểm dữ liệu, sẽ chứa trung bình thật µ trong "
               "95 % số lần."))
    b.append(fig(1, hbfig.fig_4_1()))
    b.append(p("Tuy nhiên, trong phép đo thử nghiệm người ta thường không thể lấy mẫu toàn bộ tổng thể mà phải dùng "
               "một mẫu gồm <i>N</i> điểm dữ liệu. Khi đó <b>độ lệch chuẩn mẫu</b> S<sub>X</sub> được dùng để ước "
               "lượng σ<sub>X</sub>, tức các giới hạn mong đợi của một sai số cụ thể. (Độ lệch chuẩn mẫu chia cho "
               "căn bậc hai của số điểm dữ liệu là điểm khởi đầu cho ước lượng khoảng tin cậy của µ.) Với một tập dữ "
               "liệu lớn (được định nghĩa là có 30 bậc tự do trở lên), trung bình cộng trừ 2S<sub>X</sub> chia cho "
               "căn bậc hai của số điểm dữ liệu trong trị trung bình được báo cáo <i>M</i> sẽ chứa trung bình thật µ "
               "trong 95 % số lần."))
    b.append(p("Đại lượng S<sub>X</sub> chia cho căn bậc hai của số điểm dữ liệu trong trị trung bình được báo cáo "
               "được gọi là <b>độ lệch chuẩn của trị trung bình</b> và được viết là:"))
    b.append(eq("S̄<sub>X</sub> = S<sub>X</sub> / √M", "4.4"))
    b.append(p("trong đó S̄<sub>X</sub> là độ lệch chuẩn của trị trung bình — độ lệch chuẩn mẫu của dữ liệu chia cho "
               "căn bậc hai của <i>M</i>; S<sub>X</sub> là độ lệch chuẩn mẫu; và X̄ là trung bình mẫu, tức:"))
    b.append(eq("X̄ = (1/M) · Σ<sub>i=1..M</sub> X<sub>i</sub>", "4.5"))
    b.append(p("với X<sub>i</sub> là điểm dữ liệu thứ <i>i</i> dùng để tính độ lệch chuẩn mẫu và trung bình X̄ từ dữ "
               "liệu; <i>N</i> là số điểm dữ liệu dùng để tính độ lệch chuẩn; (<i>N</i> − 1) là bậc tự do của "
               "S<sub>X</sub> và S̄<sub>X</sub>; và <i>M</i> là số điểm dữ liệu trong kết quả thử trung bình được báo "
               "cáo."))
    b.append(p("Lưu ý trong phương trình 4.4 rằng <i>N</i> không nhất thiết bằng <i>M</i>. Có thể lấy S<sub>X</sub> "
               "từ dữ liệu lịch sử với nhiều bậc tự do ([<i>N</i> − 1] lớn hơn 30) và chỉ chạy thử <i>M</i> lần. Kết "
               "quả thử, hay trị trung bình, khi đó dựa trên <i>M</i> phép đo, và độ lệch chuẩn của trị trung bình "
               "vẫn được tính bằng phương trình 4.4. Trong trường hợp đó sẽ có hai trị trung bình X̄: một từ dữ liệu "
               "lịch sử dùng để tính độ lệch chuẩn mẫu, và một là kết quả thử trung bình cho <i>M</i> phép đo."))
    b.append(p("Lưu ý độ lệch chuẩn mẫu S<sub>X</sub> đơn giản là:"))
    b.append(eq("S<sub>X</sub> = √[ Σ<sub>i=1..N</sub> (X<sub>i</sub> − X̄)² / (N − 1) ]", "4.6"))
    b.append(p("Trong một số trường hợp, phân bố sai số cụ thể có thể được giả định hoặc đã biết là <b>phân bố đều</b> "
               "hay <b>phân bố chữ nhật</b>, Hình 4-2, thay vì phân bố chuẩn. Với những trường hợp đó, độ lệch chuẩn "
               "mẫu của dữ liệu được tính là:"))
    b.append(eq("S<sub>X</sub> = L / √3", "4.7"))
    b.append(p("trong đó <i>L</i> là các giới hạn cộng/trừ của phân bố đều cho một sai số cụ thể [3]. Với những "
               "trường hợp đó, độ lệch chuẩn của trị trung bình được viết là:"))
    b.append(eq("S̄<sub>X</sub> = L / (√3 · √M)", "4.8"))
    b.append(fig(2, hbfig.fig_4_2()))
    b.append(p("Dù việc tính độ lệch chuẩn mẫu (hoặc ước lượng nó bằng một quá trình khác) là cần thiết cho phân tích "
               "độ không đảm bảo đo, toàn bộ công việc phân tích tính độ không đảm bảo đo chỉ dùng <b>độ lệch chuẩn "
               "của trị trung bình</b> cho từng nguồn sai số."))

    b.append(h3("Độ không đảm bảo (độ chính xác)", "Uncertainty (Accuracy)"))
    b.append(p("Vì sai số của bất kỳ nguồn sai số cụ thể nào là không biết và không thể biết, phải ước lượng các giới "
               "hạn của nó ở một độ tin cậy cho trước. Ước lượng này được gọi là <b>độ không đảm bảo</b> "
               "(uncertainty). Đôi khi thuật ngữ <em>độ chính xác</em> (accuracy) được dùng để mô tả chất lượng của "
               "dữ liệu thử. Đó là cách phát biểu khẳng định về các giới hạn mong đợi của sai số dữ liệu. Độ không "
               "đảm bảo là cách phát biểu phủ định. Tuy vậy độ không đảm bảo là rõ ràng, không mơ hồ. Độ chính xác "
               "đôi khi lại mơ hồ. (Ví dụ: “gấp đôi độ chính xác ±2 %” là ±1 % hay ±4 %?) Vì lý do này, chương này "
               "dùng thuật ngữ độ không đảm bảo xuyên suốt để mô tả chất lượng của dữ liệu thử."))

    # ---------------------------------------------------------------- 4.2
    b.append(h2("4.2 Mô hình độ không đảm bảo đo", "Measurement Uncertainty Model"))
    b.append(h3("Mục đích", "Purpose"))
    b.append(p("Cần một ước lượng độ không đảm bảo của kết quả thử để ra quyết định có căn cứ. Lý tưởng, độ không "
               "đảm bảo của một thí nghiệm được tiến hành tốt sẽ nhỏ hơn nhiều so với thay đổi hay kết quả thử mong "
               "đợi. Như vậy sẽ biết, với độ tin cậy cao, rằng thay đổi hay kết quả quan sát được là thật hoặc chấp "
               "nhận được, chứ không phải kết quả của sai số trong quá trình thử hay đo. Các giới hạn của những sai "
               "số đó được ước lượng bằng độ không đảm bảo, và các nguồn sai số cùng bộ ước lượng giới hạn của chúng "
               "— tức các độ không đảm bảo — có thể được nhóm thành các phân loại để dễ hiểu."))

    b.append(h3("Phân loại nguồn sai số và độ không đảm bảo",
                "Classifying Error and Uncertainty Sources"))
    b.append(p("Có hai hệ phân loại đang được dùng. Tổng độ không đảm bảo cuối cùng tính ở một độ tin cậy là như nhau "
               "dù dùng hệ phân loại nào. Hai cách phân loại được dùng là <b>phân loại ISO</b> và <b>phân loại kỹ "
               "thuật</b>. Cách thứ nhất nhóm sai số và độ không đảm bảo của chúng theo kiểu, tuỳ thuộc có hay không "
               "có dữ liệu để tính độ lệch chuẩn mẫu cho một sai số cụ thể và độ không đảm bảo của nó. Cách thứ hai "
               "nhóm sai số và độ không đảm bảo theo tác động của chúng lên thí nghiệm hay phép thử. Nghĩa là phân "
               "loại kỹ thuật nhóm sai số và độ không đảm bảo theo kiểu ngẫu nhiên và hệ thống, với chỉ số dưới dùng "
               "để cho biết có dữ liệu để tính độ lệch chuẩn hay không cho một nguồn sai số hoặc độ không đảm bảo cụ "
               "thể. Vì lý do này, các nhóm của phân loại kỹ thuật thường hữu ích hơn và được khuyến nghị."))

    b.append(h3("Phân loại ISO", "ISO Classifications"))
    b.append(p("Hệ phân loại sai số và độ không đảm bảo này không được khuyến nghị trong chương này, nhưng sẽ cho một "
               "tổng độ không đảm bảo hoàn toàn phù hợp với hệ phân loại được khuyến nghị — phân loại kỹ thuật. "
               "Trong hệ ISO, sai số và độ không đảm bảo được phân thành <b>loại A</b> nếu có dữ liệu để tính độ lệch "
               "chuẩn mẫu và <b>loại B</b> nếu không [4]. Trong trường hợp sau, độ lệch chuẩn mẫu có thể lấy từ kinh "
               "nghiệm hoặc từ thông số kỹ thuật của nhà sản xuất, là hai ví dụ."))
    b.append(p("Tác động của nhiều nguồn sai số được ước lượng bằng cách lấy căn bậc hai của tổng bình phương "
               "(root-sum-square) các độ không đảm bảo tương ứng. Các phương trình làm việc là:"))
    b.append(p("<b>Loại A</b>, có dữ liệu để tính độ lệch chuẩn:"))
    b.append(eq("U<sub>A</sub> = [ Σ<sub>i=1..N<sub>A</sub></sub> (θ<sub>i</sub> · U<sub>Ai</sub>)² ]<sup>1/2</sup>",
                "4.9"))
    b.append(p("trong đó U<sub>Ai</sub> là độ lệch chuẩn (dựa trên dữ liệu) của trị trung bình cho nguồn độ không đảm "
               "bảo loại A thứ <i>i</i>, mỗi nguồn có bậc tự do riêng. U<sub>A</sub> có đơn vị của kết quả thử hay "
               "phép đo; nó chính là một S̄<sub>X</sub>. N<sub>A</sub> là số tham số có độ không đảm bảo loại A. "
               "θ<sub>i</sub> là <b>độ nhạy</b> của kết quả thử hay phép đo <i>R</i> đối với độ không đảm bảo loại A "
               "thứ <i>i</i>: θ<sub>i</sub> là đạo hàm riêng của kết quả theo từng phép đo độc lập thứ <i>i</i>."))
    b.append(p("Độ không đảm bảo của mỗi nguồn sai số, khi tính theo đơn vị của nguồn đó, được nhân với độ nhạy của "
               "nguồn để chuyển thành đơn vị của kết quả. Khi đó tác động của nhiều nguồn sai số có thể được ước "
               "lượng bằng cách lấy căn bậc hai tổng bình phương các độ không đảm bảo, vì nay chúng cùng đơn vị. Các "
               "độ nhạy θ<sub>i</sub> nhận được cho một kết quả đo <i>R</i> là hàm của nhiều tham số P<sub>i</sub>. "
               "Các phương trình cơ bản là <i>R</i> = f(P<sub>1</sub>, P<sub>2</sub>, P<sub>3</sub> … P<sub>N</sub>) "
               "và θ<sub>i</sub> = ∂R/∂P<sub>i</sub>. Việc xác định các θ<sub>i</sub> thường được gọi là <b>truyền "
               "sai số</b> hay <b>truyền độ không đảm bảo</b> (error / uncertainty propagation)."))
    b.append(p("<b>Loại B</b> (không có dữ liệu để tính độ lệch chuẩn):"))
    b.append(eq("U<sub>B</sub> = [ Σ<sub>i=1..N<sub>B</sub></sub> (θ<sub>i</sub> · U<sub>Bi</sub>)² ]<sup>1/2</sup>",
                "4.10"))
    b.append(p("trong đó U<sub>Bi</sub> là độ lệch chuẩn (dựa trên ước lượng, không dựa trên dữ liệu) của trị trung "
               "bình cho nguồn độ không đảm bảo loại B thứ <i>i</i>; U<sub>B</sub> có đơn vị của kết quả thử hay phép "
               "đo <i>R</i> và là một S̄<sub>X</sub>; N<sub>B</sub> là số tham số có độ không đảm bảo loại B; "
               "θ<sub>i</sub> là độ nhạy của kết quả thử hay phép đo đối với độ không đảm bảo loại B thứ <i>i</i>."))
    b.append(p("Với các độ không đảm bảo này, giả định rằng U<sub>Bi</sub> biểu diễn một độ lệch chuẩn của trị trung "
               "bình cho một nguồn độ không đảm bảo với phân bố chuẩn được giả định. (Chúng cũng biểu diễn một độ "
               "lệch chuẩn vì căn bậc hai của “<i>M</i>” mà chúng được chia cho bằng một, tức chỉ có một sai số loại "
               "B được lấy mẫu từ mỗi phân bố này.) Bậc tự do gắn với độ lệch chuẩn này (cũng là độ lệch chuẩn của "
               "trị trung bình) là vô cùng."))
    b.append(p("Lưu ý θ<sub>i</sub>, độ nhạy của kết quả thử hay phép đo đối với độ không đảm bảo loại B thứ <i>i</i>, "
               "thực chất là thay đổi của kết quả <i>R</i> khi tham số vào thứ <i>i</i> dùng để tính kết quả đó thay "
               "đổi một lượng bằng độ không đảm bảo loại B."))
    b.append(p("Bậc tự do của U<sub>A</sub> và của U<sub>Bi</sub> là cần thiết để tính bậc tự do của tổng độ không "
               "đảm bảo tổng hợp. Nó được tính bằng <b>xấp xỉ Welch–Satterthwaite</b>. Công thức tổng quát cho bậc "
               "tự do [5] là:"))
    b.append(eq("df<sub>R</sub> = ν<sub>R</sub> = [ Σ (S̄<sub>i</sub>)² ]² / [ Σ (S̄<sub>i</sub>)⁴ / ν<sub>i</sub> ]",
                "4.11"))
    b.append(p("trong đó df<sub>R</sub> = ν<sub>R</sub> là bậc tự do của kết quả, và ν<sub>i</sub> là bậc tự do của độ "
               "lệch chuẩn của trị trung bình thứ <i>i</i>. Với mô hình ISO, phương trình 4.11 trở thành:"))
    b.append(eq("df<sub>R,ISO</sub> = [ (U<sub>A</sub>)² + (U<sub>B</sub>)² ]² / "
                "[ Σ<sub>A</sub> (θ<sub>i</sub>U<sub>i</sub>)⁴/ν<sub>i</sub> + "
                "Σ<sub>B</sub> (θ<sub>i</sub>U<sub>i</sub>)⁴/ν<sub>i</sub> ]", "4.12"))
    b.append(p("Bậc tự do tính bằng phương trình 4.12 thường là một phân số. Nên cắt xuống số nguyên thấp hơn kế tiếp "
               "để bảo thủ. Lưu ý trong các phương trình 4.9, 4.10 và 4.12, N<sub>A</sub> và N<sub>B</sub> không nhất "
               "thiết bằng nhau; chúng chỉ là tổng số tham số có nguồn độ không đảm bảo loại A và loại B tương ứng."))
    b.append(p("Khi tính tổng độ không đảm bảo, các độ không đảm bảo ở phương trình 4.10 và 4.11 được kết hợp. Với mô "
               "hình ISO [3], việc này được tính là:"))
    b.append(eq("U<sub>R,ISO</sub> = ± t<sub>95</sub> [ (U<sub>A</sub>)² + (U<sub>B</sub>)² ]<sup>1/2</sup>", "4.13"))
    b.append(p("trong đó t<sub>95</sub> là thống kê t của Student ứng với ν<sub>R</sub> bậc tự do, lấy từ Bảng 4-1."))
    b.append(table_t95("vi"))
    b.append(p("Lưu ý các độ tin cậy khác cũng được phép. 95 % được ASME khuyến nghị [6], nhưng 99 %, 99,7 % hay bất "
               "kỳ độ tin cậy nào khác có được bằng cách chọn thống kê t của Student thích hợp. Tuy vậy 95 % là độ "
               "tin cậy được khuyến nghị cho phân tích độ không đảm bảo."))
    b.append(p("Trong tất cả các phần trên, sai số được giả định là <b>độc lập</b>. Các nguồn sai số độc lập là những "
               "nguồn không có quan hệ với nhau. Nghĩa là không thể dùng sai số trong một phép đo từ một nguồn để dự "
               "đoán độ lớn hay chiều của sai số từ nguồn sai số độc lập kia. Các nguồn sai số không độc lập có quan "
               "hệ với nhau: nếu biết được sai số trong một phép đo từ một nguồn, có thể tính hay dự đoán độ lớn và "
               "chiều của sai số từ nguồn không độc lập kia. Chúng đôi khi được gọi là các nguồn sai số phụ thuộc. "
               "Mức độ phụ thuộc của chúng có thể được ước lượng bằng hệ số tương quan tuyến tính. Nếu chúng không "
               "độc lập, dù là loại A hay loại B, phương trình 4.13 trở thành [7]:"))
    b.append(eq("U<sub>R,ISO</sub> = ± t<sub>95</sub> { Σ<sub>T</sub> [ Σ<sub>i</sub> (θ<sub>i</sub>U<sub>i,T</sub>)² "
                "+ 2 Σ<sub>i</sub>Σ<sub>j&gt;i</sub> θ<sub>i</sub>θ<sub>j</sub>U<sub>(i,T),(j,T)</sub> ] }"
                "<sup>1/2</sup>", "4.14"))
    b.append(p("trong đó U<sub>i,T</sub> là độ không đảm bảo thành phần thứ <i>i</i> loại T (có thể là loại A hoặc B); "
               "U<sub>R,ISO</sub> là tổng độ không đảm bảo của kết quả đo hay thử; θ<sub>i</sub> và θ<sub>j</sub> là độ "
               "nhạy của kết quả đối với độ không đảm bảo loại T thứ <i>i</i> và thứ <i>j</i>; và "
               "U<sub>(i,T),(j,T)</sub> là hiệp phương sai của U<sub>i,T</sub> với U<sub>j,T</sub>:"))
    b.append(eq("U<sub>(i,T),(j,T)</sub> = Σ<sub>l=1..K</sub> U<sub>(l,T)</sub>(i) · U<sub>(l,T)</sub>(j)", "4.15"))
    b.append(p("tức tổng các tích của những độ không đảm bảo hệ thống thành phần phát sinh từ một nguồn chung (l); "
               "<i>l</i> là chỉ số hay bộ đếm cho các nguồn không đảm bảo chung; <i>K</i> là số cặp độ không đảm bảo "
               "có nguồn chung; δ<sub>i,j</sub> là delta Kronecker, δ<sub>i,j</sub> = 1 nếu <i>i</i> = <i>j</i> và "
               "bằng 0 nếu không [7]; và T là chỉ số hay bộ đếm cho kiểu độ không đảm bảo ISO, A hoặc B."))
    b.append(p("Phương trình phân loại ISO này sẽ cho cùng tổng độ không đảm bảo như phân loại kỹ thuật, nhưng phân "
               "loại ISO không cho hiểu biết về cách cải thiện độ không đảm bảo của một thí nghiệm hay phép thử. "
               "Nghĩa là không cho biết nên lấy thêm dữ liệu vì độ không đảm bảo ngẫu nhiên quá cao, hay nên hiệu "
               "chuẩn tốt hơn vì độ không đảm bảo hệ thống quá lớn. Vì vậy phân loại kỹ thuật trình bày dưới đây là "
               "cách tiếp cận được ưa dùng."))

    b.append(h3("Phân loại kỹ thuật", "Engineering Classification"))
    b.append(p("Phân loại kỹ thuật nhận rằng thí nghiệm và phép thử có hai kiểu sai số chính, với các giới hạn được "
               "ước lượng bằng độ không đảm bảo ở một độ tin cậy đã chọn. Các kiểu sai số này có thể được nhóm thành "
               "<b>ngẫu nhiên</b> và <b>hệ thống</b>. Bộ ước lượng giới hạn tương ứng là <b>độ không đảm bảo ngẫu "
               "nhiên</b> và <b>độ không đảm bảo hệ thống</b>."))
    b.append(h3("Ngẫu nhiên", "Random"))
    b.append(p("Biểu thức tổng quát cho độ không đảm bảo ngẫu nhiên là độ lệch chuẩn của trị trung bình "
               "(1S̄<sub>X</sub>) [6]:"))
    b.append(eq("S̄<sub>X,R</sub> = { Σ<sub>T</sub> Σ<sub>i</sub> [ θ<sub>i</sub> · S<sub>Xi,T</sub> / "
                "√M<sub>i,T</sub> ]² }<sup>1/2</sup>", "4.16"))
    b.append(p("trong đó S<sub>Xi,T</sub> là độ lệch chuẩn mẫu của nguồn sai số ngẫu nhiên thứ <i>i</i> loại T; "
               "S̄<sub>Xi,T</sub> là độ không đảm bảo ngẫu nhiên (độ lệch chuẩn của trị trung bình) của nguồn sai số "
               "ngẫu nhiên tham số thứ <i>i</i> loại T; S̄<sub>X,R</sub> là độ không đảm bảo ngẫu nhiên của kết quả đo "
               "hay thử; N<sub>i,T</sub> là tổng số độ không đảm bảo ngẫu nhiên, loại A và B, gộp lại; "
               "M<sub>i,T</sub> là số điểm dữ liệu được lấy trung bình cho nguồn sai số thứ <i>i</i>, loại A hoặc B; "
               "và θ<sub>i</sub> là độ nhạy của kết quả thử hay phép đo đối với độ không đảm bảo ngẫu nhiên thứ "
               "<i>i</i>."))
    b.append(p("Lưu ý S̄<sub>X,R</sub> có đơn vị của kết quả thử hay phép đo nhờ dùng các độ nhạy θ<sub>i</sub>. Ở đây "
               "các độ không đảm bảo ngẫu nhiên thành phần đã được lấy căn bậc hai tổng bình phương với sự xét đến "
               "độ nhạy, hay hệ số ảnh hưởng, của chúng. Vì tất cả đều là độ không đảm bảo ngẫu nhiên, theo định "
               "nghĩa không có tương quan trong dữ liệu sai số tương ứng, nên chúng luôn có thể được xử lý như các "
               "nguồn độ không đảm bảo độc lập."))
    b.append(h3("Hệ thống", "Systematic"))
    b.append(p("Độ không đảm bảo hệ thống của kết quả, B<sub>R</sub>, là căn bậc hai tổng bình phương của các độ "
               "không đảm bảo hệ thống thành phần, có xét đến những độ không đảm bảo tương quan [7]. Phương trình "
               "tổng quát là:"))
    b.append(eq("B<sub>R</sub> = { Σ<sub>T</sub> [ Σ<sub>i</sub> (θ<sub>i</sub>B<sub>i,T</sub>)² + "
                "2 Σ<sub>i</sub>Σ<sub>j&gt;i</sub> θ<sub>i</sub>θ<sub>j</sub>B<sub>(i,T),(j,T)</sub> ] }"
                "<sup>1/2</sup>", "4.17"))
    b.append(p("trong đó B<sub>i,T</sub> là độ không đảm bảo hệ thống thành phần của tham số thứ <i>i</i> loại T; "
               "B<sub>R</sub> là độ không đảm bảo hệ thống của kết quả đo hay thử; <i>N</i> là tổng số độ không đảm "
               "bảo hệ thống; θ<sub>i</sub>, θ<sub>j</sub> là độ nhạy của kết quả đối với độ không đảm bảo hệ thống "
               "thứ <i>i</i> và thứ <i>j</i>; và B<sub>(i,T),(j,T)</sub> là hiệp phương sai của B<sub>i</sub> với "
               "B<sub>j</sub>:"))
    b.append(eq("B<sub>(i,T),(j,T)</sub> = Σ<sub>l=1..K</sub> B<sub>(l,T)</sub>(i) · B<sub>(l,T)</sub>(j)", "4.18"))
    b.append(p("tức tổng các tích của những độ không đảm bảo hệ thống thành phần phát sinh từ một nguồn chung (l); "
               "<i>l</i> là chỉ số cho các nguồn không đảm bảo chung; δ<sub>i,j</sub> là delta Kronecker; và T là chỉ "
               "số cho kiểu độ không đảm bảo ISO, A hoặc B. Ở đây mỗi B<sub>i,T</sub> và B<sub>j,T</sub> được ước "
               "lượng là 2S<sub>X</sub> với giả định phân bố chuẩn của sai số ở độ tin cậy 95 % và bậc tự do vô cùng "
               "[6]."))
    b.append(p("Độ không đảm bảo ngẫu nhiên, phương trình 4.16, và độ không đảm bảo hệ thống, phương trình 4.17, phải "
               "được kết hợp để có tổng độ không đảm bảo:"))
    b.append(eq("U<sub>R,ENG</sub> = ± t<sub>95</sub> [ (B<sub>R</sub>)² + (S̄<sub>X,R</sub>)² ]<sup>1/2</sup>", "4.19"))
    b.append(p("Lưu ý B<sub>R</sub> có đơn vị của kết quả thử hay phép đo, cũng như S̄<sub>X,Ri</sub>. Bậc tự do sẽ "
               "cần cho tổng độ không đảm bảo của hệ kỹ thuật. Việc này được thực hiện bằng xấp xỉ "
               "Welch–Satterthwaite, dạng tổng quát là phương trình 4.10, và công thức cụ thể ở đây là:"))
    b.append(eq("ν<sub>R,ENG</sub> = [ (B<sub>R</sub>)² + (S̄<sub>X,R</sub>)² ]² / "
                "{ Σ<sub>T</sub> Σ<sub>i</sub> [ (θ<sub>i</sub>S̄<sub>Xi,T</sub>)² + (θ<sub>i</sub>B<sub>i,T</sub>)² ]² "
                "/ ν<sub>i,T</sub> }", "4.20"))
    b.append(p("trong đó NS̄<sub>Xi,T</sub> là số độ không đảm bảo ngẫu nhiên loại T; NB<sub>i,T</sub> là số độ không "
               "đảm bảo hệ thống loại T; ν<sub>i,T</sub> là bậc tự do của độ không đảm bảo thứ <i>i</i> loại T, và "
               "ν<sub>i,T</sub> = ∞ với mọi độ không đảm bảo hệ thống; <i>t</i> là thống kê t của Student ứng với bậc "
               "tự do của từng B<sub>i</sub>."))

    b.append(h3("Độ không đảm bảo hệ thống đối xứng", "Symmetrical Systematic Uncertainties"))
    b.append(p("Phần lớn các trường hợp, mọi độ không đảm bảo thành phần đều đối xứng. Nghĩa là các giới hạn ± của "
               "chúng quanh trị trung bình đo được là như nhau: ±3 °C hay ±2,05 kPa và tương tự, chứ không phải "
               "+2,0 °C/−1,0 °C hay +1,5 kPa/−0,55 kPa. Vì vậy độ không đảm bảo đo đối xứng có thể được tính như "
               "trên. (Với cách xử lý trang nhã cho độ không đảm bảo không đối xứng, xem mục đó trong Tài liệu tham "
               "khảo [6].)"))
    b.append(p("Lưu ý trong toàn bộ các phép tính độ không đảm bảo này, mọi độ không đảm bảo được biểu diễn theo đơn "
               "vị kỹ thuật. Tất cả các phương trình cũng làm việc với đơn vị tương đối; cách đó cũng có thể thấy "
               "trong [6]. Tuy nhiên thường dễ hơn là biểu diễn mọi độ không đảm bảo và các phép tính ước lượng theo "
               "đơn vị kỹ thuật, rồi cuối cùng, với tổng độ không đảm bảo, chuyển kết quả sang dạng tương đối. Đó là "
               "điều mục này khuyến nghị."))

    # ---------------------------------------------------------------- 4.3
    b.append(h2("4.3 Tính tổng độ không đảm bảo", "Calculation of Total Uncertainty"))
    b.append(h3("Tổng độ không đảm bảo (mở rộng) theo ISO", "ISO Total (Expanded) Uncertainty"))
    b.append(p("Tổng độ không đảm bảo theo ISO cho các nguồn độ không đảm bảo độc lập (trường hợp phổ biến nhất) là "
               "phương trình 4.13:"))
    b.append(eq("U<sub>R,ISO</sub> = ± t<sub>95</sub> [ (U<sub>A</sub>)² + (U<sub>B</sub>)² ]<sup>1/2</sup>", "4.21"))
    b.append(p("trong đó U<sub>R,ISO</sub> là độ không đảm bảo đo của kết quả; U<sub>A</sub> là độ không đảm bảo loại "
               "A của kết quả; U<sub>B</sub> là độ không đảm bảo loại B của kết quả; và t<sub>95</sub> là hệ số nhân "
               "t<sub>95</sub> của Student, được khuyến nghị để bảo đảm độ tin cậy 95 %. Độ không đảm bảo ISO khi có "
               "một số nguồn không độc lập là phương trình 4.14."))
    b.append(h3("Tổng độ không đảm bảo của hệ kỹ thuật", "Engineering System Total Uncertainty"))
    b.append(p("Phương trình tổng độ không đảm bảo của hệ kỹ thuật cho các nguồn độ không đảm bảo độc lập (phổ biến "
               "nhất) là:"))
    b.append(eq("U<sub>R,ENG</sub> = ± t<sub>95</sub> [ (B<sub>R</sub>)² + (S̄<sub>X,R</sub>)² ]<sup>1/2</sup>", "4.23"))
    b.append(p("Ở đây chỉ cần số hạng thứ nhất của phương trình 4.23 vì mọi nguồn độ không đảm bảo hệ thống đều độc "
               "lập. Phương trình của hệ kỹ thuật cho trường hợp có nguồn không độc lập (có độ không đảm bảo hệ thống "
               "tương quan) cũng là phương trình 4.23, nhưng phải nhớ dùng biểu thức đầy đủ cho B<sub>R</sub>, tức "
               "phương trình 4.17:"))
    b.append(eq("U<sub>R,ENG</sub> = ± t<sub>95</sub> { [ (B<sub>R</sub>)² + (S̄<sub>X,R</sub>)² ] }"
                "<sup>1/2</sup> &nbsp; với B<sub>R</sub> theo (4.17)", "4.24"))
    b.append(p("Bậc tự do cho các phương trình 4.21 đến 4.24 được tính bằng xấp xỉ Welch–Satterthwaite: phương trình "
               "4.12 cho hệ ISO và phương trình 4.20 cho hệ kỹ thuật."))

    b.append(h3("Xấp xỉ bậc tự do cao", "High Degrees of Freedom Approximation"))
    b.append(p("Thường gặp trường hợp giả định bậc tự do là 30 hoặc cao hơn. Khi đó các phương trình độ không đảm bảo "
               "đơn giản hơn nữa bằng cách đặt t<sub>95</sub> bằng 2,000. Cách này được khuyến nghị cho người lần đầu "
               "dùng thủ tục phân tích độ không đảm bảo vì đó là cách nhanh để có một xấp xỉ độ không đảm bảo đo."))

    b.append(h3("Ví dụ tính", "Calculation Example"))
    b.append(p("Ví dụ tính dưới đây lấy trường hợp mọi độ không đảm bảo đều độc lập và đều theo đơn vị của kết quả thử "
               "— nhiệt độ. Đây là ví dụ đơn giản minh hoạ việc kết hợp các độ không đảm bảo đo trong trường hợp cơ "
               "bản nhất. Nhiều ví dụ chi tiết hơn có trong các tài liệu tham khảo được nêu; cần xem lại chúng để "
               "hiểu đầy đủ hơn về phân tích độ không đảm bảo."))
    b.append(p("Đã chỉ ra [8] rằng thường có rất ít khác biệt giữa các độ không đảm bảo tính theo các mô hình khác "
               "nhau. Dữ liệu ở Bảng 4-2 [9] sẽ được dùng để tính độ không đảm bảo đo theo hai mô hình này. Các dữ "
               "liệu này đều theo đơn vị nhiệt độ, nên các hệ số ảnh hưởng hay độ nhạy đều bằng một. Lưu ý việc dùng "
               "chỉ số trên “A” và “B” để cho biết nơi có dữ liệu để tính độ lệch chuẩn. Cũng lưu ý trong ví dụ này "
               "mọi sai số (và do đó mọi độ không đảm bảo) đều độc lập, và mọi bậc tự do của các độ không đảm bảo hệ "
               "thống đều vô cùng, trừ mối nối so sánh có 12 bậc tự do."))
    b.append(table_data("vi"))
    b.append(p("Độ không đảm bảo hệ thống tổng hợp được tính là:"))
    b.append(eq("B<sub>R</sub> = [ (0,06/2)² + (0,07/2,18)² + (0,10/2)² ]<sup>1/2</sup> = 0,065 ≈ 0,13/2", "4.25"))
    b.append(p("Độ không đảm bảo loại A tổng hợp:"))
    b.append(eq("U<sub>A</sub> = [ (0,095)² + (0,045)² + (0,173)² + (0,07/2,18)² ]<sup>1/2</sup> = 0,21", "4.26"))
    b.append(p("Độ không đảm bảo loại B tổng hợp:"))
    b.append(eq("U<sub>B</sub> = [ (0,06/2)² + (0,10/2)² ]<sup>1/2</sup> = 0,058", "4.27"))
    b.append(p("Ở đây cần nhớ 0,21 là căn bậc hai tổng bình phương của các độ không đảm bảo loại A (1S̄<sub>X</sub>) "
               "trong Bảng 4-2, và 0,058 là của các độ không đảm bảo loại B (1S̄<sub>X</sub>). Cũng lưu ý trong phần "
               "lớn trường hợp, các độ không đảm bảo loại B có bậc tự do vô cùng và biểu diễn một giá trị tương đương "
               "2S<sub>X</sub>. Đó là lý do chúng được chia cho 2 — để có một 1S<sub>X</sub> tương đương. Ở đâu có "
               "ít hơn 30 bậc tự do thì phải chia cho thống kê t của Student thích hợp đã cho khoảng tin cậy 95 %. "
               "Với độ không đảm bảo hệ thống của mối nối so sánh ở trên, giá trị đó là 2,18."))
    b.append(p("Nếu lấy “K” là t<sub>95</sub> của Student thì trước hết phải tính bậc tự do. Nhớ rằng mọi thành phần "
               "hệ thống loại “B” đều có bậc tự do vô cùng, trừ giá trị 0,07 có 12 bậc tự do. Cũng vậy, mọi "
               "B<sub>i</sub> trong Bảng 4-2 biểu diễn một 2S<sub>X</sub> tương đương, trừ 0,07 biểu diễn "
               "2,18S<sub>X</sub> vì bậc tự do của nó là 12 chứ không phải vô cùng. Để dùng dữ liệu ở đây, chia tất "
               "cả trừ 0,07 cho 2 và chia 0,07 cho 2,18 để chúng đều biểu diễn 1S<sub>X</sub> như các thành phần ngẫu "
               "nhiên. Mọi độ không đảm bảo loại A, dù hệ thống hay ngẫu nhiên trong bảng, có bậc tự do như ghi "
               "trong bảng. Bậc tự do cho U<sub>ISO</sub> khi đó là:"))
    b.append(eq("df<sub>R</sub> = [ (0,095)² + (0,045)² + (0,173)² + (0,06/2)² + (0,07/2,18)² + (0,10/2)² ]² / "
                "[ (0,095)⁴/9 + (0,045)⁴/4 + (0,173)⁴/11 + 0 + (0,07/2,18)⁴/12 + 0 ] ≈ 22", "4.28"))
    b.append(p("Do đó t<sub>95</sub> = 2,07. Khi đó U<sub>R,ISO</sub> là:"))
    b.append(eq("U<sub>R,ISO</sub> = ± [ (2,07 · 0,21)² + (2,07 · 0,058)² ]<sup>1/2</sup> = ± 0,45 &nbsp; "
                "(độ tin cậy 95 %)", "4.29"))
    b.append(p("Để so sánh chi tiết với hệ kỹ thuật, ở đây ký hiệu là mô hình U<sub>R,ENG</sub>, ba chữ số có nghĩa "
               "được giữ để không bị ảnh hưởng của sai số làm tròn:"))
    b.append(eq("U<sub>R,ISO</sub> = ± [ (2,074 · 0,205)² + (2,074 · 0,0583)² ]<sup>1/2</sup> = ± 0,442", "4.30"))
    b.append(p("Với mô hình hệ kỹ thuật U<sub>R,ENG</sub>, phương trình 4.23, ta được biểu thức:"))
    b.append(eq("U<sub>R,ENG</sub> = ± t<sub>95</sub> [ (0,13/2)² + (0,20)² ]<sup>1/2</sup>", "4.31"))
    b.append(p("Ở đây (0,13/2) là B<sub>R</sub>/2 và 0,20 là thành phần ngẫu nhiên như trước. Để có t<sub>95</sub> "
               "thích hợp, cần tính bậc tự do giống như phương trình 4.28. Ở đó bậc tự do là 22 và t<sub>95</sub> "
               "bằng 2,07. Khi đó U<sub>R,ENG</sub> là:"))
    b.append(eq("U<sub>R,ENG</sub> = ± [ (2,07 · 0,13/2)² + (2,07 · 0,20)² ]<sup>1/2</sup> = ± 0,44 &nbsp; "
                "(độ tin cậy 95 %)", "4.32"))
    b.append(p("Giữ bốn chữ số có nghĩa để so sánh với U<sub>R,ISO</sub> mà không bị ảnh hưởng của làm tròn, ta được:"))
    b.append(eq("U<sub>R,ENG</sub> = ± [ (2,074 · 0,133/2)² + (2,074 · 0,202)² ]<sup>1/2</sup> = ± 0,442", "4.33"))
    b.append(p("Kết quả này trùng với U<sub>R,ISO</sub> ở phương trình 4.30, đúng như dự đoán."))

    # ---------------------------------------------------------------- 4.4
    b.append(h2("4.4 Tóm tắt", "Summary"))
    b.append(p("Dù các công thức tính độ không đảm bảo này không xử lý được mọi tình huống có thể hình dung, chúng sẽ "
               "cung cấp cho phần lớn người làm thí nghiệm một ước lượng hữu ích về độ không đảm bảo của phép thử hay "
               "phép đo. Với cách xử lý chi tiết hơn hoặc các ứng dụng cụ thể của những nguyên tắc này, hãy tham khảo "
               "các tài liệu tham khảo và mục “Thông tin thêm” được khuyến nghị ở cuối chương."))

    b.append(h2("Định nghĩa thuật ngữ", "Defining Terms"))
    b.append('<ul class="ref-list">'
             '<li><b>Độ chính xác (Accuracy):</b> Phản đề của độ không đảm bảo. Cách biểu đạt giới hạn sai số lớn nhất có thể ở một độ tin cậy xác định.</li>'
             '<li><b>Độ tin cậy (Confidence):</b> Cách biểu đạt thống kê về xác suất tính theo phần trăm.</li>'
             '<li><b>Tương quan (Correlation):</b> Quan hệ giữa hai tập dữ liệu. Không nhất thiết là bằng chứng của quan hệ nhân quả.</li>'
             '<li><b>Bậc tự do (Degrees of freedom):</b> Lượng “chỗ” còn lại cho sai số. Cũng có thể biểu diễn là số cơ hội độc lập để các thành phần sai số đóng góp vào sai số tổng hợp.</li>'
             '<li><b>Sai số (Error):</b> [Sai số] = [Đo được] − [Thật]. Là hiệu giữa giá trị đo được và giá trị thật.</li>'
             '<li><b>Hệ số ảnh hưởng (Influence coefficient):</b> Xem độ nhạy.</li>'
             '<li><b>Độ không đảm bảo đo (Measurement uncertainty):</b> Sai số lớn nhất có thể, ở một độ tin cậy xác định, có thể xảy ra một cách hợp lý. Sai số lớn hơn độ không đảm bảo đo hiếm khi xảy ra.</li>'
             '<li><b>Độ không đảm bảo không đối xứng (Non-symmetrical uncertainty):</b> Độ không đảm bảo mà xác suất giá trị thật nằm về một phía của trị trung bình không đều nhau.</li>'
             '<li><b>Truyền độ không đảm bảo (Propagation of uncertainty):</b> Kỹ thuật phân tích để đánh giá tác động của một nguồn sai số (và độ không đảm bảo của nó) lên kết quả thử. Nó dùng các hệ số ảnh hưởng.</li>'
             '<li><b>Sai số ngẫu nhiên (Random error):</b> Sai số gây tản mát trong kết quả thử.</li>'
             '<li><b>Độ không đảm bảo ngẫu nhiên (Random uncertainty):</b> Ước lượng các giới hạn của sai số ngẫu nhiên, thường là một độ lệch chuẩn của trị trung bình.</li>'
             '<li><b>Độ nhạy (Sensitivity):</b> Cách biểu đạt ảnh hưởng của một nguồn sai số lên kết quả thử hay kết quả đo. Là tỷ số giữa thay đổi của kết quả và thay đổi gia tăng của một biến vào hay tham số được đo.</li>'
             '<li><b>Độ lệch chuẩn của trị trung bình (Standard deviation of the average or mean):</b> Độ lệch chuẩn của dữ liệu chia cho số phép đo trong trị trung bình.</li>'
             '<li><b>Sai số hệ thống (Systematic error):</b> Sai số không đổi trong suốt thời gian của một phép thử hay phép đo.</li>'
             '<li><b>Độ không đảm bảo hệ thống (Systematic uncertainty):</b> Ước lượng các giới hạn của sai số hệ thống, thường lấy ở độ tin cậy 95 % với giả định phân bố sai số chuẩn.</li>'
             '<li><b>Giá trị thật (True value):</b> Kết quả mong muốn của một phép đo thực nghiệm.</li>'
             '<li><b>Welch–Satterthwaite:</b> Phương pháp xấp xỉ để xác định số bậc tự do trong độ không đảm bảo ngẫu nhiên của một kết quả.</li>'
             '</ul>')

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append('<ol class="ref-list">'
             '<li>ANSI/ASME PTC 19.1-1985, <em>Instruments and Apparatus, Part 1, Measurement Uncertainty</em>, 1985, 64.</li>'
             '<li>E. O. Doebelin, <em>Measurement Systems, Application and Design</em>, 4th ed., New York: McGraw-Hill, 1990, 38 ff.</li>'
             '<li>International Standards Organization, <em>Guide to the Expression of Uncertainty in Measurement</em>, 1993, 23.</li>'
             '<li>International Standards Organization, <em>Guide to the Expression of Uncertainty in Measurement</em>, 1993, 10 and 11.</li>'
             '<li>R. H. Dieck, <em>Measurement Uncertainty, Methods and Applications</em>, ISA, Research Triangle Park, NC, 1992, 45.</li>'
             '<li>ANSI/ASME PTC 19.1-1998, <em>Instruments and Apparatus, Part 1, Measurement Uncertainty</em>.</li>'
             '<li>K. K. Brown, H. W. Coleman, W. G. Steele and R. P. Taylor, “Evaluation of Correlated Bias Approximations in Experimental Uncertainty Analysis”, AIAA paper 94-0772, 1996.</li>'
             '<li>W. T. Strike III and R. H. Dieck, “Rocket Impulse Uncertainty; An Uncertainty Model Comparison”, Proc. 41st Int. Instrumentation Symposium, Denver, CO, May 1995.</li>'
             '<li>R. H. Dieck, “Measurement Uncertainty Models”, Proc. 42nd Int. Instrumentation Symposium, San Diego, CA, May 1996.</li>'
             '</ol>')

    b.append(h2("Thông tin thêm", "Further Information"))
    b.append('<ul class="ref-list">'
             '<li><em>ICRPG Handbook for Estimating the Uncertainty in Measurements Made with Liquid Propellant Rocket Engine Systems</em>, Chemical Propulsion Information Agency, No. 180, 1969.</li>'
             '<li>R. B. Abernethy et al., <em>Handbook — Gas Turbine Measurement Uncertainty</em>, AEDC, 1973.</li>'
             '<li>R. B. Abernethy and B. Ringhiser, “The History and Statistical Development of the New ASME-SAE-AIAA-ISO Measurement Uncertainty Methodology”, 1985.</li>'
             '<li>W. G. Steele, R. A. Ferguson and R. P. Taylor, “Comparison of ANSI/ASME and ISO Models for Calculation of Uncertainty”, 1994.</li>'
             '<li>W. T. Strike III and R. H. Dieck, “Rocket Impulse Uncertainty; An Uncertainty Model Comparison”, 1995.</li>'
             '</ul>')
    b.append('<div class="chapter-nav">'
             '<a href="%sch03-static-and-dynamic-characteristics-of-instrumentation/"><span class="k">← Chương 3</span>'
             'Đặc tính tĩnh và động của thiết bị đo</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Tất cả chương</a></div>'
             % (BASE_VI, BASE_VI))
    return "".join(b)


# ------------------------------------------------------------------ EN body
def body_en():
    figs = [(1, hbfig.fig_4_1()), (2, hbfig.fig_4_2())]
    b = []
    b.append('<div class="note"><b>What this page is.</b> A companion to Chapter 4: the argument, the equations '
             'and both tables, with the two figures redrawn. The full text lives in <code>Ch04.pdf</code> in the '
             'library catalogue and is not republished here. The complete Vietnamese translation is '
             '<a href="%s%s/">here</a>.</div>' % (BASE_VI, CSLUG))
    b.append('<p class="lead">Measurement error is unknown and unknowable, so what an uncertainty statement '
             'actually claims is a limit at a confidence. Chapter 4 builds that statement: the normal and uniform '
             'distributions, the standard deviation of the average (not of the data), the ISO A/B classification '
             'versus the engineering random/systematic classification, root-sum-squaring with sensitivity '
             'coefficients, the Welch–Satterthwaite degrees of freedom, and Student’s t at 95 %. A worked '
             'temperature example shows both models landing on ±0.44 °F.</p>')
    b.append('<h2>Chapter outline</h2><ul class="toc-list">'
             '<li><span class="n">4.1</span><span class="t">Error: the normal and uniform distributions</span></li>'
             '<li><span class="n">4.2</span><span class="t">Measurement uncertainty model — ISO and engineering '
             'classifications</span></li>'
             '<li><span class="n">4.3</span><span class="t">Calculation of total uncertainty — worked example</span></li>'
             '<li><span class="n">4.4</span><span class="t">Summary · Defining Terms</span></li></ul>')
    b.append('<h2>Figures</h2><p style="color:#888;font-size:.82rem">Redrawn from the Vietnamese edition '
             '(Figures 4-1 and 4-2).</p>')
    for n, f in figs:
        b.append(fig(n, f, lang="en"))
    b.append('<h2>Table 4.1 · Student’s t at 95 % confidence</h2>')
    b.append(table_t95("en"))
    b.append('<h2>Table 4.2 · Temperature measurement uncertainties, °F</h2>')
    b.append(table_data("en"))
    b.append('<h2>The two models agree</h2>'
             '<p>With independent sources and sensitivities of one, the systematic term is '
             'B<sub>R</sub> = √[(0.06/2)² + (0.07/2.18)² + (0.10/2)²] = 0.065, the Type A term is 0.21 and the '
             'Type B term 0.058. Welch–Satterthwaite gives 22 degrees of freedom, so t<sub>95</sub> = 2.07, and '
             'both U<sub>R,ISO</sub> and U<sub>R,ENG</sub> come out at ±0.44 °F at 95 % confidence — which is the '
             'point of the chapter: the classification changes what you learn about the experiment, not the '
             'number you report.</p>')
    b.append('<div class="chapter-nav">'
             '<a href="%sch03-static-and-dynamic-characteristics-of-instrumentation/"><span class="k">← Chapter 3'
             '</span>Static and Dynamic Characteristics</a>'
             '<a href="%s" style="text-align:right;"><span class="k">All chapters →</span>Book contents</a></div>'
             % (BASE_EN, BASE_EN))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 4 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 4 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 4 “Measurement Accuracy” của Ronald H. Dieck — phân bố chuẩn và phân bố đều, "
            "mô hình độ không đảm bảo đo (ISO loại A/B và phân loại kỹ thuật), Welch–Satterthwaite, thống kê t của "
            "Student và ví dụ tính đầy đủ." if vi else
            "Companion to Chapter 4 of the CRC Measurement Handbook — measurement accuracy, uncertainty models and "
            "the worked temperature example, with the full Vietnamese translation.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · Chương 4'
             % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors Handbook</a> · '
             'Chapter 4' % BASE_EN)
    meta = ("Chương 4 · theo Ch04.pdf (CRC Press, 1999) · 2 hình, 2 bảng" if vi
            else "Chapter 4 · 2 figures, 2 tables")
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
