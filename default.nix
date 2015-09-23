{ lib, pythonPackages, fetchurl }:

pythonPackages.buildPythonPackage rec {
  name = "morphis-${version}";
  version = "0.8";
  namePrefix = "";

  enableParallelBuilding = true;

  /*
  src = fetchurl {
    url = "https://morph.is/v${version}/morphis-${version}.tar.xz";
    sha256 = "0a6diff0lipd2lds4ix7syvdag134alfidw7g4infg9l6fx54dl9";
  };
  */

  src = ./morphis-0.8.fps.tar.gz;

  buildInputs = [ pythonPackages.pbr ];

  propagatedBuildInputs = with pythonPackages; [
      pycrypto
      sqlalchemy9
      cython
    ];

  meta = {
    homepage = http://morph.is;
    description = "A distributed datastore";
    maintainers = [ "Florian Paul Schmidt <mista.tapas@gmx.net>" ];
    platforms = lib.platforms.all;
  };

  /* all-packages.nix entry
  morphis = callPackage ../applications/networking/morphis {
    pythonPackages = python34Packages;
  };
  */
}

