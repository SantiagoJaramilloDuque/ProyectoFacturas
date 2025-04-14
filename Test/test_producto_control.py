import unittest
from Modelo.producto_control import ProductoControl

class TestProductoControl(unittest.TestCase):

    def setUp(self):
        self.producto = ProductoControl("Producto A", 50, "ICA-123", 10)

    def test_nombre(self):
        self.assertEqual(self.producto.nombre, "Producto A")

    def test_valor(self):
        self.assertEqual(self.producto.valor, 50)

    def test_registroICA(self):
        self.assertEqual(self.producto.registroICA, "ICA-123")

    def test_frecuenciaAplicacion(self):
        self.assertEqual(self.producto.frecuenciaAplicacion, 10)

    def test_set_nombre_valido(self):
        self.producto.nombre = "Producto B"
        self.assertEqual(self.producto.nombre, "Producto B")

    def test_set_nombre_invalido(self):
        with self.assertRaises(ValueError):
            self.producto.nombre = 123

    def test_set_valor_invalido(self):
        with self.assertRaises(ValueError):
            self.producto.valor = -10

if __name__ == '__main__':
    unittest.main()