import unittest
from Modelo.antibiotico import Antibiotico

class TestAntibiotico(unittest.TestCase):

    def setUp(self):
        self.antibiotico = Antibiotico("Amoxicilina", 100, 500, "Bovinos")

    def test_nombre(self):
        self.assertEqual(self.antibiotico.nombre, "Amoxicilina")

    def test_valor(self):
        self.assertEqual(self.antibiotico.valor, 100)

    def test_dosis(self):
        self.assertEqual(self.antibiotico.dosis, 500)

    def test_tipoAnimal(self):
        self.assertEqual(self.antibiotico.tipoAnimal, "Bovinos")

    def test_set_nombre_valido(self):
        self.antibiotico.nombre = "Penicilina"
        self.assertEqual(self.antibiotico.nombre, "Penicilina")

    def test_set_nombre_invalido(self):
        with self.assertRaises(ValueError):
            self.antibiotico.nombre = 123

    def test_set_valor_invalido(self):
        with self.assertRaises(ValueError):
            self.antibiotico.valor = -10

    def test_set_dosis_invalida(self):
        with self.assertRaises(ValueError):
            self.antibiotico.dosis = -50

if __name__ == '__main__':
    unittest.main()