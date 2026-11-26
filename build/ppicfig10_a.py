# -*- coding: utf-8 -*-
"""Vector figures 10.1-10.2 for PPIC chapter 10 (digital I and C reliability).

Genuine vector redraws of the printed diagrams on PDF pages 251 and 260:
the proposed digital pressurizer control system (printed p.235) and the
Markov transition diagram for the Feedwater Valve (printed p.244).
"""
from ppicfig10_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar,
                              _circle, _defs, _ellipse, _fig, _frame, _legend,
                              _line, _path, _poly, _rect, _mk, _series, _state,
                              make_registry)

FIGS, _reg = make_registry()


# ------------------------------------------------------------------- fig 10.1
@_reg
def fig_f01():
    o = [_defs()]
    o.append(T(340, 13,
               "Proposed digital system · Sơ đồ điều khiển số đề xuất",
               9.0, color=INK, weight="600"))

    # ---------------- pressurizer vessel: domed vertical cylinder (right) ----
    xl, xr = 375.0, 505.0
    vx = 440.0
    o.append(_path(
        "M375,250 L375,100 C375,68 405,62 440,62 C475,62 505,68 505,100 "
        "L505,250 C505,272 475,280 440,280 C405,280 375,272 375,250 Z",
        fill="#eef3fb", sw=1.7))

    # water-level mark and its ripples
    o.append(_line(377, 168, 503, 168, sw=1.4, color=BLUE))
    for dx in (-24, -12, 0, 12, 24):
        o.append(_line(vx + dx - 5, 173, vx + dx + 5, 173,
                       sw=0.9, color=BLUE, dash="3 2"))
    o.append(T(vx, 190, "WATER LEVEL", 6.8, color=INK))
    o.append(T(vx, 200, "MỰC NƯỚC", 6.4, color=BLUE))

    # ---------------- spray nozzle and falling droplets (upper right) -------
    o.append(_path("M505,116 L462,116 Q452,116 452,126 L452,132",
                   fill="none", sw=1.7, color=INK))
    o.append(_poly([(446, 132), (458, 132), (452, 141)],
                   fill="#cdd6e2", sw=1.0, close=True))
    for dx in (-9, -5, -1, 3, 7):
        o.append(_line(452 + dx * 0.25, 143, 452 + dx, 153,
                       sw=0.9, color=BLUE))
    o.append(T(514, 120, "SPRAYS", 6.8, color=INK, anchor="start"))
    o.append(T(514, 130, "TIA PHUN", 6.2, color=BLUE, anchor="start"))

    # ---------------- relief valve on a pipe from the vessel dome (top) -----
    o.append(_path("M400,70 L250,70", fill="none", sw=1.7, color=INK))
    o.append(_poly([(236, 62), (236, 78), (250, 70)],
                   fill="#ffffff", sw=1.3, close=True))
    o.append(_poly([(264, 62), (264, 78), (250, 70)],
                   fill="#ffffff", sw=1.3, close=True))
    o.append(_line(250, 62, 250, 53, sw=1.2, color=INK))
    o.append(_circle(250, 49, 4, fill="#ffffff", sw=1.2))
    o.append(T(160, 44, "RELIEF VALVE", 6.8, color=INK))
    o.append(T(160, 54, "VAN XẢ", 6.2, color=RED))

    # ---------------- safety valve seated on the dome apex ------------------
    o.append(_line(440, 62, 440, 58, sw=1.5, color=INK))
    o.append(_poly([(428, 43), (428, 57), (440, 50)],
                   fill="#ffffff", sw=1.3, close=True))
    o.append(_poly([(452, 43), (452, 57), (440, 50)],
                   fill="#ffffff", sw=1.3, close=True))
    o.append(_line(440, 43, 440, 37, sw=1.2, color=INK))
    o.append(_path("M436,37 L444,34 L436,31 L444,28",
                   fill="none", sw=1.0, color=RED))
    o.append(T(516, 44, "SAFETY VALVE", 6.8, color=INK, anchor="start"))
    o.append(T(516, 54, "VAN AN TOÀN", 6.2, color=RED, anchor="start"))

    # ---------------- heater elements at the vessel bottom ------------------
    o.append(_path("M505,262 L478,286", fill="none", sw=1.6, color=INK))
    o.append(_path("M418,286 L426,280 L434,291 L442,280 L450,291 "
                   "L458,280 L466,286", fill="none", sw=1.8, color=RED))
    o.append(T(vx, 305, "HEATERS", 6.8, color=INK))
    o.append(T(vx, 314, "BỘ GIA NHIỆT", 6.0, color=RED))

    # ---------------- microcontroller box (left) ----------------------------
    o.append(_rect(55, 140, 140, 65, fill="#eef3fb", sw=1.5))
    o.append(T(125, 168, "MICROCONTROLLER", 7.4, color=INK, weight="600"))
    o.append(T(125, 183, "BỘ ĐIỀU KHIỂN VI", 7.0, color=BLUE))

    # ---------------- control / signal lines --------------------------------
    # controller -> relief valve actuator
    o.append(_line(75, 140, 75, 49, sw=1.2, color=BLUE, dash="4 3"))
    o.append(_line(75, 49, 240, 49, sw=1.2, color=BLUE, dash="4 3"))
    o.append(_ar(238, 49, 246, 49, color=BLUE, sw=1.2))
    # controller -> safety valve actuator
    o.append(_line(120, 140, 120, 26, sw=1.2, color=BLUE, dash="4 3"))
    o.append(_line(120, 26, 440, 26, sw=1.2, color=BLUE, dash="4 3"))
    o.append(_ar(440, 26, 440, 33, color=BLUE, sw=1.2))
    # controller -> sprays
    o.append(_line(195, 150, 350, 150, sw=1.2, color=BLUE, dash="4 3"))
    o.append(_line(350, 150, 350, 110, sw=1.2, color=BLUE, dash="4 3"))
    o.append(_line(350, 110, 496, 110, sw=1.2, color=BLUE, dash="4 3"))
    o.append(_ar(496, 110, 504, 114, color=BLUE, sw=1.2))
    # controller -> heaters
    o.append(_line(195, 196, 350, 196, sw=1.2, color=RED, dash="4 3"))
    o.append(_line(350, 196, 350, 294, sw=1.2, color=RED, dash="4 3"))
    o.append(_line(350, 294, 460, 294, sw=1.2, color=RED, dash="4 3"))
    o.append(_ar(460, 294, 466, 287, color=RED, sw=1.2))
    # level-sensing line back from the vessel to the controller
    o.append(_line(375, 168, 215, 168, sw=1.3, color=GREEN))
    o.append(_ar(215, 168, 198, 168, color=GREEN, sw=1.3))
    o.append(T(292, 164, "LEVEL SENSOR / CẢM BIẾN MỰC", 6.0,
               color=GREEN))

    return _mk(1, o, "Proposed digital system",
               "Sơ đồ hệ thống điều khiển số đề xuất",
               "Proposed digital system",
               "Sơ đồ hệ thống điều khiển số đề xuất: bình áp lực có nóm cong, vòi phun, mực nước, lò gia nhiệt, van xả và van an toàn, cùng bộ điều khiển vi được nối bằng các đường tín hiệu điều khiển và đường cảm biến mực nước.",
               "Digital pressurizer control scheme: a domed vessel with spray nozzle, water-level mark, heaters, relief and safety valves, and a microcontroller linked by control lines and a level-sensing feedback line.")


# ------------------------------------------------------------------- fig 10.2
@_reg
def fig_f02():
    o = [_defs()]
    o.append(T(340, 14,
               "Markov transition diagram for the Feedwater Valve · "
               "Sơ đồ Markov của van nước cấp",
               8.8, color=INK, weight="600"))

    # framed diagram, as printed
    o.append(_rect(115, 55, 450, 225, fill="#fbfaf7", sw=1.3))

    # three states
    o.append(_state(210, 168, 34, 0, "VPC₀"))
    o.append(_state(455, 118, 34, 1, "VPC₁"))
    o.append(_state(455, 218, 34, 2, "VPC₂"))

    # transitions out of state (0)
    o.append(_ar(242, 158, 423, 126, color=BLUE, sw=1.8))
    o.append(T(332, 130, "λ₁ VPC", 7.4, color=BLUE))
    o.append(_ar(242, 178, 423, 212, color=BLUE, sw=1.8))
    o.append(T(332, 205, "λ₂ VPC", 7.4, color=BLUE))

    return _mk(2, o, "Markov transition diagram for the Feedwater Valve",
               "Sơ đồ chuyển trạng thái Markov của van nước cấp",
               "Markov transition diagram for the Feedwater Valve",
               "Sơ đồ Markov của van nước cấp với trạng thái (0) VPC₀ chuyển sang (1) VPC₁ và (2) VPC₂ theo tỷ lệ λ₁ VPC và λ₂ VPC.",
               "Markov diagram for the Feedwater Valve with state (0) VPC₀ transitioning to (1) VPC₁ and (2) VPC₂ at rates λ₁ VPC and λ₂ VPC.")
