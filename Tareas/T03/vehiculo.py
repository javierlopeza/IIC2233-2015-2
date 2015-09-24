class Vehiculo:
    def __init__(self):
        self.movimientos = 0
        self.movilidad = 1
        self.nombre = None
        self.size = None
        self.ataques = []
        self.tipo = ''
        self.simbolo = ''
        self.casillas_usadas = []
        self.orientacion = None
        self.ancho = 0
        self.alto = 0
        self.resistencia = None
        self.vida = None

    @property
    def posicion_guia(self):
        try:
            if not self.casillas_usadas:
                raise IndexError('Lista de casillas usadas esta vacia')

        except IndexError as err:
            print('Error: {}'.format(err))

        else:
            return self.casillas_usadas[0]

    def setear_orientacion(self, orientacion=None):
        try:
            if not self.size:
                raise AttributeError('No se ha instanciado el vehiculo en detalle')

            if self.orientacion:
                raise AttributeError('Ya esta seteada la orientacion, '
                                     'no se puede cambiar')
            if not orientacion:
                orientacion = input('Ingrese la orientacion (vertical u horizontal) '
                                    'que desea para el vehiculo {} [v/h]: '.
                                    format(self.nombre))

            if orientacion != 'h' and orientacion != 'v':
                raise TypeError('No es el tipo de argumentos que'
                                ' recibe como orientacion')

        except AttributeError as err:
            print('Error: {}'.format(err))
            self.setear_orientacion()

        else:
            self.orientacion = orientacion
            if self.orientacion == 'h':
                self.ancho = max(self.size)
                self.alto = min(self.size)
            elif self.orientacion == 'v':
                self.ancho = min(self.size)
                self.alto = max(self.size)

    def mostrar_ataques_disponibles(self):
        try:
            if not self.ataques:
                raise AttributeError('No se han cargado los ataques al vehiculo')

            ret = ''
            for ataque_disp in self.ataques_disponibles:
                ret += '  [{0}]: {1}\n'.format(
                    self.ataques_disponibles.index(ataque_disp),
                    ataque_disp.nombre)

            print(ret)

        except AttributeError as err:
            print('Error: {}'.format(err))

    @property
    def ataques_disponibles(self):
        ret = []
        for ataque in self.ataques:
            if ataque.disponible \
                    and ataque.nombre != 'GBU-43/B Massive ' \
                                         'Ordnance Air Blast ' \
                                         'Paralizer' \
                    and ataque.nombre != 'Kit de Ingenieros':
                ret.append(ataque)
        return ret

    @property
    def ptje_ataques_exitosos(self):
        n_ataques_veh = 0
        n_ataques_exitosos_veh = 0
        for ataque in self.ataques:
            n_ataques_veh += ataque.usadas
            n_ataques_exitosos_veh += ataque.exitos
        if n_ataques_veh != 0:
            p = round((n_ataques_exitosos_veh / n_ataques_veh) * 100, 2)
            ptje = '{}%'.format(p)
        else:
            ptje = 'NO REALIZO ATAQUES'
        return ptje

    @property
    def damage_recibido(self):
        if isinstance(self.resistencia, int) \
                and isinstance(self.vida, int):
            damage_rec = self.resistencia - self.vida
            return damage_rec