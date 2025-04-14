import unittest
from Modelo.control_fertilizantes import ControlFertilizantes

class TestControlFertilizantes(unittest.TestCase):

    def setUp(self):
        self.fertilizante = ControlFertilizantes("Fertilizante Y", 75, "ICA-456", 30, "2024-04-20")

    def test_fechaUltimaAplicacion(self):
        self.assertEqual(self.fertilizante.fechaUltimaAplicacion, "2024-04-20")

    def test_set_fechaUltimaAplicacion(self):
        self.fertilizante.fechaUltimaAplicacion = "2024-05-20"
        self.assertEqual(self.fertilizante.fechaUltimaAplicacion, "2024-05-20")

if __name__ == '__main__':
    unittest.main()