
{ system ? builtins.currentSystem } :

let pkgs = import <nixpkgs> { inherit system; };

in pkgs.python311Packages.buildPythonPackage {
	name = "eaglecore";
	version = "0.1";
	src = ./.;
	propagatedBuildInputs = with pkgs; [
		python311
        python311Packages.numpy
        python311Packages.scipy
        python311Packages.matplotlib
        # python310Packages.pandas
        # python310Packages.tqdm
	];
	doCheck = false;
}