# Description

---

::: eaglecore.psf.gaussian1d
    options:
        show_source: true
        show_root_heading: true

??? note "Formula"

    === "Render"

        \begin{align}
        G_{\sigma, \mu}(x) 
        = \frac{1}{\sqrt{2 \pi} \sigma} \times
        e^{-\frac{(x - \mu)^2}{2\sigma^{2}}}
        \end{align}

    === "Latex"

        ```latex
        \begin{align}
        G_{\sigma, \mu}(x) 
        = \frac{1}{\sqrt{2 \pi} \sigma} \times
        e^{-\frac{(x - \mu)^2}{2\sigma^{2}}}
        \end{align}
        ```

---

::: eaglecore.psf.gaussian2d
    options:
        show_source: true
        show_root_heading: true

??? note "Formula"

    === "Render"
    
        \begin{align}
        G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_{0}, x_{1}) 
        = \frac{1}{2 \pi \sigma_0 \sigma_1} \times
        e^{-\frac{(x_0 - \mu_0)^2}{2\sigma_{0}^{2}} - \frac{(x_1 - \mu_1)^2}{2\sigma_{1}^{2}}}
        \end{align}

    === "Latex"
    
        ```latex
        \begin{align}
        G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_{0}, x_{1}) 
        = \frac{1}{2 \pi \sigma_0 \sigma_1} \times
        e^{-\frac{(x_0 - \mu_0)^2}{2\sigma_{0}^{2}} - \frac{(x_1 - \mu_1)^2}{2\sigma_{1}^{2}}}
        \end{align}
        ```

??? tip "Gaussian 2D can be write with a product of two Gaussian 1D"

    === "Render"

        \begin{align}
        G_{\sigma_0, \mu_0}(x_0) \times G_{\sigma_1, \mu_1}(x_1)
        &= \frac{1}{\sqrt{2 \pi} \sigma_0} \times
        e^{-\frac{(x_0 - \mu_0)^2}{2\sigma_{0}^{2}}} \times
        \frac{1}{\sqrt{2 \pi} \sigma_1} \times
        e^{-\frac{(x_1 - \mu_1)^2}{2\sigma_{1}^{2}}} \\
        &= \frac{1}{2 \pi \sigma_0 \sigma_1} \times
        e^{
            -\frac{(x_0 - \mu_0)^2}{2\sigma_{0}^{2}} 
            - \frac{(x_1 - \mu_1)^2}{2\sigma_{1}^{2}}
        } \\
        &= G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_{0}, x_{1})
        \end{align}

    === "Latex"
    
        ```latex
        \begin{align}
        G_{\sigma_0, \mu_0}(x_0) \times G_{\sigma_1, \mu_1}(x_1)
        &= \frac{1}{\sqrt{2 \pi} \sigma_0} \times
        e^{-\frac{(x_0 - \mu_0)^2}{2\sigma_{0}^{2}}} \times
        \frac{1}{\sqrt{2 \pi} \sigma_1} \times
        e^{-\frac{(x_1 - \mu_1)^2}{2\sigma_{1}^{2}}} \\
        &= \frac{1}{2 \pi \sigma_0 \sigma_1} \times
        e^{
            -\frac{(x_0 - \mu_0)^2}{2\sigma_{0}^{2}} 
            - \frac{(x_1 - \mu_1)^2}{2\sigma_{1}^{2}}
        } \\
        &= G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_{0}, x_{1})
        \end{align}
        ```

---

::: eaglecore.psf.gaussian2d_dx0
    options:
        show_source: true
        show_root_heading: true

??? note "Formula"

    === "Render"
    
        \begin{align}
        \frac{d{G_{\sigma_0, \mu_0, \sigma_1, \mu_1}}}{d{x_{0}}}(x_{0}, x_{1})
        &= \frac{d}{d{x_{0}}} (\frac{1}{2 \pi \sigma_0 \sigma_1} \times
        e^{-\frac{(x_0 - \mu_0)^2}{2\sigma_{0}^{2}} - \frac{(x_1 - \mu_1)^2}{2\sigma_{1}^{2}}}) \\
        &= -2 \times \frac{x_0 - \mu_0}{2\sigma_{0}^{2}} \times \frac{1}{2 \pi \sigma_0 \sigma_1}
        e^{-\frac{(x_0 - \mu_0)^2}{2\sigma_{0}^{2}} - \frac{(x_1 - \mu_1)^2}{2\sigma_{1}^{2}}} \\
        &= -\frac{x_0 - \mu_0}{\sigma_{0}^{2}} \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_{0}, x_{1})
        \end{align}

    === "Latex"

        ```latex
        \begin{align}
        \frac{d{G_{\sigma_0, \mu_0, \sigma_1, \mu_1}}}{d{x_{0}}}(x_{0}, x_{1})
        &= \frac{d}{d{x_{0}}} (\frac{1}{2 \pi \sigma_0 \sigma_1} \times
        e^{-\frac{(x_0 - \mu_0)^2}{2\sigma_{0}^{2}} - \frac{(x_1 - \mu_1)^2}{2\sigma_{1}^{2}}}) \\
        &= -2 \times \frac{x_0 - \mu_0}{2\sigma_{0}^{2}} \times \frac{1}{2 \pi \sigma_0 \sigma_1}
        e^{-\frac{(x_0 - \mu_0)^2}{2\sigma_{0}^{2}} - \frac{(x_1 - \mu_1)^2}{2\sigma_{1}^{2}}} \\
        &= -\frac{x_0 - \mu_0}{\sigma_{0}^{2}} \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_{0}, x_{1})
        \end{align}
        ```

---

::: eaglecore.psf.gaussian2d_dx1
    options:
        show_source: true
        show_root_heading: true

??? note "Formula"

    === "Render"

        \begin{align}
        \frac{d{G_{\sigma_0, \mu_0, \sigma_1, \mu_1}}}{d{x_1}}(x_0, x_1)
        &= \frac{d}{d{x_1}} (\frac{1}{2 \pi \sigma_0 \sigma_1} \times
        e^{-\frac{(x_0 - \mu_0)^2}{2\sigma_{0}^{2}} - \frac{(x_1 - \mu_1)^2}{2\sigma_{1}{2}}}) \\
        &= -2 \times \frac{x_1 - \mu_1}{2\sigma_{1}^{2}} \times \frac{1}{2 \pi \sigma_0 \sigma_1}
        e^{-\frac{(x_0 - \mu_0)^2}{2\sigma_{0}^{2}} - \frac{(x_1 - \mu_1)^2}{2\sigma_{1}^{2}}} \\
        &= -\frac{x_1 - \mu_1}{\sigma_{1}^{2}} \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_{0}, x_{1}) \\
        \end{align}

    === "Latex"
    
        ```latex
        \begin{align}
        \frac{d{G_{\sigma_0, \mu_0, \sigma_1, \mu_1}}}{d{x_1}}(x_0, x_1)
        &= \frac{d}{d{x_1}} (\frac{1}{2 \pi \sigma_0 \sigma_1} \times
        e^{-\frac{(x_0 - \mu_0)^2}{2\sigma_{0}^{2}} - \frac{(x_1 - \mu_1)^2}{2\sigma_{1}{2}}}) \\
        &= -2 \times \frac{x_1 - \mu_1}{2\sigma_{1}^{2}} \times \frac{1}{2 \pi \sigma_0 \sigma_1}
        e^{-\frac{(x_0 - \mu_0)^2}{2\sigma_{0}^{2}} - \frac{(x_1 - \mu_1)^2}{2\sigma_{1}^{2}}} \\
        &= -\frac{x_1 - \mu_1}{\sigma_{1}^{2}} \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_{0}, x_{1}) \\
        \end{align}
        ```

---

::: eaglecore.psf.gaussian2d_d2x0
    options:
        show_source: true
        show_root_heading: true

??? note "Formula"

    === "Render"

        \begin{align}
        \frac{d^{2}{G_{\sigma_0, \mu_0, \sigma_1, \mu_1}}}{d^{2}{x_0}}(x_0, x_1)
        &= \frac{d}{d{x_0}} ( \frac{d{G_{\sigma_0, \mu_0, \sigma_1, \mu_1}}}{d{x_{0}}}(x_{0}, x_{1}) ) \\
        &= \frac{d}{d{x_0}} (- \frac{x_0 - \mu_0}{\sigma_{0}^{2}} \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1)) \\
        &= \frac{d}{d{x_0}} (- \frac{x_0 - \mu_0}{\sigma_{0}^{2}}) \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) + (- 
        \frac{x_0 - \mu_0}{\sigma_{0}^{2}}) \times \frac{d}{d{x_0}} G_{\sigma_0, \\mu_0, \sigma_1, \mu_1}(x_0, x_1) \\
        &= -\frac{1}{\sigma_{0}^{2}} \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) 
        + (- \frac{x_0 - \mu_0}{\sigma_{0}^{2}})^{2} \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) \\
        &= ( (\frac{x_0 - \mu_0}{\sigma_{0}^{2}})^{2} -\frac{1}{\sigma_{0}^{2}}) 
        \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) \\
        \end{align}

    === "Latex"

        ```latex
        \begin{align}
        \frac{d^{2}{G_{\sigma_0, \mu_0, \sigma_1, \mu_1}}}{d^{2}{x_0}}(x_0, x_1)
        &= \frac{d}{d{x_0}} ( \frac{d{G_{\sigma_0, \mu_0, \sigma_1, \mu_1}}}{d{x_{0}}}(x_{0}, x_{1}) ) \\
        &= \frac{d}{d{x_0}} (- \frac{x_0 - \mu_0}{\sigma_{0}^{2}} \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1)) \\
        &= \frac{d}{d{x_0}} (- \frac{x_0 - \mu_0}{\sigma_{0}^{2}}) \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) + (- 
        \frac{x_0 - \mu_0}{\sigma_{0}^{2}}) \times \frac{d}{d{x_0}} G_{\sigma_0, \\mu_0, \sigma_1, \mu_1}(x_0, x_1) \\
        &= -\frac{1}{\sigma_{0}^{2}} \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) 
        + (- \frac{x_0 - \mu_0}{\sigma_{0}^{2}})^{2} \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) \\
        &= ( (\frac{x_0 - \mu_0}{\sigma_{0}^{2}})^{2} -\frac{1}{\sigma_{0}^{2}}) 
        \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) \\
        \end{align}
        ```

---

::: eaglecore.psf.gaussian2d_d2x1
    options:
        show_source: true
        show_root_heading: true

??? note "Formula"

    === "Render"
    
        \begin{align}
        \frac{d^{2}{G_{\sigma_0, \mu_0, \sigma_1, \mu_1}}}{d^{2}{x_1}}(x_0, x_1)
        &= \frac{d}{d{x_1}} ( \frac{d{G_{\sigma_0, \mu_0, \sigma_1, \mu_1}}}{d{x_1}}(x_0, x_1) ) \\
        &= \frac{d}{d{x_1}} (- \frac{x_1 - \mu_1}{\sigma_{1}^{2}} \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1)) \\
        &= \frac{d}{d{x_1}} (- \frac{x_1 - \mu_1}{\sigma_{1}^{2}}) \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) + (- 
        \frac{x_1 - \mu_1}{\sigma_{1}^{2}}) \times \frac{d}{d{x_1}} G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) \\
        &= -\frac{1}{\sigma_{1}^{2}} \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) 
        + (- \frac{x_1 - \mu_1}{\sigma_{1}^{2}})^{2} \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) \\
        &= ( (\frac{x_1 - \mu_1}{\sigma_{1}^{2}})^{2} -\frac{1}{\sigma_{1}^{2}}) 
        \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) \\
        \end{align}

    === "Latex"
    
        ```latex
        \begin{align}
        \frac{d^{2}{G_{\sigma_0, \mu_0, \sigma_1, \mu_1}}}{d^{2}{x_1}}(x_0, x_1)
        &= \frac{d}{d{x_1}} ( \frac{d{G_{\sigma_0, \mu_0, \sigma_1, \mu_1}}}{d{x_1}}(x_0, x_1) ) \\
        &= \frac{d}{d{x_1}} (- \frac{x_1 - \mu_1}{\sigma_{1}^{2}} \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1)) \\
        &= \frac{d}{d{x_1}} (- \frac{x_1 - \mu_1}{\sigma_{1}^{2}}) \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) + (- 
        \frac{x_1 - \mu_1}{\sigma_{1}^{2}}) \times \frac{d}{d{x_1}} G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) \\
        &= -\frac{1}{\sigma_{1}^{2}} \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) 
        + (- \frac{x_1 - \mu_1}{\sigma_{1}^{2}})^{2} \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) \\
        &= ( (\frac{x_1 - \mu_1}{\sigma_{1}^{2}})^{2} -\frac{1}{\sigma_{1}^{2}}) 
        \times G_{\sigma_0, \mu_0, \sigma_1, \mu_1}(x_0, x_1) \\
        \end{align}
        ```

---