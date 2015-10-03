import unittest
from clases.vehiculo import Vehiculo


class TestearVehiculo(unittest.TestCase):
    def setUp(self):
        self.vehiculo = Vehiculo()

    def test_posicion_guia(self):
        self.vehiculo.casillas_usadas = [[1, 3], [2, 3]]
        self.assertEqual(self.vehiculo.posicion_guia, [1, 3])

    def test_setear_orientacion(self):
        self.vehiculo.size = [1, 3]
        self.vehiculo.setear_orientacion('h')
        self.assertEqual(self.vehiculo.orientacion, 'h')
        self.assertEqual(self.vehiculo.alto, 1)
        self.assertEqual(self.vehiculo.ancho, 3)

    def test_mostrar_ataque_disponibles(self):
        self.assertIsNone(self.vehiculo.mostrar_ataques_disponibles())

    def test_ptje_ataques_exitoso(self):
        self.assertEqual(self.vehiculo.ptje_ataques_exitosos, 'NO REALIZO ATAQUES')

    def test_damage_recibido(self):
        self.vehiculo.resistencia = 100
        self.vehiculo.vida = 100
        self.assertEqual(self.vehiculo.damage_recibido, 0)
        self.vehiculo.vida -= 10
        self.assertEqual(self.vehiculo.damage_recibido, 10)


suite = unittest.TestLoader().loadTestsFromTestCase(TestearVehiculo)
unittest.TextTestRunner().run(suite)
