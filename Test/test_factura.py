import unittest
from Modelo.factura import Factura
from Modelo.cliente import Cliente
from Modelo.antibiotico import Antibiotico

class TestFactura(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente("Ana García", "123456789")
        self.factura = Factura(self.cliente)
        self.producto = Antibiotico("Amoxicilina", 100, 500, "Bovinos")

    def test_agregar_producto(self):
        self.factura.agregarProducto(self.producto)
        self.assertIn(self.producto, self.factura.productos)
        self.assertEqual(self.factura.valorTotal, 100)

if __name__ == '__main__':
    unittest.main()