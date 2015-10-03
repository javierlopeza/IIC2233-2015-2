import unittest
from clases.partida import Partida


class TestearPartida(unittest.TestCase):
    def setUp(self):
        self.partida = Partida()

    def test_estadisticas(self):
        self.assertIsNone(self.partida.estadisticas())

    def test_jugadores(self):
        self.assertIsNone(self.partida.jugadores)

    def test_cargado(self):
        self.assertFalse(self.partida.cargado)


suite = unittest.TestLoader().loadTestsFromTestCase(TestearPartida)
unittest.TextTestRunner().run(suite)
