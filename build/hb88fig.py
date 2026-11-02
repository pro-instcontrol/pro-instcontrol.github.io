# -*- coding: utf-8 -*-
"""Figures 88.1–88.5 for Handbook Chapter 88 — Sensor Networks and Communication.

88.1  a networked sensor: an ordinary sensor plus network communication
88.2  the ISO/OSI seven-layer reference model
88.3  a sample RS-485 differential waveform
88.4  a comparison of selected network parameters  (a table on the page,
      so it is rendered here as an HTML table rather than as line art)
88.5  four network topologies drawn with four stations each

All five were read off the page rasters of work/Ch88.pdf at 200 dpi. Two
measurements from 88.3 are worth recording because they fix the drawing:
the V1 trace sits at raster y=269 and V2 at y=358 with the axis at y=432,
and the nine bit boundaries fall 90 px apart (x=344…973) while the
crossing notches occur only at the boundaries where the bit VALUE changes
(x=344, 434, 614, 793, 973 for the bit string 0 1 1 0 0 1 1 0). That is
why the redrawn waveform notches at boundaries 0, 1, 3, 5 and 7 and stays
flat at 2, 4 and 6.

88.1, 88.2 and 88.5 are line drawings rebuilt from the printed originals;
88.3 is a schematic redrawn on a clean grid from the measured geometry.

NOTE: never emit <sub>/<sup> inside <svg> text — both are on the HTML parser's
breakout list and eject the parser from SVG foreign content.
"""
import math

from hbfig import svg, _fig
from hb93base import (E, S, GRID, GOLD, BLUE, TEAL, RED, GREEN, _defs, _lbl, _r,
                      _line, _arr, _rect, _poly, _path, _dot, _circ, _hatch, Frame)

GREY = "#8a8a8a"
PALE = "#c9c9c9"


# ================================================================ 88.1
def fig_88_1():
    o = [_defs("881")]
    # dashed enclosure
    o.append(_rect(150, 56, 320, 180, 1.3, "#fff", "7 5"))
    o.append(_lbl(310, 46, "Cảm biến có mạng", "tb", "middle"))

    # the two inner blocks
    o.append(_rect(178, 78, 88, 140, 1.4))
    o.append(_rect(322, 78, 108, 140, 1.4))
    o.append(_lbl(222, 152, "Cảm biến", "tm", "middle"))
    o.append(_lbl(376, 144, "Bộ xử lý", "tm", "middle"))
    o.append(_lbl(376, 158, "mạng", "tm", "middle"))

    # the link between them, and the dotted tap that runs down to the caption
    o.append(_line(266, 148, 322, 148, 1.4))
    o.append(_line(294, 148, 352, 284, 1.1, S, "2 4"))

    # measured variable, arriving as a bolt
    o.append(_path([(58, 200), (96, 152), (104, 182)], 1.6))
    o.append(_arr(104, 182, 172, 150, "881", 1.6))
    o.append(_lbl(54, 232, "Đại lượng đo", "tm"))

    # the network itself
    o.append(_line(520, 24, 520, 300, 1.5))
    o.append(_line(430, 148, 520, 112, 1.5))
    o.append(_line(430, 148, 520, 184, 1.5))
    o.append(_lbl(534, 64, "Mạng", "tm"))
    o.append(_lbl(534, 78, "truyền thông", "tm"))

    # what the dotted tap is pointing at
    o.append(_lbl(300, 296, "biểu diễn bằng tín hiệu điện", "ts", "middle"))
    o.append(_lbl(300, 310, "của đại lượng đo", "ts", "middle"))

    return _fig(svg(680, 330, "".join(o),
                    "Cảm biến có mạng: cảm biến, bộ xử lý mạng và đường nối ra mạng"),
                "Hình 88.1 · Cảm biến có mạng là một cảm biến thông thường được thêm các thành "
                "phần truyền thông mạng. Đường chấm là đầu ra tương tự của cảm biến trước khi "
                "số hoá.",
                "Figure 88.1 · A networked sensor is an ordinary sensor with network "
                "communication components added. The dotted tap is the sensor’s analog output, "
                "taken before digitisation.",
                "Sơ khối cảm biến có mạng gồm khối cảm biến nối với khối xử lý mạng, "
                "có đường tín hiệu đo đi vào và hai nhánh nối ra mạng",
                "Block diagram of a networked sensor: a sensor block linked to a network "
                "processor block, with the measured variable entering and two branches "
                "leaving to the network")


# ================================================================ 88.2
_LAYERS = ["7 - Ứng dụng", "6 - Trình diễn", "5 - Phiên", "4 - Giao vận",
           "3 - Mạng", "2 - Liên kết dữ liệu", "1 - Vật lý"]


def fig_88_2():
    o = [_defs("882")]
    x, w, h = 225, 230, 34
    for i, lab in enumerate(_LAYERS):
        y = 20 + i * h
        o.append(_rect(x, y, w, h, 1.3))
        o.append(_lbl(x + 10, y + 21, lab, "tm"))
    # the funnel down to the medium
    o.append(_path([(295, 300), (340, 258), (385, 300)], 1.4))
    o.append(_line(200, 300, 480, 300, 1.4))
    o.append(_lbl(392, 296, "Môi trường", "ts"))

    return _fig(svg(680, 320, "".join(o),
                    "Mô hình bảy tầng ISO-OSI xếp chồng, tầng 7 ở trên, tầng 1 ở dưới"),
                "Hình 88.2 · Mô hình bảy tầng ISO-OSI đưa ra một cách phân đoạn các chức năng "
                "truyền thông. Tầng 1 nối xuống môi trường truyền vật lý.",
                "Figure 88.2 · The ISO-OSI seven-layer model provides a method for segmenting "
                "communication functions. Layer 1 connects down to the physical medium.",
                "Bảy hộp xếp chồng từ tầng ứng dụng xuống tầng vật lý, dưới cùng là phễu "
                "nối xuống môi trường truyền",
                "Seven stacked boxes from application layer down to physical layer, with a "
                "funnel at the bottom leading to the transmission medium")


# ================================================================ 88.3
_BITS = ["0", "1", "1", "0", "0", "1", "1", "0"]
_NOTCH = {0, 1, 3, 5, 7}          # boundaries where the bit value changes


def fig_88_3():
    o = [_defs("883")]
    y1, y2, ym = 64, 120, 92      # V1 level, V2 level, crossing level
    x0, cw = 96, 64               # first boundary, cell width
    n = len(_BITS)
    xa, xb = 56, 640              # vertical axis, right end of the axis

    # axes
    o.append(_line(xa, 24, xa, 190, 1.3))
    o.append(_line(xa, 190, xb, 190, 1.3))

    # bit boundaries
    for i in range(n + 1):
        bx = x0 + i * cw
        o.append(_line(bx, 40, bx, 172, 1.0, S, "4 4"))

    # the two traces: flat except for a crossing notch at a bit change
    def trace(level, sign):
        pts = [(x0 - 14, level)]
        for i in range(n + 1):
            if i in _NOTCH:
                bx = x0 + i * cw
                pts += [(bx - 13, level), (bx, ym), (bx + 13, level)]
        pts.append((xb, level))
        return _path(pts, 1.9)

    o.append(trace(y1, -1))
    o.append(trace(y2, +1))

    # labels
    o.append(_r(60, 60, [("V", False), ("1", True)], "start", "tm"))
    o.append(_r(60, 116, [("V", False), ("2", True)], "start", "tm"))
    o.append(_lbl(634, 182, "Đất", "tm", "end"))

    # bit values, one per cell
    for i, bit in enumerate(_BITS):
        cx = x0 + i * cw + cw / 2.0
        o.append(_lbl(cx, 172, "“%s”" % bit, "tm", "middle"))

    return _fig(svg(680, 230, "".join(o),
                    "Dạng sóng RS-485 vi sai: hai vết V1 và V2 cắt nhau tại mỗi chuyển bit"),
                "Hình 88.3 · Một dạng sóng RS-485 mẫu, cho thấy điện áp trên cặp dây vi sai (V1, "
                "V2) cùng các khoảng bit chồng lên, ghi các bit 0 và 1. Hai vết chỉ cắt nhau ở "
                "ranh giới bit có đổi giá trị — đúng như hình in. Mốc đất là tuỳ ý trong dải "
                "mức tín hiệu đã định nghĩa.",
                "Figure 88.3 · A sample RS-485 waveform showing voltages on the differential "
                "wire pair (V1, V2) and superimposed bit intervals showing 0 and 1 bits. The "
                "traces cross only at the bit boundaries where the value changes, exactly as "
                "printed. The ground reference is arbitrary within the defined signaling range.",
                "Hai vết điện áp đối pha V1 và V2, mỗi ô bit có một nhãn 0 hoặc 1, "
                "các vết cắt nhau tại những ranh giới bit có đổi giá trị",
                "Two complementary voltage traces V1 and V2, each bit cell labelled 0 or 1, "
                "crossing at the bit boundaries where the value changes")


# ================================================================ 88.4
# The page prints this comparison as FIGURE 88.4, but the content is a table,
# so it is built as one: an SVG would not reflow and would be unreadable on a
# phone. The caption keeps the original figure number.
_R44 = [("RS-232", "30 m", "2", "115 kb/s", "2", "TP", "P-P"),
        ("RS-485", "1200 m", "32", "10 Mb/s", "2", "TP", "D-C"),
        ("Seriplex", "1500 m", "256", "200 kb/s", "4", "2STP", "D-C,Free"),
        ("AS-i", "100 m", "32", "167 kb/s", "2", "UP", "T-B"),
        ("Interbus-S", "25.6 km*", "64", "500 kb/s", "6", "3STP", "Ring"),
        ("CAN", "450 m", "64", "1 Mb/s", "4", "2STP", "T-B"),
        ("4-20 mA", "1000 m", "2", "-", "2", "STP", "P-P"),
        ("HART", "1000 m", "2(15)", "1200 b/s", "2", "STP", "P-P(D-C)"),
        ("Profibus", "9600 m", "126", "12 Mb/s", "2", "STP", "D-C"),
        ("Found. Fieldbus", "1900 m", "32", "2.5 Mb/s", "2", "STP", "D-C"),
        ("LonWorks", "1400 m", "64", "1.2 Mb/s", "2", "STP", "D-C,Free")]


def _vnum(s):
    """Vietnamese number formatting for the 88.4 cells: '.' thousands, ',' decimal."""
    import re

    def fix(m):
        t = m.group(0)
        ip, _dot, fp = t.partition(".")
        out = []
        for i, ch in enumerate(ip):
            out.append(ch)
            rem = len(ip) - i - 1
            if rem and rem % 3 == 0:
                out.append(".")
        return "".join(out) + ("," + fp if _dot else "")

    return re.sub(r"\d+(?:\.\d+)?", fix, s)


def table_88_4(lang="vi"):
    if lang == "vi":
        hd = ("", "Chiều dài", "Số trạm", "Tốc độ bit", "Số dây", "Môi trường", "Tô-pô")
        rows = [tuple([r[0]] + [_vnum(c) for c in r[1:]]) for r in _R44]
        note = ("Ghi chú: P-P = điểm tới điểm; D-C = chuỗi nối tiếp (daisy-chain); T-B = đường "
                "trục – nhánh; TP = cặp xoắn; STP = cặp xoắn có vỏ bọc; UP = cặp không bọc. "
                "* Tối đa 400 m giữa hai trạm. ** Các tham số cực đại của một mạng không đạt "
                "được đồng thời, và không tính bộ lặp, bộ định tuyến hay cổng nối. Tham số cực "
                "đại là ước lượng dựa trên thông tin sẵn có.")
        cap = ("Hình 88.4 · So sánh một số tham số (giá trị cực đại) của các công nghệ mạng "
               "khác nhau. " + note)
    else:
        hd = ("", "Length", "Stations", "Bit Rate", "Wires", "Media", "Topology")
        rows = _R44
        note = ("Notes: P-P = point to point; D-C = daisy-chain; T-B = trunkline-branchline; "
                "TP = twisted pair; STP = shielded twisted pair; UP = unshielded pair. "
                "* Maximum 400 m between stations. ** Maximum parameters for networks are not "
                "achievable simultaneously, and do not include repeaters, routers, or gateways. "
                "Maximum parameters are estimates based on available information.")
        cap = ("Figure 88.4 · A comparison of selected parameters (maximum values) for various "
               "network technologies. " + note)

    head = "".join('<th scope="col">%s</th>' % h for h in hd)
    body = "".join('<tr><th scope="row">%s</th>%s</tr>'
                   % (r[0], "".join("<td>%s</td>" % c for c in r[1:])) for r in rows)
    return ('<div class="table-wrap"><table class="tbl dense" style="min-width:560px">'
            '<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % (head, body, cap))


def fig_88_4(lang="vi"):
    """The page calls it a figure; the content is tabular, so it is a table."""
    return ('<figure class="figure" id="fig-88-4">%s</figure>' % table_88_4(lang))


# ================================================================ 88.5
def _stations(pts, r=5.0):
    return "".join(_circ(x, y, r, E, "#fff", 1.5) for x, y in pts)


def fig_88_5():
    o = [_defs("885")]

    # ---- star: four stations, every pair joined, the joins crossing in the middle
    s = [(120, 62), (220, 62), (120, 132), (220, 132)]
    o.append(_line(*s[0], *s[3], 1.4))
    o.append(_line(*s[1], *s[2], 1.4))
    o.append(_stations(s))
    o.append(_lbl(170, 158, "Hình sao", "tm", "middle"))

    # ---- daisy chain: the four joined in series, left side left open
    d = [(460, 62), (560, 62), (460, 132), (560, 132)]
    o.append(_path([d[0], d[1], d[3], d[2]], 1.4))
    o.append(_stations(d))
    o.append(_lbl(510, 158, "Chuỗi nối tiếp", "tm", "middle"))

    # ---- trunkline-branchline: two trunks, joined at the right, stubs out to stations
    t = [(120, 214), (220, 214), (120, 284), (220, 284)]
    o.append(_path([t[0], (140, 227), (200, 227), (220, 214)], 1.4))
    o.append(_path([t[2], (140, 271), (200, 271), (220, 284)], 1.4))
    o.append(_line(200, 227, 200, 271, 1.4))
    o.append(_stations(t))
    o.append(_lbl(170, 312, "Đường trục – nhánh", "tm", "middle"))

    # ---- ring: all four sides closed, circulation clockwise
    g = [(460, 214), (560, 214), (460, 284), (560, 284)]
    o.append(_path([g[0], g[1], g[3], g[2]], 1.4, close=True))
    o.append(_stations(g))
    o.append(_poly([(502, 208), (502, 220), (514, 214)], 1.0, E, E))
    o.append(_poly([(554, 242), (566, 242), (560, 254)], 1.0, E, E))
    o.append(_poly([(518, 278), (518, 290), (506, 284)], 1.0, E, E))
    o.append(_poly([(454, 256), (466, 256), (460, 244)], 1.0, E, E))
    o.append(_lbl(510, 312, "Vòng", "tm", "middle"))

    return _fig(svg(680, 340, "".join(o),
                    "Bốn kiểu tô-pô mạng, mỗi kiểu vẽ với bốn trạm: hình sao, chuỗi nối tiếp, "
                    "đường trục – nhánh và vòng"),
                "Hình 88.5 · Một vài ví dụ trong rất nhiều kiểu tô-pô mạng có thể có, vẽ với bốn "
                "trạm. Vòng có mũi tên chỉ chiều lưu thông dữ liệu.",
                "Figure 88.5 · Some examples of the many possible network topologies using four "
                "stations. The ring carries arrows showing the direction data circulates.",
                "Bốn ô, mỗi ô vẽ bốn trạm tròn nối với nhau theo kiểu hình sao, chuỗi, "
                "đường trục có nhánh, và vòng khép kín có mũi tên",
                "Four panels, each showing four round stations wired as a star, a daisy chain, "
                "a trunkline with branches, and a closed ring with direction arrows")
