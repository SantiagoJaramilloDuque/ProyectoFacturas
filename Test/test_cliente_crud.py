import unittest
from Crud import cliente_crud

class TestClienteCRUD(unittest.TestCase):

    def setUp(self):
        self.clientes = {}

    def test_crear_cliente(self):
        cliente = cliente_crud.crear_cliente(self.clientes, "Juan", "123")
        self.assertEqual(cliente.nombre, "Juan")
        self.assertIn("123", self.clientes)

    def test_eliminar_cliente_existente(self):
        cliente_crud.crear_cliente(self.clientes, "Juan", "123")
        resultado = cliente_crud.eliminar_cliente(self.clientes, "123")
        self.assertTrue(resultado)
        self.assertNotIn("123", self.clientes)

    def test_eliminar_cliente_inexistente(self):
        resultado = cliente_crud.eliminar_cliente(self.clientes, "999")
        self.assertFalse(resultado)

    def test_buscar_cliente_existente(self):
        cliente = cliente_crud.crear_cliente(self.clientes, "Juan", "123")
        encontrado = cliente_crud.buscar_cliente(self.clientes, "123")
        self.assertEqual(encontrado, cliente)

    def test_buscar_cliente_inexistente(self):
        encontrado = cliente_crud.buscar_cliente(self.clientes, "999")
        self.assertIsNone(encontrado)

    def test_listar_clientes(self):
        cliente_crud.crear_cliente(self.clientes, "Juan", "123")
        cliente_crud.crear_cliente(self.clientes, "Ana", "456")
        clientes = cliente_crud.listar_clientes(self.clientes)
        self.assertEqual(len(list(clientes)), 2)

if __name__ == '__main__':
    unittest.main()
