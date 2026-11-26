# -*- coding: utf-8 -*-
"""Equation strings 1-16 for PPIC Chapter 11, transcribed from rendered pages p276-p279."""

EQ = {
    1: (
        "{<br>"
        "ṅ<sub>r</sub> = (ρ<sub>r</sub> − β)/Λ · n<sub>r</sub> + β/Λ · c<sub>r</sub> "
        "+ (α<sub>R</sub>/Λ) · n<sub>r</sub>(T<sub>R</sub> − T<sub>R,m</sub>),<br>"
        "ċ<sub>r</sub> = λ(n<sub>r</sub> − c<sub>r</sub>),<br>"
        "Ṫ<sub>R</sub> = −(Ω<sub>P</sub>/μ<sub>R</sub>)(T<sub>R</sub> − T<sub>H</sub>) "
        "+ (P<sub>0</sub>/μ<sub>R</sub>)n<sub>r</sub>,<br>"
        "Ṫ<sub>H</sub> = (Ω<sub>P</sub>/μ<sub>H</sub>)(T<sub>R</sub> − T<sub>H</sub>) "
        "− (Ω<sub>S</sub>/μ<sub>H</sub>)(T<sub>H</sub> − T<sub>S</sub>),<br>"
        "ḣ<sub>r</sub> = v<sub>r</sub>,<br>"
        "}"
    ),
    2: (
        "ρ<sub>r</sub> = G<sub>r</sub>h<sub>r</sub>"
        "<br><i>where:</i> n<sub>r</sub> is the relative neutron power; c<sub>r</sub> is the "
        "relative concentration of the delayed neutron precursor; β is the fraction of the "
        "delayed neutrons; Λ is the effective prompt neutron life time; ρ<sub>r</sub> is the "
        "reactivity provided by the control rods; λ is the effective radioactive decay "
        "constant of the delayed neutron precursor; T<sub>R</sub> and α<sub>R</sub> are "
        "respectively the temperature and reactivity feedback coefficient of the reactor "
        "core constituted by both the fuel elements and the reflector; T<sub>R,m</sub> is the "
        "initial equilibrium value of T<sub>R</sub>; P<sub>0</sub> is the rated thermal power; "
        "T<sub>H</sub> is the average helium temperature of the primary loop, T<sub>S</sub> is "
        "the average coolant temperature of the OTSG secondary side; Ω<sub>P</sub> is the heat "
        "transfer coefficient between the helium and the reactor core; Ω<sub>S</sub> is the "
        "heat transfer coefficient between the two sides of the OTSG; μ<sub>R</sub> and "
        "μ<sub>H</sub> is respectively the total heat capacities of the reactor core and helium "
        "flow inside the primary loop; M<sub>S</sub> is the mass flowrate times the heat "
        "capacity of the secondary water/steam flow; constant G<sub>r</sub> is the differential "
        "worth of the control rod; h<sub>r</sub> is total control rod position; v<sub>r</sub> is "
        "the designed control rod speed signal."
    ),
    3: (
        "{<br>"
        "δn<sub>r</sub> = n<sub>r</sub> − n<sub>r0</sub>,<br>"
        "δc<sub>r</sub> = c<sub>r</sub> − c<sub>r0</sub>,<br>"
        "δT<sub>R</sub> = T<sub>R</sub> − T<sub>R0</sub>,<br>"
        "δT<sub>H</sub> = T<sub>H</sub> − T<sub>H0</sub>,<br>"
        "δT<sub>S</sub> = T<sub>S</sub> − T<sub>S0</sub>,<br>"
        "δh<sub>r</sub> = h<sub>r</sub> − h<sub>r0</sub>.<br>"
        "}"
    ),
    4: "δT<sub>S</sub> ≡ 0.",
    5: (
        "x = [x<sub>1</sub> x<sub>2</sub> x<sub>3</sub> x<sub>4</sub> x<sub>5</sub>]<sup>T</sup> "
        "= [δn<sub>r</sub> δc<sub>r</sub> δT<sub>R</sub> δT<sub>H</sub> "
        "δT<sub>S</sub>]<sup>T</sup>"
    ),
    6: "ξ = δh<sub>r</sub>",
    7: "u = v<sub>r</sub>",
    8: (
        "y = [x<sub>1</sub> x<sub>4</sub> ξ]<sup>T</sup>"
        "<br><i>where</i> x is the state-vector of the NSSM; [x<sup>T</sup> ξ]<sup>T</sup> "
        "constitutes the state-vector of the whole system; u is the control input, y is the "
        "measured system output."
    ),
    9: (
        "{<br>"
        "ẋ = f(x) + g(x)ξ,<br>"
        "ξ̇ = u,<br>"
        "y = h(x, ξ),<br>"
        "}"
    ),
    10: (
        "f(x) = [<br>"
        "−(β/Λ)(x<sub>1</sub> − x<sub>2</sub>) + (α<sub>R</sub>/Λ)"
        "(n<sub>r0</sub> + x<sub>1</sub>)x<sub>3</sub>,<br>"
        "λ(x<sub>1</sub> − x<sub>2</sub>),<br>"
        "(P<sub>0</sub>/μ<sub>R</sub>)x<sub>1</sub> − (Ω<sub>P</sub>/μ<sub>R</sub>)"
        "(x<sub>3</sub> − x<sub>4</sub>),<br>"
        "(Ω<sub>P</sub>/μ<sub>H</sub>)(x<sub>3</sub> − x<sub>4</sub>) "
        "− (Ω<sub>S</sub>/μ<sub>H</sub>)x<sub>4</sub><br>"
        "]<sup>T</sup>"
    ),
    11: (
        "g(x) = [(G<sub>r</sub>/Λ)(n<sub>r0</sub> + x<sub>1</sub>)  "
        "O<sub>1×3</sub>]<sup>T</sup>"
    ),
    12: "h(x, ξ) = [x<sub>1</sub> x<sub>4</sub> ξ]<sup>T</sup>",
    13: "ż = F(z, v)",
    14: "(∂U/∂z)F(z, v) ≤ −σ(‖z‖) + ω(‖v‖)",
    15: "u = u(y)",
    16: "u<sub>min</sub> ≤ u ≤ u<sub>max</sub>",
}
