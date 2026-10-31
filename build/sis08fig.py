# -*- coding: utf-8 -*-
"""Safety Instrumented Systems, Chapter 8 — Initial System Evaluation."""
import math

from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _box,
                  _circle, _line, _path, _poly, _rect, _txt)
from pcfig import _finish

DARKRED = "#7f1d1d"
AMBER = "#f6e0b8"
PALE_GREEN = "#dcecdc"
PALE_RED = "#f3d6d2"
PALE_BLUE = "#e8eef6"
PALE_GOLD = "#f7efdd"
EDGE = "#b9b3a4"


def _vtxt(x, y, s, size=7.0, color=GREY):
    """A text label rotated 90 degrees anticlockwise about (x, y)."""
    return ('<text x="%s" y="%s" text-anchor="middle" transform="rotate(-90 %s %s)" '
            'style="font:%spx Inter,Helvetica,sans-serif;fill:%s;">%s</text>'
            % (x, y, x, y, size, color, s))


def _wedge(cx, cy, r, a0, a1, fill, n=14, sw=0.9, color=EDGE):
    """A pie slice between two angles in degrees, measured anticlockwise from +x."""
    pts = [(cx, cy)]
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / float(n))
        pts.append((cx + r * math.cos(a), cy - r * math.sin(a)))
    return _poly(pts, fill=fill, sw=sw, color=color, close=True)


def _link(c1, r1, c2, r2, off, col, sw=1.3, dash=""):
    """An arrow from circle 1 to circle 2, shifted sideways by off pixels."""
    dx, dy = c2[0] - c1[0], c2[1] - c1[1]
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    ax, ay = c1[0] + ux * r1 + nx * off, c1[1] + uy * r1 + ny * off
    bx, by = c2[0] - ux * r2 + nx * off, c2[1] - uy * r2 + ny * off
    return _arrow(ax, ay, bx, by, sw=sw, color=col, dash=dash)


def _mid(c1, r1, c2, r2, off, k=0.5):
    dx, dy = c2[0] - c1[0], c2[1] - c1[1]
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    return (c1[0] + dx * k + nx * off, c1[1] + dy * k + ny * off)


# ---------------------------------------------------------------- 8.1
def fig_8_1():
    """The four failure modes: safe/dangerous crossed with detected/undetected."""
    cx, cy, r = 168, 148, 96
    o = [_txt(330, 20, "Bốn loại hư hỏng của một kênh an toàn", 8.2, weight="600")]

    o.append(_wedge(cx, cy, r, 90, 180, PALE_GREEN))
    o.append(_wedge(cx, cy, r, 0, 90, PALE_GOLD))
    o.append(_wedge(cx, cy, r, 180, 270, PALE_BLUE))
    o.append(_wedge(cx, cy, r, 270, 360, PALE_RED))
    o.append(_circle(cx, cy, r, fill="none", sw=1.1))
    o.append(_line(cx - r, cy, cx + r, cy, sw=1.0))
    o.append(_line(cx, cy - r, cx, cy + r, sw=1.0))

    for a, s, col in ((135, "\u03bb<sub>SD</sub>", GREEN),
                      (45, "\u03bb<sub>SU</sub>", GOLD),
                      (225, "\u03bb<sub>DD</sub>", BLUE),
                      (315, "\u03bb<sub>DU</sub>", DARKRED)):
        x = cx + 54 * math.cos(math.radians(a))
        y = cy - 54 * math.sin(math.radians(a))
        o.append(_txt(x, y + 3, s, 10.5, color=col, weight="600"))

    o.append(_txt(cx, cy - r - 12, "AN TOÀN (hư hỏng an toàn)", 6.6, weight="600",
                  color=GREEN))
    o.append(_txt(cx, cy + r + 18, "NGUY HIỂM (hư hỏng nguy hiểm)", 6.6,
                  weight="600", color=DARKRED))
    o.append(_vtxt(cx - r - 14, cy, "phát hiện được", 6.6, GREEN))
    o.append(_vtxt(cx + r + 14, cy, "không phát hiện được", 6.6, GOLD))

    rows = [("λ<sub>SD</sub>", "an toàn, tự phát hiện", PALE_GREEN),
            ("λ<sub>SU</sub>", "an toàn, ẩn", PALE_GOLD),
            ("λ<sub>DD</sub>", "nguy hiểm, tự phát hiện", PALE_BLUE),
            ("λ<sub>DU</sub>", "nguy hiểm, ẩn", PALE_RED)]
    o.append(_txt(302, 62, "Bốn phần bằng nhau ở đây chỉ để dễ nhìn:", 6.4,
                  anchor="start", color=GREY))
    for i, (sym, lab, col) in enumerate(rows):
        y = 84 + i * 24
        o.append(_rect(302, y - 10, 18, 14, col, sw=0.8, stroke=EDGE))
        o.append(_txt(328, y + 1, sym, 7.4, anchor="start", weight="600"))
        o.append(_txt(366, y + 1, lab, 6.4, anchor="start", color=INK))
    o.append(_txt(302, 196, "Tỉ lệ thật phụ thuộc từng thiết bị. Hệ số phủ", 6.2,
                  anchor="start", color=GREY))
    o.append(_txt(302, 208, "chẩn đoán DC = (λ<sub>SD</sub> + λ<sub>DD</sub>) / λ<sub>TỔNG</sub>.", 6.2,
                  anchor="start", color=GREY))
    o.append(_txt(302, 228, "λ là suất hỏng, tính bằng số hư hỏng mỗi", 6.2,
                  anchor="start", color=GREY))
    o.append(_txt(302, 240, "đơn vị thời gian; λ = 1 / MTBF.", 6.2,
                  anchor="start", color=GREY))
    return _finish(o, 660, 300,
                   "Hình 8-1. Bốn loại hư hỏng. Trục dọc chia an toàn (nửa trên) với nguy hiểm "
                   "(nửa dưới); trục ngang chia phát hiện được (nửa trái) với không phát hiện được "
                   "(nửa phải). Chỉ ô dưới-phải — nguy hiểm và ẩn — mới thật sự là thứ mà phép thử "
                   "định kỳ phải tìm ra.",
                   "Figure 8-1. The four failure modes. The vertical axis separates safe (upper half) "
                   "from dangerous (lower half); the horizontal axis separates detected (left half) "
                   "from undetected (right half). Only the lower-right cell — dangerous and hidden — is "
                   "what periodic proof testing actually has to find.",
                   "Biểu đồ tròn chia bốn phần: an toàn phát hiện được, an toàn ẩn, nguy hiểm phát "
                   "hiện được, nguy hiểm ẩn, kèm phần chú giải bốn ký hiệu lambda.",
                   "A four-way pie chart: safe detected, safe undetected, dangerous detected, "
                   "dangerous undetected, with a key to the four lambda symbols.")


# ---------------------------------------------------------------- 8.2
def fig_8_2():
    """Why one word, availability, cannot describe two failure modes."""
    cx, cy, r = 176, 156, 98
    o = [_txt(330, 20, "Một chữ “khả dụng” không tả nổi hai kiểu hỏng", 8.2,
              weight="600")]

    o.append(_wedge(cx, cy, r, -55, 65, PALE_GREEN))
    o.append(_wedge(cx, cy, r, 65, 185, PALE_GOLD))
    o.append(_wedge(cx, cy, r, 185, 305, PALE_RED))
    o.append(_circle(cx, cy, r, fill="none", sw=1.1))

    o.append(_txt(cx + 52, cy - 12, "cả hai cùng", 6.2, anchor="start", weight="600",
                  color=GREEN))
    o.append(_txt(cx + 52, cy + 1, "khả dụng", 6.2, anchor="start", weight="600",
                  color=GREEN))
    o.append(_txt(cx - 8, cy + 58, "cả hai cùng", 6.2, weight="600", color=GOLD))
    o.append(_txt(cx - 8, cy + 71, "không khả dụng", 6.2, weight="600", color=GOLD))
    o.append(_txt(cx - 58, cy - 30, "nhà máy chạy", 6.2, anchor="end", weight="600",
                  color=DARKRED))
    o.append(_txt(cx - 58, cy - 17, "SIS đã chết", 6.2, anchor="end", weight="600",
                  color=DARKRED))

    rows = [("Cả hai khả dụng", GREEN,
             ("nhà máy đang sản xuất, SIS sẵn sàng.",
              "Chữ “khả dụng” ở đây nghe hợp lý.")),
            ("Cả hai không khả dụng", GOLD,
             ("SIS cắt nhầm, nhà máy dừng.",
              "Vẫn có thể gọi là “không khả dụng”.")),
            ("Nhà máy chạy, SIS chết", DARKRED,
             ("Hỏng nguy hiểm, ẩn. Nhà máy vẫn",
              "“khả dụng” — và không ai biết SIS sẽ",
              "không hành động khi có yêu cầu."))]
    y = 52
    for head, col, body in rows:
        o.append(_rect(304, y - 9, 12, 12, col, sw=0.8, stroke=EDGE))
        o.append(_txt(324, y, head, 6.8, anchor="start", weight="600"))
        for k, ln in enumerate(body):
            o.append(_txt(324, y + 14 + k * 11, ln, 6.0, anchor="start", color=GREY))
        y += 52 + 11 * (len(body) - 2)
    o.append(_txt(304, 214, "Trung bình của 99,999 % ở chế độ an toàn với 94,6 %", 6.2,
                  anchor="start", color=GREY))
    o.append(_txt(304, 226, "ở chế độ nguy hiểm không nói lên điều gì cả.", 6.2,
                  anchor="start", color=GREY))
    return _finish(o, 660, 300,
                   "Hình 8-2. Vì sao không thể gộp hai chế độ hỏng vào một chữ. Ba phần của vòng "
                   "tròn là ba trạng thái khác nhau về hậu quả, mà chỉ hai trong số đó mới được "
                   "chữ “khả dụng” phản ánh đúng.",
                   "Figure 8-2. Why the two failure modes cannot share one word. The three sectors are "
                   "three states with different consequences, and only two of them are described "
                   "correctly by the word availability.",
                   "Biểu đồ tròn ba phần: cả hai khả dụng, cả hai không khả dụng, nhà máy chạy nhưng "
                   "hệ an toàn đã hỏng, kèm chú thích.",
                   "A three-sector pie: both available, both unavailable, and plant running while the "
                   "safety system is dead, with notes.")


# ---------------------------------------------------------------- 8.3
def fig_8_3():
    """The bathtub curve, and why MTBF is not life."""
    x0, y0, W, H = 82, 56, 500, 150
    o = [_txt(330, 20, "Đường cong bồn tắm: tỉ lệ hỏng theo tuổi thiết bị", 8.2,
              weight="600")]

    def yv(v):
        return y0 + H - (v / 1.06) * H

    o.append(_line(x0, y0 + H, x0 + W + 14, y0 + H, sw=1.0))
    o.append(_line(x0, y0 + H, x0, y0 - 10, sw=1.0))
    o.append(_txt(x0 + W, y0 - 14, "thời gian", 7.2, anchor="end", color=GREY))
    o.append(_txt(x0 + 5, y0 - 12, "λ", 8.4, color=GREY))

    o.append(_rect(x0, y0, W * 0.26, H, "#fdf6f4", sw=0, stroke="none"))
    o.append(_rect(x0 + W * 0.72, y0, W * 0.28, H, "#fdf6f4", sw=0, stroke="none"))
    for k in (0.26, 0.72):
        o.append(_line(x0 + W * k, y0, x0 + W * k, y0 + H, sw=0.9, dash="3 4",
                       color=EDGE))

    pts = []
    n = 150
    for i in range(n + 1):
        t = i / float(n)
        if t <= 0.26:
            v = 0.40 + 0.60 * math.exp(-11.0 * t)
        elif t <= 0.72:
            v = 0.40
        else:
            v = 0.40 + 0.62 * ((t - 0.72) / 0.28) ** 2
        pts.append((x0 + t * W, yv(v)))
    o.append(_poly(pts, fill="none", sw=2.0, color=DARKRED))
    o.append(_line(x0, yv(0.40), x0 + W, yv(0.40), sw=0.8, dash="5 4", color=GREEN))

    o.append(_txt(x0 + W * 0.13, y0 + 22, "mồi tử", 6.8, weight="600", color=DARKRED))
    o.append(_txt(x0 + W * 0.13, y0 + 34, "(hỏng sớm)", 6.0, color=GREY))
    o.append(_txt(x0 + W * 0.49, y0 + 30, "gần như hằng số", 6.8, weight="600",
                  color=GREEN))
    o.append(_txt(x0 + W * 0.86, y0 + 30, "mòn", 6.8, weight="600", color=DARKRED))
    o.append(_txt(x0 + W * 0.86, y0 + 42, "(hết tuổi thọ)", 6.0, color=GREY))

    o.append(_txt(x0 + W * 0.49, yv(0.40) - 10, "λ ≈ hằng số", 6.6, color=GREEN))
    o.append(_txt(x0 + W * 0.49, yv(0.40) + 16, "MTBF = 1 / λ", 6.8, weight="600",
                  color=GREEN))

    o.append(_arrow(x0 + W * 0.02, y0 + H + 26, x0 + W * 0.98, y0 + H + 26, sw=0.9,
                    color=GREY))
    o.append(_txt(x0 + W * 0.5, y0 + H + 40, "tuổi thọ hữu ích — không phải “tuổi thọ” của "
                                             "một chiếc que diêm", 6.4, color=GREY))
    return _finish(o, 660, 268,
                   "Hình 8-3. Đường cong bồn tắm. Suất hỏng không cố định suốt đời thiết bị: cao "
                   "lúc đầu vì lỗi chế tạo, phẳng ở giữa, rồi tăng khi mòn. Phần phẳng là chỗ mọi "
                   "công thức trong chương này giả định, và MTBF = 1/λ chỉ có nghĩa trong đoạn ấy.",
                   "Figure 8-3. The bathtub curve. Failure rate is not constant over a device's life: "
                   "high at first from manufacturing defects, flat in the middle, then rising with "
                   "wear-out. The flat middle is where every formula in this chapter assumes you are "
                   "operating, and MTBF = 1/lambda only means anything there.",
                   "Đường cong hình bồn tắm với ba vùng mồi tử, hằng số và mòn, kèm đường λ hằng số "
                   "và nhãn MTBF bằng nghịch đảo lambda.",
                   "A bathtub curve with infant-mortality, constant and wear-out regions, plus a "
                   "constant-lambda line and the label MTBF equals one over lambda.")


# ---------------------------------------------------------------- 8.4
def fig_8_4():
    """A reliability block diagram: series and parallel blocks."""
    o = [_txt(330, 20, "Sơ đồ khối độ tin cậy: nối tiếp và song song", 8.2,
              weight="600")]
    ymid = 96

    o.append(_arrow(24, ymid, 44, ymid, sw=1.2))
    o.append(_box(44, ymid - 15, 58, 30, "A", PAPER, size=9))
    o.append(_line(102, ymid, 124, ymid, sw=1.2))

    def par(x, y1, y2, l1, l2):
        s = [_line(x, ymid, x + 14, ymid, sw=1.2)]
        s.append(_line(x + 14, y1, x + 14, y2, sw=1.2))
        s.append(_line(x + 14, y1, x + 30, y1, sw=1.2))
        s.append(_line(x + 14, y2, x + 30, y2, sw=1.2))
        s.append(_box(x + 30, y1 - 15, 58, 30, l1, PAPER, size=9))
        s.append(_box(x + 30, y2 - 15, 58, 30, l2, PAPER, size=9))
        s.append(_line(x + 88, y1, x + 104, y1, sw=1.2))
        s.append(_line(x + 88, y2, x + 104, y2, sw=1.2))
        s.append(_line(x + 104, y1, x + 104, y2, sw=1.2))
        s.append(_line(x + 104, ymid, x + 126, ymid, sw=1.2))
        return "".join(s)

    o.append(par(124, 52, 140, "C", "D"))
    o.append(par(250, 52, 140, "E", "F"))
    o.append(_box(376, ymid - 15, 58, 30, "B", PAPER, size=9))
    o.append(_line(434, ymid, 456, ymid, sw=1.2))
    o.append(_box(456, ymid - 15, 58, 30, "G", PAPER, size=9))
    o.append(_arrow(514, ymid, 540, ymid, sw=1.2))

    o.append(_txt(330, 186, "Hệ hỏng nếu A, B hoặc G hỏng — hoặc nếu cả C và D cùng hỏng — "
                            "hoặc nếu cả E và F cùng hỏng.", 6.4, color=GREY))
    o.append(_txt(330, 202, "C‖D và E‖F là hai cặp dự phòng; A, B, G là những mắt nối tiếp "
                            "không có dự phòng.", 6.4, color=GREY))
    return _finish(o, 660, 220,
                   "Hình 8-4. Sơ đồ khối độ tin cậy. Xác suất các khối nối tiếp thì cộng lại; xác "
                   "suất các khối song song thì nhân lại. Sơ đồ cho thấy ngay mắt yếu: ba khối nối "
                   "tiếp A, B, G không có dự phòng nào.",
                   "Figure 8-4. A reliability block diagram. Probabilities of series blocks add; "
                   "probabilities of parallel blocks multiply. The diagram shows the weak link at a "
                   "glance: the three series blocks A, B and G have no redundancy at all.",
                   "Sơ đồ khối: A nối tiếp với cặp song song C song song D, rồi cặp E song song F, "
                   "rồi B và G nối tiếp.",
                   "A block diagram: A in series with the parallel pair C and D, then E and F, then "
                   "B and G in series.")


# ---------------------------------------------------------------- 8.5
def fig_8_5():
    """A fault tree with a single OR gate."""
    o = [_txt(330, 20, "Cây lỗi: một cổng HOẶC, ba biến cố cơ bản", 8.2, weight="600")]
    o.append(_rect(226, 36, 208, 36, PALE_BLUE, sw=1.0))
    o.append(_txt(330, 51, "Hệ chữa cháy không hoạt động", 6.6, weight="600"))
    o.append(_txt(330, 63, "khi có cháy", 6.6, weight="600"))
    o.append(_line(330, 72, 330, 96, sw=1.2))

    o.append(_path("M 304 96 Q 330 116 356 96 Q 330 148 304 96 Z", fill=PALE_GOLD,
                   sw=1.1))
    o.append(_txt(330, 110, "≥ 1", 7.2, weight="600"))

    o.append(_line(330, 148, 330, 168, sw=1.2))
    o.append(_line(150, 168, 510, 168, sw=1.2))
    for x in (150, 330, 510):
        o.append(_line(x, 168, x, 186, sw=1.2))
        o.append(_circle(x, 196, 10, fill="#fff", sw=1.1))

    labels = [(150, "Cảm biến cháy"), (330, "Tủ báo cháy"), (510, "Bơm chữa cháy")]
    for x, lab in labels:
        o.append(_rect(x - 62, 216, 124, 30, PAPER, sw=0.9, stroke=EDGE))
        o.append(_txt(x, 235, lab, 6.4))

    o.append(_txt(150, 262, "không phát hiện", 5.8, color=GREY))
    o.append(_txt(330, 262, "không ra lệnh", 5.8, color=GREY))
    o.append(_txt(510, 262, "không bơm được", 5.8, color=GREY))

    o.append(_txt(560, 96, "Xác suất cộng qua cổng HOẶC,", 6.0, anchor="start",
                  color=GREY))
    o.append(_txt(560, 108, "nhân qua cổng VÀ.", 6.0, anchor="start", color=GREY))
    o.append(_txt(560, 126, "Vòng tròn: biến cố cơ bản.", 6.0, anchor="start",
                  color=GREY))
    o.append(_txt(560, 138, "Chữ nhật: mô tả.", 6.0, anchor="start", color=GREY))
    return _finish(o, 660, 280,
                   "Hình 8-5. Cây lỗi. Chỉ cần một trong ba phần tử — cảm biến, tủ, bơm — không làm "
                   "việc thì cả hệ không làm việc, nên đây là cổng HOẶC. Cây lỗi mô tả được cả hệ "
                   "gồm thiết bị trường, nhưng chỉ mô tả được những hỏng hóc đã biết.",
                   "Figure 8-5. A fault tree. If any one of the three elements — detector, panel or "
                   "pump — fails to work, the whole system fails, so this is an OR gate. Fault trees "
                   "can model an entire system including field devices, but only failures somebody "
                   "already knows about.",
                   "Cây lỗi: biến cố đỉnh là hệ chữa cháy không hoạt động, qua cổng HOẶC xuống ba "
                   "biến cố cơ bản là cảm biến, tủ báo cháy và bơm.",
                   "A fault tree: the top event is the fire system failing, through an OR gate to "
                   "three basic events — detector, panel and pump.")


# ---------------------------------------------------------------- 8.6
def fig_8_6():
    """A three-state Markov model."""
    o = [_txt(330, 20, "Mô hình Markov ba trạng thái", 8.2, weight="600")]
    ok = (330, 82)
    sf = (502, 208)
    df = (158, 208)

    o.append(_circle(ok[0], ok[1], 44, fill=PALE_GREEN, sw=1.1))
    o.append(_txt(ok[0], ok[1] - 5, "đang chạy", 6.6, weight="600"))
    o.append(_txt(ok[0], ok[1] + 8, "bình thường", 6.6, weight="600"))

    o.append(_circle(sf[0], sf[1], 42, fill=PALE_GOLD, sw=1.1))
    o.append(_txt(sf[0], sf[1] - 4, "cắt nhầm", 6.4, weight="600"))
    o.append(_txt(sf[0], sf[1] + 8, "an toàn", 6.4, weight="600"))

    o.append(_circle(df[0], df[1], 42, fill=PALE_RED, sw=1.1))
    o.append(_txt(df[0], df[1] - 4, "không hành", 6.4, weight="600"))
    o.append(_txt(df[0], df[1] + 8, "động", 6.4, weight="600"))

    o.append(_link(ok, 44, sf, 42, 9, GOLD))
    o.append(_link(sf, 42, ok, 44, 9, GREEN, dash="4 3"))
    o.append(_link(ok, 44, df, 42, 9, DARKRED))
    o.append(_link(df, 42, ok, 44, 9, GREEN, dash="4 3"))

    mx, my = _mid(ok, 44, sf, 42, 20, 0.5)
    o.append(_txt(mx, my, "λ<sub>s</sub>", 7.6, color=GOLD, weight="600"))
    mx, my = _mid(sf, 42, ok, 44, 20, 0.5)
    o.append(_txt(mx, my, "μ<sub>s</sub>", 7.6, color=GREEN, weight="600"))
    mx, my = _mid(ok, 44, df, 42, 20, 0.5)
    o.append(_txt(mx, my, "λ<sub>d</sub>", 7.6, color=DARKRED, weight="600"))
    mx, my = _mid(df, 42, ok, 44, 20, 0.5)
    o.append(_txt(mx, my, "μ<sub>d</sub>", 7.6, color=GREEN, weight="600"))

    o.append(_txt(330, 268, "λ = tốc độ hỏng · μ = tốc độ sửa chữa = 1/MTTR · đường nét đứt là "
                            "đường hồi phục", 6.2, color=GREY))
    return _finish(o, 660, 286,
                   "Hình 8-6. Mô hình Markov. Mỗi vòng tròn là một trạng thái; mỗi mũi tên là một "
                   "tốc độ chuyển. Cái mà sơ đồ khối và cây lỗi không làm được — thời gian, sửa "
                   "chữa, chu kỳ thử — thì mô hình Markov làm được, đổi lại phải giải ma trận.",
                   "Figure 8-6. A Markov model. Each circle is a state; each arrow is a transition "
                   "rate. What block diagrams and fault trees cannot do — time, repair, test "
                   "intervals — Markov models can, at the price of having to solve a matrix.",
                   "Ba trạng thái Markov: đang chạy, cắt nhầm, không hành động, với các mũi tên tốc "
                   "độ hỏng và tốc độ sửa chữa.",
                   "Three Markov states — normal, spurious trip, fail to function — with failure and "
                   "repair rate arrows.")


# ---------------------------------------------------------------- 8.7
def fig_8_7():
    """Redundancy: what each architecture buys and what it costs."""
    x0, y0, W, H = 96, 96, 470, 156
    lo, hi = 10.0, 3000.0
    o = [_txt(330, 20, "Ảnh hưởng thật của dự phòng (thang logarit, năm)", 8.2,
              weight="600")]

    def yv(v):
        f = (math.log10(v) - math.log10(lo)) / (math.log10(hi) - math.log10(lo))
        return y0 + H - f * H

    o.append(_line(x0, y0 + H, x0 + W, y0 + H, sw=1.0))
    o.append(_line(x0, y0 + H, x0, y0 - 8, sw=1.0))
    for v, lab in ((10, "10"), (100, "100"), (1000, "1.000")):
        o.append(_line(x0 - 4, yv(v), x0, yv(v), sw=0.8))
        o.append(_txt(x0 - 8, yv(v) + 2.4, lab, 6.4, anchor="end", color=GREY))
        o.append(_line(x0, yv(v), x0 + W, yv(v), sw=0.7, dash="2 5", color="#e2ded2"))
    o.append(_txt(x0 + 6, y0 - 10, "MTTF (năm)", 6.6, color=GREY))

    data = [("1oo1", 25, 50), ("1oo2", 12.5, 2500), ("2oo2", 625, 25),
            ("2oo3", 208, 833)]
    for i, (name, s, d) in enumerate(data):
        cx = 160 + i * 112
        for k, (v, col) in enumerate(((s, PALE_GOLD), (d, PALE_BLUE))):
            bx = cx - 32 + k * 34
            top = yv(v)
            o.append(_rect(bx, top, 30, y0 + H - top, col, sw=0.9, stroke=EDGE))
            o.append(_txt(bx + 15, top - 5, ("%.0f" % v).replace(".", ","), 5.8))
        o.append(_txt(cx, y0 + H + 16, name, 7.0, weight="600"))

    o.append(_rect(x0 + 4, 42, 14, 12, PALE_GOLD, sw=0.8, stroke=EDGE))
    o.append(_txt(x0 + 24, 52, "MTTF do cắt nhầm (an toàn)", 6.2, anchor="start"))
    o.append(_rect(x0 + 214, 42, 14, 12, PALE_BLUE, sw=0.8, stroke=EDGE))
    o.append(_txt(x0 + 234, 52, "MTTF do không hành động (nguy hiểm)", 6.2,
                  anchor="start"))

    o.append(_txt(330, 282, "1oo2 an toàn hơn nhưng cắt nhầm gấp đôi; 2oo2 thì ngược lại. "
                            "2oo3 không thắng ở cả hai phía.", 6.4, color=GREY))
    return _finish(o, 660, 298,
                   "Hình 8-7. Cái giá của dự phòng. Mỗi kiến trúc mua được một thứ và trả giá bằng "
                   "thứ khác: 1oo2 giảm mạnh xác suất không hành động nhưng tăng gấp đôi số lần cắt "
                   "nhầm; 2oo2 thì đúng ngược lại. Cột 2oo3 tính từ quy tắc “ba tổ hợp hỏng kép” mà "
                   "nguồn nêu, không phải số in sẵn trong sách.",
                   "Figure 8-7. The price of redundancy. Each architecture buys one thing and pays "
                   "with another: 1oo2 cuts the probability of failing to act but doubles nuisance "
                   "trips; 2oo2 does the exact opposite. The 2oo3 bars are derived from the source's "
                   "own rule of three dual-failure combinations, not copied from a printed table.",
                   "Biểu đồ cột so sánh bốn kiến trúc 1oo1, 1oo2, 2oo2, 2oo3 theo hai chỉ tiêu MTTF "
                   "do cắt nhầm và MTTF do không hành động.",
                   "A bar chart comparing four architectures, 1oo1, 1oo2, 2oo2 and 2oo3, on two "
                   "measures: MTTF for spurious trips and MTTF for failure to act.")


# ---------------------------------------------------------------- 8.8
def fig_8_8():
    """Common cause: one block that takes out all three legs."""
    o = [_txt(330, 20, "Nguyên nhân chung: một khối làm hỏng cả ba kênh", 8.2,
              weight="600")]
    o.append(_arrow(24, 122, 56, 122, sw=1.2))

    o.append(_rect(48, 52, 120, 144, "#fdfaf2", sw=0.8, stroke="#e6dcc4"))
    o.append(_txt(52, 44, "ba kênh “độc lập”", 6.2, anchor="start", color=GREY))

    o.append(_line(56, 74, 56, 170, sw=1.2))
    for y, lab in ((74, "A"), (122, "B"), (170, "C")):
        o.append(_line(56, y, 80, y, sw=1.2))
        o.append(_box(80, y - 15, 54, 30, lab, PAPER, size=9))
        o.append(_line(134, y, 160, y, sw=1.2))
    o.append(_line(160, 74, 160, 170, sw=1.2))
    o.append(_line(160, 122, 184, 122, sw=1.2))

    o.append(_box(184, 107, 64, 30, "D", PALE_RED, size=9))
    o.append(_txt(216, 152, "điểm chung", 5.8, color=DARKRED))
    o.append(_txt(108, 210, "ba kênh chỉ độc lập khi không có D", 5.8, color=GOLD))
    o.append(_arrow(248, 122, 296, 122, sw=1.2))
    o.append(_txt(302, 122, "đầu ra", 6.0, anchor="start", color=GREY))

    o.append(_txt(352, 62, "D là nguyên nhân chung. Nó không", 6.2, anchor="start",
                  color=INK))
    o.append(_txt(352, 74, "nằm trong kênh nào, nhưng nếu nó", 6.2, anchor="start",
                  color=INK))
    o.append(_txt(352, 86, "hỏng thì cả ba kênh cùng hỏng.", 6.2, anchor="start",
                  color=INK))
    o.append(_txt(352, 108, "D có thể là: sai thiết kế, sai lập", 6.0, anchor="start",
                  color=GREY))
    o.append(_txt(352, 120, "trình, sai bảo trì, nhiễu điện từ,", 6.0, anchor="start",
                  color=GREY))
    o.append(_txt(352, 132, "nhiệt độ, độ rung.", 6.0, anchor="start", color=GREY))
    o.append(_txt(352, 154, "Hệ số Beta: phần trăm hư hỏng của", 6.0, anchor="start",
                  color=GREY))
    o.append(_txt(352, 166, "một kênh hoá ra đánh vào cả hệ.", 6.0, anchor="start",
                  color=GREY))
    return _finish(o, 660, 224,
                   "Hình 8-8. Nguyên nhân chung. Ba kênh A, B, C song song chỉ có ích nếu chúng "
                   "hỏng độc lập. Khối D nối tiếp với cả ba làm mất tính độc lập đó, và chỉ một hệ "
                   "số Beta 1 % đủ làm con số 45.000 năm tụt xuống còn 1.100 năm.",
                   "Figure 8-8. Common cause. The three parallel channels A, B and C are only worth "
                   "anything if they fail independently. Block D in series with all three destroys "
                   "that independence, and a Beta factor of just 1 % is enough to pull 45,000 years "
                   "down to 1,100 years.",
                   "Ba kênh song song A, B, C nối tiếp với một khối D chung, minh hoạ nguyên nhân "
                   "chung làm mất tính độc lập.",
                   "Three parallel channels A, B and C in series with one common block D, showing how "
                   "common cause destroys independence.")


FIGURES = [fig_8_1, fig_8_2, fig_8_3, fig_8_4, fig_8_5, fig_8_6, fig_8_7, fig_8_8]
