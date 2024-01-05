{ pkgs ? import <nixpkgs> {}, ... }:

pkgs.mkShell {

    buildInputs = with pkgs; [

        python310

        # python310Packages.multimethod

        python310Packages.numpy
        python310Packages.scipy
        python310Packages.matplotlib
        python310Packages.pandas
        python310Packages.tqdm

        # Package for Jupyter / To comment
        python310Packages.ipywidgets
        python310Packages.ipykernel
        python310Packages.ipympl
        python310Packages.ipython
        
        # TO DELETE
        # python310Packages.scikitimage
        # python310Packages.scikit-learn

        python310Packages.mkdocs
        python310Packages.mkdocstrings
        python310Packages.mkdocstrings-python
        python310Packages.mkdocs-material
        python310Packages.mkdocs-jupyter
        python310Packages.pymdown-extensions
        # python310Packages.mkdocs-autorefs
        # python310Packages.mkdocs-redirects
        # python310Packages.mkdocs-swagger-ui-tag
        # python310Packages.mkdocs-material-extensions
        # python310Packages.mkdocs-minify
        python310Packages.mkdocs-mermaid2-plugin
        # python310Packages.mkdocs-exclude
        # python310Packages.mkdocs-simple-hooks
        # python310Packages.mkdocs-macros
        # python310Packages.mkdocs-drawio-exporter        

    ];

}
