# -*- coding: utf-8 -*-
"""Safety Instrumented Systems, Chapter 14 — Justification for a Safety System."""
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

# --- numbers behind figure 14-4 -----------------------------------------
# straight out of tables 14-3 and 14-4 of the source, in dollars
CASE1_INIT, CASE1_PV = 104000, 567031
CASE2_INIT, CASE2_PV = 142000, 454871
CASE1_TOT = CASE1_INIT + CASE1_PV      # 671,031
CASE2_TOT = CASE2_INIT + CASE2_PV      # 596,871


def _valve(x, y):
    """A bow-tie valve body centred on (x, y)."""
    return [_poly([(x - 13, y - 8), (x, y), (x - 13, y + 8)], fill="#fff", sw=1.1, close=True),
            _poly([(x, y), (x + 13, y + 8), (x + 13, y - 8)], fill="#fff", sw=1.1, close=True)]


def _actuator(x, y):
    """Piston actuator above a valve, centred on x with its top at y."""
    return _rect(x - 12, y, 24, 16, "#fff", sw=1.1)


def _vtxt(x, y, s, size=7.0, color=GREY):
    """Text rotated 90 degrees anticlockwise about (x, y)."""
    return ('<text x="%s" y="%s" font-size="%s" fill="%s" text-anchor="middle" '
            'transform="rotate(-90 %s %s)">%s</text>' % (x, y, size, color, x, y, s))


# ---------------------------------------------------------------- 14.7
def fig_14_1():
    """Basic process control for the vessel: two feeds, level control, relief valve."""
    o = [_txt(330, 20, "Điều khiển quá trình cơ bản cho bình phản ứng: hai dòng nạp, một vòng mức",
              8.2, weight="600")]

    # ---- the vessel
    o.append(_path("M 420 118 L 420 300 L 570 300 L 570 118 Q 495 78 420 118 Z",
                   fill="#fbfaf6", sw=1.3))
    o.append(_txt(495, 225, "BÌNH PHẢN ỨNG", 6.4, weight="600"))

    # ---- relief valve on the dome
    o.append(_line(495, 92, 495, 76, sw=1.2))
    o.append(_circle(495, 61, 15, fill="#fff", sw=1.2))
    o.append(_txt(495, 59, "PSV", 5.6, weight="600"))
    o.append(_txt(495, 67, "4", 5.6, weight="600"))
    o.append(_line(495, 46, 495, 34, sw=1.2))
    o.append(_line(495, 34, 517, 34, sw=1.2))
    o.append(_arrow(517, 34, 533, 34, sw=1.2))
    o.append(_txt(539, 36, "ra khí quyển", 5.0, anchor="start", color=GREY))

    # ---- feed A
    yA, yB = 200, 290
    o.append(_line(56, yA, 420, yA, sw=1.4))
    o.append(_arrow(48, yA, 62, yA, sw=1.4))
    o.append(_txt(60, yA + 14, "NẠP A", 5.6, anchor="start", weight="600"))

    o.append(_circle(150, yA, 20, fill="#fff", sw=1.2))
    o.append(_txt(150, yA - 3, "FT", 6.0, weight="600"))
    o.append(_txt(150, yA + 7, "1", 6.0, weight="600"))

    o.extend(_valve(250, yA))
    o.append(_actuator(250, yA - 24))

    # ---- feed B
    o.append(_line(56, yB, 420, yB, sw=1.4))
    o.append(_arrow(48, yB, 62, yB, sw=1.4))
    o.append(_txt(60, yB + 14, "NẠP B", 5.6, anchor="start", weight="600"))

    o.append(_circle(150, yB, 20, fill="#fff", sw=1.2))
    o.append(_txt(150, yB - 3, "FT", 6.0, weight="600"))
    o.append(_txt(150, yB + 7, "2", 6.0, weight="600"))

    o.extend(_valve(250, yB))
    o.append(_actuator(250, yB - 24))

    # ---- outlet
    o.append(_line(570, 240, 612, 240, sw=1.4))
    o.append(_arrow(612, 240, 628, 240, sw=1.4))
    o.append(_txt(618, 232, "RA", 5.6, anchor="middle", weight="600"))

    # ---- controllers, in the clear margin left of the transmitters
    o.append(_rect(48, 150, 56, 30, PALE_BLUE, sw=1.1, stroke=EDGE))
    o.append(_txt(76, 164, "FC", 6.2, weight="600"))
    o.append(_txt(76, 174, "1", 6.2, weight="600"))

    o.append(_rect(48, 240, 56, 30, PALE_BLUE, sw=1.1, stroke=EDGE))
    o.append(_txt(76, 254, "FC", 6.2, weight="600"))
    o.append(_txt(76, 264, "2", 6.2, weight="600"))

    # ---- level loop, tapped into the upper shell
    o.append(_circle(372, 150, 20, fill="#fff", sw=1.2))
    o.append(_txt(372, 147, "LT", 6.0, weight="600"))
    o.append(_txt(372, 157, "3", 6.0, weight="600"))
    o.append(_line(392, 150, 420, 150, sw=1.1))
    o.append(_line(372, 130, 372, 114, sw=1.1))

    o.append(_rect(344, 84, 56, 30, PALE_BLUE, sw=1.1, stroke=EDGE))
    o.append(_txt(372, 98, "LC", 6.2, weight="600"))
    o.append(_txt(372, 108, "3", 6.2, weight="600"))

    # ---- signal lines (dashed)
    # LC-3 sets the setpoint of FC-1
    o.append(_line(344, 99, 76, 99, sw=1.0, dash="4 3"))
    o.append(_line(76, 99, 76, 150, sw=1.0, dash="4 3"))
    o.append(_arrow(76, 146, 76, 150, sw=1.0, dash="4 3"))
    # FC-1 trims the setpoint of FC-2 to hold the ratio
    o.append(_line(76, 180, 76, 240, sw=1.0, dash="4 3"))
    o.append(_arrow(76, 236, 76, 240, sw=1.0, dash="4 3"))
    # controller outputs to the valves
    o.append(_line(104, 165, 250, 165, sw=1.0, dash="4 3"))
    o.append(_line(250, 165, 250, 176, sw=1.0, dash="4 3"))
    o.append(_arrow(250, 172, 250, 176, sw=1.0, dash="4 3"))
    o.append(_line(104, 255, 250, 255, sw=1.0, dash="4 3"))
    o.append(_line(250, 255, 250, 266, sw=1.0, dash="4 3"))
    o.append(_arrow(250, 262, 250, 266, sw=1.0, dash="4 3"))

    o.append(_txt(330, 330, "Nét liền: đường quá trình. Nét đứt: tín hiệu. Bộ điều khiển mức đặt điểm "
                            "đặt cho FC-1, và FC-1 chỉnh điểm đặt của FC-2 để giữ đúng tỉ lệ.",
                  5.4, color=GREY))

    return _finish(o, 660, 344,
                   "Hình 14-1. Điều khiển quá trình cơ bản cho bình phản ứng. Hai dòng nạp A và B được nạp "
                   "liên tục theo một tỉ lệ cố định; bộ điều khiển mức đặt điểm đặt cho bộ điều khiển lưu "
                   "lượng của dòng A, và bộ điều khiển ấy chỉnh điểm đặt của dòng B để giữ tỉ lệ. Van an "
                   "toàn PSV-4 bảo vệ bình khỏi quá áp. Toàn bộ hệ này là BPCS — không có phần tử nào ở "
                   "đây thuộc về hệ an toàn.",
                   "Figure 14-1. Basic process control for the vessel. Feeds A and B are fed continuously "
                   "in a fixed ratio; the level controller sets the setpoint of the flow controller for feed "
                   "A, and that controller trims the setpoint for feed B to hold the ratio. PSV-4 protects "
                   "the vessel against overpressure. All of this is the BPCS — none of it belongs to the "
                   "safety system.",
                   "Sơ đồ ống và thiết bị: bình phản ứng có van an toàn PSV-4 trên đỉnh, hai dòng nạp A và "
                   "B mỗi dòng có một cảm biến lưu lượng FT và một van điều khiển, cùng các bộ điều khiển "
                   "FC-1, FC-2, LC-3 và cảm biến mức LT-3.",
                   "A P&ID: a reactor vessel with relief valve PSV-4 on the dome, two feed lines A and B "
                   "each carrying a flow transmitter FT and a control valve, and controllers FC-1, FC-2, "
                   "LC-3 with level transmitter LT-3.")


# ---------------------------------------------------------------- 14.7 (case 1)
def _arch(left, mid, right, title, note_vi, note_en, cap_vi, cap_en, av, ae, sub=""):
    """A two-in, one-logic, two-out safety architecture."""
    o = [_txt(330, 20, title, 8.2, weight="600")]

    lx, lw = 40, 168
    mx, mw = 246, 168
    rx, rw = 452, 168
    ys = (72, 158)

    for i, lab in enumerate(left):
        o.append(_rect(lx, ys[i], lw, 56, PALE_BLUE, sw=1.1, stroke=EDGE))
        o.append(_txt(lx + lw / 2, ys[i] + 24, lab[0], 6.0, weight="600"))
        o.append(_txt(lx + lw / 2, ys[i] + 38, lab[1], 5.8, color=GREY))
        o.append(_arrow(lx + lw + 2, ys[i] + 28, mx - 2, ys[i] + 28, sw=1.2))

    for i, lab in enumerate(right):
        o.append(_rect(rx, ys[i], rw, 56, PALE_GOLD, sw=1.1, stroke=EDGE))
        o.append(_txt(rx + rw / 2, ys[i] + 24, lab[0], 6.0, weight="600"))
        o.append(_txt(rx + rw / 2, ys[i] + 38, lab[1], 5.8, color=GREY))
        o.append(_arrow(mx + mw + 2, ys[i] + 28, rx - 2, ys[i] + 28, sw=1.2))

    o.append(_rect(mx, 84, mw, 118, "#fff", sw=1.2, stroke=INK))
    o.append(_txt(mx + mw / 2, 112, mid[0], 6.4, weight="600"))
    for i, ln in enumerate(mid[1]):
        o.append(_txt(mx + mw / 2, 130 + i * 12, ln, 5.6, color=GREY))

    if sub:
        o.append(_txt(330, 226, sub, 5.4, color=GREY))
    o.append(_txt(330, 250, note_vi, 5.4, color=GREY))

    return _finish(o, 660, 262, cap_vi, cap_en, av, ae)


def fig_14_2():
    """Case 1: single transmitters, relay logic, single valves."""
    return _arch(
        [("Cảm biến lưu lượng A", "1oo1"), ("Cảm biến lưu lượng B", "1oo1")],
        ("Logic rơ-le", ["2 bộ khuếch đại ngưỡng", "4 rơ-le điện-cơ"]),
        [("Van cắt lưu lượng A", "1oo1"), ("Van cắt lưu lượng B", "1oo1")],
        "Ca 1: cảm biến đơn, logic rơ-le, van đơn",
        "Mỗi chức năng an toàn dùng một cảm biến, một bộ khuếch đại ngưỡng, ba rơ-le và cả hai van. "
        "Không có phần tử nào dư thừa, nên mọi hỏng hóc đều dẫn tới mất chức năng hoặc cắt nhầm.",
        "Each safety function uses one transmitter, one trip amplifier, three relays and both valves. "
        "Nothing is redundant, so every failure either loses the function or trips the plant.",
        "Hình 14-2. Hệ an toàn đề xuất cho Ca 1. Hai cảm biến đơn đưa vào một khối logic rơ-le, khối này "
        "đóng hai van cắt độc lập. Không có dự phòng ở bất kỳ đâu: một cảm biến hỏng là mất một chức năng, "
        "một rơ-le hỏng là mất luôn chức năng ấy, và một van hỏng là mất cả hai.",
        "Figure 14-2. Proposed safety system for Case 1. Two single transmitters feed one relay-logic "
        "block, which closes two independent shutdown valves. There is no redundancy anywhere: a failed "
        "transmitter loses one function, a failed relay loses it too, and a failed valve loses both.",
        "Sơ đồ khối: hai cảm biến đơn nối vào một khối logic rơ-le, khối này nối ra hai van cắt.",
        "A block diagram: two single transmitters into one relay-logic block, which drives two shutdown "
        "valves.")


def fig_14_3():
    """Case 2: triplicated transmitters, fault-tolerant PLC, single valves."""
    return _arch(
        [("3 cảm biến lưu lượng A", "2oo3"), ("3 cảm biến lưu lượng B", "2oo3")],
        ("PLC an toàn 2oo3", ["tự chẩn đoán", "chịu lỗi một kênh"]),
        [("Van cắt lưu lượng A", "1oo1"), ("Van cắt lưu lượng B", "1oo1")],
        "Ca 2: cảm biến ba kênh, PLC an toàn, van đơn",
        "Cảm biến và bộ xử lý đều chịu được một hỏng hóc, nhưng van thì không — van trở thành mắt xích "
        "yếu, và chính nó quyết định cả PFD lẫn tần suất cắt nhầm của cả hệ.",
        "Sensors and logic now tolerate a failure, but the valves do not — the valve becomes the weak link, "
        "and it alone sets both the PFD and the spurious trip rate of the whole system.",
        "Hình 14-3. Hệ an toàn đề xuất cho Ca 2. Cảm biến ba kênh bỏ phiếu 2oo3 và một PLC an toàn chịu "
        "lỗi, nhưng van vẫn là van đơn. Vì thế PFD tổng chỉ còn 0,01 — giới hạn của SIL 1 — và toàn bộ "
        "phần dư thừa ấy không cải thiện được gì cho van.",
        "Figure 14-3. Proposed safety system for Case 2. Triplicated 2oo3 transmitters and a fault-tolerant "
        "safety PLC, but the valves are still single. The total PFD falls to 0.01 — the SIL 1 limit — and "
        "none of that redundancy does anything for the valves.",
        "Sơ đồ khối: hai nhóm ba cảm biến bỏ phiếu 2oo3 nối vào một PLC an toàn 2oo3, PLC nối ra hai van "
        "cắt đơn.",
        "A block diagram: two groups of three 2oo3 transmitters into a 2oo3 safety PLC, which drives two "
        "single shutdown valves.")


# ---------------------------------------------------------------- 14.9 (added)
def fig_14_4():
    """Lifecycle cost: case 2 costs more up front and less over twenty years."""
    o = [_txt(330, 20, "Ca 2 đắt hơn lúc mua, rẻ hơn sau hai mươi năm",
              8.2, weight="600")]

    base = 300
    top = 78
    span = base - top            # pixels for 700,000 $
    per_k = span / 700.0

    def yv(v):
        return base - (v / 1000.0) * per_k

    # axis
    o.append(_line(120, base, 620, base, sw=1.2, color=INK))
    o.append(_line(120, base, 120, top - 8, sw=1.2, color=INK))
    for v in (0, 200000, 400000, 600000):
        y = yv(v)
        o.append(_line(114, y, 120, y, sw=1.0))
        o.append(_txt(108, y + 3, "%d" % (v // 1000), 5.4, anchor="end", color=GREY))
    o.append(_vtxt(92, 200, "nghìn đô-la", 5.6))

    bars = [("Ca 1", 196, CASE1_INIT, CASE1_PV, CASE1_TOT),
            ("Ca 2", 420, CASE2_INIT, CASE2_PV, CASE2_TOT)]
    bw = 116
    for name, x, init, pv, tot in bars:
        y1 = yv(init)
        y2 = yv(init + pv)
        o.append(_rect(x, y1, bw, base - y1, "#dce6f2", sw=1.1, stroke="#8fa6bf"))
        o.append(_rect(x, y2, bw, y1 - y2, "#f2e3c2", sw=1.1, stroke="#c0a878"))
        o.append(_txt(x + bw / 2, y1 + (base - y1) / 2 + 4, "%d" % (init // 1000), 6.0,
                      color="#2c3e50", weight="600"))
        o.append(_txt(x + bw / 2, y2 + (y1 - y2) / 2 + 4, "%d" % (pv // 1000), 6.0,
                      color="#6b5322", weight="600"))
        o.append(_txt(x + bw / 2, base + 18, name, 7.0, weight="600"))
        o.append(_line(x + bw / 2, y2 - 4, x + bw / 2, y2 - 14, sw=1.0, color=INK))
        o.append(_txt(x + bw / 2, y2 - 18, "tổng %d" % (tot // 1000), 6.0, weight="600"))

    # the difference in totals
    ya, yb = yv(CASE1_TOT), yv(CASE2_TOT)
    o.append(_line(312, ya, 336, ya, sw=1.0, color=DARKRED, dash="3 3"))
    o.append(_line(312, yb, 336, yb, sw=1.0, color=DARKRED, dash="3 3"))
    o.append(_line(330, ya, 330, yb, sw=1.0, color=DARKRED))
    o.append(_arrow(330, yb - 2, 330, yb + 2, sw=1.0, color=DARKRED))
    o.append(_arrow(330, ya + 2, 330, ya - 2, sw=1.0, color=DARKRED))
    o.append(_txt(336, (ya + yb) / 2 - 2, "chênh", 5.4, anchor="start", color=DARKRED))
    o.append(_txt(336, (ya + yb) / 2 + 8, "74.160 $", 5.4, anchor="start", color=DARKRED,
                  weight="600"))

    # legend
    o.append(_rect(120, 330, 12, 9, "#dce6f2", sw=1.0, stroke="#8fa6bf"))
    o.append(_txt(138, 337, "chi phí cố định ban đầu", 5.4, anchor="start", color=GREY))
    o.append(_rect(280, 330, 12, 9, "#f2e3c2", sw=1.0, stroke="#c0a878"))
    o.append(_txt(298, 337, "hiện giá chi phí hằng năm (20 năm, 5 %)", 5.4, anchor="start",
                  color=GREY))

    o.append(_txt(330, 356, "Số liệu lấy nguyên từ Bảng 14-3 và Bảng 14-4. Cột thấp hơn không phải "
                            "cột rẻ hơn lúc mua — nó chỉ rẻ hơn khi tính hết hai mươi năm.",
                  5.4, color=GREY))

    return _finish(o, 660, 370,
                   "Hình 14-4 (bổ sung). So sánh chi phí vòng đời của hai ca, dựng từ chính Bảng 14-3 và "
                   "Bảng 14-4 của sách. Ca 2 đắt hơn 38.000 $ ở phần chi phí cố định ban đầu, nhưng rẻ hơn "
                   "112.160 $ ở phần hiện giá chi phí hằng năm, nên tổng cộng rẻ hơn 74.160 $. Đây là toàn "
                   "bộ lập luận của mục 14.9 trong một hình: quyết định dựa trên chi phí ban đầu sẽ chọn "
                   "sai.",
                   "Figure 14-4 (added). Lifecycle cost of the two cases, built from the book's own "
                   "Tables 14-3 and 14-4. Case 2 costs $38,000 more in initial fixed costs but $112,160 "
                   "less in present value of annual costs, so it is $74,160 cheaper overall. That is the "
                   "whole argument of section 14.9 in one picture: a decision made on first cost alone "
                   "picks the wrong system.",
                   "Biểu đồ cột xếp chồng so sánh chi phí cố định ban đầu và hiện giá chi phí hằng năm của "
                   "hai phương án, với tổng chi phí vòng đời của mỗi phương án.",
                   "A stacked bar chart comparing initial fixed cost and present value of annual costs for "
                   "the two options, with each option's total lifecycle cost.")


FIGURES = [fig_14_1, fig_14_2, fig_14_3, fig_14_4]
