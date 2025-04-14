import unittest
from Modelo.control_plagas import ControlPlagas

class TestControlPlagas(unittest.TestCase):

    def setUp(self):
        self.plaguicida = ControlPlagas("Insecticida X", 50, "ICA-123", 15, 7)

    def test_periodoCarencia(self):
        self.assertEqual(self.plaguicida.periodoCarencia, 7)

    def test_set_periodoCarencia(self):
        self.plaguicida.periodoCarencia = 10
        self.assertEqual(self.plaguicida.periodoCarencia, 10)

if __name__ == '__main__':
    unittest.main()