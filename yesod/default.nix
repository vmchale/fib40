{ mkDerivation, base, stdenv, text, yesod }:
mkDerivation {
  pname = "yesod-fib40";
  version = "0.1.0.0";
  src = ./.;
  isLibrary = false;
  isExecutable = true;
  executableHaskellDepends = [ base text yesod ];
  homepage = "https://github.com/vmchale/yesod#readme";
  license = stdenv.lib.licenses.bsd3;
}
