import unittest
from clases.ataque import Ataque


class TestearAtaque(unittest.TestCase):
    def setUp(self):
        self.ataque = Ataque()

    def test_disponible(self):
        self.assertTrue(self.ataque.disponible)
        self.ataque.turnos_pendientes += 1
        self.assertFalse(self.ataque.disponible)

    def test_usar(self):
        self.ataque.usar()
        self.assertEqual(self.ataque.turnos_pendientes, self.ataque.disponibilidad)


suite = unittest.TestLoader().loadTestsFromTestCase(TestearAtaque)
unittest.TextTestRunner().run(suite)
