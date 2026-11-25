
class Greedy:

    def __init__(self, paquetes):
        self.paquetes = paquetes

    def resolver(self, n):

        paquetes_ordenados = sorted(
            self.paquetes,
            key=lambda paquete: paquete.obtener_viajes(),
            reverse=True
        )

        resultado = []

        while n > 0:

            for paquete in paquetes_ordenados:

                p = paquete.obtener_viajes()

                if p <= n:

                    resultado.append(p)
                    n = n - p
                    break

        return resultado
