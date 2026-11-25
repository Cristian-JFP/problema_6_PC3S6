
class Paquete:

    def __init__(self, id_paquete, viajes):
        self.id_paquete = id_paquete
        self.viajes = viajes

    def obtener_viajes(self):
        return self.viajes

    def obtener_id(self):
        return self.id_paquete
