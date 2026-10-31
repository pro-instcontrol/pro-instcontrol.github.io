# -*- coding: utf-8 -*-
"""Safety Instrumented Systems, Chapter 6 — Determining the SIL."""
import math

from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _axes, _box,
                  _circle, _curve, _line, _node, _path, _poly, _rect, _txt)
from pcfig import _finish, _legend, _legend_h

DARKRED = "#7f1d1d"
AMBER = "#f6e0b8"
PALE_GREEN = "#dcecdc"
PALE_RED = "#f3d6d2"


def _mk(x0, y0, W, H, xr, yr):
    def X(v):
        return x0 + (v - xr[0]) / float(xr[1] - xr[0]) * W

    def Y(v):
        return y0 + H - (v - yr[0]) / float(yr[1] - yr[0]) * H
    return X, Y


def _vtxt(x, y, s, size=7.0, color=GREY):
    """A text label rotated 90 degrees anticlockwise about (x, y)."""
    return ('<text x="%s" y="%s" text-anchor="middle" transform="rotate(-90 %s %s)" '
            'style="font:%spx Inter,Helvetica,sans-serif;fill:%s;">%s</text>'
            % (x, y, x, y, size, color, s))


# ---------------------------------------------------------------- 6.1
def fig_6_1():
    """The ALARP triangle: three regions and the cost-benefit boundary."""
    ax, ay = 330, 34
    bx0, bx1, by = 110, 550, 216

    def half(y):
        return (y - ay) / float(by - ay) * (bx1 - bx0) / 2.0

    y1, y2 = 98, 168
    o = [_poly([(ax, ay), (bx1, by), (bx0, by)], fill="#fbfaf7", sw=1.2, close=True)]
    o.append(_poly([(ax, ay), (ax + half(y1), y1), (ax - half(y1), y1)],
                   fill=PALE_RED, sw=0.0, color=PALE_RED, close=True))
    o.append(_poly([(ax - half(y1), y1), (ax + half(y1), y1),
                    (ax + half(y2), y2), (ax - half(y2), y2)],
                   fill=AMBER, sw=0.0, color=AMBER, close=True))
    o.append(_poly([(ax - half(y2), y2), (ax + half(y2), y2), (bx1, by), (bx0, by)],
                   fill=PALE_GREEN, sw=0.0, color=PALE_GREEN, close=True))
    o.append(_poly([(ax, ay), (bx1, by), (bx0, by)], fill="none", sw=1.3, close=True))
    o.append(_line(ax - half(y1), y1, ax + half(y1), y1, sw=1.0))
    o.append(_line(ax - half(y2), y2, ax + half(y2), y2, sw=1.0))

    o.append(_txt(ax, 88, "KHÔNG CHẤP NHẬN ĐƯỢC", 6.9, color=DARKRED, weight="600"))
    o.append(_txt(ax, 122, "VÙNG ALARP", 8.0, color=GOLD, weight="600"))
    o.append(_txt(ax, 138, "chỉ chấp nhận nếu lợi ích bù lại được chi phí", 6.6, color=INK))
    o.append(_txt(ax, 154, "chi phí giảm rủi ro tăng rất nhanh ở đây", 6.2, color=GREY))
    o.append(_txt(ax, 196, "CHẤP NHẬN RỘNG RÃI", 7.6, color=GREEN, weight="600"))

    o.append(_arrow(78, 206, 78, 44, sw=1.2, color=GREY))
    o.append(_txt(70, 128, "rủi ro tăng", 6.6, anchor="end", color=GREY))
    o.append(_txt(70, 140, "chi phí giảm", 6.6, anchor="end", color=GREY))
    o.append(_arrow(586, 44, 586, 206, sw=1.2, color=GREY))
    o.append(_txt(594, 128, "không đáng", 6.6, anchor="start", color=GREY))
    o.append(_txt(594, 140, "để chi", 6.6, anchor="start", color=GREY))
    return _finish(o, 660, 236,
                   "Hình 6-1. Nguyên lý ALARP. Ba vùng rủi ro và một đường biên không phải đường "
                   "thẳng: ở giữa là vùng mà việc giảm rủi ro chỉ bắt buộc khi lợi ích thu được bù "
                   "lại được chi phí bỏ ra. Ranh giới ấy là một khái niệm pháp lý, không phải một "
                   "con số kỹ thuật.",
                   "Figure 6-1. The ALARP principle. Three risk regions and a boundary that is not a "
                   "straight line: in the middle band, reducing risk is required only when the benefit "
                   "justifies the cost. That boundary is a legal concept, not a technical number.",
                   "Tam giác chia ba vùng: đỉnh hẹp màu đỏ là không chấp nhận được, giữa màu vàng là "
                   "vùng ALARP, đáy rộng màu xanh là chấp nhận rộng rãi.",
                   "A triangle in three bands: a narrow red apex that is unacceptable, an amber ALARP "
                   "band in the middle, and a wide green base that is broadly acceptable.")


# ---------------------------------------------------------------- 6.2
def fig_6_2():
    """The two-dimensional risk matrix of table 6-6."""
    cw, ch = 66, 40
    x0, y0 = 130, 40
    o = [_txt(295, 20, "Ma trận rủi ro hai chiều: tần suất × mức nghiêm trọng", 8.2, weight="600")]
    freqs = ["1\nkhông đáng kể", "2\nhiếm", "3\nthỉnh thoảng", "4\ncó thể", "5\nthường xuyên"]
    sevs = ["V  thảm khốc", "IV  nghiêm trọng", "III  nặng", "II  nhẹ", "I  không đáng kể"]
    for i in range(5):
        for j in range(5):
            sev = 5 - i          # row 0 is severity V = 5
            frq = j + 1
            tot = sev + frq
            fill = PALE_RED if tot >= 8 else (AMBER if tot >= 5 else PALE_GREEN)
            o.append(_rect(x0 + j * cw, y0 + i * ch, cw, ch, fill, sw=0.8))
            o.append(_txt(x0 + j * cw + cw / 2.0, y0 + i * ch + ch / 2.0 + 2.6,
                          "%d-%s" % (frq, ["I", "II", "III", "IV", "V"][sev - 1]), 6.4,
                          color=INK))
    for i, s in enumerate(sevs):
        o.append(_txt(x0 - 6, y0 + i * ch + ch / 2.0 + 2.4, s, 6.2, anchor="end", color=INK))
    for j in range(5):
        o.append(_txt(x0 + j * cw + cw / 2.0, y0 + 5 * ch + 13, str(j + 1), 7.0))
    o.append(_txt(x0 + 2.5 * cw, y0 + 5 * ch + 28, "tần suất (1 thấp → 5 cao)", 7.0, color=GREY))
    o.append(_vtxt(26, y0 + 2.5 * ch, "mức nghiêm trọng"))
    o.append(_legend_h(x0, y0 + 5 * ch + 46,
                       [(PALE_GREEN, "rủi ro thấp", ""),
                        (AMBER, "rủi ro trung bình", ""),
                        (PALE_RED, "rủi ro cao", "")], gap=18))
    return _finish(o, 600, 300,
                   "Hình 6-2. Ma trận rủi ro hai chiều của bảng 6-6: mỗi ô là một cặp tần suất – mức "
                   "nghiêm trọng, tô màu theo mức rủi ro tổng hợp. Góc dưới bên trái là rủi ro thấp "
                   "nhất, góc trên bên phải là cao nhất. Ma trận này dùng để đánh giá rủi ro, không "
                   "dùng để chọn SIL — vì nó chưa tính tới các lớp bảo vệ bổ sung.",
                   "Figure 6-2. The two-dimensional risk matrix of table 6-6: each cell is a "
                   "frequency–severity pair, shaded by the combined risk. The lower-left corner is the "
                   "lowest risk, the upper-right the highest. This matrix evaluates risk; it does not "
                   "select a SIL, because it does not yet account for additional protection layers.",
                   "Lưới năm nhân năm, các ô góc dưới bên trái màu xanh, dải chéo giữa màu vàng, góc "
                   "trên bên phải màu đỏ.",
                   "A five-by-five grid with green cells at the lower left, an amber diagonal band, and "
                   "red cells at the upper right.")


# ---------------------------------------------------------------- 6.3
def fig_6_3():
    """The third axis: the same grid before and after one extra layer."""
    o = [_txt(330, 20, "Trục thứ ba: cùng một rủi ro, thêm một lớp bảo vệ thì SIL hạ xuống",
              8.2, weight="600")]
    cw, ch = 52, 36
    for k, (title, drop) in enumerate([("không có lớp bổ sung", 0),
                                       ("có một lớp bổ sung (van an toàn)", 1)]):
        x0 = 58 + k * 300
        y0 = 62
        o.append(_txt(x0 + 2 * cw, y0 - 14, title, 7.0, weight="600",
                      color=INK if k == 0 else GREEN))
        for i in range(4):
            for j in range(4):
                sev = 4 - i
                frq = j + 1
                sil = max(0, min(3, (sev + frq) // 2 - 1 + (1 if sev + frq >= 7 else 0)))
                sil = max(0, sil - drop)
                fill = PALE_RED if sil >= 3 else (AMBER if sil == 2 else
                                                  (PALE_GREEN if sil == 1 else "#f4f2ec"))
                o.append(_rect(x0 + j * cw, y0 + i * ch, cw, ch, fill, sw=0.8))
                o.append(_txt(x0 + j * cw + cw / 2.0, y0 + i * ch + ch / 2.0 + 3.0,
                              "SIL %d" % sil if sil else "—", 6.6,
                              color=INK, weight="600"))
        for i, s in enumerate(["V", "IV", "III", "II"]):
            o.append(_txt(x0 - 5, y0 + i * ch + ch / 2.0 + 2.4, s, 6.4, anchor="end",
                          color=GREY))
        for j in range(4):
            o.append(_txt(x0 + j * cw + cw / 2.0, y0 + 4 * ch + 12, str(j + 1), 6.6,
                          color=GREY))
        o.append(_txt(x0 + 2 * cw, y0 + 4 * ch + 26, "tần suất", 6.4, color=GREY))
    o.append(_arrow(636, 200, 636, 70, sw=1.2, color=GREY))
    o.append(_txt(644, 135, "số lớp", 6.4, anchor="start", color=GREY))
    o.append(_txt(644, 147, "tăng", 6.4, anchor="start", color=GREY))
    return _finish(o, 660, 236,
                   "Hình 6-3. Trục thứ ba của ma trận rủi ro. Cùng một cặp tần suất – nghiêm trọng, "
                   "nếu ngoài hệ an toàn đang xét còn có thêm một lớp bảo vệ độc lập thì yêu cầu về "
                   "SIL hạ xuống một bậc. Đây chính là chỗ một van an toàn biến một yêu cầu SIL 3 "
                   "thành SIL 2, và đó là lý do phải liệt kê đủ các lớp trước khi chọn SIL.",
                   "Figure 6-3. The third axis of the risk matrix. For the same frequency–severity "
                   "pair, an independent protection layer outside the system under study lowers the SIL "
                   "requirement by one step. That is how a relief valve turns a SIL 3 requirement into "
                   "SIL 2 — and why every layer must be listed before a SIL is chosen.",
                   "Hai lưới bốn nhân bốn cạnh nhau, lưới bên trái ghi SIL 3, 2, 1, lưới bên phải các "
                   "ô tương ứng hạ xuống một bậc.",
                   "Two four-by-four grids side by side; the left one reads SIL 3, 2, 1, and the right "
                   "one shows each cell one step lower.")


# ---------------------------------------------------------------- 6.4
def fig_6_4():
    """The risk graph, expanded for one consequence level."""
    o = [_txt(330, 18, "Đồ thị rủi ro: từ mức nghiêm trọng tới SIL", 8.2, weight="600")]

    o.append(_box(18, 106, 92, 42, "Cc", fill="#f6e0b8", size=9.0,
                  sub="nhiều người chết"))
    for y, lab in ((74, "Fa"), (176, "Fb")):
        o.append(_box(150, y - 14, 56, 28, lab, fill="#eef3fb", size=7.6))
        o.append(_arrow(110, 127, 148, y, sw=1.0))

    ps = [(74, 58, "Pa"), (74, 100, "Pb"), (176, 154, "Pa"), (176, 196, "Pb")]
    for fy, py, lab in ps:
        o.append(_box(252, py - 12, 46, 24, lab, fill="#e6f0e8", size=7.0))
        o.append(_arrow(206, fy, 250, py, sw=0.9))

    for x, lab in ((356, "W1"), (420, "W2"), (484, "W3")):
        o.append(_txt(x, 38, lab, 7.0, color=GOLD, weight="600"))
        o.append(_txt(x, 216, lab, 7.0, color=GOLD, weight="600"))

    sil_of = {("Pa", "W1"): "a", ("Pa", "W2"): "1", ("Pa", "W3"): "2",
              ("Pb", "W1"): "1", ("Pb", "W2"): "2", ("Pb", "W3"): "3"}
    for _fy, py, lab in ps:
        for k, x in enumerate((356, 420, 484)):
            val = sil_of[(lab, ["W1", "W2", "W3"][k])]
            o.append(_circle(x, py, 9.5, fill="#ffffff", sw=0.9, color=INK))
            o.append(_txt(x, py + 2.6, val, 7.4, weight="600",
                          color=RED if val in "23" else INK))
            o.append(_line(298, py, x - 10, py, sw=0.8, color="#c3bdb0"))

    o.append(_txt(536, 92, "a = không cần", 6.0, anchor="start", color=GREY))
    o.append(_txt(536, 103, "yêu cầu riêng", 6.0, anchor="start", color=GREY))
    o.append(_txt(536, 118, "b = một SIS", 6.0, anchor="start", color=GREY))
    o.append(_txt(536, 129, "là không đủ", 6.0, anchor="start", color=GREY))
    o.append(_txt(536, 152, "Ca → a,  Cb → 1,", 6.0, anchor="start", color=INK))
    o.append(_txt(536, 163, "Cd → 3, 4, b", 6.0, anchor="start", color=INK))
    return _finish(o, 660, 232,
                   "Hình 6-4. Đồ thị rủi ro, mở đầy đủ cho một mức nghiêm trọng. Đi từ trái sang phải: "
                   "hậu quả (C) → tần suất và mức phơi nhiễm (F) → khả năng tránh được (P) → xác suất "
                   "xảy ra (W) → SIL. Mỗi tổ hợp cho một kết quả; các mức C khác có cấu trúc tương tự "
                   "nhưng cho kết quả khác.",
                   "Figure 6-4. The risk graph, expanded for one consequence level. Read left to right: "
                   "consequence (C) → frequency and exposure (F) → possibility of avoidance (P) → "
                   "probability of occurrence (W) → SIL. Each combination yields one answer; the other "
                   "consequence levels have the same structure but different results.",
                   "Cây quyết định bốn tầng từ Cc qua Fa/Fb, Pa/Pb, tới ba cột W1 W2 W3, mỗi nút lá là "
                   "một vòng tròn ghi ký hiệu SIL.",
                   "A four-stage decision tree from Cc through Fa/Fb and Pa/Pb to three W columns, each "
                   "leaf a small circle holding a SIL symbol.")


# ---------------------------------------------------------------- 6.5
def fig_6_5():
    """SIL as a band on the PFD axis, with availability and RRF alongside."""
    x0, y0, W, H = 72, 78, 516, 78
    lo, hi = -5.0, 0.0
    X, _ = _mk(x0, y0, W, H, (lo, hi), (0.0, 1.0))
    o = [_txt(330, 22, "Bốn mức SIL trên một trục logarit của PFD", 8.4, weight="600")]
    M5, M4, M3, M2, M1 = ("10<sup>\u22125</sup>", "10<sup>\u22124</sup>",
                          "10<sup>\u22123</sup>", "10<sup>\u22122</sup>",
                          "10<sup>\u22121</sup>")
    bands = [(-5.0, -4.0, "SIL 4", M5 + " \u2013 " + M4, "99,99 \u2013 99,999 %",
              "10.000 \u2013 100.000", PALE_RED),
             (-4.0, -3.0, "SIL 3", M4 + " \u2013 " + M3, "99,9 \u2013 99,99 %",
              "1.000 \u2013 10.000", AMBER),
             (-3.0, -2.0, "SIL 2", M3 + " \u2013 " + M2, "99 \u2013 99,9 %",
              "100 \u2013 1.000", PALE_GREEN),
             (-2.0, -1.0, "SIL 1", M2 + " \u2013 " + M1, "90 \u2013 99 %",
              "10 \u2013 100", "#e8eef6")]
    for a, b, name, pfd, av, rrf, fill in bands:
        cx = (X(a) + X(b)) / 2.0
        o.append(_rect(X(a), y0, X(b) - X(a), H, fill, sw=1.0))
        o.append(_txt(cx, y0 + 22, name, 8.6, weight="600"))
        o.append(_txt(cx, y0 + 41, "PFD " + pfd, 7.0))
        o.append(_txt(cx, y0 + 55, "khả dụng " + av, 6.2, color=GREY))
        o.append(_txt(cx, y0 + 68, "RRF " + rrf, 6.2, color=GREY))
    cx5 = (X(-1.0) + X(0.0)) / 2.0
    o.append(_rect(X(-1.0), y0, X(0.0) - X(-1.0), H, "#f7f5f0", sw=1.0))
    o.append(_txt(cx5, y0 + 22, "dưới SIL 1", 7.4, color=GREY))
    o.append(_txt(cx5, y0 + 41, "PFD &gt; " + M1, 7.0, color=GREY))

    for v, lab in ((-5.0, M5), (-4.0, M4), (-3.0, M3), (-2.0, M2),
                   (-1.0, M1), (0.0, "1")):
        o.append(_line(X(v), y0 + H, X(v), y0 + H + 4, sw=0.8))
        o.append(_txt(X(v), y0 + H + 16, lab, 7.4, color=GREY))
    o.append(_txt(x0 + W, y0 + H + 32, "PFD (xác suất hỏng khi có yêu cầu)", 7.2,
                  anchor="end", color=GREY))
    o.append(_txt(330, y0 - 14, "PFD càng nhỏ thì hệ càng tốt — nhưng chi phí tăng theo bậc, "
                                "không theo phần trăm", 6.8, color=RED))
    return _finish(o, 660, 204,
                   "Hình 6-5. Bốn mức SIL đặt trên một trục logarit của PFD, kèm hai cách diễn đạt "
                   "tương đương. Điều đáng chú ý là các mức cách nhau đúng một bậc mười, nên chênh "
                   "lệch giữa SIL 1 và SIL 2 không phải vài phần trăm mà là gấp mười lần — và chi phí "
                   "cũng tăng theo đúng bậc ấy.",
                   "Figure 6-5. The four SIL bands on a logarithmic PFD axis, with two equivalent ways "
                   "of stating the same thing. Note that the bands are exactly one decade apart, so the "
                   "gap between SIL 1 and SIL 2 is not a few per cent but a factor of ten — and the cost "
                   "rises by the same factor.",
                   "Dải ngang chia bốn đoạn trên trục logarit, mỗi đoạn ghi tên mức SIL, khoảng PFD, "
                   "độ khả dụng và hệ số giảm rủi ro.",
                   "A horizontal bar in four segments on a log axis, each labelled with its SIL, PFD "
                   "range, availability and risk reduction factor.")


# ---------------------------------------------------------------- 6.6
def fig_6_6():
    """The hexane surge drum of the LOPA example."""
    o = [_txt(330, 20, "Quá trình trong ví dụ LOPA: bồn chứa hexane và đê chắn", 8.2,
              weight="600")]

    # --- the drum
    o.append(_rect(150, 110, 150, 90, "#f3f1ea", sw=1.3))
    o.append(_txt(225, 142, "BỒN CHỨA", 7.6, weight="600"))
    o.append(_txt(225, 156, "hexane", 6.6, color=GREY))
    o.append(_poly([(156, 176), (294, 176), (294, 196), (156, 196)], fill="#e8dcc0",
                   sw=0.8, close=True))
    o.append(_txt(225, 190, "mức lỏng", 5.8, color=GREY))

    # --- feed through the inlet valve
    o.append(_arrow(40, 90, 118, 90, sw=1.2))
    o.append(_rect(118, 82, 38, 16, "#f6ecd8", sw=1.0))
    o.append(_txt(137, 93, "VAN", 6.2))
    o.append(_line(156, 90, 200, 90, sw=1.2))
    o.append(_arrow(200, 90, 200, 110, sw=1.2))
    o.append(_txt(42, 82, "dòng vào", 6.4, anchor="start", color=GREY))

    # --- level controller and its signal to the valve
    o.append(_circle(225, 62, 14, fill="#eef3fb", sw=1.1))
    o.append(_txt(225, 65, "LC", 7.2))
    o.append(_line(225, 76, 225, 110, sw=1.0, dash="3 3", color=GREY))
    o.append(_txt(230, 92, "LT", 6.0, anchor="start", color=GREY))
    o.append(_line(211, 62, 137, 62, sw=1.0, dash="3 3", color=GREY))
    o.append(_arrow(137, 62, 137, 80, sw=1.0, dash="3 3", color=GREY))

    # --- the vent that carries the overflow into the dike
    o.append(_line(300, 124, 420, 124, sw=1.2))
    o.append(_arrow(420, 124, 420, 208, sw=1.2))
    o.append(_txt(306, 118, "ống thông hơi", 5.8, anchor="start", color=GOLD))

    # --- the dike
    o.append(_poly([(330, 182), (330, 216), (600, 216), (600, 182)], fill="none",
                   sw=1.4, color=INK, close=False))
    o.append(_txt(500, 210, "ĐÊ CHẮN", 6.8, weight="600"))
    o.append(_txt(500, 234, "chất lỏng tràn ra được giữ lại ở đây", 5.8, color=GREY))
    return _finish(o, 660, 250,
                   "Hình 6-6. Quá trình trong ví dụ LOPA. Bồn chứa hexane được giữ mức bằng một bộ "
                   "điều khiển mức tác động lên van nạp. Nếu bồn đầy quá, hexane thoát qua ống thông "
                   "hơi và được đê chắn giữ lại. Sự cố chỉ xảy ra khi cả bộ điều khiển lẫn đê đều "
                   "không giữ được — và đó chính là điều chuỗi sự kiện ở hình sau tính tới.",
                   "Figure 6-6. The process of the LOPA example. A hexane drum is held at level by a "
                   "level controller driving the inlet valve. If the drum overfills, hexane escapes "
                   "through a vent and is caught by the dike. The accident happens only when both the "
                   "controller and the dike fail — which is exactly what the event tree quantifies.",
                   "Sơ đồ bồn chứa có bộ điều khiển mức, van nạp, ống thông hơi và một đê chắn thấp "
                   "bên phải.",
                   "A drum with a level controller, an inlet valve, a vent line and a low dike to the "
                   "right.")


# ---------------------------------------------------------------- 6.7
def fig_6_7():
    """The event tree that turns 1E-1 into 2.5E-4."""
    o = [_txt(330, 20, "Cây sự kiện của ví dụ LOPA", 8.4, weight="600")]
    heads = [(140, "hỏng vòng BPCS", "1 × 10⁻¹"),
             (245, "đê giữ được", "1 × 10⁻²"),
             (350, "có nguồn đánh lửa", "1,0"),
             (455, "có người trong vùng", "0,5"),
             (555, "tử vong", "0,5")]
    for x, a, b in heads:
        o.append(_txt(x, 46, a, 6.0, color=INK, weight="600"))
        o.append(_txt(x, 70, b, 5.8, color=GREY))

    GOLD_D = "#8a5a10"
    rows = [(96, "0,99", "—", "—", "—", "không sự cố đáng kể", GREEN),
            (124, "0,01", "0", "—", "—", "không sự cố đáng kể", GREEN),
            (152, "0,01", "1,0", "0", "—", "không sự cố đáng kể", GREEN),
            (180, "0,01", "1,0", "0,5", "0,5", "cháy, có tử vong", DARKRED),
            (208, "0,01", "1,0", "0,5", "0,5", "cháy, không tử vong", GOLD_D)]
    for y, *cells in rows:
        label, col = cells[-2], cells[-1]
        o.append(_line(96, y + 10, 600, y + 10, sw=0.5, color="#e0dbd0"))
        for k, v in enumerate(cells[:-2]):
            if v == "—":
                continue
            o.append(_txt(heads[k + 1][0], y, v, 6.0, color=INK))
        o.append(_txt(606, y + 3, label, 6.0, anchor="start", color=col))

    o.append(_line(96, 88, 96, 226, sw=1.0))
    o.append(_txt(90, 88, "1,0", 6.0, anchor="end", color=GREY))
    o.append(_txt(340, 240, "P(cháy) = 0,1 × 0,01 × 1,0 = 1 × 10⁻³   ·   "
                            "P(tử vong) = 0,1 × 0,01 × 1,0 × 0,5 × 0,5 = 2,5 × 10⁻⁴",
                  7.0, color=INK))
    return _finish(o, 700, 258,
                   "Hình 6-7. Cây sự kiện của ví dụ LOPA. Đọc từ trái sang phải, mỗi cột là một điều "
                   "kiện với xác suất của nó; tích các xác suất trên một hàng cho ra tần suất của kết "
                   "cục ở cuối hàng. Ba hàng đầu không dẫn tới sự cố; hai hàng cuối là hai kết cục có "
                   "hại: cháy không tử vong và cháy có tử vong 2,5 × 10⁻⁴ mỗi năm.",
                   "Figure 6-7. The event tree of the LOPA example. Read left to right: each column is "
                   "one condition with its probability, and the product along a row gives the frequency "
                   "of that outcome. The first three rows lead nowhere; the last two are the harmful "
                   "outcomes — a fire without fatality, and a fire with fatality at 2.5 × 10⁻⁴ per year.",
                   "Bảng cây sự kiện năm cột điều kiện, năm hàng kết cục, ba hàng đầu màu xanh, hàng "
                   "áp chót màu đỏ và hàng cuối màu vàng.",
                   "An event-tree table with five condition columns and five outcome rows: three green, "
                   "then red and amber for the two harmful outcomes.")


FIGURES = [fig_6_1, fig_6_2, fig_6_3, fig_6_4, fig_6_5, fig_6_6, fig_6_7]
