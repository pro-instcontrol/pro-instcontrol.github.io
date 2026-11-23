# -*- coding: utf-8 -*-
"""Vector figures for Chapter 12 "Safety Instrumented Systems" of Emerson,
*Control Valve Handbook*, 6th ed. (2020), printed pp. 250-259.

Five faithful vector redrawings ``fig_f12_01`` ... ``fig_f12_05``. Each
function is registered with :func:`_reg` and returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)`` through :func:`_finish`.
All text goes through :func:`T` / :func:`esc` so no bare ampersand can reach
an SVG attribute. Figure 12.4 is a redrawn bar chart whose heights are
illustrative: the printed source gives only the axes and category labels,
so no exact numeric bar values are claimed.
"""
from cvh6fig import (_reg, _finish, esc, T, _defs, _rect, _line, _circle, _poly, _arrow, svg, INK, GREY, BLUE, RED, GREEN)
from vfig import GOLD, FILL, PAPER
# Bind the canonical shared registry itself; no per-chapter alias is defined.
from cvh6fig import FIGS  # noqa: F401


def _wrap(s, limit):
    """Break a label into lines of at most `limit` characters."""
    out, cur = [], ""
    for wd in str(s).split():
        if cur and len(cur) + 1 + len(wd) > limit:
            out.append(cur)
            cur = wd
        else:
            cur = (cur + " " + wd).strip()
    if cur:
        out.append(cur)
    return out


# ---------------------------------------------------------------------------
# Figure 12.1 - Layers of Protection (printed p. 251)
# ---------------------------------------------------------------------------
@_reg
def fig_f12_01():
    """Figure 12.1 (p. 251) - The layers of protection, drawn as a pyramid."""
    w, h = 680, 440
    o = [_defs()]
    o.append(T(340, 28, "Các lớp bảo vệ / Layers of Protection", 9.2,
               weight="600"))
    o.append(T(340, 47,
               "An toàn được đảm bảo bằng các lớp bảo vệ xếp chồng / "
               "Safety is provided by layers of protection",
               7.2, color=GREY))

    # Bands listed bottom-up; the drawing runs from the top of the pyramid.
    layers = [
        ("Lớp điều khiển quy trình (BPCS)", "Process Control Layer (BPCS)",
         "#e7f0fb", BLUE,
         "Bình thường → Cảnh báo → Can thiệp",
         "Normal → Process alarm → Operator intervention"),
        ("Lớp an toàn (SIS)", "Safety Layer (SIS)",
         "#eef7ee", GREEN,
         "Dừng khẩn cấp", "Emergency shutdown"),
        ("Lớp bảo vệ chủ động", "Active Protection Layer",
         "#fdf3e6", GOLD,
         "Hệ thống phòng cháy và khí", "Fire and gas system"),
        ("Lớp bảo vệ thụ động", "Passive Protection Layer",
         "#f3ecf7", "#6b4c8a",
         "Ngăn chứa, đê hoặc bồn chứa", "Containment, dike or vessel"),
        ("Lớp ứng phó khẩn cấp", "Emergency Response Layer",
         "#fdeaea", RED,
         "Ứng phó của nhà máy", "Plant and emergency response"),
    ]
    cx, y_top, row_h = 300, 80, 64
    y_bot = y_top + row_h * len(layers)

    def hw(yy):
        return 60 + 110.0 * (yy - y_top) / float(y_bot - y_top)

    for idx, (vi, en, fill, color, tvi, ten) in enumerate(reversed(layers)):
        y0 = y_top + idx * row_h
        y1 = y0 + row_h
        o.append(_poly([(cx - hw(y0), y0), (cx + hw(y0), y0),
                        (cx + hw(y1), y1), (cx - hw(y1), y1)],
                       fill=fill, sw=1.2, close=True))
        o.append(T(cx, y0 + 20, vi, 7.8, weight="600", color=color))
        o.append(T(cx, y0 + 32, en, 7.0, color=INK))
        o.append(T(cx, y0 + 46, tvi, 6.5, color=GREY))
        o.append(T(cx, y0 + 57, ten, 6.2, color=GREY))

    # Prevent / Mitigate brackets on the left, meeting at the incident.
    o.append(T(88, 200, "Ngăn ngừa / Prevent", 7.2, weight="600",
               color=BLUE, anchor="end"))
    o.append(_line(100, 228, 100, 400, sw=1.2, color=BLUE))
    o.append(_line(100, 228, 116, 228, sw=1.2, color=BLUE))
    o.append(_line(100, 400, 116, 400, sw=1.2, color=BLUE))
    o.append(T(88, 222, "Sự cố / Incident", 6.8, color=RED, anchor="end"))
    o.append(T(88, 116, "Giảm nhẹ / Mitigate", 7.2, weight="600",
               color=RED, anchor="end"))
    o.append(_line(100, 80, 100, 212, sw=1.2, color=RED))
    o.append(_line(100, 80, 116, 80, sw=1.2, color=RED))
    o.append(_line(100, 212, 116, 212, sw=1.2, color=RED))

    # Escalation triggers on the right.
    o.append(_rect(490, 80, 170, 320, fill="#ffffff", sw=1.1))
    o.append(_rect(490, 80, 170, 30, fill="#e9eef4", sw=1.0))
    o.append(T(575, 99, "Kịch bản leo thang / Escalation", 7.6,
               weight="600"))
    steps = [
        ("Hành vi bình thường", "Normal Behavior"),
        ("Cảnh báo quy trình", "Process Alarm"),
        ("Can thiệp của người vận hành", "Operator Intervention"),
        ("Dừng khẩn cấp", "Emergency Shutdown"),
    ]
    for i, (vi, en) in enumerate(steps):
        yy = 132 + i * 64
        o.append(_circle(510, yy - 3, 3.0, fill=BLUE, sw=0))
        o.append(T(522, yy, vi, 7.4, weight="600", anchor="start"))
        o.append(T(522, yy + 12, en, 6.8, color=GREY, anchor="start"))
        if i < 3:
            o.append(_arrow(510, yy + 16, 510, yy + 52, sw=1.2,
                            color=GREY))
    o.append(T(575, 386,
               "Từ vận hành bình thường đến dừng an toàn / "
               "From normal operation to a safe shutdown",
               6.8, color=GREY))
    return _finish(
        w, h, o,
        "Figure 12.1 (p. 251) - Layers of Protection",
        "Hình 12.1 (tr. 251) · Các lớp bảo vệ / "
        "Figure 12.1 (p. 251) - Layers of Protection",
        "Hình 12.1 (tr. 251) · Các lớp bảo vệ · Năm lớp xếp từ dưới lên: lớp điều khiển quy trình "
        "(BPCS, gồm vận hành bình thường, cảnh báo quy trình và can thiệp của người vận hành), lớp "
        "an toàn (SIS, dừng khẩn cấp), lớp bảo vệ chủ động, lớp bảo vệ thụ động và lớp ứng phó khẩn "
        "cấp. Hai lớp dưới ngăn ngừa sự cố, ba lớp trên giảm nhẹ hậu quả; cột bên phải liệt kê các "
        "kịch bản leo thang.",
        "Figure 12.1 (p. 251) - Layers of Protection · Five layers stacked from the bottom up: "
        "the process control layer (BPCS, with normal behavior, process alarm and operator "
        "intervention), the safety layer (SIS, emergency shutdown), the active protection layer, "
        "the passive protection layer and the emergency response layer. The lower layers prevent "
        "an incident, the upper layers mitigate its impact; the right column lists the escalation "
        "triggers.",
        "Sơ đồ Hình 12.1 (tr. 251) năm lớp bảo vệ xếp chồng từ BPCS đến ứng phó khẩn cấp",
        "Diagram of Figure 12.1 (p. 251) five stacked protection layers from BPCS to emergency response")


# ---------------------------------------------------------------------------
# Figure 12.2 - Components of a SIS (printed p. 252)
# ---------------------------------------------------------------------------
@_reg
def fig_f12_02():
    """Figure 12.2 (p. 252) - Sensor, logic solver and final element flow."""
    w, h = 680, 350
    o = [_defs()]
    o.append(T(340, 28,
               "Thành phần của Hệ thống an toàn bằng dụng cụ (SIS) / "
               "Components of a Safety Instrumented System (SIS)",
               8.6, weight="600"))
    o.append(T(340, 47,
               "Mỗi hàm an toàn bằng dụng cụ (SIF) là một vòng gồm ba phần tử / "
               "Each safety instrumented function (SIF) is a loop of three elements",
               7.2, color=GREY))

    boxes = [
        (30, "CẢM BIẾN / SENSORS", "#e7f0fb", BLUE, [
            ("Đo nhiệt độ, áp suất,", "Measure temperature, pressure,"),
            ("lưu lượng, mật độ", "flow and density"),
            ("Chuyên dụng cho SIS", "Dedicated to SIS service"),
            ("Điểm lấy mẫu riêng biệt", "Separate, distinct process taps"),
            ("Từ công tắc đến bộ phát", "From simple switches to smart"),
            ("thông minh", "transmitters with diagnostics"),
        ]),
        (250, "BỘ GIẢI LOGIC / LOGIC SOLVER", "#eef7ee", GREEN, [
            ("Quyết định hành động", "Determines the action to be"),
            ("cần thực hiện", "taken from gathered information"),
            ("An toàn khi mất điện,", "Provides fail-safe and"),
            ("chịu lỗi", "fault-tolerant operation"),
            ("Lập trình được hoặc", "Programmable or non-programmable,"),
            ("cơ khí", "or mechanical devices"),
        ]),
        (470, "PHẦN TỬ ĐIỀU KHIỂN CUỐI / FINAL CONTROL ELEMENT",
         "#fdeaea", RED, [
             ("Thực hiện hành động đã", "Implements the action"),
             ("quyết định", "determined by the logic solver"),
             ("Thường là van đóng hoặc", "Typically an automated"),
             ("mở tự động", "on/off valve"),
             ("Chức năng fail-closed", "Fail-closed or fail-open"),
             ("hoặc fail-open", "function"),
         ]),
    ]
    for x, title, fill, color, lines in boxes:
        o.append(_rect(x, 78, 180, 206, fill="#ffffff", sw=1.2))
        o.append(_rect(x, 78, 180, 32, fill=fill, sw=1.0))
        o.append(T(x + 90, 98, title, 7.0, weight="600", color=color))
        yy = 124
        for vi, en in lines:
            o.append(T(x + 90, yy, vi, 6.9))
            o.append(T(x + 90, yy + 11, en, 6.4, color=GREY))
            yy += 26
    o.append(_arrow(210, 180, 248, 180, sw=1.8, color=BLUE))
    o.append(_arrow(430, 180, 468, 180, sw=1.8, color=BLUE))
    o.append(T(229, 168, "Tín hiệu / Signal", 6.6, color=BLUE))
    o.append(T(449, 168, "Lệnh / Output", 6.6, color=BLUE))
    o.append(T(340, 306,
               "Ba phần tử phải hoạt động đúng thiết kế để đưa quy trình về trạng thái an toàn / "
               "All three elements must function as designed to bring the process to a safe state",
               7.0, weight="600"))
    o.append(T(340, 324,
               "Sơ đồ dòng tín hiệu theo mục 12.2 · vẽ lại dạng vector / "
               "Signal-flow diagram per section 12.2 · redrawn as a vector",
               6.8, color=GREY))
    return _finish(
        w, h, o,
        "Figure 12.2 (p. 252) - Components of a Safety Instrumented System (SIS)",
        "Hình 12.2 (tr. 252) · Thành phần của Hệ thống an toàn bằng dụng cụ / "
        "Figure 12.2 (p. 252) - Components of a Safety Instrumented System (SIS)",
        "Hình 12.2 (tr. 252) · Thành phần của Hệ thống an toàn bằng dụng cụ · Sơ đồ dòng tín hiệu "
        "từ cảm biến đo nhiệt độ, áp suất, lưu lượng và mật độ qua điểm lấy mẫu riêng, đến bộ giải "
        "logic quyết định hành động với chế độ fail-safe và fault-tolerant, rồi tới phần tử điều "
        "khiển cuối là van đóng hoặc mở tự động. Cả ba phần tử phải hoạt động đúng để đưa quy "
        "trình về trạng thái an toàn.",
        "Figure 12.2 (p. 252) - Components of a Safety Instrumented System (SIS) · Signal-flow "
        "diagram from sensors measuring temperature, pressure, flow and density through dedicated "
        "process taps, to a logic solver that decides the action with fail-safe and fault-tolerant "
        "operation, and on to a final control element that is typically an automated on/off valve. "
        "All three elements must function as designed to bring the process to a safe state.",
        "Sơ đồ Hình 12.2 (tr. 252) dòng tín hiệu cảm biến, bộ giải logic và phần tử điều khiển cuối",
        "Diagram of Figure 12.2 (p. 252) signal flow sensor, logic solver and final control element")


# ---------------------------------------------------------------------------
# Figure 12.3 - SIL, PFDavg and RRF table (printed p. 253)
# ---------------------------------------------------------------------------
@_reg
def fig_f12_03():
    """Figure 12.3 (p. 253) - The exact four-row SIL data table."""
    w, h = 680, 350
    o = [_defs()]
    o.append(T(340, 28,
               "Mức toàn vẹn an toàn và số liệu PFDavg, RRF tương ứng / "
               "Safety Integrity Levels and Associated PFDavg and RRF Figures",
               8.2, weight="600"))
    o.append(T(340, 47,
               "Bốn mức SIL theo IEC; ISA S84.01 chỉ công nhận đến SIL 3 / "
               "Four SIL levels per IEC; ISA S84.01 recognizes only up to SIL 3",
               7.2, color=GREY))

    cols = [
        (40, 200, "RRF", "Hệ số giảm rủi ro", "Risk Reduction Factor"),
        (240, 280, "PFDavg", "Xác suất hỏng khi yêu cầu",
         "Probability of Failure on Demand"),
        (520, 120, "SIL", "Mức toàn vẹn an toàn", "Safety Integrity Level"),
    ]
    for x, cw, main, vi, en in cols:
        o.append(_rect(x, 70, cw, 52, fill="#e9eef4", sw=1.1))
        o.append(T(x + cw / 2.0, 88, main, 9.2, weight="600"))
        o.append(T(x + cw / 2.0, 101, vi, 6.6))
        o.append(T(x + cw / 2.0, 112, en, 6.2, color=GREY))

    rows = [
        ("100000 đến 10000", "100000 to 10000",
         ">=10^-5 đến <10^-4", ">=10^-5 to <10^-4", "SIL 4"),
        ("10000 đến 1000", "10000 to 1000",
         ">=10^-4 đến <10^-3", ">=10^-4 to <10^-3", "SIL 3"),
        ("1000 đến 100", "1000 to 100",
         ">=10^-3 đến <10^-2", ">=10^-3 to <10^-2", "SIL 2"),
        ("100 đến 10", "100 to 10",
         ">=10^-2 đến <10^-1", ">=10^-2 to <10^-1", "SIL 1"),
    ]
    for i, (rrf_vi, rrf_en, pfd_vi, pfd_en, sil) in enumerate(rows):
        y0 = 122 + i * 48
        fill = "#ffffff" if i % 2 == 0 else "#f6f8fb"
        for x, cw, _, _, _ in cols:
            o.append(_rect(x, y0, cw, 48, fill=fill, sw=1.0))
        o.append(T(140, y0 + 20, rrf_vi, 8.0, weight="600"))
        o.append(T(140, y0 + 36, rrf_en, 7.2, color=GREY))
        o.append(T(380, y0 + 20, pfd_vi, 8.0, weight="600"))
        o.append(T(380, y0 + 36, pfd_en, 7.2, color=GREY))
        o.append(T(580, y0 + 29, sil, 10.0, weight="600", color=BLUE))
    o.append(T(340, 326,
               "PFDavg = 1/RRF · ký hiệu ^ biểu thị lũy thừa / "
               "PFDavg = 1/RRF · the caret denotes a power",
               6.8, color=GREY))
    return _finish(
        w, h, o,
        "Figure 12.3 (p. 253) - Safety Integrity Levels and Associated PFDavg and RRF Figures",
        "Hình 12.3 (tr. 253) · Mức toàn vẹn an toàn và số liệu PFDavg, RRF / "
        "Figure 12.3 (p. 253) - Safety Integrity Levels and Associated PFDavg and RRF Figures",
        "Hình 12.3 (tr. 253) · Mức toàn vẹn an toàn và số liệu PFDavg, RRF tương ứng · Bảng ba cột "
        "với bốn dòng: RRF từ 100000 đến 10000, PFDavg từ 10^-5 đến dưới 10^-4, SIL 4; RRF từ "
        "10000 đến 1000, PFDavg từ 10^-4 đến dưới 10^-3, SIL 3; RRF từ 1000 đến 100, PFDavg từ "
        "10^-3 đến dưới 10^-2, SIL 2; RRF từ 100 đến 10, PFDavg từ 10^-2 đến dưới 10^-1, SIL 1. "
        "PFDavg bằng 1 chia cho RRF.",
        "Figure 12.3 (p. 253) - Safety Integrity Levels and Associated PFDavg and RRF Figures · "
        "A three-column table with four rows: RRF 100000 to 10000, PFDavg at least 10^-5 and less "
        "than 10^-4, SIL 4; RRF 10000 to 1000, PFDavg at least 10^-4 and less than 10^-3, SIL 3; "
        "RRF 1000 to 100, PFDavg at least 10^-3 and less than 10^-2, SIL 2; RRF 100 to 10, PFDavg "
        "at least 10^-2 and less than 10^-1, SIL 1. PFDavg equals 1 divided by RRF.",
        "Bảng Hình 12.3 (tr. 253) bốn mức SIL với giá trị PFDavg và RRF tương ứng",
        "Table of Figure 12.3 (p. 253) four SIL levels with matching PFDavg and RRF values")


# ---------------------------------------------------------------------------
# Figure 12.4 - OREDA Data bar chart (printed p. 255)
# ---------------------------------------------------------------------------
@_reg
def fig_f12_04():
    """Figure 12.4 (p. 255) - Illustrative distribution of SIF failures."""
    w, h = 680, 350
    o = [_defs()]
    o.append(T(340, 28, "Số liệu OREDA / OREDA Data", 9.2, weight="600"))
    o.append(T(340, 47,
               "Phân bổ hỏng hóc trong một hàm an toàn theo OREDA / "
               "Distribution of failures within a SIF per OREDA",
               7.2, color=GREY))

    x0, y_top, y0 = 100, 76, 282

    def yv(v):
        return y0 - 4.12 * v

    o.append(_line(x0, y_top, x0, y0, sw=1.4, color=INK))
    o.append(_line(x0, y0, 640, y0, sw=1.4, color=INK))
    for v in (0, 10, 20, 30, 40, 50):
        yy = yv(v)
        o.append(_line(x0 - 5, yy, x0, yy, sw=1.0, color=INK))
        o.append(T(x0 - 10, yy + 3, str(v), 7.6, anchor="end"))
        if v:
            o.append(_line(x0, yy, 640, yy, sw=0.5, color="#d9dee5"))
    o.append(T(x0 - 10, 68, "%", 7.6, anchor="end", weight="600"))

    bars = [
        (190, 12, "Cảm biến / Sensor", "Sensor", "#cddcf0", BLUE),
        (360, 8, "Bộ giải logic /", "Logic Solver", "#cfe6d3", GREEN),
        (535, 45, "Phần tử điều khiển", "Final Control Element",
         "#f4b8b8", RED),
    ]
    for cx, val, vi, en, fill, color in bars:
        top = yv(val)
        o.append(_rect(cx - 40, top, 80, y0 - top, fill=fill, sw=1.2,
                       stroke=color))
        o.append(T(cx, top - 6, "%d%%" % val, 8.0, weight="600",
                   color=color))
    o.append(T(360, 300, "Logic Solver / Bộ giải logic", 6.6, color=GREY))
    o.append(T(190, 300, "Cảm biến / Sensor", 6.6, color=GREY))
    o.append(T(535, 300, "Phần tử điều khiển cuối /", 6.6, color=GREY))
    o.append(T(535, 311, "Final Control Element", 6.6, color=GREY))
    o.append(T(340, 326,
               "Chiều cao cột chỉ mang tính minh họa · nguồn chỉ nêu trục và nhãn / "
               "Bar heights are illustrative · source gives only axes and category labels",
               6.8, color=GREY))
    return _finish(
        w, h, o,
        "Figure 12.4 (p. 255) - OREDA Data",
        "Hình 12.4 (tr. 255) · Số liệu OREDA / "
        "Figure 12.4 (p. 255) - OREDA Data",
        "Hình 12.4 (tr. 255) · Số liệu OREDA · Biểu đồ cột theo trục phần trăm 0 đến 50 và ba "
        "nhóm cảm biến, bộ giải logic, phần tử điều khiển cuối, nhấn mạnh rằng phần tử điều khiển "
        "cuối chiếm tỷ trọng hỏng hóc lớn nhất. Chiều cao các cột chỉ mang tính minh họa: bản in "
        "không cho số liệu cụ thể, chỉ có trục tung, trục hoành và nhãn ba nhóm.",
        "Figure 12.4 (p. 255) - OREDA Data · A bar chart on a 0 to 50 percent axis with three "
        "categories, sensor, logic solver and final control element, stressing that the final "
        "control element accounts for the largest share of failures. The bar heights are "
        "illustrative: the print gives no numeric bar values, only the axes and the three category "
        "labels.",
        "Biểu đồ cột Hình 12.4 (tr. 255) phân bổ hỏng hóc theo OREDA, chiều cao minh họa",
        "Bar chart of Figure 12.4 (p. 255) illustrative OREDA failure distribution by category")


# ---------------------------------------------------------------------------
# Figure 12.5 - Typical HIPPS Configuration (printed p. 258)
# ---------------------------------------------------------------------------
@_reg
def fig_f12_05():
    """Figure 12.5 (p. 258) - A typical HIPPS line schematic."""
    w, h = 680, 390
    o = [_defs()]
    o.append(T(340, 28,
               "Cấu hình HIPPS điển hình / Typical HIPPS Configuration",
               9.2, weight="600"))
    o.append(T(340, 47,
               "Hệ thống bảo vệ áp suất toàn vẹn cao ngăn quá áp / "
               "A high-integrity pressure protection system prevents overpressure",
               7.2, color=GREY))

    # Process pipe with flow arrow.
    o.append(_rect(50, 164, 500, 12, fill="#e9eef4", sw=1.2))
    o.append(_arrow(470, 170, 540, 170, sw=1.8, color=GREEN))
    o.append(T(505, 156, "Dòng quy trình / Process flow", 6.8,
               color=GREEN, weight="600"))

    # Three pressure transmitters voting 2oo3 on the upstream side.
    for i, px in enumerate((110, 160, 210), start=1):
        o.append(_line(px, 164, px, 128, sw=1.0, color=INK))
        o.append(_circle(px, 118, 10, fill="#e7f0fb", sw=1.2))
        o.append(T(px, 121, "PT%d" % i, 6.4, weight="600"))
    o.append(T(160, 98,
               "Cảm biến và bộ phát áp suất (2oo3) / Pressure transmitters (2oo3)",
               7.0, weight="600", color=BLUE))

    # Two series shutdown valves, the final elements.
    for vx, lab in ((360, "SDV-1"), (440, "SDV-2")):
        o.append(_poly([(vx - 18, 156), (vx, 170), (vx - 18, 184)],
                       fill="#fdeaea", sw=1.3, close=True))
        o.append(_poly([(vx + 18, 156), (vx, 170), (vx + 18, 184)],
                       fill="#fdeaea", sw=1.3, close=True))
        o.append(_rect(vx - 12, 138, 24, 16, fill="#e9eef4", sw=1.0))
        o.append(T(vx, 134, lab, 6.6, color=RED, weight="600"))
    o.append(T(400, 202,
               "Van ngắt (1oo2) / Shutdown valves (1oo2)",
               6.8, weight="600", color=RED))

    # Protected vessel on the low-pressure side.
    o.append(_rect(555, 132, 96, 86, fill="#f4f7fb", sw=1.4))
    o.append(_line(550, 170, 555, 170, sw=1.4, color=INK))
    o.append(T(603, 164, "Bình chứa hoặc", 6.8, weight="600"))
    o.append(T(603, 176, "thiết bị được bảo vệ", 6.8, weight="600"))
    o.append(T(603, 191, "Vessel or protected", 6.4, color=GREY))
    o.append(T(603, 202, "equipment", 6.4, color=GREY))

    # Logic solver and the dashed trip signal path.
    o.append(_rect(260, 262, 160, 46, fill="#eef7ee", sw=1.3))
    o.append(T(340, 280, "Bộ giải logic / Logic Solver", 7.6,
               weight="600", color=GREEN))
    o.append(T(340, 295, "2oo3 đến 1oo2 / 2oo3 to 1oo2", 6.6,
               color=GREY))
    for px in (110, 160, 210):
        o.append(_line(px, 128, px, 250, sw=1.0, dash="4,3", color=RED))
        o.append(_line(px, 250, 300, 250, sw=1.0, dash="4,3", color=RED))
        o.append(_line(300, 250, 300, 262, sw=1.0, dash="4,3", color=RED))
    for vx in (360, 440):
        o.append(_line(400, 262, 400, 244, sw=1.0, dash="4,3", color=RED))
        o.append(_line(400, 244, vx, 244, sw=1.0, dash="4,3", color=RED))
        o.append(_arrow(vx, 244, vx, 156, sw=1.0, dash="4,3",
                        color=RED))

    o.append(T(340, 334,
               "Đường liền là quy trình · đường gạch đứt là tín hiệu ngắt / "
               "Solid lines show process · dashed lines show the trip signal path",
               6.8, color=GREY))
    o.append(T(340, 352,
               "HIPPS đóng nguồn và giữ áp phía thượng nguồn · vẽ lại theo mục 12.10 đến 12.12 / "
               "HIPPS shuts off the source and holds pressure upstream · redrawn per sections 12.10 to 12.12",
               6.4, color=GREY))
    return _finish(
        w, h, o,
        "Figure 12.5 (p. 258) - Typical HIPPS Configuration",
        "Hình 12.5 (tr. 258) · Cấu hình HIPPS điển hình / "
        "Figure 12.5 (p. 258) - Typical HIPPS Configuration",
        "Hình 12.5 (tr. 258) · Cấu hình HIPPS điển hình · Sơ đồ đường quy trình có ba bộ phát áp "
        "suất ở phía thượng nguồn theo cấu hình 2oo3, đường tín hiệu ngắt gạch đứt dẫn tới bộ giải "
        "logic, rồi tới hai van ngắt mắc nối tiếp 1oo2 cô lập bình chứa hoặc thiết bị được bảo vệ "
        "phía hạ nguồn khi áp suất vượt giới hạn.",
        "Figure 12.5 (p. 258) - Typical HIPPS Configuration · A process line with three upstream "
        "pressure transmitters in a 2oo3 voting arrangement, a dashed trip signal path to the "
        "logic solver, and two shutdown valves in a series 1oo2 arrangement that isolate the "
        "vessel or protected equipment on the downstream side when pressure exceeds the limit.",
        "Sơ đồ Hình 12.5 (tr. 258) cấu hình HIPPS gồm cảm biến áp suất, bộ giải logic và van ngắt",
        "Diagram of Figure 12.5 (p. 258) HIPPS configuration with pressure transmitters, logic solver and shutdown valve")
