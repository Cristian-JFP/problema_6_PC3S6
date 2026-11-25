
class Reconstruccion:

    def __init__(self, ultimo):
        self.ultimo = ultimo

    def obtener_paquetes(self, n):

        resultado = []

        while n > 0:

            paquete = self.ultimo[n]

            resultado.append(paquete)

            n = n - paquete

        return resultado
