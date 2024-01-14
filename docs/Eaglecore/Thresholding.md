# Description

---

::: eaglecore.thresholding.soft
    options:
        show_source: true
        show_root_heading: true

??? note "Formula"

    === "Render"

        \begin{align} 
        Soft_{threshold}(x) 
        &= sign(x) \times max(|x| - threshold, ~0) \\
        &= \begin{cases}
        ~ -x & if  & ~ x \lt -threshold \\
        ~ ~ ~ 0  & if & ~ -threshold \lt x \lt threshold \\
        ~ ~ ~ x & if & ~ threshold \lt x
        \end{cases}
        \end{align}

    === "Latex"

        ```latex
        \begin{align} 
        Soft_{threshold}(x) 
        &= sign(x) \times max(|x| - threshold, ~0) \\
        &= \begin{cases}
        ~ -x & if  & ~ x \lt -threshold \\
        ~ ~ ~ 0  & if & ~ -threshold \lt x \lt threshold \\
        ~ ~ ~ x & if & ~ threshold \lt x
        \end{cases}
        \end{align}
        ```

---

::: eaglecore.thresholding.multidimensional_soft
    options:
        show_source: true
        show_root_heading: true

---

::: eaglecore.thresholding.singular_value
    options:
        show_source: true
        show_root_heading: true

??? note "Formula"

    === "Render"

        Let $U \Sigma V^{*}$ the singular value decomposition of x 
        (ie $x = U \Sigma V^{*}$).
        
        Thresholded $x$ will be :
        
        \begin{align} 
        U ~ Soft_{threshold}(\Sigma) ~ V^{*}
        \end{align}

    === "Latex"

        ```latex
        Let $U \Sigma V^{*}$ the singular value decomposition of x 
        (ie $x = U \Sigma V^{*}$).
        
        Thresholded $x$ will be :
        
        \begin{align} 
        U ~ Soft_{threshold}(\Sigma) ~ V^{*}
        \end{align}
        ```

??? question
    To learn more about singular value decomposition (SVD), see 
    [wiki](https://en.wikipedia.org/wiki/Singular_value_decomposition).

---

::: eaglecore.thresholding.singular_value_soft
    options:
        show_source: true
        show_root_heading: true

---