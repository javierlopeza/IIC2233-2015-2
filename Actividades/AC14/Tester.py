__author__ = 'Javier'

import pytest
from main import Ramo, Base, Alumno


class TestSistema:
    def setup_method(self, method):
        self.base = Base()
        for a in range(40):
            alumno = Alumno(base=self.base, creditos=0, nombre=str(a))
            alumno.tomar_ramo('IIC1134')
        self.alumno1 = Alumno(base=self.base, creditos=0, nombre='Javier')
        self.alumno2 = Alumno(base=self.base, creditos=50, nombre='Ignacio')

    def test_tomar_maxcreditos_bien(self):
        self.alumno1.tomar_ramo('MAT1630')
        assert self.alumno1.creditos_actuales < 50

    def test_tomar_maxcreditos_mal(self):
        self.alumno2.tomar_ramo('MAT1630')
        assert not self.alumno2.creditos_actuales > 50

    def test_tomar_maxvacantes_bien(self):
        self.alumno1.tomar_ramo('MAT1630')
        assert 'MAT1630' in self.alumno1.ramos

    def test_tomar_maxvacantes_mal(self):
        self.alumno2.tomar_ramo('IIC1134')
        assert 'IIC2233' not in self.alumno2.ramos

    def test_tomar_repetidos(self):
        self.alumno1.tomar_ramo('MAT1630')
        self.alumno1.tomar_ramo('MAT1630')
        assert len(self.alumno1.ramos) == len(set(self.alumno1.ramos))

    def test_botar_cred(self):
        self.alumno1.tomar_ramo('MAT1630')
        alumno1_cred = self.alumno1.creditos_actuales
        assert self.alumno1.botar_ramo('MAT1630')
        assert alumno1_cred - 10 == self.alumno1.creditos_actuales

        alumno2_cred = self.alumno2.creditos_actuales
        assert not self.alumno2.botar_ramo('MAT1630')
        assert alumno2_cred == self.alumno2.creditos_actuales

    def test_botar_vac(self):
        self.alumno1.tomar_ramo('IIC1237')
        vacantes_prev = self.base.db[0].vacantes
        self.alumno1.botar_ramo('IIC1237')
        vacantes_new = self.base.db[0].vacantes
        assert vacantes_new == vacantes_prev + 1

        vacantes_prev = self.base.db[1].vacantes
        assert not self.alumno1.botar_ramo('IIC2030')
        assert self.base.db[1].vacantes == vacantes_prev