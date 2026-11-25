
from base_datos import BaseDatos
from programacion_dinamica import ProgramacionDinamica
from greedy import Greedy
from reconstruccion import Reconstruccion


def main():

    bd = BaseDatos()

    paquetes = bd.obtener_paquetes()

    dinamica = ProgramacionDinamica(paquetes)
    greedy = Greedy(paquetes)

    dp, ultimo = dinamica.resolver(10)

    reconstruccion = Reconstruccion(ultimo)

    print("\nPAQUETES DISPONIBLES")

    for paquete in paquetes:
        print(paquete.obtener_viajes(), "viajes")

    print("\nTABLA DE PROGRAMACION DINAMICA")
    print("Viajes | Minimo de paquetes")

    for i in range(11):
        print(i, "     |", dp[i])

    print("\nRECONSTRUCCION DE PAQUETES")

    for n in [6, 10]:

        resultado = reconstruccion.obtener_paquetes(n)

        combinacion = " + ".join(map(str, resultado))

        print("\nViajes solicitados:", n)
        print("Paquetes:", resultado)
        print("Cantidad minima:", dp[n])

        bd.guardar_resultado(
            "Programacion Dinamica",
            n,
            dp[n],
            combinacion
        )

    print("\nRESULTADOS GREEDY")

    for n in [6, 10]:

        resultado = greedy.resolver(n)

        combinacion = " + ".join(map(str, resultado))

        print("\nViajes solicitados:", n)
        print("Paquetes:", resultado)
        print("Cantidad de paquetes:", len(resultado))

        bd.guardar_resultado(
            "Greedy",
            n,
            len(resultado),
            combinacion
        )

    print("\nRESULTADOS GUARDADOS EN LA BASE DE DATOS")

    bd.mostrar_resultados()

    bd.cerrar()


if __name__ == "__main__":
    main()
