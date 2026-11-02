# -*- coding: utf-8 -*-
"""Handbook Chapter 91 — Cathode Ray Tube Displays (Christopher J. Sherman).

Writes the full Vietnamese translation and the English companion.
Figures: hb91fig.py (91.1, 91.2). No numbered equations in this chapter.
Run:  python build/reader_hb_ch91.py
"""
import os

import hb91fig as F91
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch91-cathode-ray-tube-displays"
TITLE_EN = "Cathode Ray Tube Displays"
TITLE_VI = "Hiển thị ống tia điện tử"
BYLINE = "Christopher J. Sherman"
BYLINE_EN = "Christopher J. Sherman"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG

FIGS = {1: F91.fig_91_1, 2: F91.fig_91_2}


def fig(num, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = FIGS[num]()
    return ('<figure class="figure" id="fig-91-%d">%s<figcaption class="figcap">%s</figcaption>'
            '</figure>' % (num, svg, cap_vi if lang == "vi" else cap_en))


def p(t):
    return "<p>%s</p>" % t


def h2(t, en=""):
    return '<h2>%s%s</h2>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h3(t, en=""):
    return '<h3>%s%s</h3>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def note(t):
    return '<div class="note">%s</div>' % t


def refs(items):
    return '<ol class="ref-list">%s</ol>' % "".join("<li>%s</li>" % i for i in items)


def table(hd, rows, cap, cls="", style="", nw=(), colw=()):
    # `tbl-wrap` is the class the stylesheet actually styles (overflow-x:auto);
    # `table-wrap` is kept for the other chapters' markup.
    def cell(tag, i, c):
        st = ' style="white-space:nowrap"' if i in nw else ""
        return "<%s%s>%s</%s>" % (tag, st, c, tag)

    body = "".join("<tr>%s</tr>" % "".join(cell("td", i, c) for i, c in enumerate(r))
                   for r in rows)
    head = "".join(cell("th", i, h) for i, h in enumerate(hd))
    colg = ""
    if colw:
        colg = "<colgroup>%s</colgroup>" % "".join('<col style="width:%dpx">' % w for w in colw)
    return ('<div class="table-wrap"><table class="tbl%s"%s>%s<thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % (cls, (' style="%s"' % style) if style else "", colg, head, body, cap))


# ================================================================ TABLES
# Table 91.1 — five parameter groups, the entries exactly as printed.
_T91_1_VI = [
    ("Độ phân giải",
     "Kích thước và hình dạng đốm sáng<br>Độ chính xác hội tụ<br>Độ rộng dòng<br>"
     "Định dạng địa chỉ hoá/quét<br>Thiết kế lưới chắn"),
    ("Độ chói",
     "Dải động<br>Độ sáng cực đại<br>Thang độ xám trong ánh sáng môi trường cao và thấp<br>"
     "Thang độ xám so với độ sáng màn hình<br>Hiệu suất phát sáng của huỳnh quang"),
    ("Độ tương phản",
     "Độ tương phản dưới chiếu sáng môi trường cao<br>Độ tương phản dưới chiếu sáng môi "
     "trường thấp<br>Độ tương phản vùng lớn<br>Độ tương phản điểm ảnh-điểm ảnh (vùng nhỏ)"),
    ("Độ trung thực hình ảnh",
     "Tốc độ khung hình<br>Nhấp nháy/làm tươi<br>Độ đồng đều và tính tuyến tính<br>"
     "Quang sai (tuyến tính, méo gối, méo thùng, méo hình thang và hội tụ)"),
    ("Màu",
     "Chọn huỳnh quang<br>Độ chính xác hội tụ<br>Gam màu và độ bão hoà<br>"
     "Độ đồng đều màu<br>Độ chính xác màu"),
    ("Băng thông",
     "Băng thông video (thiết kế catôt)<br>Thiết kế lệch ngang<br>Thiết kế lệch dọc<br>"
     "Băng thông của điện tử hỗ trợ CRT<br>Băng thông của điện tử phân phối tín hiệu"),
]

_T91_1_EN = [
    ("Resolution",
     "Spot size and shape<br>Focus accuracy<br>Line width<br>Addressing/scan format<br>"
     "Shadow mask design"),
    ("Luminance",
     "Dynamic range<br>Maximum brightness<br>Gray scale in high and low ambient light<br>"
     "Gray scale vs. display brightness<br>Phosphor luminous efficiency"),
    ("Contrast",
     "Contrast under high ambient illumination<br>Contrast under low ambient illumination<br>"
     "Large area contrast<br>Pixel-to-pixel contrast (small area)"),
    ("Image fidelity",
     "Frame rate<br>Flicker/refresh<br>Uniformity and linearity<br>Aberrations (linearity, "
     "pincushion, barrel distortion, keystone, and focus)"),
    ("Color",
     "Phosphor selection<br>Convergence accuracy<br>Color gamut and saturation<br>"
     "Color uniformity<br>Color accuracy"),
    ("Bandwidth",
     "Video bandwidth (cathode design)<br>Horizontal deflection design<br>Vertical deflection "
     "design<br>Bandwidth of the CRT supporting electronics<br>Bandwidth of the signal delivery "
     "electronics"),
]

# Table 91.2 — nineteen advantages against five weaknesses; the shorter column
# is padded so the two read down the same rows.
_ADV_VI = [
    "Công nghệ có độ phân giải cao nhất",
    "Định dạng địa chỉ hoá linh hoạt",
    "Độ trung thực hình ảnh xuất sắc",
    "Tốc độ cao",
    "Băng thông (≥ 350 MHz)",
    "Độ tương phản/thang độ xám xuất sắc",
    "Nhiều lựa chọn huỳnh quang tốt",
    "Hiệu suất phát sáng cao",
    "Màn hình sáng (đến 20.000 fL)",
    "Gam màu xuất sắc",
    "Giao diện đơn giản",
    "Tiêu chuẩn giao diện phổ quát",
    "Linh hoạt trong thiết kế",
    "Nền tảng ứng dụng rộng",
    "Tuổi thọ và độ tin cậy cao",
    "Nền tảng kiến thức chín muồi và rộng",
    "Nguồn cung ống và linh kiện toàn cầu",
    "Rẻ — chi phí thấp trên mỗi phần tử phân giải",
]

_ADV_EN = [
    "Highest resolution technology",
    "Versatile addressing formats",
    "Excellent image fidelity",
    "High speed",
    "Bandwidth (≥ 350 MHz)",
    "Excellent contrast/gray scale",
    "Good selection of phosphors",
    "High luminous efficiency",
    "Bright display (up to 20,000 fL)",
    "Excellent color gamut",
    "Simplicity of interface",
    "Universal interface standards",
    "Good design flexibility",
    "Broad application base",
    "Long life and reliability",
    "Mature and broad knowledge base",
    "Worldwide sources of tubes and parts",
    "Inexpensive — low cost per resolution element",
]

_DIS_VI = [
    "Tiêu thụ công suất cao",
    "Trọng lượng thuỷ tinh",
    "Kích thước dấu chân",
    "Phát bức xạ điện từ",
    "Phải làm tươi",
]

_DIS_EN = [
    "High power consumption",
    "Weight of glass",
    "Size of footprint",
    "Emits EM radiation",
    "Must be refreshed",
]

# Table 91.3 — fourteen suppliers, addresses exactly as printed. The source's
# two-column layout was flattened by the text extractor; the halves have been
# re-paired from the printed page (the "U.S. address" block at 25358 Avenue
# Stanford belongs to Rank Brimar, not to Sony).
_T91_3 = [
    ("Clinton Electronics Corporation",
     "6701 Clinton Road<br>Rockford, Illinois 61111<br>"
     "Tel. 815-633-1444 Fax. 815-633-8712"),
    ("Hitachi, Ltd.",
     "New Marunouchi Bldg.<br>Marunouchi 1-chrome<br>Chiyoda-ku, Tyoko 100, Japan<br>"
     "Tel. 81-3-3212-1111 Fax. 81-3-3212-3857"
     "<div class='addr-sub'>Địa chỉ Hoa Kỳ</div>"
     "Hitachi America, Ltd., Electron Tube Division<br>3850 Holcomb Bridge Road, Suite 300<br>"
     "Norcross, Georgia 30092-2202<br>Tel. 770-409-3000 Fax. 770-409-3028"),
    ("Hughes Lexington, Inc.",
     "A subsidiary of Hughes Electronics Company<br>1501 Newtown Pike<br>"
     "Lexington, Kentucky 40511<br>Tel. 606-243-5500 Fax. 606-243-5555"),
    ("Image Systems Corporation",
     "11595 K-tel Drive<br>Hopkins, Minnesota 55343<br>"
     "Tel. 612-935-1171 Fax 612-935-1386"),
    ("Imaging &amp; Sensing Technology Corporation",
     "300 Westinghouse Circle<br>Horseheads, New York 14845-2299<br>"
     "Tel. 607-796-4400 Fax. 607-796-4482"),
    ("ITPO Institute of Surface Engineering and Optoelectronics",
     "Teslova 30<br>1000 Ljubljana, Slovenia<br>"
     "Tel. 386-61 1264 592/111 Fax. 386-61 1264 593"),
    ("L. G. Electronics",
     "20 Yoido-dong Youngdungpo-gu<br>Seoul, Korea<br>"
     "E-mail: display2@www.goldstar.co.kr<br>monitor@www.goldstar.co.kr"
     "<div class='addr-sub'>Địa chỉ Hoa Kỳ</div>"
     "L G Electronics, Monitors Division<br>1000 Silvan Avenue<br>"
     "Englewood Cliffs, New Jersey 07632<br>Tel. 201-816-2000 Fax. 201-816-2188"),
    ("Matsushita Electric Industrial Ltd.",
     "Twin 21 National Tower<br>1-61, Shiromi, 2-Chome, Chuo-ku,<br>Osaka 540, Japan<br>"
     "Tel. (06)908-1121"
     "<div class='addr-sub'>Địa chỉ Hoa Kỳ</div>"
     "Panasonic Industrial Company<br>Computers and Communications Division<br>"
     "2 Panasonic Way<br>Secaucus, New Jersey 07094<br>"
     "Tel. 201-392-4502 Fax. 201-392-4441"),
    ("Phillips Netherlands, BV",
     "Phillips Components and Semiconductors<br>Bldg. VB Postbus 90050<br>"
     "5600 PB Eindhoven The Netherlands<br>Tel. 040-783749 Fax. 040-788399"
     "<div class='addr-sub'>Địa chỉ Hoa Kỳ</div>"
     "Discrete Products Division<br>2001 West Blue Heron Blvd.<br>"
     "Riviera Beach, Florida 33404<br>"
     "Tel. 407-881-3200 hoặc 800-447-3762 Fax. 407-881-3300"),
    ("Rank Brimar, Ltd.",
     "Greenside Way<br>Middleton, Manchester M24 1SN, England<br>"
     "Tel. 0161-681 7072 Fax. 0161-682-3818"
     "<div class='addr-sub'>Địa chỉ Hoa Kỳ</div>"
     "25358 Avenue Stanford<br>Valencia, California 91355-1214<br>"
     "Tel. 805-295-5770 Fax. 805-295-5087"),
    ("Sony Corporation",
     "Display Systems<br>16550 Via Esprillo<br>San Diego, California 92127<br>"
     "Tel. 619-487-8500"),
    ("Thomas Electronics",
     "100 Riverview Drive<br>Wayne, New Jersey 07470<br>"
     "Tel. 201-696-5200 Fax. 201-696-8298"),
    ("Thomson Tubes Electronics",
     "13, avenue Morane Saulnier<br>Bâtiment Chavez – Vélizy Espace<br>"
     "BP 121/F-78148 VELIZY CEDEX France<br>Tel. 33-1 30 70 35 00 Fax. 33-1 30 70 35 35"
     "<div class='addr-sub'>Địa chỉ Hoa Kỳ</div>"
     "Thompson Components and Tubes Corporation<br>40 G Commerce Way<br>"
     "Totowa, New Jersey 07511<br>Tel. 201-812-9000 Fax. 201-812-9050"),
    ("Toshiba Corporation",
     "Electronic Components, Cathode Ray Tube Division<br>1-1 Shibaura 1-Chrome, Minato-KU<br>"
     "Tokyo 105, Japan<br>Tel. 03-457-3480 Fax. 03-456-1286"
     "<div class='addr-sub'>Địa chỉ Hoa Kỳ</div>"
     "Toshiba America, Inc.<br>1220 Midas Way<br>Sunnyvale, California 94086-4020<br>"
     "Tel. 408-737-9844"),
]

# ================================================================ REFERENCES
_REFS = [
    "G. Aboud, <i>Cathode Ray Tubes, 1997</i>, 2nd ed., San Jose, CA, Stanford Resources, 1997.",
    "G. Aboud, <i>Cathode Ray Tubes, 1997</i>, Internet excerpts, available "
    "http://www.stanfordresources.com/sr/crt/crt.html, Stanford Resources, February 1998.",
    "G. Shires, Ferdinand Braun and the cathode ray tube, <i>Sci. Am.</i>, 230 (3): 92–101, "
    "March 1974.",
    "N.H. Lehrer, The challenge of the cathode-ray tube, in L.E. Tannas, Jr., Ed., <i>Flat Panel "
    "Displays and CRTs</i>, New York: Van Nostrand Reinhold, 1985.",
    "P. Keller, <i>The Cathode-Ray Tube, Technology, History, and Applications</i>, New York: "
    "Palisades Press, 1991.",
    "D.C. Ketchum, CRT's: the continuing evolution, Society for Information Display "
    "International Symposium, Conference Seminar M-3, 1996.",
    "L.R. Falce, CRT dispenser cathodes using molybdenum rhenium emitter surfaces, Society for "
    "Information Display International Symposium Digest of Technical Papers, 23: 331–333, 1992.",
    "J.H. Lee, J.I. Jang, B.D. Ko, G.Y. Jung, W.H. Kim, K. Takechi, and H. Nakanishi, Dispenser "
    "cathodes for HDTV, Society for Information Display International Symposium Digest of "
    "Technical Papers, 27: 445–448, 1996.",
    "T. Nakadaira, T. Kodama, Y. Hara, and M. Santoku, Temperature and cutoff stabilization of "
    "impregnated cathodes, Society for Information Display International Symposium Digest of "
    "Technical Papers, 27: 811–814, 1996.",
    "W. Kohl, <i>Materials Technology for Electron Tubes</i>, New York, Reinhold Publishing, 1951.",
    "S. Sugawara, J. Kimiya, E. Kamohara, and K. Fukuda, A new dynamic-focus electron gun for "
    "color CRTs with tri-quadrupole electron lens, Society for Information Display International "
    "Symposium Digest of Technical Papers, 26: 103–106, 1995.",
    "J. Kimiya, S. Sugawara, T. Hasegawa, and H. Mori, A 22.5 mm neck color CRT electron gun with "
    "simplified dynamically activated quadrupole lens, Society for Information Display "
    "International Symposium Digest of Technical Papers, 27: 795–798, 1996.",
    "D. Imabayashi, M. Santoku, and J. Karasawa, New pre-focus system structure for the trinitron "
    "gun, Society for Information Display International Symposium Digest of Technical Papers, "
    "27: 807–810, 1996.",
    "K. Kato, T. Sase, K. Sasaki, and M. Chiba, A high-resolution CRT monitor using built-in "
    "ultrasonic motors for focus adjustment, Society for Information Display International "
    "Symposium Digest of Technical Papers, 27: 63–66, 1996.",
    "S. Sherr, <i>Electronic Displays</i>, 2nd ed., New York: John Wiley, 1993.",
    "N. Azzi and O. Masson, Design of an NIS pin/coma-free 108° self-converging yoke for CRTs "
    "with super-flat faceplates, Society for Information Display International Symposium Digest "
    "of Technical Papers, 26: 183–186, 1995.",
    "J.F. Fisher and R.G. Clapp, Waveforms and spectra of composite video signals, in K. Benson "
    "and J. Whitaker, <i>Television Engineering Handbook, Featuring HDTV Systems</i>, New York: "
    "McGraw-Hill Reinhold, 1992.",
    "D. Pritchard, Standards and recommended practices, in K. Benson and J. Whitaker, "
    "<i>Television Engineering Handbook, Featuring HDTV Systems</i>, New York: McGraw-Hill "
    "Reinhold, 1992.",
    "A. Vecht, Phosphors for color emissive displays, Society for Information Display "
    "International Symposium Conference Seminar Notes F-2, 1995.",
    "<i>Optical Characteristics of Cathode Ray Tube Screens</i>, EIA publication TEP116-C, "
    "Feb., 1993.",
    "G. Wyszecki and W.S. Stiles, <i>Color Science: Concepts and Methods, Quantitative Data and "
    "Formulae</i>, 2nd ed., New York: John Wiley &amp; Sons, 1982.",
    "A. Robertson and J. Fisher, Color vision, representation, and reproduction, in K. Benson and "
    "J. Whitaker, <i>Television Engineering Handbook, Featuring HDTV Systems</i>, New York: "
    "McGraw-Hill Reinhold, 1992.",
    "M. Maeda, Trinitron technology: current status and future trends, Society for Information "
    "Display International Symposium Digest of Technical Papers, 27: 867–870, 1996.",
    "C. Sherman, Field sequential color takes another step, <i>Inf. Display</i>, 11 (3): 12–15, "
    "March, 1995.",
    "L. Ozawa, Helmet mounted 0.5 in. crt for SVGA images, Society for Information Display "
    "International Symposium Digest of Technical Papers, 26: 95–98, 1995.",
    "C. Infante, CRT display measurements and quality, Society for Information Display "
    "International Symposium Conference Seminar Notes M-3, 1995.",
    "J. Whitaker, <i>Electronic Displays, Technology, Design, and Applications</i>, New York: "
    "McGraw-Hill, 1994.",
    "P. Keller, <i>Electronic Display Measurement, Concepts, Techniques, and Instrumentation</i>, "
    "New York: John Wiley &amp; Sons, 1997.",
]

_FURTHER = [
    "L. Ozawa, <i>Cathodoluminescence: Theory and Applications</i>, New York: Kodansha, 1990.",
    "V.K. Zworykin and G.A. Morton, <i>Television: The Electronics of Image Transmission in Color "
    "and Monochrome</i>, New York: John Wiley &amp; Sons, 1954.",
    "B. Wandell, The foundations of color measurement and color perception, Society for "
    "Information Display International Symposium, Conference Seminar M-1, 1993. Một phần giới "
    "thiệu ngắn gọn và dễ chịu về khoa học màu (31 trang).",
    "<b>Electronic Industries Association (EIA)</b>, 2500 Wilson Blvd., Arlington, VA 22201 "
    "(Internet: www.eia.org). Hiệp hội Công nghiệp Điện tử duy trì một bộ sưu tập hơn 1000 ấn "
    "phẩm kỹ thuật và tiêu chuẩn hiện hành. EIA là một nguồn xuất sắc về thông tin kỹ thuật CRT, "
    "tiêu chuẩn, huỳnh quang, an toàn, thông tin thị trường và điện tử nói chung.",
    "<b>The Society for Information Display (SID)</b>, 1526 Brookhollow Dr., Suite 82, Santa Ana, "
    "CA 92705-5421 (Internet: www.display.org). Hiệp hội Hiển thị Thông tin là một nguồn tốt về "
    "thông tin nghiên cứu và phát triển kỹ thuật về CRT và công nghệ hiển thị thông tin nói chung.",
]

_WEB = [
    ("The Society for Information Display", "www.display.org"),
    ("The Society of Motion Picture and Television Engineers", "www.smpte.org"),
    ("The Institute of Electrical and Electronics Engineers", "www.ieee.org"),
    ("The Electronic Industries Association", "www.eia.org"),
    ("National Information Display Laboratory", "www.nta.org"),
    ("The International Society for Optical Engineering", "www.spie.org"),
    ("The Optical Society of America", "www.osa.org"),
    ("Electronics &amp; Electrical Engineering Laboratory", "www.eeel.nist.gov"),
    ("National Institute of Standards and Technology (NIST)", "www.nist.gov"),
    ("The Federal Communications Commission", "www.fcc.gov"),
]


def _tbl91_1(rows, cap):
    return table(["Nhóm tham số", "Các tham số ảnh hưởng"], rows, cap,
                 colw=(150, 510))


def _tbl91_2(adv, dis, cap):
    n = max(len(adv), len(dis))
    rows = [(adv[i] if i < len(adv) else "", dis[i] if i < len(dis) else "")
            for i in range(n)]
    return table(["Ưu điểm", "Nhược điểm"], rows, cap, colw=(330, 330))


def _tbl91_3(rows, cap):
    return table(["Công ty", "Địa chỉ"], rows, cap, colw=(180, 480))


def _web_list(items):
    return ('<ul class="web-list">%s</ul>'
            % "".join("<li>%s — <span class=\"url\">%s</span></li>" % (a, b)
                      for a, b in items))


# ================================================================ VIETNAMESE
def body_vi():
    b = []
    b.append(note(
        "<b>Ghi chú của người dịch.</b> Bản gốc in năm 1999 có một số lỗi ký tự do quá trình "
        "chế bản, được giữ nguyên ở đây và ghi lại như sau. Ký hiệu <b>£</b> thực chất là dấu "
        "<b>≤</b> (nhỏ hơn hoặc bằng) và ký hiệu <b>³</b> thực chất là <b>≥</b> (lớn hơn hoặc "
        "bằng). Các số mũ bị mất dấu trừ và dấu trên: “1.3 ´ 10–4 Pa (10–6 torr)” phải đọc là "
        "1,3 × 10<sup>−4</sup> Pa (10<sup>−6</sup> torr), và “0.1 to 10 A/cm2” là A/cm². Chữ "
        "“21/2” là hỗn số 2½. Các chỉ số dưới trong công thức hoá học bị mất: Zn(Cd)S:Cu:Al, "
        "Y₂O₂S:Eu. Trong mục 91.8, bản gốc in “£25 mm”, “£15 mm”, “£150 mm” và “£250 mm”; đây "
        "phải là <b>µm</b> chứ không phải mm — một đốm sáng 25 mm là bất khả thi trên một ống "
        "12 mm — nên bản dịch ghi là µm. Tên “Standford Resources” ở mục 91.1 là lỗi chính tả "
        "của <i>Stanford Resources</i> (đúng như trong tài liệu tham khảo 1–2); “electromagnetic "
        "yolks” ở mục 91.3 là <i>yokes</i>; “whether of not” ở mục 91.10 là <i>whether or not</i>. "
        "Ở mục 91.6, câu “both require precise beam control” thiếu chủ ngữ — “both” ở đây chỉ hai "
        "cấu hình delta và thẳng hàng vừa nêu. Trong Bảng 91.3, bản gốc in “Phillips” (tên công "
        "ty là Philips), “1-chrome” (đúng là 1-chome), “Tyoko” (đúng là Tokyo) và “Minato-KU”; "
        "các địa chỉ được giữ nguyên như đã in."))

    b.append(h2("Giới thiệu", "Introduction"))
    b.append(p(
        "Ống phóng tia điện tử (CRT) không có đối thủ về khả năng tạo ra hình ảnh động, chất "
        "lượng cao và giàu thông tin ở độ phân giải cao. Ấn tượng hơn nữa là nó đạt được điều đó "
        "với chi phí trên mỗi điểm ảnh thấp hơn bất kỳ công nghệ hiển thị điện tử tương đương nào "
        "khác. Đối với nhà thiết kế thiết bị đo cần một màn hình giàu thông tin, CRT mang lại rất "
        "nhiều ưu điểm."))
    b.append(p(
        "Là một ống hiển thị thuần, CRT thường có sẵn như một mặt hàng mua ngay, với cơ sở hạ "
        "tầng rộng khắp gồm nhà cung cấp, đơn vị tích hợp, dịch vụ hỗ trợ và nhà cung ứng linh "
        "kiện. Các tiêu chuẩn giao diện đã được thiết lập vững chắc, và như một hệ thống hoàn "
        "chỉnh sẵn sàng nhận đầu vào tín hiệu chuẩn, CRT có mặt trên toàn thế giới với nhiều dải "
        "hiệu năng khác nhau. Để đáp ứng các yêu cầu ứng dụng khác nhau, CRT có kích thước đường "
        "chéo từ 12 mm đến hơn 1 m, với độ phân giải từ hàng nghìn điểm ảnh đến hơn 5 triệu điểm "
        "ảnh mỗi khung hình. Đặc tính của ống được cải thiện hằng năm và giá thì tiếp tục giảm."))
    b.append(p(
        "Stanford Resources đã theo dõi thị trường CRT gần 20 năm và là một nguồn thông tin xuất "
        "sắc. Trong báo cáo mới nhất, công ty cho biết bất chấp cạnh tranh từ các công nghệ hiển "
        "thị khác, CRT vẫn sẽ là thị trường đơn lẻ lớn nhất trong ngành hiển thị. Thị trường ống "
        "CRT toàn cầu năm 1997 đạt 261 triệu chiếc, trị giá 26 tỉ USD. Dự kiến con số này sẽ "
        "tăng lên 341 triệu chiếc, trị giá hơn 34 tỉ USD vào năm 2003 [1, 2]. Dù có nhiều công "
        "nghệ hiển thị thông tin cạnh tranh, CRT vẫn sẽ đồng hành cùng chúng ta suốt thế kỷ 21."))

    b.append(h2("Lịch sử", "History"))
    b.append(p(
        "CRT có một lịch sử phong phú và lâu đời. Cội nguồn của công nghệ CRT ngày nay trải dài "
        "hơn 100 năm, về nửa sau thế kỷ 19. Eugene Goldstein là người đầu tiên đưa ra thuật ngữ "
        "tia catôt; John W. Hittorf, Heinrich Geissler, Julius Plücker và những người khác đã có "
        "những đóng góp quan trọng riêng cho công nghệ CRT [3]. Suốt thế kỷ 19, các nhà nghiên "
        "cứu quan tâm đến bản chất của phóng điện khí phát sáng và những tia mờ xuất hiện khi "
        "đặt một hiệu điện thế cao giữa hai điện cực trong chân không. Sir William Crookes là "
        "một nhà thực nghiệm tích cực trong lĩnh vực này, và những thiết bị tia catôt thời kỳ "
        "đầu được gọi là ống Crookes. Crookes nhận thấy rằng ánh sáng phát ra từ bề mặt mà các "
        "tia đập vào chứ không phải từ bản thân các tia. Bằng cách chế tạo những ống có độ chân "
        "không 1,3 × 10<sup>−4</sup> Pa (10<sup>−6</sup> torr), ông đã loại bỏ được phóng điện "
        "khí phát sáng và làm việc trực tiếp với các tia catôt [4]. Crookes đã chứng minh những "
        "điều sau: độ chói phụ thuộc trực tiếp vào tính chất vật liệu của bề mặt mà các tia đập "
        "vào; từ trường làm lệch đường đi của các tia; độ lệch tỉ lệ với cường độ từ trường; và "
        "từ trường có thể được dùng để hội tụ các tia thành một chùm. Ông cũng cho rằng các tia "
        "phát ra từ catôt là một dòng hạt nhỏ mang điện, mà ít lâu sau Joseph John Thomson đã "
        "nhận diện là êlectron. Các thí nghiệm CRT tiếp nối đã dẫn đến việc Wilhelm Konrad "
        "Röntgen phát hiện tia X năm 1895."))
    b.append(p(
        "Ferdinand Braun là người đầu tiên hình dung CRT như một công cụ hiển thị thông tin và "
        "thường được ghi nhận là người phát minh ra thiết bị đầu tiên trực tiếp đi trước CRT "
        "hiện đại [5]. Năm 1896 Braun thiết kế một CRT “ống chỉ thị” để theo dõi tần số cao "
        "trong các thiết bị phát điện. Thiết kế của ông chứa đựng tất cả các phần tử giống như "
        "CRT ngày nay. Nó dùng một catôt làm nguồn êlectron, hai cuộn điều khiển để lệch dọc và "
        "lệch ngang, một anôt để gia tốc êlectron và điều khiển chùm tia, và một khe hội tụ. "
        "Ông cũng tích hợp một màn huỳnh quang vuông góc với chùm tia để vạch lại đường đi của "
        "nó. Tuy thô sơ so với tiêu chuẩn sau này, đây chính là nguyên mẫu trực tiếp của dao "
        "động ký CRT."))
    b.append(p(
        "Năm 1903 đến 1905, Arthur Wehnelt bổ sung nhiều tiến bộ rất quan trọng cho thiết kế của "
        "Braun. Wehnelt đã phát triển và đưa vào sử dụng catôt ôxít nóng và một lưới điều khiển "
        "chùm tia [5]. Điều này làm giảm điện áp cần thiết để tạo dòng êlectron và cho phép điều "
        "khiển dòng chùm tia tinh tế hơn nhiều. Những phát triển này là tiền thân của súng điện "
        "tử hiện đại."))
    b.append(p(
        "CRT chủ yếu vẫn là một thiết bị phòng thí nghiệm cho đến khi ba ứng dụng quan trọng đưa "
        "nó lên vị trí trung tâm của ngành hiển thị thông tin: dao động ký, truyền hình và radar "
        "quân sự. Đến đầu những năm 1900, dao động ký đã được dùng rộng rãi để nghiên cứu các "
        "mạch điện biến thiên theo thời gian trong thông tin liên lạc. Truyền hình được phát "
        "triển vào những năm 1920 và tháng 7 năm 1930, Công ty Phát thanh Quốc gia (NBC) bắt đầu "
        "phát sóng truyền hình thử nghiệm tại thành phố New York. Trong Thế chiến thứ hai, CRT "
        "trải qua làn sóng trưởng thành thứ hai nhờ sự ra đời của công nghệ radar. Đến cuối "
        "những năm 1940, CRT truyền hình đã có mặt như một sản phẩm tiêu dùng. Vào những năm "
        "1950, RCA hoàn thiện công nghệ lưới chắn, và chẳng bao lâu màu sắc trở thành một tiêu "
        "chuẩn mới, được người tiêu dùng rộng rãi chấp nhận trong những năm 1960. Trong khi các "
        "thành phần chính của một hệ CRT về cơ bản không thay đổi suốt nhiều thập kỷ, CRT vẫn "
        "tiếp tục được cải tiến."))

    b.append(h2("Tạo ảnh bằng CRT", "Image Formation with a CRT"))
    b.append(p(
        "Mặc dù có nhiều thiết kế CRT khác nhau, có loại khá phức tạp, quá trình tạo ảnh bằng "
        "CRT lại đơn giản. Quá trình có thể chia thành bốn giai đoạn cơ bản: tạo chùm tia, hội "
        "tụ chùm tia, làm lệch chùm tia và biến đổi năng lượng. Bốn giai đoạn này diễn ra ở bốn "
        "vùng khác nhau của ống, theo thứ tự từ phía sau ống (cổ ống) ra tới mặt trước. Như trên "
        "Hình 91.1, các phần tử ở phía sau ống được gọi chung là súng điện tử."))
    b.append(fig(1))

    b.append(h3("Tạo chùm tia bằng súng điện tử", "Beam Generation with the Electron Gun"))
    b.append(p(
        "Catôt tạo ra dòng êlectron dùng để tạo chùm tia ghi ảnh. Catôt truyền thống là một dây "
        "dẫn kim loại như niken, phủ một lớp ôxít mỏng, thường là một hợp chất bari-stronti. Để "
        "giảm điện áp cần thiết cho việc phát xạ êlectron, catôt được nung nóng đến 700 đến "
        "1200 °C. Những ứng dụng đòi hỏi độ sáng cao thường dùng các thiết kế catôt dispenser "
        "tiên tiến và đắt tiền hơn để tăng dòng chùm tia trong khi vẫn duy trì tuổi thọ catôt "
        "hợp lý. Những thiết kế này sử dụng các cấu trúc và vật liệu catôt phức tạp như gốm "
        "bari, molypden, rheni và wolfram. Bạn đọc quan tâm đến các thiết kế catôt tiên tiến và "
        "thông tin thêm về công nghệ vật liệu CRT nên tham khảo Tài liệu 6 đến 10. Dòng êlectron "
        "từ catôt được điều khiển bằng cách thay đổi điện thế giữa catôt và một loạt lưới điều "
        "khiển thường được gọi là G1 (lưới điều khiển) và G2 (lưới gia tốc). Một điện thế 100 "
        "đến 1000 V giữa G2 và catôt tạo ra điện thế cần thiết để hút một dòng êlectron ra khỏi "
        "catôt, hình thành chùm tia. Biên độ chùm tia có thể được điều khiển và thậm chí ngắt "
        "hoàn toàn bằng cách thay đổi điện thế trên G1. Như vậy, điện áp trên G1 điều khiển độ "
        "sáng, vì độ sáng tỉ lệ với dòng chùm tia. Thiết kế catôt về mặt trở kháng và tải ảnh "
        "hưởng đến tốc độ điều biến chùm tia tối đa. Catôt và các lưới điều khiển kèm theo có "
        "thể được thiết kế để tạo ra dòng êlectron hội tụ chéo (crossover) hoặc dòng phân lớp "
        "(laminar). Trong thiết kế súng crossover, các êlectron phát xạ hội tụ về một điểm phía "
        "trước catôt. Nhờ quang học êlectron, đốm chùm tia này được tạo ảnh lên màn huỳnh quang. "
        "Nhờ những ưu điểm vốn có, thiết kế crossover được dùng rộng rãi. Chùm tia crossover "
        "hẹp, nên dễ làm lệch hơn chùm tia dày, và đốm sáng có thể rất nhỏ, cải thiện độ phân "
        "giải trên màn hình. Về lý thuyết, thiết kế dòng phân lớp cho khả năng có dòng chùm tia "
        "cao hơn từ một catôt cùng kích thước. Trên thực tế, cải thiện này thường không đủ bù "
        "cho khó khăn tăng thêm khi điều khiển một chùm tia rộng hơn."))

    b.append(h3("Hội tụ chùm tia điện tử", "Electron Beam Focusing"))
    b.append(p(
        "Hội tụ chùm tia và dòng chùm tia là yếu tố quyết định kích thước đốm sáng cuối cùng, và "
        "do đó quyết định độ phân giải của CRT. Hội tụ một chùm êlectron hoàn toàn tương tự như "
        "hội tụ một chùm ánh sáng; ngành học này được gọi là quang học êlectron. Những mối quan "
        "tâm quen thuộc với tạo ảnh quang học như độ phóng đại, quang sai cầu và loạn thị cũng "
        "xuất hiện trong quang học êlectron. Khi CRT trở nên lớn hơn và hoạt động ở góc lệch lớn "
        "hơn, việc kiểm soát đốm sáng trở nên tới hạn. Hội tụ chùm tia đạt được bằng lưới hội tụ "
        "tĩnh điện hoặc cuộn hội tụ điện từ. Hội tụ tĩnh điện là kỹ thuật được dùng rộng rãi "
        "nhất. Nó có mặt trong các ứng dụng từ truyền hình đến màn hình máy tính để bàn. Hội tụ "
        "tĩnh điện đạt được bằng cách đặt một chuỗi điện thế lên một dãy lưới hội tụ phức tạp "
        "được chế tạo trong súng điện tử. Khi các nhà thiết kế tìm cách cải thiện hiệu năng hơn "
        "nữa, các thiết kế lưới trở nên tinh xảo [11, 12]. Hội tụ từ là hệ thống được chọn cho "
        "mọi hệ hiệu năng cao, nơi độ phân giải và độ sáng là mục tiêu thiết kế. Thấu kính từ "
        "tạo đốm sáng nhỏ với ít quang sai hơn. Các cuộn dây ngoài trong một yoke quanh cổ ống "
        "điều khiển chùm tia. Vì cho hiệu năng vượt trội, hội tụ điện từ phổ biến trên các hệ "
        "thương mại độ phân giải cao. Hội tụ từ cũng có thể đạt được bằng nam châm vĩnh cửu và "
        "các linh kiện hội tụ lai tĩnh điện/từ chuyên dụng. Do tác động to lớn của hội tụ lên độ "
        "phân giải, các nhà cung cấp ống tiếp tục cải thiện điều khiển hội tụ [13, 14]. Để có "
        "một trình bày xuất sắc và toàn diện về vật lý êlectron trong CRT, điều khiển chùm tia, "
        "các thảo luận thiết kế chi tiết và các khía cạnh khác của thiết bị CRT, hãy tham khảo "
        "sách giáo khoa của Sol Sherr [15]."))

    b.append(h3("Làm lệch chùm tia điện tử", "Electron Beam Deflection"))
    b.append(p(
        "Hệ làm lệch chùm tia chịu trách nhiệm điều khiển vị trí đốm sáng trên mặt trước của "
        "CRT. Cũng như hội tụ, kỹ thuật làm lệch chùm tia có thể là điện từ hoặc tĩnh điện. Một "
        "hệ làm lệch từ gồm hai yoke điện từ ở hai phía đối diện của cổ CRT: một cuộn lệch ngang "
        "và một cuộn lệch dọc. Vị trí của chùm tia được điều khiển dễ dàng; độ lệch của chùm tia "
        "tỉ lệ trực tiếp với dòng điện trong cuộn dây. Thiết kế cuộn lệch cũng ảnh hưởng đến "
        "kích thước và hình dạng đốm sáng. Các thiết kế cuộn có thể tích hợp hiệu chỉnh cho quang "
        "sai coma, sai số hội tụ và méo hình gối [16]. Nhờ chi phí thấp và hiệu quả, CRT cho cả "
        "ứng dụng độ phân giải vừa và cao thường dùng làm lệch từ. Làm lệch tĩnh điện cho dịch "
        "chuyển chùm tia nhanh hơn nhưng kiểm soát kích thước đốm sáng kém hơn. Nó thường được "
        "dùng trong các hệ dao động ký, nơi yêu cầu độ phân giải vừa phải và tốc độ lệch là "
        "quan trọng nhất."))

    b.append(h2("Địa chỉ hoá CRT: quét mành so với quét nét",
                "CRT Addressing: Raster Scanning vs. Stroke"))
    b.append(p(
        "Quét mành là kỹ thuật địa chỉ hoá CRT phổ biến nhất. Trong quét mành, chùm êlectron ghi "
        "từng khung hình theo từng dòng một. Điều này có nghĩa là hệ lệch ngang cần băng thông "
        "cao hơn hệ lệch dọc. Các CRT quét mành hiệu năng cao có băng thông ngang 15 đến "
        "150 kHz và băng thông lệch dọc 30 đến 180 Hz. Thông tin được ghi lên mặt trước CRT từ "
        "trái sang phải và từ trên xuống dưới, từng dòng một. Quét mành có thể là xen kẽ hoặc "
        "tuần tự (không xen kẽ). Trong quét xen kẽ, mỗi khung hình thông tin được phân rã thành "
        "hai trường. Trường thứ nhất gồm tất cả các dòng đánh số lẻ trong khung hình gốc, và "
        "trường thứ hai chứa tất cả các dòng đánh số chẵn. Mỗi trường được quét lên CRT với tốc "
        "độ gấp đôi tốc độ khung hình. Truyền hình thương mại dùng quét xen kẽ. Ở Hoa Kỳ, tốc độ "
        "khung hình là 30 Hz và tốc độ trường là 60 Hz; sơ đồ này được gọi là tiêu chuẩn NTSC. "
        "PAL và SECAM là hai định dạng thương mại nổi tiếng khác đang được dùng. Có rất nhiều "
        "tiêu chuẩn khác, cả tương tự lẫn số, đang được dùng trên toàn thế giới, mỗi tiêu chuẩn "
        "có tốc độ quét, định dạng độ phân giải/địa chỉ hoá, mã hoá độ chói và màu, và giao thức "
        "định thời hơi khác nhau [17, 18]. Quét xen kẽ là một thoả hiệp kỹ thuật nhằm tiết kiệm "
        "băng thông truyền dẫn, băng thông điện tử và băng thông CRT, trong khi vẫn duy trì hiệu "
        "năng chấp nhận được về hình ảnh động, độ phân giải và nhấp nháy. Màn hình máy tính dùng "
        "quét mành tuần tự. Mỗi khung hình chỉ có một trường. Hình ảnh được tạo từng dòng theo "
        "thứ tự từ điểm ảnh đầu tiên đến điểm ảnh cuối cùng. Tốc độ khung hình của màn hình để "
        "bàn điển hình thay đổi từ 60 đến 85 Hz, đến hơn 180 Hz với các hệ chuyên dụng."))
    b.append(p(
        "Quét nét là một kỹ thuật địa chỉ hoá thay thế từng khá phổ biến. Tên của kỹ thuật này "
        "bắt nguồn từ thành ngữ “nét bút”. Quét nét là một hệ địa chỉ hoá điểm-tới-điểm. Chùm "
        "tia được hướng đến điểm đầu của một đoạn thẳng, bật lên, rồi được di chuyển trực tiếp "
        "đến cuối đoạn thẳng. Vì không có các dòng quét mành, độ phân giải của CRT quét nét độc "
        "lập với hướng và chủ yếu bị giới hạn bởi kích thước đốm sáng. Địa chỉ hoá quét nét rất "
        "phù hợp cho các màn hình ít thông tin với các ký tự đồ hoạ chi tiết hoặc đồ hoạ vector "
        "đơn giản. Nó cho chất lượng vẽ rất cao, đường nét sạch, chi tiết chính xác và tốc độ "
        "cao trong khi tiết kiệm công suất và băng thông. Hệ quét nét chỉ địa chỉ hoá CRT ở nơi "
        "có thông tin, chứ không phải toàn bộ màn hình như trong quét mành. Kỹ thuật này ngày "
        "nay ít phổ biến vì quá chậm và đòi hỏi tính toán nhiều đối với các hệ có hàm lượng "
        "thông tin cao, thang độ xám hoặc hình ảnh."))

    b.append(h2("Màn huỳnh quang", "The Phosphor Screen"))
    b.append(p(
        "Huỳnh quang đóng vai trò bộ biến đổi của CRT. Nó chuyển năng lượng của chùm êlectron "
        "thành ánh sáng. Quá trình biến đổi này được gọi là phát quang catôt. Huỳnh quang CRT là "
        "những vật liệu tinh thể vô cơ được pha tạp một hoặc nhiều tạp chất gọi là chất hoạt hoá "
        "và chất đồng hoạt hoá. Huỳnh quang phát sáng theo hai cách: huỳnh quang và lân quang. "
        "Huỳnh quang là sự phát sáng của vật liệu huỳnh quang trong khi nó đang bị chùm êlectron "
        "bắn phá. Sự tiếp tục phát sáng sau khi bắn phá đã ngừng được gọi là lân quang. Khoảng "
        "thời gian lân quang kéo dài được gọi là độ dư sáng. Độ dư sáng có thể thay đổi từ vài "
        "chục nanogiây đến nhiều phút, thậm chí nhiều giờ. CRT tận dụng cả hai hình thức phát "
        "quang catôt. Tóm lại, phát quang catôt xảy ra khi chùm êlectron kích thích các êlectron "
        "của huỳnh quang lên những trạng thái năng lượng cao hơn, không bền, có sẵn nhờ sự có "
        "mặt của các chất hoạt hoá. Khi các êlectron trở về trạng thái bền, ánh sáng được phát "
        "ra. Việc chọn huỳnh quang phụ thuộc vào yêu cầu của ứng dụng về đặc trưng bước sóng "
        "(phổ phát xạ hẹp hay phổ rộng), màu, độ sáng, độ phân giải và độ dư sáng. CRT truyền "
        "hình thương mại thường dùng các bột huỳnh quang sau: ZnS:Ag:Cl (xanh dương), "
        "Zn(Cd)S:Cu:Al hoặc ZnS:Cu:Au:Al (xanh lục), và Y₂O₂S:Eu (đỏ) [19]. CRT truyền hình dùng "
        "huỳnh quang có độ dư sáng ngắn vừa phải. Điều này bảo đảm khung hình mới không bị nhoè "
        "do khung hình trước. Theo truyền thống, huỳnh quang cho màn hình radar, nơi màn hình "
        "được làm tươi không thường xuyên, có sự pha trộn giữa độ dư sáng ngắn và dài. Tuy "
        "nhiên, với sự ra đời của các hệ số ngày nay, việc dùng huỳnh quang có độ dư sáng dài đã "
        "giảm. Hiệp hội Công nghiệp Điện tử duy trì một cơ sở dữ liệu thông tin về huỳnh quang "
        "thương mại cho CRT. Bạn đọc quan tâm nên tham khảo ấn phẩm TEP116-C của hiệp hội [20]. "
        "Hình 91.2 minh hoạ đặc trưng phổ của vài loại huỳnh quang tiêu biểu."))
    b.append(fig(2))

    b.append(h2("CRT màu dùng lưới chắn", "Color CRTs Using Shadow Masks"))
    b.append(p(
        "Màu sắc đã là một phần của thế giới CRT từ đầu những năm 1950. Hiểu biết vững chắc về "
        "cảm nhận màu của người là quan trọng để hiểu chi tiết về màu trong CRT. Bạn đọc quan tâm "
        "đến một trình bày toàn diện xuất sắc về khoa học màu nên tham khảo Wyszecki và Stiles "
        "[21], hoặc Robertson và Fisher [22] để có tổng quan ngắn gọn. Phương pháp phổ biến nhất "
        "để đưa màu vào CRT là kỹ thuật lưới chắn ba súng. Lưới chắn là một lưới kim loại gồm "
        "nhiều khẩu độ nhỏ, được giữ cố định ngay trước màn huỳnh quang. Màn huỳnh quang là một "
        "mảng gồm ba loại điểm ảnh con huỳnh quang khác nhau. Ba súng êlectron được đặt sát nhau "
        "trong cổ ống, mỗi súng cho một trong ba màu cơ bản (đỏ, lục, xanh dương). Các súng tạo "
        "một góc nhỏ so với nhau. Lưới chắn và các chùm tia được căn chỉnh sao cho mỗi chùm rơi "
        "đúng vào điểm huỳnh quang thích hợp. Các điểm được đặt sát nhau để mắt tích hợp không "
        "gian các điểm ảnh con thành một hỗn hợp màu liên tục. Có hai cấu hình phổ biến: delta và "
        "thẳng hàng. Delta, phương pháp truyền thống, sắp xếp các súng êlectron và các điểm "
        "huỳnh quang thành một bộ ba. Điều này đòi hỏi một lưới chắn gồm lưới các khẩu độ tròn. "
        "Gần đây hơn, Sony giới thiệu thiết kế Trinitron™. Trong ống Trinitron, các súng được đặt "
        "thẳng hàng, lưới chắn gồm các khe dọc, và huỳnh quang ở dạng sọc dọc. Thiết kế này cho "
        "độ phân giải dọc tốt hơn và dễ hội tụ hơn, nhưng lưới hơi khó đỡ hơn và dễ gặp vấn đề "
        "ứng suất nhiệt. Trinitron tiếp tục là một thiết kế quan trọng và phổ biến [23]. Kỹ thuật "
        "lưới chắn để tạo ảnh màu có ba nhược điểm chính. Thứ nhất, lưới chắn thường hấp thụ hơn "
        "75% năng lượng chùm êlectron, làm giới hạn độ sáng và gây ra các hiệu ứng nhiệt không "
        "mong muốn. Thứ hai, cả hai cấu hình vừa nêu đều đòi hỏi điều khiển chùm tia chính xác "
        "để hội tụ ba hình ảnh khác nhau từ các súng êlectron. Thứ ba, độ phân giải của màn hình "
        "bị giới hạn bởi yêu cầu về màu không gian: cần ba điểm ảnh con để tạo nên mỗi điểm ảnh "
        "đủ màu."))

    b.append(h2("Các kỹ thuật thay thế để tạo màu bằng CRT",
                "Alternative Techniques for Realizing Color Using CRTs"))
    b.append(p(
        "Có những cách tiếp cận khác để tạo màu bằng CRT. Theo cách riêng của mình, mỗi cách tìm "
        "cách cải thiện một hoặc nhiều khía cạnh của những thiết kế lưới chắn cực kỳ thành công. "
        "Ba đối thủ đáng chú ý nhất là ống chỉ số chùm tia, ống huỳnh quang xuyên lớp và hệ màu "
        "tuần tự trường. Cả ba đã tồn tại hàng thập kỷ, nhưng chỉ hệ màu tuần tự trường là có "
        "mặt trên thị trường thương mại."))

    b.append(h3("Thiết kế ống chỉ số chùm tia và ống huỳnh quang xuyên lớp",
                "Beam Index and Penetration Phosphor Tube Designs"))
    b.append(p(
        "Ống chỉ số chùm tia dùng một lưới có khe và các sọc huỳnh quang dọc. Một chùm êlectron "
        "được hội tụ đến nhỏ hơn chiều rộng của một sọc huỳnh quang. Một tín hiệu tử ngoại phản "
        "xạ từ lưới cung cấp tín hiệu phản hồi. Tín hiệu này được dùng để đánh chỉ số vị trí của "
        "chùm tia rất chính xác. Việc chọn màu đạt được nhờ định vị chùm tia chính xác và điều "
        "biến chùm tia nhanh. Mặc dù đánh chỉ số chùm tia mang lại hội tụ hoàn hảo, ít súng, tiết "
        "kiệm năng lượng và độ phân giải cao, những vấn đề thực tiễn trong điều khiển và chế tạo "
        "đã khiến cách tiếp cận này không thành hiện thực. Ống xuyên lớp thậm chí có tiềm năng ưu "
        "việt hơn vì màu được tạo ra chỉ với một súng êlectron và không cần lưới chắn. Màn huỳnh "
        "quang gồm nhiều lớp huỳnh quang khác nhau xếp chồng. Có nhiều cách tiếp cận cấu trúc "
        "lớp, nhưng nguyên lý cơ bản là mỗi lớp tạo ra một màu khác nhau. Để chọn giữa các màu "
        "khác nhau, năng lượng chùm tia được thay đổi, làm thay đổi độ xuyên lớp của nó. Về lý "
        "thuyết, có thể dùng nhiều lớp huỳnh quang để tạo ra một màn hình đủ màu. Đáng tiếc, "
        "thiết kế này đòi hỏi điện áp chuyển mạch cao, và độ tinh khiết màu kém vì bị pha loãng "
        "do rò rỉ từ các lớp huỳnh quang không được chọn. Trước đây, một vài hệ hai màu đã được "
        "sản xuất ở quy mô hạn chế với các hệ ghi nét (tr. 147 của Tài liệu 4)."))

    b.append(h3("Màu tuần tự trường", "Field Sequential Color"))
    b.append(p(
        "Màu tuần tự trường (FSC) là một cách tiếp cận khác để tạo màu bằng một CRT đơn sắc và "
        "các bộ lọc màu [24]. Lưới chắn dựa vào khả năng của mắt trong việc tích hợp không gian "
        "một nhóm phần tử màu. Màu tuần tự trường khai thác khả năng của mắt trong việc tích hợp "
        "thời gian các trường màu. Màu tuần tự trường không phải là một khái niệm mới; nó từng là "
        "một gợi ý thiết kế ban đầu cho truyền hình màu thương mại. Để thực hiện màu tuần tự "
        "trường, mỗi khung hình đủ màu được phân rã thành các trường màu cơ bản (đỏ, lục, xanh "
        "dương). Mỗi trường màu này được hiển thị tuần tự trên một CRT đơn sắc, đồng thời một bộ "
        "lọc màu được đặt trước mặt CRT. Các bộ lọc phải được thay đổi nhanh chóng để giữ đồng bộ "
        "với từng trường, vốn được hiển thị với tốc độ gấp ba lần tốc độ khung hình mong muốn. "
        "Chuỗi này nhanh đến mức mắt hợp nhất các trường màu riêng lẻ thành một hỗn hợp màu liên "
        "tục ổn định. Hệ màu tuần tự trường có tất cả ưu điểm của một CRT đơn sắc, cụ thể là độ "
        "phân giải và sự đơn giản vượt trội. Những nhược điểm lịch sử chính của màu tuần tự "
        "trường là khó điều khiển một bánh lọc cơ khí cồng kềnh, quay, và hai phần ba năng lượng "
        "ánh sáng của huỳnh quang bị bỏ đi trong mỗi trường. Trước đây, một số người xem cho biết "
        "có thể nhận ra các trường màu riêng lẻ một cách gián đoạn; hiện tượng này được gọi là "
        "“vỡ màu”. Hệ màu tuần tự trường đã có một sự hồi sinh thương mại nhờ nhiều yếu tố. Hiệu "
        "suất phát sáng của một số huỳnh quang đã cải thiện đến mức tổn thất ánh sáng không còn "
        "là cái giá quá đắt. Những bánh lọc cơ khí vụng về đã được thay bằng nhiều loại màn trập "
        "tinh thể lỏng nhỏ gọn, công suất thấp. Việc dùng tốc độ khung hình nhanh hơn và kỹ thuật "
        "lấy mẫu số đã làm giảm các hiện tượng màu giả. Và cuối cùng, CRT đơn sắc dùng màu tuần "
        "tự trường đáp ứng nhu cầu thị trường đang tăng về các màn hình nhỏ, độ phân giải cao."))

    b.append(h2("Chất lượng hình ảnh và hiệu năng", "Image Quality and Performance"))
    b.append(p(
        "Với bất kỳ công nghệ hiển thị nào, phép thử cuối cùng về hiệu năng và chất lượng là "
        "hình ảnh trông thế nào với người xem trong một môi trường thực tế. Điều này mang tính "
        "chủ quan cao, nhưng dù sao cũng tới hạn. Bảng 91.1 nêu bật một số tham số quan trọng "
        "gắn với hiệu năng và chất lượng hình ảnh."))
    b.append(_tbl91_1(
        _T91_1_VI,
        "Bảng 91.1 · Các tham số ảnh hưởng đến hiệu năng và chất lượng hình ảnh của CRT."))
    b.append(p(
        "Độ phân giải là đặc tính tới hạn nhất của bất kỳ CRT nào. Một lưu ý cảnh báo: không nên "
        "nhầm lẫn độ phân giải với việc địa chỉ hoá. Một hệ có thể có định dạng địa chỉ hoá chính "
        "xác, nhưng nếu đốm sáng quá lớn thì khả năng phân giải của CRT sẽ kém bất chấp định dạng "
        "địa chỉ hoá. Ngược lại, nếu đốm sáng chính xác và định dạng địa chỉ hoá thô thì hình ảnh "
        "sẽ có độ phân giải thấp, nhưng độ phân giải của CRT vẫn cao. Độ phân giải bị ảnh hưởng "
        "bởi gần như mọi tham số hệ thống: kích thước đốm sáng, hội tụ, lệch, định dạng quét "
        "mành, lưới chắn và dòng chùm tia. Với một hệ được thiết kế hoàn hảo, độ rộng dòng và "
        "kích thước đốm sáng sẽ quyết định độ phân giải cuối cùng. Đường kính đốm sáng bị giới "
        "hạn bởi chất lượng quang học êlectron, kích thước hạt và độ dày của lớp huỳnh quang, và "
        "dòng chùm tia. Phân bố năng lượng theo tiết diện của chùm êlectron xấp xỉ Gauss. Dòng "
        "càng cao thì tiết diện chùm tia càng lớn. Sự tán xạ bởi từng hạt huỳnh quang cũng làm "
        "tăng kích thước đốm sáng. Do đó, độ phân giải cao khó đạt được hơn nhiều với các ứng "
        "dụng độ sáng cao. Những nhà vô địch về đốm sáng nhỏ là các CRT đơn sắc nhỏ 12 đến "
        "25 mm. Một số hệ thương mại đạt kích thước đốm sáng ≤ 25 µm, và đã có báo cáo về kích "
        "thước ≤ 15 µm [25]. CRT đơn sắc thuộc lớp 53 cm (21 in) có đường kính đốm sáng ≤ "
        "150 µm. CRT màu với bước lưới chắn ≤ 250 µm có sẵn ở kích thước đến 21 in với giá phổ "
        "thông, và điều này sẽ tiếp tục được cải thiện. Kích thước đốm sáng không kể hết câu "
        "chuyện về độ phân giải. Trong hầu hết các hệ, một yếu tố nào đó khác ngoài kích thước "
        "đốm sáng mới giới hạn hiệu năng. Định dạng quét có thể thấp hơn nhiều so với hiệu năng "
        "của CRT, băng thông của điện tử hỗ trợ thường thấp hơn băng thông của ống, và với màu, "
        "lưới chắn sẽ giới hạn độ phân giải nhiều hơn kích thước đốm sáng. Các kỹ sư vẫn có thể "
        "thiết kế một CRT duy trì được hiệu năng của nó ngay cả với điện tử hiện đại nhất. MTF "
        "(hàm truyền điều biến) là thước đo chuẩn cho độ phân giải. MTF so sánh độ điều biến của "
        "đầu ra hiển thị với độ điều biến của một tín hiệu đầu vào đã biết. Khi tần số không "
        "gian của đầu vào tăng, hiệu năng của đầu ra sẽ cho thấy sự suy giảm đều đặn về độ sâu "
        "và chất lượng điều biến. Bạn đọc quan tâm đến phần giới thiệu về chủ đề phức tạp này "
        "nên tham khảo bài tổng quan của Infante [26]. Độ tương phản và người bạn đồng hành của "
        "nó là thang độ xám cũng quan trọng đối với chất lượng hình ảnh CRT. Vì độ tương phản có "
        "thể được đo và diễn đạt theo rất nhiều cách khác nhau, thang độ xám có lẽ là chỉ báo "
        "thực tiễn hơn về hiệu năng từ góc nhìn của người dùng. Khi cố gắng thay thế phim truyền "
        "thống, cộng đồng tạo ảnh y tế đòi hỏi nhiều nhất ở CRT đơn sắc. CRT y tế có thể tạo tới "
        "256 sắc độ xám với bộ điều khiển 8 bit. Có những hệ làm được đơn sắc và màu 10 bit. Mặc "
        "dù thường được trích dẫn, số sắc độ xám không phải là chỉ báo thật sự về hiệu năng CRT "
        "và không nên nhầm với khả năng thang độ xám thật sự. Số sắc độ xám là đặc tính của "
        "nguồn hình ảnh và khả năng của điện tử; thang độ xám phản ánh khả năng của CRT. Thang "
        "độ xám thường được định nghĩa là một chuỗi bậc về độ sáng theo gia số 2½ từ đen đến đầu "
        "ra cực đại của CRT. Như vậy, thang độ xám là một chỉ báo thực tế kết hợp dải động, tỉ số "
        "tương phản, hiện tượng quầng sáng và phản xạ môi trường của CRT. Hơn 12 bậc thang độ "
        "xám được coi là hiệu năng tốt."))
    b.append(p(
        "Chủ đề chất lượng và đánh giá hình ảnh hiển thị là một chủ đề quan trọng. Ngoài độ phân "
        "giải và thang độ xám, người dùng và nhà thiết kế cần xem xét nhiều thước đo khác, như độ "
        "chói, khả năng làm mờ, độ tương phản, khả năng đọc, màu, độ dư sáng và hội tụ. Người "
        "dùng cũng có thể nhận ra các méo hình thị giác như méo gối, méo thùng và méo hình thang. "
        "Thảo luận về những chủ đề này và các vấn đề khác mà Bảng 91.1 nêu ra nằm ngoài phạm vi "
        "một chương; thực vậy, đó đã là chủ đề của cả những cuốn sách. Có những nguồn thông tin "
        "tốt trong lĩnh vực này [15, 27]; đặc biệt, sách của Keller [28] là tuyệt vời. Cần nhớ "
        "rằng bất kể dùng thước đo nào, thước đo quan trọng nhất vẫn là đánh giá chủ quan của "
        "người dùng cuối. Mặc dù nhiều yếu tố ảnh hưởng đến hiệu năng hiển thị cuối cùng, câu "
        "hỏi cuối cùng vẫn là màn hình trông tốt đến mức nào trong môi trường ứng dụng thực tế "
        "mà nó được thiết kế để đáp ứng."))

    b.append(h2("Tuổi thọ CRT và huỳnh quang", "CRT and Phosphor Lifetime"))
    b.append(p(
        "Tuổi thọ của một CRT phụ thuộc vào cách nó được điều khiển. Dòng chùm tia càng cao thì "
        "hiệu năng của nó càng suy giảm nhanh. Nói chung, sự suy giảm là do hỏng ba bộ phận của "
        "CRT: catôt, huỳnh quang và thuỷ tinh. Màn hình sáng hơn đòi hỏi dòng chùm tia cao hơn, "
        "và điều này lại đòi hỏi mức tải catôt cao hơn. Catôt ôxít có thể hoạt động thoải mái với "
        "dải tải 0,1 đến 10 A/cm². Điều này sẽ cho tuổi thọ điển hình trong khoảng 10.000 giờ. "
        "Các thiết kế catôt dispenser có thể cải thiện tuổi thọ catôt 2 đến 3 lần, nhưng tuổi thọ "
        "của từng catôt lại phụ thuộc vào mức độ sáng mà người dùng thường xuyên yêu cầu từ ống. "
        "Suy giảm huỳnh quang là cơ chế thứ hai ảnh hưởng đến tuổi thọ và hiệu năng của CRT. Mọi "
        "huỳnh quang đều suy giảm dưới sự bắn phá êlectron liên tục, một hiệu ứng gọi là cháy "
        "huỳnh quang. Tốc độ suy giảm liên quan đến dòng chùm tia, điện áp anôt và các tham số "
        "vật liệu riêng của từng loại huỳnh quang. Ngày nay có một dải rộng các vật liệu huỳnh "
        "quang tốt với đặc tính lão hoá được cải thiện nhiều. Cơ chế thứ ba là hoá nâu thuỷ tinh. "
        "Hiệu ứng này là một tương tác phức tạp giữa năng lượng cao của chùm êlectron và cấu "
        "trúc phân tử của thuỷ tinh [10]. Trong những năm gần đây, các nhà cung cấp thuỷ tinh đã "
        "đạt những bước tiến lớn trong việc cung cấp cho các nhà sản xuất CRT những vật liệu "
        "thuỷ tinh cải tiến. Tuy nhiên, lão hoá huỳnh quang và hoá nâu thuỷ tinh vẫn là những "
        "mối quan tâm quan trọng, đặc biệt trong các ứng dụng cực sáng (dòng chùm tia cao), như "
        "chiếu CRT."))

    b.append(h2("Ưu và nhược điểm của CRT", "CRT Strengths and Weaknesses"))
    b.append(p(
        "Với một thế kỷ phát triển phía sau, CRT có rất nhiều ưu điểm khiến nó trở thành một lựa "
        "chọn hiển thị hấp dẫn cho nhà thiết kế hệ thống xử lý hàm lượng thông tin cao hoặc hình "
        "ảnh động. Bảng 91.2 liệt kê một số thuộc tính, tích cực và tiêu cực, mà nhà thiết kế hệ "
        "thống nên cân nhắc khi đánh giá xem có nên dùng công nghệ CRT hay không. Những nét đáng "
        "chú ý nhất của CRT là tính linh hoạt và chi phí. CRT có thể hoạt động trên một dải rộng "
        "các định dạng độ phân giải, từ truyền hình thương mại đến những yêu cầu khắt khe của "
        "tạo ảnh y tế và ghi ảnh số ra phim. Một chiếc máy có thể dễ dàng được thiết kế để nhận "
        "vô số định dạng quét và độ phân giải, từ văn bản tĩnh đến hình ảnh động cỡ megapixel với "
        "tốc độ khung hình hàng trăm khung mỗi giây. Tính linh hoạt này có nghĩa là hệ thống có "
        "thể được nâng cấp sau này mà không phải thiết kế lại hệ thống con hiển thị. Giao tiếp "
        "với CRT cũng đơn giản; có những tiêu chuẩn và phần cứng đã được thiết lập vững chắc cho "
        "nhiều định dạng quét, từ NTSC truyền hình đến các tiêu chuẩn RGB của ngành máy tính cá "
        "nhân. Cuối cùng, chi phí là điều quan trọng cần nhấn mạnh; CRT rẻ. Màn hình CRT để bàn "
        "cung cấp hiệu năng của nó với giá ≤ 0,00005 USD cho mỗi phần tử phân giải màu! Hiện nay, "
        "không công nghệ hiển thị nhiều thông tin nào khác có thể sánh được với mức chi phí này."))
    b.append(_tbl91_2(
        _ADV_VI, _DIS_VI,
        "Bảng 91.2 · Ưu và nhược điểm của công nghệ CRT."))

    b.append(h2("Chọn CRT", "CRT Selection"))
    b.append(p(
        "Các yêu cầu thiết kế về (1) độ phân giải, (2) độ sáng và (3) kích thước màn hình sẽ "
        "nhanh chóng dẫn nhà thiết kế hệ thống đến một lớp CRT cụ thể. Nếu các yêu cầu thiết kế "
        "gần với truyền hình hoặc màn hình máy tính để bàn, việc chọn lựa rất dễ. Có hàng trăm "
        "nhà cung cấp chào bán CRT tích hợp và bộ điều khiển điện tử như những mặt hàng mua ngay. "
        "Các hệ lưới chắn màu với hơn 40 phần tử/cm thường có sẵn. Nếu cần độ phân giải cao hơn, "
        "CRT cho tạo ảnh y tế và ghi ảnh ra phim có thể đáp ứng yêu cầu. Các yêu cầu hiển thị "
        "kích thước lớn về mặt vật lý có thể được đáp ứng bằng CRT chiếu hoặc bằng CRT ghép nối "
        "dùng bộ xử lý tường video. CRT nhỏ đến cỡ tí hon cho độ phân giải đến 500–600 phần "
        "tử/cm và tính khả chuyển. Nếu ứng dụng nằm ngoài dòng chính, nhà thiết kế sẽ cần trao "
        "đổi trực tiếp với các nhà cung cấp CRT. Bảng 91.3 là danh sách một phần các nhà cung cấp "
        "CRT. Vì CRT đã được thiết kế để đáp ứng một dải rộng các ứng dụng đặc thù, khả năng là "
        "rất cao rằng một thiết kế phù hợp đã tồn tại. Nếu không, CRT đã chín muồi đến mức các "
        "nhà cung cấp làm việc từ một nền tảng kinh nghiệm đã được chứng minh có thể thiết kế "
        "một ống trực tiếp theo yêu cầu của khách hàng với ít vấn đề hoặc bất ngờ về thiết kế."))
    b.append(_tbl91_3(
        _T91_3,
        "Bảng 91.3 · Các công ty sản xuất ống phóng tia điện tử."))

    b.append(h2("Xu hướng tương lai của công nghệ CRT",
                "Future Trends in CRT Technology"))
    b.append(p(
        "Công nghệ CRT đã chín muồi, và ngành không thấy trước những bất ngờ lớn. CRT sẽ tiếp "
        "tục tiến hoá: độ phân giải sẽ cải thiện, màn hình sẽ phẳng hơn, góc lệch sẽ lớn hơn và "
        "dấu chân sẽ được thu nhỏ. Thế giới máy tính tiếp tục đòi hỏi độ phân giải cao hơn. Năm "
        "1987, màn hình lớp VGA 36 cm (14 in) (640 × 480) với 300.000 điểm ảnh và 16 màu là tiêu "
        "chuẩn mới. Năm 1998, màn hình để bàn 43 cm (17 in) đã có khả năng 1600 × 1200 "
        "(1,9 megapixel) với màu 24 bit. Lớp màn hình 53 cm (21 in), từng là một thiết bị đặt "
        "hàng đắt tiền, cũng đã phổ biến rộng rãi. Xu hướng tăng độ phân giải và hiệu năng trong "
        "khi giảm chi phí cho thấy mọi dấu hiệu tiếp tục. Cộng đồng y tế đang nhanh chóng chuyển "
        "sang các hệ đơn sắc với thang độ xám 12 bit ở độ phân giải 2560 × 2048 (5 megapixel). "
        "Tất cả những điều này có nghĩa là nhà thiết kế thiết bị đo có độ phân giải và độ trung "
        "thực tốt hơn với ít tiền hơn."))
    b.append(p(
        "Có một cuộc cách mạng thầm lặng đang diễn ra trong ngành công nghiệp hiển thị thông "
        "tin, có thể có tác động đáng kể đến CRT và mọi công nghệ hiển thị thông tin. Có một xu "
        "hướng thiết kế nhằm tách rời độ phân giải và độ trung thực của thiết bị hiển thị khỏi "
        "kích thước vật lý của nó. Có một số ứng dụng thúc đẩy sự thay đổi này: thông tin liên "
        "lạc, quân sự, máy tính xách tay, mô phỏng và thực tế ảo. Đây là lý do tại sao công nghệ "
        "CRT tí hon lại hoạt động tích cực hơn trong những năm gần đây. Đây cũng là động lực thúc "
        "đẩy một số đối thủ chính của CRT tí hon, như màn hình phát xạ trường trên chip (FED), "
        "thiết bị gương biến dạng (DMD), màn hình mạch tích hợp tinh thể lỏng sắt điện, và công "
        "nghệ màn hình tinh thể lỏng ma trận chủ động trên chip (LCD). Nếu thành hiện thực, những "
        "công nghệ này hứa hẹn là các giải pháp chi phí thấp vì chúng được xây dựng trên nền tảng "
        "công nghệ của ngành chip silic. Những đối thủ này có tiềm năng rất thực tế trong việc "
        "loại bỏ CRT tí hon, và ở một số lĩnh vực ứng dụng, cả tấm nền LCD. Tuy nhiên, CRT với "
        "100 năm tiến hoá thiết kế và độ chín muồi đáng gờm không đứng yên; tài sản và thị trường "
        "của nó vẫn rất ấn tượng. Mặc dù nó là một trong số ít các ống chân không còn được dùng "
        "ngày nay, CRT truyền thống không hề bị kết án là lỗi thời trong tương lai trước mắt."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs(_REFS))

    b.append(h2("Thông tin thêm", "Further Information"))
    b.append('<ul class="ref-list">%s</ul>' % "".join("<li>%s</li>" % i for i in _FURTHER))

    b.append(h2("Nguồn Internet", "Internet Resources"))
    b.append(p(
        "Dưới đây là danh sách ngắn những nơi nên bắt đầu tìm kiếm trên World Wide Web thông tin "
        "về CRT và màn hình, tiêu chuẩn, thước đo và nghiên cứu hiện hành. Ngoài ra, nhiều nhà "
        "sản xuất liệt kê trong Bảng 91.3 duy trì website với thông tin hữu ích."))
    b.append(_web_list(_WEB))
    return "".join(b)


# ================================================================ ENGLISH
def body_en():
    b = []
    b.append(note(
        "<b>Translator's note.</b> The 1999 original carries several typesetting faults, kept "
        "here and recorded as follows. The symbol <b>£</b> is a mangled <b>≤</b> and <b>³</b> is "
        "a mangled <b>≥</b>. Superscripts lost their minus signs and their raised position: "
        "“1.3 ´ 10–4 Pa (10–6 torr)” reads 1.3 × 10<sup>−4</sup> Pa (10<sup>−6</sup> torr), and "
        "“0.1 to 10 A/cm2” is A/cm². “21/2” is the mixed number 2½. Chemical subscripts were "
        "dropped: Zn(Cd)S:Cu:Al, Y₂O₂S:Eu. In Section 91.8 the source prints “£25 mm”, “£15 mm”, "
        "“£150 mm” and “£250 mm”; these must be <b>µm</b>, not mm — a 25 mm spot is impossible on "
        "a 12 mm tube — and the translation gives µm. “Standford Resources” in Section 91.1 is a "
        "misspelling of <i>Stanford Resources</i> (correct in References 1–2); “electromagnetic "
        "yolks” in Section 91.3 is <i>yokes</i>; “whether of not” in Section 91.10 is <i>whether "
        "or not</i>. In Section 91.6 the sentence “both require precise beam control” has no "
        "antecedent — “both” refers to the delta and in-line configurations just described. In "
        "Table 91.3 the source prints “Phillips” (the company is Philips), “1-chrome” (should be "
        "1-chome), “Tyoko” (Tokyo) and “Minato-KU”; the addresses are reproduced as printed."))

    b.append(h2("Introduction"))
    b.append(p(
        "The cathode ray tube (CRT) is unequaled in its ability to produce dynamic, quality, "
        "high-information-content imagery at high resolution. Even more impressive is that it "
        "achieves this for a lower cost per pixel than any other comparable electronic display "
        "technology. For the instrument designer requiring a high-information-content display, "
        "it offers numerous advantages."))
    b.append(p(
        "As a raw image tube, it is commonly available as an off-the-shelf item with a broad "
        "infrastructure of vendors, integrators, support, and part suppliers. Interface "
        "standards are well established and as a complete system, ready to take a standard "
        "signal input, it is available worldwide in a variety of performance ranges. To meet "
        "different application requirements, it is available in diagonal sizes from 12 mm to "
        "over 1 m with resolution from thousands of pixels to over 5 million pixels per frame. "
        "Tube characteristics improve on a yearly basis, and prices continue to decrease."))
    b.append(p(
        "Stanford Resources has been tracking the CRT market for almost 20 years, and is an "
        "excellent source of information. In its latest report, it indicates that despite "
        "competition from other display technology, the CRT will remain the single largest "
        "market in the display industry. The worldwide market for CRT tubes in 1997 was "
        "261 million units worth $26 billion U.S. This is expected to grow to 341 million units "
        "worth more than $34 billion by 2003 [1, 2]. Although there are many competing "
        "information display technologies, the CRT will be with us well into the 21st century."))

    b.append(h2("History"))
    b.append(p(
        "The CRT has a rich and distinguished history. The roots of today's CRT technology "
        "extend back more than 100 years to the latter half of the 19th century. Eugene Goldstein "
        "first introduced the term cathode rays; John W. Hittorf, Heinrich Geissler, Julius "
        "Plücker, and others made important contributions specific to CRT technology [3]. "
        "Throughout the 19th century, researchers were interested in the nature of a luminous "
        "gas discharge and shadowy rays that occurred when a high voltage potential was applied "
        "between two electrodes in a vacuum. Sir William Crookes was an active experimentalist "
        "in this field, and early cathode ray devices came to be known as Crookes tubes. "
        "Crookes noted that a glow was generated by the surface that the rays struck; the rays "
        "themselves were not the source of light. By producing tubes with a vacuum of "
        "1.3 × 10<sup>−4</sup> Pa (10<sup>−6</sup> torr), he eliminated the luminous gas "
        "discharge and worked directly with the cathode rays [4]. Crookes demonstrated the "
        "following: luminance depended directly upon the material properties of the surface the "
        "rays struck; a magnetic field would deflect the path of the rays; the deflection was "
        "proportional to the strength of the magnetic field; and a magnetic field could be used "
        "to focus the rays into a beam. He also suggested the rays emitted by the cathode were a "
        "stream of charged tiny particles, which were soon to be identified by Joseph John "
        "Thomson as electrons. Continuing CRT experimentation lead to the discovery of x rays by "
        "Wilhelm Konrad Röntgen in 1895."))
    b.append(p(
        "Ferdinand Braun was the first person to envision the CRT as a tool for the display of "
        "information and is generally credited with the invention of the first device to be a "
        "direct forerunner to the modern CRT [5]. Braun in 1896 designed a CRT “indicator tube” "
        "for monitoring high frequencies in power-generating equipment. His design contained all "
        "of the same elements as today's CRTs. It utilized a cathode as an electron source, two "
        "control coils for vertical and horizontal deflection, an anode for electron "
        "acceleration and beam control, and a focusing slit. He also incorporated a phosphor "
        "screen normal to the beam for tracing its path. Although crude by later standards, this "
        "was the direct prototype for CRT oscilloscopes."))
    b.append(p(
        "In 1903 to 1905 Arthur Wehnelt added several very significant advances to Braun's "
        "design. Wehnelt developed and implemented a hot oxide-coated cathode and a beam control "
        "grid [5]. This lowered the voltage necessary to generate the electron stream and "
        "provided for much finer control of the beam current. These developments were the "
        "forerunner of the modern electron gun."))
    b.append(p(
        "The CRT remained mostly a laboratory device until three important applications ushered "
        "it onto the center stage of information display: oscilloscopes, television, and "
        "military radar. By the early 1900s oscilloscopes were being widely used for the study "
        "of time-varying electric circuits in communication. Television was developed in the "
        "1920s and in July of 1930 the National Broadcasting Company began the experimental "
        "broadcast of television in New York City. During World War II the CRT underwent a "
        "second wave of maturation with the advent of radar technology. By the end of the 1940s "
        "the TV-CRT was available as a consumer product. In the 1950s RCA perfected shadow mask "
        "technology and before long color became a new standard, gaining wide consumer "
        "acceptance in the 1960s. While the principal components of a CRT system have not "
        "fundamentally changed in many decades, the CRT has continued to improve."))

    b.append(h2("Image Formation with a CRT"))
    b.append(p(
        "Although there are many different CRT designs, some of which are quite intricate, the "
        "process of forming an image using a CRT is straightforward. The procedure can be "
        "divided into four basic stages: beam formation, beam focusing, beam deflection, and "
        "energy conversion. These stages occur in four different regions of the CRT and follow "
        "in order from the rear of the tube (the neck) to the faceplate. As shown in "
        "Fig. 91.1, the elements at the rear of the tube are collectively called the electron "
        "gun."))
    b.append(fig(1, "en"))

    b.append(h3("Beam Generation with the Electron Gun"))
    b.append(p(
        "The cathode generates the stream of electrons used to form the image-writing beam. The "
        "traditional cathode is a metal conductor such as nickel coated with a thin layer of "
        "oxide, typically a barium strontium compound. To reduce the voltage required to "
        "generate electron emission, the cathode is heated to 700 to 1200 °C. Applications that "
        "require high brightness often use more advanced and expensive dispenser cathode designs "
        "to increase the beam current while maintaining reasonable cathode life. These designs "
        "incorporate complex cathode structures and materials such as barium ceramics, "
        "molybdenum, rhenium, and tungsten. Readers interested in advanced cathode designs and "
        "additional information on CRT materials technology should consult References 6 through "
        "10. The flow of electrons from the cathode is controlled by varying the potential "
        "between the cathode and a series of control grids commonly known as G1 (the control "
        "grid) and G2 (the acceleration grid). A voltage potential of 100 to 1000 V between G2 "
        "and the cathode creates the potential necessary to pull a stream of electrons off the "
        "cathode, forming the beam. The beam amplitude can be controlled and even completely "
        "shut off by varying the potential on G1. Thus, the voltage at G1 controls brightness "
        "because the brightness is proportional to beam current. The design of the cathode with "
        "respect to impedance and loading influences the maximum rate at which the beam can be "
        "modulated. The cathode and its associated control grids can be designed to produce a "
        "crossover flow of electrons or a laminar flow. In crossover gun designs, the emitted "
        "electrons converge to a point in front of the cathode. By using electron optics, this "
        "beam spot is imaged onto the phosphor screen. Due to inherent advantages, the crossover "
        "design is widely used. A crossover beam is narrow, making it easier to deflect than a "
        "thicker beam, and the spot can be very small, improving resolution at the screen. In "
        "theory, a laminar flow design provides for the possibility of higher beam current from "
        "a similar-sized cathode. In practice, the improvement is not usually advantageous "
        "enough to offset the added difficulty of controlling a wider beam."))

    b.append(h3("Electron Beam Focusing"))
    b.append(p(
        "Beam focusing and beam current are critical in determining the final spot size and thus "
        "the resolution of the CRT. Focusing a beam of electrons is directly analogous to "
        "focusing a beam of light; the discipline is called electron optics. Concerns familiar "
        "to optical imaging such as magnification, spherical aberration, and astigmatism also "
        "confront electron optics. As CRTs become larger, and operate at higher deflection "
        "angles, spot control becomes critical. Beam focusing is achieved using either "
        "electrostatic focusing grids or electromagnetic focusing coils. Electrostatic focus is "
        "the most extensively used technique. It can be found in use in applications from "
        "television to desktop computer monitors. Electrostatic focus is achieved by applying a "
        "succession of potentials across a complex sequence of focusing grids built into the "
        "electron gun. As designers seek to improve performance further, grid designs have "
        "become intricate [11, 12]. Magnetic focus is the system of choice for all "
        "high-performance systems where resolution and brightness are design objectives. "
        "Magnetic lenses are better at producing a small spot with few aberrations. External "
        "coils in a yoke around the neck of the tube control the beam. Since it provides "
        "superior performance, electromagnetic focus is common on high-resolution commercial "
        "systems. Magnetic focus can also be achieved using permanent magnets and specialized "
        "hybrid electrostatic/magnetic focus components. Due to the tremendous impact focus has "
        "on resolution, tube suppliers continue to improve focus control [13, 14]. For an "
        "excellent and comprehensive treatment of electron physics in CRTs, beam control, "
        "detailed design discussions, and other aspects of CRT devices, consult Sol Sherr's "
        "textbook [15]."))

    b.append(h3("Electron Beam Deflection"))
    b.append(p(
        "The beam deflection system is responsible for controlling the position of the spot on "
        "the front face of the CRT. As with focusing, beam deflection techniques can be "
        "electromagnetic or electrostatic. A magnetic deflection system consists of two "
        "electromagnetic yokes on opposite sides of the CRT neck; a horizontal deflection coil "
        "and a vertical deflection coil. The position of the beam is easily controlled; the "
        "amount of beam deflection is directly proportional to the current in the coil. "
        "Deflection coil design also influences spot size and shape. Coil designs can "
        "incorporate correction for coma, convergence errors, and pincushion distortion [16]. "
        "Because of its low cost and efficiency, CRTs for both moderate- and high-resolution "
        "applications normally use magnetic deflection. Electrostatic deflection provides faster "
        "beam displacement but less spot size control. It is typically used in oscilloscope "
        "systems, where resolution requirements are moderate and deflection speed is paramount."))

    b.append(h2("CRT Addressing: Raster Scanning vs. Stroke"))
    b.append(p(
        "Raster scanning is the most common CRT addressing technique. In raster scanning the "
        "electron beam writes each frame one line at a time. This means the horizontal "
        "deflection system requires a higher bandwidth than the vertical deflection system. "
        "High-performance raster CRTs have a horizontal bandwidth of 15 to 150 kHz, and a "
        "vertical deflection bandwidth of 30 to 180 Hz. The information is written onto the "
        "front face of the CRT from left to right and top to bottom, one line at a time. Raster "
        "scanning can be interlaced or progressive (noninterlaced). In interlace scanning, each "
        "frame of information is decomposed into two fields. The first field consists of all of "
        "the odd-numbered lines in the original frame, and the second field contains all of the "
        "even-numbered lines. Each field is scanned onto the CRT at twice the frame rate. "
        "Commercial television is interlaced. In the U.S., the frame rate is 30 Hz and the field "
        "rate is 60 Hz; this scheme is known as the NTSC standard. PAL and SECAM are two other "
        "well-known commercial formats in use today. There are numerous other standards, both "
        "analog and digital, in use worldwide, each with slightly different scan rates, "
        "resolution/addressing formats, luminance and color encoding, and timing protocols "
        "[17, 18]. Interlace scanning is an engineering compromise that conserves transmission "
        "bandwidth, electronics bandwidth, and CRT bandwidth, while maintaining acceptable "
        "performance with respect to moving imagery, resolution, and flicker. Computer monitors "
        "employ a progressive raster scan. Each frame has one field. The display is generated "
        "line by line, in order from the first pixel to the last pixel. Frame rates for the "
        "typical desktop monitor vary from 60 to 85 Hz to over 180 Hz for specialized systems."))
    b.append(p(
        "Stroke is an alternative addressing technique that was once quite common. The name for "
        "the technique comes from the phrase “the stroke of a pen.” Stroke is a point-to-point "
        "addressing system. The beam is directed to the starting point of a line, turned on, and "
        "then moved directly to the end of the line. Because there are no raster lines, stroke "
        "CRT resolution is independent of direction and is limited primarily by spot size. "
        "Stroke addressing is excellent for low-information-content screens with detailed "
        "graphic characters or simple vector graphics. It provides extremely high quality "
        "drawing, clean lines, precise detail, and high speed while conserving power and "
        "bandwidth. Stroke systems address the CRT only where there is information, not the "
        "entire screen as in raster scanning. This technique is uncommon today because it is too "
        "slow and computationally intensive for systems that have high information content, gray "
        "scale, or imagery."))

    b.append(h2("The Phosphor Screen"))
    b.append(p(
        "The phosphor functions as the CRT transducer. It converts the energy of the electron "
        "beam into light. This conversion process is called cathodoluminescence. CRT phosphors "
        "are inorganic crystalline materials doped with one or more impurities called activators "
        "and coactivators. Phosphors emit light in two ways, fluorescence and phosphorescence. "
        "Fluorescence is the emission of light by the phosphor material while it is under "
        "bombardment by the electron beam. The continued emission of light after the bombardment "
        "has ceased is called phosphorescence. The length of time phosphorescence lasts is known "
        "as persistence. Persistence can vary from tens of nanoseconds to many minutes, or even "
        "hours. CRTs take advantage of both forms of cathodoluminescence. Briefly, "
        "cathodoluminescence occurs when the electron beam excites the electrons of the phosphor "
        "into higher, unstable energy states available due to the presence of the activators. "
        "When the electrons transition back to their stable states, light is emitted. The choice "
        "of phosphor depends on the requirements of the application with respect to wavelength "
        "characteristics (narrow emission spectra or broadband emission), color, brightness, "
        "resolution, and persistence. Commercial television CRTs typically make use of the "
        "following phosphor powders: ZnS:Ag:Cl (blue), Zn(Cd)S:Cu:Al or ZnS:Cu:Au:Al (green), "
        "and Y₂O₂S:Eu (red) [19]. Television CRTs use moderately short-persistence phosphors. "
        "This ensures a new frame does not exhibit blurring due to the previous frame. "
        "Traditionally, phosphors for radar displays, where the screen is refreshed "
        "infrequently, had a mix of short and long persistence. However, with the advent of "
        "today's digital systems, the use of long-persistence phosphors has declined. The "
        "Electronics Industries Association maintains an information database of commercial "
        "phosphors for CRTs. The interested reader should consult its publication TEP116-C [20]. "
        "Figure 91.2 illustrates the spectral characteristics of several typical phosphors."))
    b.append(fig(2, "en"))

    b.append(h2("Color CRTs Using Shadow Masks"))
    b.append(p(
        "Color has been a part of the CRT world since the early 1950s. A sound understanding of "
        "human color perception is important for a detailed understanding of color in CRTs. "
        "Readers interested in an excellent comprehensive treatment of color science should "
        "consult Wyszecki and Stiles [21] or Robertson and Fisher [22] for a brief overview. The "
        "most common method of introducing color to the CRT is the three-gun shadow mask "
        "technique. The shadow mask is a metal grid of many tiny apertures held in place "
        "immediately before the phosphor screen. The phosphor screen is an array of three "
        "different phosphor subpixels. Three electron guns are placed closely together in the "
        "neck of the tube, one gun for each one of the primary colors (red, green, and blue). "
        "The guns make a small angle with respect to each other. The shadow mask and beams are "
        "aligned so that each beam falls on the appropriate phosphor dot. The dots are placed "
        "closely together so the eye spatially integrates the subpixels into a continuous blend "
        "of color. There are two common configurations, delta and in-line. Delta, the traditional "
        "method, arranges the electron guns and the phosphor dots in a triad. This requires a "
        "shadow mask consisting of a grid of circular apertures. More recently, Sony introduced "
        "the Trinitron™ design. In the Trinitron tube the guns are placed in line, the shadow "
        "mask consists of vertical slots, and the phosphors are in vertical stripes. The design "
        "offers improved vertical resolution and is easier to converge, but the mask is slightly "
        "more difficult to support and is subject to thermal stress problems. Trinitron continues "
        "to be an important and popular design [23]. The shadow mask technique of producing a "
        "color image has three main drawbacks. First, the shadow mask typically absorbs more than "
        "75% of the electron beam energy, limiting brightness and causing undesirable thermal "
        "effects. Second, both configurations require precise beam control to converge the three "
        "different images from the electron guns. Third, the resolution of the display is limited "
        "by the requirements of spatial color; three subpixels are needed to make each full-color "
        "pixel."))

    b.append(h2("Alternative Techniques for Realizing Color Using CRTs"))
    b.append(p(
        "There are alternative approaches to producing color with CRTs. In its own way, each "
        "seeks to improve upon one or more of the enormously successful shadow mask designs. The "
        "three most noteworthy challengers are beam index tubes, penetration phosphor tubes, and "
        "field sequential color systems. All three have been around for decades, but only field "
        "sequential color systems are commercially available."))

    b.append(h3("Beam Index and Penetration Phosphor Tube Designs"))
    b.append(p(
        "A beam index tube uses a slotted mask and vertical phosphor stripes. One electron beam "
        "is focused to less than the width of a phosphor stripe. A reflected ultraviolet signal "
        "from the mask provides a feedback signal. This signal is used to index the position of "
        "the beam very accurately. Color selection is achieved by precise beam positioning and "
        "rapid beam modulation. Although beam indexing offers perfect convergence, few guns, "
        "energy savings, and high resolution, practical problems in control and manufacturing "
        "have left this approach unrealized. Penetration tubes are potentially even more "
        "advantageous since color is produced with one electron gun and no mask is required. The "
        "phosphor screen consists of a layering of several different phosphors. There are many "
        "approaches to the layering structure, but the basic principle is that each layer "
        "produces a different color. To select among the different colors, the beam energy is "
        "varied, altering its layer penetration. In theory, multiple layers of phosphors could be "
        "used to produce a full-color display. Unfortunately, this design requires high switching "
        "voltages, and the color purity is poor because of the dilution caused by leakage from "
        "the unselected phosphor layers. In the past, a few two-color systems have been produced "
        "on a limited basis with stroke writer systems (p. 147 of Reference 4)."))

    b.append(h3("Field Sequential Color"))
    b.append(p(
        "Field sequential color (FSC) is a different approach to realizing color using a "
        "monochrome CRT and color filters [24]. The shadow mask relies on the ability of the eye "
        "to perform a spatial integration on a group of color elements. Field sequential color "
        "exploits the ability of the eye to perform a temporal integration of color fields. Field "
        "sequential color is not a new concept; it was an early design suggestion for commercial "
        "color television. To implement field sequential color, each full-color frame is "
        "decomposed into primary color fields (red, green, and blue). Each of these color fields "
        "is displayed sequentially on a monochrome CRT while simultaneously a color filter is "
        "placed over the front of the CRT. The filters must be rapidly changed to stay in "
        "sequence with the individual fields which are displayed at three times the desired frame "
        "rate. This sequence is so quick that the eye fuses the individual color fields into a "
        "steady blend of continuous color. Field sequential color systems have all of the "
        "advantages of a monochrome CRT, namely, superior resolution and simplicity. The major "
        "historical drawbacks to field sequential color have been the difficulty in controlling "
        "a bulky, spinning, mechanical filter wheel, and two thirds of the light energy of the "
        "phosphor is thrown away in each field. In the past, some viewers have reported the "
        "ability to perceive the individual color fields intermittently; this artifact is known "
        "as “color break up.” Field sequential color systems have seen a commercial rebirth due "
        "to several factors. The luminous efficiency of several phosphors has improved to the "
        "point where the light loss penalty is no longer a severe price to pay. Awkward, "
        "mechanical filter wheels have been replaced by several different types of compact, "
        "low-power, liquid crystal shutters. The use of faster frame rates and digital sampling "
        "techniques has reduced color artifacts. And finally, monochrome CRTs using field "
        "sequential color meet the growing market need for small high-resolution displays."))

    b.append(h2("Image Quality and Performance"))
    b.append(p(
        "For any display technology, the ultimate test of performance and quality is how the "
        "image looks to the viewer in a real-world environment. This is highly subjective, but "
        "critical none the less. Table 91.1 highlights some important parameters associated with "
        "performance and image quality."))
    b.append(_tbl91_1(
        _T91_1_EN,
        "Table 91.1 · Parameters that influence CRT performance and image quality."))
    b.append(p(
        "Resolution is the most critical characteristic of any CRT. A note of caution, "
        "resolution should not be confused with addressing. A system can have a precise "
        "addressing format, but if the spot is too large the CRT resolution capability will be "
        "poor despite the addressing format. Alternatively, if the spot is precise and the "
        "addressing format is coarse, the image will be low resolution, but the CRT resolution "
        "will be high. Resolution is affected by almost every system parameter: spot size, "
        "focus, deflection, raster format, the mask, and beam current. For a perfectly designed "
        "system, line width and spot size will ultimately determine the resolution. Spot "
        "diameter is limited by the quality of the electron optics, the particle size and "
        "thickness of the phosphor layer, and beam current. The cross section energy distribution "
        "of the electron beam is approximately Gaussian. The higher the current, the larger the "
        "beam cross section. Scattering by individual phosphor particles also increases the spot "
        "size. Thus, high resolution is much more difficult to achieve for high-brightness "
        "applications. The champions of small spot sizes are the small 12 to 25 mm monochrome "
        "CRTs. Several commercial systems achieve ≤ 25 µm spot sizes, and sizes ≤ 15 µm have "
        "been reported [25]. Monochrome CRTs in the 53 cm class (21-in.) have spot diameters "
        "≤ 150 µm. Color CRTs with shadow mask pitches ≤ 250 µm are available in sizes up to "
        "21 in. at commodity prices, and this will continue to improve. Spot size does not tell "
        "the whole resolution story. In most systems something other than spot size limits "
        "performance. The scan format may be well below the performance of the CRT, the "
        "bandwidth of the support electronics is frequently less than the tube bandwidth, and, "
        "for color, the shadow mask will limit resolution more than spot size. Engineers can "
        "still design a CRT that maintains its performance even with state-of-the-art "
        "electronics. MTF (modulation transfer function) is the standard metric for resolution. "
        "MTF compares the modulation of the displayed output with the modulation of a known "
        "input signal. As the spatial frequency of the input increases, the performance of the "
        "output will show a steady roll-off in modulation depth and quality. Readers interested "
        "in an introduction to this complex topic should consult Infante's review [26]. Contrast "
        "and its related companion, gray scale, are also important to CRT image quality. Since "
        "contrast can be measured and stated in so many different terms, gray scale is probably a "
        "more practical indicator of performance from a user's standpoint. As it attempts to "
        "replace traditional film, the medical imaging community demands the most of the "
        "monochrome CRT. Medical CRTs can produce up to 256 shades of gray with 8-bit "
        "controllers. Systems are available that will do 10-bit monochrome and color. Although "
        "frequently quoted, shades of gray is not a true indication of CRT performance and should "
        "not be confused with true gray scale capability. Shades of gray is a characteristic of "
        "the image source and the capability of the electronics; gray scale reflects the "
        "capability of the CRT. Gray scale is typically defined as a series of steps in "
        "brightness in increments of 2½ from black to maximum CRT output. Thus, gray scale is a "
        "realistic indicator that combines CRT dynamic range, contrast ratio, halation, and "
        "ambient reflections. More than 12 steps of gray scale is considered good performance."))
    b.append(p(
        "The subject of display image quality and evaluation is an important topic. In addition "
        "to resolution and gray scale, users and designers need to consider many other metrics, "
        "such as luminance, dimmability, contrast, readability, color, persistence, and "
        "convergence. Users may also be aware of visual distortions such as pincushion, barrel, "
        "and keystone. A discussion of these topics and the other issues raised by Table 91.1 is "
        "beyond the scope of a single chapter; indeed, it has been the subject of books. There "
        "are good sources of information in this area [15, 27]; in particular, Keller's [28] text "
        "is superb. It is essential to remember that no matter which metrics are used, the most "
        "single most important metric is the subjective determination of the end users. Although "
        "many factors will affect final display performance, the bottom line remains how good "
        "does the display look in the real-world application environment it was designed to "
        "meet."))

    b.append(h2("CRT and Phosphor Lifetime"))
    b.append(p(
        "The lifetime of a CRT depends on how it is driven. The higher the beam current, the more "
        "rapidly its performance will degrade. In general, degradation is due to a failure of "
        "three parts of the CRT — the cathode, the phosphor, and the glass. Brighter displays "
        "require higher beam current, and this, in turn, requires a higher level of cathode "
        "loading. Oxide cathodes can comfortably operate with a loading range of 0.1 to "
        "10 A/cm². This will provide a typical lifetime in the range of 10,000 h. Dispenser "
        "cathode designs can improve cathode life 2 to 3 times, but again individual cathode life "
        "depends on how much brightness the user regularly demands from the tube. Phosphor "
        "degradation is the second mechanism affecting CRT lifetime and performance. All "
        "phosphors degrade under constant electron bombardment, an effect called phosphor "
        "burning. The rate of degradation is related to beam current, anode voltage, and material "
        "parameters specific to each phosphor. Today, there is a broad range of good phosphor "
        "materials with greatly improved aging characteristics. The third mechanism is glass "
        "browning. This effect is a complicated interaction between the high energy of the "
        "electron beam and the molecular structure of the glass [10]. In recent years, glass "
        "suppliers have made great strides in providing CRT manufacturers with improved glass "
        "materials. However, phosphor aging and glass browning are still important concerns, "
        "especially in extremely bright (high beam current) applications, such as CRT "
        "projection."))

    b.append(h2("CRT Strengths and Weaknesses"))
    b.append(p(
        "With a century of development behind it, the CRT has abundant advantages that make it "
        "an attractive display option for the system designer dealing with high information "
        "content or dynamic imagery. Table 91.2 lists some attributes, positive and negative, "
        "which the system designer should consider in evaluating whether or not to use CRT "
        "technology. The most notable traits of the CRT are flexibility and cost. CRTs can "
        "operate over a wide range of resolution formats from commercial television to the "
        "strict requirements of medical imaging and digital-to-film recording. One unit can "
        "easily be designed to accept a myriad of scan formats and resolutions from static text "
        "to dynamic imagery with megapixels at frame rates of hundreds of frames per second. "
        "This flexibility means the system can be upgraded later without having to redesign the "
        "display subsystem. Interfacing with the CRT is also straightforward; there are "
        "well-established standards and hardware for many scan formats from the television NTSC "
        "to the RGB standards of the personal computer industry. Finally, cost is important to "
        "emphasize; CRTs are inexpensive. The desktop CRT delivers its performance for "
        "≤ $0.00005 per color resolution element! Currently, no other high-information-content "
        "display technology can match this cost."))
    b.append(_tbl91_2(
        _ADV_EN, _DIS_EN,
        "Table 91.2 · The strengths and weaknesses of CRT technology."))

    b.append(h2("CRT Selection"))
    b.append(p(
        "The design requirements for (1) resolution, (2) brightness, and (3) screen size will "
        "quickly steer the system designer to a particular class of CRTs. If the design "
        "requirements are close to either television or desktop computer monitors, the choice is "
        "easy. There are literally hundreds of vendors offering integrated CRTs and electronic "
        "drivers as off-the-shelf items. Color shadow mask systems with more than 40 elements/cm "
        "are commonly available. If higher resolution is required, then medical imaging and film "
        "recorder CRTs may meet the requirements. Physically large display requirements can be "
        "supplied by projection CRTs or by tiled CRTs using video wall processors. Small to "
        "miniature CRTs provide resolutions up to 500 to 600 elements/cm and portability. If the "
        "application falls out of the mainstream, the designer will need to speak directly with "
        "CRT vendors. Table 91.3 is a partial list of CRT suppliers. Since CRTs have been "
        "designed to satisfy a broad range of specialty applications, the chances are excellent "
        "that an acceptable design will already exist. If not, the CRT is so mature that vendors "
        "working from a proven experience base can design a tube directly to customer "
        "specifications with little in the way of design problems or surprises."))
    b.append(_tbl91_3(
        _T91_3,
        "Table 91.3 · Companies that manufacture cathode ray tubes."))

    b.append(h2("Future Trends in CRT Technology"))
    b.append(p(
        "CRT technology is mature, and the industry does not foresee major surprises on the "
        "horizon. The CRT will continue to evolve, resolution will improve, screens will be "
        "flatter, deflection angles will be larger, and footprints will be reduced. The computer "
        "world continues to demand more resolution. In 1987, the 36-cm (14-in.) VGA class monitor "
        "(640 × 480) with its 300,000 pixels and 16 colors was the new standard. In 1998, the "
        "43-cm (17-in.) desktop monitor is now capable of 1600 × 1200 performance "
        "(1.9 megapixels) with 24-bit color. The 53-cm (21-in.) monitor class, once an expensive "
        "custom device, is also widely available. The trend of increasing resolution and "
        "performance for decreasing cost shows every sign of continuing. The medical community "
        "is quickly moving to monochrome systems with 12-bit gray scale at a resolution of "
        "2560 × 2048 (5 megapixels). All of this means the instrument designer has better "
        "resolution and fidelity for less money."))
    b.append(p(
        "There is a quiet revolution taking place in the information display industry, which may "
        "have a significant effect on CRTs and all information display technology. There is a "
        "design trend to decouple the resolution and fidelity of the display device from its "
        "physical size. There are a number of applications motivating this change: "
        "communications, military, portable computing, simulation, and virtual reality. This is "
        "why miniature CRT technology has been more active in recent years. This is also the "
        "engine driving some of the major competitors to the miniature CRT, such as on-chip "
        "field emission displays (FED), deformable mirror devices (DMD), ferroelectric liquid "
        "crystal integrated circuit displays, and on-chip active matrix liquid crystal display "
        "(LCD) technology. If realized, these promise to be low-cost solutions because they are "
        "built on the technology foundation of the silicon chip industry. These challengers have "
        "the very real potential of eliminating the miniature CRT, and in some application areas, "
        "the LCD panel as well. However, the CRT backed by its formidable 100 years of design "
        "evolution and maturity is not standing still; its assets and market remain impressive. "
        "Although it is one of the few vacuum tubes still in use today, the traditional CRT is "
        "not doomed for obsolescence any time in the immediate future."))

    b.append(h2("References"))
    b.append(refs(_REFS))

    b.append(h2("Further Information"))
    b.append('<ul class="ref-list">%s</ul>' % "".join("<li>%s</li>" % i for i in _FURTHER))

    b.append(h2("Internet Resources"))
    b.append(p(
        "The following is a brief list of places to begin looking on the World Wide Web for "
        "information on CRTs and displays, standards, metrics, and current research. Also many of "
        "the manufacturers listed in Table 91.3 maintain Web sites with useful information."))
    b.append(_web_list(_WEB))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 91 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 91 — %s · Measurement, Instrumentation and Sensors Handbook"
                  % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 91 “Hiển thị ống tia điện tử” của Christopher J. Sherman — "
            "lịch sử CRT, bốn giai đoạn tạo ảnh (tạo chùm tia, hội tụ, làm lệch, biến đổi năng "
            "lượng), quét mành và quét nét, màn huỳnh quang, CRT màu dùng lưới chắn, các kỹ "
            "thuật tạo màu thay thế, chất lượng hình ảnh, tuổi thọ, ưu nhược điểm, chọn CRT và "
            "xu hướng tương lai, với 2 hình, 3 bảng và 28 tài liệu tham khảo." if vi
            else
            "Companion to Chapter 91 of the CRC Measurement Handbook — the history of the CRT, "
            "the four stages of image formation (beam generation, focusing, deflection, energy "
            "conversion), raster versus stroke addressing, the phosphor screen, shadow-mask "
            "colour CRTs, alternative colour techniques, image quality, lifetime, strengths and "
            "weaknesses, tube selection and future trends, with 2 figures, 3 tables and 28 "
            "references.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm '
             'biến</a> · Chương 91' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 91' % BASE_EN)
    meta = ("Chương 91 · theo Ch91.pdf (CRC Press, 1999) · 2 hình, 3 bảng" if vi
            else "Chapter 91 · 2 figures, 3 tables")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE if vi else BYLINE_EN, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 91)))
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
