# -*- coding: utf-8 -*-
"""Figure 10.3 - Markov transition diagrams for the Main and Backup CPUs."""
import math

from ppicfig10_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar,
                              _circle, _defs, _ellipse, _fig, _frame, _legend,
                              _line, _path, _poly, _rect, _mk, _series, _state,
                              make_registry)

FIGS, _reg = make_registry()

R = 16.0


@_reg
def fig_f03():
    o = []

    # Two framed boxes, offset diagonally as in the printed diagram.
    o.append(_rect(24, 16, 310, 132, fill="#ffffff", sw=1.4))   # Main CPU
    o.append(_rect(222, 158, 310, 150, fill="#ffffff", sw=1.4))  # Backup CPU

    # Main CPU states.
    m0, m1, m2 = (74, 92), (178, 48), (288, 48)
    m3, m4 = (288, 96), (178, 126)
    # Backup CPU states.
    b0, b1, b2 = (288, 226), (392, 182), (500, 182)
    b3, b4 = (500, 226), (392, 274)

    def ends(c1, c2):
        dx, dy = c2[0] - c1[0], c2[1] - c1[1]
        d = math.hypot(dx, dy)
        ux, uy = dx / d, dy / d
        gap = R + 1.8
        return (c1[0] + ux * gap, c1[1] + uy * gap,
                c2[0] - ux * gap, c2[1] - uy * gap)

    def arrow(c1, c2):
        return _ar(*ends(c1, c2))

    # Main CPU transitions.
    o.append(arrow(m0, m1))
    o.append(arrow(m1, m2))
    o.append(arrow(m0, m3))
    o.append(arrow(m0, m4))
    # Backup CPU transitions.
    o.append(arrow(b0, b1))
    o.append(arrow(b1, b2))
    o.append(arrow(b0, b3))
    o.append(arrow(b0, b4))

    # Dashed transfer connector MC3 -> BC0 (with a plain arrowhead).
    o.append(_line(288, 114, 288, 201, sw=1.6, dash="5 4", color=BLUE))
    o.append(_poly([(283, 200), (293, 200), (288, 209)],
                   fill=BLUE, sw=0, color=BLUE))

    # State circles (drawn over the line ends).
    o.append(_state(*m0, R, 0, "MC₀"))
    o.append(_state(*m1, R, 1, "MC₁"))
    o.append(_state(*m2, R, 2, "MC₂"))
    o.append(_state(*m3, R, 3, "MC₃"))
    o.append(_state(*m4, R, 4, "MC₄"))
    o.append(_state(*b0, R, 3, "BC₀"))
    o.append(_state(*b1, R, 5, "BC₁"))
    o.append(_state(*b2, R, 6, "BC₂"))
    o.append(_state(*b3, R, 7, "BC₃"))
    o.append(_state(*b4, R, 8, "BC₄"))

    # Transition-rate labels (Unicode lambda, plain-text subscript markers).
    for x, y, s in [
        (126, 63, "λ₁ MC"), (233, 41, "λ₂ MC"),
        (181, 90, "λ₃ MC"), (126, 116, "λ₄ MC"),
        (340, 196, "λ₁ BC"), (446, 176, "λ₂ BC"),
        (394, 219, "λ₃ BC"), (340, 262, "λ₄ BC"),
    ]:
        o.append(T(x, y, s, 7.2, color=INK))

    # Box headings.
    o.append(T(42, 31, "Main CPU", 8.6, anchor="start", color=INK,
               weight="bold"))
    o.append(T(246, 280, "Backup", 8.6, anchor="start", color=INK,
               weight="bold"))
    o.append(T(246, 292, "CPU", 8.6, anchor="start", color=INK,
               weight="bold"))

    return _mk(
        3, o,
        "Markov transition diagram for the Main CPU and the Backup CPU",
        "Sơ đồ Markov chuyển trạng thái của CPU chính và CPU dự phòng",
        "Markov transition diagram for the Main CPU and the Backup CPU",
        "Sơ đồ chuyển trạng thái Markov cho CPU chính và CPU dự phòng.",
        "Markov transition diagrams of the main and backup central "
        "processing units.",
        h=340)
