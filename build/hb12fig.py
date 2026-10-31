# -*- coding: utf-8 -*-
"""Vector redraws of the figures in the CRC Measurement Handbook, Ch. 12
(Area Measurement). Every function returns
(svg, caption_vi, caption_en, aria_vi, aria_en).
The figures are mechanical schematics; they are drawn as clean labelled
line diagrams that match the original captions rather than photographs.
"""
import math

from hbfig import GOLD, INK, MUTED, TXT, _f, svg, _fig

# palette reuse
E = "#2a2a2a"     # ink
G = "#b45309"     # gold
S = "#888888"     # muted
P = "#ffffff"     # paper


def _lbl(x, y, txt, cls="t", anchor="start"):
    return '<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>' % (
        cls, _f(x), _f(y), anchor, txt)


def _arr(x1, y1, x2, y2, col=E, dash=False):
    d = ' marker-end="url(#ah12)"' if col == E else ' marker-end="url(#ah12g)"'
    da = ' stroke-dasharray="5 4"' if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.4"%s%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, da, d))


def _defs():
    return ('<defs>'
            '<marker id="ah12" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
            '<path d="M0,0 L7,3 L0,6 Z" fill="%s"/></marker>'
            '<marker id="ah12g" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
            '<path d="M0,0 L7,3 L0,6 Z" fill="%s"/></marker>'
            '<marker id="ah12s" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
            '<path d="M0,0 L7,3 L0,6 Z" fill="%s"/></marker></defs>' % (E, G, S))


# ---------------------------------------------------------------- 12.1
def fig_12_1():
    # (a) polar: constrained end follows a circular arc about a fixed pivot
    # (b) linear: constrained end slides along a straight rail
    o = []
    o.append(_defs())
    # panel a
    o.append('<text class="tb" x="20" y="22">(a) Planimeter kiểu cực (polar)</text>')
    # fixed pivot
    o.append('<circle cx="150" cy="150" r="5" fill="%s"/>' % E)
    o.append(_lbl(150, 172, "đầu tựa cố định", "ts", "middle"))
    # pole arm to constrained joint
    jx, jy = 150, 92
    o.append('<line x1="150" y1="150" x2="%d" y2="%d" stroke="%s" stroke-width="2"/>' % (jx, jy, E))
    # arc (constrained-end path) radius = |pivot-joint|
    r = 58.0
    o.append('<path d="M%d %d A %d %d 0 1 1 %d %d" fill="none" stroke="%s" stroke-width="1.3" stroke-dasharray="5 4"/>'
            % (jx, jy - r, r, r, jx, jy + r, G))
    o.append(_lbl(jx + 60, jy, "đường đầu bị ràng buộc (cung tròn)", "ts"))
    # tracer arm from joint to pointer at boundary of a shape
    # shape to measure: a closed blob at right
    pts = [(250, 70), (320, 60), (350, 110), (330, 160), (270, 170), (235, 130)]
    d = "M" + " L".join("%s %s" % (x, y) for x, y in pts) + " Z"
    o.append('<path d="%s" fill="#f7f7f7" stroke="%s" stroke-width="1.4"/>' % (d, E))
    # pointer at vertex (250,70)
    o.append('<line x1="%d" y1="%d" x2="250" y2="70" stroke="%s" stroke-width="2"/>' % (jx, jy, E))
    o.append('<circle cx="250" cy="70" r="3.4" fill="%s"/>' % G)
    o.append(_lbl(258, 66, "con trỏ", "ts"))
    o.append(_lbl(150, 200, "cánh tay theo dõi", "ts", "middle"))
    # panel b
    o.append('<text class="tb" x="380" y="22">(b) Planimeter kiểu tuyến tính (linear)</text>')
    # rail
    o.append('<line x1="380" y1="150" x2="650" y2="150" stroke="%s" stroke-width="2.2"/>' % E)
    o.append(_lbl(515, 168, "đường ray (đường thẳng)", "ts", "middle"))
    # slider on rail
    o.append('<rect x="470" y="142" width="16" height="16" rx="2" fill="#fff" stroke="%s" stroke-width="1.4"/>' % E)
    o.append(_lbl(478, 200, "đầu bị ràng buộc (trượt thẳng)", "ts", "middle"))
    # shape
    pts = [(540, 70), (610, 62), (640, 112), (618, 160), (556, 170), (522, 128)]
    d = "M" + " L".join("%s %s" % (x, y) for x, y in pts) + " Z"
    o.append('<path d="%s" fill="#f7f7f7" stroke="%s" stroke-width="1.4"/>' % (d, E))
    # tracer arm from slider to pointer
    o.append('<line x1="478" y1="150" x2="540" y2="70" stroke="%s" stroke-width="2"/>' % E)
    o.append('<circle cx="540" cy="70" r="3.4" fill="%s"/>' % G)
    o.append(_lbl(548, 66, "con trỏ", "ts"))
    return _fig(
        svg(680, 220, "".join(o), "Hai loại planimeter: kiểu cực và kiểu tuyến tính"),
        "Hình 12.1 · Đầu bị ràng buộc của planimeter kiểu cực (a) đi theo một cung tròn; đầu bị ràng "
        "buộc của planimeter kiểu tuyến tính (b) đi theo một đường thẳng.",
        "Figure 12.1 · The constrained end of a polar planimeter (a) follows a circular path; the "
        "constrained end of a linear planimeter (b) follows a straight line path.",
        "Bên trái: cần tựa quay quanh một điểm cố định, đầu bị ràng buộc vẽ cung tròn. Bên phải: đầu bị "
        "ràng buộc trượt trên một đường ray thẳng.",
        "Left: a pole arm pivots about a fixed point and the constrained end traces a circular arc. "
        "Right: the constrained end slides along a straight rail.")


# ---------------------------------------------------------------- 12.2
def fig_12_2():
    o = []
    o.append(_defs())
    # measuring wheel: circle
    cx, cy, R = 230, 150, 46
    o.append('<circle cx="%d" cy="%d" r="%d" fill="#fff" stroke="%s" stroke-width="2"/>' % (cx, cy, R, E))
    # hub
    o.append('<circle cx="%d" cy="%d" r="4" fill="%s"/>' % (cx, cy, E))
    # wheel axis (through hub), at angle phi to direction of travel
    phi = math.radians(35)
    dx, dy = math.cos(phi), math.sin(phi)
    L = 64
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="2"/>'
            % (_f(cx - dx * L), _f(cy - dy * L), _f(cx + dx * L), _f(cy + dy * L), G))
    o.append(_lbl(cx + dx * L + 6, cy + dy * L, "trục bánh xe (axis)", "ts"))
    # direction of travel (horizontal)
    o.append(_arr(60, cy, 360, cy, E))
    o.append(_lbl(210, cy - 12, "s — hướng di chuyển (direction of travel)", "ts"))
    # radius showing rolling contact point at bottom
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1"/>'
            % (_f(cx), _f(cy), _f(cx), _f(cy + R), S))
    # angle phi between axis and travel (at hub)
    # draw small arc
    o.append('<path d="M%s %s A 26 26 0 0 1 %s %s" fill="none" stroke="%s" stroke-width="1"/>'
            % (_f(cx + 26), _f(cy), _f(cx + dx * 26), _f(cy + dy * 26), S))
    # annotate phi near hub
    o.append(_lbl(cx + 30, cy + 22, "φ", "tb"))
    o.append(_lbl(cx + 30, cy + 34, "góc giữa trục bánh xe và hướng đi", "ts"))
    # note on right
    o.append('<text class="t" x="430" y="120">Số vòng quay tích luỹ tỉ lệ với</text>')
    o.append('<text class="t" x="430" y="142">tích phân của sin φ dọc theo đường đi:</text>')
    o.append('<text class="tb" x="430" y="170">P = (K / πD) &#8747; sin φ ds</text>')
    o.append('<text class="ts" x="430" y="192">K: số xung/rev · D: đường kính bánh xe</text>')
    return _fig(
        svg(680, 240, "".join(o), "Bánh xe đo và góc φ giữa trục bánh và hướng di chuyển"),
        "Hình 12.2 · Sự quay của bánh xe đo tỉ lệ với tích phân của tích số giữa quãng đường di chuyển "
        "và sin của góc tạo bởi trục bánh xe và hướng di chuyển.",
        "Figure 12.2 · The rotation of a measuring wheel is proportional to the product of distance moved "
        "and the sine of the angle between the wheel axis and direction of travel.",
        "Bánh xe tròn với trục nghiêng một góc φ so với hướng di chuyển ngang; số vòng quay tỉ lệ với "
        "tích phân sin φ dọc đường đi.",
        "A wheel whose axis makes an angle phi with the horizontal direction of travel; rotation is "
        "proportional to the integral of sine phi along the path.")


# ---------------------------------------------------------------- 12.3
def fig_12_3():
    o = []
    o.append(_defs())
    # parallelogram: base = L (tracer arm length), height = wheel reading as distance
    x0, y0 = 90, 180
    L = 240.0
    h = 90.0
    skew = 70.0
    corners = [(x0, y0), (x0 + L, y0), (x0 + L + skew, y0 - h), (x0 + skew, y0 - h)]
    d = "M" + " L".join("%s %s" % c for c in corners) + " Z"
    o.append('<path d="%s" fill="#faf6ef" stroke="%s" stroke-width="2"/>' % (d, E))
    # base edge (L)
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="2.4"/>'
            % (_f(x0), _f(y0), _f(x0 + L), _f(y0), G))
    o.append(_lbl(x0 + L / 2.0, y0 + 20, "L — chiều dài cánh tay theo dõi", "tb", "middle"))
    # height (altitude) as dashed
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.4" stroke-dasharray="5 4"/>'
            % (_f(x0 + skew), _f(y0 - h), _f(x0 + skew), _f(y0), S))
    o.append('<text class="ts" x="%s" y="%s" text-anchor="middle" transform="rotate(-90 %s %s)">h — số đọc bánh xe (đổi ra khoảng cách)</text>'
            % (_f(x0 + skew - 8), _f(y0 - h / 2.0), _f(x0 + skew - 8), _f(y0 - h / 2.0)))
    # tracer arm overlay
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.6"/>'
            % (_f(x0 + skew), _f(y0 - h), _f(x0), _f(y0), E))
    o.append('<circle cx="%s" cy="%s" r="3.4" fill="%s"/>' % (_f(x0 + skew), _f(y0 - h), G))
    o.append(_lbl(x0 + skew - 4, y0 - h - 8, "con trỏ", "ts", "end"))
    # formula on right
    o.append('<text class="tb" x="430" y="120">Diện tích hình bình hành:</text>')
    o.append('<text class="tb" x="430" y="150">A = L &#215; h</text>')
    o.append('<text class="ts" x="430" y="176">với h = (P/K)&#215;πD là khoảng cách</text>')
    o.append('<text class="ts" x="430" y="194">bánh xe đã lăn (số vòng &#215; chu vi).</text>')
    return _fig(
        svg(680, 240, "".join(o), "Diện tích hình bình hành tỉ lệ với tích số chiều dài cần và số vòng bánh xe"),
        "Hình 12.3 · Diện tích của hình bình hành này tỉ lệ với tích số giữa chiều dài cánh tay theo dõi "
        "và số vòng quay của bánh xe đo.",
        "Figure 12.3 · The area of this parallelogram is proportional to the product of tracer arm length "
        "and measuring wheel revolutions.",
        "Hình bình hành: cạnh đáy L là chiều dài cần, chiều cao h là số đọc bánh xe đổi ra khoảng cách; "
        "diện tích = L &#215; h.",
        "A parallelogram whose base L is the tracer-arm length and whose height h is the wheel reading "
        "converted to distance; area equals L times h.")


# ---------------------------------------------------------------- 12.4
def fig_12_4():
    o = []
    o.append(_defs())
    # a four-sided figure (vertices 1-2-3-4)
    V = [(200, 70), (330, 55), (360, 150), (180, 170)]
    d = "M" + " L".join("%s %s" % v for v in V) + " Z"
    o.append('<path d="%s" fill="#f7f7f7" stroke="%s" stroke-width="1.6"/>' % (d, E))
    for i, (x, y) in enumerate(V, 1):
        o.append('<circle cx="%s" cy="%s" r="3" fill="%s"/>' % (_f(x), _f(y), E))
        o.append(_lbl(x + 6, y - 6, str(i), "tb"))
    o.append(_lbl(265, 120, "hình bốn cạnh", "ts", "middle"))
    # a planimeter (bar + pointer) pointing at vertex 1
    o.append('<line x1="120" y1="200" x2="200" y2="70" stroke="%s" stroke-width="2"/>' % E)
    o.append('<circle cx="200" cy="70" r="3.4" fill="%s"/>' % G)
    o.append('<text class="tb" x="60" y="40">(a) con trỏ chỉ vào các đỉnh</text>')
    o.append(_lbl(118, 220, "cánh tay theo dõi", "ts"))
    # (b)-(e): bar at the ends of each segment
    bx, by = 470, 60
    o.append('<text class="tb" x="%d" y="%d">(b)–(e) đầu cần tại hai đầu mỗi cạnh</text>' % (bx, by - 18))
    sub = [(bx, by + 20), (bx + 90, by + 8), (bx + 120, by + 96), (bx - 40, by + 110)]
    for i, (sx, sy) in enumerate(sub, 1):
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.6"/>'
                % (_f(sx), _f(sy - 30), _f(sx), _f(sy), E))
        o.append('<circle cx="%s" cy="%s" r="3" fill="%s"/>' % (_f(sx), _f(sy - 30), G))
        o.append(_lbl(sx + 6, sy - 30, "(%s)" % ("bced"[i - 1]), "ts"))
    # the constrained end follows a circle: small arc near top
    o.append('<path d="M%s %s A 30 30 0 1 1 %s %s" fill="none" stroke="%s" stroke-width="1.2" stroke-dasharray="5 4"/>'
            % (bx + 50, by - 6, bx + 50, by + 54, G))
    o.append(_lbl(bx + 86, by + 24, "đầu bị ràng buộc đi theo cung tròn", "ts"))
    return _fig(
        svg(680, 250, "".join(o), "Planimeter chỉ vào các đỉnh và hai đầu mỗi cạnh của hình bốn cạnh"),
        "Hình 12.4 · Sơ đồ này cho thấy một planimeter chỉ vào từng giao điểm của một hình bốn cạnh đang "
        "được theo dấu ở (a), và ở hai đầu của từng đoạn trong (b) đến (e). Đầu bị ràng buộc của cánh tay "
        "theo dõi đi theo một đường tròn.",
        "Figure 12.4 · This schematic shows a planimeter pointing to each junction of a four-sided figure "
        "being traced in (a) and at the ends of each of the segments in (b) through (e). The constrained "
        "end of the tracer arm follows a circle.",
        "Trái: planimeter chỉ vào 4 đỉnh của hình tứ giác; phải: cần đặt tại hai đầu mỗi cạnh, đầu bị "
        "ràng buộc vẽ cung tròn.",
        "Left: a planimeter points at the four vertices of a quadrilateral; right: the bar is placed at "
        "the two ends of each side while the constrained end traces a circle.")


# ---------------------------------------------------------------- 12.5
def fig_12_5():
    o = []
    o.append(_defs())
    # irregular region
    pts = [(120, 60), (300, 48), (360, 110), (340, 180), (210, 210), (110, 170), (80, 110)]
    d = "M" + " L".join("%s %s" % p for p in pts) + " Z"
    o.append('<clipPath id="clip12_5"><path d="%s"/></clipPath>' % d)
    o.append('<path d="%s" fill="#f3f7f2" stroke="%s" stroke-width="1.8"/>' % (d, E))
    # grid overlay
    o.append('<g clip-path="url(#clip12_5)">')
    for gx in range(60, 380, 28):
        o.append('<line x1="%d" y1="40" x2="%d" y2="230" stroke="%s" stroke-width="0.8"/>' % (gx, gx, S))
    for gy in range(40, 240, 28):
        o.append('<line x1="60" y1="%d" x2="380" y2="%d" stroke="%s" stroke-width="0.8"/>' % (gy, gy, S))
    o.append('</g>')
    # highlight a few squares as counted
    for (hx, hy) in [(140, 96), (196, 96), (252, 124), (168, 152), (224, 152), (280, 152)]:
        o.append('<rect x="%d" y="%d" width="28" height="28" fill="%s" opacity="0.5"/>' % (hx, hy, G))
    o.append(_lbl(230, 250, "đếm các ô nằm ít nhất một nửa trong vùng", "ts", "middle"))
    # legend
    o.append('<rect x="430" y="70" width="28" height="28" fill="%s" opacity="0.5"/>' % G)
    o.append(_lbl(466, 90, "ô được tính", "t"))
    o.append(_lbl(430, 140, "Diện tích = số ô đếm", "tb"))
    o.append(_lbl(430, 162, "&#215; diện tích một ô", "tb"))
    return _fig(
        svg(680, 280, "".join(o), "Lưới ô vuông đặt trên vùng cần đo diện tích"),
        "Hình 12.5 · Lưới ô vuông là một phương pháp đơn giản và sẵn có để đo diện tích.",
        "Figure 12.5 · Grid overlays offer a simple and readily available method for measuring areas.",
        "Một tấm trong suốt có lưới ô vuông đặt trên hình; đếm các ô nằm ít nhất một nửa trong vùng, "
        "nhân với diện tích một ô.",
        "A transparent sheet with a square grid is laid over the shape; squares at least half inside are "
        "counted and multiplied by the area of one square.")


# ---------------------------------------------------------------- 12.6
def fig_12_6():
    o = []
    o.append(_defs())
    # manual polar planimeter: weight (anchor), pole arm, tracer arm, wheel, pointer
    # weight
    o.append('<circle cx="120" cy="170" r="16" fill="#fff" stroke="%s" stroke-width="2"/>' % E)
    o.append(_lbl(120, 200, "trọng lượng (neo)", "ts", "middle"))
    # pole arm
    px, py = 150, 120
    o.append('<line x1="120" y1="170" x2="%d" y2="%d" stroke="%s" stroke-width="2.4"/>' % (px, py, E))
    o.append(_lbl(108, 150, "cánh tay cực", "ts"))
    # joint to tracer arm
    o.append('<circle cx="%d" cy="%d" r="3" fill="%s"/>' % (px, py, E))
    # tracer arm to pointer
    tx, ty = 300, 70
    o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2.4"/>' % (px, py, tx, ty, E))
    o.append(_lbl(215, 88, "cánh tay theo dõi", "ts"))
    # pointer (lens)
    o.append('<circle cx="%d" cy="%d" r="6" fill="none" stroke="%s" stroke-width="1.6"/>' % (tx, ty, G))
    o.append('<circle cx="%d" cy="%d" r="1.8" fill="%s"/>' % (tx, ty, G))
    o.append(_lbl(tx + 10, ty, "con trỏ (thấu kính)", "ts"))
    # measuring wheel on tracer arm (box)
    mx, my = 230, 96
    o.append('<rect x="%d" y="%d" width="22" height="22" rx="3" fill="#fff" stroke="%s" stroke-width="1.6"/>' % (mx - 11, my - 11, E))
    o.append(_lbl(mx, my + 30, "bánh xe đo", "ts", "middle"))
    # arc of constrained end
    o.append('<path d="M%d %d A 56 56 0 1 1 %d %d" fill="none" stroke="%s" stroke-width="1.2" stroke-dasharray="5 4"/>'
            % (px, py - 56, px, py + 56, G))
    # note
    o.append(_lbl(360, 110, "Planimeter cơ khí kiểu cực:", "tb"))
    o.append(_lbl(360, 132, "dùng khi chỉ đo thỉnh thoảng.", "ts"))
    o.append(_lbl(360, 154, "Độ dài cánh tay cực không", "ts"))
    o.append(_lbl(360, 172, "ảnh hưởng đến kết quả.", "ts"))
    return _fig(
        svg(680, 250, "".join(o), "Planimeter cơ khí kiểu cực với trọng lượng, hai cần và bánh xe đo"),
        "Hình 12.6 · Planimeter cơ khí kiểu cực thường được ưu tiên khi chỉ cần dùng thỉnh thoảng.",
        "Figure 12.6 · Mechanical planimeters are normally preferred when occasional use is required.",
        "Trọng lượng neo cánh tay cực; cánh tay theo dõi mang con trỏ và hộp bánh xe đo; đầu bị ràng "
        "buộc đi theo cung tròn.",
        "A weight anchors the pole arm; the tracer arm carries the pointer and the measuring-wheel box; "
        "the constrained end moves on a circular arc.")


# ---------------------------------------------------------------- 12.7
def fig_12_7():
    o = []
    o.append(_defs())
    # upper: electronic polar planimeter with digital readout
    o.append('<text class="tb" x="20" y="22">trên: planimeter kiểu cực có đầu đọc số</text>')
    o.append('<circle cx="110" cy="120" r="14" fill="#fff" stroke="%s" stroke-width="2"/>' % E)
    o.append('<line x1="110" y1="120" x2="170" y2="80" stroke="%s" stroke-width="2.4"/>' % E)
    o.append('<circle cx="170" cy="80" r="3" fill="%s"/>' % E)
    o.append('<line x1="170" y1="80" x2="300" y2="60" stroke="%s" stroke-width="2.4"/>' % E)
    o.append('<circle cx="300" cy="60" r="6" fill="none" stroke="%s" stroke-width="1.6"/>' % G)
    o.append('<rect x="240" y="74" width="22" height="22" rx="3" fill="#fff" stroke="%s" stroke-width="1.6"/>' % E)
    # digital readout box
    o.append('<rect x="150" y="150" width="120" height="40" rx="4" fill="#222" stroke="%s" stroke-width="1.6"/>' % E)
    o.append('<text x="210" y="175" text-anchor="middle" style="font:15px monospace;fill:#7CFC7C">12.84 cm²</text>')
    o.append(_lbl(150, 210, "đầu đọc số (digital readout)", "ts"))
    # lower: electronic linear planimeter
    o.append('<text class="tb" x="380" y="22">dưới: planimeter kiểu tuyến tính có đầu đọc số</text>')
    o.append('<line x1="360" y1="120" x2="650" y2="120" stroke="%s" stroke-width="2.4"/>' % E)
    o.append('<rect x="470" y="112" width="16" height="16" rx="2" fill="#fff" stroke="%s" stroke-width="1.4"/>' % E)
    o.append('<line x1="478" y1="120" x2="600" y2="70" stroke="%s" stroke-width="2.4"/>' % E)
    o.append('<circle cx="600" cy="70" r="6" fill="none" stroke="%s" stroke-width="1.6"/>' % G)
    o.append('<rect x="500" y="150" width="120" height="40" rx="4" fill="#222" stroke="%s" stroke-width="1.6"/>' % E)
    o.append('<text x="560" y="175" text-anchor="middle" style="font:15px monospace;fill:#7CFC7C">27.3 cm²</text>')
    o.append(_lbl(500, 210, "đầu đọc số (digital readout)", "ts"))
    return _fig(
        svg(680, 240, "".join(o), "Hai planimeter điện tử có đầu đọc số: kiểu cực (trên) và kiểu tuyến tính (dưới)"),
        "Hình 12.7 · Planimeter điện tử dễ sử dụng và đọc hơn, nên được ưu tiên nhất là khi dùng thường "
        "xuyên.",
        "Figure 12.7 · Electronic planimeters are easier to use and read, and are preferred especially "
        "when frequently used.",
        "Trên: planimeter kiểu cực gắn mã hoá quang và đầu đọc số. Dưới: planimeter kiểu tuyến tính có "
        "đầu đọc số, đầu bị ràng buộc trượt trên đường ray thẳng.",
        "Top: a polar planimeter with an optical encoder and digital readout. Bottom: a linear electronic "
        "planimeter with a readout; the constrained end slides on a straight rail.")


# ---------------------------------------------------------------- 12.8
def fig_12_8():
    o = []
    o.append(_defs())
    # top: battery-operated polar
    o.append('<text class="tb" x="20" y="22">trên: planimeter kiểu cực dùng pin</text>')
    o.append('<circle cx="110" cy="90" r="12" fill="#fff" stroke="%s" stroke-width="2"/>' % E)
    o.append('<line x1="110" y1="90" x2="160" y2="60" stroke="%s" stroke-width="2.4"/>' % E)
    # processor box on pole arm
    o.append('<rect x="95" y="66" width="40" height="26" rx="3" fill="#e8eef2" stroke="%s" stroke-width="1.4"/>' % E)
    o.append('<text x="115" y="83" text-anchor="middle" style="font:9px Inter;fill:#222">CPU pin</text>')
    o.append('<line x1="160" y1="60" x2="290" y2="55" stroke="%s" stroke-width="2.4"/>' % E)
    o.append('<circle cx="290" cy="55" r="6" fill="none" stroke="%s" stroke-width="1.6"/>' % G)
    o.append('<rect x="225" y="66" width="20" height="20" rx="3" fill="#fff" stroke="%s" stroke-width="1.4"/>' % E)
    # bottom: battery-operated linear
    o.append('<text class="tb" x="380" y="22">dưới: planimeter kiểu tuyến tính dùng pin</text>')
    o.append('<line x1="370" y1="150" x2="640" y2="150" stroke="%s" stroke-width="2.4"/>' % E)
    o.append('<rect x="470" y="138" width="16" height="16" rx="2" fill="#fff" stroke="%s" stroke-width="1.4"/>' % E)
    o.append('<rect x="500" y="132" width="40" height="26" rx="3" fill="#e8eef2" stroke="%s" stroke-width="1.4"/>' % E)
    o.append('<text x="520" y="149" text-anchor="middle" style="font:9px Inter;fill:#222">CPU pin</text>')
    o.append('<line x1="520" y1="150" x2="620" y2="60" stroke="%s" stroke-width="2.4"/>' % E)
    o.append('<circle cx="620" cy="60" r="6" fill="none" stroke="%s" stroke-width="1.6"/>' % G)
    o.append(_lbl(370, 200, "Nhỏ gọn, chạy pin, có hiệu chỉnh điện tử và lấy trung bình nhiều lần đo.", "ts"))
    return _fig(
        svg(680, 230, "".join(o), "Planimeter dùng pin kiểu cực (trên) và kiểu tuyến tính (dưới)"),
        "Hình 12.8 · Planimeter dùng pin kết hợp được ưu điểm của planimeter điện tử và tính cơ động.",
        "Figure 12.8 · Battery-operated planimeters have the advantages of electronics planimeters and "
        "are portable.",
        "Cả hai mẫu đều nhỏ gọn, dùng pin, bộ xử lý gắn trên cánh tay cực; không đo được chiều dài.",
        "Both are compact, battery-powered, with the processor mounted on the pole arm; they cannot "
        "measure length.")


# ---------------------------------------------------------------- 12.9
def fig_12_9():
    o = []
    o.append(_defs())
    # base
    o.append('<rect x="60" y="170" width="40" height="24" rx="3" fill="#fff" stroke="%s" stroke-width="2"/>' % E)
    o.append(_lbl(80, 212, "đế (base)", "ts", "middle"))
    # base arm from base up
    b0 = (80, 170)
    b1 = (80, 90)
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="2.6"/>' % (b0[0], b0[1], b1[0], b1[1], E))
    # encoder at base joint
    o.append('<circle cx="%s" cy="%s" r="7" fill="#fff" stroke="%s" stroke-width="1.6"/>' % (b1[0], b1[1], G))
    o.append(_lbl(b1[0] - 14, b1[1] + 4, "bộ mã hoá 1", "ts", "end"))
    # tracer arm from b1 to pointer
    p1 = (300, 70)
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="2.6"/>' % (b1[0], b1[1], p1[0], p1[1], E))
    o.append(_lbl(190, 120, "cánh tay theo dõi (tracer arm)", "ts", "middle"))
    # encoder at elbow
    o.append('<circle cx="%s" cy="%s" r="7" fill="#fff" stroke="%s" stroke-width="1.6"/>' % (p1[0], p1[1], G))
    o.append(_lbl(p1[0] + 12, p1[1] - 6, "bộ mã hoá 2", "ts"))
    # pointer
    o.append('<circle cx="%s" cy="%s" r="6" fill="none" stroke="%s" stroke-width="1.6"/>' % (p1[0], p1[1] - 30, G))
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.6"/>' % (p1[0], p1[1], p1[0], p1[1] - 30, E))
    o.append(_lbl(p1[0] + 12, p1[1] - 30, "con trỏ (pointer)", "ts"))
    # readout
    o.append('<rect x="360" y="60" width="150" height="60" rx="4" fill="#222" stroke="%s" stroke-width="1.6"/>' % E)
    o.append('<text x="435" y="86" text-anchor="middle" style="font:13px monospace;fill:#7CFC7C">x = 12.40</text>')
    o.append('<text x="435" y="108" text-anchor="middle" style="font:13px monospace;fill:#7CFC7C">y = 8.15</text>')
    o.append(_lbl(360, 140, "toạ độ (x, y) hiển thị &amp; truyền lên máy tính", "ts"))
    o.append(_lbl(60, 235, "Cánh tay theo dõi = cánh tay cực + cánh tay tựa; hai bộ mã hoá đo góc.", "ts"))
    return _fig(
        svg(680, 260, "".join(o), "Bộ số hoá dạng cánh tay (arm digitizer) đo toạ độ x, y"),
        "Hình 12.9 · Bộ số hoá dạng cánh tay cho phép đo diện tích, chiều dài và toạ độ, đồng thời truyền "
        "dữ liệu hiển thị lên máy tính; nó chiếm rất ít diện tích bàn làm việc.",
        "Figure 12.9 · An arm digitizer lets one measure area, length, and coordinates, and transmit the "
        "displayed data to a computer; it requires minimum desk space.",
        "Đế, hai cánh tay, hai bộ mã hoá góc và con trỏ; toạ độ (x,y) được hiển thị và truyền đi.",
        "A base, two arms, two rotary encoders and a pointer; the (x, y) coordinates are displayed and "
        "sent to a computer.")


# ---------------------------------------------------------------- 12.10
def fig_12_10():
    o = []
    o.append(_defs())
    # tablet: rectangle work surface with embedded wire grid
    o.append('<rect x="120" y="50" width="320" height="200" rx="6" fill="#fafafa" stroke="%s" stroke-width="2"/>' % E)
    o.append(_lbl(280, 40, "mặt làm việc (work surface)", "ts", "middle"))
    # grid of wires
    for gx in range(150, 430, 26):
        o.append('<line x1="%d" y1="60" x2="%d" y2="240" stroke="%s" stroke-width="0.7"/>' % (gx, gx, S))
    for gy in range(66, 246, 26):
        o.append('<line x1="128" y1="%d" x2="432" y2="%d" stroke="%s" stroke-width="0.7"/>' % (gy, gy, S))
    # puck / pointer
    px, py = 290, 150
    o.append('<circle cx="%d" cy="%d" r="12" fill="#fff" stroke="%s" stroke-width="2"/>' % (px, py, E))
    o.append('<circle cx="%d" cy="%d" r="3" fill="%s"/>' % (px, py, G))
    o.append(_lbl(px + 18, py + 4, "con trỏ dạng puck/pen", "ts"))
    # crosshair cursor
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1"/>' % (_f(px - 18), _f(py), _f(px + 18), _f(py), S))
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1"/>' % (_f(px), _f(py - 18), _f(px), _f(py + 18), S))
    # cable to computer
    o.append('<line x1="432" y1="150" x2="540" y2="150" stroke="%s" stroke-width="1.6"/>' % E)
    o.append('<rect x="540" y="125" width="80" height="50" rx="4" fill="#e8eef2" stroke="%s" stroke-width="1.4"/>' % E)
    o.append('<text x="580" y="155" text-anchor="middle" style="font:10px Inter;fill:#222">máy tính</text>')
    o.append(_lbl(300, 285, "Lưới dây ngầm xác định vị trí con trỏ theo hai trục.", "ts", "middle"))
    return _fig(
        svg(680, 310, "".join(o), "Bàn số hoá (tablet digitizer) với con trỏ và lưới dây"),
        "Hình 12.10 · Bàn số hoá dạng tấm phổ biến gồm một con trỏ nhẹ kiểu puck hoặc bút để chọn các "
        "điểm, toạ độ của chúng được truyền cho máy tính xử lý.",
        "Figure 12.10 · The popular pad digitizer includes a lightweight puck or pen-type pointer for "
        "selecting points whose coordinates are transmitted to a computer for processing.",
        "Mặt bàn hình chữ nhật có lưới dây ngầm, con trỏ puck xác định toạ độ, dữ liệu truyền cho máy "
        "tính.",
        "A rectangular tablet with an embedded wire grid; a puck pointer locates coordinates that are "
        "sent to a computer.")


# expose every figure as fig_12_N
FIGS = [fig_12_1, fig_12_2, fig_12_3, fig_12_4, fig_12_5,
        fig_12_6, fig_12_7, fig_12_8, fig_12_9, fig_12_10]


def fig(n):
    return FIGS[n - 1]()
