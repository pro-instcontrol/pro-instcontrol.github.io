# -*- coding: utf-8 -*-
"""Figures 87.1–87.11 for Handbook Chapter 87 — Telemetry.

87.1   block diagram of a telemetry system
87.2   (a) FDM channel allocation and (b) TDM pulse train
87.3   three base-band configurations: voltage, current, frequency
87.4   multiplexed multi-channel telemetry
87.5   (a) FDM transmitter and (b) the composite spectrum with guard bands
87.6   (a) a base-band spectrum and (b) its amplitude-modulated spectrum
87.7   (a) a TDM link and (b) the sampled channels and the frame
87.8   PAM, PDM and PPM against the same sampling instants
87.9   a PCM link
87.10  the six IRIG PCM codes for the bit string 1 0 1 1 0
87.11  PCM minor-frame and major-frame structure

87.2, 87.6, 87.7 and 87.8 were read off the 200 dpi page rasters. 87.10 is the
one figure that could not be transcribed point by point: the printed rows are
only a few pixels tall per transition and the right-hand edge of the biphase
rows is ambiguous even at 400 dpi. It is therefore *generated* from the
definitions the caption states, which is self-consistent and matches the print
for NRZ-L, NRZ-M, NRZ-S, BiO-L and BiO-M bit for bit.

Two printed defects are reproduced as-is and flagged in the chapter note:
Figure 87.4 labels two different conditioning boxes "CONDITIONING CIRCUIT 3",
and Figure 87.5a labels all three subcarrier multipliers "fosc1" while panel
(b) of the same figure marks fosc1, fosc2 and fosc3.

NOTE: never emit <sub>/<sup> inside <svg> text — both are on the HTML parser's
breakout list and eject the parser from SVG foreign content.
"""
import math

from hbfig import svg, _fig
from hb93base import (E, S, GRID, GOLD, BLUE, TEAL, RED, GREEN, _defs, _lbl, _r,
                      _line, _arr, _rect, _poly, _path, _dot, _circ, _hatch, Frame)

GREY = "#8a8a8a"
PALE = "#d4d4d4"


# ================================================================ helpers
def _box(x, y, w, h, lines, sw=1.3, fs=None):
    """A rectangle with centred, multi-line text."""
    o = [_rect(x, y, w, h, sw)]
    n = len(lines)
    for i, t in enumerate(lines):
        yy = y + h / 2.0 + (i - (n - 1) / 2.0) * 11 + 3.4
        o.append(_lbl(x + w / 2.0, yy, t, "tm", "middle"))
    return "".join(o)


def _mult(x, y, r=13):
    """The multiplier node: a circle with a cross."""
    o = [_circ(x, y, r, E, "#fff", 1.3)]
    o.append(_line(x - r * .45, y - r * .45, x + r * .45, y + r * .45, 1.3))
    o.append(_line(x + r * .45, y - r * .45, x - r * .45, y + r * .45, 1.3))
    return "".join(o)


def _sum(x, y, w=44, h=52):
    o = [_rect(x, y, w, h, 1.3)]
    o.append(_lbl(x + w / 2.0, y + h / 2.0 + 5, "Σ", "tb", "middle"))
    return "".join(o)


def _antenna(x, ybase, h=26):
    """The chapter's antenna symbol: a stub rising to an inverted triangle.

    The printed symbol is a triangle whose base is at the top and whose apex
    meets the feed stub below it (the shape reads like a martini glass).
    """
    o = [_line(x, ybase, x, ybase - h, 1.4)]
    o.append(_poly([(x - 9, ybase - h - 14), (x + 9, ybase - h - 14),
                    (x, ybase - h)], 1.3, "#fff", E))
    return "".join(o)


def _hrect(tag, x, y, w, h, step=7):
    """A white rectangle filled with diagonal hatching — a TDM sample pulse."""
    o = ['<rect x="%s" y="%s" width="%s" height="%s" fill="#fff"/>'
         % (int(x), int(y), int(w), int(h))]
    o.append(_hatch(tag, x, y, w, h, step))
    o.append(_rect(x, y, w, h, 1.2, "none"))
    return "".join(o)


def _radiate(x, y):
    """The little zigzag that means 'radiated'."""
    return _path([(x, y - 6), (x + 16, y + 2), (x + 30, y - 6), (x + 44, y + 2)], 1.2)


def _dimb(x1, x2, y, tag="", dy=-5, cls="ts"):
    """A horizontal double-headed dimension arrow with an optional label above."""
    o = [_line(x1, y, x2, y, 1.0)]
    o.append(_poly([(x1, y), (x1 + 7, y - 3.2), (x1 + 7, y + 3.2)], 1.0, E, E))
    o.append(_poly([(x2, y), (x2 - 7, y - 3.2), (x2 - 7, y + 3.2)], 1.0, E, E))
    if tag:
        o.append(_lbl((x1 + x2) / 2.0, y + dy, tag, cls, "middle"))
    return "".join(o)


def _dimv(y1, y2, x, tag="", dx=-5, cls="ts"):
    o = [_line(x, y1, x, y2, 1.0)]
    o.append(_poly([(x, y1), (x - 3.2, y1 + 7), (x + 3.2, y1 + 7)], 1.0, E, E))
    o.append(_poly([(x, y2), (x - 3.2, y2 - 7), (x + 3.2, y2 - 7)], 1.0, E, E))
    if tag:
        o.append(_lbl(x + dx, (y1 + y2) / 2.0 + 3.2, tag, cls, "end" if dx < 0 else "start"))
    return "".join(o)


def _hump(cx, half, h, n=48, dip=0.0):
    """A channel spectrum: two lobes with a notch of depth `dip` at the centre.

    Returns (x, height above the baseline) pairs, so a caller sitting on an
    axis at y = ay draws [(x, ay - v) for x, v in _hump(...)].
    """
    pts = []
    for i in range(n + 1):
        u = -1.0 + 2.0 * i / n
        a = abs(u)
        v = (1.0 - a ** 3) * (dip + (1.0 - dip) * (1.0 - math.exp(-(a * a) / 0.03)))
        pts.append((cx + u * half, h * v))
    return pts


# ================================================================ 87.1
def fig_87_1():
    o = [_defs("871")]
    # left column
    o.append(_box(40, 20, 112, 40, ["ĐẦU ĐO"]))
    o.append(_box(40, 92, 112, 40, ["KHỐI VÀO"]))
    o.append(_box(40, 164, 112, 52, ["ĐIỀU CHỈNH", "TÍN HIỆU"]))
    o.append(_arr(96, 60, 96, 90, "871"))
    o.append(_arr(96, 132, 96, 162, "871"))

    # the split
    o.append(_line(152, 190, 250, 190, 1.3))
    o.append(_line(250, 190, 250, 346, 1.3))
    o.append(_arr(250, 190, 298, 190, "871"))
    o.append(_arr(250, 266, 298, 266, "871"))
    o.append(_arr(250, 346, 298, 346, "871"))

    # the three forward paths
    o.append(_box(300, 164, 130, 52, ["BỘ MÃ HOÁ"]))
    o.append(_box(462, 164, 130, 52, ["BỘ LẶP"]))
    o.append(_arr(430, 190, 460, 190, "871"))
    o.append(_arr(592, 190, 642, 190, "871"))

    o.append(_box(300, 240, 130, 52, ["BỘ ĐIỀU CHẾ"]))
    o.append(_box(462, 240, 130, 52, ["THÍCH ỨNG", "ĐƯỜNG DÂY"]))
    o.append(_arr(430, 266, 460, 266, "871"))
    o.append(_arr(592, 266, 642, 266, "871"))

    o.append(_box(300, 320, 130, 52, ["KHUẾCH ĐẠI RF", "+ ĐIỀU CHẾ"]))
    o.append(_line(430, 346, 622, 346, 1.3))
    o.append(_antenna(622, 346, 22))
    o.append(_radiate(634, 300))

    # labels
    o.append('<text class="ts" x="652" y="232" text-anchor="middle" '
             'transform="rotate(-90 652 232)">Đo từ xa có dây</text>')
    o.append(_lbl(540, 366, "Đo từ xa không dây", "ts", "middle"))

    return _fig(svg(680, 400, "".join(o),
                    "Sơ đồ khối một hệ đo từ xa: ba khối vào, ba đường ra có dây và không dây"),
                "Hình 87.1 · Sơ đồ khối của một hệ đo từ xa. Đo từ xa bằng dây có thể thực hiện "
                "theo kiểu băng gốc (bộ mã hoá và bộ lặp) hoặc bằng cách gửi một tín hiệu đã "
                "điều chế (bộ điều chế và thích ứng đường dây), trong khi đo từ xa không dây "
                "dùng sóng mang RF và một ăng-ten.",
                "Figure 87.1 · Block diagram for a telemetry system. Telemetry using wires can be "
                "performed in either base-band or by sending a modulated signal, while wireless "
                "telemetry uses an RF carrier and an antenna.",
                "Sơ đồ khối: đầu đo nối với khối vào rồi khối điều chỉnh tín hiệu, sau đó tách "
                "thành ba nhánh — bộ mã hoá và bộ lặp, bộ điều chế và thích ứng đường dây, và "
                "khuếch đại RF nối với ăng-ten",
                "Block diagram: transducer, front-end and signal conditioning feeding three "
                "branches — codifier and repeater, modulator and line adapter, and an RF power "
                "stage driving an antenna")


# ================================================================ 87.2
_PATTERNS = """
<pattern id="p872a" width="6" height="6" patternUnits="userSpaceOnUse"
 patternTransform="rotate(35)"><line x1="0" y1="0" x2="0" y2="6"
 stroke="#2a2a2a" stroke-width="1.6"/></pattern>
<pattern id="p872b" width="5" height="5" patternUnits="userSpaceOnUse"
 patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5"
 stroke="#2a2a2a" stroke-width="2.4"/></pattern>
<pattern id="p872c" width="6" height="6" patternUnits="userSpaceOnUse">
 <rect width="6" height="6" fill="#fff"/>
 <circle cx="1.6" cy="1.6" r="1.1" fill="#2a2a2a"/>
 <circle cx="4.6" cy="4.6" r="1.1" fill="#2a2a2a"/></pattern>
<pattern id="p872d" width="6" height="5" patternUnits="userSpaceOnUse">
 <line x1="0" y1="1.4" x2="6" y2="1.4" stroke="#2a2a2a" stroke-width="1.2"/>
 <line x1="0" y1="3.8" x2="6" y2="3.8" stroke="#2a2a2a" stroke-width="1.2"/></pattern>
"""


def fig_87_2():
    o = [_defs("872"), "<defs>" + _PATTERNS + "</defs>"]

    # ---------------- panel a: FDM
    o.append(_lbl(40, 26, "a)", "tb"))
    ax_y = 160
    o.append(_line(60, 40, 60, ax_y, 1.3))
    o.append(_arr(60, ax_y, 636, ax_y, "872"))
    o.append(_lbl(60, 34, "Biên độ", "ts"))
    o.append(_lbl(646, ax_y + 4, "f", "tf"))

    centres = [148, 288, 428, 568]
    for i, cx in enumerate(centres):
        o.append(_lbl(cx, 72, "Kênh %d" % (i + 1), "ts", "middle"))
        pts = [(x, ax_y - y) for x, y in _hump(cx, 56, 58, 48, 0.30)]
        o.append(_path(pts, 1.5))
        o.append(_line(cx, ax_y, cx, ax_y + 5, 1.1))
        o.append(_r(cx, ax_y + 17, [("f", False), ("c%d" % (i + 1), True)], "middle", "ts"))

    # ---------------- panel b: TDM
    o.append(_lbl(40, 218, "b)", "tb"))
    ay = 366
    o.append(_line(60, 236, 60, ay, 1.3))
    o.append(_arr(60, ay, 636, ay, "872"))
    o.append(_lbl(60, 230, "Biên độ", "ts"))
    o.append(_lbl(646, ay + 4, "t", "tf"))

    fills = ["p872a", "p872b", "p872c", "p872d", "p872a", "p872b", "p872c"]
    names = ["1", "2", "3", "4", "1", "2", "3"]
    for i in range(7):
        x = 92 + i * 66
        o.append('<rect x="%d" y="%d" width="40" height="86" fill="url(#%s)" '
                 'stroke="#2a2a2a" stroke-width="1.2"/>' % (x, ay - 86, fills[i]))
        o.append(_lbl(x + 20, ay - 92, "Kênh " + names[i], "ts", "middle"))
        o.append(_line(x + 20, ay, x + 20, ay + 5, 1.1))
        o.append(_r(x + 20, ay + 17, [("t", False), ("%d" % (i + 1), True)], "middle", "ts"))
    o.append(_lbl(596, ay - 20, "…", "tb", "middle"))

    return _fig(svg(680, 400, "".join(o),
                    "Hai đặc trưng cơ bản: (a) phổ các kênh của FDM, (b) chuỗi xung của TDM"),
                "Hình 87.2 · Đặc trưng cơ bản của tín hiệu (a) FDM và (b) TDM. Trong FDM các "
                "kênh khác nhau được cấp những tần số sóng mang phụ khác nhau (fc1, fc2, …), "
                "còn trong TDM tại mỗi thời điểm chỉ một kênh được truyền; các kênh còn lại "
                "được truyền lần lượt.",
                "Figure 87.2 · Basic characteristics of (a) FDM and (b) TDM signals. In FDM "
                "different channels are allocated at different subcarrier frequencies (fc1, "
                "fc2, …) while in TDM only one channel is transmitted at a given time. The "
                "remaining channels are transmitted sequentially.",
                "Hai đồ thị: phổ bốn kênh FDM xếp cạnh nhau theo tần số, và chuỗi xung bảy ô "
                "TDM xếp theo thời gian",
                "Two plots: four FDM channel spectra side by side in frequency, and a "
                "seven-slot TDM pulse train in time")


# ================================================================ 87.3
def _line_pair(x1, x2, ytop, ybot, zl=True, vin=None, vout=None, zin=False,
               rw=52):
    """The two-conductor link with its series Z_L resistors and optional taps."""
    o = [_line(x1, ytop, x2, ytop, 1.2), _line(x1, ybot, x2, ybot, 1.2)]
    o.append(_line(x1, ytop, x1, ybot, 1.2))
    xm = (x1 + x2) / 2.0
    mid = (ytop + ybot) / 2.0 + 4
    if zl:
        o.append(_rect(xm - rw / 2, ytop - 4, rw, 8, 1.2))
        o.append(_rect(xm - rw / 2, ybot - 4, rw, 8, 1.2))
        o.append(_r(xm, mid, [("Z", False), ("L", True)], "middle", "ts"))
    if vin:
        o.append(_arr(x1 + 16, ybot - 4, x1 + 16, ytop + 6, "873"))
        o.append(_r(x1 + 22, mid, [("V", False), ("in", True)], "start", "ts"))
    if vout:
        o.append(_arr(x2 - 20, ybot - 4, x2 - 20, ytop + 6, "873"))
        o.append(_r(x2 - 26, mid, [("V", False), ("out", True)], "end", "ts"))
    if zin:
        o.append(_rect(x2 - 14, ytop + 4, 8, ybot - ytop - 8, 1.2))
        o.append(_r(x2 - 18, mid, [("Z", False), ("in", True)], "end", "ts"))
    return "".join(o)


def fig_87_3():
    o = [_defs("873")]

    def row(y, tag, left, right, mid=None, **kw):
        p = []
        p.append(_lbl(12, y + 5, "V", "tf"))
        p.append(_arr(24, y, 44, y, "873"))
        p.append(_box(46, y - 22, 96, 44, [left] if isinstance(left, str) else left))
        if mid:
            p.append(_arr(142, y, 162, y, "873"))
            p.append(_box(164, y - 22, 58, 44, [mid] if isinstance(mid, str) else mid))
            p.append(_arr(222, y, 242, y, "873"))
            px = 242
        else:
            p.append(_arr(142, y, 164, y, "873"))
            px = 164
        p.append(_line_pair(px, 380, y - 13, y + 13, **kw))
        p.append(_arr(380, y, 400, y, "873"))
        p.append(_box(402, y - 26, 116, 52, [right] if isinstance(right, str) else right))
        p.append(_arr(518, y, 538, y, "873"))
        p.append(_box(540, y - 26, 116, 52, ["HIỂN THỊ,", "LƯU TRỮ,", "XỬ LÝ…"]))
        p.append(_lbl(6, y - 26, tag + ")", "tb"))
        return "".join(p)

    o.append(row(56, "a", "ĐIỀU CHỈNH", ["CẢM BIẾN XA", "VÀ KHUẾCH ĐẠI"],
                 None, vin=True, zin=True))
    o.append(row(166, "b", "ĐIỀU CHỈNH", ["I/V"], "V/I", zin=True))
    o.append(row(276, "c", ["V/F"], ["F/V"], None, vin=True, vout=True))

    return _fig(svg(680, 320, "".join(o),
                    "Ba cách bố trí đo từ xa băng gốc: theo điện áp, theo dòng điện, theo tần số"),
                "Hình 87.3 · Ba cách bố trí khác nhau cho đo từ xa băng gốc. Ở (a) thông tin "
                "được truyền dưới dạng biến thiên của một tín hiệu điện áp. Ở (b) người ta gửi "
                "một tín hiệu dòng điện thay cho điện áp, để trung hoà sự suy giảm do bộ chia "
                "điện áp tạo bởi trở kháng vào của bên thu (Zin) và trở kháng đường dây (ZL). Ở "
                "(c) thông tin được truyền dưới dạng biến thiên tần số, nhờ đó hệ miễn nhiễm "
                "với nhiễu và giao thoa tác động lên biên độ tín hiệu.",
                "Figure 87.3 · Different configurations for base-band telemetry. In voltage-based "
                "base-band telemetry (a) the information is transmitted as variations of a "
                "voltage signal. Current-based base-band telemetry (b) is based on sending a "
                "current signal instead of a voltage signal to neutralize the signal degradation "
                "due to the voltage divider made up by the input impedance of the receiver (Zin) "
                "and the impedance of the lines (ZL). In frequency-based base-band telemetry (c), "
                "the information is transmitted as variations of frequency, which makes this "
                "system immune to noise and interference that affect the amplitude of the "
                "transmitted signal.",
                "Ba sơ đồ hàng ngang: điều chỉnh nối thẳng tới cảm biến xa qua đường dây hai "
                "dây có trở kháng ZL, qua bộ chuyển V/I rồi I/V, và qua bộ chuyển V/F rồi F/V",
                "Three horizontal chains: conditioning straight to the remote sensor through a "
                "two-wire line with ZL, through a V/I then I/V pair, and through a V/F then F/V "
                "pair")


# ================================================================ 87.4
def fig_87_4():
    o = [_defs("874")]
    rows = [(40, "CẢM BIẾN 1", "MẠCH ĐIỀU CHỈNH 1"),
            (110, "CẢM BIẾN 2", "MẠCH ĐIỀU CHỈNH 3"),
            (196, "CẢM BIẾN 3", "MẠCH ĐIỀU CHỈNH 3")]
    for y, s, c in rows:
        o.append(_arr(12, y, 32, y, "874"))
        o.append(_box(34, y - 18, 96, 36, [s]))
        o.append(_box(132, y - 18, 118, 36, [c]))
    o.append(_lbl(150, 168, "…", "tb", "middle"))

    # fan-in to the multiplexer
    o.append(_line(250, 40, 300, 76, 1.2))
    o.append(_line(250, 110, 300, 110, 1.2))
    o.append(_line(250, 196, 300, 144, 1.2))
    o.append(_lbl(272, 168, "…", "tb", "middle"))

    o.append(_box(302, 56, 118, 108, ["BỘ GHÉP KÊNH", "&", "BỘ ĐIỀU CHẾ"]))
    o.append(_line(420, 110, 442, 110, 1.2))
    o.append(_lbl(452, 106, "KÊNH", "ts", "middle"))
    o.append(_line(472, 110, 494, 110, 1.2))
    o.append(_box(496, 56, 118, 108, ["BỘ TÁCH KÊNH", "&", "BỘ GIẢI ĐIỀU CHẾ"]))

    # fan-out
    o.append(_line(614, 86, 654, 54, 1.2))
    o.append(_line(614, 110, 654, 100, 1.2))
    o.append(_line(614, 134, 654, 168, 1.2))
    o.append(_lbl(636, 140, "…", "tb", "middle"))

    return _fig(svg(680, 240, "".join(o),
                    "Nhiều kênh đo chia sẻ một kênh truyền chung qua bộ ghép kênh và bộ tách kênh"),
                "Hình 87.4 · Trong đo từ xa nhiều kênh, một kênh truyền chung được dùng để "
                "truyền tín hiệu đo của nhiều kênh khác nhau bằng những sơ đồ chia sẻ khác nhau. "
                "Hai hộp điều chỉnh thứ hai và thứ ba đều in là “MẠCH ĐIỀU CHỈNH 3” — giữ nguyên "
                "như bản in, xem ghi chú của người dịch.",
                "Figure 87.4 · In multiple-channel telemetry a common transmission channel is "
                "used to transmit the measured signals from different channels using different "
                "sharing schemes. The second and third conditioning boxes are both printed as "
                "“CONDITIONING CIRCUIT 3”; this is reproduced as printed — see the translator’s "
                "note.",
                "Ba hàng cảm biến và mạch điều chỉnh cùng góp vào bộ ghép kênh, rồi qua kênh "
                "truyền tới bộ tách kênh và toả ra ba nhánh",
                "Three sensor and conditioning rows feeding a multiplexer, then a channel to a "
                "demultiplexer that fans out to three branches")


# ================================================================ 87.5
def fig_87_5():
    o = [_defs("875")]

    # ---------------- panel (a): the FDM transmitter
    o.append(_lbl(40, 30, "a)", "tb"))
    for y, n in ((78, 1), (146, 2), (214, 3)):
        o.append(_path([(x, y - v) for x, v in _hump(78, 27, 24, 40, 0.30)], 1.3))
        o.append(_lbl(52, y + 16, "Kênh %d" % n, "ts"))
        o.append(_lbl(52, y + 27, "phổ", "ts"))
        o.append(_arr(110, y, 186, y, "875"))
        o.append(_mult(200, y))
        o.append(_arr(200, y + 34, 200, y + 16, "875"))
        o.append(_r(210, y + 40, [("f", False), ("osc1", True)], "start", "ts"))
        o.append(_line(213, y, 306, 148, 1.2))

    o.append(_sum(306, 118, 56, 60))
    o.append(_arr(362, 148, 396, 148, "875"))
    o.append(_box(398, 120, 84, 56, ["BỘ ĐIỀU", "CHẾ"]))
    o.append(_mult(432, 214))
    o.append(_arr(432, 201, 432, 178, "875"))
    o.append(_r(450, 220, [("f", False), ("osc", True)], "start", "ts"))
    o.append(_lbl(450, 232, "sóng mang", "ts"))

    # the two output routes
    o.append(_line(462, 120, 462, 92, 1.2))
    o.append(_line(462, 92, 506, 92, 1.2))
    o.append(_antenna(506, 92, 20))
    o.append(_radiate(520, 82))
    o.append(_lbl(498, 40, "Đo từ xa", "ts", "middle"))
    o.append(_lbl(498, 51, "không dây", "ts", "middle"))
    o.append(_line(480, 148, 566, 148, 1.2))
    o.append(_lbl(572, 152, "Đo từ xa có dây", "ts"))

    # ---------------- panel (b): the composite base-band spectrum
    o.append(_lbl(40, 286, "b)", "tb"))
    ay = 400
    o.append(_arr(56, ay, 646, ay, "875"))
    o.append(_lbl(654, ay + 4, "f", "tf"))

    for cx, n in ((210, 1), (370, 2), (530, 3)):
        o.append(_lbl(cx, 300, "Băng thông", "ts", "middle"))
        o.append(_lbl(cx, 311, "kênh %d" % n, "ts", "middle"))
        o.append(_dimb(cx - 52, cx + 52, 326))
        o.append(_path([(x, ay - v) for x, v in _hump(cx, 52, 56, 48, 0.35)], 1.5))
        for bx in (cx - 52, cx + 52):
            o.append(_line(bx, 352, bx, ay + 8, 1.0, E, "3 3"))
        o.append(_line(cx, ay, cx, ay + 6, 1.1))
        o.append(_r(cx, ay + 18, [("f", False), ("osc%d" % n, True)], "middle", "ts"))

    o.append(_lbl(290, 362, "Dải", "txs", "middle"))
    o.append(_lbl(290, 372, "bảo vệ", "txs", "middle"))
    o.append(_dimb(266, 314, 380))
    o.append(_lbl(450, 362, "Dải", "txs", "middle"))
    o.append(_lbl(450, 372, "bảo vệ", "txs", "middle"))
    o.append(_dimb(426, 474, 380))

    o.append(_dimb(158, 582, 440, "Băng thông tín hiệu đo từ xa", 15, "txs"))

    return _fig(svg(680, 470, "".join(o),
                    "Bộ phát FDM: ba phổ kênh nhân với sóng mang phụ rồi cộng lại, và phổ "
                    "băng gốc của tín hiệu tổng hợp"),
                "Hình 87.5 · Các kênh khác nhau trong một hệ FDM (a) được cấp những tần số "
                "sóng mang phụ khác nhau, tạo ra tín hiệu tổng hợp ở (b); tín hiệu này sau đó "
                "được điều chế bởi một tần số RF tuỳ theo kênh truyền được dùng. Các dải bảo vệ "
                "giới hạn mức độ gần nhau của những kênh liền kề để tránh điều chế tương hỗ và "
                "xuyên nhiễu. Như bản in, cả ba bộ nhân đều ghi f<sub>osc1</sub> trong khi (b) "
                "lại đánh f<sub>osc1</sub>, f<sub>osc2</sub>, f<sub>osc3</sub> — xem ghi chú "
                "của người dịch.",
                "Figure 87.5 · The different channels in an FDM system (a) are allocated at "
                "different subcarrier frequencies, producing a composite signal shown in (b) "
                "that is later modulated by an RF frequency according to the transmission "
                "channel used. The guard bands limit the closeness of contiguous channels to "
                "avoid intermodulation and cross talk. As printed, all three multipliers are "
                "labelled f_osc1 while (b) marks f_osc1, f_osc2 and f_osc3 — see the "
                "translator’s note.",
                "Sơ đồ phát FDM: ba phổ kênh vào ba bộ nhân có sóng mang phụ, cộng lại trong "
                "khối Σ, qua bộ điều chế rồi toả ra ăng-ten và đường dây; phía dưới là phổ băng "
                "gốc gồm ba kênh ngăn cách bằng dải bảo vệ",
                "FDM transmitter: three channel spectra into three subcarrier multipliers, "
                "summed in a sigma block, through a modulator and out to an antenna and a wire; "
                "below, the base-band spectrum of three channels separated by guard bands")

    # the caption above uses <sub>; figures must never contain it, but the caption
    # text sits outside the <svg>, so subscripts there are safe.


# ================================================================ 87.6
def fig_87_6():
    o = [_defs("876")]

    # ---------------- panel (a): the base-band spectrum
    o.append(_lbl(40, 40, "a)", "tb"))
    ax, ay = 268, 168
    o.append(_line(ax, 62, ax, ay, 1.3))
    o.append(_arr(ax - 26, ay, 470, ay, "876"))
    o.append(_lbl(ax, 56, "|M(jω)|", "tm", "middle"))
    o.append(_lbl(478, ay + 4, "f", "tf"))

    curve = [(ax, ay - 42), (ax + 16, ay - 50), (ax + 40, ay - 57),
             (ax + 62, ay - 58), (ax + 84, ay - 50), (ax + 100, ay - 36),
             (ax + 114, ay - 16), (ax + 124, ay)]
    o.append(_path(curve, 1.6))
    o.append(_dimv(ay, ay - 42, ax - 16))
    o.append(_lbl(ax - 22, ay - 16, "M(0)", "ts", "end"))
    o.append(_lbl(ax, ay + 16, "0", "ts", "middle"))
    o.append(_line(ax + 124, ay, ax + 124, ay + 5, 1.1))
    o.append(_r(ax + 124, ay + 16, [("f", False), ("M", True)], "middle", "ts"))

    # ---------------- panel (b): the amplitude-modulated spectrum
    o.append(_lbl(40, 216, "b)", "tb"))
    by = 340
    o.append(_line(340, 240, 340, 288, 1.2))
    o.append(_lbl(348, 236, "Phổ tín hiệu", "ts"))
    o.append(_lbl(348, 247, "điều biên", "ts"))
    o.append(_arr(90, by, 630, by, "876"))
    o.append(_lbl(638, by + 4, "f", "tf"))

    for cx in (190, 470):
        o.append(_path([(x, by - v) for x, v in _hump(cx, 72, 64, 52, 0.50)], 1.5))
        o.append(_dimv(by, by - 32, cx))
        o.append(_lbl(cx + 6, by - 20, "½M(0)", "ts"))

    ticks = [(118, [("−f", False), ("c", True), (" − f", False), ("M", True)]),
             (190, [("−f", False), ("c", True)]),
             (262, [("−f", False), ("c", True), (" + f", False), ("M", True)]),
             (398, [("f", False), ("c", True), (" − f", False), ("M", True)]),
             (470, [("f", False), ("c", True)]),
             (542, [("f", False), ("c", True), (" + f", False), ("M", True)])]
    for x, parts in ticks:
        o.append(_line(x, by, x, by + 5, 1.1))
        o.append(_r(x, by + 17, parts, "middle", "ts"))

    return _fig(svg(680, 400, "".join(o),
                    "Phổ sau khi điều biên: (a) phổ băng gốc, (b) phổ điều biên với hai dải bên "
                    "đối xứng quanh sóng mang"),
                "Hình 87.6 · Phổ thu được sau khi điều biên tín hiệu ở (a). Phổ kết quả gồm hai "
                "dải bên đối xứng qua sóng mang phụ, mỗi dải cao ½M(0) tại đúng tần số sóng "
                "mang và tắt hẳn ở cách sóng mang một khoảng f<sub>M</sub>.",
                "Figure 87.6 · Resulting spectrum after amplitude modulation of a signal shown "
                "in (a). The resulting spectrum has two sidebands that are symmetrical in "
                "reference to the subcarrier, each standing ½M(0) high at the carrier itself and "
                "falling to zero f_M away from it.",
                "Hai đồ thị: phổ băng gốc một phía tắt ở fM, và phổ điều biên với hai dải bên "
                "đối xứng quanh tần số sóng mang",
                "Two plots: a one-sided base-band spectrum dying at fM, and the modulated "
                "spectrum with two sidebands symmetrical about the carrier")


# ================================================================ 87.7
def fig_87_7():
    o = [_defs("877")]

    # ---------------- panel (a): the TDM link
    o.append(_lbl(40, 28, "a)", "tb"))
    for y, n in ((48, 1), (92, 2), (136, 3)):
        o.append(_r(14, y + 4, [("x", False), ("%d" % n, True), ("(t)", False)], "start", "ts"))
        o.append(_arr(48, y, 66, y, "877"))
        o.append(_box(68, y - 17, 80, 34, ["LPF"]))
        o.append(_dot(158, y, 2.6))
        o.append(_line(160, y, 300, 92, 1.2))
        o.append(_dot(442, y, 2.6))
        o.append(_line(400, 92, 440, y, 1.2))
        o.append(_box(452, y - 17, 80, 34, ["LPF"]))
        o.append(_arr(534, y, 552, y, "877"))
        o.append(_r(558, y + 4, [("x", False), ("%d" % n, True), ("(t)", False)], "start", "ts"))

    o.append(_box(300, 74, 100, 36, ["HỆ THỐNG", "TRUYỀN"]))
    o.append(_path([(316, 112), (286, 146)], 1.0, E, "4 3"))
    o.append(_path([(384, 112), (414, 146)], 1.0, E, "4 3"))
    o.append('<text class="ts" x="350" y="158" text-anchor="middle" '
             'font-style="italic">đồng bộ</text>')

    # ---------------- panel (b): the sampled channels
    o.append(_lbl(40, 186, "b)", "tb"))
    hx = 80

    # row 1
    o.append(_line(hx, 190, hx, 240, 1.3))
    o.append(_arr(hx, 240, 626, 240, "877"))
    o.append(_lbl(636, 244, "t", "tf"))
    o.append(_r(hx + 2, 184, [("x", False), ("1", True), ("(t)", False)], "start", "ts"))
    o.append(_path([(120, 214), (150, 204), (190, 200), (230, 206), (270, 216),
                    (310, 224), (350, 220), (390, 212), (430, 206), (470, 202),
                    (510, 200), (550, 204), (590, 210)], 1.4))
    for x, hh in ((130, 40), (310, 30), (490, 34)):
        o.append(_hrect("877a%d" % x, x - 6, 240 - hh, 12, hh, 6))
    o.append(_dimb(130, 310, 256))
    o.append(_r(220, 250, [("1/f", False), ("s", True)], "middle", "ts"))

    # row 2
    o.append(_line(hx, 262, hx, 312, 1.3))
    o.append(_arr(hx, 312, 626, 312, "877"))
    o.append(_lbl(636, 316, "t", "tf"))
    o.append(_r(hx + 2, 256, [("x", False), ("2", True), ("(t)", False)], "start", "ts"))
    o.append(_path([(120, 288), (160, 280), (200, 276), (240, 278), (280, 288),
                    (320, 298), (360, 304), (400, 302), (440, 294), (480, 284),
                    (520, 276), (560, 272), (600, 274)], 1.4))
    for x, hh in ((220, 38), (400, 26)):
        o.append(_hrect("877b%d" % x, x - 6, 312 - hh, 12, hh, 6))
    o.append(_dimb(220, 400, 330))
    o.append(_r(310, 324, [("1/f", False), ("s", True)], "middle", "ts"))

    # row 3: the composite TDM signal
    o.append(_line(hx, 356, hx, 410, 1.3))
    o.append(_arr(hx, 410, 626, 410, "877"))
    o.append(_lbl(636, 414, "t", "tf"))
    o.append(_lbl(14, 364, "Tín hiệu", "ts"))
    o.append(_lbl(14, 375, "TDM", "ts"))
    for x, hh in ((130, 52), (220, 44), (310, 30), (400, 28), (490, 40)):
        o.append(_hrect("877c%d" % x, x - 6, 410 - hh, 12, hh, 6))

    o.append(_dimb(130, 220, 424))
    o.append(_r(175, 438, [("1/M·f", False), ("s", True)], "middle", "ts"))
    o.append(_dimb(130, 310, 452, "frame", 13))
    o.append(_line(310, 412, 310, 452, 1.0, E, "3 3"))

    return _fig(svg(680, 470, "".join(o),
                    "Ghép kênh theo thời gian: (a) sơ đồ khối, (b) ba kênh được lấy mẫu và "
                    "chuỗi xung TDM"),
                "Hình 87.7 · Hệ TDM (a) dựa trên việc lấy mẫu tuần tự M kênh khác nhau với một "
                "tần số lấy mẫu thoả mãn định lý Nyquist. Ở (b), mỗi kênh được lấy mẫu ở những "
                "thời điểm khác nhau trong cùng một chu kỳ T, và các mẫu được gói thành khung "
                "một cách tuần hoàn; tín hiệu tổng hợp cuối cùng chính là chuỗi xung ở hàng "
                "dưới cùng.",
                "Figure 87.7 · TDM systems (a) are based on sequentially sampling M different "
                "channels at a sampling frequency that complies with the Nyquist criteria. In "
                "(b) the samples for the channels are framed periodically, and the composite "
                "signal is the pulse train in the bottom row.",
                "Sơ đồ khối ba kênh qua bộ lọc thấp rồi vào hệ thống truyền chung, cùng ba "
                "hàng tín hiệu: hai kênh được lấy mẫu ở những thời điểm lệch nhau và chuỗi "
                "xung TDM gộp lại",
                "Block diagram of three channels through low-pass filters into a shared "
                "transmission system, plus three waveform rows: two channels sampled at "
                "different instants and the combined TDM pulse train")


# ================================================================ 87.8
def _x87(t):
    """The sample value of the illustrated signal at position t (px)."""
    return 45.0 * math.sin(math.pi * (t - 140.0) / 380.0)


def fig_87_8():
    o = [_defs("878")]
    base_x = 110
    samp = [190, 270, 350, 430, 510]

    # ---------------- the signal itself
    o.append(_lbl(52, 58, "X(t)", "tm"))
    o.append(_arr(base_x, 64, 626, 64, "878"))
    o.append(_lbl(636, 68, "t", "tf"))
    curve = [(x, 64 - _x87(x)) for x in range(140, 605, 6)]
    o.append(_path(curve, 1.6))
    for x in samp:
        o.append(_line(x, 30, x, 420, 1.0, E, "4 4"))

    o.append(_dimb(190, 270, 86))
    o.append(_r(230, 78, [("T", False), ("s", True)], "middle", "ts"))

    # ---------------- PAM
    pam_y = 186
    o.append(_lbl(52, 180, "PAM", "tm"))
    o.append(_line(base_x, 140, base_x, pam_y, 1.3))
    o.append(_arr(base_x, pam_y, 626, pam_y, "878"))
    o.append(_lbl(636, pam_y + 4, "t", "tf"))
    heights = []
    for i, x in enumerate(samp):
        hh = abs(_x87(x))
        heights.append(hh)
        o.append(_hrect("878a%d" % i, x, pam_y - hh, 16, hh, 6))
    o.append(_dimv(pam_y, pam_y - heights[0], 172))
    o.append(_r(166, pam_y - 6, [("A", False), ("0", True)], "end", "ts"))

    # ---------------- PDM
    pdm_y = 306
    o.append(_lbl(52, 300, "PDM", "tm"))
    o.append(_line(base_x, 260, base_x, pdm_y, 1.3))
    o.append(_arr(base_x, pdm_y, 626, pdm_y, "878"))
    o.append(_lbl(636, pdm_y + 4, "t", "tf"))
    widths = []
    for i, x in enumerate(samp):
        w = 6.0 + 1.15 * heights[i]
        widths.append(w)
        o.append(_hrect("878b%d" % i, x, pdm_y - 60, w, 60, 6))
    o.append(_dimb(samp[0], samp[0] + widths[0], pdm_y - 68))
    o.append(_r(samp[0] + widths[0] / 2.0, pdm_y - 74,
                [("τ", False), ("0", True)], "middle", "ts"))

    # ---------------- PPM
    ppm_y = 400
    o.append(_lbl(52, 394, "PPM", "tm"))
    o.append(_line(base_x, 354, base_x, ppm_y, 1.3))
    o.append(_arr(base_x, ppm_y, 626, ppm_y, "878"))
    o.append(_lbl(636, ppm_y + 4, "t", "tf"))
    offs = []
    for i, x in enumerate(samp):
        d = 0.55 * heights[i]
        offs.append(d)
        o.append(_hrect("878c%d" % i, x + d, ppm_y - 60, 16, 60, 6))
    o.append(_dimb(samp[0], samp[0] + offs[0], ppm_y + 12))
    o.append(_r(samp[0] + offs[0] / 2.0, ppm_y + 26,
                [("τ", False), ("0", True)], "middle", "ts"))

    return _fig(svg(680, 440, "".join(o),
                    "Ba cách điều chế tương tự dùng trong TDM: PAM, PDM và PPM trên cùng một "
                    "tín hiệu lấy mẫu"),
                "Hình 87.8 · Các sơ đồ điều chế tương tự khác nhau dùng trong TDM. Sự biến "
                "thiên biên độ của tín hiệu x(t) được phản ánh vào biên độ xung ở PAM, vào độ "
                "rộng xung ở PDM và vào vị trí xung ở PPM; τ<sub>0</sub> là độ rộng và độ lệch "
                "nhỏ nhất. Như bản in, các xung được vẽ vuông cho dễ nhìn.",
                "Figure 87.8 · Different analog modulation schemes used in TDM. The variations "
                "in amplitude of the signal x(t) are carried by the pulse amplitude in PAM, by "
                "the pulse width in PDM and by the pulse position in PPM; τ_0 is the minimum "
                "width and the minimum displacement. The pulses are shown square for clarity, "
                "as printed.",
                "Bốn hàng: tín hiệu gốc có năm vạch lấy mẫu đứt nét, rồi PAM với các xung cao "
                "thấp khác nhau, PDM với các xung rộng hẹp khác nhau, và PPM với các xung dịch "
                "vị trí",
                "Four rows: the original signal with five dotted sampling lines, then PAM with "
                "pulses of varying height, PDM with pulses of varying width and PPM with pulses "
                "displaced from the sampling instants")


# ================================================================ 87.9
def fig_87_9():
    o = [_defs("879")]

    o.append(_lbl(48, 76, "Dữ liệu", "tm"))
    o.append(_lbl(48, 88, "vào", "tm"))
    for y in (58, 80, 102):
        o.append(_arr(96, y, 128, y, "879"))

    o.append(_box(130, 46, 118, 68, ["BỘ MÃ HOÁ", "PCM"]))
    o.append(_box(452, 46, 118, 68, ["BỘ GIẢI MÃ", "PCM"]))

    o.append(_line(248, 80, 300, 80, 1.2))
    o.append(_line(300, 80, 300, 58, 1.2))
    o.append(_antenna(300, 58, 18))
    o.append(_line(380, 80, 452, 80, 1.2))
    o.append(_line(380, 80, 380, 58, 1.2))
    o.append(_antenna(380, 58, 18))
    o.append(_path([(312, 34), (322, 40), (332, 30), (342, 38)], 1.1))

    o.append(_lbl(340, 108, "Đường truyền", "tb", "middle"))
    o.append(_lbl(340, 120, "đo từ xa", "tb", "middle"))

    for y in (58, 80, 102):
        o.append(_arr(570, y, 602, y, "879"))
    o.append(_lbl(608, 76, "Dữ liệu", "tm"))
    o.append(_lbl(608, 88, "ra", "tm"))

    return _fig(svg(680, 150, "".join(o),
                    "Sơ đồ khối một tuyến PCM: dữ liệu vào, bộ mã hoá, đường truyền đo từ xa, "
                    "bộ giải mã, dữ liệu ra"),
                "Hình 87.9 · Sơ đồ khối của một tuyến PCM cơ bản dùng cho đo từ xa. Dữ liệu vào "
                "được bộ mã hoá PCM chuyển thành chuỗi bit, phát qua đường truyền đo từ xa rồi "
                "được bộ giải mã dựng lại thành dữ liệu ra.",
                "Figure 87.9 · Block diagram showing a basic PCM link for telemetry. The input "
                "data is turned into a bit stream by the PCM encoder, sent over the telemetry "
                "link and rebuilt as output data by the decoder.",
                "Sơ đồ khối nằm ngang: dữ liệu vào, bộ mã hoá PCM, hai ăng-ten nối bằng đường "
                "truyền đo từ xa, bộ giải mã PCM và dữ liệu ra",
                "A horizontal block diagram: input data, PCM encoder, two antennas joined by a "
                "telemetry link, PCM decoder and output data")


# ================================================================ 87.10
_BITS10 = [1, 0, 1, 1, 0]

_CODES = [
    ("NRZ-L", [1, 1, 0, 0, 1, 1, 1, 1, 0, 0]),
    ("NRZ-M", [1, 1, 1, 1, 0, 0, 1, 1, 1, 1]),
    ("NRZ-S", [0, 0, 1, 1, 1, 1, 1, 1, 0, 0]),
    ("Biø-L", [0, 1, 1, 0, 0, 1, 0, 1, 1, 0]),
    ("Biø-M", [0, 1, 0, 1, 1, 0, 0, 1, 0, 1]),
    ("Biø-S", [1, 0, 0, 1, 0, 1, 0, 1, 1, 0]),
]


def _wave(x0, cw, yhi, ylo, levels):
    """Step a two-level waveform across `levels`, one level per half cell."""
    n = len(levels)
    hw = cw / 2.0

    def Y(v):
        return yhi if v else ylo

    pts = [(x0, Y(levels[0]))]
    for i in range(1, n):
        xb = x0 + i * hw
        pts.append((xb, Y(levels[i - 1])))
        pts.append((xb, Y(levels[i])))
    pts.append((x0 + n * hw, Y(levels[-1])))
    return _path(pts, 1.8)


def fig_87_10():
    o = [_defs("8710")]
    x0, cw = 128, 96
    top = 56
    rh = 50

    for i, b in enumerate(_BITS10):
        o.append(_lbl(x0 + i * cw + cw / 2.0, 40, "%d" % b, "tb", "middle"))
        if i:
            o.append(_line(x0 + i * cw, 26, x0 + i * cw, top + 6 * rh, 0.8, PALE, "3 4"))

    for r, (name, levels) in enumerate(_CODES):
        ylo = top + r * rh + 34
        yhi = ylo - 26
        o.append(_lbl(14, ylo - 8, name, "tm"))
        o.append(_wave(x0, cw, yhi, ylo, levels))

    return _fig(svg(680, 372, "".join(o),
                    "Sáu mã PCM theo chuẩn IRIG cho chuỗi bit 1 0 1 1 0"),
                "Hình 87.10 · Các mã PCM khác nhau. Trong mọi mã NRZ, mức thấp vẫn khác không. "
                "Với mã hai pha, thông tin nằm ở các chuyển mức chứ không nằm ở mức. NRZ-L: 1 "
                "là mức cao nhất, 0 là mức thấp hơn. NRZ-M: 1 là có chuyển mức, 0 là không "
                "chuyển mức. NRZ-S: 1 là không chuyển mức, 0 là có chuyển mức. Biø-L: 1 là "
                "chuyển xuống mức thấp, 0 là chuyển lên mức cao. Biø-M: 1 là không đổi mức ở "
                "đầu chu kỳ bit, 0 là đổi mức ở đầu chu kỳ bit. Biø-S: 1 là đổi mức ở đầu chu "
                "kỳ bit, 0 là không đổi mức ở đầu chu kỳ bit.",
                "Figure 87.10 · Different PCM codes. All lower levels in NRZ use a value "
                "different from zero. In biphase codes the information resides in the "
                "transitions rather than in the levels. In NRZ-L a 1 is the highest level and a "
                "0 a lower level; in NRZ-M a 1 is a change in level and a 0 no change; in NRZ-S "
                "a 1 is no change and a 0 a change. In Biø-L a 1 is a transition to the lower "
                "level and a 0 a transition to the higher level; in Biø-M a 1 is no change at "
                "the beginning of the bit period and a 0 a change; in Biø-S a 1 is a change at "
                "the beginning of the bit period and a 0 no change.",
                "Sáu hàng xung vuông trên cùng năm ô bit 1 0 1 1 0: NRZ-L, NRZ-M, NRZ-S, và ba "
                "mã hai pha Biø-L, Biø-M, Biø-S",
                "Six square-wave rows over the same five bit cells 1 0 1 1 0: NRZ-L, NRZ-M, "
                "NRZ-S and the three biphase codes Biø-L, Biø-M and Biø-S")


# ================================================================ 87.11
def fig_87_11():
    o = [_defs("8711")]
    cells = [(156, 120, "Đồng bộ khung nhỏ"), (276, 40, "1"), (316, 40, "2"),
             (356, 22, "…"), (378, 62, "(W,1)"), (440, 22, "…"), (462, 60, "N-1")]
    ty = 84                    # top row
    by = 264                   # bottom row

    o.append(_rect(146, 44, 388, 268, 1.1, "none", "6 5"))

    for x, w, t in cells:
        o.append(_box(x, ty, w, 28, [t], 1.2, 9))
        bt = t if t != "(W,1)" else "(W,Z)"
        o.append(_box(x, by, w, 28, [bt], 1.2, 9))

    # the subframe column
    o.append(_rect(378, ty + 28, 62, 108, 1.2))
    o.append('<text class="ts" x="409" y="166" text-anchor="middle" '
             'transform="rotate(-90 409 166)">Khung con Z từ</text>')
    o.append(_lbl(409, 214, "…", "tb", "middle"))
    o.append(_box(378, 226, 62, 26, ["(W,S)"], 1.2, 9))
    o.append(_line(409, 252, 409, by, 1.0, E, "3 3"))

    # annotations
    o.append(_dimb(156, 522, 34, "Độ dài cực đại của khung nhỏ", -7))
    o.append(_lbl(156, 140, "Khung nhỏ", "ts"))
    o.append(_path([(238, 136), (330, 114)], 1.0))
    o.append(_poly([(330, 114), (321, 112), (324, 120)], 1.0, E, E))
    o.append(_lbl(330, 324, "Khung lớn", "ts", "middle"))
    o.append(_path([(374, 322), (398, 314)], 1.0))
    o.append(_poly([(398, 314), (389, 313), (393, 321)], 1.0, E, E))

    return _fig(svg(680, 336, "".join(o),
                    "Cấu trúc khung của PCM: khung nhỏ, khung lớn và cột khung con Z từ"),
                "Hình 87.11 · Cấu trúc khung của một khung PCM. Độ dài cực đại của khung nhỏ là "
                "8192 bit, hoặc 512 với thiết bị cấp I. Khung lớn gồm nhiều khung nhỏ xếp liên "
                "tiếp, và mỗi từ trong một khung nhỏ lại mở ra một khung con Z từ ở "
                "cột dọc bên phải.",
                "Figure 87.11 · Structure of a PCM frame. The maximum length of a minor frame is "
                "8192 bits, or 512 for class I equipment. A major frame stacks consecutive minor "
                "frames, and each word of a minor frame opens a subframe of Z words in the "
                "vertical column on the right.",
                "Hai hàng ô giống nhau đánh dấu khung nhỏ, nối với nhau bằng một cột dọc ghi "
                "Khung con Z từ, có các ô (W,1), (W,S) và (W,Z)",
                "Two identical cell rows marking minor frames, joined by a vertical column "
                "labelled a subframe of Z words with cells (W,1), (W,S) and (W,Z)")
