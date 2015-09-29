from main import Corrector
import unittest


class TesterCorrector(unittest.TestCase):
    def setUp(self):
        self.corrector1 = Corrector('5435466-5_lucas_hidalgo.txt')
        self.corrector2 = Corrector('6968271-5_Andrea_valdes.ttxtt')
        self.corrector3 = Corrector('18936676-0_antonio_lopez.txt')
        self.corrector4 = Corrector('18936677-k_rodrigo_lave.txt')

    def tearDown(self):
        # Deshago cualquier cambio hecho a los trabajos.
        cont1 = self.corrector1.contenido
        arch1 = open("Trabajos/" + self.corrector1.nombre, "w")
        for linea in cont1:
            arch1.write(linea + '\n')

        cont2 = self.corrector2.contenido
        arch2 = open("Trabajos/" + self.corrector2.nombre, "w")
        for linea in cont2:
            arch2.write(linea + '\n')

        cont3 = self.corrector3.contenido
        arch3 = open("Trabajos/" + self.corrector3.nombre, "w")
        for linea in cont3:
            arch3.write(linea + '\n')

        cont4 = self.corrector4.contenido
        arch4 = open("Trabajos/" + self.corrector4.nombre, "w")
        for linea in cont4:
            arch4.write(linea + '\n')

    def test_revisar_nombre(self):
        self.assertTrue(self.corrector1.revisar_nombre() is not False)
        self.assertTrue(self.corrector2.revisar_nombre() is not False)
        self.assertTrue(self.corrector3.revisar_nombre() is not False)
        self.assertTrue(self.corrector4.revisar_nombre() is not False)

    def test_revisar_formato(self):
        self.assertTrue(self.corrector1.revisar_formato(self.corrector1.nombre.split('.')[-1]))
        self.assertFalse(self.corrector2.revisar_formato(self.corrector2.nombre.split('.')[-1]))
        self.assertTrue(self.corrector3.revisar_formato(self.corrector3.nombre.split('.')[-1]))
        self.assertTrue(self.corrector4.revisar_formato(self.corrector4.nombre.split('.')[-1]))

    def test_revisar_verificador(self):
        self.assertTrue(self.corrector1.revisar_verificador(self.corrector1.nombre.split('_')[0]))
        self.assertTrue(self.corrector2.revisar_verificador(self.corrector2.nombre.split('_')[0]))
        self.assertTrue(self.corrector3.revisar_verificador(self.corrector3.nombre.split('_')[0]))
        self.assertFalse(self.corrector4.revisar_verificador(self.corrector4.nombre.split('_')[0]))

    def test_revisar_orden(self):
        self.assertTrue(self.corrector1.revisar_verificador(self.corrector1.nombre))
        self.assertTrue(self.corrector2.revisar_verificador(self.corrector2.nombre))
        self.assertTrue(self.corrector3.revisar_verificador(self.corrector3.nombre))
        self.assertTrue(self.corrector4.revisar_verificador(self.corrector4.nombre))

    def test_get_palabras(self):
        self.assertTrue(self.corrector1.get_palabras() == 24)
        self.assertTrue(self.corrector2.get_palabras() == 24)
        self.assertFalse(self.corrector3.get_palabras() < 500)
        self.assertTrue(self.corrector4.get_palabras() < 500)

    def test_get_descuento(self):
        self.assertTrue(self.corrector1.get_descuento() == 1)
        self.assertTrue(self.corrector2.get_descuento() == 1.5)  # Supuse que los descuentos se suman.
        self.assertTrue(self.corrector3.get_descuento() == 1)
        self.assertTrue(self.corrector4.get_descuento() == 1)

    def test_descontar(self):
        self.corrector1.descontar()
        self.assertTrue(self.corrector1.descuento == 1)
        self.corrector2.descontar()
        self.assertTrue(self.corrector2.descuento == 1.5)  # Supuse que los descuentos se suman.
        self.corrector3.descontar()
        self.assertTrue(self.corrector3.descuento == 1)
        self.corrector4.descontar()
        self.assertTrue(self.corrector4.descuento == 1)


suite = unittest.TestLoader().loadTestsFromTestCase(TesterCorrector)
unittest.TextTestRunner().run(suite)
