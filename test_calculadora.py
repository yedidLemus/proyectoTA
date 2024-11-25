import pytest
from calculadora import suma, resta, dividir, multiplicar, es_par

# 1. Prueba para la función suma
def test_suma():
    assert suma(3, 2) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0

# 2. Prueba para la función resta
def test_resta():
    assert resta(5, 3) == 2
    assert resta(0, 5) == -5
    assert resta(10, 10) == 0

# 3. Prueba para la función dividir
def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(9, 3) == 3
    with pytest.raises(ValueError):  # Prueba para división entre cero
        dividir(10, 0)

# 4. Prueba para la función multiplicar
def test_multiplicar():
    assert multiplicar(4, 5) == 20
    assert multiplicar(0, 10) == 0
    assert multiplicar(-2, 3) == -6

# 5. Prueba para la función es_par
def test_es_par():
    assert es_par(4) is True
    assert es_par(5) is False
    assert es_par(0) is True
