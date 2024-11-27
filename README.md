# Diagrama de Clases: Pruebas de `calcularPrecioFinal`

```mermaid
classDiagram
    class calcularPrecioFinal {
        +float calcularPrecioFinal(float precio_base, float descuento, float impuesto)
    }

    class unittest.TestCase

    class TestCalcularPrecioFinal {
        +test_precio_normal()
        +test_sin_descuento()
        +test_sin_impuesto()
        +test_valores_limite()
        +test_valores_invalidos()
    }

    unittest.TestCase <|-- TestCalcularPrecioFinal
    TestCalcularPrecioFinal --> calcularPrecioFinal : testea
