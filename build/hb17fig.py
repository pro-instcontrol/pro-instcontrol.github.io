# -*- coding: utf-8 -*-
"""Vector redraws of the figures in the CRC Measurement Handbook, Ch. 17
(Acceleration, Vibration, and Shock Measurement). Twenty-three figures:
seismic/mass-spring accelerometers, frequency-response curves, electromechanical
servo, piezoelectric, piezoresistive, differential-capacitance, strain-gage, seismic,
inertial/vibrating-string, electrostatic, micro (DETF), cross-axis, and signal
conditioning. Each function returns (svg, caption_vi, caption_en, aria_vi, aria_en).
"""
import math as _m

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
            '<marker id="ah17" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
            '<path d="M0,0 L7,3 L0,6 Z" fill="%s"/></marker>'
            '<marker id="ah17g" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
            '<path d="M0,0 L7,3 L0,6 Z" fill="%s"/></marker></defs>' % (E, G))


def _arr(x1, y1, x2, y2, col=E, marker="ah17", sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, marker))


def _box(x, y, w, h, t, col=E, fill="#ffffff", fs=12):
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" stroke-width="1.4"/>'
            '<text class="%s" x="%s" y="%s" text-anchor="middle">%s</text>'
            % (_f(x), _f(y), _f(w), _f(h), fill, col, "tb", _f(x + w / 2.0), _f(y + h / 2.0 + fs * 0.35), t))


# ---------------------------------------------------------------- 17.1
def fig_17_1():
    o = [_defs()]
    # rigid frame
    o.append('<rect x="120" y="40" width="280" height="200" fill="none" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(120, 34, "khung cứng (gắn vào kết cấu rung)", "ts"))
    # vibrating structure at base
    o.append('<line x1="60" y1="240" x2="480" y2="240" stroke="%s" stroke-width="2"/>' % E)
    o.append(_lbl(60, 258, "kết cấu rung (vibrating structure)", "ts"))
    # spring suspending seismic mass
    o.append('<line x1="260" y1="40" x2="260" y2="92" stroke="%s" stroke-width="1.4"/>' % E)
    for k in range(5):
        yy = 50 + k * 8
        o.append('<path d="M250 %d q 10 4 20 0 q 10 4 20 0" fill="none" stroke="%s" stroke-width="1"/>' % (yy, E))
    o.append('<line x1="260" y1="92" x2="260" y2="120" stroke="%s" stroke-width="1.4"/>' % E)
    # seismic mass
    o.append('<rect x="225" y="120" width="70" height="48" fill="#e5e7eb" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(260, 149, "khối lượng M", "tb", "middle"))
    # relative displacement pickup
    o.append('<line x1="295" y1="144" x2="360" y2="144" stroke="%s" stroke-width="1.2" stroke-dasharray="3 2"/>' % S)
    o.append(_lbl(300, 138, "cảm biến dịch chuyển tương đối z", "ts"))
    return _fig(
        svg(680, 280, "".join(o), "Cảm biến gia tốc kiểu địa chấn lệch hướng điển hình"),
        "Hình 17.1 · Cảm biến gia tốc kiểu địa chấn lệch hướng (deflection type) điển hình. Khối lượng địa "
        "chấn M được treo bởi lò xo hoặc dầm cantilever trong một khung cứng; khung gắn vào kết cấu rung. Khi "
        "kết cấu rung, khối lượng có xu hướng đứng yên, nên chuyển động tương đối được cảm biến. Chúng thuộc "
        "hệ bậc hai.",
        "Figure 17.1 · A typical deflection-type seismic accelerometer. The seismic mass M is suspended by a "
        "spring or cantilever inside a rigid frame fixed to the vibrating structure; as the structure vibrates the "
        "mass tends to stay put, so the relative displacement is picked up. These are second-order systems.",
        "Khung cứng gắn vào kết cấu rung, lò xo treo khối lượng M, cảm biến đo chuyển động tương đối z giữa khối "
        "và khung.",
        "A rigid frame fixed to the vibrating structure, a spring suspending seismic mass M, and a pickup sensing "
        "the relative motion z between mass and frame.")


# ---------------------------------------------------------------- 17.2
def fig_17_2():
    o = [_defs()]
    o.append('<rect x="100" y="40" width="500" height="200" fill="none" stroke="%s" stroke-width="1.2"/>' % E)
    o.append(_lbl(600, 44, "tần số f (log)", "ts"))
    o.append('<text class="ts" x="40" y="60" transform="rotate(-90 40 60)">biên độ (log)</text>')
    # three parallel lines on log-log: a (flat), v (slope -1), x (slope -2)
    # approximate with straight segments in the drawing coordinates
    o.append('<line x1="120" y1="60" x2="580" y2="60" stroke="%s" stroke-width="2"/>' % E)       # acceleration flat
    o.append('<line x1="120" y1="100" x2="580" y2="200" stroke="%s" stroke-width="2"/>' % G)     # velocity slope -1
    o.append('<line x1="120" y1="150" x2="580" y2="230" stroke="%s" stroke-width="2"/>' % S)     # displacement slope -2
    o.append(_lbl(430, 52, "a (gia tốc)", "tb"))
    o.append(_lbl(470, 150, "v (vận tốc)", "tb"))
    o.append(_lbl(540, 226, "x (vị trí)", "tb"))
    o.append(_lbl(130, 258, "trục tung log: a = ω²x, v = ωx — đọc vận tốc bằng a/ω, vị trí bằng a/ω²", "tb"))
    return _fig(
        svg(680, 280, "".join(o), "Quan hệ logarit giữa gia tốc, vận tốc và vị trí"),
        "Hình 17.2 · Quan hệ logarit giữa gia tốc, vận tốc và vị trí. Vận tốc ở một tần số nhất định thu được "
        "bằng cách chia gia tốc cho một hệ số tỉ lệ tần số; vị trí thì chia gia tốc cho hệ số tỉ lệ bình phương "
        "tần số. Góc pha cần xác định riêng, nhưng bỏ qua trong đo trung bình theo thời gian.",
        "Figure 17.2 · Logarithmic relationship between acceleration, velocity, and displacement. Velocity at a "
        "given frequency is obtained by dividing acceleration by a factor proportional to frequency; displacement "
        "by dividing acceleration by a factor proportional to the square of frequency. Phase angles are found "
        "separately and neglected in time-averaged measurements.",
        "Đồ thị log–log với ba đường song song: gia tốc nằm ngang, vận tốc dốc -1, vị trí dốc -2 theo log tần số.",
        "A log–log plot with three parallel lines: acceleration horizontal, velocity slope −1, displacement slope "
        "−2 versus log frequency.")


# ---------------------------------------------------------------- 17.3
def fig_17_3():
    o = [_defs()]
    # base rectangular pulse excitation
    o.append('<path d="M120 70 L120 50 L420 50 L420 70 Z" fill="#cbd5e1" stroke="%s" stroke-width="1.4"/>' % E)
    o.append(_lbl(270, 42, "kích thích xung chữ nhật của đế", "tb", "middle"))
    # mass response: damped oscillation peaking ~2x
    pts = []
    cx = 270.0
    for i in range(0, 401, 4):
        x = 120 + i
        t = i / 60.0
        # pulse window 0..300, then damped sine
        if i < 300:
            y = 160 - 45 * _m.sin(0.18 * i) * _m.exp(-0.012 * i) * (i / 60.0)
        else:
            y = 160 - 45 * _m.sin(0.18 * i) * _m.exp(-0.012 * i)
        pts.append((x, y))
    d = "M" + " L".join("%s %s" % p for p in pts)
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2"/>' % (d, G))
    o.append('<line x1="120" y1="160" x2="560" y2="160" stroke="%s" stroke-width="1" stroke-dasharray="4 3"/>' % S)
    o.append(_lbl(120, 174, "0", "tb"))
    o.append(_lbl(440, 96, "đáp ứng đạt tới ~2× độ lớn xung", "ts"))
    o.append(_lbl(300, 232, "thời gian", "tb", "middle"))
    return _fig(
        svg(680, 250, "".join(o), "Đáp ứng thời gian của kích động xung lên hệ một bậc tự do"),
        "Hình 17.3 · Đáp ứng thời gian của một kích động xung lên hệ một bậc tự do. Khi độ dài xung tăng, dao "
        "động duy trì ngắn lại nhưng biên độ lớn hơn. Đáp ứng cực đại có thể bằng tới hai lần độ lớn của xung.",
        "Figure 17.3 · Time response of a single-degree-of-freedom system to shock excitation. As the shock-pulse "
        "duration increases, sustained oscillations get shorter in time but larger in amplitude. The maximum "
        "system response may reach twice the shock-pulse magnitude.",
        "Xung chữ nhật kích thích đế ở trên, đường dao động tắt dần của khối lượng ở dưới, đỉnh đáp ứng gần 2 lần "
        "độ lớn xung.",
        "A rectangular base-excitation pulse on top and the damped oscillatory mass response below, peaking near "
        "twice the pulse magnitude.")


# ---------------------------------------------------------------- 17.4
def fig_17_4():
    o = [_defs()]
    o.append('<rect x="100" y="40" width="500" height="200" fill="none" stroke="%s" stroke-width="1.2"/>' % E)
    o.append(_lbl(600, 44, "thời gian", "ts"))
    o.append(_lbl(40, 60, "đáp ứng", "ts"))
    # unit step line at 1.0
    o.append('<line x1="100" y1="200" x2="600" y2="200" stroke="%s" stroke-width="1" stroke-dasharray="4 3"/>' % S)
    # several step responses with different damping
    for (zeta, col) in ((0.2, G), (0.4, E), (0.707, E), (1.0, S)):
        pts = []
        for i in range(0, 401, 4):
            x = 100 + i
            t = i / 40.0
            wn = 2.2
            if zeta < 1.0:
                # underdamped second-order step response magnitude
                y = 200 - 150 * (1 - (1 / _m.sqrt(1 - zeta ** 2)) * _m.exp(-zeta * wn * t)
                                 * _m.cos(wn * _m.sqrt(1 - zeta ** 2) * t - 0))
            else:
                # critically damped: 1 - (1 + wn t) e^{-wn t}  (no overshoot, slowest)
                y = 200 - 150 * (1 - (1 + wn * t) * _m.exp(-wn * t))
            pts.append((x, y))
        d = "M" + " L".join("%s %s" % p for p in pts)
        o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2"/>' % (d, col))
    o.append(_lbl(150, 70, "ζ nhỏ: đáp ứng nhanh, quá điều chỉnh lớn", "ts"))
    o.append(_lbl(360, 110, "ζ = 0,707 phổ biến", "ts"))
    return _fig(
        svg(680, 250, "".join(o), "Đáp ứng bậc thang đơn vị của hệ bậc hai với các tỉ số giảm chấn khác nhau"),
        "Hình 17.4 · Đáp ứng bậc thang đơn vị của hệ bậc hai với các tỉ số giảm chấn khác nhau. Quá điều chỉnh, "
        "độ trễ, thời gian tăng và thời gian xác lập phụ thuộc tỉ số giảm chấn. Tỉ số giảm chấn nhỏ cho đáp ứng "
        "nhanh nhưng quá điều chỉnh lớn; nhiều ứng dụng chọn ζ ≈ 0,707.",
        "Figure 17.4 · Unit-step time responses of a second-order system for various damping ratios. Overshoot, "
        "delay, rise and settling times depend on the damping ratio; smaller damping gives faster response but "
        "larger overshoot. A damping ratio of about 0.707 is often preferred.",
        "Đồ thị các đường đáp ứng bậc thang: ζ nhỏ quá điều chỉnh lớn, ζ ≈ 0,707 phẳng, ζ = 1 quá điều chỉnh bằng "
        "không nhưng chậm.",
        "Step-response curves: small ζ overshoots, ζ ≈ 0.707 is flat, ζ = 1 has no overshoot but is slow.")


# ---------------------------------------------------------------- 17.5
def fig_17_5():
    o = [_defs()]
    # two panels: magnitude (dB) and phase
    # magnitude
    o.append(_box(80, 50, 230, 150, "độ lợi (dB)", E, "#ffffff", 12))
    o.append('<line x1="90" y1="180" x2="300" y2="180" stroke="%s" stroke-width="1"/>' % E)
    o.append('<line x1="90" y1="180" x2="90" y2="70" stroke="%s" stroke-width="1"/>' % E)
    o.append('<path d="M90 90 L210 90 L300 150" fill="none" stroke="%s" stroke-width="2"/>' % G)  # flat then -40dB/dec
    o.append(_lbl(95, 84, "phẳng → −40 dB/thập kỷ ở ωn", "ts"))
    # phase
    o.append(_box(380, 50, 230, 150, "pha (°)", E, "#ffffff", 12))
    o.append('<line x1="390" y1="180" x2="600" y2="180" stroke="%s" stroke-width="1"/>' % E)
    o.append('<line x1="390" y1="180" x2="390" y2="70" stroke="%s" stroke-width="1"/>' % E)
    o.append('<path d="M390 90 L470 90 L600 170" fill="none" stroke="%s" stroke-width="2"/>' % G)  # 0 -> -180
    o.append(_lbl(395, 84, "0° → −180°", "ts"))
    o.append(_lbl(330, 232, "Hình Bode: độ lợi và pha của hệ bậc hai theo tần số (phụ thuộc ζ)", "tb"))
    return _fig(
        svg(680, 250, "".join(o), "Đồ thị Bode độ lợi và pha của hệ bậc hai"),
        "Hình 17.5 · Đồ thị Bode độ lợi và pha theo tần số của hệ bậc hai. Các đường là hàm của tần số và tỉ số "
        "giảm chấn; có thể tính lý thuyết hoặc đo thực nghiệm trong dải tần.",
        "Figure 17.5 · Bode plots of gains and phase angles versus frequency of a second-order system. The curves "
        "are functions of frequency and damping ratio; they can be obtained theoretically or by practical tests.",
        "Hai đồ thị Bode: độ lợi (phẳng rồi tụt −40 dB/thập kỷ) và pha (0° đến −180°), phụ thuộc ζ.",
        "Two Bode plots: gain (flat then −40 dB/decade) and phase (0° to −180°), both functions of damping ratio.")


# ---------------------------------------------------------------- 17.6
def fig_17_6():
    o = [_defs()]
    # cylindrical magnet with radial field, coil as seismic mass on arm
    o.append('<rect x="180" y="80" width="120" height="120" rx="60" fill="none" stroke="%s" stroke-width="2"/>' % E)
    o.append('<rect x="222" y="80" width="36" height="120" fill="%s"/>' % "#6b7280")  # soft-iron flux return
    o.append(_lbl(228, 74, "nam châm vĩnh cửu + lõi sắt", "ts"))
    # coil in the gap, on an arm with bearing
    o.append('<rect x="220" y="120" width="40" height="40" fill="none" stroke="%s" stroke-width="2"/>' % G)
    for k in range(4):
        yy = 124 + k * 9
        o.append('<line x1="220" y1="%d" x2="260" y2="%d" stroke="%s" stroke-width="1"/>' % (yy, yy, G))
    o.append(_lbl(240, 176, "cuộn dây (khối cảm biến)", "tb", "middle"))
    # arm to bearing at left
    o.append('<line x1="180" y1="140" x2="120" y2="140" stroke="%s" stroke-width="2"/>' % E)
    o.append('<circle cx="118" cy="140" r="5" fill="%s" stroke="%s" stroke-width="1.2"/>' % (P, E))
    o.append(_lbl(80, 134, "ổ lăn\nít ma sát", "ts", "end"))
    # pickoff + servo to null
    o.append(_arr(260, 140, 330, 140, G))
    o.append(_lbl(280, 132, "điện áp cảm ứng → servo giữ vị trí null", "ts"))
    return _fig(
        svg(680, 230, "".join(o), "Cảm biến gia tốc cuộn dây và nam châm vĩnh cửu cơ bản"),
        "Hình 17.6 · Cảm biến gia tốc cuộn dây và nam châm vĩnh cửu cơ bản. Cuộn dây nằm trong khe trụ do nam "
        "châm vĩnh cửu và lõi sắt hồi từ tạo ra; nó được đỡ bằng một cánh tay trên ổ lăn ít ma sát để thành khối "
        "lượng cảm biến. Độ dịch chuyển cuộn dây do gia tốc sinh điện thế được cảm biến và xử lý; hệ servo giữ "
        "cuộn dây ở vị trí null.",
        "Figure 17.6 · A basic coil-and-permanent-magnet accelerometer. The coil sits in the cylindrical gap of a "
        "permanent magnet and a soft-iron flux-return, mounted on a minimum-friction bearing to form the proof "
        "mass. Displacement of the coil under acceleration induces a potential sensed and processed; a servo keeps "
        "the coil at null.",
        "Nam châm vĩnh cửu hình trụ với khe, cuộn dây làm khối lượng trên cánh tay ổ lăn, hệ servo giữ null.",
        "A cylindrical permanent magnet with a gap, the coil as proof mass on a low-friction bearing arm, and a "
        "servo holding it at null.")


# ---------------------------------------------------------------- 17.7
def fig_17_7():
    o = [_defs()]
    # simplified rotational servo block diagram
    o.append(_box(80, 110, 90, 46, "khối lượng\nquán tính", E))
    o.append(_arr(170, 133, 210, 133, E))
    o.append(_box(210, 110, 90, 46, "cảm biến\n(pick-off)", E))
    o.append(_arr(300, 133, 340, 133, E))
    o.append(_box(340, 110, 110, 46, "khuếch đại +\ngiải điều biến + lọc", E))
    o.append(_arr(450, 133, 490, 133, G))
    # feedback coil restoring torque
    o.append('<path d="M490 133 L560 133 L560 200 L250 200 L250 156 L210 156" fill="none" stroke="%s" stroke-width="1.4"/>' % G)
    o.append(_box(150, 198, 100, 44, "cuộn từ →\nmômen phục hồi", G, "#fff7ed"))
    o.append(_lbl(560, 128, "eo (ra)", "ts"))
    o.append(_lbl(300, 90, "gia tốc a → lực quán tính F trên khối lượng m", "tb", "middle"))
    o.append(_lbl(360, 230, "con quay servo kiểu quay: gia tốc a ∝ điện áp ra eo", "tb", "middle"))
    return _fig(
        svg(680, 260, "".join(o), "Sơ đồ khối cảm biến servo gia tốc kiểu quay"),
        "Hình 17.7 · Một dạng đơn giản của cảm biến servo gia tốc kiểu quay. Gia tốc vỏ làm lực quán tính F tác "
        "lên khối lượng nhạy, làm nó lệch khỏi vị trí null; cảm biến (pick-off) đo góc lệch, tín hiệu được khuếch "
        "đại, giải điều biến và lọc thành dòng ia tỉ lệ chuyển động. Dòng qua cuộn trong từ trường sinh mômen đưa "
        "khối lượng về null; điện áp ra eo tỉ lệ gia tốc a.",
        "Figure 17.7 · A simplified rotational servo-accelerometer. Case acceleration produces an inertial force "
        "F on the sensitive mass, deflecting it from null; the pick-off senses the angle, the signal is amplified, "
        "demodulated and filtered to a current proportional to motion, which drives a coil in a magnetic field to "
        "restore the mass; output voltage eo is proportional to acceleration a.",
        "Khối lượng quán tính → cảm biến → khuếch đại/giải điều biến/lọc → cuộn từ phục hồi về null, vòng phản "
        "hồi sinh eo ∝ a.",
        "Inertial mass → pick-off → amplifier/demod/filter → torquing coil restoring to null, a feedback loop "
        "giving eo ∝ a.")


# ---------------------------------------------------------------- 17.8
def fig_17_8():
    o = [_defs()]
    # compression PZT: mass on top, crystal discs in compression, base
    o.append('<rect x="200" y="200" width="200" height="20" fill="none" stroke="%s" stroke-width="2"/>' % E)  # base
    o.append(_lbl(200, 232, "đế (base)", "ts"))
    # crystal discs
    o.append('<rect x="255" y="150" width="90" height="20" fill="%s"/>' % "#9ca3af")
    o.append('<rect x="255" y="120" width="90" height="20" fill="%s"/>' % "#9ca3af")
    o.append(_lbl(350, 142, "tinh thể áp điện (PZT)", "ts"))
    # preload + mass
    o.append('<rect x="270" y="80" width="60" height="40" fill="#e5e7eb" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(300, 104, "khối lượng", "tb", "middle"))
    o.append('<line x1="300" y1="80" x2="300" y2="40" stroke="%s" stroke-width="1.4"/>' % E)
    o.append(_lbl(300, 34, "tải trước (preload)", "tb", "middle"))
    # force arrow
    o.append(_arr(300, 200, 300, 168, G))
    o.append(_lbl(312, 188, "F = m·a", "tb"))
    return _fig(
        svg(680, 250, "".join(o), "Cảm biến gia tốc áp điện kiểu nén"),
        "Hình 17.8 · Cảm biến gia tốc áp điện kiểu nén (compression type). Tinh thể luôn ở trạng thái nén, bởi "
        "khối lượng hoặc khối lượng và lò xo tải trước. Gia tốc làm biến dạng tinh thể, sinh tín hiệu điện tỉ lệ. "
        "Nhỏ gọn, dùng phổ biến, nhưng kém ở tần số thấp.",
        "Figure 17.8 · A compression-type piezoelectric accelerometer. The crystals are always in compression, "
        "held by a mass or a mass-and-spring preload. Acceleration deforms the crystal, producing a proportional "
        "electric signal. Small and widely used, but poor at low frequencies.",
        "Khối lượng tải trước ép lên chồng tinh thể PZT nằm trên đế; mũi tên lực F = m·a chỉ biến dạng tinh thể.",
        "A preload mass compresses a stack of PZT crystals on a base; the force arrow F = m·a shows crystal "
        "deformation.")


# ---------------------------------------------------------------- 17.9
def fig_17_9():
    o = [_defs()]
    o.append('<rect x="100" y="40" width="500" height="200" fill="none" stroke="%s" stroke-width="1.2"/>' % E)
    o.append(_lbl(600, 44, "tần số", "ts"))
    o.append(_lbl(40, 70, "độ lợi", "ts"))
    # flat then resonance peak
    pts = []
    for i in range(0, 401, 4):
        x = 100 + i
        t = i / 400.0
        # flat to 0.7 then peak near resonance at ~0.85
        if t < 0.6:
            y = 90
        else:
            y = 90 - 60 * _m.exp(-((t - 0.85) ** 2) / 0.004)
        pts.append((x, y))
    d = "M" + " L".join("%s %s" % p for p in pts)
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2"/>' % (d, G))
    o.append(_lbl(150, 84, "phần tuyến tính", "ts"))
    o.append(_lbl(470, 54, "cộng hưởng tinh thể PZT", "ts"))
    o.append(_lbl(330, 232, "tần số trên bị giới hạn bởi cộng hưởng; góc pha không đổi đến tần số cộng hưởng", "tb"))
    return _fig(
        svg(680, 250, "".join(o), "Đáp ứng tần số của cảm biến gia tốc áp điện điển hình"),
        "Hình 17.9 · Đáp ứng tần số của cảm biến gia tốc áp điện điển hình. Đo lường thường giới hạn trong phần "
        "tuyến tính của đường đáp ứng. Tần số trên của cảm biến bị giới hạn bởi cộng hưởng của tinh thể PZT; góc "
        "pha không đổi đến tần số cộng hưởng.",
        "Figure 17.9 · Frequency response of a typical piezoelectric accelerometer. Measurements are confined to "
        "the linear portion of the response. The upper frequency is limited by the resonance of the PZT crystal; "
        "the phase angle is constant up to the resonance frequency.",
        "Đường đáp ứng phẳng rồi vọt lên đỉnh cộng hưởng tại tần số cao; phần đo dùng đoạn tuyến tính trước cộng "
        "hưởng.",
        "A response curve flat then peaking at the PZT resonance; measurements use the linear portion before "
        "resonance.")


# ---------------------------------------------------------------- 17.10
def fig_17_10():
    o = [_defs()]
    # inertial beam with strain gages top/bottom
    o.append('<rect x="120" y="140" width="360" height="22" fill="#e5e7eb" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(120, 134, "phần quán tính (inertial member)", "ts"))
    # gages on top and bottom
    o.append('<rect x="200" y="120" width="40" height="14" fill="%s" stroke="%s" stroke-width="1"/>' % ("#fcd34d", E))
    o.append('<rect x="280" y="164" width="40" height="14" fill="%s" stroke="%s" stroke-width="1"/>' % ("#fcd34d", E))
    o.append(_lbl(200, 112, "lưới kéo (tension)", "ts"))
    o.append(_lbl(280, 192, "lưới nén (compression)", "ts"))
    # anchors
    o.append('<rect x="110" y="120" width="12" height="62" fill="%s"/>' % "#374151")
    o.append(_lbl(70, 158, "đế cố định", "ts", "end"))
    # vibration arrow
    o.append(_arr(500, 100, 500, 170, G))
    o.append(_lbl(506, 138, "rung", "ts"))
    return _fig(
        svg(680, 220, "".join(o), "Dán các phần tử áp điện và trở trở lên hệ quán tính"),
        "Hình 17.10 · Dán các phần tử áp điện và trở trở (piezoresistive) lên một hệ quán tính. Khi phần tử quán "
        "tính rung, biến dạng của các lưới kéo và nén làm thay đổi điện trở, được cảm biến và xử lý tiếp. Cảm biến "
        "dựa trên PZT đặc biệt hữu ích ở tần số trung bình–cao.",
        "Figure 17.10 · Bonding of piezoelectric and piezoresistive elements onto an inertial system. As the "
        "inertial member vibrates, deformation of the tension and compression gages changes the resistance, which "
        "is picked up and processed. PZT-based accelerometers are especially useful in mid- to high-frequency "
        "applications.",
        "Phần tử quán tính có lưới áp trở dán trên và dưới; khi rung, lưới kéo/nén đổi điện trở.",
        "An inertial member with piezoresistive gages bonded top and bottom; vibration deforms the gages, "
        "changing resistance.")


# ---------------------------------------------------------------- 17.11
def fig_17_11():
    o = [_defs()]
    # differential capacitance: seismic mass between two fixed electrodes
    o.append('<rect x="260" y="100" width="80" height="60" fill="#e5e7eb" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(300, 138, "khối M", "tb", "middle"))
    # springs to base
    o.append('<line x1="260" y1="130" x2="200" y2="130" stroke="%s" stroke-width="1.4"/>' % E)
    o.append('<line x1="340" y1="130" x2="400" y2="130" stroke="%s" stroke-width="1.4"/>' % E)
    for k in range(3):
        o.append('<path d="M200 %d q 12 -8 24 0 q 12 8 24 0" fill="none" stroke="%s" stroke-width="1"/>' % (126 + k * 8, E))
        o.append('<path d="M400 %d q -12 -8 -24 0 q -12 8 -24 0" fill="none" stroke="%s" stroke-width="1"/>' % (126 + k * 8, E))
    # fixed electrodes
    o.append('<rect x="170" y="108" width="16" height="44" fill="%s"/>' % "#6b7280")
    o.append('<rect x="414" y="108" width="16" height="44" fill="%s"/>' % "#6b7280")
    o.append(_lbl(150, 100, "điện cực cố định (C₁)", "ts", "end"))
    o.append(_lbl(450, 100, "điện cực cố định (C₂)", "ts"))
    o.append(_lbl(300, 196, "khối làm phần tử động của mạch dao động; gia tốc → tần số thay đổi", "tb", "middle"))
    return _fig(
        svg(680, 220, "".join(o), "Cảm biến gia tốc vi phân dung kháng điển hình"),
        "Hình 17.11 · Cảm biến gia tốc vi phân dung kháng (differential-capacitance) điển hình. Khối lượng địa "
        "chấn làm phần tử động của một mạch dao động, được đỡ bởi dầm đàn hồi chuyển động song song. Khi gia tốc, "
        "tần số dao động thay đổi qua lại giá trị danh định tuỳ hướng gia tốc; hoặc khối được giữ bởi lực phản "
        "hồi tĩnh điện để đơn giản cơ khí.",
        "Figure 17.11 · A typical differential-capacitance accelerometer. The seismic mass is the moving element "
        "of an oscillator, supported by a parallel-motion beam. Under acceleration the oscillation frequency "
        "varies above and below nominal; in a variant the mass is held by an electrostatic-feedback force for "
        "mechanical simplicity.",
        "Khối lượng M ở giữa hai điện cực cố định tạo hai tụ C₁, C₂; lò xo đỡ khối, gia tốc làm tần số mạch đổi.",
        "Seismic mass M between two fixed electrodes forming C₁ and C₂; springs support the mass, acceleration "
        "shifts the circuit frequency.")


# ---------------------------------------------------------------- 17.12
def fig_17_12():
    o = [_defs()]
    # diaphragm with spiral flexures between two electrodes, holes
    o.append('<rect x="180" y="70" width="240" height="20" fill="%s"/>' % "#6b7280")
    o.append(_lbl(180, 62, "điện cực trên", "ts"))
    o.append('<rect x="180" y="170" width="240" height="20" fill="%s"/>' % "#6b7280")
    o.append(_lbl(180, 202, "điện cực dưới", "ts"))
    # diaphragm element in middle
    o.append('<rect x="220" y="115" width="160" height="20" fill="#e5e7eb" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(300, 129, "màng (seismic element)", "tb", "middle"))
    # holes + spiral flexure hint
    for hx in (240, 280, 320, 360):
        o.append('<circle cx="%d" cy="125" r="4" fill="%s" stroke="%s" stroke-width="0.8"/>' % (hx, P, E))
    o.append(_lbl(300, 158, "lỗ thoát khí → giảm chấn màng ép (squeeze film)", "tb", "middle"))
    return _fig(
        svg(680, 230, "".join(o), "Cảm biến gia tốc dung kháng kiểu màng"),
        "Hình 17.12 · Cảm biến gia tốc dung kháng kiểu màng (diaphragm). Phần tử địa chấn được đệm giữa hai điện "
        "cực; chuyển động của khối giữa các điện cực đẩy không khí song song bề mặt qua các lỗ, tạo giảm chấn màng "
        "ép (squeeze film). Vì độ nhớt khí ít nhạy nhiệt hơn dầu, tỉ số giảm chấn 0,7 hầu như không đổi quá 15%.",
        "Figure 17.12 · A diaphragm-type capacitive accelerometer. The seismic element is cushioned between the "
        "electrodes; its motion pumps air parallel to the surface through holes, giving squeeze-film damping. Air "
        "viscosity is less temperature-sensitive than oil, so the desired 0.7 damping ratio changes by less than "
        "15%.",
        "Màng nằm giữa điện cực trên/dưới, các lỗ thoát khí tạo giảm chấn màng ép.",
        "A diaphragm between upper and lower electrodes, with holes that let air through for squeeze-film damping.")


# ---------------------------------------------------------------- 17.13
def fig_17_13():
    o = [_defs()]
    o.append('<rect x="100" y="40" width="500" height="200" fill="none" stroke="%s" stroke-width="1.2"/>' % E)
    o.append(_lbl(600, 44, "tỉ số tần số ω₁/ωₙ", "ts"))
    o.append(_lbl(40, 60, "biên độ (x₁−x₂)₀/x₀", "ts"))
    # curve rising to plateau at high frequency ratio
    pts = []
    for i in range(0, 401, 4):
        x = 100 + i
        r = i / 400.0 * 4.0  # ratio 0..4
        y = 220 - 150 * (r ** 2 / _m.sqrt((1 - r ** 2) ** 2 + (2 * 0.7 * r) ** 2))
        if y < 60:
            y = 60
        pts.append((x, y))
    d = "M" + " L".join("%s %s" % p for p in pts)
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2"/>' % (d, G))
    o.append(_lbl(300, 80, "tại c/cc = 0,7 và ω₁/ωₙ > 2: đáp ứng ≈ tuyến tính", "ts"))
    o.append(_lbl(150, 232, "chọn hằng số sao ω₁ ≫ ωₙ (lớn hơn 2); c/cc ≈ 0,7 cho kết quả tối ưu", "tb"))
    return _fig(
        svg(680, 250, "".join(o), "Chuyển động tương đối của một dụng cụ địa chấn điển hình"),
        "Hình 17.13 · Chuyển động tương đối của một dụng cụ địa chấn điển hình. Biên độ ra bằng biên độ vào khi "
        "c/cc = 0,7 và ω₁/ωₙ > 2; ở tỉ số tần số cao, đáp ứng trở thành hàm tuyến tính của vào. Nên chọn tần số "
        "rung lớn hơn hẳn tần số tự nhiên (ví dụ > 2) và c/cc ≈ 0,7.",
        "Figure 17.13 · Displacement of a typical seismic instrument. The output amplitude equals the input "
        "amplitude when c/cc = 0.7 and ω₁/ωₙ > 2; at high frequency ratios the response is essentially linear in "
        "the input. Keep the vibration frequency well above the natural frequency and c/cc ≈ 0.7.",
        "Đường đáp ứng biên độ theo tỉ số tần số, tiến tới mặt phẳng (bằng vào) khi ω₁/ωₙ > 2 và c/cc = 0,7.",
        "An amplitude-ratio curve versus frequency ratio, reaching a plateau (output = input) for ω₁/ωₙ > 2 at "
        "c/cc = 0.7.")


# ---------------------------------------------------------------- 17.14
def fig_17_14():
    o = [_defs()]
    # frame, seismic mass on spring, potentiometer track + wiper
    o.append('<rect x="150" y="50" width="320" height="180" fill="none" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(150, 44, "khung (vibrating frame)", "ts"))
    o.append('<line x1="190" y1="50" x2="190" y2="110" stroke="%s" stroke-width="1.4"/>' % E)
    for k in range(3):
        o.append('<path d="M190 %d q 10 -7 20 0 q 10 7 20 0" fill="none" stroke="%s" stroke-width="1"/>' % (82 + k * 9, E))
    o.append('<rect x="250" y="100" width="64" height="40" fill="#e5e7eb" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(282, 124, "khối M", "tb", "middle"))
    # potentiometer track along bottom
    o.append('<rect x="180" y="190" width="240" height="10" fill="%s"/>' % "#374151")
    o.append(_lbl(180, 216, "biến trở (potentiometer)", "ts"))
    # wiper connects mass to a point on track
    o.append('<line x1="282" y1="140" x2="282" y2="190" stroke="%s" stroke-width="1.6"/>' % G)
    o.append('<circle cx="282" cy="190" r="4" fill="%s" stroke="%s" stroke-width="1.2"/>' % (P, G))
    o.append(_lbl(300, 178, "con quét (wiper)", "ts"))
    return _fig(
        svg(680, 240, "".join(o), "Cảm biến gia tốc kiểu biến trở"),
        "Hình 17.14 · Cảm biến gia tốc kiểu biến trở (potentiometer). Chuyển động tương đối giữa khung và khối "
        "địa chấn được cảm biến bởi một biến trở; con quét gắn với khối lượng. Chúng thường dùng cho gia tốc biến "
        "thiên chậm và rung tần số thấp (< 100 Hz), tỉ số giảm chấn 0,5–0,8 nhờ chất lỏng giảm chấn.",
        "Figure 17.14 · A potentiometer accelerometer. The relative displacement between the frame and the "
        "seismic mass is sensed by a potentiometer, whose wiper is attached to the mass. Used for slow-varying "
        "acceleration and low-frequency vibration (< 100 Hz), with damping ratio 0.5–0.8 from fluid damping.",
        "Khung có khối M treo lò xo, con quét biến trở nối khối M với thanh biến trở ở đáy để đo dịch chuyển tương "
        "đối.",
        "A frame with spring-suspended mass M, a potentiometer wiper linking M to the resistive track at the "
        "base to sense relative displacement.")


# ---------------------------------------------------------------- 17.15
def fig_17_15():
    o = [_defs()]
    # cantilever beam anchored left, mass at right end, strain gages on beam
    o.append('<rect x="120" y="120" width="14" height="80" fill="%s"/>' % "#374151")  # anchor
    o.append(_lbl(80, 158, "đế", "ts", "end"))
    o.append('<rect x="134" y="145" width="260" height="12" fill="#e5e7eb" stroke="%s" stroke-width="1.4"/>' % E)  # beam
    o.append('<rect x="350" y="120" width="50" height="60" fill="#e5e7eb" stroke="%s" stroke-width="1.6"/>' % E)  # mass
    o.append(_lbl(375, 154, "khối M", "tb", "middle"))
    # strain gages on beam (top & bottom)
    o.append('<rect x="200" y="135" width="30" height="10" fill="%s" stroke="%s" stroke-width="1"/>' % ("#fcd34d", E))
    o.append('<rect x="200" y="157" width="30" height="10" fill="%s" stroke="%s" stroke-width="1"/>' % ("#fcd34d", E))
    o.append(_lbl(200, 126, "lưới áp trở", "ts"))
    # viscous damping fill
    o.append('<rect x="120" y="200" width="300" height="40" fill="#cfe3f0" stroke="none" opacity="0.6"/>')
    o.append(_lbl(124, 234, "chất lỏng nhớt giảm chấn (toàn phần)", "ts"))
    return _fig(
        svg(680, 250, "".join(o), "Dụng cụ địa chấn dùng lưới áp trở"),
        "Hình 17.15 · Dụng cụ địa chấn dùng lưới áp trở (strain gage). Khối lượng địa chấn lắp trên dầm cantilever "
        "thay vì lò xo; các lưới áp trở dán hai bên dầm cảm biến biến dạng do rung của khối. Giảm chấn bằng chất "
        "lỏng nhớt lấp đầy vỏ. Tần số tự nhiên khoảng 300 Hz do cần dầm dài đủ chứa lưới.",
        "Figure 17.15 · A strain-gage seismic instrument. The seismic mass is mounted on a cantilever beam rather "
        "than springs; strain gages on each side of the beam sense the strain from the mass vibration. Viscous "
        "liquid filling the housing provides damping. Natural frequency ~300 Hz because the beam must be long "
        "enough for the gages.",
        "Khối M ở đầu dầm cantilever, lưới áp trở dán trên dầm, vỏ đầy chất lỏng nhớt giảm chấn.",
        "Mass M at the end of a cantilever beam, strain gages on the beam, and a viscous-damping fluid filling "
        "the housing.")


# ---------------------------------------------------------------- 17.16
def fig_17_16():
    o = [_defs()]
    # proof mass supported by two vibrating strings
    o.append('<rect x="280" y="100" width="60" height="50" fill="#e5e7eb" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(310, 129, "khối M", "tb", "middle"))
    # two strings to anchors
    o.append('<line x1="240" y1="125" x2="140" y2="125" stroke="%s" stroke-width="2"/>' % E)
    o.append('<line x1="380" y1="125" x2="480" y2="125" stroke="%s" stroke-width="2"/>' % E)
    o.append('<rect x="120" y="115" width="20" height="20" fill="%s"/>' % "#374151")
    o.append('<rect x="480" y="115" width="20" height="20" fill="%s"/>' % "#374151")
    # vibration wiggles on strings
    o.append('<path d="M140 125 q 25 -12 50 0 q 25 12 50 0" fill="none" stroke="%s" stroke-width="1.2" stroke-dasharray="3 2"/>' % S)
    o.append('<path d="M380 125 q 25 -12 50 0 q 25 12 50 0" fill="none" stroke="%s" stroke-width="1.2" stroke-dasharray="3 2"/>' % S)
    o.append(_lbl(300, 80, "gia tốc dọc trục → ứng suất vi sai trên hai dây → đổi tần số f₁, f₂", "tb", "middle"))
    return _fig(
        svg(680, 200, "".join(o), "Cảm biến gia tốc dây rung"),
        "Hình 17.16 · Cảm biến gia tốc dây rung (vibrating string). Khối bằng chứng được đỡ dọc trục bởi hai dây "
        "rung ngang có tiết diện đều, chiều dài và khối lượng bằng nhau. Khi có gia tốc dọc trục cảm biến, hai dây "
        "có ứng suất vi sai làm đổi tần số rung; hiệu f₁² − f₂² tỉ lệ với gia tốc a. Giữ tổng tần số không đổi bằng "
        "servo, hiệu hai tần số tỉ lệ tuyến tính với gia tốc.",
        "Figure 17.16 · A vibrating-string accelerometer. The proof mass is supported longitudinally by two "
        "transversely vibrating strings of equal mass and length. Under axial acceleration a differential tension "
        "exists, changing the frequencies; f₁² − f₂² is proportional to acceleration a. Servoing the sum constant "
        "makes the frequency difference linearly proportional to a.",
        "Khối M đỡ bởi hai dây rung căng ngang, gia tốc làm ứng suất vi sai đổi tần số f₁, f₂ của hai dây.",
        "A proof mass supported by two transverse vibrating strings; axial acceleration induces differential "
        "tension, shifting their frequencies f₁ and f₂.")


# ---------------------------------------------------------------- 17.17
def fig_17_17():
    o = [_defs()]
    # three layers: substrate, structural, sacrificial, then etched
    o.append('<rect x="100" y="170" width="360" height="40" fill="%s"/>' % "#374151")
    o.append(_lbl(100, 162, "substrate (nền)", "ts"))
    o.append('<rect x="140" y="120" width="280" height="30" fill="%s"/>' % "#9ca3af")
    o.append(_lbl(140, 112, "cấu trúc (structural)", "ts"))
    o.append('<rect x="180" y="95" width="200" height="20" fill="%s" stroke="%s" stroke-width="1" stroke-dasharray="4 3"/>' % ("#cbd5e1", E))
    o.append(_lbl(180, 88, "vật hy sinh (sacrificial)", "ts"))
    # arrow down showing etch
    o.append(_arr(470, 110, 470, 200, G))
    o.append(_lbl(478, 150, "ăn mòn\n(hydrofluoric)", "ts"))
    # result: free-standing structure
    o.append('<rect x="560" y="120" width="100" height="30" fill="%s"/>' % "#9ca3af")
    o.append(_lbl(560, 112, "cấu trúc\ntự do", "ts"))
    o.append(_lbl(330, 232, "vi gia công bề mặt: lớp vật hy sinh bị ăn mòn để lại cấu trúc tự do (cách nền ~2 µm)", "tb"))
    return _fig(
        svg(680, 250, "".join(o), "Các bước của vi gia công bề mặt"),
        "Hình 17.17 · Các bước của vi gia công bề mặt (surface micromachining). Cấu trúc ba chiều nhạy gia tốc "
        "được hình thành trên nền và một phần tử hy sinh. Phần tử hy sinh bị ăn mòn (bằng axit hydrofluoric) để "
        "lại cấu trúc tự do. Khoảng cách giữa cấu trúc và nền khoảng 2 µm.",
        "Figure 17.17 · Steps of surface micromachining. The acceleration-sensitive 3-D structure is formed on a "
        "substrate and a sacrificial element; the sacrificial material is etched away (hydrofluoric acid) to leave "
        "a free-standing structure. The spacing to the substrate is about 2 µm.",
        "Ba lớp nền–cấu trúc–vật hy sinh, mũi tên ăn mòn lớp hy sinh, kết quả là cấu trúc tự do trên nền.",
        "Substrate, structural and sacrificial layers; etching the sacrificial layer leaves a free-standing "
        "structure above the substrate.")


# ---------------------------------------------------------------- 17.18
def fig_17_18():
    o = [_defs()]
    # DETF: two beams anchored at both ends, vibrating 180 out of phase
    o.append('<rect x="200" y="100" width="16" height="60" fill="%s"/>' % "#374151")   # left anchor
    o.append('<rect x="464" y="100" width="16" height="60" fill="%s"/>' % "#374151")   # right anchor
    # two beams (top and bottom) between anchors
    o.append('<rect x="216" y="108" width="248" height="12" fill="#e5e7eb" stroke="%s" stroke-width="1.4"/>' % E)
    o.append('<rect x="216" y="148" width="248" height="12" fill="#e5e7eb" stroke="%s" stroke-width="1.4"/>' % E)
    # central mass connecting them
    o.append('<rect x="290" y="108" width="60" height="52" fill="#e5e7eb" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(320, 137, "khối", "tb", "middle"))
    # vibration arrows (180 out of phase)
    o.append(_arr(330, 108, 330, 86, G))
    o.append(_arr(330, 160, 330, 182, G))
    o.append(_lbl(340, 84, "rung lệch pha 180°", "ts"))
    o.append(_lbl(300, 200, "DETF: hai dầm rung triệt tiêu lực phản ứng ở đầu; tần số cộng hưởng đổi theo gia tốc", "tb"))
    return _fig(
        svg(680, 230, "".join(o), "Bộ cảm biến gia tốc dạng nĩa móc hai đầu (DETF)"),
        "Hình 17.18 · Bộ cảm biến gia tốc dạng nĩa móc hai đầu (DETF — double-ended tuning fork). Bộ dao động "
        "ghép năng lượng vào hai dầm để chúng rung ở tần số cộng hưởng, lệch pha 180° để triệt tiêu lực phản ứng "
        "ở đầu dầm. Tần số cộng hưởng của dầm tăng/giảm theo gia tốc; tín hiệu ra là sóng vuông điều tần từ bộ "
        "dao động, giao tiếp số được.",
        "Figure 17.18 · A double-ended tuning fork (DETF) acceleration transducer. An oscillator capacitively "
        "drives two beams at their resonant frequency, 180° out of phase to cancel end reaction forces. The beam "
        "resonant frequency shifts with acceleration; the output is a frequency-modulated square wave for digital "
        "interface.",
        "Hai dầm móc hai đầu, khối ở giữa, mũi tên chỉ rung lệch pha 180°, tần số cộng hưởng đổi theo gia tốc.",
        "Two beams anchored at both ends with a central mass, arrows showing 180° out-of-phase vibration; the "
        "resonant frequency shifts with acceleration.")


# ---------------------------------------------------------------- 17.19
def fig_17_19():
    o = [_defs()]
    # sensor box with main axis + cross axis
    o.append('<rect x="280" y="100" width="120" height="80" fill="#e5e7eb" stroke="%s" stroke-width="1.8"/>' % E)
    o.append(_lbl(340, 145, "cảm biến", "tb", "middle"))
    # main axis (vertical) arrow
    o.append(_arr(340, 100, 340, 40, E))
    o.append(_arr(340, 180, 340, 240, E))
    o.append(_lbl(348, 50, "trục chính (main axis)", "ts"))
    # cross axis (horizontal) arrow
    o.append(_arr(280, 140, 180, 140, G))
    o.append(_arr(400, 140, 500, 140, G))
    o.append(_lbl(170, 132, "trục ngang (cross-axis)", "ts", "end"))
    o.append(_lbl(340, 258, "độ nhạy trục ngang thường &lt; 1%–4% độ nhạy trục chính", "tb", "middle"))
    return _fig(
        svg(680, 280, "".join(o), "Minh hoạ vectơ độ nhạy trục ngang"),
        "Hình 17.19 · Minh hoạ vectơ độ nhạy trục ngang (cross-axis sensitivity). Cảm biến có thể cảm nhận rung "
        "không chỉ dọc trục chính mà cả vuông góc với nó; độ nhạy trục ngang biểu thị bằng % độ nhạy trục chính "
        "và càng thấp càng tốt. Hiệu chuẩn cá nhân phải bảo đảm nhỏ hơn 3%–4%. Đôi khi độ nhạy này dùng để định "
        "hướng lắp đặt đúng.",
        "Figure 17.19 · Vectorial illustration of cross-axis sensitivity. An accelerometer may sense vibration "
        "not only along its main axis but also perpendicular to it; cross-axis sensitivity is expressed as a "
        "percentage of the main-axis sensitivity and should be as low as possible (individual calibration must be "
        "under 3%–4%). Sometimes it is used to set the correct mounting orientation.",
        "Hộp cảm biến với mũi tên trục chính (dọc) và trục ngang (ngang) vuông góc, độ nhạy trục ngang nhỏ hơn "
        "trục chính.",
        "A sensor box with a main-axis arrow (vertical) and a perpendicular cross-axis arrow; cross-axis "
        "sensitivity is a small fraction of the main-axis sensitivity.")


# ---------------------------------------------------------------- 17.20
def fig_17_20():
    o = [_defs()]
    # charge amplifier: transducer capacitor -> charge converter (op-amp) -> Cf -> Eo
    o.append(_box(80, 100, 90, 46, "cảm biến\n(q ∝ a)", E))
    o.append(_arr(170, 123, 210, 123, E))
    o.append(_box(210, 100, 110, 46, "bộ đổi\ntích điện (op-amp)", E))
    o.append(_arr(320, 123, 360, 123, E))
    o.append(_box(360, 100, 90, 46, "điện áp ra\nEo", G, "#fff7ed"))
    # feedback capacitor Cf back to input
    o.append('<path d="M360 123 L360 60 L210 60 L210 100" fill="none" stroke="%s" stroke-width="1.4"/>' % G)
    o.append('<text class="tb" x="285" y="54" text-anchor="middle">Cf (hồi tiếp)</text>')
    o.append(_lbl(240, 178, "tích điện lưu trong Cf → Eo = q/Cf, không phụ thuộc chiều dài cáp", "tb", "middle"))
    return _fig(
        svg(680, 220, "".join(o), "Bộ khuếch đại tích điện điển hình"),
        "Hình 17.20 · Bộ khuếch đại tích điện (charge amplifier) điển hình. Điện tích tỉ lệ gia tốc từ cảm biến "
        "được đổi sang điện áp rồi khuếch đại. Bộ khuếch đại duy trì đầu vào gần 0 V nên như một mạch ngắn với "
        "nguồn; điện tích lưu trong tụ hồi tiếp Cf sinh điện áp Eo = q/Cf. Đáp ứng xấp xỉ hệ bậc nhất; độ lợi độc "
        "lập chiều dài cáp — thuận lợi khi đo rung tần số thấp.",
        "Figure 17.20 · A typical charge amplifier. The charge proportional to acceleration from the transducer "
        "is converted to voltage and amplified. The amplifier holds the input near 0 V, so it looks like a short "
        "to the source; the charge is stored in the feedback capacitor Cf, giving Eo = q/Cf. The response is "
        "approximately first-order and the gain is independent of cable length — useful for low-frequency "
        "vibration.",
        "Cảm biến sinh q → bộ đổi tích điện op-amp → Eo, tụ hồi tiếp Cf đưa điện tích về đầu vào.",
        "Transducer charge q → charge-converter op-amp → output Eo, with feedback capacitor Cf returning charge "
        "to the input.")


# ---------------------------------------------------------------- 17.21
def fig_17_21():
    o = [_defs()]
    # Wheatstone bridge: 4 gages + 2 fixed resistors (shunt calibration)
    cx, cy = 300, 120
    r = 60
    # diamond of 4 gages
    pts = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
    for i, (x, y) in enumerate(pts):
        o.append('<rect x="%d" y="%d" width="40" height="26" fill="#fcd34d" stroke="%s" stroke-width="1.4"/>' % (x - 20, y - 13, E))
        o.append(_lbl(x, y + 4, "R%d" % (i + 1), "tb", "middle"))
    # connect diamond
    dpts = "M" + " L".join("%d %d" % p for p in pts) + " Z"
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="1.4"/>' % (dpts, E))
    # two extra fixed resistors for shunt calibration
    o.append('<rect x="%d" y="%d" width="40" height="26" fill="#e5e7eb" stroke="%s" stroke-width="1.4"/>' % (cx - 20, cy - r - 50, E))
    o.append(_lbl(cx, cy - r - 36, "R5", "tb", "middle"))
    o.append('<rect x="%d" y="%d" width="40" height="26" fill="#e5e7eb" stroke="%s" stroke-width="1.4"/>' % (cx - 20, cy + r + 24, E))
    o.append(_lbl(cx, cy + r + 38, "R6", "tb", "middle"))
    o.append(_lbl(300, 220, "cầu Wheatstone: 4 lưới làm 4 cánh, 2 điện trở cố định R5,R6 để hiệu chuẩn shunt", "tb"))
    return _fig(
        svg(680, 240, "".join(o), "Mạch cầu cho cảm biến áp trở và lưới áp trở"),
        "Hình 17.21 · Mạch cầu cho cảm biến áp trở (piezoresistive) và lưới áp trở (strain gage). Các lưới áp "
        "trở tạo bốn cánh của cầu; hai điện trở cố định thêm vào để cân bằng và chỉnh tinh, cho phép hiệu chuẩn "
        "shunt trong bộ điều kiện tín hiệu. Cách bố trí này giảm ảnh hưởng nhiệt độ.",
        "Figure 17.21 · Bridge circuit for piezoresistive and strain-gage accelerometers. The strain gages form "
        "the four arms of the bridge; two extra fixed resistors permit balancing and fine adjustment, allowing "
        "shunt calibration in the signal conditioner. This arrangement reduces temperature effects.",
        "Cầu Wheatstone kim cương với 4 lưới áp trở (R1–R4) và hai điện trở cố định (R5,R6) để hiệu chuẩn.",
        "A diamond Wheatstone bridge of four strain gages (R1–R4) with two fixed resistors (R5,R6) for shunt "
        "calibration.")


# ---------------------------------------------------------------- 17.22
def fig_17_22():
    o = [_defs()]
    o.append(_box(70, 100, 110, 46, "cảm biến\ngia tốc", E))
    o.append(_arr(180, 123, 220, 123, E))
    o.append(_box(220, 100, 110, 46, "điều kiện\ntín hiệu + A/D", E))
    o.append(_arr(330, 123, 370, 123, E))
    o.append(_box(370, 100, 110, 46, "MCU /\nmáy tính", G, "#fff7ed"))
    o.append(_arr(480, 123, 520, 123, E))
    o.append(_box(520, 100, 90, 46, "ra số", E))
    # power / switching loop note
    o.append(_lbl(300, 60, "nguồn + chuyển mạch tích hợp trong cùng chip (microaccelerometer)", "tb", "middle"))
    o.append(_lbl(300, 190, "thiết bị giao tiếp trực tiếp với DSP hoặc máy tính; một số tích hợp luôn ADC, bộ nhớ", "tb"))
    return _fig(
        svg(680, 230, "".join(o), "Sơ đồ khối cảm biến gia tốc kết hợp MCU"),
        "Hình 17.22 · Sơ đồ khối cảm biến gia tốc kết hợp MCU (vi điều khiển). Mạch điều kiện tín hiệu, chuyển "
        "mạch và nguồn được tích hợp thành một microaccelerometer, giao tiếp trực tiếp với bộ xử lý số hoặc máy "
        "tính. Một số còn tích hợp luôn ADC và bộ nhớ.",
        "Figure 17.22 · Block diagram of an accelerometer combined with an MCU. Signal conditioning, switching "
        "and power-supply circuits are integrated into a microaccelerometer that interfaces directly with a DSP or "
        "computer; some also integrate the ADC and memory.",
        "Khối cảm biến → điều kiện tín hiệu/A-D → MCU → ra số, với nguồn và chuyển mạch tích hợp.",
        "Sensor → signal conditioning/ADC → MCU → digital output, with power and switching integrated on the "
        "same chip.")


# ---------------------------------------------------------------- 17.23
def fig_17_23():
    o = [_defs()]
    o.append(_box(70, 100, 120, 46, "phần tử cảm biến\n+ bộ dao động", E))
    o.append(_arr(190, 123, 230, 123, E))
    o.append(_box(230, 100, 120, 46, "tín hiệu gia tốc\nđiều tần (FM)", E))
    o.append(_arr(350, 123, 390, 123, E))
    o.append(_box(390, 100, 110, 46, "bộ đệm sóng\nvuông (buffer)", G, "#fff7ed"))
    o.append(_arr(500, 123, 540, 123, E))
    o.append(_box(540, 100, 90, 46, "ra số", E))
    o.append(_lbl(300, 60, "hệ thống essentially là bộ dao động điều khiển bằng thạch anh", "tb", "middle"))
    o.append(_lbl(300, 188, "sóng vuông đệm đọc trực tiếp vào thiết bị số — bỏ ADC, giảm nguồn lỗi", "tb"))
    return _fig(
        svg(680, 230, "".join(o), "Sơ đồ bộ điều kiện tín hiệu của microaccelerometer"),
        "Hình 17.23 · Sơ đồ bộ điều kiện tín hiệu của microaccelerometer. Hệ thống về bản chất là một mạch dao "
        "động điều khiển bằng thạch anh; tín hiệu ra của dao động là tín hiệu gia tốc điều tần (FM). Mạch cung "
        "cấp đầu ra sóng vuông có đệm, đọc trực tiếp vào thiết bị số — loại bỏ ADC, một nguồn lỗi chính.",
        "Figure 17.23 · Block diagram of a microaccelerometer signal-conditioning circuit. The system is "
        "essentially a crystal-controlled oscillator whose output is a frequency-modulated acceleration signal. "
        "A buffered square-wave output reads directly into a digital device, eliminating the ADC — a major error "
        "source.",
        "Phần tử cảm biến + dao động → tín hiệu FM → bộ đệm sóng vuông → ra số.",
        "Sensing element + oscillator → FM acceleration signal → buffered square-wave → digital output.")


# expose
FIGS = [fig_17_1, fig_17_2, fig_17_3, fig_17_4, fig_17_5, fig_17_6, fig_17_7, fig_17_8,
        fig_17_9, fig_17_10, fig_17_11, fig_17_12, fig_17_13, fig_17_14, fig_17_15,
        fig_17_16, fig_17_17, fig_17_18, fig_17_19, fig_17_20, fig_17_21, fig_17_22, fig_17_23]


def fig(n):
    return FIGS[n - 1]()
