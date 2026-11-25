
class ProgramacionDinamica:

    def __init__(self, paquetes):
        self.paquetes = paquetes

    def resolver(self, n):

        dp = [float('inf')] * (n + 1)
        ultimo = [0] * (n + 1)

        dp[0] = 0

        for i in range(1, n + 1):

            for paquete in self.paquetes:

                p = paquete.obtener_viajes()

                if p <= i:

                    if dp[i - p] + 1 < dp[i]:

                        dp[i] = dp[i - p] + 1
                        ultimo[i] = p

        return dp, ultimo
