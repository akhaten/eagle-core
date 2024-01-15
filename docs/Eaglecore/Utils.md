# Description

---

::: eaglecore.utils.circshift
    options:
        show_source: true
        show_root_heading: true

---

::: eaglecore.utils.fourier_diagonalization
    options:
        show_source: true
        show_root_heading: true

---

::: eaglecore.utils.make_bccb
    options:
        show_source: true
        show_root_heading: true

??? question "Understand the construction of BCCB matrix"

    ??? note "Step 1 : Build circshifted kernel"

        === "Render"
            
            \begin{align}
            h = \begin{bmatrix}
            h_{0, 0} & h_{0, 1} & h_{0, 2} \\
            h_{1, 0} & \bf{h_{1, 1}} & h_{1, 2} \\ 
            h_{2, 0} & h_{2, 1} & h_{2, 2}
            \end{bmatrix}
            \rightarrow \begin{bmatrix} 
            h_{0, 1} & h_{0, 2} & h_{0, 0} \\
            \bf{h_{1, 1}} & h_{1, 2} & h_{1, 0} \\
            h_{2, 1} & h_{2, 2} & h_{2, 0}
            \end{bmatrix}
            \rightarrow \begin{bmatrix} 
            \bf{h_{1, 1}} & h_{1, 2} & h_{1, 0} \\  
            h_{2, 1} & h_{2, 2} & h_{2, 0} \\
            h_{0, 1} & h_{0, 2} & h_{0, 0}
            \end{bmatrix} \\
            \end{align}

        === "Latex"

            ```latex
            \begin{align}
            h = \begin{bmatrix}
            h_{0, 0} & h_{0, 1} & h_{0, 2} \\
            h_{1, 0} & \bf{h_{1, 1}} & h_{1, 2} \\ 
            h_{2, 0} & h_{2, 1} & h_{2, 2}
            \end{bmatrix}
            \rightarrow \begin{bmatrix} 
            h_{0, 1} & h_{0, 2} & h_{0, 0} \\
            \bf{h_{1, 1}} & h_{1, 2} & h_{1, 0} \\
            h_{2, 1} & h_{2, 2} & h_{2, 0}
            \end{bmatrix}
            \rightarrow \begin{bmatrix} 
            \bf{h_{1, 1}} & h_{1, 2} & h_{1, 0} \\  
            h_{2, 1} & h_{2, 2} & h_{2, 0} \\
            h_{0, 1} & h_{0, 2} & h_{0, 0}
            \end{bmatrix} \\
            \end{align}
            ```
    ??? note "Step 2 : Build first column of BCCB matrix"

        === "Render"
            
            \begin{align}
            \begin{bmatrix}
            h_{1, 1} & h_{1, 2} & h_{1, 0} \\  
            h_{2, 1} & h_{2, 2} & h_{2, 0} \\
            \bf{h_{0, 1}} & \bf{h_{0, 2}} & \bf{h_{0, 0}}
            \end{bmatrix}
            \rightarrow \begin{bmatrix}
            \begin{array}{c}
            h_{1, 1} \\
            h_{2, 1} \\
            \bf{h_{0, 1}} \\
            \hline
            h_{1, 2} \\
            h_{2, 2} \\
            \bf{h_{0, 2}} \\
            \hline
            h_{1, 0} \\
            h_{2, 0} \\
            \bf{h_{0, 0}}
            \end{array}
            \end{bmatrix} \\
            \end{align}

        === "Latex"

            ```latex
            \begin{align}
            \begin{bmatrix}
            h_{1, 1} & h_{1, 2} & h_{1, 0} \\  
            h_{2, 1} & h_{2, 2} & h_{2, 0} \\
            \bf{h_{0, 1}} & \bf{h_{0, 2}} & \bf{h_{0, 0}}
            \end{bmatrix}
            \rightarrow \begin{bmatrix}
            \begin{array}{c}
            h_{1, 1} \\
            h_{2, 1} \\
            \bf{h_{0, 1}} \\
            \hline
            h_{1, 2} \\
            h_{2, 2} \\
            \bf{h_{0, 2}} \\
            \hline
            h_{1, 0} \\
            h_{2, 0} \\
            \bf{h_{0, 0}}
            \end{array}
            \end{bmatrix} \\
            \end{align}
            ```
    ??? note "Step 3 : Build first column-block of BCCB matrix"

        === "Render"
            
            \begin{align}
            \begin{bmatrix}
            \begin{array}{c}
            h_{1, 1} \\ h_{2, 1} \\ \bf{h_{0, 1}} \\
            \hline
            h_{1, 2} \\ h_{2, 2} \\ \bf{h_{0, 2}} \\
            \hline
            h_{1, 0} \\ h_{2, 0} \\ \bf{h_{0, 0}}
            \end{array}
            \end{bmatrix}
            &\rightarrow \begin{bmatrix}
            \begin{array}{c c}
            h_{1, 1} & \bf{h_{0, 1}} \\
            h_{2, 1} & h_{1, 1} \\
            \bf{h_{0, 1}} & h_{2, 1} \\
            \hline
            h_{1, 2} & \bf{h_{0, 2}} \\
            h_{2, 2} & h_{1, 2}\\
            \bf{h_{0, 2}} & h_{2, 2} \\
            \hline
            h_{1, 0} & \bf{h_{0, 0}} \\
            h_{2, 0} & h_{1, 0} \\
            \bf{h_{0, 0}} & h_{2, 0}
            \end{array}
            \end{bmatrix}
            \rightarrow \begin{bmatrix}
            \begin{array}{c c c}
            h_{1, 1} & \bf{h_{0, 1}} & h_{2, 1} \\
            h_{2, 1} & h_{1, 1} & \bf{h_{0, 1}} \\
            \bf{h_{0, 1}} & h_{2, 1} & h_{1, 1} \\
            \hline
            h_{1, 2} & \bf{h_{0, 2}} & h_{2, 2} \\
            h_{2, 2} & h_{1, 2} & \bf{h_{0, 2}} \\
            \bf{h_{0, 2}} & h_{2, 2} & h_{1, 2} \\
            \hline
            h_{1, 0} & \bf{h_{0, 0}} & h_{2, 0} \\
            h_{2, 0} & h_{1, 0} & \bf{h_{0, 0}} \\
            \bf{h_{0, 0}} & h_{2, 0} & h_{1, 0}
            \end{array}
            \end{bmatrix}
            \end{align}

        === "Latex"

            ```latex
            \begin{align}
            \begin{bmatrix}
            \begin{array}{c}
            h_{1, 1} \\ h_{2, 1} \\ \bf{h_{0, 1}} \\
            \hline
            h_{1, 2} \\ h_{2, 2} \\ \bf{h_{0, 2}} \\
            \hline
            h_{1, 0} \\ h_{2, 0} \\ \bf{h_{0, 0}}
            \end{array}
            \end{bmatrix}
            &\rightarrow \begin{bmatrix}
            \begin{array}{c c}
            h_{1, 1} & \bf{h_{0, 1}} \\
            h_{2, 1} & h_{1, 1} \\
            \bf{h_{0, 1}} & h_{2, 1} \\
            \hline
            h_{1, 2} & \bf{h_{0, 2}} \\
            h_{2, 2} & h_{1, 2}\\
            \bf{h_{0, 2}} & h_{2, 2} \\
            \hline
            h_{1, 0} & \bf{h_{0, 0}} \\
            h_{2, 0} & h_{1, 0} \\
            \bf{h_{0, 0}} & h_{2, 0}
            \end{array}
            \end{bmatrix}
            \rightarrow \begin{bmatrix}
            \begin{array}{c c c}
            h_{1, 1} & \bf{h_{0, 1}} & h_{2, 1} \\
            h_{2, 1} & h_{1, 1} & \bf{h_{0, 1}} \\
            \bf{h_{0, 1}} & h_{2, 1} & h_{1, 1} \\
            \hline
            h_{1, 2} & \bf{h_{0, 2}} & h_{2, 2} \\
            h_{2, 2} & h_{1, 2} & \bf{h_{0, 2}} \\
            \bf{h_{0, 2}} & h_{2, 2} & h_{1, 2} \\
            \hline
            h_{1, 0} & \bf{h_{0, 0}} & h_{2, 0} \\
            h_{2, 0} & h_{1, 0} & \bf{h_{0, 0}} \\
            \bf{h_{0, 0}} & h_{2, 0} & h_{1, 0}
            \end{array}
            \end{bmatrix}
            \end{align}
            ```

    ??? note "Step 4 : Build others columns-blocks of BCCB matrix"

        === "Render"
            
            \begin{align}
            \begin{bmatrix}
            \begin{array}{c c c}
            h_{1, 1} & h_{0, 1} & h_{2, 1} \\
            h_{2, 1} & h_{1, 1} & h_{0, 1} \\
            h_{0, 1} & h_{2, 1} & h_{1, 1} \\
            \hline
            h_{1, 2} & h_{0, 2} & h_{2, 2} \\
            h_{2, 2} & h_{1, 2} & h_{0, 2} \\
            h_{0, 2} & h_{2, 2} & h_{1, 2} \\
            \hline
            \bf{h_{1, 0}} & \bf{h_{0, 0}} & \bf{h_{2, 0}} \\
            \bf{h_{2, 0}} & \bf{h_{1, 0}} & \bf{h_{0, 0}} \\
            \bf{h_{0, 0}} & \bf{h_{2, 0}} & \bf{h_{1, 0}}
            \end{array}
            \end{bmatrix}
            &\rightarrow \begin{bmatrix}
            \begin{array}{c c c | c c c}
            h_{1, 1} & h_{0, 1} & h_{2, 1} & \bf{h_{1, 0}} & \bf{h_{0, 0}} & \bf{h_{2, 0}} \\
            h_{2, 1} & h_{1, 1} & h_{0, 1} & \bf{h_{2, 0}} & \bf{h_{1, 0}} & \bf{h_{0, 0}} \\
            h_{0, 1} & h_{2, 1} & h_{1, 1} & \bf{h_{0, 0}} & \bf{h_{2, 0}} & \bf{h_{1, 0}} \\
            \hline
            h_{1, 2} & h_{0, 2} & h_{2, 2} & h_{1, 1} & h_{0, 1} & h_{2, 1} \\
            h_{2, 2} & h_{1, 2} & h_{0, 2} & h_{2, 1} & h_{1, 1} & h_{0, 1} \\
            h_{0, 2} & h_{2, 2} & h_{1, 2} & h_{0, 1} & h_{2, 1} & h_{1, 1} \\
            \hline
            \bf{h_{1, 0}} & \bf{h_{0, 0}} & \bf{h_{2, 0}} & h_{1, 2} & h_{0, 2} & h_{2, 2} \\
            \bf{h_{2, 0}} & \bf{h_{1, 0}} & \bf{h_{0, 0}} & h_{2, 2} & h_{1, 2} & h_{0, 2} \\
            \bf{h_{0, 0}} & \bf{h_{2, 0}} & \bf{h_{1, 0}} & h_{0, 2} & h_{2, 2} & h_{1, 2}
            \end{array}
            \end{bmatrix} \\
            &\rightarrow \begin{bmatrix}
            \begin{array}{c c c | c c c | c c c}
            h_{1, 1} & h_{0, 1} & h_{2, 1} & \bf{h_{1, 0}} & \bf{h_{0, 0}} & \bf{h_{2, 0}} & h_{1, 2} & h_{0, 2} & h_{2, 2} \\
            h_{2, 1} & h_{1, 1} & h_{0, 1} & \bf{h_{2, 0}} & \bf{h_{1, 0}} & \bf{h_{0, 0}} & h_{2, 2} & h_{1, 2} & h_{0, 2} \\
            h_{0, 1} & h_{2, 1} & h_{1, 1} & \bf{h_{0, 0}} & \bf{h_{2, 0}} & \bf{h_{1, 0}} & h_{0, 2} & h_{2, 2} & h_{1, 2} \\
            \hline
            h_{1, 2} & h_{0, 2} & h_{2, 2} & h_{1, 1} & h_{0, 1} & h_{2, 1} & \bf{h_{1, 0}} & \bf{h_{0, 0}} & \bf{h_{2, 0}} \\
            h_{2, 2} & h_{1, 2} & h_{0, 2} & h_{2, 1} & h_{1, 1} & h_{0, 1} & \bf{h_{2, 0}} & \bf{h_{1, 0}} & \bf{h_{0, 0}} \\
            h_{0, 2} & h_{2, 2} & h_{1, 2} & h_{0, 1} & h_{2, 1} & h_{1, 1} & \bf{h_{0, 0}} & \bf{h_{2, 0}} & \bf{h_{1, 0}} \\
            \hline
            \bf{h_{1, 0}} & \bf{h_{0, 0}} & \bf{h_{2, 0}} & h_{1, 2} & h_{0, 2} & h_{2, 2} & h_{1, 1} & h_{0, 1} & h_{2, 1} \\
            \bf{h_{2, 0}} & \bf{h_{1, 0}} & \bf{h_{0, 0}} & h_{2, 2} & h_{1, 2} & h_{0, 2} & h_{2, 1} & h_{1, 1} & h_{0, 1} \\
            \bf{h_{0, 0}} & \bf{h_{2, 0}} & \bf{h_{1, 0}} & h_{0, 2} & h_{2, 2} & h_{1, 2} & h_{0, 1} & h_{2, 1} & h_{1, 1}
            \end{array}
            \end{bmatrix}
            \end{align}


        === "Latex"

            ```latex
            \begin{align}
            \begin{bmatrix}
            \begin{array}{c c c}
            h_{1, 1} & h_{0, 1} & h_{2, 1} \\
            h_{2, 1} & h_{1, 1} & h_{0, 1} \\
            h_{0, 1} & h_{2, 1} & h_{1, 1} \\
            \hline
            h_{1, 2} & h_{0, 2} & h_{2, 2} \\
            h_{2, 2} & h_{1, 2} & h_{0, 2} \\
            h_{0, 2} & h_{2, 2} & h_{1, 2} \\
            \hline
            \bf{h_{1, 0}} & \bf{h_{0, 0}} & \bf{h_{2, 0}} \\
            \bf{h_{2, 0}} & \bf{h_{1, 0}} & \bf{h_{0, 0}} \\
            \bf{h_{0, 0}} & \bf{h_{2, 0}} & \bf{h_{1, 0}}
            \end{array}
            \end{bmatrix}
            &\rightarrow \begin{bmatrix}
            \begin{array}{c c c | c c c}
            h_{1, 1} & h_{0, 1} & h_{2, 1} & \bf{h_{1, 0}} & \bf{h_{0, 0}} & \bf{h_{2, 0}} \\
            h_{2, 1} & h_{1, 1} & h_{0, 1} & \bf{h_{2, 0}} & \bf{h_{1, 0}} & \bf{h_{0, 0}} \\
            h_{0, 1} & h_{2, 1} & h_{1, 1} & \bf{h_{0, 0}} & \bf{h_{2, 0}} & \bf{h_{1, 0}} \\
            \hline
            h_{1, 2} & h_{0, 2} & h_{2, 2} & h_{1, 1} & h_{0, 1} & h_{2, 1} \\
            h_{2, 2} & h_{1, 2} & h_{0, 2} & h_{2, 1} & h_{1, 1} & h_{0, 1} \\
            h_{0, 2} & h_{2, 2} & h_{1, 2} & h_{0, 1} & h_{2, 1} & h_{1, 1} \\
            \hline
            \bf{h_{1, 0}} & \bf{h_{0, 0}} & \bf{h_{2, 0}} & h_{1, 2} & h_{0, 2} & h_{2, 2} \\
            \bf{h_{2, 0}} & \bf{h_{1, 0}} & \bf{h_{0, 0}} & h_{2, 2} & h_{1, 2} & h_{0, 2} \\
            \bf{h_{0, 0}} & \bf{h_{2, 0}} & \bf{h_{1, 0}} & h_{0, 2} & h_{2, 2} & h_{1, 2}
            \end{array}
            \end{bmatrix} \\
            &\rightarrow \begin{bmatrix}
            \begin{array}{c c c | c c c | c c c}
            h_{1, 1} & h_{0, 1} & h_{2, 1} & \bf{h_{1, 0}} & \bf{h_{0, 0}} & \bf{h_{2, 0}} & h_{1, 2} & h_{0, 2} & h_{2, 2} \\
            h_{2, 1} & h_{1, 1} & h_{0, 1} & \bf{h_{2, 0}} & \bf{h_{1, 0}} & \bf{h_{0, 0}} & h_{2, 2} & h_{1, 2} & h_{0, 2} \\
            h_{0, 1} & h_{2, 1} & h_{1, 1} & \bf{h_{0, 0}} & \bf{h_{2, 0}} & \bf{h_{1, 0}} & h_{0, 2} & h_{2, 2} & h_{1, 2} \\
            \hline
            h_{1, 2} & h_{0, 2} & h_{2, 2} & h_{1, 1} & h_{0, 1} & h_{2, 1} & \bf{h_{1, 0}} & \bf{h_{0, 0}} & \bf{h_{2, 0}} \\
            h_{2, 2} & h_{1, 2} & h_{0, 2} & h_{2, 1} & h_{1, 1} & h_{0, 1} & \bf{h_{2, 0}} & \bf{h_{1, 0}} & \bf{h_{0, 0}} \\
            h_{0, 2} & h_{2, 2} & h_{1, 2} & h_{0, 1} & h_{2, 1} & h_{1, 1} & \bf{h_{0, 0}} & \bf{h_{2, 0}} & \bf{h_{1, 0}} \\
            \hline
            \bf{h_{1, 0}} & \bf{h_{0, 0}} & \bf{h_{2, 0}} & h_{1, 2} & h_{0, 2} & h_{2, 2} & h_{1, 1} & h_{0, 1} & h_{2, 1} \\
            \bf{h_{2, 0}} & \bf{h_{1, 0}} & \bf{h_{0, 0}} & h_{2, 2} & h_{1, 2} & h_{0, 2} & h_{2, 1} & h_{1, 1} & h_{0, 1} \\
            \bf{h_{0, 0}} & \bf{h_{2, 0}} & \bf{h_{1, 0}} & h_{0, 2} & h_{2, 2} & h_{1, 2} & h_{0, 1} & h_{2, 1} & h_{1, 1}
            \end{array}
            \end{bmatrix}
            \end{align}
            ```

---