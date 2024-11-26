import unittest

# Función a probar
def calcularPrecioFinal(precio_base, descuento, impuesto):
    if precio_base < 0 or descuento < 0 or impuesto < 0:
        raise ValueError("Los valores no pueden ser negativos")
    precio_descuento = precio_base - (precio_base * descuento / 100)
    precio_final = precio_descuento + (precio_descuento * impuesto / 100)
    return round(precio_final, 2)

# Clase de pruebas
class TestCalcularPrecioFinal(unittest.TestCase):

    def test_precio_normal(self):
        """Caso estándar con valores comunes"""
        self.assertEqual(calcularPrecioFinal(100, 10, 15), 103.5)

    def test_sin_descuento(self):
        """Sin descuento aplicado"""
        self.assertEqual(calcularPrecioFinal(100, 0, 10), 110.0)

    def test_sin_impuesto(self):
        """Sin impuesto aplicado"""
        self.assertEqual(calcularPrecioFinal(100, 20, 0), 80.0)

    def test_valores_limite(self):
        """Valores extremos en descuentos e impuestos"""
        self.assertEqual(calcularPrecioFinal(1, 50, 50), 0.75)

    def test_valores_invalidos(self):
        """Verifica que los valores negativos generen un error"""
        with self.assertRaises(ValueError):
            calcularPrecioFinal(-100, 10, 15)

# Punto de entrada para correr las pruebas
if __name__ == "__main__":
    unittest.main()
