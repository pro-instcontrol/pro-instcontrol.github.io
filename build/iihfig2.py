# -*- coding: utf-8 -*-
"""Vector figures for Chapter 2 "Measurement of Pressure" of
3G E-learning, *Illustrated Handbook of Industrial Instrumentation &
Control* (2018), PDF pp. 61-96 (printed pp. 47-82).

The source carries 21 numbered figures (Figure 1 - Figure 21). All are
redrawn here as simplified vector schematics that keep the topology and the
key labels of the originals; numbered callouts with bilingual legends are
used where a components list is appropriate. Figures 6, 15 and 21 are
charts with axes, tick labels and the curves/bands described in the prose.
Every function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)`` through ``_fig()``.
All SVG text is XML-escaped with ``esc()``/``T()`` before it reaches a tag.
"""
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, RED,  # noqa: E402
                  _arrow, _circle, _defs, _ellipse, _fig, _line, _path, _poly,
                  _rect, _txt, svg)

FIGS = {}


def _reg(f):
    figs = f()
    FIGS[f.__name__] = figs
    return f


def esc(s):
    """Escape SVG text while preserving entities already present in the data."""
    s = str(s)
    s = re.sub(r"&(?!amp;|lt;|gt;|quot;|apos;|#\d+;)", "&amp;", s)
    return s.replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def T(x, y, s, size=8.5, **kw):
    """XML-safe text label."""
    return _txt(x, y, esc(s), size=size, **kw)


def _num(cx, cy, n):
    """A numbered callout bubble."""
    return (_circle(cx, cy, 8, fill="#fdf3e6", sw=1.1, color=INK)
            + T(cx, cy + 3, str(n), 8.0, color=INK, weight="600"))


def _legend(items, x, y, lh=15, size=7.6):
    """Numbered parts list rendered as plain text lines."""
    return "".join(T(x, y + i * lh, "%d. %s" % (i + 1, lab), size,
                     anchor="start") for i, lab in enumerate(items))


def _callouts(items):
    """Draw connector lines and numbered bubbles from (lx,ly) to (tx,ty)."""
    o = []
    for i, (lx, ly, tx, ty) in enumerate(items):
        o.append(_line(lx, ly, tx, ty, sw=0.8, color=GREY))
        dy = 12 if ly < 200 else -12
        o.append(_num(lx, ly + dy, i + 1))
    return "".join(o)


def _foot(w, y, text):
    return T(w / 2.0, y, text, 7.6, color=GREY)


# ---------------------------------------------------------------------------
@_reg
def fig_f01():
    """Figure 1 - liquid column gauge: schematic draw and gauge views."""
    w, h = 680, 340
    o = [_defs()]
    o.append(T(180, 28, "(trái) Sơ đồ đồng hồ cột chất lỏng", 8.6, color=INK))
    o.append(T(510, 28, "(phải) Đồng hồ cột chất lỏng", 8.6, color=INK))
    o.append(_line(340, 44, 340, 296, sw=0.8, color="#cfd5db", dash="4 5"))
    # ---- left: schematic U tube
    o.append(_path("M148,66 L148,236 Q148,254 168,254 L232,254 Q252,254 252,236 L252,66",
                   sw=11, color="#dfe6ec"))
    o.append(_path("M148,150 L148,236 Q148,254 168,254 L232,254 Q252,254 252,236 L252,112",
                   sw=9, color="#7fb6d6"))
    o.append(_line(139, 150, 157, 150, sw=1.4, color=BLUE))
    o.append(_line(243, 112, 261, 112, sw=1.4, color=BLUE))
    o.append(_arrow(148, 86, 148, 58, sw=1.4, color=RED))
    o.append(_arrow(252, 86, 252, 58, sw=1.4, color=BLUE))
    o.append(T(148, 50, "p1", 8.6, color=RED))
    o.append(T(252, 50, "p2", 8.6, color=BLUE))
    o.append(_line(266, 112, 292, 112, sw=0.7, color=GREY, dash="3 3"))
    o.append(_line(266, 150, 292, 150, sw=0.7, color=GREY, dash="3 3"))
    o.append(_arrow(282, 118, 282, 144, sw=1.0, color=INK))
    o.append(T(302, 136, "Δh", 8.4, color=INK))
    o.append(T(200, 282, "Chênh mức = áp suất / level difference = pressure", 7.8,
              color=GREY))
    # ---- right: two real gauge styles
    for bx, top in ((410, 104), (548, 132)):
        o.append(_path("M%d,70 L%d,214 Q%d,232 %d,232 Q%d,232 %d,214 L%d,70"
                       % (bx, bx, bx + 12, bx + 24, bx + 36, bx + 48, bx + 48),
                       sw=9, color="#dfe6ec"))
        l = top
        r = 214 - (top - 104) * 0.7 if bx == 410 else 214 - (top - 132) * 0.7
        o.append(_path("M%d,%d L%d,214 Q%d,232 %d,232 Q%d,232 %d,214 L%d,%d"
                       % (bx, l, bx, bx + 12, bx + 24, bx + 36, bx + 48, bx + 48, r),
                       sw=7, color="#7fb6d6"))
        o.append(_rect(bx - 10, 62, 68, 26, fill="url(#h6)", sw=1.0))
        for i in range(5):
            yy = 86 + i * 30
            o.append(_line(bx + 52, yy, bx + 60, yy, sw=0.7))
            o.append(T(bx + 64, yy + 3, str(i), 6.2, color=GREY, anchor="start"))
    o.append(T(434, 74, "chữ U / U-tube", 7.6, color=BLUE))
    o.append(T(572, 100, "dạng nghiêng / inclined", 7.4, color=BLUE))
    o.append(T(510, 282, "Thủy ngân hoặc nước / mercury or water", 7.8, color=GREY))
    # ---- numbered legend
    o.append(_callouts([(120, 118, 148, 150), (120, 200, 148, 224),
                        (302, 236, 252, 200), (470, 250, 470, 214)]))
    o.append(T(40, 310, "1. Chất lỏng đo / manometric liquid   2. Ống chữ U / U-shaped tube   "
                        "3. Áp suất chuẩn / reference pressure", 7.2, anchor="start"))
    o.append(T(40, 326, "4. Vạch đọc / scale   5. Cổng áp suất / pressure port   "
                        "6. Chênh mức Δh / level difference", 7.2, anchor="start"))
    s = svg(w, h, "".join(o), esc("Figure 2.1 - Liquid column gauges"))
    return _fig(s,
                "Hình 2.1 (nguyên bản Hình 1) · (trái) Sơ đồ đồng hồ cột chất lỏng: ống chữ U chứa "
                "chất lỏng, hai đầu chịu áp suất khác nhau; (phải) các đồng hồ cột chất lỏng thực tế "
                "với thang đọc. Các số chỉ: 1. Chất lỏng đo; 2. Ống chữ U; 3. Áp suất chuẩn; "
                "4. Vạch đọc; 5. Cổng áp suất; 6. Chênh mức Δh.",
                "Figure 2.1 (source Figure 1) · (left) Schematic draw of a liquid column gauge: a "
                "U-shaped tube whose ends are exposed to different pressures; (right) liquid column "
                "gauges with reading scales. Callouts: 1. Manometric liquid; 2. U-shaped tube; "
                "3. Reference pressure; 4. Scale; 5. Pressure port; 6. Level difference Δh.",
                "Ống chữ U chứa chất lỏng với hai cột ở mức khác nhau và vạch đọc",
                "U-tube with manometric liquid at different levels and a reading scale")


# ---------------------------------------------------------------------------
@_reg
def fig_f02():
    """Figure 2 - Bourdon gauge and its mechanism."""
    w, h = 680, 350
    o = [_defs()]
    o.append(T(170, 28, "(trái) Đồng hồ Bourdon", 8.6, color=INK))
    o.append(T(510, 28, "(phải) Cơ chế đồng hồ Bourdon", 8.6, color=INK))
    o.append(_line(340, 44, 340, 300, sw=0.8, color="#cfd5db", dash="4 5"))
    # ---- left: dial gauge
    o.append(_circle(170, 168, 96, fill="#fbfaf7", sw=2.0))
    o.append(_circle(170, 168, 84, fill="none", sw=0.9, color=GREY))
    for i in range(11):
        a = math.radians(210 - i * 24)
        x1 = 170 + 72 * math.cos(a)
        y1 = 168 + 72 * math.sin(a)
        x2 = 170 + 82 * math.cos(a)
        y2 = 168 + 82 * math.sin(a)
        o.append(_line(x1, y1, x2, y2, sw=1.2))
        o.append(T(170 + 58 * math.cos(a), 168 + 58 * math.sin(a) + 3,
                   str(i * 10), 6.8, color=GREY))
    o.append(_line(170, 168, 226, 118, sw=2.6, color=RED))
    o.append(_circle(170, 168, 6, fill=INK))
    o.append(T(170, 224, "psi", 8.0, color=GREY))
    o.append(_rect(146, 268, 48, 28, fill="#e4e9ee", sw=1.4))
    o.append(_line(170, 264, 170, 256, sw=2.0))
    o.append(T(170, 302, "Đầu nối áp suất / pressure socket", 7.6, color=GREY))
    # ---- right: mechanism
    o.append(_circle(516, 170, 104, fill="none", sw=1.4, color="#d8dde2"))
    o.append(_path("M566,108 A92,92 0 1 0 566,232", sw=11, color=BLUE))
    o.append(_circle(566, 108, 7, fill="#dfe6ec", sw=1.2))
    o.append(_line(566, 108, 570, 76, sw=2.0, color=GREY))
    o.append(T(570, 70, "đầu bịt / closed tip", 7.4, color=GREY))
    o.append(_line(566, 232, 520, 248, sw=2.4, color=INK))
    o.append(_circle(520, 248, 5, fill="#fdf3e6", sw=1.2))
    # sector gear (an arc of small teeth) and pinion
    o.append(_path("M470,232 A64,64 0 0 1 458,178", sw=7, color="#c9ced4"))
    for k in range(7):
        a = math.radians(215 + k * 8)
        o.append(_line(470 + 60 * math.cos(a), 232 + 60 * math.sin(a),
                       470 + 67 * math.cos(a), 232 + 67 * math.sin(a),
                       sw=1.0, color=GREY))
    o.append(_circle(460, 174, 13, fill="#fdf3e6", sw=1.4))
    o.append(_circle(460, 174, 4, fill=GREY))
    o.append(_line(460, 174, 510, 132, sw=2.4, color=RED))
    o.append(_circle(516, 170, 3, fill=INK))
    o.append(T(512, 118, "kim / pointer", 7.4, color=RED, anchor="start"))
    o.append(T(452, 206, "bánh răng / gear", 7.2, color=GREY, anchor="end"))
    o.append(T(492, 282, "C-ống / C-shaped tube", 7.8, color=BLUE))
    o.append(_callouts([(118, 100, 150, 120), (250, 250, 220, 220),
                        (600, 250, 560, 230), (400, 130, 458, 174)]))
    o.append(T(40, 328, "1. Vỏ và mặt đồng hồ / case and dial   2. Cơ cấu bánh răng / gear train   "
                        "3. Ống Bourdon chữ C / C-shaped Bourdon tube", 7.2, anchor="start"))
    o.append(T(40, 344, "4. Đầu nối / pressure inlet   5. Kim chỉ / pointer   "
                        "6. Liên kết chỉnh được / adjustable link", 7.2, anchor="start"))
    s = svg(w, h, "".join(o), esc("Figure 2.2 - Bourdon gauge and its mechanism"))
    return _fig(s,
                "Hình 2.2 (nguyên bản Hình 2) · (trái) Đồng hồ Bourdon với mặt số và kim chỉ; "
                "(phải) cơ chế: ống kim loại dẹt uốn chữ C duỗi thẳng khi có áp, truyền qua liên kết "
                "và bánh răng làm quay kim. Các số chỉ: 1. Vỏ và mặt đồng hồ; 2. Cơ cấu bánh răng; "
                "3. Ống Bourdon chữ C; 4. Đầu nối; 5. Kim chỉ; 6. Liên kết chỉnh được.",
                "Figure 2.2 (source Figure 2) · (left) A Bourdon gauge with dial and pointer; "
                "(right) its mechanism: a flattened C-shaped tube straightens under pressure and, "
                "through a link and gear train, rotates the pointer. Callouts: 1. Case and dial; "
                "2. Gear train; 3. C-shaped Bourdon tube; 4. Pressure inlet; 5. Pointer; "
                "6. Adjustable link.",
                "Mặt đồng hồ Bourdon và sơ đồ cơ chế ống chữ C, bánh răng và kim chỉ",
                "Bourdon dial gauge and a schematic of the C-tube, gear train and pointer")


# ---------------------------------------------------------------------------
@_reg
def fig_f03():
    """Figure 3 - McLeod gauge."""
    w, h = 620, 390
    o = [_defs()]
    # vacuum connection at top, capillary and bulb
    o.append(_rect(268, 30, 24, 60, fill="#e9eef3", sw=1.4))
    o.append(T(280, 24, "nối vào hệ chân không / to vacuum system", 7.8, color=GREY))
    o.append(_rect(272, 90, 16, 96, fill="#f4f7fa", sw=1.4))
    o.append(_circle(280, 208, 42, fill="#f4f7fa", sw=1.6))
    o.append(T(280, 214, "B", 10, color=INK, weight="600"))
    o.append(T(322, 202, "bulb B", 7.6, color=GREY, anchor="start"))
    # trapped gas capillary C (top closed) beside the bulb
    o.append(_rect(364, 60, 14, 150, fill="#f4f7fa", sw=1.4))
    o.append(_line(364, 60, 378, 60, sw=1.8))
    o.append(T(386, 92, "C", 10, color=INK))
    o.append(T(390, 108, "mao dẫn / capillary C", 7.4, color=GREY, anchor="start"))
    # connecting capillary between bulb and C
    o.append(_path("M322,208 C346,208 348,210 364,210", sw=3.2, color="#b9c7d2"))
    # cut-off mark F
    o.append(_line(258, 150, 304, 150, sw=1.4, color=RED, dash="5 3"))
    o.append(T(244, 147, "F", 9.0, color=RED))
    o.append(T(196, 162, "vạch cắt / cut-off", 7.4, color=RED, anchor="start"))
    # mercury filling in bulb and bottom stem
    o.append(_rect(270, 244, 20, 60, fill="#9fb0bc", sw=1.2))
    o.append(_path("M280,252 C258,262 254,284 270,300 L290,300 C306,284 302,262 280,252",
                   fill="#9fb0bc", sw=1.2))
    o.append(_rect(272, 300, 16, 34, fill="#9fb0bc", sw=1.2))
    # movable mercury sump
    o.append(_path("M214,334 L346,334 L336,382 L224,382 Z", fill="#c9d3db", sw=1.6))
    o.append(_rect(226, 350, 108, 28, fill="#9fb0bc", sw=0.8))
    o.append(_arrow(380, 350, 380, 318, sw=1.2, color=RED))
    o.append(_arrow(380, 350, 380, 382, sw=1.2, color=RED))
    o.append(T(398, 366, "nâng/hạ / raise and lower", 7.4, color=RED, anchor="start"))
    o.append(T(280, 378, "bình thủy ngân / mercury sump", 7.4, color=GREY))
    # Boyle's law reminder
    o.append(T(480, 130, "p1·V1 = p2·V2", 10, color=BLUE))
    o.append(T(480, 152, "(định luật Boyle / Boyle's law)", 7.6, color=GREY))
    o.append(T(480, 186, "p chưa biết → thể tích biết", 7.8, color=INK, anchor="start"))
    o.append(T(480, 204, "unknown p → known volume", 7.6, color=GREY, anchor="start"))
    o.append(_callouts([(140, 190, 244, 208), (470, 92, 378, 90),
                        (140, 296, 270, 286), (470, 250, 372, 216)]))
    o.append(_legend([
        "Bình cầu B / bulb B", "Mao dẫn C / capillary C",
        "Vạch cắt F / cut-off F", "Thủy ngân / mercury",
    ], 40, 302, lh=16, size=7.4))
    o.append(_foot(w, 386, "Hình 2.3 · Đồng hồ McLeod / McLeod gauge"))
    s = svg(w, h, "".join(o), esc("Figure 2.3 - McLeod gauge"))
    return _fig(s,
                "Hình 2.3 (nguyên bản Hình 3) · Đồng hồ McLeod: bình cầu B và mao dẫn C được nối "
                "với áp suất cần đo; khi nâng bình thủy ngân, tại vạch cắt F một thể tích khí biết "
                "trước bị giam lại và áp suất được suy theo định luật Boyle p1·V1 = p2·V2. Các số "
                "chỉ: 1. Bình cầu B; 2. Mao dẫn C; 3. Vạch cắt F; 4. Thủy ngân; 5. Bình chứa thủy ngân.",
                "Figure 2.3 (source Figure 3) · McLeod gauge: bulb B and capillary C are connected "
                "to the unknown pressure; as the mercury sump is raised, a known gas volume is "
                "trapped at cut-off F and pressure follows Boyle's law p1·V1 = p2·V2. Callouts: "
                "1. Bulb B; 2. Capillary C; 3. Cut-off F; 4. Mercury; 5. Mercury sump.",
                "Sơ đồ đồng hồ McLeod với bình cầu, mao dẫn, vạch cắt và bình thủy ngân di động",
                "Schematic of the McLeod gauge with bulb, capillary, cut-off and movable mercury sump")


# ---------------------------------------------------------------------------
@_reg
def fig_f04():
    """Figure 4 - principle of the radiometer-effect gauge."""
    w, h = 640, 340
    o = [_defs()]
    # two plane-parallel plates
    o.append(_rect(140, 86, 340, 16, fill="#f2c7b5", sw=1.6))
    o.append(_rect(140, 224, 340, 16, fill="#d9e2ea", sw=1.6))
    o.append(T(310, 76, "Bản 1 / plate 1 — nóng T1", 8.6, color=RED))
    o.append(T(310, 258, "Bản 2 / plate 2 — lạnh T2", 8.6, color=BLUE))
    o.append(T(500, 86, "T1 > T2", 8.4, color=INK, anchor="start"))
    o.append(T(500, 238, "T2 có thể là nhiệt độ môi trường", 7.4, color=GREY, anchor="start"))
    o.append(T(500, 254, "T2 may be ambient temperature", 7.4, color=GREY, anchor="start"))
    # gap d between plates
    o.append(_line(96, 102, 96, 224, sw=1.0, color=GREY))
    o.append(_line(90, 102, 102, 102, sw=1.0, color=GREY))
    o.append(_line(90, 224, 102, 224, sw=1.0, color=GREY))
    o.append(T(84, 166, "d", 10, color=INK))
    # molecular impacts from hot plate to cold plate
    for x in (190, 250, 310, 370, 430):
        o.append(_arrow(x, 118, x, 200, sw=1.4, color=RED))
        o.append(_circle(x, 128, 3.5, fill=RED))
    for x in (220, 340, 460):
        o.append(_arrow(x, 212, x, 138, sw=1.0, color=BLUE, dash="3 4"))
    # mean free path squiggle with label
    o.append(_path("M150,282 q10,-9 20,0 t20,0 t20,0 t20,0 t20,0 t20,0 t20,0",
                   sw=1.4, color=GREEN))
    o.append(T(360, 286, "Λ = đường tự do trung bình / mean free path", 7.8,
              color=GREEN, anchor="start"))
    o.append(T(310, 328, "d < Λ/10  →  chế độ phân tử tự do / free-molecule regime", 8.4,
              color=INK))
    o.append(_callouts([(126, 120, 168, 94), (126, 218, 168, 230),
                        (560, 160, 470, 160)]))
    o.append(T(40, 296, "1. Bản nóng / hot plate   2. Bản lạnh / cold plate   "
                        "3. Va chạm phân tử / molecular impacts", 7.4, anchor="start"))
    s = svg(w, h, "".join(o), esc("Figure 2.4 - Principle of the radiometer-effect gauge"))
    return _fig(s,
                "Hình 2.4 (nguyên bản Hình 4) · Nguyên lý đồng hồ hiệu ứng phóng xạ nhiệt: hai bản "
                "song song, cùng diện tích nhưng ở nhiệt độ T1 và T2 khác nhau, cách nhau d nhỏ hơn "
                "Λ/10; các phân tử từ bản nóng va chạm mạnh hơn gây chênh áp lên hai mặt bản 2. "
                "Các số chỉ: 1. Bản nóng; 2. Bản lạnh; 3. Va chạm phân tử.",
                "Figure 2.4 (source Figure 4) · Principle of the radiometer-effect gauge: two "
                "plane-parallel plates of equal area at different temperatures T1 and T2, spaced "
                "by d &lt; Λ/10; molecules from the hotter plate strike harder, producing a pressure "
                "difference across plate 2. Callouts: 1. Hot plate; 2. Cold plate; 3. Molecular impacts.",
                "Hai bản song song ở nhiệt độ khác nhau với các mũi tên va chạm phân tử",
                "Two plane-parallel plates at different temperatures with molecular impact arrows")


# ---------------------------------------------------------------------------
@_reg
def fig_f05():
    """Figure 5 - construction of the radiometer-effect gauge."""
    w, h = 620, 380
    o = [_defs()]
    # vacuum housing
    o.append(_rect(120, 40, 310, 300, fill="#fbfaf7", sw=1.6))
    o.append(T(275, 32, "vỏ chân không / vacuum enclosure", 8.0, color=GREY))
    # suspension fibre and vane (plate 2)
    o.append(_line(274, 56, 274, 146, sw=1.6, color=GREY))
    o.append(_rect(228, 146, 92, 92, fill="#d9e2ea", sw=1.6))
    o.append(T(274, 196, "2", 14, color=INK, weight="600"))
    o.append(T(274, 256, "bản treo / suspended plate 2", 7.8, color=GREY))
    # fixed hot plate 1 on the left of the vane
    o.append(_rect(148, 160, 52, 64, fill="#f2c7b5", sw=1.4))
    o.append(T(174, 154, "1 / T1", 7.8, color=RED))
    # mirror and optical lever
    o.append(_rect(286, 158, 12, 36, fill="#e8eef4", sw=1.2))
    o.append(_arrow(330, 176, 410, 176, sw=1.0, color=RED))
    o.append(_arrow(410, 176, 330, 192, sw=1.0, color=RED))
    o.append(_rect(414, 128, 12, 96, fill="#eef2f6", sw=1.2))
    o.append(T(420, 118, "thang đọc / scale", 7.6, color=GREY))
    # torsion arrow around fibre
    o.append(_path("M252,110 q22,-18 44,0", sw=1.2, color=BLUE))
    o.append(_arrow(296, 110, 288, 118, sw=1.2, color=BLUE))
    o.append(T(320, 106, "góc xoắn γ / torsion γ", 7.8, color=BLUE, anchor="start"))
    o.append(_callouts([(136, 152, 174, 176), (136, 248, 228, 220),
                        (340, 92, 274, 140)]))
    o.append(T(40, 360, "1. Bản nóng cố định / fixed hot plate   "
                        "2. Bản treo / suspended plate   3. Sợi treo / suspension fibre   "
                        "4. Gương và thang đọc / mirror and scale", 7.4, anchor="start"))
    o.append(_foot(w, 378, "Hình 2.5 · Cấu tạo đồng hồ hiệu ứng phóng xạ nhiệt / radiometer gauge"))
    s = svg(w, h, "".join(o), esc("Figure 2.5 - Construction of the radiometer-effect gauge"))
    return _fig(s,
                "Hình 2.5 (nguyên bản Hình 5) · Cấu tạo đồng hồ hiệu ứng phóng xạ nhiệt: bản 2 được "
                "treo bằng sợi như trong galvanometer; chênh áp giữa hai mặt bản tạo mô-men làm bản "
                "xoắn, và mô-men đàn hồi của sợi treo cân bằng lại nên góc xoắn cho biết áp suất. "
                "Các số chỉ: 1. Bản nóng cố định; 2. Bản treo; 3. Sợi treo; 4. Gương và thang đọc.",
                "Figure 2.5 (source Figure 5) · Construction of the radiometer-effect gauge: plate 2 "
                "is suspended as in a galvanometer; the pressure difference produces a torque, "
                "balanced by the elastic moment of the suspension, so the torsion angle indicates "
                "pressure. Callouts: 1. Fixed hot plate; 2. Suspended plate; 3. Suspension fibre; "
                "4. Mirror and scale.",
                "Bản cảm biến treo bằng sợi trong vỏ chân không, có gương và thang đọc quang học",
                "Suspended vane in a vacuum enclosure with a mirror and optical scale")


# ---------------------------------------------------------------------------
@_reg
def fig_f06():
    """Figure 6 - torsion angle gamma vs pressure p (chart)."""
    w, h = 620, 340
    o = [_defs()]
    x0, y0, W, H = 96, 56, 430, 220
    o.append(T(310, 28, "Góc xoắn γ theo áp suất p / torsion angle γ vs pressure p", 9.2,
              color=INK))
    o.append(_arrow(x0, y0 + H, x0 + W + 16, y0 + H, sw=1.2))
    o.append(_arrow(x0, y0 + H, x0, y0 - 12, sw=1.2))
    o.append(T(x0 + W + 22, y0 + H + 8, "p (mbar, log)", 8.2, color=GREY,
              anchor="start"))
    o.append(T(x0 + 8, y0 - 18, "γ", 10, color=GREY))
    # log ticks from 1e-10 to 1e-2
    ticks = [(i / 8.0, lab) for i, lab in zip((0, 2, 4, 6, 8),
                                              ("10⁻¹⁰", "10⁻⁸", "10⁻⁶", "10⁻⁴", "10⁻²"))]
    for frac, lab in ticks:
        px = x0 + frac * W
        o.append(_line(px, y0 + H, px, y0 + H + 4, sw=0.8))
        o.append(T(px, y0 + H + 17, lab, 7.4, color=GREY))
    for frac, lab in ((0, "0"), (0.5, "γ/2"), (1, "γmax")):
        py = y0 + H - frac * H
        o.append(_line(x0 - 4, py, x0, py, sw=0.8))
        o.append(T(x0 - 8, py + 3, lab, 7.4, color=GREY, anchor="end"))
    # increasing, saturating characteristic gamma = gmax*(1-exp(-k*t))
    pts = []
    for i in range(101):
        t = i / 100.0
        g = 1 - math.exp(-7.0 * t)
        pts.append((x0 + t * W, y0 + H - g * H))
    o.append(_poly(pts, sw=2.6, color=BLUE))
    # low pressure limit marker
    o.append(_line(x0 + 0.25 * W, y0 + 10, x0 + 0.25 * W, y0 + H,
                   sw=0.9, color=RED, dash="4 4"))
    o.append(T(x0 + 0.25 * W + 6, y0 + 24, "≈10⁻⁸ mbar giới hạn / limit", 7.4,
              color=RED, anchor="start"))
    o.append(T(x0 + W * 0.66, y0 + H * 0.30, "γ tăng theo p", 8.0,
              color=BLUE, anchor="start"))
    o.append(T(x0 + W * 0.66, y0 + H * 0.30 + 15, "γ rises with p", 7.6,
              color=GREY, anchor="start"))
    o.append(_foot(w, 326, "Hình 2.6 (nguyên bản Hình 6) · Góc xoắn γ tỉ lệ với áp suất p; "
                   "phép đo độc lập với loại khí / independent of gas kind"))
    s = svg(w, h, "".join(o), esc("Figure 2.6 - Torsion angle vs pressure chart"))
    return _fig(s,
                "Hình 2.6 (nguyên bản Hình 6) · Đồ thị góc xoắn γ theo áp suất p (trục p logarithm, "
                "từ khoảng 10⁻¹⁰ đến 10⁻² mbar): γ tăng dần và bão hòa ở áp suất cao; giới hạn áp "
                "suất thấp của một số bản chế tạo khoảng 10⁻⁸ mbar. Theo phương trình 1, phép đo "
                "không phụ thuộc vào loại khí.",
                "Figure 2.6 (source Figure 6) · Chart of torsion angle γ vs pressure p (log p axis "
                "from about 10⁻¹⁰ to 10⁻² mbar): γ rises and saturates at higher pressure; some "
                "versions have a low-pressure limit near 10⁻⁸ mbar. By Equation 1 the method is "
                "independent of the kind of gas.",
                "Đồ thị đường cong góc xoắn tăng dần theo áp suất trên trục logarithm",
                "Chart of a saturating torsion-angle curve against logarithmic pressure")


# ---------------------------------------------------------------------------
@_reg
def fig_f07():
    """Figure 7 - cut-away and packaged electronic pressure sensor."""
    w, h = 680, 350
    o = [_defs()]
    o.append(T(175, 28, "(trái) Mặt cắt cảm biến áp suất điện tử", 8.6, color=INK))
    o.append(T(505, 28, "(phải) Cảm biến áp suất", 8.6, color=INK))
    o.append(_line(340, 44, 340, 300, sw=0.8, color="#cfd5db", dash="4 5"))
    # ---- left: cutaway housing
    o.append(_rect(96, 70, 210, 210, fill="#e9eef3", sw=1.8))
    o.append(_rect(116, 134, 170, 18, fill="#d9e2ea", sw=1.4))
    o.append(T(201, 130, "màng / diaphragm", 7.6, color=BLUE))
    # strain gauges bonded on the diaphragm: zig-zag strips
    for gx in (140, 244):
        zz = []
        for k in range(8):
            zz.append((gx + (7 if k % 2 else -7), 158 + k * 5))
        o.append(_poly(zz, sw=1.8, color=RED))
        o.append(T(gx, 205, "R", 7.0, color=RED))
    o.append(_rect(140, 218, 122, 30, fill="#fdf3e6", sw=1.2))
    o.append(T(201, 237, "mạch điện tử / electronics", 7.4, color=GREY))
    # pressure port from below
    o.append(_rect(178, 280, 46, 34, fill="#c9d7e2", sw=1.4))
    o.append(_arrow(201, 312, 201, 288, sw=1.4, color=BLUE))
    o.append(T(201, 334, "p →", 8.4, color=BLUE))
    # cable
    o.append(_line(306, 232, 348, 232, sw=2.0, color=GREY))
    # ---- right: packaged sensor
    o.append(_circle(500, 176, 68, fill="#eef2f6", sw=1.8))
    o.append(_rect(500, 108, 84, 136, fill="#dce5ec", sw=1.6))
    o.append(_rect(584, 138, 34, 76, fill="#e9eef3", sw=1.4))
    for yy in (152, 170, 188, 206):
        o.append(_line(618, yy, 640, yy, sw=1.8, color=GREY))
    o.append(T(625, 134, "chân tín hiệu / pins", 7.4, color=GREY))
    o.append(_rect(464, 236, 72, 26, fill="#c9d7e2", sw=1.4))
    o.append(T(500, 278, "cổng áp suất / pressure port", 7.6, color=GREY))
    o.append(T(500, 300, "vỏ kim loại / metal housing", 7.6, color=GREY))
    o.append(_callouts([(60, 120, 116, 142), (60, 196, 140, 180),
                        (330, 172, 264, 150), (560, 300, 520, 242)]))
    o.append(T(40, 334, "1. Vỏ / housing   2. Màng / diaphragm   3. Strain gauge   "
                        "4. Cổng áp suất / pressure port", 7.4, anchor="start"))
    s = svg(w, h, "".join(o), esc("Figure 2.7 - Electronic pressure sensor"))
    return _fig(s,
                "Hình 2.7 (nguyên bản Hình 7) · (trái) Mặt cắt cảm biến áp suất điện tử: áp suất "
                "làm màng biến dạng, các strain gauge dán trên màng đổi điện trở; (phải) cảm biến "
                "hoàn chỉnh với vỏ kim loại, cổng áp suất và chân tín hiệu. Các số chỉ: 1. Vỏ; "
                "2. Màng; 3. Strain gauge; 4. Cổng áp suất.",
                "Figure 2.7 (source Figure 7) · (left) Cut-away of an electronic pressure sensor: "
                "pressure deflects a diaphragm and bonded strain gages change resistance; "
                "(right) the packaged pressure sensor with metal housing, port and pins. "
                "Callouts: 1. Housing; 2. Diaphragm; 3. Strain gage; 4. Pressure port.",
                "Mặt cắt cảm biến áp suất với màng, strain gauge và cảm biến hoàn chỉnh",
                "Cut-away of a pressure sensor showing diaphragm and strain gages, plus packaged unit")


# ---------------------------------------------------------------------------
@_reg
def fig_f08():
    """Figure 8 - cut-away of a metering orifice."""
    w, h = 660, 320
    o = [_defs()]
    # pipe walls
    o.append(_rect(60, 96, 540, 128, fill="#eef3f7", sw=1.8))
    o.append(_rect(60, 96, 540, 10, fill="url(#h6)", sw=1.0))
    o.append(_rect(60, 214, 540, 10, fill="url(#h6)", sw=1.0))
    # orifice plate with hole
    o.append(_rect(332, 96, 18, 128, fill="#d9dee4", sw=1.6))
    o.append(_rect(332, 140, 18, 40, fill="#fbfaf7", sw=1.4))
    o.append(T(341, 88, "tấm chắn / orifice plate", 7.8, color=GREY))
    # flow arrows and contraction
    for yy in (126, 160, 194):
        o.append(_arrow(80, yy, 300, yy, sw=1.4, color=BLUE))
        o.append(_arrow(360, yy, 470, yy, sw=1.4, color=BLUE))
    o.append(_path("M350,140 C382,142 396,150 420,160 C396,170 382,178 350,180",
                   sw=1.2, color=RED, dash="3 3"))
    o.append(T(438, 114, "vena contracta", 7.4, color=RED, anchor="start"))
    # pressure taps
    o.append(_line(230, 96, 230, 62, sw=1.4, color=INK))
    o.append(_line(430, 96, 430, 62, sw=1.4, color=INK))
    o.append(T(230, 54, "P1", 9.0, color=INK))
    o.append(T(430, 54, "P2", 9.0, color=INK))
    o.append(_line(230, 74, 430, 74, sw=0.9, color=GREY, dash="4 4"))
    o.append(T(330, 68, "Δp", 8.6, color=RED))
    o.append(T(120, 250, "Q ∝ √Δp  (K hằng số / K constant)", 9.0, color=BLUE))
    o.append(_callouts([(120, 62, 230, 92), (540, 62, 430, 92),
                        (341, 244, 341, 206)]))
    o.append(T(40, 290, "1. Áp suất trước / upstream tap   2. Áp suất sau / downstream tap   "
                        "3. Lỗ tiết lưu / metering orifice", 7.6, anchor="start"))
    o.append(_foot(w, 314, "Hình 2.8 · Mặt cắt lỗ tiết lưu / cut-away of a metering orifice"))
    s = svg(w, h, "".join(o), esc("Figure 2.8 - Cut-away of a metering orifice"))
    return _fig(s,
                "Hình 2.8 (nguyên bản Hình 8) · Mặt cắt lỗ tiết lưu: một tấm có lỗ đặt trong "
                "dòng chảy làm co hẹp dòng, đo chênh áp giữa hai bên tấm (P1 - P2) để suy lưu lượng; "
                "căn bậc hai của chênh áp tỉ lệ với lưu lượng, Q = K·√Δp. Các số chỉ: 1. Điểm đo "
                "trước; 2. Điểm đo sau; 3. Lỗ tiết lưu.",
                "Figure 2.8 (source Figure 8) · Cut-away of a metering orifice: a plate with a hole "
                "constricts the flow; measuring the differential pressure P1 - P2 across the "
                "constriction gives the flow rate, Q = K·√Δp. Callouts: 1. Upstream tap; "
                "2. Downstream tap; 3. Metering orifice.",
                "Mặt cắt ống dẫn có tấm lỗ tiết lưu và hai điểm đo chênh áp",
                "Pipe cutaway with an orifice plate and two differential-pressure taps")


# ---------------------------------------------------------------------------
@_reg
def fig_f09():
    """Figure 9 - gauge head of the thermal conductivity gauge."""
    w, h = 620, 360
    o = [_defs()]
    # glass envelope
    o.append(_path("M230,56 C180,56 180,116 180,176 C180,250 206,300 310,300 "
                   "C414,300 440,250 440,176 C440,116 440,56 390,56 Z",
                   fill="#fbfaf7", sw=1.8))
    o.append(T(310, 46, "vỏ thủy tinh / glass envelope", 8.0, color=GREY))
    # heated wire in the centre
    o.append(_line(310, 82, 310, 250, sw=3.0, color=RED))
    o.append(T(330, 122, "dây nóng / heated wire", 7.8, color=RED, anchor="start"))
    # leads through the top
    for x in (296, 324):
        o.append(_line(x, 56, x, 22, sw=1.6, color=GREY))
    o.append(T(310, 16, "dây dẫn / leads  (i)", 7.6, color=GREY))
    # heat losses
    o.append(_arrow(300, 150, 240, 110, sw=1.2, color=BLUE))
    o.append(T(196, 102, "(ii) bức xạ / radiation", 7.4, color=BLUE, anchor="start"))
    o.append(_arrow(324, 190, 396, 162, sw=1.2, color=GREEN))
    o.append(T(404, 156, "(iii) qua phân tử / molecules", 7.4, color=GREEN, anchor="start"))
    o.append(_arrow(320, 226, 262, 268, sw=1.2, color=GREY, dash="3 3"))
    o.append(T(200, 282, "(i) qua dây dẫn / leads", 7.4, color=GREY, anchor="start"))
    # gas molecules (dots)
    for px, py in ((232, 160), (256, 200), (378, 200), (400, 232), (270, 120), (360, 118)):
        o.append(_circle(px, py, 3, fill="#9fb0bc"))
    o.append(T(310, 330, "dải đo / range: mm Hg → 10⁻³ mm Hg", 8.4, color=INK))
    o.append(_foot(w, 352, "Hình 2.9 · Đầu đo của đồng hồ dẫn nhiệt / thermal-conductivity gauge head"))
    s = svg(w, h, "".join(o), esc("Figure 2.9 - Thermal conductivity gauge head"))
    return _fig(s,
                "Hình 2.9 (nguyên bản Hình 9) · Đầu đo của đồng hồ dẫn nhiệt: dây nóng trong vỏ "
                "thủy tinh mất nhiệt qua (i) dây dẫn, (ii) bức xạ ra môi trường và (iii) dẫn qua "
                "các phân tử khí; chỉ thành phần thứ ba phụ thuộc áp suất trong dải khoảng từ mm Hg "
                "đến 10⁻³ mm Hg.",
                "Figure 2.9 (source Figure 9) · Gauge head of the thermal conductivity gauge: a "
                "heated wire in a glass envelope loses heat (i) through leads, (ii) by radiation "
                "and (iii) by conduction through gas molecules; only the last depends on pressure "
                "over the range from mm of Hg to 10⁻³ mm Hg.",
                "Đầu đo có dây nóng trong vỏ thủy tinh với ba đường mất nhiệt",
                "Gauge head with a heated wire in a glass envelope and three heat-loss paths")


# ---------------------------------------------------------------------------
@_reg
def fig_f10():
    """Figure 10 - thermocouple gauge head."""
    w, h = 620, 340
    o = [_defs()]
    o.append(_path("M200,64 C152,64 152,124 152,184 C152,254 180,296 310,296 "
                   "C440,296 468,254 468,184 C468,124 468,64 420,64 Z",
                   fill="#fbfaf7", sw=1.8))
    o.append(T(310, 54, "vỏ / envelope", 8.0, color=GREY))
    # heated filament and thermocouple junction
    o.append(_line(244, 92, 244, 236, sw=2.2, color=RED))
    o.append(_circle(244, 236, 6, fill="#f6d9a8", sw=1.2))
    o.append(_line(244, 236, 366, 236, sw=1.8, color=BLUE))
    o.append(T(205, 168, "dây gia nhiệt / heated wire", 7.8, color=RED, anchor="start"))
    o.append(T(302, 226, "cặp nhiệt điện / thermocouple", 7.6, color=BLUE, anchor="start"))
    # lead wires
    for x, col in ((244, RED), (366, BLUE)):
        o.append(_line(x, 92, x, 24, sw=1.6, color=col))
    o.append(T(310, 18, "dây dẫn tới cầu đo / leads to measuring circuit", 7.6, color=GREY))
    o.append(_arrow(270, 128, 216, 128, sw=1.0, color=RED))
    o.append(T(280, 132, "I", 8.0, color=RED, anchor="start"))
    o.append(_callouts([(120, 200, 244, 200), (490, 228, 366, 236)]))
    o.append(T(40, 322, "1. Dây gia nhiệt / heated wire   2. Mối nối nhiệt / thermocouple junction   "
                        "3. Dây dẫn / leads", 7.4, anchor="start"))
    o.append(_foot(w, 338, "Hình 2.10 · Đầu đo thermocouple / thermocouple gauge head"))
    s = svg(w, h, "".join(o), esc("Figure 2.10 - Thermocouple gauge head"))
    return _fig(s,
                "Hình 2.10 (nguyên bản Hình 10) · Đầu đo thermocouple: thay vì đo điện trở của dây "
                "nóng, một cặp nhiệt điện tiếp xúc trực tiếp với dây và đo nhiệt độ của dây như "
                "thước đo áp suất. Các số chỉ: 1. Dây gia nhiệt; 2. Mối nối nhiệt; 3. Dây dẫn.",
                "Figure 2.10 (source Figure 10) · Thermocouple gauge head: instead of measuring the "
                "wire's electrical resistance, a thermocouple is kept in contact with the heated "
                "wire and measures its temperature directly as a measure of pressure. Callouts: "
                "1. Heated wire; 2. Thermocouple junction; 3. Leads.",
                "Đầu đo có dây nóng và cặp nhiệt điện tiếp xúc với dây",
                "Gauge head with a heated wire and a thermocouple in contact with it")


# ---------------------------------------------------------------------------
@_reg
def fig_f11():
    """Figure 11 - hot cathode ionisation gauge."""
    w, h = 620, 370
    o = [_defs()]
    o.append(_path("M196,52 C148,52 148,122 148,196 C148,286 190,330 310,330 "
                   "C430,330 472,286 472,196 C472,122 472,52 424,52 Z",
                   fill="#fbfaf7", sw=1.8))
    o.append(T(310, 42, "vỏ thủy tinh nối với chân không / envelope to vacuum", 7.8, color=GREY))
    # grid anode (cylinder outline) and collector plate
    o.append(_rect(238, 102, 144, 170, fill="none", sw=1.4, stroke=GREY))
    for x in (250, 264, 278, 292, 306, 320, 334, 348, 362, 376):
        o.append(_line(x, 102, x, 272, sw=0.5, color="#dfe6ec"))
    o.append(T(310, 94, "grid anode", 7.8, color=GREY))
    o.append(_line(220, 132, 220, 244, sw=3.2, color=BLUE))
    o.append(T(214, 126, "collector", 7.6, color=BLUE, anchor="end"))
    # filament cathode
    o.append(_path("M270,300 q14,-22 28,0 t28,0 t28,0", sw=2.6, color=RED))
    o.append(T(310, 324, "filament (hot cathode)", 7.6, color=RED))
    # electron and ion tracks
    for x in (274, 296, 318, 340):
        o.append(_arrow(x, 276, x, 140, sw=1.0, color=RED))
        o.append(_circle(x, 232, 3, fill=GREEN))
    o.append(_arrow(286, 232, 226, 232, sw=1.1, color=GREEN))
    o.append(T(390, 200, "electron → ion → collector", 7.6, color=GREEN, anchor="start"))
    o.append(_callouts([(120, 148, 220, 172), (120, 270, 282, 300),
                        (510, 140, 382, 140)]))
    o.append(T(40, 354, "1. Bản collector âm / negative collector   "
                        "2. Catốt dây đốt nóng / hot filament cathode   "
                        "3. Lưới anode / grid anode", 7.4, anchor="start"))
    o.append(_foot(w, 368, "Hình 2.11 · Đồng hồ ion hóa catốt nóng / hot-cathode ionization gauge"))
    s = svg(w, h, "".join(o), esc("Figure 2.11 - Ionisation gauge"))
    return _fig(s,
                "Hình 2.11 (nguyên bản Hình 11) · Đồng hồ ion hóa catốt nóng gồm catốt là dây đốt "
                "nóng, lưới anode và bản collector âm; electron va chạm phân tử khí tạo ion dương, "
                "dòng ion thu được tỉ lệ với áp suất. Các số chỉ: 1. Bản collector âm; "
                "2. Catốt dây đốt nóng; 3. Lưới anode.",
                "Figure 2.11 (source Figure 11) · Hot-cathode ionisation gauge with a heated "
                "filament cathode, grid anode and negative collector plate; electrons collide with "
                "gas molecules, the resulting ion current being a measure of pressure. Callouts: "
                "1. Negative collector; 2. Hot filament cathode; 3. Grid anode.",
                "Sơ đồ đồng hồ ion hóa ba điện cực với dây đốt, lưới và bản collector",
                "Three-electrode ionisation gauge with filament, grid and collector plate")


# ---------------------------------------------------------------------------
@_reg
def fig_f12():
    """Figure 12 - cold cathode ionization gauge (Penning gauge)."""
    w, h = 640, 360
    o = [_defs()]
    # two cathodes and ring anode
    o.append(_rect(196, 92, 16, 176, fill="#d9e2ea", sw=1.5))
    o.append(_rect(428, 92, 16, 176, fill="#d9e2ea", sw=1.5))
    o.append(_ellipse(320, 180, 78, 52, fill="none", sw=3.0, color=GREEN))
    o.append(T(320, 118, "anode vòng / ring anode", 7.8, color=GREEN))
    o.append(T(204, 84, "catốt / cathode", 7.6, color=BLUE, anchor="start"))
    o.append(T(444, 84, "catốt / cathode", 7.6, color=BLUE, anchor="start"))
    # helical electron path
    path = []
    for i in range(61):
        t = i / 60.0
        path.append((214 + t * 212, 180 + 38 * math.sin(t * 8 * math.pi)))
    o.append(_poly(path, sw=1.4, color=RED))
    o.append(T(320, 284, "đường xoắn ốc electron / helical electron path", 7.8, color=RED))
    # magnetic poles and field
    o.append(_rect(150, 128, 34, 104, fill="url(#h6)", sw=1.2))
    o.append(_rect(456, 128, 34, 104, fill="url(#h6)", sw=1.2))
    o.append(T(167, 122, "N", 9.0, color=INK))
    o.append(T(473, 122, "S", 9.0, color=INK))
    o.append(T(320, 312, "từ trường vuông góc / magnetic field ⟂ cathodes  ·  ~2 kV", 8.2,
              color=INK))
    o.append(_callouts([(160, 214, 204, 200), (500, 214, 444, 200),
                        (400, 132, 386, 150)]))
    o.append(T(40, 336, "1. Catốt zirconium / zirconium cathode   2. Anode vòng / ring anode   "
                        "3. Từ trường / magnetic field", 7.4, anchor="start"))
    o.append(_foot(w, 354, "Hình 2.12 · Đồng hồ ion hóa catốt lạnh / cold-cathode ionization gauge"))
    s = svg(w, h, "".join(o), esc("Figure 2.12 - Cold cathode ionization gauge"))
    return _fig(s,
                "Hình 2.12 (nguyên bản Hình 12) · Đồng hồ ion hóa catốt lạnh (Penning): hai bản "
                "catốt và một anode vòng, đặt trong từ trường vuông góc với mặt điện cực; electron "
                "đi đường xoắn ốc dài nên ion hóa khí cả ở áp suất thấp, dòng ion cho biết áp suất. "
                "Các số chỉ: 1. Catốt zirconium/thorium; 2. Anode vòng; 3. Từ trường.",
                "Figure 2.12 (source Figure 12) · Cold-cathode (Penning) ionization gauge: two "
                "plate cathodes and a ring anode in a magnetic field perpendicular to the "
                "electrode plane; electrons follow long helical paths, ionising the gas even at "
                "low pressure, and the ion current measures pressure. Callouts: 1. Zirconium/"
                "thorium cathode; 2. Ring anode; 3. Magnetic field.",
                "Hai bản catốt và anode vòng với đường electron xoắn ốc trong từ trường",
                "Two cathode plates and a ring anode with helical electron paths in a magnetic field")


# ---------------------------------------------------------------------------
@_reg
def fig_f13():
    """Figure 13 - Bourdon tube designs (A, B, C)."""
    w, h = 660, 320
    o = [_defs()]
    labels = [("A", "Chữ C / C-shape"), ("B", "Xoắn ốc / spiral"),
              ("C", "Ốc vít / helical")]
    for i, (tag, name) in enumerate(labels):
        cx = 130 + i * 210
        o.append(_rect(cx - 96, 52, 192, 220, fill="#fbfaf7", sw=1.2))
        o.append(T(cx - 76, 76, "(%s) %s" % (tag, name), 8.2, color=INK))
        o.append(_rect(cx - 78, 218, 40, 26, fill="#c9d7e2", sw=1.3))
        o.append(T(cx - 58, 258, "đầu nối / inlet", 7.2, color=GREY))
        if i == 0:
            o.append(_path("M%d,216 A70,70 0 1 1 %d,216" % (cx + 38, cx + 38),
                           sw=7, color=BLUE))
            o.append(_line(cx + 38, 216, cx + 38, 146, sw=2.0, color=GREY))
            o.append(_circle(cx + 38, 146, 4, fill=RED))
        elif i == 1:
            pts = []
            for k in range(90):
                t = k / 89.0
                r = 12 + 64 * t
                a = t * 4.0 * math.pi
                pts.append((cx - 20 + r * math.cos(a), 178 + r * math.sin(a) * 0.9))
            o.append(_poly(pts, sw=5, color=BLUE))
            o.append(_circle(pts[-1][0], pts[-1][1], 4, fill=RED))
        else:
            pts = []
            for k in range(90):
                t = k / 89.0
                a = t * 4.5 * math.pi
                pts.append((cx - 20 + 54 * t, 178 + 40 * math.sin(a) * (1 - 0.4 * t)))
            o.append(_poly(pts, sw=5, color=BLUE))
            o.append(_circle(pts[-1][0], pts[-1][1], 4, fill=RED))
        o.append(T(cx, 296, "đầu tự do → kim / free tip → pointer", 7.4, color=GREY))
    o.append(_foot(w, 314, "Hình 2.13 · Thiết kế ống Bourdon / Bourdon tube designs "
                   "(A: chữ C, B: xoắn ốc, C: ốc vít)"))
    s = svg(w, h, "".join(o), esc("Figure 2.13 - Bourdon tube designs"))
    return _fig(s,
                "Hình 2.13 (nguyên bản Hình 13) · Thiết kế ống Bourdon: (A) ống chữ C có mặt cắt "
                "oval, một đầu nối áp suất quá trình, đầu kia bịt và nối cơ cấu kim; (B) dạng xoắn "
                "ốc và (C) dạng ốc vít giúp tăng chiều dài góc, chuyển động đầu ống và độ phân giải.",
                "Figure 2.13 (source Figure 13) · Bourdon tube designs: (A) a C-shaped tube of oval "
                "cross-section with one end connected to process pressure and the sealed end "
                "driving the pointer; (B) spiral and (C) helical forms increase effective angular "
                "length, tip travel and resolution.",
                "Ba thiết kế ống Bourdon: chữ C, xoắn ốc và ốc vít",
                "Three Bourdon tube designs: C-shaped, spiral and helical")


# ---------------------------------------------------------------------------
@_reg
def fig_f14():
    """Figure 14 - pressure sensor diaphragm designs."""
    w, h = 640, 320
    o = [_defs()]
    designs = [("phẳng / flat", 0), ("gờ sóng / corrugated", 1), ("có bướu / bossed", 2)]
    for i, (name, kind) in enumerate(designs):
        cx = 120 + i * 200
        o.append(_rect(cx - 88, 56, 176, 206, fill="#fbfaf7", sw=1.2))
        o.append(T(cx, 80, "(%s) %s" % ("ABC"[i], name), 8.0, color=INK))
        o.append(_rect(cx - 78, 110, 156, 10, fill="url(#h6)", sw=1.0))
        o.append(_rect(cx - 78, 210, 156, 10, fill="url(#h6)", sw=1.0))
        if kind == 0:
            yline = [(x, 162 + 10 * math.sin(math.pi * (x - (cx - 70)) / 140))
                     for x in range(cx - 70, cx + 71, 10)]
            o.append(_poly(yline, sw=3.0, color=BLUE))
        elif kind == 1:
            yline = [(x, 160 + 9 * math.sin((x - (cx - 70)) * 0.38))
                     for x in range(cx - 70, cx + 71, 5)]
            o.append(_poly(yline, sw=2.6, color=BLUE))
        else:
            o.append(_line(cx - 70, 164, cx + 70, 164, sw=3.0, color=BLUE))
            o.append(_rect(cx - 18, 154, 36, 20, fill="#d9e2ea", sw=1.3))
        for gx in (cx - 46, cx + 46):
            o.append(_rect(gx - 8, 150, 16, 8, fill="none", sw=1.2, stroke=RED))
        o.append(T(cx, 240, "strain gauge dán / bonded gauge", 7.2, color=RED))
        o.append(T(cx, 270, "p →", 8.2, color=BLUE))
    o.append(_foot(w, 300, "Hình 2.14 · Thiết kế màng cảm biến áp suất / pressure-sensor diaphragm designs"))
    s = svg(w, h, "".join(o), esc("Figure 2.14 - Pressure sensor diaphragm designs"))
    return _fig(s,
                "Hình 2.14 (nguyên bản Hình 14) · Thiết kế màng cảm biến áp suất: màng phẳng, màng "
                "có gờ sóng và màng có bướu trung tâm; họ phần tử mềm gồm cả bellows và màng, với "
                "các strain gauge dán trên bề mặt để chuyển biến dạng thành tín hiệu điện.",
                "Figure 2.14 (source Figure 14) · Pressure sensor diaphragm designs: flat, "
                "corrugated and bossed diaphragms; the family of flexible elements also includes "
                "bellows, and bonded strain gages convert the diaphragm deflection into an "
                "electrical signal.",
                "Ba dạng màng cảm biến: phẳng, gờ sóng và có bướu, kèm strain gauge",
                "Three diaphragm designs: flat, corrugated and bossed, with bonded strain gages")


# ---------------------------------------------------------------------------
@_reg
def fig_f15():
    """Figure 15 - electronic pressure sensor ranges (chart/table-like)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "Dải cảm biến áp suất điện tử / Electronic Pressure Sensor Ranges", 9.2,
              color=INK))
    x0, x1 = 196, 626
    lo, hi = -8.0, 8.0

    def px(e):
        return x0 + (e - lo) / (hi - lo) * (x1 - x0)

    # horizontal axis with log ticks
    o.append(_arrow(x0, 316, x1 + 14, 316, sw=1.2))
    o.append(T(x1, 346, "p (Pa, log)", 8.2, color=GREY))
    exps = [(-8, "10⁻⁸"), (-6, "10⁻⁶"), (-4, "10⁻⁴"), (-2, "10⁻²"),
            (0, "10⁰"), (2, "10²"), (4, "10⁴"), (6, "10⁶"), (8, "10⁸")]
    for e, lab in exps:
        o.append(_line(px(e), 316, px(e), 321, sw=0.8))
        o.append(T(px(e), 334, lab, 7.0, color=GREY))
    rows = [
        ("Ionisation / ionisation", -8, -1, RED),
        ("Capacitance / điện dung", -4, 5, GREEN),
        ("Pirani / nhiệt", -1, 3, "#b07d2b"),
        ("Strain gage / biến dạng", 2, 8, BLUE),
        ("Bourdon tube / ống Bourdon", 3, 8, "#6a5a9a"),
    ]
    for i, (lab, a, b, col) in enumerate(rows):
        yy = 70 + i * 46
        o.append(T(x0 - 8, yy + 12, lab, 7.6, color=INK, anchor="end"))
        o.append(_line(x0, yy + 16, x1, yy + 16, sw=0.6, color="#e3e7eb"))
        o.append(_rect(px(a), yy, px(b) - px(a), 18, fill=col, sw=0.8))
        o.append(T(px(a) + 5, yy + 13, "10%d → 10%d" % (a, b), 7.2,
                   color="#ffffff", anchor="start"))
    o.append(T(40, 366, "Tham chiếu trong / internal reference: chân không (vacuum) hoặc áp suất "
                        "khí quyển (atmospheric pressure)", 7.6, color=GREY, anchor="start"))
    s = svg(w, h, "".join(o), esc("Figure 2.15 - Electronic pressure sensor ranges chart"))
    return _fig(s,
                "Hình 2.15 (nguyên bản Hình 15) · Biểu đồ dải đo của các loại cảm biến áp suất "
                "điện tử theo trục áp suất logarithm (Pa): ion hóa ở áp suất rất thấp, điện dung "
                "phủ dải rộng, Pirani/dẫn nhiệt ở dải trung gian, strain gage và ống Bourdon ở áp "
                "suất cao; bảng cũng ghi tham chiếu bên trong là chân không hay khí quyển.",
                "Figure 2.15 (source Figure 15) · Chart of the pressure ranges of electronic "
                "pressure sensor types on a logarithmic Pa axis: ionisation at very low pressure, "
                "capacitance over a wide range, Pirani/thermal types in the intermediate range, "
                "strain gage and Bourdon tubes at high pressure; the internal reference may be "
                "vacuum or atmospheric pressure.",
                "Biểu đồ thanh ngang so sánh dải đo của các loại cảm biến áp suất",
                "Horizontal band chart comparing the ranges of pressure sensor types")


# ---------------------------------------------------------------------------
@_reg
def fig_f16():
    """Figure 16 - strain-gage based pressure cell."""
    w, h = 660, 350
    o = [_defs()]
    # sensor cross-section
    o.append(_rect(56, 86, 240, 196, fill="#e9eef3", sw=1.8))
    o.append(_rect(80, 146, 192, 16, fill="#d9e2ea", sw=1.4))
    o.append(T(176, 142, "màng đàn hồi / elastic diaphragm", 7.8, color=BLUE))
    for gx in (112, 240):
        zz = [(gx + (8 if k % 2 else -8), 172 + k * 5) for k in range(9)]
        o.append(_poly(zz, sw=1.8, color=RED))
    o.append(T(176, 226, "4 strain gauge / 4 cảm biến biến dạng", 7.8, color=RED))
    o.append(_rect(128, 246, 96, 26, fill="#fdf3e6", sw=1.2))
    o.append(T(176, 264, "cầu Wheatstone / bridge", 7.4, color=GREY))
    o.append(_rect(148, 282, 56, 22, fill="#c9d7e2", sw=1.3))
    o.append(_arrow(176, 312, 176, 304, sw=1.4, color=BLUE))
    o.append(T(176, 330, "p →", 8.2, color=BLUE))
    # bridge schematic on the right
    o.append(T(470, 60, "Cầu đo / Wheatstone bridge", 8.6, color=INK))
    o.append(_poly([(390, 110), (550, 110), (550, 250), (390, 250), (390, 110)],
                   sw=1.6, color=GREY))
    for x, y, lab in ((470, 100, "U in"), (470, 264, "U out"), (378, 180, "R1-R4")):
        o.append(T(x, y, lab, 7.8, color=GREY))
    o.append(_line(550, 110, 590, 110, sw=1.2))
    o.append(_line(550, 250, 590, 250, sw=1.2))
    o.append(_line(390, 110, 350, 110, sw=1.2))
    o.append(_line(390, 250, 350, 250, sw=1.2))
    for yy in (146, 214):
        o.append(_rect(458, yy, 24, 14, fill="none", sw=1.2, stroke=RED))
    o.append(_line(470, 110, 470, 146, sw=1.0))
    o.append(_line(470, 160, 470, 214, sw=1.0))
    o.append(_line(470, 228, 470, 250, sw=1.0))
    o.append(T(470, 292, "ΔR ∝ p  →  tín hiệu điện / electrical output", 7.8, color=INK))
    o.append(_callouts([(328, 162, 240, 180), (328, 236, 224, 260)]))
    o.append(_foot(w, 344, "Hình 2.16 · Tế bào áp suất dùng strain gage / strain-gage based pressure cell"))
    s = svg(w, h, "".join(o), esc("Figure 2.16 - Strain-gage based pressure cell"))
    return _fig(s,
                "Hình 2.16 (nguyên bản Hình 16) · Tế bào áp suất dùng strain gage: các cảm biến "
                "biến dạng dán trên màng đàn hồi đổi điện trở khi áp suất làm màng võng, được mắc "
                "trong cầu Wheatstone để cho tín hiệu điện tỉ lệ với áp suất; dải đo từ 3 inch nước "
                "đến 200.000 psig.",
                "Figure 2.16 (source Figure 16) · Strain-gage based pressure cell: gages bonded to "
                "an elastic diaphragm change resistance as pressure deflects it, and are wired "
                "into a Wheatstone bridge to give an electrical output proportional to pressure; "
                "ranges span 3 inches of water to 200,000 psig.",
                "Mặt cắt tế bào áp suất có màng, strain gauge và sơ đồ cầu Wheatstone",
                "Pressure cell cross-section with diaphragm, strain gages and a Wheatstone bridge")


# ---------------------------------------------------------------------------
@_reg
def fig_f17():
    """Figure 17 - capacitance-based pressure cell."""
    w, h = 660, 350
    o = [_defs()]
    o.append(_rect(70, 70, 240, 214, fill="#e9eef3", sw=1.8))
    # fixed plates and moving diaphragm
    o.append(_rect(100, 118, 16, 118, fill="url(#h6)", sw=1.2))
    o.append(_rect(264, 118, 16, 118, fill="url(#h6)", sw=1.2))
    o.append(_rect(120, 168, 140, 16, fill="#d9e2ea", sw=1.4))
    o.append(T(190, 162, "màng kim loại / metal diaphragm", 7.6, color=BLUE))
    o.append(T(108, 114, "C1", 8.2, color=GREEN))
    o.append(T(272, 114, "C2", 8.2, color=GREEN))
    o.append(_line(116, 177, 96, 177, sw=1.0, color=GREY, dash="3 3"))
    o.append(_line(268, 177, 286, 177, sw=1.0, color=GREY, dash="3 3"))
    o.append(T(190, 204, "p quá trình / process pressure →", 7.8, color=BLUE))
    o.append(_rect(154, 226, 72, 24, fill="#c9d7e2", sw=1.3))
    o.append(_arrow(190, 272, 190, 250, sw=1.4, color=BLUE))
    # right: oscillator and bridge
    o.append(T(470, 62, "Dao động tần số cao / HF oscillator", 8.4, color=INK))
    o.append(_rect(400, 92, 150, 40, fill="#fdf3e6", sw=1.4))
    o.append(T(475, 116, "oscillator → điện cực / electrodes", 7.6, color=GREY))
    o.append(_rect(400, 168, 150, 72, fill="#eef3fb", sw=1.4))
    o.append(T(475, 198, "Cầu đo / bridge", 8.4, color=INK))
    o.append(T(475, 222, "C1 ↔ C2 → Δp", 8.0, color=GREEN))
    o.append(_arrow(475, 132, 475, 164, sw=1.2, color=GREY))
    o.append(T(475, 276, "ΔC phát hiện bởi cầu / detected by bridge", 7.8, color=GREY))
    o.append(_callouts([(326, 150, 280, 160), (326, 226, 294, 236)]))
    o.append(T(40, 336, "1. Điện cực cố định / fixed plate   "
                        "2. Màng / diaphragm   3. Cầu đo / bridge", 7.4, anchor="start"))
    o.append(_foot(w, 350, "Hình 2.17 · Tế bào áp suất điện dung / capacitance-based pressure cell"))
    s = svg(w, h, "".join(o), esc("Figure 2.17 - Capacitance-based pressure cell"))
    return _fig(s,
                "Hình 2.17 (nguyên bản Hình 17) · Tế bào áp suất điện dung: màng kim loại hoặc thạch "
                "anh mạ kim loại nằm giữa hai điện cực; áp suất làm màng dịch chuyển làm đổi điện "
                "dung C1/C2, được cầu đo phát hiện ở chế độ cân bằng hoặc không cân bằng. Các số "
                "chỉ: 1. Điện cực cố định; 2. Màng; 3. Cầu đo.",
                "Figure 2.17 (source Figure 17) · Capacitance-based pressure cell: a metal or "
                "metal-coated quartz diaphragm lies between fixed electrodes; pressure moves the "
                "diaphragm, changing C1/C2 as detected by a balanced or unbalanced bridge. "
                "Callouts: 1. Fixed plate; 2. Diaphragm; 3. Bridge.",
                "Màng giữa hai điện cực tụ điện với mạch dao động và cầu đo",
                "Diaphragm between capacitor plates with an oscillator and bridge circuit")


# ---------------------------------------------------------------------------
@_reg
def fig_f18():
    """Figure 18 - mechanical high pressure sensors (A, B, C)."""
    w, h = 680, 370
    o = [_defs()]
    for i in range(3):
        o.append(_rect(20 + i * 220, 46, 206, 282, fill="#fbfaf7", sw=1.2))
    # A: button repeater
    o.append(T(123, 70, "(A) Bộ lặp nút / button repeater", 8.0, color=INK))
    o.append(_rect(58, 108, 130, 20, fill="#d9e2ea", sw=1.3))
    o.append(_rect(58, 188, 130, 20, fill="#d9e2ea", sw=1.3))
    o.append(T(123, 136, "màng cảm biến / sensing diaphragm", 7.4, color=BLUE))
    o.append(T(123, 218, "màng cân bằng / balancing diaphragm", 7.4, color=BLUE))
    o.append(_arrow(123, 96, 123, 106, sw=1.4, color=RED))
    o.append(T(123, 90, "P1", 8.2, color=RED))
    o.append(_arrow(123, 228, 123, 182, sw=1.4, color=GREEN))
    o.append(T(123, 246, "P2 → output air", 7.6, color=GREEN))
    o.append(T(123, 280, "cân bằng lực trực tiếp / direct force balance", 7.4, color=GREY))
    # B: helical Bourdon
    o.append(T(343, 70, "(B) Ống Bourdon ốc vít / helical Bourdon", 8.0, color=INK))
    pts = []
    for k in range(80):
        t = k / 79.0
        a = t * 5 * math.pi
        pts.append((350 + t * 62, 172 + 46 * math.sin(a) * (1 - 0.4 * t)))
    o.append(_poly(pts, sw=4.0, color=BLUE))
    o.append(_rect(324, 258, 54, 24, fill="#c9d7e2", sw=1.3))
    o.append(T(351, 300, "đầu đo quang học / optical tip", 7.4, color=GREY))
    o.append(T(351, 318, "10.000 psig+", 7.8, color=INK))
    # C: deadweight tester
    o.append(T(563, 70, "(C) Bàn cân chết / deadweight tester", 8.0, color=INK))
    o.append(_rect(528, 226, 70, 32, fill="#e9eef3", sw=1.4))
    o.append(_rect(552, 160, 22, 66, fill="#dce5ec", sw=1.4))
    o.append(_rect(536, 138, 54, 22, fill="url(#h6)", sw=1.3))
    o.append(_rect(544, 112, 38, 16, fill="url(#h6)", sw=1.3))
    o.append(T(563, 104, "trọng chuẩn NIST / NIST weight", 7.4, color=GREY))
    o.append(T(563, 284, "piston + chất lỏng / fluid", 7.4, color=GREY))
    o.append(_foot(w, 352, "Hình 2.18 · Cảm biến áp suất cao cơ khí / mechanical high-pressure sensors "
                   "(A, B, C)"))
    s = svg(w, h, "".join(o), esc("Figure 2.18 - Mechanical high pressure sensors"))
    return _fig(s,
                "Hình 2.18 (nguyên bản Hình 18) · Cảm biến áp suất cao cơ khí: (A) bộ lặp nút dùng "
                "cân bằng lực trực tiếp giữa hai màng, tự làm mát bằng khí khí cụ; (B) ống Bourdon "
                "ốc vít tới 20 vòng đo trên 10.000 psig, có thể đọc đầu ống bằng quang học; "
                "(C) bàn cân chết dùng trọng chuẩn NIST đặt lên diện tích piston đã biết làm áp chuẩn.",
                "Figure 2.18 (source Figure 18) · Mechanical high-pressure sensors: (A) the button "
                "repeater balances process pressure against output air pressure across two "
                "diaphragms and is self-cooled by instrument air; (B) a helical Bourdon element "
                "of up to twenty coils measures well beyond 10,000 psig, with optional optical tip "
                "detection; (C) a deadweight tester applies an NIST-certified weight to a known "
                "piston area to generate a reference pressure.",
                "Ba biến thể cảm biến áp suất cao: bộ lặp nút, ống Bourdon ốc vít và bàn cân chết",
                "Three high-pressure sensor variants: button repeater, helical Bourdon and deadweight tester")


# ---------------------------------------------------------------------------
@_reg
def fig_f19():
    """Figure 19 - bulk modulus cell."""
    w, h = 620, 320
    o = [_defs()]
    # hollow cylindrical steel probe
    o.append(_rect(140, 108, 300, 100, fill="#e4e9ee", sw=2.0))
    o.append(_rect(140, 108, 300, 100, fill="none", sw=1.0, stroke=GREY, dash="4 4"))
    o.append(_poly([(440, 108), (462, 120), (462, 196), (440, 208)],
                   fill="#d9e2ea", sw=1.6, close=True))
    o.append(_rect(462, 140, 92, 36, fill="#c9d7e2", sw=1.6))
    o.append(_rect(554, 148, 30, 20, fill="#eef2f6", sw=1.4))
    o.append(_arrow(596, 158, 564, 158, sw=1.4, color=BLUE))
    o.append(T(600, 162, "chuyển động → đọc áp suất / stem motion → reading", 7.6,
              color=BLUE, anchor="start"))
    # isotropic compression arrows
    for yy in (98, 218):
        o.append(_arrow(220, yy, 220, yy + (10 if yy < 150 else -10), sw=1.2, color=RED))
        o.append(_arrow(360, yy, 360, yy + (10 if yy < 150 else -10), sw=1.2, color=RED))
    o.append(T(290, 232, "co khối đẳng hướng / isotropic contraction", 7.8, color=RED))
    o.append(_arrow(120, 158, 136, 158, sw=1.6, color=GREEN))
    o.append(T(116, 152, "p", 9.0, color=GREEN))
    o.append(T(290, 86, "đầu bịt kín / closed inner end", 7.8, color=GREY))
    o.append(T(290, 270, "Đầu dò thép rỗng, thân đẩy ra ngoài / hollow steel probe with projecting stem",
               8.0, color=INK))
    o.append(_foot(w, 302, "Hình 2.19 · Tế bào mô đun khối / bulk modulus cell — tới 200.000 psig"))
    s = svg(w, h, "".join(o), esc("Figure 2.19 - Bulk modulus cell"))
    return _fig(s,
                "Hình 2.19 (nguyên bản Hình 19) · Tế bào mô đun khối: đầu dò thép rỗng bịt kín ở "
                "đầu trong và có thân nhô ra ở đầu ngoài; khi chịu áp suất, đầu dò co khối đẳng "
                "hướng làm đầu và thân dịch chuyển, chuyển thành kết đọc áp suất. Ưu điểm là đáp ứng "
                "nhanh và an toàn, đo tới 200.000 psig với sai số 1-2% toàn thang.",
                "Figure 2.19 (source Figure 19) · Bulk modulus cell: a hollow cylindrical steel "
                "probe closed at the inner end with a projecting stem outside; process pressure "
                "compresses the probe isotropically and the stem motion is converted into a "
                "pressure reading. It is fast and inherently safe, measuring up to 200,000 psig "
                "with 1-2% full-span error.",
                "Đầu dò thép rỗng bị nén với thân đẩy ra ngoài để đọc áp suất",
                "Hollow steel probe compressed isotropically with an outward-moving stem")


# ---------------------------------------------------------------------------
@_reg
def fig_f20():
    """Figure 20 - barometer."""
    w, h = 560, 390
    o = [_defs()]
    # mercury trough
    o.append(_rect(110, 316, 340, 44, fill="#d9dee4", sw=1.8))
    o.append(_rect(122, 328, 316, 28, fill="#9fb0bc", sw=0.8))
    # inverted closed tube
    o.append(_rect(250, 44, 60, 286, fill="#fbfaf7", sw=1.8))
    o.append(_line(250, 44, 310, 44, sw=2.4))
    # mercury column inside the tube
    o.append(_rect(256, 104, 48, 226, fill="#9fb0bc", sw=0.6))
    o.append(_rect(256, 104, 48, 4, fill="#7e909e", sw=0.6))
    o.append(T(280, 92, "chân không Torricelli / Torricelli vacuum", 7.6, color=GREY))
    o.append(T(280, 70, "vacuum", 7.4, color=GREY))
    # height dimension
    o.append(_line(330, 104, 366, 104, sw=0.9, color=GREY, dash="3 3"))
    o.append(_line(330, 328, 366, 328, sw=0.9, color=GREY, dash="3 3"))
    o.append(_arrow(348, 112, 348, 320, sw=1.2, color=RED))
    o.append(T(372, 220, "760 mm = 29,9 in", 8.6, color=RED, anchor="start"))
    o.append(T(372, 238, "= 1 atm = 14,7 psi", 8.0, color=GREY, anchor="start"))
    # scale
    for i in range(8):
        yy = 108 + i * 30
        o.append(_line(250, yy, 262, yy, sw=0.7))
        o.append(T(240, yy + 3, str(760 - i * 100), 6.6, color=GREY, anchor="end"))
    o.append(T(280, 374, "Thủy ngân trong máng / mercury trough  ·  P = γh", 7.8, color=GREY))
    o.append(_foot(w, 386, "Hình 2.20 · Barometer"))
    s = svg(w, h, "".join(o), esc("Figure 2.20 - Barometer"))
    return _fig(s,
                "Hình 2.20 (nguyên bản Hình 20) · Barometer thủy ngân: ống bịt kín một đầu úp vào "
                "máng thủy ngân; áp suất khí quyển nâng cột thủy ngân cao 760 mm (29,9 inch) ở mực "
                "nước biển, tương đương 1 atm hay 14,7 psi, nên chiều cao cột là thước đo trực tiếp "
                "áp suất khí quyển (P = γh).",
                "Figure 2.20 (source Figure 20) · Mercury barometer: a closed tube inverted in a "
                "mercury trough; atmospheric pressure raises the mercury column to 760 mm "
                "(29.9 in) at sea level, equal to 1 atm or 14.7 psi, so the column height directly "
                "measures atmospheric pressure (P = γh).",
                "Ống thủy ngân úp trong máng với cột cao 760 mm và vạch chia",
                "Mercury tube inverted in a trough with a 760 mm column and scale")


# ---------------------------------------------------------------------------
@_reg
def fig_f21():
    """Figure 21 - vacuum gauge measurement ranges (chart)."""
    w, h = 680, 390
    o = [_defs()]
    o.append(T(340, 24, "Dải đo đồng hồ chân không / Vacuum Gauge Measurement Ranges", 9.2,
              color=INK))
    x0, x1 = 186, 626
    lo, hi = -10.0, 3.0

    def px(e):
        return x0 + (e - lo) / (hi - lo) * (x1 - x0)

    o.append(_arrow(x0, 324, x1 + 14, 324, sw=1.2))
    o.append(T(x1, 354, "p (torr, log)", 8.2, color=GREY))
    for e in range(-10, 4, 2):
        lab = "10⁻¹⁰" if e == -10 else ("10⁰" if e == 0 else "10%d" % e)
        o.append(_line(px(e), 324, px(e), 329, sw=0.8))
        o.append(T(px(e), 343, lab, 7.0, color=GREY))
    rows = [
        ("Cơ khí / mechanical", "Bourdon, bellows", -1, 3, "#6a5a9a"),
        ("Nhiệt / thermal", "Thermocouple, Pirani", -3, 0, "#b07d2b"),
        ("Điện dung / capacitance", "Capacitance manometer", -6, 1, GREEN),
        ("Ion hóa / ionization", "Hot / cold cathode", -10, -3, RED),
        ("McLeod", "tham chiếu / reference", -9, -4, BLUE),
    ]
    for i, (grp, typ, a, b, col) in enumerate(rows):
        yy = 58 + i * 52
        o.append(T(x0 - 8, yy + 10, grp, 7.8, color=INK, anchor="end"))
        o.append(T(x0 - 8, yy + 23, typ, 7.0, color=GREY, anchor="end"))
        o.append(_line(x0, yy + 28, x1, yy + 28, sw=0.6, color="#e3e7eb"))
        o.append(_rect(px(a), yy + 8, px(b) - px(a), 18, fill=col, sw=0.8))
        o.append(T(px(a) + 5, yy + 21, "10%d – 10%d" % (a, b), 7.2, color="#ffffff",
                   anchor="start"))
    o.append(T(40, 376, "Chân không cao ~10⁻⁶ torr: catốt lạnh hoặc Bayard-Alpert; "
                        "dải millitorr: thermocouple/Pirani hoặc capacitance", 7.4,
              color=GREY, anchor="start"))
    s = svg(w, h, "".join(o), esc("Figure 2.21 - Vacuum gauge measurement ranges chart"))
    return _fig(s,
                "Hình 2.21 (nguyên bản Hình 21) · Dải đo của các loại đồng hồ chân không theo trục "
                "logarithm (torr): cơ khí (ống Bourdon, bellows) ở áp suất cao, nhiệt (thermocouple, "
                "Pirani) ở dải trung gian, capacitance manometer phủ dải rộng và chính xác, ion hóa "
                "(catốt nóng/lạnh) ở chân không cao, McLeod làm chuẩn hiệu chỉnh. Có ba nhóm chính: "
                "cơ khí, nhiệt và ion hóa.",
                "Figure 2.21 (source Figure 21) · Ranges of vacuum gauges on a logarithmic torr "
                "axis: mechanical (Bourdon, bellows) at higher pressure, thermal (thermocouple, "
                "Pirani) in the intermediate range, capacitance manometers broad and accurate, "
                "ionisation (hot/cold cathode) for high vacuum, and McLeod as a calibration "
                "standard. The three main categories are mechanical, thermal and ionisation.",
                "Biểu đồ thanh ngang các dải đo chân không theo thang logarithm torr",
                "Horizontal band chart of vacuum gauge ranges on a logarithmic torr scale")


# __END__


