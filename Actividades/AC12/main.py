class Bummer:
    def __init__(self):
        self.alumnos = {"Vicente Besa": Alumno("vabesa", 12345),
                        "Juan Pablo Schele": Alumno("jpschele", 54321),
                        "Ariel Seisdedos": Alumno("robocop6", 123456789)}

        self.ramos = [Ramo("IIC2133", 10), Ramo("ING2030", 100),
                      Ramo("ICH1104", 100), Ramo("IIC2143", 30),
                      Ramo("IIC2413", 30)]

        self.conectado = False

    def ingresar(self, usuario, clave):
        if not self.conectado:
            try:
                if self.alumnos[usuario].clave == clave:
                    self.usuario_actual = self.alumnos[usuario]
                    self.conectado = True
                    print("se conecto {0}".format(self.usuario_actual.usuario))

            except KeyError:
                print('KeyError: El usuario "{0}" no se '
                      'encuentra en la lista de alumnos.'
                      ' Para ingresar al sistema el alumno '
                      'debe estar en la lista de alumnos.'
                      .format(usuario))
                print('No se logro ingresar al sistema.')

    def inscribir_ramo(self, numero):
        if self.conectado:
            try:
                if numero >= len(self.ramos):
                    raise IndexError()

                ramo_inscribir = self.ramos[numero]
                if ramo_inscribir.vacantes > 0:
                    self.usuario_actual.agregar_ramos(ramo_inscribir)
                    print("Se inscribio el curso de sigla {0} a {1}".format(ramo_inscribir.sigla,
                                                                            self.usuario_actual.usuario))

            except IndexError:
                print('IndexError: el numero de ramo "{0}" '
                      'no es valido; debe ser menor a {1} y '
                      'mayor o igual a 0.'.
                      format(numero, len(self.ramos)))
                print('{0} no pudo inscribir el ramo.'.
                      format(self.usuario_actual.usuario))

            except TypeError:
                print('TypeError: "{0}" no corresponde a un numero (int). '
                      'Se debe ingresar el numero (int) de ramo.'.
                      format(numero))
                print('{} no pudo inscribir el ramo.'.
                      format(self.usuario_actual.usuario))

    def quitar_ramo(self, numero):
        if self.conectado:
            try:
                ramo_quitar = self.ramos[numero]
                self.usuario_actual.quitar_ramos(ramo_quitar.sigla)
                print("Se quito el curso de sigla {0} de la carga academica de {1}".format(ramo_quitar.sigla,
                                                                                           self.usuario_actual.usuario))

            except TypeError:
                print('TypeError: el numero del ramo "{0}" que se '
                      'quiere quitar no es un entero. '
                      'Se debe ingresar el numero (int) del ramo a quitar.'.
                      format(numero))
                print('{} no pudo quitar el ramo.'.format(self.usuario_actual.usuario))

            except KeyError:
                print('KeyError: el alumno {0} no tiene el ramo "{1}". '
                      'Para borrar un ramo debe tenerlo.'.
                      format(self.usuario_actual.usuario, ramo_quitar.sigla))
                print('{0} no pudo borrar el ramo "{1}".'.
                      format(self.usuario_actual.usuario, ramo_quitar.sigla))

            except IndexError:
                print('IndexError: el numero de ramo "{0}" que se quiere botar no es valido. '
                      'El numero debe ser mayor o igual que 0 y menor que {1}.'.
                      format(numero, len(self.ramos)))
                print('{} no pudo botar el ramo.'.format(self.usuario_actual.usuario))

    def calificar(self, numero, nota):
        if self.conectado:
            try:
                ramo = self.ramos[numero]
                self.usuario_actual.calificar_curso(ramo.sigla, nota)
                print(
                    "Se califico a {0} en el curso {1} con la nota {2}".format(self.usuario_actual.usuario, ramo.sigla,
                                                                               nota))
            except ValueError:
                print('ValueError: la nota ingresada "{0}" no es valida. '
                      'Debe ingresar la nota como int o float.'.format(nota))
                print('{0} no pudo calificar el ramo {1}.'.format(self.usuario_actual.usuario, ramo.sigla))

            except KeyError:
                print('KeyError: el alumno {0} no tiene el ramo "{1}". '
                      'Debe tener el ramo para calificarlo.'.format(self.usuario_actual.usuario, ramo.sigla))
                print('El alumno {0} no pudo calificar el ramo {1}.'.format(self.usuario_actual.usuario, ramo.sigla))

            except IndexError:
                print('IndexError: el numero ingresado "{0}" no corresponde a '
                      'ningun ramo en la lista de ramos. '
                      'El numero debe ser mayor o igual que 0 y menor que {1}.'.
                      format(numero, len(self.ramos)))
                print('El alumno {0} no pudo calificar el ramo.'.format(self.usuario_actual.usuario))


"""

No se puede modificar desde aquí

"""


class Ramo:
    def __init__(self, sigla, vacantes):
        self.sigla = sigla
        self.vacantes = vacantes
        self.alumnos = {}

    def inscrito(self, alumno):
        self.vacantes -= 1
        self.alumnos[alumno.usuario] = alumno


class Alumno:
    def __init__(self, usuario, clave):
        self.usuario = usuario
        self.clave = clave
        self.ramos = {}
        self.ramos_aprobados = {}

    def agregar_ramos(self, ramo):
        self.ramos[ramo.sigla] = ramo
        ramo.inscrito(self)

    def quitar_ramos(self, sigla):
        del self.ramos[sigla]

    def calificar_curso(self, sigla, nota):
        ramo = self.ramos[sigla]
        nota = float(nota)
        self.ramos_aprobados[sigla] = (ramo, nota)


if __name__ == '__main__':
    bummer = Bummer()
    bummer.ingresar("Marco Bucchi", 12345)
    bummer.ingresar("Juan Pablo Schele", 54321)
    bummer.inscribir_ramo(5)
    bummer.inscribir_ramo(0)
    bummer.inscribir_ramo("IIC2111")
    bummer.inscribir_ramo(2)
    bummer.quitar_ramo(0)
    bummer.quitar_ramo("Investigación")
    bummer.quitar_ramo(4)
    bummer.quitar_ramo(5)
    bummer.calificar(2, "siete")
    bummer.calificar(0, "7.0")
    bummer.calificar(2, "7.0")
    bummer.calificar(5, "1.0")
