# Description

---

::: eaglecore.signal.measure.energy
    options:
        show_source: true
        show_root_heading: true


??? note "Formula in spatial domain"

    === "Render"

        \begin{align}
        E_{s} &= \sum\limits_{k=0}^{N} s[k]^2
        \end{align}

    === "Latex"

        ```latex
        \begin{align}
        E_{s} &= \sum\limits_{k=0}^{N} s[k]^2
        \end{align}
        ```
 
??? note "Formula in Fourier domain"

    === "Render"

        \begin{align}
        E_{S} &= \frac{1}{N} \sum\limits_{k=0}^{N} |S[k]|^2
        \end{align}

    === "Latex"

        ```latex
        \begin{align}
        E_{S} &= \frac{1}{N} \sum\limits_{k=0}^{N} |S[k]|^2
        \end{align}
        ```


??? tip "Perceval's theorem"
    Signal can be complex because Perceval theorem says
    that the energy in real domain is equal to the energy
    in Fourier (ie complex) domain.

---

::: eaglecore.signal.measure.power
    options:
        show_source: true
        show_root_heading: true

??? note "Formula in spatial domain"

    === "Render"

        \begin{align}
        P_{s} &= \frac{1}{N} \times E_{s}
        \end{align}

    === "Latex"

        ```latex
        \begin{align}
        P_{s} &= \frac{1}{N} \times E_{s}
        \end{align}
        ```

??? note "Formula in Fourier domain"

    === "Render"

        \begin{align}
        P_{S} &= \frac{1}{N} \times E_{S}
        \end{align}

    === "Latex"

        ```latex
        \begin{align}
        P_{S} &= \frac{1}{N} \times E_{S}
        \end{align}
        ```
        
---