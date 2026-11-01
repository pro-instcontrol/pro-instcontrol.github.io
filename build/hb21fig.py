# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 21 — Density Measurement (Halit Eren,
Curtin University of Technology).

The source chapter contains exactly sixteen figures (21.1–21.16).
FIGS is a 16-figure set — nothing is padded.
"""
import math as _m

from hbfig import GOLD, INK, MUTED, TXT, _f, svg, _fig

E = "#2a2a2a"
G = "#b45309"
S = "#888888"
P = "#ffffff"
FILL = "#eef2f7"
WARM = "#fdf6e3"


def _lbl(x, y, txt, cls="t", anchor="start"):
    return '<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>' % (
        cls, _f(x), _f(y), anchor, txt)


def _defs():
    return ('<defs>'
            '<marker id="ah21" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah21g" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '</defs>' % (E, G))


def _arr(x1, y1, x2, y2, col=E, marker="ah21", sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, marker))


def _box(x, y, w, h, t, col=E, fill="#ffffff", fs=11, rx=5):
    o = ['<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" '
         'stroke-width="1.3"/>' % (_f(x), _f(y), _f(w), _f(h), _f(rx), fill, col)]
    lines = t.split("\n")
    for i, ln in enumerate(lines):
        yy = y + h / 2.0 + (i - (len(lines) - 1) / 2.0) * (fs + 3) + fs * 0.35
        o.append(_lbl(x + w / 2.0, yy, ln, "tb", "middle"))
    return "".join(o)


def _bellows(x, y, w, h=24, vertical=False):
    """Flexible coupling drawn as a zig-zag."""
    n = 5
    pts = []
    for i in range(n * 2 + 1):
        t = i / float(2 * n)
        if vertical:
            px, py = x + (h / 2.0 if i % 2 else -h / 2.0), y + w * t
        else:
            px, py = x + w * t, y + (h / 2.0 if i % 2 else -h / 2.0)
        pts.append((px, py))
    return ('<path d="M' + " L".join("%s %s" % (_f(a), _f(b)) for a, b in pts)
            + '" fill="none" stroke="%s" stroke-width="1.3"/>' % E)


def _tank(x, y, w, h, fill=FILL):
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" '
            'stroke-width="1.4"/>' % (_f(x), _f(y), _f(w), _f(h), fill, E))


def _dot(x, y, r=3, col=E):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (_f(x), _f(y), _f(r), col)


# ---------------------------------------------------------------- 21.1
def fig_21_1():
    o = [_defs()]
    # liquid inside the flask
    o.append('<rect x="268" y="152" width="104" height="54" fill="%s"/>' % FILL)
    # flask body
    o.append('<path d="M302 66 L302 130 L268 152 L268 206 L372 206 L372 152 L338 130 '
             'L338 66 Z" fill="none" stroke="%s" stroke-width="1.8"/>' % E)
    # stopper with capillary bore
    o.append('<polygon points="298,42 342,42 338,68 302,68" fill="#f2f2f2" stroke="%s" '
             'stroke-width="1.4"/>' % E)
    o.append('<line x1="320" y1="42" x2="320" y2="122" stroke="%s" stroke-width="1.1"/>' % E)
    # graduation mark on the capillary
    o.append('<line x1="313" y1="104" x2="327" y2="104" stroke="%s" stroke-width="1.8"/>' % G)

    # annotation box
    o.append('<rect x="430" y="104" width="204" height="86" rx="6" fill="#fbfbfb" '
             'stroke="#dddddd" stroke-width="1"/>')
    o.append(_lbl(532, 126, "Cân chính xác để xác định m", "ts", "middle"))
    o.append(_lbl(532, 154, "ρ = m / V", "tb", "middle"))
    o.append(_lbl(532, 180, "SG = m_mẫu / m_nước", "ts", "middle"))

    o.append(_lbl(352, 50, "Nút đậy", "t"))
    o.append(_lbl(352, 88, "Mao quản", "t"))
    o.append(_lbl(352, 116, "Vạch thể tích", "t"))
    o.append(_lbl(258, 172, "Chất lỏng mẫu", "ts", "end"))
    o.append(_lbl(258, 194, "Bình thể tích cố định", "ts", "end"))
    return _fig(
        svg(680, 236, "".join(o), "Sơ đồ bình tỉ trọng (pycnometer) có mao quản"),
        "Hình 21.1 · Bình tỉ trọng (pycnometer). Một bình có thể tích cố định được đổ đầy chất lỏng "
        "rồi cân chính xác; mao quản trên nút đậy dùng để xác định đúng thể tích chất lỏng, nhờ đó "
        "đạt độ phân giải cao khi đổ đầy. Khối lượng riêng bằng khối lượng chia thể tích; tỉ trọng "
        "bằng tỉ số khối lượng chất lỏng trên khối lượng nước.",
        "Figure 21.1 · A pycnometer. A fixed-volume container is filled with liquid and weighed "
        "accurately; the capillary in the stopper determines the exact volume of the liquid, giving "
        "high resolution when filling. Density is mass divided by volume; specific gravity is the ratio "
        "of the liquid mass to the water mass.",
        "Bình tỉ trọng: nút đậy có mao quản, vạch chia thể tích, bình chứa thể tích cố định, chất lỏng mẫu",
        "Pycnometer: stoppered flask with capillary bore, graduation mark, fixed volume, sample liquid")


# ---------------------------------------------------------------- 21.2
def fig_21_2():
    o = [_defs()]
    o.append('<rect x="170" y="150" width="330" height="66" fill="%s"/>' % FILL)
    o.append('<line x1="170" y1="150" x2="500" y2="150" stroke="%s" stroke-width="1.2" '
             'stroke-dasharray="6 4"/>' % S)
    # bulb
    o.append('<path d="M326 130 Q298 152 302 182 Q306 212 340 212 Q374 212 378 182 '
             'Q382 152 354 130 Z" fill="#ffffff" stroke="%s" stroke-width="1.6"/>' % E)
    # stem
    o.append('<rect x="326" y="44" width="28" height="88" fill="#ffffff" stroke="%s" '
             'stroke-width="1.6"/>' % E)
    # scale graduations
    for i, y in enumerate(range(54, 126, 9)):
        ln = 18 if i % 2 == 0 else 12
        o.append('<line x1="326" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1"/>'
                 % (y, 326 + ln, y, E))
    # lead ballast
    for cx, cy in ((330, 198), (340, 202), (350, 198), (335, 190), (345, 190)):
        o.append(_dot(cx, cy, 3.2, S))

    o.append(_lbl(250, 60, "Thang chia", "t", "end"))
    o.append(_lbl(250, 100, "Thân ống", "t", "end"))
    o.append(_lbl(250, 178, "Bầu thuỷ tinh kín", "ts", "end"))
    o.append(_lbl(250, 202, "Chì dằn", "ts", "end"))
    o.append(_lbl(512, 146, "Mặt thoáng chất lỏng", "ts"))
    o.append(_lbl(400, 82, "Đọc ρ trực tiếp trên thang", "ts"))
    o.append(_lbl(400, 118, "(kg m⁻³, SG, °API, °Brix…)", "ts"))
    return _fig(
        svg(680, 228, "".join(o), "Sơ đồ tỉ trọng kế (hydrometer) thả trong chất lỏng"),
        "Hình 21.2 · Tỉ trọng kế (hydrometer). Một bầu có khối lượng và thể tích cố định được thả "
        "vào chất lỏng; bầu chìm sâu hay nông tuỳ theo khối lượng riêng của chất lỏng, và khối lượng "
        "riêng được đọc trực tiếp trên thang chia ở thân ống. Cần hiệu chính theo nhiệt độ.",
        "Figure 21.2 · Hydrometer. A fixed weight and volume bulb is placed in the liquid; it sinks to "
        "a depth that depends on the density, and the density is read directly from the scale on the "
        "stem. Temperature correction is necessary.",
        "Tỉ trọng kế: thân ống có thang chia, bầu thuỷ tinh kín có chì dằn, mặt thoáng chất lỏng",
        "Hydrometer: graduated stem, sealed glass bulb ballasted with lead shot, liquid surface")


# ---------------------------------------------------------------- 21.3
def fig_21_3():
    o = [_defs()]
    o.append('<path d="M190 72 L190 170 Q190 182 202 182 L398 182 Q410 182 410 170 L410 72" '
             'fill="none" stroke="%s" stroke-width="6" stroke-linecap="round"/>' % E)
    o.append('<rect x="90" y="66" width="60" height="12" fill="%s" stroke="%s" stroke-width="1.1"/>'
             % (FILL, E))
    o.append(_bellows(150, 72, 40, 24))
    o.append(_bellows(410, 72, 40, 24))
    o.append('<rect x="450" y="66" width="60" height="12" fill="%s" stroke="%s" stroke-width="1.1"/>'
             % (FILL, E))
    o.append(_arr(96, 72, 140, 72, G, "ah21g", 1.3))
    o.append(_arr(456, 72, 500, 72, G, "ah21g", 1.3))
    # force balance below
    o.append('<line x1="300" y1="182" x2="300" y2="214" stroke="%s" stroke-width="1.4"/>' % E)
    o.append(_box(240, 214, 120, 40, "Cân lực"))

    o.append(_lbl(118, 56, "Dòng vào", "ts", "middle"))
    o.append(_lbl(478, 56, "Dòng ra", "ts", "middle"))
    o.append(_lbl(160, 108, "Khớp nối mềm", "ts", "end"))
    o.append(_lbl(160, 122, "(bellows)", "ts", "end"))
    o.append(_lbl(440, 108, "Khớp nối mềm", "ts"))
    o.append(_lbl(440, 122, "(điểm tựa)", "ts"))
    o.append(_lbl(300, 168, "Ống chữ U", "t", "middle"))
    o.append(_lbl(300, 272, "Đo chính xác trọng lượng toàn phần của ống chứa chất lỏng", "ts",
                  "middle"))
    return _fig(
        svg(680, 284, "".join(o), "Sơ đồ đo khối lượng riêng bằng cân thuỷ tĩnh với ống chữ U"),
        "Hình 21.3 · Cân thuỷ tĩnh (hydrostatic weighing). Trọng lượng toàn phần của một ống chữ U "
        "có thể tích cố định chứa chất lỏng được xác định chính xác; ống được đỡ trên các khớp nối "
        "mềm ở hai đầu và lực được đo bằng một cân lực. Khối lượng riêng được tính từ tỉ số khối "
        "lượng : thể tích.",
        "Figure 21.3 · Hydrostatic weighing. The total weight of a fixed-volume tube containing liquid "
        "is determined accurately; the U-tube is pivoted on flexible end couplings and the force is "
        "measured by a force balance. Density follows from the mass : volume ratio.",
        "Cân thuỷ tĩnh: ống chữ U treo trên hai khớp nối mềm, dòng vào và ra, cân lực ở dưới",
        "Hydrostatic weighing: U-tube on two flexible couplings, inlet and outlet, force balance below")


# ---------------------------------------------------------------- 21.4
def fig_21_4():
    o = [_defs()]
    o.append(_box(250, 26, 180, 40, "Cân lò xo / bộ truyền lực"))
    # spring
    pts = []
    for i in range(9):
        t = i / 8.0
        pts.append((340 + (9 if i % 2 else -9), 68 + 28 * t))
    o.append('<path d="M' + " L".join("%s %s" % (_f(a), _f(b)) for a, b in pts)
             + '" fill="none" stroke="%s" stroke-width="1.5"/>' % E)
    o.append('<line x1="340" y1="96" x2="340" y2="110" stroke="%s" stroke-width="1.4"/>' % E)

    o.append(_tank(250, 110, 180, 100, "#ffffff"))
    o.append('<rect x="252" y="132" width="176" height="76" fill="%s"/>' % FILL)

    # inlet with flexible coupling
    o.append('<rect x="160" y="116" width="60" height="12" fill="%s" stroke="%s" stroke-width="1.1"/>'
             % (FILL, E))
    o.append(_bellows(220, 122, 30, 20))
    # outlet
    o.append(_bellows(410, 198, 30, 20))
    o.append('<rect x="440" y="192" width="60" height="12" fill="%s" stroke="%s" stroke-width="1.1"/>'
             % (FILL, E))
    o.append(_arr(166, 122, 210, 122, G, "ah21g", 1.3))
    o.append(_arr(446, 198, 490, 198, G, "ah21g", 1.3))

    o.append(_lbl(196, 106, "Vào", "ts", "middle"))
    o.append(_lbl(470, 182, "Ra", "ts", "middle"))
    o.append(_lbl(200, 152, "Khớp nối mềm", "ts", "end"))
    o.append(_lbl(340, 168, "Chất lỏng chảy liên tục", "ts", "middle"))
    o.append(_lbl(340, 232, "Bình thể tích cố định", "t", "middle"))
    return _fig(
        svg(680, 244, "".join(o), "Sơ đồ bình dòng cân bằng (balanced flow vessel)"),
        "Hình 21.4 · Bình dòng cân bằng (balanced-flow vessel). Chất lỏng chảy liên tục qua một bình "
        "có thể tích cố định và bình được cân tự động bằng một cân lò xo nhạy hoặc một bộ truyền "
        "cân lực khí nén. Vì đã biết thể tích và trọng lượng chất lỏng, khối lượng riêng hoặc tỉ "
        "trọng được tính và chia thang theo đơn vị tương ứng.",
        "Figure 21.4 · Balanced flow vessel. Liquid flows continuously through a fixed-volume vessel "
        "that is weighed automatically by a sensitive spring balance or a pneumatic force-balance "
        "transmitter. Since the volume and weight of the liquid are known, density or specific gravity "
        "is easily calculated and scaled in the respective units.",
        "Bình dòng cân bằng: bình thể tích cố định treo trên cân lò xo, có khớp nối mềm ở đường vào và ra",
        "Balanced flow vessel: fixed-volume vessel hung from a spring balance, flexible couplings at "
        "inlet and outlet")


# ---------------------------------------------------------------- 21.5
def fig_21_5():
    o = [_defs()]
    o.append(_tank(200, 96, 220, 140, "#ffffff"))
    o.append('<rect x="202" y="120" width="216" height="114" fill="%s"/>' % FILL)
    o.append('<line x1="202" y1="120" x2="418" y2="120" stroke="%s" stroke-width="1.2" '
             'stroke-dasharray="6 4"/>' % S)

    # support + chain
    o.append('<rect x="290" y="52" width="40" height="8" fill="#f2f2f2" stroke="%s" '
             'stroke-width="1.1"/>' % E)
    pts = []
    for i in range(15):
        t = i / 14.0
        pts.append((310 + (6 if i % 2 else -6), 60 + 80 * t))
    o.append('<path d="M' + " L".join("%s %s" % (_f(a), _f(b)) for a, b in pts)
             + '" fill="none" stroke="%s" stroke-width="1.3"/>' % E)

    # plummet with transformer core
    o.append('<rect x="286" y="140" width="48" height="68" fill="#ffffff" stroke="%s" '
             'stroke-width="1.6"/>' % E)
    o.append('<rect x="300" y="150" width="20" height="48" fill="#dddddd" stroke="%s" '
             'stroke-width="1"/>' % E)
    # pickup coils
    o.append('<rect x="256" y="150" width="22" height="44" fill="%s" stroke="%s" stroke-width="1.2"/>'
             % (WARM, G))
    o.append('<rect x="342" y="150" width="22" height="44" fill="%s" stroke="%s" stroke-width="1.2"/>'
             % (WARM, G))

    o.append(_lbl(330, 80, "Xích", "t"))
    o.append(_lbl(240, 158, "Phao thể tích cố định", "ts", "end"))
    o.append(_lbl(240, 176, "tự định tâm", "ts", "end"))
    o.append(_lbl(310, 202, "Lõi biến áp", "ts", "middle"))
    o.append(_lbl(470, 150, "Cuộn thu tín hiệu", "ts"))
    o.append(_lbl(364, 168, "", "ts"))
    o.append('<line x1="364" y1="170" x2="466" y2="146" stroke="%s" stroke-width="1" '
             'stroke-dasharray="4 3"/>' % S)
    o.append(_lbl(424, 114, "Mặt thoáng", "ts"))
    o.append(_lbl(310, 254, "Cầu nhiệt điện trở bù ảnh hưởng của nhiệt độ lên khối lượng riêng", "ts",
                  "middle"))
    return _fig(
        svg(680, 266, "".join(o), "Sơ đồ phao cân bằng xích (chain balance float)"),
        "Hình 21.5 · Phao cân bằng xích (chain balance float). Phao có thể tích và khối lượng cố "
        "định, chìm hoàn toàn trong chất lỏng, tự tìm vị trí cân bằng tuỳ theo khối lượng riêng. Lực "
        "do xích tác dụng lên phao là hàm của vị trí phao, nên lực đo được tỉ lệ với khối lượng riêng "
        "của chất lỏng; lõi biến áp trong phao truyền vị trí sang cuộn thu, và một cầu nhiệt điện trở "
        "bù ảnh hưởng của nhiệt độ.",
        "Figure 21.5 · Chain balance float. The fixed-volume, fixed-weight plummet is totally suspended "
        "in the liquid and assumes an equilibrium position that depends on the density. The force the "
        "chain exerts on the plummet is a function of plummet position, so the measured force is "
        "proportional to the density; a transformer core inside the plummet transmits its position to a "
        "pickup coil, and a resistance thermometer bridge compensates for temperature.",
        "Phao cân bằng xích: bình chứa chất lỏng, phao chìm hoàn toàn treo bằng xích, lõi biến áp và "
        "hai cuộn thu hai bên",
        "Chain balance float: liquid vessel, fully submerged plummet hung from a chain, transformer core "
        "and two pickup coils")


# ---------------------------------------------------------------- 21.6
def fig_21_6():
    o = [_defs()]
    o.append(_tank(200, 120, 200, 130, "#ffffff"))
    o.append('<rect x="202" y="140" width="196" height="108" fill="%s"/>' % FILL)

    # balance beam
    o.append('<line x1="120" y1="66" x2="470" y2="66" stroke="%s" stroke-width="3" '
             'stroke-linecap="round"/>' % E)
    o.append('<polygon points="300,66 288,86 312,86" fill="#e8e8e8" stroke="%s" stroke-width="1.2"/>'
             % E)
    o.append('<rect x="294" y="86" width="12" height="32" fill="#fafafa" stroke="%s" '
             'stroke-width="1.1"/>' % E)
    o.append('<rect x="270" y="112" width="60" height="8" fill="#f2f2f2" stroke="%s" '
             'stroke-width="1.1"/>' % E)
    # displacer hanging from the beam
    o.append('<line x1="282" y1="66" x2="282" y2="140" stroke="%s" stroke-width="1.4"/>' % E)
    o.append('<rect x="262" y="140" width="40" height="80" fill="#ffffff" stroke="%s" '
             'stroke-width="1.5"/>' % E)
    o.append(_dot(300, 66, 4))
    # counterweight
    o.append('<circle cx="452" cy="66" r="11" fill="#f2f2f2" stroke="%s" stroke-width="1.3"/>' % E)

    # manometer
    o.append('<path d="M520 120 L520 176 Q520 194 536 194 Q552 194 552 176 L552 120" '
             'fill="none" stroke="%s" stroke-width="2"/>' % E)
    o.append('<path d="M520 168 L520 176 Q520 190 536 190 Q552 190 552 176 L552 168 Z" '
             'fill="%s" stroke="none"/>' % FILL)
    o.append('<line x1="400" y1="130" x2="520" y2="130" stroke="%s" stroke-width="1.3"/>' % E)

    o.append(_lbl(140, 56, "Đòn cân", "t"))
    o.append(_lbl(330, 176, "Phao (displacer)", "t"))
    o.append(_lbl(300, 240, "Bình chứa khí", "t", "middle"))
    o.append(_lbl(536, 110, "Áp kế chữ U", "ts", "middle"))
    o.append(_lbl(452, 46, "Đối trọng", "ts", "middle"))
    o.append(_lbl(300, 268, "Cân bằng phao trong không khí, rồi thay bằng khí ở cùng áp suất", "ts",
                  "middle"))
    return _fig(
        svg(680, 280, "".join(o), "Sơ đồ cân khí kiểu lực đẩy (buoyancy gas balance)"),
        "Hình 21.6 · Cân khí kiểu lực đẩy (buoyancy gas balance). Một phao được treo trên đòn cân "
        "trong bình; phao được cân bằng trong không khí và ghi lại số đọc trên áp kế tại đúng áp suất "
        "cân bằng. Sau đó không khí được thay bằng khí và áp suất được điều chỉnh cho tới khi cân "
        "bằng trở lại. Tỉ số áp suất của không khí trên áp suất của khí chính là khối lượng riêng của "
        "khí so với không khí.",
        "Figure 21.6 · Buoyancy gas balance. A displacer is mounted on a balance beam in a vessel; it is "
        "balanced for air and the manometer reading is noted at the exact balance pressure. The air is "
        "then displaced by gas and the pressure adjusted until the same balance is restored. The ratio "
        "of the pressure of air to that of the gas is the density of the gas relative to air.",
        "Cân khí kiểu lực đẩy: đòn cân có điểm tựa, phao treo trong bình khí, đối trọng và áp kế chữ U",
        "Buoyancy gas balance: pivoted beam, displacer in a gas vessel, counterweight and U-tube manometer")


# ---------------------------------------------------------------- 21.7
def fig_21_7():
    o = [_defs()]
    o.append(_tank(140, 96, 120, 120))
    o.append(_tank(380, 96, 120, 120, "#f7f7f7"))
    o.append('<line x1="200" y1="52" x2="200" y2="186" stroke="%s" stroke-width="3.4"/>' % E)
    o.append('<line x1="440" y1="52" x2="440" y2="186" stroke="%s" stroke-width="3.4"/>' % E)
    # pressure lines down to the transmitter
    o.append('<path d="M200 52 L290 52 L290 228" fill="none" stroke="%s" stroke-width="1.4"/>' % E)
    o.append('<path d="M440 52 L370 52 L370 228" fill="none" stroke="%s" stroke-width="1.4"/>' % E)
    o.append(_box(255, 228, 140, 40, "Bộ truyền áp vi sai"))

    o.append(_lbl(200, 236, "Nước (chuẩn)", "t", "middle"))
    o.append(_lbl(440, 236, "Chất lỏng mẫu", "t", "middle"))
    o.append(_lbl(210, 88, "Hai ống giống nhau, cùng khoảng cách từ mặt thoáng", "ts"))
    o.append(_lbl(340, 288, "Chênh áp ở bộ truyền được quy đổi thành tỉ trọng tương đối", "ts",
                  "middle"))
    return _fig(
        svg(680, 300, "".join(o), "Sơ đồ tỉ trọng kế cột chuẩn (reference column densitometer)"),
        "Hình 21.7 · Tỉ trọng kế cột chuẩn (reference column densitometer). Hai ống hoàn toàn giống "
        "nhau, có cùng khoảng cách từ mặt thoáng, được đặt vào nước và vào chất lỏng. Nước với đặc "
        "tính khối lượng riêng đã biết được dùng làm chuẩn; áp suất cần thiết để đẩy chất lưu trong "
        "ống tỉ lệ với khối lượng riêng của chất lưu. Chênh áp tại bộ truyền áp suất vi sai được quy "
        "đổi thành tỉ trọng tương đối. Hai cột phải giữ cùng nhiệt độ.",
        "Figure 21.7 · Reference column densitometer. Two identical tubes, at the same distance from the "
        "surface, are placed in water and in the liquid. Water of known density is the reference; the "
        "pressures needed to displace the fluids inside the tubes are proportional to their densities. "
        "The pressure difference at the differential-pressure transmitter is translated into relative "
        "densities. Both columns must be kept at the same temperature.",
        "Tỉ trọng kế cột chuẩn: bình nước và bình chất lỏng mẫu, hai ống nhúng giống nhau, bộ truyền áp vi sai",
        "Reference column densitometer: water tank and sample-liquid tank, two identical dip tubes, "
        "differential-pressure transmitter")


def _twotube(suppression=False):
    o = [_defs()]
    tx, tw = (150, 200) if suppression else (180, 220)
    ax, bx = tx + 70, tx + 160
    o.append(_tank(tx, 90, tw, 150))
    o.append('<line x1="%d" y1="50" x2="%d" y2="150" stroke="%s" stroke-width="3.2"/>' % (ax, ax, E))
    o.append('<line x1="%d" y1="50" x2="%d" y2="196" stroke="%s" stroke-width="3.2"/>' % (bx, bx, E))
    # bubbles at the tube mouths
    for cy in (158, 168):
        o.append(_dot(ax, cy, 3, S))
    for cy in (204, 214):
        o.append(_dot(bx, cy, 3, S))
    # constant drop (suppression) chamber on the low-pressure side
    if suppression:
        o.append(_box(390, 140, 130, 54, "Buồng giảm áp\nkhông đổi", E, "#fbfbfb", 10))
        o.append('<path d="M%d 50 L355 50 L355 167 L390 167" fill="none" stroke="%s" '
                 'stroke-width="1.4"/>' % (bx, E))
        o.append('<path d="M450 194 L450 262 L370 262" fill="none" stroke="%s" stroke-width="1.4"/>'
                 % E)
        o.append('<path d="M%d 50 L%d 50 L%d 262" fill="none" stroke="%s" stroke-width="1.4"/>'
                 % (ax, ax - 20, ax - 20, E))
        o.append(_box(230, 262, 140, 38, "Bộ truyền áp vi sai"))
        o.append(_lbl(452, 220, "Nối tiếp phía áp thấp", "ts"))
        o.append(_lbl(ax - 40, 44, "Ống sục khí", "ts", "end"))
    else:
        o.append('<path d="M%d 50 L%d 50 L%d 258" fill="none" stroke="%s" stroke-width="1.4"/>'
                 % (ax, ax - 20, ax - 20, E))
        o.append('<path d="M%d 50 L%d 50 L%d 258" fill="none" stroke="%s" stroke-width="1.4"/>'
                 % (bx, bx + 30, bx + 30, E))
        o.append(_box(250, 258, 140, 38, "Bộ truyền áp vi sai"))
        o.append(_lbl(ax - 40, 44, "Ống sục khí", "ts", "end"))
        o.append(_lbl(bx + 60, 150, "Miệng ống cao", "ts"))
        o.append(_lbl(bx + 60, 200, "Miệng ống thấp", "ts"))
        # dimension arrow between the two mouths
        o.append(_arr(ax + 22, 150, ax + 22, 194, G, "ah21g", 1.2))
        o.append(_arr(ax + 22, 194, ax + 22, 152, G, "ah21g", 1.2))
        o.append(_lbl(ax + 30, 176, "h", "tb"))
        o.append(_lbl(ax + 70, 244, "Δp = ρ g h", "tb"))
    return o


# ---------------------------------------------------------------- 21.8
def fig_21_8():
    o = _twotube(False)
    o.append(_lbl(340, 308, "Δp tương đương trọng lượng của cột chất lỏng có thể tích không đổi", "ts",
                  "middle"))
    return _fig(
        svg(680, 318, "".join(o), "Sơ đồ tỉ trọng kế cột hai ống sục khí"),
        "Hình 21.8 · Tỉ trọng kế cột hai ống sục khí (two-tube column densitometer). Hai ống được đặt "
        "trong chất lỏng mẫu sao cho miệng một ống cao hơn miệng ống kia. Áp suất cần để sục khí vào "
        "chất lỏng từ mỗi ống bằng áp suất của chất lỏng tại miệng ống. Vì khoảng cách giữa hai miệng "
        "ống là cố định, chênh áp bằng trọng lượng của cột chất lỏng giữa hai miệng, do đó phép đo "
        "chênh áp tương đương trọng lượng của một thể tích chất lỏng không đổi và có thể chia thang "
        "trực tiếp theo khối lượng riêng. Phương pháp này chính xác tới 0,1 %–1 % tỉ trọng.",
        "Figure 21.8 · Two-tube column densitometer. The tubes sit in the sample fluid with one mouth "
        "higher than the other. The pressure needed to bubble air into the fluid equals the fluid "
        "pressure at the tube mouth. Since the spacing of the mouths is fixed, the pressure difference "
        "equals the weight of the liquid column between them, so the differential-pressure measurement "
        "is equivalent to the weight of a constant volume of liquid and can be calibrated directly "
        "against density. Accuracy is 0.1% to 1% specific gravity.",
        "Tỉ trọng kế hai ống sục khí: hai ống có miệng ở độ cao khác nhau, bọt khí, chênh áp h, bộ truyền áp vi sai",
        "Two-tube bubbler densitometer: two tubes with mouths at different depths, bubbles, head h, "
        "differential-pressure transmitter")


# ---------------------------------------------------------------- 21.9
def fig_21_9():
    o = _twotube(True)
    o.append(_lbl(300, 312, "Cùng nguyên lý như Hình 21.7 và 21.8; buồng giảm áp cho số đọc chính xác hơn",
                  "ts", "middle"))
    return _fig(
        svg(680, 322, "".join(o), "Sơ đồ tỉ trọng kế cột hai ống kiểu nén dải đo"),
        "Hình 21.9 · Tỉ trọng kế cột hai ống kiểu nén dải đo (suppression type). Nguyên lý hoạt động "
        "giống như Hình 21.7 và 21.8, nhưng có thêm một buồng giảm áp không đổi mắc nối tiếp với phía "
        "áp thấp. Buồng này tạo thuận lợi cho việc chia thang và cho số đọc khối lượng riêng chính "
        "xác hơn.",
        "Figure 21.9 · Suppression-type, two-tube column densitometer. The principle is the same as in "
        "Figures 21.7 and 21.8, but an additional constant pressure-drop chamber is placed in series "
        "with the low-pressure side. It gives advantages in scaling and in accurate readings of density.",
        "Tỉ trọng kế hai ống kiểu nén dải: thêm buồng giảm áp không đổi nối tiếp phía áp thấp",
        "Suppression-type two-tube densitometer: additional constant pressure-drop chamber in series with "
        "the low-pressure side")


# ---------------------------------------------------------------- 21.10
def fig_21_10():
    o = [_defs()]
    o.append('<rect x="100" y="114" width="62" height="12" fill="%s" stroke="%s" stroke-width="1.1"/>'
             % (FILL, E))
    o.append(_bellows(162, 120, 40, 26))
    o.append('<line x1="202" y1="120" x2="478" y2="120" stroke="%s" stroke-width="7" '
             'stroke-linecap="round"/>' % E)
    o.append(_bellows(478, 120, 40, 26))
    o.append('<rect x="518" y="114" width="62" height="12" fill="%s" stroke="%s" stroke-width="1.1"/>'
             % (FILL, E))
    # electromagnetic vibrators
    o.append(_box(298, 72, 48, 26, "~", E, WARM, 12))
    o.append(_box(298, 142, 48, 26, "~", E, WARM, 12))
    # transverse vibration arrows
    o.append(_arr(392, 110, 392, 94, G, "ah21g", 1.3))
    o.append(_arr(392, 130, 392, 146, G, "ah21g", 1.3))

    o.append(_lbl(240, 106, "Chất lỏng", "ts", "middle"))
    o.append(_lbl(182, 164, "Bellows cách ly", "ts", "middle"))
    o.append(_lbl(322, 190, "Bộ rung điện từ", "ts", "middle"))
    o.append(_lbl(408, 100, "Dao động ngang", "ts"))
    o.append(_lbl(560, 190, "f_cộng hưởng = f(ρ)", "tb", "middle"))
    o.append(_lbl(340, 226, "Ống dài xấp xỉ 20 lần đường kính", "ts", "middle"))
    return _fig(
        svg(680, 240, "".join(o), "Sơ đồ tỉ trọng kế ống rung"),
        "Hình 21.10 · Tỉ trọng kế ống rung (vibrating tube). Ống chứa chất lưu được các bộ rung điện "
        "từ kích cho dao động ở tần số cộng hưởng; tần số cộng hưởng là hàm của khối lượng riêng chất "
        "lưu và được đo chính xác. Ống được cách ly với các chi tiết gá lắp bằng các bellows được thiết "
        "kế cẩn thận; chiều dài ống xấp xỉ 20 lần đường kính.",
        "Figure 21.10 · Vibrating tube densitometer. The tube containing the fluid is vibrated at its "
        "resonant frequency by electromagnetic vibrators; the resonant frequency is a function of the "
        "fluid density and is measured accurately. The tube is isolated from the fixtures by carefully "
        "designed bellows, and its length is about 20 times its diameter.",
        "Tỉ trọng kế ống rung: ống dẫn chất lỏng, bellows cách ly hai đầu, hai bộ rung điện từ, mũi tên dao động ngang",
        "Vibrating tube densitometer: fluid tube, isolation bellows at both ends, two electromagnetic "
        "vibrators, transverse vibration arrows")


# ---------------------------------------------------------------- 21.11
def fig_21_11():
    o = [_defs()]
    for y in (96, 140):
        o.append(_bellows(160, y, 40, 22))
        o.append('<line x1="200" y1="%d" x2="480" y2="%d" stroke="%s" stroke-width="6" '
                 'stroke-linecap="round"/>' % (y, y, E))
        o.append(_bellows(480, y, 40, 22))
    o.append('<line x1="160" y1="96" x2="160" y2="140" stroke="%s" stroke-width="5"/>' % E)
    o.append('<line x1="520" y1="96" x2="520" y2="140" stroke="%s" stroke-width="5"/>' % E)
    o.append('<rect x="100" y="112" width="60" height="12" fill="%s" stroke="%s" stroke-width="1.1"/>'
             % (FILL, E))
    o.append('<rect x="520" y="112" width="60" height="12" fill="%s" stroke="%s" stroke-width="1.1"/>'
             % (FILL, E))
    o.append(_arr(340, 86, 340, 70, G, "ah21g", 1.3))
    o.append(_arr(340, 150, 340, 166, G, "ah21g", 1.3))

    o.append(_lbl(130, 102, "Vào", "ts", "middle"))
    o.append(_lbl(550, 102, "Ra", "ts", "middle"))
    o.append(_lbl(340, 190, "Hai ống dao động ngược pha", "ts", "middle"))
    o.append(_lbl(340, 214, "Kích thước nhỏ gọn, dễ kiểm tra và vệ sinh", "ts", "middle"))
    return _fig(
        svg(680, 226, "".join(o), "Sơ đồ tỉ trọng kế hai ống rung dao động ngược pha"),
        "Hình 21.11 · Tỉ trọng kế hai ống rung. Hai ống được kích dao động ngược pha để đạt độ chính "
        "xác cao hơn. Tỉ trọng kế hai ống có kích thước nhỏ gọn, dễ sử dụng, ít cản trở dòng chảy và "
        "dễ kiểm tra, vệ sinh.",
        "Figure 21.11 · Two-tube vibrating densitometer. Two tubes are vibrated in antiphase for greater "
        "accuracy. Twin-tube densitometers are compact, easy to use, present very little blockage and are "
        "easy to inspect and clean.",
        "Tỉ trọng kế hai ống rung: hai ống song song dao động ngược pha, bellows hai đầu, đường vào và ra",
        "Two-tube vibrating densitometer: two parallel tubes in antiphase, bellows at both ends, inlet "
        "and outlet")


# ---------------------------------------------------------------- 21.12
def fig_21_12():
    o = [_defs()]
    o.append('<rect x="200" y="150" width="300" height="60" fill="%s"/>' % FILL)
    o.append('<line x1="200" y1="150" x2="500" y2="150" stroke="%s" stroke-width="1.2" '
             'stroke-dasharray="6 4"/>' % S)
    o.append('<rect x="296" y="58" width="88" height="24" rx="3" fill="#f2f2f2" stroke="%s" '
             'stroke-width="1.4"/>' % E)
    o.append('<rect x="306" y="82" width="16" height="92" fill="#ffffff" stroke="%s" '
             'stroke-width="1.5"/>' % E)
    o.append('<rect x="358" y="82" width="16" height="92" fill="#ffffff" stroke="%s" '
             'stroke-width="1.5"/>' % E)
    o.append('<rect x="252" y="64" width="36" height="14" fill="%s" stroke="%s" stroke-width="1.1"/>'
             % (WARM, G))
    o.append('<rect x="392" y="64" width="36" height="14" fill="%s" stroke="%s" stroke-width="1.1"/>'
             % (WARM, G))

    o.append(_lbl(250, 52, "Cuộn kích thích / thu", "ts", "end"))
    o.append(_lbl(392, 108, "Lưỡi nĩu (tines)", "t"))
    o.append(_lbl(512, 146, "Mặt thoáng chất lỏng", "ts"))
    o.append(_lbl(340, 232, "f_riêng của nĩu là hàm của khối lượng riêng chất lưu", "ts", "middle"))
    return _fig(
        svg(680, 244, "".join(o), "Sơ đồ tỉ trọng kế nĩu rung (tuning fork)"),
        "Hình 21.12 · Tỉ trọng kế nĩu rung (tuning fork). Thiết bị dùng tần số riêng của các nĩu rung "
        "có khối lượng nhỏ. Trong một số trường hợp chất lưu được đưa vào một buồng nhỏ đặt các nĩu "
        "được kích bằng cơ điện; trong trường hợp khác nĩu được nhúng trực tiếp vào chất lỏng. Mỗi "
        "ứng dụng đều cần hiệu chuẩn riêng.",
        "Figure 21.12 · Tuning fork densitometer. Twin forks are inserted into the fluid and their "
        "natural frequencies are measured accurately; the natural frequency is a function of the fluid "
        "density. In some cases the fluid is taken into a small chamber holding the electromechanically "
        "driven forks, in others the fork is inserted directly into the liquid. Calibration is necessary "
        "in each application.",
        "Tỉ trọng kế nĩu rung: đế có cuộn kích thích, hai lưỡi nĩu nhúng vào chất lỏng, mặt thoáng",
        "Tuning fork densitometer: base with drive coils, two tines immersed in the liquid, liquid surface")


# ---------------------------------------------------------------- 21.13
def fig_21_13():
    o = [_defs()]
    o.append('<rect x="100" y="110" width="84" height="44" fill="%s" stroke="%s" stroke-width="1.5"/>'
             % (FILL, E))
    o.append('<rect x="184" y="92" width="316" height="80" fill="%s" stroke="%s" stroke-width="1.5"/>'
             % (FILL, E))
    o.append('<rect x="500" y="110" width="84" height="44" fill="%s" stroke="%s" stroke-width="1.5"/>'
             % (FILL, E))
    # source with lead shielding
    o.append('<rect x="296" y="40" width="78" height="34" rx="4" fill="#fdf2ee" stroke="%s" '
             'stroke-width="1.5"/>' % E)
    o.append(_lbl(335, 61, "Nguồn γ", "tb", "middle"))
    o.append('<rect x="306" y="74" width="58" height="10" fill="#dddddd" stroke="%s" '
             'stroke-width="1.1"/>' % E)
    # detector
    o.append('<rect x="296" y="186" width="78" height="34" rx="4" fill="#ffffff" stroke="%s" '
             'stroke-width="1.5"/>' % E)
    o.append(_lbl(335, 207, "Đầu dò", "tb", "middle"))
    # beam
    o.append('<line x1="335" y1="84" x2="335" y2="184" stroke="%s" stroke-width="1.6" '
             'stroke-dasharray="7 5"/>' % G)
    o.append(_arr(335, 118, 335, 178, G, "ah21g", 1.2))

    o.append(_lbl(390, 58, "Nguồn phóng xạ trong vỏ chì", "ts"))
    o.append(_lbl(390, 214, "Đầu dò (ion hoá / nhấp nháy)", "ts"))
    o.append(_lbl(348, 140, "Chùm tia γ", "ts"))
    o.append(_lbl(240, 188, "Đoạn ống mở rộng", "ts", "middle"))
    return _fig(
        svg(680, 240, "".join(o), "Sơ đồ bố trí tỉ trọng kế phóng xạ trên đoạn ống mở rộng"),
        "Hình 21.13 · Bố trí tỉ trọng kế phóng xạ trên một đoạn ống được mở rộng. Ống được mở rộng "
        "để tia đi qua chất lỏng dài hơn, nhờ đó năng lượng phóng xạ bị suy giảm mạnh hơn và phép đo "
        "chính xác hơn. Nguồn được đặt trong vỏ chì kẹp lên thành ống hoặc thành bình; trong nhiều "
        "ứng dụng đầu dò cũng được kẹp lên thành.",
        "Figure 21.13 · Fixing a radioactive densitometer on an enlarged pipe. The pipe is enlarged to "
        "give a longer beam path through the liquid, and hence better attenuation of the radioactive "
        "energy. The source is mounted in a lead container clamped onto the pipe or vessel wall; in many "
        "applications the detector is also clamped onto the wall.",
        "Tỉ trọng kế phóng xạ trên ống mở rộng: nguồn gamma trong vỏ chì ở trên, chùm tia thẳng đứng, đầu dò ở dưới",
        "Radioactive densitometer on an enlarged pipe: shielded gamma source above, vertical beam, "
        "detector below")


# ---------------------------------------------------------------- 21.14
def fig_21_14():
    o = [_defs()]
    o.append('<rect x="90" y="96" width="150" height="44" fill="%s" stroke="%s" stroke-width="1.5"/>'
             % (FILL, E))
    o.append('<polygon points="240,96 430,146 430,190 240,140" fill="%s" stroke="%s" '
             'stroke-width="1.5"/>' % (FILL, E))
    o.append('<rect x="430" y="146" width="150" height="44" fill="%s" stroke="%s" stroke-width="1.5"/>'
             % (FILL, E))
    # source above, detector below the elongated section
    o.append('<rect x="262" y="34" width="76" height="32" rx="4" fill="#fdf2ee" stroke="%s" '
             'stroke-width="1.5"/>' % E)
    o.append(_lbl(300, 54, "Nguồn γ", "tb", "middle"))
    o.append('<rect x="272" y="66" width="56" height="10" fill="#dddddd" stroke="%s" '
             'stroke-width="1.1"/>' % E)
    o.append('<rect x="356" y="204" width="76" height="32" rx="4" fill="#ffffff" stroke="%s" '
             'stroke-width="1.5"/>' % E)
    o.append(_lbl(394, 224, "Đầu dò", "tb", "middle"))
    o.append('<line x1="300" y1="76" x2="392" y2="204" stroke="%s" stroke-width="1.6" '
             'stroke-dasharray="7 5"/>' % G)
    o.append(_arr(330, 118, 372, 178, G, "ah21g", 1.2))

    o.append(_lbl(240, 214, "Đoạn ống kéo dài", "ts", "middle"))
    o.append(_lbl(470, 252, "Đường đi dài hơn → suy giảm mạnh hơn", "ts", "middle"))
    return _fig(
        svg(680, 262, "".join(o), "Sơ đồ bố trí tỉ trọng kế phóng xạ trên đoạn ống kéo dài"),
        "Hình 21.14 · Bố trí tỉ trọng kế phóng xạ trên một đoạn ống kéo dài. Đường đi dài hơn của tia "
        "phóng xạ qua chất lỏng cho suy giảm mạnh hơn, do đó tín hiệu đo tốt hơn. Cách bố trí này dùng "
        "khi không thể mở rộng đường ống như trên Hình 21.13.",
        "Figure 21.14 · Fixing a radioactive densitometer on an elongated pipe. The elongated path "
        "yields a longer path length of the radioactive energy through the liquid, hence a stronger "
        "attenuation. This arrangement is used where the pipe cannot be enlarged as in Figure 21.13.",
        "Tỉ trọng kế phóng xạ trên ống kéo dài: đoạn ống chéo dài, nguồn gamma ở trên, chùm tia chéo, đầu dò ở dưới",
        "Radioactive densitometer on an elongated pipe: long slanted section, gamma source above, "
        "oblique beam, detector below")


# ---------------------------------------------------------------- 21.15
def fig_21_15():
    o = [_defs()]
    o.append('<rect x="280" y="96" width="120" height="110" fill="%s" stroke="%s" stroke-width="1.6"/>'
             % (FILL, E))
    o.append('<line x1="280" y1="96" x2="280" y2="206" stroke="%s" stroke-width="4"/>' % E)
    o.append('<line x1="400" y1="96" x2="400" y2="206" stroke="%s" stroke-width="4"/>' % E)
    # incoming, refracted and emerging beams
    o.append(_arr(150, 100, 280, 140, G, "ah21g", 2.0))
    o.append('<line x1="280" y1="140" x2="400" y2="152" stroke="%s" stroke-width="2"/>' % G)
    o.append(_arr(400, 152, 500, 168, G, "ah21g", 2.0))
    # undeviated reference
    o.append('<line x1="280" y1="140" x2="500" y2="208" stroke="%s" stroke-width="1.2" '
             'stroke-dasharray="6 4"/>' % S)
    # position-sensitive detector
    o.append('<line x1="500" y1="150" x2="500" y2="220" stroke="%s" stroke-width="3"/>' % E)
    o.append(_dot(500, 168, 4, G))
    o.append(_dot(500, 208, 4, S))
    o.append(_arr(516, 168, 516, 206, E, "ah21", 1.2))
    o.append(_arr(516, 206, 516, 170, E, "ah21", 1.2))

    o.append(_lbl(146, 92, "Tia laser", "ts", "end"))
    o.append(_lbl(292, 118, "Cửa sổ", "ts"))
    o.append(_lbl(300, 186, "Chất lỏng", "ts", "middle"))
    o.append(_lbl(462, 148, "Tia lệch", "ts"))
    o.append(_lbl(470, 232, "Tia không lệch (chuẩn)", "ts", "middle"))
    o.append(_lbl(528, 190, "Δx", "tb"))
    o.append(_lbl(560, 210, "Cảm biến vị trí", "ts"))
    o.append(_lbl(340, 258, "Độ dịch ngang của chùm tia tỉ lệ với chiết suất của chất lỏng", "ts",
                  "middle"))
    return _fig(
        svg(680, 268, "".join(o), "Sơ đồ tỉ trọng kế kiểu chiết suất với chùm laser bị dịch ngang"),
        "Hình 21.15 · Tỉ trọng kế kiểu chiết suất (index of refraction). Góc khúc xạ của chùm tia phụ "
        "thuộc hình dạng, kích thước và độ dày của bình chứa, và khối lượng riêng của chất lưu trong "
        "bình. Vì các đặc tính của bình là cố định, vị trí của chùm tia có thể liên hệ với khối lượng "
        "riêng của chất lưu; cần đo chính xác vị trí chùm tia bằng cảm biến vị trí nhạy.",
        "Figure 21.15 · Index-of-refraction densitometer. The angle of refraction of the beam depends on "
        "the shape, size and thickness of the container and on the density of the fluid inside it. "
        "Because the container characteristics are fixed, the position of the beam can be related to the "
        "density of the fluid; accurate measurement of the beam position is necessary.",
        "Tỉ trọng kế chiết suất: ô đo có hai cửa sổ, tia laser tới xiên, tia khúc xạ, tia chuẩn không lệch và độ dịch ngang",
        "Index-of-refraction densitometer: cell with two windows, oblique laser beam, refracted beam, "
        "undeviated reference and lateral displacement")


# ---------------------------------------------------------------- 21.16
def fig_21_16():
    o = [_defs()]
    o.append('<rect x="200" y="80" width="240" height="120" rx="6" fill="#fbfbfb" stroke="%s" '
             'stroke-width="1.4" stroke-dasharray="6 4"/>' % S)
    o.append('<path d="M250 80 L250 150 Q250 170 270 170 L370 170 Q390 170 390 150 L390 80" '
             'fill="none" stroke="%s" stroke-width="5.5" stroke-linecap="round"/>' % E)
    o.append('<rect x="240" y="70" width="20" height="10" fill="#dddddd" stroke="%s" '
             'stroke-width="1"/>' % E)
    o.append('<rect x="380" y="70" width="20" height="10" fill="#dddddd" stroke="%s" '
             'stroke-width="1"/>' % E)
    # drive coil under the bend
    o.append(_box(296, 182, 48, 20, "~", E, WARM, 12))
    o.append(_arr(320, 180, 320, 172, G, "ah21g", 1.2))
    # pickup sensors on the legs
    o.append('<rect x="228" y="118" width="16" height="30" fill="%s" stroke="%s" stroke-width="1.2"/>'
             % (WARM, G))
    o.append('<rect x="396" y="118" width="16" height="30" fill="%s" stroke="%s" stroke-width="1.2"/>'
             % (WARM, G))
    # transmitter
    o.append(_box(470, 96, 160, 52, "Bộ truyền\nxử lý tín hiệu", E, "#ffffff", 11))
    o.append('<line x1="440" y1="122" x2="470" y2="122" stroke="%s" stroke-width="1.4"/>' % E)

    o.append(_lbl(240, 62, "Điểm neo cố định", "ts", "end"))
    o.append(_lbl(200, 210, "Vỏ cảm biến", "ts"))
    o.append(_lbl(404, 140, "Cảm biến", "ts"))
    o.append(_lbl(470, 84, "Bộ truyền", "ts", "middle"))
    o.append(_lbl(300, 250, "ρ = f(chu kỳ dao động của ống), có hiệu chính theo nhiệt độ", "ts",
                  "middle"))
    return _fig(
        svg(680, 262, "".join(o), "Sơ đồ tỉ trọng kế Coriolis với ống rung neo hai đầu"),
        "Hình 21.16 · Tỉ trọng kế Coriolis. Dao động của ống được phát hiện và liên hệ với khối lượng "
        "và lưu lượng của chất lưu; cần hiệu chuẩn và tính toán thêm để xác định khối lượng riêng. Ống "
        "cảm biến được neo chắc tại điểm vào và ra của chất lưu, đầu tự do được kích dao động; khối "
        "lượng chất lưu trong ống bằng khối lượng riêng nhân thể tích, và vì thể tích ống không đổi "
        "nên tần số dao động liên hệ trực tiếp với khối lượng riêng.",
        "Figure 21.16 · Coriolis densitometer. Vibration of the tube is detected and related to the mass "
        "and flow rate of the fluid; further calibration and calculation are needed to determine "
        "density. The sensor tubes are anchored at the fluid inlet and outlet and the free end is "
        "vibrated; the fluid mass in the tube equals density times volume, and since the volume is "
        "constant the oscillation frequency relates directly to density.",
        "Tỉ trọng kế Coriolis: vỏ cảm biến, ống chữ U neo hai đầu, cuộn kích thích ở đáy, hai cảm biến và bộ truyền",
        "Coriolis densitometer: sensor housing, U-tube anchored at both ends, drive coil at the bend, two "
        "pickups and a transmitter")


FIGS = [fig_21_1, fig_21_2, fig_21_3, fig_21_4, fig_21_5, fig_21_6, fig_21_7, fig_21_8,
        fig_21_9, fig_21_10, fig_21_11, fig_21_12, fig_21_13, fig_21_14, fig_21_15, fig_21_16]


def fig(n):
    return FIGS[n - 1]()
