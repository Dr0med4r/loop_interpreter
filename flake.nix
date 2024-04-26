{
  description = "Nix flake for loop_interpreter";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {
        inherit system;
      };
    in {
      packages.loop_interpreter = pkgs.callPackage ./derivation.nix {};
      packages.default = self.packages.${system}.loop_interpreter;
      devShells.default = let
        pythonPackages = with pkgs.python3Packages; [setuptools];
      in
        pkgs.mkShell
        {
          nativeBuildInputs = with pkgs;
            [
              python3
            ]
            ++ pythonPackages;
        };
    });
}
