def calcularPrecioFinal(precio_base, descuento, impuesto):
    if precio_base < 0 or descuento < 0 or impuesto < 0:
        raise ValueError("Los valores no pueden ser negativos")
    precio_descuento = precio_base - (precio_base * descuento / 100)
    precio_final = precio_descuento + (precio_descuento * impuesto / 100)
    return round(precio_final, 2)
def test_precio_normal():
    assert calcularPrecioFinal(100, 10, 15) == 103.5
def test_sin_descuento():
    assert calcularPrecioFinal(100, 0, 10) == 110.0
def test_sin_impuesto():
    assert calcularPrecioFinal(100, 20, 0) == 80.0
def test_valores_limite():
    assert calcularPrecioFinal(1, 50, 50) == 0.75  # Aplicando descuentos e impuestos extremos
import pytest

def test_valores_invalidos():
    with pytest.raises(ValueError):
        calcularPrecioFinal(-100, 10, 15)
