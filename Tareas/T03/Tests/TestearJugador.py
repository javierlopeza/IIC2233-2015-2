import unittest
from clases.jugador import Jugador


class TestearJugador(unittest.TestCase):
    def setUp(self):
        self.jugador = Jugador()

    def test_revisar_historial_radar(self):
        self.assertIsNone(self.jugador.revisar_historial_radar())

    def test_revisar_casillas_espiadas(self):
        self.assertIsNone(self.jugador.revisar_casillas_espiadas())

    def test_mostrar_flota_activa(self):
        self.assertIsNone(self.jugador.mostrar_flota_activa())

    def test_mostrar_flota_movible(self):
        self.assertIsNone(self.jugador.mostrar_flota_movible())

    def test_mostrar_flota_maritima_reparable(self):
        self.assertIsNone(self.jugador.mostrar_flota_maritima_reparable())

    def test_mostrar_flota_paralizadora(self):
        self.assertIsNone(self.jugador.mostrar_flota_paralizadora())

    def test_mover_vehiculo(self):
        self.assertIsNone(self.jugador.mover_vehiculo())

    def test_kit(self):
        self.assertIsNone(self.jugador.kit_ingenieros())

    def test_terminar_turno(self):
        self.assertEqual(self.jugador.turnos, 0)
        self.jugador.terminar_turno()
        self.assertEqual(self.jugador.turnos, 1)

    def test_damage_total(self):
        self.assertEqual(self.jugador.damage_total_recibido, 0)


suite = unittest.TestLoader().loadTestsFromTestCase(TestearJugador)
unittest.TextTestRunner().run(suite)
