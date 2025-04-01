import unittest
from Modelo.producto import Producto
from Modelo.control_plagas import ControlPlagas

class TestProducto(unittest.TestCase):
    def test_crear_producto(self):
        producto = ControlPlagas("Plaga Y", 30, "ICA-67890", 15, 10)
        self.assertEqual(producto.nombre, "Plaga Y")
        self.assertEqual(producto.valor, 30)
        self.assertEqual(producto.periodo_carencia, 10)

if __name__ == '__main__':
    unittest.main()
