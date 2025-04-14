import unittest
from Modelo.cliente import Cliente
from Modelo.factura import Factura

class TestCliente(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente("Ana García", "123456789")
        self.factura = Factura(self.cliente)

    def test_nombre(self):
        self.assertEqual(self.cliente.nombre, "Ana García")

    def test_cedula(self):
        self.assertEqual(self.cliente.cedula, "123456789")

    def test_agregar_factura(self):
        self.cliente.agregarFactura(self.factura)
        self.assertIn(self.factura, self.cliente.historialCompras)

    def test_set_nombre_valido(self):
        self.cliente.nombre = "Pedro"
        self.assertEqual(self.cliente.nombre, "Pedro")

    def test_set_nombre_invalido(self):
        with self.assertRaises(ValueError):
            self.cliente.nombre = 123
    
    def test_set_cedula_valido(self):
        self.cliente.cedula = "456789123"
        self.assertEqual(self.cliente.cedula, "456789123")
    
    def test_set_cedula_invalido(self):
        with self.assertRaises(ValueError):
            self.cliente.cedula = 123

if __name__ == '__main__':
    unittest.main()