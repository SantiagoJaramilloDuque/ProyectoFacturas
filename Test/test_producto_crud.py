import unittest
from Modelo.antibiotico import Antibiotico
from Modelo.control_fertilizantes import ControlFertilizantes
from Modelo.control_plagas import ControlPlagas
from Crud import producto_crud

class TestProductoCRUD(unittest.TestCase):

    def setUp(self):
        self.productos = [
            ControlFertilizantes("Fertilizante X", 50, "ICA-12345", 30, "2025-03-01"),
            ControlPlagas("Plaga Y", 30, "ICA-67890", 15, 10),
            Antibiotico("Antibiótico Z", 70, 500, "Bovinos")
        ]

    def test_listar_productos(self):
        productos = producto_crud.listar_productos(self.productos)
        self.assertEqual(len(productos), 3)
        self.assertEqual(productos[0].nombre, "Fertilizante X")

    def test_obtener_producto_valido(self):
        producto = producto_crud.obtener_producto_por_indice(self.productos, 0)
        self.assertEqual(producto.nombre, "Fertilizante X")

    def test_obtener_producto_invalido(self):
        producto = producto_crud.obtener_producto_por_indice(self.productos, 10)
        self.assertIsNone(producto)

if __name__ == '__main__':
    unittest.main()
