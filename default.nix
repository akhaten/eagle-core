
{ pkgs ? import <nixpkgs> {} }:

pkgs.python311Packages.buildPythonPackage {
	name = "eaglecore";
	version = "0.1";
	src = ./.;
	propagatedBuildInputs = with pkgs; [
		python311
		python311Packages.numpy
		python311Packages.scipy
		python311Packages.matplotlib
	];
	doCheck = true;
}