{ pkgs ? import <nixpkgs> {} }:
(pkgs.buildFHSUserEnv {
  name = "pipzone";
  targetPkgs = pkgs: (with pkgs; [
    python310
    python310Packages.pip
    python310Packages.virtualenv
    python310Packages.discordpy
    git
    openssh
  ]);
  runScript = "./venv-activate.sh bash";
}).env
