{ pkgs ? import <nixpkgs> {}, script ? "" }:

(pkgs.buildFHSUserEnv {
  name = "pipzone";
  targetPkgs = pkgs: (with pkgs; [
    python310
    python310Packages.pip
    python310Packages.virtualenv
    python310Packages.discordpy
  ]);
  runScript = "./venv-activate.sh '" + script + "'";
}).env
