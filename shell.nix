{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python310
    pkgs.python310Packages.pip
    pkgs.python310Packages.discordpy
    pkgs.python310Packages.docker
    pkgs.git
    pkgs.openssh
  ];
}