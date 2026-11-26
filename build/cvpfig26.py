# -*- coding: utf-8 -*-
"""Vector redraws of Figures 26-1..26-4 in Baumann Chapter 26,
*Control Valve Primer*, 5th ed. -- "Valves for Sanitary or Aseptic Service".

Each printed figure is an unlabelled cross-section (26-2 also has a plan
detail).  These modules redraw them as genuinely labelled vector schematics
with bilingual (VI/EN) callouts derived from the chapter text, never as
raster images.  Architecture mirrors `cvpfig24.py` exactly.
"""
from vfig import (BLUE, GREEN, GREY, INK, PAPER, RED, _arrow, _circle, _defs,
                  _fig, _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def T(x, y, s, size=8.2, **kw):
    return _txt(x, y, esc(s), size, **kw)


def _lead(o, x, y, tx, ty, text, size=7.6, color=INK, anchor="end"):
    """A grey leader line plus a bilingual T() label."""
    o.append(_line(x, y, tx, ty, sw=0.9, color=GREY))
    lx = tx - 4 if anchor == "end" else tx + 4
    o.append(T(lx, ty + 2.5, text, size, anchor=anchor, color=color))
    return o


@_reg
def fig_f261():
    """Figure 26-1 -- self-draining angle valve with metal plug (3-A Council)."""
    w, h = 680, 460
    o = [_defs()]
    o.append(T(340, 20, "Van góc tự thoát nước / Self-draining angle valve (3-A design)",
               10.0, color=INK, weight="600"))

    # Centre lines: stem axis (vertical) and inlet axis (horizontal).
    o.append(_line(340, 46, 340, 402, sw=0.9, color=GREY, dash="6,4"))
    o.append(_line(376, 286, 636, 286, sw=0.9, color=GREY, dash="6,4"))

    # Bonnet: sectioned metal with a central stem bore and O-ring seal.
    o.append(_poly([(300, 222), (300, 92), (310, 76), (310, 70),
                    (370, 70), (370, 76), (380, 92), (380, 222)],
                   fill="url(#h6)", sw=1.3, close=True))
    o.append(_rect(316, 60, 48, 8, fill="url(#h6)", sw=1.1))     # guide nut
    o.append(_rect(328, 70, 24, 152, fill=PAPER, sw=1.0))        # stem bore
    o.append(_rect(334, 48, 12, 224, fill="#dfe7f0", sw=1.2))    # stem
    o.append(_rect(328, 44, 24, 8, fill="#cbd5df", sw=1.1))      # stem top cap
    for rx in (326, 346):                                        # O-ring
        o.append(_rect(rx, 148, 8, 8, fill="#2a2a2a", sw=0.8))

    # Upper housing flange and its bolts.
    o.append(_rect(248, 222, 184, 16, fill="url(#h6)", sw=1.3))
    for bx in (256, 412):
        o.append(_rect(bx, 226, 12, 8, fill="#cbd5df", sw=1.0))

    # Body: sectioned walls around an L-shaped (angle) flow cavity.
    o.append(_rect(294, 238, 92, 24, fill="url(#h6)", sw=1.2)) # body roof
    o.append(_rect(268, 238, 26, 160, fill="url(#h6)", sw=1.2))# left wall
    o.append(_rect(386, 246, 250, 16, fill="url(#h6)", sw=1.2))# inlet top
    o.append(_rect(386, 310, 250, 16, fill="url(#h6)", sw=1.2))# inlet bottom
    o.append(_rect(386, 326, 22, 72, fill="url(#h6)", sw=1.2)) # drain wall
    o.append(_rect(628, 246, 16, 80, fill="url(#h6)", sw=1.2)) # inlet flange
    o.append(_poly([(294, 262), (636, 262), (636, 310), (386, 310),
                    (386, 398), (294, 398)], fill=PAPER, sw=1.2, close=True))

    # Seat and tapered metal plug on the stem.
    o.append(_rect(310, 306, 60, 8, fill="#9aa9b8", sw=1.0))
    o.append(_poly([(324, 268), (356, 268), (350, 304), (330, 304)],
                   fill="#c9d4de", sw=1.3, close=True))

    # Bilingual callouts.
    _lead(o, 300, 110, 204, 102, "Nắp van / Bonnet")
    _lead(o, 248, 232, 204, 198, "Mặt bích / Housing flange")
    _lead(o, 310, 310, 204, 290, "Đế van / Seat")
    _lead(o, 274, 352, 204, 352, "Thân van / Valve body")
    _lead(o, 354, 152, 466, 142, "Vòng đệm O / O-ring", anchor="start")
    _lead(o, 354, 286, 466, 212, "Nút kim loại / Metal plug", anchor="start")
    o.append(T(520, 240, "Cổng vào / Inlet", 7.6, anchor="middle"))

    # Drain arrow and bilingual strip.
    o.append(_arrow(340, 400, 340, 424, sw=1.4, color=INK))
    o.append(T(356, 418, "DRAIN / THOÁT NƯỚC", 7.4, anchor="start", color=INK))
    o.append(T(340, 436, "Hình 26-1 · Van góc tự thoát nước, nút kim loại (thiết kế 3-A Council)",
               6.8, color=INK))
    o.append(T(340, 450, "Figure 26-1 · Self-draining angle valve with metal plug (3-A Council design)",
               6.8, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Sơ đồ cắt van góc tự thoát nước với nút kim loại")),
                "Hình 26-1 · Van góc tự thoát nước với nút kim loại, thiết kế theo hướng dẫn 3-A Council cho ngành thực phẩm",
                "Figure 26-1 · Typical self-draining angle valve with metal plug originally designed for service in the food industry under the guidelines of the 3-A Council.",
                "Sơ đồ cắt van góc tự thoát nước với nút kim loại, nắp van, vòng đệm O, cổng vào và mũi tên thoát nước",
                "Cross-section of a self-draining angle valve with metal plug, bonnet, O-ring, inlet and drain arrow")


@_reg
def fig_f262():
    """Figure 26-2 -- modern sanitary/aseptic valve, stable flow-to-open."""
    w, h = 680, 460
    o = [_defs()]
    o.append(T(340, 20, "Van vệ sinh hiện đại dòng chảy theo chiều mở / Modern flow-to-open sanitary valve",
               10.0, color=INK, weight="600"))
    o.append(_line(340, 44, 340, 292, sw=0.9, color=GREY, dash="6,4"))

    # Bonnet with external threads, bore and threaded stem.
    o.append(_poly([(296, 176), (296, 88), (306, 72), (306, 66),
                    (374, 66), (374, 72), (384, 88), (384, 176)],
                   fill="url(#h6)", sw=1.3, close=True))
    for y in (78, 86, 94, 102):
        o.append(_line(290, y, 296, y, sw=0.9, color=INK))
        o.append(_line(384, y, 390, y, sw=0.9, color=INK))
    o.append(_rect(330, 66, 20, 110, fill=PAPER, sw=1.0))
    o.append(_rect(334, 50, 12, 160, fill="#dfe7f0", sw=1.2))
    for y in (58, 64, 70):
        o.append(_line(330, y, 350, y, sw=0.7, color=GREY))

    # Body: inverted-U chamber with a horizontal inlet from the left.
    o.append(_rect(270, 180, 20, 96, fill="url(#h6)", sw=1.2))
    o.append(_rect(410, 180, 20, 96, fill="url(#h6)", sw=1.2))
    o.append(_rect(270, 180, 160, 20, fill="url(#h6)", sw=1.2))
    o.append(_rect(140, 200, 130, 16, fill="url(#h6)", sw=1.2))
    o.append(_rect(140, 246, 130, 16, fill="url(#h6)", sw=1.2))
    o.append(_rect(140, 200, 12, 62, fill="url(#h6)", sw=1.2))
    o.append(_poly([(152, 216), (290, 216), (410, 200), (410, 262),
                    (290, 262), (290, 246), (152, 246)],
                   fill=PAPER, sw=0.6, close=True))

    # Polished ball plug, clamped-in seal and seat.
    o.append(_circle(340, 236, 26, fill="#dfe7f0", sw=1.4))
    o.append(_circle(332, 228, 6, fill="#ffffff", sw=0.0))
    o.append(_rect(310, 260, 60, 6, fill="#9aa9b8", sw=1.0))
    o.append(_rect(308, 266, 64, 4, fill="#2a2a2a", sw=0.8))

    # Flow arrows: inlet from the left, two outlets downward.
    o.append(_arrow(158, 231, 288, 231, sw=1.6, color=GREEN))
    o.append(_arrow(300, 268, 300, 294, sw=1.6, color=GREEN))
    o.append(_arrow(380, 268, 380, 294, sw=1.6, color=GREEN))

    # Plan detail: circular seat with four tapered grooves.
    o.append(T(340, 306, "Rãnh côn / Tapered grooves — nhìn từ trên / plan view",
               7.4, anchor="middle", color=BLUE))
    o.append(_circle(340, 370, 54, fill=PAPER, sw=1.3))
    o.append(_circle(340, 370, 42, sw=0.8, color=GREY))
    o.append(_line(286, 370, 394, 370, sw=0.7, color=GREY, dash="5,3"))
    o.append(_line(340, 316, 340, 424, sw=0.7, color=GREY, dash="5,3"))
    for pts in ([(360, 365), (394, 358), (394, 382), (360, 375)],
                [(320, 365), (286, 358), (286, 382), (320, 375)],
                [(335, 350), (328, 316), (352, 316), (345, 350)],
                [(335, 390), (328, 424), (352, 424), (345, 390)]):
        o.append(_poly(pts, fill="#dbe8f2", sw=0.9, color=BLUE, close=True))
    o.append(_circle(340, 370, 20, fill="url(#h6)", sw=1.1))

    # Bilingual callouts.
    _lead(o, 276, 190, 204, 168, "Thân van / Valve body")
    _lead(o, 346, 130, 466, 120, "Thân van / Stem", anchor="start")
    _lead(o, 362, 230, 466, 214, "Nút bi cầu / Polished ball plug", anchor="start")
    _lead(o, 340, 268, 204, 292, "Gioăng kẹp / Clamped-in seal")
    o.append(T(200, 222, "Dòng vào / Inlet", 7.4, color=GREEN))
    o.append(T(400, 286, "Dòng ra / Outlet", 7.4, color=GREEN))
    o.append(T(474, 244, "Nút trụ / Cylindrical plug (large sizes)",
               7.0, anchor="start", color=GREY))
    o.append(T(340, 436, "Hình 26-2 · Van vệ sinh chiều mở; rãnh côn, gioăng kẹp Class VI",
               6.8, color=INK))
    o.append(T(340, 450, "Figure 26-2 · Flow-to-open sanitary valve with tapered grooves and clamped-in seal",
               6.8, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Sơ đồ cắt van vệ sinh và hình chiếu rãnh côn")),
                "Hình 26-2 · Van vệ sinh và vô trùng hiện đại với nút van chạy theo chiều dòng chảy mở ổn định; rãnh côn dễ đánh bóng, số rãnh quyết định lưu lượng, gioăng kẹp đạt độ kín Class VI",
                "Figure 26-2 · A modern sanitary and aseptic valve design where the plug is operating in the stable flow-to-open direction. Tapered grooves provide easy-to-polish and easy-to-clean flow passages. The number of grooves determines flow capacity. The flow characteristic is about 'equal percentage.' A clamped-in seal (not shown) will provide Class VI shutoff. A cylindrical plug replaces the polished ball in larger valve sizes.",
                "Sơ đồ cắt van vệ sinh với nút bi cầu, rãnh côn nhìn từ trên, dòng vào bên trái và dòng ra phía dưới",
                "Cross-section of a sanitary valve with polished ball plug, top view of tapered grooves, inlet from left and downward outlets")


@_reg
def fig_f263():
    """Figure 26-3 -- diaphragm valve, good shutoff but poor flow characteristic."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 20, "Van màng / Diaphragm valve — vị trí lắp thông thường",
               10.0, color=INK, weight="600"))
    o.append(_line(230, 54, 230, 330, sw=0.9, color=GREY, dash="6,4"))

    # Vertical pipe body with flanged ends and a raised weir.
    o.append(_rect(168, 76, 18, 240, fill="url(#h6)", sw=1.2))
    o.append(_rect(274, 76, 18, 240, fill="url(#h6)", sw=1.2))
    o.append(_rect(158, 64, 124, 14, fill="url(#h6)", sw=1.2))
    o.append(_rect(158, 316, 124, 14, fill="url(#h6)", sw=1.2))
    o.append(_poly([(186, 158), (238, 188), (186, 218)],
                   fill="url(#h6)", sw=1.2, close=True))

    # Black diaphragm clamped at its edges, pressing onto the weir.
    o.append(_path("M 274,148 C 246,150 236,172 240,188 C 236,206 246,224 274,226",
                   sw=9, color="#1a1a1a"))
    o.append(_rect(266, 144, 18, 10, fill="#9aa9b8", sw=1.0))
    o.append(_rect(266, 222, 18, 10, fill="#9aa9b8", sw=1.0))

    # Horizontal actuator and stem.
    o.append(_rect(276, 182, 30, 12, fill="#dfe7f0", sw=1.1))
    o.append(_path("M 320,142 H 460 Q 480,142 480,188 Q 480,234 460,234 "
                   "H 320 Q 300,234 300,188 Q 300,142 320,142 Z",
                   fill="#e8edf2", sw=1.3))
    o.append(_line(430, 142, 430, 234, sw=0.8, color=GREY, dash="5,3"))
    o.append(_rect(470, 168, 14, 12, fill="#cbd5df", sw=1.0))

    # Drain arrow.
    o.append(_arrow(230, 332, 230, 352, sw=1.4, color=INK))
    o.append(T(252, 348, "DRAIN / THOÁT", 7.2, anchor="start"))

    # Bilingual callouts.
    _lead(o, 174, 120, 204, 110, "Thân van / Valve body")
    _lead(o, 210, 196, 204, 248, "Bệ van / Weir")
    _lead(o, 252, 166, 360, 100, "Màng / Diaphragm", anchor="start")
    _lead(o, 420, 150, 466, 262, "Bộ truyền động / Actuator", anchor="start")
    o.append(T(340, 290, "Đóng kín tốt / Good shutoff · Đặc tính dòng kém / Poor flow characteristic",
               7.0, color=GREY))
    o.append(T(340, 394, "Hình 26-3 · Van màng ở vị trí lắp điển hình, đóng kín tốt nhưng đặc tính dòng kém",
               6.8, color=INK))
    o.append(T(340, 408, "Figure 26-3 · Diaphragm valve: good shutoff but poor flow characteristic",
               6.8, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Sơ đồ cắt van màng với bệ van và bộ truyền động")),
                "Hình 26-3 · Van màng ở vị trí lắp đặt điển hình, đóng kín tốt nhưng đặc tính dòng chảy kém",
                "Figure 26-3 · A diaphragm valve, shown in a typical mounting position, provides good shutoff but poor flow characteristic.",
                "Sơ đồ cắt van màng với bệ van, màng đen, bộ truyền động ngang và mũi tên thoát nước",
                "Cross-section of a diaphragm valve with weir, black diaphragm, horizontal actuator and drain arrow")


@_reg
def fig_f264():
    """Figure 26-4 -- improved diaphragm-style valve for aseptic modulating control."""
    w, h = 680, 460
    o = [_defs()]
    o.append(T(340, 20, "Van màng cải tiến điều tiết vô trùng / Improved aseptic modulating diaphragm valve",
               10.0, color=INK, weight="600"))
    o.append(_line(340, 120, 340, 380, sw=0.9, color=GREY, dash="6,4"))

    # Horizontal cylindrical actuator, clamped at both ends.
    o.append(_path("M 236,40 H 444 Q 472,40 472,68 Q 472,96 444,96 "
                   "H 236 Q 208,96 208,68 Q 208,40 236,40 Z",
                   fill="#eef2f7", sw=1.3))
    o.append(_rect(208, 38, 14, 60, fill="url(#h6)", sw=1.1))
    o.append(_rect(458, 38, 14, 60, fill="url(#h6)", sw=1.1))
    for bx in (204, 468):
        for by in (44, 86):
            o.append(_rect(bx, by, 8, 6, fill="#cbd5df", sw=0.8))
    o.append(_rect(450, 28, 18, 12, fill="#dfe7f0", sw=1.0))

    # Bonnet with toggle mechanism and secondary seal/telltale.
    o.append(_poly([(288, 104), (392, 104), (404, 208), (276, 208)],
                   fill="url(#h6)", sw=1.3, close=True))
    o.append(_rect(300, 110, 80, 86, fill=PAPER, sw=1.0))
    o.append(_rect(334, 96, 12, 92, fill="#dfe7f0", sw=1.1))
    for (a, b) in (((340, 138), (306, 166)), ((340, 138), (374, 166)),
                   ((306, 166), (340, 190)), ((374, 166), (340, 190))):
        o.append(_line(a[0], a[1], b[0], b[1], sw=2.0, color="#7a8794"))
    for (cx, cy) in ((340, 138), (306, 166), (374, 166), (340, 190)):
        o.append(_circle(cx, cy, 4, fill="#cbd5df", sw=1.0))
    o.append(_rect(282, 148, 14, 22, fill="#f6e6c8", sw=1.0))
    o.append(_line(282, 159, 258, 159, sw=1.0, color=GREEN))
    o.append(_circle(250, 159, 8, fill=PAPER, sw=1.0, color=GREEN))
    o.append(T(250, 162, "T", 7.0, color=GREEN, weight="600"))
    o.append(_rect(266, 208, 148, 12, fill="url(#h6)", sw=1.2))
    for bx in (272, 400):
        o.append(_rect(bx, 210, 8, 8, fill="#cbd5df", sw=0.9))

    # Bonded PTFE-over-EPDM diaphragm with ~45 degree retracted slope.
    o.append(_path("M 268,222 C 300,222 312,230 322,246 C 330,256 334,260 340,260 "
                   "C 346,260 350,256 358,246 C 368,230 380,222 412,222",
                   sw=9, color="#1a1a1a"))
    o.append(_path("M 268,228 C 300,228 314,236 324,251 C 331,260 336,264 340,264 "
                   "C 344,264 349,260 356,251 C 366,236 380,228 412,228",
                   sw=2.4, color="#cfd6da"))

    # Body with circular orifice and a self-draining inlet from the left.
    o.append(_rect(266, 270, 22, 100, fill="url(#h6)", sw=1.2))
    o.append(_rect(392, 270, 22, 100, fill="url(#h6)", sw=1.2))
    o.append(_rect(306, 268, 24, 10, fill="url(#h6)", sw=1.0))
    o.append(_rect(350, 268, 24, 10, fill="url(#h6)", sw=1.0))
    o.append(_rect(150, 292, 138, 10, fill="url(#h6)", sw=1.1))
    o.append(_rect(150, 318, 138, 10, fill="url(#h6)", sw=1.1))
    o.append(_rect(296, 370, 88, 12, fill="url(#h6)", sw=1.2))
    o.append(_arrow(162, 310, 286, 310, sw=1.5, color=GREEN))
    o.append(_arrow(340, 384, 340, 406, sw=1.4, color=INK))
    o.append(T(356, 400, "DRAIN", 7.2, anchor="start"))

    # Bilingual callouts.
    _lead(o, 240, 62, 204, 66, "Bộ truyền động / Actuator")
    _lead(o, 282, 158, 204, 152, "Phớt phụ + báo động / Secondary seal + telltale")
    _lead(o, 272, 330, 204, 328, "Thân van / Valve body")
    _lead(o, 374, 166, 466, 154, "Cơ cấu bẩy / Toggle mechanism", anchor="start")
    _lead(o, 380, 232, 466, 220, "Màng PTFE/EPDM / Bonded diaphragm", anchor="start")
    _lead(o, 350, 273, 466, 272, "Lỗ tiết lưu tròn / Circular orifice", anchor="start")
    o.append(T(210, 286, "Dòng vào / Inlet", 7.2, color=GREEN))
    o.append(T(474, 242, "Góc lùi ~45° / retracted slope", 7.0, anchor="start", color=GREY))
    o.append(T(340, 420, "Đặc tính gần tuyến tính / Nearly linear characteristic",
               6.8, color=GREY))
    o.append(T(340, 436, "Hình 26-4 · Van màng cải tiến điều tiết trong môi trường vô trùng",
               6.8, color=INK))
    o.append(T(340, 450, "Figure 26-4 · Improved diaphragm-style valve for aseptic modulating control",
               6.8, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Sơ đồ cắt van màng cải tiến với cơ cấu bẩy và màng PTFE")),
                "Hình 26-4 · Phiên bản cải tiến của van kiểu màng dùng để điều khiển điều tiết trong môi trường vô trùng, có màng PTFE liên kết trên EPDM",
                "Figure 26-4 · Improved version of diaphragm-style valve designed specifically for modulating control in a septic service. A diaphragm is available with bonded PTFE over EPDM elastomer.",
                "Sơ đồ cắt van màng cải tiến với bộ truyền động nằm ngang, cơ cấu bẩy, phớt phụ, màng và lỗ tiết lưu tròn",
                "Cross-section of an improved diaphragm valve with horizontal actuator, toggle mechanism, secondary seal, diaphragm and circular orifice")
