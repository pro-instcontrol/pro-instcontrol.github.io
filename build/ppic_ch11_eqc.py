# -*- coding: utf-8 -*-
"""Equation strings 34-54 for PPIC Chapter 11.

Transcribed from the rendered page images p281.png-p284.png.  Eq. (34) has a
tofu box on its left-hand side in the PDF; from the surrounding proof text
("subsystem (34)", xi_d the setpoint of xi) the intended symbol is xi-dot.
"""

EQ = {
    34: "<i>ξ̇</i> = <i>f</i>(<i>x</i>) + <i>g</i>(<i>x</i>)<i>ξ</i><sub>d</sub>",

    35: "<i>ζ</i><sub>N</sub>(<i>x</i><sub>1</sub>, <i>x</i><sub>2</sub>) = "
        "Λ[(1 + <i>x</i><sub>1</sub>/<i>n</i><sub>r0</sub>) − ln(1 + <i>x</i><sub>1</sub>/<i>n</i><sub>r0</sub>)] "
        "+ (β/λ)[(1 + <i>x</i><sub>2</sub>/<i>n</i><sub>r0</sub>) − ln(1 + <i>x</i><sub>2</sub>/<i>n</i><sub>r0</sub>)]",

    36: "<i>V</i><sub>N</sub>(<i>x</i><sub>1</sub>, <i>x</i><sub>2</sub>) = "
        "<i>ζ</i><sub>N</sub>(<i>x</i><sub>1</sub>, <i>x</i><sub>2</sub>) "
        "+ (<i>G</i><sub>r</sub><i>k</i><sub>NI</sub>/2)[∫<sub>0</sub><sup><i>t</i></sup><i>x</i><sub>1</sub>(<i>s</i>)d<i>s</i>]<sup>2</sup>",

    37: "<i>V̇</i><sub>N</sub>(<i>x</i><sub>1</sub>, <i>x</i><sub>2</sub>) = "
        "−β(<i>x</i><sub>1</sub> − <i>x</i><sub>2</sub>)<sup>2</sup>/"
        "[(<i>n</i><sub>r0</sub> + <i>x</i><sub>1</sub>)(<i>n</i><sub>r0</sub> + <i>x</i><sub>1</sub>)] "
        "+ <i>x</i><sub>1</sub>[<i>G</i><sub>r</sub><i>ξ</i><sub>d</sub> + α<sub>R</sub><i>x</i><sub>3</sub> "
        "+ κ<sub>I</sub>∫<sub>0</sub><sup><i>t</i></sup><i>x</i><sub>1</sub>(<i>s</i>)d<i>s</i>]",

    38: "<i>ζ</i><sub>T</sub>(<i>x</i><sub>3</sub>, <i>x</i><sub>4</sub>) = "
        "½(μ<sub>R</sub><i>x</i><sub>3</sub><sup>2</sup> + μ<sub>H</sub><i>x</i><sub>4</sub><sup>2</sup>)",

    39: "<i>V</i><sub>T</sub>(<i>x</i><sub>3</sub>, <i>x</i><sub>4</sub>) = "
        "(1 − γ)<i>ζ</i><sub>T</sub>(<i>x</i><sub>3</sub>, <i>x</i><sub>4</sub>) "
        "+ γ<i>ς</i><sub>T</sub>(<i>x</i><sub>3</sub>, <i>x</i><sub>4</sub>)",

    40: "<i>ς</i><sub>T</sub>(<i>x</i><sub>3</sub>, <i>x</i><sub>4</sub>) = "
        "1/(2μ<sub>R</sub>)[μ<sub>R</sub><i>x</i><sub>3</sub> + μ<sub>H</sub><i>x</i><sub>4</sub> "
        "+ Ω<sub>S</sub>∫<sub>0</sub><sup><i>t</i></sup><i>x</i><sub>4</sub>(<i>s</i>)d<i>s</i>]<sup>2</sup>",

    41: "<i>V̇</i><sub>T</sub>(<i>x</i><sub>3</sub>, <i>x</i><sub>4</sub>) = "
        "<i>P</i><sub>0</sub><i>x</i><sub>1</sub><i>x</i><sub>3</sub> "
        "+ γ<i>P</i><sub>0</sub><i>x</i><sub>1</sub>[μ<sub>H</sub>/μ<sub>R</sub><i>x</i><sub>4</sub> "
        "+ Ω<sub>S</sub>/μ<sub>R</sub>∫<sub>0</sub><sup><i>t</i></sup><i>x</i><sub>4</sub>(<i>s</i>)d<i>s</i>] "
        "− (1 − γ)(1 − η)[Ω<sub>P</sub>(<i>x</i><sub>3</sub> − <i>x</i><sub>4</sub>)<sup>2</sup> "
        "+ Ω<sub>S</sub><i>x</i><sub>4</sub><sup>2</sup>]<br>"
        "− (1 − γ)η[(Ω<sub>P</sub> + Ω<sub>S</sub>)"
        "(<i>x</i><sub>4</sub> − Ω<sub>P</sub>/(Ω<sub>P</sub> + Ω<sub>S</sub>)<i>x</i><sub>3</sub>)<sup>2</sup> "
        "+ Ω<sub>P</sub>Ω<sub>S</sub>/(Ω<sub>P</sub> + Ω<sub>S</sub>)<i>x</i><sub>4</sub><sup>2</sup>]",

    42: "<i>V</i><sub>1</sub>(<i>x</i>) = <i>V</i><sub>N</sub>(<i>x</i><sub>1</sub>, <i>x</i><sub>2</sub>) "
        "+ (<i>q</i><sub>R</sub>/<i>P</i><sub>0</sub>)<i>V</i><sub>T</sub>(<i>x</i><sub>3</sub>, <i>x</i><sub>4</sub>)",

    43: "<i>V̇</i><sub>1</sub>(<i>x</i>) = "
        "−β(<i>x</i><sub>1</sub> − <i>x</i><sub>2</sub>)<sup>2</sup>/"
        "[(<i>n</i><sub>r0</sub> + <i>x</i><sub>1</sub>)(<i>n</i><sub>r0</sub> + <i>x</i><sub>1</sub>)] "
        "− (1 − γ)(1 − η)(<i>q</i><sub>R</sub>/<i>P</i><sub>0</sub>)"
        "[Ω<sub>P</sub>(<i>x</i><sub>3</sub> − <i>x</i><sub>4</sub>)<sup>2</sup> + Ω<sub>S</sub><i>x</i><sub>4</sub><sup>2</sup>]<br>"
        "− (1 − γ)η(Ω<sub>P</sub> + Ω<sub>S</sub>)(<i>q</i><sub>R</sub>/<i>P</i><sub>0</sub>)"
        "(<i>x</i><sub>4</sub> − Ω<sub>P</sub>/(Ω<sub>P</sub> + Ω<sub>S</sub>)<i>x</i><sub>3</sub>)<sup>2</sup> "
        "− <i>q</i><sub>R</sub>/(2Σ<sub>R</sub>){<i>x</i><sub>3</sub><sup>2</sup> "
        "+ [<i>x</i><sub>3</sub> − Σ<sub>R</sub>(1 + α<sub>R</sub>/<i>q</i><sub>R</sub>)<i>x</i><sub>1</sub>]<sup>2</sup>}<br>"
        "+ <i>G</i><sub>r</sub><i>x</i><sub>1</sub>{<i>ξ̃</i><sub>d</sub> "
        "+ ½(<i>q</i><sub>R</sub>Σ<sub>R</sub>/<i>G</i><sub>r</sub>)"
        "(1 + α<sub>R</sub>/<i>q</i><sub>R</sub>)<sup>2</sup><i>x</i><sub>1</sub><br>"
        "+ κ<sub>N</sub>∫<sub>0</sub><sup><i>t</i></sup><i>x</i><sub>1</sub>(<i>s</i>)d<i>s</i> "
        "+ γ<i>q</i><sub>R</sub>[μ<sub>H</sub>/(<i>G</i><sub>r</sub>μ<sub>R</sub>)<i>x</i><sub>4</sub> "
        "+ Ω<sub>S</sub>/(<i>G</i><sub>r</sub>μ<sub>R</sub>)"
        "∫<sub>0</sub><sup><i>t</i></sup><i>x</i><sub>4</sub>(<i>s</i>)d<i>s</i>]}",

    44: "Σ<sub>R</sub> = (Ω<sub>P</sub> + Ω<sub>S</sub>)<i>P</i><sub>0</sub>/"
        "[(1 − γ)ηΩ<sub>P</sub>Ω<sub>S</sub>]",

    45: "θ<sub>1</sub> = μ<sub>H</sub>/(<i>G</i><sub>r</sub>μ<sub>R</sub>)",

    46: "θ<sub>2</sub> = Ω<sub>S</sub>/(<i>G</i><sub>r</sub>μ<sub>R</sub>)",

    47: "<i>V̇</i><sub>1</sub>(<i>x</i>) ≤ "
        "−β(<i>x</i><sub>1</sub> − <i>x</i><sub>2</sub>)<sup>2</sup>/"
        "[(<i>n</i><sub>r0</sub> + <i>x</i><sub>1</sub>)(<i>n</i><sub>r0</sub> + <i>x</i><sub>1</sub>)] "
        "− <i>G</i><sub>r</sub>ε<sub>NP</sub><i>x</i><sub>1</sub><sup>2</sup> "
        "− (1 − γ)(1 − η)(<i>q</i><sub>R</sub>/<i>P</i><sub>0</sub>)"
        "[Ω<sub>P</sub>(<i>x</i><sub>3</sub> − <i>x</i><sub>4</sub>)<sup>2</sup> + Ω<sub>S</sub><i>x</i><sub>4</sub><sup>2</sup>]<br>"
        "− (1 − γ)η(Ω<sub>P</sub> + Ω<sub>S</sub>)(<i>q</i><sub>R</sub>/<i>P</i><sub>0</sub>)"
        "(<i>x</i><sub>4</sub> − Ω<sub>P</sub>/(Ω<sub>P</sub> + Ω<sub>S</sub>)<i>x</i><sub>3</sub>)<sup>2</sup> "
        "− <i>q</i><sub>R</sub>/(2Σ<sub>R</sub>){<i>x</i><sub>3</sub><sup>2</sup> "
        "+ [<i>x</i><sub>3</sub> − Σ<sub>R</sub>(1 + α<sub>R</sub>/<i>q</i><sub>R</sub>)<i>x</i><sub>1</sub>]<sup>2</sup>}<br>"
        "− γ<i>q</i><sub>R</sub>[θ̃<sub>1</sub><i>x</i><sub>1</sub><i>x</i><sub>4</sub> "
        "+ θ̃<sub>2</sub><i>x</i><sub>1</sub>∫<sub>0</sub><sup><i>t</i></sup><i>x</i><sub>4</sub>(<i>s</i>)d<i>s</i>],",

    48: "θ̃<sub>i</sub> = θ̂<sub>i</sub> − θ<sub>i</sub>, (<i>i</i> = 1, 2)",

    49: "<i>V</i><sub>2</sub>(<i>x</i>, θ̃) = <i>V</i><sub>1</sub>(<i>x</i>) "
        "+ ½θ̃<sup>T</sup>Π<sup>−1</sup>θ̃",

    50: "θ̃ = [θ̃<sub>1</sub>  θ̃<sub>2</sub>]<sup>T</sup>",

    51: "Π = [<i>π</i><sub>1</sub>  0<br>0  <i>π</i><sub>2</sub>], "
        "<i>π</i><sub>i</sub> > 0, (<i>i</i> = 1, 2)",

    52: "<i>V̇</i><sub>2</sub>(<i>x</i>, θ̃) ≤ "
        "−β(<i>x</i><sub>1</sub> − <i>x</i><sub>2</sub>)<sup>2</sup>/"
        "[(<i>n</i><sub>r0</sub> + <i>x</i><sub>1</sub>)(<i>n</i><sub>r0</sub> + <i>x</i><sub>1</sub>)] "
        "− <i>G</i><sub>r</sub>ε<sub>NP</sub><i>x</i><sub>1</sub><sup>2</sup> "
        "− (1 − γ)(1 − η)(<i>q</i><sub>R</sub>/<i>P</i><sub>0</sub>)"
        "[Ω<sub>P</sub>(<i>x</i><sub>3</sub> − <i>x</i><sub>4</sub>)<sup>2</sup> + Ω<sub>S</sub><i>x</i><sub>4</sub><sup>2</sup>]<br>"
        "− (1 − γ)η(Ω<sub>P</sub> + Ω<sub>S</sub>)(<i>q</i><sub>R</sub>/<i>P</i><sub>0</sub>)"
        "(<i>x</i><sub>4</sub> − Ω<sub>P</sub>/(Ω<sub>P</sub> + Ω<sub>S</sub>)<i>x</i><sub>3</sub>)<sup>2</sup> "
        "− <i>q</i><sub>R</sub>/(2Σ<sub>R</sub>){<i>x</i><sub>3</sub><sup>2</sup> "
        "+ [<i>x</i><sub>3</sub> − Σ<sub>R</sub>(1 + α<sub>R</sub>/<i>q</i><sub>R</sub>)<i>x</i><sub>1</sub>]<sup>2</sup>}<br>"
        "− γ<i>q</i><sub>R</sub>[θ̃<sub>1</sub><i>x</i><sub>1</sub><i>x</i><sub>4</sub> "
        "+ θ̃<sub>2</sub><i>x</i><sub>1</sub>∫<sub>0</sub><sup><i>t</i></sup><i>x</i><sub>4</sub>(<i>s</i>)d<i>s</i>] "
        "+ θ̃<sup>T</sup>Π<sup>−1</sup>θ̂̇",

    53: "<i>V̇</i><sub>2</sub>(<i>x</i>, θ̃) ≤ "
        "−β(<i>x</i><sub>1</sub> − <i>x</i><sub>2</sub>)<sup>2</sup>/"
        "[(<i>n</i><sub>r0</sub> + <i>x</i><sub>1</sub>)(<i>n</i><sub>r0</sub> + <i>x</i><sub>1</sub>)] "
        "− <i>G</i><sub>r</sub>ε<sub>NP</sub><i>x</i><sub>1</sub><sup>2</sup> "
        "− (1 − γ)(1 − η)(<i>q</i><sub>R</sub>/<i>P</i><sub>0</sub>)"
        "[Ω<sub>P</sub>(<i>x</i><sub>3</sub> − <i>x</i><sub>4</sub>)<sup>2</sup> + Ω<sub>S</sub><i>x</i><sub>4</sub><sup>2</sup>]<br>"
        "− (1 − γ)η(Ω<sub>P</sub> + Ω<sub>S</sub>)(<i>q</i><sub>R</sub>/<i>P</i><sub>0</sub>)"
        "(<i>x</i><sub>4</sub> − Ω<sub>P</sub>/(Ω<sub>P</sub> + Ω<sub>S</sub>)<i>x</i><sub>3</sub>)<sup>2</sup> "
        "− <i>q</i><sub>R</sub>/(2Σ<sub>R</sub>){<i>x</i><sub>3</sub><sup>2</sup> "
        "+ [<i>x</i><sub>3</sub> − Σ<sub>R</sub>(1 + α<sub>R</sub>/<i>q</i><sub>R</sub>)<i>x</i><sub>1</sub>]<sup>2</sup>}",

    54: "{<br>"
        "<i>ξ̇</i><sub>d</sub> = −[<i>k</i><sub>NP</sub><i>x</i><sub>1</sub> "
        "+ <i>k</i><sub>NI</sub>∫<sub>0</sub><sup><i>t</i></sup><i>x</i><sub>1</sub>(<i>s</i>)d<i>s</i>] "
        "− γ<i>q</i><sub>R</sub>[θ̂<sub>1</sub><i>x</i><sub>4</sub> "
        "+ θ̂<sub>2</sub>∫<sub>0</sub><sup><i>t</i></sup><i>x</i><sub>4</sub>(<i>s</i>)d<i>s</i>]<br>"
        "θ̂̇<sub>1</sub> = <i>π</i><sub>1</sub>γ<i>q</i><sub>R</sub><i>x</i><sub>1</sub><i>x</i><sub>4</sub><br>"
        "θ̂̇<sub>2</sub> = <i>π</i><sub>2</sub>γ<i>q</i><sub>R</sub><i>x</i><sub>1</sub>"
        "∫<sub>0</sub><sup><i>t</i></sup><i>x</i><sub>4</sub>(<i>s</i>)d<i>s</i><br>}",
}
