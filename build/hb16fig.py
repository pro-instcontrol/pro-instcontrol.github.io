# -*- coding: utf-8 -*-
"""Vector redraws of the figures in the CRC Measurement Handbook, Ch. 16
(Velocity Measurement). Sixteen schematic figures: position-time (16.1), LVT
transducers (16.2), Michelson interferometer (16.3), VISAR (16.4), seismic
instrument (16.5), dc/ac tach-generators (16.6, 16.7), moving-conductor EMF
(16.8), magnetic sensor curve (16.9), slotted-disk opto (16.10), Hall-effect
gear-tooth sensor (16.11, 16.12), Wiegand wire (16.13), quartz tuning fork
(16.14), MHD rate sensor (16.15), differenced accelerometers (16.16). Each
function returns (svg, caption_vi, caption_en, aria_vi, aria_en).
"""
import math
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
            '<marker id="ah16" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
            '<path d="M0,0 L7,3 L0,6 Z" fill="%s"/></marker>'
            '<marker id="ah16g" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
            '<path d="M0,0 L7,3 L0,6 Z" fill="%s"/></marker>'
            '<marker id="ah16w" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
            '<path d="M0,0 L7,3 L0,6 Z" fill="%s"/></marker></defs>' % (E, G, "#ffffff"))


def _arr(x1, y1, x2, y2, col=E, marker="ah16", sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, marker))


# ---------------------------------------------------------------- 16.1
def fig_16_1():
    o = [_defs()]
    # axes
    o.append('<line x1="90" y1="232" x2="610" y2="232" stroke="%s" stroke-width="1.4"/>' % E)
    o.append('<line x1="90" y1="232" x2="90" y2="46" stroke="%s" stroke-width="1.4"/>' % E)
    o.append(_lbl(616, 236, "thời gian t", "ts"))
    o.append(_lbl(70, 40, "vị trí y", "ts"))
    # monotonic rising position-time curve
    pts = [(90, 220), (180, 200), (260, 168), (340, 130), (440, 86), (540, 56), (610, 46)]
    d = "M" + " L".join("%s %s" % p for p in pts)
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.2"/>' % (d, G))
    # t1,t2 verticals
    x1, x2 = 260, 440
    y1, y2 = 168, 86
    for x, y, t, yy in ((x1, y1, "t₁", "y₁"), (x2, y2, "t₂", "y₂")):
        o.append('<line x1="%s" y1="%s" x2="%s" y2="232" stroke="%s" stroke-width="1" stroke-dasharray="4 3"/>' % (_f(x), _f(y), _f(x), S))
        o.append('<circle cx="%s" cy="%s" r="4" fill="%s" stroke="%s" stroke-width="1.4"/>' % (x, y, P, E))
        o.append(_lbl(x, 248, t, "tb", "middle"))
        o.append(_lbl(76, y + 4, yy, "tb", "end"))
    # secant chord between the two points = average velocity
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.4" stroke-dasharray="6 3"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), E))
    # V labels near the points (slope interpretation)
    o.append(_lbl(x1 - 4, y1 - 12, "V₁", "tb", "end"))
    o.append(_lbl(x2 + 6, y2 - 12, "V₂", "tb"))
    o.append(_lbl(345, 130, "Δy / Δt = v_tb", "ts", "middle"))
    o.append(_lbl(360, 262, "Hình 16.1 · Hàm vị trí–thời gian của một vật chuyển động trên đường thẳng", "ts", "middle"))
    return _fig(
        svg(680, 280, "".join(o), "Đồ thị vị trí theo thời gian của vật chuyển động thẳng"),
        "Hình 16.1 · Hàm vị trí–thời gian y(t) của một vật chuyển động trên đường thẳng. Vận tốc trung bình "
        "trong khoảng t₁–t₂ là v_tb = (y₂ − y₁)/(t₂ − t₁), bằng độ dốc của dây cung (đường gạch). Khi khoảng "
        "thời gian thu nhỏ, v_tb trở thành vận tốc tức thời V_y = dy/dt, tức độ dốc của tiếp tuyến với đường "
        "cong vị trí–thời gian.",
        "Figure 16.1 · The position–time function y(t) of an object moving along a straight path. The average "
        "speed over t₁–t₂ is v_avg = (y₂ − y₁)/(t₂ − t₁), the slope of the secant (dashed line). As the interval "
        "shrinks, v_avg becomes the instantaneous velocity V_y = dy/dt, the slope of the tangent to the curve.",
        "Đồ thị với trục hoành thời gian và trục tung vị trí; một đường cong tăng đơn điệu, hai điểm (t₁,y₁) và "
        "(t₂,y₂) nối bởi dây cung gạch thể hiện vận tốc trung bình.",
        "A graph with time on the horizontal axis and position on the vertical; a monotonically rising curve with "
        "two points (t₁,y₁) and (t₂,y₂) joined by a dashed secant representing average velocity.")


# ---------------------------------------------------------------- 16.2
def fig_16_2():
    o = [_defs()]
    # panel (a) Moving Coil Type
    o.append(_lbl(175, 36, "(a) kiểu cuộn dây chuyển động (moving coil)", "tb", "middle"))
    # magnet poles top/bottom, coil in gap, lead eo
    o.append('<rect x="110" y="60" width="130" height="22" fill="%s"/>' % "#6b7280")   # N pole block
    o.append('<rect x="110" y="178" width="130" height="22" fill="%s"/>' % "#374151")   # S pole block
    o.append(_lbl(120, 54, "N", "tb"))
    o.append(_lbl(120, 204, "S", "tb"))
    o.append('<rect x="150" y="92" width="50" height="66" fill="none" stroke="%s" stroke-width="2"/>' % E)  # coil form
    # coil windings
    for k in range(5):
        yy = 98 + k * 12
        o.append('<line x1="150" y1="%d" x2="200" y2="%d" stroke="%s" stroke-width="1.2"/>' % (yy, yy, G))
    o.append(_lbl(150, 86, "cuộn dây (coil)", "ts"))
    o.append(_lbl(150, 176, "lõi cuộn (coil form)", "ts"))
    o.append(_arr(200, 125, 250, 125, E))   # output lead
    o.append(_lbl(254, 129, "eo", "tb"))
    o.append(_lbl(110, 230, "nam châm vĩnh cửu (permanent magnet)", "ts"))
    # panel (b) Moving Magnet Type
    o.append(_lbl(495, 36, "(b) kiểu nam châm chuyển động (moving magnet)", "tb", "middle"))
    o.append('<rect x="430" y="92" width="34" height="66" fill="%s"/>' % "#6b7280")   # N
    o.append('<rect x="500" y="92" width="34" height="66" fill="%s"/>' % "#374151")   # S
    o.append(_lbl(440, 86, "N", "tb"))
    o.append(_lbl(510, 86, "S", "tb"))
    # coil fixed around, leads to eo
    o.append('<rect x="450" y="70" width="64" height="110" fill="none" stroke="%s" stroke-width="1.6" stroke-dasharray="4 3"/>' % S)
    for k in range(6):
        yy = 84 + k * 16
        o.append('<line x1="450" y1="%d" x2="514" y2="%d" stroke="%s" stroke-width="1"/>' % (yy, yy, S))
    o.append(_lbl(460, 64, "cuộn dây cố định", "ts"))
    o.append(_arr(514, 125, 560, 125, E))
    o.append(_lbl(564, 129, "eo", "tb"))
    # relation
    o.append(_lbl(350, 262, "cảm ứng điện áp: e_i ∝ B · L · V", "tb", "middle"))
    return _fig(
        svg(680, 280, "".join(o), "Cảm biến vận tốc kiểu máy phát tuyến tính (LVT)"),
        "Hình 16.2 · Cảm biến vận tốc tuyến tính (LVT). (a) Kiểu cuộn dây chuyển động: cuộn dây cắt từ thông của "
        "nam châm vĩnh cửu, sinh điện áp e_o. (b) Kiểu nam châm chuyển động: nam châm trượt trong cuộn dây cố "
        "định. Cả hai đều tuân hệ thức e_i ∝ B·L·V (công thức 16.4).",
        "Figure 16.2 · Linear velocity transducers (LVTs). (a) Moving-coil type: a coil cuts the magnetic flux "
        "of a permanent magnet, inducing e_o. (b) Moving-magnet type: the magnet slides inside a fixed coil. Both "
        "obey e_i ∝ B·L·V (Eq. 16.4).",
        "Hai bảng: (a) cuộn dây trong khe từ của nam châm vĩnh cửu, đầu ra eo; (b) nam châm N–S trượt trong "
        "cuộn dây cố định, đầu ra eo; phía dưới ghi e_i ∝ B·L·V.",
        "Two panels: (a) a coil in the gap of a permanent magnet with output eo; (b) an N–S magnet sliding inside "
        "a fixed coil, output eo; below, e_i ∝ B·L·V.")


# ---------------------------------------------------------------- 16.3
def fig_16_3():
    o = [_defs()]
    # extended light source (left)
    o.append('<rect x="50" y="116" width="40" height="28" fill="none" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(45, 162, "nguồn sáng\nmở rộng", "ts"))
    # 45 degree beamsplitter
    o.append('<rect x="180" y="116" width="28" height="28" fill="#e5e7eb" stroke="%s" stroke-width="1.4"/>' % E)
    o.append('<line x1="180" y1="144" x2="208" y2="116" stroke="%s" stroke-width="1.2"/>' % S)
    o.append(_lbl(214, 150, "gương mỏng\nphủ bạc 45°", "ts"))
    # beam from source to splitter
    o.append(_arr(90, 130, 180, 130, E))
    # upward arm to M1
    o.append(_arr(194, 116, 194, 56, E))
    o.append('<rect x="180" y="40" width="28" height="16" fill="%s"/>' % "#374151")  # M1
    o.append(_lbl(214, 50, "M₁", "tb"))
    # rightward arm through compensating plate C to M2
    o.append(_arr(208, 130, 330, 130, E))
    o.append('<rect x="330" y="120" width="10" height="20" fill="#cbd5e1" stroke="%s" stroke-width="1"/>' % S)  # C
    o.append(_lbl(300, 158, "tấm bù C", "ts", "middle"))
    o.append(_arr(340, 130, 470, 130, E))
    o.append('<rect x="470" y="116" width="16" height="28" fill="%s"/>' % "#374151")  # M2
    o.append(_lbl(492, 150, "M₂", "tb"))
    # recombined beam to eye (down-left from splitter)
    o.append(_arr(194, 144, 150, 210, G))
    o.append('<circle cx="146" cy="214" r="10" fill="%s" stroke="%s" stroke-width="1.4"/>' % (P, E))
    o.append(_lbl(130, 238, "Mắt (hoặc\nđầu dò khác)", "ts"))
    return _fig(
        svg(680, 270, "".join(o), "Sơ đồ giao thoa kế Michelson"),
        "Hình 16.3 · Các bộ phận cơ bản của giao thoa kế Michelson. Chùm đơn sắc từ nguồn sáng mở rộng được tấm "
        "gương mỏng phủ bạc ở 45° chia làm hai: một chùm hướng lên gương M₁, một chùm xuyên tấm bù C tới gương "
        "M₂. Hai chùm phản xạ hội tụ ở mắt, tạo vân sáng–tối; tần số chuyển sáng–tối tỉ lệ với vận tốc của bề "
        "mặt chuyển động. Tấm bù C có cùng kích thước và hướng với gương 45° để hai nhánh có đường truyền trong "
        "thủy tinh bằng nhau khi dùng ánh sáng trắng.",
        "Figure 16.3 · The basic components of a Michelson interferometer. A monochromatic beam from an extended "
        "source is split by a thin 45° half-silvered mirror: one arm goes up to mirror M₁, the other passes the "
        "compensating plate C to mirror M₂. The reflected beams recombine at the eye, producing bright–dark "
        "fringes whose rate is proportional to the velocity of the moving surface. Plate C matches the 45° "
        "mirror so the two glass paths are equal for white light.",
        "Sơ đồ với nguồn sáng trái, gương chẻ tia 45° ở giữa, nhánh lên gương M₁, nhánh ngang qua tấm bù C tới "
        "gương M₂, và chùm hội tụ về mắt; ghi chú tấm bù C.",
        "Schematic with a source at left, a 45° beam splitter in the centre, an up-arm to mirror M₁, a horizontal "
        "arm through compensating plate C to mirror M₂, and the recombined beam to the eye; plate C is noted.")


# ---------------------------------------------------------------- 16.4
def fig_16_4():
    o = [_defs()]
    # laser source
    o.append('<rect x="60" y="120" width="64" height="34" fill="none" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(60, 172, "nguồn laser", "ts"))
    # fiber to a probe on the target, return fiber to detector
    o.append(_arr(124, 137, 250, 137, E))
    o.append('<circle cx="270" cy="137" r="14" fill="#e5e7eb" stroke="%s" stroke-width="1.4"/>' % E)
    o.append(_lbl(270, 166, "đầu dò\n(probe)", "ts", "middle"))
    # target
    o.append('<rect x="330" y="112" width="80" height="50" fill="none" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(330, 178, "bề mặt thử\n(target)", "ts"))
    # return fiber to photodiode
    o.append(_arr(410, 137, 540, 137, G))
    o.append('<rect x="540" y="120" width="64" height="34" fill="none" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(540, 172, "quang điện\n(photodiode)", "ts"))
    # motion arrow on target
    o.append(_arr(370, 90, 410, 90, G))
    o.append(_lbl(374, 84, "vận tốc V", "ts"))
    # fiber labels
    o.append(_lbl(150, 128, "sợi quang tới", "ts"))
    o.append(_lbl(440, 128, "sợi quang về", "ts"))
    return _fig(
        svg(680, 230, "".join(o), "Sơ đồ thử nghiệm VISAR dùng sợi quang"),
        "Hình 16.4 · Sơ đồ hệ VISAR dùng linh kiện sợi quang (Valyn). Ánh sáng laser được dẫn bằng sợi quang "
        "tới đầu dò chiếu vào bề mặt thử chuyển động; ánh sáng tán xạ/phản xạ theo vân giao thoa được thu về "
        "qua sợi quang thứ hai tới quang điện. Tốc độ góc của vân tỉ lệ với vận tốc bề mặt. Sợi quang giúp đưa "
        "ánh sáng tới/thoát khỏi thử nghiệm va chạm mà không gây nguy hiểm chùm tia.",
        "Figure 16.4 · A VISAR test setup using fiber-optic components (Valyn). Laser light is carried by fiber "
        "to a probe illuminating the moving target; the interferometric return is collected by a second fiber to "
        "a photodiode. The fringe rate is proportional to the surface velocity. Fiber delivery minimises laser "
        "beam hazards in a shock experiment.",
        "Khối nguồn laser nối sợi quang tới đầu dò trên bề mặt thử, rồi sợi quang về quang điện; mũi tên vận tốc "
        "V trên bề mặt thử.",
        "A laser block feeds a fiber-optic probe on the moving target and a return fiber to a photodiode; a "
        "velocity arrow V is shown on the target.")


# ---------------------------------------------------------------- 16.5
def fig_16_5():
    o = [_defs()]
    # instrument housing
    o.append('<rect x="220" y="50" width="200" height="190" fill="none" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(224, 44, "vỏ thiết bị (housing)", "ts"))
    # springs supporting seismic mass M (top)
    o.append('<line x1="270" y1="50" x2="270" y2="92" stroke="%s" stroke-width="1.4"/>' % E)
    o.append('<line x1="370" y1="50" x2="370" y2="92" stroke="%s" stroke-width="1.4"/>' % E)
    for x, y in ((260, 60), (280, 60), (360, 60), (380, 60)):
        o.append('<path d="M%s 52 q 6 8 12 0 q 6 8 12 0" fill="none" stroke="%s" stroke-width="1"/>' % (x, E))
    # seismic mass M
    o.append('<rect x="285" y="92" width="70" height="44" fill="#e5e7eb" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(320, 119, "khối lượng M", "tb", "middle"))
    o.append(_lbl(320, 148, "chuyển động khối Sm", "ts", "middle"))
    # dashpot (viscous damping)
    o.append('<rect x="300" y="136" width="40" height="60" fill="none" stroke="%s" stroke-width="1.4"/>' % S)
    o.append('<line x1="320" y1="136" x2="320" y2="196" stroke="%s" stroke-width="1" stroke-dasharray="3 2"/>' % S)
    o.append(_lbl(346, 170, "giảm chấn x", "ts"))
    # secondary transducer -> output
    o.append('<rect x="285" y="200" width="70" height="26" fill="none" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(320, 218, "cảm biến phụ", "tb", "middle"))
    o.append(_arr(355, 213, 410, 213, E))
    o.append(_lbl(414, 217, "đầu ra đã biến đổi", "ts"))
    # base / member whose motion is measured
    o.append('<line x1="120" y1="240" x2="560" y2="240" stroke="%s" stroke-width="2"/>' % E)
    o.append(_lbl(120, 258, "vật mang chuyển động Ss = SsO·cos ωt", "ts"))
    o.append(_arr(320, 240, 320, 240, E))  # anchor to base
    return _fig(
        svg(680, 280, "".join(o), "Thiết bị đo chuyển động kiểu địa chấn (seismic)"),
        "Hình 16.5 · Thiết bị đo chuyển động kiểu địa chấn. Khối lượng địa chấn M được treo bởi lò xo (hằng số "
        "k) và giảm chấn nhớt (hệ số x) trong vỏ thiết bị gắn vào bề mặt cần đo (Ss = SsO·cos ωt). Chuyển động "
        "tương đối Sm của khối so với vỏ được cảm biến phụ đo, cho đầu ra tỉ lệ gia tốc (trong dải tần quy định) "
        "— gọi là gia tốc kế. Lấy tích phân gia tốc theo thời gian (công thức 16.3) thu được hàm vận tốc–thời "
        "gian.",
        "Figure 16.5 · A seismic motion-measuring instrument. The seismic mass M is suspended by springs "
        "(constant k) and a viscous dashpot (coefficient x) inside a housing fixed to the surface whose motion "
        "is wanted (Ss = SsO·cos ωt). The relative motion Sm of the mass is read by a secondary transducer, "
        "giving an output proportional to acceleration over a specified band — an accelerometer. Integrating "
        "acceleration over time (Eq. 16.3) yields the velocity–time function.",
        "Vỏ thiết bị chứa lò xo treo khối lượng M, giảm chấn nhớt, cảm biến phụ dẫn tới đầu ra; đáy là vật mang "
        "chuyển động Ss = SsO·cos ωt.",
        "An instrument housing holding springs suspending seismic mass M, a viscous dashpot, and a secondary "
        "transducer feeding the output; the base is the moving member Ss = SsO·cos ωt.")


# ---------------------------------------------------------------- 16.6
def fig_16_6():
    o = [_defs()]
    # DC tach: output eo is a DC level proportional to speed wi
    # frame
    o.append('<rect x="120" y="60" width="440" height="150" fill="none" stroke="%s" stroke-width="1.4"/>' % E)
    o.append(_lbl(126, 54, "máy phát tacho DC từ tính vĩnh cửu", "ts"))
    # time axis
    o.append('<line x1="140" y1="190" x2="540" y2="190" stroke="%s" stroke-width="1.2"/>' % E)
    o.append(_lbl(544, 194, "thời gian", "ts"))
    # two DC levels for two speeds
    o.append('<line x1="150" y1="150" x2="530" y2="150" stroke="%s" stroke-width="2.2"/>' % G)   # low speed
    o.append('<line x1="150" y1="100" x2="530" y2="100" stroke="%s" stroke-width="2.2"/>' % E)   # high speed
    o.append(_lbl(150, 96, "eo (tốc độ cao)", "tb"))
    o.append(_lbl(150, 146, "eo (tốc độ thấp)", "tb"))
    o.append(_lbl(420, 176, "mức điện áp ∝ tốc độ quay wi", "ts"))
    return _fig(
        svg(680, 240, "".join(o), "Máy phát tacho DC: điện áp tỉ lệ tốc độ"),
        "Hình 16.6 · Máy phát tacho DC từ tính vĩnh cửu. Điện áp ra eo là một mức một chiều có độ lớn tỉ lệ "
        "với tốc độ quay wi của trục vào: tốc độ càng cao, mức eo càng lớn. Chiều quay không đổi được phản ánh "
        "bởi cực tính của điện áp.",
        "Figure 16.6 · A permanent-magnet dc tach-generator. The output voltage eo is a dc level whose "
        "magnitude is proportional to the rotational speed wi of the input shaft: the higher the speed, the "
        "larger the eo level. Direction of rotation is reflected in the polarity of the voltage.",
        "Khung đồ thị với trục thời gian và hai mức điện áp một chiều eo (thấp và cao) ứng với hai tốc độ wi.",
        "A graph frame with a time axis and two dc voltage levels eo (low and high) corresponding to two shaft "
        "speeds wi.")


# ---------------------------------------------------------------- 16.7
def fig_16_7():
    o = [_defs()]
    o.append('<rect x="120" y="50" width="440" height="170" fill="none" stroke="%s" stroke-width="1.4"/>' % E)
    o.append(_lbl(126, 44, "máy phát tacho xoay chiều (ac)", "ts"))
    o.append('<line x1="140" y1="210" x2="540" y2="210" stroke="%s" stroke-width="1.2"/>' % E)
    o.append(_lbl(544, 214, "thời gian", "ts"))
    # two sine waves of different frequency at y=130
    for (f, col, lab, ph) in ((0.045, G, "eo (tốc độ thấp)", 0), (0.085, E, "eo (tốc độ cao)", 0)):
        pts = []
        for i in range(0, 401, 4):
            x = 140 + i
            y = 130 - 55 * _m.sin(ph + f * i)
            pts.append((x, y))
        d = "M" + " L".join("%s %s" % p for p in pts)
        o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2"/>' % (d, col))
    o.append(_lbl(150, 80, "eo (tốc độ cao)", "tb"))
    o.append(_lbl(150, 200, "eo (tốc độ thấp)", "tb"))
    # opposite-direction 180 deg phase note
    o.append(_lbl(300, 232, "tần số ∝ tốc độ; hai chiều quay lệch pha 180°", "tb", "middle"))
    return _fig(
        svg(680, 250, "".join(o), "Máy phát tacho xoay chiều: tần số tỉ lệ tốc độ"),
        "Hình 16.7 · Máy phát tacho xoay chiều. Điện áp ra là xoay chiều có tần số tỉ lệ với tốc độ quay; tốc "
        "độ càng cao, tần số càng lớn (hai đường hình sin). Chiều quay được xác định bởi pha của tín hiệu: hai "
        "chiều ngược nhau lệch pha 180°.",
        "Figure 16.7 · An ac tach-generator. The output is an ac voltage whose frequency is proportional to "
        "rotational speed; the higher the speed, the higher the frequency (two sine waves shown). Direction is "
        "given by the phase: opposite directions are 180° out of phase.",
        "Đồ thị hai sóng hình sin tần số khác nhau ứng với hai tốc độ, ghi chú lệch pha 180° giữa hai chiều quay.",
        "A plot of two sine waves of different frequency for two speeds, noting a 180° phase shift between the "
        "two directions of rotation.")


# ---------------------------------------------------------------- 16.8
def fig_16_8():
    o = [_defs()]
    # N and S poles top/bottom, conductor moving with velocity f, current through R
    o.append('<rect x="150" y="40" width="200" height="22" fill="%s"/>' % "#6b7280")
    o.append('<rect x="150" y="200" width="200" height="22" fill="%s"/>' % "#374151")
    o.append(_lbl(160, 34, "N", "tb"))
    o.append(_lbl(160, 226, "S", "tb"))
    # moving conductor (horizontal rod) at mid
    o.append('<rect x="200" y="118" width="100" height="14" fill="none" stroke="%s" stroke-width="2"/>' % E)
    o.append(_lbl(245, 110, "dây dẫn chuyển động", "tb", "middle"))
    # velocity arrow f to the right
    o.append(_arr(300, 125, 360, 125, G))
    o.append(_lbl(364, 129, "vận tốc f", "ts"))
    # terminal a (left) and b (right) and resistor R closing the loop below
    o.append('<circle cx="200" cy="125" r="4" fill="%s" stroke="%s" stroke-width="1.2"/>' % (P, E))
    o.append('<circle cx="300" cy="125" r="4" fill="%s" stroke="%s" stroke-width="1.2"/>' % (P, E))
    o.append(_lbl(190, 140, "a", "tb", "end"))
    o.append(_lbl(308, 140, "b", "tb"))
    # down leads to resistor R
    o.append('<line x1="200" y1="125" x2="200" y2="170" stroke="%s" stroke-width="1.4"/>' % E)
    o.append('<line x1="300" y1="125" x2="300" y2="170" stroke="%s" stroke-width="1.4"/>' % E)
    o.append('<rect x="190" y="170" width="120" height="16" fill="none" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(250, 192, "điện trở R", "tb", "middle"))
    # induced EMF arrow along the loop
    o.append(_arr(200, 110, 200, 70, E))
    o.append(_lbl(176, 90, "suất điện động e sinh ra", "ts", "end"))
    return _fig(
        svg(680, 240, "".join(o), "Suất điện động cảm ứng trong dây dẫn chuyển động"),
        "Hình 16.8 · Suất điện động cảm ứng trong dây dẫn chuyển động. Một dây dẫn (thanh a–b) trượt với vận "
        "tốc f trong từ trường giữa cực N và S, sinh suất điện động e được đưa ra qua điện trở R (định luật "
        "Faraday). Tốc độ dây càng lớn, e càng lớn; chiều e tuân quy tắc bàn tay phải.",
        "Figure 16.8 · Electromotive force generated in a moving conductor. A conductor (rod a–b) slides with "
        "velocity f through the field between N and S poles, inducing an EMF e delivered through resistor R "
        "(Faraday's law). The faster the conductor, the larger e; the sense of e follows the right-hand rule.",
        "Cực N trên, S dưới, thanh dây dẫn chuyển động với vận tốc f, mạch kín qua điện trở R; mũi tên e chỉ "
        "suất điện động cảm ứng.",
        "N pole above, S below, a moving conductor rod at velocity f, the loop closed through resistor R; an "
        "arrow e marks the induced EMF.")


# ---------------------------------------------------------------- 16.9
def fig_16_9():
    o = [_defs()]
    o.append('<rect x="110" y="50" width="470" height="180" fill="none" stroke="%s" stroke-width="1.4"/>' % E)
    o.append('<line x1="130" y1="210" x2="560" y2="210" stroke="%s" stroke-width="1.2"/>' % E)
    o.append('<line x1="130" y1="210" x2="130" y2="60" stroke="%s" stroke-width="1.2"/>' % E)
    o.append(_lbl(564, 214, "tốc độ bề mặt (in/s)", "ts"))
    o.append(_lbl(86, 64, "điện áp ra", "ts", "end"))
    # roughly linear rising curve
    pts = [(130, 205), (200, 188), (270, 166), (340, 138), (420, 104), (500, 72), (560, 64)]
    d = "M" + " L".join("%s %s" % p for p in pts)
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.2"/>' % (d, G))
    # a couple of operating points
    for x, y, t in ((270, 166, "A"), (500, 72, "B")):
        o.append('<circle cx="%s" cy="%s" r="3.5" fill="%s" stroke="%s" stroke-width="1.2"/>' % (x, y, P, E))
        o.append(_lbl(x + 6, y - 6, t, "tb"))
    o.append(_lbl(330, 232, "cảm biến từ: điện áp ra ∝ tốc độ bề mặt", "tb", "middle"))
    return _fig(
        svg(680, 250, "".join(o), "Đặc tuyến cảm biến tốc độ từ"),
        "Hình 16.9 · Đặc tuyến điện áp ra theo tốc độ bề mặt của cảm biến tốc độ từ (Smith Systems). Khi cảm "
        "biến từ đặt gần một mục sắt (ví dụ răng bánh răng trên trục quay), tần số điện áp ra tỉ lệ với tốc độ "
        "quay; tín hiệu qua bộ chuyển tần số–điện áp cho điện áp tỉ lệ vận tốc. Đặc tuyến gần tuyến tính trong "
        "dải làm việc.",
        "Figure 16.9 · Output voltage versus surface speed for a magnetic speed sensor (Smith Systems). When the "
        "magnetic sensor is near a ferrous target (e.g. gear teeth on a rotating shaft), the output frequency "
        "is proportional to rotational speed; a frequency-to-voltage converter gives a velocity-proportional "
        "voltage. The characteristic is nearly linear over the operating range.",
        "Đồ thị điện áp ra (trục tung) theo tốc độ bề mặt (trục hoành), đường đặc tuyến dốc lên gần tuyến tính, "
        "hai điểm A, B minh hoạ.",
        "A graph of output voltage (vertical) versus surface speed (horizontal), a near-linear rising "
        "characteristic with two illustrative points A and B.")


# ---------------------------------------------------------------- 16.10
def fig_16_10():
    o = [_defs()]
    # light source - slotted disk - detector
    o.append('<rect x="90" y="70" width="44" height="30" fill="none" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(80, 64, "nguồn sáng", "ts"))
    o.append(_arr(134, 85, 200, 85, G))   # beam
    o.append(_lbl(150, 78, "ánh sáng", "ts"))
    # rotating disk with slots
    o.append('<circle cx="270" cy="85" r="48" fill="none" stroke="%s" stroke-width="2"/>' % E)
    for k in range(8):
        a = k * _m.pi / 4.0
        x1 = 270 + 30 * _m.cos(a); y1 = 85 + 30 * _m.sin(a)
        x2 = 270 + 48 * _m.cos(a); y2 = 85 + 48 * _m.sin(a)
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="3"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), E))
    o.append(_lbl(270, 148, "đĩa có rãnh (quay)", "tb", "middle"))
    o.append(_arr(318, 85, 380, 85, G))
    o.append('<rect x="380" y="70" width="44" height="30" fill="none" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(388, 64, "đầu dò sáng", "ts"))
    # pulse train below
    o.append('<line x1="120" y1="200" x2="560" y2="200" stroke="%s" stroke-width="1.2"/>' % E)
    o.append(_lbl(564, 204, "t", "ts"))
    for k in range(6):
        x0 = 140 + k * 64
        o.append('<path d="M%s 200 L%s 175 L%s 200" fill="none" stroke="%s" stroke-width="1.6"/>' % (_f(x0), _f(x0 + 18), _f(x0 + 36), E))
    o.append(_lbl(300, 222, "xung ra: một xung mỗi vòng quay", "tb", "middle"))
    return _fig(
        svg(680, 240, "".join(o), "Cảm biến quang dùng đĩa có rãnh"),
        "Hình 16.10 · Cảm biến vận tốc góc bằng phương pháp quang học. Một đĩa có rãnh đặt trên trục quay; LED "
        "và diode quang ghép cặp. Mỗi rãnh cho ánh sáng qua, đầu dò sinh một xung. Tần số xung tỉ lệ với vận "
        "tốc góc — một xung cho mỗi vòng quay (hay mỗi rãnh).",
        "Figure 16.10 · An optical angular-velocity sensor using a slotted disk. An LED and a photodiode are "
        "paired across a slotted disk on the shaft. Each slot lets light through, producing one pulse. The pulse "
        "rate is proportional to angular velocity — one pulse per revolution (or per slot).",
        "Nguồn sáng trái, đĩa có rãnh ở giữa, đầu dò sáng phải; phía dưới là chuỗi xung tỉ lệ tốc độ quay.",
        "A light source on the left, a slotted disk in the middle, a light detector on the right; below, a pulse "
        "train whose rate is proportional to the rotational speed.")


# ---------------------------------------------------------------- 16.11
def fig_16_11():
    o = [_defs()]
    # gear with a few teeth at right, Hall sensor package at left near a tooth
    cx, cy, R = 470, 140, 70
    o.append('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-width="2"/>' % (_f(cx), _f(cy), _f(R), E))
    for k in range(12):
        a = k * _m.pi / 6.0
        x1 = cx + (R - 8) * _m.cos(a); y1 = cy + (R - 8) * _m.sin(a)
        x2 = cx + (R + 10) * _m.cos(a); y2 = cy + (R + 10) * _m.sin(a)
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="3"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), E))
    o.append(_lbl(470, 224, "bánh răng (mục sắt)", "tb", "middle"))
    # Hall sensor package (shell + magnet + IC) near the gear
    o.append('<rect x="180" y="120" width="90" height="40" fill="#e5e7eb" stroke="%s" stroke-width="1.6"/>' % E)
    o.append('<rect x="214" y="132" width="22" height="16" fill="%s"/>' % "#6b7280")  # magnet
    o.append('<circle cx="248" cy="140" r="6" fill="%s" stroke="%s" stroke-width="1.2"/>' % (P, E))  # IC
    o.append(_lbl(180, 112, "cảm biến hiệu ứng Hall (vỏ + nam châm + IC)", "ts"))
    o.append(_arr(270, 140, 392, 140, G))
    o.append(_lbl(300, 132, "từ trường tới răng", "ts"))
    return _fig(
        svg(680, 250, "".join(o), "Cảm biến răng bánh răng hiệu ứng Hall"),
        "Hình 16.11 · Cảm biến răng bánh răng hiệu ứng Hall (Allegro ATS632LSC). Một vỏ nhựa chịu nhiệt giữ "
        "một nam châm samarium–coban, một IC hiệu ứng Hall tự hiệu chuẩn và bộ điều áp. Khi răng bánh răng đi "
        "qua, từ trường biến thiên làm IC đổi mức đầu ra, sinh xung tỉ lệ tốc độ trục — ứng dụng điển hình là "
        "cảm biến tốc độ bánh xe cho hệ phanh chống bó cứng (ABS).",
        "Figure 16.11 · A Hall-effect gear-tooth sensor (Allegro ATS632LSC). A high-temperature plastic shell "
        "holds a samarium–cobalt magnet, a self-calibrating Hall-effect IC, and a voltage regulator. As gear "
        "teeth pass, the varying field switches the IC output, producing pulses proportional to shaft speed — "
        "a typical application is the wheel-speed sensor for antilock brakes.",
        "Bánh răng phải, cảm biến hiệu ứng Hall (vỏ, nam châm, IC) trái, mũi tên từ trường tới răng.",
        "A gear at right, a Hall-effect sensor package (shell, magnet, IC) at left, with an arrow showing the "
        "field reaching the tooth.")


# ---------------------------------------------------------------- 16.12
def fig_16_12():
    o = [_defs()]
    # block flow: gear tooth -> field -> Hall IC -> amp -> output
    def box(x, y, w, h, t):
        o.append('<rect x="%s" y="%s" width="%s" height="%s" fill="none" stroke="%s" stroke-width="1.6"/>' % (_f(x), _f(y), _f(w), _f(h), E))
        o.append(_lbl(x + w / 2.0, y + h / 2.0 + 4, t, "tb", "middle"))
    box(80, 110, 90, 44, "răng bánh răng")
    box(210, 110, 90, 44, "từ trường biến thiên")
    box(340, 110, 90, 44, "IC hiệu ứng Hall")
    box(470, 110, 90, 44, "khuếch đại")
    o.append(_arr(170, 132, 210, 132, E))
    o.append(_arr(300, 132, 340, 132, E))
    o.append(_arr(430, 132, 470, 132, E))
    o.append(_arr(560, 132, 610, 132, G))
    o.append(_lbl(566, 126, "ra", "tb"))
    o.append(_lbl(330, 178, "sơ đồ mạch cảm biến răng hiệu ứng Hall", "tb", "middle"))
    return _fig(
        svg(680, 210, "".join(o), "Sơ đồ mạch cảm biến răng hiệu ứng Hall"),
        "Hình 16.12 · Sơ đồ mạch cảm biến răng bánh răng hiệu ứng Hall. Răng bánh răng sinh từ trường biến "
        "thiên tới IC hiệu ứng Hall; IC chuyển thành xung, qua khuếch đại cho tín hiệu ra tỉ lệ tốc độ. Cảm "
        "biến tự hiệu chuẩn nên bù được nhiệt độ và độ lệch lắp đặt.",
        "Figure 16.12 · Circuit diagram of a Hall-effect gear-tooth sensor. The gear tooth produces a varying "
        "field at the Hall IC; the IC converts it to pulses, which an amplifier shapes into a speed-proportional "
        "output. Self-calibration compensates for temperature and mounting offset.",
        "Chuỗi khối: răng bánh răng → từ trường biến thiên → IC hiệu ứng Hall → khuếch đại → ra.",
        "A block chain: gear tooth → varying field → Hall IC → amplifier → output.")


# ---------------------------------------------------------------- 16.13
def fig_16_13():
    o = [_defs()]
    # Wiegand wire (short rod) with sensing coil, two small magnets on sides
    o.append('<rect x="250" y="120" width="120" height="14" fill="%s"/>' % "#9ca3af")  # wire
    o.append(_lbl(250, 110, "dây Wiegand (sắt từ)", "ts"))
    # coil around it
    for k in range(6):
        x = 262 + k * 16
        o.append('<ellipse cx="%s" cy="127" rx="9" ry="20" fill="none" stroke="%s" stroke-width="1.2"/>' % (_f(x), S))
    o.append(_lbl(300, 158, "cuộn cảm biến", "ts", "middle"))
    # small magnets on both sides
    o.append(_lbl(180, 110, "nam châm nhỏ (trái)", "ts", "end"))
    o.append(_arr(210, 127, 250, 127, G))
    o.append(_lbl(440, 110, "nam châm nhỏ (phải)", "ts"))
    o.append(_arr(450, 127, 410, 127, G))
    # arrow of reversal
    o.append(_arr(250, 160, 370, 160, E))
    o.append(_lbl(300, 176, "đảo cực từ đột ngột → xung Wiegand", "tb", "middle"))
    return _fig(
        svg(680, 210, "".join(o), "Cảm biến hiệu ứng Wiegand"),
        "Hình 16.13 · Cảm biến hiệu ứng Wiegand. Dây sắt từ được gia công đặc biệt, khi gặp từ trường ngoài "
        "đủ mạnh sẽ đảo cực từ đột ngột, cảm ứng một xung điện áp sắc nét (~10 µs) trong cuộn cảm biến. Không "
        "cần nguồn cấp, hai dây, không tiếp xúc — thích hợp tachymetry và đếm vòng.",
        "Figure 16.13 · A Wiegand-effect sensor. A specially processed ferromagnetic wire, exposed to a strong "
        "enough alternating field, suddenly reverses its magnetisation and induces a sharp voltage pulse "
        "(~10 µs) in the sensing coil. No external power, two-wire, non-contact — suited to tachometry and shaft "
        "encoding.",
        "Dây Wiegand giữa, cuộn cảm biến quấn quanh, hai nam châm nhỏ hai bên gây đảo cực từ; mũi tên chỉ xung "
        "Wiegand.",
        "A Wiegand wire in the centre, a sensing coil wound around it, two small magnets on the sides causing "
        "the sudden reversal; an arrow marks the Wiegand pulse.")


# ---------------------------------------------------------------- 16.14
def fig_16_14():
    o = [_defs()]
    # support block
    o.append('<rect x="300" y="190" width="80" height="20" fill="%s"/>' % "#374151")
    o.append(_lbl(300, 224, "giá đỡ (support)", "ts"))
    # tuning fork: two tines going up
    base_y = 190
    o.append('<rect x="320" y="120" width="14" height="70" fill="none" stroke="%s" stroke-width="2"/>' % E)
    o.append('<rect x="346" y="120" width="14" height="70" fill="none" stroke="%s" stroke-width="2"/>' % E)
    # drive tines (active) arrows toward/away
    o.append(_arr(327, 120, 327, 96, G))
    o.append(_arr(353, 120, 353, 96, G))
    o.append(_lbl(300, 96, "chân truyền động (drive)", "ts", "end"))
    # pickup tines (sensing) slightly offset, moving in/out of plane
    o.append('<path d="M320 120 q -22 -10 0 -28" fill="none" stroke="%s" stroke-width="1.4" stroke-dasharray="4 3"/>' % S)
    o.append('<path d="M360 120 q 22 -10 0 -28" fill="none" stroke="%s" stroke-width="1.4" stroke-dasharray="4 3"/>' % S)
    o.append(_lbl(360, 84, "chân thu (pickup)", "ts"))
    # Coriolis force arrows (perpendicular to plane)
    o.append(_arr(327, 100, 327, 80, E))
    o.append(_lbl(250, 84, "lực Coriolis F = 2m·Ω × Vr", "ts", "end"))
    return _fig(
        svg(680, 250, "".join(o), "Nĩa thạch anh rung dùng hiệu ứng Coriolis"),
        "Hình 16.14 · Nĩa thạch anh vi cơ dùng hiệu ứng Coriolis để đo vận tốc góc (GyroChip™). Hai chân truyền "
        "động được kích dao động về/ra với biên độ không đổi. Khi cảm biến quay quanh trục dọc, lực Coriolis "
        "F = 2m·Ω × Vr tác dụng vuông góc, làm các chân thu dao động trong mặt phẳng; tín hiệu sau giải điều "
        "biến là một điện áp một chiều tỉ lệ tốc độ quay. Chỉ cảm nhận được thành phần quay quanh trục đối xứng "
        "nên đo được tốc độ bằng không thực sự.",
        "Figure 16.14 · A micromachined quartz tuning fork using the Coriolis effect to sense angular velocity "
        "(GyroChip™). Drive tines oscillate toward and away at constant amplitude. When the sensor rotates about "
        "its longitudinal axis, a Coriolis force F = 2m·Ω × Vr acts perpendicular, driving the pickup tines out "
        "of plane; the demodulated signal is a dc voltage proportional to the rate. It senses only rotation "
        "about the symmetry axis, so it can truly detect a zero rate.",
        "Nĩa thạch anh với hai chân truyền động (mũi tên lên) và hai chân thu (đường gạch), lực Coriolis vuông "
        "góc với mặt nĩa, giá đỡ ở đáy.",
        "A quartz tuning fork with drive tines (up arrows) and pickup tines (dashed), a Coriolis force "
        "perpendicular to the fork plane, and a support block at the base.")


# ---------------------------------------------------------------- 16.15
def fig_16_15():
    o = [_defs()]
    # circular MHD chamber with magnet on outer case, conductive fluid, electrodes for E
    cx, cy, R = 300, 140, 90
    o.append('<circle cx="%s" cy="%s" r="%s" fill="#eef2f7" stroke="%s" stroke-width="2"/>' % (_f(cx), _f(cy), _f(R), E))
    # magnet on outer case (top)
    o.append('<rect x="270" y="36" width="60" height="20" fill="%s"/>' % "#6b7280")
    o.append(_lbl(270, 30, "nam châm vĩnh cửu (trên vỏ)", "ts"))
    # rotating case arrow (U)
    o.append(_arr(380, 140, 430, 140, G))
    o.append(_lbl(384, 134, "U (vỏ quay)", "ts"))
    # conductive fluid relative motion arrow opposite
    o.append(_arr(240, 140, 190, 140, E))
    o.append(_lbl(196, 134, "chất lỏng U", "ts", "end"))
    # magnetic field B downward in gap
    o.append(_arr(300, 60, 300, 110, S))
    o.append(_lbl(308, 86, "B", "tb"))
    # electrodes E across conductor
    o.append('<line x1="215" y1="140" x2="385" y2="140" stroke="%s" stroke-width="1" stroke-dasharray="4 3"/>' % S)
    o.append('<circle cx="215" cy="140" r="5" fill="%s" stroke="%s" stroke-width="1.2"/>' % (P, E))
    o.append('<circle cx="385" cy="140" r="5" fill="%s" stroke="%s" stroke-width="1.2"/>' % (P, E))
    o.append(_lbl(206, 158, "E", "tb", "end"))
    o.append(_lbl(390, 158, "E", "tb"))
    o.append(_lbl(300, 250, "cảm biến tốc độ góc từ thuỷ động lực học (MHD)", "tb", "middle"))
    return _fig(
        svg(680, 270, "".join(o), "Cảm biến tốc độ góc MHD"),
        "Hình 16.15 · Cảm biến tốc độ góc từ thuỷ động lực học (MHD). Nam châm gắn trên vỏ sinh từ trường B. "
        "Khi vỏ quay, chất lỏng dẫn điện bên trong theo quán tính đứng yên (theo định luật Newton I), tạo chuyển "
        "động tương đối U giữa từ trường và dòng dẫn. Theo định luật Faraday, điện áp E sinh ra tỉ lệ vận tốc "
        "góc quanh trục tâm. Không đo được vận tốc không đổi (dc); dùng cho dao động 1 Hz–1000 Hz và môi trường "
        "xung kích mạnh.",
        "Figure 16.15 · A magnetohydrodynamic (MHD) angular-rate sensor. A permanent magnet on the case creates "
        "field B. As the case turns, the conductive fluid inside stays put by inertia (Newton I), giving a "
        "relative motion U between field and conductor. By Faraday's law a voltage E is produced proportional to "
        "the angular velocity about the centre axis. It cannot sense a constant (dc) rate; it is used for "
        "oscillations of 1 Hz–1000 Hz and high-shock environments.",
        "Buồng tròn chứa chất lỏng dẫn điện, nam châm trên vỏ sinh B, vỏ quay U, chất lỏng đứng yên, điện áp E "
        "qua hai cực.",
        "A circular chamber of conductive fluid, a magnet on the case giving B, the case turning at U while the "
        "fluid stays still, and voltage E across two electrodes.")


# ---------------------------------------------------------------- 16.16
def fig_16_16():
    o = [_defs()]
    # two accelerometers a1, a2 separated by l, differenced, /l, two integrals -> omega
    def box(x, y, w, h, t):
        o.append('<rect x="%s" y="%s" width="%s" height="%s" fill="none" stroke="%s" stroke-width="1.6"/>' % (_f(x), _f(y), _f(w), _f(h), E))
        o.append(_lbl(x + w / 2.0, y + h / 2.0 + 4, t, "tb", "middle"))
    box(80, 110, 70, 40, "a₁")
    box(80, 180, 70, 40, "a₂")
    o.append(_lbl(60, 130, "cảm biến", "ts", "end"))
    o.append(_lbl(60, 200, "cảm biến", "ts", "end"))
    # minus node
    o.append('<circle cx="210" cy="155" r="16" fill="none" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(206, 160, "−", "tb"))
    o.append(_arr(150, 130, 194, 150, E))
    o.append(_arr(150, 200, 194, 162, E))
    # divide by l
    o.append('<rect x="250" y="135" width="60" height="40" fill="none" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(280, 160, "÷ l", "tb", "middle"))
    o.append(_arr(226, 155, 250, 155, E))
    o.append(_lbl(238, 144, "l", "tb"))
    # two integrals -> omega
    o.append('<rect x="350" y="120" width="60" height="34" fill="none" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(380, 142, "∫", "tb", "middle"))
    o.append('<rect x="350" y="162" width="60" height="34" fill="none" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(380, 184, "∫", "tb", "middle"))
    o.append(_arr(310, 155, 350, 137, E))
    # output omega
    o.append('<rect x="470" y="135" width="80" height="40" fill="none" stroke="%s" stroke-width="1.6"/>' % G)
    o.append(_lbl(510, 160, "ω (tốc độ góc)", "tb", "middle"))
    o.append(_arr(410, 152, 470, 152, G))
    o.append(_lbl(440, 128, "ω = (a₁ − a₂)/l dt", "ts", "middle"))
    return _fig(
        svg(680, 230, "".join(o), "Gia tốc góc bằng cách hiệu hai gia tốc kế"),
        "Hình 16.16 · Xác định gia tốc góc bằng cách hiệu hai gia tốc kế. Hai gia tốc kế a₁, a₂ lắp cách nhau "
        "một khoảng l trên cùng một kết cấu cứng; hiệu (a₁ − a₂) chia cho l cho gia tốc góc, lấy tích phân hai "
        "lần theo thời gian thu được vận tốc góc ω. Phép hiệu loại bỏ thành phần chuyển động tuyến tính. Áp "
        "dụng phổ biến trong thử va đập hành huấn luyện (ATD).",
        "Figure 16.16 · Angular acceleration from differenced accelerometers. Two accelerometers a₁, a₂ are "
        "mounted a distance l apart on a rigid structure; the difference (a₁ − a₂) divided by l gives angular "
        "acceleration, and two time integrations yield the angular velocity ω. Differencing removes the linear "
        "motion component. Commonly applied in anthropomorphic test-device (ATD) crash testing.",
        "Hai hộp a₁, a₂ nối vào nút trừ, chia cho l, qua hai phép tích phân tới đầu ra ω (tốc độ góc).",
        "Two boxes a₁, a₂ feed a minus node, divided by l, through two integrators to the output ω (angular "
        "velocity).")


# expose
FIGS = [fig_16_1, fig_16_2, fig_16_3, fig_16_4, fig_16_5, fig_16_6, fig_16_7, fig_16_8,
        fig_16_9, fig_16_10, fig_16_11, fig_16_12, fig_16_13, fig_16_14, fig_16_15, fig_16_16]


def fig(n):
    return FIGS[n - 1]()
