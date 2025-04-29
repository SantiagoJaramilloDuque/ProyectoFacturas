import unittest
from Modelo.cliente import Cliente
from Modelo.factura import Factura
from Crud import factura_crud

class TestFacturaCRUD(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente("Pedro", "789")
        self.factura = factura_crud.crear_factura(self.cliente)

    def test_crear_factura(self):
        self.assertIsInstance(self.factura, Factura)
        self.assertEqual(self.factura.cliente, self.cliente)

    def test_agregar_producto_a_factura(self):
        producto = type("ProductoMock", (object,), {"nombre": "Producto X", "valor": 100})()
        factura_crud.agregar_producto_a_factura(self.factura, producto)
        self.assertIn(producto, self.factura.productos)

    def test_mostrar_factura(self):
        producto = type("ProductoMock", (object,), {"nombre": "Producto X", "valor": 100})()
        factura_crud.agregar_producto_a_factura(self.factura, producto)

        try:
            factura_crud.mostrar_factura(self.factura)
        except Exception as e:
            self.fail(f"mostrar_factura lanzó una excepción: {e}")

if __name__ == '__main__':
    unittest.main()
