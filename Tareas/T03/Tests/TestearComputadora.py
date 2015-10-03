import unittest
from clases.computadora import Computadora


class TestearComputadora(unittest.TestCase):
    def setUp(self):
        self.computadora = Computadora()

    def test_posicionar(self):
        self.assertIsNone(self.computadora.posicionar_vehiculos())

    def test_mover_espiado(self):
        self.assertFalse(self.computadora.mover_espiado())


suite = unittest.TestLoader().loadTestsFromTestCase(TestearComputadora)
unittest.TextTestRunner().run(suite)
