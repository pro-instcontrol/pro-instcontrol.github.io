# -*- coding: utf-8 -*-
"""Vector figures for Handbook Chapter 9 — Distance (W. John Ballantyne).

Nine figures, one table.  The response curves are computed from the relation
named in the caption, never sketched.

Every function returns (svg, caption_vi, caption_en, aria_vi, aria_en).
"""
import math

from hbfig import GOLD, INK, MUTED, TXT, _f, svg, _fig

BLUE = "#2f5d8a"
RED = "#a8322d"
GREEN = "#3f6b47"
SAND = "#f7f4ed"
BAND = "#eef2f6"

STY = ('<style>'
       '.b9{font:9.2px Inter,Helvetica,sans-serif;fill:#111;font-weight:600}'
       '.t9{font:8.8px Inter,Helvetica,sans-serif;fill:#111}'
       '.s9{font:8.0px Inter,Helvetica,sans-serif;fill:#555}'
       '.k9{font:7.4px Inter,Helvetica,sans-serif;fill:#666}'
       '</style>')


# ---------------------------------------------------------------- primitives
def _t(x, y, s, fs=8.8, anchor="middle", fill=TXT, bold=False, rot=None):
    w = ' font-weight="600"' if bold else ""
    r = ' transform="rotate(%s %s %s)"' % (rot, _f(x), _f(y)) if rot else ""
    return ('<text x="%s" y="%s" font-size="%s" fill="%s" text-anchor="%s"%s%s>%s</text>'
            % (_f(x), _f(y), fs, fill, anchor, w, r, s))


def _l(x1, y1, x2, y2, sw=1.0, color=INK, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), color, sw, d))


def _r(x, y, w, h, fill="none", sw=1.0, stroke=INK, rx=0):
    return ('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"/>' % (_f(x), _f(y), _f(w), _f(h), _f(rx), fill, stroke, sw))


def _c(cx, cy, r, fill="none", sw=1.0, stroke=INK):
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s"/>'
            % (_f(cx), _f(cy), _f(r), fill, stroke, sw))


def _poly(pts, fill="none", sw=1.0, stroke=INK, close=False):
    tag = "polygon" if close else "polyline"
    return '<%s points="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>' % (
        tag, " ".join("%s,%s" % (_f(x), _f(y)) for x, y in pts), fill, stroke, sw)


def _arrow(x1, y1, x2, y2, sw=1.0, color=INK, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    ang = math.atan2(y2 - y1, x2 - x1)
    L, W = 7.0, 2.6
    ax, ay = x2 - L * math.cos(ang), y2 - L * math.sin(ang)
    head = ('<polygon points="%s,%s %s,%s %s,%s" fill="%s"/>'
            % (_f(x2), _f(y2),
               _f(ax + W * math.sin(ang)), _f(ay - W * math.cos(ang)),
               _f(ax - W * math.sin(ang)), _f(ay + W * math.cos(ang)), color))
    return (_l(x1, y1, ax, ay, sw, color, dash) + head)


def _p(d, fill="none", sw=1.0, color=INK, dash=""):
    dd = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<path d="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (d, fill, color, sw, dd))


def _plot(x0, y0, w, h, xlab, ylab, xt, yt, fn, n=90, color=INK, sw=1.7, xr=(0, 1), yr=(0, 1)):
    """A framed plot with ticks; fn(u) -> v with u in xr, v in yr."""
    out = [_l(x0, y0, x0 + w, y0, 1.1) + _l(x0, y0, x0, y0 - h, 1.1)]
    for u, lab in xt:
        px = x0 + (u - xr[0]) / (xr[1] - xr[0]) * w
        out.append(_l(px, y0, px, y0 + 3.5, 0.9))
        if lab:
            out.append(_t(px, y0 + 13, lab, 7.6, "middle", "#555"))
    for v, lab in yt:
        py = y0 - (v - yr[0]) / (yr[1] - yr[0]) * h
        out.append(_l(x0, py, x0 - 3.5, py, 0.9))
        if lab:
            out.append(_t(x0 - 6, py + 2.6, lab, 7.6, "end", "#555"))
    pts = []
    for i in range(n + 1):
        u = xr[0] + (xr[1] - xr[0]) * i / float(n)
        v = max(yr[0], min(yr[1], fn(u)))
        pts.append((x0 + (u - xr[0]) / (xr[1] - xr[0]) * w,
                    y0 - (v - yr[0]) / (yr[1] - yr[0]) * h))
    out.append(_poly(pts, "none", sw, color))
    out.append(_t(x0 + w / 2.0, y0 + 27, xlab, 8.0, "middle", "#555"))
    out.append('<text x="%s" y="%s" font-size="8" fill="#555" text-anchor="middle" '
               'transform="rotate(-90 %s %s)">%s</text>'
               % (_f(x0 - 26), _f(y0 - h / 2.0), _f(x0 - 26), _f(y0 - h / 2.0), ylab))
    return "".join(out)


def _blk(x, y, w, h, lines, fs=7.8, fill="#fff", stroke=INK, sw=1.0):
    o = [_r(x, y, w, h, fill, sw, stroke)]
    n = len(lines)
    for i, s in enumerate(lines):
        o.append(_t(x + w / 2.0, y + h / 2.0 + (i - (n - 1) / 2.0) * 10 + 3, s, fs, "middle", "#222"))
    return "".join(o)


# ---------------------------------------------------------------- 9.1
def fig_9_1():
    b = []
    x0, x1, y = 46, 520, 120
    b.append(_t(283, 26, "thang khoảng cách (m)", 9.6, "middle", INK, True))
    b.append(_arrow(x0 - 8, y, x1 + 6, y, 1.2))

    ticks = [(-12, "10⁻¹²"), (-9, "10⁻⁹"), (-6, "10⁻⁶"), (-3, "10⁻³"), (0, "10⁰"),
             (3, "10³"), (6, "10⁶"), (9, "10⁹"), (12, "10¹²"), (15, "10¹⁵"), (18, "10¹⁸")]
    for e, lab in ticks:
        px = x0 + (e + 12) / 30.0 * (x1 - x0)
        b.append(_l(px, y - 6, px, y + 6, 1.0))
        b.append(_t(px, y + 20, lab, 7.4, "middle", "#444"))

    cats = [(-10.0, "liên nguyên tử"), (-6.4, "liên tế bào"), (-1.0, "liên thành phố"),
            (4.4, "liên lục địa"), (9.2, "liên hành tinh"), (13.2, "liên sao"),
            (16.8, "liên thiên hà")]
    for e, lab in cats:
        px = x0 + (e + 12) / 30.0 * (x1 - x0)
        b.append(_l(px, y + 24, px, y + 32, 0.8, MUTED, "3 3"))
        b.append(_t(px, y + 36, lab, 7.6, "end", "#555", rot=-40))

    xa = x0 + 9 / 30.0 * (x1 - x0)
    xb = x0 + 15 / 30.0 * (x1 - x0)
    b.append(_r(xa, y - 18, xb - xa, 12, "none", 1.4, RED, rx=2))
    b.append(_l((xa + xb) / 2.0, y - 18, (xa + xb) / 2.0 - 20, y - 48, 0.9, RED))
    b.append(_t((xa + xb) / 2.0 - 24, y - 52, "phạm vi chương này: cm → km", 8.0, "middle",
                RED, True))
    b.append(_t(283, 200, "ba mươi bậc độ lớn, từ hạt nhân tới thiên hà — chương này chỉ "
                          "chiếm sáu bậc", 8.0, "middle", "#555"))
    return _fig(svg(560, 212, STY + "".join(b), "Thang khoảng cách đo được và phạm vi của chương"),
                "Hình 9-1. Từ liên nguyên tử tới liên thiên hà, thang khoảng cách đo được trải ít "
                "nhất ba mươi bậc độ lớn. Khung chữ nhật đánh dấu đoạn tương đối nhỏ mà chương này "
                "quan tâm — từ xentimét tới kilômét.",
                "Figure 9-1. From the interatomic to the intergalactic, the range of measurable "
                "distances spans at least thirty orders of magnitude. The box marks the relatively "
                "small segment that concerns this chapter, from centimetres to kilometres.",
                "Trục ngang biểu diễn thang khoảng cách từ 10 mũ trừ 12 tới 10 mũ 18 mét, với khung đánh dấu phạm vi chương.",
                "A horizontal distance scale from 10^-12 to 10^18 metres, with a box marking the chapter's range.")


# ---------------------------------------------------------------- 9.2
def fig_9_2():
    b = []
    L = (110, 208)
    Rr = (330, 208)
    T = (452, 58)

    b.append(_l(56, 236, 508, 236, 1.0, "#999"))
    b.append(_c(L[0], L[1], 4.0, "#fff", 1.2))
    b.append(_c(Rr[0], Rr[1], 4.0, "#fff", 1.2))
    b.append(_t(L[0], 252, "trạm trái", 7.8, "middle", "#555"))
    b.append(_t(Rr[0], 252, "trạm phải", 7.8, "middle", "#555"))

    b.append(_l(L[0], L[1], Rr[0], Rr[1], 1.8, GREEN))
    b.append(_t((L[0] + Rr[0]) / 2.0, L[1] - 9, "b", 9.4, "middle", GREEN, True))

    b.append(_l(L[0], L[1], T[0], T[1], 1.1))
    b.append(_l(Rr[0], Rr[1], T[0], T[1], 1.1))
    b.append(_c(T[0], T[1], 3.2, INK))
    b.append(_t(T[0] + 8, T[1] - 4, "đích", 8.2, "start", INK, True))

    # the angle at the left station, measured from the baseline
    b.append(_p("M 144 208 A 34 34 0 0 0 141.1 194.4", "none", 1.2, RED))
    b.append(_t(151, 203, "α₁", 9.0, "middle", RED, True))

    # the angle at the right station, measured from the baseline
    b.append(_p("M 300 208 A 30 30 0 0 1 348.9 184.7", "none", 1.2, RED))
    b.append(_t(311, 197, "α₂", 9.0, "middle", RED, True))

    # the range is the side from the left station to the target
    b.append(_t(270, 126, "R", 9.6, "middle", BLUE, True))

    b.append(_t(300, 288, "định lý sin: R = b · sin α₂ / sin(α₁ + α₂)", 8.8, "middle", "#333"))
    b.append(_t(300, 304, "đo hai góc tại hai đầu đường đáy đã biết, suy ra khoảng cách", 7.8,
                "middle", "#555"))
    return _fig(svg(560, 316, STY + "".join(b), "Hình học tam giác đạc cổ điển"),
                "Hình 9-2. Hình học tam giác đạc cơ bản dùng trong trắc địa cổ điển: khoảng cách tới "
                "một điểm xa được xác định bằng cách ngắm nó từ hai vị trí cách nhau một đường đáy đã "
                "biết. Các góc ngắm α₁ và α₂ được đo tại chỗ.",
                "Figure 9-2. The basic triangulation geometry as used in classical surveying: the "
                "distance to a remote point is found by sighting it from two locations separated by a "
                "known baseline. The pointing angles α₁ and α₂ are measured locally.",
                "Hai trạm quan trắc cách nhau một đường đáy b, cùng ngắm tới đích; hai góc alpha đo tại chỗ và khoảng cách R.",
                "Two survey stations separated by a baseline b sighting a target, with the two local angles and the range R.")


# ---------------------------------------------------------------- 9.3
def fig_9_3():
    def tri(u):
        return 0.05 + 0.95 * u * u

    def tof(u):
        return 0.42

    b = [_plot(90, 194, 336, 126, "khoảng cách từ cảm biến tới đích", "độ bất định khoảng cách",
               [(0, "0"), (1, "")], [(0, "0"), (1, "")], tri, color=BLUE)]
    pts = []
    for i in range(61):
        u = i / 60.0
        pts.append((90 + u * 336, 194 - tof(u) * 126))
    b.append(_poly(pts, "none", 1.7, RED))

    ux = math.sqrt((0.42 - 0.05) / 0.95)
    px = 90 + ux * 336
    py = 194 - 0.42 * 126
    b.append(_l(px, 194, px, py, 0.9, MUTED, "4 3"))
    b.append(_c(px, py, 3.0, INK))
    b.append(_t(px + 8, py + 16, "điểm cắt", 7.8, "start", "#444"))

    b.append(_t(300, 74, "tam giác đạc: sai số ∝ R²", 8.2, "middle", BLUE, True))
    b.append(_t(404, 122, "thời gian bay: sai số không đổi", 8.2, "end", RED, True))
    b.append(_t(96, 108, "trước điểm cắt: tam giác đạc tốt hơn", 7.6, "start", "#555"))
    b.append(_t(332, 174, "sau điểm cắt: thời gian bay tốt hơn", 7.6, "start", "#555"))
    return _fig(svg(560, 230, STY + "".join(b), "Sai số của tam giác đạc và thời gian bay theo khoảng cách"),
                "Hình 9-3. Kỹ thuật thời gian bay (TOF) và tam giác đạc chủ động có đặc trưng sai số "
                "gắn với nguyên lý hoạt động của chúng. Nguồn sai số chủ yếu của hệ TOF thường là "
                "khoảng thời gian ngắn nhất đo được — một vấn đề phát hiện, hầu như độc lập với "
                "khoảng cách. Hệ tam giác đạc chủ động thường chính xác hơn ở cự ly gần, nhưng hình "
                "học buộc ảnh hưởng của các nguồn sai số tăng theo bình phương khoảng cách.",
                "Figure 9-3. Time-of-flight (TOF) and active triangulation techniques show error "
                "characteristics tied to their principles of operation. The dominant error source in "
                "TOF systems is usually the shortest measurable time interval — a detection issue, "
                "essentially independent of distance. Active triangulation is typically more accurate "
                "at close range, but geometry dictates that its error sources grow with the square of "
                "distance.",
                "Đồ thị so sánh: đường sai số tam giác đạc tăng theo bình phương khoảng cách, đường thời gian bay nằm ngang.",
                "A comparison plot: triangulation error rising with the square of range, TOF error flat.")


# ---------------------------------------------------------------- 9.4
def fig_9_4():
    b = []
    cx, top, bot = 280, 48, 196

    def half(v):
        return 22 + 22 * math.sin(math.pi * v) + 10 * (1 - v)

    # the scanner on its tripod
    b.append(_r(48, 168, 58, 26, BAND, 1.1))
    b.append(_t(77, 185, "đầu quét", 7.6, "middle", "#333"))
    for dx in (-16, 0, 16):
        b.append(_l(77 + dx * 0.45, 194, 77 + dx, 240, 1.0, "#777"))
    b.append(_l(50, 206, 106, 218, 1.0, "#777"))

    # the beam and the two scan angles
    b.append(_arrow(106, 178, cx - 18, 116, 1.1, BLUE))
    b.append(_p("M 128 160 A 46 46 0 0 0 116 190", "none", 1.1, RED))
    b.append(_t(134, 158, "φ", 9.2, "start", RED, True))
    b.append(_p("M 122 200 A 32 32 0 0 0 138 210", "none", 1.1, GREEN))
    b.append(_t(140, 220, "θ", 9.2, "start", GREEN, True))

    # the scanned surface
    left, right = [], []
    for i in range(31):
        v = i / 30.0
        y = top + v * (bot - top)
        w = half(v)
        left.append((cx - w, y))
        right.append((cx + w, y))
    b.append(_poly(left + right[::-1], SAND, 1.2, INK, close=True))

    for i in range(9):
        for j in range(7):
            v = 0.06 + i * 0.105
            w = half(v)
            x = cx + (-1 + j / 3.0) * w * 0.94
            y = top + v * (bot - top)
            b.append(_c(x, y, 1.6, INK))

    b.append(_c(cx - 6, 122, 3.0, RED))
    b.append(_t(cx + 46, 132, "Pₙ = (rₙ, θₙ, φₙ)", 8.4, "start", RED, True))
    b.append(_l(cx - 6, 122, cx + 42, 128, 0.8, RED))

    b.append(_t(cx, 218, "mỗi mẫu là một bộ ba cực (khoảng cách, phương vị, góc tà)", 8.0,
                "middle", "#555"))
    b.append(_t(cx, 234, "lưới cực đổi sang toạ độ vuông góc khi cần", 8.0, "middle", "#555"))
    return _fig(svg(560, 246, STY + "".join(b), "Ảnh khoảng cách dạng cực"),
                "Hình 9-4. Ảnh khoảng cách thường là một dãy các giá trị khoảng cách riêng lẻ, lấy mẫu "
                "trong khi hướng ngắm của đầu đo thay đổi (theo phương vị và góc tà). Ảnh khoảng cách "
                "số ở dạng cực như hình vẽ có thể chuyển thẳng sang toạ độ vuông góc nếu cần.",
                "Figure 9-4. Range images are typically an array of individual range values sampled "
                "while the pointing direction of the ranging device changes (azimuth and elevation). A "
                "digital range image in the polar form shown can be transformed into rectangular "
                "coordinates if required.",
                "Đầu quét trên giá ba chân quét một vật, mỗi điểm cho một bộ ba khoảng cách, phương vị và góc tà.",
                "A tripod-mounted scanner sweeping an object, each point giving a range, azimuth and elevation triple.")


# ---------------------------------------------------------------- 9.5
def fig_9_5():
    b = []

    def panel(ox, u_at, caption):
        o = []
        o.append(_r(ox, 26, 220, 80, "#fff", 1.2))
        o.append(_r(ox + 16, 40, 30, 44, SAND, 1.0))
        # the receiving lens and the detector behind it
        o.append(_l(ox + 120, 32, ox + 120, 100, 2.2, GREEN))
        o.append(_l(ox + 150, 46, ox + 192, 58, 2.8, BLUE))
        o.append(_c(ox + u_at, 46 + (u_at - 150) * 0.286, 2.8, RED))
        # the two dimensions inside the head
        o.append(_l(ox + 46, 88, ox + 120, 88, 0.9))
        o.append(_t(ox + 83, 84, "b", 8.6, "middle", INK, True))
        o.append(_l(ox + 120, 88, ox + 150, 88, 0.9))
        o.append(_t(ox + 135, 84, "f", 8.2, "middle", RED, True))
        o.append(_l(ox + 46, 84, ox + 46, 92, 0.8))
        o.append(_l(ox + 120, 84, ox + 120, 92, 0.8))
        o.append(_l(ox + 150, 84, ox + 150, 92, 0.8))
        # the target surface and the spot
        o.append(_p("M %d 176 q 26 -10 52 0 q 26 10 52 0 q 26 -10 52 0" % (ox + 6),
                    "none", 1.4, "#666"))
        sx = ox + 96
        o.append(_c(sx, 173, 2.8, INK))
        # the outgoing and returning rays
        o.append(_arrow(ox + 31, 84, sx - 2, 171, 1.0, BLUE))
        o.append(_arrow(sx + 2, 171, ox + 120, 84, 1.0, RED))
        # the range
        o.append(_arrow(ox + 8, 172, ox + 8, 108, 1.0, INK))
        o.append(_t(ox + 2, 140, "R", 9.2, "middle", INK, True, rot=-90))
        # labels under the head
        o.append(_t(ox + 31, 118, "phát", 7.6, "middle", "#444"))
        o.append(_t(ox + 120, 118, "thấu kính thu", 7.6, "middle", GREEN))
        o.append(_t(ox + 171, 40, "dãy thu", 7.4, "middle", BLUE))
        o.append(_t(sx + 8, 168, "vệt sáng", 7.4, "start", "#444"))
        o.append(_t(ox + 110, 200, caption, 8.0, "middle", "#555"))
        return o

    b.extend(panel(14, 186, "(a) đích ở gần: vệt lệch nhiều"))
    b.extend(panel(296, 158, "(b) đích ở xa: vệt lệch ít"))
    b.append(_t(280, 224, "R = b·f / u", 9.0, "middle", "#333"))
    return _fig(svg(560, 238, STY + "".join(b), "Mô hình camera lỗ kim của tam giác đạc chủ động"),
                "Hình 9-5. Mô hình camera lỗ kim đơn giản minh hoạ nguyên lý tam giác đạc chủ động. Khi "
                "khoảng cách R tới bề mặt đích thay đổi, vị trí vệt sáng u trên bộ thu thay đổi theo, "
                "giữ nguyên sự đồng dạng giữa tam giác lớn ngoài camera và tam giác nhỏ bên trong. Giữa "
                "R và u có quan hệ nghịch đảo.",
                "Figure 9-5. A simple pinhole camera model illustrates the basic active triangulation "
                "principle. As the distance R to the target surface changes, the spot position u on the "
                "detector changes, maintaining similarity between the large triangle outside the camera "
                "and the small triangle inside. R and u are inversely related.",
                "Hai sơ đồ camera lỗ kim: đích gần cho vệt lệch lớn, đích xa cho vệt lệch nhỏ.",
                "Two pinhole-camera diagrams: a near target displaces the spot more than a far one.")


# ---------------------------------------------------------------- 9.6
def fig_9_6():
    b = []
    # target
    b.append(_p("M 236 26 q 22 -10 44 0 q 18 8 40 -2", "none", 1.4, "#666"))
    b.append(_t(262, 16, "vật đích", 8.2, "middle", INK, True))
    b.append(_c(262, 30, 2.4, INK))

    # outbound and return paths
    b.append(_arrow(250, 196, 258, 36, 1.1, BLUE))
    b.append(_arrow(266, 36, 290, 194, 1.1, RED))
    b.append(_t(224, 104, "chùm laser tới", 7.4, "middle", BLUE, rot=-84))
    b.append(_t(300, 108, "tán xạ ngược", 7.4, "middle", RED, rot=84))

    # laser head
    b.append(_blk(220, 120, 84, 24, ["laser"], 8.0))
    b.append(_c(262, 152, 4.2, "#fff", 1.0))
    b.append(_c(262, 162, 2.8, "#fff", 1.0))

    # mirrors: fixed, oscillating, fixed
    for x in (140, 384):
        b.append(_p("M %d 186 L %d 218 L %d 196 L %d 164 Z" % (x, x + 20, x + 20, x), SAND, 1.1))
        b.append(_t(x + 10, 234, "gương cố định", 7.2, "middle", "#555"))
    b.append(_p("M 236 208 L 262 240 L 288 208 L 262 176 Z", SAND, 1.2))
    b.append(_t(262, 204, "gương", 7.0, "middle", "#333"))
    b.append(_t(262, 213, "dao động", 7.0, "middle", "#333"))
    b.append(_l(160, 196, 236, 208, 1.0))
    b.append(_l(288, 208, 384, 196, 1.0))
    b.append(_c(262, 168, 3.0, "#fff", 1.0))

    # control box, taken out to the right below the mirror row
    b.append(_blk(292, 252, 100, 24, ["điều khiển gương"], 7.2))
    b.append(_arrow(280, 238, 292, 258, 0.9))
    b.append(_arrow(392, 264, 462, 264, 0.9))
    b.append(_t(468, 267, "phương vị", 7.8, "start", "#444"))

    # detection lens and array
    b.append(_c(262, 272, 4.0, "#fff", 1.0))
    b.append(_c(262, 282, 2.6, "#fff", 1.0))
    b.append(_p("M 172 328 L 250 300 L 256 312 L 178 340 Z", BAND, 1.0))
    b.append(_t(168, 296, "dãy thu tuyến tính", 7.4, "end", "#333"))
    b.append(_arrow(256, 308, 296, 308, 1.0))
    b.append(_blk(296, 296, 76, 24, ["bộ lấy mẫu"], 7.4))

    b.append(_arrow(372, 302, 396, 286, 1.0))
    b.append(_blk(396, 272, 88, 24, ["tách đỉnh"], 7.4))
    b.append(_arrow(440, 296, 440, 312, 1.0))
    b.append(_blk(396, 312, 88, 24, ["tách vị trí"], 7.4))
    b.append(_arrow(484, 284, 512, 284, 1.0))
    b.append(_t(516, 287, "cường độ", 7.6, "start", "#444"))
    b.append(_arrow(440, 336, 440, 352, 1.0))
    b.append(_blk(396, 352, 88, 24, ["tính khoảng cách"], 7.2))
    b.append(_arrow(484, 364, 512, 364, 1.0))
    b.append(_t(516, 367, "khoảng cách", 7.6, "start", "#444"))
    return _fig(svg(560, 386, STY + "".join(b), "Sơ đồ nguyên lý quét đồng bộ của Hymarc"),
                "Hình 9-6. Máy quét tuyến tam giác đạc laser của Hymarc dùng nguyên lý quét đồng bộ. "
                "Hai mặt của một gương dao động được dùng để quét đồng thời chùm sáng phát ra và trục "
                "thu trên vật. Dãy thu được nghiêng so với mặt phẳng thấu kính để tối đa hoá độ sâu "
                "trường ảnh.",
                "Figure 9-6. The Hymarc laser triangulation line scanner uses the synchronized scanning "
                "principle. Both faces of an oscillating mirror sweep the projected beam and the axis of "
                "detection across the target at the same time. The detector array is tilted with respect "
                "to the lens plane to maximise the depth of focus.",
                "Sơ đồ quét đồng bộ: laser, gương dao động hai mặt, hai gương cố định, dãy thu nghiêng và chuỗi xử lý tín hiệu.",
                "The synchronized scanning layout: laser, two-sided oscillating mirror, two fixed mirrors, a tilted detector array and the processing chain.")


# ---------------------------------------------------------------- 9.7
def fig_9_7():
    b = []
    b.append(_p("M 200 22 q 22 -9 44 0 q 18 8 40 -2", "none", 1.4, "#666"))
    b.append(_t(226, 12, "vật đích", 8.0, "middle", INK, True))
    b.append(_c(226, 26, 2.2, INK))

    b.append(_arrow(218, 108, 222, 32, 1.1, BLUE))
    b.append(_arrow(232, 32, 254, 106, 1.1, RED))
    b.append(_t(186, 74, "chùm phát", 7.2, "middle", BLUE, rot=-86))
    b.append(_t(272, 74, "tán xạ ngược", 7.2, "middle", RED, rot=86))

    # nodding mirror with its galvo, at the top of the optical bench
    b.append(_r(176, 118, 84, 22, SAND, 1.1))
    b.append(_t(218, 132, "gương gật", 7.2, "middle", "#333"))
    b.append(_r(268, 120, 24, 16, BAND, 1.0))
    b.append(_l(260, 128, 268, 128, 1.0))
    b.append(_t(280, 148, "galvo", 7.0, "middle", "#555"))
    b.append(_t(218, 156, "(quét góc tà)", 7.0, "middle", "#666"))

    # polygon mirror with its motor
    b.append(_p("M 196 182 L 218 168 L 240 182 L 240 206 L 218 220 L 196 206 Z", SAND, 1.2))
    b.append(_c(218, 194, 8, "#fff", 1.0))
    b.append(_t(218, 197, "M", 7.4, "middle", "#333"))
    b.append(_t(218, 238, "gương đa giác", 7.2, "middle", "#333"))
    b.append(_t(218, 247, "(quét phương vị)", 7.0, "middle", "#666"))
    b.append(_blk(256, 184, 62, 22, ["động cơ"], 7.2))
    b.append(_arrow(240, 194, 256, 194, 1.0))

    # laser diode and projection optics
    b.append(_blk(28, 180, 66, 28, ["laser diode"], 7.2))
    b.append(_blk(108, 180, 62, 28, ["quang phát"], 7.2))
    b.append(_arrow(94, 194, 108, 194, 1.0))
    b.append(_arrow(170, 194, 196, 194, 1.0))

    # detection optics and avalanche photodiode
    b.append(_blk(256, 140, 66, 24, ["quang thu"], 7.2))
    b.append(_arrow(240, 152, 256, 152, 1.0))
    b.append(_blk(340, 140, 82, 24, ["photodiode thác"], 6.8))
    b.append(_arrow(322, 152, 340, 152, 1.0))

    # the electronic chain, laid out left to right along the bottom
    b.append(_blk(28, 282, 68, 26, ["điều chế"], 7.2))
    b.append(_arrow(62, 282, 62, 210, 1.0))
    b.append(_l(62, 210, 28, 210, 1.0))
    b.append(_blk(136, 282, 84, 26, ["tách pha"], 7.4))
    b.append(_arrow(96, 295, 136, 295, 1.0))
    b.append(_t(116, 310, "tín hiệu chuẩn", 7.0, "middle", "#555"))
    b.append(_arrow(422, 164, 422, 258, 1.0))
    b.append(_l(422, 258, 200, 258, 1.0))
    b.append(_arrow(200, 258, 200, 282, 1.0))
    b.append(_t(330, 254, "tín hiệu thu", 7.2, "middle", "#555"))

    b.append(_arrow(220, 308, 220, 330, 1.0))
    b.append(_t(240, 322, "pha", 7.2, "start", "#555"))
    b.append(_blk(136, 330, 84, 26, ["hiệu chỉnh"], 7.4))
    b.append(_arrow(178, 356, 178, 376, 1.0))
    b.append(_t(178, 390, "khoảng cách", 8.2, "middle", INK, True))

    b.append(_blk(262, 282, 84, 26, ["tách biên độ"], 7.4))
    b.append(_arrow(232, 258, 262, 276, 0.9))
    b.append(_arrow(304, 308, 304, 330, 1.0))
    b.append(_t(304, 344, "cường độ", 8.2, "middle", INK, True))

    # the two servo channels report the scan angles directly
    b.append(_arrow(428, 199, 470, 199, 0.9))
    b.append(_t(476, 203, "phương vị", 7.8, "start", "#444"))
    b.append(_arrow(284, 128, 470, 128, 0.9))
    b.append(_t(476, 131, "góc tà", 7.8, "start", "#444"))
    b.append(_blk(340, 116, 88, 22, ["servo gương gật"], 6.6))
    b.append(_blk(340, 188, 88, 22, ["servo đa giác"], 6.6))
    return _fig(svg(560, 400, STY + "".join(b), "Sơ đồ khối hệ lidar điều chế biên độ LASAR"),
                "Hình 9-7. Hệ lidar AM của Perceptron mô tả trong bằng phát minh Hoa Kỳ 5.006.721 dùng "
                "một gương đa giác quay để quét đồng bộ. Thêm một gương gật để quét chậm hơn theo "
                "phương vuông góc, tạo ra mẫu quét raster. Khoảng cách được xác định bằng cách so pha "
                "của tín hiệu laser điều chế biên độ phát ra và tín hiệu trở về.",
                "Figure 9-7. The Perceptron AM lidar system described in U.S. patent 5,006,721 uses a "
                "rotating polygon mirror for synchronized scanning. A nodding mirror adds a slower sweep "
                "in the orthogonal direction, producing a raster scan pattern. Range is determined by "
                "comparing the phase of the outgoing and returning AM laser signals.",
                "Sơ đồ khối LASAR: laser diode, quang phát, gương đa giác, gương gật, quang thu, photodiode thác và chuỗi tách pha cho ra khoảng cách.",
                "The LASAR block diagram: laser diode, projection optics, polygon and nodding mirrors, detection optics, avalanche photodiode and the phase chain that yields range.")


# ---------------------------------------------------------------- 9.8
def fig_9_8():
    b = []
    b.append(_p("M 232 62 q 14 -22 40 -18 q 22 4 26 20 q 6 18 -8 26 q -20 12 -40 4 q -18 -8 -18 -32 z",
                SAND, 1.2))
    b.append(_c(272, 84, 3.2, INK))
    b.append(_t(196, 84, "vật đích", 8.0, "middle", INK, True))
    b.append(_t(196, 96, "(nguồn chủ động)", 7.2, "middle", "#555"))
    b.append(_arrow(292, 66, 330, 52, 1.0, BLUE))
    b.append(_t(334, 52, "X", 8.2, "start", BLUE, True))
    b.append(_arrow(292, 66, 320, 84, 1.0, BLUE))
    b.append(_t(324, 90, "Y", 8.2, "start", BLUE, True))
    b.append(_l(292, 66, 292, 104, 0.9, MUTED, "4 3"))
    b.append(_t(296, 114, "Z", 8.2, "start", "#666", True))

    b.append(_l(160, 178, 470, 178, 1.0, GREEN))
    b.append(_t(316, 172, "b", 9.0, "middle", GREEN, True))
    b.append(_l(160, 172, 160, 184, 0.9, GREEN))
    b.append(_l(470, 172, 470, 184, 0.9, GREEN))

    for cx in (150, 300, 450):
        b.append(_p("M %d 196 q 30 -14 60 0 q -30 14 -60 0 z" % (cx - 30), BAND, 1.1))
        b.append(_r(cx - 40, 224, 80, 10, "#fff", 1.0))
        b.append(_l(272, 88, cx, 224, 0.9, BLUE, "4 3"))

    b.append(_c(150, 229, 3.0, RED))
    b.append(_c(300, 229, 3.0, RED))
    b.append(_c(450, 229, 3.0, RED))
    b.append(_t(150, 250, "u", 8.4, "middle", RED, True))
    b.append(_t(158, 250, "trái", 6.6, "start", RED))
    b.append(_t(450, 250, "u", 8.4, "middle", RED, True))
    b.append(_t(458, 250, "phải", 6.6, "start", RED))
    b.append(_t(300, 250, "v", 8.4, "middle", GREEN, True))

    b.append(_t(104, 198, "quang trụ", 7.4, "end", "#555"))
    b.append(_t(104, 232, "dãy thu tuyến tính", 7.4, "end", "#555"))
    b.append(_l(470, 188, 470, 224, 1.0, INK))
    b.append(_t(478, 208, "f", 8.4, "start", INK, True))
    b.append(_t(300, 284, "xₚ = b(u_phải + u_trái)/2(u_phải − u_trái)", 8.2, "middle", "#333"))
    return _fig(svg(560, 296, STY + "".join(b), "Bố trí ba dãy thu của hệ OPTOTRAK"),
                "Hình 9-8. Hệ theo dõi vị trí OPTOTRAK dùng một cách bố trí mới của quang học trụ và "
                "các bộ thu một chiều để tam giác đạc vị trí ba chiều của một đích LED hồng ngoại. Hệ "
                "có thể theo dõi tới 255 đích được ghép kênh riêng rẽ.",
                "Figure 9-8. The OPTOTRAK position tracking system uses a novel arrangement of "
                "cylindrical optics and one-dimensional detectors to triangulate the 3-D position of an "
                "infrared LED target. Up to 255 individually multiplexed targets can be tracked.",
                "Ba cụm thấu kính trụ và ba dãy thu tuyến tính dưới một đích LED, với đường đáy b và các vị trí u trái, u phải, v.",
                "Three cylindrical lens and line-detector pairs beneath an LED target, with the baseline b and the positions u-left, u-right and v.")


FIGURES = [fig_9_1, fig_9_2, fig_9_3, fig_9_4, fig_9_5, fig_9_6, fig_9_7, fig_9_8]
