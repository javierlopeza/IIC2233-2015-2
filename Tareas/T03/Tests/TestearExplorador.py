import unittest
from clases.vehiculos import AvionExplorador


class TestearAvionExplorador(unittest.TestCase):
    def setUp(self):
        self.avion = AvionExplorador()

    def test_paralizar(self):
        self.assertEqual(self.avion.turnos_paralizado, 0)
        self.avion.paralizar()
        self.assertEqual(self.avion.turnos_paralizado, 5)


suite = unittest.TestLoader().loadTestsFromTestCase(TestearAvionExplorador)
unittest.TextTestRunner().run(suite)