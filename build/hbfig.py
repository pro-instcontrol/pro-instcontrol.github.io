# -*- coding: utf-8 -*-
"""Vector redraws of the figures in the CRC Measurement Handbook, Ch. 3 and 4.

Every function returns (svg, caption_vi, caption_en, aria_vi, aria_en).
Curves that come from a formula (step responses, Bode plots) are computed
here rather than sketched, so the shapes are right.
"""
import math

INK = "#2a2a2a"
TXT = "#111111"
MUTED = "#888888"
GOLD = "#b45309"
PAPER = "#ffffff"

STYLE = ("<style>.ax{stroke:#2a2a2a;stroke-width:1.2;fill:none}"
         ".gr{stroke:#d8d8d8;stroke-width:.9;fill:none}"
         ".c1{stroke:#2a2a2a;stroke-width:2;fill:none}"
         ".c2{stroke:#b45309;stroke-width:2;fill:none}"
         ".c3{stroke:#888;stroke-width:1.6;fill:none;stroke-dasharray:5 4}"
         ".d1{stroke:#2a2a2a;stroke-width:1.4;fill:none;stroke-dasharray:4 4}"
         ".t{font:11px Inter,Helvetica,sans-serif;fill:#111}"
         ".tb{font:11px Inter,Helvetica,sans-serif;fill:#111;font-weight:600}"
         ".ts{font:10px Inter,Helvetica,sans-serif;fill:#666}"
         "</style>")


def _f(v):
    return ("%.2f" % v).rstrip("0").rstrip(".")


class Box(object):
    """Maps data coordinates onto the SVG canvas."""

    def __init__(self, w, h, xr, yr, pad=(46, 16, 16, 34)):
        self.w, self.h = w, h
        self.x0, self.x1 = xr
        self.y0, self.y1 = yr
        l, t, r, b = pad
        self.l, self.t, self.r, self.b = l, t, r, b
        self.pw = w - l - r
        self.ph = h - t - b

    def x(self, v):
        return self.l + (v - self.x0) * self.pw / (self.x1 - self.x0)

    def y(self, v):
        return self.t + self.ph - (v - self.y0) * self.ph / (self.y1 - self.y0)

    def axes(self, xlab="", ylab="", xt=(), yt=(), grid=True):
        o = ['<line class="ax" x1="%s" y1="%s" x2="%s" y2="%s"/>'
             % (_f(self.l), _f(self.t + self.ph), _f(self.l + self.pw), _f(self.t + self.ph)),
             '<line class="ax" x1="%s" y1="%s" x2="%s" y2="%s"/>'
             % (_f(self.l), _f(self.t), _f(self.l), _f(self.t + self.ph))]
        for v, lab in xt:
            x = self.x(v)
            o.append('<line class="ax" x1="%s" y1="%s" x2="%s" y2="%s"/>'
                     % (_f(x), _f(self.t + self.ph), _f(x), _f(self.t + self.ph + 4)))
            o.append('<text class="ts" x="%s" y="%s" text-anchor="middle">%s</text>'
                     % (_f(x), _f(self.t + self.ph + 15), lab))
            if grid:
                o.append('<line class="gr" x1="%s" y1="%s" x2="%s" y2="%s"/>'
                         % (_f(x), _f(self.t), _f(x), _f(self.t + self.ph)))
        for v, lab in yt:
            y = self.y(v)
            o.append('<line class="ax" x1="%s" y1="%s" x2="%s" y2="%s"/>'
                     % (_f(self.l - 4), _f(y), _f(self.l), _f(y)))
            o.append('<text class="ts" x="%s" y="%s" text-anchor="end">%s</text>'
                     % (_f(self.l - 7), _f(y + 3.5), lab))
            if grid:
                o.append('<line class="gr" x1="%s" y1="%s" x2="%s" y2="%s"/>'
                         % (_f(self.l), _f(y), _f(self.l + self.pw), _f(y)))
        if xlab:
            o.append('<text class="ts" x="%s" y="%s" text-anchor="middle">%s</text>'
                     % (_f(self.l + self.pw / 2), _f(self.h - 4), xlab))
        if ylab:
            o.append('<text class="ts" x="10" y="%s" text-anchor="middle" '
                     'transform="rotate(-90 10 %s)">%s</text>'
                     % (_f(self.t + self.ph / 2), _f(self.t + self.ph / 2), ylab))
        return "".join(o)

    def curve(self, pts, cls="c1"):
        d = "M" + " L".join("%s %s" % (_f(self.x(a)), _f(self.y(b))) for a, b in pts)
        return '<path class="%s" d="%s"/>' % (cls, d)

    def poly(self, pts, cls="c1"):
        return self.curve(pts, cls)

    def dot(self, xv, yv, r=2.6, fill=TXT):
        return ('<circle cx="%s" cy="%s" r="%s" fill="%s"/>'
                % (_f(self.x(xv)), _f(self.y(yv)), _f(r), fill))

    def label(self, xv, yv, txt, cls="t", anchor="start", dx=0, dy=0):
        return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
                % (cls, _f(self.x(xv) + dx), _f(self.y(yv) + dy), anchor, txt))


def svg(w, h, body, title):
    return ('<svg viewBox="0 0 %d %d" role="img" aria-label="%s">%s%s</svg>'
            % (w, h, title, STYLE, body))


def _fig(svg_s, cap_vi, cap_en, aria_vi, aria_en):
    return (svg_s, cap_vi, cap_en, aria_vi, aria_en)


# ---------------------------------------------------------------- 3.1
def fig_3_1():
    b = Box(560, 220, (0, 12), (36, 40.5), pad=(46, 18, 18, 40))
    t = [0, .8, 1.6, 2.4, 3.2, 4.0, 4.8, 5.6, 6.4, 7.2, 8.0, 8.8, 9.6, 10.4, 11.2, 12]
    v = [36.6, 37.4, 38.1, 38.6, 38.9, 39.0, 38.9, 38.6, 38.2, 37.9, 38.3, 38.8, 39.1, 39.0, 38.7, 38.5]
    body = b.axes("thời gian (ngày)", "°C", xt=[(0, "0"), (4, "4"), (8, "8"), (12, "12")],
                  yt=[(37, "37"), (38, "38"), (39, "39"), (40, "40")])
    body += b.curve(list(zip(t, v)))
    body += b.dot(4.0, 39.0) + b.dot(10.4, 39.0)
    body += b.label(4.2, 39.25, "sốt cao nhất")
    body += b.label(8.2, 37.55, "hạ sốt")
    return _fig(svg(560, 220, body, "Biểu đồ nhiệt độ bệnh nhân theo thời gian"),
                "Hình 3-1 · Biểu đồ nhiệt độ của một bệnh nhân cho thấy các thay đổi diễn ra theo thời gian.",
                "Figure 3.1 · A patient’s temperature chart shows changes taking place over time.",
                "Đường nhiệt độ bệnh nhân tăng tới đỉnh rồi giảm dần theo ngày",
                "Patient temperature curve rising to a peak and falling over days")


# ---------------------------------------------------------------- 3.2
def fig_3_2():
    b = Box(560, 220, (1, 1000), (0, 1.05), pad=(46, 18, 18, 40))
    body = b.axes("tần số đầu vào (Hz, thang log)", "hệ số khuếch đại",
                  xt=[(1, "1"), (10, "10"), (100, "100"), (1000, "1k")],
                  yt=[(0, "0"), (0.5, "0,5"), (1, "1,0")])
    # single-pole open-loop gain, normalized
    pts = []
    for i in range(0, 121):
        lg = i / 120.0 * 3.0
        f = 10 ** lg
        a = 1.0 / math.sqrt(1 + (f / 30.0) ** 2)
        pts.append((f, a))
    body += b.curve(pts)
    body += '<line class="d1" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
        _f(b.x(30)), _f(b.y(0)), _f(b.x(30)), _f(b.y(0.707)))
    body += b.label(33, 0.30, "f = 30 Hz: còn 0,707")
    return _fig(svg(560, 220, body, "Đồ thị hệ số khuếch đại theo tần số đầu vào"),
                "Hình 3-2 · Đồ thị này cho thấy hệ số khuếch đại của một bộ khuếch đại thay đổi thế nào theo tần số đầu vào.",
                "Figure 3.2 · This graph shows how the amplification of an amplifier changes with input frequency.",
                "Đường cong khuếch đại giảm khi tần số tăng",
                "Gain curve falling as frequency rises")


# ---------------------------------------------------------------- 3.3
def fig_3_3():
    out = []
    targets = [(150, "precision cao, độ chính xác thấp"), (400, "độ chính xác cao, precision thấp")]
    sets = [[(-26, 14), (-18, 20), (-10, 8), (-4, 16), (2, 10)], [(-30, -26), (18, 30), (-24, 26), (26, -18), (4, 2)]]
    for (cx, lab), pts in zip(targets, sets):
        out.append('<circle cx="%d" cy="112" r="66" fill="#fafafa" stroke="#2a2a2a" stroke-width="1.4"/>' % cx)
        for r in (48, 30, 13):
            out.append('<circle cx="%d" cy="112" r="%d" fill="none" stroke="#c9a961" stroke-width="1"/>' % (cx, r))
        out.append('<circle cx="%d" cy="112" r="3.4" fill="#b45309"/>' % cx)
        for dx, dy in pts:
            out.append('<circle cx="%d" cy="%d" r="3.6" fill="#111"/>' % (cx + dx, 112 + dy))
        out.append('<text class="ts" x="%d" y="196" text-anchor="middle">%s</text>' % (cx, lab))
    out.append('<text class="tb" x="150" y="28" text-anchor="middle">(a)</text>')
    out.append('<text class="tb" x="400" y="28" text-anchor="middle">(b)</text>')
    return _fig(svg(560, 210, "".join(out), "Hai bia bắn cung so sánh độ phân giải, độ lặp lại và độ chính xác"),
                "Hình 3-3 · Hai tập mũi tên bắn vào bia giúp hiểu các khái niệm đo lường: độ phân giải, precision và độ chính xác. (a) Bia dùng để bắn tên, cho phép khảo sát các thuật ngữ mô tả kết quả đo. (b) Một tập vị trí khác.",
                "Figure 3.3 · Two sets of arrow shots fired into a target allow understanding of the measurement concepts of discrimination, precision, and accuracy. (a) The target used for shooting arrows. (b) A different set of placements.",
                "Hai bia tròn có các điểm bắn: một tập chụm nhưng lệch tâm, một tập tản nhưng quanh tâm",
                "Two targets: one tight cluster off centre, one scattered around centre")


# ---------------------------------------------------------------- 3.4
def fig_3_4():
    o = []
    boxes = [(48, "đại lượng vào", 120), (200, "cảm biến", 104),
             (336, "điều hoà tín hiệu", 128), (496, "ra", 52)]
    for x, lab, w in boxes:
        o.append('<rect x="%d" y="70" width="%d" height="56" rx="4" fill="#fff" stroke="#2a2a2a" stroke-width="1.4"/>'
                 % (x, w))
        o.append('<text class="t" x="%d" y="102" text-anchor="middle">%s</text>' % (x + w // 2, lab))
    for x1, x2 in ((168, 200), (304, 336), (464, 496)):
        o.append('<line class="c1" x1="%d" y1="98" x2="%d" y2="98" marker-end="url(#a34)"/>' % (x1, x2))
    o.append('<defs><marker id="a34" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
             '<path d="M0,0 L7,3 L0,6 Z" fill="#2a2a2a"/></marker></defs>')
    o.append('<text class="ts" x="280" y="160" text-anchor="middle">mỗi khối có một hàm truyền G = tĩnh × động</text>')
    return _fig(svg(560, 180, "".join(o), "Sơ đồ khối một cảm biến độ ẩm"),
                "Hình 3-4 · Thiết bị đo được tạo thành từ sự nối tiếp các khối. Mỗi khối có thể được biểu diễn bằng một mô hình khái niệm và toán học. Ví dụ này là một loại cảm biến độ ẩm.",
                "Figure 3.4 · Instruments are formed from a connection of blocks. Each block can be represented by a conceptual and mathematical model. This example is of one type of humidity sensor.",
                "Sơ đồ khối: đầu vào vật lý, phần tử cảm biến, điều hoà tín hiệu, đầu ra",
                "Block diagram: physical input, sensing element, signal conditioning, output")


# ---------------------------------------------------------------- 3.5
def fig_3_5():
    b = Box(560, 300, (0, 10), (0, 10), pad=(52, 22, 22, 42))
    body = b.axes("đại lượng vào (0–100 % dải)", "đại lượng ra",
                  xt=[(0, "0"), (5, "50"), (10, "100")], yt=[(0, "0"), (5, "50"), (10, "100")])
    body += b.curve([(0, 1.6), (10, 9.2)], "c1")          # actual response
    body += b.curve([(0, 1.6), (8.4, 9.2)], "c3")         # ideal through offset
    body += '<line class="d1" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
        _f(b.x(0)), _f(b.y(1.6)), _f(b.x(2.4)), _f(b.y(1.6)))
    body += '<line class="d1" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
        _f(b.x(8.4)), _f(b.y(9.2)), _f(b.x(8.4)), _f(b.y(0)))
    body += b.label(0.12, 1.02, "offset (lệch zero)")
    body += b.label(5.2, 4.4, "độ dốc = độ nhạy", "ts")
    body += b.label(8.5, 9.55, "span 0–100 %", "ts", anchor="end")
    body += b.label(1.2, 8.6, "đường lý tưởng", "ts")
    return _fig(svg(560, 300, body, "Đồ thị quan hệ vào–ra của một khối thiết bị đo"),
                "Hình 3-5 · Đồ thị quan hệ giữa đại lượng vào và ra của một khối thiết bị đo, cho thấy một số đặc tính tĩnh đặc trưng.",
                "Figure 3.5 · The graph relating input to output variables for an instrument block shows several distinctive static performance characteristics.",
                "Đồ thị vào–ra có độ dốc, điểm lệch zero và dải làm việc",
                "Input-output graph with slope, zero offset and span")


# ---------------------------------------------------------------- 3.6
def fig_3_6():
    o = []
    panels = [(14, "(a)"), (196, "(b)"), (378, "(c)")]
    # (a) spring drift
    b = Box(178, 150, (0, 10), (0, 1.1), pad=(30, 22, 10, 24))
    o.append('<g transform="translate(%d,20)">' % panels[0][0])
    o.append(b.axes("", "", xt=[], yt=[(1, "1,00")]))
    o.append(b.curve([(0, 1.0), (10, 0.93)], "c1"))
    o.append('<text class="tb" x="4" y="12">(a)</text>')
    o.append('<text class="ts" x="89" y="140" text-anchor="middle">thời gian</text>')
    o.append('</g>')
    # (b) amplifier settling
    b = Box(178, 150, (0, 6), (0, 1.1), pad=(30, 22, 10, 24))
    o.append('<g transform="translate(%d,20)">' % panels[1][0])
    o.append(b.axes("", "", xt=[], yt=[]))
    pts = [(i / 10.0, 1.0 - 0.28 * math.exp(-i / 10.0 * 1.4)) for i in range(0, 61)]
    o.append(b.curve(pts, "c1"))
    o.append('<text class="tb" x="4" y="12">(b)</text>')
    o.append('<text class="ts" x="89" y="140" text-anchor="middle">thời gian sau khi cấp điện</text>')
    o.append('</g>')
    # (c) temperature drift
    b = Box(178, 150, (0, 60), (0.96, 1.18), pad=(30, 22, 10, 24))
    o.append('<g transform="translate(%d,20)">' % panels[2][0])
    o.append(b.axes("", "", xt=[(0, "0 °C"), (30, "30"), (60, "60")], yt=[]))
    pts = [(t, 1.0 + 0.00012 * (t - 25) ** 2) for t in range(0, 61, 2)]
    o.append(b.curve(pts, "c1"))
    o.append('<text class="tb" x="4" y="12">(c)</text>')
    o.append('</g>')
    return _fig(svg(560, 210, "".join(o), "Ba dạng trôi của thiết bị đo"),
                "Hình 3-6 · Trôi trong đặc tính của thiết bị đo có nhiều dạng: (a) trôi theo thời gian của một cân lò xo; (b) cách một bộ khuếch đại điện tử ổn định theo thời gian về giá trị cuối sau khi cấp điện; (c) trôi do nhiệt độ của một bộ khuếch đại điện tử thay đổi theo nhiệt độ làm việc thực tế.",
                "Figure 3.6 · Drift in the performance of an instrument takes many forms: (a) drift over time for a spring balance; (b) how an electronic amplifier might settle over time to a final value after power is supplied; (c) drift, due to temperature, of an electronic amplifier varies with the actual temperature of operation.",
                "Ba biểu đồ nhỏ: trôi theo thời gian, ổn định sau cấp điện, trôi theo nhiệt độ",
                "Three small plots: drift over time, settling after power-on, drift vs temperature")


# ---------------------------------------------------------------- 3.7
def fig_3_7():
    b = Box(560, 280, (0, 10), (0, 10), pad=(52, 20, 24, 40))
    body = b.axes("đại lượng vào", "đại lượng ra",
                  xt=[(0, "0"), (5, "50"), (10, "100")], yt=[(0, "0"), (5, "50"), (10, "100")])
    up = [(0, 1.2), (2, 2.4), (4, 3.9), (6, 5.6), (8, 7.5), (10, 9.4)]
    dn = [(10, 9.0), (8, 6.7), (6, 4.8), (4, 3.1), (2, 1.8), (0, 0.8)]
    body += b.curve(up, "c1")
    body += b.curve(dn, "c2")
    body += b.label(6.4, 6.3, "nhánh tăng", "ts")
    body += b.label(6.4, 4.0, "nhánh giảm", "ts")
    body += '<line class="d1" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
        _f(b.x(5)), _f(b.y(4.75)), _f(b.x(5)), _f(b.y(5.45)))
    body += b.label(5.15, 5.1, "vùng trễ", "ts")
    return _fig(svg(560, 280, body, "Vòng trễ của quan hệ vào–ra"),
                "Hình 3-7 · Đồ thị tổng quát của quan hệ vào–ra khi có hiện tượng trễ. (Từ P. H. Sydenham, Handbook of Measurement Science, Vol. 2, Chichester, U.K., John Wiley & Sons, 1983. Được phép sử dụng.)",
                "Figure 3.7 · Generalized graph of output/input relationship where hysteresis is present. (From P. H. Sydenham, Handbook of Measurement Science, Vol. 2, Chichester, U.K., John Wiley & Sons, 1983. With permission.)",
                "Vòng trễ kín giữa nhánh tăng và nhánh giảm",
                "Closed hysteresis loop between rising and falling branches")


# ---------------------------------------------------------------- 3.8
def fig_3_8():
    b = Box(560, 230, (0, 10), (0, 10), pad=(50, 20, 20, 40))
    body = b.axes("đại lượng vào tăng tuyến tính", "đại lượng ra",
                  xt=[(0, "0"), (10, "t")], yt=[(0, "0")])
    body += b.curve([(0, 0.6), (10, 9.2)], "c3")
    pts = []
    for i in range(0, 101):
        x = i / 10.0
        y = 0.6 + 0.86 * x - 0.012 * x ** 3
        pts.append((x, y))
    body += b.curve(pts, "c1")
    body += b.label(7.0, 8.9, "ra thực (bão hoà dần)", "ts")
    body += b.label(2.0, 6.0, "ra lý tưởng", "ts")
    return _fig(svg(560, 230, body, "Khuếch đại phi tuyến gây méo dạng đầu ra"),
                "Hình 3-8 · Khuếch đại phi tuyến có thể gây ra méo dạng đầu ra không mong muốn.",
                "Figure 3.8 · Nonlinear amplification can give rise to unwanted output distortion.",
                "Đường ra bám đường lý tưởng rồi bão hoà ở biên độ lớn",
                "Output follows the ideal line then saturates at high amplitude")


# ---------------------------------------------------------------- 3.9
def fig_3_9():
    o = []
    for k, (lab, kind) in enumerate([("(a) chỉnh lưu", "rect"), ("(b) bão hoà", "sat"), ("(c) méo chuyển tiếp", "cross")]):
        b = Box(168, 130, (0, 2 * math.pi), (-1.35, 1.35), pad=(26, 14, 8, 22))
        o.append('<g transform="translate(%d,16)">' % (14 + k * 180))
        o.append(b.axes("", "", xt=[], yt=[(0, "0")]))
        inp = [(i / 60.0 * 2 * math.pi, math.sin(i / 60.0 * 2 * math.pi)) for i in range(0, 61)]
        o.append(b.curve(inp, "c3"))
        if kind == "rect":
            out = [(i / 60.0 * 2 * math.pi, max(0.0, math.sin(i / 60.0 * 2 * math.pi))) for i in range(0, 61)]
        elif kind == "sat":
            out = [(i / 60.0 * 2 * math.pi, max(-0.62, min(0.62, math.sin(i / 60.0 * 2 * math.pi) * 1.5)))
                   for i in range(0, 61)]
        else:
            out = []
            for i in range(0, 61):
                ph = i / 60.0 * 2 * math.pi
                v = math.sin(ph)
                out.append((ph, 0.0 if abs(v) < 0.18 else v - (0.18 if v > 0 else -0.18)))
        o.append(b.curve(out, "c1"))
        o.append('<text class="tb" x="4" y="12">%s</text>' % lab)
        o.append('</g>')
    return _fig(svg(560, 170, "".join(o), "Ba dạng méo dạng sóng do bão hoà và chuyển tiếp"),
                "Hình 3-9 · Các khối có thể làm sai dạng sóng nếu hiệu ứng bão hoà và chuyển tiếp không được kiểm soát: (a) chỉnh lưu; (b) bão hoà; và (c) méo chuyển tiếp.",
                "Figure 3.9 · Blocks can incorrectly alter the shape of waveforms if saturation and crossover effects are not controlled: (a) rectification; (b) saturation; and (c) crossover distortion.",
                "Ba ô sóng: nửa sóng bị cắt, đỉnh bị cắt bằng, và điểm zero bị nhảy bậc",
                "Three waveform panels: rectified, clipped, and crossover notch")


# ---------------------------------------------------------------- 3.10
def fig_3_10():
    b = Box(560, 210, (0, 2 * math.pi), (-0.2, 2.3), pad=(40, 20, 20, 34))
    body = b.axes("góc pha", "biên độ", xt=[(0, "0"), (math.pi, "π"), (2 * math.pi, "2π")],
                  yt=[(0, "0"), (1, "1"), (2, "2")])
    body += b.curve([(i / 80.0 * 2 * math.pi, 1 + math.sin(i / 80.0 * 2 * math.pi))
                     for i in range(0, 81)], "c1")
    body += '<line class="d1" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
        _f(b.x(0)), _f(b.y(1)), _f(b.x(2 * math.pi)), _f(b.y(1)))
    body += b.label(0.15, 2.18, "mức dc thêm vào (bias) = 1")
    return _fig(svg(560, 210, body, "Dạng sóng xoay chiều được dịch lên mức dương bằng bias"),
                "Hình 3-10 · Bias là khi toàn bộ giá trị của tín hiệu được nâng lên một lượng bằng nhau. Ở đây là một dạng sóng xoay chiều vào được dịch để toàn bộ mang cực tính dương.",
                "Figure 3.10 · Bias is where a signal has all of its value raised by an equal amount. Shown here is an ac input waveform biased to be all of positive polarity.",
                "Sóng sin được nâng lên nằm hoàn toàn trên trục zero",
                "Sine wave shifted up so it stays above zero")


# ---------------------------------------------------------------- 3.11
def fig_3_11():
    o = []
    data = [(0.5, 1.3), (1.6, 2.1), (2.7, 3.4), (3.8, 3.9), (4.9, 5.4), (6.0, 5.9), (7.1, 7.2), (8.2, 7.7)]
    variants = ["(a) khớp bình phương nhỏ nhất", "(b) khớp qua zero", "(c) nối 0 % và 100 %", "(d) đường lý thuyết"]
    for k, lab in enumerate(variants):
        b = Box(262, 150, (0, 9), (0, 9), pad=(28, 14, 10, 24))
        o.append('<g transform="translate(%d,%d)">' % (14 + (k % 2) * 272, 18 + (k // 2) * 168))
        o.append(b.axes("", "", xt=[], yt=[]))
        for x, y in data:
            o.append(b.dot(x, y, 2.4))
        if k == 0:
            seg = [(0, 0.42), (9, 8.55)]
        elif k == 1:
            seg = [(0, 0), (9, 8.2)]
        elif k == 2:
            seg = [(0.2, 0.9), (8.2, 8.05)]
        else:
            seg = [(0, 0.9), (9, 8.6)]
        o.append(b.curve(seg, "c2" if k == 3 else "c1"))
        o.append('<text class="tb" x="4" y="12">%s</text>' % lab)
        o.append('</g>')
    return _fig(svg(560, 350, "".join(o), "Bốn cách biểu diễn sai số phi tuyến"),
                "Hình 3-11 · Sai số phi tuyến có thể được biểu diễn theo bốn cách khác nhau: (a) đường khớp tốt nhất (theo phương pháp đã chọn); (b) đường khớp tốt nhất qua zero; (c) đường nối điểm 0 % và 100 %; và (d) đường lý thuyết. (Từ P. H. Sydenham, Handbook of Measurement Science, Vol. 2, Chichester, U.K., John Wiley & Sons, 1983. Được phép sử dụng.)",
                "Figure 3.11 · Error of nonlinearity can be expressed in four different ways: (a) best fit line (based on selected method used to decide this); (b) best fit line through zero; (c) line joining 0% and 100% points; and (d) theoretical line. (From P. H. Sydenham, Handbook of Measurement Science, Vol. 2, Chichester, U.K., John Wiley & Sons, 1983. With permission.)",
                "Bốn ô đồ thị với cùng tập điểm và bốn đường khớp khác nhau",
                "Four panels of the same data points with four different fit lines")


# ---------------------------------------------------------------- 3.12
def fig_3_12():
    o = []
    kinds = [("bậc thang", "step"), ("dốc", "ramp"), ("sin", "sine"), ("xung", "impulse")]
    for k, (lab, kind) in enumerate(kinds):
        b = Box(262, 140, (0, 10), (-0.2, 1.35), pad=(26, 14, 10, 22))
        o.append('<g transform="translate(%d,%d)">' % (14 + (k % 2) * 272, 14 + (k // 2) * 152))
        o.append(b.axes("", "", xt=[], yt=[]))
        if kind == "step":
            pts = [(0, 0), (3.4, 0), (3.4, 1), (10, 1)]
        elif kind == "ramp":
            pts = [(0, 0), (3.0, 0), (9.6, 1.05)]
        elif kind == "sine":
            pts = [(i / 60.0 * 10, math.sin(i / 60.0 * 2 * math.pi * 1.6)) for i in range(0, 61)]
        else:
            pts = [(0, 0), (4.6, 0), (4.6, 1.15), (4.9, 0), (10, 0)]
        o.append(b.curve(pts, "c1"))
        o.append('<text class="tb" x="4" y="12">%s</text>' % lab)
        o.append('</g>')
    return _fig(svg(560, 310, "".join(o), "Bốn hàm kích thích thử nghiệm"),
                "Hình 3-12 · Có thể khảo sát đáp ứng động của một khối bằng một loạt hàm kích thích vào đơn giản. (Từ P. H. Sydenham, Handbook of Measurement Science, Vol. 2, Chichester, U.K., John Wiley & Sons, 1983. Được phép sử dụng.)",
                "Figure 3.12 · The dynamic response of a block can be investigated using a range of simple input forcing functions. (From P. H. Sydenham, Handbook of Measurement Science, Vol. 2, Chichester, U.K., John Wiley & Sons, 1983. With permission.)",
                "Bốn dạng tín hiệu: bậc thang, dốc, sin, xung",
                "Four input signals: step, ramp, sine, impulse")


# ---------------------------------------------------------------- 3.13
def fig_3_13():
    o = []
    # (a) strain gauge bridge
    o.append('<text class="tb" x="14" y="18">(a)</text>')
    o.append('<rect x="60" y="46" width="150" height="26" rx="3" fill="#fff" stroke="#2a2a2a" stroke-width="1.4"/>')
    o.append('<text class="t" x="135" y="64" text-anchor="middle">strain gage R</text>')
    o.append('<line class="c1" x1="20" y1="59" x2="60" y2="59"/><line class="c1" x1="210" y1="59" x2="250" y2="59"/>')
    o.append('<text class="ts" x="16" y="50">V vào</text><text class="ts" x="214" y="50">V ra</text>')
    o.append('<text class="ts" x="135" y="96" text-anchor="middle">R thay đổi theo biến dạng: V ra = V vào · R/(R+R₀)</text>')
    # (b) responses
    b = Box(262, 150, (0, 10), (0, 1.4), pad=(26, 14, 10, 24))
    o.append('<g transform="translate(292,10)">')
    o.append(b.axes("", "", xt=[], yt=[]))
    o.append(b.curve([(0, 0), (2.6, 0), (2.6, 1), (10, 1)], "c3"))
    o.append(b.curve([(0, 0), (2.6, 0), (2.6, 1), (10, 1)], "c1"))
    o.append('<text class="tb" x="4" y="12">(b)</text>')
    o.append('<text class="ts" x="120" y="140" text-anchor="middle">vào và ra trùng dạng, chỉ khác biên độ</text>')
    o.append('</g>')
    return _fig(svg(560, 170, "".join(o), "Khối bậc zero: cảm biến biến dạng và đáp ứng"),
                "Hình 3-13 · Đáp ứng vào và ra của một khối bậc zero: (a) mô hình vật lý và toán học của cảm biến biến dạng; và (b) các đáp ứng. (Từ P. H. Sydenham, Handbook of Measurement Science, Vol. 2, Chichester, U.K., John Wiley & Sons, 1983. Được phép sử dụng.)",
                "Figure 3.13 · Input and output responses for a zero-order block: (a) strain gage physical and mathematical model; and (b) responses. (From P. H. Sydenham, Handbook of Measurement Science, Vol. 2, Chichester, U.K., John Wiley & Sons, 1983. With permission.)",
                "Sơ đồ cảm biến biến dạng và đáp ứng bậc thang không méo",
                "Strain gauge model and an undistorted step response")


# ---------------------------------------------------------------- 3.14
def fig_3_14():
    b = Box(560, 250, (0, 6), (0, 1.08), pad=(50, 20, 24, 40))
    body = b.axes("t/τ", "y/(AK)",
                  xt=[(0, "0"), (1, "1τ"), (2, "2τ"), (3, "3τ"), (4, "4τ")],
                  yt=[(0, "0"), (0.632, "0,632"), (0.95, "0,95"), (1, "1")])
    body += b.curve([(i / 20.0, 1 - math.exp(-i / 20.0)) for i in range(0, 121)], "c1")
    body += '<line class="d1" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
        _f(b.x(1)), _f(b.y(0)), _f(b.x(1)), _f(b.y(0.632)))
    body += '<line class="d1" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
        _f(b.x(0)), _f(b.y(0.632)), _f(b.x(1)), _f(b.y(0.632)))
    body += b.label(1.08, 0.60, "63,2 % sau một hằng số thời gian")
    body += b.label(3.15, 0.86, "95 % sau 3τ")
    return _fig(svg(560, 250, body, "Đáp ứng bậc thang chuẩn hoá của hệ bậc một"),
                "Hình 3-14 · Đáp ứng bậc thang của mọi hệ bậc một đều nằm trong hai đồ thị chuẩn hoá này. (Từ P. H. Sydenham, Handbook of Measurement Science, Vol. 2, Chichester, U.K., John Wiley & Sons, 1983. Được phép sử dụng.)",
                "Figure 3.14 · The step response for all first-order systems is covered by these two normalized graphs. (From P. H. Sydenham, Handbook of Measurement Science, Vol. 2, Chichester, U.K., John Wiley & Sons, 1983. With permission.)",
                "Đường cong hàm mũ tiến tới 1, đánh dấu 63,2 % tại τ",
                "Exponential rise to 1 with 63.2 % marked at one time constant")


# ---------------------------------------------------------------- 3.15
def fig_3_15():
    o = []
    # (a) amplitude ratio, log x
    b = Box(262, 170, (0, 2), (-45, 2), pad=(34, 20, 12, 30))
    o.append('<g transform="translate(10,16)">')
    o.append(b.axes("ωτ (thang log)", "biên độ (dB)", xt=[(0, "0,1"), (1, "1"), (2, "10")],
                    yt=[(0, "0"), (-20, "–20"), (-40, "–40")]))
    pts = []
    for i in range(0, 121):
        u = i / 120.0 * 2 - 1
        w = 10 ** u
        pts.append((u + 1, -10 * math.log10(1 + w * w)))
    o.append(b.curve(pts, "c1"))
    o.append('<text class="tb" x="4" y="12">(a)</text>')
    o.append('</g>')
    # (b) phase
    b = Box(262, 170, (0, 2), (-95, 5), pad=(34, 20, 12, 30))
    o.append('<g transform="translate(288,16)">')
    o.append(b.axes("ωτ (thang log)", "pha (độ)", xt=[(0, "0,1"), (1, "1"), (2, "10")],
                    yt=[(0, "0"), (-45, "–45"), (-90, "–90")]))
    pts = []
    for i in range(0, 121):
        u = i / 120.0 * 2 - 1
        w = 10 ** u
        pts.append((u + 1, -math.degrees(math.atan(w))))
    o.append(b.curve(pts, "c1"))
    o.append('<text class="tb" x="4" y="12">(b)</text>')
    o.append('</g>')
    return _fig(svg(560, 210, "".join(o), "Biên độ và pha của hệ bậc một theo tần số"),
                "Hình 3-15 · Biên độ và độ lệch pha đầu ra của mọi hệ bậc một khi đầu vào là sóng sin được thể hiện bằng hai đường chuẩn hoá này: (a) biên độ và (b) pha. (Từ P. H. Sydenham, Handbook of Measurement Science, Vol. 2, Chichester, U.K., John Wiley & Sons, 1983. Được phép sử dụng.)",
                "Figure 3.15 · The amplitude and phase shift of the output of all first-order systems to a sine-wave input is shown by these two normalized curves; (a) amplitude and (b) phase. (From P. H. Sydenham, Handbook of Measurement Science, Vol. 2, Chichester, U.K., John Wiley & Sons, 1983. With permission.)",
                "Hai đồ thị Bode: biên độ giảm 20 dB/decade và pha từ 0 tới –90 độ",
                "Two Bode plots: amplitude falling and phase going to minus 90 degrees")


# ---------------------------------------------------------------- 3.16
def fig_3_16():
    b = Box(560, 270, (0, 12), (0, 2.05), pad=(50, 20, 26, 40))
    body = b.axes("ωₙt", "y/(AK)",
                  xt=[(0, "0"), (3, "3"), (6, "6"), (9, "9"), (12, "12")],
                  yt=[(0, "0"), (1, "1"), (2, "2")])
    for zeta, cls in ((0.15, "c3"), (0.4, "c2"), (1.0, "c1"), (2.0, "d1")):
        pts = []
        for i in range(0, 241):
            t = i / 20.0
            if zeta < 1:
                wd = math.sqrt(1 - zeta ** 2)
                y = 1 - math.exp(-zeta * t) * (math.cos(wd * t) + zeta / wd * math.sin(wd * t))
            elif abs(zeta - 1) < 1e-9:
                y = 1 - math.exp(-t) * (1 + t)
            else:
                s = math.sqrt(zeta ** 2 - 1)
                y = 1 - math.exp(-zeta * t) * (math.cosh(s * t) + zeta / s * math.sinh(s * t))
            pts.append((t, y))
        body += b.curve(pts, cls)
    body += b.label(6.2, 1.62, "ζ = 0,15", "ts")
    body += b.label(4.0, 1.34, "ζ = 0,4", "ts")
    body += b.label(6.4, 1.08, "ζ = 1 (tới hạn)", "ts")
    body += b.label(3.4, 0.52, "ζ = 2", "ts")
    return _fig(svg(560, 270, body, "Đáp ứng bậc thang của hệ bậc hai với các tỉ số tắt dần khác nhau"),
                "Hình 3-16 · Đáp ứng của hệ bậc hai với đầu vào bậc thang được thấy từ đồ thị chuẩn hoá này. (Từ P. H. Sydenham, Handbook of Measurement Science, Vol. 2, Chichester, U.K., John Wiley & Sons, 1983. Được phép sử dụng.)",
                "Figure 3.16 · The response of second-order systems to a step input is seen from this normalized plot. (From P. H. Sydenham, Handbook of Measurement Science, Vol. 2, Chichester, U.K., John Wiley & Sons, 1983. With permission.)",
                "Bốn đường đáp ứng: dao động tắt dần, tắt dần tới hạn và quá tắt dần",
                "Four step responses: oscillatory, critically damped and overdamped")


# ---------------------------------------------------------------- 3.17
def fig_3_17():
    o = []
    b = Box(262, 180, (-0.3, 1.7), (0, 6.2), pad=(34, 22, 12, 30))
    o.append('<g transform="translate(10,16)">')
    o.append(b.axes("ω/ωₙ (thang log)", "biên độ", xt=[(0, "0,5"), (0.301, "1"), (1, "5")],
                    yt=[(1, "1"), (3, "3"), (6, "6")]))
    for zeta, cls in ((0.1, "c3"), (0.25, "c2"), (0.5, "c1"), (1.0, "d1")):
        pts = []
        for i in range(0, 161):
            u = -0.3 + i / 160.0 * 2.0
            r = 10 ** u
            amp = 1.0 / math.sqrt((1 - r * r) ** 2 + (2 * zeta * r) ** 2)
            pts.append((u, min(amp, 6.1)))
        o.append(b.curve(pts, cls))
    o.append('<text class="tb" x="4" y="12">(a)</text>')
    o.append('</g>')
    b = Box(262, 180, (-0.3, 1.7), (-190, 10), pad=(34, 22, 12, 30))
    o.append('<g transform="translate(288,16)">')
    o.append(b.axes("ω/ωₙ (thang log)", "pha (độ)", xt=[(0, "0,5"), (0.301, "1"), (1, "5")],
                    yt=[(0, "0"), (-90, "–90"), (-180, "–180")]))
    pts = []
    for i in range(0, 161):
        u = -0.3 + i / 160.0 * 2.0
        r = 10 ** u
        ph = -math.degrees(math.atan2(2 * r, 1 - r * r)) if r != 1 else -90
        pts.append((u, ph))
    o.append(b.curve(pts, "c1"))
    o.append('<text class="tb" x="4" y="12">(b)</text>')
    o.append('</g>')
    return _fig(svg(560, 220, "".join(o), "Đáp ứng tần số của hệ bậc hai: biên độ và pha"),
                "Hình 3-17 · Hai đồ thị này cho phép xác định đặc tính của khối bậc hai khi đầu vào là sóng sin: (a) biên độ và (b) pha. (Từ P. H. Sydenham, Handbook of Measurement Science, Vol. 2, Chichester, U.K., John Wiley & Sons, 1983. Được phép sử dụng.)",
                "Figure 3.17 · These two plots allow the behavior of second-order blocks with sine-wave inputs to be ascertained: (a) amplitude and (b) phase. (From P. H. Sydenham, Handbook of Measurement Science, Vol. 2, Chichester, U.K., John Wiley & Sons, 1983. With permission.)",
                "Đỉnh cộng hưởng ở tần số riêng và pha chuyển từ 0 tới –180 độ",
                "Resonance peak at natural frequency and phase going to minus 180 degrees")


# ---------------------------------------------------------------- 3.18
def fig_3_18():
    o = []
    # constant head tank
    o.append('<rect x="40" y="40" width="150" height="86" fill="#fff" stroke="#2a2a2a" stroke-width="1.6"/>')
    o.append('<path d="M40 78 H190" stroke="#2a2a2a" stroke-width="1"/>')
    o.append('<rect x="40" y="78" width="150" height="48" fill="#eef4f8" stroke="none"/>')
    o.append('<path d="M150 40 V26 H196 V40" fill="none" stroke="#2a2a2a" stroke-width="1.2"/>')
    o.append('<text class="ts" x="200" y="34">tràn (mức không đổi)</text>')
    o.append('<text class="ts" x="52" y="150">bình cấp, mức không đổi</text>')
    # pipe to meter
    o.append('<path d="M190 104 H244" stroke="#2a2a2a" stroke-width="2"/>')
    o.append('<rect x="244" y="90" width="68" height="28" fill="#fff" stroke="#2a2a2a" stroke-width="1.4"/>')
    o.append('<text class="ts" x="278" y="108" text-anchor="middle">lưu lượng kế</text>')
    o.append('<path d="M312 104 H352" stroke="#2a2a2a" stroke-width="2"/>')
    # diverter
    o.append('<circle cx="352" cy="104" r="4" fill="#2a2a2a"/>')
    o.append('<path d="M352 104 L392 74" stroke="#2a2a2a" stroke-width="2"/>')
    o.append('<text class="ts" x="386" y="142" text-anchor="end">bộ chuyển dòng</text>')
    # weigh tank
    o.append('<rect x="392" y="120" width="120" height="86" fill="#fff" stroke="#2a2a2a" stroke-width="1.6"/>')
    o.append('<rect x="392" y="160" width="120" height="46" fill="#eef4f8" stroke="none"/>')
    o.append('<text class="ts" x="452" y="222" text-anchor="middle">bình cân + cân</text>')
    # return line
    o.append('<path d="M512 168 H536 V60 H120 V40" fill="none" stroke="#888" stroke-width="1.2" stroke-dasharray="5 4"/>')
    o.append('<text class="ts" x="300" y="52">hoàn lưu về bình cấp</text>')
    o.append('<text class="tb" x="278" y="264" text-anchor="middle">Q = khối lượng nước / thời gian → so với chỉ thị của lưu lượng kế</text>')
    return _fig(svg(560, 280, "".join(o), "Sơ đồ hiệu chuẩn lưu lượng kế bằng bình cân"),
                "Hình 3-18 · Ví dụ thực tế này minh hoạ cách hiệu chuẩn lưu lượng kế bằng cách cho một lượng chất lưu đã biết chảy qua đồng hồ trong một khoảng thời gian xác định. (Công bố lần đầu trong P. H. Sydenham, Transducers in Measurement and Control, Adam Hilger, Bristol, IOP Publishing, Bristol, 1984. Bản quyền P. H. Sydenham.)",
                "Figure 3.18 · This practical example illustrates how flow meters are calibrated by passing a known quantity of fluid through the meter over a given time. (Originally published in P. H. Sydenham, Transducers in Measurement and Control, Adam Hilger, Bristol, IOP Publishing, Bristol, 1984. Copyright P. H. Sydenham.)",
                "Sơ đồ bình cấp tràn, lưu lượng kế, bộ chuyển dòng và bình cân",
                "Rig with constant-head tank, flow meter, diverter and weigh tank")


# ---------------------------------------------------------------- 4.1
def fig_4_1():
    b = Box(560, 240, (-4, 4), (0, 0.45), pad=(46, 18, 20, 40))
    body = b.axes("X (đơn vị độ lệch chuẩn)", "mật độ xác suất",
                  xt=[(-3, "–3σ"), (-2, "–2σ"), (-1, "–1σ"), (0, "µ"), (1, "+1σ"), (2, "+2σ"), (3, "+3σ")],
                  yt=[(0, "0")])
    def pdf(x):
        return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)

    band = [(-1 + i / 40.0, pdf(-1 + i / 40.0)) for i in range(0, 81)]
    d = "M%s %s " % (_f(b.x(-1)), _f(b.y(0)))
    d += " ".join("L%s %s" % (_f(b.x(x)), _f(b.y(y))) for x, y in band)
    d += " L%s %s Z" % (_f(b.x(1)), _f(b.y(0)))
    body += '<path d="%s" fill="#f6e6c8" stroke="none"/>' % d
    body += b.curve([(x / 20.0, pdf(x / 20.0)) for x in range(-80, 81)], "c1")
    for s in (-2, -1, 1, 2):
        body += '<line class="d1" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
            _f(b.x(s)), _f(b.y(0)), _f(b.x(s)), _f(b.y(pdf(s))))
    body += '<line class="d1" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
        _f(b.x(0)), _f(b.y(0)), _f(b.x(0)), _f(b.y(0.399)))
    body += b.label(1.12, 0.27, "68,3 % trong ±1σ")
    body += b.label(2.15, 0.10, "95 % trong ±2σ")
    return _fig(svg(560, 240, body, "Phân bố chuẩn của sai số đo"),
                "Hình 4-1 · Phân bố chuẩn của sai số: 68,3 % các giá trị nằm trong ±1σ, 95 % trong ±2σ và 99,7 % trong ±3σ.",
                "Figure 4.1 · The normal distribution of error: 68.3 % of values lie within ±1σ, 95 % within ±2σ and 99.7 % within ±3σ.",
                "Đường cong phân bố chuẩn có vùng tô trong khoảng ±2σ",
                "Normal curve with the plus or minus two sigma band shaded")


# ---------------------------------------------------------------- 4.2
def fig_4_2():
    b = Box(560, 220, (-4, 4), (0, 0.30), pad=(46, 18, 20, 40))
    body = b.axes("X", "mật độ xác suất",
                  xt=[(-3, "–L"), (0, "µ"), (3, "+L")], yt=[(0, "0")])
    body += '<rect x="%s" y="%s" width="%s" height="%s" fill="#f6e6c8" stroke="#2a2a2a" stroke-width="1.4"/>' % (
        _f(b.x(-3)), _f(b.y(0.1667)), _f(b.x(3) - b.x(-3)), _f(b.y(0) - b.y(0.1667)))
    body += b.label(0.15, 0.19, "1/(2L) — mọi giá trị trong ±L đều có xác suất như nhau")
    body += b.label(0.15, 0.13, "σ = L/√3", "ts")
    return _fig(svg(560, 220, body, "Phân bố đều của sai số"),
                "Hình 4-2 · Phân bố đều (hình chữ nhật): mọi giá trị trong khoảng ±L đều có xác suất như nhau, và độ lệch chuẩn bằng L/√3.",
                "Figure 4.2 · The uniform (rectangular) distribution: every value within ±L is equally likely, and the standard deviation is L/√3.",
                "Hình chữ nhật phẳng giữa trừ L và cộng L",
                "Flat rectangular density between minus L and plus L")
