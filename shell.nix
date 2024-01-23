{ pkgs ? import <nixpkgs> {}, ... }:

pkgs.mkShell {

    buildInputs = with pkgs; [

        python311

        # python311Packages.multimethod

        python311Packages.numpy
        python311Packages.scipy
        python311Packages.matplotlib
        python311Packages.pandas
        python311Packages.tqdm

        # Package for Jupyter / To comment
        python311Packages.ipywidgets
        python311Packages.ipykernel
        python311Packages.ipympl
        python311Packages.ipython
        
        # TO DELETE
        # python311Packages.scikitimage
        # python311Packages.scikit-learn

        python311Packages.mkdocs
        python311Packages.mkdocstrings
        python311Packages.mkdocstrings-python
        python311Packages.mkdocs-material
        python311Packages.mkdocs-jupyter
        python311Packages.pymdown-extensions
        # python311Packages.mkdocs-autorefs
        # python311Packages.mkdocs-redirects
        # python311Packages.mkdocs-swagger-ui-tag
        # python311Packages.mkdocs-material-extensions
        # python311Packages.mkdocs-minify
        python311Packages.mkdocs-mermaid2-plugin
        # python311Packages.mkdocs-exclude
        # python311Packages.mkdocs-simple-hooks
        # python311Packages.mkdocs-macros
        # python311Packages.mkdocs-drawio-exporter        

    ];

}
