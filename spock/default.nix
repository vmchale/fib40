{ mkDerivation, base, mtl, Spock, stdenv, text }:
mkDerivation {
  pname = "spock";
  version = "0.1.0.0";
  src = ./.;
  isLibrary = false;
  isExecutable = true;
  executableHaskellDepends = [ base mtl Spock text ];
  homepage = "https://github.com/vmchale/spock#readme";
  license = stdenv.lib.licenses.bsd3;
}
