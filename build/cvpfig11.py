# -*- coding: utf-8 -*-
"""Vector figures for Book 7 - Baumann, *Control Valve Primer*, 5th ed.

Chapter 11 "The Mystery of Line Pressure-Produced Valve Stem Forces":
simplified vector re-drawings of source Figures 11-1 to 11-3.  Each function
returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)``.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, FILL, GREEN, GREY, INK, RED, _arrow, _box, _circle,
                  _defs, _ellipse, _f, _fig, _line, _path, _poly, _rect,
                  _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f
    return f


def esc(s):
    s = str(s)
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return s.replace('"', "&quot;")


@_reg
def fig_f111():
    """Figure 11-1 - simplified ISA control valve data sheet (P1 highlighted)."""
    w, h = 680, 552
    o = [_defs()]
    o.append(_txt(340, 17, esc("CONTROL VALVE DATA SHEET"), 11.4,
                  color=INK, weight="600"))
    o.append(_txt(36, 31, esc("ISA FORM S20.50 Rev.1 (1981)"), 7.4,
                  anchor="start", color=GREY))
    o.append(_txt(644, 31, esc("Simplified redrawing - not a facsimile"), 7.4,
                  anchor="end", color=GREY))

    # form outline
    o.append(_rect(32, 42, 616, 474, fill="#fdfcf9", sw=1.4, stroke=INK))

    # ---- header fields -------------------------------------------------
    o.append(_line(340, 42, 340, 106, sw=1.0, color="#9fa8b3"))

    def hdr(x, y, label):
        o.append(_txt(x, y + 9, esc(label), 7.2, anchor="start",
                      color=GREY, weight="600"))
        o.append(_line(x + 74, y + 9, x + 296, y + 9, sw=0.8,
                       color="#9fa8b3"))

    for i, lab in enumerate(("PROJECT", "UNIT", "TAG", "SERVICE")):
        hdr(38, 46 + i * 15, lab)
    for i, lab in enumerate(("DATA SHEET", "SPEC NO", "PO NO", "DWO NO")):
        hdr(344, 46 + i * 15, lab)

    # ---- shared blocks -------------------------------------------------
    def band(y, title):
        o.append(_rect(34, y, 612, 12, fill="#dfe6ee", sw=0.9,
                       stroke="#9fa8b3"))
        o.append(_txt(40, y + 9, esc(title), 7.8, anchor="start",
                      color=INK, weight="600"))

    def spec_field(x, y, ww, hh, label):
        o.append(_rect(x, y, ww, hh, fill="#ffffff", sw=0.9,
                       stroke="#b9bec4"))
        o.append(_txt(x + 4, y + 9, esc(label), 6.8, anchor="start",
                      color=GREY, weight="600"))
        o.append(_line(x + 4, y + hh - 6, x + ww - 4, y + hh - 6,
                       sw=0.7, color="#c9cdd2"))

    def cell(x, y, ww, hh, text="", hi=False, head=False,
             size=7.0, anchor="middle"):
        fill = "#dfe6ee" if head else ("#fff3cd" if hi else "#ffffff")
        stroke = "#9fa8b3" if head else (RED if hi else "#b9bec4")
        sw = 0.9 if head else (1.5 if hi else 0.8)
        o.append(_rect(x, y, ww, hh, fill=fill, sw=sw, stroke=stroke))
        if text:
            color = INK if head else (RED if hi else INK)
            tx = x + (ww / 2.0 if anchor == "middle" else 3)
            o.append(_txt(tx, y + hh / 2.0 + size * 0.36, esc(text),
                          size, anchor=anchor, color=color,
                          weight="600" if (head or hi) else ""))

    # ---- PROCESS CONDITIONS -------------------------------------------
    band(110, "PROCESS CONDITIONS")
    tx, ty = 34, 122
    colw = [40, 156, 56, 92, 92, 92, 84]
    colx = [tx]
    for cw in colw[:-1]:
        colx.append(colx[-1] + cw)
    heads = ("No.", "Condition", "Units", "Max Flow", "Norm Flow",
             "Cv / Min Flow", "Shut Off")
    for i, lab in enumerate(heads):
        cell(colx[i], ty, colw[i], 14, lab, head=True, size=6.6)
    rows = [
        ("1", "Flow Rate", "gpm", "", "", "", ""),
        ("2", "Inlet Pressure P1 / MAX", "psig", "P1 MAX", "", "", ""),
        ("3", "Outlet Pressure P2", "psig", "", "", "", ""),
        ("4", "Inlet Temperature", "°F", "", "", "", ""),
    ]
    for r, row in enumerate(rows):
        ry = ty + 14 + r * 14
        hi = (r == 1)
        for i, val in enumerate(row):
            cell(colx[i], ry, colw[i], 14, val, hi=hi, size=6.9,
                 anchor="start" if i == 1 else "middle")
    o.append(_line(340, 150, 340, 194, sw=1.5, color=RED))
    o.append(_arrow(340, 164, 340, 194, sw=1.4, color=RED))
    o.append(_txt(340, 206,
                  esc("P1 = MAXIMUM INLET / SHUTOFF PRESSURE - STATE IT ON THE SPECIFICATION FORM"),
                  7.4, color=RED, weight="600"))

    # ---- VALVE / TRIM --------------------------------------------------
    band(218, "VALVE / TRIM")
    vx = (34, 238, 442)
    for i, x0 in enumerate(vx):
        spec_field(x0, 234, 200, 22,
                   ("Size", "Type", "Characteristic")[i])
        spec_field(x0, 258, 200, 22,
                   ("Seat Material", "Body Material", "Rated Travel")[i])

    # ---- ACTUATOR ------------------------------------------------------
    band(290, "ACTUATOR")
    for i, x0 in enumerate(vx):
        spec_field(x0, 306, 200, 24,
                   ("Type", "Size / Eff. Area", "Spring / Bench Range")[i])
        spec_field(x0, 334, 200, 24,
                   ("Max Pressure", "Air Supply", "Fail Action")[i])

    # ---- POSITIONER ----------------------------------------------------
    band(378, "POSITIONER")
    for x0, lab in ((34, "Input Signal"), (238, "Output"),
                    (442, "Cam Characteristic")):
        spec_field(x0, 394, 200, 24, lab)

    # ---- NOTES / REVISIONS --------------------------------------------
    band(438, "NOTES / REVISIONS")
    nx = (34, 154, 454, 550)
    nw = (120, 300, 96, 96)
    for i, lab in enumerate(("Date", "Revisions", "Orig", "App")):
        cell(nx[i], 452, nw[i], 14, lab, head=True, size=6.8)
    for r in range(2):
        for i in range(4):
            cell(nx[i], 466 + r * 18, nw[i], 18, "")

    o.append(_txt(340, 530,
                  esc("* Information supplied by manufacturer unless already specified"),
                  6.8, color=GREY))
    o.append(_txt(340, 543,
                  esc("ISA FORM S20.50 Rev.1 05/81 - simplified redrawing, not a facsimile"),
                  6.8, color=GREY))

    s = svg(w, h, "".join(o),
            esc("Simplified ISA-20.50-1981 control valve data sheet"))
    return _fig(s,
                "Hình 11.1 · Bản vẽ lại đơn giản hóa, không phải bản sao chính xác, của phiếu dữ liệu van điều khiển ISA-20.50-1981 (ISA Form S20.50 Rev.1): gồm các ô PROJECT, UNIT, TAG, SERVICE; khối PROCESS CONDITIONS; các khối VALVE/TRIM, ACTUATOR, POSITIONER và dải NOTES/REVISIONS. Ô áp suất inlet lớn nhất P1 được làm nổi bật: P1 là áp suất vào cực đại / áp suất đóng (shutoff) và phải được ghi rõ trên phiếu đặc tả. Đây là bản vẽ lại dạng vector, đã đơn giản hóa.",
                "Figure 11.1 · Simplified redrawing, not a facsimile, of the ISA-20.50-1981 control valve data sheet (ISA Form S20.50 Rev.1): PROJECT, UNIT, TAG and SERVICE header fields, a PROCESS CONDITIONS block, VALVE/TRIM, ACTUATOR and POSITIONER blocks, and a NOTES/REVISIONS strip. The maximum inlet pressure field P1 is highlighted: P1 is the maximum inlet/shutoff pressure and must be stated on the specification form. This is a simplified vector redrawing.",
                "Phiếu dữ liệu van điều khiển ISA-20.50-1981 được vẽ lại đơn giản, có các ô PROJECT, UNIT, TAG, SERVICE, khối PROCESS CONDITIONS và ô P1 áp suất vào cực đại được tô đậm.",
                "Simplified ISA-20.50-1981 control valve data sheet with header fields, process conditions, valve/trim, actuator, positioner blocks and a highlighted maximum inlet pressure P1 field")


@_reg
def fig_f112():
    """Figure 11-2 - butterfly-valve dynamic torque characteristic chart."""
    w, h = 680, 404
    o = [_defs()]
    o.append(_txt(340, 18,
                  esc("Dac tinh mo-men dong cua van canh buom (ve lai don gian)"),
                  10.6, color=INK, weight="600"))
    o.append(_txt(340, 34,
                  esc("Truc ngang: do mo canh  -  truc doc: mo-men lap dat danh muc"),
                  7.4, color=GREY))

    L, T, R, B = 88, 58, 622, 330
    PW, PH = R - L, B - T
    YMAX = 0.09

    def px(d):
        return L + d / 90.0 * PW

    def py(v):
        return B - v / YMAX * PH

    def rot_txt(x, y, s, ang, size=8.2, color=INK):
        return ('<text x="%s" y="%s" text-anchor="middle" '
                'style="font:%spx Inter,Helvetica,sans-serif;fill:%s;'
                'font-weight:600" transform="rotate(%s,%s,%s)">%s</text>'
                % (_f(x), _f(y), size, color, _f(ang), _f(x), _f(y), esc(s)))

    def smooth(pts, per=12):
        out = []
        n = len(pts)
        for i in range(n - 1):
            p0, p1 = pts[max(0, i - 1)], pts[i]
            p2, p3 = pts[i + 1], pts[min(n - 1, i + 2)]
            for j in range(per):
                t = j / float(per)
                t2, t3 = t * t, t * t * t
                x = 0.5 * (2 * p1[0] + (-p0[0] + p2[0]) * t
                           + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2
                           + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
                y = 0.5 * (2 * p1[1] + (-p0[1] + p2[1]) * t
                           + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2
                           + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
                out.append((x, y))
        out.append(pts[-1])
        return out

    # grid and frame
    for d in (0, 20, 40, 60, 80):
        o.append(_line(px(d), T, px(d), B, sw=0.8, color="#e6e6e6"))
        o.append(_txt(px(d), B + 13, "%d°" % d, 7.0, color=GREY))
    for v in (0.0, 0.02, 0.04, 0.06, 0.08):
        o.append(_line(L, py(v), R, py(v), sw=0.8, color="#e6e6e6"))
        o.append(_txt(L - 7, py(v) + 2.4, "%.2f" % v, 6.8,
                      anchor="end", color=GREY))
    o.append(_rect(L, T, PW, PH, fill="#fdfcf9", sw=1.2))
    o.append(rot_txt(24, (T + B) / 2.0,
                     "SPEC. INSTALLED TORQUE, in-lb/d³ psi", -90))
    o.append(_txt(R, B + 32, esc("DEGREES OF VANE OPENING (0–90)"), 8.4,
                  anchor="end", color=INK, weight="600"))

    # conventional vane: rising to a sharp peak near 70 degrees, then reversal
    conv = [(0, 0.029), (5, 0.031), (10, 0.033), (15, 0.036),
            (20, 0.038), (25, 0.040), (30, 0.041), (35, 0.043),
            (40, 0.047), (45, 0.051), (50, 0.055), (55, 0.064),
            (60, 0.070), (65, 0.075), (68, 0.082), (70, 0.085),
            (72, 0.0852), (75, 0.081), (78, 0.078), (80, 0.074),
            (85, 0.065), (90, 0.056)]
    o.append(_poly([(px(d), py(v)) for d, v in smooth(conv)],
                   sw=2.3, color=INK))

    # low-torque vane with 15 degree seating angle
    low = [(0, 0.029), (5, 0.032), (10, 0.034), (15, 0.037),
           (20, 0.039), (25, 0.0405), (30, 0.041), (35, 0.041),
           (40, 0.040), (45, 0.038), (50, 0.035), (55, 0.031),
           (60, 0.028), (65, 0.026), (66, 0.026)]
    o.append(_poly([(px(d), py(v)) for d, v in smooth(low)],
                   sw=2.1, color=BLUE, dash="5 4"))

    # curve labels and gamma values
    o.append(_line(px(43), py(0.051), px(39), py(0.046), sw=0.9, color=GREY))
    o.append(_txt(px(44), py(0.050), esc("CONV. VANE"), 7.6,
                  anchor="start", color=INK, weight="600"))
    o.append(_line(px(60), py(0.072), px(58), py(0.066), sw=0.9, color=GREY))
    o.append(_txt(px(61), py(0.072), esc("γ = 0.25"), 7.4,
                  anchor="start", color=INK, weight="600"))
    o.append(_line(px(30), py(0.028), px(38), py(0.040), sw=0.9, color=GREY))
    o.append(_txt(px(8), py(0.025), esc("LOW-TORQUE VANE 15° ANGLE SEATING"),
                  7.0, anchor="start", color=BLUE, weight="600"))
    o.append(_line(px(62), py(0.021), px(60), py(0.028), sw=0.9, color=GREY))
    o.append(_txt(px(63), py(0.021), esc("γ = 0.25"), 7.4,
                  anchor="start", color=BLUE, weight="600"))

    # callout with the two torque values quoted in the prose
    bx, by, bw, bh = px(30), py(0.088), px(54) - px(30), py(0.077) - py(0.088)
    o.append(_rect(bx, by, bw, bh, fill="#ffffff", sw=1.0, stroke=RED))
    o.append(_txt(bx + 5, by + 13, esc("0.064 at 55°"), 7.2,
                  anchor="start", color=RED, weight="600"))
    o.append(_txt(bx + 5, by + 26, esc("0.075 at 65°"), 7.2,
                  anchor="start", color=RED, weight="600"))
    for d, v in ((55, 0.064), (65, 0.075)):
        o.append(_line(px(54), py(0.077) - 2, px(d), py(v),
                       sw=0.9, color=GREY))
        o.append(_circle(px(d), py(v), 2.8, fill="#ffffff",
                         sw=1.2, color=RED))

    o.append(_txt(340, 362,
                  esc("NOTE: 60° STANDARD VANE ≈ 45° LOW-TORQUE VANE"),
                  7.8, color=INK, weight="600"))
    o.append(_txt(340, 386,
                  esc("Ve lai don gian theo Baumann, Control Valve Primer, 5th ed. "
                      "(Fig. 11-2) - Nguon: Reference 6"),
                  7.0, color=GREY))

    s = svg(w, h, "".join(o),
            esc("Butterfly-valve dynamic torque characteristic with torque reversal"))
    return _fig(s,
                "Hình 11.2 · Đồ thị đơn giản hóa đặc tính mô-men động của van bướm: trục hoành là độ mở cánh (0–90°), trục tung là mô-men lắp đặt riêng (in-lb/d³ psi, 0–0,085). Đường CONV. VANE tăng từ khoảng 0,029 ở 0° lên khoảng 0,041 ở 30° và 0,055 ở 50°, đạt đỉnh khoảng 0,085 gần 68–70°, rồi đảo chiều giảm mạnh còn khoảng 0,056 ở 90°; chính sự đảo mô-men dữ dội quanh 70° hành trình này là nội dung chính của hình. Đường LOW-TORQUE VANE với góc đệm 15° chỉ đạt đỉnh khoảng 0,041 gần 30–35° rồi giảm còn khoảng 0,026 gần 60–65°; ghi chú nêu 60° cánh chuẩn ≈ 45° cánh mô-men thấp. Các mốc 0,064 ở 55° và 0,075 ở 65° được gọi ra. Nguồn: tài liệu tham khảo 6; bản gốc không in lời cảm ơn từ bên ngoài. Đây là bản vẽ lại dạng vector, đã đơn giản hóa.",
                "Figure 11.2 · Simplified butterfly-valve dynamic torque chart: x is vane opening (0–90°), y is specific installed torque (in-lb/d³ psi, 0–0.085). The CONV. VANE curve rises from about 0.029 at 0° through 0.041 at 30° and 0.055 at 50° to a peak near 0.085 at about 68–70°, then reverses sharply and falls to roughly 0.056 at 90°; this drastic torque reversal around 70° of travel is the point of the figure. The LOW-TORQUE VANE with a 15° seating angle peaks at only about 0.041 near 30–35° and falls to roughly 0.026 near 60–65°; the note states that 60° standard vane ≈ 45° low-torque vane. The values 0.064 at 55° and 0.075 at 65° are called out. Source adapted from Reference 6; the source prints no external courtesy credit. This is a simplified vector redrawing.",
                "Đồ thị mô-men van bướm: đường cánh thường đạt đỉnh 0,085 gần 70° rồi giảm mạnh; đường cánh mô-men thấp chỉ đạt 0,041 gần 30–35°; 60° cánh chuẩn tương đương 45° cánh mô-men thấp.",
                "Butterfly-valve torque chart with a conventional-vane peak near 70 degrees followed by reversal, a lower low-torque-vane curve and a note equating 60 degrees standard vane with 45 degrees low-torque vane")


@_reg
def fig_f113():
    """Figure 11-3 - three-panel stall and torque-reversal analogy sketch."""
    w, h = 680, 344
    o = [_defs()]
    o.append(_txt(340, 18,
                  esc("Stall va dao mo-men: ba so do minh hoa (ve lai don gian)"),
                  10.6, color=INK, weight="600"))
    o.append(_txt(340, 34,
                  esc("Tuong tu giua canh may bay bi stall va van bong co xu huong dong"),
                  7.4, color=GREY))

    xs = (32, 246, 460)
    pw = 188
    for x0 in xs:
        o.append(_rect(x0, 48, pw, 236, fill="#fdfcf9", sw=1.1,
                       stroke="#c9c9c9"))

    # ---- (a) airfoil at low angle of attack ---------------------------
    x0 = xs[0]
    o.append(_txt(x0 + 94, 64, esc("(a) AIRFOIL - LOW ANGLE OF ATTACK"),
                  7.6, color=INK, weight="600"))
    le = (x0 + 38, 166)
    te = (x0 + 150, 142)
    o.append(_path("M%s,%s C%s,%s %s,%s %s,%s C%s,%s %s,%s %s,%s Z"
                   % (le[0], le[1], x0 + 65, 146, x0 + 120, 134,
                      te[0], te[1], x0 + 120, 150, x0 + 65, 168,
                      le[0], le[1]),
                   fill="#dfe6ee", sw=1.2, color=INK))
    o.append(_line(le[0], le[1], te[0], te[1], sw=0.8,
                   color=GREY, dash="4 3"))
    o.append(_line(x0 + 28, 166, x0 + 164, 166, sw=0.7,
                   color="#c9cdd2", dash="3 3"))
    # smooth free-stream arrows
    o.append(_arrow(x0 + 14, 116, x0 + 170, 110, sw=1.1, color=BLUE))
    o.append(_arrow(x0 + 14, 190, x0 + 170, 186, sw=1.1, color=BLUE))
    o.append(_arrow(x0 + 14, 154, x0 + 44, 150, sw=1.1, color=BLUE))
    o.append(_arrow(x0 + 148, 144, x0 + 170, 142, sw=1.1, color=BLUE))
    o.append(_txt(x0 + 94, 100, esc("SMOOTH FLOW"), 7.0, color=GREY))
    o.append(_path("M%s,%s Q%s,%s %s,%s"
                   % (x0 + 50, 166, x0 + 56, 152, x0 + 68, 150),
                   sw=0.9, color=INK))
    o.append(_txt(x0 + 96, 202, esc("α = 18–20°"), 8.4,
                  color=INK, weight="600"))
    o.append(_poly([(x0 + 32, 224), (x0 + 48, 224), (x0 + 40, 238)],
                   fill="#fff3cd", sw=1.1, color=RED, close=True))
    o.append(_txt(x0 + 40, 235, esc("!"), 7.6, color=RED, weight="600"))
    o.append(_txt(x0 + 106, 232, esc("STALL WARNING"), 7.4,
                  color=RED, weight="600"))

    # ---- (b) butterfly vane at low attachment angle -------------------
    x0 = xs[1]
    o.append(_txt(x0 + 94, 64, esc("(b) BUTTERFLY VANE - LOW ANGLE"),
                  7.6, color=INK, weight="600"))
    o.append(_rect(x0 + 16, 130, 156, 56, fill="#eef3fb", sw=0.0))
    o.append(_line(x0 + 16, 130, x0 + 172, 130, sw=1.2, color=INK))
    o.append(_line(x0 + 16, 186, x0 + 172, 186, sw=1.2, color=INK))
    o.append(_line(x0 + 52, 168, x0 + 136, 148, sw=4.0, color="#9aa5ae"))
    o.append(_circle(x0 + 94, 158, 5, fill="#ffffff", sw=1.1, color=INK))
    o.append(_path("M%s,%s Q%s,%s %s,%s"
                   % (x0 + 112, 158, x0 + 118, 150, x0 + 128, 151),
                   sw=0.9, color=INK))
    o.append(_txt(x0 + 128, 151, esc("α"), 8.0, color=INK, weight="600"))
    for y1, y2 in ((140, 140), (176, 176)):
        o.append(_arrow(x0 + 18, y1, x0 + 166, y2, sw=1.1, color=BLUE))
    o.append(_arrow(x0 + 18, 158, x0 + 48, 158, sw=1.1, color=BLUE))
    o.append(_arrow(x0 + 140, 158, x0 + 170, 158, sw=1.1, color=BLUE))
    o.append(_txt(x0 + 94, 210, esc("SMOOTH FLOW"), 7.0, color=GREY))
    o.append(_txt(x0 + 94, 228, esc("LOW ATTACHMENT ANGLE"), 7.4,
                  color=INK, weight="600"))

    # ---- (c) vane near the seat at high angle -------------------------
    x0 = xs[2]
    o.append(_txt(x0 + 94, 64, esc("(c) NEAR SEAT - HIGH ANGLE"),
                  7.6, color=INK, weight="600"))
    o.append(_rect(x0 + 16, 130, 156, 56, fill="#eef3fb", sw=0.0))
    o.append(_line(x0 + 16, 130, x0 + 172, 130, sw=1.2, color=INK))
    o.append(_line(x0 + 16, 186, x0 + 172, 186, sw=1.2, color=INK))
    o.append(_rect(x0 + 118, 130, 8, 12, fill="#b8bfc6", sw=1.0, stroke=INK))
    o.append(_rect(x0 + 118, 174, 8, 12, fill="#b8bfc6", sw=1.0, stroke=INK))
    o.append(_line(x0 + 83, 182, x0 + 115, 132, sw=4.0, color="#9aa5ae"))
    o.append(_circle(x0 + 99, 158, 5, fill="#ffffff", sw=1.1, color=INK))
    # separated, swirling flow downstream of the vane
    for yy in (142, 158, 174):
        o.append(_path("M%s,%s Q%s,%s %s,%s Q%s,%s %s,%s"
                       % (x0 + 128, yy, x0 + 140, yy - 8, x0 + 150, yy + 2,
                          x0 + 160, yy + 9, x0 + 170, yy - 2),
                       sw=0.9, color=GREY))
    o.append(_arrow(x0 + 18, 140, x0 + 74, 140, sw=1.1, color=BLUE))
    # closing torque arrow about the pivot
    o.append(_arrow(x0 + 128, 138, x0 + 110, 156, sw=1.6, color=RED))
    o.append(_path("M%s,%s Q%s,%s %s,%s"
                   % (x0 + 118, 146, x0 + 106, 140, x0 + 102, 152),
                   sw=0.9, color=RED))
    o.append(_txt(x0 + 94, 210, esc("α ABOVE 70° TRAVEL"), 8.4,
                  color=RED, weight="600"))
    o.append(_txt(x0 + 94, 228, esc("VALVE TENDS TO CLOSE"), 7.4,
                  color=RED, weight="600"))

    o.append(_txt(340, 308,
                  esc("SAME STALL MECHANISM: AIRPLANE STALL AND VALVE TORQUE REVERSAL"),
                  7.6, color=INK, weight="600"))
    o.append(_txt(340, 330,
                  esc("Ve lai don gian theo Baumann, Control Valve Primer, 5th ed. "
                      "(Fig. 11-3)"),
                  7.0, color=GREY))

    s = svg(w, h, "".join(o),
            esc("Stall analogy: airfoil and butterfly valve torque reversal"))
    return _fig(s,
                "Hình 11.3 · Bản vẽ lại đơn giản hóa sơ đồ ba ô minh họa sự tương tự giữa máy bay bị stall và van bị đảo mô-men: (a) cánh máy bay ở góc tới thấp α = 18–20°, dòng chảy êm nhưng đã có cảnh báo tới ngưỡng stall; (b) cánh van bướm trong ống ở góc đính kèm thấp, dòng chảy êm; (c) cánh van gần đế ở góc lớn, trên khoảng 70° hành trình, dòng chảy tách rời và mũi tên cho thấy van có xu hướng đóng lại. Khi góc đính kèm dưới 18–20° hoặc hành trình van trên 70°, máy bay sẽ bị stall và van có xu hướng đóng. Đây là bản vẽ lại dạng vector, đã đơn giản hóa.",
                "Figure 11.3 · Simplified redrawing of the three-panel stall/torque-reversal sketch: (a) an airfoil at a low angle of attack, α = 18–20°, with smooth flow and a stall warning; (b) a butterfly vane in a pipe at a low attachment angle with smooth flow; (c) a vane near the seat at a high angle, above roughly 70° of travel, with separated flow and an arrow showing the valve tending to close. Below 18–20° attachment angle or above 70° valve travel, airplanes stall and valves tend to close. This is a simplified vector redrawing.",
                "Ba ô minh họa: cánh máy bay góc tới thấp có dòng êm và cảnh báo stall, cánh van bướm dòng êm, và cánh van gần đế trên 70° có dòng tách rời và van có xu hướng đóng.",
                "Three-panel sketch of an airfoil with smooth flow and stall warning, a butterfly vane with smooth flow, and a vane near its seat above 70 degrees travel with separated flow and a closing arrow")
