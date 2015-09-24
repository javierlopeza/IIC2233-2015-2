class Ataque:
    def __init__(self):
        self.disponibilidad = 1
        self.turnos_pendientes = 0
        self.usadas = 0
        self.damage_efectivo = 0

    @property
    def disponible(self):
        if self.turnos_pendientes:
            return False
        return True

    def usar(self):
        self.turnos_pendientes = self.disponibilidad
