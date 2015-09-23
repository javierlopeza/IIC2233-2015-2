from ataque import Ataque


class Trident(Ataque):
    def __init__(self):
        super().__init__()
        self.nombre = 'Misil UGM-133 Trident II'
        self.damage = 5


class Tomahawk(Ataque):
    def __init__(self):
        super().__init__()
        self.nombre = 'Misil de crucrero BGM-109 Tomahawk'
        self.damage = 5
        self.disponibilidad = 3


class Napalm(Ataque):
    def __init__(self):
        super().__init__()
        self.nombre = 'Napalm'
        self.damage = 5
        self.disponibilidad = 8
        self.ataque_pendiente = False


class Minuteman(Ataque):
    def __init__(self):
        super().__init__()
        self.nombre = 'Misil Balistico Intercontinental Minuteman III'
        self.damage = 15
        self.disponibilidad = 3


class Kamikaze(Ataque):
    def __init__(self):
        super().__init__()
        self.nombre = 'Kamikaze'
        self.damage = float('infinity')


class Kit(Ataque):
    def __init__(self):
        super().__init__()
        self.nombre = 'Kit de Ingenieros'
        self.damage = -1
        self.disponibilidad = 2


class Paralizer(Ataque):
    def __init__(self):
        super().__init__()
        self.nombre = 'GBU-43/B Massive Ordnance Air Blast Paralizer'
