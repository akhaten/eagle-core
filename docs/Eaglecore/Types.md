# Description

---

::: eaglecore.types.snr_db
    options:
        show_source: true
        show_root_heading: true

??? note "Formula"

    === "Render"

        \begin{align}
        SNR_{dB} &= 10 \times log_{10}(SNR) \\
        \frac{SNR_{dB}}{10} &= log_{10}(SNR) \\
        SNR &= 10^{\frac{SNR_{dB}}{10}}
        \end{align}

    === "Latex"

        ```latex
        \begin{align}
        SNR_{dB} &= 10 \times log_{10}(SNR) \\
        \frac{SNR_{dB}}{10} &= log_{10}(SNR) \\
        SNR &= 10^{\frac{SNR_{dB}}{10}}
        \end{align}
        ```
??? warning
    Do not confusion with formula using amplitudes. 
    See [wiki](https://en.wikipedia.org/wiki/Signal-to-noise_ratio).

---

::: eaglecore.types.snr
    options:
        show_source: true
        show_root_heading: true

??? note "Formula"

    === "Render"

        \begin{align}
        SNR &= 10^{\frac{SNR_{dB}}{10}} \\
        \frac{SNR_{dB}}{10} &= log_{10}(SNR) \\
        SNR_{dB} &= 10 \times log_{10}(SNR) \\
        \end{align}

    === "Latex"

        ```latex
        \begin{align}
        SNR_{dB} &= 10 \times log_{10}(SNR) \\
        \frac{SNR_{dB}}{10} &= log_{10}(SNR) \\
        SNR &= 10^{\frac{SNR_{dB}}{10}}
        \end{align}
        ```
??? warning
    Do not confusion with formula using amplitudes. 
    See [wiki](https://en.wikipedia.org/wiki/Signal-to-noise_ratio).

