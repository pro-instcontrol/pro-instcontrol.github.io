# -*- coding: utf-8 -*-
"""Handbook Chapter 22 — Strain Measurement
(Christopher S. Lynch, The Georgia Institute of Technology).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch22.py
"""
import os

import hb22fig as F
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch22-strain-measurement"
TITLE_EN = "Strain Measurement"
TITLE_VI = "Đo biến dạng"
BYLINE = "Christopher S. Lynch · Georgia Institute of Technology"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch21-density-measurement"
PREV_VI = "ch21-density-measurement"
PREV_T_EN = "Density Measurement"
PREV_T_VI = "Đo khối lượng riêng"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-22-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
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


def note(t):
    return '<div class="note">%s</div>' % t


def wl(items):
    return ('<p style="font-size:.92rem;color:#333;line-height:1.8;margin:-.3rem 0 1.2rem">'
            + "<br>".join(items) + "</p>")


def ol(items):
    return ('<p style="font-size:.94rem;color:#333;line-height:1.85;margin:-.3rem 0 1.2rem">'
            + "<br>".join("%d. %s" % (i + 1, t) for i, t in enumerate(items)) + "</p>")


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
        "Chương này bắt đầu bằng việc ôn lại các định nghĩa cơ bản về biến dạng và các cách đo biến "
        "dạng. Tiếp theo là tổng quan về nhiều loại cảm biến biến dạng cùng ứng dụng của chúng, và các "
        "nguồn cung cấp cảm biến biến dạng và thiết bị điều kiện tín hiệu. Sau đó, chương đi sâu vào "
        "nguyên lý hoạt động của các kỹ thuật đo biến dạng khác nhau và phần điều kiện tín hiệu đi kèm."))

    # ---- 22.1
    b.append(h2("22.1 Các định nghĩa cơ bản về biến dạng", "Fundamental Definitions of Strain"))
    b.append(p(
        "Ứng suất và biến dạng được định nghĩa trong nhiều giáo trình cơ sở về cơ học vật thể biến dạng "
        "[1, 2]. Hai thuật ngữ này được dùng để mô tả tải tác dụng lên và biến dạng của vật liệu rắn. Loại "
        "vật rắn dễ mô tả nhất là vật liệu đồng nhất và đẳng hướng. Đồng nhất nghĩa là tính chất vật liệu "
        "như nhau tại các vị trí khác nhau; đẳng hướng nghĩa là tính chất vật liệu không phụ thuộc phương "
        "trong vật liệu. Một thanh thép đã ủ là đồng nhất và đẳng hướng, trong khi xương đùi người không "
        "đồng nhất vì tủy có tính chất rất khác xương, và cũng không đẳng hướng vì tính chất của nó khác "
        "nhau dọc theo chiều dài và theo tiết diện."))
    b.append(p(
        "Các khái niệm ứng suất và biến dạng được trình bày trong bối cảnh một thanh dài, đồng nhất, đẳng "
        "hướng chịu tải kéo (Hình 22.1). Ứng suất σ là lực tác dụng F chia cho diện tích tiết diện A. Biến "
        "dạng thu được ε là độ thay đổi chiều dài ΔL chia cho chiều dài ban đầu L. Thanh giãn dài theo "
        "phương của lực kéo (biến dạng dọc ε_L) và co lại theo phương vuông góc với lực (biến dạng ngang "
        "ε_t)."))
    b.append(fig(1, F.fig(1), "vi"))
    b.append(p(
        "Khi biến dạng không quá lớn, nhiều vật liệu rắn có ứng xử như một lò xo tuyến tính; nghĩa là độ "
        "dịch chuyển tỉ lệ với lực tác dụng. Nếu cùng một lực tác dụng lên một miếng vật liệu dày hơn thì "
        "“lò xo” cứng hơn và độ dịch chuyển nhỏ hơn. Điều này dẫn tới một quan hệ giữa lực và độ dịch "
        "chuyển phụ thuộc kích thước của vật liệu. Các tính chất vật liệu như khối lượng riêng và nhiệt "
        "dung riêng phải được định nghĩa theo cách không phụ thuộc hình dạng và kích thước của mẫu. Các "
        "tính chất đàn hồi của vật liệu được định nghĩa thông qua ứng suất và biến dạng. Trong vùng ứng xử "
        "tuyến tính của vật liệu, ứng suất tỉ lệ với biến dạng (Hình 22.2). Tỉ số giữa ứng suất và biến "
        "dạng của thanh chịu kéo là một hằng số đàn hồi gọi là mô-đun Young E. Tỉ số âm giữa biến dạng "
        "ngang và biến dạng dọc là hệ số Poisson ν."))
    b.append(fig(2, F.fig(2), "vi"))
    b.append(p(
        "Lực cũng có thể được tác dụng lên vật liệu theo cách gây méo hình học thay vì giãn dài (Hình "
        "22.3). Lực tác dụng tiếp tuyến với một mặt chia cho diện tích tiết diện được mô tả là ứng suất "
        "trượt τ. Độ méo có thể được đo bằng góc thay đổi tạo ra; khi góc thay đổi nhỏ thì đó là biến dạng "
        "trượt γ. Khi quan hệ giữa ứng suất trượt và biến dạng trượt là tuyến tính, tỉ số giữa ứng suất "
        "trượt và biến dạng trượt là mô-đun trượt G."))
    b.append(fig(3, F.fig(3), "vi"))
    b.append(p(
        "Sự thay đổi nhiệt độ cũng gây ra biến dạng. Đó là sự giãn nở nhiệt. Ở phần lớn vật liệu, biến "
        "dạng nhiệt tăng theo nhiệt độ. Trong một dải nhiệt độ hẹp, quan hệ giữa biến dạng nhiệt và nhiệt "
        "độ là tuyến tính. Trong trường hợp này, biến dạng chia cho độ thay đổi nhiệt độ là hệ số giãn nở "
        "nhiệt α. Ở vật liệu đẳng hướng, giãn nở nhiệt chỉ tạo ra biến dạng giãn dài, không tạo ra biến "
        "dạng trượt."))
    b.append(p(
        "Các phương chính trong một vật liệu là những phương chỉ bị giãn dài mà không bị trượt. Trên một "
        "mặt bất kỳ của vật rắn, luôn có ít nhất hai phương chính mà biến dạng thuần là giãn dài. Điều này "
        "thấy được nếu vẽ hai hình vuông trên thanh chịu kéo đều (Hình 22.4). Khi thanh bị kéo, hình vuông "
        "thẳng hàng với tải bị giãn dài, còn hình vuông đặt 45° vừa bị méo (các góc đã thay đổi) vừa bị "
        "giãn dài. Nếu biết các phương chính, như với thanh chịu kéo, thì có thể dán các gage biến dạng "
        "theo các phương đó. Nếu chưa biết các phương chính — ví dụ gần một lỗ hoặc một rãnh khía, trong "
        "mẫu dị hướng, hoặc trong kết cấu có hình học phức tạp — thì cần thêm các gage biến dạng để mô tả "
        "đầy đủ trạng thái biến dạng."))
    b.append(fig(4, F.fig(4), "vi"))
    b.append(p(
        "Có thể kết hợp các tính chất đàn hồi và tính chất nhiệt để được định luật Hooke, các phương trình "
        "22.1 đến 22.6."))
    b.append(eq("ε_x = σ_x/E − (ν/E)(σ_y + σ_z)", "22.1"))
    b.append(eq("ε_y = σ_y/E − (ν/E)(σ_x + σ_z)", "22.2"))
    b.append(eq("ε_z = σ_z/E − (ν/E)(σ_x + σ_y)", "22.3"))
    b.append(eq("γ_xy = τ_xy / G", "22.4"))
    b.append(eq("γ_xz = τ_xz / G", "22.5"))
    b.append(eq("γ_yz = τ_yz / G", "22.6"))
    b.append(p(
        "Có nhiều loại cảm biến được dùng để đo biến dạng, gồm gage áp điện trở (gage biến dạng lá hoặc "
        "dây và gage biến dạng bán dẫn), gage áp điện (màng polyvinylidene fluoride — PVDF — và thạch "
        "anh), gage sợi quang, màng và vật liệu lưỡng chiết, và cách tử Moiré. Mỗi loại cảm biến cần một "
        "hệ điều kiện tín hiệu chuyên dụng riêng. Việc chọn cảm biến biến dạng tốt nhất cho một phép đo "
        "dựa trên nhiều yếu tố: hình học mẫu, nhiệt độ, tốc độ biến dạng, tần số, độ lớn, cũng như giá "
        "thành, độ phức tạp, độ chính xác, độ phân giải không gian, độ phân giải thời gian, độ nhạy với "
        "biến dạng ngang, độ nhạy với nhiệt độ và độ phức tạp của phần điều kiện tín hiệu. Bảng 22.1 mô tả "
        "các đặc tính điển hình của một số cảm biến. Bảng 22.2 liệt kê một số nhà cung cấp cùng giá xấp xỉ "
        "của cảm biến và thiết bị điện tử điều kiện tín hiệu đi kèm."))
    b.append(table(
        ["Mô tả", "Độ nhạy biến dạng dọc", "Độ nhạy biến dạng ngang", "Độ nhạy nhiệt độ",
         "Độ phân giải biến dạng", "Độ phân giải không gian", "Độ phân giải thời gian",
         "Dải biến dạng đo được"],
        [["Foil constantan áp điện trở", "ΔR/R trên Δε_L = 2,1", "ΔR/R trên Δε_t &lt; 0,02",
          "ΔR/R trên ΔT = 2 × 10⁻⁶/°C", "&lt; 1 µstrain ᵃ", "5–100 mm ᵇ", "&lt; 1 µs ᶜ", "0–3 %"],
         ["Foil constantan đã ủ ᵈ", "2,1", "&lt; 0,02", "2 × 10⁻⁶/°C", "&lt; 11 µstrain",
          "5–100 mm", "&lt; 1 µs", "0–10 %"],
         ["Bán dẫn áp điện trở", "150", "???", "1,7 × 10⁻³/°C", "&lt; 0,1 µstrain", "1–15 mm",
          "&lt; 1 µs", "0–0,1 %"],
         ["Áp điện PVDF", "120 nC/m²/µε", "60 nC/m²/µε", "−27 µC/m²/°C", "1–10 µstrain",
          "cỡ gage", "&lt; 1 µs", "0–30 %"],
         ["Áp điện thạch anh dán lên thép", "150 nC/m²/µε", "—", "0", "&lt; 0,01 µstrain",
          "gage 20 mm", "&lt; 10 µs", "0–0,1 %"],
         ["Sợi quang Fabry–Perot", "2 đến 1000 µstrain/V", "gần bằng 0", "—", "&lt; 1 µstrain",
          "2–10 mm", "&lt; 20 µs", "—"],
         ["Màng lưỡng chiết", "Kε = 0,15–0,002", "—", "—", "—", "0,5 mm ᶠ", "&lt; 5 µs",
          "0,05–5 %"],
         ["Moiré", "1 bậc vân / 417 nm dịch chuyển", "1 bậc vân / 417 nm", "không xác định",
          "41,7 µε trên 10 mm", "toàn trường ᵍ", "giới hạn bởi mạch điện", "0,005–5 %"]],
        "Bảng 22.1 · So sánh các loại cảm biến biến dạng (theo bản gốc). "
        "ᵃ Khi có phần điều kiện tín hiệu tốt. ᵇ Bằng diện tích lưới. ᶜ Đáp ứng của gage trong vòng "
        "100 ns; phần lớn mạch điều kiện tín hiệu giới hạn thời gian đáp ứng nhỏ hơn nhiều. ᵈ Foil đã ủ "
        "có giới hạn chảy thấp và biến dạng tới đứt lớn; nó cũng có trễ khi dỡ tải và dịch điểm không "
        "dưới tải chu kỳ. ᵉ Kỹ thuật này đo hiệu các biến dạng chính: ε₂ − ε₁ = Nλ/2tK. ᶠ Xấp xỉ bằng "
        "chiều dày màng. ᵍ Độ phân giải biến dạng theo không gian phụ thuộc mức biến dạng; đây là kỹ "
        "thuật đo dịch chuyển."))
    b.append(p(
        "Số liệu trong Bảng 22.1 chỉ mang tính minh hoạ và hoàn toàn không đầy đủ. Phần mô tả cảm biến chỉ "
        "nêu loại cảm biến, không nêu nhiều kích thước và hình dạng khác nhau. Độ nhạy biến dạng dọc được "
        "cho bằng đầu ra của cảm biến trên một đơn vị biến dạng dọc theo phương của cảm biến. Nếu tính cả "
        "phần điều kiện tín hiệu thì mọi độ nhạy có thể được biểu diễn bằng vôn trên một đơn vị biến dạng "
        "[3, 4], nhưng giá trị này phụ thuộc độ khuếch đại và chất lượng của bộ điều kiện tín hiệu. Độ "
        "nhạy nhiệt độ được cho bằng sự thay đổi đầu ra do một thay đổi nhiệt độ. Trong nhiều trường hợp "
        "có thể đạt độ phân giải biến dạng cao hơn, nhưng phân giải được biến dạng nhỏ hơn thì khó hơn và "
        "có thể cần cách ly rung và cách ly nhiệt. Với kỹ thuật Moiré, độ phân giải biến dạng là hàm của "
        "chiều dài vùng quan sát: kỹ thuật này phân giải được độ dịch chuyển 100 nm (1/4 bậc vân), và lấy "
        "giá trị đó chia cho chiều dài quan sát để được độ phân giải biến dạng. Độ phân giải không gian "
        "tương ứng với chiều dài gage với phần lớn các loại cảm biến. Dải biến dạng đo được liệt kê là "
        "giới hạn trên của từng loại cảm biến; độ chính xác và độ tin cậy thường giảm khi cảm biến được "
        "dùng ở giới hạn trên của khả năng."))
    b.append(table(
        ["Nhà cung cấp", "Loại cảm biến", "Giá cảm biến", "Giá thiết bị điều kiện tín hiệu"],
        [["Micro Measurements (Raleigh, NC)", "Foil áp điện trở; màng lưỡng chiết",
          "từ 5,00 USD; từ 10,00 USD",
          "Cầu Wheatstone: từ 500 USD; kính phân cực: 5.000–10.000 USD"],
         ["Texas Measurements (College Station, TX)", "Foil và dây áp điện trở; load cell",
          "từ 5,00 USD", "—"],
         ["Omega Engineering (Stamford, CT)", "Foil áp điện trở", "từ 5,00 USD",
          "Máy đo biến dạng: từ 550 USD; cầu Wheatstone: từ 2.700 USD"],
         ["Dynasen (Goleta, CA)",
          "Foil áp điện trở; gage chuyên dụng cho phép đo sóng xung kích; PVDF áp điện đã hiệu chuẩn",
          "từ 55,00 USD; từ 55,00 USD",
          "Cầu Wheatstone xung 2 kênh: 5.000 USD; bộ tích phân điện tích thụ động: 250,00 USD"],
         ["Entran Sensors and Electronics (Fairfield, NJ)", "Bán dẫn áp điện trở",
          "từ 15,00 USD", "—"],
         ["Amp Inc. Piezo Film Sensors (Valley Forge, PA)", "PVDF áp điện (chưa hiệu chuẩn)",
          "từ 5,00 USD", "—"],
         ["Kistler Instrument Corp. (Amherst, NY)", "Thạch anh áp điện", "—",
          "Điện kế; bộ khuếch đại điện tích"],
         ["F&amp;S Inc., Fiber and Sensor Technologies (Blacksburg, VA)",
          "Cảm biến biến dạng Fabry–Perot", "từ 75 USD", "Điện tử: từ 3.500,00 USD"],
         ["Photomechanics (Vestal, NY)", "Giao thoa kế Moiré", "60.000 USD", "—"]],
        "Bảng 22.2 · Nguồn cung cấp và giá cảm biến biến dạng. Giá là giá niêm yết năm 1999 (USD) trong "
        "bản gốc; địa chỉ bưu chính đầy đủ đã được lược bớt, chỉ giữ thành phố và bang."))
    b.append(p(
        "Các nhà sản xuất cảm biến khác nhau cung cấp thông tin kỹ thuật bao gồm chi tiết cách dùng cảm "
        "biến, dữ liệu hiệu chuẩn hoặc đặc tính đầy đủ, và chi tiết về phần điều kiện tín hiệu. Các ghi "
        "chú và mẹo kỹ thuật phong phú do Measurements Group, Inc. cung cấp đề cập những vấn đề như ảnh "
        "hưởng nhiệt [5], hiệu chính độ nhạy ngang [6], kỹ thuật hàn [7], bộ ba gage (rosette) [8] và mỏi "
        "của gage [9]. Danh mục gage biến dạng có thông tin về vật liệu làm gage, kích thước và cách chọn. "
        "Các nhà sản xuất cảm biến khác cũng cung cấp thông tin tương tự."))

    # ---- 22.2
    b.append(h2("22.2 Nguyên lý hoạt động của cảm biến biến dạng",
                "Principles of Operation of Strain Sensors"))

    # -- foil
    b.append(h3("Gage lá áp điện trở", "Piezoresistive Foil Gages"))
    b.append(p(
        "Gage lá và gage dây áp điện trở gồm một đế cách điện mỏng (thường là màng polyimide), một lưới lá "
        "hoặc dây (thường bằng constantan) dán lên đế, các dây dẫn nối lưới với mạch đo điện trở, và thường "
        "có thêm một lớp bọc cách điện (một tấm polyimide thứ hai) (Hình 22.5). Lưới được bố trí theo một "
        "phương duy nhất để biến dạng sẽ kéo giãn các nhánh của lưới theo chiều dài. Gage được thiết kế sao "
        "cho biến dạng theo chiều rộng hay chiều ngang chỉ tách các nhánh lưới ra mà không kéo giãn chúng. "
        "Nhờ vậy gage chỉ nhạy với biến dạng dọc theo chiều dài của nó. Luôn có một ít độ nhạy với biến "
        "dạng ngang, và hầu như không có độ nhạy với biến dạng trượt. Trong phần lớn trường hợp, có thể bỏ "
        "qua độ nhạy ngang."))
    b.append(fig(5, F.fig(5), "vi"))
    b.append(p(
        "Khi gage lá hoặc gage dây áp điện trở được dán lên mẫu và mẫu bị biến dạng, gage cũng biến dạng "
        "theo. Sự thay đổi điện trở liên hệ với biến dạng qua hệ số gage, phương trình 22.7."))
    b.append(eq("ΔR / R = G · ε", "22.7"))
    b.append(wl(["trong đó <b>ΔR/R</b> = thay đổi điện trở tương đối",
                 "<b>G</b> = hệ số gage",
                 "<b>ε</b> = biến dạng"]))
    b.append(p(
        "Các gage này đáp ứng với biến dạng trung bình trên diện tích mà lưới phủ [10]. Sự thay đổi điện "
        "trở cũng nhạy với nhiệt độ. Nếu nhiệt độ thay đổi trong thời gian đo thì phải hiệu chính để phân "
        "biệt đáp ứng do biến dạng với đáp ứng do nhiệt. Đáp ứng của gage với biến dạng dọc, biến dạng "
        "ngang và thay đổi nhiệt độ được cho bởi phương trình 22.8."))
    b.append(eq("ΔR / R = G_L · ε_L + G_t · ε_t + G_T · ΔT", "22.8"))
    b.append(wl(["trong đó <b>G_L</b>, <b>G_t</b> và <b>G_T</b> lần lượt là độ nhạy dọc, độ nhạy ngang và "
                 "độ nhạy nhiệt độ"]))
    b.append(p(
        "Micromeasurements, Inc. dùng một cách ký hiệu khác: dữ liệu gage của hãng được cung cấp dưới dạng "
        "G_L = FG, G_t = K_tFG, G_T = βg. Khi một gage biến dạng được dán lên mẫu và nhiệt độ thay đổi thì "
        "biến dạng dùng trong phương trình 22.8 là biến dạng tổng, gồm cả biến dạng nhiệt và biến dạng do "
        "ứng suất, như cho bởi phương trình 22.7."))
    b.append(p(
        "Phải loại bỏ phần đóng góp của nhiệt độ vào đầu ra của gage nếu gage được dùng trong các thử "
        "nghiệm có nhiệt độ thay đổi. Có thể dùng một sơ đồ gọi là tự bù nhiệt (self-temperature "
        "compensation — STC). Việc này được thực hiện bằng cách chọn một vật liệu áp điện trở mà đầu ra "
        "nhiệt của nó có thể bị triệt tiêu bởi biến dạng do giãn nở nhiệt của mẫu thử. Các nhà sản xuất "
        "gage quy định các số STC tương ứng với hệ số giãn nở nhiệt của các vật liệu mẫu thông dụng."))
    b.append(p(
        "Biến dạng của vật liệu áp điện trở tạo ra sự thay đổi điện trở tương đối. Sự thay đổi điện trở là "
        "kết quả của thay đổi điện trở suất và thay đổi kích thước. Xét một nhánh đơn của lưới gage biến "
        "dạng có tiết diện chữ nhật (Hình 22.6). Điện trở được cho bởi phương trình 22.9."))
    b.append(eq("R = ρ · L / A", "22.9"))
    b.append(wl(["trong đó <b>R</b> = điện trở",
                 "<b>ρ</b> = điện trở suất",
                 "<b>L</b> = chiều dài",
                 "<b>A</b> = diện tích tiết diện"]))
    b.append(fig(6, F.fig(6), "vi"))
    b.append(p(
        "Một thay đổi nhỏ của điện trở được cho bởi các số hạng bậc nhất của khai triển chuỗi Taylor, "
        "phương trình 22.10."))
    b.append(eq("ΔR = (∂R/∂L)·ΔL + (∂R/∂A)·ΔA + (∂R/∂ρ)·Δρ", "22.10"))
    b.append(p(
        "Lấy vi phân phương trình 22.9 để được từng số hạng của phương trình 22.10 rồi chia cho điện trở "
        "ban đầu, ta được phương trình 22.11."))
    b.append(eq("ΔR / R₀ = Δρ / ρ₀ + ΔL / L₀ − ΔA / A₀", "22.11"))
    b.append(p(
        "Sự thay đổi điện trở tương đối là do thay đổi điện trở suất, thay đổi biến dạng chiều dài và thay "
        "đổi biến dạng diện tích."))
    b.append(p(
        "Gage biến dạng là một vật liệu composite. Kim loại trong gage giống như một sợi kim loại trong "
        "nền polymer. Khi nền polymer bị biến dạng, kim loại bị kéo theo theo chiều dài; nhưng theo chiều "
        "rộng và chiều dày, biến dạng không được truyền sang kim loại. Điều này dẫn tới một trạng thái ứng "
        "suất gọi là ứng suất một trục. Trạng thái này đã được thảo luận trong các ví dụ trên. Chi tiết "
        "toán học liên quan tới bài toán vật thể nhúng [11, 12]. Chấp nhận rằng trạng thái ứng suất là một "
        "trục, quan hệ giữa thay đổi diện tích và thay đổi chiều dài trong phương trình 22.11 được tìm từ "
        "hệ số Poisson. Biến dạng diện tích là tổng của biến dạng chiều rộng và biến dạng chiều dày, "
        "phương trình 22.12."))
    b.append(eq("ΔA / A₀ = Δw / w₀ + Δt / t₀", "22.12"))
    b.append(p("Định nghĩa hệ số Poisson cho phương trình 22.13."))
    b.append(eq("ΔA / A₀ = −2ν · ΔL / L₀", "22.13"))
    b.append(wl(["trong đó <b>Δw/w</b> = biến dạng chiều rộng và <b>Δt/t</b> = biến dạng chiều dày"]))
    b.append(p(
        "Thay phương trình 22.13 vào phương trình 22.11 ta được phương trình 22.14 cho sự thay đổi điện "
        "trở tương đối."))
    b.append(eq("ΔR / R₀ = Δρ / ρ₀ + (1 + 2ν) · ΔL / L₀", "22.14"))
    b.append(p(
        "Điện trở suất tương đối thay đổi theo ứng suất. Điện trở suất là một ten-xơ bậc hai [13], và phần "
        "đóng góp vào thay đổi điện trở tổng có thể được tìm theo biến dạng bằng định luật cấu tạo đàn hồi "
        "[14]. Kết quả dẫn tới hệ số gage đàn hồi chỉ hơn 2 một chút đối với gage constantan. Nếu biến dạng "
        "lớn, lá hoặc dây trong gage sẽ bị biến dạng dẻo. Khi biến dạng là dẻo, thay đổi điện trở suất là "
        "không đáng kể và thay đổi kích thước chiếm ưu thế. Trong trường hợp này hệ số Poisson là 0,5 và hệ "
        "số gage là 2. Hiệu ứng này được dùng để chế tạo các gage đo biến dạng lớn hơn 1,5 %. Trong trường "
        "hợp đó người ta dùng foil đã ủ; foil ủ chịu biến dạng dẻo mà không bị đứt. Các gage này có thể đo "
        "biến dạng vượt quá 10 %. Khi kim loại bị biến dạng dẻo, chúng không dỡ tải trở về biến dạng ban "
        "đầu; điều này thể hiện thành độ trễ trong đáp ứng của gage, nghĩa là khi dỡ tải, điện trở không "
        "trở về giá trị ban đầu."))
    b.append(p(
        "Gage biến dạng lá và dây có thể có nhiều cấu hình khác nhau. Chúng có thể được chế tạo với các vật "
        "liệu đế khác nhau, và để hở mặt hoặc bọc kín hoàn toàn. Vật liệu đế gồm polyimide và nhựa phenolic "
        "gia cố sợi thuỷ tinh. Gage có thể có các vấu hàn để gắn dây dẫn, hoặc có dây dẫn gắn sẵn. Chúng có "
        "nhiều kích thước, và có nhiều cấu hình nhiều gage gọi là bộ ba gage (rosette)."))
    b.append(p(
        "Gage biến dạng được gắn lên mẫu thử bằng keo dán theo một quy trình phù hợp để dán phần lớn các "
        "loại cảm biến biến dạng. Việc này được thực hiện theo một quy trình từng bước [15], bắt đầu bằng "
        "chuẩn bị bề mặt. Dưới đây tóm tắt quy trình. Để gắn gage biến dạng thành công, trước tiên bề mặt "
        "được tẩy dầu mỡ. Bề mặt được mài bằng vải nhám mịn hoặc giấy ráp hạt 400 để loại bỏ sơn bong, gỉ "
        "hoặc các cặn bám. Các đường bố trí gage được vẽ (không phải khắc) trên bề mặt theo hình chữ thập "
        "bằng bút mực hoặc bút chì, một đường theo phương của lưới và một đường theo phương ngang. Sau đó "
        "bề mặt được làm sạch bằng cồn isopropyl, có thể bằng máy rửa siêu âm hoặc bằng khăn lau. Nếu lau, "
        "khăn giấy hoặc gạc phải được gấp lại và nhỏ một ít cồn lên; bề mặt phải được lau một lần theo một "
        "chiều rồi bỏ khăn đi, và lặp lại động tác lau theo chiều kia. Bước cuối cùng là trung hoà bề mặt, "
        "đưa độ kiềm về pH 7 đến 7,5; chất trung hoà bề mặt có bán tại phần lớn nhà cung cấp keo dán. Bước "
        "cuối là dán gage."))
    b.append(p(
        "Việc dán gage được thực hiện bằng băng dính cellophane, keo đông nhanh và chất xúc tác. Gage được "
        "đặt trên một mặt thuỷ tinh hoặc nhựa sạch, mặt dán úp xuống, dùng nhíp. (Không bao giờ chạm tay "
        "vào gage — dầu từ da sẽ ngăn cản việc dính đúng.) Sau đó gage được dán cố định bằng một đoạn băng "
        "cellophane dài 100 mm, rồi băng được bóc lên cùng với gage đã dính vào. Lúc này có thể dán gage "
        "vào đúng vị trí mong muốn trên mẫu thử. Khi gage đã được căn chỉnh đúng, băng được bóc ngược lại "
        "từ một phía, nhấc gage ra khỏi bề mặt; băng phải còn dính vào bề mặt khoảng 1 cm tính từ gage, sao "
        "cho một phía của băng vẫn gắn với mẫu để có thể đưa gage về đúng vị trí một cách dễ dàng. Một lớp "
        "mỏng chất xúc tác được phết lên mặt gage đã lộ ra. Một giọt keo được nhỏ vào chỗ tiếp giáp giữa "
        "băng và mẫu. Giữ băng nghiêng khoảng 30° so với bề mặt rồi từ từ miết băng xuống bề mặt; động tác "
        "này đẩy đường keo tiến về phía trước. Sau khi đường keo đã đi qua gage, ấn gage vào vị trí và giữ "
        "khoảng 1 phút. Lúc này có thể bóc băng ra để lộ gage và gắn dây dẫn."))
    b.append(p(
        "Sự thay đổi điện trở tương đối của gage áp điện trở thường được đo bằng một cầu Wheatstone [16]. "
        "Cách này cho phép đo một thay đổi điện trở nhỏ so với một giá trị không ban đầu, thay vì so với "
        "một giá trị điện trở lớn, nhờ đó tăng độ nhạy và độ phân giải tương ứng. Cầu Wheatstone là tổ hợp "
        "của bốn điện trở và một nguồn điện áp (Hình 22.7). Một đến bốn điện trở trong cầu có thể là gage "
        "biến dạng. Đầu ra của cầu là hiệu giữa điện áp tại điểm B và điểm D. Các nhánh ABC và ADC là những "
        "bộ chia áp, nên V_B và V_D được cho bởi phương trình 22.15a và 22.15b."))
    b.append(fig(7, F.fig(7), "vi"))
    b.append(eq("V_B = V_in · R₂ / (R₁ + R₂)", "22.15a"))
    b.append(eq("V_D = V_in · R₃ / (R₃ + R₄)", "22.15b"))
    b.append(p(
        "Đầu ra của cầu, phương trình 22.16, bằng không khi thoả mãn điều kiện cân bằng, phương trình "
        "22.17."))
    b.append(eq("V₀ = V_B − V_D", "22.16"))
    b.append(eq("R₁ · R₃ = R₂ · R₄", "22.17"))
    b.append(p(
        "Các bộ điều kiện tín hiệu cầu Wheatstone được chế tạo có thêm cách “cân bằng” cầu bằng việc điều "
        "chỉnh tỉ số các điện trở sao cho đầu ra của cầu ban đầu bằng không."))
    b.append(p(
        "Điều kiện cân bằng không còn được thoả mãn nếu các giá trị điện trở thay đổi nhỏ ΔR₁, ΔR₂, ΔR₃, "
        "ΔR₄. Nếu thay các giá trị R₁ + ΔR₁… vào phương trình 22.15, thay kết quả vào phương trình 22.16, "
        "dùng điều kiện 22.17 và bỏ qua các số hạng bậc cao hơn, ta được phương trình 22.18 cho đầu ra của "
        "cầu."))
    b.append(eq("V_out = V_in · [R₁R₃ / ((R₁+R₂)(R₃+R₄))] · "
                "( ΔR₁/R₁ − ΔR₂/R₂ + ΔR₃/R₃ − ΔR₄/R₄ )", "22.18"))
    b.append(p(
        "Cầu Wheatstone có thể được dùng để triệt tiêu trực tiếp ảnh hưởng của trôi nhiệt. Nếu R₁ là một "
        "gage biến dạng dán lên mẫu và R₂ là một gage biến dạng được giữ trên mẫu bằng hợp chất tản nhiệt "
        "(một loại mỡ dẫn nhiệt có bán tại mọi cửa hàng điện tử) thì R₁ sẽ đáp ứng với cả biến dạng và "
        "nhiệt độ, còn R₂ chỉ đáp ứng với nhiệt độ. Vì cầu trừ đầu ra của R₁ cho đầu ra của R₂, ảnh hưởng "
        "của nhiệt độ bị triệt tiêu."))
    b.append(p(
        "Độ nhạy của một hệ đo là đầu ra trên một đơn vị thay đổi của đại lượng cần đo. Nếu sự thay đổi "
        "điện trở là do một gage biến dạng, độ nhạy của hệ cầu Wheatstone tỉ lệ với điện áp vào; tăng điện "
        "áp sẽ tăng độ nhạy. Việc tăng điện áp lên giá trị lớn có một giới hạn thực tế. Công suất tiêu tán "
        "(nhiệt) trong gage là P = I²R, trong đó I là dòng điện qua gage, có thể tìm được từ điện áp vào và "
        "các điện trở của cầu. Nhiệt này phải được truyền đi đâu đó, nếu không nhiệt độ của gage sẽ tăng "
        "liên tục và điện trở sẽ thay đổi do bị đốt nóng. Nếu gage được gắn trên một vật dẫn nhiệt tốt thì "
        "có thể truyền nhiều nhiệt đi hơn so với khi gage gắn trên một chất cách nhiệt. Mẫu phải đóng vai "
        "trò một bộ tản nhiệt."))
    b.append(p(
        "Khả năng tản nhiệt tỉ lệ với độ dẫn nhiệt của vật liệu mẫu. Một gradient nhiệt độ hợp lý để cho phép "
        "gage gây ra trong vật liệu là 40 °C mỗi mét (khoảng 1 °C mỗi 25 mm). Với các mẫu dày (chiều dày "
        "gấp vài lần kích thước lớn nhất của gage), nhiệt này có thể được truyền tới các ngàm kẹp hoặc đối "
        "lưu ra khí quyển xung quanh. Nếu bốn điện trở của cầu xấp xỉ bằng nhau thì công suất cấp cho gage "
        "theo điện áp cầu được cho bởi phương trình 22.19."))
    b.append(eq("P = V_in² / (4R)", "22.19"))
    b.append(p(
        "Công suất trên một đơn vị diện tích lưới A_g, hay mật độ công suất cấp cho gage, có thể được cân "
        "bằng với độ dẫn nhiệt của mẫu và gradient nhiệt độ cho phép trong mẫu theo phương trình 22.20."))
    b.append(eq("P / A_g = V_in² / (4 R A_g) = K · ∇T", "22.20"))
    b.append(p(
        "Độ dẫn nhiệt của phần lớn vật liệu có thể tra trong các bảng hoặc trên Web. Một số giá trị điển "
        "hình: Al: K = 204 W m⁻¹ °C⁻¹; thép: K = 20 đến 70 W m⁻¹ °C⁻¹; thuỷ tinh: K = 0,78 W m⁻¹ °C⁻¹ "
        "[17]. Điện áp cầu chấp nhận được có thể tính từ phương trình 22.21."))
    b.append(eq("V_in = √( 4 K · ∇T · R · A_g )", "22.21"))
    b.append(p(
        "Một phép tính mẫu cho thấy với một lưới 120 Ω kích thước 0,010 m × 0,010 m dán lên một miếng nhôm "
        "dày có độ dẫn nhiệt 204 W m⁻¹ °C⁻¹ và gradient nhiệt độ chấp nhận được 40 °C mỗi mét, điện áp cầu "
        "cực đại là 19 V. Nếu dùng mẫu mỏng thì gradient nhiệt độ cho phép sẽ nhỏ hơn. Nếu dùng gage nhỏ hơn "
        "để có độ phân giải không gian tốt hơn thì phải giảm điện áp kích thích cầu, kéo theo giảm độ nhạy."))
    b.append(p(
        "Có thể dùng điện áp cầu cao hơn đáng kể nếu điện áp cầu được tạo xung trong thời gian ngắn. Cách "
        "này tiêu tán năng lượng trong gage ít hơn nhiều, do đó tăng độ nhạy lên 10 đến 100 lần. Trên thị "
        "trường có các bộ nguồn xung cho cầu Wheatstone với độ rộng xung thay đổi từ 10 µs và điện áp kích "
        "thích 350 V [18]."))
    b.append(p(
        "Phép đo biến dạng cần thực hiện thường nằm trong một tình huống tải phức tạp, khi chưa biết các "
        "phương của biến dạng chính. Trong trường hợp này phải dán ba gage biến dạng lên mẫu thử theo ba "
        "góc. Cấu hình này gọi là bộ ba gage (strain rosette). Góc giữa bộ ba gage và các phương chính, "
        "cũng như độ lớn của các biến dạng chính, có thể được xác định từ đầu ra của ba gage. Việc này được "
        "thực hiện dễ dàng nhất bằng cách dựng vòng tròn Mohr (Hình 22.8)."))
    b.append(fig(8, F.fig(8), "vi"))
    b.append(p(
        "Một bộ ba gage thông dụng là kiểu 0–45–90°. Bộ gage được dán lên mẫu với các góc quay tương đối "
        "0°, 45° và 90°; các phương này được gọi là phương x, x′ và y. Các phương chính được gọi là phương 1 "
        "và phương 2. Góc chưa biết giữa phương x và phương 1 được gọi là θ. Vòng tròn Mohr được dựng với "
        "biến dạng giãn trên trục hoành và biến dạng trượt trên trục tung. Tâm của vòng tròn được gọi là C "
        "và bán kính là R. Các phương chính ứng với biến dạng trượt bằng không. Các giá trị chính được cho "
        "bởi phương trình 22.22 và 22.23."))
    b.append(eq("ε₁ = C + R", "22.22"))
    b.append(eq("ε₂ = C − R", "22.23"))
    b.append(p(
        "Một phép quay góc 2θ trên vòng tròn Mohr tương ứng với một phép quay bộ gage góc θ so với các "
        "phương chính. Tâm của vòng tròn được cho bởi phương trình 22.24 và đầu ra của các gage biến dạng "
        "được cho bởi phương trình 22.25 đến 22.27."))
    b.append(eq("C = (ε_x + ε_y) / 2", "22.24"))
    b.append(eq("ε_x − C = R · cos2θ", "22.25"))
    b.append(eq("ε_x′ − C = −R · sin2θ", "22.26"))
    b.append(eq("ε_y − C = −R · cos2θ", "22.27"))
    b.append(p(
        "Chia phương trình 22.25 cho phương trình 22.26 ta được θ, rồi từ đó được R, theo phương trình "
        "22.28 và 22.29."))
    b.append(eq("R = √[ (C − ε_x′)² + (C − ε_x)² ]", "22.28"))
    b.append(eq("tan2θ = −(ε_x′ − C) / (ε_x − C)", "22.29"))
    b.append(p(
        "Như vậy các phương chính và các giá trị biến dạng chính đã được tìm ra từ đầu ra của ba gage trong "
        "bộ ba."))

    # -- semiconductor
    b.append(h3("Gage bán dẫn áp điện trở", "Piezoresistive Semiconducting Gages"))
    b.append(p(
        "Gage biến dạng bán dẫn áp điện trở, giống như gage lá và gage dây áp điện trở, thay đổi điện trở "
        "khi có biến dạng, nhưng với hệ số gage lớn hơn gần một bậc [19]. Sự ghép giữa thay đổi điện trở và "
        "nhiệt độ rất lớn, nên các gage này phải được bù nhiệt. Sự thay đổi điện trở khi nhiệt độ thay đổi "
        "một lượng nhỏ có thể lớn hơn một bậc so với sự thay đổi do biến dạng gây ra. Gage biến dạng bán "
        "dẫn thường được dùng để chế tạo các bộ chuyển đổi như load cell. Chúng dễ vỡ và cần hết sức cẩn "
        "thận khi sử dụng."))

    # -- piezoelectric
    b.append(h3("Gage áp điện", "Piezoelectric Gages"))
    b.append(p(
        "Gage biến dạng áp điện thực chất là những tụ điện bản song song mà chất điện môi thay đổi phân cực "
        "khi có biến dạng [14]. Khi sự phân cực thay đổi, một điện tích tỉ lệ với biến dạng được sinh ra "
        "trên các điện cực. Gage biến dạng màng PVDF rẻ tiền nhưng không chính xác lắm và dễ bị khử phân cực "
        "ở nhiệt độ vừa phải. Chúng là cảm biến tốt cho các phép đo động như tần số và suy giảm logarit, "
        "nhưng không dùng để đo định lượng biến dạng. Khi dùng cho các phép đo gần tĩnh, điện tích có xu "
        "hướng rò qua dụng cụ đo, làm tín hiệu suy giảm với hằng số thời gian phụ thuộc trở kháng vào của "
        "dụng cụ đo. Gage thạch anh rất chính xác nhưng cũng mất điện tích qua dụng cụ đo. Hằng số thời "
        "gian có thể tương đối dài (từ giây đến giờ) khi dùng điện kế hoặc bộ khuếch đại điện tích."))
    b.append(p(
        "Gage PVDF gồm một màng áp điện mỏng có các điện cực kim loại (Hình 22.9). Dây dẫn nối các điện cực "
        "với một mạch đo điện tích. Có thể mua loại gage có các điện cực được bọc kín giữa các lớp polyimide "
        "cách điện."))
    b.append(fig(9, F.fig(9), "vi"))
    b.append(p(
        "Đầu ra của gage có thể được mô tả theo mô-men lưỡng cực thực trên một đơn vị thể tích. Nếu mô-men "
        "lưỡng cực thực là tổng điện tích Q trên các điện cực nhân với khoảng cách d giữa hai điện cực thì "
        "sự phân cực được cho bởi phương trình 22.30."))
    b.append(eq("P = Q · d / V", "22.30"))
    b.append(p(
        "Từ phương trình 22.30 thấy rằng sự phân cực P (xấp xỉ bằng dịch chuyển điện D) là điện tích trên "
        "một đơn vị diện tích điện cực (Hình 22.10)."))
    b.append(fig(10, F.fig(10), "vi"))
    b.append(p("Khai triển chuỗi Taylor của phương trình 22.30 cho phương trình 22.31."))
    b.append(eq("ΔP = (∂P/∂V)·ΔV + (∂P/∂(Qd))·Δ(Qd)", "22.31"))
    b.append(p(
        "Sau khi lấy vi phân phương trình 22.30 và thay vào, ta được phương trình 22.32."))
    b.append(eq("ΔP = −(P₀/V₀)·ΔV + Δ(Qd)/V₀", "22.32"))
    b.append(p(
        "Với màng PVDF, số hạng thứ hai trong phương trình 22.32 chiếm ưu thế. Đầu ra tỉ lệ với phân cực "
        "dư P₀. Phân cực dư suy giảm chậm theo thời gian, phụ thuộc mạnh vào nhiệt độ, và suy giảm nhanh ở "
        "nhiệt độ khoảng 50 °C. Điều này làm cho độ chính xác thành vấn đề. Nếu cảm biến được giữ ở nhiệt độ "
        "thấp thì có thể duy trì độ chính xác trong khoảng ±3 %."))
    b.append(p(
        "Cảm biến biến dạng cũng có thể được chế tạo từ gốm áp điện như chì zirconat titanat (PZT) hoặc "
        "bari titanat. Gốm giòn và có thể bị khử phân cực bởi biến dạng, nên chỉ nên dùng ở biến dạng nhỏ "
        "hơn 200 microstrain. PZT mất một phần phân cực theo thời gian nên có vấn đề về độ chính xác, nhưng "
        "vẫn giữ phân cực tới nhiệt độ 150 °C hoặc cao hơn. PZT “cứng” (thường pha sắt) là thành phần tốt "
        "nhất về độ ổn định phân cực và độ trễ thấp. Thạch anh có độ chính xác tốt nhất. Nó không phân cực "
        "sẵn mà phân cực được cảm ứng bởi biến dạng. Thạch anh có độ phân giải và độ chính xác tuyệt vời "
        "trên một dải nhiệt độ rộng nhưng bị giới hạn ở mức biến dạng thấp; nó cũng giòn nên chỉ dùng được "
        "với biến dạng nhỏ."))
    b.append(p(
        "Hai mạch thường được dùng để điều kiện tín hiệu áp điện: điện kế và bộ khuếch đại điện tích (Hình "
        "22.11). Trong mạch điện kế, cảm biến áp điện được nối với một tụ điện có điện dung C lớn hơn ít "
        "nhất 1000 lần điện dung C_g của cảm biến. Luôn có một điện trở nào đó trong cáp nối cảm biến với tụ "
        "điện; mạch đơn giản là hai tụ điện mắc song song, nối với nhau bằng một điện trở. Điện tích cân "
        "bằng với hằng số thời gian R_gC_g. Hằng số thời gian này giới hạn thời gian lên nhanh nhất có thể "
        "phân giải vào khoảng 50 ns — với phần lớn ứng dụng là tức thời. Điện tích được đo bằng cách đo điện "
        "áp trên tụ rồi dùng phương trình 22.33."))
    b.append(fig(11, F.fig(11), "vi"))
    b.append(eq("Q = C · V", "22.33"))
    b.append(p(
        "Khó khăn là các dụng cụ đo lại rút điện tích, gây suy giảm theo hằng số thời gian RC. Điều này làm "
        "mất tín hiệu nhanh nếu dùng các khuếch đại thuật toán thông thường. Khuếch đại thuật toán đầu vào "
        "FET có trở kháng vào rất cao và có thể kéo dài hằng số thời gian này tới nhiều giờ. Bộ khuếch đại "
        "điện tích là một mạch khác dùng để đo điện tích; đây thường là một khuếch đại thuật toán đầu vào "
        "FET có tụ hồi tiếp. Mạch này không thực sự khuếch đại điện tích mà tạo ra một điện áp tỉ lệ với "
        "điện tích vào. Một lần nữa, hằng số thời gian có thể tới nhiều giờ, cho phép dùng cảm biến áp điện "
        "cho các phép đo gần tĩnh."))
    b.append(p(
        "Các bộ điều kiện tín hiệu kiểu điện kế và bộ khuếch đại điện tích có trở kháng vào cao, dùng cho "
        "các phép đo gần tĩnh, có bán trên thị trường [20], cùng với các bộ kết cuối điện dung giá rẻ cho "
        "các phép đo tần số cao (từ vài chục kHz đến MHz) [18]. Một ưu điểm của cảm biến áp điện là chúng "
        "là cảm biến chủ động, không cần nguồn năng lượng bên ngoài."))

    # -- fiber optic
    b.append(h3("Gage biến dạng sợi quang", "Fiber Optic Strain Gages"))
    b.append(p(
        "Gage biến dạng sợi quang là những giao thoa kế thu nhỏ [21, 22]. Nhiều cảm biến bán trên thị trường "
        "dựa trên giao thoa kế Fabry–Perot. Giao thoa kế Fabry–Perot đo sự thay đổi kích thước của một "
        "buồng rất nhỏ."))
    b.append(p(
        "Cảm biến biến dạng Fabry–Perot (Hình 22.12) gồm một nguồn sáng laser, các sợi quang đơn mode, một "
        "coupler (tương đương bộ tách chùm trong quang học), một buồng cảm nhận biến dạng và một đầu dò "
        "quang. Ánh sáng rời đi-ốt laser, đi dọc sợi quang, qua coupler và tới buồng. Đầu sợi quang tương "
        "đương một gương tráng bạc một phần: một phần ánh sáng bị phản xạ trở lại dọc sợi, phần còn lại "
        "truyền qua. Ánh sáng truyền qua đi ngang buồng rồi bị phản xạ từ đầu đối diện trở lại vào sợi, nơi "
        "nó tái hợp với chùm phản xạ thứ nhất. Hai chùm có độ lệch pha liên quan tới hai lần chiều dài "
        "buồng. Chùm tái hợp đi qua coupler tới đầu dò quang. Nếu hai chùm phản xạ đồng pha thì có giao "
        "thoa tăng cường; nếu ngược pha thì có giao thoa triệt tiêu. Buồng được dán lên mẫu; khi mẫu bị "
        "biến dạng, buồng giãn ra, làm thay đổi pha của chùm trong buồng và gây ra sự luân phiên giữa giao "
        "thoa tăng cường và triệt tiêu. Với nguồn sáng 1,3 µm, mỗi đỉnh ở đầu ra ứng với độ dịch khe 650 nm. "
        "Lấy độ dịch khe chia cho chiều dài khe ta được biến dạng. Đầu ra là liên tục giữa các đỉnh, nên một "
        "gage dài 3 mm có thể phân giải 1 µstrain."))
    b.append(fig(12, F.fig(12), "vi"))

    # -- birefringent
    b.append(h3("Cảm biến biến dạng dùng màng lưỡng chiết", "Birefringent Film Strain Sensing"))
    b.append(p(
        "Cảm biến biến dạng dùng màng lưỡng chiết cho một phép đo biến dạng toàn trường. Có thể thực hiện "
        "một minh hoạ đẹp về hiệu ứng này bằng hai tấm phim Polaroid rẻ tiền, một thanh Plexiglas "
        "(polymethylmethacrylate — PMMA) dày 6 mm, kích thước 25 mm × 200 mm, và một máy chiếu qua đầu. Đặt "
        "hai tấm Polaroid vuông góc với nhau sao cho ánh sáng bị chặn; đặt thanh PMMA vào giữa hai tấm. Tác "
        "dụng một mô-men uốn lên thanh thì các vân màu sẽ xuất hiện. Vật liệu lưỡng chiết có tốc độ ánh sáng "
        "khác nhau theo các phương khác nhau. Điều này có nghĩa là nếu ánh sáng được phân cực theo một "
        "phương nhất định và đi qua một mẫu lưỡng chiết, thì khi phương nhanh trùng với vectơ điện trường, "
        "ánh sáng đi qua nhanh hơn so với khi phương chậm trùng với vectơ điện trường. Hiệu ứng này có thể "
        "được dùng để tạo giao thoa quang học. Ở một số vật liệu, tính lưỡng chiết được cảm ứng bởi biến "
        "dạng: phương nhanh và phương chậm tương ứng với các phương của biến dạng chính, và độ lớn của "
        "lưỡng chiết tương ứng với độ lớn của biến dạng. Một thành phần của vectơ điện trường đi qua mẫu "
        "nhanh hơn thành phần kia; chúng ló ra với một độ lệch pha, làm thay đổi biên độ tương đối và do đó "
        "quay mặt phẳng phân cực của ánh sáng. Nếu không có lưỡng chiết thì không có ánh sáng nào qua được "
        "bản phân cực thứ hai. Khi lưỡng chiết tăng theo biến dạng, ánh sáng bắt đầu đi qua; khi tăng tiếp "
        "tới mức độ quay mặt phẳng phân cực đủ 180° thì lại không có ánh sáng đi qua. Điều này tạo ra một "
        "vân ứng với một hiệu các biến dạng chính không đổi. Hiệu các biến dạng chính được cho bởi phương "
        "trình 22.34."))
    b.append(eq("ε₁ − ε₂ = N · λ / (t · K)", "22.34"))
    b.append(wl(["trong đó <b>ε₁, ε₂</b> = các biến dạng chính",
                 "<b>N</b> = bậc vân",
                 "<b>λ</b> = bước sóng",
                 "<b>t</b> = chiều dày mẫu",
                 "<b>K</b> = hệ số quang–đàn hồi của vật liệu quang đàn hồi"]))
    b.append(p(
        "Một kỹ thuật tương tự có thể được dùng với một màng nhựa lưỡng chiết có lớp tráng bạc dán lên bề "
        "mặt mẫu. Ánh sáng phân cực đi qua màng, phản xạ từ lớp tráng bạc, đi ngược qua màng và qua bản "
        "phân cực thứ hai. Trong trường hợp này, vì ánh sáng đi qua màng hai lần, phương trình mô tả hiệu "
        "các biến dạng chính là phương trình 22.35."))
    b.append(eq("ε₁ − ε₂ = N · λ / (2 · t · K)", "22.35"))
    b.append(p(
        "Nếu các bản phân cực trùng với các phương của biến dạng chính thì không quan sát thấy lưỡng chiết. "
        "Xoay cả hai bản phân cực cho phép tìm các phương chính tại nhiều vị trí khác nhau trên mẫu thử. "
        "Nếu muốn quan sát toàn bộ trường vân thì dùng các bản 1/4 sóng (Hình 22.13): ánh sáng đi qua bản "
        "phân cực thứ nhất (phân cực phẳng), qua bản 1/4 sóng (phân cực tròn), qua mẫu thử (thay đổi pha), "
        "qua bản 1/4 sóng thứ hai để trở lại phân cực phẳng, rồi qua bản phân cực cuối cùng."))
    b.append(fig(13, F.fig(13), "vi"))
    b.append(p(
        "Các hệ quang học để quan sát lưỡng chiết có bán trên thị trường dưới tên “Polariscope” [23]. Các "
        "linh kiện quang học để tự dựng hệ thống riêng có bán tại nhiều nhà cung cấp linh kiện quang học."))

    # -- moire
    b.append(h3("Cảm biến biến dạng dùng Moiré", "Moiré Strain Sensing"))
    b.append(p(
        "Giao thoa Moiré là một kỹ thuật khác cho phép đo toàn trường, nhưng nó đo dịch chuyển chứ không "
        "đo biến dạng; trường biến dạng phải được tính từ trường dịch chuyển. Kỹ thuật này dựa trên hiện "
        "tượng giao thoa thu được khi hai tấm trong suốt được phủ các vạch cách đều nhau. Nếu đặt hai tấm "
        "chồng lên nhau, có thể căn chỉnh sao cho không có ánh sáng đi qua, hoặc toàn bộ ánh sáng đi qua. "
        "Nếu một trong hai tấm bị kéo giãn thì khoảng cách các vạch trên tấm bị kéo rộng ra. Khi đó, nếu đặt "
        "tấm này lên tấm kia, ở một số vùng ánh sáng sẽ đi qua và ở một số vùng thì không (Hình 22.14). Các "
        "dải sáng tối tạo thành cung cấp thông tin về trường dịch chuyển."))
    b.append(fig(14, F.fig(14), "vi"))
    b.append(p(
        "Moiré được định nghĩa là một loạt các dải sáng tối rộng hình thành do sự chồng chập của hai cách tử "
        "đều [24]. Các vùng tối hoặc sáng được gọi là vân. Hình minh hoạ hai ví dụ: giãn thuần và quay "
        "thuần. Trong cả hai trường hợp, một phần ánh sáng lẽ ra thoát ra khỏi cách tử thứ nhất bị cách tử "
        "chồng lên chặn lại. Tại tâm các vân tối, vạch của cách tử này che khoảng trống của cách tử kia và "
        "không có ánh sáng đi qua; cường độ ló ra I bằng không. Đi từ đó về phía vân tối kế tiếp, mức che "
        "chắn giảm tuyến tính và lượng ánh sáng tăng tuyến tính cho tới khi vạch của cách tử này nằm trên "
        "vạch của cách tử kia; tại đó lượng ánh sáng lớn nhất đi qua hai cách tử."))
    b.append(p(
        "Cả giao thoa hình học và giao thoa quang học đều được dùng. Phần thảo luận này chỉ giới hạn ở giao "
        "thoa hình học. Moiré hình học tận dụng sự giao thoa của hai cách tử để xác định dịch chuyển và góc "
        "quay trong mặt phẳng quan sát. Moiré trong mặt phẳng thường được thực hiện với hai cách tử: một "
        "cách tử gắn lên mẫu (cách tử mẫu) và cách tử kia đặt tiếp xúc với cách tử mẫu (cách tử chuẩn). Khi "
        "mẫu bị biến dạng, các hình giao thoa hay vân xuất hiện. Gọi N là bậc vân moiré; mỗi vân ứng với "
        "một sự tăng hoặc giảm dịch chuyển của mẫu đúng bằng một bước cách tử. Quan hệ giữa dịch chuyển và "
        "vân là δ = gN, trong đó δ là thành phần dịch chuyển vuông góc với các vạch của cách tử chuẩn, g là "
        "bước của cách tử chuẩn và N là bậc vân."))
    b.append(p(
        "Để thuận tiện, người ta quy ước một vân bậc không tại nơi được giả định có dịch chuyển bằng không. "
        "Với cách tử chuẩn đặt ở 0° và 90°, ta thu được các bậc vân N_x và N_y. Khi đó các dịch chuyển theo "
        "phương x và y được cho bởi phương trình 22.36 và 22.37."))
    b.append(eq("u_x(x, y) = g · N_x(x, y)", "22.36"))
    b.append(eq("u_y(x, y) = g · N_y(x, y)", "22.37"))
    b.append(p(
        "Lấy vi phân phương trình 22.36 và 22.37 ta được các biến dạng, phương trình 22.38 đến 22.40."))
    b.append(eq("ε_x = ∂u_x/∂x = g · ∂N_x/∂x", "22.38"))
    b.append(eq("γ_xy = ½( ∂u_x/∂y + ∂u_y/∂x ) = ½( g·∂N_x/∂y + g·∂N_y/∂x )", "22.39"))
    b.append(eq("ε_y = ∂u_y/∂y = g · ∂N_y/∂y", "22.40"))
    b.append(p(
        "Trong phần lớn trường hợp, độ nhạy của moiré hình học không đủ để xác định phân bố biến dạng. Việc "
        "phân tích biến dạng nên được thực hiện bằng phép đo dịch chuyển có độ nhạy cao dùng giao thoa kế "
        "moiré [24, 25]. Giao thoa kế moiré có bán trên thị trường [26]. Phép đo ngoài mặt phẳng có thể được "
        "thực hiện với một cách tử (cách tử chuẩn), cho cách tử chuẩn giao thoa với ảnh phản xạ hoặc bóng "
        "của chính nó [27, 28]."))

    # ---- references
    b.append(h2("Tài liệu tham khảo", "References"))
    refs = [
        "N. E. Dowling, <i>Mechanical Behavior of Materials</i>, Englewood Cliffs, NJ: Prentice-Hall, "
        "1993, 99–108.",
        "R. C. Craig, <i>Mechanics of Materials</i>, New York: John Wiley &amp; Sons, 1996.",
        "A. Vengsarkar, Fiber optic sensors: a comparative evaluation, <i>The Photonics Design and "
        "Applications Handbook</i>, 1991, 114–116.",
        "H. U. Eisenhut, Force measurement on presses with piezoelectric strain transducers and their "
        "static calibration up to 5 MN, <i>New Industrial Applications of the Piezoelectric Measurement "
        "Principle</i>, July 1992, 1–16.",
        "TN-501-4, <i>Strain Gauge Temperature Effects</i>, Measurements Group, Inc., Raleigh, NC 27611.",
        "TN-509, <i>Transverse Sensitivity Errors</i>, Measurements Group, Inc., Raleigh, NC 27611.",
        "TT-609, <i>Soldering Techniques</i>, Measurements Group, Inc., Raleigh, NC 27611.",
        "TN-515, <i>Strain Gage Rosettes</i>, Measurements Group, Inc., Raleigh, NC 27611.",
        "TN-08-1, <i>Fatigue of Strain Gages</i>, Measurements Group, Inc., Raleigh, NC 27611.",
        "C. C. Perry and H. R. Lissner, <i>The Strain Gage Primer</i>, New York: McGraw-Hill, 1962.",
        "J. B. Aidun and Y. M. Gupta, Analysis of Lagrangian gauge measurements of simple and nonsimple "
        "plane waves, <i>J. Appl. Phys.</i>, 69, 6998–7014, 1991.",
        "Y. M. Gupta, Stress measurement using piezoresistance gauges: modeling the gauge as an "
        "elastic-plastic inclusion, <i>J. Appl. Phys.</i>, 54, 6256–6266, 1983.",
        "D. Y. Chen, Y. M. Gupta, and M. H. Miles, Quasistatic experiments to determine material constants "
        "for the piezoresistance foils used in shock wave experiments, <i>J. Appl. Phys.</i>, 55, 3984, "
        "1984.",
        "C. S. Lynch, Strain compensated thin film stress gauges for stress wave measurements in the "
        "presence of lateral strain, <i>Rev. Sci. Instrum.</i>, 66(11), 1–8, 1995.",
        "B-129-7 <i>M-Line Accessories Instruction Bulletin</i>, Measurements Group, Inc., Raleigh, NC "
        "27611.",
        "J. W. Dally, W. F. Riley, and K. G. McConnell, <i>Instrumentation for Engineering Measurements</i>, "
        "2nd ed., New York: John Wiley &amp; Sons, 1993.",
        "J. P. Holman, <i>Heat Transfer</i>, 7th ed., New York: McGraw Hill, 1990.",
        "Dynasen, Inc., 20 Arnold Pl., Goleta, CA 93117.",
        "M. Dean (ed.) and R. D. Douglas (assoc. ed.), <i>Semiconductor and Conventional Strain Gages</i>, "
        "New York: Academic Press, 1962.",
        "Kistler Instruments Corp., Amherst, NY 14228-2171.",
        "J. S. Sirkis, Unified approach to phase strain temperature models for smart structure "
        "interferometric optical fiber sensors. 1. Development, <i>Opt. Eng.</i>, 32(4), 752–761, 1993.",
        "J. S. Sirkis, Unified approach to phase strain temperature models for smart structure "
        "interferometric optical fiber sensors. 2. Applications, <i>Optical Engineering</i>, 32(4), "
        "762–773, 1993.",
        "Photoelastic Division, Measurements Group, Inc., P.O. Box 27777, Raleigh, NC 27611.",
        "T. Valis, D. Hogg, and R. M. Measures, Composite material embedded fiber-optic Fabry–Perot strain "
        "rosette, <i>SPIE</i>, 1370, 154–161, 1990.",
        "D. Post, B. Han, and P. Lfju, <i>High Sensitivity Moiré</i>, New York: Springer-Verlag, 1994.",
        "V. J. Parks, Geometric Moiré, <i>Handbook on Experimental Mechanics</i>, A. S. Kobayashi, Ed., VCH "
        "Publisher, Inc., 1993.",
        "Photomechanics, Inc., 512 Princeton Dr., Vestal, NY 13850-2912.",
        "T. Y. Kao and F. P. Chiang, Family of grating techniques of slope and curvature measurements for "
        "static and dynamic flexure of plates, <i>Opt. Eng.</i>, 21, 721–742, 1982.",
        "D. R. Andrews, Shadow moiré contouring of impact craters, <i>Opt. Eng.</i>, 21, 650–654, 1982.",
    ]
    b.append('<ol class="refs">' + "".join("<li>%s</li>" % r for r in refs) + "</ol>")

    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chương 21</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Nội dung sách</a></div>'
             % (BASE_VI, PREV_VI, PREV_T_VI, BASE_VI))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "Stress and strain describe loads on and deformations of solid materials. Homogeneous means the "
        "properties are the same everywhere; isotropic means they are independent of direction — an annealed "
        "steel bar is both, a human femur is neither. For a long bar under a tensile load, stress is force "
        "divided by cross-sectional area and strain is length change divided by original length; the bar "
        "elongates longitudinally (ε_L) and contracts transversely (ε_t). In the linear range the ratio of "
        "stress to strain is the Young's modulus E and the negative ratio of transverse to longitudinal "
        "strain is the Poisson's ratio ν. A tangential force per unit area is the shear stress τ, whose "
        "distortion is the shear strain γ; their ratio is the shear modulus G. Temperature change gives "
        "thermal strain, whose ratio to temperature change is the expansion coefficient α."))
    b.append(h2("22.1 Fundamental Definitions of Strain", "Các định nghĩa cơ bản về biến dạng"))
    b.append(fig(1, F.fig(1), "en"))
    b.append(fig(2, F.fig(2), "en"))
    b.append(fig(3, F.fig(3), "en"))
    b.append(p(
        "Principal directions undergo elongation but no shear; at least two always exist on any surface. "
        "Where they are unknown — near a hole or notch, in an anisotropic specimen, or in a complicated "
        "structure — extra gages are needed. Elastic and thermal properties combine into Hooke's law, "
        "Equations 22.1–22.6."))
    b.append(fig(4, F.fig(4), "en"))
    b.append(p(
        "Sensor families are piezoresistive (foil, wire and semiconductor), piezoelectric (PVDF and quartz), "
        "fiber optic, birefringent film and Moiré grids; each needs its own signal conditioning. Selection "
        "depends on geometry, temperature, strain rate, frequency, magnitude, cost, complexity, accuracy, "
        "spatial and time resolution, transverse and temperature sensitivity, and conditioning complexity. "
        "Table 22.1 compares typical characteristics of several sensors. Table 22.2 lists a number of "
        "suppliers together with approximate prices for sensors and the accompanying signal conditioning "
        "electronics."))
    b.append(table(
        ["Description", "Longitudinal strain sensitivity", "Transverse strain sensitivity",
         "Temperature sensitivity", "Strain resolution", "Spatial resolution", "Time resolution",
         "Measurable strain range"],
        [["Piezoresistive constantan foil", "ΔR/R per Δε_L = 2.1", "ΔR/R per Δε_t &lt; 0.02",
          "ΔR/R per ΔT = 2 × 10⁻⁶/°C", "&lt; 1 µstrain ᵃ", "5–100 mm ᵇ", "&lt; 1 µs ᶜ", "0–3%"],
         ["Annealed constantan foil ᵈ", "2.1", "&lt; 0.02", "2 × 10⁻⁶/°C", "&lt; 11 µstrain",
          "5–100 mm", "&lt; 1 µs", "0–10%"],
         ["Piezoresistive semiconductor", "150", "???", "1.7 × 10⁻³/°C", "&lt; 0.1 µstrain", "1–15 mm",
          "&lt; 1 µs", "0–0.1%"],
         ["Piezoelectric PVDF", "120 nC/m²/µε", "60 nC/m²/µε", "−27 µC/m²/°C", "1–10 µstrain",
          "gage size", "&lt; 1 µs", "0–30%"],
         ["Piezoelectric quartz bonded to steel", "150 nC/m²/µε", "—", "0", "&lt; 0.01 µstrain",
          "20 mm gage", "&lt; 10 µs", "0–0.1%"],
         ["Fiber optic Fabry–Perot", "2 to 1000 µstrain/V", "near zero", "—", "&lt; 1 µstrain",
          "2–10 mm", "&lt; 20 µs", "—"],
         ["Birefringent film", "Kε = 0.15–0.002", "—", "—", "—", "0.5 mm ᶠ", "&lt; 5 µs", "0.05–5%"],
         ["Moiré", "1 fringe order / 417 nm displacement", "1 fringe order / 417 nm", "undefined",
          "41.7 µε over 10 mm", "full field ᵍ", "limited by electronics", "0.005–5%"]],
        "Table 22.1 · Comparison of strain sensor types (after the original). "
        "ᵃ With good signal conditioning. ᵇ By grid area. ᶜ Gage response within 100 ns; most signal "
        "conditioning electronics limit the response time to much less. ᵈ Annealed foil has a low yield "
        "strength and a large strain to failure; it also exhibits hysteresis on unloading and zero shift "
        "under cyclic loading. ᵉ This technique measures the difference of principal strains: "
        "ε₂ − ε₁ = Nλ/2tK. ᶠ Approximately the film thickness. ᵍ Spatial strain resolution depends on the "
        "strain level; this is a displacement measurement technique."))
    b.append(p(
        "The data in Table 22.1 are illustrative only and are by no means complete. The sensor descriptions "
        "name only the sensor type, not the many different sizes and shapes available. Longitudinal strain "
        "sensitivity is given as the sensor output per unit longitudinal strain along the sensor axis. If "
        "the signal conditioning is included, every sensitivity can be expressed as volts per unit strain "
        "[3, 4], but that value depends on the gain and quality of the conditioner. Temperature sensitivity "
        "is given as the output change caused by a temperature change. In many cases a higher strain "
        "resolution can be reached, but resolving smaller strains is harder and may need vibration and "
        "thermal isolation. With the Moiré technique the strain resolution is a function of the observed "
        "gauge length: the technique resolves 100 nm of displacement (1/4 fringe order), and dividing that "
        "by the observed length gives the strain resolution. Spatial resolution corresponds to the gage "
        "length for most sensor types. The measurable strain range listed is the upper limit of each sensor "
        "type; accuracy and reliability usually degrade when a sensor is used near the top of its range."))
    b.append(table(
        ["Vendor", "Sensor type", "Sensor price", "Signal conditioner price"],
        [["Micro Measurements (Raleigh, NC)", "Piezoresistive foil; birefringent film",
          "from $5.00; from $10.00",
          "Wheatstone bridge: from $500; polariscope: $5,000–10,000"],
         ["Texas Measurements (College Station, TX)", "Piezoresistive foil and wire; load cells",
          "from $5.00", "—"],
         ["Omega Engineering (Stamford, CT)", "Piezoresistive foil", "from $5.00",
          "Strain indicator: from $550; Wheatstone bridge: from $2,700"],
         ["Dynasen (Goleta, CA)",
          "Piezoresistive foil; gages for shock-wave measurement; calibrated piezoelectric PVDF",
          "from $55.00; from $55.00",
          "2-channel pulsed Wheatstone bridge: $5,000; passive charge integrator: $250.00"],
         ["Entran Sensors and Electronics (Fairfield, NJ)", "Piezoresistive semiconductor",
          "from $15.00", "—"],
         ["Amp Inc. Piezo Film Sensors (Valley Forge, PA)", "Piezoelectric PVDF (uncalibrated)",
          "from $5.00", "—"],
         ["Kistler Instrument Corp. (Amherst, NY)", "Piezoelectric quartz", "—",
          "Electrometer; charge amplifier"],
         ["F&amp;S Inc., Fiber and Sensor Technologies (Blacksburg, VA)",
          "Fabry–Perot strain sensors", "from $75", "Electronics: from $3,500.00"],
         ["Photomechanics (Vestal, NY)", "Moiré interferometer", "$60,000", "—"]],
        "Table 22.2 · Sources and prices for strain sensors. Prices are 1999 list prices (USD) in the "
        "original; full postal addresses have been omitted, keeping only city and state."))
    b.append(h2("22.2 Principles of Operation of Strain Sensors", "Nguyên lý hoạt động"))
    b.append(p(
        "Piezoresistive foil gages (Figure 22.5) are a polyimide substrate, a constantan foil grid, lead "
        "wires and often a polyimide encapsulation. The grid runs in one direction so that strain stretches "
        "the legs lengthwise; transverse strain merely separates them, so the gage is sensitive only along "
        "its length, with almost no shear sensitivity. The resistance change follows ΔR/R = Gε (Eq. 22.7), "
        "and with temperature and transverse terms, Eq. 22.8. Self-temperature compensation (STC) cancels "
        "thermal output by choosing a material whose thermal response is offset by the specimen's thermal "
        "expansion; manufacturers quote STC numbers matched to common specimen materials."))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p(
        "For one rectangular leg (Figure 22.6) R = ρL/A (Eq. 22.9). A first-order Taylor expansion (Eq. "
        "22.10) gives Eq. 22.11, where the relative change comes from resistivity, length strain and area "
        "strain. Because the metal behaves as a fibre in a polymer matrix, the stress state is uniaxial, so "
        "area strain is the sum of width and thickness strain (Eq. 22.12) and equals −2νΔL/L₀ (Eq. 22.13), "
        "giving Eq. 22.14. The elastic gage factor for constantan comes out just over 2. Under plastic "
        "deformation resistivity change is negligible, Poisson's ratio becomes 0.5 and the factor is 2 — "
        "annealed foil exploits this to measure beyond 10% strain, at the cost of hysteresis on unloading."))
    b.append(fig(6, F.fig(6), "en"))
    b.append(p(
        "Gages come with various backings (polyimide, glass-fibre reinforced phenolic), open-faced or "
        "encapsulated, with solder tabs or attached leads, and in rosettes. Bonding follows a step-by-step "
        "procedure: degrease; abrade with fine emery or 400-grit paper; draw (do not scribe) layout lines; "
        "clean with isopropyl alcohol using one-pass wipes; neutralise to pH 7–7.5; then apply the gage with "
        "cellophane tape, quick-set glue and catalyst, never touching it with bare fingers. The tape lifts "
        "the gage, positions it, is peeled back from one side, catalyst is applied, a drop of glue is placed "
        "at the tape/specimen joint, and the tape is wiped down at about 30° to drive the glue line forward; "
        "press for about a minute, peel the tape back and attach the leads."))
    b.append(p(
        "The relative resistance change is measured with a Wheatstone bridge (Figure 22.7), which reads a "
        "small change against an initial zero rather than against a large resistance. One to four arms may "
        "be gages; paths ABC and ADC are dividers, so V_B and V_D follow Eqs. 22.15a and 22.15b, the output "
        "is Eq. 22.16 and balance is Eq. 22.17. With small changes the first-order output is Eq. 22.18. "
        "Thermal drift cancels directly if R₁ is bonded to the specimen and R₂ is held on it with heat-sink "
        "compound: R₁ sees strain plus temperature, R₂ only temperature, and the bridge subtracts them."))
    b.append(fig(7, F.fig(7), "en"))
    b.append(p(
        "Sensitivity is proportional to bridge voltage, but the dissipated power P = I²R must be conducted "
        "away or the gage heats and its resistance drifts. Heat-sinking scales with the specimen's thermal "
        "conductivity; a reasonable allowable gradient is 40 °C per metre (about 1 °C per 25 mm). For "
        "roughly equal arms, P = V_in²/4R (Eq. 22.19), and equating power density to K∇T gives Eqs. 22.20 "
        "and 22.21. A 0.010 m × 0.010 m 120 Ω grid on thick aluminium (K = 204 W m⁻¹ °C⁻¹) allows 19 V; "
        "thin specimens allow less, and smaller gages force lower excitation. Pulsing the bridge for a short "
        "duration cuts the energy dissipated and raises sensitivity 10–100 times; commercial pulse supplies "
        "offer widths from 10 µs at 350 V."))
    b.append(p(
        "Where principal directions are unknown, three gages at three angles form a rosette. The common "
        "0–45–90° pattern gives directions x, x′ and y against principal directions 1 and 2 at angle θ; "
        "Mohr's circle (Figure 22.8) is drawn with elongational strain horizontal and shear strain vertical, "
        "centre C and radius R. Principal values are Eqs. 22.22–22.23, the centre Eq. 22.24, the gage "
        "outputs Eqs. 22.25–22.27, and division gives θ and R via Eqs. 22.28–22.29."))
    b.append(fig(8, F.fig(8), "en"))
    b.append(p(
        "Semiconductor piezoresistive gages work the same way with a gage factor nearly an order of "
        "magnitude larger, but the resistance–temperature coupling is very large — a small temperature "
        "change can shift resistance an order of magnitude more than strain — so they must be temperature "
        "compensated. They are used mainly in transducers such as load cells, are fragile and need great "
        "care in application."))
    b.append(p(
        "Piezoelectric gages are parallel-plate capacitors whose dielectric repolarizes under strain, "
        "producing charge on the electrodes. PVDF (Figure 22.9) is cheap but inaccurate and depoles at "
        "moderate temperature; it suits dynamic measurements such as frequency and logarithmic decrement, "
        "not quantitative strain. Quasistatic use drains charge through the instrument, decaying the signal "
        "with a time constant set by input impedance; quartz is very accurate but also loses charge, though "
        "electrometers and charge amplifiers give time constants from seconds to hours. Polarization is "
        "P = Qd/V (Eq. 22.30), i.e. charge per unit electrode area (Figure 22.10); the Taylor expansion "
        "(Eqs. 22.31–22.32) shows PVDF is dominated by the second term and proportional to remanent "
        "polarization, which decays with time, depends strongly on temperature and falls rapidly near 50 °C "
        "— accuracy within ±3% is possible only if the sensor is kept cool. PZT ceramics are brittle and "
        "depole above 200 microstrain, keep polarization to 150 °C or more, with iron-doped \"hard\" PZT "
        "best for stability; quartz is the most accurate, non-polar but strain-polarized, and limited to "
        "small strain."))
    b.append(fig(9, F.fig(9), "en"))
    b.append(fig(10, F.fig(10), "en"))
    b.append(p(
        "Two conditioning circuits dominate (Figure 22.11). The electrometer drives a capacitor C at least "
        "1000 times C_g through a cable resistance, equilibrating with time constant R_gC_g — about 50 ns "
        "risetime — and charge follows from Q = CV (Eq. 22.33). Because instruments drain charge with time "
        "constant RC, FET-input op amps extend it to many hours. The charge amplifier is an FET-input op amp "
        "with capacitive feedback; it does not amplify charge but produces a voltage proportional to it, "
        "again with a time constant of hours, enabling near-static use. High-impedance conditioners and "
        "low-cost capacitive terminators for high-frequency work are both available, and piezoelectric "
        "sensors are active — they need no external energy source."))
    b.append(fig(11, F.fig(11), "en"))
    b.append(p(
        "Fiber optic gages are miniature interferometers, most commercially as Fabry–Perot cavities (Figure "
        "22.12): laser, single-mode fiber, coupler, sensing cavity and photodetector. Light partly reflects "
        "at the fiber end and partly crosses the cavity to reflect from the far end; the recombined beams "
        "interfere according to twice the cavity length. Straining the specimen stretches the cavity, "
        "cycling constructive and destructive interference — for a 1.3 µm source each peak is a 650 nm gap "
        "change, and a 3 mm gage resolves 1 µstrain."))
    b.append(fig(12, F.fig(12), "en"))
    b.append(p(
        "Birefringent film sensing gives a full-field measurement. Two crossed Polaroid sheets with a PMMA "
        "bar between them show colour fringes under bending: birefringent materials carry light at different "
        "speeds in different directions, so a polarized beam emerges with a phase difference that rotates "
        "its polarization, and the analyzer transmits or blocks accordingly. Fast and slow directions are "
        "the principal strain directions and the amount of birefringence tracks strain magnitude, giving "
        "fringes of constant principal-strain difference, Eq. 22.34; with a silvered backing the light "
        "traverses the film twice, giving Eq. 22.35. Quarter-wave plates (Figure 22.13) give a full view of "
        "the fringe field, and commercial systems are sold as polariscopes."))
    b.append(fig(13, F.fig(13), "en"))
    b.append(p(
        "Moiré gives a full field but measures displacement, from which strain must be differentiated. Two "
        "equally spaced gratings superposed either block or pass light; stretching one changes its pitch so "
        "some regions pass light and some do not (Figure 22.14). Fringes of order N correspond to a "
        "displacement of one grating pitch, δ = gN. With reference gratings at 0° and 90°, displacements "
        "follow Eqs. 22.36–22.37 and strains Eqs. 22.38–22.40. Geometric moiré is usually not sensitive "
        "enough for strain distributions, so moiré interferometry is used instead, and out-of-plane "
        "measurement uses a single grating interfering with its reflection or shadow."))
    b.append(fig(14, F.fig(14), "en"))
    b.append(p("The chapter closes with 29 references, reproduced in the Vietnamese version above."))
    b.append('<div class="chapter-nav">'
             '<a href="%s%s/"><span class="k">← Chapter 21</span>%s</a>'
             '<a href="%s" style="text-align:right;"><span class="k">All chapters →</span>Book contents</a></div>'
             % (BASE_EN, PREV_EN, PREV_T_EN, BASE_EN))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 22 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 22 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 22 “Đo biến dạng” của Christopher S. Lynch (Georgia Institute of "
            "Technology) — định nghĩa ứng suất và biến dạng, định luật Hooke, gage lá và dây áp điện trở, "
            "cầu Wheatstone, bộ ba gage và vòng tròn Mohr, gage bán dẫn, gage áp điện, gage sợi quang "
            "Fabry–Perot, màng lưỡng chiết và moiré, với 14 hình, 2 bảng và 40 phương trình." if vi
            else
            "Companion to Chapter 22 of the CRC Measurement Handbook — strain measurement: stress and "
            "strain, Hooke's law, foil and semiconductor gages, the Wheatstone bridge, rosettes, "
            "piezoelectric, fiber optic, birefringent and Moiré techniques.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 22' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 22' % BASE_EN)
    meta = ("Chương 22 · theo Ch22.pdf (CRC Press, 1999) · 14 hình, 2 bảng, 40 phương trình, "
            "29 tài liệu tham khảo" if vi
            else "Chapter 22 · 14 figures, 2 tables, 40 equations, 29 references")
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
