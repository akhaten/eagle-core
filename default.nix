
{ system ? builtins.currentSystem } :

let pkgs = import <nixpkgs> { inherit system; };

in pkgs.python310Packages.buildPythonPackage {
	name = "eaglecore";
	version = "0.1";
	src = ./.;
	propagatedBuildInputs = with pkgs; [
		python310
        python310Packages.numpy
        python310Packages.scipy
        python310Packages.matplotlib
        # python310Packages.pandas
        # python310Packages.tqdm
	];
	doCheck = false;
}