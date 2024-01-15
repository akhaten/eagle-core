# Description

---

::: eaglecore.signal.processing.normalize
    options:
        show_source: true
        show_root_heading: true

??? note "Formula"

    === "Render"

        \begin{align}
        s_{normalized} &= (s - s_{min}) 
        \times \frac{new_{max} - new_{min}}{s_{max} - s_{min}} + new_{min}
        \end{align}

    === "Latex"

        ```latex
        \begin{align}
        s_{normalized} &= (s - s_{min}) 
        \times \frac{new_{max} - new_{min}}{s_{max} - s_{min}} + new_{min}
        \end{align}
        ```

---

::: eaglecore.signal.processing.average_method
    options:
        show_source: true
        show_root_heading: true

??? note "Formula"

    === "Render"

        \begin{align}
        graylevel &= \frac{ red + green + blue}{3}
        \end{align}

    === "Latex"

        ```latex
        \begin{align}
        graylevel &= \frac{ red + green + blue}{3}
        \end{align}
        ```

---

::: eaglecore.signal.processing.luminosity_method
    options:
        show_source: true
        show_root_heading: true

??? note "Formula"

    === "Render"

        \begin{align}
        graylevel &= 0.299 \times red + 0.587 \times green + 0.114 \times blue
        \end{align}

    === "Latex"

        ```latex
        \begin{align}
        graylevel &= 0.299 \times red + 0.587 \times green + 0.114 \times blue
        \end{align}
        ```

---

<!-- ::: eaglecore.signal.processing.nb_graylevel
    options:
        show_source: true
        show_root_heading: true -->



<!-- ::: eaglecore.signal.processing.dynamic_graylevel
    options:
        show_source: true
        show_root_heading: true -->

