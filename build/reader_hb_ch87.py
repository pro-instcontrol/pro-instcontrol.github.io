# -*- coding: utf-8 -*-
"""Handbook Chapter 87 — Telemetry.

Albert Lozano-Nieto (Penn State University)

Writes the full Vietnamese translation and the English companion.
Figures: hb87fig.py (87.1–87.11). Tables 87.1–87.3 are printed tables and are
emitted as such. The printed chapter numbers none of its display equations;
they are numbered 87.1–87.15 here, in order of appearance, purely so that the
text can refer to them — this is flagged in the translator's note.

Figure 87.10 could not be transcribed point by point: the printed rows are only
a few pixels tall per transition. It is generated from the definitions the
caption states, which reproduce NRZ-L, NRZ-M, NRZ-S, Biø-L and Biø-M bit for
bit. See the header of hb87fig.py.

Run:  python build/reader_hb_ch87.py
"""
import os

import hb87fig as F87
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch87-telemetry"
TITLE_EN = "Telemetry"
TITLE_VI = "Đo từ xa"
BYLINE = "Albert Lozano-Nieto"
BYLINE_EN = "Albert Lozano-Nieto"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


def fig(num, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = getattr(F87, "fig_87_%d" % num)()
    return ('<figure class="figure" id="fig-87-%d">%s<figcaption class="figcap">%s</figcaption>'
            '</figure>' % (num, svg, cap_vi if lang == "vi" else cap_en))


def p(t):
    return "<p>%s</p>" % t


def h2(t, en=""):
    return '<h2>%s%s</h2>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h3(t, en=""):
    return '<h3>%s%s</h3>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h4(t, en=""):
    return '<h4>%s%s</h4>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def note(t):
    return '<div class="note">%s</div>' % t


def eq(body, num=""):
    if not num:
        return '<div class="eq">%s</div>' % body
    return '<div class="eq"><span class="n">(%s)</span>%s</div>' % (num, body)


def refs(items):
    return '<ol class="ref-list">%s</ol>' % "".join("<li>%s</li>" % i for i in items)


def ul(items):
    return "<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in items)


def _glossary(items):
    o = ['<dl class="glossary">']
    for term, body in items:
        o.append("<dt>%s</dt><dd>%s</dd>" % (term, body))
    o.append("</dl>")
    return "".join(o)


def _frac(num, den, size="0.94em"):
    """A stacked fraction built from two inline-blocks.

    Chapter 87 sets 87.4, 87.6–87.11 and 87.14–87.15 as true two-line
    fractions, so a slash would misrepresent them. No `.frac` class exists in
    library.css and adding one would touch every reader page, so the styling
    stays inline — the same construction chapter 90 uses.
    """
    return ('<span style="display:inline-block;vertical-align:middle;text-align:center;'
            'max-width:100%%;font-size:%s;line-height:1.25;margin:0 0.18em">'
            '<span style="display:block;border-bottom:1.2px solid currentColor;'
            'padding:0 0.4em 2px">%s</span>'
            '<span style="display:block;padding:2px 0.4em 0">%s</span></span>'
            % (size, num, den))


def _big(x, size="1.9"):
    """An oversized delimiter, aligned to the middle of a stacked fraction."""
    return ('<span style="font-size:%sem;vertical-align:middle;line-height:1">%s</span>'
            % (size, x))


def _sub(x):
    return "<sub>%s</sub>" % x


def _sup(x):
    return "<sup>%s</sup>" % x


def _tbl(num, title_vi, title_en, head_vi, head_en, rows, lang="vi",
         minw=520, dense=False, first_row_head=True):
    """One printed table. `rows` holds already-localised cells."""
    cls = "tbl dense" if dense else "tbl"
    head = head_vi if lang == "vi" else head_en
    o = ['<div class="table-wrap"><table class="%s" style="min-width:%dpx">' % (cls, minw)]
    o.append("<caption><b>%s</b> %s</caption>" % (num, title_vi if lang == "vi" else title_en))
    o.append("<thead><tr>%s</tr></thead><tbody>"
             % "".join('<th scope="col">%s</th>' % h for h in head))
    for r in rows:
        cells = []
        for i, c in enumerate(r):
            if i == 0 and first_row_head:
                cells.append('<th scope="row">%s</th>' % c)
            else:
                cells.append("<td>%s</td>" % c)
        o.append("<tr>%s</tr>" % "".join(cells))
    o.append("</tbody></table></div>")
    return "".join(o)


# ================================================================ TABLES
def table_87_1(lang="vi"):
    if lang == "vi":
        head = ["Dải tần, MHz", "Công dụng", "Ghi chú"]
        rows = [
            ["72–76", "Đo sinh học từ xa", "Thiết bị công suất thấp; bị giới hạn bởi Phần 15 "
                                          "quy định của FCC"],
            ["88–108", "Giáo dục", "Bốn tần số trong dải này; Phần 90 quy định của FCC"],
            ["154", "Công nghiệp", "Dải nằm trong các kênh truyền hình 7–13"],
            ["174–216", "Đo sinh học từ xa", "Hoạt động công suất thấp, chỉ trong bệnh viện"],
            ["216–222", "Nhiều dịch vụ", "Băng thông < 200 kHz"],
            ["450–470", "Dùng chung", "Đo từ xa với tư cách thứ cấp; giới hạn 2 W RF"],
            ["467", "Công nghiệp", "Băng nghiệp vụ; giới hạn 2 W RF"],
            ["458–468", "Đo sinh học từ xa", "Dải nằm trong các kênh truyền hình 21–29"],
            ["512–566", "Đo sinh học từ xa", "Hoạt động công suất thấp, chỉ trong bệnh viện"],
            ["1427–1435", "Cố định", "Dùng trong dịch vụ di động mặt đất (đo từ xa và điều "
                                     "khiển từ xa)"],
            ["1435–1535", "Hàng không", ""],
            ["2200–2290", "Di động", ""],
        ]
        title = "Các dải tần được cấp cho đo từ xa"
    else:
        head = ["Frequency band, MHz", "Uses", "Notes"]
        rows = [
            ["72–76", "Biotelemetry", "Low power devices; restricted by Part 15 of FCC rules"],
            ["88–108", "Educational", "Four frequencies in this band; part 90 of FCC rules"],
            ["154", "Industry", "Band in TV channels 7–13"],
            ["174–216", "Biotelemetry", "Low-power operations restricted to hospitals"],
            ["216–222", "Multiple", "BW < 200 kHz"],
            ["450–470", "General", "Telemetry as secondary basis; limited to 2 W of RF"],
            ["467", "Industry", "Business band; limited to 2 W of RF"],
            ["458–468", "Biotelemetry", "Band in TV channels 21–29"],
            ["512–566", "Biotelemetry", "Low-power operations restricted to hospitals"],
            ["1427–1435", "Fixed", "Uses in land mobile services (telemetering and telecommand)"],
            ["1435–1535", "Aeronautical", ""],
            ["2200–2290", "Mobile", ""],
        ]
        title = "Frequency Bands Allocated for Telemetry"
    return _tbl("Bảng 87.1" if lang == "vi" else "Table 87.1", title, title,
                head, head, rows, lang, minw=560, dense=True)


def table_87_2(lang="vi"):
    if lang == "vi":
        head = ["Kênh", "Độ lệch tần, kHz", "Tần số trung tâm thấp nhất, kHz",
                "Tần số trung tâm cao nhất, kHz", "Số kênh", "Khoảng cách giữa các kênh, kHz"]
        title = "Đặc trưng của các kênh băng thông không đổi (CBW) dùng cho FDM"
    else:
        head = ["Channel", "Frequency deviation, kHz", "Lowest channel centre, kHz",
                "Highest channel centre, kHz", "No. of channels", "Separation, kHz"]
        title = "Characteristics of Constant Bandwidth (CBW) Channels for FDM"
    rows = [["A", "±2", "8", "176", "22", "8"],
            ["B", "±4", "16", "352", "22", "16"],
            ["C", "±8", "32", "704", "22", "32"],
            ["D", "±16", "64", "1408", "22", "64"],
            ["E", "±32", "128", "2816", "22", "128"],
            ["F", "±64", "256", "3840", "15", "256"],
            ["G", "±128", "512", "3584", "7", "512"],
            ["H", "±256", "1024", "3072", "4", "1024"]]
    return _tbl("Bảng 87.2" if lang == "vi" else "Table 87.2", title, title,
                head, head, rows, lang, minw=600, dense=True)


def table_87_3(lang="vi"):
    if lang == "vi":
        head = ["Chỉ tiêu", "Cấp I", "Cấp II"]
        rows = [
            ["Khuôn dạng được hỗ trợ", "Cấp I (khuôn dạng đơn giản) hỗ trợ trên mọi bãi thử",
             "Cấp II (khuôn dạng phức tạp) cần sự đồng ý của bãi thử liên quan"],
            ["Cách biểu diễn bit chính (mã PCM)",
             "NRZ-L, NRZ-M, NRZ-S, RNRZ-L, BiØ-L, BiØ-M, BiØ-S", "Như cấp II"],
            ["Tốc độ bit", "10 bit/s đến 5 Mbit/s", "10 bit/s đến trên 5 Mbit/s"],
            ["Độ chính xác và độ ổn định tốc độ bit", "0,1%", "Như cấp I"],
            ["Độ rung bit", "0,1 bit", "Như cấp I"],
            ["Cách đánh số bit", "MSB = bit số 1", "Như cấp I"],
            ["Độ dài từ", "4 đến 16 bit", "4 đến 64 bit"],
            ["Từ bị phân đoạn", "Không cho phép",
             "Tối đa 8 đoạn mỗi từ; mọi đoạn nằm trong cùng một khung nhỏ"],
            ["Độ dài khung nhỏ", "< 8192 bit hoặc < 1024 từ (kể cả đồng bộ)",
             "< 16.384 bit (kể cả đồng bộ)"],
            ["Độ dài khung lớn", "< 256 khung nhỏ", "Như cấp I"],
            ["Cách đánh số khung nhỏ", "Khung nhỏ đầu tiên trong mỗi khung lớn mang số 1",
             "Như cấp I"],
            ["Thay đổi khuôn dạng", "Không cho phép",
             "Cấu trúc khung được chỉ định bởi từ nhận dạng khuôn dạng khung (FFI) trong mọi "
             "khung nhỏ"],
        ]
        title = "Tóm tắt các chỉ tiêu PCM quan trọng nhất theo IRIG 106-96"
    else:
        head = ["Specification", "Class I", "Class II"]
        rows = [
            ["Class format support", "Class I (simple formats) supported on all ranges",
             "Class II (complex formats) requires concurrence of range involved"],
            ["Primary bit representation (PCM codes)",
             "NRZ-L, NRZ-M, NRZ-S, RNRZ-L, BiØ-L, BiØ-M, BiØ-S", "Same as class II"],
            ["Bit rate", "10 bps to 5 Mbps", "10 bps to > 5 Mbps"],
            ["Bit rate accuracy and stability", "0.1%", "Same as class I"],
            ["Bit jitter", "0.1 bit", "Same as class I"],
            ["Bit numbering", "MSB = bit number 1", "Same as class I"],
            ["Word length", "4 to 16 bits", "4 to 64 bits"],
            ["Fragmented words", "Not allowed",
             "Up to 8 segments each; all segments in the same minor frame"],
            ["Minor frame length", "<8192 bits or <1024 words (includes synchro)",
             "<16,384 bits (includes synchro)"],
            ["Major frame length", "<256 minor frames", "Same as class I"],
            ["Minor frame numbering", "First minor frame in each major frame is number 1",
             "Same as class I"],
            ["Format change", "Not allowed",
             "Frame structure is specified by frame format identification (FFI) word in every "
             "minor frame"],
        ]
        title = "Summary of the Most Relevant PCM Specifications According to IRIG 106-96"
    return _tbl("Bảng 87.3" if lang == "vi" else "Table 87.3", title, title,
                head, head, rows, lang, minw=600, dense=True)


# ================================================================ NOTE
def _transnote(lang="vi"):
    if lang == "vi":
        return note(
            "<b>Ghi chú của người dịch.</b> Chương này dịch từ bản in Ch87.pdf của CRC Press "
            "(1999). Bản trích văn bản lấy từ lớp văn bản của file PDF đã làm hỏng toàn bộ phần "
            "công thức — chúng hiện ra thành những cột ký tự rời như “f t tt t = t p [] + () = p "
            "+ () 1 22”. Mọi công thức dưới đây được đọc lại trực tiếp từ ảnh trang 200–300 dpi "
            "và dựng lại bằng HTML. <b>Bản in không đánh số công thức</b>; ở đây chúng được đánh "
            "số (87.1)–(87.15) theo thứ tự xuất hiện chỉ để phần thân bài tiện tham chiếu, và "
            "cách đánh số này là của người dịch, không có trong nguyên bản. "
            "Có mấy chỗ bản in tự mâu thuẫn, xin giữ nguyên và nêu ra đây: "
            "(1) Mục 87.3 viết “Figure 87.7a shows a basic block diagram for an <i>FDM</i> "
            "system”, nhưng hình 87.7a là sơ đồ <i>TDM</i> và cả đoạn văn xung quanh đều nói về "
            "TDM — đây là lỗi in, bản dịch dịch đúng chữ “FDM” và thêm chú thích tại chỗ. "
            "(2) Hình 87.5a ghi cả ba bộ nhân là f<sub>osc1</sub>, trong khi chính hình 87.5b lại "
            "đánh f<sub>osc1</sub>, f<sub>osc2</sub>, f<sub>osc3</sub>. "
            "(3) Hình 87.4 in hai hộp điều chỉnh khác nhau đều là “CONDITIONING CIRCUIT 3”. "
            "(4) Chú thích hình 87.11 viết độ dài cực đại của khung nhỏ là “8192 bit hoặc 512 "
            "với cấp I”, còn phần thân bài và Bảng 87.3 đều viết “< 8192 bit hoặc < 1024 từ” — "
            "hai con số 512 và 1024 không khớp nhau. Cùng chú thích đó ghi 16.284 bit cho cấp II, "
            "trong khi thân bài và Bảng 87.3 ghi 16.384 bit. "
            "(5) Bảng 87.1 xếp hàng 467 <i>trước</i> hàng 458–468, tức không theo thứ tự tăng "
            "dần; bản dịch giữ nguyên thứ tự in. "
            "(6) Chú thích hình 87.10 trong bản trích in “Bif-L”, “Bif-M”, “Bif-S” — đó là chữ "
            "BiØ bị mất ký tự Ø khi trích văn bản, không phải một mã khác. "
            "Cuối cùng, hình 87.10 không thể chép lại từng điểm: các chuyển mức trên bản in chỉ "
            "cao vài pixel. Hình được <i>sinh ra</i> từ đúng các định nghĩa mà chú thích hình "
            "phát biểu, và khớp với bản in ở cả năm mã NRZ-L, NRZ-M, NRZ-S, Biø-L và Biø-M.")
    return note(
        "<b>Translator’s note.</b> Translated from the printed Ch87.pdf of CRC Press (1999). "
        "The PDF’s text layer has destroyed every display equation in this chapter — they come "
        "out as loose columns of characters such as “f t tt t = t p [] + () = p + () 1 22”. All "
        "equations below were re-read from the 200–300 dpi page rasters and rebuilt in HTML. "
        "<b>The printed chapter numbers none of its equations.</b> They are numbered (87.1)–"
        "(87.15) here, in order of appearance, only so that the running text can refer to them; "
        "the numbering is the translator’s and is not in the original. "
        "Several places where the print contradicts itself are kept as printed and flagged: "
        "(1) Section 87.3 says “Figure 87.7a shows a basic block diagram for an <i>FDM</i> "
        "system”, but figure 87.7a is a <i>TDM</i> diagram and the whole surrounding passage is "
        "about TDM — a printed slip; the translation renders the word “FDM” as printed and adds "
        "a note in place. (2) Figure 87.5a labels all three multipliers f<sub>osc1</sub> while "
        "figure 87.5b itself marks f<sub>osc1</sub>, f<sub>osc2</sub>, f<sub>osc3</sub>. "
        "(3) Figure 87.4 prints two different conditioning boxes both as “CONDITIONING CIRCUIT "
        "3”. (4) The caption of figure 87.11 gives the maximum minor-frame length as “8192 bits "
        "or 512 for class I”, while the body text and Table 87.3 both say “< 8192 bits or < 1024 "
        "words” — 512 and 1024 do not agree. The same caption gives 16,284 bits for class II, "
        "where the body and Table 87.3 give 16,384. (5) Table 87.1 lists the 467 MHz row "
        "<i>before</i> the 458–468 MHz row, i.e. out of ascending order; the translation keeps "
        "the printed order. (6) The caption of figure 87.10 appears in the extract as “Bif-L”, "
        "“Bif-M”, “Bif-S” — that is the character Ø lost by the text extraction, not a different "
        "code. Finally, figure 87.10 could not be transcribed point by point: each printed "
        "transition is only a few pixels tall. It is <i>generated</i> from the definitions the "
        "caption states, and matches the print for NRZ-L, NRZ-M, NRZ-S, Biø-L and Biø-M.")


# ================================================================ GLOSSARY
_GLOSS_VI = [
    ("Băng thông", "Khoảng tần số mà một tín hiệu chiếm chỗ."),
    ("Sóng mang", "Một tần số được điều chế bởi tín hiệu mang thông tin."),
    ("Kênh", "Một sóng mang phụ có mang thông tin."),
    ("Kênh băng thông không đổi (CBW)",
     "Kênh có băng thông không phụ thuộc vào tần số sóng mang của nó."),
    ("Tỉ số độ lệch",
     "Tỉ số giữa độ lệch tần số sóng mang cực đại và độ lệch tần số dữ liệu cực đại."),
    ("Độ lệch tần số",
     "Hiệu giữa tần số trung tâm của một sóng mang và giới hạn lệch trên hoặc dưới của nó."),
    ("Ghép kênh theo tần số (FDM)",
     "Một tín hiệu tổng hợp gồm một nhóm sóng mang phụ được sắp xếp sao cho tần số của chúng "
     "không chồng lấn hay gây nhiễu lẫn nhau."),
    ("Đáp ứng tần số",
     "Tần số dữ liệu cao nhất mà kênh có thể mang được."),
    ("IRIG",
     "Nhóm Thiết bị Đo liên bãi thử (Inter-Range Instrumentation Group) thuộc Hội đồng Chỉ huy "
     "Bãi thử (RCC)."),
    ("Kênh băng thông tỉ lệ (PBW)",
     "Kênh có băng thông tỉ lệ với tần số sóng mang của nó."),
    ("Chuyển mạch từ xa",
     "Đo từ xa chỉ gồm các lệnh có/không hoặc bật/tắt."),
    ("Báo hiệu",
     "Đo từ xa gồm thông tin nhị phân."),
    ("Sóng mang phụ",
     "Một sóng mang được ghép với những sóng mang khác để tạo ra tín hiệu tổng hợp."),
    ("Băng thông sóng mang phụ",
     "Hiệu giữa tần số trên và tần số dưới của một sóng mang đã điều chế."),
]

_GLOSS_EN = [
    ("Bandwidth", "The range of frequencies occupied by a signal."),
    ("Carrier", "A frequency that is modulated by a signal containing information."),
    ("Channel", "A subcarrier that carries information."),
    ("Constant bandwidth (CBW) channel",
     "A channel whose bandwidth is independent of its carrier frequency."),
    ("Deviation ratio",
     "The ratio of the maximum carrier frequency deviation to the maximum data frequency "
     "deviation."),
    ("Frequency deviation",
     "The difference between the center frequency of a carrier and its upper or lower deviation "
     "limit."),
    ("Frequency division multiplexing (FDM)",
     "A composite signal consisting of a group of subcarriers arranged so that their frequencies "
     "do not overlap or interfere with each other."),
    ("Frequency response",
     "The highest data frequency that can be carried by the channel."),
    ("IRIG",
     "Inter-Range Instrumentation Group of the Range Commanders Council (RCC)."),
    ("Proportional bandwidth (PBW) channel",
     "A channel whose bandwidth is proportional to its carrier frequency."),
    ("Remote switching", "Telemetry consisting only of yes/no or on/off orders."),
    ("Signaling", "Telemetry consisting of binary information."),
    ("Subcarrier", "A carrier combined with other carriers to create a composite signal."),
    ("Subcarrier bandwidth",
     "The difference between the upper and lower frequencies of a modulated carrier."),
]

# ================================================================ REFERENCES
_REFS = [
    "B.P. Dagarin, R.K. Taenaka, and E.J. Stofel, Galileo probe battery system, <i>IEEE "
    "Aerospace Electron. Syst. Mag.</i>, 11 (6): 6–13, 1996.",
    "M.W. Pollack, Communications-based signaling: advanced capability for mainline railroads, "
    "<i>IEEE Aerospace Electron. Syst. Mag.</i>, 11 (11): 13–18, 1996.",
    "M.C. Shults, R.K. Rhodes, S.J. Updike, B.J. Gilligan, and W.N. Reining, A "
    "telemetry-instrumentation system for monitoring multiple subcutaneously implanted glucose "
    "sensors, <i>IEEE Trans. Biomed. Eng.</i>, 41: 937–942, 1994.",
    "M. Rezazadeh and N.E. Evans, Multichannel physiological monitor plus simultaneous "
    "full-duplex speech channel using a dial-up telephone line, <i>IEEE Trans. Biomed. Eng.</i>, "
    "37: 428–432, 1990.",
    "Y.S. Trisno, P. Hsieh, and D. Wobschall, Optical pulses powered signal telemetry system for "
    "sensor network application, <i>IEEE Trans. Instrum. Meas.</i>, 39: 225–229, 1990.",
    "R. Pallás-Areny and J.G. Webster, <i>Sensors and Signal Conditioning</i>, New York: John "
    "Wiley &amp; Sons, 1991, 352–379.",
    "Part 90: Private land mobile radio services. Subpart J: Non voice and other specialized "
    "operations (Sec. 90.238: Telemetry), <i>Code of Federal Regulations</i>, Title 47, "
    "Telecommunication. Chapter I: Federal Communications Commission.",
    "Part 15: Radio frequency devices, <i>Code of Federal Regulations</i>, Title 47, "
    "Telecommunication. Chapter I: Federal Communications Commission.",
    "H. Taub and D.L. Schilling, <i>Principles of Communication Systems</i>, 2nd ed., New York: "
    "McGraw-Hill, 1986.",
    "IRIG, <i>Telemetry Standard IRIG 106-96</i>, Range Commander Council, U.S. Army White Sands "
    "Missile Range, 1996.",
    "K.M. Uglow, Noise and bandwidth in FM/FM radio telemetry, <i>IRE Trans. Telemetry Remote "
    "Control</i>, 19–22, 1957.",
    "J.L. Maury and J. Styles, Development of optimum frame synchronization codes for Goddard "
    "space flight center PCM telemetry standards, <i>Proc. Natl. Telemetering Conf.</i>, 1964.",
]

_FURTHER_VI = [
    "E.H. Higman, Pneumatic instrumentation, trong B.E. Noltingk (chủ biên), <i>Instrument "
    "Technology: Instrumentation Systems</i>, Tập 4, London: Butterworths, 1987.",
    "C.H. Hoeppner, Telemetry, trong R.C. Dorf (chủ biên), <i>The Electrical Engineering "
    "Handbook</i>, Boca Raton, FL: CRC Press, 1993.",
    "R.S. Mackay, <i>Bio-Medical Telemetry</i>, tái bản lần 2, Piscataway, NJ: IEEE Press, 1993.",
    "Telemetry Group, <i>Test Methods for Telemetry Systems and Subsystems</i>. Tài liệu 118-97, "
    "Range Commanders Council, U.S. Army White Sands Missile Range, 1997.",
    "Telemetry Group, <i>Telemetry Applications Handbook</i>. Tài liệu 119-88, Range Commanders "
    "Council, U.S. Army White Sands Missile Range, 1988.",
]

_FURTHER_EN = [
    "E.H. Higman, Pneumatic instrumentation, in B.E. Noltingk, Ed., <i>Instrument Technology: "
    "Instrumentation Systems</i>, Vol. 4, London: Butterworths, 1987.",
    "C.H. Hoeppner, Telemetry, in R.C. Dorf, Ed., <i>The Electrical Engineering Handbook</i>, "
    "Boca Raton, FL: CRC Press, 1993.",
    "R.S. Mackay, <i>Bio-Medical Telemetry</i>, 2nd ed., Piscataway, NJ: IEEE Press, 1993.",
    "Telemetry Group, <i>Test Methods for Telemetry Systems and Subsystems</i>. Document 118-97, "
    "Range Commanders Council, U.S. Army White Sands Missile Range, 1997.",
    "Telemetry Group, <i>Telemetry Applications Handbook</i>. Document 119-88, Range Commanders "
    "Council, U.S. Army White Sands Missile Range, 1988.",
]


def _pf(n, d):
    """A bracketed stacked fraction — the shape the printed SNR equation uses."""
    return _big("(") + _frac(n, d) + _big(")")


# ================================================================ VI
def body_vi():
    b = []
    b.append(_transnote("vi"))

    # ---------------------------------------------------------- 87.1
    b.append(h2("87.1 Giới thiệu", "Introduction"))
    b.append(p(
        "Đo từ xa là khoa học thu thập thông tin tại một địa điểm ở xa rồi truyền dữ liệu về "
        "một nơi thuận tiện để khảo sát và ghi lại. Có thể thực hiện đo từ xa bằng nhiều cách "
        "khác nhau: quang học, cơ khí, thuỷ lực, điện, v.v. Các phương pháp cơ khí — khí nén hay "
        "thuỷ lực — cho kết quả chấp nhận được ở những khoảng cách ngắn, và được dùng trong môi "
        "trường có mức nhiễu điện từ cao cũng như trong những tình huống mà vì lý do an toàn "
        "không thể dùng tín hiệu điện, chẳng hạn môi trường dễ cháy nổ. Gần đây hơn, các hệ sợi "
        "quang cho phép đo với băng thông rộng và khả năng miễn nhiễm cao với nhiễu và giao "
        "thoa. Một số hệ đo từ xa khác được đề xuất dựa trên siêu âm, ghép điện dung hoặc ghép "
        "từ, và bức xạ hồng ngoại, tuy nhiên những phương pháp này chưa được dùng thường xuyên. "
        "Phần thảo luận trong chương này chỉ giới hạn ở những hệ thống được dùng nhiều nhất: đo "
        "từ xa dựa trên tín hiệu điện. Ưu điểm chính của phương pháp điện so với cơ khí là đo "
        "từ xa bằng điện không có giới hạn thực tế về khoảng cách giữa khu vực đo và khu vực "
        "phân tích, đồng thời có thể dễ dàng thích ứng và nâng cấp trên những cơ sở hạ tầng đã "
        "có. Các phương pháp đo từ xa bằng điện lại được chia tiếp, tuỳ theo kênh truyền mà "
        "chúng dùng, thành đo từ xa có dây và đo từ xa không dây (hay đo từ xa vô tuyến). Đo từ "
        "xa có dây là giải pháp đơn giản nhất về mặt kỹ thuật. Hạn chế của nó là băng thông thấp "
        "và tốc độ truyền thấp. Tuy vậy, nó vẫn được dùng khi dây truyền có thể tận dụng cơ sở "
        "hạ tầng sẵn có, ví dụ phần lớn đường dây điện lực cũng được dùng làm vật mang cho đo "
        "từ xa có dây. Đo từ xa không dây phức tạp hơn vì cần thêm một tầng cao tần (RF) ở cuối. "
        "Dù phức tạp, nó vẫn được dùng rộng rãi vì có thể truyền thông tin đi xa hơn; nhờ vậy nó "
        "được dùng trong những ứng dụng mà khu vực đo thường không tiếp cận được. Nó cũng có "
        "thể truyền với tốc độ cao hơn và đủ dung lượng để truyền nhiều kênh thông tin nếu cần."))
    b.append(fig(1))
    b.append(p(
        "Hình 87.1 trình bày một hệ đo từ xa tổng quát. Hệ gồm (không phải lúc nào cũng có đủ "
        "mọi khối): (1) các đầu đo để chuyển những đại lượng vật lý cần đo thành tín hiệu điện "
        "dễ xử lý; (2) các mạch điều chỉnh để khuếch đại tín hiệu mức thấp từ đầu đo, giới hạn "
        "băng thông của nó và thích ứng mức trở kháng; (3) một mạch xử lý tín hiệu, đôi khi có "
        "thể gộp vào các mạch trước đó; (4) một bộ dao động sóng mang phụ, mà tín hiệu của nó sẽ "
        "bị điều chế bởi đầu ra của các đầu đo khác nhau sau khi đã được xử lý và thích ứng; "
        "(5) một mạch mã hoá — có thể là bộ mã hoá số, bộ điều chế tương tự hoặc bộ điều chế số "
        "— làm cho tín hiệu phù hợp với đặc tính của kênh truyền, tức là một dây dẫn hoặc một "
        "ăng-ten; (6) một máy phát vô tuyến, trong đo từ xa không dây, được điều chế bởi tín "
        "hiệu tổng hợp; (7) một bộ thích ứng trở kháng đường dây, trong trường hợp truyền bằng "
        "dây, để phối hợp trở kháng đặc tính của đường dây với trở kháng ra của các mạch nối vào "
        "bộ thích ứng; và (8) với thông tin không dây, một ăng-ten phát. Đầu thu gồm những khối "
        "tương tự. Với đo từ xa không dây, các khối đó là (1) một ăng-ten thu được thiết kế để "
        "đạt hiệu suất cao nhất trong dải RF đang dùng; (2) một máy thu vô tuyến có sơ đồ giải "
        "điều chế tương thích với sơ đồ điều chế; và (3) các mạch giải điều chế cho từng kênh "
        "đã truyền. Với đo từ xa có dây, ăng-ten và máy thu vô tuyến được thay bằng một khối đầu "
        "vào tổng quát có nhiệm vụ khuếch đại tín hiệu và phối hợp trở kháng đường dây với trở "
        "kháng vào của các mạch phía sau."))
    b.append(p(
        "Việc truyền trong các hệ đo từ xa, đặc biệt là hệ không dây, được thực hiện bằng cách "
        "gửi đi một tín hiệu mà những biến thiên tương tự về biên độ hoặc tần số của nó là một "
        "hàm đã biết của những biến thiên tín hiệu từ các đầu đo. Gần đây hơn, các hệ đo từ xa "
        "số gửi dữ liệu dưới dạng số như một tập hữu hạn các ký hiệu, mỗi ký hiệu biểu diễn một "
        "trong các giá trị hữu hạn có thể có của tín hiệu tổng hợp tại thời điểm nó được lấy "
        "mẫu. Khoảng cách thông tin hiệu dụng trong một hệ không dây bị giới hạn bởi công suất "
        "bức xạ của ăng-ten phát, độ nhạy của máy thu và băng thông của tín hiệu RF. Khi băng "
        "thông tăng lên, phần đóng góp của nhiễu vào tín hiệu tổng cũng tăng, và do đó cần nhiều "
        "công suất phát hơn để giữ nguyên tỉ số tín hiệu trên nhiễu (SNR). Đây là một trong "
        "những hạn chế chính của các hệ đo từ xa không dây. Trong một số ứng dụng, việc truyền "
        "tới máy thu được thực hiện ở băng gốc, ngay sau các mạch điều chỉnh. Ưu điểm của hệ đo "
        "từ xa băng gốc là sự đơn giản, tuy vậy vì truyền ở băng gốc nên chúng thường chỉ giới "
        "hạn ở một kênh với tốc độ thấp."))
    b.append(p(
        "Không hiếm khi một hệ đo lường cần thu nhận hoặc những loại tín hiệu khác nhau, hoặc "
        "cùng một loại dữ liệu tại những vị trí khác nhau trong quá trình đang được giám sát. "
        "Những tín hiệu thông tin khác nhau này có thể được truyền trên cùng một sóng mang chung "
        "bằng cách ghép kênh các tín hiệu dữ liệu. Ghép kênh cho phép nhiều tín hiệu khác nhau "
        "chia sẻ cùng một kênh. Các kỹ thuật ghép kênh thường được xếp vào hai loại: ghép kênh "
        "theo tần số (FDM) và ghép kênh theo thời gian (TDM). Trong FDM, những tần số sóng mang "
        "phụ khác nhau bị điều chế bởi tín hiệu của các kênh đo khác nhau, khiến phổ thông tin "
        "dịch từ băng gốc lên tần số sóng mang phụ. Sau đó các tần số sóng mang phụ này lại điều "
        "chế sóng mang RF, cho phép truyền đồng thời mọi kênh đo mong muốn. Trong TDM, toàn bộ "
        "kênh được giao trọn cho từng kênh đo, nhưng chỉ trong một phần thời gian. Các kỹ thuật "
        "TDM dùng điều chế số để lấy mẫu những kênh đo khác nhau ở những thời điểm khác nhau; "
        "các mẫu này sau đó được đưa tuần tự vào điều chế sóng mang RF. Hình 87.2 minh hoạ những "
        "khái niệm này bằng đồ thị tần số và đồ thị thời gian cho FDM và TDM."))
    b.append(fig(2))
    b.append(p(
        "Hầu như mọi tình huống đo lường và thiết bị đo đều là ứng viên cho việc dùng một tuyến "
        "đo từ xa. Đo từ xa được dùng rộng rãi trong các ứng dụng vũ trụ, hoặc để đo từ xa một "
        "đại lượng ở nơi xa, hoặc để điều khiển từ xa các cơ cấu chấp hành. Trong phần lớn những "
        "ứng dụng loại này, ví dụ đo từ xa vũ trụ, việc thiết kế hệ đo từ xa sao cho tiêu thụ "
        "công suất ít nhất là rất quan trọng [1]. Một số phương tiện di động trên mặt đất như tàu "
        "hoả cũng dùng hệ đo từ xa, hoặc không dây, hoặc tận dụng một phần dây điện lực sẵn có, "
        "để truyền dữ liệu về trạm trung tâm và nhận lệnh từ đó [2]. Trong thực hành lâm sàng, "
        "đo từ xa cho bệnh nhân làm tăng chất lượng cuộc sống và khả năng vận động của họ, vì "
        "bệnh nhân không cần nối vào một hệ đo lường để được theo dõi. Một số ứng dụng y tế dựa "
        "trên việc cấy một cảm biến vào bệnh nhân rồi truyền dữ liệu để phân tích và xử lý tiếp, "
        "hoặc bằng vô tuyến [3], hoặc qua đường điện thoại được thích ứng [4] từ trạm thu. Cảm "
        "biến quang và thông tin sợi quang được dùng trong công nghiệp để đo trong những môi "
        "trường không nên có tín hiệu điện, chẳng hạn môi trường dễ cháy nổ [5]. Người thiết kế "
        "hệ đo từ xa cũng cần lưu tâm tới những điều kiện mà hệ sẽ phải làm việc. Trong phần lớn "
        "ứng dụng, hệ đo từ xa phải làm việc lặp đi lặp lại mà không cần chỉnh hay hiệu chuẩn "
        "trong một dải nhiệt độ rộng. Cuối cùng, khi ngày càng nhiều hệ đo từ xa được phát "
        "triển, nhu cầu cho phép trao đổi lẫn nhau giữa các phép thử ở mọi dải đo cũng tăng "
        "lên, kéo theo yêu cầu về tính tương thích của thiết bị phát, thu và xử lý tín hiệu ở "
        "mọi dải. Vì lý do đó, Ban Nghiên cứu và Phát triển của Bộ Quốc phòng đã lập Uỷ ban Tên "
        "lửa có điều khiển, và uỷ ban này thành lập Nhóm công tác về Đo từ xa. Nhóm này sau đó "
        "trở thành Nhóm Thiết bị Đo liên bãi thử (IRIG), và IRIG đã xây dựng các Tiêu chuẩn Đo "
        "từ xa. Ngày nay, tiêu chuẩn IRIG 106-96 là tiêu chuẩn đo từ xa chính được cả chính phủ "
        "và công nghiệp dùng trên toàn thế giới."))

    # ---------------------------------------------------------- 87.2
    b.append(h2("87.2 Đo từ xa băng gốc", "Base-Band Telemetry"))
    b.append(p(
        "Đo từ xa băng gốc dùng một đường dây để trao đổi với phía thu tín hiệu từ đầu đo sau "
        "khi tín hiệu đã được xử lý và điều chỉnh. Dưới đây chúng ta mô tả vắn tắt các hệ đo từ "
        "xa dựa trên biên độ hoặc trên tần số. Những nghiên cứu sâu hơn về các hệ đo từ xa băng "
        "gốc này có thể tìm ở Tài liệu tham khảo 6."))

    b.append(h3("Đo từ xa băng gốc theo biên độ", "Base-Band Telemetry Based on Amplitude"))
    b.append(h4("Đo từ xa băng gốc theo điện áp", "Voltage-Based Base-Band Telemetry"))
    b.append(p(
        "Hình 87.3a cho thấy một hệ đo từ xa theo điện áp đơn giản. Tín hiệu từ đầu đo được "
        "khuếch đại, thường lên mức điện áp trong khoảng 1 đến 15 V, rồi được gửi qua một đường "
        "dây hai sợi tới phía thu. Nhờ đặt đầu dưới của thang đo ở 1 V, hệ này có thể phát hiện "
        "ngắn mạch [6]. Vấn đề chính của cấu hình này là giới hạn về khoảng cách truyền, phụ "
        "thuộc vào điện trở đường dây và điện trở vào của phía thu. Ngoài ra, các dây nối tạo "
        "thành một vòng rất dễ bị nhiễu từ những tín hiệu ký sinh."))
    b.append(fig(3))
    b.append(h4("Đo từ xa băng gốc theo dòng điện", "Current-Based Base-Band Telemetry"))
    b.append(p(
        "Hạn chế về khoảng cách truyền của hệ theo điện áp, do trở kháng đường dây gây ra, được "
        "khắc phục bằng cách dùng tín hiệu dòng điện thay cho điện áp, như trên Hình 87.3b. Cách "
        "này cần thêm một mô-đun chuyển đổi từ điện áp sang dòng điện sau các mạch xử lý tín "
        "hiệu. Ở phía thu, tín hiệu được phát hiện bằng cách đo điện áp trên một điện trở. Hệ "
        "được dùng nhiều nhất trong công nghiệp là vòng dòng 4 đến 20 mA. Điều đó có nghĩa là "
        "0 V được truyền đi thành 4 mA, còn giá trị điện áp cao nhất được truyền thành dòng "
        "20 mA. Ưu điểm của việc truyền 4 mA cho 0 V là có thể dễ dàng phát hiện đứt mạch trong "
        "vòng (0 mA). Những giá trị dòng chuẩn khác là 0 đến 5, 0 đến 20, 10 đến 50, 1 đến 5 và "
        "2 đến 10 mA. Ngoài ra, sụt áp do điện trở của dây không ảnh hưởng tới tín hiệu đã truyền, "
        "nhờ vậy có thể dùng dây mảnh hơn. Vì đây là chế độ dòng, những điện áp ký sinh cảm ứng "
        "trên đường dây cũng không ảnh hưởng tới tín hiệu. Đo từ xa theo dòng cho phép dùng bộ "
        "phát nối đất hoặc bộ phát thả nổi mà chỉ cần ít sửa đổi [6]."))

    b.append(h3("Đo từ xa băng gốc theo tần số", "Base-Band Telemetry Based on Frequency"))
    b.append(p(
        "Truyền theo tần số được biết là có khả năng miễn nhiễm với nhiễu cao hơn truyền theo "
        "biên độ. Đo từ xa theo tần số, như trên Hình 87.3c, được dùng khi có giao thoa điện cảm "
        "hoặc điện dung, nhờ khả năng miễn nhiễm nhiễu của nó. Nó cũng mở ra khả năng cách ly "
        "phía thu khỏi phía phát. Tín hiệu ở đầu ra của mạch điều chỉnh làm thay đổi tần số của "
        "tín hiệu đo từ xa, thường nhờ một bộ chuyển đổi điện áp sang tần số. Ở phía thu, một bộ "
        "chuyển đổi tần số sang điện áp thực hiện chức năng ngược lại. Một trường hợp đặc biệt "
        "của đo từ xa theo tần số là đo từ xa xung, trong đó tín hiệu điều chế làm thay đổi một "
        "số đặc tính của một chuỗi xung. Vì tầm quan trọng và mức độ dùng rộng rãi của nó, đo từ "
        "xa xung sẽ được phân tích kỹ trong các mục tiếp theo."))

    # ---------------------------------------------------------- 87.3
    b.append(h2("87.3 Đo từ xa nhiều kênh", "Multiple-Channel Telemetry"))
    b.append(p(
        "Phần lớn các quá trình công nghiệp có dùng đo từ xa đòi hỏi phải đo nhiều đại lượng vật "
        "lý khác nhau để điều khiển quá trình, hoặc đo chỉ một đại lượng vật lý tại nhiều vị trí "
        "khác nhau, hoặc — thường là — kết hợp cả hai. Trong những phép đo nhiều kênh như vậy, "
        "đo từ xa băng gốc không còn là một lựa chọn, vì sẽ phải xây một hệ riêng cho từng kênh. "
        "Đo từ xa nhiều kênh đạt được bằng cách chia sẻ một tài nguyên chung (kênh truyền), như "
        "trên Hình 87.4. Việc chia sẻ kênh truyền cho mọi kênh đo được gọi là ghép kênh. Có hai "
        "kỹ thuật ghép kênh cơ bản: FDM và TDM. Trong FDM, các kênh khác nhau được gán cho những "
        "dải phổ khác nhau và tín hiệu tổng hợp được truyền qua kênh thông tin. Trong TDM, thông "
        "tin của các kênh khác nhau được truyền tuần tự qua kênh thông tin."))
    b.append(fig(4))

    b.append(h3("Ghép kênh theo tần số", "Frequency Division Multiplexing"))
    b.append(p(
        "Trong FDM, như trên Hình 87.5a, mỗi kênh đo điều chế một tín hiệu hình sin có tần số "
        "khác nhau. Những tín hiệu hình sin này được gọi là sóng mang phụ. Mỗi tín hiệu đã điều "
        "chế sau đó được lọc thấp để bảo đảm tuân thủ các giới hạn băng thông. Sau khâu lọc, mọi "
        "tín hiệu đã điều chế được đưa vào một khối cộng, tạo ra cái được gọi là tín hiệu băng "
        "gốc. “Băng gốc” ở đây có nghĩa là sóng mang cuối cùng chưa bị điều chế. Phổ của tín "
        "hiệu băng gốc được trình bày trên Hình 87.5b, ở đó có thể thấy mỗi kênh đo được cấp một "
        "tần số riêng cho phổ của mình. Tín hiệu tổng hợp này cuối cùng điều chế một sóng mang có "
        "tần số tuỳ thuộc vào môi trường truyền được dùng. Tín hiệu sau đó được đưa vào một dây "
        "truyền (tương tự các hệ truyền hình cáp) hoặc, thông dụng hơn, vào một ăng-ten trong "
        "trường hợp hệ đo từ xa không dây. Trong đo từ xa không dây, không thể chọn tuỳ ý tần số "
        "sóng mang mà phải chọn theo những thoả thuận quốc tế về việc sử dụng phổ điện từ. Ở Hoa "
        "Kỳ, Uỷ ban Truyền thông Liên bang (FCC) là cơ quan quy định việc phân bổ tần số cho các "
        "dịch vụ thông tin khác nhau. Bảng 87.1 liệt kê những dải tần đo từ xa thông dụng nhất "
        "và mục đích sử dụng của chúng. Bảng 87.1 chỉ nhằm mục đích tham khảo và không phải là "
        "một chỉ dẫn toàn diện về tần số đo từ xa. Để biết những tần số đo từ xa được phép dùng "
        "cho một ứng dụng cụ thể, công suất tối đa được phép và những hạn chế khác, bạn đọc nên "
        "tham khảo các tài liệu áp dụng của FCC [7,8]."))
    b.append(table_87_1("vi"))
    b.append(fig(5))
    b.append(p(
        "Việc phân bổ các dải tần là một quá trình có thể thay đổi. Ví dụ, tháng 10 năm 1997 "
        "FCC đã giao một phần các dải kênh truyền hình cho đo từ xa bệnh nhân trong bệnh viện, "
        "với công suất bị hạn chế. FCC công bố mọi thay đổi ảnh hưởng tới dải tần hoặc những đặc "
        "tính kỹ thuật khác của đo từ xa."))
    b.append(p(
        "Ở phía thu, bộ giải điều chế sóng mang phát hiện và khôi phục tín hiệu băng gốc tổng "
        "hợp. Bước tiếp theo là tách từng sóng mang phụ ra bằng cách đưa tín hiệu vào một dãy "
        "các bộ lọc dải song song. Mỗi kênh sau đó được giải điều chế tiếp để khôi phục thông "
        "tin từ đầu đo. Vấn đề thực tế chính của các hệ FDM là xuyên nhiễu giữa các kênh. Xuyên "
        "nhiễu xuất hiện do tính phi tuyến của các linh kiện điện tử: tín hiệu của một kênh điều "
        "chế một phần một sóng mang phụ khác ngoài sóng mang phụ đã gán cho kênh đó. Xuyên nhiễu "
        "cũng xuất hiện khi phổ của hai kênh liền kề chồng lấn lên nhau. Để tránh hiệu ứng này, "
        "phải chọn các sóng mang phụ sao cho có một khoảng cách (dải bảo vệ) giữa phổ của hai "
        "kênh liền kề. Tăng dải bảo vệ thì khả năng xuyên nhiễu giảm, nhưng băng thông hiệu dụng "
        "cũng tăng lên. Băng thông hiệu dụng bằng tổng băng thông của mọi kênh cộng với tổng của "
        "mọi dải bảo vệ."))
    b.append(p(
        "Với mỗi quá trình điều chế trong hai quá trình — điều chế tín hiệu của các kênh đo và "
        "điều chế tín hiệu tổng hợp — đều có ba phương pháp thay thế: điều chế biên độ (AM), "
        "điều chế tần số (FM) và điều chế pha (PM). Những tổ hợp thường dùng là FM/FM, FM/PM hoặc "
        "AM/FM [6]. Ở đây chúng ta chỉ phân tích các sơ đồ điều chế sóng mang phụ; việc điều chế "
        "tín hiệu RF được phân tích ở Chương 81."))

    b.append(h4("Điều chế sóng mang phụ theo biên độ",
                "Subcarrier Modulation of Amplitude"))
    b.append(p(
        "Trong một sơ đồ điều chế sóng mang phụ kiểu AM, biên độ của một sóng mang phụ cụ thể "
        "được thay đổi theo giá trị của kênh đo đã gán cho tần số đó. Tín hiệu AM thu được là"))
    b.append(eq("<i>v</i>(<i>t</i>) = <i>A</i><sub>c</sub>[1 + <i>m</i>(<i>t</i>)] "
                "cos(ω<sub>c</sub><i>t</i>)", "87.1"))
    b.append(p(
        "trong đó <i>A</i><sub>c</sub> là biên độ của sóng mang, <i>m</i>(<i>t</i>) là tín hiệu "
        "điều chế và ω<sub>c</sub> là tần số của sóng mang. Ưu điểm của kiểu điều chế này là sự "
        "đơn giản của các mạch thực hiện điều chế cũng như của các mạch cần cho việc giải điều "
        "chế, nhằm khôi phục tín hiệu điều chế mang thông tin mong muốn. Phần trăm điều chế biểu "
        "thị mức độ mà một sóng mang đã bị điều chế biên độ. Giả sử cho đơn giản rằng tín hiệu "
        "điều chế là hình sin có tần số ω<sub>m</sub>, tức là"))
    b.append(eq("<i>m</i>(<i>t</i>) = <i>m</i> × cos(ω<sub>m</sub><i>t</i>)", "87.2"))
    b.append(p("thì phần trăm điều chế (<i>P</i>) được tính là"))
    b.append(eq("<i>P</i> = <i>m</i> × 100 (%)", "87.3"))
    b.append(p("Một cách tổng quát hơn, phần trăm điều chế (<i>P</i>) được biểu diễn là"))
    b.append(eq(_frac("<i>P</i>", "100%") + " = " +
                _frac("<i>A</i><sub>c(max)</sub> − <i>A</i><sub>c(min)</sub>",
                      "2<i>A</i><sub>c</sub>"), "87.4"))
    b.append(p(
        "trong đó <i>A</i><sub>c(max)</sub> và <i>A</i><sub>c(min)</sub> là những giá trị lớn "
        "nhất và nhỏ nhất mà tín hiệu sóng mang đạt tới."))
    b.append(fig(6))
    b.append(p(
        "Hình 87.6 trình bày phổ của một tín hiệu đã điều chế biên độ, giả sử tín hiệu điều chế "
        "là một tín hiệu không tuần hoàn, bị giới hạn băng và có năng lượng hữu hạn. Hình 87.6 "
        "cho thấy phổ gồm hai dải bên đối xứng qua sóng mang phụ. Hình 87.6 cũng cho thấy những "
        "nhược điểm chính của các sơ đồ AM. Thứ nhất, băng thông của kênh đã điều chế bằng hai "
        "lần băng thông của tín hiệu điều chế, do có hai dải bên giống nhau; điều này dẫn tới "
        "việc dùng phổ kém hiệu quả. Thứ hai, việc phân tích công suất của từng thành phần trên "
        "Hình 87.6 cho thấy ít nhất 50% công suất phát được dùng để phát chính sóng mang phụ, mà "
        "sóng mang này không phụ thuộc vào tín hiệu đo vì nó không mang thông tin nào. Phần công "
        "suất còn lại được chia cho hai dải bên, khiến hiệu suất cực đại mà về lý thuyết có thể "
        "đạt được thấp hơn 25%. Vấn đề chính thứ ba của AM là khả năng điều chế quá mức, xảy ra "
        "khi <i>m</i> > 1. Một khi tín hiệu đã bị điều chế quá mức thì không thể khôi phục tín "
        "hiệu điều chế bằng những mạch đơn giản vốn được dùng rộng rãi cho truyền đo từ xa AM."))
    b.append(p(
        "Có thể khắc phục những hạn chế của điều chế sóng mang phụ kiểu AM bằng các kỹ thuật "
        "điều chế hiệu quả hơn như hai dải bên (DSB), một dải bên (SSB) và một dải bên tương "
        "thích (CSSB) — cũng được coi là các kỹ thuật AM. Tuy nhiên, sự phức tạp của những hệ "
        "điều chế này cùng chi phí của các hệ có khả năng khôi phục tín hiệu sóng mang phụ được "
        "điều chế theo cách đó khiến chúng không được dùng trong phần lớn các hệ đo từ xa thương "
        "mại. Phần lớn các hệ hiện có dùng kỹ thuật sóng mang phụ AM đều dùng kiểu AM truyền "
        "thống đã mô tả ở đây, vì sự đơn giản của nó bù lại được những vấn đề có thể gặp khi "
        "dùng."))

    b.append(h4("Điều chế sóng mang phụ theo tần số",
                "Subcarrier Modulation of Frequency"))
    b.append(p(
        "FM (hoặc PM) cho tới nay là sơ đồ điều chế sóng mang phụ được dùng nhiều nhất trong các "
        "hệ đo từ xa FDM. Những kiểu điều chế góc này về bản chất là phi tuyến, trái với AM. Có "
        "thể biểu diễn điều chế góc là"))
    b.append(eq("<i>v</i>(<i>t</i>) = <i>A</i> cos[ω<sub>c</sub><i>t</i> + φ(<i>t</i>)]", "87.5"))
    b.append(p(
        "trong đó φ(<i>t</i>) là tín hiệu điều chế, tức là tín hiệu từ các đầu đo sau khi đã "
        "được điều chỉnh."))
    b.append(p("Từ đó có thể tính giá trị của tần số tức thời là"))
    b.append(eq("<i>f</i> = " + _frac("1", "2π") + " " + _frac("d", "d<i>t</i>") +
                "[ω<sub>c</sub><i>t</i> + φ(<i>t</i>)] = " +
                _frac("ω<sub>c</sub>", "2π") + " + " + _frac("d", "d<i>t</i>") + "φ(<i>t</i>)",
                "87.6"))
    b.append(p(
        "Phương trình này cho thấy tín hiệu <i>v</i>(<i>t</i>) được điều chế tần số như thế nào. "
        "Từ các phương trình trên có thể rút ra hai tham số: độ lệch tần số và chỉ số điều chế. "
        "Độ lệch tần số (<i>f</i><sub>m</sub>) là mức lệch lớn nhất của tần số tức thời so với "
        "tần số sóng mang. Chỉ số điều chế (β) là độ lệch pha lớn nhất. Những phương trình sau "
        "cho thấy các tham số này liên hệ với nhau ra sao. Giá trị của tần số tức thời "
        "(<i>f</i>) là [9]"))
    b.append(eq("<i>f</i> = " + _frac("ω<sub>c</sub>", "2π") + " + " +
                _frac("βω<sub>m</sub>", "2π") + " cos(ω<sub>m</sub><i>t</i>) = " +
                "<i>f</i><sub>c</sub> + β<i>f</i><sub>m</sub> cos(ω<sub>m</sub><i>t</i>)",
                "87.7"))
    b.append(p("Độ lệch tần số cực đại là Δ<i>f</i> và được cho bởi"))
    b.append(eq("Δ<i>f</i> = β<i>f</i><sub>m</sub>", "87.8"))
    b.append(p("Do đó có thể viết phương trình của tín hiệu đã điều chế tần số là"))
    b.append(eq("<i>v</i>(<i>t</i>) = <i>A</i> cos[ω<sub>c</sub><i>t</i> + " +
                _frac("Δ<i>f</i>", "<i>f</i><sub>m</sub>") + " sin(ω<sub>m</sub><i>t</i>)]",
                "87.9"))
    b.append(p(
        "Phương trình trên cho thấy tần số tức thời <i>f</i> nằm trong khoảng "
        "<i>f</i><sub>c</sub> ± Δ<i>f</i>. Tuy vậy, điều đó không có nghĩa là mọi thành phần phổ "
        "đều nằm trong khoảng này. Không thể viết phổ của một dạng sóng đã điều chế góc bằng một "
        "phương trình đơn giản. Trong trường hợp đơn giản nhất, khi tín hiệu điều chế là một tín "
        "hiệu hình sin, một quy tắc thực hành phát biểu rằng băng thông của một tín hiệu FM bằng "
        "hai lần tổng của độ lệch tần số cực đại và tần số điều chế. Với những tín hiệu điều chế "
        "thường gặp trong các hệ đo, băng thông phụ thuộc vào chỉ số điều chế; nghĩa là, vì băng "
        "thông cấp cho mỗi kênh là hữu hạn, chỉ số điều chế cũng sẽ bị giới hạn."))

    b.append(h3("Tiêu chuẩn đo từ xa ghép kênh theo tần số",
                "Frequency Division Multiplexing Telemetry Standards"))
    b.append(p(
        "IRIG 106-96 là tiêu chuẩn được dùng nhiều nhất cho các hệ đo từ xa, thu nhận dữ liệu và "
        "ghi dữ liệu quân sự cũng như thương mại của chính phủ và công nghiệp trên toàn thế giới "
        "[10]. Tiêu chuẩn này công nhận hai kiểu khuôn dạng cho FM trong các hệ FDM: điều chế "
        "băng thông tỉ lệ (PBW) và điều chế băng thông không đổi (CBW). Tiêu chuẩn cũng cho phép "
        "kết hợp các kênh PBW và CBW. Trong PBW, băng thông của một kênh tỉ lệ với tần số sóng "
        "mang phụ. Tiêu chuẩn công nhận ba loại độ lệch sóng mang phụ: 7,5; 15 và 30%. Có 25 "
        "kênh PBW với độ lệch 7,5%, đánh số từ 1 đến 25. Kênh thấp nhất có tần số trung tâm "
        "400 Hz, nghĩa là giới hạn lệch dưới là 370 Hz và giới hạn lệch trên là 430 Hz. Kênh cao "
        "nhất (kênh 25) có tần số trung tâm 560.000 Hz (lệch từ 518.000 đến 602.000 Hz). Các tần "
        "số trung tâm được chọn sao cho tỉ số giữa giới hạn lệch trên của một kênh và giới hạn "
        "lệch dưới của kênh kế tiếp vào khoảng 1,2. Có 12 kênh PBW với độ lệch 15%, ký hiệu A, "
        "B, … L. Tần số trung tâm của kênh thấp nhất là 22.000 Hz (lệch từ 18.700 Hz đến "
        "25.300 Hz), còn tần số trung tâm của kênh cao nhất là 560.000 Hz (476.000 đến "
        "644.000 Hz), với tỉ số giữa tần số trung tâm của hai kênh kề nhau khoảng 1,3. Ngoài ra "
        "còn có 12 kênh PBW với độ lệch 30%, ký hiệu từ AA, BB, … đến LL. Tần số trung tâm của "
        "những kênh này giống như của các kênh 15%."))
    b.append(p(
        "Các kênh CBW giữ băng thông không đổi, độc lập với tần số sóng mang của chúng. Có tám "
        "mức lệch tần số sóng mang phụ cực đại, ký hiệu từ A (độ lệch 2 kHz) đến H (độ lệch "
        "256 kHz). Độ lệch tần số tăng gấp đôi từ nhóm này sang nhóm kế tiếp. Có 22 kênh A, với "
        "tần số trung tâm trải từ 8 đến 176 kHz. Khoảng cách giữa các kênh kề nhau là một hằng "
        "số 8 kHz. Bảng 87.2 tóm tắt các đặc trưng của các kênh CBW."))
    b.append(table_87_2("vi"))
    b.append(p(
        "IRIG 106-96 đưa ra trong phần phụ lục những tiêu chí cho việc dùng các tiêu chuẩn FDM. "
        "Phần này tập trung vào các giới hạn — phần lớn phụ thuộc vào phần cứng được dùng — và "
        "vào những đánh đổi về hiệu năng như độ chính xác dữ liệu theo băng thông dữ liệu mà "
        "việc triển khai hệ có thể đòi hỏi. Tỉ số độ lệch sóng mang phụ quyết định SNR của một "
        "kênh. Theo một quy tắc kinh nghiệm, SNR biến thiên theo luỹ thừa ba phần hai của tỉ số "
        "độ lệch sóng mang phụ. Mặt khác, số kênh sóng mang phụ có thể dùng đồng thời để điều "
        "chế một sóng mang RF bị giới hạn bởi băng thông kênh của sóng mang RF cũng như bởi các "
        "yếu tố SNR. Với một băng thông RF hữu hạn, càng thêm nhiều kênh vào hệ FDM thì càng "
        "phải giảm tỉ số độ lệch của mỗi kênh, và điều đó làm giảm SNR của mỗi kênh. Vì vậy, "
        "việc đánh giá sự đánh đổi chấp nhận được giữa số kênh sóng mang phụ và các giá trị SNR "
        "chấp nhận được là rất quan trọng. Một phương trình tổng quát có thể dùng để ước lượng "
        "hiệu năng tạp âm nhiệt của một kênh FM/FM là như sau [11]:"))
    b.append(eq(_pf("S", "N") + "<sub>d</sub> = " + _pf("S", "N") + "<sub>c</sub> " +
                _big("(") + _frac("3", "4") + _big(")") + "<sup>1/2</sup> " +
                _pf("<i>B</i><sub>c</sub>", "<i>F</i><sub>ud</sub>") +
                _pf("<i>f</i><sub>dc</sub>", "<i>f</i><sub>s</sub>") +
                _pf("<i>f</i><sub>ds</sub>", "<i>F</i><sub>ud</sub>"), "87.10"))
    b.append(p(
        "trong đó (S/N)<sub>d</sub> là SNR ở đầu ra bộ tách sóng, (S/N)<sub>c</sub> là SNR của "
        "máy thu, <i>B</i><sub>c</sub> là băng thông trung tần của máy thu, "
        "<i>F</i><sub>ud</sub> là bộ lọc đầu ra của bộ tách sóng sóng mang phụ (tại −3 dB), "
        "<i>f</i><sub>s</sub> là tần số trung tâm của sóng mang phụ, <i>f</i><sub>dc</sub> là độ "
        "lệch đỉnh của sóng mang đối với sóng mang phụ đang xét, và <i>f</i><sub>ds</sub> là độ "
        "lệch đỉnh của sóng mang phụ."))
    b.append(p(
        "Theo tiêu chuẩn, tín hiệu FDM tổng hợp FM/FM dùng để điều chế một sóng mang RF có thể "
        "theo khuôn dạng PBW, khuôn dạng CBW hoặc kết hợp cả hai, với điều kiện duy nhất là các "
        "dải bảo vệ giữa những kênh dùng trong khuôn dạng hỗn hợp phải bằng hoặc lớn hơn dải bảo "
        "vệ của chính những kênh đó trong khuôn dạng không hỗn hợp."))

    b.append(h3("Ghép kênh theo thời gian", "Time Division Multiplexing"))
    b.append(p(
        "TDM là một kỹ thuật truyền chia thời gian thành những khe khác nhau và gán một khe cho "
        "mỗi kênh đo. Trong TDM, toàn bộ băng thông truyền được giao trọn cho từng kênh đo trong "
        "một phần thời gian. Sau khi tín hiệu từ các kênh đo đã được lọc thấp, chúng được lấy "
        "mẫu tuần tự bằng một chuyển mạch số, chuyển mạch này lấy mẫu mọi kênh đo trong một "
        "khoảng thời gian (<i>T</i>) thoả mãn định lý Nyquist. Hình 87.7a trình bày một sơ đồ "
        "khối cơ bản cho một hệ FDM.<sup>1</sup> Đầu ra của bộ lấy mẫu là một chuỗi xung AM chứa các mẫu "
        "riêng lẻ của từng kênh, được gói thành khung một cách tuần hoàn, như trên Hình 87.7b. "
        "Cuối cùng, tín hiệu tổng hợp điều chế một sóng mang RF. Tập hợp các mẫu của mỗi kênh "
        "vào được gọi là một khung. Với M kênh đo, khoảng thời gian giữa hai xung liên tiếp là "
        "<i>T</i><sub>s</sub>/M = 1/M<i>f</i><sub>s</sub>, trong đó <i>T</i><sub>s</sub> là chu "
        "kỳ lấy mẫu. Khoảng thời gian giữa hai mẫu của cùng một kênh là "
        "<i>T</i><sub>s</sub>. Ở phía thu, nhờ tách các tín hiệu số ra thành từng kênh bằng một "
        "bộ tách kênh được đồng bộ và nhờ lọc thấp, có thể khôi phục tín hiệu gốc của từng kênh "
        "đo."))
    b.append(note(
        "[^1] Bản in ghi “FDM” ở câu này, nhưng hình 87.7a là sơ đồ TDM và cả đoạn văn đều nói "
        "về TDM. Bản dịch giữ đúng chữ đã in và ghi chú lại — xem ghi chú của người dịch ở đầu "
        "chương."))
    b.append(fig(7))
    b.append(p(
        "Các hệ TDM có ưu điểm so với các hệ FDM. Thứ nhất, FDM cần bộ điều chế và bộ giải điều "
        "chế sóng mang phụ cho từng kênh, trong khi TDM chỉ cần một bộ ghép kênh và một bộ tách "
        "kênh. Thứ hai, tín hiệu TDM có khả năng chống lại những nguồn sai số gây ra xuyên nhiễu "
        "trong FDM: lọc không lý tưởng và điều chế tương hỗ do tính phi tuyến. Trong TDM, việc "
        "tách các kênh phụ thuộc vào hệ lấy mẫu. Tuy nhiên, vì trên thực tế không thể tạo ra xung "
        "vuông hoàn hảo, thời gian lên và xuống của xung khác không. Do đó cần có thời gian bảo "
        "vệ giữa các xung, tương tự các dải bảo vệ trong hệ FDM. Có thể ước lượng dễ dàng xuyên "
        "nhiễu trong TDM nếu giả sử xung tắt theo hàm mũ với hằng số thời gian (τ) xấp xỉ bằng"))
    b.append(eq("τ = " + _frac("1", "2π<i>B</i>"), "87.11"))
    b.append(p(
        "trong đó <i>B</i> là băng thông kênh tại −3 dB. Xuyên nhiễu (<i>k</i>) giữa các kênh có "
        "thể được xấp xỉ bằng"))
    b.append(eq("<i>k</i> = −54,5<i>T</i><sub>g</sub> (dB)", "87.12"))
    b.append(p(
        "trong đó <i>T</i><sub>g</sub> là khoảng thời gian tách biệt nhỏ nhất giữa các kênh, được "
        "gọi là thời gian bảo vệ."))
    b.append(p(
        "Một tình huống thường gặp trong các hệ đo là M tín hiệu cần đo có tốc độ rất khác nhau. "
        "Tốc độ lấy mẫu của kênh do tín hiệu nhanh nhất quyết định, do đó cần một bộ ghép kênh M "
        "đầu vào có khả năng xử lý tín hiệu ở tần số lấy mẫu đó. Một giải pháp thuận tiện là đưa "
        "một số tín hiệu chậm vào một bộ ghép kênh, rồi kết hợp đầu ra của nó với tín hiệu nhanh "
        "trong một bộ ghép kênh thứ hai [6]."))

    b.append(h3("Các sơ đồ điều chế sóng mang phụ tương tự cho ghép kênh theo thời gian",
                "Analog Subcarrier Modulation Schemes for Time Division Multiplexing"))
    b.append(p(
        "Trong điều chế tương tự cho sóng mang phụ, tín hiệu thu được sau quá trình ghép kênh và "
        "lấy mẫu sẽ điều chế một chuỗi xung. Những phương pháp điều chế sóng mang phụ tương tự "
        "thông dụng nhất là điều chế biên độ xung (PAM), điều chế độ rộng xung (PDM) và điều chế "
        "vị trí xung (PPM). Hình 87.8 minh hoạ ba sơ đồ điều chế này, trong đó các xung được vẽ "
        "vuông cho đơn giản. Trong điều chế tương tự, tham số được điều chế (biên độ, độ rộng "
        "hay vị trí tương đối) thay đổi tỉ lệ với biên độ của tín hiệu đã lấy mẫu. Tuy nhiên, ở "
        "PAM và PDM các giá trị có một độ dịch, sao cho khi giá trị mẫu bằng không thì biên độ "
        "xung hoặc độ rộng xung vẫn khác không. Lý do của những độ dịch này là để giữ tốc độ của "
        "chuỗi xung không đổi, điều rất quan trọng cho việc đồng bộ. Những đặc điểm chung của "
        "các sơ đồ điều chế tương tự khác nhau cho xung trong TDM là: (1) phổ tín hiệu đã điều "
        "chế có nhiều thành phần tần số thấp, đặc biệt ở gần tần số lấy mẫu; (2) cần tránh sự "
        "chồng lấn giữa các xung liên tiếp để bảo toàn các tham số điều chế; và (3) có thể khôi "
        "phục các mẫu gốc từ tín hiệu đã điều chế bằng cách lọc thấp sau khi tách kênh. Việc "
        "giảm nhiễu phụ thuộc vào băng thông của tín hiệu đã điều chế, và đây chính là tiêu chí "
        "thiết kế chính."))
    b.append(fig(8))
    b.append(h4("Điều chế biên độ xung", "Pulse Amplitude Modulation"))
    b.append(p(
        "Dạng sóng PAM gồm những xung đơn cực, không vuông, có biên độ tỉ lệ với giá trị của các "
        "mẫu. Có thể định nghĩa chỉ số điều chế theo những tiêu chí tương tự như trong AM tương "
        "tự. Tương tự, trong PAM chỉ số điều chế bị giới hạn ở những giá trị nhỏ hơn 1."))
    b.append(h4("Điều chế độ rộng xung", "Pulse Duration Modulation"))
    b.append(p(
        "PDM gồm những xung đơn cực, vuông, có độ rộng phụ thuộc vào giá trị của các mẫu. Chu kỳ "
        "giữa tâm của hai xung liên tiếp là không đổi. Việc phân tích phổ thu được cho thấy có "
        "thể khôi phục các mẫu bằng cách lọc thấp [9]."))
    b.append(h4("Điều chế vị trí xung", "Pulse Position Modulation"))
    b.append(p(
        "PPM gần gũi với PDM, vì có thể tạo ra PPM thông qua PDM. Trong PPM, thông tin nằm ở vị "
        "trí thời gian của các xung chứ không nằm ở bản thân các xung. Nhờ vậy có thể truyền "
        "những xung rất hẹp để giảm năng lượng cần thiết; việc giảm năng lượng này là ưu điểm "
        "quan trọng nhất của PPM."))
    b.append(h4("Điều chế xung mã cho ghép kênh theo thời gian",
                "Pulse Code Modulation for Time Division Multiplexing"))
    b.append(p(
        "Mọi sơ đồ điều chế sóng mang phụ đã phân tích ở trên trong các hệ đo từ xa đều dựa trên "
        "một tín hiệu tương tự điều chế hoặc một sóng mang tương tự, hoặc một chuỗi xung. Điều "
        "chế xung mã (PCM) thì khác: đây là một kiểu điều chế số, trong đó tín hiệu đo được biểu "
        "diễn bằng một nhóm xung số đã mã hoá. Hai biến thể của PCM cũng thường được dùng là "
        "điều chế delta (DM) và điều chế xung mã vi sai (DPCM). Trong các sơ đồ điều chế tương "
        "tự, tín hiệu điều chế từ đầu đo có thể nhận bất kỳ giá trị nào giữa các giới hạn. Nếu "
        "nhiễu làm thay đổi tín hiệu điều chế thì không thể quyết định giá trị thực của nó. "
        "Ngược lại, nếu không phải mọi giá trị của tín hiệu điều chế đều được phép, và khoảng "
        "cách giữa các mức được phép lớn hơn giá trị nhiễu dự kiến, thì có thể quyết định được "
        "giá trị mà phía phát đã gửi. Chính khả năng miễn nhiễm với nhiễu này khiến các hệ PCM "
        "trở thành một trong những lựa chọn được ưu tiên cho đo từ xa. Hình 87.9 trình bày những "
        "phần tử cơ bản của một hệ đo từ xa PCM. Một bộ mã hoá PCM (hay bộ chuyển mạch PCM) "
        "chuyển dữ liệu vào thành một khuôn dạng dữ liệu nối tiếp thích hợp để truyền qua đường "
        "dây hoặc bằng kỹ thuật không dây. Ở đầu thu, một bộ giải mã PCM (hay bộ phân kênh PCM) "
        "chuyển dữ liệu nối tiếp trở lại thành những tín hiệu dữ liệu ra riêng lẻ. Các hệ PCM "
        "truyền dữ liệu dưới dạng một dòng nối tiếp các từ số. Bộ mã hoá PCM lấy mẫu dữ liệu vào "
        "và chèn các từ dữ liệu vào một khung PCM. Mỗi từ được gán một vị trí xác định trong "
        "khung PCM, để bộ giải mã có thể khôi phục các mẫu dữ liệu tương ứng với từng tín hiệu "
        "vào. Khung PCM đơn giản nhất gồm một từ đồng bộ khung, theo sau là một chuỗi từ dữ "
        "liệu. Khung lặp lại liên tục để cung cấp những mẫu dữ liệu mới khi dữ liệu vào thay "
        "đổi. Đồng bộ khung cho phép bộ giải mã PCM dễ dàng định vị điểm bắt đầu của mỗi khung."))
    b.append(fig(9))

    b.append(h3("Tiêu chuẩn đo từ xa PCM", "Pulse Code Modulation Telemetry Standards"))
    b.append(p(
        "IRIG 106-96 cũng định nghĩa những đặc tính của việc truyền PCM cho mục đích đo từ xa, "
        "cụ thể là cấu trúc chuỗi xung và các đặc tính thiết kế hệ thống. Vì mục đích tiêu chuẩn "
        "hoá, các khuôn dạng PCM được chia thành hai cấp: cấp I và cấp II. Những kiểu đơn giản "
        "hơn thuộc cấp I, còn những kiểu phức tạp hơn thuộc cấp II. Một số đặc tính của các hệ "
        "cấp II là tốc độ bit lớn hơn 5 Mbit/s, độ dài từ vượt quá 16 bit, các từ bị phân đoạn, "
        "ghép kênh phụ không đều, thay đổi khuôn dạng, khuôn dạng dữ liệu có gắn thẻ, truyền dữ "
        "liệu dị bộ, và hợp nhất nhiều kiểu khuôn dạng, cùng nhiều đặc tính khác. Bảng 87.3 tóm "
        "tắt ngắn gọn những chỉ tiêu PCM liên quan. Bạn đọc muốn biết chi tiết và mô tả đầy đủ "
        "xin xem Chương 4 của Tiêu chuẩn IRIG 106-96 [10]."))
    b.append(table_87_3("vi"))
    b.append(p(
        "Những mã PCM sau đây, được trình bày trên Hình 87.10, được các tiêu chuẩn IRIG công "
        "nhận: NRZ-L (không trở về không — mức), NRZ-M (không trở về không — dấu), NRZ-S (không "
        "trở về không — trống), BiØ-L (hai pha — mức), BiØ-M (hai pha — dấu) và BiØ-S (hai pha — "
        "trống). Tiêu chuẩn cũng khuyến nghị rằng dòng bit được truyền phải liên tục và chứa đủ "
        "các chuyển mức để bảo đảm việc bắt bit và duy trì đồng bộ bit. Tốc độ bit phải ít nhất "
        "là 10 bit/s. Nếu tốc độ bit trên 5 Mbit/s thì hệ PCM được xếp vào cấp II. Về khuôn dạng "
        "từ, tiêu chuẩn định nghĩa khuôn dạng cố định là khuôn dạng không thay đổi trong suốt "
        "quá trình truyền về mặt cấu trúc khung, độ dài từ hay vị trí, trình tự chuyển mạch, "
        "khoảng lấy mẫu, hoặc danh mục phép đo. Các từ riêng lẻ có thể có độ dài từ 4 bit đến "
        "không quá 16 bit ở cấp I và không quá 64 bit ở cấp II. Từ bị phân đoạn — định nghĩa là "
        "một từ được chia thành không quá tám đoạn và đặt ở nhiều vị trí khác nhau trong một "
        "khung nhỏ — chỉ được phép ở cấp II. Mọi đoạn của một từ dữ liệu đều bị ràng buộc trong "
        "biên của một khung nhỏ duy nhất. Cấu trúc khung mà tiêu chuẩn cho phép đối với đo từ xa "
        "PCM quy định rằng dữ liệu được định khuôn thành những khung có độ dài cố định, chứa một "
        "số cố định các khoảng bit có độ dài bằng nhau. Khung nhỏ được định nghĩa là cấu trúc dữ "
        "liệu theo trình tự thời gian từ đầu mẫu đồng bộ khung nhỏ đến đầu mẫu đồng bộ khung nhỏ "
        "kế tiếp. Độ dài khung nhỏ là số khoảng bit từ đầu mẫu đồng bộ khung đến đầu mẫu đồng bộ "
        "kế tiếp. Độ dài cực đại của một khung nhỏ sẽ không vượt quá 8192 bit cũng không vượt "
        "quá 1024 từ ở cấp I, và sẽ không vượt quá 16.384 bit ở cấp II. Khung nhỏ gồm mẫu đồng "
        "bộ, các từ dữ liệu và, nếu có dùng, các từ đồng bộ khung con. Tiêu chuẩn cho phép dùng "
        "những từ có độ dài khác nhau nếu chúng được ghép trong cùng một khung nhỏ. Hình 87.11 "
        "trình bày một biểu diễn đồ hoạ của cấu trúc khung PCM. Khung lớn chứa số khung nhỏ cần "
        "thiết để bao gồm một mẫu của mọi tham số trong khuôn dạng. Độ dài của khung lớn được "
        "định nghĩa là độ dài khung nhỏ nhân với số khung nhỏ chứa trong khung lớn. Số khung nhỏ "
        "tối đa trong một khung lớn bị giới hạn ở 256."))
    b.append(fig(10))
    b.append(fig(11))
    b.append(p(
        "Phụ lục C của Tiêu chuẩn IRIG 106-96 đưa ra những khuyến nghị nhằm đạt hiệu suất truyền "
        "tối đa trong đo từ xa PCM. Băng thông trung tần (IF) của các máy thu dữ liệu đo từ xa "
        "PCM nên được chọn sao cho 90 đến 99% phổ công suất đã truyền nằm trong băng thông −3 dB "
        "của máy thu. Trung tần cũng ảnh hưởng tới xác suất lỗi bit (BEP) theo phương trình sau "
        "đây cho PCM/FM kiểu NRZ-L [10]:"))
    b.append(eq("BEP = 0,5e<sup><i>k</i>·SNR</sup>", "87.13"))
    b.append(p("trong đó <i>k</i> ≈ −0,7 khi băng thông IF bằng tốc độ bit"))
    b.append(ul(["<i>k</i> ≈ −0,65 khi băng thông IF bằng 1,2 lần tốc độ bit",
                 "<i>k</i> ≈ −0,55 khi băng thông IF bằng 1,5 lần tốc độ bit"]))
    b.append(p(
        "Những mã dữ liệu và kỹ thuật điều chế khác có đặc tuyến BEP theo SNR khác, nhưng trong "
        "mọi trường hợp xu hướng đều tương tự."))
    b.append(p(
        "Tiêu chuẩn cũng quy định những mẫu đồng bộ khung được khuyến nghị dùng chung trong đo "
        "từ xa PCM. Có nhiều độ dài khác nhau cho các mẫu đồng bộ, nhưng ở mọi độ dài thì 111 là "
        "chuỗi bit đầu tiên được truyền. Các mẫu có độ dài từ 16 đến 30 được chọn nhằm giảm "
        "thiểu xác suất đồng bộ nhầm trên toàn bộ phần chồng lấn mẫu trong khối đồng bộ khung "
        "của trạm mặt đất [12]. Mật độ phổ (<i>S</i>) của các mã NRZ và BiØ là"))
    b.append(eq("NRZ: <i>S</i> = " +
                _frac("sin<sup>2</sup>(π<i>fT</i>)", "(π<i>fT</i>)<sup>2</sup>"), "87.14"))
    b.append(eq("Hai pha: <i>S</i> = " +
                _frac("sin<sup>4</sup>(π<i>fT</i>/2)", "(π<i>fT</i>/2)<sup>4</sup>"), "87.15"))
    b.append(p(
        "Việc tính các mật độ phổ cho phép xác định BEP cho kiểu mã nói trên, giả sử đã có đồng "
        "bộ bit hoàn hảo. Những tính toán này cho thấy với cùng một SNR, BEP thấp nhất đạt được "
        "với NRZ-L và các mã Bi, tiếp đó là các mã NRZ và BiØ kiểu dấu và trống, và cuối cùng là "
        "các mã NRZ-L ngẫu nhiên (RNRZ-L)."))
    b.append(p(
        "Dữ liệu đo từ xa thường được ghi lên băng từ để phân tích sau. Khi ghi dữ liệu PCM, "
        "điều quan trọng là phải bảo đảm máy ghi băng có đáp ứng tần số đủ để thu và tái tạo "
        "tín hiệu PCM. Những quy tắc hữu ích để tính tốc độ bit cực đại cho các mã PCM khác "
        "nhau chỉ ra rằng với các mã NRZ và RNRZ, tốc độ bit cực đại bằng 1,4 lần đáp ứng tần số "
        "của máy ghi băng, còn với mọi mã hai pha, tốc độ cực đại bằng 0,7 lần đáp ứng của máy "
        "ghi. Để hạn chế băng thông truyền mà PCM tạo ra — vì đây là tín hiệu số có chuyển mức "
        "nhọn — tín hiệu PCM thường được cho qua một bộ lọc tiền điều chế trước khi đưa vào đầu "
        "vào máy phát. Tần số cắt của bộ lọc có thể tính bằng 0,7 lần tốc độ bit PCM với các mã "
        "NRZ và RNRZ, và bằng 1,4 lần tốc độ bit PCM với mọi mã hai pha."))

    # ---------------------------------------------------------- terms
    b.append(h2("Thuật ngữ của chương 87", "Chapter 87 terminology"))
    b.append(note(
        "Phần này do người dịch thêm vào; nguyên bản không có mục này. Nó gom những thuật ngữ mà "
        "chính chương 87 định nghĩa trong mục “Defining Terms” thành một bảng để tiện tra cứu "
        "khi đọc. Định nghĩa giữ nguyên nội dung của nguyên bản, chỉ rút gọn câu chữ."))
    b.append(_glossary(_GLOSS_VI))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs(_REFS))
    b.append(h2("Thông tin thêm", "Further Information"))
    b.append('<ul class="ref-list">%s</ul>' % "".join("<li>%s</li>" % i for i in _FURTHER_VI))
    return "".join(b)


# ================================================================ EN
def body_en():
    b = []
    b.append(_transnote("en"))

    # ---------------------------------------------------------- 87.1
    b.append(h2("87.1 Introduction"))
    b.append(p(
        "Telemetry is the science of gathering information at some remote location and "
        "transmitting the data to a convenient location to be examined and recorded. Telemetry "
        "can be done by different methods: optical, mechanical, hydraulic, electric, etc. The "
        "mechanical methods, either pneumatic or hydraulic, have acceptable results for short "
        "distances and are used in environments that have a high level of electromagnetic "
        "interference and in those situations where, for security reasons, it is not possible to "
        "use electrical signals — for example, in explosive environments. More recently, the use "
        "of optical fiber systems allows the measurement of broad bandwidth and high immunity to "
        "noise and interference. Other proposed telemetry systems are based on ultrasound, "
        "capacitive or magnetic coupling, and infrared radiation, although these methods are not "
        "routinely used. The discussion in this chapter is limited to the most-used systems: "
        "telemetry based on electric signals. The main advantage of electric over mechanical "
        "methods is that electrically based telemetry does not have practical limits regarding "
        "the distance between the measurement and the analysis areas, and can be easily adapted "
        "and upgraded in already existing infrastructures. Electric telemetry methods are "
        "further divided, depending on the transmission channel they use, into wire telemetry "
        "and wireless (or radio) telemetry. Wire telemetry is technologically the simplest "
        "solution. The limitations of wire telemetry are the low bandwidth and low transmission "
        "speed it can support. However, it is used when the transmission wires can use the "
        "already existing infrastructure, as, for example, in most electric power lines that are "
        "also used as wire telemetry carriers. Wireless telemetry is more complex than wire "
        "telemetry, as it requires a final radio frequency (RF) stage. Despite its complexity it "
        "is widely used because it can transmit information over longer distances; thus it is "
        "used in those applications in which the measurement area is not normally accessible. It "
        "can also transmit at higher speeds and have enough capacity to transmit several "
        "channels of information if necessary."))
    b.append(fig(1, "en"))
    b.append(p(
        "Figure 87.1 displays a generic telemetry system. It consists of (not all the blocks "
        "will always be present): (1) transducers to convert the physical variables to be "
        "measured into electric signals that can be easily processed; (2) conditioning circuits "
        "to amplify the low-level signal from the transducer, limit its bandwidth and adapt "
        "impedance levels; (3) a signal-processing circuit that sometimes can be integrated in "
        "the previous circuits; (4) a subcarrier oscillator whose signal will be modulated by "
        "the output of the different transducers once processed and adapted; (5) a codifier "
        "circuit — which can be a digital encoder, an analog modulator or a digital modulator — "
        "that adapts the signal to the characteristics of the transmission channel, which is a "
        "wire or an antenna; (6) a radio transmitter, in wireless telemetry, modulated by the "
        "composite signal; (7) an impedance line adapter, in case of wire transmission, to adapt "
        "the characteristic impedance of the line to the output impedance of the circuits "
        "connected to the adapter; and (8) for wireless communication, a transmitting antenna. "
        "The receiver end consists of similar modules. For wireless telemetry these modules are "
        "(1) a receiving antenna designed for maximum efficiency in the RF band used; (2) a radio "
        "receiver with a demodulation scheme compatible with the modulation scheme; and (3) "
        "demodulation circuits for each of the transmitted channels. For wire telemetry, the "
        "antenna and the radio receiver are replaced by a generic front end to amplify the signal "
        "and adapt the line impedance to the input impedance of the circuits that follow."))
    b.append(p(
        "The transmission in telemetry systems, in particular wireless ones, is done by sending "
        "a signal whose analog variations in amplitude or frequency are a known function of the "
        "variations of the signals from the transducers. More recently, digital telemetry "
        "systems send data digitally as a finite set of symbols, each one representing one of the "
        "possible finite values of the composite signals at the time it was sampled. The "
        "effective communication distance in a wireless system is limited by the power radiated "
        "by the transmitting antenna, the sensitivity of the receiver and the bandwidth of the RF "
        "signal. As the bandwidth increases, the contribution of noise to the total signal also "
        "increases, and consequently more transmitted power is needed to maintain the same "
        "signal-to-noise ratio (SNR). This is one of the principal limitations of wireless "
        "telemetry systems. In some applications the transmission to the receiver is done on "
        "base band, after the conditioning circuits. The advantage of base-band telemetry "
        "systems is their simplicity, although because of the base-band transmission they are "
        "normally limited to only one channel at low speeds."))
    b.append(p(
        "Not uncommonly, a measurement system needs to acquire either different types of signals "
        "or the same type of data at different locations in the process that is being monitored. "
        "These different information signals can be transmitted using the same common carrier by "
        "multiplexing the data signals. Multiplexing allows different signals to share the same "
        "channel. Multiplexing techniques are usually considered either frequency division "
        "multiplexing (FDM) or time division multiplexing (TDM). In FDM, different subcarrier "
        "frequencies are modulated by the different measurement channel signals, which causes the "
        "information spectrum to shift from base band to the subcarrier frequency. Then the "
        "subcarrier frequencies modulate the RF carrier signal, which allows the transmission of "
        "all desired measurement channels simultaneously. In TDM, the whole channel is assigned "
        "entirely to each measurement channel, although only during a fraction of the time. TDM "
        "techniques use digital modulation to sample the different measurement channels at "
        "different times; these samples are then applied sequentially to modulate the RF carrier. "
        "Figure 87.2 illustrates these concepts by showing frequency and time graphs for FDM and "
        "TDM, respectively."))
    b.append(fig(2, "en"))
    b.append(p(
        "Almost all instrumentation and measurement situations are candidates for the use of a "
        "telemetry link. Telemetry is widely used in space applications for either "
        "telemeasurement of a distant variable or telecommandment of actuators. In most of these "
        "types of applications, for example in space telemetry, it is very important to design "
        "the telemetry systems to minimize the consumption of power [1]. Some land-mobile "
        "vehicles, such as trains, also use telemetry systems, either wireless or by using some "
        "of the existing power wires, to transmit data to the central station and receive its "
        "commands [2]. In clinical practice, the telemetry of patients increases their quality of "
        "life and their mobility, as patients do not need to be connected to a measurement system "
        "to be monitored. Several medical applications are based on implanting a sensor in a "
        "patient and transmitting the data to be further analyzed and processed either by radio "
        "[3] or by adapted telephone lines [4] from the receiving station. Optical sensors and "
        "fiber-optic communications are used in industry to measure in environments where it is "
        "not desirable to have electric signals, such as explosive atmospheres [5]. The designer "
        "of a telemetry system needs also to keep in mind the conditions in which the system will "
        "have to operate. In most applications the telemetry systems must operate repeatedly "
        "without adjustment and calibration in a wide range of temperatures. Finally, as "
        "different telemetry systems are developed, the need to permit tests to be made "
        "interchangeable at all ranges increases, which requires compatibility of transmitting, "
        "receiving and signal-processing equipment at all ranges. For this reason the Department "
        "of Defense Research and Development Squad created the Guided Missiles Committee, which "
        "formed the Working Group on Telemetry. This later became the Inter-Range Instrumentation "
        "Group (IRIG) that developed Telemetry Standards. Today the IRIG Standard 106-96 is the "
        "primary Telemetry Standard used worldwide by both government and industry."))

    # ---------------------------------------------------------- 87.2
    b.append(h2("87.2 Base-Band Telemetry"))
    b.append(p(
        "Base-band telemetry uses a wire line to communicate the signal from the transducer, "
        "after being processed and conditioned, with the receiver. We will briefly describe "
        "telemetry systems based either on amplitude or on frequency. More in-depth study of "
        "these base-band telemetry systems can be found in Reference 6."))

    b.append(h3("Base-Band Telemetry Based on Amplitude"))
    b.append(h4("Voltage-Based Base-Band Telemetry"))
    b.append(p(
        "Figure 87.3a shows a simple voltage-based telemetry system. The signal from the "
        "transducer is amplified, normally to a voltage level between 1 and 15 V, and sent "
        "through a line consisting of two wires to the receiver. By making the low end of the "
        "scale 1 V, this system can detect short circuits [6]. The main problem of this "
        "configuration is the limitation on the transmission distance, which depends on the "
        "resistance of the line and the input resistance of the receiver. Also, the connecting "
        "wires form a loop that is very susceptible to interference from parasitic signals."))
    b.append(fig(3, "en"))
    b.append(h4("Current-Based Base-Band Telemetry"))
    b.append(p(
        "The limitation on transmission distance of the voltage-based system due to the "
        "impedance of the line is solved by using a current signal instead of a voltage, as is "
        "shown in Figure 87.3b. This requires an additional conversion module after the "
        "signal-processing circuits, from voltage to current. At the receiver end the signal is "
        "detected by measuring the voltage across a resistor. The most-used system in industry is "
        "the 4 to 20 mA loop. This means that 0 V is transmitted as 4 mA, while the highest "
        "voltage value is transmitted as a 20 mA current. The advantage of transmitting 4 mA for "
        "0 V is the easy detection of an open circuit in the loop (0 mA). Other standard current "
        "values are 0 to 5, 0 to 20, 10 to 50, 1 to 5 and 2 to 10 mA. Also, voltage drops due to "
        "the resistance of the wires do not affect the transmitted signal, which allows the use "
        "of thinner wires. Because this is a current mode, the parasitic voltages induced in the "
        "line do not affect the signal either. Current-based telemetry allows the use of grounded "
        "or floating transmitters with few modifications [6]."))

    b.append(h3("Base-Band Telemetry Based on Frequency"))
    b.append(p(
        "Frequency-based transmission is known to have higher immunity to noise than "
        "amplitude-based transmission. Frequency-based telemetry, shown in Figure 87.3c, is used "
        "in the presence of inductive or capacitive interference due to its immunity to noise. It "
        "also offers the possibility of isolating the receiver from the transmitter. The signal at "
        "the output of the conditioning circuit modifies the frequency of the telemetry signal, "
        "normally using a voltage-to-frequency converter. In the receiver, a "
        "frequency-to-voltage converter performs the opposite function. A special case of "
        "frequency-based telemetry is pulse telemetry, in which the modulating signal changes "
        "some characteristics of a train of pulses. Because of its importance and widespread use, "
        "pulse telemetry is analyzed in depth in the following sections."))

    # ---------------------------------------------------------- 87.3
    b.append(h2("87.3 Multiple-Channel Telemetry"))
    b.append(p(
        "Most of the industrial processes in which telemetry is used require the measurement of "
        "different physical variables to control the process, the measurement of only one "
        "physical variable at different locations, or normally a combination of both. In these "
        "multiple-channel measurements, base-band telemetry is not an option, as it would require "
        "building a different system for each channel. Multiple-channel telemetry is achieved by "
        "sharing a common resource (the transmission channel), as is shown in Figure 87.4. The "
        "sharing of the transmission channel by all the measurement channels is designated by "
        "multiplexing. There are two basic multiplexing techniques: FDM and TDM. In FDM, different "
        "channels are assigned to different spectral bands and the composite signal is transmitted "
        "through the communication channel. In TDM, the information for different channels is "
        "transmitted sequentially through the communication channel."))
    b.append(fig(4, "en"))

    b.append(h3("Frequency Division Multiplexing"))
    b.append(p(
        "In FDM, shown in Figure 87.5a, each measurement channel modulates a sinusoidal signal of "
        "different frequency. These sinusoidal signals are called subcarriers. Each of the "
        "modulated signals is then low-pass filtered to ensure that the bandwidth limits are "
        "observed. After the filtering stage, all the modulated signals are fed into a summing "
        "block, producing what is known as a base-band signal. A base-band signal indicates here "
        "that the final carrier has not yet been modulated. The spectrum of the base-band signal "
        "is shown in Figure 87.5b, where it is possible to see how each measurement channel "
        "spectrum signal is allocated its own frequency. This composite signal finally modulates a "
        "carrier signal whose frequency depends on the transmission medium that is used. The "
        "signal is then fed into a transmission wire (similar to TV-broadcasting systems by "
        "cable) or, more commonly, into an antenna in the case of wireless telemetry systems. In "
        "wireless telemetry the frequency of the carrier cannot be chosen arbitrarily, but is "
        "chosen in accordance with international agreements on the use of the electromagnetic "
        "spectrum. In the U.S., the Federal Communications Commission (FCC) is the body that "
        "regulates the allocation of frequencies for different communication services. Table 87.1 "
        "shows the most common telemetry frequency bands and their intended use. Table 87.1 is for "
        "informational purposes only, and it is not a comprehensive guide to telemetry "
        "frequencies. To find the allowed telemetry frequencies for a specific application, the "
        "maximum power allowed and other limitations, the reader should consult the applicable "
        "FCC documents [7,8]."))
    b.append(table_87_1("en"))
    b.append(fig(5, "en"))
    b.append(p(
        "The allocation of bands is a process subject to change. For example, in October 1997 "
        "the FCC assigned some of the TV channel bands for patient telemetry inside hospitals, "
        "with restricted power. The FCC publishes all changes that affect frequency bands or "
        "other technical characteristics for telemetry."))
    b.append(p(
        "At the receiver end, the carrier demodulator detects and recovers the composite "
        "base-band signal. The next step is to separate each of the subcarriers by feeding the "
        "signal into a bank of parallel passband filters. Each channel is further demodulated, "
        "recovering the information from the transducer. The main practical problem of FDM systems "
        "is the cross talk between channels. Cross talk appears due to the nonlinearities of the "
        "electronic devices, which originates when the signal for one channel partially modulates "
        "another subcarrier in addition to the one assigned to that channel. Cross talk also "
        "originates when the spectra for two adjacent channels overlap. To avoid this effect, the "
        "subcarriers have to be chosen so that there is a separation (guard band) between the "
        "spectra of two contiguous channels. By increasing the guard band the possibility of cross "
        "talk decreases, but the effective bandwidth also increases. The effective bandwidth "
        "equals the sum of the bandwidth of all channels plus the sum of all the guard bands."))
    b.append(p(
        "There are three alternative methods for each of the two modulation processes — the "
        "modulation of the measurement channel signals and the modulation of the composite "
        "signal. These methods are amplitude modulation (AM), frequency modulation (FM) and phase "
        "modulation (PM). The usual combinations are FM/FM, FM/PM or AM/FM [6]. Here we analyze "
        "only the subcarrier modulation schemes; the modulation of the RF signal is analyzed in "
        "Chapter 81."))

    b.append(h4("Subcarrier Modulation of Amplitude"))
    b.append(p(
        "In an AM subcarrier modulation scheme, the amplitude of a particular subcarrier signal "
        "is changed according to the value of the measured channel assigned to that frequency. "
        "The resulting AM signal is given by"))
    b.append(eq("<i>v</i>(<i>t</i>) = <i>A</i><sub>c</sub>[1 + <i>m</i>(<i>t</i>)] "
                "cos(ω<sub>c</sub><i>t</i>)", "87.1"))
    b.append(p(
        "where <i>A</i><sub>c</sub> is the amplitude of the carrier, <i>m</i>(<i>t</i>) the "
        "modulating signal, and ω<sub>c</sub> the frequency of the carrier. The advantage of this "
        "type of modulation is the simplicity of the circuits that perform the modulation and of "
        "the circuits required for the demodulation, in order to recover the modulating signal "
        "that carries the desired information. The percentage of modulation denotes the extent to "
        "which a carrier has been amplitude modulated. Assuming for simplicity that the modulating "
        "signal is sinusoidal of frequency ω<sub>m</sub>, such as"))
    b.append(eq("<i>m</i>(<i>t</i>) = <i>m</i> × cos(ω<sub>m</sub><i>t</i>)", "87.2"))
    b.append(p("the percentage of modulation (<i>P</i>) can be found as"))
    b.append(eq("<i>P</i> = <i>m</i> × 100 (%)", "87.3"))
    b.append(p("In a more general way, the percentage of modulation (<i>P</i>) is expressed as"))
    b.append(eq(_frac("<i>P</i>", "100%") + " = " +
                _frac("<i>A</i><sub>c(max)</sub> − <i>A</i><sub>c(min)</sub>",
                      "2<i>A</i><sub>c</sub>"), "87.4"))
    b.append(p(
        "where <i>A</i><sub>c(max)</sub> and <i>A</i><sub>c(min)</sub> are the maximum and "
        "minimum values that the carrier signal achieves."))
    b.append(fig(6, "en"))
    b.append(p(
        "Figure 87.6 shows the spectrum of an amplitude-modulated signal, assuming that the "
        "modulating signal is a band-limited, nonperiodic signal of finite energy. It consists of "
        "two sidebands that are symmetrical in reference to the subcarrier. Figure 87.6 also shows "
        "the main disadvantages of AM schemes. First, the bandwidth of the modulated channel is "
        "two times the bandwidth of the modulating signal, due to the two similar sidebands that "
        "appear; this results in an inefficient use of the spectrum. Second, the analysis of power "
        "for each of the components in Figure 87.6 shows that at least 50% of the transmitted "
        "power is used in transmitting the subcarrier, which is independent of the measured "
        "signal, as it does not contain any information. The remaining power is split between the "
        "two sidebands, which results in a maximum efficiency that it is theoretically possible to "
        "achieve of below 25%. The third main problem of AM is the possibility of overmodulation, "
        "which occurs when <i>m</i> > 1. Once a signal is overmodulated, it is not possible to "
        "recover the modulating signal with the simple circuits that are widely used for AM "
        "telemetry transmission."))
    b.append(p(
        "The limitations of AM subcarrier modulation can be overcome using more efficient "
        "modulation techniques, such as double sideband (DSB), single sideband (SSB) and "
        "compatible single sideband (CSSB), which are also considered AM techniques. However, the "
        "complexity of these modulation systems and the cost associated with systems capable of "
        "recovering subcarrier signals modulated this way cause these not to be used in most "
        "commercial telemetry systems. Most of the available systems that use AM subcarrier "
        "techniques use the traditional AM described here, because its simplicity overcomes the "
        "possible problems of its use."))

    b.append(h4("Subcarrier Modulation of Frequency"))
    b.append(p(
        "FM (or PM) is by far the most-used subcarrier modulation scheme in FDM telemetry "
        "systems. These angle modulations are inherently nonlinear, in contrast to AM. Angle "
        "modulation can be expressed as"))
    b.append(eq("<i>v</i>(<i>t</i>) = <i>A</i> cos[ω<sub>c</sub><i>t</i> + φ(<i>t</i>)]", "87.5"))
    b.append(p(
        "where φ(<i>t</i>) is the modulating signal, that is, the signal from the transducers "
        "after conditioning."))
    b.append(p("It is then possible to calculate the value of the instantaneous frequency as"))
    b.append(eq("<i>f</i> = " + _frac("1", "2π") + " " + _frac("d", "d<i>t</i>") +
                "[ω<sub>c</sub><i>t</i> + φ(<i>t</i>)] = " +
                _frac("ω<sub>c</sub>", "2π") + " + " + _frac("d", "d<i>t</i>") + "φ(<i>t</i>)",
                "87.6"))
    b.append(p(
        "This equation shows how the signal <i>v</i>(<i>t</i>) is modulated in frequency. We can "
        "analyze two parameters that can be derived from the previous equations: frequency "
        "deviation and modulation index. Frequency deviation (<i>f</i><sub>m</sub>) is the maximum "
        "departure of the instantaneous frequency from the carrier frequency. The modulation "
        "index (β) is the maximum phase deviation. The following equations show how these "
        "parameters are related. The value of the instantaneous frequency (<i>f</i>) is [9]"))
    b.append(eq("<i>f</i> = " + _frac("ω<sub>c</sub>", "2π") + " + " +
                _frac("βω<sub>m</sub>", "2π") + " cos(ω<sub>m</sub><i>t</i>) = " +
                "<i>f</i><sub>c</sub> + β<i>f</i><sub>m</sub> cos(ω<sub>m</sub><i>t</i>)",
                "87.7"))
    b.append(p("The maximum frequency deviation is Δ<i>f</i> and is given by"))
    b.append(eq("Δ<i>f</i> = β<i>f</i><sub>m</sub>", "87.8"))
    b.append(p("Therefore we can write the equation for the frequency modulated signal as"))
    b.append(eq("<i>v</i>(<i>t</i>) = <i>A</i> cos[ω<sub>c</sub><i>t</i> + " +
                _frac("Δ<i>f</i>", "<i>f</i><sub>m</sub>") + " sin(ω<sub>m</sub><i>t</i>)]",
                "87.9"))
    b.append(p(
        "The previous equation shows that the instantaneous frequency <i>f</i> lies in the range "
        "<i>f</i><sub>c</sub> ± Δ<i>f</i>. However, it does not mean that all the spectral "
        "components lie in this range. The spectrum of an angle-modulated waveform cannot be "
        "written as a simple equation. In the simplest case, when the modulating signal is a "
        "sinusoidal signal, a practical rule states that the bandwidth of an FM signal is twice "
        "the sum of the maximum frequency deviation and the modulating frequency. For modulating "
        "signals commonly found in measuring systems, the bandwidth is dependent upon the "
        "modulation index; that is, as the bandwidth allocated for each channel is limited, the "
        "modulation index will also be limited."))

    b.append(h3("Frequency Division Multiplexing Telemetry Standards"))
    b.append(p(
        "IRIG Standard 106-96 is the most used standard for military and commercial telemetry, "
        "data acquisition and recording systems by government and industry worldwide [10]. It "
        "recognizes two types of formats for FM in FDM systems: proportional-bandwidth modulation "
        "(PBW) and constant-bandwidth modulation (CBW). It also allows the combination of PBW and "
        "CBW channels. In PBW, the bandwidth for a channel is proportional to the subcarrier "
        "frequency. The standard recognizes three classes of subcarrier deviations: 7.5, 15 and "
        "30%. There are 25 PBW channels with a deviation frequency of 7.5%, numbered 1 to 25. The "
        "lowest channel has a center frequency of 400 Hz, which means that the lower deviation "
        "frequency is 370 Hz and the upper deviation frequency is 430 Hz. The highest channel "
        "(channel 25) has a center frequency of 560,000 Hz (deviation from 518,000 to 602,000 Hz). "
        "The center frequencies have been chosen so that the ratio between the upper deviation "
        "limit for a given channel and the lower deviation limit for the next channel is around "
        "1.2. There are 12 PBW channels with a deviation frequency of 15%, identified as A, B, … "
        "L. The center frequency for the lowest channel is 22,000 Hz (deviation from 18,700 Hz to "
        "25,300 Hz), while the center frequency for the highest channel is 560,000 Hz (476,000 to "
        "644,000 Hz), with a ratio for the center frequencies of adjacent channels of about 1.3. "
        "There are also 12 PBW channels for a deviation frequency of 30%, labeled from AA, BB, … "
        "to LL. The center frequency for these channels is the same as that for the 15% "
        "channels."))
    b.append(p(
        "CBW channels keep the bandwidth constant and independent of their carrier frequency. "
        "There are eight possible maximum subcarrier frequency deviations, labeled A (for 2 kHz "
        "deviation) to H (for 256 kHz deviation). The deviation frequency doubles from one group "
        "to the next. There are 22 A-channels, whose center frequencies range from 8 to 176 kHz. "
        "The separation between adjacent channels is a constant of 8 kHz. Table 87.2 shows a "
        "summary of the characteristics of CBW channels."))
    b.append(table_87_2("en"))
    b.append(p(
        "IRIG Standard 106-96 gives in its appendix criteria for the use of the FDM Standards. "
        "It focuses on the limits, most of the time dependent on the hardware used, and "
        "performance trade-offs such as data accuracy for data bandwidth that may be required in "
        "the implementation of the system. The subcarrier deviation ratio determines the SNR for a "
        "channel. As a rule of thumb, the SNR varies as the three-halves power of the subcarrier "
        "deviation ratio. On the other hand, the number of subcarrier channels that can be used "
        "simultaneously to modulate an RF carrier is limited by the channel bandwidth of the RF "
        "carrier as well as by considerations of SNR. Given a limited RF bandwidth, as more "
        "channels are added to the FDM system it is necessary to reduce the deviation ratio for "
        "each channel, which reduces the SNR for each channel. It is then very important to "
        "evaluate the acceptable trade-off between the number of subcarrier channels and the "
        "acceptable SNR values. A general equation that might be used to estimate the thermal "
        "noise performance of an FM/FM channel is the following [11]:"))
    b.append(eq(_pf("S", "N") + "<sub>d</sub> = " + _pf("S", "N") + "<sub>c</sub> " +
                _big("(") + _frac("3", "4") + _big(")") + "<sup>1/2</sup> " +
                _pf("<i>B</i><sub>c</sub>", "<i>F</i><sub>ud</sub>") +
                _pf("<i>f</i><sub>dc</sub>", "<i>f</i><sub>s</sub>") +
                _pf("<i>f</i><sub>ds</sub>", "<i>F</i><sub>ud</sub>"), "87.10"))
    b.append(p(
        "where (S/N)<sub>d</sub> represents the SNR at the discriminator output, "
        "(S/N)<sub>c</sub> represents the SNR of the receiver, <i>B</i><sub>c</sub> is the "
        "intermediate-frequency bandwidth of the receiver, <i>F</i><sub>ud</sub> is the subcarrier "
        "discriminator output filter (at −3 dB), <i>f</i><sub>s</sub> is the subcarrier center "
        "frequency, <i>f</i><sub>dc</sub> is the carrier peak deviation for the subcarrier "
        "considered, and <i>f</i><sub>ds</sub> is the subcarrier peak deviation."))
    b.append(p(
        "According to the Standard, the FM/FM composite FDM signal that is used to modulate an "
        "RF carrier can be of PBW format, CBW format, or a combination of both, with the only "
        "limitation that the guard bands between the channels used in the mixed format are equal "
        "to or greater than the guard bands for the same channels in an unmixed format."))

    b.append(h3("Time Division Multiplexing"))
    b.append(p(
        "TDM is a transmission technique that divides the time into different slots and assigns "
        "one slot to each measurement channel. In TDM, all the transmission bandwidth is assigned "
        "entirely to each measurement channel during a fraction of the time. After the signals "
        "from the measurement channels have been low-pass filtered, they are sequentially sampled "
        "by a digital switch that samples all the measurement channels in a period of time "
        "(<i>T</i>) that complies with the Nyquist criteria. Figure 87.7a shows a basic block "
        "diagram for an FDM system.<sup>1</sup> The output of the sampler is a train of AM pulses that "
        "contains the individual samples for the channels framed periodically, as is shown in "
        "Figure 87.7b. Finally, the composite signal modulates an RF carrier. The set of samples "
        "from each one of the input channels is called a frame. For M measurement channels, the "
        "period between two consecutive pulses is <i>T</i><sub>s</sub>/M = "
        "1/M<i>f</i><sub>s</sub>, where <i>T</i><sub>s</sub> is the sampling period. The period "
        "between samples from the same channel is <i>T</i><sub>s</sub>. At the receiver end, by "
        "separating the digital signals into different channels with a synchronized demultiplexer "
        "and by low-pass filtering, it is possible to recover the original signal for each "
        "measurement channel."))
    b.append(note(
        "[^1] The print says “FDM” at this point, but figure 87.7a is a TDM diagram and the "
        "whole passage is about TDM. The translation keeps the printed word and flags it — see "
        "the translator’s note at the head of the chapter."))
    b.append(fig(7, "en"))
    b.append(p(
        "TDM systems have advantages over FDM systems. First, FDM requires subcarrier modulators "
        "and demodulators for each channel, whereas in TDM only one multiplexer and demultiplexer "
        "are required. Second, TDM signals are resistant to the error sources that originate cross "
        "talk in FDM: nonideal filtering and cross modulation due to nonlinearities. In TDM the "
        "separation between channels depends on the sampling system. However, because it is "
        "impossible in practice to produce perfectly square pulses, their rise and fall times are "
        "different from zero. It is then necessary to provide guard time between pulses, similar "
        "to the guard bands in FDM systems. Cross talk in TDM can be easily estimated assuming "
        "that the pulse decay is exponential with a time constant (τ) approximately equal to"))
    b.append(eq("τ = " + _frac("1", "2π<i>B</i>"), "87.11"))
    b.append(p(
        "where <i>B</i> is the −3 dB channel bandwidth. The cross talk (<i>k</i>) between "
        "channels can be approximated as"))
    b.append(eq("<i>k</i> = −54.5<i>T</i><sub>g</sub> (dB)", "87.12"))
    b.append(p(
        "where <i>T</i><sub>g</sub> is the minimum time separation between channels, called "
        "guard time."))
    b.append(p(
        "A common situation in measurement systems occurs when the M signals that need to be "
        "measured have very different speeds. The channel sampling rate is determined by the "
        "fastest signal, thus needing an M-input multiplexer capable of handling signals at that "
        "sampling frequency. A convenient solution is to feed several slow signals into one "
        "multiplexer, then combine its output with the fast signal in a second multiplexer [6]."))

    b.append(h3("Analog Subcarrier Modulation Schemes for Time Division Multiplexing"))
    b.append(p(
        "In analog modulation for subcarriers, the signal that results after the multiplexing "
        "and sampling process modulates a train of pulses. The most common methods for analog "
        "subcarrier modulation are pulse amplitude modulation (PAM), pulse duration modulation "
        "(PDM) and pulse position modulation (PPM). Figure 87.8 illustrates these three "
        "modulation schemes, where the pulses are shown square for simplicity. In analog "
        "modulation, the parameter that is modulated (amplitude, duration or relative position) "
        "changes proportionally to the amplitude of the sampled signal. However, in PAM and PDM "
        "the values have an offset, so that when the value of the sample is zero, the pulse "
        "amplitude or the pulse width is different from zero. The reason for these offsets is to "
        "maintain the rate of the train of pulses constant, which is very important for "
        "synchronization purposes. The common characteristics of the different analog modulation "
        "schemes for pulses in TDM are: (1) a modulated signal spectrum with a large "
        "low-frequency content, especially close to the sampling frequency; (2) the need to avoid "
        "overlaying between consecutive pulses in order to conserve the modulation parameters; and "
        "(3) the possibility of reconstructing the original samples from the modulated signal "
        "through low-pass filtering after demultiplexing. The reduction of noise depends on the "
        "bandwidth of the modulated signal, this being the principal design criterion."))
    b.append(fig(8, "en"))
    b.append(h4("Pulse Amplitude Modulation"))
    b.append(p(
        "PAM waveforms are made of unipolar, nonrectangular pulses whose amplitudes are "
        "proportional to the values of the samples. It is possible to define the modulation index "
        "using similar criteria as in analog AM. Similarly, in PAM the modulation index is "
        "limited to values less than 1."))
    b.append(h4("Pulse Duration Modulation"))
    b.append(p(
        "PDM is made of unipolar, rectangular pulses whose durations or widths depend on the "
        "values of the samples. The period between the centers of two consecutive pulses is "
        "constant. The analysis of the resulting spectrum shows that it is possible to "
        "reconstruct the samples by low-pass filtering [9]."))
    b.append(h4("Pulse Position Modulation"))
    b.append(p(
        "PPM is closely related to PDM, as PPM can be generated through PDM. In PPM the "
        "information resides on the time location of the pulses rather than in the pulses "
        "themselves. It is then possible to transmit very narrow pulses to reduce the energy "
        "needed; this energy reduction is the most important advantage of PPM."))
    b.append(h4("Pulse Code Modulation for Time Division Multiplexing"))
    b.append(p(
        "All the previously analyzed subcarrier modulation schemes in telemetry systems are "
        "based on an analog signal that modulates either an analog carrier or a train of pulses. "
        "Pulse code modulation (PCM) is different: it is a digital modulation in which the "
        "measured signal is represented by a group of codified digital pulses. Two variations of "
        "PCM that are also often used are delta modulation (DM) and differential pulse code "
        "modulation (DPCM). In analog modulation schemes, the modulating signal from the "
        "transducer can take any value between the limits. If noise alters the modulating signal, "
        "it is impossible to decide its real value. Instead, if not all the values in the "
        "modulating signal are allowed, and the separation between the allowed levels is higher "
        "than the expected noise values, it is then possible to decide which were the values sent "
        "by the transmitter. This immunity against noise makes PCM systems one of the preferred "
        "alternatives for telemetry. Figure 87.9 shows the basic elements of a PCM telemetry "
        "system. A PCM encoder (or PCM commutator) converts the input data into a serial data "
        "format suitable for transmission through lines or by wireless techniques. At the "
        "receiving end, a PCM decoder (or PCM decommutator) converts the serial data back into "
        "individual output data signals. PCM systems transmit data as a serial stream of digital "
        "words. The PCM encoder samples the input data and inserts the data words into a PCM "
        "frame. Words are assigned specific locations in the PCM frame, so the decoder can "
        "recover the data samples corresponding to each input signal. The simplest PCM frame "
        "consists of a frame synchronization word followed by a string of data words. The frame "
        "repeats continually to provide new data samples as the input data change. Frame "
        "synchronization enables the PCM decoder to locate the start of each frame easily."))
    b.append(fig(9, "en"))

    b.append(h3("Pulse Code Modulation Telemetry Standards"))
    b.append(p(
        "IRIG Standard 106-96 also defines the characteristics of PCM transmission for telemetry "
        "purposes, in particular the pulse train structure and system design characteristics. The "
        "PCM formats are divided into two classes for Standards purposes: class I and class II. "
        "The simpler types are class I, whereas the more complex types are class II. Some of the "
        "characteristics of class II systems are bit rates greater than 5 Mbit/s, word lengths in "
        "excess of 16 bits, fragmented words, unevenly spaced subcommutation, format changes, "
        "tagged data formats, asynchronous data transmission, and merger of multiple format "
        "types, among others. Table 87.3 provides a brief summary of relevant PCM specifications. "
        "Readers interested in the detailed specifications and descriptions should refer to "
        "Chapter 4 of the IRIG 106-96 Standard [10]."))
    b.append(table_87_3("en"))
    b.append(p(
        "The following PCM codes, shown in Figure 87.10, are recognized by the IRIG Standards: "
        "NRZ-L (nonreturn to zero — level), NRZ-M (nonreturn to zero — mark), NRZ-S (nonreturn to "
        "zero — space), BiØ-L (biphase — level), BiØ-M (biphase — mark) and BiØ-S (biphase — "
        "space). The Standard also recommends that the transmitted bit stream be continuous and "
        "contain sufficient transitions to ensure bit acquisition and continued bit "
        "synchronization. Bit rates should be at least 10 bits/s. If the bit rate is above "
        "5 Mbit/s, the PCM system is classified as class II. In reference to the word formats, "
        "the Standard defines a fixed format as one that does not change during transmissions "
        "with regard to the frame structure, word length or location, commutation sequence, "
        "sample interval or measurement list. Individual words may vary in length from 4 bits to "
        "not more than 16 bits in class I and not more than 64 bits in class II. Fragmented "
        "words, defined as a word divided into not more than eight segments and placed in various "
        "locations within a minor frame, are only allowed in class II. All word segments used to "
        "form a data word are constrained to the boundaries of a single minor frame. The frame "
        "structure allowed by the Standards for PCM telemetry specifies that data are formatted "
        "into fixed frame lengths that contain a fixed number of equal-duration bit intervals. A "
        "minor frame is defined as the data structure in time sequence from the beginning of a "
        "minor frame synchronization pattern to the beginning of the next minor frame "
        "synchronization pattern. The minor frame length is the number of bit intervals from the "
        "beginning of the frame synchronization pattern to the beginning of the next "
        "synchronization pattern. The maximum length of a minor frame will not exceed 8192 bits "
        "nor 1024 words in class I and will not exceed 16,384 bits in class II. Minor frames "
        "consist of the synchronization pattern, data words, and subframe synchronization words "
        "if they are used. The Standard allows the use of words of different length if they are "
        "multiplexed in a single minor frame. Figure 87.11 shows a graphical representation of a "
        "PCM frame structure. Major frames contain the number of minor frames required to include "
        "one sample of every parameter in the format. Their length is defined as the minor frame "
        "length multiplied by the number of minor frames contained in the major frame. The "
        "maximum number of minor frames per major frame is limited to 256."))
    b.append(fig(10, "en"))
    b.append(fig(11, "en"))
    b.append(p(
        "Appendix C in the 106-96 IRIG Standard gives recommendations for maximal transmission "
        "efficiency in PCM telemetry. The intermediate-frequency (IF) bandwidth for PCM telemetry "
        "data receivers should be selected so that 90 to 99% of the transmitted power spectrum is "
        "within the receiver 3-dB bandwidth. The IF also has effects on the bit error probability "
        "(BEP) according to the following equation for NRZ-L PCM/FM [10]:"))
    b.append(eq("BEP = 0.5e<sup><i>k</i>·SNR</sup>", "87.13"))
    b.append(p("where <i>k</i> ≈ −0.7 for IF bandwidth equal to bit rate"))
    b.append(ul(["<i>k</i> ≈ −0.65 for IF bandwidth equal to 1.2 times bit rate",
                 "<i>k</i> ≈ −0.55 for IF bandwidth equal to 1.5 times bit rate"]))
    b.append(p(
        "Other data codes and modulation techniques have different BEP vs. SNR performance "
        "characteristics, but in any case they will have similar trends."))
    b.append(p(
        "The Standard also specifies the recommended frame synchronization patterns for general "
        "use in PCM telemetry. There are different lengths for synchronization patterns, but in "
        "all of them 111 is the first bit sequence transmitted. The patterns for lengths 16 to 30 "
        "were selected in order to minimize the probability of false synchronization over the "
        "entire pattern overlap portion of the ground station frame synchronization [12]. The "
        "spectral density (<i>S</i>) for the NRZ and BiØ codes is"))
    b.append(eq("NRZ: <i>S</i> = " +
                _frac("sin<sup>2</sup>(π<i>fT</i>)", "(π<i>fT</i>)<sup>2</sup>"), "87.14"))
    b.append(eq("Biphase: <i>S</i> = " +
                _frac("sin<sup>4</sup>(π<i>fT</i>/2)", "(π<i>fT</i>/2)<sup>4</sup>"), "87.15"))
    b.append(p(
        "The calculation of spectral densities allows the determination of the BEP for the "
        "previous type of codes, assuming perfect bit synchronization. These calculations show "
        "that for the same SNR the lowest BEP is achieved for NRZ-L and Bi codes, followed by NRZ "
        "and BiØ mark and space codes and finally for random NRZ-L codes (RNRZ-L)."))
    b.append(p(
        "Telemetry data are usually recorded onto magnetic tape for later analysis. When "
        "recording PCM data, it is important to ensure that the tape recorder provides sufficient "
        "frequency response to capture and reproduce the PCM signal. Useful rules to calculate "
        "the maximum bit rate for various PCM codes specify that for NRZ and RNRZ codes the "
        "maximum bit rate is 1.4 times the tape recorder frequency response, while for all "
        "biphase codes the maximum rate is 0.7 times the tape recorder response. To limit the "
        "transmission bandwidth that PCM creates because it is a digital signal with sharp "
        "transitions, the PCM signal is usually passed through a premodulation filter before it "
        "is fed into the transmitter input. The filter cutoff frequency can be calculated as 0.7 "
        "times the PCM bit rate for NRZ and RNRZ codes and 1.4 times the PCM bit rate for all "
        "biphase codes."))

    # ---------------------------------------------------------- terms
    b.append(h2("Chapter 87 terminology"))
    b.append(note(
        "Added by the translator; this section is not in the original. It gathers the terms that "
        "chapter 87 itself defines under “Defining Terms” into one list for reference while "
        "reading. The definitions keep the original’s content and only compress the wording."))
    b.append(_glossary(_GLOSS_EN))

    b.append(h2("References"))
    b.append(refs(_REFS))
    b.append(h2("Further Information"))
    b.append('<ul class="ref-list">%s</ul>' % "".join("<li>%s</li>" % i for i in _FURTHER_EN))
    return "".join(b)


# ================================================================ PAGE
def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 87 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 87 — %s · Measurement, Instrumentation and Sensors Handbook"
                  % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 87 “Đo từ xa” của Albert Lozano-Nieto — đo từ xa băng "
            "gốc theo điện áp, dòng điện và tần số, ghép kênh theo tần số và theo thời gian, "
            "các sơ đồ điều chế PAM/PDM/PPM và PCM, cùng các tiêu chuẩn IRIG, với 11 hình, 3 "
            "bảng và 12 tài liệu tham khảo." if vi
            else
            "Companion to Chapter 87 of the CRC Measurement Handbook — base-band telemetry by "
            "voltage, current and frequency; frequency and time division multiplexing; the "
            "PAM/PDM/PPM and PCM modulation schemes; and the IRIG standards, with 11 figures, 3 "
            "tables and 12 references.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm '
             'biến</a> · Chương 87' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 87' % BASE_EN)
    meta = ("Chương 87 · theo Ch87.pdf (CRC Press, 1999) · 11 hình, 3 bảng, 15 công thức" if vi
            else "Chapter 87 · 11 figures, 3 tables, 15 equations")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE if vi else BYLINE_EN, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 87)))
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
