{python3Packages}:
with python3Packages;
  buildPythonApplication {
    pname = "loop_interpreter";
    version = "0.1";
    pyproject = true;

    src = ./.;

    nativeBuildInputs = [
      setuptools
      wheel
    ];
  }
