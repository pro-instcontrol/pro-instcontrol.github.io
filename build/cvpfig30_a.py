# -*- coding: utf-8 -*-
"""Vector redraws of Figures 30-1 and 30-2 in Baumann Chapter 30,
*Control Valve Primer*, 5th ed. -- "The Bus System to the Rescue, or What
the Future May Bring".

Both printed figures are unlabelled line drawings.  They are redrawn here
as genuinely labelled vector schematics with bilingual (VI/EN) callouts
derived from the chapter text and the printed captions, never as raster
images.  Architecture mirrors `cvpfig26.py` exactly.
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
def fig_f301():
    """Figure 30-1 -- solid-state control valve, horizontal cross-section."""
    w, h = 680, 522
    o = [_defs()]
    o.append(T(340, 20,
               "Van điều khiển thể rắn / Solid-state control valve",
               10.2, color=INK, weight="600"))

    # ---- callout rows above the drawing -------------------------------
    o.append(T(44, 46, "Bộ chuyển đổi (điện môi) / Converter (dielectric)",
               7.6, anchor="start", color=INK))
    o.append(T(654, 46, "Trường điện cảm ứng / Induced electric field",
               7.6, anchor="end", color=INK))
    o.append(T(44, 66, "Cọc / Pole", 7.6, anchor="start", color=INK))
    o.append(T(616, 66, "Cọc / Pole", 7.6, anchor="end", color=INK))

    # ---- DC voltage loop and its two terminals ------------------------
    o.append(T(350, 88, "Điện áp một chiều / DC voltage", 8.0,
               color=INK, weight="600"))
    o.append(_line(290, 104, 330, 104, sw=1.2))
    o.append(_circle(330, 104, 3.4, fill=PAPER, sw=1.2))
    o.append(_circle(370, 104, 3.4, fill=PAPER, sw=1.2))
    o.append(_line(370, 104, 545, 104, sw=1.2))
    o.append(_line(290, 104, 290, 172, sw=1.2))
    o.append(_line(545, 104, 545, 164, sw=1.2))

    # ---- top wall, bottom wall and end walls (sectioned metal) --------
    o.append(_rect(110, 250, 530, 18, fill="url(#h6)", sw=1.2))
    o.append(_rect(110, 392, 530, 18, fill="url(#h6)", sw=1.2))
    o.append(_rect(110, 250, 14, 160, fill="url(#h6)", sw=1.2))
    o.append(_rect(626, 250, 14, 160, fill="url(#h6)", sw=1.2))
    o.append(_rect(124, 268, 502, 124, fill=PAPER, sw=0))

    # ---- liquid inlet -------------------------------------------------
    o.append(_arrow(52, 330, 108, 330, sw=1.6, color=GREEN))
    o.append(T(80, 316, "Chất lỏng / Liquid", 7.6,
               anchor="middle", color=GREEN))

    # ---- suspended sleeve: outer dielectric layer and inner mass ------
    o.append(_path("M 240,282 H 548 Q 572,282 580,302 L 604,330 "
                   "L 580,358 Q 572,378 548,378 H 240 "
                   "Q 228,378 228,366 V 294 Q 228,282 240,282 Z",
                   fill="url(#h7)", sw=1.3))
    o.append(_path("M 246,290 H 538 Q 556,290 563,307 L 582,330 "
                   "L 563,353 Q 556,370 538,370 H 246 "
                   "Q 236,370 236,360 V 300 Q 236,290 246,290 Z",
                   fill="url(#h6)", sw=1.1))
    o.append(_rect(196, 322, 34, 16, fill=PAPER, sw=1.0))  # suspension
    o.append(_circle(213, 330, 3.0, fill="#cbd5df", sw=0.8))

    # ---- two threaded pole screws above the body ---------------------
    o.append(_rect(268, 172, 44, 18, fill="#eef3fb", sw=1.1))  # converter
    o.append(_rect(280, 186, 20, 6, fill="#cbd5df", sw=1.0))   # pole head
    o.append(_rect(284, 190, 12, 72, fill="#dfe7f0", sw=1.1))
    for yy in (198, 206, 214, 222, 230, 238, 246, 254):
        o.append(_line(284, yy, 296, yy, sw=0.8, color=GREY))
    o.append(_rect(534, 164, 22, 8, fill="#cbd5df", sw=1.0))   # pole head
    o.append(_rect(538, 172, 14, 90, fill="#dfe7f0", sw=1.1))
    for yy in (182, 190, 198, 206, 214, 222, 230, 238, 246, 254):
        o.append(_line(538, yy, 552, yy, sw=0.8, color=GREY))

    # ---- leaders from the printed callouts ----------------------------
    _lead(o, 272, 180, 40, 46, "Bộ chuyển đổi (điện môi) / Converter (dielectric)",
          anchor="start")
    _lead(o, 286, 208, 40, 66, "Cọc / Pole", anchor="start")
    _lead(o, 604, 330, 654, 46, "Trường điện cảm ứng / Induced electric field")
    _lead(o, 546, 180, 616, 66, "Cọc / Pole")
    o.append(T(340, 192, "Điện cực ngoài / Outer electrode", 7.6,
               anchor="middle"))
    o.append(_line(336, 278, 340, 198, sw=0.9, color=GREY))
    o.append(T(460, 212, "Điện cực trong / Inner electrode", 7.6,
               anchor="middle"))
    o.append(_line(488, 292, 460, 218, sw=0.9, color=GREY))

    # ---- printed note and bilingual caption strip ---------------------
    o.append(T(340, 452,
               "LƯU Ý: TĂNG ĐIỆN ÁP MỘT CHIỀU LÀM GIẢM VẬN TỐC DÒNG CHẢY, "
               "DO ĐÓ LÀM GIẢM LƯU LƯỢNG.", 7.2, color=INK))
    o.append(T(340, 466,
               "NOTE: INCREASE OF DC VOLTAGE REDUCES FLOW VELOCITY AND, "
               "HENCE, FLOW RATE.", 7.2, color=GREY))
    o.append(T(340, 496, "Hình 30-1 · Van điều khiển thể rắn",
               6.8, color=INK))
    o.append(T(340, 510, "Figure 30-1 · Solid-state control valve.",
               6.8, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Sơ đồ cắt van điều khiển thể rắn với vòng điện áp một chiều, "
                        "cọc, bộ chuyển đổi điện môi, điện cực trong và ngoài "
                        "cùng trường điện cảm ứng")),
                "Hình 30-1 · Van điều khiển thể rắn. Sơ đồ cắt cho thấy tăng điện áp "
                "một chiều làm giảm vận tốc dòng chảy, do đó làm giảm lưu lượng.",
                "Figure 30-1 · Solid-state control valve. Horizontal cross-section "
                "showing that an increase of DC voltage reduces flow velocity and, "
                "hence, flow rate.",
                "Sơ đồ cắt ngang thân van có gạch chéo, mũi tên chất lỏng đi vào từ bên "
                "trái, vòng điện áp một chiều ở đỉnh nối với hai cọc ren qua bộ chuyển "
                "đổi điện môi; bên trong là ống bọc treo có đầu nhọn gồm điện cực ngoài "
                "và điện cực trong, với trường điện cảm ứng ở đầu phải; ghi chú dưới "
                "hình nói rằng tăng điện áp một chiều làm giảm vận tốc và lưu lượng "
                "dòng chảy",
                "Horizontal cross-section of a hatched valve body with a liquid inlet "
                "arrow from the left and a DC voltage loop across the top feeding two "
                "threaded pole screws through a dielectric converter; a suspended "
                "tapered sleeve carries outer and inner electrodes with an induced "
                "electric field at its right end; a note states that increasing DC "
                "voltage reduces flow velocity and hence flow rate")


@_reg
def fig_f302():
    """Figure 30-2 -- fieldbus connection schematic, control room and field."""
    w, h = 680, 522
    o = [_defs()]
    o.append(T(340, 20,
               "Sơ đồ nguyên lý kết nối fieldbus / Fieldbus connection schematic",
               10.2, color=INK, weight="600"))

    # ---- console-device zone -------------------------------------------
    o.append(_rect(60, 52, 440, 174, fill="none", sw=1.2, dash="7,5"))
    o.append(T(280, 70, "Thiết bị bàn điều khiển / Console device",
               8.4, color=INK, weight="600"))
    o.append(T(510, 150, "Phòng điều khiển / Control room",
               7.6, anchor="start", color=INK))
    o.append(_line(510, 154, 632, 154, sw=0.8, color=INK))

    # ---- personal computer ---------------------------------------------
    o.append(_rect(118, 92, 74, 52, fill="#dfe7f0", sw=1.1))
    o.append(_rect(124, 98, 62, 34, fill="#ffffff", sw=0.9))
    o.append(_rect(150, 144, 10, 6, fill="#cbd5df", sw=0.8))
    o.append(_rect(106, 154, 98, 12, fill="#eef3fb", sw=1.0))
    for yy in (157, 160, 163):
        o.append(_line(112, yy, 198, yy, sw=0.5, color=GREY))
    _lead(o, 155, 166, 155, 196, "Máy tính cá nhân / PC", anchor="middle")

    # ---- panel with indicators and pushbuttons -------------------------
    o.append(_rect(270, 92, 78, 92, fill="#eef3fb", sw=1.1))
    for i in range(6):
        o.append(_circle(282, 102 + i * 13, 3.0, fill="#ffffff", sw=0.7))
    for c in range(2):
        for i in range(6):
            o.append(_rect(298 + c * 16, 100 + i * 13, 11, 8,
                           fill="#dfe7f0", sw=0.6))
    _lead(o, 309, 184, 309, 196, "Bảng điều khiển / Panel", anchor="middle")

    # ---- keypad terminal ------------------------------------------------
    o.append(_rect(410, 92, 80, 60, fill="#eef3fb", sw=1.1))
    o.append(_rect(416, 98, 68, 12, fill="#dfe7f0", sw=0.8))
    for r in range(3):
        for c in range(8):
            o.append(_rect(416 + c * 8.5, 116 + r * 10, 7, 7,
                           fill="#ffffff", sw=0.6))
    _lead(o, 450, 152, 450, 196, "Bàn phím / Keypad terminal", anchor="middle")

    # ---- drops from the console devices into the bus -------------------
    o.append(_line(155, 166, 155, 286, sw=1.0, color=INK))
    o.append(_line(309, 184, 309, 286, sw=1.0, color=INK))
    o.append(_line(450, 152, 450, 286, sw=1.0, color=INK))

    # ---- the single fieldbus twisted pair ------------------------------
    o.append(_line(70, 286, 620, 286, sw=1.5, color=INK))
    o.append(_line(70, 292, 620, 292, sw=1.5, color=INK))
    o.append(T(500, 312, "Đường truyền trường / FIELDBUS", 7.8,
               anchor="middle", color=INK, weight="600"))
    o.append(_line(436, 316, 564, 316, sw=0.8, color=INK))
    o.append(T(640, 344, "Trường / FIELD", 7.8,
               anchor="end", color=INK, weight="600"))
    o.append(_line(574, 348, 660, 348, sw=0.8, color=INK))

    # ---- bus drops into the field devices ------------------------------
    o.append(_line(200, 289, 200, 322, sw=1.2, color=INK))
    o.append(_line(200, 322, 260, 322, sw=1.2, color=INK))
    o.append(_line(260, 322, 260, 346, sw=1.2, color=INK))
    o.append(_line(440, 289, 440, 328, sw=1.2, color=INK))
    o.append(_line(440, 328, 514, 328, sw=1.2, color=INK))
    o.append(_line(514, 328, 514, 346, sw=1.2, color=INK))

    # ---- valve positioner and actuator ---------------------------------
    o.append(_rect(232, 346, 56, 42, fill="#eef3fb", sw=1.1))
    o.append(_circle(260, 364, 6, fill="#ffffff", sw=0.9))
    o.append(_rect(248, 388, 24, 30, fill="#e8edf2", sw=1.0))
    for yy in (394, 400, 406):
        o.append(_line(248, yy, 272, yy, sw=0.6, color=GREY))
    o.append(_line(260, 418, 260, 424, sw=1.2, color=INK))
    o.append(_rect(238, 424, 44, 20, fill="#dfe7f0", sw=1.1))
    o.append(_rect(226, 428, 12, 12, fill="url(#h6)", sw=0.9))
    o.append(_rect(282, 428, 12, 12, fill="url(#h6)", sw=0.9))
    _lead(o, 260, 444, 260, 452, "Bộ định vị van / Valve positioner",
          anchor="middle")

    # ---- transmitter with two sensing elements ------------------------
    o.append(_rect(484, 346, 60, 36, fill="#eef3fb", sw=1.1))
    for i in range(5):
        o.append(_line(488 + i * 12, 350, 488 + i * 12, 378,
                       sw=0.6, color=GREY))
    o.append(_circle(496, 392, 8, fill="#ffffff", sw=1.0))
    o.append(_circle(532, 392, 8, fill="#ffffff", sw=1.0))
    o.append(_line(492, 392, 500, 392, sw=0.6, color=GREY))
    o.append(_line(528, 392, 536, 392, sw=0.6, color=GREY))
    _lead(o, 514, 400, 514, 452, "Bộ phát / Transmitter", anchor="middle")

    # ---- bilingual caption strip ---------------------------------------
    o.append(T(340, 496,
               "Hình 30-2 · Sơ đồ nguyên lý thiết bị kết nối trong hệ thống fieldbus",
               6.8, color=INK))
    o.append(T(340, 510,
               "Figure 30-2 · Schematic diagram of a component connected in a fieldbus system.",
               6.8, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Sơ đồ nguyên lý fieldbus: hộp đứt nét thiết bị bàn điều khiển "
                        "chứa máy tính cá nhân, bảng điều khiển và bàn phím trong phòng "
                        "điều khiển, một đường truyền xoắn đôi chạy xuống trường và "
                        "nhánh tới bộ định vị van cùng bộ phát")),
                "Hình 30-2 · Sơ đồ nguyên lý của một thiết bị được kết nối trong hệ "
                "thống fieldbus, gồm thiết bị bàn điều khiển trong phòng điều khiển và "
                "hai thiết bị hiện trường trên cùng một đường truyền xoắn đôi.",
                "Figure 30-2 · Schematic diagram of a component connected in a "
                "fieldbus system. Console devices sit in the control room and two "
                "field devices share a single twisted-pair bus.",
                "Hộp đứt nét nhãn thiết bị bàn điều khiển chứa máy tính cá nhân, bảng "
                "điều khiển có đèn và nút bấm, cùng bàn phím terminal; nhãn phòng điều "
                "khiển ở bên phải; một cặp dây fieldbus chạy ngang xuống vùng trường, "
                "có nhánh ngắn tới bộ định vị van kiểu màng ở bên trái và bộ phát có "
                "hai cảm biến ở bên phải",
                "Dashed console-device box holding a personal computer, a panel with "
                "indicators and pushbuttons, and a keypad terminal, with a control-room "
                "label at the right; a single fieldbus twisted pair runs into the field "
                "area with short drops to a diaphragm valve positioner on the left and "
                "a two-sensor transmitter on the right")
