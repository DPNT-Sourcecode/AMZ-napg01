{
  pkgs ? import <nixpkgs> { },
}:
with pkgs;
mkShell {
  nativeBuildInputs = [
    python3
    pyright
  ];
}
