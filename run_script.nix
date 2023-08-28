{ pkgs ? import <nixpkgs> {}, path ? "", script ? "" }:

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
  runScript = "./script-activate.sh '" + path + "' '" + script + "'";
}).env
