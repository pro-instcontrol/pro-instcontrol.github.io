# -*- coding: utf-8 -*-
"""Vector figure 11.3 for PPIC chapter 11 (adaptive power control).

fig_f03 -- closed-loop control structure, printed p.271 (PDF p.287):
the saturated adaptive output-feedback controller (adaptation law, virtual
controller, saturation compensator, saturation element) drives the control
rods of the HTR-PM reactor model; neutron kinetics and reactor
thermal-hydraulics feed the OTSG and secondary loop; the measured relative
neutron power, average helium temperature and rod position return as three
labelled feedback signals.
"""
from ppicfig11_common import (BLUE, GREEN, GREY, INK, RED, W, T, _ar,
                              _circle, _defs, _fig, _frame, _line,
                              _poly, _rect, _mk, _series, make_registry)

FIGS, _reg = make_registry()

_YELLOW = "#fff2a8"
_CYAN = "#d9eef7"


def _blk(x, y, w, h, lines, size=7.0, fill=_YELLOW, stroke=INK):
    """Rectangle with one or more centred text lines."""
    o = [_rect(x, y, w, h, fill, sw=1.1, stroke=stroke)]
    n = len(lines)
    y0 = y + h / 2.0 - (n - 1) * size * 0.62 + size * 0.34
    for i, ln in enumerate(lines):
        o.append(T(x + w / 2.0, y0 + i * size * 1.24, ln, size, color=INK))
    return "".join(o)


# ------------------------------------------------------------------- fig 11.3
@_reg
def fig_f03():
    o = [_defs()]
    o.append(T(340, 13, "Closed-loop control structure: saturated adaptive "
               "output-feedback power regulation", 8.6, color=INK,
               weight="600"))

    # ---- two enclosing groups -------------------------------------------
    o.append(_rect(8, 22, 332, 266, fill="#fbfdff", sw=1.5, stroke=BLUE))
    o.append(_rect(428, 22, 244, 266, fill="#fffbfb", sw=1.5, stroke=RED))
    o.append(T(174, 283, "Saturated Adaptive Output-Feedback Controller",
               7.2, color=BLUE, weight="600"))
    o.append(T(550, 36, "Simulation Model", 8.0, color=RED, weight="600"))

    # ---- controller: adaptation law -------------------------------------
    o.append(_blk(18, 32, 120, 52,
                  ["Adaptation Law",
                   "θ̂1 = -π1 θ̂1 n_r² x1²",
                   "θ̂2 = -π2 θ̂2 q_R x1 ∫x4 dτ"], size=6.5))
    # virtual controller -> derivative -> saturation -> summing junction
    o.append(_blk(18, 98, 150, 46,
                  ["Virtual Controller",
                   "ξ_d = -[k_NP x1 + k_NI ∫x1(τ)dτ]",
                   "- q_R[θ̂1 x1 + θ̂2 x1(x1 x4)]"], size=6.5))
    o.append(_blk(206, 110, 34, 28, ["d/dt"], size=7.0, fill="#eef3fb"))
    o.append(_blk(248, 110, 38, 28, ["sat(·)"], size=7.0, fill="#eef3fb"))
    o.append(_circle(304, 124, 7, fill="#ffffff", sw=1.2, color=INK))
    o.append(T(304, 127, "+", 8.0, color=INK))

    # saturation compensator
    o.append(_blk(18, 182, 170, 54,
                  ["Saturation Compensator",
                   "u_cp = -q_E1 |u_m| th(·) - q_E2 |u_m| th(·)",
                   "e_ξ = ξ - ξ_d ; e_f : expanded state (21)"], size=6.3))

    # adapted parameters: dashed connections to both upper blocks
    o.append(_ar(138, 56, 160, 98, color=GREEN, sw=1.1, dash="4 3"))
    o.append(_poly([(138, 76), (196, 76), (196, 174)],
                   sw=1.1, color=GREEN, dash="4 3"))
    o.append(_ar(196, 174, 160, 182, color=GREEN, sw=1.1, dash="4 3"))
    o.append(T(200, 92, "θ̂1, θ̂2", 6.0, color=GREEN, anchor="start"))

    # main signal chain inside the controller
    o.append(_ar(168, 124, 206, 124, color=INK, sw=1.4))
    o.append(_ar(240, 124, 248, 124, color=INK, sw=1.4))
    o.append(_ar(286, 124, 297, 124, color=INK, sw=1.4))
    # compensator feeds both the saturation element and the final summing node
    o.append(_poly([(188, 209), (267, 209)], sw=1.4, color=INK))
    o.append(_ar(267, 209, 267, 138, color=INK, sw=1.4))
    o.append(_poly([(267, 209), (304, 209)], sw=1.4, color=INK))
    o.append(_ar(304, 209, 304, 131, color=INK, sw=1.4))
    o.append(T(178, 260, "measured outputs  y = [x1, x4, ξ]ᵀ",
               6.4, color=GREY, anchor="start"))

    # ---- plant: rod drive then HTR-PM reactor ----------------------------
    o.append(_ar(311, 124, 428, 124, color=INK, sw=1.6))
    o.append(T(384, 117, "Rod Speed u", 6.2, color=INK))
    o.append(_blk(436, 54, 88, 30, ["Control Rods"], size=7.4,
                  fill="#f4f4f4"))
    o.append(_ar(480, 84, 480, 110, color=BLUE, sw=1.4))
    o.append(T(490, 101, "ρ_r", 6.0, color=BLUE, anchor="start"))

    # HTR-PM reactor sub-model
    o.append(_rect(436, 110, 156, 122, fill="#f7fcff", sw=1.2, stroke=GREY))
    o.append(T(514, 228, "HTR-PM Reactor", 6.4, color=GREY))
    o.append(_blk(444, 126, 62, 50, ["Neutron", "Kinetics"], size=7.0,
                  fill=_CYAN))
    o.append(_blk(518, 126, 66, 50, ["Reactor", "Thermal-", "Hydraulics"],
                  size=6.6, fill=_CYAN))
    o.append(_ar(506, 142, 518, 142, color=BLUE, sw=1.3))
    o.append(T(512, 138, "n", 5.8, color=BLUE))
    o.append(_ar(518, 160, 506, 160, color=BLUE, sw=1.3))
    o.append(T(512, 182, "reactivity", 5.2, color=BLUE))
    o.append(T(512, 189, "feedback", 5.2, color=BLUE))

    # ---- OTSG and secondary loop ----------------------------------------
    o.append(_blk(606, 112, 54, 104,
                  ["OTSG", "&", "Secondary", "Loop"], size=7.0,
                  fill="#f4f4f4"))
    o.append(_ar(584, 136, 606, 136, color=RED, sw=1.4))
    o.append(T(595, 130, "T_h,out", 5.6, color=RED))
    o.append(_ar(606, 166, 584, 166, color=BLUE, sw=1.4))
    o.append(T(595, 181, "T_c,in", 5.6, color=BLUE))

    # ---- three explicit feedback paths back to the controller -----------
    o.append(_ar(428, 196, 340, 196, color=INK, sw=1.4))
    o.append(T(384, 190, "x1 := δ n_r", 6.2, color=INK))
    o.append(_ar(428, 222, 340, 222, color=INK, sw=1.4))
    o.append(T(384, 216, "x4 := δ T_H", 6.2, color=INK))
    o.append(_ar(428, 248, 340, 248, color=INK, sw=1.4))
    o.append(T(384, 242, "ξ := δ h_r", 6.2, color=INK))

    return _mk(
        3, o,
        "Closed-loop structure of the saturated adaptive output-feedback "
        "power-level control",
        "Sơ đồ cấu trúc vòng lặp kín của bộ điều khiển công suất thích ứng "
        "bão hòa phản hồi đầu ra",
        "Closed-loop structure of the saturated adaptive output-feedback "
        "power-level control",
        "Sơ đồ khối vòng lặp kín gồm bộ điều khiển thích ứng bão hòa phản hồi "
        "đầu ra với luật thích ứng, bộ điều khiển ảo, bộ bù bão hòa và phần tử "
        "bão hòa dẫn động thanh điều khiển trong mô hình lò phản ứng HTR-PM; "
        "động học neutron và thủy nhiệt lò cấp khí nóng cho OTSG và vòng tuần "
        "hoàn phụ, còn các tín hiệu đo n_r, T_h và ξ được phản hồi về bộ điều "
        "khiển theo ba đường riêng biệt.",
        "Block diagram of the closed loop: the saturated adaptive "
        "output-feedback controller with adaptation law, virtual controller, "
        "saturation compensator and saturation element drives the control "
        "rods of the HTR-PM reactor model; neutron kinetics and reactor "
        "thermal-hydraulics feed the OTSG and secondary loop, while the "
        "measured signals n_r, T_h and xi return to the controller on three "
        "labelled feedback paths.")
