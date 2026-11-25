# -*- coding: utf-8 -*-
"""Figures 4.1-4.15 for IPC Chapter 4 (Telemetry).

Supplier module ``_a``: pneumatic signalling, cable construction, fibre
optics and the beginning of analog (carrier / AM) telemetry.  Every figure
is a simplified vector redraw of the printed original; all labels stay
inside the 680 x 250 canvas and above y = 232 (the 4.n strip sits at 245).
"""
import math

from ipcfig4_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series,
                            _wavey, make_registry)

FIGS, _reg = make_registry()


# ----------------------------------------------------------------- helpers
def _zig_h(x1, x2, y, n=5, amp=3.2, color=INK):
    """Horizontal zig-zag resistor between two end points."""
    pts = []
    for i in range(2 * n + 1):
        pts.append((x1 + (x2 - x1) * i / float(2 * n),
                    y + (amp if i % 2 else -amp)))
    return _poly(pts, sw=1.1, color=color)


def _zener(x, yb, lab, ytop, ybot):
    """Vertical zener diode: bar with bent ends, triangle below, shunt wire."""
    o = [_line(x, ytop, x, yb - 8, sw=1.0),
         _path("M%d,%d H%d M%d,%d l-5,-4 M%d,%d l5,4"
               % (x - 10, yb - 8, x + 10,
                  x - 10, yb - 8, x + 10, yb - 8)),
         _poly([(x - 7, yb + 6), (x + 7, yb + 6), (x, yb - 6)],
               sw=1.1, color=INK),
         _line(x, yb + 6, x, ybot, sw=1.0),
         T(x + 15, yb + 4, lab, 7.6, anchor="start")]
    return "".join(o)


def _mesh(x, y, w, h):
    """Cross-hatched braid / shield patch (two hatch directions)."""
    return (_rect(x, y, w, h, fill="url(#h6)", sw=1.2)
            + _rect(x, y, w, h, fill="url(#h7)", sw=0))


def _corr_v(x0, y0, y1, amp=2.0, step=2.4, color=GREY):
    """A wavy vertical line, used for corrugated jackets and conduits."""
    pts = [(x0 + amp * math.sin(i * 0.9), y0 + i * step)
           for i in range(int((y1 - y0) / step) + 1)]
    return _poly(pts, sw=0.7, color=color)


def _sine(x0, x1, cy, amp, cycles, phase=0.0, color=BLUE, sw=1.6, n=120):
    pts = []
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / float(n)
        pts.append((x, cy - amp * math.sin(
            2 * math.pi * cycles * (x - x0) / float(x1 - x0) + phase)))
    return _poly(pts, sw=sw, color=color)


def _twist(x0, x1, cy, amp, loops):
    return (_sine(x0, x1, cy, amp, loops, 0.0, BLUE)
            + _sine(x0, x1, cy, amp, loops, math.pi, GREEN))


def _call(label, lx, ly, tx, ty, anchor="middle", size=7.2, color=INK):
    """A short leader arrow plus its text label."""
    return T(lx, ly, label, size, anchor=anchor, color=color) + _ar(lx, ly + 3, tx, ty)


def _led(x, y):
    return (_poly([(x - 6, y - 6), (x - 6, y + 6), (x + 6, y)],
                  fill="#ffffff", sw=1.2, color=RED)
            + _line(x + 7, y - 4, x + 12, y - 8, sw=0.9, color=RED)
            + _line(x + 7, y + 4, x + 12, y + 8, sw=0.9, color=RED))


def _pto(x, y):
    return (_circle(x, y, 7, fill="none", sw=1.1, color=BLUE)
            + _line(x - 8, y + 4, x + 8, y + 4, sw=1.1, color=BLUE)
            + _line(x - 3, y - 7, x + 4, y - 1, sw=1.1, color=BLUE))


def _post(cx, ytop, h, w, core_w, lab):
    """A standing fibre cylinder used for the core/clad size comparison."""
    o = [_rect(cx - w / 2.0, ytop, w, h, fill="#eef3fb", sw=1.2),
         _ellipse(cx, ytop, w / 2.0, min(12.0, w / 4.0), fill="#ffffff", sw=1.2),
         _path("M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f"
               % (cx - w / 2.0, ytop + h, cx, ytop + h + 16,
                  cx + w / 2.0, ytop + h))]
    o.append(_rect(cx - core_w / 2.0, ytop - 22, core_w, 22,
                   fill="#fbfaf7", sw=1.0))
    o.append(_ellipse(cx, ytop - 22, core_w / 2.0, 5, fill="#ffffff", sw=1.0))
    o.append(T(cx, ytop + h + 32, lab, 8.0))
    return "".join(o)


# ---------------------------------------------------------------- 4.1
@_reg
def fig_f01():
    """Fig. 4.1 - pneumatic junction box and field signal tubes."""
    o = [_defs()]
    o.append(_call("Pneumatic junction box", 340, 46, 340, 60))
    o.append(_rect(250, 62, 180, 88, fill="#ffffff", sw=1.4))
    for i, ey in enumerate((78, 96, 114, 132)):
        o.append(_poly([(56, ey + 40), (56, ey + 14), (64, ey + 6),
                        (76, ey), (250, ey)], sw=1.2))
        o.append(_poly([(430, ey), (604, ey), (616, ey + 6),
                        (624, ey + 14), (624, ey + 40)], sw=1.2))
        o.append(_circle(56, ey + 40, 2.4, fill="#ffffff", sw=1.0))
        o.append(_circle(624, ey + 40, 2.4, fill="#ffffff", sw=1.0))
        o.append(_path("M250,%d Q300,%d 350,150" % (ey, ey + 22),
                       sw=0.8, color=GREY, dash="3,3"))
        o.append(_path("M430,%d Q380,%d 350,150" % (ey, ey + 22),
                       sw=0.8, color=GREY, dash="3,3"))
    o.append(_rect(338, 150, 24, 12, fill="#eef3fb", sw=1.2))
    for dx in (-6, -3, 0, 3, 6):
        o.append(_line(350 + dx, 162, 350 + dx, 190, sw=0.9, color=BLUE))
    o.append(_call("Field signal tubes", 120, 194, 76, 172, size=7.0))
    o.append(_call("Field signal tubes", 560, 194, 604, 172, size=7.0))
    o.append(_call("Cable gland", 500, 164, 366, 156, anchor="start", size=7.0))
    o.append(T(340, 204, "Pneumatic cable bundle to be put underground", 7.0))
    o.append(T(340, 220, "To control room", 7.2))
    return _mk(1, o, "Pneumatic junction box",
               "Hộp nối khí nén nhận ống tín hiệu từ hiện trường và bó cáp đi ngầm về phòng điều khiển",
               "Pneumatic junction box collecting field signal tubes and an underground cable bundle",
               "Sơ đồ hộp nối khí nén: bốn ống tín hiệu mỗi bên đi vào hộp qua đầu nối, các đường đứt nét hội tụ về đầu bó cáp ở đáy hộp và bó ống đi ngầm về phòng điều khiển.",
               "Diagram of a pneumatic junction box: four field signal tubes enter from each side through compression fittings, dashed lines inside converge at the cable gland, and a multi-core tube bundle runs underground to the control room.")


# ---------------------------------------------------------------- 4.2
@_reg
def fig_f02():
    """Fig. 4.2 - terminal board, instruments and field junction box."""
    o = [_defs()]
    o.append(T(240, 58, "To individual instrument", 7.6))
    for x in (92, 130, 168, 206, 244, 282):
        o.append(_poly([(x, 140), (x, 90), (x + 10, 82),
                        (x + 22, 90), (x + 22, 140)], sw=1.1))
    o.append(_rect(76, 140, 244, 24, fill="#fbfaf7", sw=1.3))
    o.append(_call("Terminal board", 150, 186, 150, 166))
    o.append(_poly([(500, 96), (516, 84), (626, 84), (610, 96)], sw=1.2))
    o.append(_rect(500, 96, 110, 60, fill="#eef3fb", sw=1.3))
    o.append(_poly([(610, 96), (626, 84), (626, 144), (610, 156)], sw=1.2))
    o.append(T(555, 122, "Field", 7.6))
    o.append(T(555, 136, "junction box", 7.6))
    o.append(_poly([(206, 164), (206, 204), (556, 204), (556, 156)],
                   sw=1.3, color=BLUE))
    o.append(_line(374, 199, 386, 209, sw=1.2))
    o.append(_line(382, 199, 394, 209, sw=1.2))
    o.append(T(380, 222, "Underground routing", 7.2))
    return _mk(2, o, "Terminal board and field junction box",
               "Bảng đầu cuối nối ống đồng tới thiết bị trong phòng và hộp nối hiện trường qua đường đi ngầm",
               "Terminal board linked to instruments and to the field junction box by underground routing",
               "Sơ đồ bảng đầu cuối với các ống đồng hình chữ U dẫn tới từng thiết bị; một đường đi ngầm nối bảng này với hộp nối hiện trường ở bên phải.",
               "Diagram of a terminal board with U-shaped copper tubes leading to individual instruments, joined by an underground route to the field junction box on the right.")


# ---------------------------------------------------------------- 4.3
@_reg
def fig_f03():
    """Fig. 4.3 - zener safety barrier circuit."""
    o = [_defs()]
    o.append(_line(70, 64, 610, 64, sw=1.2))
    o.append(_line(70, 160, 610, 160, sw=1.2))
    for x in (70, 610):
        o.append(_circle(x, 64, 2.6, fill="#ffffff", sw=1.0))
        o.append(_circle(x, 160, 2.6, fill="#ffffff", sw=1.0))
    o.append(_rect(120, 56, 40, 16, fill="#ffffff", sw=1.2))
    o.append(_line(126, 64, 154, 64, sw=1.0))
    o.append(T(140, 46, "Fuse", 7.4))
    o.append(_zig_h(160, 240, 64))
    o.append(T(200, 50, "R1", 7.4))
    o.append(_circle(240, 64, 2.4, fill="#ffffff", sw=1.0))
    o.append(_zener(240, 116, "Z1", 64, 160))
    o.append(_zig_h(240, 360, 64))
    o.append(T(300, 50, "R2", 7.4))
    o.append(_circle(360, 64, 2.4, fill="#ffffff", sw=1.0))
    o.append(_zener(360, 116, "Z2", 64, 160))
    o.append(_zig_h(360, 470, 64))
    o.append(T(415, 50, "R3", 7.4))
    o.append(_line(226, 160, 254, 160, sw=1.0))
    o.append(_line(230, 165, 250, 165, sw=1.0))
    o.append(_line(234, 170, 246, 170, sw=1.0))
    o.append(T(120, 192, "Control room end", 7.8, anchor="start"))
    o.append(T(560, 192, "Hazardous area", 7.8, anchor="end"))
    return _mk(3, o, "Zener safety barrier",
               "Rào chắn an toàn zener gồm cầu chì, ba điện trở và hai diode zener nối đất",
               "Zener safety barrier with a fuse, three resistors and two zener diodes to ground",
               "Sơ đồ mạch rào chắn an toàn: cầu chì và các điện trở R1, R2, R3 nằm trên đường dẫn, diode zener Z1 và Z2 nối xuống đất để ngăn điện áp cao từ phòng điều khiển đi tới khu vực nguy hiểm.",
               "Circuit of a zener safety barrier: a fuse and resistors R1, R2, R3 lie along the upper line while zener diodes Z1 and Z2 shunt to ground, preventing high voltage from the control room reaching the hazardous area.")


# ---------------------------------------------------------------- 4.4
@_reg
def fig_f04():
    """Fig. 4.4 - unshielded twisted pair (UTP)."""
    o = [_defs()]
    o.append(_rect(90, 78, 150, 56, fill="#fbfaf7", sw=1.3))
    for x in range(102, 239, 14):
        o.append(_corr_v(x, 80, 132))
    o.append(_twist(240, 610, 106, 14, 4.0))
    o.append(_call("Flexible conduit", 165, 158, 165, 134, size=7.2))
    o.append(_call("Twisted wire (UTP)", 470, 158, 470, 120, size=7.2))
    return _mk(4, o, "Unshielded twisted pair cable",
               "Cáp xoắn đôi không che chắn UTP gồm ống dẫn mềm và hai dây xoắn",
               "Unshielded twisted pair (UTP) with a flexible conduit and a twisted wire pair",
               "Sơ đồ cáp UTP: ống dẫn mềm dạng ống gờ ở bên trái, hai dây đồng được xoắn thành hình xoắn ốc liên tục ở bên phải.",
               "Diagram of UTP cable: a corrugated flexible conduit on the left and two insulated copper wires twisted into a continuous helix on the right.")


# ---------------------------------------------------------------- 4.5
@_reg
def fig_f05():
    """Fig. 4.5 - shielded twisted pair (STP)."""
    o = [_defs()]
    o.append(_rect(80, 78, 148, 56, fill="#fbfaf7", sw=1.3))
    for x in range(92, 227, 14):
        o.append(_corr_v(x, 80, 132))
    o.append(_poly([(228, 88), (300, 96), (300, 116), (228, 124)],
                   fill="url(#h6)", sw=1.2))
    o.append(_poly([(228, 88), (300, 96), (300, 116), (228, 124)],
                   fill="url(#h7)", sw=0))
    o.append(_twist(300, 610, 106, 14, 3.5))
    o.append(_call("Flexible conduit", 150, 158, 150, 134, size=7.2))
    o.append(_call("Shield", 264, 158, 264, 122, size=7.2))
    o.append(_call("STP", 500, 158, 500, 120, size=7.2))
    return _mk(5, o, "Shielded twisted pair cable",
               "Cáp xoắn đôi có che chắn STP gồm ống dẫn mềm, lớp che chắn và hai dây xoắn",
               "Shielded twisted pair (STP) with a flexible conduit, a shield layer and a twisted wire pair",
               "Sơ đồ cáp STP: ống dẫn mềm, lớp che chắn kim loại bao quanh cặp dây và hai dây đồng xoắn đôi dẫn tín hiệu ở bên phải.",
               "Diagram of STP cable: a flexible conduit, a metallic shield surrounding the pair, and two twisted copper signal wires extending to the right.")


# ---------------------------------------------------------------- 4.6
@_reg
def fig_f06():
    """Fig. 4.6 - complete structure of a coaxial cable."""
    o = [_defs()]
    o.append(_rect(180, 86, 420, 48, fill="#fbfaf7", sw=1.4))
    o.append(_line(60, 110, 600, 110, sw=2.8, color=RED))
    o.append(_line(120, 101, 330, 101, sw=1.0, color=GREY))
    o.append(_line(120, 119, 330, 119, sw=1.0, color=GREY))
    o.append(_mesh(330, 94, 110, 32))
    o.append(_call("Braiding made of copper mesh", 385, 66, 385, 94, size=7.2))
    o.append(_call("Single copper conductor", 95, 158, 100, 112, size=7.2))
    o.append(_call("Teflon insulation", 250, 158, 250, 119, size=7.2))
    o.append(_call("Thick PVC cover", 540, 158, 540, 134, size=7.2))
    return _mk(6, o, "Coaxial cable construction",
               "Cáp đồng trục với lõi đồng đơn, lớp cách điện teflon, bọc lưới đồng và vỏ PVC dày",
               "Coaxial cable showing a single copper conductor, teflon insulation, copper mesh braid and a thick PVC cover",
               "Sơ đồ cắt cáp đồng trục: dây đồng đơn ở giữa, lớp cách điện teflon, lớp bọc lưới đồng dạng mắt lưới và lớp vỏ PVC dày bên ngoài.",
               "Cutaway of a coaxial cable: a single copper conductor at the centre, teflon insulation, a woven copper mesh braid and a thick outer PVC cover.")


# ---------------------------------------------------------------- 4.7
@_reg
def fig_f07():
    """Fig. 4.7 - twin-axial cable cross-section."""
    o = [_defs()]
    o.append(_rect(60, 80, 90, 64, fill="#fbfaf7", sw=1.3))
    o.append(_mesh(150, 84, 54, 56))
    o.append(_rect(204, 86, 400, 52, fill="#ffffff", sw=1.2))
    o.append(_twist(204, 604, 112, 12, 3.5))
    o.append(_call("Common shield", 177, 66, 177, 84, size=7.2))
    o.append(_call("Twin inner copper conductor", 555, 62, 555, 100, size=7.2))
    o.append(_call("PVC cover", 105, 164, 105, 144, size=7.2))
    o.append(_call("Outer teflon insulation", 404, 164, 404, 138, size=7.2))
    return _mk(7, o, "Twin-axial cable",
               "Cáp hai lõi đồng trục với vỏ PVC, lớp che chắn chung và lớp cách điện teflon",
               "Twin-axial cable with a PVC cover, a common shield, teflon insulation and two inner copper conductors",
               "Sơ đồ cắt cáp hai trục: vỏ PVC, lớp che chắn chung có gờ chéo, lớp cách điện teflon và hai dây đồng bên trong được xoắn cùng nhau.",
               "Cutaway of a twin-axial cable: a PVC cover, a common hatched shield, teflon insulation and two intertwined inner copper conductors.")


# ---------------------------------------------------------------- 4.8
@_reg
def fig_f08():
    """Fig. 4.8 - light ray trapped by total internal reflection."""
    o = [_defs()]
    o.append(_rect(140, 80, 420, 80, fill="#fbfaf7", sw=1.4))
    for x in range(150, 560, 12):
        o.append(_line(x, 82, x, 158, sw=0.5, color=GREY))
    o.append(_poly([(140, 120), (196, 82), (250, 158), (304, 82),
                    (358, 158), (412, 82), (466, 158), (520, 82),
                    (560, 120)], sw=2.0, color=BLUE))
    o.append(T(80, 116, "Light in", 7.8, anchor="end"))
    o.append(_ar(88, 120, 138, 120))
    o.append(_ar(562, 120, 616, 120))
    o.append(T(622, 124, "Light out", 7.8, anchor="start"))
    return _mk(8, o, "Total internal reflection in a fibre",
               "Đường tia sáng phản xạ toàn phần bên trong sợi quang, với đầu vào và đầu ra",
               "Light ray undergoing total internal reflection inside an optical fibre",
               "Sơ đồ sợi quang: tia sáng đi vào từ bên trái, phản xạ nhiều lần giữa hai thành sợi và đi ra ở đầu bên phải.",
               "Diagram of an optical fibre: a ray enters from the left, reflects repeatedly between the fibre walls and exits at the right.")


# ---------------------------------------------------------------- 4.9
@_reg
def fig_f09():
    """Fig. 4.9 - a single fibre with glass core, clad and plastic jacket."""
    o = [_defs()]
    o.append(_line(70, 110, 380, 110, sw=2.6, color=RED))
    o.append(_line(200, 98, 380, 98, sw=1.1, color=GREY))
    o.append(_line(200, 122, 380, 122, sw=1.1, color=GREY))
    o.append(_ellipse(200, 110, 8, 12, fill="#ffffff", sw=1.2))
    o.append(_ellipse(380, 110, 8, 12, fill="#ffffff", sw=1.2))
    o.append(_line(380, 92, 600, 92, sw=1.1, color=GREY))
    o.append(_line(380, 128, 600, 128, sw=1.1, color=GREY))
    for x in range(394, 601, 14):
        o.append(_corr_v(x, 93, 127, amp=2.2))
    o.append(_ellipse(600, 110, 9, 18, fill="#fbfaf7", sw=1.2))
    o.append(_call("Glass core", 120, 70, 140, 107, size=7.4))
    o.append(_call("Clad", 290, 150, 290, 122, size=7.4))
    o.append(_call("Plastic jacket", 500, 150, 500, 128, size=7.4))
    return _mk(9, o, "Single optical fibre",
               "Một sợi quang đơn gồm lõi thủy tinh, lớp bao và vỏ nhựa",
               "A single optical fibre showing the glass core, cladding and plastic jacket",
               "Sơ đồ cắt một sợi quang: lõi thủy tinh mảnh ở giữa, lớp bao quanh lõi và vỏ nhựa có gờ ở bên ngoài.",
               "Cutaway of a single optical fibre: a thin glass core at the centre, a cladding layer around it and a corrugated plastic jacket outside.")


# ---------------------------------------------------------------- 4.10
@_reg
def fig_f10():
    """Fig. 4.10 - three practical core/clad fibre sizes."""
    o = [_defs()]
    o.append(_post(150, 100, 90, 120, 44, "200/230"))
    o.append(_post(350, 126, 64, 76, 20, "62.5/125"))
    o.append(_post(550, 138, 52, 52, 9, "9/125"))
    return _mk(10, o, "Three optical fibre sizes",
               "So sánh ba loại sợi quang theo đường kính lõi và lớp bao: 200/230, 62.5/125 và 9/125",
               "Comparison of three fibre types by core and cladding diameter: 200/230, 62.5/125 and 9/125",
               "Sơ đồ ba loại sợi quang có kích thước giảm dần, với nhãn 200/230, 62.5/125 và 9/125 theo đơn vị micron.",
               "Diagram of three optical fibres of decreasing size, labelled 200/230, 62.5/125 and 9/125 micrometres.")


# ---------------------------------------------------------------- 4.11
@_reg
def fig_f11():
    """Fig. 4.11 - step-index fibre and modal dispersion."""
    o = [_defs()]
    o.append(_line(50, 150, 640, 150, sw=1.0))
    o.append(_poly([(70, 150), (78, 110), (100, 110), (108, 150)],
                   fill="#eef3fb", sw=1.3, color=BLUE))
    o.append(T(88, 92, "In", 7.2))
    o.append(T(88, 103, "pulse", 7.2))
    o.append(_ar(115, 130, 155, 130))
    o.append(_rect(160, 100, 270, 50, fill="#fbfaf7", sw=1.2))
    o.append(T(295, 88, "Optical path inside the core", 7.6))
    o.append(_poly([(160, 148), (215, 104), (270, 148), (325, 104),
                    (380, 148), (430, 104)], sw=1.6, color=BLUE, dash="5,4"))
    o.append(_ar(435, 130, 475, 130))
    o.append(_poly([(480, 150), (500, 148), (515, 138), (528, 118),
                    (540, 106), (552, 118), (565, 138), (580, 148),
                    (600, 150)], fill="#eef3fb", sw=1.3, color=BLUE))
    o.append(T(622, 120, "out", 7.2, anchor="start"))
    o.append(T(622, 131, "pulse", 7.2, anchor="start"))
    o.append(T(295, 178, "Step refractive index fiber", 7.8))
    return _mk(11, o, "Step-index fibre",
               "Sợi quang chỉ số khúc bậc với đường đi gãy trong lõi và xung ra bị trễ",
               "Step-index fibre with a zig-zag ray path in the core and a broadened output pulse",
               "Sơ đồ sợi chỉ số bậc: xung vào dạng hình thang, tia sáng phản xạ dạng đường gãy trong lõi và xung ra dạng đường cong rộng hơn.",
               "Step-index fibre diagram: a trapezoidal input pulse, a zig-zag ray bouncing inside the core, and a broader bell-shaped output pulse.")


# ---------------------------------------------------------------- 4.12
@_reg
def fig_f12():
    """Fig. 4.12 - graded-index fibre and reduced pulse spreading."""
    o = [_defs()]
    o.append(_line(50, 150, 640, 150, sw=1.0))
    o.append(_poly([(70, 150), (78, 110), (100, 110), (108, 150)],
                   fill="#eef3fb", sw=1.3, color=BLUE))
    o.append(T(88, 92, "In", 7.2))
    o.append(T(88, 103, "pulse", 7.2))
    o.append(_ar(115, 130, 155, 130))
    o.append(_rect(160, 100, 270, 50, fill="#fbfaf7", sw=1.2))
    o.append(T(295, 88, "Optical path inside the core", 7.6))
    pts = [(x, 128 + 18 * math.sin(2 * math.pi * (x - 160) / 95.0))
           for x in range(160, 431, 6)]
    o.append(_poly(pts, sw=1.6, color=BLUE, dash="5,4"))
    o.append(_ar(435, 130, 475, 130))
    o.append(_poly([(480, 150), (505, 149), (520, 140), (532, 115),
                    (540, 96), (548, 115), (560, 140), (575, 149),
                    (600, 150)], fill="#eef3fb", sw=1.3, color=BLUE))
    o.append(T(622, 120, "out", 7.2, anchor="start"))
    o.append(T(622, 131, "pulse", 7.2, anchor="start"))
    o.append(T(295, 178, "Graded refractive index fiber", 7.8))
    return _mk(12, o, "Graded-index fibre",
               "Sợi quang chỉ số graded với đường đi cong trong lõi và xung ra hẹp hơn",
               "Graded-index fibre with a curved ray path in the core and a narrower output pulse",
               "Sơ đồ sợi chỉ số graded: xung vào dạng hình thang, tia sáng đi cong dần trong lõi và xung ra hẹp, cao hơn.",
               "Graded-index fibre diagram: a trapezoidal input pulse, a smoothly curved ray path inside the core, and a narrower, taller output pulse.")


# ---------------------------------------------------------------- 4.13
@_reg
def fig_f13():
    """Fig. 4.13 - cross-section of a complete fibre optic cable."""
    o = [_defs()]
    cx, cy = 300, 125
    o.append(_circle(cx, cy, 90, fill="#fbfaf7", sw=1.3))
    o.append(_circle(cx, cy, 80, fill="#eef3fb", sw=1.1))
    o.append(_circle(cx, cy, 70, fill="#f4efe2", sw=1.1))
    for i in range(12):
        a = 2 * math.pi * i / 12.0
        o.append(_circle(cx + 60 * math.cos(a), cy + 60 * math.sin(a),
                         5.5, fill="#ffffff", sw=0.9))
    o.append(_circle(cx, cy, 44, fill="#ffffff", sw=1.2))
    o.append(_circle(cx, cy, 26, fill="#dfe8f2", sw=1.1))
    o.append(_circle(cx, cy, 12, fill="#ffffff", sw=1.1))
    o.append(_circle(cx, cy, 5, fill=BLUE, sw=0))
    o.append(_call("PVC jacket", 130, 58, 240, 60, anchor="end", size=7.2))
    o.append(_call("Kelvar jacket", 118, 100, 222, 100, anchor="end", size=7.2))
    o.append(_call("Resin cover", 125, 140, 232, 140, anchor="end", size=7.2))
    o.append(_call("Protection tube", 442, 42, 330, 93, anchor="start", size=7.2))
    o.append(_call("Cladding", 442, 78, 322, 108, anchor="start", size=7.2))
    o.append(_call("Glass fibre", 442, 112, 311, 121, anchor="start", size=7.2))
    o.append(T(442, 160, "Kelvar rod to provide", 7.2, anchor="start"))
    o.append(T(442, 171, "mechanical strength", 7.2, anchor="start"))
    o.append(_ar(438, 166, 352, 155))
    return _mk(13, o, "Complete fibre optic cable cross-section",
               "Mặt cắt cáp quang hoàn chỉnh với các lớp vỏ, ống bảo vệ, thanh Kelvar và lõi sợi",
               "Cross-section of a complete fibre optic cable with jacket layers, protection tube, Kelvar rods and glass fibre",
               "Sơ đồ mặt cắt tròn cáp quang: từ ngoài vào là vỏ PVC, lớp Kelvar, lớp nhựa thông, vòng thanh Kelvar, ống bảo vệ, lớp bao và sợi thủy tinh ở giữa.",
               "Circular cross-section of a fibre optic cable: from outside inward, a PVC jacket, a Kelvar jacket, a resin cover, a ring of Kelvar rods, a protection tube, cladding and the glass fibre at the centre.")


# ---------------------------------------------------------------- 4.14
@_reg
def fig_f14():
    """Fig. 4.14 - complete opto-electric telemetry system."""
    o = [_defs()]
    o.append(_rect(50, 100, 90, 50, fill="#eef3fb", sw=1.3))
    o.append(T(95, 120, "Measurement", 7.6))
    o.append(T(95, 132, "device", 7.6))
    o.append(_rect(540, 100, 90, 50, fill="#eef3fb", sw=1.3))
    o.append(T(585, 120, "Measurement", 7.6))
    o.append(T(585, 132, "device", 7.6))
    o.append(T(200, 44, "Photo", 7.2))
    o.append(T(200, 55, "transistor", 7.2))
    o.append(_pto(200, 72))
    o.append(_ar(188, 82, 142, 98))
    o.append(_led(200, 160))
    o.append(T(200, 184, "LED", 7.4))
    o.append(T(100, 178, "Electrical signal", 6.8))
    o.append(_ar(142, 150, 188, 158))
    o.append(_led(480, 72))
    o.append(T(480, 44, "LED", 7.4))
    o.append(_ar(538, 98, 492, 82))
    o.append(_pto(480, 160))
    o.append(T(480, 176, "Photo", 7.2))
    o.append(T(480, 187, "transistor", 7.2))
    o.append(T(582, 178, "Electrical signal", 6.8))
    o.append(_ar(492, 158, 538, 150))
    o.append(_line(204, 72, 476, 72, sw=2.0, color=BLUE))
    o.append(_ar(320, 72, 252, 72))
    o.append(_line(204, 160, 476, 160, sw=2.0, color=BLUE))
    o.append(_ar(330, 160, 400, 160))
    o.append(_rect(250, 58, 180, 116, fill="none", sw=1.0,
                   dash="5,4", stroke=GREY))
    o.append(T(340, 116, "Fiber cable", 7.8))
    o.append(T(340, 210, "Optical coupling arrangement", 7.4))
    o.append(_ar(300, 202, 266, 174, color=GREY, sw=1.0))
    o.append(_ar(380, 202, 414, 174, color=GREY, sw=1.0))
    return _mk(14, o, "Opto-electric telemetry system",
               "Hệ thống telemetry quang điện với hai thiết bị đo, LED, phototransistor và hai sợi cáp quang",
               "Opto-electric telemetry link with two measurement devices, LEDs, photo transistors and two fibre cables",
               "Sơ đồ hệ thống đo quang điện: mỗi thiết bị đo có một LED phát và một phototransistor thu; hai sợi cáp quang truyền tín hiệu theo hai hướng ngược nhau.",
               "Diagram of an opto-electric telemetry system: each measurement device has an LED transmitter and a photo transistor receiver, linked by two fibre cables carrying signals in opposite directions.")


# ---------------------------------------------------------------- 4.15
@_reg
def fig_f15():
    """Fig. 4.15 - sinusoidal carrier waveform."""
    o = [_defs()]
    o.append(_line(80, 62, 80, 158, sw=1.2))
    o.append(_line(80, 110, 470, 110, sw=0.9, color=GREY))
    o.append(_sine(82, 460, 110, 28, 7.0, sw=1.8))
    o.append(_ar(562, 110, 470, 110))
    o.append(T(658, 114, "Carrier waveform", 7.8, anchor="end"))
    return _mk(15, o, "Carrier waveform",
               "Dạng sóng mang tần số cao, tín hiệu sinusoidal dùng làm sóng mang cho điều chế",
               "High-frequency carrier waveform, a sinusoidal wave used for modulation",
               "Sơ đồ dạng sóng mang: đường cong sinusoidal tần số cao dao động quanh trục giữa với khoảng bảy chu kỳ.",
               "Carrier waveform diagram: a high-frequency sinusoidal curve oscillating about the centre line with about seven cycles.")
