# -*- coding: utf-8 -*-
"""Vector redraws of the figures in the CRC Measurement Handbook, Ch. 15
(Tilt Measurement). There are five figures, all schematic line diagrams:
subsidence from tilt (15.1), hydrostatic equilibrium in connected vessels (15.2),
hydrostatic leveling (15.3), suspended/inverted plumb lines (15.4), and the
air-current / spiral-wire error diagrams (15.5). Each function returns
(svg, caption_vi, caption_en, aria_vi, aria_en).
"""
import math

from hbfig import GOLD, INK, MUTED, TXT, _f, svg, _fig

E = "#2a2a2a"
G = "#b45309"
S = "#888888"
P = "#ffffff"


def _lbl(x, y, txt, cls="t", anchor="start"):
    return '<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>' % (
        cls, _f(x), _f(y), anchor, txt)


def _defs():
    return ('<defs>'
            '<marker id="ah15" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
            '<path d="M0,0 L7,3 L0,6 Z" fill="%s"/></marker>'
            '<marker id="ah15g" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
            '<path d="M0,0 L7,3 L0,6 Z" fill="%s"/></marker></defs>' % (E, G))


# ---------------------------------------------------------------- 15.1
def fig_15_1():
    o = [_defs()]
    # original (reference) horizontal profile
    o.append('<line x1="90" y1="60" x2="600" y2="60" stroke="%s" stroke-width="1.2" stroke-dasharray="5 4"/>' % S)
    o.append(_lbl(95, 52, "mặt tham chiếu (ban đầu)", "ts"))
    # subsided profile through points 1..4
    pts = [(120, 92), (250, 122), (380, 152), (510, 204)]
    d = "M" + " L".join("%s %s" % p for p in pts)
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.2"/>' % (d, G))
    for i, (x, y) in enumerate(pts, 1):
        o.append('<circle cx="%s" cy="%s" r="4" fill="%s" stroke="%s" stroke-width="1.4"/>' % (x, y, P, E))
        o.append(_lbl(x, y - 10, "P%d" % i, "tb", "middle"))
    # distance spans
    for (a, b, lab) in ((pts[0], pts[1], "s₁"), (pts[1], pts[2], "s₂"), (pts[2], pts[3], "s₃")):
        x0, x1 = a[0], b[0]
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1"/>'
                 % (_f(x0), _f(pts[3][1] + 28), _f(x1), _f(pts[3][1] + 28), S))
        o.append(_lbl((x0 + x1) / 2.0, pts[3][1] + 42, lab, "tb", "middle"))
    # tilt arcs on each segment
    for (a, b, lab) in ((pts[0], pts[1], "α₁"), (pts[1], pts[2], "α₂"), (pts[2], pts[3], "α₃")):
        mx, my = (a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0
        o.append(_lbl(mx + 6, my - 8, lab, "tb"))
    # delta h4 at P4
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2" marker-start="url(#ah15)" marker-end="url(#ah15)"/>'
             % (pts[3][0] + 28, 60, pts[3][0] + 28, pts[3][1], E))
    o.append(_lbl(pts[3][0] + 34, (60 + pts[3][1]) / 2.0, "δh₄", "tb"))
    o.append(_lbl(360, 250, "sập (subsidence) tích luỹ từ các độ nghiêng αᵢ", "ts", "middle"))
    return _fig(
        svg(680, 280, "".join(o), "Sự sập (sụt lún) mặt đất từ đo độ nghiêng"),
        "Hình 15.1 · Sụt lún mặt đất suy ra từ đo độ nghiêng. Độ sụt lún của điểm 4 so với điểm 1 ước tính từ "
        "các thay đổi độ nghiêng quan sát αᵢ (rad) và khoảng cách sᵢ đã biết: δh₄ = α₁s₁ + α₂s₂ + α₃s₃. Độ "
        "chính xác phụ thuộc mật độ đo và giả thiết dốc đều giữa các điểm.",
        "Figure 15.1 · Ground subsidence derived from tilt measurements. The subsidence of point 4 relative "
        "to point 1 is estimated from the observed tilts αᵢ (rad) and the distances sᵢ: δh₄ = α₁s₁ + α₂s₂ + "
        "α₃s₃. Fidelity depends on measurement density and the assumption of a uniform slope between points.",
        "Một đường tham chiếu nằm ngang và một mặt cắt sụt lún đi qua 4 điểm P1–P4 với các góc nghiêng α₁–α₃ "
        "và khoảng cách s₁–s₃; mũi tên δh₄ chỉ độ sụt lún tích luỹ tại P4.",
        "A horizontal reference line and a subsided profile through points P1–P4 with tilts α₁–α₃ and distances "
        "s₁–s₃; δh₄ marks the accumulated subsidence at P4.")


# ---------------------------------------------------------------- 15.2
def fig_15_2():
    o = [_defs()]
    # U-shaped connected vessels
    o.append('<path d="M140 80 L140 212 L240 212 L240 80" fill="none" stroke="%s" stroke-width="2"/>' % E)
    o.append('<path d="M440 80 L440 212 L540 212 L540 80" fill="none" stroke="%s" stroke-width="2"/>' % E)
    o.append('<rect x="140" y="212" width="400" height="12" fill="none" stroke="%s" stroke-width="2"/>' % E)
    # liquid fill (same level h1 = h2)
    o.append('<rect x="142" y="150" width="96" height="62" fill="#cfe3f0" stroke="none"/>')
    o.append('<rect x="442" y="150" width="96" height="62" fill="#cfe3f0" stroke="none"/>')
    o.append('<line x1="142" y1="150" x2="538" y2="150" stroke="%s" stroke-width="1" stroke-dasharray="4 3"/>' % S)
    o.append(_lbl(340, 144, "mực bằng nhau (h₁ = h₂)", "ts", "middle"))
    # labels
    o.append(_lbl(120, 185, "h₁", "tb"))
    o.append(_lbl(560, 185, "h₂", "tb"))
    o.append(_lbl(190, 235, "P₁, ρ₁", "ts", "middle"))
    o.append(_lbl(490, 235, "P₂, ρ₂", "ts", "middle"))
    o.append(_lbl(340, 75, "hai bình thông nhau (connected vessels)", "ts", "middle"))
    return _fig(
        svg(680, 260, "".join(o), "Cân bằng thuỷ tĩnh trong các bình thông nhau"),
        "Hình 15.2 · Cân bằng thuỷ tĩnh trong các bình thông nhau. Nếu hai bình chứa nối với nhau được đổ "
        "một phần chất lỏng, độ cao h₁ và h₂ liên hệ qua phương trình thuỷ tĩnh: P₁ + ρ₁gh₁ = P₂ + ρ₂gh₂ = hằng "
        "số (phương trình Bernoulli).",
        "Figure 15.2 · Hydrostatic equilibrium in connected vessels. If two connected containers are "
        "partially filled, the heights h₁ and h₂ are related through the hydrostatic equation: P₁ + ρ₁gh₁ = "
        "P₂ + ρ₂gh₂ = constant (Bernoulli's equation).",
        "Hai bình chứa nối đáy, chất lỏng trong hai bình dâng đến cùng một mực h₁ = h₂; áp suất và khối lượng "
        "riêng tại hai bên liên hệ bởi P₁ + ρ₁gh₁ = P₂ + ρ₂gh₂.",
        "Two bottom-connected vessels with liquid rising to the same level h₁ = h₂; pressure and density at "
        "each side obey P₁ + ρ₁gh₁ = P₂ + ρ₂gh₂.")


# ---------------------------------------------------------------- 15.3
def fig_15_3():
    o = [_defs()]
    # two containers with liquid + air tube (top) and liquid tube (bottom)
    o.append('<rect x="120" y="90" width="80" height="150" fill="none" stroke="%s" stroke-width="2"/>' % E)
    o.append('<rect x="480" y="90" width="80" height="150" fill="none" stroke="%s" stroke-width="2"/>' % E)
    o.append('<rect x="122" y="170" width="76" height="68" fill="#cfe3f0" stroke="none"/>')
    o.append('<rect x="482" y="150" width="76" height="88" fill="#cfe3f0" stroke="none"/>')
    # air tube (top) and liquid tube (bottom)
    o.append('<line x1="160" y1="100" x2="520" y2="100" stroke="%s" stroke-width="1.2" stroke-dasharray="4 3"/>' % S)
    o.append(_lbl(340, 92, "ống khí (air tube)", "ts", "middle"))
    o.append('<line x1="160" y1="215" x2="520" y2="215" stroke="%s" stroke-width="2"/>' % E)
    o.append(_lbl(340, 232, "ống chất lỏng (liquid tube)", "ts", "middle"))
    # level heights r1, r2
    o.append('<line x1="120" y1="170" x2="106" y2="170" stroke="%s" stroke-width="1"/>' % E)
    o.append('<line x1="480" y1="150" x2="466" y2="150" stroke="%s" stroke-width="1"/>' % E)
    o.append(_lbl(100, 174, "r₁", "tb", "end"))
    o.append(_lbl(460, 154, "r₂", "tb", "end"))
    # Dh12 between the two surfaces
    o.append('<line x1="300" y1="170" x2="300" y2="150" stroke="%s" stroke-width="1.2" marker-start="url(#ah15)" marker-end="url(#ah15)"/>' % G)
    o.append(_lbl(308, 162, "Dh₁₂ = r₂ − r₁", "tb"))
    return _fig(
        svg(680, 270, "".join(o), "Cân bằng thuỷ tĩnh dùng để đo độ nghiêng (hydrostatic leveling)"),
        "Hình 15.3 · Cân bằng thuỷ tĩnh (hydrostatic leveling). Ống khí nối hai bình loại bỏ sai số do áp "
        "suất khí khác nhau tại hai trạm. Độ chênh mực chất lỏng đo được là Dh₁₂ = r₂ − r₁; nhiệt độ chất "
        "lỏng cần giữ không đổi để tránh sai số.",
        "Figure 15.3 · Hydrostatic leveling. The air tube connecting the two containers removes error from "
        "different air pressures at the stations. The measured level difference is Dh₁₂ = r₂ − r₁; the liquid "
        "temperature must be kept constant to avoid error.",
        "Hai bình nối bằng ống chất lỏng ở đáy và ống khí ở nắp; mực chất lỏng r₁, r₂ trong hai bình, độ chênh "
        "Dh₁₂ = r₂ − r₁ được đo bằng cảm biến.",
        "Two containers linked by a bottom liquid tube and a top air tube; liquid levels r₁ and r₂ give the "
        "difference Dh₁₂ = r₂ − r₁ measured by sensors.")


# ---------------------------------------------------------------- 15.4
def fig_15_4():
    o = [_defs()]
    # panel (a) suspended pendulum
    o.append(_lbl(170, 40, "(a) con lắc treo (suspended)", "tb", "middle"))
    o.append('<path d="M150 60 L190 60 L170 78 Z" fill="%s"/>' % E)  # anchor
    o.append('<line x1="170" y1="78" x2="170" y2="225" stroke="%s" stroke-width="1.6"/>' % E)
    o.append('<circle cx="170" cy="232" r="10" fill="%s" stroke="%s" stroke-width="1.4"/>' % (P, E))
    # reading table
    o.append('<rect x="196" y="150" width="46" height="10" fill="#f3f7f2" stroke="%s" stroke-width="1.2"/>' % E)
    o.append('<line x1="242" y1="155" x2="284" y2="155" stroke="%s" stroke-width="1.2" marker-end="url(#ah15)"/>' % G)
    o.append(_lbl(288, 159, "Δ", "tb"))
    o.append(_lbl(150, 250, "H (tách dọc)", "ts"))
    # panel (b) inverted pendulum
    o.append(_lbl(500, 40, "(b) con lắc ngược (inverted)", "tb", "middle"))
    o.append('<path d="M480 235 L520 235 L500 217 Z" fill="%s"/>' % E)  # anchor at bottom (deep)
    o.append('<line x1="500" y1="217" x2="500" y2="78" stroke="%s" stroke-width="1.6"/>' % E)
    o.append('<circle cx="500" cy="72" r="10" fill="%s" stroke="%s" stroke-width="1.4"/>' % (P, E))
    o.append('<rect x="526" y="68" width="46" height="10" fill="#f3f7f2" stroke="%s" stroke-width="1.2"/>' % E)
    o.append('<line x1="526" y1="73" x2="488" y2="73" stroke="%s" stroke-width="1.2" marker-end="url(#ah15)"/>' % G)
    o.append(_lbl(444, 56, "Δ", "tb", "end"))
    o.append(_lbl(470, 252, "mỏ neo sâu (nền đá ổn định)", "ts"))
    o.append('<line x1="90" y1="262" x2="600" y2="262" stroke="%s" stroke-width="0.8" stroke-dasharray="3 3"/>' % S)
    return _fig(
        svg(680, 280, "".join(o), "Đo độ nghiêng bằng dây dọi (plumb lines)"),
        "Hình 15.4 · Đo độ nghiêng bằng dây dọi. (a) Con lắc treo: dây treo từ mỏ neo trên, quả dọi ở dưới, "
        "bàn đọc ở giữa đo vị trí ngang. (b) Con lắc ngược: mỏ neo sâu trong nền đá ổn định, dây đi lên, bàn "
        "đọc trên cùng đo chuyển vị tuyệt đối of bề mặt so với nền.",
        "Figure 15.4 · Inclination measurements with plumblines. (a) Suspended pendulum: wire hung from an "
        "upper anchor, bob below, reading table partway measures horizontal position. (b) Inverted pendulum: "
        "anchor deep in stable foundation rock, wire rises, top reading table measures absolute displacement "
        "of the surface relative to the foundation.",
        "Hai bảng: (a) dây dọi treo từ mỏ neo trên, quả dọi dưới, bàn đọc đo Δ; (b) dây dọi ngược, mỏ neo "
        "dưới nền, bàn đọc trên cùng đo chuyển vị Δ.",
        "Two panels: (a) a suspended plumb line with an upper anchor and a lower reading table; (b) an "
        "inverted plumb line anchored deep in the foundation with a top reading table, both measuring Δ.")


# ---------------------------------------------------------------- 15.5
def fig_15_5():
    o = [_defs()]
    # panel (a) air current
    o.append(_lbl(170, 38, "(a) ảnh hưởng của luồng khí", "tb", "middle"))
    o.append('<path d="M150 60 L190 60 L170 76 Z" fill="%s"/>' % E)
    o.append('<path d="M170 76 C 178 120, 200 160, 205 232" fill="none" stroke="%s" stroke-width="1.6"/>' % E)
    o.append('<circle cx="205" cy="236" r="9" fill="%s" stroke="%s" stroke-width="1.4"/>' % (P, E))
    # wind arrows along exposed length h
    for yy in (130, 150, 170):
        o.append('<line x1="120" y1="%d" x2="150" y2="%d" stroke="%s" stroke-width="1.4" marker-end="url(#ah15)"/>' % (yy, yy, G))
    o.append(_lbl(96, 152, "luồng khí v", "ts", "end"))
    # ideal vertical (dashed) and deflection e
    o.append('<line x1="170" y1="76" x2="170" y2="232" stroke="%s" stroke-width="1" stroke-dasharray="4 3"/>' % S)
    o.append('<line x1="170" y1="232" x2="205" y2="236" stroke="%s" stroke-width="1.2" marker-start="url(#ah15)"/>' % E)
    o.append(_lbl(178, 226, "e", "tb"))
    o.append(_lbl(150, 252, "h (phơi)  H (từ mỏ neo)", "ts"))
    # panel (b) spiral shape
    o.append(_lbl(500, 38, "(b) lỗi do dạng xoắn dây", "tb", "middle"))
    # a spiral (helix) drawn as ellipse loops
    cx, cy = 500, 160
    for k in range(4):
        ry = 8 + k * 9
        o.append('<ellipse cx="%d" cy="%d" rx="22" ry="%d" fill="none" stroke="%s" stroke-width="1.4"/>' % (cx, cy, ry, E))
    # envelope circle of radius r with diameter 2r
    o.append('<circle cx="%d" cy="%d" r="40" fill="none" stroke="%s" stroke-width="1" stroke-dasharray="4 3"/>' % (cx, cy, G))
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2" marker-start="url(#ah15)" marker-end="url(#ah15)"/>' % (_f(cx - 40), _f(cy), _f(cx + 40), _f(cy), E))
    o.append(_lbl(cx, cy + 54, "2r (lỗi cực đại)", "tb", "middle"))
    o.append(_lbl(cx - 60, cy - 50, "r", "tb"))
    return _fig(
        svg(680, 280, "".join(o), "Sai số dây dọi: luồng khí và dạng xoắn của dây"),
        "Hình 15.5 · (a) Luồng khí tốc độ v dọc theo chiều dài h, cách mỏ neo một khoảng H, làm dây lệch một "
        "lượng e = f₀hH/Q (công thức 15.3). (b) Dạng xoắn (ủ mềm) của dây có bán kính xoắn r (15.5); nếu dây "
        "xoay giữa hai đợt đo, sai số ghi nhận có thể tới 2r.",
        "Figure 15.5 · (a) An air current of speed v along length h, at distance H from the anchor, deflects "
        "the wire by e = f₀hH/Q (Eq. 15.3). (b) The spiral (annealed) shape of the wire has spiral radius r "
        "(Eq. 15.5); if the wire rotates between campaigns, the recorded displacement error can reach 2r.",
        "Hai bảng: (a) dây dọi treo bị gió thổi lệch một đoạn e so với đường thẳng đứng; (b) dây có dạng xoắn "
        "bán kính r, lỗi cực đại 2r khi dây xoay.",
        "Two panels: (a) a suspended plumb wire blown sideways by an air current to a deflection e; (b) a "
        "helically coiled wire with spiral radius r, giving a worst-case error of 2r when it rotates.")


# expose
FIGS = [fig_15_1, fig_15_2, fig_15_3, fig_15_4, fig_15_5]


def fig(n):
    return FIGS[n - 1]()
