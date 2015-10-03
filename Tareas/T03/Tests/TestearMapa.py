import unittest
from clases.mapa import Mapa


class TestearMapa(unittest.TestCase):
    def setUp(self):
        self.mapa = Mapa(10)

    def test_armar_mapa(self):
        self.assertEqual(len(self.mapa.sector['aereo']), 10)
        self.assertEqual(len(self.mapa.sector['maritimo']), 10)

    def test_mover_vehiculo(self):
        self.assertEqual(self.mapa.mover_vehiculo('string'), None)

    def test_agregar_vehiculo(self):
        self.assertEqual(self.mapa.agregar_vehiculo('string'), None)

    def test_eliminar_vehiculo(self):
        self.assertEqual(self.mapa.eliminar_vehiculo('string', 'tierra'), None)

suite = unittest.TestLoader().loadTestsFromTestCase(TestearMapa)
unittest.TextTestRunner().run(suite)
