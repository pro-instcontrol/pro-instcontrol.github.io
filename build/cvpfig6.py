# -*- coding: utf-8 -*-
"""Vector figures for Book 7 - Baumann, *Control Valve Primer*, 5th ed.

Chapter 6 "High-Recovery Valves": simplified vector re-drawings of source
Figures 6-1 and 6-2.  Each function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)``.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, RED, _arrow, _box, _circle,
                  _defs, _fig, _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f
    return f


def esc(s):
    s = str(s)
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return s.replace('"', "&quot;")


@_reg
def fig_f61():
    """Figure 6-1 - simplified longitudinal cutaway of an in-line high-recovery valve."""
    w, h = 680, 350
    o = [_defs()]
    o.append(_txt(340, 18,
                  esc("Van phuc hoi ap suat cao kieu noi tuyen - mat cat doc don gian"),
                  10.6, color=INK, weight="600"))
    o.append(_txt(340, 35,
                  esc("Ve lai theo ban ve bang sang che US 105 782 15 / so do minh hoa, "
                      "khong phai ban goc"),
                  7.4, color=GREY))

    # centreline and flow direction
    o.append(_line(60, 165, 616, 165, sw=0.8, dash="6 4", color=GREY))
    o.append(_arrow(96, 165, 240, 165, sw=1.8, color=BLUE))
    o.append(_arrow(398, 165, 574, 165, sw=1.8, color=BLUE))
    o.append(_txt(166, 153, esc("chay / flow"), 7.2, color=BLUE))

    # metal walls: hatch-filled polygons following the inner flow contour
    top_wall = [(70, 108), (190, 108), (190, 96), (248, 96), (256, 84),
                (334, 84), (342, 96), (382, 98), (445, 110), (600, 110),
                (600, 132), (470, 132), (285, 158), (200, 126), (70, 126)]
    bot_wall = [(70, 222), (190, 222), (190, 234), (248, 234), (256, 246),
                (334, 246), (342, 234), (382, 232), (445, 220), (600, 220),
                (600, 198), (470, 198), (285, 172), (200, 204), (70, 204)]
    o.append(_poly(top_wall, fill="url(#h6)", sw=1.2, color=INK, close=True))
    o.append(_poly(bot_wall, fill="url(#h6)", sw=1.2, color=INK, close=True))
    # flanges
    o.append(_line(66, 104, 66, 226, sw=2.2, color=INK))
    o.append(_line(606, 104, 606, 226, sw=2.2, color=INK))

    # throttling plug and stem
    o.append(_rect(287, 60, 10, 70, fill="url(#h6)", sw=1.1))
    o.append(_poly([(266, 128), (316, 128), (305, 157), (277, 157)],
                   fill="url(#h6)", sw=1.2, color=INK, close=True))
    # seat faces at the throat
    o.append(_line(270, 158, 277, 158, sw=2.4, color=INK))
    o.append(_line(305, 158, 312, 158, sw=2.4, color=INK))

    def callout(n, tx, ty, lx, ly):
        return (_line(tx, ty, lx, ly, sw=0.9, color=GREY)
                + _circle(lx, ly, 9, fill="#ffffff", sw=1.0, color=BLUE)
                + _txt(lx, ly + 2.8, str(n), 7.6, color=BLUE, weight="600"))

    # numbered callouts kept from the patent drawing
    o.append(callout(22, 92, 110, 94, 66))      # inlet
    o.append(callout(1, 214, 99, 204, 62))      # body
    o.append(callout(9, 296, 108, 366, 62))     # plug
    o.append(callout(5, 299, 156, 444, 60))     # throttling area
    o.append(callout(11, 288, 171, 404, 264))   # throat gap
    o.append(callout(13, 486, 126, 522, 74))    # venturi outlet

    o.append(_txt(175, 288,
                  esc("So hieu goi ra theo ban ve goc: 1 than van / 5, 11 vung tiet luu / "
                      "9 nut van / 13 doan venturi / 22 cang vao"),
                  7.0, anchor="start", color=INK))
    o.append(_txt(556, 312, esc("So do don gian, khong theo ty le"),
                  7.0, color=GREY))

    # small end section
    o.append(_circle(120, 292, 30, fill="url(#h6)", sw=1.1, color=INK))
    o.append(_circle(120, 292, 19, fill="#ffffff", sw=1.0, color=INK))
    o.append(_circle(120, 292, 7, fill="url(#h6)", sw=1.0, color=INK))
    o.append(_line(120, 273, 120, 311, sw=0.7, dash="3 3", color=GREY))
    o.append(_line(101, 292, 139, 292, sw=0.7, dash="3 3", color=GREY))
    o.append(_txt(120, 335, esc("mat cat ngang A-A / end section"),
                  7.2, color=GREY))

    s = svg(w, h, "".join(o),
            esc("Simplified longitudinal cutaway of an in-line high-recovery valve"))
    return _fig(s,
                "Hình 6.1 · Bản vẽ lại dạng vector, đã đơn giản hóa, của bản vẽ bằng sáng chế "
                "van phục hồi áp suất cao kiểu nội tuyến (US Patent 105 782 15): mặt cắt dọc cho "
                "thấy cổng vào hội tụ, vùng tiết lưu tại đế van với nút van, đoạn khuếch tán dạng "
                "venturi ở hạ lưu và mũi tên dòng chảy, cùng một số số hiệu gọi ra (1 thân van, "
                "5 và 11 vùng tiết lưu, 9 nút van, 13 đoạn venturi, 22 cổng vào) và mặt cắt ngang "
                "nhỏ. Đây là sơ đồ minh họa, không phải bản sao nguyên bản.",
                "Figure 6.1 · Simplified vector redrawing of the patent drawing of an in-line "
                "high-recovery valve (US Patent 105 782 15): a longitudinal cutaway showing the "
                "converging inlet, the throttling area at the seat with its plug, the gradually "
                "expanding venturi outlet, flow arrows, a few retained callout numbers (1 body, "
                "5 and 11 throttling area, 9 plug, 13 venturi section, 22 inlet), and a small end "
                "section. This is an illustrative schematic, not a facsimile of the original.",
                "So do cat doc van phuc hoi ap suat cao: cang vao hoi tu, nut van va doan venturi, "
                "kem so hieu goi ra va mat cat ngang",
                "Longitudinal cutaway of a high-recovery valve with converging inlet, plug and "
                "venturi outlet, numbered callouts and a small end section")


@_reg
def fig_f62():
    """Figure 6-2 - sound level versus pressure drop, conventional vs high-recovery."""
    w, h = 680, 425
    o = [_defs()]
    o.append(_txt(340, 18,
                  esc("So sanh muc ong: van thong thuong va van phuc hoi ap suat cao"),
                  10.6, color=INK, weight="600"))
    o.append(_txt(340, 36,
                  esc("Duong den lien: van thong thuong, FL 0.75 / duong do dot: van phuc hoi. "
                      "So trong hop: inch travel"),
                  7.4, color=GREY))

    L, T, R, B = 72, 64, 620, 300
    PW, PH = R - L, B - T
    # the source dashed curve starts just below 70 dBA; clip it to the frame
    o.append('<clipPath id="plotclip"><rect x="%d" y="%d" width="%d" height="%d"/></clipPath>'
             % (L, T, PW, PH))

    def px(v):
        return L + v / 55.0 * PW

    def py(v):
        return B - (v - 70.0) / 50.0 * PH

    # grid and axes
    for gx in range(0, 56, 5):
        o.append(_line(px(gx), T, px(gx), B, sw=0.8, color="#e6e6e6"))
        o.append(_txt(px(gx), B + 13, str(gx), 6.8, color=GREY))
    for gy in range(70, 121, 10):
        o.append(_line(L, py(gy), R, py(gy), sw=0.8, color="#e6e6e6"))
        o.append(_txt(L - 6, py(gy) + 2.4, str(gy), 6.8, anchor="end", color=GREY))
    o.append(_line(L, B, R, B, sw=1.3, color=INK))
    o.append(_line(L, T, L, B, sw=1.3, color=INK))
    o.append(_txt(L, T - 9, esc("Noise (dBA)"), 8.4, anchor="start",
                  color=INK, weight="600"))
    o.append(_txt((L + R) / 2, B + 30, esc("ΔP (psi)"), 8.4,
                  color=INK, weight="600"))

    def smooth(pts, per=14):
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

    conv = [(18, 72), (20, 73), (25, 78), (30, 84), (35, 91),
            (40, 99), (45, 104), (50, 106), (55, 107)]
    rec = [(18, 65), (20, 66), (25, 71), (30, 76), (35, 82),
           (40, 89), (45, 95), (50, 99), (55, 102)]
    o.append(_poly([(px(x), py(y)) for x, y in smooth(conv)], sw=2.2, color=INK))
    o.append('<g clip-path="url(#plotclip)">'
             + _poly([(px(x), py(y)) for x, y in smooth(rec)], sw=2.2,
                     color=RED, dash="6 4")
             + '</g>')

    # maximum cavitation at Xy = 0.55 (~30 psi on this 0-55 scale)
    o.append(_line(px(30), B, px(30), py(85), sw=0.9, dash="3 3", color=GREY))
    o.append(_txt(px(30) + 5, py(85) - 3, esc("Xy = 0,55"),
                  7.0, anchor="start", color=GREY))

    # travel-number box near the bottom, as in the source figure
    o.append(_txt(px(18), 336, esc("inch travel"), 7.0,
                  anchor="start", color=GREY))
    o.append(_rect(px(18) - 4, 340, px(52) - px(18) + 8, 22,
                   fill="#f4f4f4", sw=0.8, stroke=GREY))
    for tv in (20, 25, 30, 35, 40, 45, 50):
        o.append(_txt(px(tv), 355, str(tv), 7.2, color=INK))

    # legend
    o.append(_line(120, 381, 144, 381, sw=2.2, color=INK))
    o.append(_txt(150, 384, esc("conventional (FL 0.75)"), 7.6,
                  anchor="start", color=INK))
    o.append(_line(360, 381, 384, 381, sw=2.2, color=RED, dash="6 4"))
    o.append(_txt(390, 384, esc("high-recovery (FL 0.4)"), 7.6,
                  anchor="start", color=RED))

    o.append(_txt(340, 410,
                  esc("Ve lai don gian theo Baumann, Control Valve Primer, 5th ed. (Fig. 6-2)"),
                  7.0, color=GREY))

    s = svg(w, h, "".join(o),
            esc("Sound level versus pressure drop for conventional and high-recovery valves"))
    return _fig(s,
                "Hình 6.2 · Đồ thị đơn giản hóa so sánh mức ồn theo độ giảm áp ΔP từ 0 đến 55: "
                "đường đen liền là van điều khiển thông thường với FL khoảng 0,75, đường đỏ đứt "
                "nét là van phục hồi áp suất cao; các số 20, 25, 30, 35, 40, 45, 50 trong ô nhỏ "
                "ở dưới trục là hành trình tính bằng inch. Mức ồn tổng thể của van phục hồi thấp "
                "hơn khoảng 5 đến 8 dB. Đây là bản vẽ lại dạng vector, đã đơn giản hóa.",
                "Figure 6.2 · Simplified chart of sound level versus pressure drop ΔP from 0 to "
                "55: the solid black line is the conventional control valve (FL about 0.75) and "
                "the dashed red line the high-recovery valve; the numbers 20, 25, 30, 35, 40, 45, "
                "50 in the small box near the bottom are inch travel. The high-recovery valve runs "
                "about 5 to 8 dB quieter overall. This is a simplified vector redrawing.",
                "Bieu do muc ong theo do giam ap 0 den 55, duong lien den va duong dot do, "
                "kem hop so hanh tinh inch",
                "Sound level versus 0 to 55 pressure drop chart, solid black conventional and "
                "dashed red high-recovery curves with an inch-travel number box")
