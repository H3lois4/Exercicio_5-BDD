"""Liga todos os cenários dos arquivos .feature aos passos definidos em conftest.py."""
from pytest_bdd import scenarios

scenarios("../../features")
