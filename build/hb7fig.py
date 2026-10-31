# -*- coding: utf-8 -*-
"""Vector figures for Handbook Chapter 7 — Thickness Measurement.

The source chapter carries three tables and no figures at all, so every
diagram here is drawn to show the principle the text describes.  Curves are
computed from the relation named in the caption — nothing is sketched.

Every function returns (svg, caption_vi, caption_en, aria_vi, aria_en).
"""
import math

from hbfig import Box, INK, TXT, MUTED, GOLD, _f, _box, svg, _fig

BLUE = "#2f5d8a"
RED = "#a8322d"
GREEN = "#3f6b47"
SAND = "#f6f3ec"
BAND = "#eef2f6"

MYSTYLE = ('<style>'
           '.p7h{font:9.4px Inter,Helvetica,sans-serif;fill:#111;font-weight:600}'
           '.p7t{font:9.2px Inter,Helvetica,sans-serif;fill:#111}'
           '.p7s{font:8.4px Inter,Helvetica,sans-serif;fill:#555}'
           '.p7k{font:8.6px Inter,Helvetica,sans-serif;fill:#444}'
           '</style>')


# ---------------------------------------------------------------- primitives

def _txt(x, y, s, fs=9.2, anchor="start", fill=TXT, bold=False):
    w = "font-weight:600;" if bold else ""
    return ('<text x="%s" y="%s" text-anchor="%s" style="font:%spx Inter,Helvetica,sans-serif;%s'
            'fill:%s">%s</text>' % (_f(x), _f(y), anchor, fs, w, fill, s))


def _line(x1, y1, x2, y2, w=1.1, color=INK, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), color, w, d))


def _arrow(x1, y1, x2, y2, w=1.1, color=INK, head=5.0):
    o = [_line(x1, y1, x2, y2, w=w, color=color)]
    a = math.atan2(y2 - y1, x2 - x1)
    for s in (0.42, -0.42):
        o.append(_line(x2, y2, x2 - head * math.cos(a - s), y2 - head * math.sin(a - s),
                       w=w, color=color))
    return "".join(o)


def _dim(x1, y1, x2, y2, w=0.9, color=MUTED):
    """A dimension line with an arrowhead at each end."""
    return (_arrow(x1, y1, x2, y2, w=w, color=color, head=4.2)
            + _arrow(x2, y2, x1, y1, w=w, color=color, head=4.2))


def _rect(x, y, w, h, fill="#fff", color=INK, sw=1.1, dash="", r=0):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"%s/>'
            % (_f(x), _f(y), _f(w), _f(h), _f(r), fill, color, sw, d))


def _circle(cx, cy, r, fill="none", color=INK, sw=1.1, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(cx), _f(cy), _f(r), fill, color, sw, d))


def _panel(x, y, w, h, header, lines, fs=8.8, fill=SAND, color=INK, dash=""):
    """A titled box with left-aligned lines.  A line may be (text, "b") to go bold."""
    o = [_rect(x, y, w, h, fill=fill, color=color, dash=dash)]
    if header:
        o.append(_txt(x + 8, y + 14.5, header, 9.0, fill=TXT, bold=True))
    cy = y + (30 if header else 15)
    for ln in lines:
        txt, wt = ln if isinstance(ln, tuple) else (ln, "")
        o.append(_txt(x + 8, cy, txt, fs, fill=TXT, bold=(wt == "b")))
        cy += fs + 5.2
    return "".join(o)


def _plot(box, fn, n=241, xr=(0.0, 1.0), ylim=None, color=INK, sw=1.8, dash="", closed=False):
    """Sample fn(x); drop samples outside ylim and break the path there."""
    segs, cur = [], []
    for i in range(n):
        x = xr[0] + (xr[1] - xr[0]) * i / (n - 1.0)
        y = fn(x)
        if y is None or (ylim is not None and not (ylim[0] <= y <= ylim[1])):
            if len(cur) > 1:
                segs.append(cur)
            cur = []
            continue
        cur.append((x, y))
    if len(cur) > 1:
        segs.append(cur)
    d = "".join("M" + " L".join("%s %s" % (_f(box.x(a)), _f(box.y(b))) for a, b in s)
                for s in segs)
    da = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="%s" '
            'stroke-linejoin="round"%s/>' % (d, color, sw, da))


def _key(x, y, items, gap=16):
    """Horizontal colour key: items are (colour, dash, label)."""
    o, cx = [], x
    for col, dash, lab in items:
        o.append(_line(cx, y, cx + 15, y, w=1.8, color=col, dash=dash))
        o.append(_txt(cx + 19, y + 3.2, lab, 8.6, fill="#444"))
        cx += 19 + 4.6 * len(lab) + gap
    return "".join(o)


def _sup(s, fs="6.6"):
    """Superscript inside a <text>; the trailing dy puts the cursor back on the line."""
    return '<tspan dy="-3.2" font-size="%s">%s</tspan><tspan dy="3.2">\u200b</tspan>' % (fs, s)


def _sub(s, fs="6.6"):
    return '<tspan dy="2.6" font-size="%s">%s</tspan><tspan dy="-2.6">\u200b</tspan>' % (fs, s)


def _svg(w, h, body, title):
    return svg(w, h, MYSTYLE + body, title)


# ---------------------------------------------------------------- 7.1
def fig_7_1():
    """The thickness scale, as a row chart on a log axis."""
    W, H = 560, 268
    X0, X1 = 152.0, 502.0
    lo, hi = -9.0, 21.0

    def px(v):
        return X0 + (v - lo) * (X1 - X0) / (hi - lo)

    rows = [("Thiên hà", 20.0, "10²⁰ m"),
            ("Hệ Mặt Trời", 12.0, "10¹² m"),
            ("Khí quyển", 4.60, "4·10⁴ m"),
            ("Vỏ Trái Đất", 4.54, "3,5·10⁴ m"),
            ("Vành Sao Thổ", 4.00, "10⁴ m"),
            ("Đại dương", 3.59, "3,9·10³ m"),
            ("Vi hoá thạch Sao Hoả", -7.20, "< 10⁻⁷ m")]

    o = [_rect(px(-9), 32, px(0) - px(-9), 186, fill=BAND, color="none", sw=0)]
    ticks = [(-8, "10⁻⁸"), (-4, "10⁻⁴"), (0, "1"), (4, "10⁴"),
             (8, "10⁸"), (12, "10¹²"), (16, "10¹⁶"), (20, "10²⁰")]
    for v, _lab in ticks:
        o.append(_line(px(v), 32, px(v), 218, w=0.8, color="#dcdcdc"))
    o.append(_txt(X1, 24, "chiều dày, thang logarit (m)", 8.6, anchor="end", fill=MUTED))

    y = 48.0
    for name, v, lab in rows:
        o.append(_txt(8, y + 3.4, name, 9.2, fill=TXT))
        o.append(_circle(px(v), y, 3.4, fill=INK, color=INK))
        o.append(_txt(px(v) + 8, y + 3.4, lab, 8.6, fill="#444"))
        y += 25.0

    o.append(_line(X0, 218, X1, 218, w=1.2))
    for v, lab in ticks:
        o.append(_line(px(v), 218, px(v), 223, w=1.1))
        o.append(_txt(px(v), 233, lab, 8.4, anchor="middle", fill="#444"))

    bx0, bx1 = px(-9), px(0)
    o.append(_line(bx0, 242, bx1, 242, w=0.9, color=MUTED))
    o.append(_line(bx0, 242, bx0, 238, w=0.9, color=MUTED))
    o.append(_line(bx1, 242, bx1, 238, w=0.9, color=MUTED))
    o.append(_txt((bx0 + bx1) / 2.0, 256, "dải công nghiệp: m → nm", 8.4,
                  anchor="middle", fill=MUTED))

    return _fig(_svg(W, H, "".join(o),
                     "Biểu đồ thang logarit chiều dày, từ 10 mũ trừ mười mét tới 10 mũ hai mươi mét"),
                "Hình 7-1. Chiều dày trong tự nhiên và trong công nghiệp, xếp theo thang logarit. "
                "Dải tô xám là khoảng mà ngành chế tạo phải xử lý — từ mét ở công trình xây dựng "
                "xuống tới nanomet ở lớp phủ quang học.",
                "Figure 7-1. Thickness from the cosmic to the nanoscale on a log axis. The shaded "
                "band is the range industry actually works in.",
                "Biểu đồ hàng ngang, trục hoành logarit từ 10 mũ trừ chín tới 10 mũ hai mươi mốt mét. "
                "Bảy hàng: thiên hà 10 mũ hai mươi, hệ Mặt Trời 10 mũ mười hai, khí quyển bốn nhân "
                "10 mũ bốn, vỏ Trái Đất ba phẩy năm nhân 10 mũ bốn, vành Sao Thổ 10 mũ bốn, đại dương "
                "ba phẩy chín nhân 10 mũ ba, vi hoá thạch Sao Hoả dưới 10 mũ trừ bảy. Dải từ 1 m xuống "
                "10 mũ trừ chín được tô sáng và ghi là dải công nghiệp.",
                "Row chart on a logarithmic axis from 10 to the minus nine up to 10 to the twenty-first "
                "metre. Seven rows: galaxy 10^20, solar system 10^12, atmosphere 4x10^4, Earth's crust "
                "3.5x10^4, Saturn's rings 10^4, ocean 3.9x10^3, Martian microfossils below 10^-7. The "
                "band from 1 m down to 10^-9 m is shaded and labelled the industrial range.")


# ---------------------------------------------------------------- 7.2
def fig_7_2():
    """Why a caliper is not always the answer."""
    W, H = 560, 248
    o = []
    o.append(_box(12, 96, 112, 46, ["Đo chiều dày"], fs=9.4))
    o.append(_arrow(124, 119, 160, 119))
    o.append(_panel(162, 88, 132, 62, "Hai mặt đều",
                    ["tiếp cận được?"], fill="#fff", dash="5 4"))

    o.append(_arrow(294, 104, 344, 64))
    o.append(_panel(346, 26, 202, 62, "CÓ — đo trực tiếp",
                    ["thước, calip, panme", "LVDT, khí nén, quang học"], fs=8.6))

    o.append(_arrow(294, 134, 344, 166))
    o.append(_panel(346, 126, 202, 108, "KHÔNG — đo gián tiếp",
                    ["vật quá lớn hoặc quá nhỏ", "vật dễ vỡ, không chịu tiếp xúc",
                     "quá nóng hoặc quá lạnh", "đang chạy trên dây chuyền",
                     "một mặt bị che, hoặc không rắn"], fs=8.4))

    return _fig(_svg(W, H, "".join(o),
                     "Sơ đồ quyết định: khi nào dùng được dụng cụ tiếp xúc, khi nào phải đo gián tiếp"),
                "Hình 7-2. Bốn lý do buộc phải bỏ thước cặp. Chúng không phải ngoại lệ hiếm — trên "
                "dây chuyền sản xuất chúng là trường hợp thường gặp, và đó là lý do cả một ngành "
                "công cụ đo không tiếp xúc tồn tại.",
                "Figure 7-2. Four reasons a caliper will not do — the everyday case on a production "
                "line, not an exotic exception.",
                "Sơ đồ khối ba cột. Bên trái là ô Đo chiều dày, mũi tên sang ô câu hỏi Hai mặt đều "
                "tiếp cận được. Nhánh CÓ dẫn tới nhóm dụng cụ tiếp xúc trực tiếp: thước, calip, panme, "
                "LVDT, khí nén, quang học. Nhánh KHÔNG dẫn tới nhóm đo gián tiếp, kèm năm lý do: vật "
                "quá lớn hoặc quá nhỏ, dễ vỡ, quá nóng hoặc quá lạnh, đang chuyển động, một mặt bị che.",
                "Three-column block diagram. Left box Measure thickness leads to the question Are both "
                "faces accessible. The YES branch lists direct-contact instruments; the NO branch lists "
                "indirect methods with five reasons: too large or small, fragile, too hot or cold, "
                "moving, one face hidden.")


# ---------------------------------------------------------------- 7.3
def fig_7_3():
    """Reading a micrometer: 0.5 mm pitch over 50 thimble divisions."""
    W, H = 560, 254
    o = []
    x0, x1 = 40.0, 424.0
    pxmm = (x1 - x0) / 4.0

    o.append(_rect(x0, 58, x1 - x0, 30, fill="#f4f1e8"))
    o.append(_line(x0, 73, x1, 73, w=1.3))
    for k in range(9):
        v = k * 0.5
        x = x0 + v * pxmm
        if k % 2 == 0:
            o.append(_line(x, 58, x, 70, w=1.1))
            o.append(_txt(x, 52, "%d" % v, 8.6, anchor="middle", fill="#444"))
        else:
            o.append(_line(x, 58, x, 66, w=1.0))
            o.append(_txt(x, 52, _f(v).replace(".", ","), 7.4, anchor="middle", fill=MUTED))

    xe = x0 + 3.78 * pxmm
    o.append(_line(xe, 44, xe, 96, w=1.4, color=RED))
    o.append(_txt(xe + 5, 44, "mép thimble", 8.4, fill=RED))

    # thimble dial
    cx, cy, r = 148.0, 176.0, 54.0
    o.append(_circle(cx, cy, r, fill="#fbfaf6"))
    o.append(_circle(cx, cy, r - 11, fill="none", color="#d8d3c6", sw=0.8))
    for i in range(50):
        a = math.radians(-90.0 + 7.2 * i)
        long_t = (i % 5 == 0)
        r1 = r - (10 if long_t else 6)
        o.append(_line(cx + r1 * math.cos(a), cy + r1 * math.sin(a),
                       cx + r * math.cos(a), cy + r * math.sin(a),
                       w=0.9 if not long_t else 1.1))
        if long_t:
            o.append(_txt(cx + (r - 16) * math.cos(a), cy + (r - 16) * math.sin(a) + 2.6,
                          "%d" % i, 7.2, anchor="middle", fill="#444"))
    a = math.radians(-90.0 + 7.2 * 28)
    o.append(_line(cx + 13 * math.cos(a), cy + 13 * math.sin(a),
                   cx + 28 * math.cos(a), cy + 28 * math.sin(a), w=1.8, color=RED))
    o.append(_txt(cx, cy + 3.2, "28", 9.4, anchor="middle", fill=RED, bold=True))
    o.append(_txt(cx, 248, "thimble: 50 vạch", 8.4, anchor="middle", fill=MUTED))

    o.append(_panel(240, 118, 308, 116, "Đọc số trên panme",
                    ["bước ren 0,5 mm ÷ 50 vạch = 0,01 mm/vạch",
                     "thước ống:  7,5 mm",
                     "thimble:  28 × 0,01 = 0,28 mm",
                     ("tổng:  7,78 mm", "b")], fs=8.8))

    return _fig(_svg(W, H, "".join(o),
                     "Sơ đồ đọc số panme: thước ống chia nửa milimét, thimble chia năm mươi vạch"),
                "Hình 7-3. Panme đọc được tới 0,01 mm vì bước ren 0,5 mm được chia thành 50 vạch "
                "trên thimble. Đây là lý do một dụng cụ cơ khí thuần tuý vẫn chính xác hơn thước cặp "
                "có du xích.",
                "Figure 7-3. A micrometer reads to 0.01 mm because a 0.5 mm screw pitch is divided "
                "into fifty thimble graduations.",
                "Hình trên là thước ống nằm ngang chia vạch mỗi nửa milimét từ 0 tới 4, mép thimble đứng "
                "ở 3,78 mm. Hình dưới là mặt thimble chia 50 vạch, kim chỉ vạch 28. Khung bên phải ghi "
                "cách tính: 0,5 chia 50 bằng 0,01 mm mỗi vạch, cộng 7,5 với 0,28 được 7,78 mm.",
                "Top: a horizontal sleeve scale graduated every half millimetre from 0 to 4, with the "
                "thimble edge at 3.78 mm. Bottom: a fifty-division thimble dial with the pointer on 28. "
                "The box at right shows the arithmetic: 0.5 divided by 50 is 0.01 mm per division, and "
                "7.5 plus 0.28 gives 7.78 mm.")


# ---------------------------------------------------------------- 7.4
def fig_7_4():
    """LVDT: schematic plus the differential transfer curve."""
    W, H = 560, 252
    o = []
    # core first, then the windings as open frames drawn over it
    o.append(_rect(138, 46, 14, 148, fill="#c9c2b4", color="#8a8375"))
    for yy, lab in ((58, "S₁"), (100, "P"), (142, "S₂")):
        o.append(_rect(100, yy, 96, 34, fill="none"))
        o.append(_txt(116, yy + 21, lab, 10, anchor="middle", fill=TXT, bold=True))
    o.append(_line(145, 46, 145, 30, w=1.2))
    o.append(_rect(129, 20, 32, 10, fill="#e6e0d4"))
    o.append(_txt(145, 16, "đầu đo", 8.0, anchor="middle", fill=MUTED))

    o.append(_dim(86, 58, 86, 176, color=MUTED))
    o.append(_txt(78, 120, "x", 10, anchor="middle", fill=TXT, bold=True))

    g = ['<g transform="translate(248,0)">']
    b = Box(312, 252, (-1.5, 1.5), (-1.0, 1.0), pad=(38, 26, 12, 38))
    g.append(b.axes("dịch chuyển lõi  x", "V" + _sub("out"),
                    xt=[(-1, "-1"), (-0.5, "-0,5"), (0, "0"), (0.5, "0,5"), (1, "1")],
                    yt=[(-1, "-1"), (-0.5, "-0,5"), (0, "0"), (0.5, "0,5"), (1, "1")]))

    def V(x):
        return math.exp(-((x - 0.5) / 0.62) ** 2) - math.exp(-((x + 0.5) / 0.62) ** 2)

    g.append(_plot(b, V, n=241, xr=(-1.5, 1.5), ylim=(-1.0, 1.0), color=INK, sw=1.9))
    g.append(b.label(-1.40, 0.74, "V = S₁ − S₂", "p7s", anchor="start"))
    g.append(b.label(0.0, -0.92, "tuyến tính", "p7s", anchor="middle"))
    g.append(b.label(1.45, 0.55, "bão hoà", "p7s", anchor="end"))
    g.append("</g>")
    o.append("".join(g))

    return _fig(_svg(W, H, "".join(o),
                     "Sơ đồ LVDT và đường cong truyền đạt hiệu số hai cuộn thứ cấp"),
                "Hình 7-4. LVDT: lõi sắt dịch chuyển làm thay đổi hỗ cảm với hai cuộn thứ cấp đấu "
                "ngược chiều. Hiệu số của chúng triệt tiêu đúng tại vị trí không, tuyến tính ở giữa "
                "và bão hoà ở hai đầu — nên đây là cảm biến dịch chuyển chứ không phải cảm biến "
                "khoảng cách.",
                "Figure 7-4. An LVDT: the core shifts the coupling to two opposing secondaries. Their "
                "difference is zero at null, linear in the middle, and saturates at the ends.",
                "Bên trái là mặt cắt LVDT: một cuộn sơ cấp P ở giữa, hai cuộn thứ cấp S một và S hai "
                "ở trên và dưới, lõi sắt chạy dọc qua cả ba, đầu đo nối với lõi. Bên phải là đồ thị "
                "điện áp ra theo dịch chuyển lõi: đường cong chữ S, bằng không tại gốc, tuyến tính "
                "trong khoảng cộng trừ 0,4, bão hoà ở hai đầu.",
                "Left: an LVDT cross-section with a primary winding in the middle, secondaries above "
                "and below, and an iron core sliding through all three. Right: output voltage against "
                "core displacement, an S-curve that is zero at null, linear within about plus or minus "
                "0.4, and saturating at the ends.")


# ---------------------------------------------------------------- 7.5
def fig_7_5():
    """Pneumatic backpressure against nozzle gap."""
    W, H = 560, 250
    b = Box(W, H, (0.0, 4.0), (0.0, 1.0), pad=(54, 24, 20, 42))
    o = [b.axes("khe hở  g / g₀", "áp suất ngược  P / P_s",
                xt=[(0, "0"), (1, "g₀"), (2, "2g₀"), (3, "3g₀"), (4, "4g₀")],
                yt=[(0, "0"), (0.25, "0,25"), (0.5, "0,5"), (0.75, "0,75"), (1, "1")])]

    def P(g):
        return 1.0 / (1.0 + g * g)

    o.append(_plot(b, P, n=241, xr=(0.0, 4.0), color=INK, sw=1.9))

    gm = 1.0 / math.sqrt(3.0)
    o.append(_line(b.x(gm), b.y(0), b.x(gm), b.y(0.75), w=0.9, color=BLUE, dash="4 3"))
    o.append(_circle(b.x(gm), b.y(0.75), 3.0, fill=BLUE, color=BLUE))
    o.append(_txt(b.x(gm) + 8, b.y(0.88), "độ nhạy cực đại", 8.4, fill=BLUE))
    o.append(_txt(b.x(gm) + 8, b.y(0.80), "tại g = g₀/√3", 8.4, fill=BLUE))

    o.append(_txt(b.x(2.6), b.y(0.20), "P / P" + _sub("s") + " = 1 / (1 + (g/g₀)²)", 9.0,
                  fill="#333"))

    return _fig(_svg(W, H, "".join(o),
                     "Đồ thị áp suất ngược của đầu đo khí nén theo khe hở, có đánh dấu điểm độ nhạy cực đại"),
                "Hình 7-5. Đo khí nén: áp suất dựng lại phía sau lỗ phun giảm theo bình phương khe hở. "
                "Độ nhạy dP/dg lớn nhất không phải ở khe hở bằng không mà ở g = g₀/√3 — nên đầu đo "
                "khí nén luôn được đặt làm việc lệch khỏi vị trí chạm.",
                "Figure 7-5. Pneumatic gauging: backpressure falls as the square of the gap. Peak "
                "sensitivity is at g = g0/root-3, not at zero gap, so the head is always biased away "
                "from contact.",
                "Đường cong giảm từ một tại khe hở bằng không xuống còn khoảng không phẩy không sáu ở "
                "khe hở bốn g không. Điểm độ nhạy cực đại được đánh dấu ở g bằng g không chia căn ba, "
                "tương ứng áp suất không phẩy bảy lăm, có đường chấm dọc dóng xuống trục hoành.",
                "A curve falling from one at zero gap to about 0.06 at four times g0. Peak sensitivity "
                "is marked at g equals g0 over root three, where the pressure is 0.75, with a dotted "
                "vertical dropping to the axis.")


# ---------------------------------------------------------------- 7.6
def fig_7_6():
    """Capacitance against dielectric thickness."""
    W, H = 560, 250
    b = Box(W, H, (0.25, 3.0), (0.0, 4.2), pad=(54, 24, 20, 44))
    o = [b.axes("chiều dày điện môi  d / d₀", "C / C₀",
                xt=[(0.5, "0,5d₀"), (1, "d₀"), (1.5, "1,5d₀"), (2, "2d₀"), (2.5, "2,5d₀"),
                    (3, "3d₀")],
                yt=[(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4")])]

    def C(d):
        return 1.0 / d

    o.append(_plot(b, C, n=241, xr=(0.25, 3.0), ylim=(0.0, 4.2), color=INK, sw=1.9))
    o.append(_txt(b.x(1.55), b.y(3.6), "C = ε₀·ε" + _sub("r") + "·A / d", 10, fill="#333"))
    o.append(_txt(b.x(1.55), b.y(3.2), "nên C ∝ 1/d", 8.6, fill=MUTED))
    o.append(_line(b.x(0.25), b.y(1.0), b.x(3.0), b.y(1.0), w=0.8, color=GREEN, dash="3 3"))
    o.append(_txt(b.x(2.05), b.y(1.12), "C₀ tại d = d₀", 8.2, fill=GREEN))
    o.append(_txt(b.x(0.27), b.y(4.05), "dưới micromet", 8.2, fill=RED))
    o.append(_arrow(b.x(0.30), b.y(3.95), b.x(0.34), b.y(3.55), w=0.9, color=RED, head=4))

    return _fig(_svg(W, H, "".join(o),
                     "Đồ thị điện dung theo chiều dày lớp điện môi, đường cong giảm theo nghịch đảo"),
                "Hình 7-6. Đo điện dung: vật liệu phi kim đặt vào điện trường đã biết làm thay đổi "
                "điện dung theo C = ε₀ε_r A/d. Vì quan hệ là nghịch đảo, độ nhạy tăng nhanh khi lớp "
                "mỏng đi — đây là kỹ thuật đo dưới micromet.",
                "Figure 7-6. Capacitive gauging: C = eps0 epsr A/d. The inverse relation means "
                "sensitivity climbs steeply as the layer thins, which is why sub-micron thickness is "
                "reachable.",
                "Đường cong giảm theo nghịch đảo chiều dày: tại d bằng không phẩy năm d không thì C "
                "gấp đôi C không, tại d bằng ba d không thì còn một phần ba. Đường chấm ngang đánh "
                "dấu mức C không tại d bằng d không. Mũi tên đỏ ghi chú vùng dưới micromet ở phía "
                "chiều dày nhỏ.",
                "The curve falls as the inverse of thickness: at half d0 the capacitance is twice C0, "
                "at three d0 it is one third. A dotted horizontal marks C0 at d equal to d0. A red "
                "arrow points to the sub-micron end.")


# ---------------------------------------------------------------- 7.7
def fig_7_7():
    """Eddy current: geometry on the left, lift-off response on the right."""
    W, H = 560, 252
    o = []

    o.append(_rect(28, 172, 196, 42, fill="#e6e0d4"))
    o.append(_txt(126, 198, "tấm dẫn điện", 8.8, anchor="middle", fill=TXT))
    o.append(_rect(28, 160, 196, 12, fill="#f2e7d0", color="#b9a97e"))
    o.append(_txt(232, 168, "lớp phủ", 8.2, fill=MUTED))

    o.append(_rect(86, 104, 84, 26, fill="#fff"))
    for k in range(6):
        o.append(_line(90 + k * 14, 106, 90 + k * 14, 128, w=1.0, color="#6b6b6b"))
    o.append(_txt(128, 98, "cuộn dò", 8.4, anchor="middle", fill=MUTED))

    o.append('<path d="M 96 130 C 96 150, 74 150, 74 160" fill="none" stroke="#8a8a8a" '
             'stroke-width="0.9" stroke-dasharray="4 3"/>')
    o.append('<path d="M 160 130 C 160 150, 182 150, 182 160" fill="none" stroke="#8a8a8a" '
             'stroke-width="0.9" stroke-dasharray="4 3"/>')
    o.append(_circle(80, 184, 9, fill="none", color=BLUE, sw=1.0, dash="2 2"))
    o.append(_circle(172, 184, 9, fill="none", color=BLUE, sw=1.0, dash="2 2"))
    o.append(_txt(96, 228, "dòng xoáy", 8.0, fill=BLUE))

    o.append(_line(86, 130, 58, 130, w=0.8, color=MUTED, dash="3 3"))
    o.append(_line(28, 160, 58, 160, w=0.8, color=MUTED, dash="3 3"))
    o.append(_dim(58, 130, 58, 160, color=RED))
    o.append(_txt(52, 148, "lift-off", 8.2, anchor="end", fill=RED))

    g = ['<g transform="translate(250,0)">']
    b = Box(310, 252, (0.0, 2.0), (0.0, 1.0), pad=(42, 26, 12, 40))
    g.append(b.axes("chiều dày lớp phủ (mm)", "tín hiệu  S / S₀",
                    xt=[(0, "0"), (0.5, "0,5"), (1, "1"), (1.5, "1,5"), (2, "2")],
                    yt=[(0, "0"), (0.5, "0,5"), (1, "1")]))
    g.append(_plot(b, lambda z: math.exp(-z / 0.55), n=241, xr=(0.0, 2.0),
                   color=INK, sw=1.9))
    g.append(b.label(0.62, 0.62, "S = S" + _sub("0") + "·e" + _sup("−z/zc"), "p7s",
                     anchor="start"))
    g.append("</g>")
    o.append("".join(g))

    return _fig(_svg(W, H, "".join(o),
                     "Sơ đồ cuộn dò dòng xoáy trên lớp phủ, kèm đường cong tín hiệu giảm theo lift-off"),
                "Hình 7-7. Dòng xoáy: lớp phủ phi dẫn tạo ra một khe hở — lift-off — giữa cuộn kích và "
                "dòng xoáy trong kim loại nền. Tín hiệu tắt dần theo hàm mũ, nên kỹ thuật này hợp với "
                "lớp phủ mỏng chứ không hợp với chiều dày lớn.",
                "Figure 7-7. Eddy current: a non-conducting coating creates lift-off between the "
                "exciting coil and the eddy currents in the substrate. The signal dies exponentially, "
                "which suits thin coatings and not thick sections.",
                "Bên trái là mặt cắt: cuộn dò nằm trên lớp phủ mỏng, dưới là tấm dẫn điện, hai vòng "
                "dòng xoáy vẽ bằng nét đứt xanh trong tấm, mũi tên đỏ ghi lift-off giữa cuộn và lớp "
                "phủ. Bên phải là đường cong tín hiệu giảm theo hàm mũ khi chiều dày lớp phủ tăng từ "
                "không tới hai milimét.",
                "Left: a cross-section with the probe coil above a thin coating, a conducting plate "
                "below, two dashed blue eddy-current loops inside the plate, and a red lift-off "
                "dimension. Right: signal falling exponentially as coating thickness runs from zero "
                "to two millimetres.")


# ---------------------------------------------------------------- 7.8
def fig_7_8():
    """Magnetic pull-off force against gap, on a log axis."""
    W, H = 560, 250
    b = Box(W, H, (0.0, 4.0), (-4.0, 0.0), pad=(56, 24, 20, 44))
    o = [b.axes("khe hở  z (mm)", "F / F₀  (thang log)",
                xt=[(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4")],
                yt=[(-4, "10⁻⁴"), (-3, "10⁻³"), (-2, "10⁻²"), (-1, "10⁻¹"), (0, "1")])]

    a = 0.35

    def F(z):
        return 1.0 / (1.0 + z / a) ** 4

    def Flog(z):
        return math.log10(F(z))

    o.append(_plot(b, Flog, n=241, xr=(0.0, 4.0), color=INK, sw=1.9))
    o.append(_txt(b.x(1.45), b.y(-0.85), "F / F₀ = 1 / (1 + z/a)⁴", 9.2, fill="#333"))
    o.append(_txt(b.x(1.45), b.y(-1.35), "a = 0,35 mm", 8.4, fill=MUTED))

    for zv in (0.35, 1.0, 2.0):
        o.append(_line(b.x(zv), b.y(-4.0), b.x(zv), b.y(Flog(zv)), w=0.8, color=GREEN, dash="3 3"))
        o.append(_circle(b.x(zv), b.y(Flog(zv)), 2.6, fill=GREEN, color=GREEN))

    return _fig(_svg(W, H, "".join(o),
                     "Đồ thị lực kéo của đầu dò từ tính giảm theo lũy thừa bậc bốn của khe hở, thang logarit"),
                "Hình 7-8. Cảm ứng từ: lớp phủ phi từ tách nền sắt từ ra khỏi đầu dò, và lực hút tắt "
                "rất nhanh — giảm một nghìn lần khi khe hở chỉ vào cỡ hai milimét. Đó là lý do tầm "
                "đo của phương pháp này dừng ở khoảng 4 mm.",
                "Figure 7-8. Magnetic induction: the non-magnetic coating lifts the ferromagnetic "
                "substrate away from the probe, and the force collapses — a thousandfold within about "
                "two millimetres. That is why the range stops near 4 mm.",
                "Đường cong giảm rất dốc trên thang logarit: tại khe hở không phẩy ba lăm milimét lực "
                "còn một phần mười sáu, tại một milimét còn khoảng hai phần nghìn, tại hai milimét "
                "còn khoảng năm phần mười nghìn. Ba điểm này được đánh dấu bằng chấm xanh và đường "
                "chấm dọc.",
                "A steeply falling curve on a log axis: at 0.35 mm the force is one sixteenth, at "
                "1 mm about two thousandths, at 2 mm about five hundred-thousandths. The three points "
                "are marked with green dots and dotted verticals.")


# ---------------------------------------------------------------- 7.9
def fig_7_9():
    """Hall-effect thickness gauge: the sandwich."""
    W, H = 560, 224
    o = []
    o.append(_rect(78, 34, 128, 52, fill="#f4f1e8"))
    o.append(_txt(142, 56, "đầu dò nam châm", 8.8, anchor="middle", fill=TXT))
    o.append(_rect(110, 62, 64, 16, fill="#fff"))
    o.append(_txt(142, 74, "phần tử Hall", 7.6, anchor="middle", fill=MUTED))

    o.append(_rect(56, 122, 172, 30, fill="#e6e0d4"))
    o.append(_txt(142, 141, "vật đo, kim loại không sắt", 8.6, anchor="middle", fill=TXT))

    o.append(_circle(142, 182, 22, fill="#c9c2b4", color="#8a8375"))
    o.append(_txt(142, 186, "bi thép", 7.8, anchor="middle", fill=TXT))

    for xx in (100, 184):
        o.append('<path d="M %d 86 C %d 104, %d 104, %d 122" fill="none" stroke="#8a8a8a" '
                 'stroke-width="0.9" stroke-dasharray="4 3"/>' % (xx, xx, xx, xx))
    for xx in (118, 166):
        o.append('<path d="M %d 152 C %d 162, %d 162, %d 170" fill="none" stroke="#8a8a8a" '
                 'stroke-width="0.9" stroke-dasharray="4 3"/>' % (xx, xx, xx, xx))

    o.append(_dim(244, 122, 244, 152, color=RED))
    o.append(_txt(250, 141, "chiều dày cần đo", 8.4, fill=RED))
    o.append(_txt(250, 122, "từ trường giảm", 8.2, fill=MUTED))

    o.append(_panel(366, 56, 182, 104, "Đặc điểm",
                    ["sai số khoảng 1 %", "tầm đo tới 10 mm",
                     "đo một phía, không cần mặt sau"], fs=8.4))

    return _fig(_svg(W, H, "".join(o),
                     "Sơ đồ đầu đo Hall: vật mẫu kẹp giữa đầu dò nam châm và một bi thép"),
                "Hình 7-9. Đo Hall: vật mẫu kẹp giữa đầu dò nam châm và một bi thép nhỏ ở mặt sau. "
                "Từ trường tại phần tử Hall giảm khi vật dày lên, nên đọc được chiều dày — nhưng phải "
                "tiếp cận được cả hai mặt, chỉ khác là mặt sau chỉ cần đặt một viên bi.",
                "Figure 7-9. Hall-effect gauge: the specimen is sandwiched between a magnetic probe "
                "and a small steel ball. The field at the Hall element falls as the specimen thickens.",
                "Mặt cắt thẳng đứng: trên cùng là đầu dò nam châm có phần tử Hall, giữa là vật đo bằng "
                "kim loại không sắt, dưới cùng là bi thép. Các đường chấm xám là từ trường đi từ đầu dò "
                "qua vật mẫu tới bi thép. Mũi tên đỏ bên phải đánh dấu chiều dày cần đo. Khung bên "
                "phải ghi sai số một phần trăm và tầm đo tới mười milimét.",
                "Vertical cross-section: a magnetic probe with a Hall element on top, the non-ferrous "
                "specimen in the middle, and a steel ball below. Grey dashed paths show the field "
                "running from probe through specimen to ball. A red dimension at right marks the "
                "thickness. The side box gives one percent accuracy and a ten millimetre range.")


# ---------------------------------------------------------------- 7.10
def fig_7_10():
    """Pulse-echo A-scan."""
    W, H = 560, 250
    b = Box(W, H, (0.0, 12.0), (0.0, 1.35), pad=(52, 26, 20, 44))
    o = [b.axes("thời gian (µs)", "biên độ echo",
                xt=[(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10"), (12, "12")],
                yt=[(0, "0"), (0.5, "0,5"), (1, "1")])]

    def env(t):
        s = 0.0
        for t0, amp, wid in ((0.30, 1.00, 0.10), (2.00, 0.92, 0.11), (4.00, 0.62, 0.13)):
            s += amp * math.exp(-((t - t0) / wid) ** 2)
        return s

    pts = [(0.0 + 12.0 * i / 400.0, env(0.0 + 12.0 * i / 400.0)) for i in range(401)]
    top = " L".join("%s %s" % (_f(b.x(t)), _f(b.y(min(v, 1.35)))) for t, v in pts)
    bot = " L".join("%s %s" % (_f(b.x(t)), _f(b.y(0.0))) for t, v in reversed(pts))
    o.append('<path d="M%s L%s Z" fill="#dfe7ef" stroke="none"/>' % (top, bot))
    o.append(_plot(b, env, n=401, xr=(0.0, 12.0), ylim=(0.0, 1.35), color=INK, sw=1.5))

    o.append(_txt(b.x(0.34), b.y(1.20), "xung phát", 8.2, fill=MUTED))
    o.append(_txt(b.x(2.12), b.y(1.08), "echo mặt trước", 8.2, fill=MUTED))
    o.append(_txt(b.x(4.30), b.y(0.78), "echo mặt sau", 8.2, fill=MUTED))

    o.append(_line(b.x(2.0), b.y(0.26), b.x(2.0), b.y(0.90), w=0.8, color=MUTED, dash="3 3"))
    o.append(_line(b.x(4.0), b.y(0.26), b.x(4.0), b.y(0.60), w=0.8, color=MUTED, dash="3 3"))
    o.append(_dim(b.x(2.0), b.y(0.30), b.x(4.0), b.y(0.30), color=RED))
    o.append(_txt(b.x(3.0), b.y(0.42), "Δt", 9.4, anchor="middle", fill=RED, bold=True))

    o.append(_txt(b.x(5.3), b.y(1.20), "d = c · Δt / 2", 10, fill="#333"))
    o.append(_txt(b.x(5.3), b.y(1.02), "thép c = 5.900 m/s, Δt = 2 µs → d = 5,9 mm", 8.2, fill=MUTED))

    return _fig(_svg(W, H, "".join(o),
                     "Ảnh A-scan của siêu âm xung phản hồi, hai echo cách nhau hai micro giây"),
                "Hình 7-10. Siêu âm xung – phản hồi: thời gian đi về chia đôi rồi nhân với vận tốc "
                "sóng cho chiều dày. Với thép, hai micro giây ứng với 5,9 mm — nên độ phân giải thời "
                "gian của thiết bị chính là độ phân giải chiều dày.",
                "Figure 7-10. Pulse-echo ultrasound: half the round-trip time times the sound speed is "
                "the thickness. In steel, two microseconds is 5.9 mm.",
                "Đường bao ba xung: xung phát ở 0,3 micro giây, echo mặt trước ở 2 micro giây với biên "
                "độ 0,92, echo mặt sau ở 4 micro giây với biên độ 0,62. Mũi tên đỏ hai chiều giữa hai "
                "echo ghi delta t. Góc trên bên phải ghi công thức d bằng c nhân delta t chia hai, kèm "
                "ví dụ thép với vận tốc 5.900 mét trên giây cho 5,9 milimét.",
                "Envelope of three pulses: transmit at 0.3 microseconds, front echo at 2 with "
                "amplitude 0.92, back echo at 4 with amplitude 0.62. A red double arrow between the "
                "echoes marks delta t. Top right gives d equals c delta t over two, with a steel "
                "example at 5900 metres per second giving 5.9 millimetres.")


# ---------------------------------------------------------------- 7.11
def fig_7_11():
    """Channeled transmission spectrum for two slab thicknesses."""
    W, H = 560, 250
    b = Box(W, H, (4000.0, 4800.0), (0.0, 1.05), pad=(54, 30, 20, 44))
    o = [_key(58, 14, [(INK, "", "d = 20 µm"), (GOLD, "6 4", "d = 40 µm")]),
         _txt(542, 14, "Δν̄ = 1 / (2nd) → 167 cm⁻¹ với d = 20 µm", 8.6, anchor="end",
              fill="#444"),
         b.axes("số sóng (cm⁻¹)", "độ truyền qua",
                xt=[(4000, "4000"), (4200, "4200"), (4400, "4400"),
                    (4600, "4600"), (4800, "4800")],
                yt=[(0, "0"), (0.5, "0,5"), (1, "1")])]

    n = 1.5
    F = 4.0

    def T(d):
        nd = n * d * 1e-6  # metres

        def f(nu):
            ph = 2.0 * math.pi * nd * (nu * 100.0)
            return 1.0 / (1.0 + F * math.sin(ph) ** 2)
        return f

    o.append(_plot(b, T(20.0), n=801, xr=(4000.0, 4800.0), color=INK, sw=1.5))
    o.append(_plot(b, T(40.0), n=1601, xr=(4000.0, 4800.0), color=GOLD, sw=1.2, dash="6 4"))

    return _fig(_svg(W, H, "".join(o),
                     "Phổ truyền qua có kênh của hai tấm trong suốt dày hai mươi và bốn mươi micromét"),
                "Hình 7-11. Giao thoa kế phổ: hai mặt song song của tấm trong suốt tạo ra cực đại và "
                "cực tiểu xen kẽ trong phổ truyền qua — gọi là hiệu ứng Fabry–Perot, và sự xuất hiện "
                "của chúng trong phổ gọi là kênh hoá. Khoảng cách giữa hai đỉnh cho chiều dày, miễn là "
                "biết chiết suất.",
                "Figure 7-11. Spectral interferometry: the two parallel faces of a transparent slab "
                "produce alternating maxima and minima in transmission — the Fabry–Perot effect, and "
                "its appearance in a spectrum is called channeling.",
                "Hai đường cong dao động đều: đường liền ứng với tấm dày hai mươi micromét, chu kỳ "
                "khoảng một trăm sáu mươi bảy xentimét nghịch đảo; đường nét đứt ứng với tấm dày bốn "
                "mươi micromét, chu kỳ chỉ còn một nửa. Cả hai dao động giữa không và một trên dải số "
                "sóng bốn nghìn tới bốn nghìn tám trăm xentimét nghịch đảo.",
                "Two evenly oscillating curves: the solid one is a twenty micrometre slab with a period "
                "of about 167 inverse centimetres; the dashed one is forty micrometres with half that "
                "period. Both swing between zero and one over the 4000 to 4800 inverse centimetre band.")


# ---------------------------------------------------------------- 7.12
def fig_7_12():
    """Newton's rings and the intensity profile they produce."""
    W, H = 560, 252
    o = []
    lam, R = 589e-9, 1.0

    cx, cy, rmax, mmax = 118.0, 142.0, 96.0, 3.2
    scale = rmax / mmax
    for m in range(15):
        rr = math.sqrt((m + 0.5) * lam * R) * 1000.0
        o.append(_circle(cx, cy, rr * scale, fill="none", color="#2a2a2a", sw=1.3))
    o.append(_txt(cx, 248, "λ = 589 nm · R = 1 m", 8.2, anchor="middle", fill=MUTED))

    g = ['<g transform="translate(232,0)">']
    b = Box(328, 252, (0.0, mmax), (0.0, 1.05), pad=(38, 26, 12, 44))
    g.append(_txt(b.x(3.15), 14, "r" + _sub("m") + " = √((m+½)λR)", 8.6, anchor="end",
                  fill="#444"))
    g.append(b.axes("bán kính r (mm)", "cường độ",
                    xt=[(0, "0"), (1, "1"), (2, "2"), (3, "3")],
                    yt=[(0, "0"), (0.5, "0,5"), (1, "1")]))

    def I(r):
        return math.sin(math.pi * (r * 1e-3) ** 2 / (lam * R)) ** 2

    g.append(_plot(b, I, n=801, xr=(0.0, mmax), color=INK, sw=1.4))
    g.append("</g>")
    o.append("".join(g))

    return _fig(_svg(W, H, "".join(o),
                     "Vân tròn Newton và đồ thị cường độ theo bán kính"),
                "Hình 7-12. Giao thoa kế không gian: tấm phẳng quang học đặt trên mặt cần đo, ánh sáng "
                "đơn sắc truyền qua. Mỗi vân là một đường đồng cao, và vân càng mau thì mặt càng dốc. "
                "Bán kính vân thứ m là √((m+½)λR), nên vân thưa dần ra phía ngoài.",
                "Figure 7-12. Spatial interferometry: an optical flat over the surface under test. Each "
                "ring is a contour of constant height; ring radius is root of (m + half) lambda R, so "
                "the rings crowd together near the centre.",
                "Bên trái là mười lăm vân tròn đồng tâm, thưa dần ra phía ngoài. Bên phải là đồ thị "
                "cường độ theo bán kính: dao động giữa không và một, các đỉnh cách nhau xa dần khi bán "
                "kính tăng, đúng như quy luật căn của m cộng một nửa nhân lambda nhân R.",
                "Left: fifteen concentric rings, spacing outwards. Right: intensity against radius, "
                "oscillating between zero and one with peaks that spread apart as radius grows, "
                "following the square root of m plus one half times lambda times R.")


# ---------------------------------------------------------------- 7.13
def fig_7_13():
    """Beta backscatter saturates; transmission dies away."""
    W, H = 560, 250
    b = Box(W, H, (0.0, 4.0), (0.0, 1.05), pad=(54, 30, 20, 44))
    o = [_key(58, 14, [(INK, "", "tán xạ ngược"), (GOLD, "6 4", "truyền qua")]),
         b.axes("chiều dày  x / (1/µ)", "cường độ tương đối",
                xt=[(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4")],
                yt=[(0, "0"), (0.5, "0,5"), (1, "1")])]

    o.append(_plot(b, lambda x: 1.0 - math.exp(-x), n=241, xr=(0.0, 4.0), color=INK, sw=1.9))
    o.append(_plot(b, lambda x: math.exp(-x), n=241, xr=(0.0, 4.0), color=GOLD, sw=1.5, dash="6 4"))

    o.append(_line(b.x(3.0), b.y(0.0), b.x(3.0), b.y(0.95), w=0.8, color=GREEN, dash="3 3"))
    o.append(_txt(b.x(3.05), b.y(0.90), "bão hoà", 8.4, fill=GREEN))
    o.append(_txt(b.x(2.0), b.y(0.22), "I = I" + _sub("0") + "·e" + _sup("−µx"), 9.2,
                  fill="#333"))

    return _fig(_svg(W, H, "".join(o),
                     "Đồ thị tán xạ ngược beta bão hoà và truyền qua beta tắt dần theo hàm mũ"),
                "Hình 7-13. Tán xạ ngược và truyền qua: cả hai đều là hàm mũ của chiều dày, nhưng "
                "ngược chiều nhau. Tán xạ ngược bão hoà — quá một độ dày nào đó thì dày thêm cũng "
                "không đổi tín hiệu, nên nó chỉ dùng được cho lớp mỏng. Truyền qua thì không bao giờ "
                "bão hoà, nên dùng được cho tấm dày.",
                "Figure 7-13. Backscatter and transmission are both exponential in thickness, but in "
                "opposite directions. Backscatter saturates, which limits it to thin layers; "
                "transmission never does, which suits plate.",
                "Hai đường cong: đường liền tăng từ không và tiến dần tới một, bão hoà sau khoảng ba "
                "đơn vị nghịch đảo hệ số hấp thụ; đường nét đứt giảm từ một xuống gần không. Đường "
                "chấm dọc màu xanh đánh dấu chỗ bão hoà.",
                "Two curves: the solid one rises from zero toward one and saturates after about three "
                "inverse attenuation lengths; the dashed one falls from one toward zero. A green "
                "dotted vertical marks the saturation point.")


# ---------------------------------------------------------------- 7.14
def fig_7_14():
    """AFM force against tip-sample separation, with the three scanning modes."""
    W, H = 560, 252
    b = Box(W, H, (0.35, 3.0), (-0.45, 1.30), pad=(56, 26, 20, 44))
    o = [b.axes("khoảng cách mũi – mẫu  z (nm)", "lực (đơn vị quy ước)",
                xt=[(0.5, "0,5"), (1, "1"), (1.5, "1,5"), (2, "2"), (2.5, "2,5"), (3, "3")],
                yt=[(-0.4, "−0,4"), (0, "0"), (0.4, "0,4"), (0.8, "0,8"), (1.2, "1,2")])]

    z0, A = 0.60, 0.25
    B = A * z0 ** 6

    def F(z):
        return -A / z ** 2 + B / z ** 8

    o.append(_plot(b, F, n=601, xr=(0.35, 3.0), ylim=(-0.45, 1.30), color=INK, sw=1.9))
    o.append(_line(b.x(z0), b.y(-0.45), b.x(z0), b.y(1.20), w=0.8, color=MUTED, dash="4 3"))
    o.append(_txt(b.x(z0) - 4, b.y(1.24), "z₀", 8.6, anchor="end", fill=MUTED))

    zmin = (4.0 * B / A) ** (1.0 / 6.0)
    o.append(_circle(b.x(zmin), b.y(F(zmin)), 3.0, fill=RED, color=RED))
    o.append(_txt(b.x(0.92), b.y(-0.30), "lực hút cực đại", 8.2, fill=RED))

    o.append(_txt(b.x(0.37), b.y(1.05), "tiếp xúc", 8.2, fill=BLUE))
    o.append(_txt(b.x(0.37), b.y(0.94), "(đẩy)", 8.2, fill=BLUE))
    o.append(_txt(b.x(0.70), b.y(0.72), "gián đoạn", 8.2, fill=GREEN))
    o.append(_txt(b.x(1.55), b.y(-0.20), "không tiếp xúc (hút)", 8.2, fill=MUTED))

    return _fig(_svg(W, H, "".join(o),
                     "Đường cong lực theo khoảng cách của kính hiển vi lực nguyên tử, chia ba vùng quét"),
                "Hình 7-14. AFM: lực giữa mũi dò và mẫu đổi dấu tại z₀. Bên trái là vùng đẩy — quét "
                "kiểu tiếp xúc; quanh z₀ là vùng gián đoạn; bên phải là vùng hút của van der Waals — "
                "quét kiểu không tiếp xúc. Ba chế độ không phải ba thiết bị khác nhau, mà là ba điểm "
                "làm việc trên cùng một đường cong.",
                "Figure 7-14. AFM: the tip-sample force changes sign at z0. Repulsive to the left "
                "(contact mode), attractive to the right (non-contact), intermittent around z0. The "
                "three modes are three operating points on one curve.",
                "Đường cong cắt trục hoành tại z không bằng không phẩy sáu nanomét: phía trái dốc đứng "
                "và dương, phía phải âm, đạt cực tiểu khoảng âm không phẩy ba ba tại z khoảng không "
                "phẩy bảy lăm nanomét rồi tiến dần về không. Ba nhãn ghi vùng tiếp xúc, vùng gián đoạn "
                "và vùng không tiếp xúc.",
                "The curve crosses zero at z0 of 0.6 nanometres: steep and positive to the left, "
                "negative to the right, reaching a minimum near minus 0.33 at about 0.75 nanometres "
                "before decaying toward zero. Labels mark the contact, intermittent and non-contact "
                "regions.")


# ---------------------------------------------------------------- 7.15
def fig_7_15():
    """STM tunnelling current against gap, from the barrier height."""
    W, H = 560, 250
    b = Box(W, H, (0.0, 0.60), (-4.0, 0.0), pad=(56, 24, 20, 46))
    o = [b.axes("khoảng cách mũi – mẫu  z (nm)", "I / I₀  (thang log)",
                xt=[(0, "0"), (0.1, "0,1"), (0.2, "0,2"), (0.3, "0,3"),
                    (0.4, "0,4"), (0.5, "0,5"), (0.6, "0,6")],
                yt=[(-4, "10⁻⁴"), (-3, "10⁻³"), (-2, "10⁻²"), (-1, "10⁻¹"), (0, "1")])]

    # kappa = sqrt(2 m phi) / hbar, with phi = 4.0 eV
    m_e, e, hbar = 9.1093837e-31, 1.602176634e-19, 1.054571817e-34
    phi = 4.0 * e
    kappa = math.sqrt(2.0 * m_e * phi) / hbar       # m^-1
    kappa_A = kappa * 1e-10                         # per angstrom

    def I(z):
        return -2.0 * kappa_A * (z * 10.0) / math.log(10.0)

    o.append(_plot(b, I, n=241, xr=(0.0, 0.60), ylim=(-4.0, 0.0), color=INK, sw=1.9))

    dec = math.log(10.0) / (2.0 * kappa_A)          # angstroms per decade
    o.append(_txt(b.x(0.02), b.y(-2.35), "I = I" + _sub("0") + "·e" + _sup("−2κz"), 9.6,
                  fill="#333"))
    o.append(_txt(b.x(0.02), b.y(-2.75), "φ = 4 eV → κ = %.2f Å⁻¹" % kappa_A, 8.4, fill=MUTED))
    o.append(_txt(b.x(0.02), b.y(-3.15), "mười lần mỗi %.1f Å" % dec, 8.4, fill=RED))

    return _fig(_svg(W, H, "".join(o),
                     "Đồ thị dòng tunnel của STM giảm theo hàm mũ khi khoảng cách tăng, thang logarit"),
                "Hình 7-15. STM: dòng tunnel tắt theo hàm mũ với khoảng cách, và hằng số tắt tính "
                "được từ chiều cao rào thế. Với φ = 4 eV, dòng giảm mười lần mỗi 1,1 Å — độ nhạy theo "
                "trục z này chính là thứ cho STM độ phân giải nguyên tử.",
                "Figure 7-15. STM: tunnelling current dies exponentially with gap, and the decay "
                "constant follows from the barrier height. At 4 eV the current drops tenfold every "
                "1.1 Å — that z-sensitivity is what buys atomic resolution.",
                "Đường thẳng dốc trên thang logarit, từ một tại khoảng cách không xuống mười mũ trừ bốn "
                "tại khoảng bốn phẩy năm nanomét. Hằng số tắt tính từ chiều cao rào thế bốn electron "
                "vôn cho một phẩy không hai nghịch ăngstrôm, tức dòng giảm mười lần mỗi một phẩy một "
                "ăngstrôm. Ba dòng chú thích nằm ở góc dưới bên trái, dưới đường cong.",
                "A steep straight line on a log axis, from one at zero gap to 10 to the minus four at "
                "about 4.5 nanometres. The decay constant computed from a 4 electron-volt barrier is "
                "1.02 inverse angstroms, so the current drops tenfold every 1.1 angstroms. Three "
                "annotation lines sit in the empty lower-left corner, below the curve.")


# ---------------------------------------------------------------- 7.16
def fig_7_16():
    """A 100 fs THz transient and its spectrum."""
    W, H = 560, 246
    o = []

    g1 = ['<g transform="translate(0,0)">']
    b1 = Box(280, H, (-400.0, 600.0), (-1.0, 1.0), pad=(42, 26, 10, 42))
    g1.append(b1.axes("thời gian (fs)", "E(t)",
                      xt=[(-400, "-400"), (0, "0"), (400, "400")],
                      yt=[(-1, "-1"), (0, "0"), (1, "1")]))
    tau = 100.0

    def E(t):
        return -2.0 * t / tau ** 2 * math.exp(-(t / tau) ** 2)

    peak = max(abs(E(t)) for t in range(-400, 601, 2))
    g1.append(_plot(b1, lambda t: E(t) / peak, n=601, xr=(-400.0, 600.0),
                    ylim=(-1.0, 1.0), color=INK, sw=1.7))
    g1.append(b1.label(240, -0.72, "τ = 100 fs", "p7s", anchor="start"))
    g1.append("</g>")
    o.append("".join(g1))

    g2 = ['<g transform="translate(288,0)">']
    b2 = Box(272, H, (0.0, 4.0), (0.0, 1.0), pad=(38, 26, 10, 42))
    g2.append('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="none"/>'
              % (_f(b2.x(0.1)), _f(b2.y(1.0)), _f(b2.x(3.0) - b2.x(0.1)),
                 _f(b2.y(0.0) - b2.y(1.0)), "#eef2f6"))
    g2.append(b2.axes("tần số (THz)", "|E(f)|",
                      xt=[(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4")],
                      yt=[(0, "0"), (0.5, "0,5"), (1, "1")]))

    def S(f):
        fHz = f * 1e12
        return (math.pi * fHz * tau * 1e-15) * math.exp(-(math.pi * fHz * tau * 1e-15) ** 2)

    pk = max(S(f / 100.0) for f in range(0, 401))
    g2.append(_plot(b2, lambda f: S(f) / pk, n=401, xr=(0.0, 4.0), color=INK, sw=1.7))
    g2.append(_txt(b2.x(1.05), b2.y(0.93), "0,1 – 3 THz", 8.2, fill=BLUE))
    g2.append("</g>")
    o.append("".join(g2))

    return _fig(_svg(W, H, "".join(o),
                     "Xung điện từ một chu kỳ dài một trăm femto giây và phổ tần số của nó"),
                "Hình 7-16. Công nghệ THz: laser xung femto giây kích một anten phát ra xung cỡ 100 fs, "
                "tương ứng dải 0,1–3 THz. Xung nhận được mang thông tin về hằng số điện môi và cả "
                "chiều dày của lớp vật liệu mà nó đi qua.",
                "Figure 7-16. THz technology: a femtosecond laser drives an antenna that emits a 100 fs "
                "transient, occupying 0.1 to 3 THz. The received pulse carries both the dielectric "
                "properties and the thickness of what it passed through.",
                "Hai khung: bên trái là xung một chu kỳ có dạng đạo hàm Gauss, đỉnh dương khoảng một "
                "trăm femto giây và đỉnh âm khoảng ba trăm femto giây; bên phải là phổ của nó, một "
                "đường cong lệch khỏi gốc, đạt đỉnh quanh hai phẩy hai lăm terahertz rồi tắt dần. Dải "
                "từ không phẩy một tới ba terahertz được tô sáng.",
                "Two panels: left, a single-cycle transient shaped as a Gaussian derivative with a "
                "positive peak near 100 femtoseconds and a negative one near 300; right, its spectrum, "
                "a curve rising from zero to a peak near 2.25 terahertz then decaying. The 0.1 to "
                "3 terahertz band is shaded.")
