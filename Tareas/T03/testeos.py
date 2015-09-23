import unittest
from mapa import Mapa
from vehiculo import Vehiculo
from ataque import Ataque


class TestearMapa(unittest.TestCase):
    def setUp(self):
        self.stats = Mapa(10)

    def test_armar_mapa(self):
        self.assertEqual(self.stats.armar_mapa(15), None)

    def test_mover_vehiculo(self):
        with self.assertRaises(TypeError):
            self.stats.mover_vehiculo(1)

    def test_agregar_vehiculo(self):
        with self.assertRaises(TypeError):
            self.stats.agregar_vehiculo(1)

    def test_eliminar_vehiculo(self):
        with self.assertRaises(TypeError):
            self.stats.agregar_vehiculo(1)


class TestearVehiculo(unittest.TestCase):
    def setUp(self):
        self.stats = Vehiculo()

    def test_posicion_guia(self):
        with self.assertRaises(Exception):
            self.stats.posicion_guia()
        self.stats.casillas_usadas = [[1, 3], [2, 3]]
        self.assertEqual(self.stats.posicion_guia, [1, 3])

    def test_setear_orientacion(self):
        self.stats.size = [1,3]
        self.stats.setear_orientacion()
        self.assertEqual(self.stats.orientacion, 'h')
        self.assertEqual(self.stats.alto, 1)
        self.assertEqual(self.stats.ancho, 3)


suite = unittest.TestLoader().loadTestsFromTestCase(TestearMapa)
unittest.TextTestRunner().run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(TestearVehiculo)
unittest.TextTestRunner().run(suite)
