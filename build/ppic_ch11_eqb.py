# -*- coding: utf-8 -*-
"""Equation strings 17-33 for PPIC Chapter 11, transcribed from rendered pages p279-p280."""

EQ = {
    17: "u = sat(ξ̇<sub>d</sub>) + u<sub>cp</sub>",
    18: (
        "ξ̇<sub>d</sub> = −[k<sub>NP</sub>x<sub>1</sub> + k<sub>NI</sub>"
        "∫<sub>0</sub><sup>t</sup>x<sub>1</sub>(s)ds] − γq<sub>R</sub>"
        "[θ̂<sub>1</sub>x<sub>4</sub> + θ̂<sub>2</sub>"
        "∫<sub>0</sub><sup>t</sup>x<sub>4</sub>(s)ds]"
    ),
    19: (
        "u<sub>cp</sub> = −k<sub>g</sub>th(e<sub>g</sub>) "
        "− [q<sub>E1</sub> + κ<sub>g2</sub>κ<sub>f3</sub> "
        "− κ<sub>g1</sub><sup>2</sup>ch<sup>−2</sup>"
        "(∫<sub>t0</sub><sup>t</sup>e<sub>ξ</sub>(s)ds)]"
        "th(∫<sub>t0</sub><sup>t</sup>e<sub>ξ</sub>(s)ds)<br>"
        "+ [q<sub>E2</sub>κ<sub>f1</sub> + κ<sub>g2</sub>κ<sub>f3</sub> "
        "+ κ<sub>g1</sub>κ<sub>g2</sub>ch<sup>−2</sup>"
        "(∫<sub>t0</sub><sup>t</sup>e<sub>ξ</sub>(s)ds)]th(e<sub>f</sub>)"
    ),
    20: (
        "e<sub>g</sub> = e<sub>ξ</sub> "
        "+ κ<sub>g1</sub>th(∫<sub>t0</sub><sup>t</sup>e<sub>ξ</sub>(s)ds) "
        "+ κ<sub>g2</sub>th(e<sub>f</sub>)"
    ),
    21: (
        "ė<sub>f</sub> = ch<sup>2</sup>(e<sub>f</sub>)"
        "[−κ<sub>f1</sub>e<sub>g</sub> "
        "+ κ<sub>f2</sub>th(∫<sub>0</sub><sup>t</sup>e<sub>ξ</sub>(s)ds) "
        "− κ<sub>f3</sub>th(e<sub>f</sub>)]"
    ),
    22: "e<sub>ξ</sub> = ξ − ξ<sub>d</sub>",
    23: (
        "sat(z) = {<br>"
        "u<sub>max</sub> − u<sub>cp</sub>, z > u<sub>max</sub> − u<sub>cp</sub><br>"
        "z, u<sub>min</sub> − u<sub>cp</sub> ≤ z ≤ u<sub>max</sub> − u<sub>cp</sub>, z ∈ R<br>"
        "u<sub>min</sub> − u<sub>cp</sub>, z < u<sub>min</sub> − u<sub>cp</sub><br>"
        "}"
    ),
    24: (
        "th(z) = (e<sup>z</sup> − e<sup>−z</sup>)/(e<sup>z</sup> + e<sup>−z</sup>), "
        "z ∈ R"
    ),
    25: "ch(z) = (e<sup>z</sup> + e<sup>−z</sup>)/2, z ∈ R",
    26: "θ̂̇<sub>1</sub> = π<sub>1</sub>γq<sub>R</sub>x<sub>1</sub>x<sub>4</sub>",
    27: (
        "θ̂̇<sub>2</sub> = π<sub>2</sub>γq<sub>R</sub>x<sub>1</sub>"
        "∫<sub>t0</sub><sup>t</sup>x<sub>4</sub>(s)ds"
    ),
    28: (
        "k<sub>NP</sub> ≥ q<sub>R</sub>P<sub>0</sub>"
        "(Ω<sub>P</sub> + Ω<sub>S</sub>)/"
        "[2(1 − γ)ηG<sub>r</sub>Ω<sub>P</sub>Ω<sub>S</sub>] + ε<sub>NP</sub>"
    ),
    29: "κ<sub>f2</sub> = (q<sub>E1</sub>/q<sub>E2</sub>)κ<sub>g2</sub>",
    30: "u<sub>min</sub> ≤ u<sub>cp</sub> ≤ u<sub>max</sub>",
    31: (
        "κ<sub>g2</sub>κ<sub>f1</sub> − κ<sub>g1</sub> "
        "− G<sub>r</sub>/ε<sub>NP</sub> − γ<sub>w</sub> > 0"
    ),
    32: (
        "q<sub>E1</sub>κ<sub>g1</sub> "
        "− (G<sub>r</sub>/ε<sub>NP</sub>)κ<sub>g1</sub><sup>2</sup> > 0"
    ),
    33: (
        "q<sub>E2</sub>κ<sub>f3</sub> "
        "− (G<sub>r</sub>/ε<sub>NP</sub>)κ<sub>g2</sub><sup>2</sup> > 0"
    ),
}
